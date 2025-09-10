# import the cv2 module
import cv2 as c

print("Hello to your program to resize your image!")
print("\n========================================\n")

# get image path and store it in a var using imread(image read) in cv2
ImagePath = input("Enter the path for Image: ")
image = c.imread(ImagePath)

# taking option to resize or just show the image
option = input("do you want to resize it or no?: ")

if option.startswith('y'): # if string starts with 'y' (yes, yeah, yea, y, etc......)

    # taking the sizes of the image
    sizex = input("what size do you want it for X: ")
    sizey = input("what size do you want it for Y: ")

    # resize the image using resize func                      the interpolation to sure that no pixels lost
    image_resized = c.resize(image, (int(sizex), int(sizey)), interpolation=c.INTER_CUBIC)

    # finaly show the image
    c.imshow("Image Resized*", image_resized)
else: # otherwise if do not want to resize show it!
    c.imshow("Your Image", image)

# wait a key from user(waitKey func), because the image appear and close really fast to fix it we need to wait a key
c.waitKey(0)
# when user press any key such as 'k' destroy window(close it)
c.destroyAllWindows()

