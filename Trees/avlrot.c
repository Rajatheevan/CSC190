#include <stdio.h>
#include <stdlib.h>
struct bstNode {
   int val;
   struct bstNode *l;
   struct bstNode *r;
};
typedef struct bstNode bstNode;

struct avlNode {
   int balance; /* -1 Left, 0 balanced, +1 Right */
   int val;
   struct avlNode *l;
   struct avlNode *r;
};
typedef struct avlNode avlNode;

struct bstqueue{
    avlNode *pval;
    struct bstqueue *next;
    };
typedef struct bstqueue bstqueue;

struct qNode {
   avlNode *pval;
   struct qNode *nxt;
};
typedef struct qNode qNode;

/*The Code designed for adding to structs*/
int add_avl(avlNode **root,int val) {
   avlNode *newnode;
   if (root == NULL) { return -1; }
   if (*root == NULL) {
        newnode = (avlNode *)malloc(sizeof(avlNode)*1);
        newnode->val = val;
        newnode->l=NULL;
        newnode->r=NULL;
        *root = newnode;
        return 0;

      }
     else if((*root)->val > val) {
            return add_avl(&(*root)->l,val);

        }
     else{
        return add_avl(&(*root)->r,val);
     }
   return -1;
}
/*The exact same */
int add_bst(avlNode **root,int val) {
   avlNode *newnode;
   if (root == NULL) { return -1; }
   if (*root == NULL) {
        newnode = (avlNode *)malloc(sizeof(avlNode)*1);
        newnode->val = val;
        newnode->l=NULL;
        newnode->r=NULL;
        *root = newnode;
        return 0;

      }
     else if((*root)->val > val) {
            return add_avl(&(*root)->l,val);

        }
     else{
        return add_avl(&(*root)->r,val);
     }
   return -1;
}
int add_to_q(bstqueue **x, avlNode *val ){
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
int print_in_order(avlNode *root){
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

int print_by_level(avlNode *root,bstqueue **que){
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
        printf("\n");
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

/*ALL of the code from this point onwards is relative to the AvlROtation Assignment*/

int height(avlNode *root){
        int hl = 0;
        int hr = 0;
/*      if (root==NULL){return 0;}*/
        if(root->l){
                hl = height(root->l);
        }
        if(root->r){
                hr = height(root->r);
        }

        return (hr>hl) ? (hr=hr+1):(hl=hl+1);
}


int isAVL(avlNode **root){
        int lo = 0;
        int ru = 0;
        int judge;
        if(*root==NULL){return -1;}
        if((*root)->l){
                lo = height((*root)->l);
        }
        if((*root)->r){
                ru = height((*root)->r);
        }
        judge= (ru-lo);
        if ((judge != 1) && (judge != 0) && (judge != -1)){
                return -1;/*Is not AVL*/
        }
        else{return 0;}

}

/*This section pertains directly to the rotations*/
int rotate(avlNode **root, unsigned int Left0_Right1){
/*      avlNode *temp = NULL;*/
        avlNode *hel=NULL;
        if (*root==NULL){return -1;}

        if (Left0_Right1==1){
                if((*root)->l == NULL){return -1;}
                hel = (*root)->l;
                (*root)->l = hel->r;
                hel->r = (*root);
                (*root) = hel;
                printf("get rotate r\n");
                return 0;

        }
        if(Left0_Right1==0){
                if((*root)->l == NULL){return -1;}
                hel = (*root)->r;
                (*root)->r = hel ->l;
                hel->l=(*root);
                (*root)=hel;
                 printf("get rotate l\n");
                return 0;
        }
        return -1;
}
int dblrotate(avlNode **root, unsigned int MajLMinR0_MajRMinL1){

        if (MajLMinR0_MajRMinL1==0){
                rotate(&(*root)->r,1);
                rotate(root,0);
                return 0;
        }
        if (MajLMinR0_MajRMinL1==1){
                rotate(&(*root)->l,0);
                rotate(root,1);
                return 0;
        }
        return -1;



}
int main(void){
int a=1;
    bstqueue *hold=NULL;
   /* bstNode *root=NULL;*/
    avlNode *rolo = NULL;

    add_avl(&rolo,10);
    add_avl(&rolo,12);
    add_avl(&rolo,13);
    add_avl(&rolo,3);
    add_avl(&rolo, 11);
    add_avl(&rolo,15);
  /*  add_avl(&rolo, 20);*/
 /*   add_bst(&root,100);
 *       add_bst(&root,1200);
 *           add_bst(&root,200);
 *               add_bst(&root,12);*/
    print_in_order(rolo);
    print_by_level(rolo,&hold);
   /* printf("This is the Heights: %d\n",height(root));
 *     printf("This is the Test of isAVL: %d\n",isAVL(&root));
 *     */
   printf("is avl? #1: %d\n",isAVL(&rolo));
   printf("here is a test value: %d\n",dblrotate(&rolo,a));
   print_by_level(rolo,&hold);
   print_in_order(rolo);
   printf("is avl?: %d\n", isAVL(&rolo));




}





