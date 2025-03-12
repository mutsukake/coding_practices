package main

import (
	"fmt"
)

func main() {
	var r, c int
	fmt.Scan(&r, &c)

	// Read the table
	table := make([][]int, r)
	for i := 0; i < r; i++ {
		table[i] = make([]int, c)
		for j := 0; j < c; j++ {
			fmt.Scan(&table[i][j])
		}
	}

	// Prepare slices for column sums
	colSum := make([]int, c)
	totalSum := 0

	// Print table with row sums
	for i := 0; i < r; i++ {
		rowSum := 0
		for j := 0; j < c; j++ {
			val := table[i][j]
			rowSum += val
			colSum[j] += val
			// Print each element followed by a space (but you can handle spacing differently if you like)
			fmt.Printf("%d ", val)
		}
		totalSum += rowSum
		// Print the row sum at the end of each row
		fmt.Printf("%d\n", rowSum)
	}

	// Print column sums plus the total sum
	for j := 0; j < c; j++ {
		fmt.Printf("%d ", colSum[j])
	}
	fmt.Printf("%d\n", totalSum)
}
