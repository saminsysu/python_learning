#! /usr/bin/env python
# -*- coding:utf-8 -*-

import re


if __name__ == '__main__':
	fp=open('test.txt','r')
	count=0
	for line in fp.readlines():
		# print(line)
		line=line[:-1]
		print line
		# charList=re.split(r'\s+',line)
		charList=line.split() #str.split
		count+=len(charList)
		print(charList)
		print(count)
