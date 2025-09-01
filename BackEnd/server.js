import express from 'express';
import dotenv from 'dotenv';
import cookieParser from "cookie-parser";
import authRoutes from "./routes/authRoutes.js";
import profileRoutes from "./routes/profileRoutes.js";
import routineRoutes from "./routes/weeklyRoutineRoutes.js";
import { errorHandler } from './utils/errorHandler.js';
import connectDB from "./config/db.js";

dotenv.config();

const app = express();

connectDB()
app.use(cookieParser());
app.use(express.json());


app.use("/api/auth", authRoutes);
app.use("/api/profile", profileRoutes);
app.use("/api/routines", routineRoutes);

app.use(errorHandler);

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
