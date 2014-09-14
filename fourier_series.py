import matplotlib.pyplot as plt
import math

def plot(x,y):
	fig = plt.figure(figsize=(7,7))
	ax = fig.add_axes([0.06, 0.05, 0.6, 0.9])
	ax.plot(x,y,'go-')
	plt.show()
	plt.close('all')

def getFn(x):
	f = math.pi/2
	for n in range(1,11):
		f = f + (((2*((-1)**n))-2)*math.cos(n*x))/(math.pi*n*n)
	return f

def start():
	end = int(math.pi*100*2)
	xarr,yarr = end*[None],end*[None]
	for x in range(0,end,1):
		x_offset = (x/100)-round(math.pi,2)
		xarr[x] = x_offset
		yarr[x] = getFn(x_offset)
	plot(xarr,yarr)
start()	

