#include <stdio.h>

// �� Warning : C���� �Լ� �����ε�(X)	/	C++���� �Լ� �����ε�(O)	/	JAVA���� �Լ� �����ε�(O)
int add(const int a, const int b) {
	return a + b;
}
double add(const double a, const double b) {
	return a + b;
}
int main() {
	printf("%d", add(1, 2));
	printf("%.2lf", add(3.1, 4.2));

	return 0;
}