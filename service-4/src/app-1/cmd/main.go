package main

import (
	"context"
	"fmt"

	"app-1/internal/orders"
)

func main() {
	ordersService := orders.New()
	err := ordersService.Start(context.TODO())
	if err != nil {
		fmt.Println("failed to start app.", err)
		panic("failed to start app")
	}
}
