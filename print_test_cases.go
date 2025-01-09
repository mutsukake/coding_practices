package main

import (
	"fmt"
)

func main() {
	z := 0
	for {
		z++
		var input int
		fmt.Scanln(&input) // Reads input from standard input
		if input == 0 {   // Stops the loop if input is zero
			break
		}
		fmt.Printf("Case %d: %d\n", z, input) // Prints in the required format
	}
}