#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* next;
} Node, *LinkList;

// 创建带头结点的链表
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

// 释放链表内存（不释放原A的头结点）
void DestroyList(LinkList* L) {
    LinkList p = (*L)->next;
    while (p) {
        LinkList temp = p;
        p = p->next;
        free(temp);
    }
    free(*L);  // 释放头结点
    *L = NULL;
}


typedef struct DNode {
    int data;
    struct DNode *prior, *next;
} DNode, *DLinkList;

void Exchange(DLinkList p) {
    DLinkList q = p->prior;
    q->prior->next = p;
    p->prior = q->prior;
    q->next = p->next;
    q->prior = p;
    p->next->prior = q;
    p->next = q;
}

int main() {
    DLinkList head = (DLinkList)malloc(sizeof(DNode));
    head->next = head->prior = head;
    // 创建示例节点：...（代码略）
    // 假设p指向某个节点，调用Exchange(p);
    return 0;
}