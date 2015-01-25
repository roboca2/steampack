
#include "Tree_Based_Allocation.h"


Tree_Based_Allocation::Tree_Based_Allocation()
{
	K=4;
	I_k = 20;
	memset(T, 0, 32*sizeof(int));
	T[0] = TYPE1;
	T[1] = TYPE2;
	T[2] = TYPE3;
	T[3] = TYPE4;

	D_ik = new int*[K];
	N_k = new int[K];

	memset(N_k, 0, K*sizeof(int));

	for(int i=0; i<K; i++)
	{
		D_ik[i] = new int[I_k];
		for(int j=0; j<I_k; j++)
		{
			//D_ik[i][j] = rand()%D_max+1;
			D_ik[i][j] = 1;
			N_k[i] += D_ik[i][j];
			cout<<D_ik[i][j]<<" ";
		}
		// D_ik  ramdomly selected
		cout<<"     "<<N_k[i]<<endl;
	}

	t = 1;
	
	for(int i=0; i<32; i++)
	{
		T_p [i] = 0;
		T_p1[i] = 0;
		T_p2[i] = 0;
		t_p [i] = 0;
		t_p1[i] = 0;
		t_p2[i] = 0;
		P[i] = 0;
		Q[i] = 0;
	}
	gcd = 0;
	J_s = 0;
	// initialize
}


Tree_Based_Allocation::~Tree_Based_Allocation(void)
{

}
void Tree_Based_Allocation::Initialize()
{
	for(int i=0; i<32; i++)
	{
		T_p1[i] = 0;
		T_p2[i] = 0;
		t_p [i] = 0;
		t_p1[i] = 0;
		t_p2[i] = 0;
		P[i] = 0;
		Q[i] = 0;
	}
	J_s = 0;
}
void Tree_Based_Allocation::PushRoot()
{
	root = new Node;
	root->set_index(t);
	root->set_S(T);

	U.push_back(root);
	root_child.push_back(root);
}

bool Tree_Based_Allocation::Construct_Tree()
{
	PushRoot();
	int step=1;
	
	while(step)
	{
		if(step == 1)
		{
			step = tree_1();
			if(step == -1) 
				break;
		}

		else if(step == 2) 
		{
			step = tree_2();
			Initialize();
		}

		else if(step == 3)
		{ 
			step = tree_3();
			Initialize();
		}	
		else
		{
			cout<<"Construct error"<<endl;
			break;
		}
	}
	
	return true;
}

Node* Tree_Based_Allocation::get_root()
{
	return root;
}

int Tree_Based_Allocation::tree_1()
{
	////STEP1///////////////////////////////////////////////////////////

	if(U.empty()) return 0;
	// Algorithm is already Construct tree structure


	/* U is not empty, this is case 'otherwise' */
	
	int *n_S=new int[32];
	memset(n_S, 0, 32*sizeof(int));

	n_Node = U[0];
	//  pick arbitrarily node n.

	
	C_n.clear();
	n_S = n_Node->get_S();
	// if this part is error, then dynamic allocate n_S
	memset(T_p, 0, 32);
	for(int i=0; i<32; i++)
	{
		if(n_S[i]==0)break;
		T_p[i] = n_S[i];
	}
	// T_parent = S_n

	return 2;
	////STEP1 END///////////////////////////////////////////////////////////
}

int Tree_Based_Allocation::tree_2()
{
	int j,q;
	j=0;q=0;
	int argmax= 0;
	// using determine j_star

	int remainder =0;

	////STEP2///////////////////////////////////////////////////////
	if(!Calculator())
	{
		cout<<"Calculate error"<<endl;
		return -1;
	}
		//// Determine J* ///////////////////////////////////////////////////
	for(int i=0; i<32; i++)
	{
		if(Q[i]==0)break;
		if(argmax <= Q[i])
		{
			if(argmax == Q[i])
			{
				if(P[J_s] < P[i])
				{
					argmax = Q[i];
					J_s = i;
				}
			}
			// if j_star is not unique, select the one for which prime factor is the largest among them.

			else
			{
				argmax = Q[i];
				J_s = i;
			}		
		}
	}

		
	if(Q[J_s] > 0)
	{
		// divide T_parent = T(1)_parent U T(2)_parent
		// first, ~T(1)_parent, ~T(2)_parent
		for(int i=0; i<32; i++)
		{
			if(t_p[i] == 0) break;
			remainder = t_p[i]%P[J_s];

			if(remainder == 0) // it is divisable, so ~T(1)_parent's elements
			{
				t_p1[j] = t_p[i];
				j++;
			}
			else // it is not divisable, so ~T(2)_parent's elements
			{
				t_p2[q] = t_p[i];
				q++;
			}
		}
		// second, using gcd change ~T(1)_parent, ~T(2)_parent to T(1)_parent, T(2)_parent
		int T_p1_num =0;
		for(int i=0; i<32; i++)
		{
			if(t_p1[i] == 0) 
			{
				T_p1_num = i;
				break;
			}
			T_p1[i] = t_p1[i] * gcd;
		}

		for(int i=0; i<32; i++)
		{
			if(t_p2[i] == 0)
				break;
			T_p2[i] = t_p2[i] * gcd;
		}

		if(T_p1_num > 1)
		{
			int* T_p1_temp = new int[32];
			memset(T_p1_temp,0,32*4);
			for(int i=0; i<32; i++)
			{
				T_p1_temp[i] = T_p1[i];
				if(T_p1[i+1]==0)break;
			}
			C_n.push_back(T_p1_temp);
			//add T(1)_parent into C_n

			memset(T_p,0,32);

			for(int i=0; i<32; i++)
			{
				if(T_p2[i]==0)break;
				T_p[i] = T_p2[i];
			}
			// T_parent <---T(2)_parent;

			if(T_p[0] != 0) return 2;
			else return 3;
		}

		else if(T_p1_num==1)
		{
			int* T_p1_temp = new int[32];
			memset(T_p1_temp,0,32*4);
			T_p1_temp[0] = T_p1[0];
			
			C_n.push_back(T_p1_temp);
			return 3;
		}
	}

	////STEP2 END///////////////////////////////////////////////////
}

int Tree_Based_Allocation::tree_3()
{
	n_Node = U[0];
	U.pop_front();
	int size = C_n.size();

	if(size>1)
	{
		for(int i=0; i<size; i++)
		{
			t++;
			Node* t_Node = new Node;
			t_Node->set_index(t);
			t_Node->set_S(C_n[i]);
			n_Node->set_child(t_Node);
			U.push_back(t_Node);
			root_child.push_back(t_Node);
		}
		return 1;
	}

	else if(C_n.size() == 1)
	{
		n_Node->set_leaf(true);
		return 1;
	}
}

bool Tree_Based_Allocation::Calculator()
{
	Cal_gcd(T_p);
	//// ~T_parent /////////////////////////////////////////////////////////
	for(int i=0; i<32; i++)
	{	
		if(T_p[i] == 0) break;
		// nubmer of element of T_p is two, gcd is T_p[0]
		t_p[i] = T_p[i]/gcd;
	}
	//// ~T_parent END ///////////////////////////////////////////////////

	Prime_factor();
	// caculate P(~T_parent), Q(~T_parent)
	return true;
}

int Tree_Based_Allocation::GCD(int a, int b)
{
	int A=a;
	int B=b;
	int C =0;

	while(true)
	{
		C = A%B;

		if(C == 0)
			break;
		A=B;
		B=C;
	}

	return B;
	// return GCD
}
int Tree_Based_Allocation::Cal_gcd(int* a)
{
	gcd =a[0];
	
	if(!gcd)
	{
		cout<<"list is empty"<<endl;
		return false;
	}

	for(int i=1; i<32; i++)
	{	
		if(a[i] == 0)
			break;

		gcd = GCD(gcd, a[i]);
		// calculate GCD between (gcd,T_p[i]), after this for loop, finaly we have real gcd 
	}
	return gcd;
	//// GCD END ///////////////////////////////////////////////////
}

void Tree_Based_Allocation::Prime_factor()
{
	int n,k,j,q;
	n=0;k=0;j=0;q=0;
	// index variables

	int p_num=0;
	int remainder=0;
	int target =0;
	// p_num : prime number
	// remainder : remainder (in division)
	// target : t_p[i], current target integer

	int Prime_x[32][32] = {0,};
	int Prime_X[32] = {0,};

	for(int i=0; i<32; i++)
	{
		remainder=0; j=0;
		// initialization

		target = t_p[i];
		// current x which includes t_p
		// ~T_parent's i-th period

		if(!target) break;
		// end of array, break for loop!

		for(p_num=1; ;p_num++) // Prime number is start "2"
		{
			remainder = target%p_num;
			// if remainder is zero, it is dividable

			if(target == 1)
			{
				Prime_x[i][j] = target;
				j++;
				break;
				// if target is 1, we already have prime factors, so keep 1, end this loop
			}

			if(!remainder)
				// if remainder is zero, it is prime factor.
			{
				target = target/p_num;
				// divide

				Prime_x[i][j]=p_num;
				j++;
				// increase j
				if(p_num != 1)
					p_num --;
				// if p_num is prime factor, repeat this operation
			}

		}
	}


	///////////Prime_X///////////////////////////////////// 1 2 3
	for(int i=0; i<32; i++)
	{
		if(Prime_x[i][j] ==0)break;

		for(int j=0; j<32; j++)
		{
			if(Prime_x[i][j] ==0)break;

			for(k=0; k<32; k++)
			{
				if(Prime_x[i][j] == P[k])
				{	
					Q[k]++;
					break;
				}	
			}

			if(k == 32)
			{
				P[q] = Prime_x[i][j];
				Q[q]++;
				q++;
			}
		}
	}


	for(int i=0; i<32; i++)
	{
		if(P[i] == 0)break;
		if(P[i]==1) Q[i]=1;
		cout<<P[i]<<"("<<Q[i]<<" times"<<")"<<"  ";
	}
	cout<<endl;

}

void Tree_Based_Allocation::print_tree()
{
	int i=0;
	int* S_n = new int[32];
	memset(S_n,0,32);

	deque<Node*> child = root->get_child();
	
	S_n = root->get_S();
	cout<<endl<<"<< NODE "<<root->get_index()<<" >>"<<endl;
	cout<<"S_n :{";
	for(int i=0; i<32; i++)
	{
		if(S_n[i]==0)
		{
			cout<<"}"<<endl;
			break;
		}
		if(i) cout<<", ";
		cout<<S_n[i];
			
	}
	cout<<endl;

	while(1)
	{
		if(child.empty()) break;
		cout<<"<< NODE "<<child[0]->get_index()<<" >>";
		if(child[0]->get_leaf() == true) cout<<" (LEAF NODE)"<<endl;
		S_n = child[0]->get_S();
		cout<<"S_n :{";
		for(int i=0; i<32; i++)
		{
			if(S_n[i]==0)
			{
				cout<<"}"<<endl;
				break;
			}
			if(i) cout<<", ";
			cout<<S_n[i];
			
		}
		cout<<endl;
		child.pop_front();
		memset(S_n,0,32);
	}
}

Node* Tree_Based_Allocation::search(int index)
{
	int len = root_child.size();

	for(int i=0; i<len; i++)
	{
		if(root_child[i]->get_index() == index)
			return root_child[i];
	}

}

bool Tree_Based_Allocation::Allocater()
{
	U.clear();
	L_n.clear();
	f = new double[t];
	memset(f, 0, t*sizeof(double));
	Cal_f(1);
	root->set_channels(Cal_R_tree(f));
	int step=1;
	
	while(step)
	{
		if(step == 1)
		{
			step = allocate_1();
			if(step == -1) 
				break;
		}

		else if(step == 2) 
		{
			step = allocate_2();
			Initialize();
		}

		else if(step == 3)
		{ 
			step = allocate_3();
			Initialize();
		}	
		else
		{
			cout<<"Construct error"<<endl;
			break;
		}
	}
	
	return true;
}

int Tree_Based_Allocation::allocate_1()
{
	if(U.empty())
		return -1;
	// if U = NULL, finish the algorithm

	n_Node = U[0];
	// otherwise pick arbitrarily a node n, which has been allocated f_n level-Gn subchannels
	
	U.pop_front();
	// remove this node from U

	L_n = n_Node->get_child();
	// L_n denote the set of child nodes of node n;

	

	if(n_Node->get_leaf())
		return 3;
	// node n is leaf node-> go to step3
	else
		return 2;
	// node n is non-leaf node -> go to step2
	
}
int Tree_Based_Allocation::allocate_2()
{

	return 1;
}
int Tree_Based_Allocation::allocate_3()
{
	return 1;
}

int Tree_Based_Allocation::Cal_R_tree(double* f)
{
	double R_tree = 0.0;
	R_tree = f[0] / root->get_G();

	return ceil(R_tree);
}

int Tree_Based_Allocation::Cal_f(int node_index)
{
	Node* cur_node = search(node_index);
	deque<Node*> child = cur_node->get_child();

	cur_node->set_G(Cal_gcd(cur_node->get_S()));
	// setting G
	int size = child.size();

	int* V_n = cur_node->get_S();

	double f_n=0.0;
	double T_k=0.0;
	double r_value=0.0;
	double G_i =0.0;
	if(cur_node->get_leaf())
	{
		for(int i=0; i<4; i++)
		{
			if(V_n[i] == 0)
				break;
			else if(V_n[i] == TYPE1)
			{
				T_k = TYPE1;
				f_n =  (N_k[0]*cur_node->get_G())/T_k;
				f[node_index-1] += ceil(f_n);
			}
			
			else if(V_n[i] == TYPE2)
			{
				T_k = TYPE2;
				f_n = (N_k[1]*cur_node->get_G())/T_k;
				f[node_index-1] += ceil(f_n);
			}
			
			else if(V_n[i] == TYPE3)
			{
				T_k = TYPE3;
				f_n = (N_k[2]*cur_node->get_G())/T_k;
				f[node_index-1] += ceil(f_n);
			}
			
			else if(V_n[i] == TYPE4)
			{
				T_k = TYPE4;
				f_n = (N_k[3]*cur_node->get_G()) / T_k;
				f[node_index-1] += ceil(f_n);
			}
			else
				break;

		}
		return f[node_index-1];
	}
	else
	{
		for(int i=0; i<size; i++)
		{
			G_i = Cal_gcd(child[i]->get_S());
			r_value = Cal_f(child[i]->get_index());
			r_value = (r_value * (cur_node->get_G())) / G_i;
			f[node_index-1] += ceil(r_value);
		}
	}
	return 0;
}


