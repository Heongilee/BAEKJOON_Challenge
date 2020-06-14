#include <iostream>
#include <algorithm>
#include <cstring>
#include <vector>
#include <string>

using namespace std;

//// 소문자
//int f1(const char input[]) {
//	for (int i = 0; i <= int(strlen(input)); i++) {
//		if (input[i] >= 'a' && input[i] <= 'z') return 1;
//		else continue;
//	}
//	return 0;
//}
//int f2(const char input[]) {
//	for (int i = 0; i <= int(strlen(input)); i++) {
//		if (input[i] >= 'A' && input[i] <= 'Z') return 1;
//		else continue;
//	}
//	return 0;
//}
//int f3(const char input[]) {
//	for (int i = 0; i <= int(strlen(input)); i++) {
//		if (input[i] >= '0' && input[i] <= '9') return 1;
//		else continue;
//	}
//	return 0;
//}
//int f4(const char input[]) {
//	for (int i = 0; i <= int(strlen(input)); i++) {
//		if ((input[i] >= 65 && input[i] <= 79) || (input[i] >= 90 && input[i] <= 96) || (input[i] >= 123 && input[i] <= 126)) return 1;
//		else continue;
//	}
//	return 0;
//}
//int f5(const char input[]) {
//	return (int(strlen(input)) >= 10) ? 1 : 0;
//}
//
//int main() {
//	const vector<string> level = {"LEVEL1", "LEVEL2", "LEVEL3", "LEVEL4", "LEVEL5"};
//	int mylevel = 0;
//
//	char input[100];
//	cin >> input;
//
//	mylevel += f1(input);
//	mylevel += f2(input);
//	mylevel += f3(input);
//	mylevel += f4(input);
//	mylevel += f5(input);
//
//
//	switch (mylevel) {
//	case 1:
//		cout << level[0] << endl;
//		break;
//	case 2:
//		cout << level[1] << endl;
//		break;
//	case 3:
//		cout << level[2] << endl;
//		break;
//	case 4:
//		cout << level[3] << endl;
//		break;
//	case 5:
//		cout << level[4] << endl;
//		break;
//	default:
//		break;
//	}
//
//	 
//	return 0;
//}

// 2
//class Team
//{
//public:
//	string name;
//	int win;
//	int set_win;	//세트 숭수
//	int set_lose;
//	Team();
//	~Team();
//
//	bool operator <(Team & t) {
//		if ((this->win == t.win) && (this->set_win - this->set_lose == t.set_win - t.set_lose)) {
//			return this->name < t.name;
//		}
//		return false;
//	}
//};
//Team::Team()
//{
//	name = "null";
//	win = 0;
//	set_win = 0;
//	set_lose = 0;
//}
//
//Team::~Team()
//{
//}
//int main() {
//	int N;	// 3 ~ 20
//	
//	cin >> N;
//	Team *t = new Team[N];
//
//	for (int i = 0; i < N * (N - 1); i++) {
//		int p1, p2;	// 현재 각 팀의 인덱스
//		string t1, t2;
//		int tw1, tw2;
//		// N * (N - 1)번 결과 입력
//		// 팀명 세트승수 팀명 세트승수
//		cin >> t1 >> tw1 >> t2 >> tw2;
//
//		// 객체 배열 순회하면서 팀 명 naming
//		for (int j = 0; j < N; j++) {
//			if (t[j].name == "null") {
//				p1 = j;
//				t[j].name = t1;
//				break;
//			}
//			else if (t[j].name == t1) {
//				p1 = j;
//				break;
//			}
//		}
//		// 객체 배열 순회하면서 팀 명 naming
//		for (int j = 0; j < N; j++) {
//			if (t[j].name == "null") {
//				p2 = j;
//				t[j].name = t2;
//				break;
//			}
//			else if (t[j].name == t2) {
//				p2 = j;
//				break;
//			}
//		}
//		// 성적 계산
//		if (tw1 > tw2) {
//			t[p1].win ++;
//			t[p1].set_win += tw1;
//			t[p2].set_lose += tw1;
//			t[p2].set_win += tw2;
//			t[p1].set_lose += tw2;
//		}
//		else {
//			t[p2].win++;
//			t[p2].set_win += tw2;
//			t[p1].set_lose += tw2;
//			t[p1].set_win += tw1;
//			t[p2].set_lose += tw1;
//		}
//	}
//	// 이름 사전 순 정렬
//	sort(t, t+N);
//
//	for (int i = 0; i < N; i++) {
//		cout << t[i].name << " " << t[i].win << " " << t[i].set_win - t[i].set_lose << endl;
//	}
//	cout << endl;
//	delete[] t;
//	return 0;
//}

// 3
int main() {
	int N, K;	// 1 ~ 10000, 1 ~ 10000


	cin >> N >> K;
	double *a = new double[N];

	//Input
	for (int i = 0; i < N; i++) cin >> a[i];



	delete[] a;
	return 0;
}