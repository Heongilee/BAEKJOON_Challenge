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
	10870�� ����

	(���־����� )�Ǻ���ġ �� ����Լ� ¥����
	*/

	int N;

	scanf("%d", &N);

	printf("%d", fibo(N));
	return 0;
}