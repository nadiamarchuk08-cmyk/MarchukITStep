import cv2
from PIL import Image

image_path = 'cat.jpg'
overlay_path = 'vusa.png'
cat_face_cascade = cv2.CascadeClassifier('cascade.xml')

image = cv2.imread(image_path)
cat = Image.open(image_path)
mustache = Image.open(overlay_path)

cat = cat.convert("RGBA")
mustache = mustache.convert("RGBA")

cat_face = cat_face_cascade.detectMultiScale(image)

for (x, y, w, h) in cat_face:
    mustache_width = int(w * 1.2)
    mustache_height = int(mustache_width * (mustache.height / mustache.width))
    mustache_start_y = y + int(h * 0.6)
    mustache_start_x = x - int((mustache_width - w) / 2)
    mustache_resized = mustache.resize((mustache_width, mustache_height))

    cat.save('cat_with_mustache.png')
    new_cat = cv2.imread('cat_with_mustache.png')

    cv2.imshow('My cat with mustache', new_cat)

    cv2.waitKey()
