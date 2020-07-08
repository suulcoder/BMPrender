"""
---------------------------------------------------------------------

Universidad del Valle de Guatemala
Saúl Contreras	18409
Gráficas por Computadora
SR1: Point

This file is a test of the class render.py
---------------------------------------------------------------------
"""

from render import Render

gl = Render()										#glinit is in the constructor of the class
gl.finish('test1.bmp')								#Should shave a black image with default width and height 720*480

gl.CreateWindow(600,300)								
gl.finish('test2.bmp')								#Should shave a black image width and height 200*100					

gl.viewPort(300, 0, 300, 150)						#ViewPort should be the fourth quadrant of the image
gl.vertex(0,0)
gl.color(1,0,0)										
for i in range(-50,51):
	gl.vertex(-1,i/50)
	gl.vertex(1,i/50)
gl.color(0,1,0)								
for i in range(-50,51):
	gl.vertex(i/50,-1)
	gl.vertex(i/50,1)
gl.finish('test3.bmp')								#Should save an image with a square with green lines on top and bottom, and red lines in right and left. and a black point in the middle of viewport

gl.clearColor(1,0,0)									
gl.clear()
gl.finish('test4.bmp')								#Should shave a red image width and height 200*100						
