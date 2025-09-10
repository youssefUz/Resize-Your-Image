import cv2 as c

print("Hello to your program to resize your image!")

ImagePath = input("Enter the path for Image: ")
image = c.imread(ImagePath)

option = input("do you want to resize it or no?: ")

if option.startswith('y'):
    sizex = input("what size do you want it for X: ")
    sizey = input("what size do you want it for Y: ")

    image_resized = c.resize(image, (int(sizex), int(sizey)), interpolation=c.INTER_CUBIC)

    c.imshow("Image Resized*", image_resized)
else:
    c.imshow("Your Image", image)

c.waitKey(0)
c.destroyAllWindows()
