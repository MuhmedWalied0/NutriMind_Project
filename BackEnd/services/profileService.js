import Profile from "../models/profileModel.js";
import AppError from "../utils/appError.js";

class ProfileService {
  profileFields = "first_name last_name date_of_birth weight height gender -_id";

  async createProfile(userId, data) {
    const existingProfile = await Profile.findOne({ user_id: userId });
    if (existingProfile) {
      throw new AppError("Profile already exists", 409);
    }

    const profile = await Profile.create({ ...data, user_id: userId });

    return await Profile.findById(profile._id).select(this.profileFields);
  }

  async getProfile(userId) {
    const profile = await Profile.findOne({ user_id: userId }).select(this.profileFields);
    if (!profile) {
      throw new AppError("Profile not found", 404);
    }
    return profile;
  }

  async updateProfile(userId, data) {
    const profile = await Profile.findOneAndUpdate(
      { user_id: userId },
      data,
      { new: true }
    );
    if (!profile) {
      throw new AppError("Profile not found", 404);
    }

    return await Profile.findById(profile._id).select(this.profileFields);
  }
}

export default new ProfileService();
