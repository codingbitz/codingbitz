// Golang program to illustrate
// the working of the slice components
package main

import "fmt"

func main() {

	// Creating an array
	arr := [7]string{"This", "is", "the", "tutorial",
						"of", "Go", "language"}

	// Display array
	fmt.Println("Array:", arr)

	// Creating a slice
	myslice := arr[1:6]

	// Display slice
	fmt.Println("Slice:", myslice)

	// Display length of the slice
	fmt.Printf("Length of the slice: %d", len(myslice))

	// Display the capacity of the slice
	fmt.Printf("\nCapacity of the slice: %d", cap(myslice))

// using the var keyword
	var my_slice_1 = []string{"Geeks", "for", "Geeks"}
 	fmt.Println("\nMy Slice 1:", my_slice_1)
//using shorthand declaration
	my_slice_2 := []int{12, 45, 67, 56, 43, 34, 45}
	fmt.Println("\nMy Slice 2:", my_slice_2)
}
