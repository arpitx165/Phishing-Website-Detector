from Tkinter import *
import tkMessageBox
from web_trainer import Webtrainer as WT
import pandas
from web_main import Webmain as WM
#from PIL import Image, ImageTk
import datetime

root = Tk()
lab = Label(root, bg= "#007777", fg= "silver")
lab.pack()

def clock():
    time = datetime.datetime.now().strftime("Time: %H:%M:%S")
    lab.config(text=time)
    #lab['text'] = time
    root.after(1000, clock) # run itself again after 1000 ms

# run first time
clock()
#
#im = Image.open('apple_ex.png')
#tkimage = ImageTk.PhotoImage(im)
#l =Label(root,  image = tkimage)
#l.place(x=0, y=0, relwidth=1, relheight=1)
frame = Frame(root, bg = "#007777")
frame.pack()
bottomframe1 = Frame(root, bg = "#007777")
bottomframe1.pack()
bottomframe = Frame(root, bg = "#007777")
bottomframe.pack(side = BOTTOM )
#root.attributes("-alpha", 0.5)    # this is for the opacity of the window


backgroundC = StringVar()
backgroundC.set("bl")
var = StringVar()
label = Label(frame, textvariable=var, pady= 30, relief=FLAT, fg="silver", font=("Cambria", 26) , bg = "#007777")
var.set("PHISHING WEBSITE DETECTOR")
label.pack()


L1 = Label(frame, text="Enter the URL: ", bg = "#007777", fg = "grey", pady = "40")
L1.pack( side = LEFT)
E1 = Entry(frame, bd =1, width=100)
E1.pack(side = RIGHT)
def submitCallBack():
	url=E1.get()
	print url
	processing_reference=WM()
	processing_reference.TestUrl(url,'test_features.csv')
	#ans = tr.gui_caller('url_features.csv','test_features.csv')
	'''
	a=str(ans).split()
	if int(a[1])==0:
		tkMessageBox.showinfo( "PWD Result","The URL ->"+url+" is Good")
	elif int(a[1])==1:
		tkMessageBox.showinfo( "PWD Result","The URL ->"+url+" is Malicious")
	else:
		tkMessageBox.showinfo( "PWD Result","The URL ->"+url+" is Malware")
	'''
B1 = Button(bottomframe1, text ="Check!", command = submitCallBack, bg = "#d1d6d6", font=("Cambria", 12), padx= 10, relief= RAISED )
B1.pack()
names = Label(bottomframe, text = "A project by - Arpit, Mukul, Nagarjun, Himanchal", fg = "grey", font=("Comic Sans MS", 8), bg = "#007777")
names.pack(side= BOTTOM)
root.configure(bg="#007777")
w = 800 # width for the Tk root
h = 350 # height for the Tk root

# get screen width and height
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

# calculate x and y coordinates for the Tk root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
#root.geometry('{}x{}'.format(800, 400))
root.wm_title("P W D - BTP Project")
#root.wm_overrideredirect(True)
#root.iconbitmap(r'.\detective-multi-size.ico')
root.mainloop()
