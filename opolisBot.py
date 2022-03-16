import os
import discord
from pathlib import Path
from dotenv import load_dotenv

# load env variables
env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

# loading discording token
TOKEN = os.getenv("API_KEY")


intents = discord.Intents()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    print("hi")
    print(member)
    print("Name of the member is",member.name)
    await member.send(f'Hi {member.name}, welcome to my Discord server!')
    # await member.create_dm()
    # await member.dm_channel.send(
    #     f'Hi {member.name}, welcome to my Discord server!'
        
    # )
    
@client.event
async def on_message(message):
    if message.content == "project owner":
      await message.channel.send("Kindly enter the following detail role,range of experience,type of project")
    elif message.content == "contributor":
      await message.channel.send("Kindly enter the following detail type of experience,years of experience,area of interest,last project worked on")
    if message.author == client.user:
        return
    print(message.content)
    if message.content == 'Hi':
        await message.channel.send('Hi')

client.run(TOKEN)
