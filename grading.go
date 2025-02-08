package main

import "fmt"

func main() {
	var m, f, r int
	for {
		fmt.Scan(&m, &f, &r)
		if m == -1 && f == -1 && r == -1 {
			break
		}
		if m == -1 || f == -1 {
			fmt.Println("F")
		} else if m+f >= 80 {
			fmt.Println("A")
		} else if m+f >= 65 {
			fmt.Println("B")
		} else if m+f >= 50 {
			fmt.Println("C")
		} else if m+f >= 30 {
			if r >= 50 {
				fmt.Println("C")
			} else {
				fmt.Println("D")
			}
		} else {
			fmt.Println("F")
		}
	}
}
