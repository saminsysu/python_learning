#! /usr/bin/env python
# -*- coding:utf-8 -*-

from PIL import Image, ImageDraw, ImageFont

def write_num(img,num):
	w,h=img.size
	draw = ImageDraw.Draw(img)
	ttFont = ImageFont.truetype("/usr/share/fonts/truetype/freefont/FreeSans.ttf",(int)(h/30+w/30))
	draw.text((w/2,h/2),num,fill=(255,0,0),font=ttFont)
	# draw.text((w-10,10),num,fill=(255,0,0))
	img.show()
	img.save('0_draw.png')
	# print ('width=%d,height=%d' %(w,h))

if __name__ == '__main__':
	img=Image.open('0')
	write_num(img,'1')
