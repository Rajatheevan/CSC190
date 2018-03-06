#include<stdlib.h>
#include<stdio.h>
/*Structs*/
typedef struct {
   int *store;
   unsigned int size;
   unsigned int end;
} HeapType;

/*Function prototypes*/
int initHeap(HeapType *pHeap, int size);
int inorder  (HeapType *pHeap, int **output, int *o_size);
int preorder (HeapType *pHeap, int **output, int *o_size);
int postorder(HeapType *pHeap, int **output, int *o_size);
int addHeap(HeapType *pHeap,int key);
int igtp(HeapType *pHeap,int index);
int switcher(HeapType *pHead, int index);
int isrl(HeapType *pHeap, int index);

/*Functions*/

        int initHeap(HeapType *pHead, int size){
        int *hold;
        if(size <= 0){return -1;}
        if(pHead == NULL){return -1;}
        (*pHead).size = size;
        hold = (int*)malloc(sizeof(int)*size);
        (*pHead).store = hold;
        pHead->end = 0;
        return 0;
}
/*-------------------------------------------------------------------------------*/
int inorder(HeapType *pHeap, int **output, int *o_size){
        int index = 0;

        *output=(int*)malloc(sizeof(int)*(pHeap->size));

        inhelp(pHeap,&index,(output),o_size,0);
        return 0;

}
int preorder(HeapType *pHeap, int **output, int *o_size){
        int index = 0;

        *output=(int*)malloc(sizeof(int)*(pHeap->size));

        inhelp(pHeap,&index,(output),o_size,1);
        return 0;

}
int postorder(HeapType *pHeap, int **output, int *o_size){
        int index = 0;

       *output=(int*)malloc(sizeof(int)*(pHeap->size));

        inhelp(pHeap,&index,(output),o_size,2);
        return 0;

}

int inhelp(HeapType *pHeap, int *index, int **output,int *o_size,int type){
        int lu;
        int cu;
        int ru;
        if((*index)>=(pHeap-> end)){return -1;}
        ru = 2*(*index)+2;
        lu = 2*(*index)+1;
        printf("the index is //%d\n", (*index));
        if(type ==0/*in Order*/){
        inhelp(pHeap,&lu,output,o_size,type);/*left*/
        (*output)[*o_size] = (pHeap->store)[*index];/*Center Bro*/
        printf("The value that was just drawn is // %d\n",(*output)[*o_size]);
        inhelp(pHeap,&ru,output,o_size,type);/*Right*/
        return 0;
        }
        if(type ==1/*Preorder*/){
        (*output)[*o_size] = (pHeap->store)[*index];/*Center Bro*/
         printf("The value that was just drawn is // %d\n",(*output)[*o_size]);
        inhelp(pHeap,&lu,output,o_size,type);/*left*/
        inhelp(pHeap,&ru,output,o_size,type);/*Right*/
        return 0;
        }
        if (type==2/*PostOrder*/){
        inhelp(pHeap,&lu,output,o_size,type);/*left*/
        inhelp(pHeap,&ru,output,o_size,type);/*Right*/
        (*output)[*o_size] = (pHeap->store)[*index];/*Center Bro*/
        printf("The value that was just drawn is // %d\n",(*output)[*o_size]);
        return 0;
        }
        return -1;
}
/*================================================================================*/
/*Part B heap Manipulation Functions*/
int addHeap(HeapType *pHeap, int key){
        int index;
        if((pHeap->end)>=(pHeap->size)){printf("weirdfail "); return -1;}
        pHeap->store[pHeap->end] = key;
        pHeap->end = pHeap->end +1;
        printf("the new end is %d\n",pHeap->end);
        /*The Key is added to the end of the list*/
        switcher(pHeap, (pHeap->end)-1);
        return 0;
}
/*checks if the parent is less than the child return 0 if so*/
int igtp(HeapType *pHeap,int index){
        int blah;
        if (index%2 == 0){
                /*parent of an even node*/
                blah = ((index-2)/2);
                if((pHeap->store)[index]>(pHeap->store)[blah]){
                return blah;
                }

        }
        if(index%2 ==1){
                /*parent of an odd node*/
                blah = (((index-1)/2));

                if((pHeap->store)[index]>(pHeap->store)[blah]){

                return blah;
                }


        }
        return -1;
}
/*Will switch if the parent is not greater otherwise return -1*/
int switcher(HeapType *pHead, int index){
        int hold;
        int pcheck =-1;
        if(index == 0){return -1;}
        pcheck = igtp(pHead, index);

        if (pcheck == -1){printf("pheck fail"); return -1;}
        (hold) = (pHead->store)[pcheck];
        (pHead->store)[pcheck] = (pHead->store)[index];
        (pHead->store)[index] = hold;
        switcher(pHead, pcheck);
        return 0;
        }
/*===================================================================*/

/*Find Heap Bro*/
int findHeap(HeapType *pHeap, int key){
        int cnt=0;
        if(pHeap ==NULL){return -1;}
        while (1){
                if ((pHeap->store)[cnt]==key){
                        return 1;}
                cnt = cnt +1;
                if (cnt == (pHeap->end)){return 0;}
        }
        return -1;


}

int delHeap(HeapType *pHeap, int *key){
        *key = (pHeap->store)[0];
        (pHeap->store)[0] = (pHeap->store)[(pHeap->end)-1];
        pHeap->end = pHeap->end -1;
        isrl(pHeap, 0);
        return 0;

}

int isrl(HeapType *pHeap, int index){
        int blah;
        int lu=0;
        int ru=0;
        int *out,size=0;
        if(pHeap == NULL){return -1;}
        /*Check if nodes exist*/
        if(index >= (pHeap->end)){return -1;}
        if((2*index)+1 >= (pHeap->end)){ printf("lu");lu = -1;}
        if((2*index)+2 >= (pHeap->end)){ printf("ru");ru = -1;}
        if((ru==-1)&&(lu==-1)){printf("END");   return -1;}
        if(ru ==-1){
           if((pHeap->store)[index] < (pHeap->store)[(2*index)+1]){
                 blah = (pHeap->store)[(2*index)+1];
                 (pHeap->store)[(2*index)+1] = (pHeap->store)[(index)];
                 (pHeap->store)[(index)] = blah;
                /* isrl(pHeap, ((2*index)+1));*/
                        return 0;
            }

        }
        if(lu == -1){
                if((pHeap->store)[index] < (pHeap->store)[(2*index)+2]){
                        blah = (pHeap->store)[(2*index)+2];
                        (pHeap->store)[(2*index)+2] = (pHeap->store)[(index)];
                        (pHeap->store)[(index)] = blah;
         /*               isrl(pHeap, ((2*index)+2));*/
                return 0;
                }

        }
        /*handles the general case where both nodes exist*/

        if ((pHeap->store)[(2*index)+1] >= (pHeap->store)[(2*index)+2]) {
        /*      preorder(pHeap,&out,&size);
        */      if((pHeap->store)[index] < (pHeap->store)[(2*index)+1]){
                        blah = (pHeap->store)[(2*index)+1];
                        (pHeap->store)[(2*index)+1] = (pHeap->store)[(index)];
                        (pHeap->store)[(index)] = blah;
                        isrl(pHeap, ((2*index)+1));
                        return 0;
                }

        }
        if ((pHeap->store)[(2*index)+2] > (pHeap->store)[(2*index)+1]){
        /*      preorder(pHeap,&out,&size);
        */      if((pHeap->store)[index] < (pHeap->store)[(2*index)+2]){
                        blah = (pHeap->store)[(2*index)+2];
                        (pHeap->store)[(2*index)+2] = (pHeap->store)[(index)];
                        (pHeap->store)[(index)] = blah;
                        isrl(pHeap, ((2*index)+2));
                return 0;
                }
        }
        return -1;
}

int main(){
        HeapType root;
        int *out,blaj;
        int i;
        int blah;
        int sze = 0;
        initHeap(&root,10);
        for(i=0;i<=9;i=i+1){
                blah=1+i;
                addHeap(&root,blah);
                printf("the i is //%d The value just interred was //%d\n",i,blah);
        }
        printf("=======================InORDER========================\n");
        inorder(&root,&out, &sze);
        printf("=======================PreORDER========================\n");
        preorder(&root,&out, &sze);
        printf("=======================PostORDER========================\n");
        postorder(&root,&out, &sze);
        printf("========================TESTING FOR FIND HEAP==================\n");
        printf("The Value drawn is %d\n", findHeap(&root, 10));
        printf("The Value drawn is %d\n", findHeap(&root, 2));
        printf("The Value drawn is %d\n", findHeap(&root, -2666666));

        printf("----------------------------------------DEL ME ---------------\n");
        delHeap(&root,&blaj);
        printf("The success of the del is %d\n",blaj);
        printf("=======================PreORDER========================\n");
        preorder(&root,&out, &sze);

        return 0;}


