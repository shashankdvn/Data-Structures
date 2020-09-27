#include <iostream>
using namespace std;
#include <queue>

struct Node{
    int key;
    Node * left;
    Node * right;
};

Node* newNode(int key){
    struct Node* temp = new Node;
    temp->key = key;
    temp->left = NULL;
    temp->right = NULL;
    return temp;

};

/*Function to delete the deepest node 
in a given tree */
void inorder(Node* temp){
    if (!temp)
    return;
    inorder(temp->left);
    cout <<temp->key<<" ";
    inorder(temp->right);

}

void deldeepest(Node* root,Node* d_node){

    queue<struct Node*> q;
    q.push(root);
    //we perform level order traversal till last node
    struct Node* temp;
    while(!q.empty()){
        temp = q.front();
        q.pop();
        if (temp==d_node){
            temp = NULL;
            delete (d_node);
            return;
        }
        if (temp->right == d_node){
            temp = NULL;
            delete (d_node);
            return;
        }
        else(q.push(temp->right));
        if (temp->left == d_node){
            temp = NULL;
            delete(d_node);
            return;
        }else(q.push(temp->left));
        
    }

} 

Node* deletion(Node* root,int key){
    if (root ==NULL)
       return NULL;
    if (root->left ==NULL && root->right == NULL){
        if (root->key == key)
            return NULL;
        else
             return root;
    }
    queue<Node*> q;
    q.push(root);
    struct Node* temp;
    struct Node* key_node = NULL;
    while(!q.empty()){
        temp = q.front();
        q.pop();
        if (temp->key == key){
            key_node = temp;
        }
        if (temp->left)
            q.push(temp->left);
        if (temp->right)
            q.push(temp->right);
        
    }
    if (key_node !=NULL){
        int x =  temp->key;
        deldeepest(root,temp);
        key_node->key = x; 

    } 
    return root;
}

int main(){
    struct Node* root = newNode(10);
    root->left = newNode(11); 
    root->left->left = newNode(7); 
    root->left->right = newNode(12); 
    root->right = newNode(9); 
    root->right->left = newNode(15); 
    root->right->right = newNode(8);
    cout << "Inorder traversal before deletion : "; 
    inorder(root);
    cout << endl;
    root = deletion(root,12);
    cout << "Inorder traversal after deletion : "; 
    inorder(root);
    cout << endl;
    
    

}