#Topicos especiais em programacao - DCC - UFRJ
#Assignment 3 - Limited Subgroups
#Allan Monteiro David

#Optimized version!!!

#Given n, t_min and t_max: generate all subsets of
#{1, 2, ..., n} with size between t_min and t_max (inclusive)

import sys

N = 5;
t_Min = 2;
t_Max = 4;

result = [];

def findSubgroups(lista, iniNum):
	if(iniNum <= N):
		lista.append(iniNum);
		if(len(lista) >= t_Min and len(lista) <= t_Max):
			newLista = lista[:];
			result.append(newLista);
		if(len(lista) < t_Max):
			findSubgroups(lista, iniNum + 1);
		lista.pop(len(lista) - 1);
		if(len(lista) < t_Max):
			findSubgroups(lista, iniNum + 1);

def runProgram():
	findSubgroups([], 1);
	print("Total de subgrupos: "+str(len(result)));
	for lista in result:
		print(lista);

runProgram();
