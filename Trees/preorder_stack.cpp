#include <iostream>
#include<stack>
using namespace std;
struct Node{
    int key;
    Node* left;
    Node* right;

    Node(int x){
        key = x;
        left = NULL;
        right = NULL;
    }
};

void preorder(Node* root){
    stack <Node* > s;
    s.push(root);

    while(!s.empty()){
        Node* curr_node = s.top();
        cout << curr_node->key<< " ";
        s.pop();

        if (curr_node->right != NULL){
            s.push(curr_node->right);
        }
        if (curr_node->left !=NULL){
            s.push(curr_node->left);
        }

    }


}

int main(){
    struct Node* root = new Node(10);
    root->left = new Node(8);
    root->right = new Node(2);
    root->left->left = new Node(3);
    root->left->right = new Node(5);
    root->right->left = new Node(2);
    preorder(root);
}
