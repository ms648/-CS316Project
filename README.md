# CS316Project

docker-compose build
  builds docker images
  have to be in same directory as the project
  shouldn't use too often... only if we add new python library or something
  
docker images

docker-compose up
  this starts running things
  
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

localhost:3000 to get to it on web browser.

docker cp file to transfer containerID 

./manage.py startapp teacher_musicapp to make teacher_musicapp directory in github + the musicapp image. 

might need the sudo chown -R $USER:$USER . if the teacher_music user after ls -al returns root.

models: didn't catch this, is in comments

test: tests

views: controller, semi-handles routing (urls.py is urls for whole project)

to set up admin:

in container, do ./manage.py createsuperuser

if it says development.auth_user doesn't exist, do ./manage.py migrate

then do ./manage.py createsuperuser 

next:
./manage.py shell gives interactive shell (to test commands if needed)

can type localhost:3000/music to see users stuff
localhost:3000/admin to view admin page
