# kivy-thelab
 
This is my first project using the Kivy framework, my goal is to understand the basics to apply them on my own projects.
I will follow the instructions from a freeCodeCamp video (link below).
I will also write down some notes that will be useful to me and could be useful for other people, I take this video as a class.

# Notes from freeCodeCamp Video

### Random notes
- on mac - Option + 9 = ` (backtick)
- while writing I noticed that I used a lot of CSS-like terminology, I hope this isn't a big issue for readers.
- you can use # to make comments in the .kv file

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
Elements will be placed one on top of each other (covering the first one) if they have the same dimensions and position. 
You can define colors with ```color: r, g, b, a```. This works for text, just like CSS.

## BoxLayout

We can switch our main interface from ```MainWidget:``` to ```BoxLayoutExample```. 
We have to import the BoxLayout but this allows us to have a more _responsive_ layout.
When defining the constructor for the BoxLayout class, you have to pass the ```**kwargs``` argument and inherit from that class with the super() function. 
When you add, for example, two buttons A and B they will take all the available space.
You can change the orientation just like with the ```flex-direction: column;``` in CSS, the default here is orizontal.
Everything that you declare in the _main.py_ file with Python syntax can be exported in the _project.kv_ file using the appropriate syntax.
The ```size``` and ```pos``` commands don't work in BoxLayout.

## Size_hint and Pos_hint
```size_hint```by default is 1, 1. Meaning 100% width and 100% height. You can declare both to None so you can use the size. The size can be divided into width and height.
The ```pos_hint``` is a dictionary that takes two inputs (one for x and one for y) choosing from three alternatives: x / center_x / right.

## Embed a Layout
You can put more layouts inside others. 

## AnchorLayout
The default behavior creates a button that takes up all the space and is centered. We need to use size_hint.
```anchor_x: ``` is "center" by default but can be changed to "right" or "left".
Like a normal widget, two elements in an AnchorLayout with the same charateristics will overlap one on top of the other.
Example: stacking vertically two Button in a BoxLayout that is anchored on the top-center of the AnchorLayout (made in the _AnchorLayour_ folder).


### Code Lines: 
- ```size: 400, 200``` -> size: _width_, _height_
- *1: ```size: "400dp", "200dp"```
- ```orientation: "value"```
