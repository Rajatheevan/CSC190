#include <stdio.h>
#include <stdlib.h>

struct llnode {
  char value;
   struct llnode *next;
};
typedef struct llnode llnode;
/*These are the Linkied List helpr functions that are the basis of the structure for this lab*/
int llnode_add_to_tail(llnode **x,char value) {
   if (x==NULL) { return -1; }
   if (*x==NULL) {
      *x = (llnode *) malloc(sizeof(llnode));
      (*x)->value = value;
      (*x)->next = NULL;
      return 0;
   } else {
      return llnode_add_to_tail(&((*x)->next),value);
   }
}
int llnode_add_to_head(llnode **x, char value){
        llnode* new;
        if (x==NULL){return -1;}
        if(*x==NULL){return llnode_add_to_tail((x),value);}
        else{
        new = (llnode*)malloc(sizeof(llnode));
        new->next=*x;
        new-> value = value;
        *x=new;
        return 1;}}
int llnode_print_from_head(llnode *x) {
   if (x==NULL) { return 0; }
   else {
      printf("%c\n",x->value);
      return llnode_print_from_head(x->next);
   }
}
int llnode_print_from_tail(llnode *x) {
   if (x==NULL) { return 0; }
   else {
      if (x->next == NULL) {
         printf("%c\n",x->value);
         return 0;
      } else {
         llnode_print_from_tail(x->next);
         printf("%c\n",x->value);
         return 0;
      }
   }
}
/*The following function are the actual use cases for the stack itself using the backend helper functions of the LL*/
int push(llnode **x, char value){
llnode_add_to_head(x,value);
return 0;

}
int pop(llnode **x,char *return_value){
  llnode *old_head;
  char temp;
  if (x==NULL){return-1;}
  *return_value = (*x)->value;
  old_head = *x;
  (*x)=(*x)->next;
  free(old_head);
  return 0;


}


int main(void) {
   int n=0;
   int cnt=-1;
   char value;
   int rvalue=0;
   char hold;
   int oldn = 0;
   llnode *input_list=NULL;
   while (scanf("%c",&value) != EOF) {
     cnt=cnt+1;

     if ((value=='[') || (value == '{') || (value == '(')){
      n=n+1;
      push(&input_list, value);

      }
        if((value==']') || (value == ')') || (value == '}')){
        if(n==0){n=n+1;break;}
        pop(&input_list,&hold);
        n=n+1;
        oldn=n;
        if((hold=='[') && (value==']')){
        n=n-2;
        }

        if((hold == '(') && (value ==')')){
        n=n-2;
}
        if((hold=='{')&& (value=='}')){
        n=n-2;
}
        if(oldn == n){break;}
}
   }
   if(n==0){printf("PASS\n");return 0;}
   if(n!=0){printf("Fail, %d\n",cnt);return -1;}
   printf("INFO: you entered %d items that were not cleared\n",n);
   /*rvalue=llnode_print_from_tail(input_list);*/

   return 0;
}
