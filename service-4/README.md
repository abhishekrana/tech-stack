# Service-4

## Run orders

```bash
# Start redis (dependency)
task run-redis

# Start orders service
task run-orders
```

## Test orders

```bash
# POST
curl -v -X POST 127.0.0.1:3000/orders -H "Content-Type: application/json" -d  '{"customer_id": "aa975279-bccb-4f0e-be89-47d6108d4ab5"}'
{"id":"ae94ed28-fc77-419f-a3f2-5fecc21506cb","customer_id":"aa975279-bccb-4f0e-be89-47d6108d4ab5","created_at":"2023-10-29T19:14:32.706553257Z"}

# GET
curl 127.0.0.1:3000/orders/ae94ed28-fc77-419f-a3f2-5fecc21506cb
{"id":"ae94ed28-fc77-419f-a3f2-5fecc21506cb","customer_id":"aa975279-bccb-4f0e-be89-47d6108d4ab5","created_at":"2023-10-29T19:14:32.706553257Z"}
```
