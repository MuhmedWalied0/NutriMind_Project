const mongoose = require("mongoose");

const questionsSchema = new mongoose.Schema(
    {
        // questionID:{
        //     type:String,
        //     required:true,
        // }
        questionCategory:{
            type : String,
            required : [true , "The category of questions is required"],
            minLength :[3 , "The category name is too small"],
            maxLength :[70 , "The category name is too big"]
        },
        questionTitle:{
            type:String,
            required : [true , "The title of questions is required"],
            minLength :[3 , "The title name is too small"],
            maxLength :[70 , "The title name is too big"]
        }

    }
    ,
    {
        timestamps:true
    }
)

module.exports = mongoose.model("Questions",questionsSchema);