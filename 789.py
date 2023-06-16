
import os   
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

import sys
import datetime
import note 
 

root = Tk()                #окно
root.title("ЗАМЕТКИ")      #заголовок
root.geometry("400x400")   #размер окна



f_text = Frame(root)# Создание Frame
f_text.pack(fill=BOTH, expand=1)# Расположение виджета Frame в окне

text_fild = Text(f_text,
                 bg='grey',
                 fg='white',
                 padx=10,
                 pady=10,
                 wrap=WORD,
                 insertbackground='black',
                 selectbackground='#8D917A',
                 spacing3=10,
                 width=30,
                 font='Arial 14 bold'
                 )
text_fild.pack(expand=1, fill=BOTH, side=LEFT)


def new_file():         # Создать новый файл
       root.title
       file = None
       text_fild.delete(1.0,END)

def open_file():        # Открыть файл
    file_path = askopenfilename(title='Выбор файла', filetypes=(('Текстовые документы (*.txt)', '*.txt'), ('Все файлы', '*.*')))
    if file_path:
        text_fild.delete('1.0', END)
        text_fild.insert('1.0', open(file_path, encoding='utf-8').read())
      
def save_file():        # Сохранить файл
    file_path = asksaveasfilename(filetypes=(('Текстовые документы (*.txt)', '*.txt'), ('Все файлы', '*.*')))
    f = open(file_path, 'w', encoding='utf-8')
    text = text_fild.get('1.0', END)   
    f.write(text)
    f.close()
    def quitApplication():
        Tk.destroy()
        exit()


def notes_exit():        # Выход из приложения
    answer = askokcancel('Выход', 'Вы точно хотите выйти?')
    if answer:
        root.destroy()  


# Изменение тем
# def chenge_theme(theme):
#     text_fild['bg'] = view_colors[theme]['text_bg']
#     text_fild['fg'] = view_colors[theme]['text_fg']
#     text_fild['insertbackground'] = view_colors[theme]['cursor']
#     text_fild['selectbackground'] = view_colors[theme]['select_bg']

# Изменение шрифтов
# def chenge_fonts(fontss):
#     text_fild['font'] = fonts[fontss]['font']        

# def background():             # Изменение фона заметки
#     text_fild['bg'] = view_colors[theme]['text_bg']
#     text_fild['fg'] = view_colors[theme]['text_fg']
#     text_fild['insertbackground'] = view_colors[theme]['cursor']
#     text_fild['selectbackground'] = view_colors[theme]['select_bg']


#def chenge_fonts(fontss):       # Изменение шрифтов
 #   text_fild['font'] = fonts[fontss]['font'] 

#def delete_file():
    


 

# def show():
#     showinfo("Notes","Mrinal Verma")             


# Темы
# view_colors = {
#     'dark': {
#         'text_bg': 'black', 'text_fg': 'lime', 'cursor': 'brown', 'select_bg': '#8D917A'
#     },
#     'light': {
#         'text_bg': 'white', 'text_fg': 'black', 'cursor': '#A5A5A5', 'select_bg': '#FAEEDD'
#     }
# }

main_menu = Menu(root)   # Привязываем класс Menu к root

file_menu = Menu(main_menu, tearoff=0)

main_menu.add_cascade(label='Файл', menu=file_menu)   # Добавление вкладки Файл
file_menu.add_command(label='Новый', command = new_file)
file_menu.add_command(label='Открыть', command = open_file)
file_menu.add_command(label='Сохранить', command = save_file)
file_menu.add_command(label='Закрыть', command = notes_exit)
#file_menu.add_command(label='Удалить', command = delete_file)
#file_menu.add_command(label='Показать', command = show)


view_menu = Menu(main_menu, tearoff=0)
main_menu.add_cascade(label='Редактор', menu=view_menu)    # Добавление вкладки Редактор


view_menu_sub = Menu(view_menu, tearoff=0)

# view_menu_sub.add_command(label='Тёмная', command=chenge_theme)
# view_menu_sub.add_command(label='Светлая',command=chenge_theme)
# view_menu.add_cascade(label='Тема', menu=view_menu_sub)

# font_menu_sub = Menu(view_menu, tearoff=0)

# font_menu_sub.add_command(label='Arial')
# font_menu_sub.add_command(label='Comic Sans MS')
# font_menu_sub.add_command(label='Times New Roman')
# view_menu.add_cascade(label='Шрифт...', menu=font_menu_sub)
#view_menu.add_command(label='Изменить шрифт', command = chenge_fonts)
#view_menu.add_cascade(label='Фон', menu=view_menu)




# Темы
# view_colors = {
#     'dark': {
#         'text_bg': 'black', 'text_fg': 'lime', 'cursor': 'brown', 'select_bg': '#8D917A'
#     },
#     'light': {
#         'text_bg': 'white', 'text_fg': 'black', 'cursor': '#A5A5A5', 'select_bg': '#FAEEDD'
#     }
# }

root.config(menu=main_menu)

#title_name = Label(root, text="Новая заметка").pack()

button1 = Button(root,text='СОХРАНИТЬ', bg = 'Black',fg='White',command = save_file).place(x=150,y=300)     #кнопка

button2 = Button(root,text='НОВАЯ ЗАМЕТКА', bg = 'Black',fg='White',command=new_file).place(x=10,y=300)     #кнопка
#button3 = Button(root,text='НОВАЯ ЗАМЕТКА', bg = 'Black',fg='White',command=delete_file).place(x=190,y=300) #кнопка

# id_name = Label(root, text="ID").place(x=30,y=40)            
# id_entry = Entry(root, width=10)
# id_entry.place(x=50,y=40)

# text_data = QtWidgets.label()
# text_data.setText("Выберите дату")
# text_data.adjustSize()
# text_data.move(10,52)
# date_name = Label(root, text="Дата").place(x=400,y=40)            
# date_name = Entry(root, width=17)
# date_name.place(x=260,y=40)


root.mainloop()


 
 
# def __init__(self,**kwargs):
 
#         # Set icon
    
#         try:
#                root.wm_iconbitmap("Notepad.ico")
#         except:
#                 pass
 
#         # Set window size (the default is 300x300)
 
#         try:
#            Width = kwargs['width']
#         except KeyError:
#             pass
 
#         try:
#            Height = kwargs['height']
#         except KeyError:
#             pass
 
        


 

 
         

 




 
#     def __cut(self):
#        TextArea.event_generate("<<Cut>>")
 
#     def __copy(self):
#        TextArea.event_generate("<<Скопировать>>")
 
#     def __paste(self):
#        TextArea.event_generate("<<Copy>>")


    



# # title_name = Label(root, text="Заголовок").place(x=30,y=100)  #название заметки
# # title_name_entry = Entry(root, width=55)
# # title_name_entry.place(x=120,y=100)

# # note_text = Label(root, text="Заметка").place(x=30,y=230)     #текст заметки
# # note_text_entry = Text(root, width=55, height=10)
# # note_text_entry.place(x=120,y=150)








# Реализовать консольное приложение заметки, с +++сохранением, +++чтением,
# +++добавлением, редактированием и удалением заметок. Заметка должна
# содержать идентификатор, заголовок, тело заметки и дату/время создания или
# последнего изменения заметки. Сохранение заметок необходимо сделать в
# формате json или csv формат (разделение полей рекомендуется делать через
# точку с запятой). Реализацию пользовательского интерфейса студент может
# делать как ему удобнее, можно делать как параметры запуска программы
# (команда, данные), можно делать как запрос команды с консоли и
# последующим вводом данных, как-то ещё, на усмотрение студента.
 