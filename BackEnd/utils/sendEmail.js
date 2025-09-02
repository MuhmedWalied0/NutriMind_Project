import nodemailer from "nodemailer";
import { resetPasswordTemplate } from "./emailTemplates/resetPasswordTemplate.js";

export const generateResetToken = (length = 6) => {
  let token = '';
  for (let i = 0; i < length; i++) {
    token += Math.floor(Math.random() * 10);
  }
  return token;
};


export const sendResetEmail = async (email, token) => {
  const transporter = nodemailer.createTransport({
    service: "gmail",
    auth: {
      user: process.env.EMAIL_USER,
      pass: process.env.EMAIL_PASS,
    },
  });

  await transporter.sendMail({
  from: `"NutriMind Support" <${process.env.EMAIL_USER}>`,
  to: email,
  subject: "Password Reset Request",
  html:resetPasswordTemplate(token)
});


};
