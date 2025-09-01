import WeeklyRoutine from "../models/weeklyRoutineModel.js";
import asyncHandler from "express-async-handler";
import { sendResponse } from "../utils/response.js";
import { updateStatusRoutine } from "../utils/weeklyRoutineUtils.js";

export const getRoutines = asyncHandler(async (req, res) => {
  const routines = await WeeklyRoutine.find({ user_id: req.user.id }).select(
    "start_date progress status"
  );

  return sendResponse(res, 200, true, "Routines fetched successfully", routines);
});

export const getCurrentRoutine = asyncHandler(async (req, res) => {
  const existingRoutine = await WeeklyRoutine.findOne({
    user_id: req.user.id,
    status: "active",
  }).select("progress start_date status _id");

  if (!existingRoutine) {
    return sendResponse(res, 404, false, "No active routine found");
  }

  const isUpdated = await updateStatusRoutine(existingRoutine);
  if (isUpdated) {
    return sendResponse(res,200,true,"Your previous routine has ended. You can create a new one.",existingRoutine);
  }

  return sendResponse(res, 200, true, "Current routine", existingRoutine);
});

export const createRoutine = asyncHandler(async (req, res) => {
  const routine = await WeeklyRoutine.create({
    user_id: req.user.id,
  });

  const response = await WeeklyRoutine.findById(routine._id).select(
    "start_date status _id"
  );

  return sendResponse(res, 201, true, "Routine created successfully", response);
});