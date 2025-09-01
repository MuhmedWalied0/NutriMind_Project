import express from "express";
import {createRoutine,getRoutines,getCurrentRoutine,} from "../controllers/weeklyRoutineController.js";
import { protect } from "../middlewares/authMiddleware.js";

const router = express.Router();

router.use(protect);

router.route("/")
  .get(getRoutines)
  .post(createRoutine)

router.route("/current")
  .get(getCurrentRoutine)

export default router;
