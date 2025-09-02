import mongoose from 'mongoose';

const questionsSchema = new mongoose.Schema({
    name:{type : String,required :true,},
    question:{ type:String,required :true }
    },{timestamps:true}
)

const Question = mongoose.model('Question', questionsSchema);

export default Question;
