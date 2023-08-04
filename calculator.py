import tkinter as tk

def add_numbers():
    num1=int(entry1.get())
    num2=int(entry2.get())
    result=num1 + num2
    label_result.config(text=f'Result:{result}')

def sub_numbers():
    num1=int(entry1.get())
    num2=int(entry2.get())
    result=num1 - num2
    label_result.config(text=f"Result:{result}")

def Divide_numbers():
    try:
        num1=int(entry1.get())
        num2=int(entry2.get())
        result=num1//num2
        label_result.config(text=f"Result:{result}")
    except Exception as e:
        label_result.config(text=f"Error of type: {type(e).__name__} occured. Try again.")


light_red = "#ffcccc"
light_green = '#90ee90'

window=tk.Tk()
window.title("calculator")

entry1=tk.Entry(window,width=20)
entry1.pack(padx=15,pady=5)
entry2=tk.Entry(window,width=20)
entry2.pack(padx=15,pady=5)

button_add=tk.Button(window,text="ADD",command=add_numbers,width=10,height=1,bg="blue",fg="white")
button_add.pack(padx=10,pady=5)


button_add.bind("<Enter>",lambda event:button_add.config(bg="lightblue"))
button_add.bind("<Leave>",lambda event:button_add.config(bg="blue"))


button_sub=tk.Button(window,text="SUB",command=sub_numbers,width=10,height=1,bg="red",fg="white")
button_sub.pack(padx=10,pady=5)


button_sub.bind("<Enter>",lambda event:button_sub.config(bg=light_red))
button_sub.bind("<Leave>",lambda event:button_sub.config(bg="red"))

button_divide=tk.Button(window,text="DIV",command=Divide_numbers,width=10,height=1,bg="green",fg="white")
button_divide.pack(padx=10,pady=5)

button_divide.bind("<Enter>",lambda event:button_divide.config(bg=light_green))
button_divide.bind("<Leave>",lambda event:button_divide.config(bg="green"))

label_result=tk.Label(window,text="Result:  ")
label_result.pack(padx=5,pady=2)

window.geometry("400x400")
window.mainloop()

