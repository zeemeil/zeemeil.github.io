#include <stdio.h>
#include <stdlib.h>

// 链表节点结构
typedef struct Node {
    int data;
    struct Node* next;
} Node, *LinkList;

// 合并两个有序链表
void MergeList(LinkList La, LinkList Lb, LinkList* Lc) {
    LinkList pa = La->next;   // La的工作指针
    LinkList pb = Lb->next;   // Lb的工作指针
    *Lc = La;                 // 复用La的头结点作为Lc的头
    LinkList pc = *Lc;        // 维护Lc的尾指针

    pc->next = NULL;          // 初始化Lc链表

    while (pa && pb) {
        if (pa->data < pb->data) {  // La节点更小
            pc->next = pa;
            pc = pa;
            pa = pa->next;
        } else if (pa->data > pb->data) { // Lb节点更小
            pc->next = pb;
            pc = pb;
            pb = pb->next;
        } else {  // 相等时取La节点，删除Lb节点
            pc->next = pa;
            pc = pa;
            pa = pa->next;
            LinkList del = pb;
            pb = pb->next;
            free(del);
        }
    }

    // 链接剩余节点
    pc->next = pa ? pa : pb;

    // 释放Lb头结点
    free(Lb);
    Lb = NULL;
}

// 创建带头结点的有序链表
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

// 打印链表
void PrintList(LinkList L) {
    LinkList p = L->next;
    while (p) {
        printf("%d ", p->data);
        p = p->next;
    }
    printf("\n");
}

// 释放链表内存
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
    // 示例1
    LinkList La, Lb, Lc;
    int arr1[] = {1, 3, 5};
    int arr2[] = {2, 3, 6};
    CreateList(&La, arr1, 3);
    CreateList(&Lb, arr2, 3);

    MergeList(La, Lb, &Lc);
    printf("合并结果1: ");
    PrintList(Lc);  // 输出：1 2 3 5 6
    DestroyList(&Lc);

    // 示例2
    int arr3[] = {2, 2, 3};
    int arr4[] = {2, 3, 3};
    CreateList(&La, arr3, 3);
    CreateList(&Lb, arr4, 3);

    MergeList(La, Lb, &Lc);
    printf("合并结果2: ");
    PrintList(Lc);  // 输出：2 2 3 3
    DestroyList(&Lc);

    return 0;
}