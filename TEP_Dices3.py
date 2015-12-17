#Topicos especiais em programacao - DCC - UFRJ
#Assignment 6 - Dices
#Allan Monteiro David

#Simulates the roll of dices to test which case is most likely
#In three rolls:
#   to get the first and third different
#   or to get the first and second different given that the first is different than the third

import random

def rollThree():
	return (random.randint(1, 6), random.randint(1, 6), random.randint(1, 6));

def testProbabilities():
	numberOf1Dif2GivenDif3 = 0;
	numberOf1Dif3 = 0;

	numberOfTests = 1000000;

	for _ in range(0, numberOfTests):
		result = rollThree();
		if(result[0] != result[2]):
			numberOf1Dif3 += 1;
			if(result[0] != result[1]):
				numberOf1Dif2GivenDif3 += 1;

	print("1!=2: "+str(numberOf1Dif3/numberOfTests)+"\n"+"1!=3 given 1!=2: "+str(numberOf1Dif2GivenDif3/numberOf1Dif3));

testProbabilities();