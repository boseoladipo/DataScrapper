# Data Scrapper

## Solution

A python application for getting image urls for the most visited websites worldwide

## Installation

Download and install Docker for your os if you do not have it setup from https://docs.docker.com/install/

## Usage
Ensure that docker is running and run the following commands to setup and run the application:
```bash
git clone https://github.com/StudentFinance/GetLinks.git
cd GetLinks
```

## Tests
To run tests run the following command
```bash
docker build --target test --tag my-python-app .
```
## Run application
To run the application, run the following commands
```bash
docker build --tag my-python-app .
docker run -it --rm  --name python-app -v $(pwd):/my_app my-python-app
```

## Result
Links to website will be found in /data/results.txt. 
Websites for which url retrieval failed will be found in /data/failed_urls.txt