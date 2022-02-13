import discord
from discord.ext import commands
from discord_components import DiscordComponents
from config.Auth import read_token

token = read_token()
bot = commands.Bot(command_prefix='>>')
bot.remove_command('help')
DiscordComponents(bot)


@bot.event
async def on_ready():
    print(f'{bot.user.name} is online')
    await bot.change_presence(
        status=discord.Status.online,
        activity=discord.Activity(type=discord.ActivityType.playing, name='SCUM ON DRONE')
    )


bot.run(token)
