"""Denoise an image

Uses the method in Bishop p.387
"""

import numpy as np
import matplotlib.pyplot as mp
import Image

def pt_gen(rows, cols, border=1):
    return ((y, x) for x in range(border, cols - border) for y in range(border, rows - border))

def energy(y, x, xi, i):
    h, beta, nu = 0, 1., 2.1
    ns = np.array([(0, 1), (0, -1), (1, 0), (-1, 0)])
    e = h if xi else 0.
    e += -nu if xi ==  y[i] else nu
    e += sum([-beta if xi == x[tuple(n + i)] else beta for n in ns])
    return e

def pix_diff(gt, x):
    cor = np.sum(gt == x) / float(gt.size)
    print('Correct [%f]' % (cor))


def img_to_bool(img):
    cols, rows = img.size
    return np.fromstring(img.tostring(), dtype=np.bool).reshape((rows, cols))

def main(gt_fn='gt.png', input_fn='input.png'):
    img = Image.open(input_fn)
    gt_img = Image.open(gt_fn)
    cols, rows = img.size
    y = img_to_bool(img)
    gt = img_to_bool(gt_img)
    x = np.array(y)
    pix_diff(gt, x)
    for i in pt_gen(rows, cols):
        e0 = energy(y, x, x[i], i)
        e1 = energy(y, x, not x[i], i)
        if e1 < e0:
            x[i] = not x[i]
    pix_diff(gt, x)
    mp.imshow(x  * np.uint8(255))
    mp.gray()
    mp.show()

if __name__ == '__main__':
    main()
