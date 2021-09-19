package com.dsajava.src.main.java.dsa_java;

class ArrayDSAMthod
{

public static void main(String args[]){
// Driver method   
int arr[]= {1,2,3};

// accessing specified element in array
 for (int i =0; i < 2 ; i++)
 // pass array to method
     sum(arr);
}   


public static void sum(int[] arr) {
    int sum =0;
    for (int i =0; i  <arr.length; i++)
        sum +=arr[i];

    System.out.println("Sum    :" + sum);
    
}
}
