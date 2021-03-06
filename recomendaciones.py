import sys
import webbrowser
from random import choice,randint
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtWidgets import QLabel
from PyQt5.QtGui import QPixmap
import pandas as pd
import random


class recomendaciones(QMainWindow):
    def __init__(self):
        super().__init__()
        self.preferencia=[0,0,0]
        uic.loadUi("recomendaciones.ui",self)
        try:
            f = open('vector_preferencia.txt','r')
            self.preferencia=[]

            for dato in f.readlines()[-1].split(","):
                self.preferencia.append(int(dato))

            f.close()
            print("Puntos de cada eleccion")
            print("Comedia, Drama, Accion\n")
            print(self.preferencia)

        except:
            f = open('vector_preferencia.txt','a')
            f.write("{},{},{}\n".format(self.preferencia[0],self.preferencia[1],self.preferencia[2]))
            f.close()
            
            
        
        self.imgs_accion=["accion1.jpg","accion2.jpg","accion3.jpg","accion4.jpg"]
        self.imgs_drama=["drama1.jpg","drama2.jpg","drama3.jpg","drama4.jpg"]
        self.imgs_comedia=["comedia1.jpg","comedia2.jpg","comedia3.jpg","comedia4.jpg"]
        self.Accion.clicked.connect(self.accion)
        self.Drama.clicked.connect(self.drama)
        self.Comedia.clicked.connect(self.comedia)
        self.label
        self.reco.clicked.connect(self.recomendacion)
        self.opt=1
    
    def accion(self):
        self.contador(2,self.opt)
        imgs=[]
        imgs.append(randint(0,3))
        imgs.append(randint(0,3))
        imgs.append(randint(0,3))
        self.label.setText("Accion")


        while imgs[0] == imgs[1] or imgs[0] == imgs[2] or imgs[1] == imgs[2]:
            imgs=[]
            imgs.append(randint(0,3))
            imgs.append(randint(0,3))
            imgs.append(randint(0,3))


        pixmapImagen1=QPixmap(self.imgs_accion[imgs[0]]).scaled(161,161)
        pixmapImagen2=QPixmap(self.imgs_accion[imgs[1]]).scaled(161,161)
        pixmapImagen3=QPixmap(self.imgs_accion[imgs[2]]).scaled(161,161)

        


        
        self.img1.setPixmap(pixmapImagen1)
        self.img2.setPixmap(pixmapImagen2)
        self.img3.setPixmap(pixmapImagen3)
        self.opt=1
    
    def drama(self):
        self.contador(1,self.opt)

        imgs=[]
        imgs.append(randint(0,3))
        imgs.append(randint(0,3))
        imgs.append(randint(0,3))
        self.label.setText("Drama")
        

        while imgs[0] == imgs[1] or imgs[0] == imgs[2] or imgs[1] == imgs[2]:
            imgs=[]
            imgs.append(randint(0,3))
            imgs.append(randint(0,3))
            imgs.append(randint(0,3))



        pixmapImagen1=QPixmap(self.imgs_drama[imgs[0]]).scaled(161,161)
        pixmapImagen2=QPixmap(self.imgs_drama[imgs[1]]).scaled(161,161)
        pixmapImagen3=QPixmap(self.imgs_drama[imgs[2]]).scaled(161,161)


        self.img1.setPixmap(pixmapImagen1)
        self.img2.setPixmap(pixmapImagen2)
        self.img3.setPixmap(pixmapImagen3)

        self.opt=1

    def comedia(self):
        self.contador(0,self.opt)
        
        imgs=[]
        imgs.append(randint(0,3))
        imgs.append(randint(0,3))
        imgs.append(randint(0,3))
        self.label.setText("Comedia")

        while imgs[0] == imgs[1] or imgs[0] == imgs[2] or imgs[1] == imgs[2]:
            imgs=[]
            imgs.append(randint(0,3))
            imgs.append(randint(0,3))
            imgs.append(randint(0,3))


        pixmapImagen1=QPixmap(self.imgs_comedia[imgs[0]]).scaled(161,161)
        pixmapImagen2=QPixmap(self.imgs_comedia[imgs[1]]).scaled(161,161)
        pixmapImagen3=QPixmap(self.imgs_comedia[imgs[2]]).scaled(161,161)


        self.img1.setPixmap(pixmapImagen1)
        self.img2.setPixmap(pixmapImagen2)
        self.img3.setPixmap(pixmapImagen3)


        self.opt=1


    def contador(self,n,opt):
        if(opt):
            self.preferencia[n]=self.preferencia[n]+1
            f = open('vector_preferencia.txt','a')
            f.write("{},{},{}\n".format(self.preferencia[0],self.preferencia[1],self.preferencia[2]))
            f.close()
            print(self.preferencia)
        else:
            pass

    def recomendacion(self):
        self.opt=0
        if self.preferencia[0]>self.preferencia[1] and self.preferencia[0]>self.preferencia[2]:
            self.comedia()
        elif self.preferencia[1]>self.preferencia[0] and GUI.preferencia[1]>self.preferencia[2]:
            self.drama()
        elif self.preferencia[2]>self.preferencia[1] and self.preferencia[2]>self.preferencia[0]:
            self.accion()
        else:
            opcion=randint(0,2)
            if opcion==0:
                self.comedia()
            elif opcion==1:
                pass
                self.drama()
            else:
                self.accion()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = recomendaciones()
    GUI.show()
    GUI.recomendacion()

    
    sys.exit(app.exec_())

