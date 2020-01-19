#include <stdio.h>
#include <stdlib.h>

int fibo(int N) {
	if (N == 0) return 0;
	if (N == 1) return 1;
	else return fibo(N - 1) + fibo(N - 2);
}
int main() 
{
	/*
	10870번 문제

	(워밍업으로 )피보나치 수 재귀함수 짜보기
	*/

	int N;

	scanf("%d", &N);

	printf("%d", fibo(N));
	return 0;
}