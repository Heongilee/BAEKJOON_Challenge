package _11729;

import java.util.Scanner;

public class Main {
	private static Scanner sc = new Scanner(System.in);
	private static int[][] arr;
	public static void move_to(int from, int to) {
		arr[to][0] = arr[from][0];
		
		return;
	}
	public static void Hanoi(int N, int from, int by, int to) {
		if(N == 1) {
			move_to(from, to);
		}
		else {
			Hanoi(N - 1, from, to, by);
			move_to(from, to);
			Hanoi(N - 1, by, from, to);
		}
	}
	public static void rHanoi(int N) {
		
	}
	public static void main(String[] args) {
		arr = new int [3][];
		//원판 수 N 입력.
		int N;
		N = sc.nextInt();
		int cnt = 1;
		
		//연산 횟수 = 2^N - 1
		for(int i=0;i<N;i++) {
			cnt *= 2;
		}
		cnt -= 1;
		System.out.println(cnt);
		
		//탑 초기화
		for(int i=0;i<3;i++) {
			arr[i] = new int[N];
			for(int j=0;j<5;j++) {
				if(i == 0) arr[i][j] = j + 1;
				else arr[i][j] = -1;
			}
		}
		
		
		rHanoi(N);
		sc.close();	//Scanner close
	}
}