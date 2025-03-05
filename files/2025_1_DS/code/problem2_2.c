#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* next;
} Node, *LinkList;

void MergeList(LinkList* La, LinkList* Lb, LinkList* Lc) {
    LinkList pa = (*La)->next;
    LinkList pb = (*Lb)->next;
    *Lc = *La;
    (*Lc)->next = NULL;

    while (pa || pb) {
        LinkList q;
        if (!pa) {
            q = pb;
            pb = pb->next;
        } else if (!pb) {
            q = pa;
            pa = pa->next;
        } else if (pa->data <= pb->data) {
            q = pa;
            pa = pa->next;
        } else {
            q = pb;
            pb = pb->next;
        }
        q->next = (*Lc)->next;
        (*Lc)->next = q;
    }
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
    // 示例1: 合并 1->3->5 和 2->3->6
    LinkList La, Lb, Lc;
    int arr1[] = {1, 3, 5};
    int arr2[] = {2, 3, 6};
    CreateList(&La, arr1, 3);
    CreateList(&Lb, arr2, 3);
    MergeList(&La, &Lb, &Lc);
    printf("合并结果1: ");
    PrintList(Lc);  // 输出：6 5 3 3 2 1
    DestroyList(&Lc);

    // 示例2: 合并 2->2->3 和 2->3->3
    int arr3[] = {2, 2, 3};
    int arr4[] = {2, 3, 3};
    CreateList(&La, arr3, 3);
    CreateList(&Lb, arr4, 3);
    MergeList(&La, &Lb, &Lc);
    printf("合并结果2: ");
    PrintList(Lc);  // 输出：3 3 3 2 2 2
    DestroyList(&Lc);

    return 0;
}