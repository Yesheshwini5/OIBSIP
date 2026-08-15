# 🌦️ Basic Weather App

A Python-based **Weather Application** that fetches real-time weather information for a user-specified city using the **OpenWeatherMap API**.

This project was developed as part of my **Python Internship** to demonstrate API integration, JSON data handling, user input validation, error handling, and Python programming fundamentals.

---

## 📌 Project Overview

The Basic Weather App allows users to enter a city name and retrieve its current weather information.

The application connects to the **OpenWeatherMap API**, receives weather data in JSON format, processes the response, and displays useful information such as:

* 🌡️ Temperature in Celsius and Fahrenheit
* 💧 Humidity percentage
* ☁️ Weather condition
* 💨 Wind speed
* 📍 City and country information

The application also handles common errors such as invalid city names, network problems, empty input, and invalid API keys.

---

## 🎯 Objectives

The main objectives of this project are:

1. Learn how to work with APIs in Python.
2. Fetch real-time weather data from an external service.
3. Understand and process JSON responses.
4. Use the `requests` library for HTTP requests.
5. Validate user input.
6. Handle API and network errors gracefully.
7. Display weather information in an easy-to-understand format.

---

## 🛠️ Technologies Used

| Technology         | Purpose                          |
| ------------------ | -------------------------------- |
| Python             | Main programming language        |
| Requests           | Sending API requests             |
| JSON               | Processing API response data     |
| OpenWeatherMap API | Providing real-time weather data |

---

## ✨ Features

### Beginner Version

* [ ] Enter a city name or ZIP code
* [ ] Fetch real-time weather information
* [ ] Display temperature in °C
* [ ] Display temperature in °F
* [ ] Display humidity
* [ ] Display weather condition
* [ ] Display wind speed
* [ ] Validate empty input
* [ ] Handle city-not-found errors
* [ ] Handle invalid API key errors
* [ ] Handle network/timeout errors

### Advanced Version

* [ ] Graphical User Interface using Tkinter
* [ ] City input field
* [ ] "Get Weather" button
* [ ] Weather results panel
* [ ] Weather icons
* [ ] Hourly forecast
* [ ] Five-day forecast
* [ ] Celsius/Fahrenheit unit toggle
* [ ] Automatic location detection
* [ ] GUI-based error messages

---

## 📂 Project Structure

```text
Basic-Weather-App/
│
├── weather_app.py
├── README.md
└── requirements.txt
```

---

## 🔑 OpenWeatherMap API Setup

This project uses the OpenWeatherMap API.

### Step 1: Create an Account

Create a free account on OpenWeatherMap and generate an API key.

Official website:

https://openweathermap.org/

### Step 2: Get Your API Key

After creating an account:

1. Log in to OpenWeatherMap.
2. Open your API Keys section.
3. Generate/copy your API key.
4. Add the key to your Python program.

**Important:** Do not upload your private API key to GitHub.

A safer approach is to store it in an environment variable.

---

## 📦 Installation

Make sure Python is installed on your computer.

Check your Python installation:

```bash
python --version
```

Install the required library:

```bash
pip install requests
```

---

## 🚀 How to Run the Project

Open Command Prompt or Terminal and navigate to the project folder.

For example:

```bash
cd path\to\Basic-Weather-App
```

Then run:

```bash
python weather_app.py
```

The program will ask you to enter a city name.

Example:

```text
Enter city name: Hyderabad
```

The application will then display the current weather information.

---

## 💻 Example Output

```text
========================================
        BASIC WEATHER APP
========================================

Enter city name: Hyderabad

Weather Information
----------------------------------------
City        : Hyderabad
Country     : IN
Temperature : 28.5 °C
Temperature : 83.3 °F
Humidity    : 65%
Condition   : Clear sky
Wind Speed  : 3.5 m/s
----------------------------------------
```

---

## 🌡️ Temperature Conversion

The application displays temperature in both Celsius and Fahrenheit.

The Fahrenheit conversion formula is:

```text
°F = (°C × 9/5) + 32
```

For example:

```text
28°C = 82.4°F
```

---

## 🌐 API Workflow

The application follows these steps:

```text
User enters city
       ↓
Validate input
       ↓
Send request to OpenWeatherMap API
       ↓
Receive JSON response
       ↓
Check API response
       ↓
Extract weather information
       ↓
Convert temperature
       ↓
Display results
```

---

## ⚠️ Error Handling

The application handles several possible errors.

### Empty City

If the user does not enter a city:

```text
Error: City name cannot be empty.
```

### City Not Found

If the entered city does not exist:

```text
Error: City not found. Please check the city name.
```

### Invalid API Key

If the API key is incorrect:

```text
Error: Invalid API key.
```

### Network Error

If there is no internet connection or the API cannot be reached:

```text
Error: Unable to connect to the weather service.
```

### Request Timeout

If the server takes too long to respond:

```text
Error: Request timed out. Please try again.
```

---

## 📚 What I Learned

Through this project, I learned:

* Python API integration
* HTTP requests
* JSON data processing
* Exception handling
* Input validation
* Temperature conversion
* Working with external APIs
* Basic project organization
* Command-line application development

---

## 🔮 Future Enhancements

The project can be improved by adding:

* 🌤️ Graphical user interface using Tkinter
* 🕐 Hourly weather forecast
* 📅 Five-day weather forecast
* 🖼️ Weather condition icons
* 🌡️ Celsius/Fahrenheit toggle
* 📍 Automatic location detection
* 🔍 Search history
* 📊 Weather charts
* 🌙 Dark mode
* 📱 Responsive interface

---

## 🏆 Internship Project

**Project:** Basic Weather App
**Domain:** Python Development
**Level:** Beginner / Intermediate
**API:** OpenWeatherMap
**Language:** Python

This project demonstrates my understanding of Python programming and my ability to integrate an external API into a working application.

---

## 👩‍💻 Author

**P. Yesheshwini**

Python Internship Project – 2026

---

## 📄 License

This project is created for educational and internship purposes.
