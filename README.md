# 🐍 Project 01: Student Grade Average Calculator (Python Fundamentals)

This project marks the successful completion of my initial phase of studying Programming Logic and Core Data Structures in Python. It simulates a system for collecting student grades, calculating the final average, and determining the pass/fail status.

## 🎯 Objective

To consolidate the use of **control flow** and **basic data structures** in a single, functional script.

## ✨ Key Features

* Dynamic grade collection: The program continues to collect grades until the user inputs "FIM" (End).
* Zero Division Protection: Includes a check to prevent calculation errors if no grades are entered.
* Final Grade Calculation.
* Determines Student Status: Approved (>= 7.0), Remedial (>= 5.0), Failed (< 5.0).

## 🛠️ Technologies Used

| Concept | Application in Code |
| :--- | :--- |
| **Repetition Logic** | `while True` for data collection and `break` for controlled exit. |
| **Data Structures** | `Lists` (`notas`) to store grade collections. |
| **Calculations** | `float()` for input conversion; `len()` to get the total number of grades. |
| **Control Flow** | `if/elif/else` to classify the student's final status. |

## 💻 How to Run

1.  Clone this repository.
2.  Execute the `calculadora_media.py` file in your terminal.

```bash
python calculadora_media.py
