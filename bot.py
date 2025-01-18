import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from groq import Groq

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
        


app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("tanya", tanya))

app.run_polling()
