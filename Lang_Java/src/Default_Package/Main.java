package Default_Package;

import java.util.Scanner;

public class Main {
	public static int fibo(int N) {
		if(N == 0) return 0;
		if(N == 1) return 1;
		else return fibo(N - 1) + fibo(N - 2);
	}
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int N;
		
		N = sc.nextInt();
		
		System.out.println(fibo(N));
		
		sc.close();
	}
}