# AIQ_challange
# Prerequsites:  Need to have docker and Mongodb in the system

# How to the RUN code in docker:
First UNCOMMENT the ENVIROMENT=dockertest and DB_URI/DB_NAME fields for docketest in .env file, then run the following
- Build Docker image
  - docker build -t aiq-api .
- Run Docker image
  - Detached
    - docker run -d -p 5000:5050 aiq-api
  - Interactive
    - docker run -i -p 5000:5050 aiq-api
- To access the api, use this url http://localhost:5000/

# How to make API calls:
The API endpoints can be invoked from the associated swagger doc (OpenAPI) using localhost/api/docs.
Click Tryit Out button on each route and give the required input and execute it

The algorithm used to get the circles and their bounds boxes uses multiple filtering techquines to detect edges and then countours.
First a bluring is applied on the images to remove the extra sharpness in the middle portion of the circles while keeping the edges intact.
Then Soble and Canny filters are applied on the images to highlight the edges.
Then countour and bounding box details are fetched from the images of the circles.
