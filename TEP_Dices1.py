#Topicos especiais em programacao - DCC - UFRJ
#Assignment 6 - Dices
#Allan Monteiro David

#Simulates the roll of dices to test which case is most likely
#Three of a number or two pairs

import random

def rollThree():
	return (random.randint(1, 6), random.randint(1, 6), random.randint(1, 6));

def rollFour():
	return (random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6));

def testProbabilities():
	numberOfThrees = 0;
	numberOfTwoPairs = 0;

	numberOfTests = 1000000;

	for _ in range(0, numberOfTests):
		result = rollThree();
		if(result[0] == result[1] == result[2]):
			numberOfThrees += 1;
			
		result = rollFour();
		if(result[0] == result[1] and result[2] == result[3]):
			numberOfTwoPairs += 1;

	print("Threes: "+str(numberOfThrees)+"\n"+"Two Pairs: "+str(numberOfTwoPairs));

testProbabilities();