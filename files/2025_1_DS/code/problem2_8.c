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

void DeleteRange(LinkList* L, int mink, int maxk) {
    LinkList p = (*L)->next;
    LinkList pre = *L;
    while (p && p->data <= mink) {
        pre = p;
        p = p->next;
    }
    while (p && p->data < maxk) p = p->next;
    LinkList q = pre->next;
    pre->next = p;
    while (q != p) {
        LinkList temp = q->next;
        free(q);
        q = temp;
    }
}

int main() {
    LinkList L;
    int arr[] = {1, 2, 3, 4, 5};
    CreateList(&L, arr, 5);
    DeleteRange(&L, 1, 4);
    printf("删除结果: ");
    PrintList(L); // 输出：1 4 5 
    DestroyList(&L);
    return 0;
}