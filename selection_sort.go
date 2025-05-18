package main

import "fmt"

func main() {
	var n int
	fmt.Scan(&n)

	// Read the array
	arr := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&arr[i])
	}

	// Simplified selection sort
	swapCount := 0
	for i := 0; i < n-1; i++ {
		minIndex := i
		for j := i + 1; j < n; j++ {
			if arr[j] < arr[minIndex] {
				minIndex = j
			}
		}
		// Only swap if needed and count
		if minIndex != i {
			arr[i], arr[minIndex] = arr[minIndex], arr[i]
			swapCount++
		}
	}

	// Print results more concisely
	fmt.Println(fmt.Sprint(arr)[1 : len(fmt.Sprint(arr))-1])
	fmt.Println(swapCount)
}
