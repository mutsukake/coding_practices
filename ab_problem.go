package main
import "fmt"


func main() {
	var a, b int
	var d, r int
	var f float64

	fmt.Scanln(&a, &b)
	d = a / b
	fmt.Println(d)

	r = a % b	
	fmt.Println(r)

	// f is float64 type
	f = float64(a) / float64(b)
	fmt.Println(f)

}