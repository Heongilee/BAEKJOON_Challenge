#include <iostream>

using namespace std;

int fibo(const int &N) {
	if (N == 0) return 0;
	if (N == 1) return 1;
	else return fibo(N - 1) + fibo(N - 2);
}
int main() 
{
	/*
	10870��
	
	(���־�����) �Ǻ���ġ �� ����Լ��� ¥����
	*/

	int N;

	cin >> N;

	cout << fibo(N);

	return 0;
}