/*����ͷ�ļ��͹�������Ļ���������ʵ���ļ�*/
#include <stdio.h>
#include<malloc.h>
#include<stdlib.h>
#include<string.h>
typedef char AtomType;
#include"GList.h"
#include"SeqString.h"
/*��������*/
void CreateList(GList *L,SeqString S);
void DistributeString(SeqString *Str,SeqString *HeadStr);
void PrintGList(GList L);

void main()
{
	GList L,T;
	SeqString S;
	int depth,length;
	StrAssign(&S,"(a,(),(a,(b,c)))");	/*���ַ�����ֵ����S*/
	CreateList(&L,S);				/*�ɴ����������L*/
	printf("��������L�е�Ԫ��:\n");
	PrintGList(L);					/*���������е�Ԫ��*/
	length=GListLength(L);			/*������ĳ���*/
	printf("\n�����L�ĳ���length=%2d\n",length);
	depth=GListDepth(L);			/*����������*/
	printf("�����L�����depth=%2d\n",depth);
	CopyList(&T,L);
	printf("�ɹ����L���Ƶõ������T.\n�����T��Ԫ��Ϊ:\n");
	PrintGList(T);
	length=GListLength(T);			/*������ĳ���*/
	printf("\n�����T�ĳ���length=%2d\n",length);
	depth=GListDepth(T);			/*����������*/
	printf("�����T�����depth=%2d\n",depth);
	system("pause");
}
void CreateList(GList *L,SeqString S)
/*����ͷβ�����������*/
{
	SeqString Sub,HeadSub,Empty;
	GList p,q;
	StrAssign(&Empty,"()"); 
	if(!StrCompare(S,Empty))			/*�������Ĵ��ǿմ��򴴽�һ���յĹ����*/
		*L=NULL; 
	else 
	{
		if(!(*L=(GList)malloc(sizeof(GLNode))))		/*Ϊ���������һ�����*/
			exit(-1);
		if(StrLength(S)==1)							/*�������ԭ�ӣ���ԭ�ӵ�ֵ��ֵ���������*/
		{
			(*L)->tag=ATOM;
			(*L)->atom=S.str[0];
		}
		else										/*������ӱ�*/
		{
			(*L)->tag=LIST;
			p=*L;
			SubString(&Sub,S,2,StrLength(S)-2);		/*��Sȥ�����������ţ�Ȼ��ֵ��Sub*/
			do
			{ 
				DistributeString(&Sub,&HeadSub);	/*��Sub�������ͷ�ͱ�β�ֱ�ֵ��HeadSub��Sub*/
				CreateList(&(p->ptr.hp),HeadSub);	/*�ݹ�������ɹ����*/
				q=p;
				if(!StrEmpty(Sub))					/*�����β���գ������ɽ��p������βָ����ָ��p*/
				{
					if(!(p=(GLNode *)malloc(sizeof(GLNode))))
						exit(-1);
					p->tag=LIST;
					q->ptr.tp=p;
				}
			}while(!StrEmpty(Sub));
			q->ptr.tp=NULL;
		}
	}
}
void PrintGList(GList L)
/*���������Ԫ��*/
{
	if(L)								/*����������*/
	{
		if(L->tag==ATOM)				/*�����ԭ�ӣ������*/
			printf("%c ",L->atom);
		else 
		{
			PrintGList(L->ptr.hp);		/*�ݹ����L�ı�ͷ*/
			PrintGList(L->ptr.tp);		/*�ݹ����L�ı�β*/
		}
	}
}

void DistributeString(SeqString *Str,SeqString *HeadStr)
/*����Str������������֣�HeadStrΪ��һ������֮ǰ���Ӵ���StrΪ���ź���Ӵ�*/
{ 
	int len,i,k; 
	SeqString Ch,Ch1,Ch2,Ch3;
	len=StrLength(*Str);				
	StrAssign(&Ch1,",");			
	StrAssign(&Ch2,"("); 
	StrAssign(&Ch3,")"); 
	SubString(&Ch,*Str,1,1);		
	for(i=1,k=0;i<=len&&StrCompare(Ch,Ch1)||k!=0;i++) 
	{ 
		SubString(&Ch,*Str,i,1);		
		if(!StrCompare(Ch,Ch2))			/*�����һ���ַ���'('������k��1*/
			k++; 
		else if(!StrCompare(Ch,Ch3))	
			k--; 
	}
	if(i<=len)							/*��Str�д���','�����ǵ�i-1���ַ�*/
	{
		SubString(HeadStr,*Str,1,i-2);	
		SubString(Str,*Str,i,len-i+1);	/*Str���洮Str','����ַ�*/
	}
	else								/*��Str�в�����','*/
	{
		StrCopy(HeadStr,*Str);			/*����Str�����ݸ��Ƶ���HeadStr*/
		StrClear(Str);					/*��մ�Str*/
	}
}
