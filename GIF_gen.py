import imageio.v3 as iio

print("This script creates a GIF from two images, The images should be in the same directory as this script and they need to be of the same width and height.")


image1 = input("Enter the first image filename (with extension): ")
image2 = input("Enter the second image filename (with extension): ")
gifname = input("Enter the desired GIF filename (with .gif extension): ")
if not gifname.lower().endswith('.gif'):
    print("Error: The filename must end with .gif")
    exit()

if not (image1.lower().endswith(('.png', '.jpg', '.jpeg')) and image2.lower().endswith(('.png', '.jpg', '.jpeg'))):
    print("Error: Please provide valid image files with .png, .jpg, or .jpeg extensions.")
    exit()

if image1 == image2:
    print("Error: Please provide two different images.")
    exit()

if image1 == '' or image2 == '':
    print("Error: Please provide both image filenames.")
    exit()

filenames = [ image1, image2]
images = [ ]

for filename in filenames:
    images.append(iio.imread(filename))

iio.imwrite(gifname, images, duration=500, loop=0)
print(f"GIF '{gifname}' created successfully.")
