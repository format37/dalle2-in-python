import cv2
import os
import sys


def main():
    # path = './image_sequence/'
    # read path from first parameter
    path = sys.argv[1]
    # if path is not exist, warn and exit
    if not os.path.exists(path):
        print('Path does not exist!')
        exit()
    # read all files in path
    filenames = []
    for fname in os.listdir(path):
        filenames.append(os.path.join(path, fname))
    # sort filenames by name descending
    # filenames = sorted(filenames, key=lambda x: x.split('/')[-1], reverse=True)
    # sort filenames by name ascending
    filenames = sorted(filenames)
    # append reversed filenames to list
    #for f in sorted(filenames, key=lambda x: x.split('/')[-1], reverse=True):
    #    filenames.append(f)
    # read images
    images = []
    for fname in filenames:
        #images.append(cv2.imread(fname))
        # read image
        img = cv2.imread(fname)
        # downgrade image size to 900x900
        img = cv2.resize(img, (900, 900))
        # add image to list
        images.append(img)
    # read framerate from cmd params
    fps = int(input('Enter framerate: '))
    # create a video
    height, width, layers = images[0].shape
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    video = cv2.VideoWriter('./video.avi', fourcc, fps, (width, height))
    for image in images:
        video.write(image)
    cv2.destroyAllWindows()
    video.release()
    """# create a gif animation
    gif_name = 'animation.gif'
    frame = images[0]
    height, width, layers = frame.shape
    video = cv2.VideoWriter(gif_name, 0, frameRate, (width, height))
    for image in images:
        video.write(image)
    cv2.destroyAllWindows()
    video.release()"""


if __name__ == '__main__':
    main()
