from reportlab.graphics.barcode import code39
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
import csv

c = canvas.Canvas("barcode_example.pdf", pagesize=A4)

code_list = 

x = 1 * mm
y = 285 * mm
x1 = 6.4 * mm

for code in code_list:
    barcode = code39.Extended39(code)
    barcode.drawOn(c, x, y)
    x1 = x + 6.4 * mm
    y = y - 5 * mm
    c.drawString(x1, y, code)
    x = x
    y = y - 10 * mm

    if int(y) == 0:
        x = x + 50 * mm
        y = 285 * mm

c.showPage()
c.save()
