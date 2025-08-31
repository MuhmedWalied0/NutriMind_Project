import asyncHandler from "express-async-handler";
import Profile from "../models/profileModel.js";
import { profileSchema } from "../validations/profileValidation.js";
import { sendResponse } from "../utils/response.js";

export const createProfile = asyncHandler(async (req, res) => {  
  const existingProfile = await Profile.findOne({ user_id: req.user.id });
  if (existingProfile) {
    return sendResponse(res, 400, false, "Profile already exists");
  }

  const profile = await Profile.create({ ...req.body, user_id: req.user.id });

  const responseProfile = await Profile.findById(profile._id).select(
    "first_name last_name date_of_birth weight height gender -_id"
  );

  return sendResponse(res, 201, true, "Profile created successfully", responseProfile);
});

export const getProfile = asyncHandler(async (req, res) => {
  const profile = await Profile.findOne({ user_id: req.user.id }).select(
  "-_id first_name last_name date_of_birth weight height gender"
);
  if (!profile) {
    return sendResponse(res, 404, false, "Profile not found");
  }
  return sendResponse(res, 200, true, "Profile fetched successfully", profile);
});

export const updateProfile = asyncHandler(async (req, res) => {
  const profile = await Profile.findOneAndUpdate(
    { user_id: req.user.id },
    req.body,
    { new: true }
  );
  if (!profile) {
    return sendResponse(res, 404, false, "Profile not found");
  }
  
  const responseProfile = await Profile.findById(profile._id).select(
    "first_name last_name date_of_birth weight height gender -_id"
  );

  return sendResponse(res, 200, true, "Profile updated successfully", responseProfile);
});
