package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Scan(&n)

	// We have 4 buildings, 3 floors, 10 rooms.
	// Using 1-indexing so we declare an array with extra space.
	// tenants[b][f][r] will hold the number of tenants in building b, floor f, room r.
	var tenants [5][4][11]int

	// Process each notice.
	for i := 0; i < n; i++ {
		var b, f, r, v int
		fmt.Scan(&b, &f, &r, &v)
		tenants[b][f][r] += v
	}

	// Print the results for each building.
	// Buildings are printed in order from 1 to 4.
	for b := 1; b <= 4; b++ {
		// Each building has 3 floors.
		for f := 1; f <= 3; f++ {
			// Each floor has 10 rooms.
			for r := 1; r <= 10; r++ {
				// Print a space before each number as specified.
				fmt.Printf(" %d", tenants[b][f][r])
			}
			fmt.Println()
		}
		// Between buildings, print the border line of 20 '#' characters.
		// Do not print this after the last building.
		if b < 4 {
			fmt.Println("####################")
		}
	}
}
