#include <iostream>
#include <algorithm>

//Sol2.에 추가된 헤더
#include <queue>

using namespace std;

////Sol1. Dynamic_Programming으로 풀기.
//class DP {
//private:
//	int N;
//	int* D;
//
//public:
//	DP(){
//		cin >> this->N;
//
//		//mem_alloc
//		this->D = new int[this->N + 1];
//
//		this->run();
//	}
//
//	~DP() {
//		delete[] D;
//	}
//
//	void run() {
//		//인덱스 0는 비워둔다.
//		this->D[0] = -1;
//		
//		//인덱스가 숫자고, 값이 숫자까지 가기위해 최소 경우의 수라고 했을 때...
//		this->D[1] = 0;
//
//		for (int i = 2; i <= this->N; i++) {
//			//작은 연산부터 시도해본다.
//			D[i] = D[i - 1] + 1;
//
//			if (i % 2 == 0) {
//				D[i] = std::min(D[i], D[i / 2] + 1);
//			}
//			if (i % 3 == 0) {
//				D[i] = std::min(D[i], D[i / 3] + 1);
//			}
//		}
//		return;
//	}
//
//	void print(){
//		cout << this->D[this->N] << endl;
//
//		return;
//	}
//
//};
//int main() 
//{
//	DP().print();
//
//	return 0;
//}

//2. Queue ADT를 이용한 BFS 알고리즘으로 해결
class BFS {
private:
	int N;
	bool* visited;
	std::queue<pair<int, int>> q;	//pair의 first는 숫자, second는 그 숫자까지 도달하는 최소의 경우 수.
	int res;

public:
	BFS() {
		cin >> this->N;

		this->visited = new bool[this->N + 1]{ false };
		res = 0;

		this->run();
	}

	~BFS() {
		delete[] this->visited;
	}

	void run() {
		// Solution URL : https://blockdmask.tistory.com/257?category=250801
	}
};
int main() 
{
	
	return 0;
}