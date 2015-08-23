import random

DEBUG = False


def isSafe(queen1, queen2):
	if queen1[0] == queen2[0]:
		return False
	if queen1[1] == queen2[1]:
		return False

	for i in range(8):
		if queen1[0] + i == queen2[0] and queen1[1] + i == queen2[1]:
			return False
		if queen1[0] + i == queen2[0] and queen1[1] - i == queen2[1]:
			return False

	return True		


def printKnownError(queens, i, j):
	if DEBUG:
		print(str(i)+':'+str(queens[i])+' '+str(j)+':'+str(queens[j]))	

def doPuzzle(queens):
	N = len(queens)
	for i in range(N):
		for j in range(N):
			if i != j:
				if not isSafe(queens[i], queens[j]):
					printKnownError(queens, i, j)
					return False

	return True




print('testing known errors...')
assert False == doPuzzle( [ (0,0), (0,1) ] )
assert True == doPuzzle( [ (0,0), (1,2) ] )

assert False == doPuzzle( [ (0,0), (1,1) ] )
assert False == doPuzzle( [ (0,1), (1,0) ] )

assert False == doPuzzle( [ (0,0), (2,2) ] )
assert False == doPuzzle( [ (2,2), (0,0) ] )
assert False == doPuzzle( [ (0,0), (3,3) ] )
assert False == doPuzzle( [ (0,0), (7,7) ] )
assert False == doPuzzle( [ (2,2), (5,5) ] )
assert False == doPuzzle( [ (0,1), (1,2) ] )
assert False == doPuzzle( [ (0,1), (2,3) ] )

assert False == doPuzzle( [ (4,4), (3,5) ] )
assert False == doPuzzle( [ (4,4), (2,6) ] )
assert False == doPuzzle( [ (4,4), (1,7) ] )
assert False == doPuzzle( [ (2,2), (0,4) ] )
assert False == doPuzzle( [ (7,0), (0,7) ] )
assert False == doPuzzle( [ (4,5), (2,7) ] )
assert False == doPuzzle( [ (2,7), (4,5) ] )
assert True == doPuzzle( [ (4,5), (2,6) ] )
assert True == doPuzzle( [ (1,5), (2,3) ] )
assert True == doPuzzle( [ (4,5), (2,2) ] )
assert True == doPuzzle( [ (5,2), (4,5) ] )


assert True == doPuzzle( [ (5,2), (4,5), (0,0) ] )
assert False == doPuzzle( [ (5,2), (4,4), (0,0) ] )



print('solving...')

queens = [(5,2), (4,4), (0,0)]


while not doPuzzle(queens):
	queens = []
	N = 5
	for i in range(N):
		queen = (random.randint(0,N-1), random.randint(0,N-1))
		queens.append(queen)
print queens
