import WeeklyRoutine from "../models/weeklyRoutineModel.js";
import AppError from "../utils/appError.js";
import { updateStatusRoutine } from "../utils/weeklyRoutineUtils.js";

class WeeklyRoutineService {
  routineFields = "start_date progress status _id";

  async getRoutines(userId) {
    return await WeeklyRoutine.find({ user_id: userId }).select(
      this.routineFields
    );
  }

  async getCurrentRoutine(userId) {
    const existingRoutine = await WeeklyRoutine.findOne({
      user_id: userId,
      status: "active",
    }).select(this.routineFields);

    if (!existingRoutine) {
      throw new AppError("No active routine found", 404);
    }

    const isUpdated = await updateStatusRoutine(existingRoutine);
    if (isUpdated) {
      return {
        routine: existingRoutine,
        message: "Your previous routine has ended. You can create a new one.",
        updated: true,
      };
    }

    return { routine: existingRoutine, message: "Current routine", updated: false };
  }

  async createRoutine(userId) {
    const existingRoutine = await WeeklyRoutine.findOne({
      user_id: userId,
      status: "active",
    }).select(this.routineFields);

    if (existingRoutine) {
      const isUpdated = await updateStatusRoutine(existingRoutine);
      if (!isUpdated) {
        return {
          routine: existingRoutine,
          message: "You already have an active routine",
          blocked: true
        };
      }
    }

    const routine = await WeeklyRoutine.create({ user_id: userId });

    const response = await WeeklyRoutine.findById(routine._id).select(this.routineFields);

    return { routine: response, message: "Routine created successfully", blocked: false };
  }
}

export default new WeeklyRoutineService();
