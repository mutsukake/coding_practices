package main

import (
	"fmt"
)

func bubbleSort(arr []int) int {
	n := len(arr)
	swapCount := 0
	for i := 0; i < n-1; i++ {
		for j := 0; j < n-i-1; j++ {
			if arr[j] > arr[j+1] {
				arr[j], arr[j+1] = arr[j+1], arr[j]
				swapCount++
			}
		}
	}
	return swapCount
}

func main() {
	var n int
	fmt.Scan(&n)

	// Create and fill the array
	arr := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&arr[i])
	}

	// Sort the array and get swap count
	swapCount := bubbleSort(arr)

	// Print the sorted array
	for i, v := range arr {
		if i > 0 {
			fmt.Printf(" ")
		}
		fmt.Printf("%d", v)
	}
	fmt.Println()

	// Print the number of swaps
	fmt.Println(swapCount)
}
