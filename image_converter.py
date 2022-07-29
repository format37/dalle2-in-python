from PIL import Image


def remove_color_rectangle(image, width, height):
    rectangle_size = (80,16)
    image = image.convert('RGBA')
    image_box = Image.new('RGBA', rectangle_size, (255, 255, 255, 0))
    image.paste(image_box, (width - rectangle_size[0],height - rectangle_size[1]))
    return image


def downsize(image, N):
    width, height = image.size
    new_width = int(width * (1-N))
    new_height = int(height * (1-N))
    return image.resize((new_width, new_height))


def rotate_image(img, angle):
    img = img.convert('RGBA')
    img_rot = img.rotate(angle, expand=1, resample=Image.BICUBIC)
    fff = Image.new('RGBA', img_rot.size, (255, 255, 255, 0))
    out = Image.composite(img_rot, fff, img_rot)
    return out


def upscale(image, width, height):
    image_upscaled = Image.new("RGBA", (width, height), (255, 255, 255, 0))
    image_upscaled.paste(image, (int((width - image.size[0]) / 2), int((height - image.size[1]) / 2)))
    return image_upscaled


def convert(image, size_step, angle_step):
    # read image from file
    # image = Image.open('image_sequence/image_0000_0.png')
    original_size = image.size

    # put a transparent rectangle in the right bottom corner of the image
    image = remove_color_rectangle(image, original_size[0], original_size[1])

    # downsize the image to N % of its original size
    # size_step = 0.5/3  # 3 times to 0.5% of original size
    image = downsize(image, size_step)

    # rotate image with transparent background
    # angle_step = -10
    image = rotate_image(image, angle_step)

    # Upscale canvas size to fixed values,
    # with creating transparent background.
    # Original image is centered in the canvas.
    image = upscale(image, original_size[0], original_size[1])

    # save the image
    # image.save('out.png')
    return image
