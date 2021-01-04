# Docker Swarm Guide
Guide of docker swarm
# Initializing the swarm node
If you are using the Docker Desktop for Windows or for Mac, Docker swarm comes prebuilt. You can check that using $ docker swarm -v. To initialize the swarm mode, type $ docker swarm init.

# Creating services
Like we have created containers using docker run command, a service does the same thing for a swarm cluster.

$ docker service create <service name> allows us to create a service on swarm with a defined number of containers in it.

Our aim is to create a load-balanced Flask app service and attach a database to it.

"Swarm cluster only works with prebuilt images. This means we cannot build an image using a Dockerfile while creating a container. So, we have to build the image of our app first and then create a service from it."

So, create an image using $ docker build -t flask_app:3.0 . or $ docker pull venky8283/flask_app:3.0 to pull the image from Docker Hub.

Now, let’s create the first service, which is our Flask login app.

# Flask app
Type $ docker service create -p 5000:5000 flask_app:3.0. This will create a service with one container in it, which is also called a task.

# Database services
We already have a mysql-server image locally so, let’s create a service by using it. Type $ docker service create --name database --env-file <.env file location> --mount type=bind,src=<location of init.sql>,dst=/docker-entrypoint-initdb.d/init.sql mysql/mysql-server:5.7

# Networking
Both services are running now, but, you will get the same error as they are not connected. If you remember, we used the link argument to connect the database container. In swarm mode, the link option is not supported and we have to connect services using a network.

Services connected to the same network can talk to each other. So, to connect our database service to app service, we will create an “overlay network”. In swarm mode, we deal with distributed systems, hence, we use an overlay network to establish communication between services.

To create an overlay network, type $ docker network create --driver=overlay app. This will create a new network named ‘app’ on Docker host.

# Updating services
Now, we have our overlay network. Let’s attach it to both the services and let’s see if it solves the problem or not.

To update a service, type $ docker service update --network-add <network name> <service name/ID>.

