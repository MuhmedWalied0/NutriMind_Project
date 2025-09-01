import User from "../models/userModel.js";
import bcrypt from "bcrypt";
import jwt from "jsonwebtoken";
import AppError from "../utils/appError.js";

class AuthService {
  safeFields = "username email _id";

  generateToken(user) {
    return jwt.sign(
      { id: user._id, email: user.email },
      process.env.JWT_SECRET,
      { expiresIn: process.env.JWT_EXPIRES_IN || "7d" }
    );
  }

  async registerUser({ username, email, password }) {
    const existingEmail = await User.findOne({ email });
    if (existingEmail) {
      throw new AppError("Email already in use", 409);
    }

    const existingUsername = await User.findOne({ username });
    if (existingUsername) {
      throw new AppError("Username already taken", 409);
    }

    const hashedPassword = await bcrypt.hash(password, 10);

    const user = await User.create({
      username,
      email,
      password: hashedPassword,
    });

    const token = this.generateToken(user);

    const safeUser = await User.findById(user._id).select(this.safeFields);

    return { user: safeUser, token };
  }

  async loginUser({ email, password }) {
    const user = await User.findOne({ email });
    if (!user) {
      throw new AppError("Invalid email or password", 409);
    }

    const isMatch = await bcrypt.compare(password, user.password);
    if (!isMatch) {
      throw new AppError("Invalid email or password", 409);
    }

    const token = this.generateToken(user);

    const safeUser = await User.findById(user._id).select(this.safeFields);

    return { user: safeUser, token };
  }
}

export default new AuthService();
