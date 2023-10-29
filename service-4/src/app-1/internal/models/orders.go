package models

import (
	"time"

	"github.com/google/uuid"
)

type Order struct {
	ID         uuid.UUID  `json:"id"`
	CustomerID uuid.UUID  `json:"customer_id"`
	CreatedAt  *time.Time `json:"created_at"`
}
