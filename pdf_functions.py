import reportlab
from reportlab.pdfgen import canvas


def create_pdf(path: str, image_path: str ="images\\image_1712159976.png" ):
    new_pdf = canvas.Canvas("text.pdf")


    new_pdf.drawString(250,500, "Imagine aici")
    new_pdf.drawImage(image_path, x=250, y=300)
    new_pdf.save()