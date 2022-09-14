package javalearning;

import java.util.Arrays;

public class Array {
	public static void main(String[] args) {
		//int physics = 73;
		//int che = 89;
		//int math = 92;
		int [] marks = new int[3];
		marks[0] = 73;
		marks[1] = 89;
		marks[2] = 92;
		System.out.println(marks[1]);
		//Lenght
		System.out.println(marks.length);
		
		System.out.println(marks[0]);
		
		//sort
		Arrays.sort(marks);
		System.out.println(marks[0]);
	}

}
