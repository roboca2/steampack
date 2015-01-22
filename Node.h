#pragma once
#include <string.h>
#include <deque>
#include <iostream>
#include <math.h>
#define TYPE1 8
#define TYPE2 12
#define TYPE3 24
#define TYPE4 32
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
	int channels;
	deque<Node*> Child;

public:
	Node(void);
	~Node(void);

	void set_index(int new_index);
	void set_channels(int new_channels);
	void set_G(int new_G);
	void set_S(int* new_S);
	void set_leaf(bool new_leaf);
	void set_child(Node* new_child);

	int get_index();
	int get_channels();
	int get_G();
	int* get_S();
	deque<Node*> get_child();
	bool get_leaf();
};
