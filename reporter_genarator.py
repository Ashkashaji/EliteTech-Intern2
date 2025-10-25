
from fpdf import FPDF
import pandas as pd

data = pd.read_csv('data.csv')
pdf = FPDF()
pdf.add_page()


pdf.set_font("Arial", 'B', 16)
pdf.cell(0, 10, "Employee Score Report", 0, 1,"c")
avg_score = data['Score'].mean()
pdf.set_font("Arial", '', 12)
pdf.cell(0, 10, f"Average Score: {avg_score:.2f}", 0, 1)

pdf.set_font("Arial", 'B', 12)
pdf.cell(60, 10, "Name", 1)
pdf.cell(60, 10, "Department", 1)
pdf.cell(60, 10, "Score", 1)
pdf.ln()


pdf.set_font("Arial", '', 12)
for _, row in data.iterrows():
    pdf.cell(60, 10, str(row["Name"]), 1)
    pdf.cell(60, 10, str(row["Department"]), 1)
    pdf.cell(60, 10, str(row["Score"]), 1)
    pdf.ln()

pdf.output("sample_report.pdf")
print("PDF generated successfully!")
