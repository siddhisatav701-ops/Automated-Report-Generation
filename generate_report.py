import pandas as pd
from fpdf import FPDF
from datetime import datetime


INPUT_FILE = "data.csv"        # change filename if needed
OUTPUT_PDF = "report.pdf"      # generated report


def load_data(path: str) -> pd.DataFrame:
    """Read CSV data into a DataFrame."""
    df = pd.read_csv(path)
    return df


def analyze_data(df: pd.DataFrame) -> dict:
    """Return basic statistics and insights for the report."""
    summary = {}

    summary["row_count"] = len(df)
    summary["columns"] = list(df.columns)

    numeric_df = df.select_dtypes(include="number")

    summary["describe"] = numeric_df.describe().round(2)

    # Example: per‑city mean temperature and humidity (if columns exist)
    if {"City", "Temperature"}.issubset(df.columns):
        summary["mean_temp_by_city"] = (
            df.groupby("City")["Temperature"].mean().round(2).sort_values(ascending=False)
        )
    else:
        summary["mean_temp_by_city"] = None

    return summary


class ReportPDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 16)
        self.cell(0, 10, "Data Analysis Report", ln=1, align="C")
        self.set_font("Helvetica", "", 10)
        self.cell(0, 6, f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
                  ln=1, align="C")
        self.ln(4)
        self.line(10, self.get_y(), 200, self.get_y())
        self.ln(4)

    def footer(self):
        self.set_y(-15)
        self.set_font("Helvetica", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")


def add_section_title(pdf: ReportPDF, title: str):
    pdf.set_font("Helvetica", "B", 13)
    pdf.ln(4)
    pdf.cell(0, 8, title, ln=1)
    pdf.set_font("Helvetica", "", 11)


def add_paragraph(pdf: ReportPDF, text: str):
    pdf.set_font("Helvetica", "", 11)
    pdf.multi_cell(0, 6, text)
    pdf.ln(1)


def dataframe_to_table(pdf: ReportPDF, df: pd.DataFrame, col_widths=None):
    pdf.set_font("Helvetica", "B", 10)
    if col_widths is None:
        # simple equal‑width columns
        col_width = pdf.w / (len(df.columns) + 1)
        col_widths = [col_width] * len(df.columns)

    # header
    for w, col in zip(col_widths, df.columns):
        pdf.cell(w, 8, str(col), border=1, align="C")
    pdf.ln(8)

    # rows
    pdf.set_font("Helvetica", "", 10)
    for _, row in df.iterrows():
        for w, item in zip(col_widths, row):
            pdf.cell(w, 8, str(item), border=1, align="C")
        pdf.ln(8)


def series_to_table(pdf: ReportPDF, series: pd.Series, col1="Label", col2="Value"):
    pdf.set_font("Helvetica", "B", 10)
    pdf.cell(80, 8, col1, border=1, align="C")
    pdf.cell(40, 8, col2, border=1, align="C")
    pdf.ln(8)

    pdf.set_font("Helvetica", "", 10)
    for idx, val in series.items():
        pdf.cell(80, 8, str(idx), border=1)
        pdf.cell(40, 8, str(val), border=1, align="C")
        pdf.ln(8)


def build_pdf_report(df: pd.DataFrame, summary: dict, output_path: str):
    pdf = ReportPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Section 1 – Overview
    add_section_title(pdf, "1. Dataset Overview")
    overview_text = (
        f"The input file contains {summary['row_count']} rows and "
        f"{len(summary['columns'])} columns.\n\n"
        f"Columns: {', '.join(summary['columns'])}."
    )
    add_paragraph(pdf, overview_text)

    # Section 2 – Descriptive statistics
    add_section_title(pdf, "2. Descriptive Statistics")
    stats_df = summary["describe"].reset_index().rename(columns={"index": "Metric"})
    dataframe_to_table(pdf, stats_df)

    # Section 3 – Mean temperature by city (if available)
    if summary["mean_temp_by_city"] is not None:
        pdf.add_page()
        add_section_title(pdf, "3. Mean Temperature by City")
        add_paragraph(
            pdf,
            "The following table shows the average temperature for each city "
            "in the dataset (sorted from highest to lowest).",
        )
        series_to_table(pdf, summary["mean_temp_by_city"],
                        col1="City", col2="Mean Temperature")

    # Section 4 – Notes
    pdf.add_page()
    add_section_title(pdf, "4. Notes")
    add_paragraph(
        pdf,
        "This report was generated automatically using a Python script. "
        "The analysis can be extended with additional metrics, charts, or "
        "domain-specific insights as required."
    )

    pdf.output(output_path)


def main():
    df = load_data(INPUT_FILE)
    summary = analyze_data(df)
    build_pdf_report(df, summary, OUTPUT_PDF)
    print(f"Report generated: {OUTPUT_PDF}")


if __name__ == "__main__":
    main()
