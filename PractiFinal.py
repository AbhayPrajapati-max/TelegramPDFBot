from telegram import Update
from telegram.ext import MessageHandler,CommandHandler,filters,Application
from PractiDocxToPDF import DocxToPdf
from PractiTextToPDF import texttoPdf
async def start(update:Update,context):
    await update.message.reply_text('Welcome PDF maker bot'
    'Send me Text Messege Or Docx file I will convert into Pdf')
Token=''
Mybot=Application.builder().token(Token).build()

Mybot.add_handler(CommandHandler('start',start))
Mybot.add_handler(MessageHandler(filters.TEXT&~filters.COMMAND,texttoPdf))
Mybot.add_handler(MessageHandler(filters.Document.FileExtension('docx'),DocxToPdf))

print('Making PDF')
Mybot.run_polling()
