#include <stdio.h>
#pragma warning(disable:4996)

void calc(int a, int b)	//1. �Ķ���� Ÿ�� ���
{
	//int a, b;	//2.�Ķ���� ������ ����ϹǷ� �ߺ��ؼ� ���� ���� �� �ʿ�
	if (a > b)
		printf(">");
	else if (a < b)
		printf("<");
	else if (a == b)
		printf("==");
	else return ;	//3. void type�̱� ������ ���ϰ� �ʿ� ����.
}

void main()
{
	int a, b;
	scanf("%d%d", &a, &b);
	calc(a, b);

	return;
}