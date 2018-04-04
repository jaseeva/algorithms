from PIL import Image
from math import exp
import os


radius = 5
length = ((radius * 2) + 1)
sigma = 5
ext = ['.png', '.jpg', '.jpeg', '.bmp']


def isImage(file):
    for i in ext:
        if os.path.splitext(file)[1].lower() == i:
            return True
    return False


def selectImage():
    while True:
        imgpath = input("Please enter path to the image. Press x to exit. >>> ")
        if os.path.exists(imgpath):
            if isImage(imgpath):
                return imgpath
            else:
                print('Error: not an image. Please select another file.')
                continue
        elif imgpath == 'x':
            quit()
        else:
            print('Error: invalid path')
            continue


def gaussian(x, mu, sigma):
    return exp(-(((x-mu)/sigma)**2)/2.0)


def gauss():
    kernel_radius = radius

    # compute the actual kernel elements
    hkernel = [gaussian(x, kernel_radius, sigma) for x in range(2*kernel_radius+1)]
    vkernel = [x for x in hkernel]
    kernel2d = [[xh*xv for xh in hkernel] for xv in vkernel]

    # normalize the kernel elements
    kernelsum = sum([sum(row) for row in kernel2d])
    kernel2d = [[x/kernelsum for x in row] for row in kernel2d]

    # for line in kernel2d:
        # print(["%.4f" % x for x in line])

    return kernel2d


def checkpixel(targetx, targety, xsize, ysize):
    if targetx <= 0:
        targetx = 0
    if targetx >= (xsize - 1):
        targetx = xsize - 1
    if targety <= 0:
        targety = 0
    if targety >= ysize - 1:
        targety = ysize - 1
    return targetx, targety


def calculatePixel(img, xcord, ycord, kernel2d):
    resR = 0
    resG = 0
    resB = 0
    for i in range(-radius, radius+1):
        for j in range(-radius, radius+1):
            targx = xcord + i
            targy = ycord + j
            p = img.getpixel((checkpixel(targx, targy, img.size[0], img.size[1])))

            ki = radius + i
            kj = radius + j
            resR += p[0] * kernel2d[ki][kj]
            resG += p[1] * kernel2d[ki][kj]
            resB += p[2] * kernel2d[ki][kj]

    return int(resR), int(resG), int(resB)


def blur(img, imgOut, xsize, ysize, imgpath):
    kernel = gauss()
    part = int(ysize / 100)
    for y in range(0, ysize):
        for x in range(0, xsize):
            pix = (calculatePixel(img, x, y, kernel))
            imgOut.putpixel((x, y), pix)
        if y % part == 0:
            print(int(y / part), '%')
        newname = os.path.splitext(imgpath)[0] + '_blurred' + os.path.splitext(imgpath)[1]
        imgOut.save(newname)


if __name__ == "__main__":
    path = selectImage()
    img = Image.open(path)
    imgOut = Image.open(path)
    xs, ys = img.size
    blur(img, imgOut, xs, ys, path)

