
import sys
import sqlite3 as sql 
import os
from PyQt5 import QtWidgets
from Ui_Musteri import Ui_Musteri
from PyQt5.QtWidgets import QApplication,  QTableWidgetItem, QInputDialog

 

global mid, ad, soyad, marka, model, motor, hasar, sehir, fiyat, tarih
class Windows(QtWidgets.QMainWindow):

   def __init__(self):
      super().__init__()
      self.ui = Ui_Musteri()
      self.ui.setupUi(self) 

      self.Data()


      self.ui.tableWidget.clicked.connect(self.Input)
      self.ui.pushButton.clicked.connect(self.Save)
      self.ui.pushButton_2.clicked.connect(self.Delete)
      self.ui.pushButton_4.clicked.connect(self.Update)


   def Input(self):
      self.ui.lineEdit_10.setText(self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), 0).text()) 
      self.ui.lineEdit.setText(self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), 1).text())   
      self.ui.lineEdit_2.setText(self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), 2).text())   
      self.ui.lineEdit_3.setText(self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), 3).text())  
      self.ui.lineEdit_4.setText(self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), 4).text())         
      self.ui.lineEdit_5.setText(self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), 5).text())
      self.ui.lineEdit_6.setText(self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), 6).text())
      self.ui.lineEdit_7.setText(self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), 7).text())
      self.ui.lineEdit_8.setText(self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), 8).text())
      self.ui.lineEdit_9.setText(self.ui.tableWidget.item(self.ui.tableWidget.currentRow(), 9).text())
   



   def Data(self):
      self.ui.tableWidget.clear()
      self.ui.tableWidget.setColumnCount(10)
      self.ui.tableWidget.setHorizontalHeaderLabels(('Id','Ad', 'Soyad', 'Marka', 'Model', 'Motor', 'Hasar', 'Sehir', 'Fiyat', 'Tarih'))
      self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)

      db = sql.connect('Final/Arac_Otomasyon.db')
      cur =  db.cursor()
      sorgu= "Select * From  Musteri"
      cur.execute(sorgu)

      col = cur.fetchall()

      self.ui.tableWidget.setRowCount(len(col))

                        
      for index ,satir in enumerate(col):
         for index2,row in enumerate(satir):
          self.ui.tableWidget.setItem(index,index2,QTableWidgetItem(str(row)))
      

   def Clear(self):
      mid = self.ui.lineEdit_10.clear()
      ad = self.ui.lineEdit.clear()
      soyad = self.ui.lineEdit_2.clear()
      marka = self.ui.lineEdit_3.clear()
      model = self.ui.lineEdit_4.clear()
      motor = self.ui.lineEdit_5.clear()
      hasar = self.ui.lineEdit_6.clear()
      sehir = self.ui.lineEdit_7.clear()
      fiyat = self.ui.lineEdit_8.clear()
      tarih = self.ui.lineEdit_9.clear()

      

   def Save(self):
      mid = self.ui.lineEdit_10.text()
      ad = self.ui.lineEdit.text()
      soyad = self.ui.lineEdit_2.text()
      marka = self.ui.lineEdit_3.text()
      model = self.ui.lineEdit_4.text()
      motor = self.ui.lineEdit_5.text()
      hasar = self.ui.lineEdit_6.text()
      sehir = self.ui.lineEdit_7.text()
      fiyat = self.ui.lineEdit_8.text()
      tarih = self.ui.lineEdit_9.text()

      try:
         self.baglanti = sql.connect('Final/Arac_Otomasyon.db')
         self.save = self.baglanti.cursor()
         self.save.execute("insert into Musteri values(?,?,?,?,?,?,?,?,?,?)", (mid,ad,soyad,marka,model,motor,hasar,sehir,fiyat,tarih))
         self.baglanti.commit()
         self.save.close()
         self.baglanti.close()

         print("Kayıt Başaralı...")
      
      except Exception:
         print("Kayıt Başarısız...")

      self.Clear()
      self.Data()



   def Update(self):
      mid = self.ui.lineEdit_10.text()
      ad = self.ui.lineEdit.text()
      soyad = self.ui.lineEdit_2.text()
      marka = self.ui.lineEdit_3.text()
      model = self.ui.lineEdit_4.text()
      motor = self.ui.lineEdit_5.text()
      hasar = self.ui.lineEdit_6.text()
      sehir = self.ui.lineEdit_7.text()
      fiyat = self.ui.lineEdit_8.text()
      tarih = self.ui.lineEdit_9.text()

      try:
         self.baglanti = sql.connect('Final/Arac_Otomasyon.db')
         self.save = self.baglanti.cursor()
         self.save.execute("update Musteri set mid = ?, ad = ? , soyad = ?, marka_id = ?, model_id = ?, motor_id = ?, hasar_id = ?, sehir_id = ?, fiyat = ?, tarih=? where mid = ?",
         (mid,ad,soyad,marka,model,motor,hasar,sehir,fiyat,tarih,mid))
         self.baglanti.commit()
         self.save.close()
         self.baglanti.close()

         print("Güncelleme Başaralı...")
      
      except Exception:
         print("Güncelleme Başarısız...")
      
      self.Clear()
      self.Data()


   def Delete(self):

      mid = self.ui.lineEdit_10.text()

      try: 
             
            self.baglanti=sql.connect("Final/Arac_Otomasyon.db")
            self.u=self.baglanti.cursor()
            self.u.execute("Delete from  Musteri where mid= ?",(mid,))
            self.baglanti.commit()
            self.u.close()
            self.baglanti.close()
            print('Kayıt Silindi...')

      except Exception :
            print('Kayıt Silenemedi...')

      self.Clear()   
      self.Data()

        
app = QApplication(sys.argv)
win = Windows()
win.show()
sys.exit(app.exec_())
        

        
       
