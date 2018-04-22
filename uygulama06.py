from tkinter import Tk, Label, Button, LEFT, RIGHT
import random

class uygulama1:
    def __init__(self, master):
        self.master = master
        master.title("Günün Şarkısı")
        master.configure(background="pink")

        self.label= Label (master, text= "Bugünün Şarkısı:", font="calibri 17 italic" , bg="pink" )
        self.label.pack()

        self.sec_button= Button (master, text= "Seç", font= "calibri 15 italic"  , command= self.sarki)
        self.sec_button.pack(side= LEFT)

        self.cık_button= Button (master, text= "Çık", font= "calibri 15 italic"  , command= master.quit)
        self.cık_button.pack(side= RIGHT)
    def sarki(self):
        sarkilar= ["Eleni Karaindrou - The Weeping Meadow","The Veils - Lavinia","Agnes Obel - Riverside", "Pixies - Where Is My Mind?" ,"Beirut - La Llorona", "Hindi Zahra - Beautiful Tango" ,"Fikret Kızılok - Razıyım","Yeni Türkü - Başka Türlü Bir Şey", "Sezen Aksu - Düş Bahçeleri", "Gülce Duru - My Woman"]
        secilenSarki = random.choice(sarkilar)
        self.song = Label (self.master, text=secilenSarki, font= "calibri 15 italic", bg="pink")
        self.song.pack()

root = Tk()
secilenSarki = uygulama1(root)
root.mainloop()
