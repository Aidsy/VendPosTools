import csv

#Get items from "codes.csv" and convert to a Python dictonary
#File should have first column as item name, second as barcode number
reader = csv.reader(open("codes.csv", "rb"))
code_dict = {k: v for k, v in reader}

from reportlab.graphics.barcode import code39
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas


x= 1 * mm
y = 20 * mm


for code in code_dict:
    c = canvas.Canvas(code + ".pdf",pagesize=(80*mm,y))
    barcode = code39.Extended39(code,barWidth=x,barHeight=y)
    barcode.drawOn(c,-9,0)
    c.showPage()
    c.save()


