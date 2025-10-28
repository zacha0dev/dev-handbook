[← Back to Home](../README.md)

# 9D - Monitoring and Logging

Once your app is deployed, you need to **track its health and behavior**.  
Monitoring and logging help find issues before users do.

---

### 1. Why It Matters
- Detect crashes or downtime early  
- Measure performance  
- Audit user activity and security

---

### 2. Logging in Python

```python
import logging

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("App started successfully")
logging.error("Something went wrong")
```

---

### 3. Structured Logs

Send JSON logs to cloud dashboards like Datadog, Grafana, or ELK stack.

```python
import json, logging
logging.info(json.dumps({"event": "user_login", "status": "success"}))
```

---

### 4. Monitoring Tools

| Tool | Purpose |
|------|----------|
| **Prometheus + Grafana** | Metrics dashboards |
| **Sentry** | Error tracking |
| **Datadog / New Relic** | App performance monitoring |

---

### 5. Key Takeaways
- Logs show what happened.  
- Monitoring shows how things are running.  
- Combine both for full visibility.
