import discord
import json
import os
from discord.ext import commands
from discord import Intents

intents = Intents.default()
intents.message_content = True

with open('config.json', 'r') as config_file:
    config_data = json.load(config_file)
    bot_token = config_data['token']


bot = commands.Bot(command_prefix='!', intents=intents)

file_path = "data.json"

data = {
    "Name" : "Unkown",
    "Level":0,  
    "HP" : 0,
    "XP" : 0,
    "Coins" : 0,
    "slot 1" : "empty",
    "slot 2" : "empty",
    "slot 3" : "empty",
    "slot 4" : "empty",
    "slot 5" : "empty",
    "slot 6" : "empty",
    "slot 7" : "empty",
    "slot 8" : "empty",
    "slot 9" : "empty",
    "slot 10" : "empty"
    }


directory = "members_data"

# Create the directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)

with open("data.json", "w") as file:
    json.dump(data, file)


def get_member_file_path(member_id):
    file_path = f"members_data/{member_id}.json"  # Example: members_data/123456789.json
    return file_path

def load_member_json_data(member_id):
    file_path = get_member_file_path(member_id)
    with open(file_path, "r") as file:
       data = json.load(file)
    return data


@bot.command()
async def create_character(ctx):
    member_id = ctx.author.id
    with open(get_member_file_path(member_id), 'w') as f:
       json.dump(data, f)
       await ctx.send('Character has been created!')


@bot.command()
async def xp(ctx, new_data:int):
    member_id = ctx.author.id
    data = load_member_json_data(member_id)
    data["XP"] += new_data
    with open(get_member_file_path(member_id), 'w') as f:
       json.dump(data, f)
    await ctx.send("Your total XP is " + str(data["XP"]))

@bot.command()
async def hp(ctx, new_data:int):
    member_id = ctx.author.id
    data = load_member_json_data(member_id)
    data["HP"] += new_data
    with open(get_member_file_path(member_id), 'w') as f:
       json.dump(data, f)
    await ctx.send("Your HP is " + str(data["HP"]))

@bot.command()
async def name_char(ctx, *new_data:str):
    member_id = ctx.author.id
    data = load_member_json_data(member_id)
    data["Name"] = ' '.join(new_data)
    with open(get_member_file_path(member_id), 'w') as f:
       json.dump(data, f)
    await ctx.send("Your name is now " + data["Name"])

@bot.command()
async def coins(ctx, new_data:int):
    member_id = ctx.author.id
    data = load_member_json_data(member_id)
    data["Coins"] += new_data
    with open(get_member_file_path(member_id), 'w') as f:
       json.dump(data, f)
    await ctx.send("You have " + str(data["Coins"]) + " coins")

@bot.command()
async def level(ctx, new_data:int):
    member_id = ctx.author.id
    data = load_member_json_data(member_id)
    data["Level"] += new_data
    with open(get_member_file_path(member_id), 'w') as f:
       json.dump(data, f)
    await ctx.send("You are now level " + str(data["Level"]))

@bot.command()
async def next_level(ctx):
    member_id = ctx.author.id
    data = load_member_json_data(member_id)
    data["Level"] += 1
    with open(get_member_file_path(member_id), 'w') as f:
       json.dump(data, f)
    await ctx.send("You are now level " + str(data["Level"]))

@bot.command()
async def show_charinfo(ctx, member_id=None):
    if member_id is None:
        member_id = ctx.author.id
    data = load_member_json_data(member_id)

    # Format the output as a dictionary
    output = "Character Information:\n"
    for key, value in data.items():
        output += f"{key}: {value}\n"

    await ctx.send(output)

@bot.command()
async def new_item(ctx, *new_data: str):
    member_id = ctx.author.id
    data = load_member_json_data(member_id)

    for key, value in data.items():
        if value == "empty":
            data[key] = ' '.join(new_data)  # Join the sentence into a single string
            break  # Exit the loop after the first occurrence of "empty"
    else:
        await ctx.send("Your inventory is full")
        return

    with open(get_member_file_path(member_id), 'w') as f:
        json.dump(data, f)
    
    await ctx.send("The new item has been added to your inventory")

@bot.command()
async def remove_item(ctx, *new_data: str):
    member_id = ctx.author.id
    data = load_member_json_data(member_id)

    for key, value in data.items():
        if value == ' '.join(new_data) :
            data[key] = "empty"
            break  
    else:
        await ctx.send("mispelled item")
        return

    with open(get_member_file_path(member_id), 'w') as f:
        json.dump(data, f)
    
    await ctx.send("The item has been removed from your inventory")


@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user.name}')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

bot.run('bot_token')