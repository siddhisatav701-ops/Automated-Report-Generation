# Automated-Report-Generation

COMPANY: CODTECH IT SOLUTIONS

NAME: SIDDHI TANAJI SATAV

INTERN ID: CTIS0158

DOMAIN: Python Programming

DURATION: 4 WEEEKS

MENTOR: NEELA SANTOSH

Internship Project Submission

CODTECH Internship – Task 2
Title: File Data Analysis and PDF Report Generation in Python

1. Objective
Develop a Python script that reads data from a file, analyzes it using pandas, and generates a formatted PDF report using a PDF library (fpdf2). The deliverables are the script and a sample PDF report.

2. Tech Stack
Language: Python 3
Libraries:
pandas – load and analyze tabular data
fpdf2 – create and format PDF documents programmatically
Install dependencies:
bash
pip install pandas fpdf2

3. Input Data
The script expects a CSV file named data.csv in the same folder.
Example structure (city‑wise weather or any numeric dataset):
text
City,Temperature,Humidity
Delhi,25,60
Mumbai,30,70
Bangalore,22,65
Chennai,29,68
Kolkata,27,72
Pune,24,55
Solapur,26,50
You can replace this with any dataset; the script reads it using pandas.read_csv() and computes basic statistics.

4. Script Overview (generate_report.py)
4.1. Data Loading
python
df = pd.read_csv("data.csv")
Reads the CSV into a DataFrame.
Supports any numeric columns for summary statistics.
4.2. Analysis
The script:
Counts rows and columns.
Lists all column names.
Selects numeric columns and computes descriptive statistics using DataFrame.describe() (count, mean, std, min, quartiles, max).
If City and Temperature exist, calculates mean temperature per city with groupby().
4.3. PDF Report Generation
Using a custom ReportPDF class (subclass of FPDF), the script builds a multi‑section PDF:
Header & Footer
Title: “Data Analysis Report”.
Timestamp of generation.
Page number in the footer.
Section 1 – Dataset Overview
Number of rows and columns.
List of all columns.
Section 2 – Descriptive Statistics
Table of metrics (count, mean, min, max, etc.) for numeric columns.
Section 3 – Mean Temperature by City (optional)
Table of average temperature per city, sorted from highest to lowest, if relevant columns exist.
Section 4 – Notes
Short paragraph explaining that the report was auto‑generated and can be extended with more metrics.
Tables are drawn using helper functions that loop through DataFrame/Series rows and render them as PDF table cells.
4.4. Output
The final PDF is saved as:
python
OUTPUT_PDF = "report.pdf"
After running, you will see report.pdf in the same folder, ready to open and share.

5. How to Run
From the project folder containing generate_report.py and data.csv:
bash
python generate_report.py
Expected console message:
text
Report generated: report.pdf
Open report.pdf to view:
Overview of the dataset.
Descriptive statistics table.
Optional per‑city summary.
Notes section.

Output

<img width="794" height="577" alt="image" src="https://github.com/user-attachments/assets/e30c1347-8b43-4081-a0ca-c04167889fab" />
<img width="791" height="561" alt="image" src="https://github.com/user-attachments/assets/2be69302-8b0d-4ec5-b80d-ddcf536bdcab" />
<img width="791" height="540" alt="image" src="https://github.com/user-attachments/assets/b8f773d3-ceb8-4f55-8a0d-672d5efc7e3a" />


