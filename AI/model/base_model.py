# This folder will contain the base model before fine tunning process (These codes has been written in IEEE competition peroid!)
# Importing needing libraries
import json
import os
from os.path import join
import random
from tqdm.auto import tqdm
import requests

from pydantic import BaseModel, Field
from typing import List, Optional, Literal
from datetime import datetime


from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig
import torch

base_model_id = 'Qwen/Qwen2.5-1.5B-Instruct' # I choosed a little model, don't make well but with fine-tuining will perform will (- hope (: -
device = 'cuda'


#use case example
user_input = '''
User Info:
- Name: Isabella
- Age: 22
- Gender: male
- Height: 147 cm
- Weight: 67.9 kg 
- Lives in: India

This is a survery answers from the user:
Health Problems / Symptoms:
- Do you have difficulty sleeping?: true
  - How many hours do you sleep per night?: 6
  - Do you feel tired or have low focus during work?: true
- Do you sometimes feel dehydrated or have headaches?: true
  - How often does this happen per week?: 5
- Do you have any mental health problems?: true
    - Name some of them: Anxiety disorders, Attention deficit hyperactivity disorder (ADHD)

Lifestyle:
- Do you work at a desk job for long hours?: true
  - How many hours do you usually sit at your desk per day?: 8
- Do you exercise regularly?: false
- Do you drink coffee daily?: true
  - How many cups of coffee do you usually drink per day?: 3
  - Do you usually drink coffee late at night?: true

Additional Information:
I live with my family, so my meals are mostly home-cooked., I usually sleep late because of using my phone at night., I fast during Ramadan every year and adjust my eating schedule.
'''.strip()


# I will work in two models, one for a fully health analysis about the user's issues, other for generating the routine personalized for user-info and life style.
# That's will give us more flexibility and such a light model!

# Health Issue: Output Structure (JSON)
class HealthIssue(BaseModel):
    name: str
    cause: List[str] = Field(..., min_items=1, max_items=5,
        description="short possible causes of these issues generated specifically for the user's condition, talk with him like his doctor and be abbreviated!")
    severity: Optional[str] = None
    description: Optional[str] = Field(...,
           min_length=3, max_length=15,
          description="descripe for the user (talk with him like his doctor) why these issues may happend.")

class HI_StructuredOutput(BaseModel):
    health_issues: List[HealthIssue] = Field(..., min_items=1,
        description="List of health issues reported by the user and analyzed well according to user life sytel, health information.")


# Health Issue: Message to give roles for the system.
HI_message = [
    {
        "role": "system",
        "content": "\n".join([
            "You are an assistant that generates a fully health analysis about the user's issues.",
            "You must take the user's health information, lifestyle, and reported health issues, "
            "then return ONLY a valid JSON object strictly matching the Pydantic schema StructuredOutput.",
            "You must talk with the user as he listens to you, use words like (you, your...) and so on."
            "",
        ])
    },
    {
        "role": "user",
        "content": "/n".join([
            "## User Info:", user_input,
            "## Pydantic Scheme: ", json.dumps(HI_StructuredOutput.model_json_schema()),
            "## Issues Analysis with causeds for the user case: ",
            "```json"  
        ])
    }
    
]

#####- Routine-Builder Structure -#####
task_times = Literal["Morning", "Mid-Day", "Evening", "Night", "Any-Time"]
class Task(BaseModel):
    type: str
    title: str
    description: str
    points: int
    task_time: task_times = Field(...,
    description="The period of the day to perform the task, personalized for lifestyle")


class DayRoutine(BaseModel):
    day_number: int
    tasks: List[Task] = Field(..., min_items=3, max_items=7,
        description="Customized tasks (routine/nutrition) the user should follow for this day, for each day total tasks' points should be 100.")

class RB_StructuredOutput(BaseModel):
    weekly_plan: List[DayRoutine]

# Routine Builder: Message to give roles for the system.
RB_message = [
    {
        "role": "system",
        "content": "\n".join([
            "You are an assistant that generates a fully personalized health plan for each user.",
            "You must take the user's health information, lifestyle in count while generating the routine, "
            "then return ONLY a valid JSON object strictly matching the Pydantic schema StructuredOutput.",
            "",
        ])
    },
    {
        "role": "user",
        "content": "/n".join([
            "## User Info:", user_input,
            "## Pydantic Scheme: ", json.dumps(RB_StructuredOutput.model_json_schema()),
            "## Customized plan for the user case: ",
            "```json"  
        ])
    }
    
]




###### Model & Toknizer Downloading######
model = AutoModelForCausalLM.from_pretrained(
    base_model_id,
    device_map="auto",
    torch_dtype = None
)

tokenizer = AutoTokenizer.from_pretrained(base_model_id) # The Tokenizer

def call_model(message):
    input_text = tokenizer.apply_chat_template(message,
                                  tokenize=False,
                                  add_generation_prompt=True)
    model_inputs = tokenizer([input_text], return_tensors="pt").to(device)
    
    generated_ids = model.generate(model_inputs.input_ids,
                                   max_new_tokens=2000,
                                   do_sample=False, top_k=None, temperature=None, top_p=None, # Don't be creative (Greedy)
                                   )
    generated_ids = [generated_ids[0][len(model_inputs.input_ids[0]):]]
    text_output = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
    return text_output


call_model(HI_message)
call_model(RB_message)
# In the next stage fine tuining process: we will branch this model to two differ models for each case!

