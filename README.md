# AsciiPy
translate images, videos and text to Ascii arts easy

translate text to asciiart with 400+ different fonts and images, videos from any path or url!

![](https://media.giphy.com/media/WrJ7YDJhx8J5KjYmwM/giphy.gif)
## Install
to install you have to clone the repository
```shell
$ git clone https://github.com/R4yGM/AsciiPy
```
## Depencies
this tool has dependency, and to install them you have to run 
```shell
$ chmod +x requirements.sh
$ ./requirements.sh
```
## Asciify in your python script
to start asciifying in your script you have to import the module
```python
import AsciiPy
```
### Asciify a text in python script
after you have imported the module type:
```python
text = AsciiPy.AsciiText.GenerateText(TEXT, FONT")
text = AsciiPy.AsciiText.GenerateText("Hey", "graffiti")
print(text)
```
to asciify a text
### Asciify a image from url in your python script
after you have imported the module type:
```python
img = AsciiPy.AsciiImage.GenerateFromUrl("https://r4yan.ga/images-videos/python-logo.png")
print(img)
```
to asciify a image by url
### Asciify a image from path in your python script
after you have imported the module type:
```python
img = AsciiPy.AsciiImage.GenerateFromPath("python-logo.png")
print(img)
```
to asciify a image by url
### Asciify a video from path in your python script
after you have imported the module type:
```python
AsciiPy.AsciiImage.VideoFromPath("images-videos/cube.mp4")
#this will automatically prints the video
```
to asciify a video by path
### Asciify a video from url in your python script
after you have imported the module type:
```python
AsciiPy.AsciiImage.VideoFromUrl("https://r4yan.ga/images-videos/cube.mp4")
#this will automatically prints the video
```
to asciify a video by url
### Get list of fonts in python script
after you have imported the module type:
```python
lst = AsciiPy.AsciiText.FontList()
print(lst)
```
this will print ove 400 different fonts you can use to generate texts
## Asciify in Terminal

### Asciify a image from url
to asciify a image you have to run
```shell
$ py AsciiPy -u [url for your image]
```
example 
```shell
$ py AsciiPy -u https://r4yan.ga/images-videos/python-logo.png
```
### Asciify a image from path
to asciify a image from path you have to run
```shell
$ py AsciiPy -p [path for your image]
```
### Asciify a text
```shell
$ py AsciiPy -t [text] [font]
```
if you need a font list just type
```shell
$ py AsciiPy -f
```
### Asciify a Video from path
```shell
$ py AsciiPy -vid-path [path to video]
```
### Asciify a Video from url
```shell
$ py AsciiPy -vid-url [url to video]
```
### help
```shell
$ py AsciiPy -h
```
this prints a list of commands with examples
