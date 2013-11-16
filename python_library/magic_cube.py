import random
from Tkinter import Tk, Frame, Canvas

WINDOW_WIDTH = 800
WINDOW_HEIGHT = 800
base = 80
width = WINDOW_WIDTH - 2*base
height = WINDOW_HEIGHT - 2 * base

data = []
line = 4
row = 4

root = Tk()
canvas = Canvas(root, width = WINDOW_WIDTH, height = WINDOW_HEIGHT)

def draw():
	#for i in data:
	#	print str(i) + ' ',
	#print ""
	for i in range(line):
		canvas.create_oval(0, base + height * i / line, base, base + height * (i+1)/line, fill = 'pink')
		canvas.create_oval(width+base, base + height * i / line, WINDOW_WIDTH, base + height * (i+1)/line, fill = 'pink')

	for i in range(row):
		canvas.create_oval(base + width * i / row, 0, base + width * (i+1)/row, base, fill = 'pink')
		canvas.create_oval(base + width * i / row, height + base, base + width * (i+1)/row, WINDOW_HEIGHT, fill = 'pink')

	for i in range(line+1):
		canvas.create_line(base, base + height * i / line, base + width, base + height * i / line)
	for i in range(row+1):
		canvas.create_line(base + width * i / row, base, base + width * i / row, base + height)
	for i in range(line):
		for j in range(row):
			x = base + height * i / line + height / 2 / line
			y = base + width * j / row + width / 2 / row
			d = data[i * 4 + j]
			if d%4 == 0:
				#canvas.create_text(x, y, text = str(i*4+j) + " " + str(d/4+1), fill = 'red', font = ('', 20))
				canvas.create_text(x, y, text = str(d/4+1), fill = 'red', font = ('', 20))
			elif d%4 == 1:
				canvas.create_text(x, y, text = str(d/4+1), fill = 'black', font = ('', 20))
			elif d%4 == 2:
				canvas.create_text(x, y, text = str(d/4+1), fill = 'blue', font = ('', 20))
			else:
				canvas.create_text(x, y, text = str(d/4+1), fill = 'green', font = ('', 20))


def tick():
	canvas.delete("all")
	draw()
	canvas.after(100, tick)

def random_list(data):
	for (i, d) in enumerate(data):
		p = random.randint(0, i)
		(data[p], data[i]) = (data[i], data[p])

def key_event(event):
	key_char = event.char.upper()
	if key_char == 'R':
		random_list(data)
		tick()

def switch(start, step, num):
	t = data[start]
	for i in range(num-1):
		data[start + i * step] = data[start + (i+1) * step]
	data[start + (num-1) * step] = t

def click(x, y):
	if x < base or x > width + base:
		if y < base or y > height+base:
			return
		else:
			py = (y-base)/(height/line)
			start = py
			step = 4
			num = 4
			if x > width + base:
				start += 12
				step = -4
			switch(start, step, num)
	
	if y < base or y > height + base:
		if x < base or x > width + base:
			return
		else:
			px = (x-base)/(width/row)
			start = px * 4
			step = 1
			num = 4
			if y > height + base:
				start += 3
				step = -1
			switch(start, step, num)

def mouse_event(event):
	canvas.focus_set()
	click(event.x, event.y)

for i in range(4):
	for j in range(4):
		data.append(i*4 + j)
random_list(data)
canvas.focus_set()
canvas.bind('<Key>', key_event)
canvas.bind("<Button-1>", mouse_event)
tick()

canvas.pack()
root.mainloop()

