#include "Tree_Based_Allocation.h"
#include <time.h>

int main()
{
	srand((unsigned)time(NULL));

	Tree_Based_Allocation Tree;
	Node* node = new Node;

	int K = 4;
	// number of types

	int T[32] = {2, 4, 8, 0};
	// report period of each type of machines

	int I_k = 20;
	// nubmer of type k machines

	int D_max =4;
	// value of d_max 

	int D_ik = rand()%D_max+1;
	// D_ik  ramdomly selected

	node->set_index(1);
	node->set_S(T);

	Tree.PushRoot(node);

	if(!Tree.Construct_Tree())
		cout<<"Construction fail"<<endl;

	Tree.print_tree();
	return 0;
}