#! /usr/bin/env python
# -*- coding:utf-8 -*-

import string, random


class LengthError(ValueError):
	def __init__(self,msgs):
		self.msgs = msgs

chars=string.ascii_letters+string.digits

invitation_code=lambda x,y: ''.join([random.choice(x) for i in range(y)])

def generate_invi_code(count,num,lengthOfkey):
	placeHolder='@'
	codeList=[]
	for i in range(count):
		try:
			code=invitation_code(chars,num)+placeHolder+padZeroToKey(1000,lengthOfkey)
			codeList.append(code)
		except LengthError as e:
			print(e.msgs)
	if len(codeList) > 0:
		return codeList

def padZeroToKey(index,lengthOfkey):
	lenOfIndex=len(str(index))
	if lenOfIndex==lengthOfkey:
		return str(index)
	elif lenOfIndex<lengthOfkey:
		return '0'*(lengthOfkey-lenOfIndex)+str(index)
	else:
		raise LengthError("Index exceeds the length of master key.")

if __name__ == '__main__':
	# pass
	print(generate_invi_code(200,16,3))
