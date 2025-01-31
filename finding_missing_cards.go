package main

import (
	"fmt"
)

func main() {
	var n int
	fmt.Scan(&n) // Number of cards that Taro has

	// Keep track of which cards we've seen
	seen := make(map[string]bool)

	// Read each card, e.g. "S 2" or "H 10"
	for i := 0; i < n; i++ {
		var suit string
		var rank int
		fmt.Scan(&suit, &rank)
		card := fmt.Sprintf("%s %d", suit, rank)
		seen[card] = true
	}

	// The order of suits we want
	suits := []string{"S", "H", "C", "D"}

	// Print any cards not seen in input, in the correct order
	for _, s := range suits {
		for r := 1; r <= 13; r++ {
			card := fmt.Sprintf("%s %d", s, r)
			if !seen[card] {
				fmt.Println(card)
			}
		}
	}
}
