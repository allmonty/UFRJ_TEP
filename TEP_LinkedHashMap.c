//Topicos especiais em programacao - DCC - UFRJ
//Assignment 5 - linked hash map
//Allan Monteiro David

//My own linked hash map.
//A hash map used when you want to have a fixed sized hash map.
//When it's full and you want to add another element, it will remove the
//less recently accessed element from the hash map.

#include <stdio.h>
#include <stdlib.h>

int LINKEDHASHMAP_SIZE = 0;
int LINKEDHASHMAP_MAXNUMOFELEMENTS = 10;
float LINKEDHASHMAP_LOADFACTOR = 2;

struct HashElement
{
	struct HashElement* nextInHash;
	struct HashElement* previousInHash;
	struct HashElement* nextInOrder;
	struct HashElement* previousInOrder;
	int key;
	int info;
};

struct LinkedHashMap
{
	struct HashElement** list;
	int numberOfElements;
	struct HashElement* firstInOrder; //more recently accessed
	struct HashElement* lastInOrder;  //less recently accessed
} linkedHashMap;

void initLinkedHashMap()
{
	LINKEDHASHMAP_SIZE = (int) LINKEDHASHMAP_MAXNUMOFELEMENTS / LINKEDHASHMAP_LOADFACTOR;
	linkedHashMap.list = (struct HashElement**) malloc (sizeof(struct HashElement*) * LINKEDHASHMAP_SIZE);
	linkedHashMap.numberOfElements = 0;
	linkedHashMap.firstInOrder = NULL;
	linkedHashMap.lastInOrder = NULL;
}

int hashFunction(int key)
{
	return key % LINKEDHASHMAP_SIZE;
}

struct HashElement* findInHash(int key)
{
	int hashedKey = hashFunction(key);

	if(linkedHashMap.list[hashedKey] == NULL)
	{
		printf("FindInHash: There was no element with key: %d!\n", key);
		return NULL;
	}
	else
	{
		struct HashElement* actualHashElement = linkedHashMap.list[hashedKey];
		while(actualHashElement->key != key)
		{
			if(actualHashElement->nextInHash == NULL)
			{
				printf("FindInHash: There was no element with key: %d!\n", key);
				return NULL;
			}
			else
			{
				actualHashElement = actualHashElement->nextInHash;
			}
		}
		return actualHashElement;
	}
}

void putElementAsFirstInOrder(struct HashElement* element)
{	
	if(linkedHashMap.firstInOrder == element)
		return;

	if(linkedHashMap.lastInOrder == NULL)
		linkedHashMap.lastInOrder = element;

	if(linkedHashMap.firstInOrder != NULL)
		linkedHashMap.firstInOrder->nextInOrder = element;
	
	if(element->previousInOrder != NULL)
		element->previousInOrder->nextInOrder = element->nextInOrder;
	
	if(element->nextInOrder != NULL)
		element->nextInOrder->previousInOrder = element->previousInOrder;

	element->nextInOrder = NULL;
	element->previousInOrder = linkedHashMap.firstInOrder;

	linkedHashMap.firstInOrder = element;
}

void removeElementInOrder(struct HashElement* element)
{	
	if(element->previousInOrder != NULL)
		element->previousInOrder->nextInOrder = element->nextInOrder;
	
	if(element->nextInOrder != NULL)
		element->nextInOrder->previousInOrder = element->previousInOrder;

	if(linkedHashMap.firstInOrder == element)
	{
		linkedHashMap.firstInOrder = element->previousInOrder;
		linkedHashMap.firstInOrder->nextInOrder = NULL;
	}
	if(linkedHashMap.lastInOrder == element)
	{
		linkedHashMap.lastInOrder = element->nextInOrder;
		linkedHashMap.lastInOrder->previousInOrder = NULL;
	}
}

void deleteInHash(int key)
{
	struct HashElement* auxElement = findInHash(key);
	
	if(auxElement == NULL)
	{
		printf("DeleteInHash: did nothing.\n");
	}
	else
	{
		removeElementInOrder(auxElement);

		int hashedKey = hashFunction(key);

		if(linkedHashMap.list[hashedKey] == auxElement)
			linkedHashMap.list[hashedKey] = auxElement->nextInHash;

		if(auxElement->previousInHash != NULL)
			auxElement->previousInHash->nextInHash = auxElement->nextInHash;
		if(auxElement->nextInHash != NULL)
			auxElement->nextInHash->previousInHash = auxElement->previousInHash;
		
		free(auxElement);
		auxElement = NULL;
		linkedHashMap.numberOfElements -= 1;
	}
}

void removeLastElementInOrder()
{
	if(linkedHashMap.lastInOrder != NULL)
	{
		deleteInHash(linkedHashMap.lastInOrder->key);
	}
}

void insertInHash(int key, int info)
{
	struct HashElement* newHashElement = (struct HashElement*) malloc(sizeof(struct HashElement));
	newHashElement->info = info;
	newHashElement->key = key;

	int hashedKey = hashFunction(key);

	if(linkedHashMap.list[hashedKey] == NULL)
	{
		linkedHashMap.numberOfElements += 1;
		if(linkedHashMap.numberOfElements > LINKEDHASHMAP_MAXNUMOFELEMENTS)
		{
			removeLastElementInOrder();
		}

		linkedHashMap.list[hashedKey] = newHashElement;
		putElementAsFirstInOrder(newHashElement);
	}
	else
	{
		linkedHashMap.numberOfElements += 1;
		if(linkedHashMap.numberOfElements > LINKEDHASHMAP_MAXNUMOFELEMENTS)
		{
			removeLastElementInOrder();
		}

		struct HashElement* actualHashElement = linkedHashMap.list[hashedKey];
		while(actualHashElement->nextInHash != NULL)
		{
			actualHashElement = actualHashElement->nextInHash;
		}
		actualHashElement->nextInHash = newHashElement;
		newHashElement->previousInHash = actualHashElement;
		putElementAsFirstInOrder(newHashElement);
	}
}

int accessInHash(int key)
{
	struct HashElement* auxElement = findInHash(key);
	
	if(auxElement == NULL)
	{
		printf("AccessInHash: returned zero.\n");
		return 0;
	}
	else
	{
		putElementAsFirstInOrder(auxElement);
		return auxElement->info;
	}
}

void printOrder()
{
	printf("=======ORDER======\n");
	struct HashElement* auxElement = linkedHashMap.lastInOrder;
    while(auxElement != NULL)
    {
    	printf("-> %d", auxElement->info);
    	auxElement = auxElement->nextInOrder;
    }
    printf("\n=======ORDER======\n");
}

void printReverseOrder()
{
	printf("=======REVERSEORDER======\n");
	struct HashElement* auxElement = linkedHashMap.firstInOrder;
    while(auxElement != NULL)
    {
    	printf("-> %d", auxElement->info);
    	auxElement = auxElement->previousInOrder;
    }
    printf("\n=======REVERSEORDER======\n");
}

void printHashMap()
{
	printf("=======HASH======\n");
	int i = 0;
	struct HashElement* pointer = NULL;
	for(i = 0; i < LINKEDHASHMAP_SIZE; i++)
	{
		pointer = linkedHashMap.list[i];
		printf("line %d:  ", i);
		while(pointer != NULL)
		{
			printf("%d  ", pointer->key);
			pointer = pointer->nextInHash;
		}
		printf("\n");
	}
    printf("=======HASH======\n");
}

main()
{
	initLinkedHashMap();

	//test of behaviour
	int i = 0;
	for(i = 0; i < 13; i++)
	{
		insertInHash(i, i*10);
		printf("Num of elements: %d\n", linkedHashMap.numberOfElements);
		printOrder();
    	printReverseOrder();
    	printHashMap();
    	printf("\n");
	}
}






