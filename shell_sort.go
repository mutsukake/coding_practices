package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func shellSort(a []int, n int) ([]int, int) {
	cnt := 0
	var G []int
	// Generate the increment sequence (using Shell's original sequence: 1, 4, 13, ...)
	for h := 1; h <= n; {
		G = append([]int{h}, G...)
		h = 3*h + 1
	}
	// Shell sort
	for _, g := range G {
		for i := g; i < n; i++ {
			v := a[i]
			j := i - g
			for ; j >= 0 && a[j] > v; j -= g {
				a[j+g] = a[j]
				cnt++
			}
			a[j+g] = v
		}
	}
	return G, cnt
}

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	scanner.Split(bufio.ScanWords)
	scanner.Scan()
	n, _ := strconv.Atoi(scanner.Text())
	a := make([]int, n)
	for i := 0; i < n; i++ {
		scanner.Scan()
		a[i], _ = strconv.Atoi(scanner.Text())
	}
	G, cnt := shellSort(a, n)
	fmt.Println(len(G))
	for i, g := range G {
		if i > 0 {
			fmt.Print(" ")
		}
		fmt.Print(g)
	}
	fmt.Println()
	fmt.Println(cnt)
	for i := 0; i < n; i++ {
		fmt.Println(a[i])
	}
}
