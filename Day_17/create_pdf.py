from fpdf import FPDF


pdfFile = FPDF()

pdfFile.add_page()
 
pdfFile.set_font("Arial", size = 12)

pdfFile.cell(20, 10, txt = "Report text", ln = 2, align = 'C')

pdfFile.image('histogram.png', 10, 40, 30)

pdfFile.output("report.pdf") 
