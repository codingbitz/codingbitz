package main

import "fmt"

// Main function
func main() {
	
	// Here rvariable is a array
	rvariable:= []string{"ABC", "DEF", "QRDR"}
	for i, j:= range rvariable {
	fmt.Println(i, j)
	}
	
}