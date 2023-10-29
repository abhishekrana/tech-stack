package handlers

import (
	"encoding/json"
	"errors"
	"fmt"
	"net/http"
	"time"

	"github.com/go-chi/chi/v5"
	"github.com/google/uuid"

	"app-1/internal/models"
	"app-1/internal/repos"
)

type Order struct {
	Repo *repos.RedisRepo
}

func (o *Order) Create(w http.ResponseWriter, r *http.Request) {
	fmt.Println("Creating order")
	var body struct {
		CustomerID uuid.UUID `json:"customer_id"`
	}

	if err := json.NewDecoder(r.Body).Decode(&body); err != nil {
		w.WriteHeader(http.StatusBadRequest)
		return
	}

	now := time.Now().UTC()

	order := models.Order{
		ID:         uuid.New(),
		CustomerID: body.CustomerID,
		CreatedAt:  &now,
	}

	err := o.Repo.Insert(r.Context(), order)
	if err != nil {
		fmt.Println("failed to insert:", err)
		w.WriteHeader(http.StatusInternalServerError)
		return
	}

	res, err := json.Marshal(order)
	if err != nil {
		fmt.Println("failed to marshal:", err)
		w.WriteHeader(http.StatusInternalServerError)
		return
	}

	w.WriteHeader(http.StatusCreated)
	w.Write(res)

	fmt.Println("Created order. id:", order.ID, ", customer_id:", order.CustomerID)
}

func (o *Order) GetByID(w http.ResponseWriter, r *http.Request) {
	fmt.Println("Get by order ID")
	idParam := chi.URLParam(r, "id")

	id, err := uuid.Parse(idParam)
	if err != nil {
		w.WriteHeader(http.StatusBadRequest)
		return
	}

	odr, err := o.Repo.FindByID(r.Context(), id)
	if errors.Is(err, repos.ErrNotExist) {
		w.WriteHeader(http.StatusNotFound)
		return
	} else if err != nil {
		fmt.Println("failed to find by id:", err)
		w.WriteHeader(http.StatusInternalServerError)
		return
	}

	if err := json.NewEncoder(w).Encode(odr); err != nil {
		fmt.Println("failed to marshal:", err)
		w.WriteHeader(http.StatusInternalServerError)
		return
	}
	fmt.Println("Got by order ID", idParam)
}
