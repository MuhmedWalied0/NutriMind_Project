import express from 'express';
import dotenv from 'dotenv';
import authRoutes from "./routes/authRoutes.js";
import { errorHandler } from './utils/errorHandler.js';
import connectDB from "./config/db.js";

dotenv.config();

const app = express();

connectDB()

// Middlewares
app.use(express.json());


app.use("/api/auth", authRoutes);

app.use(errorHandler);

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
