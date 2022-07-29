import cv2
import os

###
# 1. Read video file
# 2. Split video by frames
# 3. Save frames to images
###


def main():
    images_path = './extracted_from_video/'
    video_file_name = 'video-8x-192fps.mp4'
    # read video file
    video = cv2.VideoCapture(video_file_name)
    # get video framerate
    #fps = video.get(cv2.CAP_PROP_FPS)
    # get video size
    #width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
    #height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # get count of frames
    count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
    print(count)
    # read images from video
    #images = []
    i = 0
    while True:
        ret, frame = video.read()
        if not ret:
            break
        # add image to list
        #images.append(frame)
        # define a file name from i with 10 lead zeros
        file_name = '{:010d}.jpg'.format(i)

        cv2.imwrite(images_path + file_name, frame)
        # print(len(images))
        #if len(images) >= count:
        #    break
        i += 1 
    # save images to images folder
    #for i, image in enumerate(images):
    #    cv2.imwrite(images_path + str(i) + '.jpg', image)    
    print('Job done!')


if __name__ == '__main__':
    main()