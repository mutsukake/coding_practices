package main

import "fmt"

func main() {
	var n, m int
	fmt.Scan(&n, &m)

	// Read matrix A
	A := make([][]int, n)
	for i := 0; i < n; i++ {
		A[i] = make([]int, m)
		for j := 0; j < m; j++ {
			fmt.Scan(&A[i][j])
		}
	}

	// Read vector b
	b := make([]int, m)
	for j := 0; j < m; j++ {
		fmt.Scan(&b[j])
	}

	// Compute c = A * b and output result
	for i := 0; i < n; i++ {
		c := 0
		for j := 0; j < m; j++ {
			c += A[i][j] * b[j]
		}
		fmt.Println(c)
	}
}
