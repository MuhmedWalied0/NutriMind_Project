import asyncHandler from "express-async-handler";
import PasswordResetService from "../services/passwordService.js";
import { sendResponse } from "../utils/response.js";

export const forgotPassword = asyncHandler(async (req, res) => {
  const { email } = req.body;
  const result = await PasswordResetService.requestPasswordReset(email);

  if (result.error) {
    return sendResponse(res, 400,result.error);
  }
  return sendResponse(res, 200, result.message);
});

export const verifyResetCode = asyncHandler(async (req, res) => {
  const { email, code } = req.body;
  const result = await PasswordResetService.verifyResetCode(email, code);

  if (result.error) {
    return sendResponse(res, 400,result.error);
  }
  
  return sendResponse(res, 200, "Code verified, you can reset password");
});

export const resetPassword = asyncHandler(async (req, res) => {
  const { email, code, newPassword } = req.body;
  const result = await PasswordResetService.resetPassword(email, code, newPassword);

  if (result.error) {
    return sendResponse(res, 400,result.error);
  }
  return sendResponse(res, 200, result.message);
});
