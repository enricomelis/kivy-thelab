# Notes from freeCodeCamp Video

### Random notes
on mac - Option + 9 = ` (backtick)

link to the video [here](https://youtu.be/l8Imtec4ReQ)

## Installation

As now, Apr 27th 2023, the  ```pip3 install kivy```  only works with Python 3.10
(I'm using Python 3.10.11)

## Button and Label

In your _project.kv_ file you can define some stuff for the actual window, that will be showed when executing the _main.py_ file. 
The _project.kv_ file has to be in the same directory as the _main.py_ file.

The default coordinates for objects are 0, 0. This means that an object with undefined coordinates will be placed in the bottom-left corner.
The default dimensions for a Button are 100px x 100px.
Best practice is to declare sizes that are _responsive_ (in Web Dev terms) to fit as much screen sizes as we can. We accomplish this with _dp_ *1. 40dp x 40dp is the size of a finger and will be the same across all devices.

### Code Lines: 
- ```size: 400, 200``` -> size: _width_, _height_
- *1: ```size: "400dp", "200dp"```