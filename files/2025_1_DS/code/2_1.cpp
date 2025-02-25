#include<iostream>
#include<fstream>
#include<string>
#include<iomanip>
using namespace std;
#define OK 1
#define ERROR 0
#define OVERFLOWS -2
typedef int Status; 
typedef int ElemType; 

#define MAXSIZE 100

struct Book {
    string id;
    string name;
    double price;
};
typedef struct {
    Book *elem;
    int length;
} SqList;


Status InitList_Sq(SqList &L) {
    L.elem = new Book[MAXSIZE];
    if (!L.elem)
        exit(OVERFLOWS);
    L.length=0;
    return OK;
}

Status GetElem(SqList L, int i, Book &e) {
    if (i < 1 || i > L.length)
        return ERROR;
    e = L.elem[i-1];
    return OK;
}

int LocateElem_Sq(SqList L, double e) {
    for (int i = 0; i < L.length; i++)
        if  (L.elem[i].price == e)
            return i + 1;
    return 0;
}

Status ListInsert_Sq(SqList &L, int i, Book e) {
    if ((i<1) || (i>L.length+1))
        return ERROR;
    if (L.length == MAXSIZE)
        return ERROR;
    for (int j = L.length -1; j>=i-1; j--)
        L.elem[j+1] = e;
    L.elem[i-1] = e;
    ++L.length;
    return OK;
}

Status ListDelete_Sq(SqList &L, int i) {
    if ((i < 1) || (i > L.length))
        return ERROR;
    for (int j = i; j <= L.length; j++)
        L.elem[j-1] = L.elem[j];
    --L.length;
    return OK;
}
 

int main(){
    SqList L;
    int i = 0, temp, a, c, choose;
    double price;
    Book e;
    string line, head_1, head_2, head_3;
    cout << "1.建立\n";
    cout << "2.输入\n";
    cout << "3.取值\n";
    cout << "4.查找\n";
    cout << "5.插入\n";
    cout << "6.删除\n";
    cout << "7.输出\n";
    cout << "0.推出\n";

    choose = -1;
    while (choose != 0)
    {
        cout << "请选择";
        cin >> choose;
        switch (choose)
        {
        case 1:
            /* code */
            if (InitList_Sq(L))
                cout << "Success install array\n\n";
            else
                cout << "Lost install array\n\n";
            break;
        case 2: {
            i = 0;
            L.elem = new Book[MAXSIZE];
            if (!L.elem)
                exit(OVERFLOWS);
            L.length = 0;
            fstream readfile("book.txt");
            while (getline(readfile, line))
            {
                if (!readfile) {
                    printf("错误！未找到文件！");
                exit(ERROR);
                }
                readfile >> head_1 >> head_2 >> head_3;
                while (!readfile.eof()) {
                    readfile >> L.elem[i].id >> L.elem[i].name >> L.elem[i].price;
                    i++;
                }
            }
            cout << "输入book.txt 信息完毕\n\n";
            L.length = i;
            readfile.close();
        }
            break;
        case 3: 
            cout << "请输入一个位置用来取值：\n";
            cin >> i;
            temp = GetElem(L, i, e);
            if (temp != 0){
                printf("查找成功\n");
                printf("第%d本图书的信息是：\n",i);
                cout << left << setw(15) << e.id << "\t" << left << setw(50) << e.name << "\t" << left << setw(5) << e.price << endl << endl;
            } else {
                printf("查找失败！位置超出范围\n\n");
            }
            break;
        case 4:
            printf("请输入所要查找的价格：\n");
            cin >> price;
            temp = LocateElem_Sq(L, price);
            if (temp != 0) {
                printf("查找成功\n");
                cout << "该价格对于的书名为:" << L.elem[temp-1].name << endl << endl;
            } else {
                printf("查找失败，没有对应价格的书籍\n\n");
            }
            break;
        case 5:
            cout << "请输入增加的位置和书的信息，包括编号，书名，价格(用空格隔开):";
            cin >> a;
            cin >> e.id >> e.name >> e.price;
            if (ListInsert_Sq(L, a, e))
                cout << "增加成功.\n\n";
            else
                cout << "增加失败.\n\n";
            break;
        case 6:
            cout << "请输入删除的书的位置:" ;
            cin >> c;
            if (ListDelete_Sq(L, c))
                cout << "删除成功。\n\n" ;
            else
                cout << "删除失败。\n\n";
            break;
        case 7:
            cout << "当前图书系统信息(顺序表)读出：\n";
            for (i=0; i<L.length; i++)
                cout << left << setw(15) << L.elem[i].id << "\t" << left << setw(50) << L.elem[i].name << "\t" << setw(5) << L.elem[i].price << endl;
            cout << endl;
            break;
        }
    }
    return 0;

}