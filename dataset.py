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


#co-occurence matrix of size n x m for n nouns and m context_patterns
total_nouns_len = len(person_nouns) + len(sports_nouns) + len(kitchen_nouns)
total_context_len = len(kitchen_items) + len(sport) + len(person)
co_matrix = [[0 for i in range(total_context_len)] for j in range(total_nouns_len)]

# co_kitchen = [[0 for i in range(len(kitchen_items))] for j in range(len(kitchen_nouns))]
# co_person = [[0 for i in range(len(person))] for j in range(len(person_nouns))]
# co_sport = [[ 0 for i in range(len(sport))] for j in range(len(sports_nouns))]

rand_temp_in = [1, 2, 3]
rand_temp_not_in = [0, 1]

#initializing co-occurence matrix
#for the kitchen nouns
for i in range(0, len(kitchen_nouns)) :
	for j in range(len(co_matrix[i])) :
		if j in range(0, len(kitchen_items)) :
			co_matrix[i][j] = random.choice(rand_temp_in)
		else :
			co_matrix[i][j] = random.choice(rand_temp_not_in)

#for person nouns
for i in range(len(kitchen_nouns), len(kitchen_nouns) + len(person_nouns)) :
	for j in range(len(co_matrix[i])) :
		if j in range(len(kitchen_items), len(kitchen_items) + len(person)) :
			co_matrix[i][j] = random.choice(rand_temp_in)
		else :
			co_matrix[i][j] = random.choice(rand_temp_not_in)

#for sports nouns
for i in range(len(kitchen_nouns) + len(person_nouns), total_nouns_len) :
	for j in range(len(co_matrix[i])) :
		if j in range(len(kitchen_items) + len(person), total_context_len) :
			co_matrix[i][j] = random.choice(rand_temp_in)
		else :
			co_matrix[i][j] = random.choice(rand_temp_not_in)


# for row in co_matrix :
# 	print(row)



# for i in range(len(co_person)) :
# 	for j in range(len(co_person[i])) :
# 		co_person[i][j] = random.choice(rand_temp)

# for i in range(len(co_sport)) :
# 	for j in range(len(co_sport[i])) :
# 		co_sport[i][j] = random.choice(rand_temp)


# def pr(mat) :
# 	for row in mat :
# 		print(row)

# pr(co_kitchen)
# print()
# pr(co_person)
# print()
# pr(co_sport)



# context_k = [[] for _ in range(len(kitchen_nouns))]
# context_p = [[] for _ in range(len(person_nouns))]
# context_s = [[] for _ in range(len(sports_nouns))]
# all_nouns = kitchen_nouns + person_nouns + sports_nouns

# for i in range(len(kitchen_nouns)) :
# 	curr_noun_context = []
# 	for j in range(len(co_kitchen[i])) :
# 		curr_noun_context.append()
# 	context_k[i] = 


# for i in range(len(person_nouns)) :
# 	c1 = random.sample(kitchen_items, 10)
# 	c2 = random.sample(person, 30)
# 	c3 = random.sample(sport, 10)
# 	context_p[i] = c1 + c2 + c3

# for i in range(len(sports_nouns)) :
# 	c1 = random.sample(kitchen_items, 10)
# 	c2 = random.sample(person, 10)
# 	c3 = random.sample(sport, 30)
# 	context_s[i] = c1 + c2 + c3

#contexts for nouns
all_nouns = kitchen_nouns + person_nouns + sports_nouns
all_noun_context = [[] for _ in range(total_nouns_len)]

for i in range(len(co_matrix)) :
	common = []
	for j in range(len(co_matrix[0])) :
		#get the current context
		if j in range(0, len(kitchen_items)) :
			context = kitchen_items[j]
		elif j in range(len(kitchen_items), len(kitchen_items) + len(person)) :
			context = person[j - len(kitchen_items)]
		else :
			context = sport[j - len(kitchen_items) - len(person)]

		#append (context X co_matrix[i][j]) to common
		for k in range(co_matrix[i][j]) :
			common.append(context)

	all_noun_context[i] = common



all_context = kitchen_items + person + sport
#nouns for contexts
all_context_noun = [[] for _ in range(total_context_len)]

for i in range(len(co_matrix[0])) :
	common = []
	for j in range(len(co_matrix)) :
		#get the current noun
		if j in range(0, len(kitchen_nouns)) :
			noun = kitchen_nouns[j]
		elif j in range(len(kitchen_nouns), len(kitchen_nouns) + len(person_nouns)) :
			noun = person_nouns[j - len(kitchen_nouns)]
		else :
			noun = sports_nouns[j - len(kitchen_nouns) - len(person_nouns)]

		#append (noun X co_matrix[i][j]) to common
		for k in range(co_matrix[j][i]) :
			common.append(noun)

	all_context_noun[i] = common


# for row in all_noun_context :
# 	print(row)

# print()

# for row in all_context_noun :
# 	print(row)
# print()


# for i in range(len(all_context)) :
# 	common = []
# 	for j in range(len(all_noun_context)) :
# 		if all_context[i] in all_noun_context[j] :
# 			common.append(all_nouns[j])
# 	all_context_noun[i] = common




