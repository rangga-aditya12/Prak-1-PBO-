# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 15:31:51 2024

@author: Rangga Aditya
"""

print('======Kalkulator Penjumlahan======')
class Penjumlahan:
    def penjumlahan (self):
        a1 = float(input('Masukan angka PERTAMA : '))
        a2 = float(input('Masukan angka KEDUA : '))        
        Total = a1 + a2
        print(f'Hasil penjumlahan = {Total}' )
    
Kalkulator = Penjumlahan()
Kalkulator.penjumlahan()
