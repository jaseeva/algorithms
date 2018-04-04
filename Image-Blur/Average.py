from PIL import Image
import os


radius = 2
length = ((radius * 2) + 1)
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


def averageval(image, xcord, ycord):
    aveR = 0
    aveG = 0
    aveB = 0
    for i in range(-radius, radius+1):
        for j in range(-radius, radius+1):
            targx = xcord + i
            targy = ycord + j
            p = image.getpixel((checkpixel(targx, targy, image.size[0], image.size[1])))

            aveR += p[0]
            aveG += p[1]
            aveB += p[2]

    aveR /= (length ** 2)
    aveG /= (length ** 2)
    aveB /= (length ** 2)
    return int(aveR), int(aveG), int(aveB)


def blur(imgIn, imgOut, xsize, ysize, imgpath):
    part = int(ysize / 100)
    for y in range(0, ysize):
        for x in range(0, xsize):
            pix = (averageval(imgIn, x, y))
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
