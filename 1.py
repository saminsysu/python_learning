#! /usr/bin/env python
# -*- coding:utf-8 -*-

import string, random

chars=string.ascii_letters+string.digits

invitation_code=lambda x,y: ''.join([random.choice(x) for i in range(y)])

def generate_invi_code(count,num):
	codeList=[]
	for i in range(count):
		codeList.append(invitation_code(chars,num))
	return codeList

if __name__ == '__main__':
	# pass
	print(generate_invi_code(200,16))
