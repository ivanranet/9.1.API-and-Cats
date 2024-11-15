from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import requests
from io import BytesIO

alloved_tags = ['sleep', 'jump', 'fight', 'black', 'white', 'cats',
                'bengal', 'siamese', 'cute', 'little', 'fat']

def load_image(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        image_data = BytesIO(response.content)
        img_local = Image.open(image_data)
        img_local.thumbnail((600, 500), Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img_local)
    except Exception as e:
        print(f'Произошла ошибка: {e}')
        return  None

def open_new_window():
    tag = tag_combobox.get()
    url_tag = f'https://cataas.com/cat/{tag}' if tag else 'https://cataas.com/cat'
    img = load_image(url_tag)
    if img:
        new_window = Toplevel()
        new_window.title('Картинка котика')
        new_window.geometry('600x500')
        label = Label(new_window, image = img)
        label.pack()
        label.image = img

def exit_go():
    window.destroy()

window = Tk()
window.title('Cats!')
window.geometry('600x520')

menu_bar = Menu(window)
window.config(menu = menu_bar)

file_menu = Menu(menu_bar, tearoff = 0)
menu_bar.add_cascade(label = 'Файл', menu = file_menu)
file_menu.add_command(label = 'Загрузить фото', command = open_new_window)
file_menu.add_separator()
file_menu.add_command(label = 'Выход', command = exit_go)

url = 'https://cataas.com/cat'

tag_label = Label(text = 'Выберите тег')
tag_label.pack()

tag_combobox = ttk.Combobox(values = alloved_tags)
tag_combobox.pack()

load_button = Button(text = 'Загрузить фото', command = open_new_window)
load_button.pack()

window.mainloop()
