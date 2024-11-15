from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO

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
    img = load_image(url)
    if img:
        new_window = Toplevel()
        new_window.title('Картинка котика')
        new_window.geometry('600x500')
        label = Label(new_window, image = img)
        label.pack()
        label.image = img

def exit():
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
file_menu.add_command(label = 'Выход', command = exit)

url = 'https://cataas.com/cat'

window.mainloop()
