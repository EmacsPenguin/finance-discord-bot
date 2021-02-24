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
    if message.content.startswith('!finance'):
        msg = message.content.split(" ")
        await message.channel.send(price_get(msg[1]))


client.run('PUT TOKEN HERE')
