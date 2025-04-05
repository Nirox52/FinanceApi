# Finance App API

## Run
### Docker
docker compose up -d

### Server
- uv sync
- uv run uvicorn main:app --reload


## Documentation
### User

| Method   | Endpoint                    | Description                                                  |
|---------|-----------------------------|-----------------------------------------------------------|
| `POST`  | `/users/`                   | Creating new user. Geting `telegram_id`.    |
| `GET`   | `/users/{telegram_id}`      | Geting info about user by `telegram_id`.     |
| `DELETE`| `/users/{telegram_id}`      | Deleting user by `telegram_id`.                   |

### Operations

| Method   | Endpoint                      | Description                                                                 |
|---------|-------------------------------|--------------------------------------------------------------------------|
| `POST`  | `/operations/`                | Creating new operation. Geting  `telegram_id`, `type`, `amount`, `description`. |
| `GET`   | `/operations/tg/{telegram_id}`   | Geting all user's operations  |
| `GET`   | `/operations/id/{operation_id}`   | Geting operation by id                                 |
| `PUT`   | `/operations/{operation_id}`   | Changing operation by id                                  |
| `GET`   | `/operations/operations_date/{telegram_id}`   | Geting operations in date range                                  |
| `DELETE`| `/operations/{operation_id}`  | Deleting operation by `operation_id`.                                 |

