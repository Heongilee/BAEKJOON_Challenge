#include <iostream>

using namespace std;

inline int Black_Jack(const int* arr, const int &N, const int &M) {
	int min = 0;
	for (int i = 0; i < N - 2; i++) {
		for (int j = i + 1; j < N - 1; j++) {
			for (int k = j + 1; k < N; k++) {
				if ((arr[i] + arr[j] + arr[k] <= M) && (arr[i] + arr[j] + arr[k] > min)) {
					min = arr[i] + arr[j] + arr[k];
				}
			}
		}
	}

	return min;
}
int main() 
{
	int N, M;
	cin >> N >> M;

	int* arr = new int[N];

	for (int i = 0; i < N; i++) {
		cin >> arr[i];
	}

	cout << Black_Jack(arr, N, M);
	return 0;
}