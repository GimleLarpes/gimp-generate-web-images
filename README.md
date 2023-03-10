# gimp-generate-web-images
GIMP plugin to quickly generate .jpeg and .webp images of various sizes for use on websites.

![Screenshot](https://github.com/GimleLarpes/gimp-generate-web-images/blob/main/screenshot.png?raw=true)

# Installation
- Download the script [generate_web_images.py](https://github.com/GimleLarpes/gimp-generate-web-images/blob/main/generate_web_images.py) and save it in your GIMP plugin directory. 
  - WINDOWS: `~\AppData\Roaming\GIMP\2.10\plug-ins\generate_web_images.py`
  - LINUX: `~/.gimp/plug-ins/generate_web_images.py`
- On Linux you need to set the script file to be executable. (`chmod +x generate_web_images.py`)
- Restart GIMP
- Run plugin from Image > Generate Web Images

# Usage
- Open the image you want to create web-optimized versions of in GIMP
- Run the plugin from Image > Generate Web Images
- ![plugin_location](https://user-images.githubusercontent.com/97182804/222878492-00aa0768-694b-4df4-8c9c-76af7a81be24.png)
- Choose image filename
- Choose desired resolutions (resolution given is the horizontal resolution of the generated images)
- If desired, change compression quality and/or add a copyright notice to JPEG images.
- Set export directory




Exported images will have their resolution appended to the end of their filename.
![exported_files](https://user-images.githubusercontent.com/97182804/222878500-d3b9faaa-491d-4cb9-a26f-43c02cb8019e.png)

