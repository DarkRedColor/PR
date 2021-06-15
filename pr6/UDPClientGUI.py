from socket import *
from tkinter import *
from tkinter import filedialog
import threading
import time



# My girly things
color_white = '#f8f5f1'
color_txt_fld = '#525252'
color_btn = '#414141'
color_bg = '#313131'
color_active = '#ca3e47'

font = ("Cascadia Code PL", 10, "bold")

def callback():
	root.quit()

def get_host():
    pass
    host = adrEntry.get()
    #print(host)
    return host

def get_filename():
    filename = feEntry.get()
    #print(filename)
    return filename


def send():
    s = socket(AF_INET,SOCK_DGRAM)
    host = get_host()
    host = host.encode()
    port = 9999
    buf = 1024
    addr = (host,port)

    file_name= get_filename()
    file_name = file_name.encode()

    s.sendto(file_name,addr)

    f=open(file_name,"rb")
    data = f.read(buf)
    ##print(data)
    while (data):
        if(s.sendto(data,addr)):
            lolzLabel.configure(text=f"Sending {file_name} ...")
            data = f.read(buf)
    s.close()
    f.close()
    time.sleep(5)
    lolzLabel.configure(text='')


def get():
    host="0.0.0.0"
    port = 9999
    s = socket(AF_INET,SOCK_DGRAM)
    s.bind((host,port))

    addr = (host,port)
    buf=1024

    data,addr = s.recvfrom(buf)
    #print("Received File:", data.strip())
    lolzLabel.configure(text=f"File {data.strip()} Downloaded")
    f = open(data.strip(),'wb')

    data,addr = s.recvfrom(buf)
    try:
        while(data):
            f.write(data)
            s.settimeout(2)
            data,addr = s.recvfrom(buf)
    except timeout:
        f.close()
        s.close()
        time.sleep(5)
        lolzLabel.configure(text='')

def browseFiles():
    filename = filedialog.askopenfilename()
    # Change label contents
    feEntry.delete(0, END)
    feEntry.insert(0, filename)


root = Tk()
root.title("The coolest UDP Client thing ever")
root.protocol("WM_DELETE_WINDOW", callback)
root.configure(bg=color_bg)
# Adress Label
adrLabel = Label(root, font= font, bg = color_bg, fg = color_white, text="Enter your destination :")
adrLabel.grid(row=0, column=0, pady=5, sticky="w")
# Adress Entry
adrEntry = Entry(root, bg=color_txt_fld, width=40, font=font, fg=color_white)
adrEntry.grid(row=1, column=0)
# File Explorer label
feLabel = Label(root, font= font, bg = color_bg, fg = color_white, text="Select a file to send :")
feLabel.grid(row=2, column=0, pady=5, sticky="w")
# File Explorer Entry
feEntry = Entry(root, bg=color_txt_fld, width=40, font=font, fg=color_white)
feEntry.grid(row=3, column=0)
# File Explorer Button
feBtn = Button(root, text = "Browse", command = browseFiles, font = font, bg = color_btn, activebackground=color_active, fg = color_white)
feBtn.grid(row=3, column=1, padx=5)
# Send Button
sendBtn = Button(root, text = "Send", command = lambda: threading.Thread(target=send).start(), font = font, bg = color_btn, activebackground=color_active, fg = color_white, width=20)
sendBtn.grid(row=4, column=0, padx=5, pady=5, sticky="w")
# Recive Button
getBtn = Button(root, text = "Recive", command = lambda: threading.Thread(target=get).start(), font = font, bg = color_btn, activebackground=color_active, fg = color_white, width=20)
getBtn.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky="e")

lolzLabel = Label(root, font= font, bg = color_active, fg = color_white, text=" ", width=50)
lolzLabel.grid(row=99, column=0, columnspan=99)
root.mainloop()
