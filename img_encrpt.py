from tkinter import *
from tkinter import filedialog

root=Tk()
root.geometry("300x300")

def encrypt_image():
    file1=filedialog.askopenfile(mode='r', filetypes=[('jpg file', '*.jpg'),('pngg file', '*.png')])
    if file1 is not None:
        file_name=file1.name
        key=entry1.get(1.0,END)
        print(file_name,key)
        fi=open(file_name,'rb')
        image=fi.read()
        fi.close()
        image=bytearray(image)
        for index,values in enumerate(image):
            image[index]=values^int(key)
        fi1=open(file_name,'wb')
        fi1.write(image)
        fi1.close()
        
b1=Button(root,text="encrypt/decrypt",command=encrypt_image , height=1, width=15 )
b1.place(x=110,y=90)

print("key:")
entry1=Text(root,height=1,width=15)
entry1.place(x=110,y=130)

root,mainloop()
        