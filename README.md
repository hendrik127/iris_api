# Iris API

## Development
```
docker-compose up -d
```

## Testing
When running in development mode 
```
docker exec -it iris-api-1 bash 
pytest -v
```


## Production

```
docker-compose -f docker-compose.prod.yaml up -d
```

