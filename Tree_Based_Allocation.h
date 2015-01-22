#pragma once
#include "Node.h"

class Tree_Based_Allocation
{
private:
	deque<Node*> U;
	// list of nodes which have been not been processed

	deque<int*> C_n;
	
	deque<Node*> L_n;


	deque<Node*> root_child;

	int t;
	// number of node in the tree

	Node* n_Node;

	Node* root;

	int T_p[32];
	// T_parent
	int T_p1[32];
	// T_parent1
	int T_p2[32];
	// T_parent2

	int t_p[32];
	// ~T_parent
	int t_p1[32];
	// ~T_parent1
	int t_p2[32];
	// ~T_parent2

	int J_s;
	
	int P[32];
	int Q[32];

	int gcd;

	double* f;

	int** D_ik;
	int* N_k;

	int I_k;
	// nubmer of type k machines

	int D_max;
	// value of d_max 

	int K;
	// number of types
	//int T[32] = {2,4,8, 0};
	int T[32];
	// report period of each type of machines

public:
	Tree_Based_Allocation();
	~Tree_Based_Allocation(void);

	void PushRoot();
	void Initialize();

	bool Construct_Tree();
	void print_tree();

	int tree_1();
	int tree_2();
	int tree_3();

	bool Calculator();
	int GCD(int a, int );
	void Prime_factor();
	
	int Cal_gcd(int* a);
	bool Allocater();

	int allocate_1();
	int allocate_2();
	int allocate_3();

	int Cal_R_tree(double* f);
	int Cal_f(int node_index);
	
	Node* get_root();
	Node* search(int index);
};
