# ANGRY_test

# Как запустить проект

1. Создаем образ:

   ```bash
   docker build -t angry_test .
   ```
2. Запуск контейнера:
   ```bash
   docker run -d -p 8080:8080 angry_test
   ```

## Примеры запросов к API

1. healthcheck:

   ```bash
   GET /healthcheck
   ```

2. hash:

    ```bash
    GET /hash
    {
      "string": "test"
    }
    ```

Теперь ваш проект должен быть доступен по адресу http://localhost:8080/.