package main

import (
	"fmt"
	"math"
)

func main() {
	var n int

	if _, err := fmt.Scan(&n); err != nil {
		fmt.Println("Error reading input:", err)
		return
	}

	prices := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&prices[i])
	}

	// Initialize variables
	minPrice := prices[0]
	maxProfit := math.MinInt64

	// Start from the second price to ensure buy before sell
	for i := 1; i < n; i++ {
		// Calculate profit if we sell at current price
		profit := prices[i] - minPrice
		if profit > maxProfit {
			maxProfit = profit
		}

		// Update minimum price seen so far
		if prices[i] < minPrice {
			minPrice = prices[i]
		}
	}

	// If no profit is possible, output -1
	fmt.Println(maxProfit)
}
