#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* next;
} Node, *LinkList;

void Mix(LinkList* La, LinkList* Lb, LinkList* Lc) {
    LinkList pa = (*La)->next;
    LinkList pb = (*Lb)->next;
    *Lc = *La;
    LinkList pc = *Lc;
    pc->next = NULL;

    while (pa && pb) {
        if (pa->data == pb->data) {
            pc->next = pa;
            pc = pa;
            pa = pa->next;
            LinkList u = pb;
            pb = pb->next;
            free(u);
        } else if (pa->data < pb->data) {
            LinkList u = pa;
            pa = pa->next;
            free(u);
        } else {
            LinkList u = pb;
            pb = pb->next;
            free(u);
        }
    }

    while (pa) {
        LinkList u = pa;
        pa = pa->next;
        free(u);
    }
    while (pb) {
        LinkList u = pb;
        pb = pb->next;
        free(u);
    }

    pc->next = NULL;
    free(*Lb);
    *Lb = NULL;
}

void CreateList(LinkList* L, int arr[], int n) {
    *L = (LinkList)malloc(sizeof(Node));
    (*L)->next = NULL;
    LinkList tail = *L;
    for (int i = 0; i < n; i++) {
        LinkList newNode = (LinkList)malloc(sizeof(Node));
        newNode->data = arr[i];
        newNode->next = NULL;
        tail->next = newNode;
        tail = newNode;
    }
}

void PrintList(LinkList L) {
    LinkList p = L->next;
    while (p) {
        printf("%d ", p->data);
        p = p->next;
    }
    printf("\n");
}

void DestroyList(LinkList* L) {
    LinkList p = *L;
    while (p) {
        LinkList temp = p;
        p = p->next;
        free(temp);
    }
    *L = NULL;
}

int main() {
    LinkList La, Lb, Lc;
    
    // 示例1: A={1,2,3}, B={2,3,4}
    int arr1[] = {1, 2, 3};
    int arr2[] = {2, 3, 4};
    CreateList(&La, arr1, 3);
    CreateList(&Lb, arr2, 3);
    Mix(&La, &Lb, &Lc);
    printf("交集结果1: ");
    PrintList(Lc);  // 输出：2 3
    DestroyList(&Lc);

    // 示例2: A={2,4,6}, B={4,6,8}
    int arr3[] = {2, 4, 6};
    int arr4[] = {4, 6, 8};
    CreateList(&La, arr3, 3);
    CreateList(&Lb, arr4, 3);
    Mix(&La, &Lb, &Lc);
    printf("交集结果2: ");
    PrintList(Lc);  // 输出：4 6
    DestroyList(&Lc);

    return 0;
}