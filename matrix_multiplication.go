package main

import (
	"fmt"
)

func main() {
	var m, n, l int
	fmt.Scan(&m, &n, &l)

	// 行列Aの入力
	A := make([][]int, m)
	for i := 0; i < m; i++ {
		A[i] = make([]int, n)
		for j := 0; j < n; j++ {
			fmt.Scan(&A[i][j])
		}
	}

	// 行列Bの入力
	B := make([][]int, n)
	for i := 0; i < n; i++ {
		B[i] = make([]int, l)
		for j := 0; j < l; j++ {
			fmt.Scan(&B[i][j])
		}
	}

	// 行列の積 C = A x B
	C := make([][]int, m)
	for i := 0; i < m; i++ {
		C[i] = make([]int, l)
		for j := 0; j < l; j++ {
			sum := 0
			for k := 0; k < n; k++ {
				sum += A[i][k] * B[k][j]
			}
			C[i][j] = sum
		}
	}

	// 結果を出力 (各行の要素を横に並べる)
	for i := 0; i < m; i++ {
		for j := 0; j < l; j++ {
			// j > 0 なら前にスペースを入れて整形
			if j > 0 {
				fmt.Print(" ")
			}
			fmt.Print(C[i][j])
		}
		// 行の終わりで改行
		fmt.Println()
	}
}
