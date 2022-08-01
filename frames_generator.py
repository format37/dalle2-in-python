from PIL import Image
from image_converter import convert
from dalee_generator import generate_frames
import os
import numpy as np
import json


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


def main():
    # Parameters
    with open('frames_generator.json', 'r') as f:
        config = json.load(f)    

    # read lines from text file: config['text_path']
    with open(config['text_path'], 'r') as f:
        full_text = f.read()
    splitted_text = full_text.split('\n')
    # reverse lines in splitted_text
    splitted_text.reverse()

    frame_number = int(config['frame_number'])
    frame_sub = int(config['frame_sub'])

    for i in range(int(config['generations_count_limit'])):
        current_frame = frame_name_format(frame_number, frame_sub)
        # Prepare the prompt image
        image = Image.open(config['frames_path'] + current_frame)        

        # update frame number
        if frame_sub == int(config['frame_sub_limit'])-1:
            frame_number += 1
            frame_sub = 0
        else:
            frame_sub += 1

        current_frame = frame_name_format(frame_number, frame_sub)

        image = convert(image, float(config['size_step']), float(config['angle_step']))
        image.save(config['prompt_path'] + current_frame)
        
        prompt_text = splitted_text[frame_number] + config['prompt_appendix']
        print('# Prompt:', prompt_text)

        if frame_number>len(splitted_text):
            print('# End of text file')
            break

        if int(config['generate_prompt_and_exit']):
            print('# Prompt image generated')
            print(config['prompt_path'] + current_frame)
            exit()

        # Generate dalee2 frames
        print('Generating dalee2 frames...')
        file_paths = generate_frames(
            prompt_text,
            config['prompt_path'] + current_frame
            )
        print(file_paths)

        # copy one of files to the image_sequence folder
        selected_file = frame_selector(file_paths)        
        
        current_frame = frame_name_format(frame_number, frame_sub)
        os.system('cp ' + selected_file + ' ' + config['frames_path'] + current_frame)

        # make directory current_frame if it doesn't exist
        if not os.path.exists(config['generations_path'] + current_frame):
            os.mkdir(config['generations_path'] + current_frame)

        # move these files to the generations_path
        for file_path in file_paths:
            dst = config['generations_path'] + current_frame + '/' + file_path.split('/')[-1]
            print(
                'moving:',
                file_path,
                'to:',
                dst
                )
            os.rename(file_path, dst)
        
        print('frame_number:', frame_number)
        print('frame_sub:', frame_sub)    


if __name__ == '__main__':
    main()
