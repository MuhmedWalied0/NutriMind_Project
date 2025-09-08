"""
In this file, I chose to synthesize the dataset myself due to the limited timeframe of the IEEE competition.
To achieve a higher level of generalization, I generated four different versions of the dataset:

1. Version 1: 1,000 rows focusing on the core concept of the project — Customization.
2. Version 2: 1,000 rows as well, but enriched with new scenarios and variations in user inputs to create a more generalized version.
3. Version 3: Divided into two parts:
   - 3.1: 500 rows featuring new names, countries, user lifestyles, and issues, while reducing the likelihood of severe illnesses to enhance diversity and generalization.
   - 3.2: Similar to 3.1, but additionally incorporating user instructions, where the user provides specific preferences that guide the model in generating a personalized routine.
"""

#------ Gemeni Versions Used -------#
from google import genai
models_names = ['gemini-2.5-flash-lite', 'gemini-2.5-pro', 'gemini-2.5-flash']

# A function to synthesize the data with more varations
def generate_inputs(n_samples, new_add_info = [], replace = False):
    list_of_inputs = []
    names = [
    # Arabic Male
    "Ahmed", "Mohamed", "Omar", "Youssef", "Karim", "Hassan", "Ibrahim", "Tamer", "Ali", "Samir",
    "Khaled", "Walid", "Mustafa", "Fadi", "Nader", "Rami", "Bilal", "Fouad", "Adel", "Majed", "Kareem",
    
    
    # Arabic Female
    "Fatima", "Layla", "Mona", "Nora", "Amira", "Huda", "Dina", "Rania", "Nada", "Laila",
    "Salma", "Aya", "Reem", "Yasmin", "Nadia", "Hanan", "Marwa", "Bushra", "Sara", "Farah",
    
    # International Male
    "John", "David", "Michael", "Daniel", "James", "Thomas", "Robert", "William", "Andrew", "Mark",
    
    # International Female
    "Sarah", "Emily", "Jessica", "Olivia", "Sophia", "Hannah", "Emma", "Chloe", "Isabella", "Grace"
    ]

    if not replace:
        additional_info = [
        "I sometimes take vitamins, especially Vitamin D during winter.",
        "I have mild seasonal allergies, mostly in spring due to pollen.",
        "I follow a vegetarian diet but occasionally eat fish.",
        "My stress level is usually around 5–6, especially during work deadlines.",
        "I don’t smoke or drink alcohol, and I try to avoid fast food.",
        "I fast during Ramadan every year and adjust my eating schedule.",
        "I am trying to lose weight by reducing carbs and sweets.",
        "I often skip breakfast due to a busy morning schedule.",
        "I usually sleep late because of using my phone at night.",
        "I drink energy drinks twice a week when I feel tired.",
        "I sometimes experience dizziness after long hours at the desk.",
        "I go for a walk on weekends, but I don’t exercise regularly.",
        "I try to drink more water, but I usually forget during work hours.",
        "I eat fast food about 2–3 times a week.",
        "I live with my family, so my meals are mostly home-cooked.",
        "I use herbal tea to help me sleep better at night.",
        "I spend long hours in front of the computer daily.",
        "I sometimes take painkillers for headaches.",
        "I usually drink 2–3 cups of tea instead of coffee.",
        "I try to follow a Mediterranean diet with fruits and vegetables.",
        "I often skip lunch during workdays and rely on snacks or coffee instead.",
        "I usually eat fast food 3–4 times a week because of my busy schedule.",
        "I follow a vegetarian diet but sometimes struggle with protein intake.",
        "I eat dinner late at night, usually after 10 PM, which affects my sleep.",
        "I walk around 6,000 steps a day but rarely do structured exercise.",
        "I spend most of my day on a computer screen and often get eye strain.",
        "I don’t exercise regularly, but I try to stretch for a few minutes daily.",
        "I go to the gym 4 times a week, focusing mostly on weight training.",
        "I feel constant pressure at work, which sometimes causes anxiety.",
        "I meditate for 10 minutes daily to help manage stress.",
        "My job requires frequent night shifts, which makes me feel drained and moody.",
        "My father has diabetes, so I try to limit sugar in my diet.",
        "I have mild seasonal allergies, especially in spring.",
        "I sometimes experience digestive problems after eating spicy food.",
        "I don’t smoke or drink alcohol, but I often consume energy drinks when tired.",
       "I often wake up with back pain after long hours at my desk.",
        "I sometimes feel short of breath when climbing stairs.",
        "I have frequent migraines, especially when I skip meals.",
        "I often feel bloated after eating heavy meals at night.",
        "I experience mild joint stiffness in the morning.",
        "I get heartburn if I drink coffee on an empty stomach.",
        "I sometimes feel dizzy when I stand up too quickly.",
        "I have occasional chest tightness when I’m stressed.",
        "I often struggle with dry eyes from screen time.",
        "I catch colds more frequently during the winter season.",
        "I have trouble focusing when I don’t sleep enough.",
        "I experience tingling in my hands after typing for long hours.",
        "I sometimes feel nausea after eating fast food.",
        "I often have low energy levels in the afternoon.",
        "I have mild lactose intolerance, especially after dairy products.",
        "I sometimes feel restless at night even when I’m tired.",
        "I experience skin dryness and itching in cold weather.",
        "I occasionally get muscle cramps in my legs at night.",
        "I feel fatigued after spending too much time in hot weather.",
        "I sometimes have ringing in my ears after loud events.",
        "I often skip lunch during workdays and rely on snacks or coffee instead.",
        "I usually eat fast food 3–4 times a week because of my busy schedule.",
        "I follow a vegetarian diet but sometimes struggle with protein intake.",
        "I eat dinner late at night, usually after 10 PM, which affects my sleep.",
        "I walk around 6,000 steps a day but rarely do structured exercise.",
        "I spend most of my day on a computer screen and often get eye strain.",
        "I don’t exercise regularly, but I try to stretch for a few minutes daily.",
        "I go to the gym 4 times a week, focusing mostly on weight training.",
        "I feel constant pressure at work, which sometimes causes anxiety.",
        "I meditate for 10 minutes daily to help manage stress.",
        "My job requires frequent night shifts, which makes me feel drained and moody.",
        "My father has diabetes, so I try to limit sugar in my diet.",
        "I have mild seasonal allergies, especially in spring.",
        "I sometimes experience digestive problems after eating spicy food.",
        "I don’t smoke or drink alcohol, but I often consume energy drinks when tired.",
            
        ]
        additional_info.extend(new_add_info)
    else:
        additional_info = new_add_info

    TF = ['true', 'false']
    genders = ['male', 'female']
    some_mental_problems = [
    "Anxiety disorders",
    "Depression",
    "Obsessive-compulsive disorder (OCD)",
    "Social anxiety disorder",
    "Phobias",
    "Eating disorders",
    "Attention deficit hyperactivity disorder (ADHD)",
    "Insomnia",
    "Stress-related disorders",
    ]
    countries = [
    # Arabic countries (10)
    "Egypt",
    "Saudi Arabia",
    "United Arab Emirates",
    "Qatar",
    "Kuwait",
    "Jordan",
    "Lebanon",
    "Morocco",
    "Algeria",
    "Oman",
    
    # Non-Arabic countries (5)
    "USA",
    "Germany",
    "Canada",
    "Turkey",
    "India"
    ]

    for i in range(n_samples):
        # semi - Healthy BMI Range [20 - 35]
        unhealthy_BMI = np.round(np.random.uniform(low=20.0, high=35.0, size=1,)[0], 1)
        random_height = np.random.randint(130, 180)
        additional_infos = ', '.join(np.random.choice(additional_info, 3, replace=False))
        user_input = f"""
        User Info:
        - Name: {np.random.choice(names)}
        - Age: {np.random.randint(18, 70)}
        - Gender: {np.random.choice(genders)}
        - Height: {random_height} cm
        - Weight: {np.round(unhealthy_BMI * pow(random_height/100, 2), 1)} kg 
        - Lives in: {np.random.choice(countries)}
        
        This is a survery answers from the user:
        Health Problems / Symptoms:
        - Do you have difficulty sleeping?: {np.random.choice(TF, p=[0.7, 0.3])}
          - How many hours do you sleep per night?: {np.random.randint(3,7)}
          - Do you feel tired or have low focus during work?: {np.random.choice(TF, p=[0.6, 0.4])}
        - Do you sometimes feel dehydrated or have headaches?: {np.random.choice(TF, p=[0.6, 0.4])}
        - Do you have any mental health problems?: true
            - Name some of them: {', '.join(np.random.choice(some_mental_problems, replace=False, size=1))}
        
        Lifestyle:
        - Do you work at a desk job for long hours?: {np.random.choice(TF, p=[0.6, 0.4])}
        - Do you exercise regularly?: {np.random.choice(TF, p=[0.4, 0.6])}
        - Do you drink coffee daily?: {np.random.choice(TF, p=[0.6, 0.4])}
          - How many cups of coffee do you usually drink per day?: {np.random.randint(0,2)}
        
        Additional Information:
        {additional_infos}
        
            """.strip()
        list_of_inputs.append(user_input)
    return list_of_inputs



# A function to generate me reasponses help me to fine tuine the model
def gemeni_gate(df, start_index, coloumn_name='HI_Target'):
    assert coloumn_name in df.columns 
    
    if coloumn_name == 'HI_Target':
        schema = HI_StructuredOutput
    else:
        schema = RB_StructuredOutput
    # elif:
    for i in range(start_index, 1500):
        if coloumn_name == 'HI_Target':
            contents_ = f"This is my info with my health issues{df.loc[i, 'user_inputs']}, give me a structured analysis about my issues in the following json structure"
        else:
            contents_ = contents=f"This is user info with his health issues{df.loc[i, 'user_inputs']}, give me a structured routine according to user's issues and info in the following json structure  "
            
            
        client = genai.Client(api_key='AIzaSyDz1GqqIoF83e1FcEqLvIgMORNhQQOA9NY')
        cur_model_name = np.random.choice(models_names, p=[0.9, 0.05, 0.05])
        response = client.models.generate_content(
            model=cur_model_name,
            contents = contents_,
            config={
                "response_mime_type": "application/json",
                "response_schema": schema,
            },
        )
    
        out_put = response.text
        
        df.loc[i, coloumn_name] = str(out_put)
        print(f'{i} Done! with {cur_model_name}')
        if i % 20 == 0:
            df.to_csv('/kaggle/working/all_in_one.csv')
    

## First data version (1000 rows) focusing on the main feature of our project (Customization)
new_info = [
    "I often feel stomach pain after eating late at night.",
    "I get frequent lower back pain from sitting long hours at my desk job.",
    "I usually eat bread and cheese for breakfast because it’s quick and easy.",
    "I try to walk for 20 minutes after dinner to help digestion.",
    "I often skip lunch when I’m busy at work, then overeat at dinner.",
    "I sometimes experience heartburn after eating spicy or fried foods.",
    "I drink 2–3 cups of coffee daily, usually in the morning.",
    "I fast during Ramadan every year, so my eating routine changes completely.",
    "I don’t smoke or drink alcohol, but I often eat fast food when I’m stressed.",
    "I usually sleep late because I spend time on my phone before bed.",
    "I try to drink at least 6 glasses of water daily but often forget during work.",
    "I feel knee pain when climbing stairs, especially after a long day.",
    "I use herbal tea in the evening to help me relax before sleeping.",
    "I often eat dinner with my family, so meals are mostly home-cooked.",
    "I sometimes feel bloated after eating too much bread or rice.",
    "I do not exercise regularly, but I walk to work when the weather is nice.",
    "I sometimes take Omega-3 supplements to support my concentration.",
    "I have mild dust allergies, especially when cleaning my room.",
    "I follow a mostly plant-based diet but eat chicken once in a while.",
    "My stress level is usually around 7 during exams or busy projects.",
    "I don’t smoke or drink alcohol, but I do eat fast food when I’m in a rush.",
    "I fast occasionally for health reasons, not only during Ramadan.",
    "I am currently trying to gain muscle by eating more protein-rich meals.",
    "I usually skip dinner when I work late at night.",
    "I often stay up late watching TV or scrolling on my phone.",
    "I drink coffee 3–4 times a day to stay awake.",
    "I sometimes feel lightheaded when I don’t drink enough water.",
    "I walk to work daily but don’t follow a strict exercise plan.",
    "I try to stay hydrated, but I often forget during hot weather.",
    "I eat fried snacks 2–3 times a week with my friends.",
    "I live alone, so I often cook quick meals instead of full dishes.",
    "I sometimes drink chamomile tea to reduce stress before sleeping."
]

new_list_of_inputs = generate_inputs(1000, new_info)
first_thousands_unhealthy_data = pd.DataFrame(new_list_of_inputs, columns=['user_inputs'])
first_thousands_unhealthy_data['HI_Target'] = ''
gemeni_gate(first_thousands_unhealthy_data, 0)
# first_thousands_unhealthy_data.to_csv('/kaggle/working/first_thousands_unhealthy_data.csv')

## Secoend version of the data, focusing more on the main feature of our project (Customization), With making the data more generalized by useing 
## Different usage scinarios
new_info = ["I often feel stomach cramps after eating oily food.",
    "I sometimes get sharp pain in my lower back after sitting for long hours.",
    "I experience chest discomfort when I’m very stressed.",
    "I occasionally have sharp headaches after working on the computer too long.",
    "I feel pain in my knees when climbing stairs.",
    "I sometimes wake up with neck stiffness and discomfort.",
    "I experience bloating and stomach pain after heavy dinners.",
    "I get mild chest tightness when I drink too much coffee.",
    "I occasionally feel pressure around my eyes after long screen time.",
    "I sometimes have abdominal pain when I skip meals.",
    "I experience shoulder pain after carrying heavy bags.",
    "I sometimes feel lower abdominal discomfort after fast food.",
    "I have mild wrist pain from using the keyboard for long hours.",
    "I sometimes feel burning pain in my stomach after spicy meals.",
    "I experience aching in my legs after standing too long.",
    "I get pain in my jaw when I clench my teeth at night.",
    "I occasionally feel sharp pain in my chest when I breathe deeply.",
    "I sometimes feel heaviness and discomfort in my stomach after late-night meals.",
    "I often get mild pain in my ankles when walking long distances.",
    "I occasionally experience stomach pain when I drink soft drinks too fast."]
new_list_of_inputs = generate_inputs(1000, new_info)
secoend_thousands_unhealthy_data = pd.DataFrame(new_list_of_inputs, columns=['user_inputs'])
secoend_thousands_unhealthy_data['HI_Target'] = ''
gemeni_gate(secoend_thousands_unhealthy_data, 0)
# secoend_thousands_unhealthy_data.to_csv('/kaggle/working/secoend_thousands_unhealthy_data.csv')


### Third version of the data, as a way for making the data more generalized, I decided to decrease the percentage of common diseases as possible,
##w ith adding some new life styles and train the model in the **instructions context**, adding new countries and names.

def special_generate_inputs(n_samples, new_add_info = [], replace = False):
    list_of_inputs = []
    names = [
    # Arabic Male
    "Yasin", "Ziad", "Kamal", "Jalal", "Hussein", "Malik", "Nabil", "Raafat", "Saeed", "Hamza",
    "Osama", "Faisal", "Salem", "Wassim", "Hisham", "Anwar", "Badr", "Jamil", "Khalil", "Maher",

    # Arabic Female
    "Joud", "Tasneem", "Rima", "Hala", "Maya", "Rana", "Amina", "Zahra", "Sana", "Dalia",
    "Elham", "Ghada", "Hind", "Inas", "Lina", "Mariam", "Nour", "Rasha", "Sahar", "Wafa",

    # International Male
    "Christopher", "Matthew", "Joshua", "Anthony", "Kevin", "Brian", "Steven", "Paul", "Eric", "Ryan",
    "Nicholas", "Jonathan", "Benjamin", "Samuel", "Nathan", "Timothy", "Richard", "Jeffrey", "Jacob", "Alexander",

    # International Female
    "Elizabeth", "Megan", "Rachel", "Lauren", "Amanda", "Jennifer", "Nicole", "Victoria", "Stephanie", "Rebecca",
    "Michelle", "Samantha", "Ashley", "Kimberly", "Alexis", "Tiffany", "Abigail", "Brianna", "Vanessa", "Melissa"
]

    if not replace:
        user_lifestyle_descriptions = [
                "I sit at my desk for almost 8 hours straight every day for work.",
                "I drink about 4 cups of coffee to get through my morning and afternoon.",
                "I go to bed at a different time every night, sometimes very late.",
                "I often have my biggest meal right before I go to sleep.",
                "I'm so busy that I frequently forget to eat lunch.",
                "Most of my meals are from packages or the drive-thru because they're fast.",
                "I spend at least an hour on my phone right before trying to sleep.",
                "I might only have one or two glasses of water all day.",
                "I can't remember the last time I went to the gym or did a workout.",
                "I feel stressed and overwhelmed by my job almost constantly.",
                "I slouch in my chair and often work with my laptop on the couch.",
                "When I'm tired, I grab a candy bar or chips for a quick boost.",
                "If I've had a hard day, I'll order a large pizza and eat it by myself.",
                "I've been saying no to friends a lot lately and just staying home.",
                "I leave for work before the sun is up and get home after it's dark.",
                "I type and use a mouse all day, and my hands never get a break.",
                "I get most of my steps in just walking around my house or office.",
                "My sleep schedule is completely different on the weekends.",
                "I always choose the elevator over the stairs.",
                "I eat while I'm working at my computer so I don't waste time.",
                "I absolutely love cheesy pasta and could eat it every single day, it's my ultimate comfort food.",
                "I have a major sweet tooth and always need something like cookies or chocolate after dinner.",
                "I can't stand the taste of plain water, so I rarely drink it unless it's flavored.",
                "I'm a creature of habit and eat the same breakfast—a peanut butter sandwich—every morning because it's easy.",
                "I really dislike most vegetables, especially broccoli and spinach, so I rarely eat salads.",
                "I'm a total night owl and do my best work after 10 PM, but then I struggle to wake up early.",
                "I hate the gym—it feels like a chore—so I avoid it at all costs.",
                "I get most of my social interaction from online gaming with friends rather than going out.",
                "I have a bad habit of biting my nails whenever I'm focused on a difficult task or feeling anxious.",
                "I drink my coffee with a lot of sugar and cream; I can't stand it black.",
                "I love spicy food, the hotter the better, but my stomach doesn't always agree with me afterwards.",
                "I'm a procrastinator and often end up rushing to finish tasks right before the deadline, which is super stressful.",
                "I prefer salty snacks like chips and pretzels over sweet ones when I'm watching a movie.",
                "I always take the elevator, even if it's just one or two floors—I just hate stairs.",
                "I find cooking for one person really depressing, so I usually just order in or make a frozen meal.",
                "I'm on my phone constantly, checking social media or news, even during meals.",
                "I can't fall asleep in complete silence; I always have to have a TV show or podcast playing in the background.",
                "I have a weak spot for fast-food burgers and fries, especially when I'm tired after work.",
                "I tend to shop impulsively online when I'm feeling bored or down.",
                "I really enjoy my weekend beer, usually having a few while watching the game."
            ]
            
        
        user_lifestyle_descriptions.extend(new_add_info)
    else:
        user_lifestyle_descriptions = new_add_info

    TF = ['true', 'false']
    genders = ['male', 'female']
    countries = [
        # Arab Countries (10)
        "Tunisia",
        "Iraq",
        "Sudan",
        "Libya",
        "Yemen",
        "Syria",
        "Palestine",
        "Mauritania",
        "Bahrain",
        "Djibouti",
    
        # Non-Arab Countries (5)
        "Japan",
        "Brazil",
        "Italy",
        "South Korea",
        "Sweden"
    ]
    for i in range(n_samples):
        # semi - Healthy BMI Range [20 - 35]
        semi_healthy_BMI = np.round(np.random.uniform(low=21.0, high=32.0, size=1,)[0], 1)
        random_height = np.random.randint(130, 180)
        additional_infos = ', '.join(np.random.choice(user_lifestyle_descriptions, 3, replace=False))
        user_input = f"""
        User Info:
        - Name: {np.random.choice(names)}
        - Age: {np.random.randint(18, 70)}
        - Gender: {np.random.choice(genders)}
        - Height: {random_height} cm
        - Weight: {np.round(semi_healthy_BMI * pow(random_height/100, 2), 1)} kg 
        - Lives in: {np.random.choice(countries)}
        
        This is a survery answers from the user:
        Health Problems / Symptoms:
        - Do you have difficulty sleeping?: {np.random.choice(TF, p=[0.6, 0.4])}
          - How many hours do you sleep per night?: {np.random.randint(4,10)}
          - Do you feel tired or have low focus during work?: {np.random.choice(TF, p=[0.6, 0.4])}
        - Do you sometimes feel dehydrated or have headaches?: {np.random.choice(TF, p=[0.6, 0.4])}
        
        Lifestyle:
        - Do you work at a desk job for long hours?: {np.random.choice(TF, p=[0.6, 0.4])}
        - Do you exercise regularly?: {np.random.choice(TF, p=[0.4, 0.6])}
        - Do you drink coffee daily?: {np.random.choice(TF, p=[0.6, 0.4])}
        
        Additional Information:
        {additional_infos}
        
            """.strip()
        list_of_inputs.append(user_input)
    return list_of_inputs


instructions = [
    "I am not a morning person at all, so don't suggest I wake up early to exercise.",
    "I really dislike cooking, so any plan that involves complicated recipes is a no for me.",
    "I have a very sweet tooth and find it hard to resist desserts after dinner.",
    "I get bored easily with repetitive workouts, so I need variety to stay motivated.",
    "I prefer relaxing in the evenings, so don't recommend high-energy activities after work.",
    "I love my coffee and won't give it up, so suggest alternatives that work with my caffeine habit.",
    "I am on a tight budget, so any suggestions need to be low-cost or free.",
    "I get overwhelmed easily, so break any big goals down into very small steps for me.",
    "I have a desk job and sit all day, so I need reminders to move around.",
    "I am not a fan of gyms, so prefer outdoor activities or home workouts.",
    "I hit the snooze button multiple times, so don't schedule anything important for my first waking hour.",
    "I get decision fatigue from work, so just tell me what to eat for dinner; don't give me options.",
    "I love long, hot showers to decompress, even though I know they might dry out my skin.",
    "I strongly prefer salty snacks over sweet ones, so keep that in mind for healthy alternatives.",
    "I have a very irregular work schedule, so my routine changes from day to day.",
    "I am highly motivated by tracking and data, so give me apps or tools to log my progress.",
    "I tend to overcommit socially, so help me build in rest days without guilt.",
    "I work better with immediate rewards, not long-term goals.",
    "I am sensitive to criticism, so frame suggestions as positive choices, not failures.",
    "I spend most of my day on video calls, so my eyes get very tired from screen time.",
    "I have a long commute, so I need activities that can fit into short pockets of time.",
    "I am deeply uncomfortable with group fitness classes; I prefer to exercise alone.",
    "I forget to drink water unless I'm reminded, so I need prompts throughout the day.",
    "I love reading and quiet time, so suggest activities that are calming, not stimulating.",
    "I am trying to reduce my plastic use and be more eco-friendly in my choices.",
    "I often work through lunch, so I need quick meals that I can eat at my desk.",
    "I am very affected by the weather; my motivation drops on gloomy days.",
    "I prefer practical, actionable advice over general motivational quotes.",
    "I have a family to cook for, so any meal plans need to be kid-friendly.",
    "I am a creature of habit and resist change, so introduce new things slowly.",
    "I usually skip breakfast, so don’t build meal plans that rely heavily on it.",
    "I often travel for work, so I need routines that don’t require special equipment.",
    "I have stomach sensitivity, so avoid suggesting very spicy or greasy foods.",
    "I really enjoy listening to music while exercising, so recommend activities where I can use headphones.",
    "I don’t drink enough water, so give me reminders or tricks to stay hydrated.",
    "I live in a small apartment, so workouts should fit in limited space.",
    "I sometimes work night shifts, so my sleep schedule is not regular.",
    "I eat late dinners, so avoid recommending heavy snacks before bed.",
    "I get anxious with strict routines, so I prefer flexible plans.",
    "I don’t like running, so suggest alternatives for cardio.",
    "I have limited cooking skills, so I need very simple, step-by-step recipes.",
    "I’m usually on my phone a lot, so suggest health tips I can integrate with apps or reminders.",
    "I sometimes forget to take breaks, so encourage short stretches during the day.",
    "I prefer walking as my main form of exercise, so build around that.",
    "I enjoy social activities, so group-based suggestions work better for me.",
    "I often stay up late watching shows, so morning plans don’t fit me well.",
    "I like to reward myself with small treats, so include balance instead of strict restrictions.",
    "I’m on a budget, so suggest seasonal and affordable food options.",
    "I don’t enjoy tracking calories, so focus on portion sizes or habits instead.",
    "I value mental health, so mix in relaxation practices like meditation or journaling."
    
    
    
]
new_list_of_inputs_3_1 = generate_inputs(500, instructions, False)
new_list_of_inputs_3_2 = generate_inputs(500, instructions, True) ## Introduce the idea of giving instructions

third_thousands_unhealthy_data_1 = pd.DataFrame(new_list_of_inputs_3_1, columns=['user_inputs'])
third_thousands_unhealthy_data_1['HI_Target'] = ''
gemeni_gate(third_thousands_unhealthy_data_1, 0)
# third_thousands_unhealthy_data_1.to_csv('/kaggle/working/secoend_thousands_unhealthy_data_1.csv', index=False)

third_thousands_unhealthy_data_2 = pd.DataFrame(new_list_of_inputs_3_2, columns=['user_inputs'])
third_thousands_unhealthy_data_2['HI_Target'] = ''
gemeni_gate(third_thousands_unhealthy_data_2, 0)
# third_thousands_unhealthy_data_2.to_csv('/kaggle/working/secoend_thousands_unhealthy_data_2.csv', index=False)

## All data collected with one file, then start generating RB_Column with Gemeni
all_in_one = pd.DataFrame(columns=['user_inputs', 'HI_Target'])

df1 = pd.read_csv('/kaggle/input/seperated-data/first_thousands_unhealthy_data.csv')
df1.drop('Unnamed: 0', axis=1, inplace=True)

df2 = pd.read_csv('/kaggle/input/seperated-data/secoend_thousands_unhealthy_data.csv')
df3 = pd.read_csv('/kaggle/input/seperated-data/third_thousands_unhealthy_data_1.csv')
df3.drop('Unnamed: 0', axis=1, inplace=True)

df4 = pd.read_csv('/kaggle/input/seperated-data/third_thousands_unhealthy_data_2.csv')
all_in_one = pd.concat([all_in_one, df1, df2, df3, df4], ignore_index = True)
all_in_one.isna().value_counts()
all_in_one.dropna(ignore_index = True, inplace=True)
all_in_one.to_csv('/kaggle/working/all_in_one.csv', index=False)


## Generating RB_Target (Routine Building Target)
all_in_one['RB_Target'] = ''
all_in_one = all_in_one.sample(all_in_one.shape[0]) #Shuffeling 
gemeni_gate(all_in_one, 0, "RB_Target") 
# all_in_one.to_csv('/kaggle/working/all_in_one.csv', index=False)

################# - Done! --------->
