#coding=utf-8
"""
下过象棋的人都知道，马只能走'日'字形（包括旋转90°的日），现在想象一下，给你一个n行m列网格棋盘，
棋盘的左下角有一匹马，请你计算至少需要几步可以将它移动到棋盘的右上角，若无法走到，则输出-1.
如n=1，m=2,则至少需要1步；若n=1，m=3,则输出-1。
"""

"""
给你一个时间t（t是一个字典，共有六个字符串key(year,month,day,hour,minute,second),值为每个值为数字组成的字符串，
如t={'year':'2013','month':'9','day':'30','hour':'16','minute':'45','second':'2'}
请将其按照以下格式输出， 格式:XXXX-XX-XX XX:XX:XX。如上例应该输出： 2013-09-30 16:45:02。
"""
t={'year':'2013','month':'9','day':'30','hour':'16','minute':'45','second':'2'}
def sup(s,n):
	return '0'*(n-len(s))+s
print ("%s-%s-%s %s:%s:%s" % (sup(t['year'],4),sup(t['month'],2),sup(t['day'],2),sup(t['hour'],2),sup(t['minute'],2),sup(t['second'],2))) 
