#! /usr/bin/env python
# -*- coding:utf-8 -*-

import string
import random
import Image,ImageDraw,ImageFont,ImageFilter

def generateChars(num):
	return [random.choice(string.ascii_letters) for i in range(num)]

def generateColor():
	return (random.randint(0,255),random.randint(0,255),random.randint(0,255))

def generatePic():
	width=200
	height=40
	num=4
	pic=Image.new('RGB',(width,height),(220,220,220))
	# pic.show()
	draw=ImageDraw.Draw(pic)
	chars=generateChars(num)
	font=ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSerif.ttf",20)
	for i in range(num):
		draw.text(((i+1)*width/(num+1),height/5),chars[i],generateColor(),font)
	for _ in range(random.randint(500,1000)):
		draw.point((random.randint(0,width),random.randint(0,height)),fill=generateColor())
	pic.filter(ImageFilter.BLUR)
	pic.save('code.png')
	pic.show()

if __name__ == '__main__':
	generatePic()
