import os
from reportlab.pdfgen import canvas
from telegram import Update
import uuid
async def texttoPdf(update:Update,context):
    text=update.message.text
    Username=update.message.from_user.full_name
    file_Name=Username+uuid.uuid4().hex[:8]
    c=canvas.Canvas(file_Name)
    c.setFontSize(14)
    y=800
    for line in text.split('\n'):
        c.drawString(40,y,line)
        y-=20
        if y<40:
            c.showPage()
            y=800
    c.save()
    with open(file_Name,'rb') as pdf:
       await update.message.reply_document(document=pdf)
    await os.remove(file_Name)    
