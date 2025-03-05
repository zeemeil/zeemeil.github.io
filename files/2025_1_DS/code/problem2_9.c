#include <stdio.h>
#include <stdlib.h>

typedef struct DNode {
    int data;
    struct DNode* prior;
    struct DNode* next;
} DNode, *DLinkList;

// 创建带头结点的双向循环链表
DLinkList CreateList(int arr[], int n) {
    DLinkList head = (DLinkList)malloc(sizeof(DNode));
    head->prior = head;
    head->next = head;
    
    for (int i = 0; i < n; i++) {
        DLinkList newNode = (DLinkList)malloc(sizeof(DNode));
        newNode->data = arr[i];
        
        // 插入到链表末尾
        newNode->prior = head->prior;
        newNode->next = head;
        head->prior->next = newNode;
        head->prior = newNode;
    }
    return head;
}

// 交换p节点与其前驱节点
void Exchange(DLinkList p) {
    if (!p || p->next == p || p->prior == p) return; // 空表或唯一节点
    
    DLinkList q = p->prior;
    DLinkList q_prior = q->prior;  // 保存原始前驱的前驱
    
    // 共修改6处指针连接
    q_prior->next = p;
    p->prior = q_prior;
    
    q->next = p->next;
    p->next->prior = q;
    
    q->prior = p;
    p->next = q;
}

// 打印双向循环链表（顺时针）
void PrintList(DLinkList L) {
    if (L->next == L) {
        printf("空链表\n");
        return;
    }
    
    DLinkList p = L->next;
    while (p != L) {
        printf("%d ⇄ ", p->data);
        p = p->next;
    }
    printf("头节点\n");
}

// 释放内存
void DestroyList(DLinkList* L) {
    DLinkList p = (*L)->next;
    while (p != *L) {
        DLinkList temp = p;
        p = p->next;
        free(temp);
    }
    free(*L);
    *L = NULL;
}

int main() {
    // 示例1: 1 ⇄ 2 ⇄ 3 ⇄ 头节点（p指向3的前驱2）
    int arr[] = {1, 2, 3};
    DLinkList L = CreateList(arr, 3);
    printf("原始链表: ");
    PrintList(L); // 输出：1 ⇄ 2 ⇄ 3 ⇄ 头节点
    
    // 获取第二个节点（值为2）
    DLinkList p = L->next->next;
    printf("交换节点 %d 与其前驱\n", p->data);
    Exchange(p);
    
    printf("交换后链表: ");
    PrintList(L); // 输出：2 ⇄ 1 ⇄ 3 ⇄ 头节点
    DestroyList(&L);

    // 示例2: 单节点链表
    DLinkList L2 = CreateList((int[]){5}, 1);
    printf("\n原始单节点链表: ");
    PrintList(L2);
    Exchange(L2->next); // 无变化
    printf("交换后保持原样: ");
    PrintList(L2);
    DestroyList(&L2);

    return 0;
}