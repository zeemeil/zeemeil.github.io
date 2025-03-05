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

// 查找链表最大值
int Max(LinkList L) {
    if (L->next == NULL) return -1;  // 空链表返回-1
    
    LinkList pmax = L->next;        // 首元结点为初始最大值
    LinkList p = pmax->next;        // 从第二个结点开始比较
    
    while (p != NULL) {
        if (p->data > pmax->data) { // 发现更大值
            pmax = p;
        }
        p = p->next;
    }
    return pmax->data;
}

// 打印链表（仅用于调试）
void PrintList(LinkList L) {
    LinkList p = L->next;
    while (p) {
        printf("%d -> ", p->data);
        p = p->next;
    }
    printf("NULL\n");
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
    LinkList L;
    
    // 测试用例1：常规情况
    int arr1[] = {5, 9, 3, 2, 7};
    CreateList(&L, arr1, 5);
    printf("链表1最大值: %d\n", Max(L)); // 输出：9
    DestroyList(&L);

    // 测试用例2：最大值在末尾
    int arr2[] = {1, 4, 6, 3, 8};
    CreateList(&L, arr2, 5);
    printf("链表2最大值: %d\n", Max(L)); // 输出：8
    DestroyList(&L);

    // 测试用例3：单个元素
    int arr3[] = {5};
    CreateList(&L, arr3, 1);
    printf("链表3最大值: %d\n", Max(L)); // 输出：5
    DestroyList(&L);

    // 测试用例4：空链表
    CreateList(&L, NULL, 0);
    printf("空链表最大值: %d\n", Max(L)); // 输出：-1
    DestroyList(&L);

    return 0;
}