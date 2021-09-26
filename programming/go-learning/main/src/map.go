// Go program to illustrate how to
// create and initialize a map
// Using make() function
package main

import "fmt"

func main() {

	var myMap = make(map[float64]string)
	fmt.Println(myMap)
	myMap[1.3] = "Rohit"
	myMap[1.5] = "Sumit"
	fmt.Println(myMap[1.3])
	delete(myMap,1.5)
	fmt.Println(myMap)
}
