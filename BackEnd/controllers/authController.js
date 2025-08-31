import User from "../models/userModel.js";
import bcrypt from "bcrypt";
import jwt from "jsonwebtoken";
import asyncHandler from "express-async-handler";
import { sendResponse } from "../utils/response.js";

export const signUp = asyncHandler(async (req, res) => {
  const { username, email, password } = req.body;

  // Check if user already exists
  const existingUser = await User.findOne({ email });
  if (existingUser) {
    return sendResponse(res, 400, false, "User already exists");
  }

  // Hash password
  const hashedPassword = await bcrypt.hash(password, 10);

  // Create new user
  const user = await User.create({
    username,
    email,
    password: hashedPassword,
  });
  const token = jwt.sign(
    { id: user._id, email: user.email },
    process.env.JWT_SECRET,
    { expiresIn: "7d" }
  );
  return sendResponse(res, 201, true, "Account created successfully", {
    id: user._id,
    username: user.username,
    email: user.email,
    token
  });
});

export const signIn = asyncHandler(async (req, res) => {
  const { email, password } = req.body;

  // Find user
  const user = await User.findOne({ email });
  if (!user) {
    return sendResponse(res, 400, false, "Invalid email or password");
  }

  // Compare password
  const isMatch = await bcrypt.compare(password, user.password);
  if (!isMatch) {
    return sendResponse(res, 400, false, "Invalid email or password");
  }

  // Generate JWT
  const token = jwt.sign(
    { id: user._id, email: user.email },
    process.env.JWT_SECRET,
    { expiresIn: "7d" }
  );

  return sendResponse(res, 200, true, "Login successful", {
    id: user._id,
    username: user.username,
    email: user.email,
    token
  });
});

// Log Out
export const logout = asyncHandler(async (req, res) => {
  res.clearCookie("token");
  return sendResponse(res, 200, true, "Logged out successfully");
});
