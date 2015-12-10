#Topicos especiais em programacao - DCC - UFRJ
#Assignment 1 - Histogram
#Allan Monteiro David

import sys
import math

stepSize = 100;

minPlotNum = 50;
maxPlotNum = 650;

resultArray = {};

inputArray = [ (60, 350), (30, 150), (50, 200), (55, 650), (280, 320), (400, 600), (30, 510), (100, 500), (50, 450) ]

for player in inputArray:
	start = player[0];
	end = player[1];

	if start < minPlotNum:
		start = minPlotNum;
	if end > maxPlotNum:
		end = maxPlotNum;

	i = (start - minPlotNum)/stepSize;
	i = math.ceil(i);
	x = stepSize*i + minPlotNum;
	
	i = (end - minPlotNum)/stepSize;
	i = math.floor(i);
	finalX = stepSize*i + minPlotNum;
	
	while x <= finalX:
		if not x in resultArray:
			resultArray[x] = 0;

		resultArray[x] += 1;
		x += stepSize;

for item in resultArray.items():
	print(item);