package main

import (
	"fmt"
)

func main() {
	for {
		// two inputs of numbers
		var a, b int
		fmt.Scanln(&a, &b)
		// if both numbers are 0, break the loop
		if a == 0 && b == 0 {
			break
		}
		if a <= b {  // Print in ascending order
			fmt.Printf("%d %d\n", a, b)
		} else {
			fmt.Printf("%d %d\n", b, a)
		}
	}
}