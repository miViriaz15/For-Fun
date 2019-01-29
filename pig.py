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
orange = Color(0xFF8247, 1.0)
green = Color(0x2E8B57, 1.0)

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
thinlineorange = LineStyle(1, orange) 
thinlinegreen = LineStyle(1, green)

#Defining Shapes
head = CircleAsset(150, thinlinewhite, pink)
nose = EllipseAsset(50, 30, thinlinedarkestpink, darkestpink)
nostril = CircleAsset (10, thinlinewaydark, waydark)
eye = CircleAsset(13, thinlinebrown, brown)
eartopl = PolygonAsset([(70, 170), (180, 220), (140, 260)], thinlinedarkerpink, darkerpink)
eartopr = PolygonAsset([(70,220), (110, 260), (180, 170)], thinlinedarkerpink, darkerpink)
earbottoml = PolygonAsset([(70, 170), (140, 260), (100, 260)], thinlinedarkestpink, darkestpink)
earbottomr = PolygonAsset([(110,260), (180,170), (150, 260)], thinlinedarkestpink, darkestpink)
body = RectangleAsset(350,200,thinlinepink, pink)
carrot = PolygonAsset([(90,100), (300, 80), (300, 130)], thinlineorange, orange)
shoot = RectangleAsset(100,3,thinlinegreen, green)
    
#print
Sprite(head, (200,200))
Sprite(nose, (300, 350))
Sprite(nostril, (318, 370))
Sprite(nostril, (361, 370))
Sprite(eye, (260, 300))
Sprite(eye, (410, 300))
Sprite(eartopl, (155,178))
Sprite(eartopr, (435, 180))
Sprite(earbottoml, (155,178))
Sprite(earbottomr, (475,181))
Sprite(body, (175, 485))
s = Sprite(shoot, (800, 340))
r = Sprite(shoot, (800, 340))
c = Sprite(carrot, (600, 390))
c.rotation=.4

#s.rotation=inradians
# add your code here /\  /\  /\


myapp = App()
myapp.run()
