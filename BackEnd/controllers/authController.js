import asyncHandler from "express-async-handler";
import { sendResponse } from "../utils/response.js";
import authService from "../services/authService.js";

export const signUp = asyncHandler(async (req, res) => {
  const { username, email, password } = req.body;
  const { user, token } = await authService.registerUser({ username, email, password });
  res.cookie("token", token, { httpOnly: true, secure: false, sameSite: "lax" });

  return sendResponse(res, 201, "Account created successfully", {
    id: user._id,
    username: user.username,
    email: user.email,
  });
});

export const signIn = asyncHandler(async (req, res) => {
  const { email, password } = req.body;
  const { user, token } = await authService.loginUser({ email, password });
  res.cookie("token", token, { httpOnly: true, secure: false, sameSite: "lax" });

  return sendResponse(res, 200, "Login successful", {
    id: user._id,
    username: user.username,
    email: user.email,
  });
});

export const logout = asyncHandler(async (req, res) => {
  res.clearCookie("token");

  return sendResponse(res, 200, "Logged out successfully");
});