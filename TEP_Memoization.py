#Topicos especiais em programacao - DCC - UFRJ
#Assignment 4 - Memoization
#Allan Monteiro David

#Calculates the number x that maximizes g(x) between Nmin and Nmax.
#g(x) = 1 + g(f(x))
#f(x) = if x is even: n/2
#       if x is odd: 3*n + 1

def f(n):
	if n % 2 == 0 :
		return (n/2)
	else:
		return (3*n + 1)

def g(n):
	if n == 1:
		return 1;
	else:
		if n not in memo:
			resp = 1 + g(f(n))
			if len(memo) <= memoMaxSize:
				memo[n] = resp
			return resp
		else:
			return memo[n]

Nmin = 1
Nmax = 10000000

memo = {}
memoMaxSize = 1000000000

def calcMax():
	result = 0
	n = 0
	for i in range(Nmin, Nmax + 1):
		aux = g(i)
		if aux > result:
			result = aux
			n = i
	return result, n

answer, N = calcMax()
print("N = " + str(N) + " | Result: " + str(answer))