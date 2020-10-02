import sys
import webbrowser
from random import choice,randint
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
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
    
    def accion(self):
        self.contador(2)
        imgs=[]
        imgs.append(randint(0,3))
        imgs.append(randint(0,3))
        imgs.append(randint(0,3))

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
    
    def drama(self):
        self.contador(1)

        imgs=[]
        imgs.append(randint(0,3))
        imgs.append(randint(0,3))
        imgs.append(randint(0,3))

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

    def comedia(self):
        self.contador(0)
        
        imgs=[]
        imgs.append(randint(0,3))
        imgs.append(randint(0,3))
        imgs.append(randint(0,3))

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


    def contador(self,n):
        self.preferencia[n]=self.preferencia[n]+1
        f = open('vector_preferencia.txt','a')
        f.write("{},{},{}\n".format(self.preferencia[0],self.preferencia[1],self.preferencia[2]))
        f.close()
        print(self.preferencia)


if __name__ == '__main__':
    print("hola mundo")
    app = QApplication(sys.argv)
    GUI = recomendaciones()
    GUI.show()
    if GUI.preferencia[0]>GUI.preferencia[1] and GUI.preferencia[0]>GUI.preferencia[2]:
        GUI.comedia()
    elif GUI.preferencia[1]>GUI.preferencia[0] and GUI.preferencia[1]>GUI.preferencia[2]:
        GUI.drama()
    elif GUI.preferencia[2]>GUI.preferencia[1] and GUI.preferencia[2]>GUI.preferencia[0]:
        GUI.accion()
    else:
        opcion=randint(0,2)
        if opcion==0:
            GUI.comedia()
        elif opcion==1:
            pass
            GUI.drama()
        else:
            GUI.accion()

    
    sys.exit(app.exec_())

