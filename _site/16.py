# This Python file uses the following encoding: utf-8
"""
银行在打印票据的时候，常常需要将阿拉伯数字表示的人民币金额转换为大写表示，现在请你来完成这样一个程序。
在中文大写方式中，0到10以及100、1000、10000被依次表示为：
    零壹贰叁肆伍陆柒捌玖拾佰仟万
以下的例子示范了阿拉伯数字到人民币大写的转换规则：

1	壹圆
11	壹拾壹圆
111	壹佰壹拾壹圆
101	壹佰零壹圆
-1000	负壹仟圆
1234567	壹佰贰拾叁万肆仟伍佰陆拾柒圆

现在给你一个整数a(|a|<100000000), 打印出人民币大写表示
"""

a = 10000000
s = ''
n = 0 # 位数
flag = False #上次是不是加入'零'了
digit2ch = "零壹贰叁肆伍陆柒捌玖" 
weight2ch = "圆拾佰仟万"
while a:
	b = a%10
	if b != 0:
		while n > 4:
			s+=weight2ch[4]
			n-=4
		s+=weight2ch[n]
		s+=digit2ch[b]
		flag = False
	else:
		if not flag:
			s+='零'
			flag = True

	a/=10
	n+=1
