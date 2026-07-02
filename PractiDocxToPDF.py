import os 
from docx2pdf import convert
from telegram import Update
import uuid
async def DocxToPdf(update:Update,context):
    document=update.message.document
    #user_name=update.message.from_user.full_name
    Docx_Linl=await document.get_file()
    name=update.message.document.file_name
    file_name=f'{name[:5]+uuid.uuid4().hex[:8]}.docx'
    await Docx_Linl.download_to_drive(file_name)
    print(file_name)
    output_Pdf=file_name.replace('.docx','.pdf')
    try:
        convert(file_name,output_Pdf)
        with open(output_Pdf,'rb') as pdf:
           await update.message.reply_document(document=pdf)
    finally:
       print('file deleting\n')
       if os.path.exists(file_name):
          os.remove(file_name)
          print('First Deleted\n')
       if os.path.exists(output_Pdf):
          os.remove(output_Pdf)
          print('deleted\n')
    