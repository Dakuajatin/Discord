import discord
from discord.ext import commands
import subprocess

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

@bot.command()
async def execute(ctx, *, command):
    try:
        result = subprocess.check_output(command, shell=True, text=True)
        await ctx.send(f"Command executed successfully:\n```{result}```")
    except subprocess.CalledProcessError as e:
        await ctx.send(f"Error executing command:\n```{e.output}```")

# Replace 'YOUR_BOT_TOKEN' with your actual bot token
bot.run('MTIwMjIyMDY1MjYzMTk1NzU0NQ.GcBPIQ.r1TijaD5T9EWSeCp_of7Jti7YQNEMSfFe9jolY')
