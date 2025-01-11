package main

import (
	"fmt"
)

func main() {
	var a, b, c, divisors int
	fmt.Scanln(&a, &b, &c)
	
	for a <= b {
		if c % a == 0 {
			divisors++
		}
		a++
	}
	fmt.Println(divisors)
}