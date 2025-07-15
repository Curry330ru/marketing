from fpdf import FPDF
from pathlib import Path


def create_report(text: str, path: Path) -> bool:
    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        for line in text.splitlines():
            pdf.cell(200, 10, txt=line, ln=1)
        pdf.output(str(path))
        return True
    except Exception:
        return False
