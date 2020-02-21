package Default_Package;

import java.util.Scanner;

public class Main {
	private static Scanner sc = new Scanner(System.in);
	public static void add(int a, int b) {
		System.out.println("Function 1 is called...");
	}
	public static void add(double a, double b) {
		System.out.println("Function 2 is called...");
		
	}
	public static void main(String[] args) {
		add(1, 2);
		add(3.1, 4.2);
	}
}