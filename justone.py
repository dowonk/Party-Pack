import discord
from discord.ext import commands
from players import Players
		
class JustOne(commands.Cog):
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
		
		embed = discord.Embed(title = 'Just One', description = 'It\'s your choice, make a difference!', colour = discord.Colour.orange())
		embed.add_field(name = 'How to Play', value = 'Click [here](https://www.ultraboardgames.com/just-one/game-rules.php) to view the rules.\n\n Just One is a cooperative party game in which you play together to discover as many mystery words as possible.\n\n A game is played over 13 cards and the goal is to get a score as close to 13 as possible. Players take turns guessing and draw a card from the deck. Teammates must then help the guesser by secretly submitting one word clues relating to the card. But be careful - if your clues are similar, they will not be shown to the guesser!\n\n Correct guesses will score the team 1 point. Wrong answers will cause the team to lose the current card as well as the top card from the deck.', inline = False)
		embed.add_field(name = 'Players', value = (', '.join(p.name for p in self.client.players)) if self.client.players else ('-----'), inline = False)
		self.client.menu = await self.client.menu.edit(embed=embed)
		await interaction.response.defer()

	@discord.ui.button(label = "Leave", custom_id = "Leave", style = discord.ButtonStyle.red)
	async def button2(self, interaction, button):
		for p in self.client.players:
			if p.name == interaction.user.display_name:
				self.client.players.remove(p)
				
		embed = discord.Embed(title = 'Just One', description = 'It\'s your choice, make a difference!', colour = discord.Colour.orange())
		embed.add_field(name = 'How to Play', value = 'Click [here](https://www.ultraboardgames.com/just-one/game-rules.php) to view the rules.\n\n Just One is a cooperative party game in which you play together to discover as many mystery words as possible.\n\n A game is played over 13 cards and the goal is to get a score as close to 13 as possible. Players take turns guessing and draw a card from the deck. Teammates must then help the guesser by secretly submitting one word clues relating to the card. But be careful - if your clues are similar, they will not be shown to the guesser!\n\n Correct guesses will score the team 1 point. Wrong answers will cause the team to lose the current card as well as the top card from the deck.', inline = False)
		embed.add_field(name = 'Players', value = (', '.join(p.name for p in self.client.players)) if self.client.players else ('-----'), inline = False)
		self.client.menu = await self.client.menu.edit(embed=embed)
		await interaction.response.defer()

	@discord.ui.select(
			placeholder = "Select a game",
			options = [
					discord.SelectOption(label="Menu"),
					discord.SelectOption(label="Shiritori"),
					discord.SelectOption(label="The Chameleon")
			]
	)

	async def select_callback(self, select, interaction):
		if interaction.values[0] == 'Menu':
			try:
				await self.client.unload_extension('justone')
			except:
				pass
			await self.client.load_extension('menu')
		elif interaction.values[0] == 'Shiritori':
			try:
				await self.client.unload_extension('justone')
			except:
				pass
			await self.client.load_extension('shiritori')
		if interaction.values[0] == 'The Chameleon':
			try:
				await self.client.unload_extension('justone')
			except:
				pass
			await self.client.load_extension('chameleon')
			
		await select.response.defer()

async def setup(client):
	embed = discord.Embed(title = 'Just One', description = 'It\'s your choice, make a difference!', colour = discord.Colour.orange())
	embed.add_field(name = 'How to Play', value = 'Click [here](https://www.ultraboardgames.com/just-one/game-rules.php) to view the rules.\n\n Just One is a cooperative party game in which you play together to discover as many mystery words as possible.\n\n A game is played over 13 cards and the goal is to get a score as close to 13 as possible. Players take turns guessing and draw a card from the deck. Teammates must then help the guesser by secretly submitting one word clues relating to the card. But be careful - if your clues are similar, they will not be shown to the guesser!\n\n Correct guesses will score the team 1 point. Wrong answers will cause the team to lose the current card as well as the top card from the deck.', inline = False)
	embed.add_field(name = 'Players', value = (', '.join(p.name for p in client.players)) if client.players else ('-----'), inline = False)
	client.menu = await client.menu.edit(embed=embed, view=Menu(client))
	
	await client.add_cog(JustOne(client))
