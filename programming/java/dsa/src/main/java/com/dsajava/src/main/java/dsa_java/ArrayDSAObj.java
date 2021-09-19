package com.dsajava.src.main.java.dsa_java;

public class ArrayDSAObj
{

public static void main(String[] args){
   
Product[] arr;
// allocating memory for 2 integers
arr = new Product[2];
// initialize first element of array
arr[0] = new Product(1, "rice");
arr[1] = new Product(2, "carrot");

// accessing specified element in array
 for (int i =0; i < arr.length ; i++)
    System.out.println("Elements at index" + i +": " + arr[i].prod_no + " "+ arr[i].prod_name);
}   

}

class Product
{
public int prod_no;
public String prod_name;
Product(int prod_no, String prod_name)

{
this.prod_no = prod_no;
this.prod_name = prod_name;
}
}