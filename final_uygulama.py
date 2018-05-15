from tkinter import *
from tkinter import messagebox
import random
from time import sleep

class Simon_Game:
    def __init__(self):
        self.__pencere=Tk()
        self.__etiket=self.__pencere.title("Simon Oyunu")
        self.__pencere.geometry("300x450")  
        self.__pencere.resizable(False, False)  ## pencerenin yeniden boyutlanamsına izin vermiyoruz. bunu silerken default olarak true oluyorlar zaten. 

        self.__pc_Secimi=[]
        self.__kullanıcı_Secimi=[]
        self.__renkler=["red","blue","yellow","green"]
        self.__renkMethods = {"red" : self.red, "blue": self.blue, "green" : self.green, "yellow" : self.yellow}  ##bu sözlük yapısıdır.

        self.__buton1 = Button(self.__pencere, text="Yeşil", height=10, width=20, bg="green", activebackground="green", state=DISABLED, command=self.doldur1)
        self.__buton1.grid(row=1, column=0)

        self.__buton2=Button(self.__pencere,text="Sarı", height=10, width=20,bg="yellow", activebackground="yellow",state=DISABLED, command=self.doldur2)
        self.__buton2.grid(row=1,column=1)

        self.__buton3=Button(self.__pencere,text="Mavi", height=10, width=20,bg="blue", activebackground="blue" ,state=DISABLED, command=self.doldur3)
        self.__buton3.grid(row=2,column=0)

        self.__buton4=Button(self.__pencere,text="Kırmızı",height=10,width=20,bg="red", activebackground="red", state=DISABLED, command=self.doldur4)
        self.__buton4.grid(row=2,column=1)
        
        self.__seviye=1


        self.__strvar2 = StringVar()
        ## Cümle girişi. StringVar kısımları label lara atanır textvariable=... kısmı ile. 
        
        self.__buton5=Button(self.__pencere,text="Oyuna Başla",command=self.başla)
        self.__buton5.grid(row=3,column=0)
        self.__buton7=Button(self.__pencere,text="Kontrol Et", state=DISABLED, command=self.kontrol)
        self.__buton7.grid(row=3,column=1)
        self.__buton8=Button(self.__pencere, text="Devam Et", state=DISABLED, command=self.devam_et)
        self.__buton8.grid(row=4, column=1)


        self.__labelSeviye = Label(self.__pencere, textvariable=self.__strvar2)
        self.__labelSeviye.grid(row=4, column=0)
        self.__labelSeviye.grid_remove()

        self.__pencere.mainloop()


    def devam_et(self):
        self.__strvar2.set("Güncel Seviye = "+str(self.__seviye))
        for i in range(self.__seviye):
            self.__renk = random.choice(self.__renkler)
            self.__pc_Secimi.append(self.__renk)
            self.__renkMethods[self.__renk]()
            ## tekrar tekrar seçimyap ve göster yerine for döngüsü kullanmak çok daha kullanışlıdır. tek satırlık işlemler için ayrı fonksiyon yazmaya gerek yok. yuakrda sözlük yapısı buralarda kulanılıyor.
            ## seçilen rengin isminden direkt fonksiyona erişmek için. bu olmasa 4 tane if ekleyecektik.

        self.__buton7.config(state=NORMAL)
        self.__buton8.config(state=DISABLED)
        self.__buton1.config(state=NORMAL)
        self.__buton2.config(state=NORMAL)
        self.__buton3.config(state=NORMAL)
        self.__buton4.config(state=NORMAL)
        ## default ayarı NORMAL. basılmaması gerekirken butonları DISABLE ediyorum zamanı gelince açıyorum.

        self.__strvar2.set("Güncel Seviye = "+str(self.__seviye))

    def doldur1(self):
        self.__kullanıcı_Secimi.append("green")

    def doldur2(self):
        self.__kullanıcı_Secimi.append("yellow")

    def doldur3(self):
        self.__kullanıcı_Secimi.append("blue")

    def doldur4(self):
        self.__kullanıcı_Secimi.append("red")


    def green(self):

        self.__buton1.configure(bg="white")
        self.__buton1.after(100, lambda: self.__buton1.configure(bg="green"))
        #lambda tanımlamayı tek satırda yapmamızı sağlar
        self.__pencere.update()
        sleep(0.5)
        self.__buton1.configure(bg="green")
        self.__pencere.update()
        sleep(0.5)

    def yellow(self):

        self.__buton2.configure(bg="white")
        self.__buton2.after(100, lambda: self.__buton2.configure(bg="yellow"))
        self.__pencere.update()
        sleep(0.5)
        self.__buton2.configure(bg="yellow")
        self.__pencere.update()
        sleep(0.5)

    def blue(self):

        self.__buton3.configure(bg="white")
        self.__buton3.after(100, lambda: self.__buton3.configure(bg="blue"))
        self.__pencere.update()
        sleep(0.5)
        self.__buton3.configure(bg="blue")
        self.__pencere.update()
        sleep(0.5)

    def red(self):

        self.__buton4.configure(bg="white")
        self.__buton4.after(100, lambda: self.__buton4.configure(bg="red"))
        self.__pencere.update()
        sleep(0.5)
        self.__buton4.configure(bg="red")
        self.__pencere.update()
        sleep(0.5)

    def başla(self):  ## başla kısmı ayrı devam et kısmı ayrı fonksiyonları çalıştırıyor. 
        self.__pc_Secimi.clear()
        self.__kullanıcı_Secimi.clear()
        self.__seviye=1
        

        self.__strvar2.set("Güncel Seviye = "+str(self.__seviye))
        self.__labelSeviye.grid()
        self.__buton5.config(text="Oyunu Bitir")
        self.__buton5.config(command=self.yeniden_basla_kontrol)

        for i in range(self.__seviye):
            self.__renk = random.choice(self.__renkler)
            self.__pc_Secimi.append(self.__renk)
            self.__renkMethods[self.__renk]()

        self.__buton7.config(state=NORMAL)
        self.__buton1.config(state=NORMAL)
        self.__buton2.config(state=NORMAL)
        self.__buton3.config(state=NORMAL)
        self.__buton4.config(state=NORMAL)
        #oyuna başla ve kontrol et butonlarını yapmadık
        
    def yeniden_basla_kontrol(self):
        ## oyuna başlayınca oyuna basla butonu oyunu bitir e dönüşüyor. ve bu fonksyona bağlıyor.
        answer = messagebox.askyesno("Emin misiniz?","Oyun Hala Devam Ediyor. Yeniden başlamak istediğinize emin misiniz?")  ## ekerana uyarı vermesini sağlayan yapı. evet e basarsak True döndürür.
        if answer:                                                                                                           ## hayır a basarsak False Döndürür.  yani return eder. buna göre de o an oyunu bitirip ilk haline 
            self.__pc_Secimi.clear()                                                                                         ## dönüştürebiliriz.
            self.__kullanıcı_Secimi.clear()
            self.__seviye=1
            self.__buton7.config(state=DISABLED)
            self.__buton8.config(state=DISABLED)
            self.__buton1.config(state=DISABLED)
            self.__buton2.config(state=DISABLED)
            self.__buton3.config(state=DISABLED)
            self.__buton4.config(state=DISABLED)

            self.__labelSeviye.grid_remove()   ##  grid edilen label ları o an göstermek istemiyorsam grid_remowe ediyorum.
            self.__buton5.config(text="Oyuna Başla")
            self.__buton5.config(command=self.başla)

    def kontrol(self):           
        if self.__kullanıcı_Secimi==self.__pc_Secimi:
            self.__buton8.config(state=NORMAL)
            self.__buton7.config(state=DISABLED)
            self.__buton1.config(state=DISABLED)
            self.__buton2.config(state=DISABLED)
            self.__buton3.config(state=DISABLED)
            self.__buton4.config(state=DISABLED)

            self.__seviye+=1
            messagebox.showinfo("Tebrikler", "Tebrikler! Doğru bildiniz. Sonraki seviyeye geçebilirsiniz.")
        else:
            self.__seviye=1
            self.__buton7.config(state=DISABLED)
            self.__buton8.config(state=DISABLED)
            self.__labelİpucu.grid_remove()
            self.__labelSeviye.grid_remove()
            self.__buton5.config(command=self.başla)
            self.__buton5.config(text="Oyuna Başla")
            messagebox.showerror("Olmadı", "Yanlış seçim yaptınız. Oyun Bitti.")
        self.__kullanıcı_Secimi.clear()
        self.__pc_Secimi.clear()
        
        if self.__kullanıcı_Secimi==self.__pc_Secimi and self.__seviye>5:
            self.__pc_Secimi.clear()
            self.__kullanıcı_Secimi.clear()
            self.__seviye=1
            self.__buton7.config(state=DISABLED)
            self.__buton8.config(state=DISABLED)
            self.__buton1.config(state=NORMAL)
            self.__buton2.config(state=NORMAL)
            self.__buton3.config(state=NORMAL)
            self.__buton4.config(state=NORMAL)

            self.__labelSeviye.grid_remove()
            self.__buton5.config(text="Oyuna Başla")
            messagebox.showinfo("Tebrikler", "Tebrikler! Tüm seviyeleri geçtiniz. Oyuna tekrar başlayabilirsiniz.")
        

start = Simon_Game()
