package main

import (
    "fmt"
)

func main() {
	for {
		// input
		var x, y int
		var op string
	
		fmt.Scan(&x, &op, &y)
		if op == "?" {
			return
		}
		
		if op == "+" {
			fmt.Println(x + y)
		} else if op == "-" {
			fmt.Println(x - y)
		} else if op == "*" {
			fmt.Println(x * y)
		} else if op == "/" {
			fmt.Println(x / y)
		} else {
			fmt.Println("Invalid operator")
		}
	
	}
    
}