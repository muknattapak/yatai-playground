# Yatai Playground

## Dependencies
- docker (docker-engine or docker-desktop)
- docker-compose

## Usage
1. Launch yatai deployment service
  `docker-compose up -d`
1. Bundle iris-classifier
  `docker-compose run iris-classifier-bundle`
1. Yatai web console 
  http://localhost:3000/