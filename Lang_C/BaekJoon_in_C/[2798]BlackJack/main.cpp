#include <stdio.h>
#include <stdlib.h>
#pragma warning (disable:4996)

int main() {
	// 2798�� : ���� ����
	/////////////////////////////////////////////////////////////////////////////////////////
	// �ٽ��� 3�� for�� ����ð��� nC3���� ����� ��!
	/////////////////////////////////////////////////////////////////////////////////////////


	int N, M;
	int *arr;
	
	scanf("%d%d", &N, &M);
	
	arr = (int*)malloc(sizeof(int) * N);
	if (arr == NULL) return -1;

	for (int i = 0; i < N; i++)
		scanf("%d", &arr[i]);

	int min = 0;

	//����� �� : nC3
	for (int i = 0; i < N - 2; i++) 
	{
		for (int j = i + 1; j < N - 1; j++)
		{
			for (int k = j + 1; k < N; k++) {
				if ((arr[i] + arr[j] + arr[k] <= M) && (arr[i] + arr[j] + arr[k] > min)) {
					min = arr[i] + arr[j] + arr[k];
				}
			}
		}
	}
	printf("%d", min);

	//dealloc
	free(arr);
	return 0;
}