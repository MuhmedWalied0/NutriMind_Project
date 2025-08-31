import express from "express";
import { validate } from "../middlewares/validate.js";
import { profileSchema } from "../validations/profileValidation.js";
import { createProfile, getProfile, updateProfile } from "../controllers/profileController.js";
import { protect } from "../middlewares/authMiddleware.js";

const router = express.Router();

router.use(protect);

router.route("/")
  .get(getProfile)
  .post(validate(profileSchema), createProfile)
  .put(validate(profileSchema), updateProfile)

export default router;
