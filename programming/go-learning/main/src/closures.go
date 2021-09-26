package main

import "fmt"

func adder() func(int) int {
	sum := 0
	return func(x int) int {
		sum += x
		return sum
	}

}

func main() {

	addFunc := adder()
	fmt.Println(addFunc(10))
	fmt.Println(addFunc(20))

	sndFunc := adder()
	fmt.Println(sndFunc(10))
	fmt.Println(sndFunc(20))

}
