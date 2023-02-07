import discord
import re
import os

def run_disc_bot():
    tkn = os.getenv('DISCORD_TOKEN')

    # print(tkn)

    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents = intents)

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        thing = re.findall("[iI]m\s\s*\w\w*",message.content)
        thing2 = re.findall("[iI]'m\s\s*\w\w*",message.content)
        if thing:
            name = re.findall("\s\s*\w\w*", thing[0])[0]
            to_send = "hi" + name + ", im dadBot"
            await message.channel.send(to_send)
        elif thing2:
            name = re.findall("\s\s*\w\w*", thing[0])[0]
            to_send = "hi" + name + ", i'm dadBot"
            await message.channel.send(to_send)
        elif client.user == "gates#9081":
            await message.channel.send("my regex is better than yours")

    client.run(tkn)
    

    

