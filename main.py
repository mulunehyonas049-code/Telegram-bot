import logging
from telegram import Update, ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    MessageHandler,
    filters,
    ConversationHandler,
)

FULL_NAME, PHONE, AGE, LOCATION, EDUCATION, GENDER, PAYMENT_SCREENSHOT = range(7)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "ሰላም! ወደ ዩኒሴፍ ምዝገባ ቦት እንኳን ደህና መጡ።\n"
        "እባክዎን ሙሉ ስምዎን ይጻፉልን:",
        reply_markup=ReplyKeyboardRemove()
    )
    return FULL_NAME

async def get_full_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['full_name'] = update.message.text
    await update.message.reply_text("አመሰግናለን። አሁን ደግሞ ስልክ ቁጥርዎን ይጻፉልን (ለምሳሌ: 09...):")
    return PHONE

async def get_phone(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['phone'] = update.message.text
    await update.message.reply_text("እባክዎን ዕድሜዎን ቁጥር ብቻ ይጻፉ:")
    return AGE

async def get_age(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['age'] = update.message.text
    await update.message.reply_text("አሁን ያሉበትን አካባቢ (ከተማ/ክልል) ይጻፉ:")
    return LOCATION

async def get_location(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['location'] = update.message.text
    await update.message.reply_text("የእርስዎ የትምህርት ደረጃ ምን ይመስላል? (ለምሳሌ፦ ዲግሪ፣ ዲፕሎማ፣ 2ኛ ደረጃ...)")
    return EDUCATION

async def get_education(update: Update, context: ContextTypes.DEFAULT_TYPE):
    context.user_data['education'] = update.message.text
    
    reply_keyboard = [['ወንድ', 'ሴት']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True, resize_keyboard=True)
    
    await update.message.reply_text("እባክዎን ጾታዎን ይምረጡ:", reply
