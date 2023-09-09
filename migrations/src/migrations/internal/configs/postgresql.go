package configs

import (
	"log"

	"github.com/caarlos0/env"
)

type PostgresqlConfig struct {
	Host     string `env:"POSTGRESQL_SVC_HOST" envDefault:"127.0.0.1"`
	Port     string `env:"POSTGRESQL_SVC_PORT" envDefault:"5432"`
	Database string `env:"POSTGRESQL_SVC_DATABASE" envDefault:"tech_stack_db"`
	User     string `env:"POSTGRESQL_SVC_USER" envDefault:"admin"`
	Password string `env:"POSTGRESQL_SVC_PASSWORD" envDefault:"adminAdmin123!"`
}

func LoadPostgresqlConfig() PostgresqlConfig {
	config := PostgresqlConfig{}
	err := env.Parse(&config)
	if err != nil {
		log.Fatal("invalid postgresql config: ", config.Host, config.Port, config.Database, config.User)
		// panic(err)
		// panic("invalid postgresql config")
	}
	log.Println("postgresql config: ", config.Host, config.Port, config.Database, config.User)
	return config
}
