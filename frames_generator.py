from PIL import Image
from image_converter import convert
from dalee_generator import generate_frames
import os
import numpy as np

def frame_name_format(frame_number, frame_sub):
    # convert frame number to string with leading zeros
    # number is 4-digit number
    frame_number_str = '{:04d}'.format(frame_number)
    # convert frame_sub number to string with leading zeros
    # frame_sub is 2-digit number
    frame_sub_str = '{:02d}'.format(frame_sub)
    return 'image_'+frame_number_str+'_'+frame_sub_str+'.png'


def frame_selector(file_names):
    # given a list of 3 pathes
    # return rantom path
    return np.random.choice(file_names)

# Parameters
size_step = 0.2
angle_step = 1
prompt_appendix = ' Digital art'
prompt_path = 'prompt_images/'
generations_path = 'generations/'
frames_path = 'image_sequence/'

frame_sub_limit = 10  # count of frames in each generation
frame_number = 1
frame_sub = 1

for i in range(6):
    #prompt_text = 'My favorite bird She has known this for a long time ...'
    prompt_text = 'My sorrows, doubts And a pile of fears burns.'
    current_frame = frame_name_format(frame_number, frame_sub)

    # Prepare the prompt image
    image = Image.open(frames_path + current_frame)
    image = convert(image, size_step, angle_step)
    image.save(prompt_path + current_frame)

    # Generate dalee2 frames
    print('Generating dalee2 frames...')
    file_paths = generate_frames(
        prompt_text + prompt_appendix,
        prompt_path + current_frame
        )
    print(file_paths)

    # copy one of files to the image_sequence folder
    selected_file = frame_selector(file_paths)
    # update frame number
    if frame_sub == frame_sub_limit-1:
        frame_number += 1
        frame_sub = 0
    else:
        frame_sub += 1
    
    current_frame = frame_name_format(frame_number, frame_sub)
    os.system('cp ' + selected_file + ' ' + frames_path + current_frame)

    # make directory current_frame if it doesn't exist
    if not os.path.exists(generations_path + current_frame):
        os.mkdir(generations_path + current_frame)

    # move these files to the generations_path
    for file_path in file_paths:
        dst = generations_path + current_frame + '/' + file_path.split('/')[-1]
        print(
            'moving:',
            file_path,
            'to:',
            dst
            )
        os.rename(file_path, dst)
    
    print('frame_number:', frame_number)
    print('frame_sub:', frame_sub)    
