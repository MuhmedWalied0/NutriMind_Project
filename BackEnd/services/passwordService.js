import User from "../models/userModel.js";
import bcrypt from "bcrypt";
import { generateResetToken, sendResetEmail } from "../utils/sendEmail.js";

class PasswordResetService {
  constructor(expireMinutes = parseInt(process.env.RESET_PASSWORD_EXPIRES) || 10) {
    this.expireMinutes = expireMinutes;
  }

  async requestPasswordReset(email) {
    const user = await User.findOne({ email });
    if (!user) return { error: "Email not found" };

    if (user.lastResetRequest && Date.now() - user.lastResetRequest < 60 * 1000) {
      return { error: "Please wait a minute before requesting again" };
    }

    const token = generateResetToken();
    user.resetPasswordToken = token;
    user.resetPasswordExpires = Date.now() + this.expireMinutes * 60 * 1000;
    user.lastResetRequest = Date.now();
    await user.save();

    await sendResetEmail(email, token);
    return { success: true, message: "Reset code sent to email" };
  }

  async verifyResetCode(email, code) {
    const user = await User.findOne({ email });
    if (!user || user.resetPasswordToken !== code) return { error: "Invalid code" };
    if (Date.now() > user.resetPasswordExpires) return { error: "Code expired" };

    return { success: true };
  }

  async resetPassword(email, code, newPassword) {
    const user = await User.findOne({ email });
    if (!user || user.resetPasswordToken !== code) return { error: "Invalid or expired code" };
    if (Date.now() > user.resetPasswordExpires) return { error: "Code expired" };

    user.password = await bcrypt.hash(newPassword, 10);
    user.resetPasswordToken = undefined;
    user.resetPasswordExpires = undefined;
    await user.save();

    return { success: true, message: "Password reset successfully" };
  }
}

export default new PasswordResetService;
