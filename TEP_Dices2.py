#Topicos especiais em programacao - DCC - UFRJ
#Assignment 6 - Dices
#Allan Monteiro David

#Simulates the roll of dices to test which case is most likely
#Three of a number or two pairs
#But in this case we addicted the dice to roll more 6's

import random

def rollDiceAddictIn6():
	rand = random.randint(1, 6*6);

	if(rand > 6):
		rand = 6;

	return rand;

def rollThree():
	return (rollDiceAddictIn6(), rollDiceAddictIn6(), rollDiceAddictIn6());

def rollFour():
	return (rollDiceAddictIn6(), rollDiceAddictIn6(), rollDiceAddictIn6(), rollDiceAddictIn6());

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