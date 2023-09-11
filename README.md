# tech-stack

## Services

| Service    | Stack                |
| ---------- | -------------------- |
| migrations | GoLang               |
| service-1  | FastAPI + PostgreSQL |
| service-2  | FastAPI + MongoDB    |
| service-3  | Vue.js               |

## Setup

```
# Bootstrap
./bootstrap.sh

# Install dependencies and setup k8s cluster
./setup.sh

# Deploy
cd k8s/deployments/local
tilt up
```

## Roadmap

- [x] [Devcontainers](https://code.visualstudio.com/docs/devcontainers/containers)
  - [x] [WSL2 Windows](https://code.visualstudio.com/blogs/2020/07/01/containers-wsl)
  - [ ] [Linux](https://code.visualstudio.com/docs/devcontainers/create-dev-container)
- [x] Python
  - [x] [FastAPI](https://fastapi.tiangolo.com)
  - [x] [Pydantic V2](https://docs.pydantic.dev/latest)
  - [x] [SQL Alchemy 2](https://docs.sqlalchemy.org/en/20)
- [x] [k3d](https://k3d.io)
- [x] [Helm](https://helm.sh)
- [x] [Tilt](https://tilt.dev)
- [x] [Postgresql](https://www.postgresql.org/)
- [x] [MongoDB](https://www.mongodb.com/)
- [ ] [Redis](https://redis.io/)
- [ ] [Rabbitmq](https://www.rabbitmq.com/)
- [ ] [Github Actions](https://github.com/features/actions)
- [x] [Golang](https://go.dev/)
- [x] [Vue3](https://vuejs.org/)
  - [x] [Typescript](https://vuejs.org/guide/typescript/overview.html)
  - [x] [Pinia (State Management)](https://pinia.vuejs.org/)

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
