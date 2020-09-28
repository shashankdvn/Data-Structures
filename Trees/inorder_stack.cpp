/* Program for the Inorder Traversal without recursion and using stack*/
#include <iostream>
using namespace std;
#include <stack>
#include<bits/stdc++.h>
struct Node{
    int data;
    Node* left;
    Node* right;

    Node(int data){
        this->data =data;
        left = NULL;
        right = NULL; 
    }
};

void inorder(struct Node* root){
    stack <Node*> s;
    Node *curr = root;
    while(curr!=NULL || s.empty()==false){
        while(curr !=NULL){
            s.push(curr);
            curr = curr->left;
        }
        curr = s.top();
        s.pop();
        cout << curr->data << " ";
        curr = curr->right;

    }
}
int main() 
{ 
  
    /* Constructed binary tree is 
              1 
            /   \ 
          2      3 
        /  \ 
      4     5 
    */
    struct Node *root = new Node(1); 
    root->left        = new Node(2); 
    root->right       = new Node(3); 
    root->left->left  = new Node(4); 
    root->left->right = new Node(5); 
  
    inorder(root); 
    return 0; 
} 
