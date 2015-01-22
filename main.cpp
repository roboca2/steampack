#include "Tree_Based_Allocation.h"
#include <time.h>
#define TYPE1 8
#define TYPE2 12
#define TYPE3 24
#define TYPE4 32



int main()
{
	srand((unsigned)time(NULL));

	
	Node* node = new Node;

	Tree_Based_Allocation Tree;

	if(!Tree.Construct_Tree())
		cout<<"Construction fail"<<endl;

	//Tree.print_tree();

	Tree.Allocater();

	return 0;
}