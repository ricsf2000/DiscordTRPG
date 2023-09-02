import discord
import json
import os
import asyncio
from discord.ext import commands
from discord import Intents

intents = Intents.default()
intents.message_content = True

#Setting up variable to hide bot token.
with open('config.json', 'r') as config_file:
    config_data = json.load(config_file)
    bot_token = config_data['token']


bot = commands.Bot(command_prefix='&', intents=intents)

#Character information data structure
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

characterslot = {"Character Slot" : 1}

file_path = "data.json"

directory = "members_data"

# Create the directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)


def get_member_file_path(member_id):
    file_path = f"members_data/{member_id}.json" 
    data = load_charslot_data(member_id)
    if data["Character Slot"] > 1:
        for number in range(6):
            if number == data["Character Slot"]:
                file_path = f"members_data/slot{number}{member_id}.json"
    return file_path

def load_member_json_data(member_id):
    file_path = get_member_file_path(member_id)
    with open(file_path, "r") as file:
       data = json.load(file)
    return data

def load_charslot_data(member_id):
    file_path2 = f"members_data/charslots{member_id}.json" 
    with open(file_path2, "r") as file:
       data = json.load(file)
    return data

@bot.command()
async def delete_character(ctx):
    member_id = ctx.author.id
    with open(get_member_file_path(member_id), 'w') as f:
       json.dump(data, f)

@bot.command()
async def change_character(ctx, new_data:int = 1):
    member_id = ctx.author.id
    if new_data > 1 or new_data < -1:
        await ctx.send("Type -1 to move one slot back and 1 to move one slot forward.")
        return
    data = load_charslot_data(member_id)
    if (data["Character Slot"] + new_data) > 5:
        await ctx.send("Maximmum number of slots reached.")
        return
    if not os.path.exists(f"members_data/slot{data['Character Slot'] + new_data}{member_id}.json"):
        await ctx.send("Last slot reached, new slot will be created")
        with open(f"members_data/slot{data['Character Slot'] + new_data}{member_id}.json" , 'w') as f:
            json.dump(data, f)
    data["Character Slot"] += new_data
    with open(f"members_data/charslots{member_id}.json" , 'w') as f:
       json.dump(data, f)
    await ctx.send("You are now in character slot " + str(data["Character Slot"]))
    

@bot.command()
async def create_character(ctx):
    member_id = ctx.author.id
    if os.path.exists(f"members_data/{member_id}.json"):
        try:
            await ctx.send('Do you want to delete your previous character? (type yes or no)')
            response = await bot.wait_for('message', timeout = 60.0, check = lambda m: m.author == ctx.author)
            content = response.content
            if response.content == "yes":
                await delete_character(ctx)
            elif response.content == "no":
                await ctx.send('New character will be created')
                await change_character(ctx, 1)
        except asyncio.TimeoutError:
            await ctx.send('No response, character creation canceled')
            return
    else:
        with open(f"members_data/charslots{member_id}.json", 'w') as f:
            json.dump(characterslot, f)

    with open(get_member_file_path(member_id), 'w') as f:
       json.dump(data, f)

    await ctx.send('What is your character\'s name?')
    try:
        response = await bot.wait_for('message', timeout = 90.0, check = lambda m: m.author == ctx.author)
        content = response.content
        await name_char(ctx, content)
    except asyncio.TimeoutError:
        await ctx.send('No response, character creation canceled.')
        return

    await ctx.send('What is your character\'s level?')    
    try:
        response = await bot.wait_for('message', timeout = 90.0, check = lambda m: m.author == ctx.author)
        content = int(response.content)
        await level(ctx, content)
    except asyncio.TimeoutError:
        await ctx.send('No response, character creation canceled.') 
        return

    await ctx.send('How much xp does your character have?')    
    try:
        response = await bot.wait_for('message', timeout = 90.0, check = lambda m: m.author == ctx.author)
        content = int(response.content)
        await xp(ctx, content)
    except asyncio.TimeoutError:
        await ctx.send('No response, character creation canceled.')  
        return
    
    await ctx.send('What is your character\'s hp?')    
    try:
        response = await bot.wait_for('message', timeout = 90.0, check = lambda m: m.author == ctx.author)
        content = int(response.content)
        await hp(ctx, content)
    except asyncio.TimeoutError:
        await ctx.send('No response, character creation canceled.')  
        return

    await ctx.send('How many coins does your character have?')    
    try:
        response = await bot.wait_for('message', timeout = 90.0, check = lambda m: m.author == ctx.author)
        content = int(response.content)
        await coins(ctx, content)
    except asyncio.TimeoutError:
        await ctx.send('No response, character creation canceled.')  
        return

    await ctx.send('Character has been created!')


@bot.command()
async def xp(ctx, new_data:int = 0):
    member_id = ctx.author.id
    data = load_member_json_data(member_id)
    if new_data == 0:
        await ctx.send('Invalid, please include character information.')
        return
    data["XP"] += new_data
    with open(get_member_file_path(member_id), 'w') as f:
       json.dump(data, f)
    await ctx.send("Your total XP is " + str(data["XP"]))

@bot.command()
async def hp(ctx, new_data:int = 0):
    member_id = ctx.author.id
    data = load_member_json_data(member_id)
    if new_data == 0:
        await ctx.send('Invalid, please include character information.')
        return
    data["HP"] += new_data
    with open(get_member_file_path(member_id), 'w') as f:
       json.dump(data, f)
    await ctx.send("Your HP is " + str(data["HP"]))

@bot.command()
async def name_char(ctx, *new_data:str):
    member_id = ctx.author.id
    data = load_member_json_data(member_id)
    if len(new_data) == 0:
        await ctx.send('Invalid, please include character information.')
        return
    data["Name"] = ' '.join(new_data)
    with open(get_member_file_path(member_id), 'w') as f:
       json.dump(data, f)
    await ctx.send("Your name is now " + data["Name"])

@bot.command()
async def coins(ctx, new_data:int = 0):
    member_id = ctx.author.id
    data = load_member_json_data(member_id)
    if new_data == 0:
        await ctx.send('Invalid, please include character information.')
        return
    data["Coins"] += new_data
    with open(get_member_file_path(member_id), 'w') as f:
       json.dump(data, f)
    await ctx.send("You have " + str(data["Coins"]) + " coins")

@bot.command()
async def level(ctx, new_data:int = 0):
    member_id = ctx.author.id
    data = load_member_json_data(member_id)
    if new_data == 0:
        await ctx.send('Invalid, please include character information.')
        return
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
    if len(new_data) == 0:
        await ctx.send('Invalid, please include character information.')
        return
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
    if len(new_data) == 0:
        await ctx.send('Invalid, please include character information.')
        return
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

bot.run(bot_token)