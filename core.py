#Library Imports
import discord
from discord.ext import commands
import json
import asyncio

#Data Structures
users = dict()

#Save Data Structures to Json Files
def save():
    try:
        with open("users.json", "w+") as f:
            json.dumps(users, f)
    except Exception as e:
        print(e)
        
#Load Data Structures from Json Files
def load():
    try:
        print("Loading Users...")
        with open("users.json", "r") as f:
            users = json.loads(f)
    except Exception as e:
        print(e)

#Check if User Exists
def userExists(param):
    if param in users:
        return True
    return False

#Create a New User
def createUser(param):
    if not userExists(param):
        users[param] = dict()
        save()
        return True
    return False

@isla.event
async def on_ready():
    print(isla.user.name)
    print(isla.user.id)
    await isla.change_presence(game = discord.Game(name = 'Memes'))

@isla.command(pass_context = True)
async def register(ctx):
    author_id = ctx.message.author.id
    author_name = ctx.message.author.name
    if createUser(author_id):
        await isla.say(author_name + " has been registered.")
    else:
        await isla.say(author_name + " you are already registered.")

isla = commands.Bot(command_prefix = "#", description = "memes")
token = "Place Token Here"
isla.run(token)
