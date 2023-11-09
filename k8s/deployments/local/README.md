# Local deployment

1. Update charts

```bash
cd k8s/charts/tech-stack/
task update-dependency
```

2. Deploy kubernetes cluster

```bash
cd k8s/deployments/local
task create-k3d
```

3. Deploy dependencies

```bash
cd k8s/deployments/local
task install-dependencies
```

4. Deploy application

```bash
cd k8s/deployments/local
tilt up
```
