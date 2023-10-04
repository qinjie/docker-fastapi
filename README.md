# docker-fastapi

Run FastAPI app in a docker container.

```
docker compose up -d --force-recreate
docker compose down
```

If database is running in another container, use `host.docker.internal` as the MYSQL_HOST instead of `127.0.0.1`.

### Sample Database

```
CREATE TABLE IF NOT EXISTS product(
	id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(1024),
    price BIGINT DEFAULT 0,
    is_available BOOLEAN DEFAULT FALSE,
    seller_email VARCHAR(512),
    deleted BOOLEAN DEFAULT FALSE,
    created_by INT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_by INT NULL,
    updated_at TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) ENGINE = INNODB;
```
