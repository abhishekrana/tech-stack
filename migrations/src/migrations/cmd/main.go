package main

import (
	"database/sql"
	"fmt"

	"github.com/golang-migrate/migrate/v4"
	"github.com/golang-migrate/migrate/v4/database/postgres"
	_ "github.com/golang-migrate/migrate/v4/source/file"
	_ "github.com/lib/pq"

	"migrations/internal/configs"
)

func main() {
	configs.LoadPostgresqlConfig()
	postgresqlConfig := configs.LoadPostgresqlConfig()
	fmt.Println(postgresqlConfig)

	// Connect to the database
	url := fmt.Sprintf("host=%s port=%s user=%s password=%s dbname=%s sslmode=disable search_path=public",
		postgresqlConfig.Host, postgresqlConfig.Port, postgresqlConfig.User, postgresqlConfig.Password, postgresqlConfig.Database)
	fmt.Println(url)
	db, err := sql.Open("postgres", url)
	if err != nil {
		panic(err)
	}
	defer db.Close()

	// Ping database
	if err = db.Ping(); err != nil {
		panic(err)
	}

	// Run migrations
	driver, err := postgres.WithInstance(db, &postgres.Config{})
	if err != nil {
		panic(err)
	}
	m, err := migrate.NewWithDatabaseInstance(
		"file:///workspace/migrations/files",
		"postgres", driver)
	if err != nil {
		panic(err)
	}
	m.Up()
	// m.Step(2) // to explicitly set the number of migrations to run
	// if err := m.Up(); err != nil {
	// 	panic(err)
	// }

	fmt.Println("migration completed successfully")
}
