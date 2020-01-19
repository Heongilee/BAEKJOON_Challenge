#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#pragma warning(disable:4996)

//Hanoi Tower
typedef struct Towers {
	int** Matrix;
	int* Size_arr;
}T;
void insertion_sort(int* arr, int N) {
	for (int i = 0; i < N - 1;i++) 
	{
		int j = i;
		int k = i + 1;	//key
		int tmp = arr[k];
		while (j >= 0 && arr[j] > tmp) {
			arr[j + 1] = arr[j];
			j--;
		}
		arr[j + 1] = tmp;
	}

	return;
}
void put(int* arr, int* N, int elem) { // -1인 곳을 찾아서 원소를 넣고 삽입정렬 수행.
	arr[*N] = elem;
	(*N)++;
	insertion_sort(arr, *N);

	return;
}
int get_E(int* arr, int* N) { //맨 위에 있는 원소를 삭제하고 해당 원소를 반환.
	if ((*N) == 0) {
		printf("\n Dont Exist Elem... \n");
		return -1;
	}
	int res = arr[0];
	int i;
	for (i = 0; i < (*N) - 1;i++)	//moving down
		arr[i] = arr[i + 1];
	arr[i] = -1;

	(*N)--;

	return res;
}
//void P(const T* t) {
//	printf("\n------------------------------------------\n");
//	for (int i = 0; i < t->Size_arr[0]; i++)
//		printf(" %d", t->Matrix[0][i]);
//	printf("\n");
//
//	for (int i = 0; i < t->Size_arr[1]; i++)
//		printf(" %d", t->Matrix[1][i]);
//	printf("\n");
//
//	for (int i = 0; i < t->Size_arr[2]; i++)
//		printf(" %d", t->Matrix[2][i]);
//	printf("\n");
//
//
//	return;
//}
void move_to(T* t, int a, int b) {
	put(t->Matrix[b], &(t->Size_arr[b]), get_E(t->Matrix[a], &(t->Size_arr[a])));

	printf("%d %d\n", a + 1, b + 1);
	return;
}
void Hanoi(T* t, int S, int from, int by, int to) {
	if (S == 1) {
		move_to(t, from, to);
	}
	else {
		Hanoi(t, S - 1, from, to, by);
		move_to(t, from, to);
		Hanoi(t, S - 1, by, from, to);
	}
	return;
}
void rHanoi(T* t) {//Driver
	int cnt = 1;
	for (int i = 0; i < t->Size_arr[0]; i++)
		cnt *= 2;
	cnt--;	//2^N - 1

	printf("%d\n", cnt);
	Hanoi(t, t->Size_arr[0], 0, 1, 2);

	return;
}
int main() 
{
	//// 11729번 문제 하노이탑 문제를 재귀함수로 해결.
	T t;
	int N;

	scanf("%d", &N);

	//초기 설정.
	t.Matrix = (int**)malloc(sizeof(int*) * 3);
	if (t.Matrix == NULL) return -1;
	t.Size_arr = (int*)malloc(sizeof(int) * 3);
	if (t.Size_arr == NULL) return -1;


	if (t.Matrix == NULL) return -1;
	for (int i = 0; i < 3; i++)
	{
		t.Matrix[i] = (int*)malloc(sizeof(int) * N);
		if (t.Matrix[i] == NULL) return -1;

		//값 초기화
		for (int j = 0; j < N; j++) {
			if (i == 0) {
				t.Matrix[i][j] = j + 1;
			}
			else {
				t.Matrix[i][j] = -1;
			}
		}

		//사이즈 초기화
		if (i == 0)
			t.Size_arr[i] = N;
		else
			t.Size_arr[i] = 0;

	}

	rHanoi(&t);

	return 0;
}
