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

class Players:
	def __init__(self, name):
		self.name = name

class Menu(discord.ui.View):
	@discord.ui.button(label = "Join Lobby", custom_id = "Join", style = discord.ButtonStyle.secondary)
	async def button1(self, interaction, button):
		for p in client.players:
			if p.name == interaction.user.display_name:
				await interaction.response.defer()
				return
				
		client.players.append(Players(interaction.user.display_name))
		
		embed = discord.Embed(title = 'Dowon\'s Party Pack', description = 'Welcome to Dowon\'s Party Pack! A bot containing a variety of board games that can be played right here on Discord. Created by <@314300380051668994>', colour = discord.Colour.green())
		embed.add_field(name = 'Players', value = (', '.join(p.name for p in client.players)) if client.players else ('-----'), inline = False)
		client.menu = await client.menu.edit(embed=embed)
		await interaction.response.defer()

	@discord.ui.button(label = "Leave Lobby", custom_id = "Leave", style = discord.ButtonStyle.secondary)
	async def button2(self, interaction, button):
		for p in client.players:
			if p.name == interaction.user.display_name:
				client.players.remove(p)
				
		embed = discord.Embed(title = 'Dowon\'s Party Pack', description = 'Welcome to Dowon\'s Party Pack! A bot containing a variety of board games that can be played right here on Discord. Created by <@314300380051668994>', colour = discord.Colour.green())
		embed.add_field(name = 'Players', value = (', '.join(p.name for p in client.players)) if client.players else ('-----'), inline = False)
		client.menu = await client.menu.edit(embed=embed)
		await interaction.response.defer()
		
	@discord.ui.select(
			placeholder = "Select a game",
			min_values = 1,
			max_values = 1,
			options = [
					discord.SelectOption(label="Just One"),
					discord.SelectOption(label="Shiritori"),
					discord.SelectOption(label="The Chameleon")
			]
	)
	async def select_callback(self, select, interaction):
		if interaction.values[0] == 'The Chameleon':
			await client.load_extension('chameleon')

@client.command()
async def play(ctx):
	embed = discord.Embed(title = 'Dowon\'s Party Pack', description = 'Welcome to Dowon\'s Party Pack! A bot containing a variety of board games that can be played right here on Discord. Created by <@314300380051668994>', colour = discord.Colour.green())
	embed.add_field(name = 'Players', value = (', '.join(p.name for p in client.players)) if client.players else ('-----'), inline = False)
	client.menu = await ctx.send(embed=embed, view = Menu())

client.run('OTg2ODk3NTIwOTEzNDQwNzc4.GbfKcn.1xpI7M1S922hQ2_bATOhHYdMsmZDdNi25LA9TM')
