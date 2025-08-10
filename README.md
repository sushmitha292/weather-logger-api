# 🌦 Weather Logger API – Real-Time Data Pipeline

A real-time weather data ingestion pipeline built with **Python**, **FastAPI**, and **MongoDB**, designed to fetch, store, and manage live weather information from the **OpenWeatherMap API**.  
ETL jobs are scheduled using **APScheduler** to automate data collection every 5 minutes, simulating a production-grade data pipeline.

---

## 📌 Features
- **RESTful API** built with FastAPI for weather data ingestion and retrieval.
- **Automated ETL**: Fetches and stores live weather data every 5 minutes.
- **Secure API Keys**: Managed via `.env` to protect sensitive credentials.
- **MongoDB Integration** for storing structured weather data.
- **Version Control** with Git and GitHub for collaborative development.

---

## 🛠 Tech Stack
- **Programming Language**: Python 3.x
- **Framework**: FastAPI
- **Database**: MongoDB
- **Scheduler**: APScheduler
- **API Provider**: OpenWeatherMap API
- **Version Control**: Git & GitHub

---

## 📂 Project Structure
weather-logger-api/
│
├── app/
│ ├── main.py # FastAPI entry point
│ ├── database.py # MongoDB connection
│ ├── scheduler.py # APScheduler setup
│ ├── utils.py # Helper functions
│
├── requirements.txt # Dependencies
├── .env.example # Environment variables template
├── README.md # Project documentation
|



