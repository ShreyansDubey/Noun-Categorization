import random

kitchen_items = ['cutting food', ' food preparation', 'food', 'hand held', 'tool', 'baking', 'mixing', ' blending', 'measuring', 'chef', ' preparation', 'kitchenware', ' eating', 'serving of food', 'serving vessel', 'large', 'hot', 'baked in', ' prepare and', 'hold or store', 'contents of', 'handle', 'flat-bottomed', 'grab handle', 'frying', 'non-stick cookware', 'metal', 'stovetop', 'appliance', 'skin with', 'type of', 'dipped in', 'fed by', 'milk with', 'made of', 'stir with', 'prepared by', 'to knead', 'a handheld motorized', 'counter-top']
#print(len(kitchen_items))

person = ['played with', 'ate the', 'part of', 'captain of', 'defeated by', 'won by', 'feels', 'does job', 'takes responsibility', 'individual', 'prefer to', 'inspired by', 'killed by', 'struck from', 'leader of', 'group of', 'in care of', 'will be at', 'with his', 'with her', 'him', 'her', 'with him', 'to discover', 'to prove', 'to see', 'walking to', 'buys the', 'sells', 'talks to', 'talks about', 'to him', 'to her', 'to them', 'running to', 'with them', 'with it', 'calling the', 'rides', 'walks with']
#print(len(person))

sport = ['played by', 'won by', 'lost by', 'played at', 'watched by', 'airing at', 'keeps fit', 'atheletes', 'performence', 'skilled', 'training', 'to play', 'version of', 'physical activity', 'competitive', 'to participants', 'in teams of', 'many contestants', 'one winner', 'physical', 'rules of', 'judged by', 'limits the', 'global', 'professional', 'at all levels', 'designed for', 'popular', 'exploits of', 'principles of', 'cheated on', 'looking for', 'national', 'international', 'viewership', 'being so great', 'recieve', 'allow it to', 'critisied by', 'as a form of']
#print(len(sport))

kitchen_nouns = ['knife', 'bowl', 'frying pan', 'spatula', 'spoon', 'peeler', 'grinder', 'stove', 'platter', 'plate', 'glass', 'tumbler', 'cup', 'rolling pin', 'pot', 'fork', 'grill', 'whisk', 'tray', 'wooden spoon']
#print(len(kitchen_nouns))

person_nouns = ['Albert', 'Emma', 'Ritesh', 'Sumit', 'Peter', 'Karen', 'Susan', 'Elizabeth', 'Morgan', 'Shubham', 'Arvind', 'Emily', 'Johnathan', 'Hanna', 'Erik', 'Simon', 'Meryl', 'Jack', 'Johnny', 'Jose']
#print(len(person_nouns))

sports_nouns = ['football', 'cricket', 'soccer', 'wrestling', 'archery', 'marathaon', 'hockey', 'tennis', 'vollyball', 'table tennis', 'basketball', 'baseball', 'rugby', 'golf', 'gymnastics', 'cycling', 'skating', 'surfing', 'polo', 'ice hockey']
#print(len(sports_nouns))

context_k = [[] for _ in range(len(kitchen_nouns))]
context_p = [[] for _ in range(len(person_nouns))]
context_s = [[] for _ in range(len(sports_nouns))]
all_nouns = kitchen_nouns + person_nouns + sports_nouns

for i in range(len(kitchen_nouns)) :
	c1 = random.sample(kitchen_items, 30)
	c2 = random.sample(person, 10)
	c3 = random.sample(sport, 10)
	context_k[i] = c1 + c2 + c3

for i in range(len(person_nouns)) :
	c1 = random.sample(kitchen_items, 10)
	c2 = random.sample(person, 30)
	c3 = random.sample(sport, 10)
	context_p[i] = c1 + c2 + c3

for i in range(len(sports_nouns)) :
	c1 = random.sample(kitchen_items, 10)
	c2 = random.sample(person, 10)
	c3 = random.sample(sport, 30)
	context_s[i] = c1 + c2 + c3

#contexts for nouns
all_noun_context = context_k + context_p + context_s
all_context = kitchen_items + person + sport

#nouns for contexts
all_context_noun = [[] for _ in range(len(all_context))]

for i in range(len(all_context)) :
	common = []
	for j in range(len(all_noun_context)) :
		if all_context[i] in all_noun_context[j] :
			common.append(all_nouns[j])
	all_context_noun[i] = common








