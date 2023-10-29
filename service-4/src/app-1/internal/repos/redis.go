package repos

import (
	"context"
	"encoding/json"
	"errors"
	"fmt"

	"github.com/google/uuid"
	"github.com/redis/go-redis/v9"

	"app-1/internal/models"
)

var ErrNotExist = errors.New("order does not exist")

type RedisRepo struct {
	Client *redis.Client
}

func (r *RedisRepo) Connect(ctx context.Context) error {
	err := r.Client.Ping(ctx).Err()
	if err != nil {
		return fmt.Errorf("failed to connect to redis: %w", err)
	}
	return nil
}

func orderIDKey(id uuid.UUID) string {
	return fmt.Sprintf("order:%v", id)
}

func (r *RedisRepo) Insert(ctx context.Context, order models.Order) error {
	data, err := json.Marshal(order)
	if err != nil {
		return fmt.Errorf("failed to encode order: %w", err)

	}
	key := orderIDKey(order.ID)

	res := r.Client.SetNX(ctx, key, string(data), 0)
	if err := res.Err(); err != nil {
		return fmt.Errorf("failed to encode order: %w", err)

	}
	return nil
}

func (r *RedisRepo) FindByID(ctx context.Context, id uuid.UUID) (models.Order, error) {
	key := orderIDKey(id)

	value, err := r.Client.Get(ctx, key).Result()
	if errors.Is(err, redis.Nil) {
		return models.Order{}, ErrNotExist
	} else if err != nil {
		return models.Order{}, fmt.Errorf("get order: %w", err)
	}

	var order models.Order
	err = json.Unmarshal([]byte(value), &order)
	if err != nil {
		return models.Order{}, fmt.Errorf("failed to decode order json: %w", err)
	}

	return order, nil
}
