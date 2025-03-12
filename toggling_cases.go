package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func main() {
	// Read entire line
	reader := bufio.NewReader(os.Stdin)
	input, _ := reader.ReadString('\n')
	input = strings.TrimSpace(input)

	var result []rune
	for _, char := range input {
		switch {
		case char >= 'a' && char <= 'z':
			// Convert to uppercase
			result = append(result, char-'a'+'A')
		case char >= 'A' && char <= 'Z':
			// Convert to lowercase
			result = append(result, char-'A'+'a')
		default:
			// Non-alphabetic characters remain the same
			result = append(result, char)
		}
	}

	fmt.Println(string(result))
}
