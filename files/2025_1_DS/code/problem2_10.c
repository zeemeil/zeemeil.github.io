#include <stdio.h>
#include <stdlib.h>

// 时间复杂度O(n)，空间复杂度O(1)
void DeleteItem(int A[], int* n, int item) {
    int i = 0;          // 左指针（数组起始位置）
    int j = *n - 1;     // 右指针（数组末尾位置）

    while (i <= j) {
        // 找到左边第一个等于item的元素
        while (i <= j && A[i] != item) i++;
        // 找到右边第一个不等于item的元素
        while (i <= j && A[j] == item) j--;
        // 用右边的有效元素覆盖左边的无效元素
        if (i <= j) A[i++] = A[j--];
    }
    *n = i;  // 新数组长度为i
}

// 打印数组元素
void PrintArray(int A[], int n) {
    for (int i = 0; i < n; i++) {
        printf("%d ", A[i]);
    }
    printf("\n");
}

int main() {
    // 测试用例1：常规情况
    int A1[] = {2, 1, 3, 2, 4, 2};
    int n1 = 6;
    printf("原始数组1: ");
    PrintArray(A1, n1);
    DeleteItem(A1, &n1, 2);
    printf("删除后数组1: ");
    PrintArray(A1, n1);  // 输出：4 1 3 
    printf("新长度: %d\n\n", n1);  // 输出：3

    // 测试用例2：全为删除元素
    int A2[] = {5, 5, 5, 5};
    int n2 = 4;
    printf("原始数组2: ");
    PrintArray(A2, n2);
    DeleteItem(A2, &n2, 5);
    printf("删除后数组2: ");
    PrintArray(A2, n2);  // 输出：（空）
    printf("新长度: %d\n\n", n2);  // 输出：0

    // 测试用例3：没有需要删除的元素
    int A3[] = {1, 3, 5, 7};
    int n3 = 4;
    printf("原始数组3: ");
    PrintArray(A3, n3);
    DeleteItem(A3, &n3, 2);
    printf("删除后数组3: ");
    PrintArray(A3, n3);  // 输出：1 3 5 7 
    printf("新长度: %d\n\n", n3);  // 输出：4

    // 测试用例4：空数组
    int* A4 = NULL;
    int n4 = 0;
    printf("原始数组4: 空数组\n");
    DeleteItem(A4, &n4, 2);
    printf("删除后数组4长度: %d\n", n4);  // 输出：0

    return 0;
}