package main

import (
    "fmt"
)

func main() {
	// input
	var n int
	fmt.Scan(&n)
	var sum, max, min, x int
	for i := 0; i < n; i++ {
		fmt.Scan(&x)
		sum += x
		if i == 0 {
			max = x
			min = x
		} else {
			if x > max {
				max = x
			}
			if x < min {
				min = x
			}
		}
	}
	fmt.Println(min, max, sum)
}