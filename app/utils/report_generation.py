from fpdf import FPDF

class PDFReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Stock Market Analysis Report', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, title, 0, 1, 'L')
        self.ln(10)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

def generate_report(symbol, start_date, end_date):
    pdf = PDFReport()
    pdf.add_page()

    pdf.chapter_title('Stock Symbol: ' + symbol)
    pdf.chapter_body(f'Analysis Period: {start_date} to {end_date}')

    # Placeholder for more detailed analysis content
    pdf.chapter_body('Detailed analysis content goes here...')

    pdf_output = f'report_{symbol}_{start_date}_{end_date}.pdf'
    pdf.output(pdf_output)

    return pdf_output
