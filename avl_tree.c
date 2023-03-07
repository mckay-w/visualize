#define _CRT_SECURE_NO_WARNINGS
#include<stdio.h>
#include<stdlib.h>

typedef struct node* Node;
struct node {
    Node left;
    Node right;
    int value;
    int depth;
};

int cal_bf(Node left,Node right) {
    int l, r;
    if (left == 0) {
        l = 0;
    }
    else {
        l = left->depth+1;
    }
    if (right == 0) {
        r = 0;
    }else{
        r = right->depth+1;
    }
    return l - r;
}

int depthUpdate(Node root) {
    int l, r;
    if (root->left == 0) {
        l = -1;
    }
    else {
        //l=depthUpdate(root->left);
        l = root->left->depth;
    }
    if (root->right == 0) {
        r = -1;
    }
    else {
        r = root->right->depth;
    }
    root->depth =l > r ? l + 1 : r + 1;
    return root->depth;
}

Node RLRotation(Node root) {
    Node p1, p2, p3;
    p1 = root;
    p2 = root->right;
    p3 = p2->left;
    Node tempc = p3->left, tempd = p3->right;
    p3->left = p1;
    p3->right = p2;
    p1->right = tempc;
    p2->left = tempd;
    depthUpdate(p1);
    depthUpdate(p2);
    depthUpdate(p3);
    return p3;
}

Node RRRotation(Node root) {
    Node nroot = root->right, temp;
    temp = nroot->left;
    nroot->left = root;
    root->right = temp;
    depthUpdate(root);
    depthUpdate(nroot);
    return nroot;
}

Node LLRotation(Node root) {
    Node nroot = root->left, temp;
    temp = nroot->right;
    nroot->right = root;
    root->left = temp;
    depthUpdate(root);
    depthUpdate(nroot);
    return nroot;
}

Node LRRotation(Node root) {
    Node p1, p2, p3;
    p1 = root;
    p2 = root->left;
    p3 = p2->right;
    Node tempc = p3->left, tempd = p3->right;
    p3->left = p2;
    p3->right = p1;
    p2->right = tempc;
    p1->left = tempd;
    depthUpdate(p2);
    depthUpdate(p1);
    depthUpdate(p3);
    return p3;
}

Node insert(Node root, int x) {
    Node p = root, son = 0;
    if (p != 0) {
        if (p->value < x) {
            p->right = insert(p->right, x);
            depthUpdate(p->right);
            if (cal_bf(p->left,p->right) <= -2)//如果插入后右边的树高度达到2
            {
                if (x < p->right->value)//RL
                    p = RLRotation(p);
                else//RR
                    p = RRRotation(p);
            }
        }
        else {
            p->left = insert(p->left, x);//L
            depthUpdate(p->left);
            if (cal_bf(p->left,p->right) >= 2) {
                if (x < p->left->value)//LL
                    p = LLRotation(p);
                else//RR
                    p = LRRotation(p);
            }
        }
        return p;
    }
    else {
        p = (Node)malloc(sizeof(struct node));
        p->value = x;
        p->left = p->right = 0;
        p->depth = 0;
        return p;
    }

}


int main() {
    int n, a[30] = { 0 };
    scanf("%d", &n);
    for (int i = 0; i < n; i++) {
        scanf("%d", a + i);
    }
    Node root;
    root = (Node)malloc(sizeof(struct node));
    root->value = a[0];
    root->left = root->right = 0;
    root->depth = 0;
    for (int i = 1; i < n; i++) {
        root = insert(root, a[i]);
        depthUpdate(root);
    }
    printf("%d", root->value);
}

