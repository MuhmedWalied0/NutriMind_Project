import { z } from "zod";

const limits = {
  username: { min: 3, max: 20 },
  password: { min: 8, max: 30 },
};

export const signupSchema = z.object({
  username: z.string().trim()
  .min(limits.username.min, `Username must be at least ${limits.username.min} characters long`)
  .max(limits.username.max, `Username must be at most ${limits.username.max} characters long`),
  email: z.email("Invalid email address"),
  password: z.string()
  .min(limits.password.min, `Password must be at least ${limits.password.min} characters long`)
  .max(limits.password.max, `Password must be at most ${limits.password.max} characters long`),
});

export const signinSchema = z.object({
  email: z.email("Invalid email address"),
  password: z.string()
  .min(limits.password.min, `Password must be at least ${limits.password.min} characters long`)
  .max(limits.password.max, `Password must be at most ${limits.password.max} characters long`),
});