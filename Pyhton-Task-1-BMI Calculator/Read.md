# BMI Calculator — Internship Project

## 📌 Project Overview

The **BMI Calculator** is a Python-based application developed as part of my internship project. It calculates a user's **Body Mass Index (BMI)** from their weight and height and classifies the result into standard BMI categories.

The project can be implemented in two levels:

* **Beginner Tier:** Command-line BMI calculator using Python.
* **Advanced Tier:** Graphical BMI application using `tkinter`, SQLite/CSV storage, and `matplotlib` for BMI trend visualization.

---

## 🎯 Objective

The main objective of this project is to develop a simple and user-friendly application that:

* Accepts the user's weight and height.
* Calculates BMI using the standard formula.
* Classifies BMI into appropriate categories.
* Validates user input.
* Stores BMI records for future reference in the advanced version.
* Displays BMI trends over time.

---

## 🛠️ Technologies Used

### Beginner Version

* Python
* `input()`
* Basic arithmetic
* Conditional statements
* Exception handling

### Advanced Version

* Python
* `tkinter` — GUI development
* `sqlite3` — database storage
* `matplotlib` — BMI trend visualization
* CSV — optional data storage

---

## 📐 BMI Formula

The BMI is calculated using:

```text
BMI = weight / (height²)
```

Where:

* **Weight** is measured in kilograms (kg).
* **Height** is measured in meters (m).

Example:

```text
Weight = 60 kg
Height = 1.65 m

BMI = 60 / (1.65 × 1.65)
BMI = 22.04
```

---

## 📊 BMI Classification

| BMI Range      | Category    |
| -------------- | ----------- |
| Below 18.5     | Underweight |
| 18.5 – 24.9    | Normal      |
| 25.0 – 29.9    | Overweight  |
| 30.0 and above | Obese       |

---

## ✅ Beginner Features

* [ ] Enter weight in kilograms.
* [ ] Enter height in meters.
* [ ] Calculate BMI automatically.
* [ ] Display BMI rounded to two decimal places.
* [ ] Display the BMI category.
* [ ] Reject non-numeric input.
* [ ] Reject zero or negative values.
* [ ] Display helpful error messages.

---

## 🖥️ Advanced Features

* [ ] GUI application using `tkinter`.
* [ ] Input fields for user name, weight, and height.
* [ ] Calculate button for BMI calculation.
* [ ] Color-coded BMI result.
* [ ] Support for multiple users.
* [ ] Save BMI records in SQLite or CSV.
* [ ] View historical BMI records.
* [ ] Display BMI trend using a line chart.
* [ ] Handle database read/write errors gracefully.

---

## 📁 Suggested Project Structure

```text
BMI-Calculator/
│
├── bmi_calculator.py
├── bmi_gui.py
├── database.py
├── bmi_history.db
├── requirements.txt
└── README.md
```

For the beginner version, the main file can simply be:

```text
bmi_calculator.py
```

---

## 🚀 How to Run

### 1. Install Python

Make sure Python is installed on your computer.

Check the installation using:

```bash
python --version
```

### 2. Clone or Download the Project

Download the project files and open the project folder in **VS Code**, **IDLE**, or another Python editor.

### 3. Run the Beginner Version

Open a terminal in the project folder and run:

```bash
python bmi_calculator.py
```

### 4. Run the Advanced Version

Run:

```bash
python bmi_gui.py
```

---

## 🧪 Example Output

### Command-Line Version

```text
BMI Calculator
--------------

Enter your weight in kg: 60
Enter your height in meters: 1.65

Your BMI is: 22.04
Category: Normal
```

### Invalid Input

```text
Enter your weight in kg: abc

Error: Please enter a valid number for weight.
```

```text
Enter your height in meters: -1.5

Error: Weight and height must be greater than zero.
```

---

## 🗄️ Data Storage

The advanced version can store BMI records using **SQLite**.

A record may contain:

```text
User Name
Weight
Height
BMI
Category
Date and Time
```

This allows users to review previous BMI measurements and monitor changes over time.

---

## 📈 BMI Trend Visualization

The advanced application uses `matplotlib` to create a line graph showing a user's BMI over time.

Example:

```text
BMI
│
│        ●
│      ●   ●
│   ●
│ ●
└────────────────── Date
```

This makes it easier for users to understand changes in their BMI.

---

## 🔐 Input Validation and Error Handling

The application checks user input before performing calculations.

Examples of invalid input include:

* Empty input
* Text instead of numbers
* Negative weight
* Negative height
* Zero height
* Invalid database operations

Helpful error messages are displayed instead of allowing the application to crash.

---

## 📚 Learning Outcomes

Through this project, I gained practical experience in:

* Python programming fundamentals
* Variables and data types
* User input handling
* Arithmetic operations
* Conditional statements
* Exception handling
* GUI development with `tkinter`
* Database operations with SQLite
* Data visualization with `matplotlib`
* File and project organization
* Building a practical Python application

---

## 🔮 Future Enhancements

Possible future improvements include:

* User login and authentication
* Cloud-based data storage
* Mobile-friendly interface
* PDF BMI reports
* Personalized health recommendations
* Multiple measurement units
* Improved charts and dashboards

---

## 📖 References

The project was developed using Python documentation and tutorial resources, including:

* Python Documentation: https://docs.python.org/
* Tkinter Documentation: https://docs.python.org/3/library/tkinter.html
* SQLite Documentation: https://docs.python.org/3/library/sqlite3.html
* Matplotlib Documentation: https://matplotlib.org/

---

## 👨‍💻 Internship Project

**Project Name:** BMI Calculator
**Task:** Task 1
**Programming Language:** Python
**Project Level:** Beginner / Advanced
**Purpose:** Internship Training Project

---

## ⭐ Conclusion

The BMI Calculator demonstrates how Python can be used to build a practical application from basic calculations to a complete graphical system with **database storage and data visualization**. The project provides hands-on experience with Python programming and demonstrates the development of a real-world application from a simple command-line program to an advanced GUI-based solution.
