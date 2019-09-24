from dataset import *

#Threshold Parameter theta, change depending on the corpus
theta = 0.3

#Contributing factors of the micro score
alpha = 1
beta = 1
gamma = 1

#Function to generate powerset of a list of elements
# def powerset(s) :
# 	result = [[]]
# 	for elem in s:
# 		result.extend([x + [elem] for x in result])
# 	return result

#Function to find length of intersection of two lists
def intersection(lst1, lst2) : 
	lst3 = [value for value in lst1 if value in lst2] 
	return len(lst3) 

#nu
def nu(a, b) :
	common = intersection(a ,b)
	result = common / len(a)
	return result

#Overlap index function omega(A,B)
def omega(a, b) :
	common = intersection(a, b)
	result = (2 * common)/(len(a) + len(b))
	return result


#Three categories 
categories = ['Kitchen Item', 'Person', 'Sport']

#Set of nouns needed to be classified
nouns = all_nouns

#A list of lists to hold the trusted instances of each category
trusted = [[4, 11, 17], [22, 28, 35], [40, 45, 57]]

#A list of lists to hold the indices of the instances promoted to trusted in the previous iteration
new_trusted = trusted

#flag bit list to check if the noun is trusted
# 0 - Not trusted
# 1 - Trusted
flag = [0 for i in range(len(nouns))]
for i in range(len(trusted)) :
	for j in range(len(trusted[i])) :
		flag[trusted[i][j]] = 1
#power_nouns = powerset(nouns)

#Contextual pattens of each noun
contextual_patterns = all_noun_context

#All the contextual patterns
contextual_patterns_all = all_context

#Finding the total number of contextual patterns
total_contextual_patterns = len(contextual_patterns_all)

#Co-occuring nouns for each contextual pattern
noun_co = all_context_noun

#Upper Tolerance class U_a
def U_a(noun) :
	res_set = []
	for i in range(len(contextual_patterns_all)) :
		uncertanity = []
		for j in range(len(contextual_patterns_all)) :
			overlap = omega(noun_co[i], noun_co[j])
			if overlap >= theta :
				uncertanity.append(j)
		context_co = contextual_patterns[noun]
		if nu(uncertanity, context_co) > 0 :
			res_set.append(i)
	return res_set

#Lower Tolerence class L_a
def L_a(noun) :
	res_set = []
	for i in range(len(contextual_patterns_all)) :
		uncertanity = []
		for j in range(len(contextual_patterns_all)) :
			overlap = omega(noun_co[i], noun_co[j])
			if overlap >= theta :
				uncertanity.append(j)
		context_co = contextual_patterns[noun]
		if nu(uncertanity, context_co) == 1 :
			res_set.append(i)
	return res_set

#Micro-score for candidate instance noun2 by trusted instance noun1
def micro(noun1, noun2) :
	res_1 = omega(contextual_patterns[noun1], contextual_patterns[noun2]) * alpha
	res_2 = omega(U_a(noun1), contextual_patterns[noun2]) * beta
	res_3 = omega(L_a(noun1), contextual_patterns[noun2]) * gamma
	#print(res_1 + res_2 + res_3)
	return res_1 + res_2 + res_3

#List for storing micro scores
micro_list = [[]]

#Training the Tolerence Pattern Learner
#Break when needed
while sum(flag) < 60 :
	print(sum(flag))
	for i in range(len(categories)) :
		#macro score for n
		macro = []
		promo_idx = [None, None, None]
		# for j in range(len(new_trusted[i])) :
		# 	ua = U_a(new_trusted[i][j])
		# 	la = L_a(new_trusted[i][j])
			
		# 	for k in range(len(nouns)) :
		# 		if flag[k] == 0 :
		# 			#move nouns from 'nouns' to 'trusted'
		# 			micro(new_trusted[i][j], k)
					
		for k in range(len(nouns)) :
			macro_curr = 0
			if flag[k] == 0 :
				for idx in range(len(trusted[i])) :
					print('here')
					macro_curr = macro_curr + micro(trusted[i][idx] ,k)
			macro.append(macro_curr)
			print(k, 'out of ', len(nouns))
		
		#Ranking instances by macro/|cat|
		for j in range(len(macro)) :
			macro[j] = macro[j] / len(trusted[i])
		print(macro)
		#Getting top three instances
		for j in range(3) :
			promo = max(macro)
			if promo != 0 :
				#print(macro)
				promo_idx[j] = macro.index(promo)
				macro[macro.index(promo)] = 0
		print(promo_idx)
		#Promoting the top three instances
		new_trusted = [[] for _ in range(3)]
		for j in range(3) :
			if promo_idx[j] != None :
				trusted[i].append(promo_idx[j])
				new_trusted[i].append(promo_idx[j])
				flag[promo_idx[j]] = 1

print('Categorized as kitchen items')
print()
for i in range(len(trusted[0])) :
	print(nouns[trusted[0][i]])

print('Person')
print()
for i in range(len(trusted[1])) :
	print(nouns[trusted[1][i]])

print('Sport')
print()
for i in range(len(trusted[2])) :
	print(nouns[trusted[2][i]])




