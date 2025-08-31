# NutriMind Project

[![Work in Progress](https://img.shields.io/badge/Status-Work%20in%20Progress-yellow)](https://github.com/MuhmedWalied0/NutriMind_Project)
[![Node.js](https://img.shields.io/badge/Node.js-18%2B-green)](https://nodejs.org/)
[![MongoDB](https://img.shields.io/badge/MongoDB-Latest-brightgreen)](https://www.mongodb.com/)

A backend API for user authentication and profile management built with Node.js, Express, MongoDB, and Zod validation.

> **⚠️ Note:** This project is currently under development. Some features are incomplete or may change.

---

## 📋 Table of Contents
- [Features](#-features)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Environment Variables](#-environment-variables)
- [Running the Project](#-running-the-project)
- [API Endpoints](#-api-endpoints)
- [Validation](#-validation)
- [Error Handling](#-error-handling)
---

## ✨ Features

- **User Authentication**: Sign Up, Sign In, Logout functionality
- **Profile Management**: Create, retrieve, and update user profiles
- **Input Validation**: Robust validation using Zod schemas
- **JWT Authentication**: Secure token-based authentication
- **Cookie Support**: Secure token storage in HTTP-only cookies
- **Error Handling**: Consistent error response format
- **MongoDB Integration**: NoSQL database for data persistence

---

## 🔧 Prerequisites

Before running this project, make sure you have the following installed:

- [Node.js](https://nodejs.org/) (version 16 or higher)
- [MongoDB](https://www.mongodb.com/) (local installation or MongoDB Atlas)

---

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/MuhmedWalied0/NutriMind_Project.git
   cd BackEnd
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

---

## 🔐 Environment Variables

Create a `.env` file in the root directory with the following variables:

```env
# Server Configuration
PORT=5000

# Database Configuration
MONGO_URI=mongodb://localhost:27017/nutrimind

# Security
JWT_SECRET=your_super_secure_jwt_secret_here

```

---

## 🚀 Running the Project

### Development Mode
```bash
npm run dev
```

### Production Mode
```bash
npm start
```

The server will be available at `http://localhost:5000`

---

## 📡 API Endpoints

### 🔒 Authentication Endpoints

#### Sign Up
- **Endpoint:** `POST /api/auth/signup`
- **Description:** Create a new user account
- **Request Body:**
  ```json
  {
    "username": "john_doe",
    "email": "john@example.com",
    "password": "password123"
  }
  ```
- **Success Response:**
  ```json
  {
    "success": true,
    "message": "Account created successfully",
    "data": {
      "id": "<user_id>",
      "username": "john_doe",
      "email": "john@example.com"
    }
  }
  ```

#### Sign In
- **Endpoint:** `POST /api/auth/signin`
- **Description:** Authenticate user and receive JWT token
- **Request Body:**
  ```json
  {
    "email": "john@example.com",
    "password": "password123"
  }
  ```
- **Success Response:**
  ```json
  {
    "success": true,
    "message": "Login successful",
    "token": "<jwt_token>"
  }
  ```

#### Logout
- **Endpoint:** `POST /api/auth/logout`
- **Description:** Invalidate user session
- **Authentication:** Required
- **Success Response:**
  ```json
  {
    "success": true,
    "message": "Logged out successfully"
  }
  ```

### 👤 Profile Endpoints

> **Note:** All profile endpoints require authentication via JWT token in cookies.

#### Create Profile
- **Endpoint:** `POST /api/profile`
- **Description:** Create a new user profile
- **Authentication:** Required

#### Get Profile
- **Endpoint:** `GET /api/profile`
- **Description:** Retrieve current user's profile
- **Authentication:** Required

#### Update Profile
- **Endpoint:** `PUT /api/profile`
- **Description:** Update current user's profile
- **Authentication:** Required

---

## ✅ Validation

All API requests are validated using **Zod** schemas. Invalid requests return structured error messages:

### Validation Error Response Format:
```json
{
  "success": false,
  "message": [
    {
      "path": ["username"],
      "message": "Username must be at least 3 characters long"
    },
    {
      "path": ["email"],
      "message": "Invalid email address"
    }
  ]
}
```

### Common Validation Rules:
- **Username:** Minimum 3 characters, alphanumeric with underscores
- **Email:** Valid email format required
- **Password:** Minimum 6 characters (consider increasing for production)

---

## 🚨 Error Handling

All API errors follow a consistent response format:

```json
{
  "success": false,
  "message": "Error message description",
  "data": null
}
```

### Common HTTP Status Codes:
- `200` - Success
- `400` - Bad Request (validation errors)
- `401` - Unauthorized (authentication required)
- `403` - Forbidden (insufficient permissions)
- `404` - Not Found
- `500` - Internal Server Error

---

## 🔗 Links

- **Repository:** [GitHub](https://github.com/MuhmedWalied0/NutriMind_Project)
- **Documentation:** Coming Soon

---
