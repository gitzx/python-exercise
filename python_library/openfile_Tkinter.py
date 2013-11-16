# -*- coding:utf-8 -*-
import Tkinter
import Tkinter
from Tkinter import *
import tkFileDialog as filedialog
	
def callback(event):
    global war_file
    entry_excel.delete(0,END) #清空entry里面的内容
    #调用filedialog模块的askdirectory()函数去打开文件夹
    #filepath = filedialog.askdirectory()
    filepath = filedialog.askopenfilename(initialdir = 'E:')
    war_file = filepath
    if filepath:
        entry_excel.insert(0,filepath) #将选择好的路径加入到entry里面
        
def eBtnCompute(event):
    sheetA = entry_sheetA.get()
    sheetB = entry_sheetB.get()
    sheet1 = int(sheetA)
    sheet2 = int(sheetB)
    print sheet1+sheet2
	
#点击关闭按钮后： 
def eBtnClose(event):
	entry_sheet.delete(0, END)
	root.destroy()
	
if __name__ == '__main__':
	war_file =''
	sheet1 = 0
	sheet2 = 1
	root = Tkinter.Tk(className="gui")
	root.geometry("400x220+400+400") #在xy轴200-200的位置创建400*220的窗口
	line_1 = Tkinter.Frame(root)
	l_1 = Tkinter.Label(line_1,text="选择一个文件：",width="18")
	entry_excel = Tkinter.Entry(line_1,width="31")
	l_1.pack(side = "left",pady = 25)
	entry_excel.pack(side = "left")

	btnRead = Tkinter.Button(line_1,text="打开")
	btnRead.bind('<Button-1>',callback)
	btnRead.pack(side="left")
	line_1.pack(side = "top",fill = "x")

	line_2 = Tkinter.Frame(root)
	l_2 = Tkinter.Label(line_2,text="编号1：",width="15")
	entry_sheetA = Tkinter.Entry(line_2,width="9")
	l_2.pack(side = "left",pady = 10)
	entry_sheetA.pack(side = "left")
	
	l_2 = Tkinter.Label(line_2,text="编号2：",width="15")
	entry_sheetB = Tkinter.Entry(line_2,width="9")
	l_2.pack(side = "left",pady = 10)
	entry_sheetB.pack(side = "left")

	btnCompute = Tkinter.Button(line_2,text="计算")
	btnCompute.bind('<Button-1>',eBtnCompute)
	btnCompute.pack(side="left")
	line_2.pack(side = "top",fill = "x")

	
	root.mainloop()
