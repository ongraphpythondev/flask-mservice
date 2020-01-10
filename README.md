# Flask Microservices on Kubernetes(k8s)

This is a POC to check if microservices can be made using flask with proper API documentation and openAPI 2.0 support and can be deployed on a kubernetes cluster on local machines using minikube and kubectl .

## Installation and running flask server

1. Make a python3.x virtual environment using [virtualenvwrapper](https://virtualenvwrapper.readthedocs.io/en/latest/)
2. ``` pip install -r requirements.txt ```
3. ``` export FLASK_APP=main.py ```
4. ``` flask run ```

## Building a docker image using Dockerfile and running the container

1. Build docker image:```docker build -f Dockerfile --rm -t flask_micro_docker:latest .```
2. Running in interactive mode: ```docker run docker run -it -p 8000:5000 flask_micro_docker:latest```
 

## Setting up minikube and kubectl:
  
1. To setup minikube follow official [minikube installation guide](https://kubernetes.io/docs/tasks/tools/install-minikube/).
2. To setup kubectl follow [kubectl installation guide](https://kubernetes.io/docs/tasks/tools/install-kubectl/).


## Making a service and deployment over kubernetes
1. ```kubectl apply -f kubertoy.yaml```
2. Get the url of your service by using ```minikube service flaskr-service --url ```
3. Access swagger ui at http://{base-url}/ui/ in your browser.
4. To see the services running and health check use command ```minikube dashboard``` 

## Automated tests for each micro-service:
**needs to be added [WIP].
