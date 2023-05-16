import pyautogui


def calc_dict():
    color_dict = {}
    for i in range(10):
        tiles = pyautogui.locateAllOnScreen(f'img/img_{i}.png')
        if tiles:
            color_dict[i] = [t for t in tiles]
    return color_dict


def calc():
    color_dict = calc_dict()
    if color_dict is None:
        return
    for k, v in color_dict.items():
        print(f'{k} : {len(list(v))}')

def main():
    calc()

if __name__ == '__main__':
    main()
