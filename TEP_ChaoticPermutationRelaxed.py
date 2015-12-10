#Topicos especiais em programacao - DCC - UFRJ
#Assignment 2 - Chaotic Permutation
#Allan Monteiro David

#Version with restriction relaxation,
#enabling k elements to exist in their homes

#Finds the chaotic permutation given N elements 

import sys

N = 3;
K = 2; #Relaxamento da restricao

def findChaosPermut(myList, nCount, kCount):
	if(nCount == N):
		print(myList);
	else:
		for i in range(0, N):
			if(i == nCount):
				kCount += 1;
			if(kCount <= K or i != nCount):
				if(i not in myList):
					newList = myList[:];
					newList.append(i);
					findChaosPermut(newList, nCount + 1, kCount);

findChaosPermut([], 0, 0);