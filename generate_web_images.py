#!/usr/bin/env python

#Create .webp and .jpg images in sizes: 3840, 2560, 1920, 1600, 1440, 1280, 1080, 720, 480, 360
from gimpfu import *
import os

def generate_web_images(image, drawable, filename, res_3840, res_2560, res_1920, res_1600, res_1440, res_1280, res_1080, res_720, res_480, res_360, jpeg_quality, jpeg_smooth, webp_quality, savedir, COPYRIGHT):
    pdb.gimp_image_undo_group_start(image)
    #Aspect Ratio
    h = float(pdb.gimp_image_height(image))
    w = float(pdb.gimp_image_width(image))
    ASPECT_RATIO = float(w / h)

    #JPEG SETTINGS
    jpeg_quality = float(jpeg_quality/100.0)
    jpeg_smooth =  float(jpeg_smooth/100.0)
    #WEBP SETTINGS
    webp_quality = float(webp_quality)


    ####Create Images
    #Create 3840 images if possible
    generate_images(image, drawable, savedir, filename, w, ASPECT_RATIO, 3840, res_3840, jpeg_quality, jpeg_smooth, webp_quality, COPYRIGHT)
    #Create 2560 images if possible
    generate_images(image, drawable, savedir, filename, w, ASPECT_RATIO, 2560, res_2560, jpeg_quality, jpeg_smooth, webp_quality, COPYRIGHT)
    #Create 1920 images if possible
    generate_images(image, drawable, savedir, filename, w, ASPECT_RATIO, 1920, res_1920, jpeg_quality, jpeg_smooth, webp_quality, COPYRIGHT)
    #Create 1600 images if possible
    generate_images(image, drawable, savedir, filename, w, ASPECT_RATIO, 1600, res_1600, jpeg_quality, jpeg_smooth, webp_quality, COPYRIGHT)
    #Create 1440 images if possible
    generate_images(image, drawable, savedir, filename, w, ASPECT_RATIO, 1440, res_1440, jpeg_quality, jpeg_smooth, webp_quality, COPYRIGHT)
    #Create 1280 images if possible
    generate_images(image, drawable, savedir, filename, w, ASPECT_RATIO, 1280, res_1280, jpeg_quality, jpeg_smooth, webp_quality, COPYRIGHT)
    #Create 1080 images if possible
    generate_images(image, drawable, savedir, filename, w, ASPECT_RATIO, 1080, res_1080, jpeg_quality, jpeg_smooth, webp_quality, COPYRIGHT)
    #Create 720 images if possible
    generate_images(image, drawable, savedir, filename, w, ASPECT_RATIO, 720, res_720, jpeg_quality, jpeg_smooth, webp_quality, COPYRIGHT)
    #Create 480 images if possible
    generate_images(image, drawable, savedir, filename, w, ASPECT_RATIO, 480, res_480, jpeg_quality, jpeg_smooth, webp_quality, COPYRIGHT)
    #Create 360 images if possible
    generate_images(image, drawable, savedir, filename, w, ASPECT_RATIO, 360, res_360, jpeg_quality, jpeg_smooth, webp_quality, COPYRIGHT)

    pdb.gimp_image_undo_group_end(image)



####FUNCTIONS####
def generate_images(image, drawable, savedir, filename, picture_width, ASPECT_RATIO, scale_width, enabled, jpeg_quality, jpeg_smooth, webp_quality, COPYRIGHT):
    #Create image if possible
    if picture_width >= scale_width and enabled:
        if scale_width >= 1000:
            filler_digit = ""
        else:
            filler_digit = "0"
        pdb.gimp_image_scale(image, scale_width, int(round(scale_width/ASPECT_RATIO)))
        #Save JPEG
        pdb.file_jpeg_save(image, drawable, os.path.join(savedir,(filename+"-"+str(filler_digit)+str(scale_width)+".jpeg")), filename+"-"+str(filler_digit)+str(scale_width)+".jpeg", jpeg_quality, jpeg_smooth, 1, 1, COPYRIGHT, 1, 0, 128, 2)
        #Save WEBP
        pdb.file_webp_save2(image, drawable, os.path.join(savedir,(filename+"-"+str(filler_digit)+str(scale_width)+".webp")), filename+"-"+str(filler_digit)+str(scale_width)+".webp", 2, 0, webp_quality, 0.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
#################




register(
    "python-fu-generate-web-images",
    "Generate Images For Websites",
    "Creates .webp and .jpg images with horizontal resolution: 3840, 2560, 1920, 1600, 1440, 1080, 720, 480, 360. Images are exported to given folder or reverts to 'Pictures' folder.",
    "Gimle Larpes",
    "Gimle Larpes",
    "2023",
    "Generate Web Images",
    "*",
    [
    (PF_IMAGE, "image", "takes current image", None),
    (PF_DRAWABLE, "drawable", "Input layer", None),
    (PF_STRING, "filename", "Image Name:", "Image"),
    (PF_BOOL, "res_3840", "3840:", False),
    (PF_BOOL, "res_2560", "2560:", False),
    (PF_BOOL, "res_1920", "1920:", False),
    (PF_BOOL, "res_1600", "1600:", False),
    (PF_BOOL, "res_1440", "1440:", False),
    (PF_BOOL, "res_1280", "1280:", False),
    (PF_BOOL, "res_1080", "1080:", True),
    (PF_BOOL, "res_720", "720:", True),
    (PF_BOOL, "res_480", "480:", True),
    (PF_BOOL, "res_360", "360:", False),
    (PF_SLIDER, "jpeg_quality", "JPEG Quality:", 90, (0, 100, 1)),
    (PF_SLIDER, "jpeg_smooth", "JPEG Smoothing:", 25, (0, 100, 1)),
    (PF_SLIDER, "webp_quality", "WebP Quality:", 85, (0, 100, 1)),
    (PF_DIRNAME, "savedir", "Export Directory:", os.path.join(os.environ['USERPROFILE'],"Pictures")),
    (PF_STRING, "COPYRIGHT", "Copyright Notice:", ""),    #COPYRIGHT NOTICE (jpeg)
    ],
    [],
    generate_web_images,
    menu="<Image>/Image"
    )

main()
