#!/usr/bin/env python

# Create .webp and .jpg images in variable sizes
from gimpfu import *
import os

def generate_web_images(image, drawable, filename, resolutions, jpeg_quality, jpeg_smooth, webp_quality, savedir, comment):
    pdb.gimp_image_undo_group_start(image)

    # Aspect ratio
    h = float(pdb.gimp_image_height(image))
    w = float(pdb.gimp_image_width(image))
    ASPECT_RATIO = float(w / h)

    # JPEG settings
    jpeg_quality = float(jpeg_quality/100.0)
    jpeg_smooth =  float(jpeg_smooth/100.0)
    # WEBP settings
    webp_quality = float(webp_quality)


    # Create images
    resolutions = resolutions.replace(","," ")
    resolutions = "".join(c for c in resolutions if (c.isdigit() or c ==" "))
    resolutions = sorted(list(map(int, resolutions.split())), reverse=True)
    max_width = max(resolutions)
    for resolution in resolutions:
        generate_images(image, drawable, savedir, filename, w, ASPECT_RATIO, resolution, max_width, jpeg_quality, jpeg_smooth, webp_quality, comment)
    
    pdb.gimp_image_undo_group_end(image)


def generate_images(image, drawable, savedir, filename, picture_width, ASPECT_RATIO, scale_width, max_width, jpeg_quality, jpeg_smooth, webp_quality, comment):
    # Filler digits
    max_slength = len(str(max_width))
    scale_slength = len(str(scale_width))
    d_slength = max_slength - scale_slength
    if d_slength > 0:
        filler_digit = "0" * d_slength
    else:
        filler_digit = ""

    # Create image if possible
    if picture_width >= scale_width:
        pdb.gimp_image_scale(image, scale_width, int(round(scale_width/ASPECT_RATIO)))

        # Save JPEG
        pdb.file_jpeg_save(image, drawable, os.path.join(savedir,(filename+"-"+str(filler_digit)+str(scale_width)+".jpeg")), filename+"-"+str(filler_digit)+str(scale_width)+".jpeg", jpeg_quality, jpeg_smooth, 1, 1, comment, 1, 0, 128, 2)
        
        # Save WEBP
        pdb.file_webp_save2(image, drawable, os.path.join(savedir,(filename+"-"+str(filler_digit)+str(scale_width)+".webp")), filename+"-"+str(filler_digit)+str(scale_width)+".webp", 2, 0, webp_quality, 0.0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)


register(
    "python-fu-generate-web-images",
    "Generate Images For Websites",
    "Creates .webp and .jpg images for use on the web. Images are exported to the provided folder or to 'Pictures' if no folder is provided.",
    "Gimle Larpes",
    "Gimle Larpes",
    "2023",
    "Generate Web Images",
    "*",
    [
    (PF_IMAGE, "image", "takes current image", None),
    (PF_DRAWABLE, "drawable", "Input layer", None),
    (PF_STRING, "filename", "Image Name:", "Image"),
    (PF_STRING, "resolutions", "Horizontal Resolutions:", "720, 1280, 1920"),
    (PF_SLIDER, "jpeg_quality", "JPEG Quality:", 85, (0, 100, 1)),
    (PF_SLIDER, "jpeg_smooth", "JPEG Smoothing:", 25, (0, 100, 1)),
    (PF_SLIDER, "webp_quality", "WebP Quality:", 80, (0, 100, 1)),
    (PF_DIRNAME, "savedir", "Export Directory:", os.path.join(os.environ['USERPROFILE'],"Pictures")),
    (PF_STRING, "comment", "Image Comment:", ""),  # (jpeg only)
    ],
    [],
    generate_web_images,
    menu="<Image>/Image"
    )


main()
