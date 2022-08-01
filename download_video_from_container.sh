###
# this shell script downloads video file from the container
###

# get id of running container with image name "jperldev/dain"
container_id=$(docker ps | grep jperldev/dain | awk '{print $1}')
echo "container id: $container_id"
# upload a file video_low_fps.avi to path /usr/local/dain/ of container
docker cp $container_id:/usr/local/dain/video_low_fps-8x-192fps.mp4 ./
