package main

import "fmt"

func print_a_frame() {
	for {
		var h, w int
		fmt.Scanln(&h, &w)

		// Break when both H and W are zero
		if h == 0 && w == 0 {
			break
		}

		// Generate the frame
		for i := 0; i < h; i++ {
			for j := 0; j < w; j++ {
				// Print '#' for borders
				if i == 0 || i == h-1 || j == 0 || j == w-1 {
					fmt.Print("#")
				} else {
					fmt.Print(".")
				}
			}
			fmt.Println()
		}
		fmt.Println() // Print a blank line after each dataset
	}
}
