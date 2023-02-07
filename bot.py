import discord
import re
import os
from dotenv import load_dotenv

load_dotenv()

def run_disc_bot():
    tkn = os.getenv('DISCORD_TOKEN')

    print(tkn)

    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents = intents)

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        thing = re.findall("[iI]m\s+\w+",message.content)
        thing2 = re.findall("[iI]'m\s+\w+",message.content)
        thing3 = re.findall("[iI]\s+am\s+\w+",message.content)
        if thing:
            name = re.findall("\s\s*\w\w*", thing[0])[0]
            to_send = "hi" + name + ", im dadBot"
            await message.channel.send(to_send)
        elif thing2:
            name = re.findall("\s\s*\w\w*", thing2[0])[0]
            to_send = "hi" + name + ", i'm dadBot"
            await message.channel.send(to_send)
        elif thing3:
            name = re.findall("\s\s*\w\w*", thing3[0])[1]
            to_send = "hi" + name + ", i am dadBot"
            await message.channel.send(to_send)
        elif str(message.author) == "ER bot#2861":
            await message.channel.send("my regex is better than yours")
        elif str(message.author) == "jeremyliu#4616":
            await message.channel.send("jermy")
        elif str(message.author) == "zallada#8370":
            print("DEBUG: father")
            
            

    client.run(tkn)
    

    

