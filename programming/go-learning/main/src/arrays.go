// Go program to illustrate how to create
// an array using shorthand declaration
// and accessing the elements of the
// array using for loop
package main

import "fmt"

func main() {

// Shorthand declaration of array
arr:= [4]string{"a", "b", "c23", "d4"}

fmt.Println("Elements of the array:")
fmt.Println("Length of the array is:", len(arr))

for i:= 0; i < 3; i++{
fmt.Println(arr[i])
}
// ellipsis
arr_ell:= [...] string{"b","c","d"}
fmt.Println("ellipsis", arr_ell)

// 2 dim array
var arr1 [2][2] int
arr1[0][0] = 100
arr1[0][1] = 200
arr1[1][0] = 300
arr1[1][1] = 400
  
// Accessing the values of the array
fmt.Println("Elements of array 2")
for p:= 0; p<2; p++{
for q:= 0; q<2; q++{
fmt.Println(arr1[p][q])
  
}
}

}
