import { sendResponse } from "../utils/response.js";

export const validate = (schema) => {
  return (req, res, next) => {
    if (!req.body) {
      return sendResponse(res, 400, "Request body is missing");
    }
    const result = schema.safeParse(req.body);
    if (!result.success) {
      const formattedErrors = result.error.issues.map((issue) => ({
        field: issue.path.join("."),
        message: issue.message,
      }));
      return sendResponse(res, 400, "Validation failed", formattedErrors);
    } else {
      req.body = result.data;
      next();   
    }
  };
};
