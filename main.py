from tkinter import *
import smtplib, ssl
from tkinter import messagebox

win = Tk()
win.minsize(500,600)
win.title("Artin Email Sender")
win.iconbitmap("./logo.ico")
bg = "green"
fg = "white"
input_width = 40
win.configure(bg=f"{bg}")

def send():
    if message_input.get("1.0", "end-1c") and password_input.get() and sender_input.get() and reciver_input.get():
        def read_creds():
            user = sender_input.get()
            password = password_input.get()
            return user, password
        port = 465
        sender, password = read_creds()
        receiver = reciver_input.get()
        message = message_input.get("1.0", "end-1c")

        context = ssl.create_default_context()
        try:
            with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
                server.login(sender, password)
                server.sendmail(sender, receiver, message)
            messagebox.showinfo(title="Success", message="The email Sent")
        except Exception as e:
            messagebox.showerror(title="ERROR", message="An error occured")
        
        sender_input.delete(0,END)
        password_input.delete(0,END)
        reciver_input.delete(0,END)
        message_input.delete("1.0","end")
    else:
        messagebox.showerror(title="ERROR", message="fill out the form completely!")
        

from_label = Label(win, text="From: ", font=("None",20,"bold"), bg=f"{bg}", fg=f"{fg}")
from_label.pack()
sender_input = Entry(win,width=input_width, font=("None",12))
sender_input.pack()

passwrod_label = Label(win, text="Passwrod: ", font=("None",20,"bold"), bg=f"{bg}", fg=f"{fg}")
passwrod_label.pack(pady=(40,0))
password_input = Entry(win,width=input_width, font=("None",12), show="•")
password_input.pack()

to_label = Label(win, text="To: ", font=("None",20,"bold"), bg=f"{bg}", fg=f"{fg}")
to_label.pack(pady=(40,0))
reciver_input = Entry(win,width=input_width, font=("None",12))
reciver_input.pack()

message_label = Label(win, text="Message: ", font=("None",20,"bold"), bg=f"{bg}", fg=f"{fg}")
message_label.pack(pady=(40,0))
message_input = Text(win,width=input_width, height=9, font=("None",12))
message_input.pack()

send_btn = Button(win, text="Send Email", font=("None",16,"bold"), relief="flat",command=send)
send_btn.pack(pady=(30,0))

win.mainloop()