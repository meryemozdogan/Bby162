from tkinter import Tk, Label, Button, LEFT, RIGHT
from PIL import Image, ImageTk

class album:

    def __init__(self, anaSayfa):

        global fotoIndexNo
        fotoIndexNo = 0

        self.anaSayfa = anaSayfa
        anaSayfa.title("National Geographic")
        self.etiket = Label (anaSayfa, text= "National Geographic")
        self.etiket.pack()

        self.ileripng = Image.open("ileri.png")
        self.ileriFoto =ImageTk.PhotoImage(self.ileripng)
        self.ileri = Button (anaSayfa, image =self.ileriFoto, command = self.fotoIleri)
        self.ileri.pack()
        self.ileri.pack(side=RIGHT)

        self.geripng = Image.open ("geri.png")
        self.geriFoto = ImageTk.PhotoImage(self.geripng)
        self.geri = Button (anaSayfa, image =self.geriFoto, command = self. fotoGeri)
        self.geri.pack()
        self.geri.pack(side= LEFT)


        self.goster(fotoIndexNo)

    def fotoGeri (self):
        global fotoIndexno
        if(fotoIndexno > 0):
            self.resim.destroy()
            fotoIndexno -=1
            self.goster(fotoIndexno)
        else:

            self.resim.destroy()
            fotoIndexno = 0
            self.goster(fotoIndexno)

    def goster (self, fotoIndex):
        listeFoto = ["foto1.jpg", "foto2.jpg", "foto3.jpg", "foto4.jpg"]

        global uzunluk
        uzunluk = len(listeFoto)
        self.foto = Image.open(listeFoto(fotoIndex))
        self.tkimage =ImageTk.PhotoImage(self.foto)
        self.resim = Label (root, image = self.tkimage)
        self.resim.pack()

root = Tk()
album = album(root)
root.mainloop()
