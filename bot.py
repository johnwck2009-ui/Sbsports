import os
import random
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes

FACTS = [
    "⚽ ព្រឹត្តិការណ៍ FIFA World Cup លើកដំបូងបានធ្វើឡើងនៅប្រទេសអ៊ុយរូហ្គាយក្នុងឆ្នាំ 1930។",
    "🏀 កីឡាបាល់បោះត្រូវបានបង្កើតឡើងដោយ James Naismith ក្នុងឆ្នាំ 1891។",
    "🎾 Wimbledon គឺជាការប្រកួតកីឡាវាយកូនបាល់ចាស់ជាងគេបំផុតក្នុងពិភពលោក ដែលចាប់ផ្តើមនៅឆ្នាំ 1877។",
    "🏃 ចម្ងាយម៉ារ៉ាតុងផ្លូវការគឺ 42.195 គីឡូម៉ែត្រ។",
    "🏊 Michael Phelps ឈ្នះមេដាយអូឡាំពិកសរុប 28 គ្រឿង ក្នុងនោះមានមេដាយមាស 23 គ្រឿង។",
    "⚽ ប្រទេសប្រេស៊ីលជាក្រុមជម្រើសជាតិបុរសដែលឈ្នះ FIFA World Cup បានច្រើនជាងគេ។",
    "🏀 NBA ត្រូវបានបង្កើតឡើងក្នុងឆ្នាំ 1946 ហើយដំបូងមានឈ្មោះថា Basketball Association of America មុនពេលក្លាយជា NBA ក្នុងឆ្នាំ 1949។",
    "🎾 ការប្រកួត Grand Slam កីឡាវាយកូនបាល់ទាំង 4 គឺ Australian Open, French Open, Wimbledon និង US Open។",
    "🏎️ ការប្រកួតជើងឯកពិភពលោក Formula 1 លើកដំបូងបានធ្វើឡើងនៅ Silverstone ក្នុងឆ្នាំ 1950។",
    "🥊 កីឡាប្រដាល់ត្រូវបានដាក់បញ្ចូលក្នុងកីឡាអូឡាំពិកបុរាណ។",
    "🏉 ឈ្មោះកីឡា Rugby មានប្រភពមកពី Rugby School នៅ Warwickshire ប្រទេសអង់គ្លេស។",
    "🏏 ក្រុមកីឡាគ្រីឃីតស្តង់ដារមួយមានកីឡាករ 11 នាក់។",
    "⚽ ការប្រកួតបាល់ទាត់ស្តង់ដារមួយមាន 2 តង់ ដែលមួយតង់មាន 45 នាទី មិនរាប់បញ្ចូលម៉ោងបន្ថែម។",
    "🏀 ការប្រកួតបាល់បោះដំបូងគេប្រើកន្ត្រកផ្លែប៉េសជាគោលដៅ។",
    "🎾 ពាក្យ «love» ត្រូវបានប្រើជាប្រពៃណី ដើម្បីបង្ហាញពិន្ទុសូន្យក្នុងកីឡាវាយកូនបាល់។",
    "🏅 កីឡាអូឡាំពិកសម័យទំនើបបានចាប់ផ្តើមនៅទីក្រុង Athens ក្នុងឆ្នាំ 1896។",
    "⛳ ការលេងកីឡាវាយកូនហ្គោលមួយជុំស្តង់ដារមាន 18 រន្ធ។",
    "🏐 កីឡាបាល់ទះដំបូងត្រូវបានហៅថា «mintonette» នៅពេលបង្កើតឡើងក្នុងឆ្នាំ 1895។",
    "⚽ ពាក្យ «soccer» មានប្រភពមកពីពាក្យកាត់នៃ «association football»។",
    "🏓 កីឡាវាយកូនឃ្លីលើតុត្រូវបានអភិវឌ្ឍនៅប្រទេសអង់គ្លេស ជាកំណែខាងក្នុងនៃកីឡាវាយកូនបាល់លើវាលស្មៅ។",
]

def keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🧠 ចំណេះដឹងកីឡា", callback_data="fact")],
        [InlineKeyboardButton("🔄 ចំណេះដឹងមួយទៀត", callback_data="fact")],
    ])

def fact_message():
    return f"🧠 <b>ចំណេះដឹងកីឡា</b>\n\n{random.choice(FACTS)}"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = (
        "🧠 <b>សូមស្វាគមន៍មកកាន់ Sportfact!</b>\n\n"
        "ស្វែងយល់ពីចំណេះដឹងកីឡាដែលគួរឱ្យចាប់អារម្មណ៍ និងសាកល្បងចំណេះដឹងរបស់អ្នក។\n\n"
        "ចុចប៊ូតុងខាងក្រោម ដើម្បីចាប់ផ្តើម។"
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
