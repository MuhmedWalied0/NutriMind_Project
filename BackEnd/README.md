---

# NutriMind Project

[![Work in Progress](https://img.shields.io/badge/Status-Work%20in%20Progress-yellow)](https://github.com/MuhmedWalied0/NutriMind_Project)
[![Node.js](https://img.shields.io/badge/Node.js-18%2B-green)](https://nodejs.org/)
[![MongoDB](https://img.shields.io/badge/MongoDB-Latest-brightgreen)](https://www.mongodb.com/)

A backend API for user authentication, profile, and weekly routine management built with Node.js, Express, MongoDB, and Zod validation.

> **⚠️ Note:** This project is under active development. Some features may change.

---

## 📋 Table of Contents

* [Features](#-features)
* [Prerequisites](#-prerequisites)
* [Installation](#-installation)
* [Environment Variables](#-environment-variables)
* [Running the Project](#-running-the-project)
* [API Endpoints](#-api-endpoints)
* [Validation](#-validation)
* [Error Handling](#-error-handling)
* [Implemented Improvements](#-implemented-improvements)

---

## ✨ Features

* **User Authentication**: Sign Up, Sign In, Logout
* **Profile Management**: Create, retrieve, and update user profiles
* **Weekly Routine Management**: Create, get current, and list weekly routines
* **Input Validation**: Robust validation using Zod schemas
* **JWT Authentication**: Secure token-based authentication
* **Cookie Support**: HTTP-only cookies for token storage
* **Error Handling**: Consistent error response format using AppError and global middleware
* **MongoDB Integration**: NoSQL database for data persistence

---

## 🔧 Prerequisites

* [Node.js](https://nodejs.org/) (version 16+)
* [MongoDB](https://www.mongodb.com/) (local installation or Atlas)

---

## 📦 Installation

```bash
git clone https://github.com/MuhmedWalied0/NutriMind_Project.git
cd BackEnd
npm install
```

---

## 🔐 Environment Variables

```env
PORT=5000
MONGO_URI=mongodb://localhost:27017/nutrimind
JWT_SECRET=your_super_secure_jwt_secret_here
JWT_EXPIRES_IN=7d
```

---

## 🚀 Running the Project

**Development:**

```bash
npm run dev
```

**Production:**

```bash
npm start
```

Server runs at `http://localhost:5000`

---

## 📡 API Endpoints

### 🔒 Authentication

* **Sign Up**: `POST /api/auth/signup`
* **Sign In**: `POST /api/auth/signin`
* **Logout**: `POST /api/auth/logout`

### 👤 Profile

* **Create Profile**: `POST /api/profile`
* **Get Profile**: `GET /api/profile`
* **Update Profile**: `PUT /api/profile`

### 📅 Weekly Routine

* **Get Routines**: `GET /api/routines`
* **Get Current Routine**: `GET /api/routines/current`
* **Create Routine**: `POST /api/routines`

> All protected endpoints require JWT authentication via HTTP-only cookies.

---

## ✅ Validation

* **Zod** schemas validate inputs.
* Invalid requests return structured error messages.

Example:

```json
{
  "success": false,
  "message": [
    {
      "path": ["username"],
      "message": "Username must be at least 3 characters long"
    }
  ]
}
```

---

## 🚨 Error Handling

* All errors use **AppError** with proper HTTP status codes.
* Global error middleware ensures consistent JSON responses.

Example:

```json
{
  "success": false,
  "message": "Profile not found",
  "data": null
}
```

Status codes include: `200`, `400`, `401`, `403`, `404`, `409`, `500`.

---

## 🛠 Implemented Improvements

* **AppError** class for consistent error handling and HTTP status codes.
* **Global error middleware** to capture and return errors with proper codes.
* **Service Layer Refactor**: AuthService, ProfileService, WeeklyRoutineService

  * Centralized logic, removed redundant controller checks.
  * Validation and checks moved from middleware to services.
* **Safe/select fields** returned in responses to avoid exposing sensitive data (e.g., password).
* Controllers simplified to just call services and return `sendResponse`.
* Standardized error messages and response format across the project.

---

## 🔗 Links

* **Repository:** [GitHub](https://github.com/MuhmedWalied0/NutriMind_Project)
* **Documentation:** Coming Soon

---
