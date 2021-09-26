package main

import ( "fmt")

func main()  {
	p:= 1
	q:= 2
   // Addition
   result1:= p + q
   fmt.Printf("\nResult of p + q = %d", result1)
     
   // Subtraction
   result2:= p - q
   fmt.Printf("\nResult of p - q = %d", result2)
     
   // Multiplication
   result3:= p * q
   fmt.Printf("\nResult of p * q = %d", result3)
     
   // Division
   result4:= p / q
   fmt.Printf("\nResult of p / q = %d", result4)
     
   // Modulus
   result5:= p % q
   fmt.Printf("\nResult of p %% q = %d", result5)

   // & (bitwise AND)
   result6:= p & q
   fmt.Printf("\nResult of p & q = %d", result6)
     
   // | (bitwise OR)
   result7:= p | q
   fmt.Printf("\nResult of p | q = %d", result7)
     
   // ^ (bitwise NOT)
   result8:= p ^ q
   fmt.Printf("\nResult of p ^ q = %d", result8)
     
   // << (left shift)
   result9:= p << 1
   fmt.Printf("\nResult of p << 1 = %d", result9)
     
   // >> (right shift)
   result10:= p >> 1
   fmt.Printf("\nResult of p >> 1 = %d", result10)   


}