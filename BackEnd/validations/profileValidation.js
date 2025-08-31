import { z } from "zod";

const limits = {
  name: { min: 2, max: 30 },
  weight: { min: 1 },
  height: { min: 1 },
};

export const profileSchema = z.object({
  first_name: z.string()
    .trim()
    .min(limits.name.min, `First name must be at least ${limits.name.min} characters`)
    .max(limits.name.max, `First name must be at most ${limits.name.max} characters`),
  last_name: z.string()
    .trim()
    .min(limits.name.min, `Last name must be at least ${limits.name.min} characters`)
    .max(limits.name.max, `Last name must be at most ${limits.name.max} characters`),
  date_of_birth: z.string().refine(
    val => !isNaN(Date.parse(val)),
    { message: "Invalid date format" }
  ),
  weight: z.number().min(limits.weight.min, `Weight must be at least ${limits.weight.min}`),
  height: z.number().min(limits.height.min, `Height must be at least ${limits.height.min}`),
  gender: z.enum(['male', 'female'], { message: () => ({ message: "Gender must be 'male' or 'female'" }) }),
});
