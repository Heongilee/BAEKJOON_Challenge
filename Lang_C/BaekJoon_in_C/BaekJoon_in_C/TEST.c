#include <stdio.h>

// ※ Warning : C에서 함수 오버로딩(X)	/	C++에서 함수 오버로딩(O)	/	JAVA에서 함수 오버로딩(O)
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