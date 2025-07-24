from tkinter import *
from tkinter import filedialog
import zipfile
import os
import shutil
window=Tk()
window.configure(padx=20,pady=20)
list_box=Listbox(window,width=50)
list_box.pack()
list_path=[]

# Add Button command
def add():
    global list_path
    file_path=filedialog.askopenfilename()
    list_path.append(file_path)
    file_name=os.path.basename(file_path)
    list_box.insert(END,file_name)

# clear Button Command
def clear():
    list_box.delete(0,END)
    file1 = input1.get()
    input1.delete(0,END)

# Compress Button Command
def compress():
    file1=input1.get()
    zip_file=zipfile.ZipFile(file1,'w')

    for path in list_path:
        file_name=os.path.basename(path)
        zip_file.write(path,arcname=file_name,compress_type=zipfile.ZIP_DEFLATED)
    zip_file.close()
    shutil.move(file1,f'C:\\Users\\aarav_qoo\\Downloads\\{file1}.zip')


# Add Button
button1 = Button(text="Add",command=add)
button1.pack(padx=10,pady=20,side='left')

# Compress Button
button2=Button(text="Compress",command=compress)
button2.pack(padx=60,pady=20,side='left')

# Clear Button
button3=Button(text="Clear",command=clear)
button3.pack(padx=20,pady=20,side='left')


# Input
input1=Entry()
input1.pack(pady=20)
input1.get()

window.mainloop()

