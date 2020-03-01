import time
import os
from colorama import Fore, Style, Back

print(Fore.RED + Style.BRIGHT+ "If you see this, something went wrong."+ Style.RESET_ALL)

os.system('clear')

dead = False
complete = False

checkpoint = 0

path = "START"

etiHeader = "-------------------------"
etiText = "	ESCAPE THE ISLAND"

center = 160

print(Style.BRIGHT+etiHeader.center(center)+"\n"+etiText.center(center)+"\n"+etiHeader.center(center) + Style.RESET_ALL)

print(Style.BRIGHT + "CONTROLS:" + Style.RESET_ALL)
print("Type the number which = the choice \n OR type [I] to open your inventory")
input(Style.BRIGHT + Fore.LIGHTCYAN_EX + "\nPress [ENTER] to continue:")
os.system('clear')

def Path(description, choices, ChoiceCont, pathNext):
	global path

	print(Fore.YELLOW+Style.BRIGHT+Back.WHITE+"- " + Back.LIGHTWHITE_EX+Fore.BLACK+description+"\n" + Style.RESET_ALL)
	for i in range (len(choices)):
		print(Fore.RED+Style.BRIGHT+"["+str(i + 1)+"] " + Style.RESET_ALL + choices[i])
	
	cont = False
	while cont != True:
		choice = input(Style.BRIGHT+Fore.LIGHTCYAN_EX+"\nWhat choice do you choose? " + Fore.RED)
		if choice.isnumeric():
			choice = int(choice) - 1
			if 0 <= choice <= len(choices) - 1:
				os.system('clear')
				print(Style.RESET_ALL + str(choice + 1)+"- " + ChoiceCont[choice] + "\n")
				time.sleep(1)
				path = pathNext[choice]
				cont = True
			else:
				print("Not in range! \n")
				time.sleep(.5)
		else:
			if choice.lower() == "i":
					Inventory()
					input(Style.BRIGHT + Fore.LIGHTCYAN_EX +"Press [ENTER] to continue: " + Fore.RED)
					cont = True
					os.system('clear')
					Path(description, choices, ChoiceCont, pathNext)
			else:
				print("Not a number! \n")
				time.sleep(.5)

def Inventory():
	os.system('clear')

	print(Style.BRIGHT + Fore.GREEN +"_________________________")
	if knife > 0:
		print("|"+ str(knife), "x", "Knife		|")
		print("|			|")
	print("|GEAR:			|")
	print("|Helmet	|", helmet, "		|")
	print("|Chest	|", chest, "	|")
	print("|Legs	|", legs, "	|")
	print("|Shoes	|", shoes, "		|")
	print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")

def GetItem(item, change):
	global knife
	global helmet
	global chest
	global legs
	global shoes

	if str(item).isnumeric():
		if item == knife:
			item += change
			knife = item
			print(Style.BRIGHT + Fore.GREEN + "You got", change, "knife!" + Style.RESET_ALL)
	else:
		item = change
		print(Style.BRIGHT + Fore.GREEN + "You got", change + Style.RESET_ALL)

def Checkpoint(currentCheckpoint, nextPath):
	global checkpoint
	global path

	print(Style.BRIGHT+ Fore.GREEN + "Checkpoint [" + str(currentCheckpoint + 1) + "] Reached! \n\n"+ Style.RESET_ALL)
	checkpoint += 1
	
	path = nextPath
	
while dead == False or complete == False:
	if path == "START":
		knife = 0
		helmet = "NONE"
		chest = "Torn Shirt"
		legs = "Torn Shorts"
		shoes = "NONE"

		Path("You wake up, you are in a dark, cold, small room, with only a rusted iron door in front of your eyes, a large man walks in, light interrogating you from behind the door, he grabs you, you try to struggle but you are weak from lying in the room for so long, you give up, and let him take you forward. You and the large man walk for a while through the whitewashed, windowless hall for what fells like an eternity, you stop, he reaches forward, clasping his security card, and a part of the wall opens, he throws you towards the opening, making you fly and skid on the ground, torn and blodied, and closes the door behind you. What do you do?", ["Immediately run and try to destroy the door you are locked behind", "Assess the area, see what is around you", "Lay down and try to sleep"], ["The door isn't there, interesting...", "You look around...", "Whilst in your sleep, you were attacked by something and died."], ["START", "ForestInspect", "DEAD"])

	if path == "ForestInspect":
		GetItem(knife, 1)

		Path("What you found:\n.You're in a dense forest, the moon is up\n.There's no sign of the door, interesting...\n.You can hear faint rustling of leaves and twigs\n.You can hear the sound of a river\n.There is a knife on the floor, you pick it up\n", ["Enter the forest to try to find the river", "Wait for an animal to come, maybe you can follow it to the river"], ["You enter into the depths of the jungle...", "You wait for an animal to come..."], ["ForestEnter", "Tiger!"])

	if path == "Tiger!":
		Path("An angry tiger is coming towards you! Hurry!", ["Attack! [1x Knife]", "RUN!", "Stay still..."], ["The tiger gets to you, you attack, but it attacks you as well, will you survive? No. You're tired. Why did you choose to attack.", "You run, But the tiger is faster than you! It catches up to you and attacks you.", "You stay still, the tiger is not stupid, it attacks you."], ["DEAD", "DEAD", "DEAD"])
	
	if path == "ForestEnter":
		Path("You hear yourself getting closer to the river, but you also hear a monkey close to it.\n", ["Carry on to the river, this monkey might be dangerous, or a decoy...", "Find a longer way, there might be more dangers this way", "Go back to where you started", "Make as much noise as you can, lure the monkey out"], ["You go closer to the river, you hear the monkey getting closer", "You find a longer way around...", "You go back to where you started...", "You make loads of noise, all the animals go towards you, some attack you."], ["MonkeyRiver", "LongRiver", "ForestInspect", "DEAD"])
	
	if path == "MonkeyRiver":
		Path("You come face to face with the monkey, it runs away screaming, a tiger picks up this and comes towards you.", ["Run! Follow the river!", "Stay and fight the tiger", "Hide!"], ["You follow the river...", "The tiger gets to you, you attack, but it attacks you as well, will you survive? No. You're tired. Why did you choose to attack.", "You hide, the tiger picks up your scent, it attacks you."], ["FollowRiver", "DEAD", "DEAD"])
	
	if path == "LongRiver":
		Path("Whist finding a long way around, you find yourself wandering into a region of the forest coated in spider webs, you hear a sound of twigs hitting things quickly, or are they twigs?", ["Carry on into this spider-infested region", "Try to get out, find an even longer way around", "Call out- lure the spider to you, if there are any", "Start destroying the webs"], ["You carry on...", "You try to get out, and find a giant spider waiting for you, you run the other way, but you fall and get trapped in a web...", "You call out for the spiders, why? They run for you, they trap you.", "You start destroying the webs, ok.. the spiders see this, they run for you, they trap you."], ["SpiderTrap", "DEAD", "DEAD", "DEAD"])
	
	if path == "FollowRiver":
		Path("Ahed, you spot a crocodile waiting near the water, it spots you.", ["Carry on, hope it doesn't attack you", "Attack it", "Run"], ["The crocodile's hungry, while you approach near, it attacks you", "You attack the crocodile, you have no weapons, it defeats you", "You run back, regroup, and enter the forest again"], ["DEAD", "DEAD", "ForestEnter"])

	if path == "SpiderTrap":
		Path("As you edge your way through the spider-infested region, you pick up a faint scent, this scent gets more potent, until it overwhelmes your senses. You feel youself slowling drifting in an out of consciousness, until you lose it all together.\nYou wake up. Your whole body feels costricted, and cramped, you open your eyes, and see nothing but webs! You're trapped!", ["Stay, wait for a spider to come, maybe before it eats you you can escape", "Struggle! Get out of the web as fast as you can!", "Call out for help, maybe something will..."], ["You wait, after a while you hear a spider approaching...", "You struggle and struggle, but it's no use, you made too much of a commotion, the spiders are coming to kill you", "You call out for help, your weak voice croaking with the effort"], ["SpiderTrick", "DEAD", "SpiderHelp"])

	if path == "SpiderHelp":
		Path("Rusling, moving, shaking, something approaches you. Maybe it's someone coming to help! You see their faint shadow growing bigger. It's the man that threw you in here! He comes forward, knife sliding into his hand from his belt, and stabs you.", ["Die", "Also die", "Die?", "Just die", "dead."],["You died", "You didn't die, then you die", "Did you die? Yes.", "You just died", "yes"], ["DEAD", "DEAD", "DEAD", "DEAD", "DEAD"])

	if path == "SpiderTrick":
		Path("A spider crawls up to you... It cuts the web, you fall out onto the soft ground covered in leaves ranging in a myriad of colours from green to yellow to orange to red. You stand up, the spider hits you back down to the ground.", ["Get back up and run", "Lay down for a bit, it might get bored of you", "Attack the spider", "Call for help"], ["You run, it knocks you down, you get back up and keep running", "You lay down, it eats you", "You attack the spider, you are weak, it defeats you and eats you", "You call for help..., you winded voice whistling through the trees"], ["Checkpoint1", "DEAD", "DEAD", "SpiderHelp"])
	
	if path == "Checkpoint1":
		Checkpoint(0, "SpiderChase")
	

	if path == "SpiderChase":
		Path("You're running through all of the spider webs, sipders chasing you, the path you're folowing splits in two ways", ["The path that is clear and open", "The path that is dark and covered in webs and thorns"], ["You follow the open path...", "You follow the dark path..."], ["OpenSpiderTracks", "DarkSpiderTracks"])
	
	if path == "OpenSpiderTracks":
		Path("You take the open path, you sense a forbidding being in your prescense, not in sight but nearby. You reach the end of the path, spiders no longer chasing you, instantly running as soon as they set foot on this path. In front of you is the ruins of an ancient city, metal sprouting from the overgrown ground, moss and vines engulfing metal and concrete alike.", ["Carry on slowly, being careful not to tread on anything sharp", "Run through the city, whatever is close won't want to take the chase", "Run back to the opening where the other path split"], ["You carry on, slowly...", "You run, you trip over something, something attacks you", "You go back to the split"], ["BrokenCity", "DEAD", "SpiderChase"])

	if path == "DarkSpiderTracks":
		Path("You take the dark path, it feels safe. Suddenly your eyes go dark, you lose your balance.", ["Hold onto a tree and keep yourself upright", "Fall to the ground and black out, get some rest"], ["You hold on to the tree, your hand feels like it's burning, you look at it through your dark clouded eyes and see hot red marks on your palm, the burning acid from the tree gets into your veins", "You fall to the ground, landing on the hard ground littered woth sharp twigs and leaves, one twig hits into your side, pain sweeping through your torso, but was numbed by the soft hum of sleep overwhelming you, you feel yourself being dragged into the other path, the open path..."], ["DEAD", "OpenSpiderTracks"])

	if path == "BrokenCity":
		Path("You make your way through the broken city, looking at the remenants of this society. You see glimpses of bright red eyes in the shadows, watching you, you dismiss it, you're tired, you're just imagining it. Something catches your eye, something shining, something gold, something interesting...", ["Run away!", "Walk past it, it's not your main concern", "Go up and inspect it"], ["You run away, something hits you on the haed, something like a metal pole", "You walk past it, a mist appears, shrouding your vision, something knocks you to the ground and ravages you", "You walk up and inspect it..."], ["DEAD", "DEAD", "ShinyInspect"])

	if path == "ShinyInspect":
		Path("You walk up to inspect the shiny thing. Something moves. You walk closer. It moves again, shaking and rustling all the leaves encapsulating it, you reach out to touch it. Suddenly, the silver disapears and something jumps out of the bush! A writhing skin-covered beast with metal implants; almost like cybernetics. Thick saliva streaming out of its disjointed dispersed mouth, with razor teeth in random positions and angles, sprouting outwards of its inwards abyss. He charges at you.", ["Drop on the floor", "Run", "Attack", "Die"], ["You drop to the floor, it loses sight of you, while trying to find you again, it accidentally steps on you, and crushes you", "You run, it chases you, you have to fight, it's too fast", "You fight the beast...", "You stop breathing, you have a heart attack"], ["DEAD", "MonsterFight", "MonsterFight", "DEAD"])
	
	if path == "MonsterFight":
		Path("You try to punch it, it moves back quickly. It stabs you with one of its metal claws. Your eyes become hazy, your vision shrouded, you fall to the ground.", ["Die", "Wait", "Almost die"], ["You die.", "You wait and don't die...", "You almost die, but you lose control of your dying and die."], ["DEAD", "checkpoint2", "DEAD"])
	
	if path == "checkpoint2":
		Checkpoint(1, "MonsterCave")
	
	if path == "MonsterCave":
		Path("You wake up, in a cave, moss and vines encapulating the insidious sharp rocks surrounding you, a strong smell of rotten flesh blocks your nose, making you want to gag... Heavy footsteps tremble the cold, hard stone floor; making the vines sway with the effort.", ["Run", "Go deeper into the cave", "Wait for your captor to return"], ["You run and try to escape the cave", "You enter deeper into the cave...", "You wait for the monster to return, you wait for hours, the sun slowly descending in waves of crimson, it sets, the monster still doesn't return. You get tired, and fall asleep."], ["MonsterRun", "MonsterCaveEnter", "MonsterCave"])
	
	if path == "MonsterRun":
		Path("Long strands of grass scrape against your bare legs, cutting you in all places as you attempt to escape the cave behind you, its prescence like a large fist pessing against your back. Movement catches your eye, there's something in the bushes to your right.", ["Carry on running", "Turn back and find another way away from the cave", "Stop. Get ready in case it jumps out at you"], ["You carry on running, suddenly aware of how loud the crunching of the leaves beneath your feet are, you feel a prescence behind you, getting closer... ", "You run back to the cave, you feel tired after all the running, you go to sleep...", "The being in the bush jumps out at you, it's the beast; It attacks you, your futile attempts to resist and fight instantly absorbed by its strength."],["MonsterChase", "MonsterCave", "DEAD"])
	
	if path == "MonsterChase":
		Path("With an accelerated surge, the being that was behind you tears into your view out of the bushes in front. Its misshapen body twisted clear of the shrouding leaves and stood, forbidding, awaiting, ready. A deep, heavy growl seemed to emenate from every fiber of its being, the sound giving the illusion that the being's body was tremoring, almost as if it was shifting in and out of existence. Its eyes snapped directly to your weak form. Its body pointed directly at you. Its half-metallic half-flesh limbs were angled at an attacking stance; directly at you.", ["Turn right, run into the bushes", "Turn left, you haven't had a chance to see what's there", "Run back to the cave and hide", "Fight it"], ["You run into the bushes, as you turn, so does the beast. It chases you and after a few seconds of hopless chase, it surges at you.", "You turn left, and run. Twigs and leaves slapping against your face, your eyes start to water, blurring your vision. You don't see the ledge coming up; You don't see yourself running off it, into the impending doom below.", "You go back to the cave, and enter deeper into it...", "You fight it? You fight it. Guess what happened."], ["DEAD", "WaterPlunge", "MonsterCaveEnter", "DEAD"])
	
	if path == "MonsterCaveEnter":
		Path("Echoes of water dripping into a lake cascade around the walls of the cave. You proceed, entering into the heart to the cave, closer and closer to the source of the sound. You reach the end of the narrow walkway, and enter into a large opening; In the center of this opening is a large lake, with a source that comes from nowhere in sight. Steam was emmitting from the lake, with a strange green tint to it, but the more you concentrate on the tint, the harder it was to see. Directly in front of you, you see bubbles, large bubbles, and a lot of them. Then, with a thunderous surge, something beaks the surface of the lake and bursts free into the open cavern. A misshapen black body wrenched clear of the steaming waters, and hung silhouetted in the darkness. Out of the darkness blinked a pair of cold, red eyes; Stretching as it rose, the being was more than twenty feet from top to bottom and ten across.", ["Run out of the cave", "Run away deeper into the cave", "Hide and wait for it to go back into the water", "Jump into the water"], ["You try to run deeper into the cave, the being swung one of his massive arms at you, you get knocked over, you fly and hit against the walls of the cave", "You go deeper into the cave...", "You hide, you wait, water starts filling up the cave, the water is steaming hot, and burns your whole body.", "You jump into the water, the water is boiling hot, your body gets burned."], ["DEAD", "DeeperCave", "DEAD", "DEAD"])
	
	if path == "DeeperCave":
		Path("The walkway you are following starts to ascend, the darkness shrouding you starts to dissipate, its coat slowly lifting off of you. Ahead, you see the cave open, blinding light straining your eyes, you exit the cave. Which way do you go?", ["Back into the cave", "Keep going forwards until you find something", "Go up the hill behind you"], ["You go back into the cave..", "You keep going,As you are walking, you see towering mountains on either side of you, a rock falls on you.", "You trek up the hill, it levels off, and then it descends, when you reach the bottom of the descent, you realise you are at the start of the cave you just came out of, tiredness from all the walking overwhelms you, you decide to go into the cave and sleep..."], ["MonsterCave", "DEAD", "MonsterCave"])
	
	if path == "WaterPlunge":
		Path("You plunge downward, a tiny speck of darkness against the deep blue-gray of the night sky, your stomach dropping away, the rush of the wind filling your ears with its sound. Far below you the waters of a lake shimmered with pieces of crimson light as the glaring eyes of the beast reflected against the rippling surface, all about you the sweep of vast mountains and cliffs rose up through the blur of your vision. Time seemed to come to a sudden standstill, and it felt as if you would never come to rest.\nYou struck with a jarring force, breaking through the surface of the lake and plunging deep into the cold, dark waters. The breath left your lungs suddenly, and your whole body when numb with shock. Frantically, you claw your way through the chill blackness that had closed about you, barely conscious of anything beyond the need to reach the surface to breathe.\nLike a boulder struck into your chest, resisting your ascent, you realise that the forbidding, menacing eyes of the moster will be waiting your return above, you feel time slowly slipping and sliding out of your delicate grasp on it, you need to act fast", ["Get back up to the surface. Breathe", "Stay in the waters, wait for the monster to think you're dead", "Swim downwards, the monster might be in the waters chasing you, you do not know the full extent of its powers"], ["You apprach the surface, a a rushing force presses in against you, so strong that it treatenes to break you in two, you open your blurred eyes to see what hit you, but you could see nothing, a crimson haze shrouding your view, you thrash, but it feels like your arms are not working, you feel nothing where the should be, you attempt to move your hand to shift away the crimson haze, but no hand moved to shift it. Panic and desperation floods your body like a waterfall, your arms have been ripped off, the monster is here with you in the water.", "A moment later, everything slipped away from you", "You swim downwards, the pressure sqeezing your lungs, its desperate efforts to steal your last breath, instinct overwhelms you, you open your mouth. You breathe in the water"], ["DEAD", "WaterDream", "DEAD"])
	
	if path == "WaterDream":
		Path("You dream, a long, endless dream of disconnected feelings and sensations of times and places both rembered and yet somehow new. Waves of sound and motion carried you through landscapes of nightmare and haunts of the familiar, through the forest, and through sweeps of black, cold water, where life passed in tangled disarray in faces and shapes not fixed one to the other, but disjointed and free. The man you met before was there, come and gone in brief glimpses, a distorted form that combined reality with falsehood and begged for understanding. Words came at you from things misshapen and lifeless, yet a voice seemed to speak words, calling to you, calling...\nThen the monster was holding you, metallic and covetous arms wrapped tightly about your body, the voices of the forest a whisper of life in a dark place. You floated, the waters buoying you, and your face turned skyward into the cloaded night. Gasping, you sought to shout but could not manage. You were awake again, come back from where you had slipped away, yet not fully conscious of having left. You drifted in and out of darkness, reaching back each time you began to slide too far so that you might be grasped by the sound and colour and feeling that meant life.\nMore hands were grasping you, pulling you up from the waters and the blackness, easing you down onto solid ground once more. Muffled voices muttered vaguely, the fragmented words slipping through your mind. His eyes flickered, and then the man that you met at the start was bending over you, hard face damp and drawn with chill, his hair plastered againts his head.", ["Ask who he is", "Ask where you are", "Ask are you safe", "Ask where the monster is", "Shout for help", "Remain silent"], ["You open your mouth to ask, but he places a finger upon your frozen lips. \n'Don't worry, there's no need, don't try to talk, just rest. I sense your question. You ask who I am? I am the one you met before, the one who has been watching you, I will explain more when you are in a fit state to talk, sleep, you're all right now.", "You open your mouth to ask, but he places a finger upon your frozen lips. \n'Don't worry, there's no need, don't try to talk, just rest. I sense your question. You want to know where we are? We are in the same forest, where you have been since the beginning, you will be leaving shortly, I will explain more when you are in a fit state to talk, sleep, you're all right now.","You open your mouth to ask, but he places a finger upon your frozen lips. \n'Don't worry, there's no need, don't try to talk, just rest. I sense your question. You want to know if we're safe? We are safe, nothing will harm you now, no more running, I will explain more when you are in a fit state to talk, sleep, you're all right now.", "You open your mouth to ask, but he places a finger upon your frozen lips. \n'Don't worry, there's no need, don't try to talk, just rest. I sense your question. You want to know where the monster is? He is gone, we sent him away, it will not chase you any longer, I will explain more when you are in a fit state to talk, sleep, you're all right now.", "You open your mouth to ask, but he places a finger upon your frozen lips. \n'Don't worry, there's no need, don't try to talk, just rest. I sense your question. You want help? We are help, you will be safe with us, you always have been safe with us, I will explain more when you are in a fit state to talk, sleep, you're all right now.", "You stay silent.\n'Don't worry if you don't want to talk now, we will have plenty of time later, I will explain more when you are in a fit state to talk, sleep, you're all right now."], ["THE END", "THE END", "THE END", "THE END", "THE END", "THE END"])
	
	if path == "THE END": 
		input("Press [ENTER] To Continue: ")
		os.system('clear')
		print(Back.LIGHTWHITE_EX+Fore.BLACK+Style.BRIGHT + "You wake up. You might not have came awake even then if it had not been for the echoing footseps that relieved you not too gently from your slumber. The door behind you opens, you feel a prescence enter the small, plain room you lie in. He comes into your view. It's the man again.\n'I guess you have lots of questions, too much for what needs to happen next, so I will explain as much as I can. The forest you have just been in is our testing ground for new recruits, we call them the 'limbos', you will be told about why through experience, both past and future ones yet to come. You may ask why? It's simple. We let only the most determined, strongest of selected candidates, like you, to enter our training program. This training program was real, no simulation or dream, you could have died, like multiple people have, some people may even be familiar to you, so count yourself lucky. Unfortunately, this project requires ultimate secrecy, the type of which not even you may be allowed to hold until further tests, even though you just went through our program. You may be wondering why you cannot remember anything before the jungle, those memories were supressed for the test, they will return shortly. The drug we used has a timer for its effectiveness, reach that time and it will wear off, hence why you were being chased so much in the jungle, we cannot let past memeories returning by hiding compromise our results. Now it is time for you to show your worth, I am sorry for what I am about to do, but it is standard procedure.'\nLike a bolt of lightning, his hand struck at your head. Darkness once again overwhelms you.\n\nYour eyes quickly open. You see yourself walking through a whitewashed, windowless hall for what seems like an eternity, you reach a door and open it. Your eyes instantly adjust to the shift into darkness, and you find youself looking at a frail figure which looks like it had been jolted awake; In a dark, cold, small room. Without any hestation, you pick it up and drag it back through the hall, until you reach a door. You grab on to the handle. You open the door. You push the person out of the door. Just as you shut it, realisation slams into you. Doubts swarm your mind like a disturbed swarm of bees, however your body disobeys the anarchy in your mind, it turns back and walk through the hall to another door, and you enter the door...\n\nThe man is standing there, staring right through your thoughts, slicing your mind in two, one side doubt, one side tiredness. The doubt and triedness bridge together and form one single thought:\n 'Did I really get rescued or did I drown?'\nThe answer forms at your lips yet you cannot ask it, forever hanging in limbo between thought and reality.")
		input("THE END")

	if path == "DEAD":
		print(Fore.RED+Style.BRIGHT+"\nYou died!")
		restartCheck = False
		while restartCheck == False:
			restart = input("Enter [Y] to restart or [N] to exit: ")
			if restart.lower() == "y":
				print("restarting...")
				path = "START"
				os.system('clear')
				restartCheck = True

				if checkpoint == 1:
					path = "SpiderChase"
					print(Style.BRIGHT + Fore.GREEN +"Starting at checkpoint[" + str(checkpoint) + "] ... \n" + Style.RESET_ALL)
				if checkpoint == 2:
					path = "MonsterCave"
					print(Style.BRIGHT + Fore.GREEN +"Starting at checkpoint[" + str(checkpoint) + "] ... \n" + Style.RESET_ALL)
			elif restart.lower() == "n":
				print("Ok, closing down...")
				dead = True
				exit()
			else:
				print("Unknown input, please enter either [Y] or [N]")
