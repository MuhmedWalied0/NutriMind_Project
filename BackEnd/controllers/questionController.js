import asyncHandler from "express-async-handler";
import Question from "../models/questionModel.js";
import { sendResponse } from "../../../nutriMind-main/utils/response.js";

export const createQuestion = asyncHandler(async (req, res) => {
  const { name, question } = req.body;
  const newQuestion = await Question.create({ name, question });
  return sendResponse(
    res,
    201,
    "Question created successfully",
    newQuestion
  );
});

export const getQuestions = asyncHandler(async (req, res) => {
  const questions = await Question.find().sort({ createdAt: -1 });
  return sendResponse(
    res,
    200,
    "Questions retrieved successfully",
    questions
  );
});

export const getQuestion = asyncHandler(async (req, res) => {
  const question = await Question.findById(req.params.id);
  if (!question) {
    return sendResponse(res, 404, false, "Question not found");
  }
  return sendResponse(
    res,
    200,
    "Question retrieved successfully",
    question
  );
});

export const updateQuestion = asyncHandler(async (req, res) => {
  const { name, question } = req.body;
  const updated = await Question.findByIdAndUpdate(
    req.params.id,
    { name, question },
    { new: true, runValidators: true }
  );
  if (!updated) {
    return sendResponse(res, 404, "Question not found");
  }
  return sendResponse(res, 200, "Question updated successfully", updated);
});

export const deleteQuestion = asyncHandler(async (req, res) => {
  const deleted = await Question.findByIdAndDelete(req.params.id);
  if (!deleted) {
    return sendResponse(res, 404,"Question not found");
  }
  return sendResponse(res, 200,"Question deleted successfully", deleted);
});
