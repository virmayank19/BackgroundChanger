# BackgroundChanger
Changes background in video in a green screen 

![ezgif com-gif-maker (4)](https://user-images.githubusercontent.com/52134872/128388582-d8299016-c016-4db3-99fc-db2c8f473e4b.gif)

## How it works
We can describe this process in a straightforward way. 

- Takes the image captured through webcam or the image added in the folder
- Then takes the video from the webcam and subtracts the desired colour value from the image
- Then the adds the area of the image and replaces it with thearea which has the desired colour 

I also used dilation to remove the grainy effect and smoothen the desired area.
## How to use
If you want to capture the image which you want to apply then first run BackgroundCapture and if you want to add some other image then replace it with the image in the file location.

Built this project in **python** language with the help of **OpenCv** library.
### Requirements 
- numpy
- python3
- opencv
