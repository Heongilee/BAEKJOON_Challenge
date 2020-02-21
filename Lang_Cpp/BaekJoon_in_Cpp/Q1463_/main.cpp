#include <iostream>
#include <algorithm>

//Sol2.�� �߰��� ���
#include <queue>

using namespace std;

////Sol1. Dynamic_Programming���� Ǯ��.
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
//		//�ε��� 0�� ����д�.
//		this->D[0] = -1;
//		
//		//�ε����� ���ڰ�, ���� ���ڱ��� �������� �ּ� ����� ����� ���� ��...
//		this->D[1] = 0;
//
//		for (int i = 2; i <= this->N; i++) {
//			//���� ������� �õ��غ���.
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

//2. Queue ADT�� �̿��� BFS �˰������� �ذ�
class BFS {
private:
	int N;
	bool* visited;
	std::queue<pair<int, int>> q;	//pair�� first�� ����, second�� �� ���ڱ��� �����ϴ� �ּ��� ��� ��.
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