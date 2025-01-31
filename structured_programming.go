package main

import (
	"fmt"
)

func call(n int) {
	i := 1

	for {
		x := i
		if x%3 == 0 {
			fmt.Printf(" %d", i)
		} else {
			include3 := false
			for x > 0 {
				if x%10 == 3 {
					include3 = true
					break
				}
				x /= 10
			}
			if include3 {
				fmt.Printf(" %d", i)
			}
		}

		i++
		if i > n {
			break
		}
	}
	fmt.Println()
}

func structured_programming() {
	var n int
	fmt.Scanln(&n)
	call(n)
}
