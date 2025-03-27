#include<stdlib.h>
#include<stdio.h>
#include<malloc.h>
/*ϡ��������Ͷ���*/
#define MaxSize 200
typedef int DataType;
typedef struct			/*��Ԫ�����Ͷ���*/
{
    int i,j;
    DataType e;
}Triple;
typedef struct			/*�������Ͷ���*/
{
    Triple data[MaxSize];
	int rpos[MaxSize];
    int m,n,len; 		/*����������������ͷ���Ԫ�صĸ���*/
}TriSeqMatrix;
/*��������*/
void MultMatrix(TriSeqMatrix A,TriSeqMatrix B,TriSeqMatrix *C);
void PrintMatrix(TriSeqMatrix M);
int CreateMatrix(TriSeqMatrix *M); /*����ϡ����������ļ�TriSeqMatrix.h��*/
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
/*ϡ���������*/
{ 
	int i;
	printf("ϡ�������%d�С�%d�У���%d������Ԫ�ء�\n",M.m,M.n,M.len);
	printf("��    ��    Ԫ��ֵ\n");
	for(i=0;i<M.len;i++)
		printf("%2d%6d%8d\n",M.data[i].i,M.data[i].j,M.data[i].e);
} 
void MultMatrix(TriSeqMatrix A,TriSeqMatrix B,TriSeqMatrix *C)  
/*ϡ��������*/
{
	int i,k,t,p,q,arow,brow,ccol;
	int temp[MaxSize];		/*�ۼ���*/
	int num[MaxSize];
	if(A.n!=B.m)				
		return;  
	C->m=A.m;					/*��ʼ��C�������������ͷ���Ԫ�صĸ���*/
	C->n=B.n;
	C->len=0;  
	if(A.len*B.len==0)		
		return; 
	/*�����B��ÿһ�е�һ������Ԫ�ص�λ��*/
	for(i=0;i<B.m;i++)		
		num[i]=0; 
	for(k=0;k<B.len;k++)		/*num��ž���B��ÿһ�з���Ԫ�صĸ���*/
	{
		i=B.data[k].i;
		num[i]++;
	}
	B.rpos[0]=0;     
	for(i=1;i<B.m;i++)			
		B.rpos[i]=B.rpos[i-1]+num[i-1];
	/*�����A��ÿһ�е�һ������Ԫ�ص�λ��*/
	for(i=0;i<A.m;i++)			
		num[i]=0;  
	for(k=0;k<A.len;k++)
	{
		i=A.data[k].i;
		num[i]++;
	}
	A.rpos[0]=0;     
	for(i=1;i<A.m;i++)			/*rpos��ž���A��ÿһ�е�һ������Ԫ�ص�λ��*/
		A.rpos[i]=A.rpos[i-1]+num[i-1];
	/*������������ĳ˻�*/
	for(arow=0;arow<A.m;arow++)		/*����ɨ�����A��ÿһ��*/
	{
		for(i=0;i<B.n;i++)			/*��ʼ���ۼ���temp*/
			temp[i]=0;				
		C->rpos[arow]=C->len;		
		/*��ÿ����0Ԫ����*/
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
/*����ϡ�����Ҫ����������˳���������Ԫ��ֵ*/
{ 
	int i,m,n;
	DataType e;
	int flag;
	printf("������ϡ����������������������Ԫ������");
	scanf("%d,%d,%d",&M->m,&M->n,&M->len);
	if(M->len>MaxSize)
		return 0;
	for(i=0;i<M->len;i++)
	{
		do
		{
			printf("�밴����˳�������%d������Ԫ�����ڵ���(1��%d),��(1��%d),Ԫ��ֵ:",i,M->m,M->n);
			scanf("%d,%d,%d",&m,&n,&e);
			flag=0;							/*��ʼ����־λ*/
			if(m<0||m>M->m||n<0||n>M->n)			/*����кŻ��к���ȷ����־λΪ1*/
				flag=1;
/*��������˳����ȷ����־λΪ1*/
			if(i>0&&m<M->data[i-1].i||m==M->data[i-1].i&&n<=M->data[i-1].j)	
				flag=1;
		}while(flag);
		M->data[i].i=m;
		M->data[i].j=n;
		M->data[i].e=e;
	}
	return 1;
}
