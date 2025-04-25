# 🌱 Plant Tracker – Web App for Plant Enthusiasts

- [🌱 Plant Tracker – Web App for Plant Enthusiasts](#-plant-tracker--web-app-for-plant-enthusiasts)
  - [✨ Features](#-features)
  - [🧱 Tech Stack](#-tech-stack)
  - [🚀 Getting Started](#-getting-started)
    - [Prerequisites](#prerequisites)
    - [Setup](#setup)
  - [📚 API Overview](#-api-overview)
    - [🨴 Plant Catalog](#-plant-catalog)
    - [👤 User Management](#-user-management)
    - [💬 Comments](#-comments)
    - [📊 Graph Data](#-graph-data)
    - [📄 Wishlist](#-wishlist)


**Plant Tracker** is a web application designed for plant lovers to manage their own plant collections, track care parameters, interact with the plant community, and explore a plant catalog. This project combines features of a structured database with community-driven content and data visualization.

---

## ✨ Features

- 📘 **Plant Catalog** – Add, browse, and explore plant profiles with detailed care information (e.g., pH, humidity, temperature).
- 💬 **Comment System** – Comment on and discuss plant entries with other users.
- 📊 **Data Visualization** – Generate graphs for parameters like pH, humidity, temperature, EC, and more.
- 🤝 **Friends & Followers System** – Connect with other users, follow their activity, and build a community.
- 📝 **Wishlist** – Create a personal wishlist of plants you'd like to purchase or grow.
- 🔐 **Google OAuth Login** – Seamless and secure authentication via Google.

---

## 🧱 Tech Stack

- **Frontend:** React (Next.js or Vite), Tailwind CSS, Chart.js or Recharts
- **Backend:** Node.js (Express), REST API, JWT Auth, Passport.js (Google OAuth)
- **Database:** PostgreSQL (via Prisma ORM)
- **Hosting:** Vercel (frontend), Render / Railway (backend + DB)
- **Other:** Cloudinary (image storage), Zod (validation), Day.js (date utils)

---

## 🚀 Getting Started

### Prerequisites

- Node.js
- PostgreSQL
- Google OAuth credentials (Client ID and Secret)

### Setup

```bash
# Clone the repo
git clone https://github.com/yourname/plant-tracker.git

# Install dependencies
cd backend
npm install

cd ../frontend
npm install

# Configure environment variables (see .env.example files)
```

---

## 📚 API Overview

The backend will expose a RESTful API with the following main routes:

### 🨴 Plant Catalog

- `GET /plants` – List all plants (with filters)
- `GET /plants/:id` – Get plant details
- `POST /plants` – Create new plant (admin only)
- `PUT /plants/:id` – Update plant
- `DELETE /plants/:id` – Delete plant (admin only)

### 👤 User Management

- `POST /auth/login-google` – Google OAuth login
- `GET /users/:id` – Get user profile
- `PUT /users/:id` – Update user profile
- `GET /users/:id/friends` – List friends/followers

### 💬 Comments

- `POST /plants/:id/comments` – Add comment to plant
- `GET /plants/:id/comments` – Get all comments for plant
- `DELETE /comments/:id` – Delete comment

### 📊 Graph Data

- `GET /plants/:id/graph-data` – Get historical data for graphs

### 📄 Wishlist

- `GET /wishlist` – Get current user's wishlist
- `POST /wishlist` – Add a plant to wishlist
- `DELETE /wishlist/:id` – Remove a plant from wishlist

---

Stay tuned for ongoing development!
