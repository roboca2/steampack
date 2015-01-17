#pragma once
#include "Node.h"

class Tree_Based_Allocation
{
private:
	deque<Node*> U;
	// list of nodes which have been not been processed
	deque<int*> C_n;
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

	int p_x;
	int q_x;
	int i_x;
	int m_x;
	int J_s;
	
	int P[32];
	int Q[32];

	int gcd;


public:
	Tree_Based_Allocation(void);
	~Tree_Based_Allocation(void);

	void PushRoot(Node* root);

	bool Construct_Tree();
	void print_tree();
	bool STEP1();
	int STEP2();
	void STEP3();

	bool Calculator();
	int GCD(int a, int );
	void Prime_factor();
	Node Search(int* U);
	void Initialize();
};
