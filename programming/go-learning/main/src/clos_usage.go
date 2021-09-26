package main

import (
	"fmt"
	"time"
)

var ids = []int{1, 2, 3, 4, 5}

func process(n int) {
	time.Sleep(50 * time.Millisecond)
	fmt.Println(n)
}

func main() {
	for i := 0; i < len(ids); i++ {
		go func(input int) {
			process(input)

		}(i)
	}
	for {

	}
}
