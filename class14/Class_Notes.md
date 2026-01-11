### Q) Why Docker?
- Same Application Code
- Same Packages with their PARTICULAR 
  VERSION
- Same Platform agnostic


### Difference of version introducing errors is called Breaking Changes
- Docker Image
 - It is a blueprint or a compressed version of our application.
 - Image is the same as Class in OOP.
 - It contains all the stuff like, 	Application code, libraries with 	their version

- Docker Container
- It is the same as an object in OOP.
- When up and running my application in a Docker container.


Q)What is Dockerfile
- The thing that is used to create an image is called a Dockerfile.
- It should be at the root level of your application code
- Dockerhub is just like a Play Store for Docker

### Dockerfile Keywords/functions

- FROM
- COPY
- RUN
- EXPOSE
- CMD

### Demonstration of Dockerfile functions with example
- Example: FROM(1,28)

- COPY /requirements.txt .
1- First arg:/requirements.txt
2- Second arg: .

### Raw Example through python functions

#### Example 1:

def user(name, email):
  return ....

user("ali", "ali@gmail.com")

#### Example 2:
COPY /requirements.txt . 

def COPY(apnaLaptop, dockerContainer):
  return ...

COPY("/requirements.txt" , ".")
