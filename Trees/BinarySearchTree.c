#include <stdio.h>
#include <stdlib.h>
struct bstNode {
   int val;
   struct bstNode *l;
   struct bstNode *r;
};
typedef struct bstNode bstNode;
struct bstqueue{
    bstNode *pval;
    struct bstqueue *next;
    };
typedef struct bstqueue bstqueue;
struct avlNode {
   int balance; /* -1 Left, 0 balanced, +1 Right */
   int val;
   struct avlNode *l;
   struct avlNode *r;
};
typedef struct avlNode avlNode;
struct qNode {
   avlNode *pval;
   struct qNode *nxt;
};
typedef struct qNode qNode;
/*The Code designed for adding to structs*/
int add_bst(bstNode **root,int val) {
   bstNode *newnode;
   if (root == NULL) { return -1; }
   if (*root == NULL) {
        newnode = (bstNode *)malloc(sizeof(bstNode)*1);
        newnode->val = val;
        newnode->l=NULL;
        newnode->r=NULL;
        *root = newnode;
        return 0;

      }
     else if((*root)->val > val) {
            return add_bst(&(*root)->l,val);

        }
     else{
        return add_bst(&(*root)->r,val);
     }
   return -1;
}
int add_to_q(bstqueue **x, bstNode *val ){
   if (x==NULL) { return -1; }
   if (*x==NULL) {
      *x = (bstqueue *) malloc(sizeof(bstqueue));
      (*x)->pval = val;
      (*x)->next = NULL;
      return 0;
   } else {
      return add_to_q(&((*x)->next),val);
   }
}

int pop(bstqueue **x,int *return_value){



return -1;
}
/*Basic Print Functions for the BST*/
int print_in_order(bstNode *root){
    if(root == NULL){return -1;}
    print_in_order(root->l);
    printf("%d\n", root->val);
    print_in_order(root->r);
    return 0;

}
int printq(bstqueue *root){
if (root==NULL){return -1;}
printf("%d",(root)->pval);
/*if(*root==NULL){return 0;}*/
root = root->next;
}
int print_by_level(bstNode *root,bstqueue **que){
  if (root==NULL){return -1;}
  printf("%d ",root->val);
  if (root->l != NULL){
      add_to_q(que,root->l);
  }
  if (root->r != NULL){
      add_to_q(que,root->r);
  }
  while(1){
    if(*que == NULL){
      return 0;
    }
    printf("%d ",(*que)->pval->val);
    if((*que)->pval->l != NULL){
      add_to_q(que,(*que)->pval->l);
    }
    if((*que)->pval->r != NULL){
      add_to_q(que,(*que)->pval->r);
    }
    *que = (*que)->next;
        }
  return 0;
}
#takes in numbers.txt and emits sorted.txt
int main(void){
    int n=0;
    bstqueue *hold=NULL;
    bstNode *root=NULL;
    int val = 0;
        while (scanf("%d",&val) != EOF) {
        n=n+1;
        add_bst(&root,val);  }
    print_in_order(root);
/*    print_by_level(root,&hold);*/


return 0;}

