import discord
from discord.ext import commands
import discord.ui
	
class Chameleon(commands.Cog):
	def __init__(self,client):
		self.client = client
	@commands.Cog.listener()
	async def on_ready(self):
		print('loaded')
	@commands.command()
	async def roles(self,ctx):
		print(self.client.players)

class Roles(discord.ui.View, Chameleon):
	def __init__(self, client, counter=0):
		self.client = client
		self.counter = counter
		super().__init__(timeout = None)
	@discord.ui.button(label = "Role 1", custom_id = "Role 1", style = discord.ButtonStyle.secondary)
	async def button1(self, interaction, button):
		self.counter += 1
		print(self.counter, self.client.test.testnum)

	@discord.ui.button(label = "Role 2", custom_id = "Role 2", style = discord.ButtonStyle.secondary)
	async def button2(self, interaction, button):
		self.counter += 1
		print(self.counter, self.client.test.testnum)

async def setup(client):
	await client.add_cog(Chameleon(client))
