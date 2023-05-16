import PIL.Image


def split_image():
    img = PIL.Image.open('img/all.png')
    for i in range(10):
        offset = 25 * i
        c = img.crop((5 + offset, 1, 20 + offset, 22))
        c.save(f'img/img_{i}.png')


if __name__ == '__main__':
    split_image()
