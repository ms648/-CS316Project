# CS316Project

docker-compose build
  builds docker images
  have to be in same directory as the project
  shouldn't use too often... only if we add new python library or something
  
docker images

docker-compose up
  this starts running shit?
  
docker ps -a
  shows you ports that things are running on
  also gives the container ID
  
docker exec -it *container ID* bash 
  this gets you inside of a docker container -- get the DB container
  
  mysql -u root -p
    password = example
    
docker-compose down 
  opposite of up - brings everything down

sudo chown -R $USER:$USER .
  If a file gets created in the container vs on your host machine root will own it. This will just fix it so you own it and can edit.
