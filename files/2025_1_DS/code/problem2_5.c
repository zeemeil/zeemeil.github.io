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

// 分解链表为负数链表B和非负数链表C
void DisCompose(LinkList A, LinkList* B, LinkList* C) {
    *B = A;          // B表复用A的头结点
    (*B)->next = NULL;
    *C = (LinkList)malloc(sizeof(Node));  // C表新建头结点
    (*C)->next = NULL;

    LinkList p = A->next;  // 从A的第一个元素开始遍历
    while (p) {
        LinkList nextNode = p->next;  // 保存后继结点
        if (p->data < 0) {            // 负数插入B表头部
            p->next = (*B)->next;
            (*B)->next = p;
        } else {                      // 非负数插入C表头部
            p->next = (*C)->next;
            (*C)->next = p;
        }
        p = nextNode;  // 处理下一个结点
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

int main() {
    LinkList A, B, C;
    
    // 示例：原链表包含 -1 -> 2 -> -3 -> 4 -> -5
    int arr[] = {-1, 2, -3, 4, -5};
    CreateList(&A, arr, 5);
    
    // 分解链表
    DisCompose(A, &B, &C);
    
    // 打印结果
    printf("负数链表B: ");
    PrintList(B);  // 输出：-5 -3 -1 
    printf("非负数链表C: ");
    PrintList(C);  // 输出：4 2 
    
    // 释放内存（注意B头结点是原A头结点，只需释放一次）
    DestroyList(&B);
    DestroyList(&C);
    
    return 0;
}