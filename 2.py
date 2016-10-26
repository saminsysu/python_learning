#! /usr/bin/env python
# -*- coding:utf-8 -*-

import string, random
import MySQLdb

class LengthError(ValueError):
	def __init__(self,msgs):
		self.msgs = msgs

chars=string.ascii_letters+string.digits

invitation_code=lambda x,y: ''.join([random.choice(x) for i in range(y)])

def generate_invi_code(count,num,lengthOfkey):
	conn=MySQLdb.connect(host='localhost',user='root',passwd='admin123',db='code')
	cursor=conn.cursor()
	placeHolder='@'
	codeList=[]
	for i in range(count):
		try:
			code=invitation_code(chars,num)+placeHolder+padZeroToKey(i,lengthOfkey)
			cursor.execute("insert into invitation_code values('%d','%s')" %(i, code))
			conn.commit()
			codeList.append(code)
		except LengthError as e:
			print(e.msgs)
	if len(codeList) > 0:
		return codeList
	cursor.close()
	conn.close()

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

