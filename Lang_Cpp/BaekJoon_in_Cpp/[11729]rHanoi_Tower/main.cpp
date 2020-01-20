#include <iostream>
#include <algorithm>	//sort를 사용하기 위함 -> 퀵 소트를 사용함 O(NlogN)
#include <cmath>		//std::pow를 사용하기위함.
#pragma warning(disable:4996)

using namespace std;

void move_to(int** arr, const int &N, const int &from, const int &to) {
	int j;
	for (int i = 0; i < N; i++) {
		if (arr[to][i] == -1) {
			arr[to][i] = arr[from][0];
		}
	}

	//to 타워 sorting
	sort(arr[to], arr[to] + N);

	//from 타워에 있는 첫번째 원소 삭제하기 (moving down)
	for (j = 0; j < N - 1; j++) {
		arr[from][j] = arr[from][j + 1];
	}
	arr[from][j] = -1;

	//cout << from + 1 << " " << to + 1 << endl;
	printf("%d %d\n", from + 1, to + 1);
	return;
}
inline void rHanoi(int** arr, const int &N, const int &from, const int &by, const int &to) {
	if (N == 1) {
		move_to(arr, N, from, to);
	}
	else {
		rHanoi(arr, N - 1, from, to, by);
		move_to(arr, N, from, to);
		rHanoi(arr, N - 1, by, from, to);
	}
	return;
}
void Hanoi(const int &N, const int &from, const int &by, const int &to) {
	int** arr = new int*[3];

	//Initializing
	for (int i = 0; i < 3; i++) {
		arr[i] = new int[N];
		for (int j = 0; j < N; j++) {
			if (i == 0) {
				arr[i][j] = j + 1;
			}
			else {
				arr[i][j] = -1;
			}
		}
	}

	rHanoi(arr, N, from, by, to);

	//dealloc
	for (int i = 0; i < 3; i++)
		delete[] arr[i];
	delete[] arr;

	return;
}
void hanoi_Count(const int &N) {
	//cout << std::pow(2.0, N) - 1 << endl;
	printf("%d\n", (int)(std::pow(2.0, N) - 1));
}
int main() 
{
	////////////////////////////////////////////////////////////////////////////////
	//						※	11729번 : 하노이 탑	※
	//	Language : C++
	// 핵심 : cout & cin 문장이 생각보다 시간을 많이 잡아 먹는 것 같다.
	// 앞으로 printf & scanf를 써야할 것 같다...
	////////////////////////////////////////////////////////////////////////////////

	int N;

	scanf("%d", &N);

	hanoi_Count(N);
	Hanoi(N, 0, 1, 2);

	return 0;
}