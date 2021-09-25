package main

import "fmt"

func main() {
	var name string = "codingbitz"
	var number uint16 = 12345
	var salary float32 = 12345.67
	var bonus float32 = 123.45
	var tot_sal float32 = salary + bonus

    fmt.Println("Hello World!", name, number, tot_sal)
}