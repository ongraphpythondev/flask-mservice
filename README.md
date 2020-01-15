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

1. Using [pytest](https://docs.pytest.org/en/latest/contents.html) to run automated tests.
2. To run the tests cd into the project root and run ```pytest -v```
3. to run specific test method use ```pytest tests/test_hello.py::test_hello -v```
4. More pytest usage [reference](https://docs.pytest.org/en/latest/usage.html).

# Notes

## Installing VirtualBox on MacOS

If you want to run minikube on a Mac, you need to install a virtual machine. The most common VM is VirtualBox. Some recent versions of MacOS don’t allow VirtualBox to be installed (the OS doesn’t recognize Oracle’s Developer ID). Here’s a solution for that (not simple): 

Based on these instructions: [installation fails for vbox 6.0.8 on osx 10.14.5](https://forums.virtualbox.org/viewtopic.php?f=8&t=93151)

* In Terminal, run:
  * `sudo spctl --master-disable`
  * `sudo kextcache --clear-staging`
* Restart the Mac in **Recovery Mode**
  * _Restart, hold down Command-R until the Mac starts up_
* In **Recovery Mode**, go to the **Utilities** menu and launch the **Terminal**
* Enter the command: `spctl kext-consent add VB5E2TV963`
* Restart the Mac
* Mount the VirtualBox drive image (the .dmg file)
* Run the Uninstall script, to clean up the environment
* Run the VirtualBox installer
* Restore security in Security & Privacy by entering this in a terminal: 
  * `sudo spctl --master-enable`

Note: this was necessary on one developer's machine, running Mac OS 10.14.6 (Mojave)
