import cv2
import json

###
# 1. Read video file
# 2. Split video by frames
# 3. Save frames to images
###


def main():
    # Parameters
    with open('video2images.json', 'r') as f:
        config = json.load(f)
    images_path = config['images_path']
    video_file_name = config['video_file_name']
    # read video file
    video = cv2.VideoCapture(video_file_name)    
    # get count of frames
    count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    print(count)
    # read images from video    
    i = 0
    while True:
        ret, frame = video.read()
        if not ret:
            break
        # define a file name from i with 10 lead zeros
        file_name = '{:010d}.jpg'.format(i)

        cv2.imwrite(images_path + file_name, frame)
        i += 1 
    print('Job done!')


if __name__ == '__main__':
    main()
