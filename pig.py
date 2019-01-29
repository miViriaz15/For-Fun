"""
picture.py
Author: miViriaz15
Credit: I used the internet for drawing inspiration, https://www.rapidtables.com/web/color/html-color-codes.html for color codes 
https://www.google.com/url?sa=i&source=images&cd=&cad=rja&uact=8&ved=2ahUKEwiPp8yf6JHgAhWnpYMKHcIeDt4Qjhx6BAgBEAM&url=http%3A%2F%2Flfas-computer-arts.blogspot.com%2F2016%2F09%2Fillustrator-shape-tool.html&psig=AOvVaw23gIAWwOWVCQlJECaK8GmZ&ust=1548810854186598 --> inspiration for the pig

Assignment:

Use the ggame library to "paint" a graphical picture of something (e.g. a house, a face or landscape).

Use at least:
1. Three different Color objects.
2. Ten different Sprite objects.
3. One (or more) RectangleAsset objects.
4. One (or more) CircleAsset objects.
5. One (or more) EllipseAsset objects.
6. One (or more) PolygonAsset objects.

See:
https://github.com/HHS-IntroProgramming/Standards-and-Syllabus/wiki/Displaying-Graphics
for general information on how to use ggame.

See:
http://brythonserver.github.io/ggame/
for detailed information on ggame.

"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset
from math import sqrt
# add your code here \/  \/  \/
#defining colors
cornflowerblue = Color(0x6495ED, 1.0)
black = Color(0x000000, 1.0)
white = Color(0xFFFFFF, 1.0)
gold = Color(0xFFD700, 1.0)
golder = Color(0xFFC900, 1.0)
pink = Color(0xFFB6C1, 1.0)
darkerpink = Color(0xDB7093, 1.0)
darkestpink = Color(0xCD5278, 1.0)
waydark = Color(0x8B2252, 1.0)
brown = Color(0x8B5A2B, 1.0)

#defining line
thinlineblue = LineStyle(1, cornflowerblue) 
thinlinewhite = LineStyle(1, white)
thinlineblack = LineStyle(1, black)
thinlinegold = LineStyle(1, gold)
thinlinegolder = LineStyle(1, golder) #I played around to get this one
thinlinepink = LineStyle(1, pink)
thinlinedarkerpink = LineStyle(1, darkerpink)
thinlinedarkestpink = LineStyle(1, darkestpink)
thinlinewaydark = LineStyle(1, waydark)
thinlinebrown = LineStyle(1, brown)

#Defining Shapes
head = CircleAsset(150, thinlinepink, pink)
nose = EllipseAsset(50, 30, thinlinedarkestpink, darkestpink)
nostril = CircleAsset (10, thinlinewaydark, waydark)
eye = CircleAsset(13, thinlinebrown, brown)
eartop =
#print
Sprite(head, (200,200))
Sprite(nose, (300, 350))
Sprite(nostril, (318, 370))
Sprite(nostril, (361, 370))
Sprite(eye, (260, 300))
Sprite(eye, (410, 300))
#s.rotation=inradians
# add your code here /\  /\  /\


myapp = App()
myapp.run()
