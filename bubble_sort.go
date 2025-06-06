package main

import (
	"fmt"
)

func insertionSort(arr []int) int {
	n := len(arr)
	shiftCount := 0
	for i := 1; i < n; i++ {
		key := arr[i]
		j := i - 1
		for j >= 0 && arr[j] > key {
			arr[j+1] = arr[j]
			shiftCount++
			j--
		}
		arr[j+1] = key
	}
	return shiftCount
}

func shellSort(arr []int) (int, []int) {
	n := len(arr)
	cnt := 0
	var G []int
	// Generate Shell's increment sequence (1, 4, 13, ...)
	for h := 1; h <= n; {
		G = append([]int{h}, G...)
		h = 3*h + 1
	}
	// Shell sort using insertion sort for each gap
	for _, g := range G {
		for i := g; i < n; i++ {
			v := arr[i]
			j := i - g
			for ; j >= 0 && arr[j] > v; j -= g {
				arr[j+g] = arr[j]
				cnt++
			}
			arr[j+g] = v
		}
	}
	return cnt, G
}

func main() {
	var n int
	fmt.Scan(&n)
	arr := make([]int, n)
	for i := 0; i < n; i++ {
		fmt.Scan(&arr[i])
	}

	// Uncomment one of the following blocks to use the desired sort:

	// --- Insertion Sort ---
	// shiftCount := insertionSort(arr)
	// for i, v := range arr {
	// 	if i > 0 {
	// 		fmt.Printf(" ")
	// 	}
	// 	fmt.Printf("%d", v)
	// }
	// fmt.Println()
	// fmt.Println(shiftCount)

	// --- Shell Sort ---
	shiftCount, G := shellSort(arr)
	fmt.Println(len(G))
	for i, g := range G {
		if i > 0 {
			fmt.Print(" ")
		}
		fmt.Print(g)
	}
	fmt.Println()
	fmt.Println(shiftCount)
	for i, v := range arr {
		if i > 0 {
			fmt.Print(" ")
		}
		fmt.Printf("%d", v)
	}
	fmt.Println()
}
