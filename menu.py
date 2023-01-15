import discord
from discord.ext import commands

class Menu(commands.Cog, discord.ui.View):
	def __init__(self, client):
		super().__init__()
		self.client = client
	@discord.ui.select(
			placeholder = "Select a game",
			options = [
					discord.SelectOption(label="Just One"),
					discord.SelectOption(label="Shiritori"),
					discord.SelectOption(label="The Chameleon")
			]
	)
	
	async def select_callback(self, select, interaction):
		if interaction.values[0] == 'Just One':
			try:
				await self.client.unload_extension('menu')
			except:
				pass
			await self.client.load_extension('justone')
		elif interaction.values[0] == 'Shiritori':
			try:
				await self.client.unload_extension('menu')
			except:
				pass
			await self.client.load_extension('shiritori')
		if interaction.values[0] == 'The Chameleon':
			try:
				await self.client.unload_extension('menu')
			except:
				pass
			await self.client.load_extension('chameleon')
		await select.response.defer()

async def setup(client):
	embed = discord.Embed(title = 'Menu', description = 'Created by <@314300380051668994>. Please report any problems/bugs.\n\n**Just One** *(3-8 players)*\n*> A cooperative party game where you play together to discover as many mystery words as possible.*\n**Shiritori** *(2-8 players)*\n*> A word game where you type words that starts with the last letter of your opponent\'s word.*\n**The Chameleon** *(3-8 players)*\n*> A social deduction game where players must race to catch the Chameleon.*', colour = discord.Colour.green())
	try:
		client.menu = await client.menu.edit(embed=embed, view=Menu(client))
	except:
		client.menu = await client.get_channel(client.channel_id).send(embed=embed, view=Menu(client))
		
	await client.add_cog(Menu(client))
