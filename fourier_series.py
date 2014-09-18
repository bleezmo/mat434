import matplotlib.pyplot as plt
from math import *

def plot(x,y):
	fig = plt.figure(figsize=(7,7))
	ax = fig.add_axes([0.06, 0.05, 0.6, 0.9])
	ax.plot(x,y,'go-')
	plt.show()
	plt.close('all')

def getFn(x,a0,an,bn):
	f = pi/2
	for n in range(1,11):
		f = f + (eval(an)*cos(n*x))+(eval(bn)*sin(n*x))
	return f

def start(a0,an,bn):
	end = int(pi*100*2)
	xarr,yarr = end*[None],end*[None]
	for x in range(0,end,1):
		x_offset = (x/100)-round(pi,2)
		xarr[x] = x_offset
		yarr[x] = getFn(x_offset,a0,an,bn)
	plot(xarr,yarr)

def sample():
	start("pi/2","(((2*((-1)**n))-2))/(pi*n*n)","0")