package main

import ("fmt")

func say_hello(msg string){
	fmt.Println(msg)
}

func reg_ret_ano_fun() func(string){

	return func(msg string){
		fmt.Println(msg)
	}

}

func main(){
	// regular function
	// say_hello("hello howdy")

	func(msg string) {
		fmt.Println(msg)
	}("hello anonyfunc howdy")

	print_fnc := reg_ret_ano_fun()
	print_fnc("hello regu fun retn ano func")

}