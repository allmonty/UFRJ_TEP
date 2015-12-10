#Topicos especiais em programacao - DCC - UFRJ
#Assignment 1 - Histogram
#Allan Monteiro David

import sys
import math

stepSize = 100;

minPlotNum = 50;
maxPlotNum = 650;

pMap = {50:0, 150:0, 250:0, 350:0, 450:0, 550:0, 650:0, 750:0};

result = {50:0, 150:0, 250:0, 350:0, 450:0, 550:0, 650:0}

inputArray = [ (60, 350), (30, 150), (50, 200), (55, 650), (280, 320), (400, 600), (30, 510), (100, 500), (50, 450) ]

for player in inputArray:
	start = player[0];
	end = player[1];

	if end < minPlotNum:
		continue;

	start = max(start, minPlotNum);
	end = min(end, maxPlotNum + stepSize);

	i = (start - minPlotNum)/stepSize;
	i = math.floor(i);
	pIn = stepSize*i + minPlotNum;

	pMap[pIn] += 1;
	
	j = (end - minPlotNum)/stepSize;
	j = math.ceil(j);
	pOut = stepSize*j + minPlotNum;

	pMap[pOut] -= 1;

numOfActualPlayers = 0;
for i in result.keys():
	numOfActualPlayers = pMap[i];
	if numOfActualPlayers < 0:
		numOfActualPlayers = 0;
	result[i] = numOfActualPlayers;

for item in result.items():
	print(item);