#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* next;
} Node, *LinkList;

void Difference(LinkList* La, LinkList* Lb, int* n) {
    // 差集的结果存储于单链表La中，*n是结果集合中元素个数，调用时为0
    LinkList pa = (*La)->next;
    LinkList pb = (*Lb)->next;
    LinkList pre = *La;
    *n = 0;

    while (pa && pb) {
        if (pa->data < pb->data) {
            // pa和pb分别是链表La和Lb的工作指针,初始化为相应链表的第一个结点
            (*n)++;
            pre = pa;
            pa = pa->next;
        } else if (pa->data > pb->data) {
            LinkList temp = pb;
            pb = pb->next;
            free(temp);
        } else {
            pre->next = pa->next;
            LinkList temp = pa;
            pa = pa->next;
            free(temp);
            temp = pb;
            pb = pb->next;
            free(temp);
        }
    }

    while (pb) {
        LinkList temp = pb;
        pb = pb->next;
        free(temp);
    }

    LinkList current = (*La)->next;
    while (current) {
        (*n)++;
        current = current->next;
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
    LinkList La, Lb;
    int count;

    // 示例1: A={1,2,3}, B={2,3,4}
    int arr1[] = {1, 2, 3};
    int arr2[] = {2, 3, 4};
    CreateList(&La, arr1, 3);
    CreateList(&Lb, arr2, 3);
    Difference(&La, &Lb, &count);
    printf("差集结果1: ");
    PrintList(La); // 输出：1
    printf("元素个数: %d\n", count); // 输出：1
    DestroyList(&La);

    // 示例2: A={2,4,6}, B={3,5,7}
    int arr3[] = {2, 4, 6};
    int arr4[] = {3, 5, 7};
    CreateList(&La, arr3, 3);
    CreateList(&Lb, arr4, 3);
    Difference(&La, &Lb, &count);
    printf("差集结果2: ");
    PrintList(La); // 输出：2 4 6
    printf("元素个数: %d\n", count); // 输出：3
    DestroyList(&La);

    return 0;
}