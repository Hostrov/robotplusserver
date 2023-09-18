import tkinter.ttk
import threading
import customtkinter
import chlisis

cc = chlisis.app4app()

class myappp(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.set_appearance_mode('dark')
        self.title("EF ARE SEE HILARIOUS")
        self.geometry("800x500")
        self.hh = tkinter.ttk.Style()
        self.phrame = customtkinter.CTkFrame()
        self.buttoun = customtkinter.CTkButton(text="start connection", command=self.the_dread_of_a_thread,
                                               fg_color='#6d4f7d', corner_radius=8, text_color="black",
                                               bg_color="#212325", hover_color='#3f055c').place(relx=0.8150, rely=0.93)

        self.recbutton = customtkinter.CTkButton(text="starrrt").place(rely=0.9, relx=0.2)

        self.label = customtkinter.CTkLabel(text='1')
        self.label.place(relx=0.4, rely=0.2)

        self.ipplabel = customtkinter.CTkLabel(text='connectoin form:', text_color='white', bg_color='#212325')
        self.ipplabel.grid(pady=100, padx=100)

        self.labvel = customtkinter.CTkLabel(text='idk')
        self.labvel.place(rely=0.1, relx=0.2)

    def deafthh(self):
        print("porrol")

    def re_fresh(self):
        teckst = cc.adderr
        numm = 0
        if cc.co is True:
            tekst = cc.labebel()
            uteckst = cc.daataa
            self.label.configure(text=tekst)
            self.labvel.configure(text=uteckst)
            if teckst is not None and numm < 1:
                self.ipplabel.configure(text=teckst)
                num = +1
            else:
                pass
        else:
            self.label.configure(text="N/A")

            print("client is no")

        self.after(500, self.re_fresh)

    def the_dread_of_a_thread(self):
        tread = threading.Thread(target=cc.start_connection)
        tread.start()


if __name__ == "__main__":
    root = myappp()
    root.after(500, root.re_fresh)
    print('@huhh?')
    root.mainloop()
