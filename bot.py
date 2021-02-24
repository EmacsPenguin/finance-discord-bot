import discord
import requests

client = discord.Client()

def price_get(stock_symbol):
    r = requests.get(
     'https://query1.finance.yahoo.com/v7/finance/quote?symbols=' + stock_symbol).json()
    output_value = stock_symbol.upper() + ": " + str(r['quoteResponse']['result'][0]['regularMarketPrice'])
    return output_value

@client.event
async def on_ready():
    print("The bot is ready!")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$finance'):
        msg = message.content.split(" ")
        await message.channel.send(price_get(msg[1]))
    elif message.content.startswith('$help'):
        await message.channel.send("Finance is a discord bot that will pull the price of stocks from yahoo finance.\nTo use it say $finance <stock symbol>.\nAn example of this is $finance amd.\nRemember you have to use the stock symbol not the company name so you can use $finance fb, but not $finance facebook")


client.run('TOKEN HERE')
