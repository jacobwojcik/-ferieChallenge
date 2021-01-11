from PIL import Image
import os

try:
    os.mkdir('./images/smaller')
except:
    pass

images_dir = './images'

old_size=0
new_size=0
for img in os.listdir(images_dir):
    try:
        img_resolve =  Image.open("./images/{}".format(img))
        img_resolve.save("./images/smaller/{}".format(img), quality=50) 
        print(img + " compressed")
        old_size+=(os.stat('./images/{}'.format(img)).st_size)
        new_size+=(os.stat('./images/smaller/{}'.format(img)).st_size)
    except:
        pass

print("\n")
print("Images before compression: {:.2f} MB".format(old_size/1024**2))
print("Compressed images: {:.2f} MB, {:.0f}% less".format(new_size/1024**2,100-(new_size*100/old_size)))