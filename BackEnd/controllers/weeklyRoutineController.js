import asyncHandler from "express-async-handler";
import { sendResponse } from "../utils/response.js";
import weeklyRoutineService from "../services/weeklyRoutineService.js";

export const getRoutines = asyncHandler(async (req, res) => {
  const routines = await weeklyRoutineService.getRoutines(req.user.id);
  return sendResponse(res, 200, true, "Routines fetched successfully", routines);
});

export const getCurrentRoutine = asyncHandler(async (req, res) => {
  const { routine, message, updated } = await weeklyRoutineService.getCurrentRoutine(req.user.id);

  return sendResponse(res, updated ? 200 : 200, true, message, routine);
});

export const createRoutine = asyncHandler(async (req, res) => {
  const { routine, message, blocked } = await weeklyRoutineService.createRoutine(req.user.id);

  if (blocked) {
    return sendResponse(res, 200, true, message, routine);
  }

  return sendResponse(res, 201, true, message, routine);
});
