import discord
from dotenv import load_dotenv
import os
from src.ryuka_personality import ryuka_response

load_dotenv()
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if client.user.mentioned_in(message):
        user_input = message.content.replace(f"<@{client.user.id}>", "").strip()
        
        response = ryuka_response(user_input)
        
        await message.channel.send(response)

client.run(DISCORD_TOKEN)