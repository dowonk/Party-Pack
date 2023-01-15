import discord
import asyncio
import os
from discord.ext import commands

intents = discord.Intents.all()
client = commands.Bot("!", intents=intents)

client.players = []

@client.event
async def on_ready():
  print("Ready")

@client.command()
async def play(ctx):
	client.channel_id = ctx.channel.id
	client.menu = None
	client.players = []
	
	try:
		await client.unload_extension('menu')
	except:
		pass
	try:
		await client.unload_extension('justone')
	except:
		pass
	try:
		await client.unload_extension('shiritori')
	except:
		pass
	try:
		await client.unload_extension('chameleon')
	except:
		pass
	await client.load_extension('menu')

client.run('OTg2ODk3NTIwOTEzNDQwNzc4.GbfKcn.1xpI7M1S922hQ2_bATOhHYdMsmZDdNi25LA9TM')
