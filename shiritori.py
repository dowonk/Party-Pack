import discord
from discord.ext import commands
from players import Players
		
class Shiritori(commands.Cog):
	def __init__(self, client):
		self.client = client
	@commands.command()
	async def roles(self,ctx):
		print(self.client.players)

class Menu(discord.ui.View, Players):
	def __init__(self, client):
		super().__init__()
		self.client = client
		
	@discord.ui.button(label = "Join", custom_id = "Join", style = discord.ButtonStyle.green)
	async def button1(self, interaction, button):
		for p in self.client.players:
			if p.name == interaction.user.display_name:
				await interaction.response.defer()
				return
				
		self.client.players.append(Players(interaction.user.display_name))
		
		embed = discord.Embed(title = 'Shiritori', description = 'Based on the Japanese word game!', colour = discord.Colour.purple())
		embed.add_field(name = 'How to Play', value = 'Type in a word starting with the last letter of the previous word.\n', inline = False)
		embed.add_field(name = 'Game Modes', value = '***Normal***\n> Points are calculated by the word\'s letter point values plus your remaining time. Example: If you type in **\'apple\'** at the **7** second mark, you will get **9** points from the letters and **7** points from the remaining time for a total of **16** points. At the end of the game, the player with the most points wins.\n\n> __Letter Point Values__\n> **1** - A, E, I, L, N, O, R, S, T, U\n> **2** - D, G\n> **3** - B, C, M, P\n> **4** - F, H, V, W, Y\n> **5** - K\n> **8** - J, X\n> **10** - Q, Z\n\n***Last Man Standing***\n> Each player is given their own personal timer. Entering a word correctly adds 3 seconds to their next turn. Players will be eliminated if they run out of time. Last remaining player wins.', inline = False)
		embed.add_field(name = 'Players', value = (', '.join(p.name for p in self.client.players)) if self.client.players else ('-----'), inline = False)
		self.client.menu = await self.client.menu.edit(embed=embed)
		await interaction.response.defer()

	@discord.ui.button(label = "Leave", custom_id = "Leave", style = discord.ButtonStyle.red)
	async def button2(self, interaction, button):
		for p in self.client.players:
			if p.name == interaction.user.display_name:
				self.client.players.remove(p)
				
		embed = discord.Embed(title = 'Shiritori', description = 'Based on the Japanese word game!', colour = discord.Colour.purple())
		embed.add_field(name = 'How to Play', value = 'Type in a word starting with the last letter of the previous word.\n', inline = False)
		embed.add_field(name = 'Game Modes', value = '***Normal***\n> Points are calculated by the word\'s letter point values plus your remaining time. Example: If you type in **\'apple\'** at the **7** second mark, you will get **9** points from the letters and **7** points from the remaining time for a total of **16** points. At the end of the game, the player with the most points wins.\n\n> __Letter Point Values__\n> **1** - A, E, I, L, N, O, R, S, T, U\n> **2** - D, G\n> **3** - B, C, M, P\n> **4** - F, H, V, W, Y\n> **5** - K\n> **8** - J, X\n> **10** - Q, Z\n\n***Last Man Standing***\n> Each player is given their own personal timer. Entering a word correctly adds 3 seconds to their next turn. Players will be eliminated if they run out of time. Last remaining player wins.', inline = False)
		embed.add_field(name = 'Players', value = (', '.join(p.name for p in self.client.players)) if self.client.players else ('-----'), inline = False)
		self.client.menu = await self.client.menu.edit(embed=embed)
		await interaction.response.defer()

	@discord.ui.select(
			placeholder = "Select a game",
			options = [
					discord.SelectOption(label="Menu"),
					discord.SelectOption(label="Just One"),
					discord.SelectOption(label="The Chameleon")
			]
	)

	async def select_callback(self, select, interaction):
		if interaction.values[0] == 'Menu':
			try:
				await self.client.unload_extension('shiritori')
			except:
				pass
			await self.client.load_extension('menu')
		elif interaction.values[0] == 'Just One':
			try:
				await self.client.unload_extension('shiritori')
			except:
				pass
			await self.client.load_extension('justone')
		if interaction.values[0] == 'The Chameleon':
			try:
				await self.client.unload_extension('shiritori')
			except:
				pass
			await self.client.load_extension('chameleon')
		await select.response.defer()

async def setup(client):
	embed = discord.Embed(title = 'Shiritori', description = 'Based on the Japanese word game!', colour = discord.Colour.purple())
	embed.add_field(name = 'How to Play', value = 'Type in a word starting with the last letter of the previous word.\n', inline = False)
	embed.add_field(name = 'Game Modes', value = '***Normal***\n> Points are calculated by the word\'s letter point values plus your remaining time. Example: If you type in **\'apple\'** at the **7** second mark, you will get **9** points from the letters and **7** points from the remaining time for a total of **16** points. At the end of the game, the player with the most points wins.\n\n> __Letter Point Values__\n> **1** - A, E, I, L, N, O, R, S, T, U\n> **2** - D, G\n> **3** - B, C, M, P\n> **4** - F, H, V, W, Y\n> **5** - K\n> **8** - J, X\n> **10** - Q, Z\n\n***Last Man Standing***\n> Each player is given their own personal timer. Entering a word correctly adds 3 seconds to their next turn. Players will be eliminated if they run out of time. Last remaining player wins.', inline = False)
	embed.add_field(name = 'Players', value = (', '.join(p.name for p in client.players)) if client.players else ('-----'), inline = False)
	client.menu = await client.menu.edit(embed=embed, view=Menu(client))
	
	await client.add_cog(Shiritori(client))
