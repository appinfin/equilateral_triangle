from tkinter import *

ent_list=[]

def create_entry():
    'Функция создаёт 9 виджетов Entry'
    for i in range(1,4):
        ent= Entry(width=5)
        ent.grid(row=2, column=i, padx=5, pady=5)
        ent.insert(i,'0')
        ent_list.append(ent)
    for i in range(1,4):
        ent= Entry(width=5)
        ent.grid(row=3, column=i, padx=5, pady=5)
        ent.insert(i,'0')
        ent_list.append(ent)
    for i in range(1,4):
        ent= Entry(width=5)
        ent.grid(row=4, column=i, padx=5, pady=5)
        ent.insert(i,'0')
        ent_list.append(ent)
    print(ent_list)

def clear_label_err():
    label_err.grid_forget()
    
def check():
    if xyz[:3]==xyz[3:6] or xyz[:3]==xyz[6:9] or xyz[3:6]==xyz[6:9]:
        label_err['text']= "!!! Ошибка ввода !!!\n"\
                           "Вы ввели вершины с одинаковыми координатами"
        label_err.grid(row= 6, column= 0, columnspan= 4, pady=5)

def err_init(err):
    dict_err= {1: "Координата \'х\' вершины A",
               2: "Координата \'y\' вершины A",
               3: "Координата \'z\' вершины A",
               4: "Координата \'х\' вершины B",
               5: "Координата \'y\' вершины B",
               6: "Координата \'z\' вершины B",
               7: "Координата \'х\' вершины C",
               8: "Координата \'y\' вершины C",
               9: "Координата \'z\' вершины C",
              }
    label_err['text']= f"!!! Ошибка ввода !!! {dict_err[err]}"
    label_err.grid(row= 6, column= 0, columnspan= 4, pady=5)
    
def get_coordinates(event):
    clear_label_err()
    global xyz
    xyz=[]
    for i in range(0,9):
        try:
            xyz.append(round(float(ent_list[i].get()), 2))
            print(ent_list[i].get())
        except:
            err_init(i+1)
    check()

root = Tk()
root.title("Equilateral triangle")
root.geometry('400x200')

create_entry()

lable = Label(root, text='Введите координаты вершин треугольника ABC',\
              font='Arial 10 bold')
lable_x = Label(root, text='x', font='Arial 10')
lable_y = Label(root, text='y', font='Arial 10')
lable_z = Label(root, text='z', font='Arial 10')
lable_A = Label(root, text='A', font='Arial 10')
lable_B = Label(root, text='B', font='Arial 10')
lable_C = Label(root, text='C', font='Arial 10')
label_err= Label(root, font='Arial 10 bold', fg='red')
    
but = Button(root, text="рассчитать", font='Arial 10')

but.bind("<Button-1>", get_coordinates)
but.bind("<Return>", get_coordinates)


lable.grid(row=0, column=0, columnspan=4)
lable_x.grid(row=1, column=1)
lable_y.grid(row=1, column=2)
lable_z.grid(row=1, column=3)
lable_A.grid(row=2, column=0, sticky='e')
lable_B.grid(row=3, column=0, sticky='e')
lable_C.grid(row=4, column=0, sticky='e')
but.grid(row=5, column=0, columnspan=4, sticky='e')

root.mainloop()
