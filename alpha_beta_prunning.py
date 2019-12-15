## state 0, empty
## state 1, my emiter
## state 2, his emiter
## state 3, block
## state 4, controlled by me
## state 5, controlled by him
## state 6, controlled by both


infinity = 2**32

def terminal_test(state):
	a = state["board"]
	n = len(a)
	if(n<7):
		maxd = 10
	if(7<=n<9):
		maxd = 6		
	if(9<=n<12):
		maxd = 4
	if(12<=n<30):
		maxd = 2		
	if(n>=30):
		maxd = 0

	d = state["depth"]
	# print d
	if(d>=maxd): return True # stop if true
	
	for line in a:
		for c in line:
			if(c==0): return False
	return True # loop over all if no valid stop

def utility(state):
	a = state["board"]
	#print state
	my_score = 0
	his_score = 0
	for line in a:
		for c in line:
			if(c==1 or c==4 or c==6): my_score += 1
			if(c==2 or c==5 or c==6): his_score += 1
	#print state, my_score, his_score
	return my_score-his_score

def actions(state):
	a = state["board"]
	n = len(a)
	empty_cell = []
	for i in range(n):
		for j in range(n):
			c = a[i][j]
			if(c==0): empty_cell.append((i,j)) # append on argument tuple
	return empty_cell

def result(state, act):
	a = state["board"]
	d = state["depth"]

	n = len(a)
	a1 = [[a[i][j] for j in range(n)] for i in range(n)]

	row, col = act
	occ, ctr, ctr1 = None, None, None
	if(d%2==0): 
		occ, ctr, ctr1 = 1, 4, 5
	else:
		occ, ctr, ctr1 = 2, 5, 4

	a1[row][col] =  occ


	## direcion 1
	for i in range(1,4):
		row1, col1 = row, col+i
		if(row1<0 or row1>=n or col1<0 or col1>=n): break
		if(a1[row1][col1]==3): break
		
		if(a1[row1][col1] == ctr1 or a1[row1][col1]==6): a1[row1][col1] = 6
		else: a1[row1][col1] = ctr

	## dir 2
	for i in range(1,4):
		row1, col1 = row-i, col+i
		if(row1<0 or row1>=n or col1<0 or col1>=n): break
		if(a1[row1][col1]==3): break
		
		if(a1[row1][col1] == ctr1 or a1[row1][col1]==6): a1[row1][col1] = 6
		else: a1[row1][col1] = ctr

	## dir 3
	for i in range(1,4):
		row1, col1 = row-i, col
		if(row1<0 or row1>=n or col1<0 or col1>=n): break
		if(a1[row1][col1]==3): break
		
		if(a1[row1][col1] == ctr1 or a1[row1][col1]==6): a1[row1][col1] = 6
		else: a1[row1][col1] = ctr

	## dir 4
	for i in range(1,4):
		row1, col1 = row-i, col-i
		if(row1<0 or row1>=n or col1<0 or col1>=n): break
		if(a1[row1][col1]==3): break
		
		if(a1[row1][col1] == ctr1 or a1[row1][col1]==6): a1[row1][col1] = 6
		else: a1[row1][col1] = ctr

	## dir 5
	for i in range(1,4):
		row1, col1 = row, col-i
		if(row1<0 or row1>=n or col1<0 or col1>=n): break
		if(a1[row1][col1]==3): break
		
		if(a1[row1][col1] == ctr1 or a1[row1][col1]==6): a1[row1][col1] = 6
		else: a1[row1][col1] = ctr

	## dir 6
	for i in range(1,4):
		row1, col1 = row+i, col-i
		if(row1<0 or row1>=n or col1<0 or col1>=n): break
		if(a1[row1][col1]==3): break
		
		if(a1[row1][col1] == ctr1 or a1[row1][col1]==6): a1[row1][col1] = 6
		else: a1[row1][col1] = ctr

	## dir 7
	for i in range(1,4):
		row1, col1 = row+i, col
		if(row1<0 or row1>=n or col1<0 or col1>=n): break
		if(a1[row1][col1]==3): break
		
		if(a1[row1][col1] == ctr1 or a1[row1][col1]==6): a1[row1][col1] = 6
		else: a1[row1][col1] = ctr

	## dir 8
	for i in range(1,4):
		row1, col1 = row+i, col+i
		if(row1<0 or row1>=n or col1<0 or col1>=n): break
		if(a1[row1][col1]==3): break
		
		if(a1[row1][col1] == ctr1 or a1[row1][col1]==6): a1[row1][col1] = 6
		else: a1[row1][col1] = ctr

	return {"board":a1, "depth":d+1}


def alpha_beta_serach(state):
	"""define main function of alpha-bete-serach"""
	#print state
	all_actions = actions(state)
	v = -infinity
	opt_action = None
	#alpha = -infinity
	#beta = infinity
	for a in all_actions:
		vi = min_value(result(state,a),-infinity,infinity)
		if(vi>v):
			v = vi
			opt_action = a

	return opt_action


def max_value(state,alpha,beta):
	print "max", state
	if terminal_test(state):
		return utility(state)
	v = -infinity
	for a in actions(state):
		v = max(v,min_value(result(state,a),alpha,beta))
		if v >= beta:
			return v
		alpha = max(alpha,v)
	return v

def min_value(state,alpha,beta):
	print "min", state
	if terminal_test(state):
		return utility(state)
	v = infinity
	for a in actions(state):
		v = min(v,max_value(result(state,a),alpha,beta))
		if v <= alpha:
			return v
		beta = min(beta,v)
	return v


input = open('input00.txt','r')
# N1 = input.readline().strip('\n')
N1 = input.readline().replace('\n','').replace('\r','')
n = int(N1)
# print N1,n
a = []
for i in range(n):
	NN = input.readline().replace('\n','').replace('\r','')
	ai = []
	# print NN
	for x in range(n):
		# print x # x is the index 
		ai.append(int(NN[x]))
	a.append(ai)
print(a)

state0 = {"board":a, "depth":0}

# print terminal_test(state0)
#print utility(state0)
#print actions(state0)
# print result(state0,(1,1))

# print alpha_beta_serach(state0)
# print "optimal action = ",  Minimax_decision(state0) 
opt = alpha_beta_serach(state0)
ro, cl = opt
print opt
filename = 'output.txt'
with open(filename,'w') as zaili:
	zaili.write(str(ro)+" "+str(cl))
