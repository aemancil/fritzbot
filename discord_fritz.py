# Discord bot that autoassigns a role to a new user along with a hello command.

import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.members = True
intents.messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Enter token here
TOKEN = ""

@bot.event
async def on_ready():
    print(f"{bot.user.name} is now online!")

@bot.event
async def on_member_join(member):
    role_name = "" #Enter role name here
    role = discord.utils.get(member.guild.roles, name=role_name)

    if not role:
        try:
            role = await member.guild.create_role(name=role_name, reason="Role for new users.")
        except discord.Forbidden:
            print("Bot does not have the 'Manage Roles' permission.")
            return

    try:
        await member.add_roles(role)
        print(f"Assigned '{role_name}' role to {member.name}.")
    except discord.Forbidden:
        print("Bot doesn't have the required permissions to assign roles.")

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello, {ctx.author.name}!")
    print(f"Responded to !hello command from {ctx.author.name}")

if __name__ == "__main__":
    bot.run(TOKEN)
