# tech-stack

```
./bootstrap.sh

./setup.sh

# Port forward postgresql and run all SQL in `migrations` directory.

cd k8s/deployments/local
tilt up
```

## Roadmap

- [x] [Devcontainers](https://code.visualstudio.com/docs/devcontainers/containers)
  - [x] WSL2 (Windows)
  - [ ] Linux
- [x] Python
  - [x] [FastAPI](https://fastapi.tiangolo.com)
  - [x] [Pydantic V2](https://docs.pydantic.dev/latest)
  - [x] [SQL Alchemy 2](https://docs.sqlalchemy.org/en/20)
- [x] [k3d](https://k3d.io)
- [x] [Helm](https://helm.sh)
- [x] [Tilt](https://tilt.dev)
- [x] Postgresql
- [x] MongoDB
- [ ] Redis
- [ ] Rabbitmq
- [ ] Github Actions
- [ ] Golang
- [x] Vue3
  - [x] Typescript
  - [x] Pinia (State Management)

## Deployment

![K3D deployment](assets/k3d_deployment.jpg 'K3D Deployment')

## Service-1

**Backend**

- /v1/users/ - PostgreSQL
- /v1/products/ - MongoDB

![Service-1: Swagger](assets/service-1_swagger.png 'Service-1: Swagger')

## Service-2

**Frontend**

![Service-2: Products](assets/service-2_products.jpg 'Service-2: Products')
