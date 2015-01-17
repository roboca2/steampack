#pragma once
#include <string.h>
#include <deque>
#include <iostream>
using namespace std;

class Node
{
private:
	int index;
	// index of node

	int G;
	// GCD of S

	int S[32];
	// set of period

	bool leaf;
	// flag, whether node is leaf node

	deque<Node*> Child;

public:
	Node(void);
	~Node(void);

	void set_index(int new_index);
	void set_G(int new_G);
	void set_S(int* new_S);
	void set_leaf(bool new_leaf);
	void set_child(Node* new_child);

	int get_index();
	int get_G();
	int* get_S();
	deque<Node*> get_child();
	bool get_leaf();
};
