import discord
from discord.ext import commands
from discord.ui import Select
from players import Players
import random

categories = {'Artists':['Damien Hirst','Salvador Dali','Pablo Picasso','Vincent Van Gogh','Claude Monet','Andy Warhol','Leonardo da Vinci','Michelangelo','Banksy','Mark Rothko','Keith Haring','Jeff Koons','Rembrandt','Jackson Pollock','Edward Hopper'],
						 'Authors':['Shakespeare','Tolkien','C.S. Lewis','J.K. Rowling','Stephen King','Ernest Hemingway','Edgar Allan Poe','Charles Dickens','Stephanie Meyer','Tolstoy','Jane Austen','Mark Twain','F. Scott Fitzgerald','John Grisham','Dan Brown'],
						 'Bands':['The Beatles','The Rolling Stones','AC/DC','Nirvana','Backstreet Boys','One Direction','Guns N\' Roses','Queen','The Beach Boys','Red Hot Chili Peppers','KISS','Jackson 5','ABBA','The Eagles','The Who'],
						 'Capitals':['London','Moscow','Paris','Berlin','Madrid','Rome','Cairo','Helsinki','Stockholm','Oslo','Washington','Mexico City','Beijing','Tokyo','Seoul'],
						 'Cartoon Animals':['Garfield','Scooby-Doo','Yogi Bear','Bugs Bunny','Mickey Mouse','Goofy','Jiminy Cricket','Kung Fu Panda','Nemo','Tony the Tiger','Snoopy','Bambi','Dumbo','Toothless','Simba'],
						 'Children\'s Books':['The Hobbit','Matilda','Stuart Little','Whinnie-the-Pooh','Peter Pan','Harry Potter & the Sorcerer\'s Stone','The Cat in the Hat','The Adventures of Tom Sawyer','The Very Hungry Caterpillar','Alice in Wonderland','Charlie and the Chocolate Factory','The Jungle Book','101 Dalmatians','The Lion, the Witch and the Wardrobe','Where the Wild Things Are'],
						 'Cities':['New York City','Paris','Tokyo','Chicago','Moscow','Rome','Athena','L.A.','Delhi','Rio de Jamneiro','Cairo','San Francisco','London','Sydney','Hong Kong'],
						 'Civilizations':['Romans','Egyptians','Mayans','Mongols','Aztecs','Japanese','Persians','Greeks','Turks','Vikings','Incas','Spanish','Zulu','Chinese','Spartans'],
						 'Colors':['Red','Blue','Green','Yellow','Black','White','Orange','Pink','Brown','Purple','Gray','Gold','Silver','Bronze','Rainbow'],
						 'Countries':['U.K.','Spain','Japan','Brazil','France','U.S.A','Italy','Australia','Germany','Mexico','India','Israel','Canada','China','Russia'],
						 'Disney':['Cinderella','Belle','Snow White','Ariel','Mulan','Jasmine','Pocahontas','Mickey Mouse','Donald Duck','Pluto','Bambi','Peter Pan','Captain Hook','Baloo','Winnie the Pooh'],
						 'Drinks':['Coffee','Tea','Lemonade','Coca-Cola','Wine','Beer','Punch','Tequila','Hot Chocolate','Milkshake','Root Beer','Water','Smoothie','Orange Juice','Milk'],
						 'Fairy Tales':['Cinderella','Goldilocks','Jack and the Beanstalk','Hare and the Tortoise','Snow White','Rapunzel','Aladdin','Princess and the Pea','Peter Pan','Little Red Riding Hood','Pinocchio','Beauty and the Beast','Sleeping Beauty','Hansel and Gretel','Gingerbread Man'],
						 'Fictional Characters':['Indiana Jones','Mary Poppins','Spiderman','Catwoman','James Bond','Wonder Woman','Princess Leia','The Little Mermaid','Dracula','Lara Croft','Robin Hood','Hermione Granger','Super Mario','Homer Simpson','Hercules'],
						 'Film Genres':['Horror','Action','Thriller','Sci-Fi','Rom-Com','Western','Comedy','Christmas','Gangster','Foreign Language','War','Documentary','Musical','Animation','Zombie'],
						 'Food':['Curry','Chips','Salad','Fish','Chicken','Sausage','Orange','Mango','Leek','Tomato','Chilli','Beef','Pizza','Pasta','Ice Cream'],
						 'Games':['Monopoly','Scrabble','Mouse Trap','Guess Who','Risk','Operation','Twister','Pictionary','Battleship','Backgammon','Clue','Chess','Checkers','Trivial Pursuit','Jenga'],
						 'Geography':['Lake','Sea','Valley','Mountain','River','Desert','Ocean','Forest','Jungle','Island','Glacier','Waterfall','Volcano','Cave','Arctic'],
						 'Harry Potter':['Harry Potter','Ron Weasley','Hermione Granger','Neville Longbottom','Luna Lovegood','Albus Dumbledore','Minerva Mcgonnagal','Pomona Sprout','Severus Snape','Dobby','Sirius Black','Remus Lupin','Peter Pettigrew','Lord Voldemort','Draco Malfoy'],
						 'Historial Figure':['Jesus','Napoleon','Stalin','Hitler','Darwin','Martin Luther King Jr.','Pocahontas','Einstein','Christopher Columbus','Mother Teresa','Ulysses S. Grant','Caesar','Mozart','Cleopatra','Buddha'],
						 'Hobbies':['Stamps','Trains','Model Making','Knitting','Fishing','Reading','Painting','Gardening','Sailing','Travel','Walking','Pottery','Cooking','Yoga','Photography'],
						 'Inventions':['Matches','Gunpowder','Wheel','Printing','Computer','Internet','Compass','Plane','TV','Electricity','Writing','Steam Engine','Car','Telephone','Camera'],
						 'Jobs':['Fisherman','Lumberjack','Nurse','Waiter','Lighthouse Keeper','Secretary','Accountant','Teacher','Lorry Driver','Security Guard','Chef','Architect','Police Officer','Lawyer','Carpenter'],
						 'Marvel Heroes':['Spiderman','Ironman','Hulk','Captain America','Thor','Deadpool','Wolverine','Groot','Loki','Star-Lord','Gamora','Drax','Magneto','Ant Man','Daredevil'],
						 'Movies':['Jurassic Park','Jaws','Raiders of the Lost Ark','The Avengers','Transformers','Toy Story','Home Alone','Titanic','E.T.','The Wizard of Oz','King Kong','The Matrix','Shrek','The Godfather','Finding Nemo'],
						 'Music':['Rock','Heavy Metal','Classical','Funk','Hip Hop','Pop','Techno','Blues','Rap','Punk','Indie','Christmas','Country','House','Disco'],
						 'Musical Instruments':['Electric Guitar','Piano','Violin','Drums','Bass Guitar','Saxophone','Cello','Flute','Clarinet','Trumpet','Voice','Ukulele','Harp','Bagpipe','Harmonica'],
						 'Musicals':['West Side Story','Cats','Jersey Boys','School of Rock','Phantom of the Opera','Les Miserables','Oliver','Hamilton','Chicago','Hadestown','Annie','Book of Mormon','Lion King','Wicked','Hairspray'],
						 'Mythical Creatures':['Cyclops','Pegasus','Medusa','Sphinx','Werewolf','Unicorn','Dragon','Troll','Loch Ness Monster','Mermaid','Phoenix','Vampire','Minotaur','Hydra','Yeti'],
						 'Pets':['Dog','Cat','Parrot','Rabbit','Hamster','Guinea Pig','Goldfish','Snake','Lizard','Horse','Alpaca','Frog','Rat','Crab','Budgie'],
						 'Phobias':['Ghosts','Spiders','Monsters','Rats','Toilets','Snakes','Germs','Clowns','Needles','Dogs','Birds','Insects','Children','Shadows','Roller Coasters'],
						 'Presidents':['Clinton','Reagan','Roosevelt (FDR)','Eisenhower','George W. Bush','George Bush Sr.','Obama','Trump','Kennedy','Lincoln','Washington','Nixon','Teddy Roosevelt','Jefferson','Adams'],
						 'Rooms':['Hallway','Kitchen','Dining Room','Living Room','Bathroom','Bedroom','Cellar','Attic','Dungeon','Conservatory','Shed','Study','Garage','Music Room','Workshop'],
						 'School':['Math','Chemistry','Physics','Biology','History','Philosophy','Geography','English','Economics','French','Art','Music','Physical Education','Latin','Religious Studies'],
						 'Sci-Fi/Fantasy':['Star Wars','Lord of the Rings','Star Trek','Blade Runner','The Addams Family','2001: A Space Odyssey','Terminator','Game of Thrones','Dune','The Princess Bride','Alice in Wonderland','The Avengers','The War of the Worlds','The Martian','WALL-E'],
						 'Sports':['Football','Rugby','Athletics','Swimming','Hockey','Tennis','Badminton','Golf','Squash','Gymnastics','Trampolining','Cycling','Volleyball','Cricket','Baseball'],
						 'Sports Stars':['Tiger Woods','Pele','Michael Jordan','LeBron James','Michael Phelps','Serena Williams','Muhammad Ali','Tom Brady','Hope Solo','Babe Ruth','Wayne Gretzky','Ronda Rousey','Tony Hawk','Shaun White','Usain Bolt'],
						 'States':['California','Texas','Alabama','Hawaii','Florida','Montana','Nevada','Mississippi','North Carolina','New York','Kentucky','Tennessee','Colorado','Washington','Illinois'],
						 'The Arts':['Painting','Sculpture','Architecture','Dance','Literature','Opera','Stand-Up','Comic Books','Illustration','Music','Theatre','Cinema','Video Games','Graffiti','Fashion'],
						 'Toys':['Lego','Rocking Horse','Super Soaker','Cabbage Patch Dolls','Rubik\'s Cube','Etch a Sketch','Teddy Bear','Play-Doh','Yo-yo','Frisbee','Hot Wheels','Barbie','Slinky','self.I. Joe','Hula Hoop'],
						 'Transport':['Plane','Car','Tank','Helicopter','Cruise Ship','Hovercraft','Motorbike','Bus','Segway','Cable Car','Jet Ski','Hot Air Balloon','Train','Spaceship','Magic Carpet'],
						 'TV Shows':['Friends','Sex and the City','Star Trek','The Walking Dead','Breaking Bad','Days of Our Lives','How I Met Your Mother','Lost','The Office','The X-Files','General Hospital','Frasier','Mad Men','South Park','Game of Thrones'],
						 'Under the Sea':['Octopus','Starfish','Shark','Jellyfish','Lobster','Seal','Dolphin','Killer Whale','Crab','Giant Squid','Seahorse','Stingray','Sea Turtle','Clownfish','Swordfish'],
						 'Wedding Anniversaries':['Wood','China','Paper','Cotton','Bronze','Gold','Ruby','Diamond','Crystal','Flowerse','Silk','Leather','Pearl','Coral','Tin'],
						 'World Wonders':['Pyramids','Eiffel Tower','Statue of Liberty','Big Ben','Stonehenge','Golden Gate Bridge','Colosseum','Sydney Opera House','Christ the Redeemer','Machu Picchu','Taj Mahal','Hoover Dam','Great Wall of China','Mount Rushmore','Empire State Building'],
						 'Zoo':['Elephant','Giraffe','Koala','Tiger','Lion','Leopard','Meerkat','Buffalo','Ostrich','Owl','Eagle','Parrot','Scorpion','Alligator','Zebra']}
		
class Chameleon(commands.Cog):
	def __init__(self, client, start = False, guessing = False, most_voted = [], category = None, word = None, chameleon = None):
		self.client = client
		self.start = start
		self.guessing = guessing
		self.most_voted = most_voted
		self.category = category
		self.word = word
		self.chameleon = chameleon

	def reset(self):
		for p in self.client.players:
			if not self.start:
				p.score = 0
			p.voting = None
			
		self.client.game.most_voted = []
		self.client.game.chameleon = random.choice(list(p.user for p in self.client.players))
		self.client.game.category = random.choice(list(categories))
		self.client.game.word = random.choice(list(categories[self.client.game.category]))

class Menu(discord.ui.View, Players):
	def __init__(self, client):
		super().__init__()
		self.client = client
		
	@discord.ui.button(label = "Join", style = discord.ButtonStyle.green)
	async def button1(self, interaction, button):
		if self.client.game.start or interaction.user in [p.user for p in self.client.players]:
			await interaction.response.defer()
			return
				
		self.client.players.append(Players(interaction.user.display_name, interaction.user, 0, None))
		
		embed = discord.Embed(title = 'The Chameleon', description = 'Blend in, don\'t get caught.', colour = discord.Colour.green())
		embed.add_field(name = 'Rules', value = '[Click Here](https://bigpotato.com/blogs/blog/how-to-play-the-chameleon-instructions)', inline = False)
		embed.add_field(name = 'Recommended Players', value = '3-8', inline = False)
		embed.add_field(name = 'How to Play', value = 'Each round, a player is randomly selected as **The Chameleon** and a secret word is drawn from a category.\n\nEach player must submit a word related to the secret word. The Chameleon does not know the secret word and must blend in with the group.\n\nThe goal of the Chameleon is to blend in with the players and figure out what the secret word while the rest of the players try to unmask the Chameleon. If Chameleon is caught, they will have one chance to guess the secret word.', inline = False)
		embed.add_field(name = 'Players', value = (', '.join(p.name for p in self.client.players)) if self.client.players else ('-----'), inline = False)
		self.client.menu = await self.client.menu.edit(embed=embed)
		await interaction.response.defer()

	@discord.ui.button(label = "Leave", style = discord.ButtonStyle.red)
	async def button2(self, interaction, button):
		for p in self.client.players:
			if p.user == interaction.user:
				self.client.players.remove(p)
				
		embed = discord.Embed(title = 'The Chameleon', description = 'Blend in, don\'t get caught.', colour = discord.Colour.green())
		embed.add_field(name = 'Rules', value = '[Click Here](https://bigpotato.com/blogs/blog/how-to-play-the-chameleon-instructions)', inline = False)
		embed.add_field(name = 'Recommended Players', value = '3-8', inline = False)
		embed.add_field(name = 'How to Play', value = 'Each round, a player is randomly selected as **The Chameleon** and a secret word is drawn from a category.\n\nEach player must submit a word related to the secret word. The Chameleon does not know the secret word and must blend in with the group.\n\nThe goal of the Chameleon is to blend in with the players and figure out what the secret word while the rest of the players try to unmask the Chameleon. If Chameleon is caught, they will have one chance to guess the secret word.', inline = False)
		embed.add_field(name = 'Players', value = (', '.join(p.name for p in self.client.players)) if self.client.players else ('-----'), inline = False)
		self.client.menu = await self.client.menu.edit(embed=embed)
		await interaction.response.defer()

	@discord.ui.button(label = "Start", style = discord.ButtonStyle.blurple)
	async def button3(self, interaction, button):
		if interaction.user not in [p.user for p in self.client.players] or len(self.client.players) < 2:
			await interaction.response.defer()
			return

		self.client.game.start = True
		self.client.game.chameleon = random.choice(list(p.user for p in self.client.players))
		self.client.game.category = random.choice(list(categories))
		self.client.game.word = random.choice(list(categories[self.client.game.category]))

		embed = discord.Embed(title = self.client.game.category, colour = discord.Colour.green())
		embed.add_field(name = 'Player', value = '\n'.join(p.name for p in self.client.players), inline = True)
		embed.add_field(name = 'Vote', value = '\u200b', inline = True)
		embed.add_field(name = 'Score', value = '\n'.join(str(p.score) for p in self.client.players), inline = True)
		self.client.menu = await self.client.menu.edit(embed=embed, view=Category(self.client))
		await interaction.response.defer()

	@discord.ui.select(
			placeholder = "Select a game",
			options = [
					discord.SelectOption(label="Menu"),
					discord.SelectOption(label="Just One"),
					discord.SelectOption(label="Shiritori")
			]
	)

	async def select_callback(self, select, interaction):
		if interaction.values[0] == 'Menu':
			try:
				await self.client.unload_extension('chameleon')
			except:
				pass
			await self.client.load_extension('menu')
		elif interaction.values[0] == 'Just One':
			try:
				await self.client.unload_extension('chameleon')
			except:
				pass
			await self.client.load_extension('justone')
		if interaction.values[0] == 'Shiritori':
			try:
				await self.client.unload_extension('chameleon')
			except:
				pass
			await self.client.load_extension('shiritori')
			
		await select.response.defer()

class Next(discord.ui.View):
	def __init__(self, client):
		super().__init__()
		self.client = client
		
	@discord.ui.button(label = "Next", style = discord.ButtonStyle.green)
	async def button1(self, interaction, button):
		self.client.game.reset()
		
		if self.client.game.start and interaction.user in [p.user for p in self.client.players]:
			embed = discord.Embed(title = self.client.game.category, colour = discord.Colour.green())
			embed.add_field(name = 'Player', value = '\n'.join(p.name for p in self.client.players), inline = True)
			embed.add_field(name = 'Vote', value = '\u200b', inline = True)
			embed.add_field(name = 'Score', value = '\n'.join(str(p.score) for p in self.client.players), inline = True)
			self.client.menu = await interaction.response.send_message(embed=embed, view=Category(self.client))
		else:
			embed = discord.Embed(title = 'The Chameleon', description = 'Blend in, don\'t get caught.', colour = discord.Colour.green())
			embed.add_field(name = 'Rules', value = '[Click Here](https://bigpotato.com/blogs/blog/how-to-play-the-chameleon-instructions)', inline = False)
			embed.add_field(name = 'Recommended Players', value = '3-8', inline = False)
			embed.add_field(name = 'How to Play', value = 'Each round, a player is randomly selected as **The Chameleon** and a secret word is drawn from a category.\n\nEach player must submit a word related to the secret word. The Chameleon does not know the secret word and must blend in with the group.\n\nThe goal of the Chameleon is to blend in with the players and figure out what the secret word while the rest of the players try to unmask the Chameleon. If Chameleon is caught, they will have one chance to guess the secret word.', inline = False)
			embed.add_field(name = 'Players', value = (', '.join(p.name for p in self.client.players)) if self.client.players else ('-----'), inline = False)
			self.client.menu = await self.client.get_channel(self.client.channel_id).send(embed=embed, view=Menu(self.client))
		await interaction.response.defer()

class Category(discord.ui.View):
	def __init__(self, client):
		super().__init__()
		self.client = client
		self.cards()

	def cards(self):
		async def click(interaction: discord.Interaction):
			if interaction.data['component_type'] == 2 and self.client.game.guessing and interaction.user == self.client.game.chameleon:
				self.client.game.guessing = False
				winners = []
				
				if self.client.game.word == interaction.data['custom_id']:
					for p in self.client.players:
						if p.user == self.client.game.chameleon:
							p.score += 1
							if p.score == 5:
								winners.append(p.name)
											
					embed = discord.Embed(title = f'✅ **{self.client.game.word}**', colour = discord.Colour.green())
					embed.add_field(name = 'Player', value = '\n'.join(p.name for p in self.client.players), inline = True)
					embed.add_field(name = 'Score', value = '\n'.join(str(p.score) + (' `+1`' if p.user == self.client.game.chameleon else '\u200b') for p in self.client.players), inline = True)
				else:
					for p in self.client.players:
						if p.voting == self.client.game.chameleon.display_name:
							p.score += 1
							if p.score == 5:
								winners.append(p.name)
									
					embed = discord.Embed(title = f'❌ {interaction.data["custom_id"]}', description = f'The secret word was **{self.client.game.word}**.', colour = discord.Colour.green())
					embed.add_field(name = 'Player', value = '\n'.join(p.name for p in self.client.players), inline = True)
					embed.add_field(name = 'Score', value = '\n'.join(str(p.score) + (' `+1`' if p.voting == self.client.game.chameleon.display_name else '\u200b') for p in self.client.players), inline = True)
					
				if winners:
					self.client.game.start = False
					embed.add_field(name = '\u200b', value = f'**{winners[0]}** has won the game!' if len(winners) == 1 else f'**{", ".join(winners)}** have won the game!', inline = False)
				await interaction.response.send_message(embed=embed, view=Next(self.client))
				
			elif interaction.data['component_type'] == 3:
				if interaction.data['values'][0] == 'Draw' and interaction.user in [p.user for p in self.client.players]:
					if interaction.user in [p.user for p in self.client.players] and interaction.user == self.client.game.chameleon:
						embed = discord.Embed(title = '', description = 'You are **The Chameleon**! Blend in!', colour = discord.Colour.green())
						await interaction.response.send_message(embed=embed, ephemeral=True)
						
					elif interaction.user in [p.user for p in self.client.players] and interaction.user != self.client.game.chameleon:
						embed = discord.Embed(title = '', description = f'You are **NOT** the chameleon! The secret word is **{self.client.game.word}**.', colour = discord.Colour.green())
						await interaction.response.send_message(embed=embed, ephemeral=True)
						
				elif interaction.user in [p.user for p in self.client.players]:
					for p in self.client.players:
						if p.user == interaction.user and interaction.data['values'][0] != interaction.user.display_name:
							p.voting = interaction.data['values'][0]
							self.client.game.most_voted.append(interaction.data['values'][0])

							embed = discord.Embed(title = self.client.game.category, colour = discord.Colour.green())
							embed.add_field(name = 'Player', value = '\n'.join(p.name for p in self.client.players), inline = True)

							if all([p.voting != None for p in self.client.players]):
								embed.add_field(name = 'Vote', value = '\n'.join((p.voting if p.voting != None else '\u200b') for p in self.client.players), inline = True)
							else:
								embed.add_field(name = 'Vote', value = '\n'.join(('✓' if p.voting != None else '\u200b') for p in self.client.players), inline = True)
							embed.add_field(name = 'Score', value = '\n'.join(str(p.score) for p in self.client.players), inline = True)
							self.client.menu = await interaction.response.edit_message(embed=embed, view=Category(self.client))

							if all([p.voting != None for p in self.client.players]):
								self.client.game.most_voted = {i:self.client.game.most_voted.count(i) for i in self.client.game.most_voted}
								self.client.game.most_voted = sorted(self.client.game.most_voted.items(), key=lambda x: x[1], reverse = True)
								
								if self.client.game.chameleon.display_name == self.client.game.most_voted[0][0] and self.client.game.most_voted[0][1] > self.client.game.most_voted[1][1]:
									self.client.game.guessing = True
									embed = discord.Embed(title = 'You must make a guess.', colour = discord.Colour.green())
									embed.set_author(name=f'{self.client.game.chameleon.display_name} was caught!', icon_url=self.client.game.chameleon.display_avatar.url)
									await interaction.followup.send(embed=embed)
								else:
									for p in self.client.players:
										if p.user == self.client.game.chameleon:
											p.score += 1
											if p.score == 5:
												winners = p.name
											
									embed = discord.Embed(description = f'The secret word was **{self.client.game.word}**.', colour = discord.Colour.green())
									embed.add_field(name = 'Player', value = '\n'.join(p.name for p in self.client.players), inline = True)
									embed.add_field(name = 'Score', value = '\n'.join(str(p.score) + (' `+1`' if p.user == self.client.game.chameleon else '\u200b') for p in self.client.players), inline = True)
									embed.set_author(name=f'{self.client.game.chameleon.display_name} escaped!', icon_url=self.client.game.chameleon.display_avatar.url)
									
									if winners:
										self.client.game.start = False
										embed.add_field(name = '\u200b', value = f'**{p.name}** has won the game!', inline = False)
									await interaction.followup.send(embed=embed, view=Next(self.client))
							break
			await interaction.response.defer()
			
		for c in range(15):
			card = discord.ui.Button(label = categories[self.client.game.category][c], custom_id = categories[self.client.game.category][c], style = discord.ButtonStyle.green)
			card.callback = click
			self.add_item(card)
			
		options = []
		options.append(discord.SelectOption(label='Draw Card', value='Draw', emoji='🃏', description='View your role/word'))
		for p in self.client.players:
			options.append(discord.SelectOption(label=f'Vote {p.name}', value = p.name))
		select = Select(placeholder = 'Select Option', options = options)
		select.callback = click
		self.add_item(select)
		
async def setup(client):
	embed = discord.Embed(title = 'The Chameleon', description = 'Blend in, don\'t get caught.', colour = discord.Colour.green())
	embed.add_field(name = 'Rules', value = '[Click Here](https://bigpotato.com/blogs/blog/how-to-play-the-chameleon-instructions)', inline = False)
	embed.add_field(name = 'Recommended Players', value = '3-8', inline = False)
	embed.add_field(name = 'How to Play', value = 'Each round, a player is randomly selected as **The Chameleon** and a secret word is drawn from a category.\n\nEach player must submit a word related to the secret word. The Chameleon does not know the secret word and must blend in with the group.\n\nThe goal of the Chameleon is to blend in with the players and figure out what the secret word while the rest of the players try to unmask the Chameleon. If Chameleon is caught, they will have one chance to guess the secret word.', inline = False)
	embed.add_field(name = 'Players', value = (', '.join(p.name for p in client.players)) if client.players else ('-----'), inline = False)
	client.menu = await client.menu.edit(embed=embed, view=Menu(client))

	client.game = Chameleon(client)
	await client.add_cog(client.game)
