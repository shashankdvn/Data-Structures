#include <iostream>
using namespace std;
#include <queue>

struct Node{
    int key;
    Node* left;
    Node* right;

    Node(int x){
        key = x;
        left  = NULL;
        right = NULL;
    }
};

void levelorder(Node *root){
    queue <Node *> q;
    q.push(root);

    while (!q.empty())
    {
        /* code */
        Node* curr = q.front();
        cout << curr->key << " ";
        q.pop();
        if (curr->left != NULL){
            q.push(curr->left);
        }
        if (curr->right !=NULL){
            q.push(curr->right);
        }

    }
    
}

int main(){
    struct Node* root = new Node(4);
    root->left = new Node(3);
    root->left->left = new Node(2);
    root->left->right = new Node(1);
    root->left->right->right =new Node(7);
    root->right = new Node(5);
    levelorder(root);

}