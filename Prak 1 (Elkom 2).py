# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 21:19:02 2024

@author: Rangga Aditya
"""

class Scanner:
    def rentan_nilai(self):
        
        nama = input("Masukkan Nama Anda : ")
        nilai = float(input("Masukkan Nilai Anda : "))
        nim = int(input("Masukkan Nim Anda : "))
        
        #Ketentuan Nilai Yang Ada 
        if nilai >= 80:
            grade = "A"
        
        elif nilai >= 77 and nilai <= 79.99:
            grade = "A-"
        
        elif nilai >= 74 and nilai <= 76.99:
            grade = "B+"
        
        elif nilai >= 68 and nilai <= 73.99:
            grade = "B"
        
        elif nilai >= 65 and nilai <= 67.99:
            grade = "B-"
             
        elif nilai >= 62 and nilai <= 64.99:
            grade = "C+"    
            
        elif nilai >= 56 and nilai <= 61.99:
            grade = "C"
           
        elif nilai >= 45 and nilai <= 55.99:
            grade = "D" 

        elif nilai >= 0.00 and nilai <= 44.99:
            grade = "E"        

        

        #Tampilan untuk user 
        print("--- DATA PRAKTIKUM PBO 2024 ---")
        print(f"Nama :{nama}")
        print(f"Nim  :{nim}")
        print(f"Mark = {grade}") 

           

#Pemanggilan fungsi 
scan = Scanner()
scan.rentan_nilai()  