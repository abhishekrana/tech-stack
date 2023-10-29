package orders

import (
	"context"
	"fmt"
	"net/http"

	"github.com/redis/go-redis/v9"

	"app-1/internal/configs"
)

type Orders struct {
	router http.Handler
	rdb    *redis.Client
}

func New() *Orders {
	redisConfig := configs.LoadRedisConfig()
	orders := &Orders{
		rdb: redis.NewClient(&redis.Options{
			Addr: redisConfig.Host + ":" + redisConfig.Port,
		}),
	}
	orders.loadRoutes()
	return orders
}

func (a *Orders) Start(ctx context.Context) error {
	server := &http.Server{
		Addr:    ":3000",
		Handler: a.router,
	}

	err := a.rdb.Ping(ctx).Err()
	if err != nil {
		return fmt.Errorf("failed to start server: %w", err)
	}

	err = server.ListenAndServe()
	if err != nil {
		return fmt.Errorf("failed to start server: %w", err)
	}

	return nil

}
