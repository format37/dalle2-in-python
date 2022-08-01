###
# this shell script uploads video file to container
###

# get id of running container with image name "jperldev/dain"
container_id=$(docker ps | grep jperldev/dain | awk '{print $1}')
echo "container id: $container_id"
# upload a file video_low_fps.avi to path /usr/local/dain/ of container
docker cp video_low_fps.avi $container_id:/usr/local/dain/
