package main
import ("fmt"
		"strings")

func mult(a,b int) int{
	multi:= a * b
	return multi
}

// Variadic function to join strings
func joinstr(element...string)string{
	defer fmt.Println("hello")
	println("before")
	return strings.Join(element, "-")
}

func main(){
	fmt.Printf("multi is : %d",mult(2,3))
	fmt.Println(joinstr())
	fmt.Println(joinstr("A", "E", "I", "O", "U"))
}


