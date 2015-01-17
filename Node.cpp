#include "Node.h"
 

Node::Node(void)
{
	index=0;
	G=0;
	leaf=false;
	memset(S, 0, 32);
}


Node::~Node(void)
{
}

void Node::set_index(int new_index)
{
	index = new_index;
}

void Node::set_G(int new_G)
{
	G = new_G;
}

void Node::set_S(int* new_S)
{
	for(int i=0; i<32; i++)
		S[i]=new_S[i];
}

void Node::set_leaf(bool new_leaf)
{
	leaf = new_leaf;
}

void Node::set_child(Node* new_child)
{
	Child.push_back(new_child);
}


int Node::get_index()
{
	return index;
}

int Node::get_G()
{
	return G;
}

int* Node::get_S()
{
	return S;
}

bool Node::get_leaf()
{
	return leaf;
}

 deque<Node*> Node::get_child()
{
	return Child;
}