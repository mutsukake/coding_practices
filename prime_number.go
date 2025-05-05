package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Scan(&n)
	count := 0

	for i := 0; i < n; i++ {
		var num int
		fmt.Scan(&num)
		if isPrime(num) {
			count++
		}
	}
	fmt.Println(count)
}

func isPrime(n int) bool {
	if n < 2 {
		return false
	}
	for i := 2; i*i <= n; i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}
