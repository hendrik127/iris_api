# Iris API
## Clone repo
```
git clone https://github.com/hendrik127/iris_api.git
```
## Development
To start development only one command is needed.
```
docker-compose up -d
```
App files are mounted to the container so reload is supported.
## Linting & Testing
When running in development mode.
```
docker exec -it iris-api-1 bash 
pylint .
pytest -v
```


## Production
An image is built and pushed to ghcr when there is a push to the main branch and files have changed in the **/app** folder. That image is used along with the default postgres image run the app.
```
docker-compose -f docker-compose.prod.yaml up -d
```

