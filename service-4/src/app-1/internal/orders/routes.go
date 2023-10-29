package orders

import (
	"net/http"

	"github.com/go-chi/chi/v5"
	"github.com/go-chi/chi/v5/middleware"

	"app-1/internal/handlers"
	"app-1/internal/repos"
)

func (a *Orders) loadRoutes() {
	router := chi.NewRouter()

	router.Use(middleware.Logger)

	router.Get("/", func(w http.ResponseWriter, r *http.Request) {
		w.WriteHeader(http.StatusOK)
	})
	router.Route("/orders", a.loadOrderRoutes)
	a.router = router
}

func (a *Orders) loadOrderRoutes(router chi.Router) {
	orderHandler := &handlers.Order{
		Repo: &repos.RedisRepo{
			Client: a.rdb,
		},
	}

	router.Post("/", orderHandler.Create)
	router.Get("/{id}", orderHandler.GetByID)
}
