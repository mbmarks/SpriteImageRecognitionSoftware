## Sprite Image Recognition Software (SIRS)
This software uses machine learning techniques to automatically pick sprite images from the image bank from the GRT-WF (Gamma Ray Telescope – Wide Field) setup.
### Why use image recognition?
We use image recognition to speed up the process of finding sprite images among the potentially hundreds of images captured a day. We do sacrifice some accuracy, but with time and computing resources the accuracy can be increased.
### Where can I find SIRS?
The SIRS is available on GitHub. mbmarks/SpriteImageRecognitionSoftware (github.com)
### How to use the Sprite Image Recognition Software?
To use the software, you will need to have knowledge of Python and the terminal environment. The “raw” sprite images should be contained in a directory structure by camera, month, day, and year. The images are also named in the format of:
“M_YEAR/MONTH/DAY_HOUR/MINUTE/SECOND_FGCU_CAMERA”
Example: M20120110_231539_FGCU_02

Depending on which version being used the sprites are either analyzed by month or in a heap (all raw images in one folder). In this solution we will discuss when the images are in a heap.
