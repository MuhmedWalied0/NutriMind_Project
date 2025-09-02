export const sendResponse = (res, statusCode, message, data = null) => {
  res.status(statusCode).json({
    success:statusCode<300,
    message,
    data
  });
};
