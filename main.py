import telebot
import requests
from bs4 import BeautifulSoup

# Add your telegram bot token below 
Token = 'YOUR_BOT_TOKEN'
bot = telebot.TeleBot(Token)

@bot.message_handler(commands=['start'])
def show_data(msg):
    # Show Srart Msg
    bot.send_message(msg.chat.id, 'لطفا کمی منتظر بمانید...')

    url = 'https://www.tgju.org/currency'
    response = requests.get(url)
    
    if response.status_code == 200:


        parser = BeautifulSoup(response.text, 'html.parser')

        dollar = parser.select_one('table.data-table tr[data-market-nameslug="price_dollar_rl"] td.nf').contents[0]
        uro = parser.select_one('table.data-table tr[data-market-nameslug="price_eur"] td.nf').contents[0]
        uae_Dirham = parser.select_one('table.data-table tr[data-market-nameslug="price_aed"] td.nf').contents[0]
        pound = parser.select_one('table.data-table tr[data-market-nameslug="price_gbp"] td.nf').contents[0]
        turkish_lira = parser.select_one('table.data-table tr[data-market-nameslug="price_try"] td.nf').contents[0]
        switzerland_franc = parser.select_one('table.data-table tr[data-market-nameslug="price_chf"] td.nf').contents[0]
        coin = parser.select_one('li#l-sekee span.info-price').contents[0]
        gold = parser.select_one('li#l-geram18 span.info-price').contents[0]


        # show result 
        result = f'''
        {dollar} دلار 🇺🇸
        {uro} یورو 🇪🇺 
        {uae_Dirham} درهم امارات 🇦🇪
        {pound} پوند انگلستان 🏴󠁧󠁢󠁥󠁮󠁧󠁿
        {turkish_lira} لیر ترکیه 🇹🇷
        {switzerland_franc} فرانک سویس 🇨🇭
        {coin} سکه 🪙
        {gold} طلای ۱۸ عیار 🧈
        '''
        bot.send_message(msg.chat.id, result)
    else :
        bot.send_message(msg.chat.id, 'خطا در ارتباط با ای پی آی ')



bot.polling(timeout=1)
