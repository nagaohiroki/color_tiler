import pyautogui

def add_list(norm, val, bias):
    index = 0
    for n in norm:
        if val > n - bias and val < n + bias:
            return index
        index += 1
    norm.append(val)


def calc():
    bias = 2
    color_dict = {}
    ys = []
    xs = []
    for i in range(10):
        tiles = pyautogui.locateAllOnScreen(f'img/img_{i}.png')
        if tiles is None:
            return
        centers = []
        for tile in tiles:
            center = pyautogui.center(tile)
            add_list(ys, center.y, bias)
            add_list(xs, center.x, bias)
            centers.append(center)
        color_dict[i] = centers
    xs.sort()
    ys.sort()
    normalize_dict = {}
    for k, vals in color_dict.items():
        norm_pos = []
        for val in vals:
            norm_x = add_list(xs, val.x, bias)
            norm_y = add_list(ys, val.y, bias)
            norm_pos.append((norm_x, norm_y))
        normalize_dict[k] = norm_pos
    print(normalize_dict)
    print(xs)
    print(ys)
    max_x = len(xs)
    max_y = len(ys)
    for x in range(max_x):
        for y in range(max_y):
            print(xs[x], ys[y])


def is_cross_tile(normalize_dict, x, y):
    pass





def main():
    calc()

if __name__ == '__main__':
    main()
