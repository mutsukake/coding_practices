package main

import (
	"fmt"
)

func main() {
	for {
		var h, w int
		fmt.Scan(&h, &w)
		if h == 0 && w == 0 {
			return
		}

		// Print the rectangle
		for i := 0; i < h; i++ {
			for j := 0; j < w; j++ {
				fmt.Print("#")
			}
			fmt.Println() // Line break after each row
		}
		fmt.Println() // Blank line after each rectangle
	}
}