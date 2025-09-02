import mongoose from "mongoose";

const weeklyRoutineSchema = new mongoose.Schema(
  {
    user_id: { type: mongoose.Schema.Types.ObjectId, ref: 'User', required: true },
    start_date: {type: Date,default: Date.now,},
    status: {type: String,enum: ["active", "completed", "expired"],default: "active",},
    progress: { type: Number, default: 0 },
  },
  { timestamps: true }
);

const WeeklyRoutine = mongoose.model("WeeklyRoutine", weeklyRoutineSchema);

export default WeeklyRoutine;
