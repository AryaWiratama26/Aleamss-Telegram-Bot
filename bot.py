import os
from dotenv import load_dotenv
from telegram import Update, BotCommand
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from groq import Groq
from db import create_db, add_data, koneksi, read, all

# Load token
load_dotenv()
BOT_TOKEN = os.getenv('BOT_TOKEN')
GROQ_TOKEN = os.getenv('GROQ_TOKEN')

# Groq
client = Groq(api_key=GROQ_TOKEN)

# Fungsii hello
async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) :
    await update.message.reply_text(f'Hello {update.effective_user.first_name}, apa yang bisa saya bantu?')
    
async def tanya(update: Update, context: ContextTypes.DEFAULT_TYPE) :
    ask = context.args
    final_questions = " ".join(ask)
    
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role" : "user",
                "content" : final_questions},
            ],
            model="llama-3.3-70b-versatile",
            stream=False
            
        ) 
        final_answers = chat_completion.choices[0].message.content
        await update.message.reply_text("Jawaban anda sedang diproses!")
        if final_answers:
            await update.message.reply_text(f"Jawaban : \n{final_answers}")
        else:
            await update.message.reply_text("Saya tidak dapat memproses")
    except ValueError:
        await update.message.reply_text("Saya tidak mengerti")

# Fungsi Tambah Note
async def note(update: Update, context: ContextTypes.DEFAULT_TYPE):
    note = context.args
    judul = note[0].strip()
    notes = note[1].strip()
    waktu = note[2].strip()
    
    koneksi()
    create_db()
    add_data(judul, notes, waktu)
    
    await update.message.reply_text(f"""
    Catatan Anda : 
    📝 *Judul:* {judul}
    📌 *Catatan:* {notes}
    ⏰ *Waktu:* {waktu}
    
    Data berhasil disimpan""", parse_mode="MarkDown")
 
# Fungsi Baca Note   
async def readNote(update: Update, context: ContextTypes.DEFAULT_TYPE):
    judul = context.args
    finals = "".join(judul).strip()
    await update.message.reply_text(read(finals))
    
async def listDB(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(all())
    
async def help(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("""
/hello untuk menyapa bot
/tanya bertanya kepada AI
/note untuk membuat note dengan format <Judul> <Isi-notes> <Tahun> contoh = (Upacara Mengibarkan-bendera 2024-02-02)
/read membaca note berdasarkan judul""")
    

app = ApplicationBuilder().token(BOT_TOKEN).build()


app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("tanya", tanya))
app.add_handler(CommandHandler("note", note))
app.add_handler(CommandHandler("read", readNote))
app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("list", listDB))



app.run_polling()
