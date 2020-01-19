package _11729;

import java.util.Arrays;
import java.util.Scanner;

/////////////////////////////////////////////////////
// �������� �迭 (3 x N)�� �̿��� �ϳ���ž ����Լ��� �����غ���
// Time Limit Error �ߴµ� ������ �𸣰ڴ�.
// ���̺귯�� �ᰡ���� ���� ����ð��� ������...
// Ȥ�� moving down �����ΰ�??
// �ٵ�, �Ʊ� ���� ��ôµ��� Time Limit �ߴ��� ���� ��¥
// �� ���� �ڹٷ� Ǫ�°� �����ΰ� ������ ����
/////////////////////////////////////////////////////
public class Main {
	private static int[][] arr;
	private static Scanner sc = new Scanner(System.in);
	public static void put(int t, int e) {	//t��° Ÿ���� ���� e�� �ִ´�.
		for(int i=0;i<arr[t].length;i++) {
			if(arr[t][i] == -1) {
				arr[t][i] = e;
			}
			// Arrays ���̺귯���� �ִ� Quick-Sort (Big-O nlog(n))
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
		// ���� �� = 2^N - 1;
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