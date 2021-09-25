package main

import ("fmt"
		"bufio"
		"os"
		"strconv"
)

func main()  {

scanner := bufio.NewScanner(os.Stdin)
fmt.Printf("Type the year born: ")
scanner.Scan()
input,_ := strconv.ParseInt(scanner.Text(),10,64)
fmt.Printf("Ur age %d : ", 2021 - input)

}