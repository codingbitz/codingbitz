// Go program to illustrate the
// use for loop using maps
package main

import "fmt"

// Main function
func main() {
	
	// using maps
	mmap := map[int]string{
		1:"A",
		2:"B",
		3:"C",
	}
	for key, value:= range mmap {
	fmt.Println(key, value)
	}
	
}
