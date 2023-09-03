# Character Manager Bot

Welcome to the TRPG Character Manager Bot! This bot helps users manage character information in a Discord server. This bot was made with the intention of being used in TRPG games but it can serve many other purposes. Players can create characters, track character attributes, and perform various actions using commands.

## Features

- Create and manage up to 5 characters and their attributes.
- Track character levels, XP, HP, and coins.
- Manage inventory with slots for items.
- Roll any type and number of dice.
- Add modifiers to die rolls.
- Interact with the bot using simple commands.

## Installation

1. Clone this repository to your local machine.
2. Install the required dependencies.
3. Create a Discord bot on the Discord Developer Portal and obtain a bot token.
4. Create a config.json file with the following:
```
{
  "token": "YOUR_BOT_TOKEN_HERE"
}
```
5. Replace the `YOUR_BOT_TOKEN_HERE` placeholder with your actual bot token.

## Usage

1. Invite the bot to your Discord server using the OAuth2 link provided by Discord.
2. Use the command prefix `&` to interact with the bot (e.g., `&create_character`).

## Commands

- `&create_character`: Create a new character with customizable attributes.
- `&delete_character`: Delete the currently selected character.
- `&change_character`: Move between character slots, use +1 and -1 to move back and forth between slots.
- `&xp`, `&hp`, `&name_char`, `&coins`, `&level`: Modify various character attributes.
- `&next_level`: Increase the character's level by one.
- `&show_charinfo`: Display a character's information.
- `&new_item`, `&remove_item`: Add and remove items from the character's inventory.
- `&roll`: For die rolling, format is: NdT +/- Modifier where N is number of dice and T is type. Ex: 3d6 + 3, roll 3 six sided die and add 3. 

## Contributing

Contributions are welcome! If you want to enhance the bot's functionality or fix issues, follow these steps:

1. Fork this repository.
2. Create a new branch for your feature or fix.
3. Make your changes and test them locally.
4. Commit your changes and push them to your fork.
5. Create a pull request to this repository's `main` branch.
