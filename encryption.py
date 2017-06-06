"""
此模块用来加密密码
"""

import hashlib

def sysu_entryption(password):
	m = hashlib.md5()
	#使用md5进行加密密码
	m.update(password.encode("utf-8"))
	psw = m.hexdigest()
	#学校选课系统在md5的基础上使得加密后的字符串小写变大写
	psw = psw.upper()
	return psw