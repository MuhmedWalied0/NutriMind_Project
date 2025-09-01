import WeeklyRoutine from "../models/weeklyRoutineModel.js";
import { sendResponse } from "../utils/response.js";
import asyncHandler from "express-async-handler";
import { updateStatusRoutine } from "../utils/weeklyRoutineUtils.js";

export const checkRoutineBeforeCreate = asyncHandler(async (req, res, next) => {
  const existingRoutine = await WeeklyRoutine.findOne({
    user_id: req.user.id,
    status: "active",
  }).select("progress start_date status _id");

  if (existingRoutine) {
    const isUpdated = await updateStatusRoutine(existingRoutine);
    if (isUpdated) {
      return next(); 
    } else {
      return sendResponse(res,200,true,"You already have an active routine",existingRoutine);
    }
  } else {
    return next();
  }
});