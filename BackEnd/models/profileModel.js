import mongoose from 'mongoose';

const userSchema = new mongoose.Schema({
  user_id: { type: mongoose.Schema.Types.ObjectId, ref: 'User', required: true },
  first_name: { type: String, required: true, trim: true },
  last_name: { type: String, required: true, trim: true },
  date_of_birth: { type: Date, required: true },
  weight: { type: Number, required: true, min: 1 },
  height: { type: Number, required: true, min: 1 }, 
  gender: { 
    type: String, 
    required: true, 
    enum: ['male', 'female'] 
  },
}, { timestamps: true });

const User = mongoose.model('User', userSchema);

export default User;
