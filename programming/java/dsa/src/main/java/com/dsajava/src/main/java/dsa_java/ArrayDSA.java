package com.dsajava.src.main.java.dsa_java;

class ArrayDSA
{

public static void main(String[] args){
   
int[] arr;
// allocating memory for 2 integers
arr = new int[2];
// initialize first element of array
arr[0] =10;
arr[1] =15;

// accessing specified element in array
 for (int i =0; i < arr.length ; i++)
    System.out.println("Elements at index" + i +": " + arr[i]);
}   

}