#include<stdlib.h>
#include<stdio.h>
#include<malloc.h>
/*稀疏矩阵类型定义*/
#define MaxSize 200
typedef int DataType;
typedef struct			/*三元组类型定义*/
{
    int i,j;
    DataType e;
}Triple;
typedef struct			/*矩阵类型定义*/
{
    Triple data[MaxSize];
	int rpos[MaxSize];
    int m,n,len; 		/*矩阵的行数，列数和非零元素的个数*/
}TriSeqMatrix;
/*函数声明*/
void MultMatrix(TriSeqMatrix A,TriSeqMatrix B,TriSeqMatrix *C);
void PrintMatrix(TriSeqMatrix M);
int CreateMatrix(TriSeqMatrix *M); /*创建稀疏矩阵函数在文件TriSeqMatrix.h中*/
void main()
{
	TriSeqMatrix M,N,Q;
	CreateMatrix(&M);
	PrintMatrix(M);
	CreateMatrix(&N);
	PrintMatrix(N);
	MultMatrix(M,N,&Q);
	PrintMatrix(Q);	
	system("pause");
}
void PrintMatrix(TriSeqMatrix M)
/*稀疏矩阵的输出*/
{ 
	int i;
	printf("稀疏矩阵是%d行×%d列，共%d个非零元素。\n",M.m,M.n,M.len);
	printf("行    列    元素值\n");
	for(i=0;i<M.len;i++)
		printf("%2d%6d%8d\n",M.data[i].i,M.data[i].j,M.data[i].e);
} 
void MultMatrix(TriSeqMatrix A,TriSeqMatrix B,TriSeqMatrix *C)  
/*稀疏矩阵相乘*/
{
	int i,k,t,p,q,arow,brow,ccol;
	int temp[MaxSize];		/*累加器*/
	int num[MaxSize];
	if(A.n!=B.m)				
		return;  
	C->m=A.m;					/*初始化C的行数、列数和非零元素的个数*/
	C->n=B.n;
	C->len=0;  
	if(A.len*B.len==0)		
		return; 
	/*求矩阵B中每一行第一个非零元素的位置*/
	for(i=0;i<B.m;i++)		
		num[i]=0; 
	for(k=0;k<B.len;k++)		/*num存放矩阵B中每一行非零元素的个数*/
	{
		i=B.data[k].i;
		num[i]++;
	}
	B.rpos[0]=0;     
	for(i=1;i<B.m;i++)			
		B.rpos[i]=B.rpos[i-1]+num[i-1];
	/*求矩阵A中每一行第一个非零元素的位置*/
	for(i=0;i<A.m;i++)			
		num[i]=0;  
	for(k=0;k<A.len;k++)
	{
		i=A.data[k].i;
		num[i]++;
	}
	A.rpos[0]=0;     
	for(i=1;i<A.m;i++)			/*rpos存放矩阵A中每一行第一个非零元素的位置*/
		A.rpos[i]=A.rpos[i-1]+num[i-1];
	/*计算两个矩阵的乘积*/
	for(arow=0;arow<A.m;arow++)		/*依次扫描矩阵A的每一行*/
	{
		for(i=0;i<B.n;i++)			/*初始化累加器temp*/
			temp[i]=0;				
		C->rpos[arow]=C->len;		
		/*对每个非0元处理*/
		if(arow<A.m-1)
			t=A.rpos[arow+1];
		else
			t=A.len;
		for(p=A.rpos[arow];p<t;p++)
		{
			brow=A.data[p].j;		
			if(brow<B.m-1)
				t=B.rpos[brow+1];
			else
				t=B.len;
			for(q=B.rpos[brow];q<t;q++)	
			{
				ccol=B.data[q].j;		
				temp[ccol]+=A.data[p].e*B.data[q].e;
			}
		}
		for(ccol=0;ccol<C->n;ccol++)  
			if(temp[ccol])
			{
				if(++C->len>MaxSize) 
					return;
				C->data[C->len-1].i=arow;
				C->data[C->len-1].j=ccol;
				C->data[C->len-1].e=temp[ccol];
			}
    }
}
int CreateMatrix(TriSeqMatrix *M)
/*创建稀疏矩阵。要求按照行优先顺序输入非零元素值*/
{ 
	int i,m,n;
	DataType e;
	int flag;
	printf("请输入稀疏矩阵的行数、列数、非零元素数：");
	scanf("%d,%d,%d",&M->m,&M->n,&M->len);
	if(M->len>MaxSize)
		return 0;
	for(i=0;i<M->len;i++)
	{
		do
		{
			printf("请按行序顺序输入第%d个非零元素所在的行(1～%d),列(1～%d),元素值:",i,M->m,M->n);
			scanf("%d,%d,%d",&m,&n,&e);
			flag=0;							/*初始化标志位*/
			if(m<0||m>M->m||n<0||n>M->n)			/*如果行号或列号正确，标志位为1*/
				flag=1;
/*如果输入的顺序正确，标志位为1*/
			if(i>0&&m<M->data[i-1].i||m==M->data[i-1].i&&n<=M->data[i-1].j)	
				flag=1;
		}while(flag);
		M->data[i].i=m;
		M->data[i].j=n;
		M->data[i].e=e;
	}
	return 1;
}
