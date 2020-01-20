package _2798;

import java.util.Scanner;

class BlackJack {
	private static Scanner sc = new Scanner(System.in);
	private int N, M;
	private int min = 0;
	private int[] arr;

	public BlackJack() {
		this.setN(sc.nextInt());
		this.setM(sc.nextInt());
		
		arr = new int[N];
		
		for(int i=0;i<N;i++)
			arr[i] = sc.nextInt();
		
		for(int i=0;i<N - 2;i++) {
			for(int j=i + 1;j<N - 1;j++) {
				for(int k=j+1;k<N;k++) {
					if((arr[i] + arr[j] + arr[k] <= this.getM())&&(arr[i] + arr[j] + arr[k] > this.getMin())) {
						this.setMin(arr[i] + arr[j] + arr[k]);
					}
				}
			}
		}
		
		System.out.println(this.getMin());
		sc.close();
	}

	public int getN() {
		return N;
	}

	public void setN(int n) {
		N = n;
	}

	public int getM() {
		return M;
	}

	public void setM(int m) {
		M = m;
	}

	public int getMin() {
		return min;
	}

	public void setMin(int min) {
		this.min = min;
	}
}

public class Main {
	public static void main(String[] args) {
		// 백준 2798번 : 블랙 잭
		new BlackJack();
	}
}
