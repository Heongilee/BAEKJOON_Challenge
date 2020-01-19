package _11729;

import java.util.Arrays;
import java.util.Scanner;

/////////////////////////////////////////////////////
// 비정방형 배열 (3 x N)을 이용한 하노이탑 재귀함수로 구현해보기
// Time Limit Error 뜨는데 왜인지 모르겠다.
// 라이브러리 써가지고 정렬 수행시간도 괜찮고...
// 혹시 moving down 때문인가??
// 근데, 아까 벡터 써봤는데도 Time Limit 뜨던데 뭐지 진짜
// 아 백준 자바로 푸는거 에바인거 같은데 ㄹㅇ
/////////////////////////////////////////////////////
public class Main {
	private static int[][] arr;
	private static Scanner sc = new Scanner(System.in);
	public static void put(int t, int e) {	//t번째 타워에 원판 e를 넣는다.
		for(int i=0;i<arr[t].length;i++) {
			if(arr[t][i] == -1) {
				arr[t][i] = e;
			}
			// Arrays 라이브러리에 있는 Quick-Sort (Big-O nlog(n))
			Arrays.sort(arr[t], 0, i);
			
		}
		
		return;
	}
	public static int rm(int t) {
		int res = arr[t][0];
		int i;
		for(i=0;i<arr[t].length - 1;i++) {	//moving down (Big-O n)
			arr[t][i] = arr[t][i + 1];
		}
		arr[t][i] = -1;
		
		return res;
	}
	public static void move_to(int from, int to) {
		put(from, rm(to));
		
		System.out.println((from + 1) + " " + (to + 1));
	}
	public static void Hanoi(int N, int from, int by, int to) {
		if(N == 1) {
			move_to(from, to);
		}
		else {
			Hanoi(N - 1, from, to, by);
			move_to(from ,to);
			Hanoi(N - 1, by, from, to);
		}
		return;
	}
	public static void rHanoi(int N) {
		// 연산 수 = 2^N - 1;
		System.out.println((int)(Math.pow(2.0, (double)N) - 1));
		
		arr = new int[3][];
		for(int i=0;i<3;i++) {
			arr[i] = new int[N];
			for(int j=0;j<N;j++) {
				if(i == 0) arr[i][j] = j + 1;
				else arr[i][j] = -1;
			}
		}
		
		Hanoi(N, 0, 1, 2);
		return;
	}
	public static void main(String[] args) {
		int N;
		
		N = sc.nextInt();
		
		rHanoi(N);
		
		sc.close();
	}
}