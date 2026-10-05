import os
import random
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes

FACTS = [
    "⚽ The first FIFA World Cup was held in Uruguay in 1930.",
    "🏀 Basketball was invented by James Naismith in 1891.",
    "🎾 Wimbledon is the oldest tennis tournament in the world, first held in 1877.",
    "🏃 The marathon distance is officially 42.195 kilometres.",
    "🏊 Michael Phelps won 28 Olympic medals, including 23 gold medals.",
    "⚽ Brazil has won the FIFA World Cup more times than any other men's national team.",
    "🏀 The NBA was founded in 1946 as the Basketball Association of America before becoming the NBA in 1949.",
    "🎾 The four Grand Slam tennis tournaments are the Australian Open, French Open, Wimbledon, and US Open.",
    "🏎️ Formula 1's first World Championship race was held at Silverstone in 1950.",
    "🥊 Boxing was included in the ancient Olympic Games.",
    "🏉 Rugby is named after Rugby School in Warwickshire, England.",
    "🏏 A standard cricket team has 11 players.",
    "⚽ A standard football match is played with two 45-minute halves, subject to added time.",
    "🏀 The original basketball game used a peach basket as the goal.",
    "🎾 The term 'love' is traditionally used for a score of zero in tennis.",
    "🏅 The modern Olympic Games began in Athens in 1896.",
    "⛳ A standard round of golf consists of 18 holes.",
    "🏐 Volleyball was originally called 'mintonette' when it was invented in 1895.",
    "⚽ The word 'soccer' originated as an abbreviation of 'association football'.",
    "🏓 Table tennis was developed in England as an indoor version of lawn tennis.",
]

def keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🧠 Sports Fact", callback_data="fact")],
        [InlineKeyboardButton("🔄 Another Fact", callback_data="fact")],
    ])

def fact_message():
    return f"🧠 <b>Sports Fact</b>\n\n{random.choice(FACTS)}"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🏟️ <b>SB Sports Facts</b>\n\n"
        "Discover interesting facts from the world of sports.\n\n"
        "No scores. No betting. Just sports facts.\n\n"
        "Tap below to get started."
    )
    await update.message.reply_text(text, parse_mode="HTML", reply_markup=keyboard())

async def fact(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    await update.callback_query.edit_message_text(
        fact_message(), parse_mode="HTML", reply_markup=keyboard()
    )

def main():
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        raise RuntimeError("TELEGRAM_BOT_TOKEN is not set.")

    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(fact, pattern="^fact$"))
    app.run_polling()

if __name__ == "__main__":
    main()
