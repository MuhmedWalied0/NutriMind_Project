import express from "express";
import { signUp, signIn, logout } from "../controllers/authController.js";
import { signupSchema, signinSchema } from "../validations/authValidation.js";
import { validate } from "../middlewares/validate.js";
import { protect } from "../middlewares/authMiddleware.js";

const router = express.Router();

router.post("/signup", validate(signupSchema), signUp);
router.post("/signin", validate(signinSchema), signIn);
router.post("/logout",protect, logout);

export default router;
