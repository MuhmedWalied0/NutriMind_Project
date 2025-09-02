import express from "express";
import {
  createQuestion,
  getQuestions,
  getQuestion,
  updateQuestion,
  deleteQuestion,
} from "../controllers/questionController.js";
import { validate } from "../../../nutriMind-main/middlewares/validate.js";
import { questionSchema } from "../validations/questionValidation.js";
import { protect } from "../../../nutriMind-main/middlewares/authMiddleware.js";

const router = express.Router();

router.use(protect);

router
  .route("/")
  .get(getQuestions)
  .post(validate(questionSchema), createQuestion);

router
  .route("/:id")
  .get(getQuestion)
  .put(validate(questionSchema), updateQuestion)
  .delete(deleteQuestion);

export default router;
