from tkinter import *
from tkinter import ttk

Colors1 = "#000000" #
Colors2 = "#feffff" #
Colors3 = "#000000" #
Colors4 = "#feffff" #
Colors5 = "#ff0000" #

Windowwns=Tk()
Windowwns.title("Github.com/cassioestevao")
Windowwns.geometry("235x310")
Windowwns.config(bg=Colors1)

frame_tela = Frame(Windowwns,width=235, height=50, bg=Colors3)
frame_tela.grid(row=0, column=0)

frame_Extruct = Frame(Windowwns,width=235, height=268)
frame_Extruct.grid(row=1, column=0)

#Var_All_Valor
All_Valor = ''
Val_Text = StringVar()

#Fuctions
def Pull_Valor(event):
    
    global All_Valor
    
    All_Valor = All_Valor + str(event)
    
#Screen_Valor
    Val_Text.set(All_Valor)
    
    
#Function_Math
def Calculit():
    global All_Valor
    Result = eval(All_Valor)
    Val_Text.set(str(Result))
0
#Function_Clear
def Clear_Screen():
    global All_Valor
    All_Valor = ""
    Val_Text.set("")

#Create_Label
Val_Text =StringVar()

app_label = Label(frame_tela, textvariable=Val_Text, width=16, height=2, padx=7, relief=FLAT, anchor="e", justify=RIGHT, font=('Ivy 18'), bg=Colors3, fg=Colors2)
app_label.place(x=0,y=0)

#Buttons
b_1 = Button(frame_Extruct, command=Clear_Screen, text="C", width=11, height=2, bg=Colors4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=0, y=0)
b_2 = Button(frame_Extruct, command=lambda:Pull_Valor('%'), text="%", width=5, height=2, bg=Colors4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=118, y=0)
b_3 = Button(frame_Extruct, command=lambda:Pull_Valor('/'), text="/", width=5, height=2, bg=Colors5, fg=Colors2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=177, y=0)

b_4 = Button(frame_Extruct, command=lambda:Pull_Valor('7'), text="7", width=5, height=2, bg=Colors4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=0, y=52)
b_5 = Button(frame_Extruct, command=lambda:Pull_Valor('8'), text="8", width=5, height=2, bg=Colors4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=59, y=52)
b_6 = Button(frame_Extruct, command=lambda:Pull_Valor('9'), text="9", width=5, height=2, bg=Colors4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=118, y=52)
b_7 = Button(frame_Extruct, command=lambda:Pull_Valor('*'), text="*", width=5, height=2, bg=Colors5, fg=Colors2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=177, y=52)
 
b_8 = Button(frame_Extruct, command=lambda:Pull_Valor('4'), text="4", width=5, height=2, bg=Colors4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=0, y=104)
b_9 = Button(frame_Extruct, command=lambda:Pull_Valor('5'), text="5", width=5, height=2, bg=Colors4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=59, y=104)
b_10 = Button(frame_Extruct, command=lambda:Pull_Valor('6'), text="6", width=5, height=2, bg=Colors4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=118, y=104)
b_11 = Button(frame_Extruct, command=lambda:Pull_Valor('-'), text="-", width=5, height=2, bg=Colors5, fg=Colors2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=177, y=104)

b_12 = Button(frame_Extruct, command=lambda:Pull_Valor('1'), text="1", width=5, height=2, bg=Colors4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=0, y=156)
b_13 = Button(frame_Extruct, command=lambda:Pull_Valor('2'), text="2", width=5, height=2, bg=Colors4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=59, y=156)
b_14 = Button(frame_Extruct, command=lambda:Pull_Valor('3'), text="3", width=5, height=2, bg=Colors4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=118, y=156)
b_15 = Button(frame_Extruct, command=lambda:Pull_Valor('+'), text="+", width=5, height=2, bg=Colors5, fg=Colors2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=177, y=156)

b_16 = Button(frame_Extruct, command=lambda:Pull_Valor('0'), text="0", width=11, height=2, bg=Colors4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=0, y=208)
b_17 = Button(frame_Extruct, command=lambda:Pull_Valor('.'), text=".", width=5, height=2, bg=Colors4, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=118, y=208)
b_18 = Button(frame_Extruct, command=Calculit, text="=", width=5, height=2, bg=Colors5, fg=Colors2, font=('Ivy 13 bold'), relief=RAISED, overrelief=RIDGE) #LineCommand
b_18.place(x=177, y=208)

#Calling_the_function

Windowwns.mainloop()
