import asyncHandler from "express-async-handler";
import { sendResponse } from "../utils/response.js";
import profileService from "../services/profileService.js";

export const createProfile = asyncHandler(async (req, res) => {
  const profile = await profileService.createProfile(req.user.id, req.body);
  return sendResponse(res, 201, "Profile created successfully", profile);
});

export const getProfile = asyncHandler(async (req, res) => {
  const profile = await profileService.getProfile(req.user.id);
  return sendResponse(res, 200,"Profile fetched successfully", profile);
});

export const updateProfile = asyncHandler(async (req, res) => {
  const profile = await profileService.updateProfile(req.user.id, req.body);
  return sendResponse(res, 200,"Profile updated successfully", profile);
});
