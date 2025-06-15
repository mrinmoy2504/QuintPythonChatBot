from tkinter import * 
from main_code import chat_with_ai 
BG_col = "#0F151A"
graycol = "#8693D1"
textcol = "#E2E3E3"


class ChatApp:

    def __init__(self):
        self.window = Tk()
        self.setup_win()

    def run(self):
        self.window.mainloop()

    def setup_win(self):
        self.window.title("Quint")
        self.window.resizable(width=True , height=True)
        self.window.configure(width=600,height=700, bg=BG_col)

        #headlabel
        head_label = Label(self.window, bg =BG_col , fg = textcol, text = "Quint Chatbot"  ,font="Calibri 15", pady = 0)
        head_label.place(relwidth=1 , rely = 0.0001)
        label2 = Label(self.window, bg =BG_col , fg = textcol, text = "Powered by: Meta Llama // Made by : Mrinmoy Sarker"  ,font="Calibri 8", pady = 5)
        label2.place(relwidth=0.5  , rely= 0.03 , relx = 0.52 )
        
        #divider 
        line = Label(self.window ,bg = graycol )
        line.place(relwidth=1 , rely= 0.06 , relheight= 0.005)

        #text_widget
        self.text_widget = Text(self.window , width=20 , height=2 , bg=BG_col , fg = textcol , 
                                padx=5 , pady=5 , bd=0 , font="Calibri 14" )
        self.text_widget.place(relheight=0.83 , relwidth=1 , rely=0.07)
        self.text_widget.configure(cursor="arrow" , state= DISABLED)

        #scroll
        scroll = Scrollbar(self.text_widget)
        scroll.place(relheight=1 , relx=0.99)
        scroll.configure(command = self.text_widget.yview) 

        #chatbox label 
        down_label = Label(self.window, bg ="#171C2A"  )
        down_label.place( relheight=0.108 , relwidth=1 , rely=0.892)

        #msg entry box
        self.msg_entry = Entry(down_label , bg = "#8693D1" , font="Calibri 10")
        self.msg_entry.place(relwidth=0.8 , relheight = 0.75 , rely= 0.12 , relx= 0.009)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>" , self.press_enter) 

        #send button
        send_button = Button(down_label, text="Send" , font= "Calibri 15 bold"  , bg="#3D8E8E" , activebackground="#3E6262",
                             command=lambda: self.press_enter(None))
        send_button.place(relx = 0.84 , rely = 0.15 , relheight=0.7 , relwidth= 0.15 )


    def press_enter(self , event):
        msg = self.msg_entry.get()
        self.inter_msg(msg,"You ")

    def inter_msg(self , msg , sender):
        if not msg:
            return
        
        self.msg_entry.delete(0,END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)

        msg2 = f"Quint:  {chat_with_ai(msg)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)


if __name__ == "__main__":
    app = ChatApp()
    app.run()

 