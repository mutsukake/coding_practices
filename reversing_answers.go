package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Scanln(&n)
	a := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&a[i])
	}

	for i := n - 1; i >= 0; i-- {
		if i == 0 {
			fmt.Printf("%d", a[i]) // No space after the last number
		} else {
			fmt.Printf("%d ", a[i])
		}
	}
	fmt.Println() // Add a newline at the end
}
