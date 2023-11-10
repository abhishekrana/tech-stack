# Local deployment

1. Update charts

```bash
cd k8s/charts/tech-stack/
task update-dependency
```

2. Deploy kubernetes cluster

```bash
cd k8s/deployments/local
task install-k3d
```

3. Deploy ingress nginx

```bash
cd k8s/deployments/local
task install-ingress-nginx
```

4. Deploy dependencies

```bash
cd k8s/deployments/local
task install-dependencies
```

5. Deploy application

```bash
cd k8s/deployments/local
tilt up
```

6. Access services

```bash
task get-ingress-nginx-ip
```
