from dalle2 import Dalle2

def generate_frames(prompt_text, file_path):
    with open('token.txt','r') as f:
        token = f.read().replace('\n','')
    dalle = Dalle2(token)
    # ask DALL·E to fill-in the transparent right half
    download_finished = False    
    for d in range(4):        
        generation_finished = False
        for i in range(9):
            try:
                generations = dalle.generate_from_masked_image(prompt_text, file_path)
                generation_finished = True
                break
            except Exception as e:
                print('===', str(i)+'th generation try failed:', e)
                continue
        if not generation_finished:
            print('=== Failed to generate dalee2 frames')
            exit()

        try:
            file_paths = dalle.download(generations)
            download_finished = True
            break
        except Exception as e:
            print('===', str(d)+'th download try failed:', e)
            continue

    if not download_finished:
        print('=== Failed to download dalee2 frames')
        exit()

    return file_paths