#include <stdio.h>
#pragma warning(disable:4996)

void calc(int a, int b)	//1. 파라미터 타입 명시
{
	//int a, b;	//2.파라미터 변수를 사용하므로 중복해서 변수 선언 불 필요
	if (a > b)
		printf(">");
	else if (a < b)
		printf("<");
	else if (a == b)
		printf("==");
	else return ;	//3. void type이기 때문에 리턴값 필요 없음.
}

void main()
{
	int a, b;
	scanf("%d%d", &a, &b);
	calc(a, b);

	return;
}