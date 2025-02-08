package main

import (
	"fmt"
)

func printChessboard() {
	for {
		var h, w int
		fmt.Scanln(&h, &w)
		if h == 0 && w == 0 {
			break
		}

		for i := 0; i < h; i++ {
			for j := 0; j < w; j++ {
				if (i+j)%2 == 0 {
					fmt.Print("#")
				} else {
					fmt.Print(".")
				}
			}
			fmt.Println()
		}
		fmt.Println()
	}
}
