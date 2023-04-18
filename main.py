import image_loader as img_loader
import image_preprocessing as img_preproc

img = img_loader.load_image('mona_lisa.png')
img_loader.show_image(img)

img_loader.show_image(img_preproc.grayscale_conversion(img, True))

new_size = (200, 350)
img_loader.show_image(img_preproc.resize(img, new_size, True))

top_left = (0, 0)
bottom_right = (100, 300)
img_loader.show_image(img_preproc.crop(img, top_left, bottom_right, True))

#pula