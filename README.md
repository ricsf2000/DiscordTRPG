# Character Manager Bot

Welcome to the Character Manager Bot! This bot helps users manage character information in a Discord server. Players can create characters, track character attributes, and perform various actions using commands.

## Features

- Create characters and manage their attributes.
- Track character levels, XP, HP, and coins.
- Manage inventory with slots for items.
- Interact with the bot using simple commands.

## Installation

1. Clone this repository to your local machine.
2. Install the required dependencies.
3. Create a Discord bot on the Discord Developer Portal and obtain a bot token.
4. Replace the `YOUR_BOT_TOKEN_HERE` placeholder in `config.json` with your actual bot token.

## Usage

1. Invite the bot to your Discord server using the OAuth2 link provided by Discord.
2. Use the command prefix `&` to interact with the bot (e.g., `!create_character`).
3. 

## Commands

- `!create_character`: Create a new character.
- `!xp <amount>`: Add XP to your character.
- `!hp <amount>`: Add HP to your character.
- `!name_char <new_name>`: Change your character's name.
- `!coins <amount>`: Add coins to your character.
- `!level <amount>`: Increase your character's level.
- `!next_level`: Progress your character to the next level.
- `!show_charinfo [member_id]`: Show character information (optional: specify member's ID).
- `!new_item <item_name>`: Add a new item to your inventory.
- `!remove_item <item_name>`: Remove an item from your inventory.

## Contributing

Contributions are welcome! If you want to enhance the bot's functionality or fix issues, follow these steps:

1. Fork this repository.
2. Create a new branch for your feature or fix.
3. Make your changes and test them locally.
4. Commit your changes and push them to your fork.
5. Create a pull request to this repository's `main` branch.
