package configs

import (
	"log"

	"github.com/caarlos0/env"
)

type RedisConfig struct {
	Host string `env:"REDIS_SVC_ADDRESS" envDefault:"127.0.0.1"`
	Port string `env:"REDIS_SVC_PORT" envDefault:"6379"`
}

func LoadRedisConfig() RedisConfig {
	config := RedisConfig{}
	err := env.Parse(&config)
	if err != nil {
		log.Fatal("invalid redis config: ", config.Host, config.Port)
	}
	log.Printf("redis config - host:%v, port:%v", config.Host, config.Port)
	return config
}
