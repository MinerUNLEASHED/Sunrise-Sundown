import requests
import bs4
import tkinter as tk
from tkinter.font import Font
from PIL import Image, ImageTk

input_city_link = input('Input City From "timeanddate.com/sun/usa/...": ')
sun_res = requests.get(input_city_link)
soup = bs4.BeautifulSoup(sun_res.text, 'lxml')
for item in soup.select('.dn-mob'):
    sun_times = item.text
sun_times = sun_times.split('pm')
sun_times[0] += 'pm'

pre_image_items = []
for item in soup.select('div main article section div img'):
    pre_image_items += str(item)
img_url = "".join(pre_image_items[pre_image_items.index('c', (pre_image_items.index('/')+1)):(pre_image_items.index('g', pre_image_items.index('p')))+1])
img_url = requests.get('https://'+img_url)
given_image = open('../given_image.png', 'wb')
given_image.write(img_url.content)
given_image.close()

display_window = tk.Tk()
display_window.title('Weather App')
display_window.geometry('500x500')
text_font = Font(display_window, size=30)
time_text_font = Font(display_window, size=20)
app_frame = tk.Frame(master=display_window, width=400, height=400, bg='#34A2FE')
presized_image = Image.open('../given_image.png')
resized_image = presized_image.resize((400, 400))
input_image = ImageTk.PhotoImage(resized_image)
image_label = tk.Label(app_frame, image=input_image, height=400, background='#34A2FE')
sunrise_sunset_label = tk.Label(app_frame, text=f'{sun_times[0]}', bg='#34A2FE', fg='white', font=text_font)
time_label = tk.Label(app_frame, text=f'{sun_times[1]}', bg='#34A2FE', fg='white', font=time_text_font)
image_label.pack()
sunrise_sunset_label.pack()
time_label.pack()
app_frame.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
display_window.mainloop()
