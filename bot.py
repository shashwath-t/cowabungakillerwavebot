import discord
import random
from discord.ext import commands

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('Bot is Ready')

@client.command()
async def ping(ctx):
    await ctx.send('Pong!')

@client.command()
async def cowabunga(ctx, member):
    prefixes = [
        'Cowabunga',
        "Oh my Poseidon's trident",
        'Oh my word',
        'Radical Dude'
    ]
    suffixes = [
        'caught a killer wave',
        'caught a radical wave',
        'rode a cool tide',
        'drowned'
    ]

    string = random.choice(prefixes) + ' ' + member + ' ' + random.choice(suffixes)

    await ctx.send(string)

client.run('Nzg0ODQ3MDE3MjU1NTAxODQ0.X8vPvg.UpS-hE1DAR1iuP9Vcs66PbJccxo')
