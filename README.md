# Diabetes Tracker CLI

A simple command-line tool to log and visualize blood sugar and insulin data.

## Features

- Log blood sugar values with optional notes
- Log insulin doses (bolus/basal) with optional notes
- View all logs in a formatted table
- View statistics (average, highest, lowest blood sugar)
- Plot blood sugar or insulin data as ASCII graphs directly in the terminal

## Requirements

- Python 3.7+
- Install dependencies with:
  ```sh
  pip install -r requirements.txt
  ```

## Installation and Usage

### 1. Clone the Repository

```sh
git clone https://github.com/aimabe/diabetes_tracker.git
cd diabetes_tracker
```

### 2. Create and Activate a Virtual Environment

```sh
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```sh
pip install -r requirements.txt
```

**OR install as a package using `setup.py`:**

```sh
pip install .
```

This will install the app and its dependencies. You can then run the CLI using:

```sh
diabetes-tracker
```

### 4. Run the Application

#### Interactive Menu

```sh
python3 main.py
```
or, if installed as a package:
```sh
diabetes-tracker
```
Follow the prompts to log blood sugar, log insulin, view stats, or plot graphs.

#### Command Line Usage

- **Log blood sugar:**
  ```sh
  python3 main.py blood-sugar --value 120 --time 08:30 --note "Fasting"
  # or
  diabetes-tracker blood-sugar --value 120 --time 08:30 --note "Fasting"
  ```

- **Log insulin:**
  ```sh
  python3 main.py insulin --kind bolus --amount 5 --time 12:00 --note "Lunch"
  # or
  diabetes-tracker insulin --kind bolus --amount 5 --time 12:00 --note "Lunch"
  ```

- **Show all logs:**
  ```sh
  python3 main.py stats
  # or
  diabetes-tracker stats
  ```

- **Show a graph:**
  ```sh
  python3 main.py graph --type blood_sugar
  python3 main.py graph --type insulin
  # or
  diabetes-tracker graph --type blood_sugar
  diabetes-tracker graph --type insulin
  ```

### 5. Data Storage

All logs are saved in `storage.csv` in the project directory.

---

**Tip:**  
Make sure your virtual environment is activated each time you run the application or install new dependencies.

## Example Output

### Table View

```
| Date       | Type        | Kind  | Value | Time  | Note     |
|------------|-------------|-------|-------|-------|----------|
| 2025-07-25 | blood_sugar |       | 120   | 08:30 | Fasting  |
| 2025-07-25 | insulin     | bolus | 5     | 12:00 | Lunch    |
```

### Graph View

When you run a graph command, an ASCII graph will be displayed directly in your terminal using `plotext`.

---

## Notes

- Make sure your virtual environment is activated before installing requirements or running the program.
- All logs are appended to `storage.csv`.
- For best results, use a terminal window wide enough to display the ASCII graphs.

---

## Future Addition:

- Log Meals
- Log Activity
- Adding Unit tests
- Add exporting
- Add printing
- Add filtering of data by date, type
- Advanced Analytics
  - Mean Glucose Value
  - Percentage time spent in 
      - hypoglycemia (BG < 70 mg/dL)
      - target range ( 70 < BG < 180)
      - hyperglycemia (BG > 180)
  - Statistical Analysis
    - Time-based patterns (time of day with highest/lowest readings)
    - Correlation between insulin doses and subsequent blood sugar readings
    - Day-of-week analysis to identify weekend vs weekday patterns
    - Standard deviation and variability metrics for glucose control assessment
    - Moving averages to show trends over different timeframes (7-day, 14-day, 30-day)
  - Predictive Features
    - Glucose prediction based on meal content, insulin timing, and historical patterns
    - Insulin sensitivity factor calculations
    - Carb ratio effectiveness analysis
  - Reporting
    - Time in range calculations (% of readings within target glucose range)
    - A1C estimations based on average glucose readings
    - Exportable reports for healthcare provider appointments
    - Monthly/quarterly summary statistics
  - Advanced Visualizations
    - Heatmaps showing glucose patterns by time of day and day of week
    - Overlay graphs of insulin doses with blood glucose responses
    - Box and whisker plots to show glucose variability by time period
    - Ambulatory glucose profile (AGP) style reports
- Pull in data from Continuous Glucose Monitor (CGM)
  - Process CGM data
- Move from using CSV to a database (SQLite or PostgreSQL)
- Transitioning to a Web App
    - Choose a Web Framework (Flask or Django)
    - Convert CLI to Web Routes
        - Routes for logging blood sugar, viewing stats, and plotting graphs.
    - Frontend (UI/UX)
    - HTML + CSS: Simple static pages
    - JavaScript: Add interactivity
    - Use a charting library (like Chart.js or Plotly) to render the blood sugar graph dynamically
- Hosting
