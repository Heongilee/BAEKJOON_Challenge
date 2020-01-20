package Default_Package;

import java.util.Scanner;

public class Main {
	public static void add(int a, int b) {
		System.out.println("Function 1 is called...");
	}
	public static void add(double a, double b) {
		System.out.println("Function 2 is called...");
		
	}
	public static int add(int a, int b) {
		System.out.println("Function 3 is called...");
		
	}
	public static void main(String[] args) {
		add(1, 2);
		add(3.1, 4.2);
	}
}