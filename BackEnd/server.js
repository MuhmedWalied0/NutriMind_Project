import express from 'express';
import dotenv from 'dotenv';
import { errorHandler } from './utils/errorHandler.js';

dotenv.config();

const app = express();

// Middlewares
app.use(express.json());

app.get("/api",(req,res)=>{
  res.json({msg:"Hello World"})
})

app.use(errorHandler);

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
