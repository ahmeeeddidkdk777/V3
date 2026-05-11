import discord
import mss
import os
from datetime import datetime

TOKEN = os.environ.get("DISCORD_BOT_TOKEN", "MTI4MTU4MDM4MzM2ODExODMzMw.GYsrko.-Key5tmBAv7YZ1eHfktvO4eGCRWFNiv9ohwmGk")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

def take_screenshot():
    folder = "screenshots"
    os.makedirs(folder, exist_ok=True)
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = os.path.join(folder, f"screenshot_{timestamp}.png")
    with mss.mss() as sct:
        sct.shot(output=filename)
    return filename

@client.event
async def on_ready():
    print(f"Bot online: {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == "!see":
        filename = take_screenshot()
        await message.channel.send(file=discord.File(filename))

client.run(TOKEN)
