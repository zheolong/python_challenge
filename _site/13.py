# This Python file uses the following encoding: utf-8
"""
光棍们对1总是那么敏感，因此每年的11.11被戏称为光棍节。
鄙人光棍几十载，光棍自有光棍的快乐。让我们勇敢面对光棍的身份吧，
现在就证明自己：给你一个整数a，数出a在二进制表示下1的个数，并输出。
"""
def count_binary_1(a):
	c=0
	while a:
		c+=1
		a&=a-1
	
	return c

n=4
print count_binary_1(a)
