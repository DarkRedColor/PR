from threading import *
import tkinter as tk
import http.client
import requests
import urllib
import re


proxies = {
    "http" : "http://118.140.160.84:80"
}
data ={'key':'value'}


# Get Request
def get_request(URL):
    cookie = str(cookie_entry.get())
    cookies = dict(My_cookie=cookie)
    req = requests.get(URL, cookies=cookies, proxies=proxies)
    # print(req.text)
    links = re.findall(r'href=\"(https://.*?)\"', req.text)
    response_textbox.delete("1.0", tk.END)
    response_textbox.insert(tk.END, 'GET request send!\n')
    for link in links:
        print(link)
        response_textbox.insert(tk.END, str(link)+'\n')
        


# Post Request
def post_request(URL):
    values = {'key1':'value1', 'key2':'value2'}
    print(URL[8:])
    conn = http.client.HTTPSConnection(URL[8:])
    conn.request('POST', '/', str(values), {'Content-Type': 'application/json'})
    response_textbox.delete("1.0", tk.END)
    response_textbox.insert(tk.END, 'POST request send!\n')

# Head Request
def head_request(URL):
    r = requests.head(URL, data=data)
    # check status code for response recieved
    # success code - 200
    print(r)
    # print headers of request
    print(r.headers)
    response_textbox.delete("1.0", tk.END)
    response_textbox.insert(tk.END, str(r.headers)+'\n')


def options_request(URL):
    response = requests.options(URL)
    print(response.headers)
    response_textbox.delete("1.0", tk.END)
    response_textbox.insert(tk.END, str(response.headers)+'\n')


def start_thread(nr):
    URL = str(url_entry.get())
    if nr == 1:
        Thread(target=get_request, args=(URL, )).start()
    elif nr == 2:
        Thread(target=post_request, args=(URL, )).start()
    elif nr == 3:
        Thread(target=head_request, args=(URL, )).start() 
    elif nr == 4:
        Thread(target=options_request, args=(URL, )).start()
    else:
        print("Something wrong!")


# Window Size
width = 700
height = 500
# Background-color
bg_color = '#a8c779'
# Initiate main window
root = tk.Tk()
canvas = tk.Canvas(root, height=height, width=width, bg=bg_color)
canvas.grid(columnspan=4, rowspan=5)
# Title
title = 'Request Generator'
root.title(title)
# Window icon
photo = tk.PhotoImage(file='icon.png')
root.iconphoto(False, photo)
# Text Font
base_font = 'Raleway'

# Main Window Widgets:

# URL Label & Entry
url_label = tk.Label(root, text="URL:", background=bg_color, font=base_font)
url_label.grid(column=0, row=0)

url_entry = tk.Entry(root, font=base_font, width=50)
url_entry.grid(column=1, row=0, columnspan=3, stick='w')

# Cookies Label & Entry
cookie_label = tk.Label(root, text="Cookies:", background=bg_color, font=base_font)
cookie_label.grid(column=0, row=1)

cookie_entry = tk.Entry(root, font=base_font, width=50)
cookie_entry.grid(column=1, row=1, columnspan=3, stick='w')

#Hardcoded URL & Cookie
url_entry.insert(tk.END, 'https://enezdcp7ljqxe.x.pipedream.net')
# cookie_entry.insert(tk.END, "Even Santa Claus don't accept cookies without milk!")
cookie_entry.insert(tk.END, "Even Santa don't use cookies without milk!")

# Get Request Button
get_btn = tk.Button(root, text="GET", command=lambda: start_thread(1), font=base_font, width=10)
get_btn.grid(column=0, row=2)

# Post Request Button
post_btn = tk.Button(root, text="POST", command=lambda: start_thread(2), font=base_font, width=10)
post_btn.grid(column=1, row=2)

# Head Request Button
head_btn = tk.Button(root, text="HEAD", command=lambda: start_thread(3), font=base_font, width=10)
head_btn.grid(column=2, row=2)

# Options Request Button
options_btn = tk.Button(root, text="OPTIONS", command=lambda: start_thread(4), font=base_font, width=10)
options_btn.grid(column=3, row=2)

# Request responses Label & Textbox
response_title_label = tk.Label(root, text="Response:", background=bg_color, font=(base_font, 15))
response_title_label.grid(column=0, row=3, stick='s')

response_textbox = tk.Text(root, font=base_font, width=70, height=8, yscrollcommand=tk.Scrollbar(orient=tk.VERTICAL))
response_textbox.grid(column=0, row=4, columnspan=4, stick='n')

root.mainloop()