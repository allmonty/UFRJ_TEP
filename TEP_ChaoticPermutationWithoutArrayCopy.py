#Topicos especiais em programacao - DCC - UFRJ
#Assignment 2 - Chaotic Permutation
#Allan Monteiro David

#Simple Version,
#without the necessity of copying the list in the recursion.

#Finds the chaotic permutation given N elements 

import sys

N = 4;

def findChaosPermut(myList, count):
	if(count == N):
		print(myList);
	else:
		for i in range(0, N):
			if(i != count and (i not in myList)):
				myList.append(i);
				findChaosPermut(myList, count + 1);
				myList.pop(len(myList) - 1);

findChaosPermut([], 0);