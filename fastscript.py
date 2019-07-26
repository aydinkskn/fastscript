#coding: utf-8
import os
import sys
import time
import webbrowser
import getpass
import subprocess

def print_banner():
    print("""
        ______           __  _____           _       __ 
       / ____/___ ______/ /_/ ___/__________(_)___  / /_
      / /_  / __ `/ ___/ __/\__ \/ ___/ ___/ / __ \/ __/
     / __/ / /_/ (__  ) /_ ___/ / /__/ /  / / /_/ / /_  
    /_/    \__,_/____/\__//____/\___/_/  /_/ .___/\__/  
                                          /_/

                                          Aydin Keskin
    """)

    print("\nHoşgeldiniz")

def account():
    while True:
        print("\n\n1-)Kullanıcı hesabı ekle\n2-)Kullanıcı hesabı sil\n3-)Kullanıcıları Listele\n4-)Geri")
        hesap=input("\nSeçim yapınız :")
        if hesap=="4":
            break
        elif hesap=="3":
            kullanicilar = subprocess.Popen(["net","user"])
            output,error = kullanicilar.communicate()
            print(output)

        elif hesap=="1":
            hesap_isim=input("Hesap adı :")
            hesap_grup=input("Standart User (U) veya Administrator (A)")
            while True:
                global hesap_parola
                num=0       #Parola rakam içermeli
                lower=0     #Parola küçük harf içermeli
                upper=0     #Parola büyük harf içermeli
                special=0   #Parola özel karakter içermeli
                hesap_parola=getpass.getpass('Parola :')
                #Parola en az 8 karakterli olmalı
                #Users için
                if hesap_grup=="u" or hesap_grup=="U":
                    if len(hesap_parola)<=7:
                        print("[!]Parola en az 8 karakterli olmalıdır")
                    else:
                        for i in hesap_parola:
                            if i.isdecimal():
                                num+=1
                            elif i.islower():
                                lower+=1
                            elif i.isupper():
                                upper+=1
                            else:
                                special+=1
                    if num and lower and upper and special:
                        hesap_parola_tekrar=getpass.getpass('Parola tekrar :')
                        if hesap_parola==hesap_parola_tekrar:
                            break
                        else:
                            print("[!]Parola eşleşmiyor. Tekrar deneyiniz\n")
                    else:
                        print("[!]Parola mutlaka rakam, küçük-büyük harf, özel karakter kombinasyonunu içermeli")
                        

                #Administrator için
                elif hesap_grup=="A" or hesap_grup=="a":
                    if len(hesap_parola)<=15:
                        print("[!]Parola en az 16 karakterli olmalıdır")
                    else:
                        for i in hesap_parola:
                            if i.isdecimal():
                                num+=1
                            elif i.islower():
                                lower+=1
                            elif i.isupper():
                                upper+=1
                            else:
                                special+=1
                    if num and lower and upper and special:
                        hesap_parola_tekrar=getpass.getpass('Parola tekrar :')
                        if hesap_parola==hesap_parola_tekrar:
                            break
                        else:
                            print("[!]Parola eşleşmiyor. Tekrar deneyiniz\n")
                    else:
                        print("[!]Parola mutlaka rakam, küçük-büyük harf, özel karakter kombinasyonunu içermeli")

            
            liste=[]
            komut="net user /add "
            liste.append(komut)
            liste.append(hesap_isim)
            liste.append(hesap_parola)
            bos=""
            bos+=liste[0]
            bos+=liste[1]
            bos+=" "
            bos+=liste[2]
            if hesap_grup=="u" or hesap_grup=="U":
                os.system(bos)
                time.sleep(2)
                #print("[+]Hesap başarılı şekilde eklendi.")
                #print("[+]{} kullanıcısı /users grubuna dahil edildi".format(hesap_isim))
            elif hesap_grup=="A" or hesap_grup=="a":
                os.system(bos)
                liste=[]
                komut="net localgroup administrators "
                liste.append(komut)
                liste.append(hesap_isim)
                liste.append(" /add")
                bos=""
                for i in liste:
                    bos+=i
                os.system(bos)
                liste.clear()
                komut="net localgroup users "
                liste.append(komut)
                liste.append(hesap_isim)
                liste.append(" /delete")
                bos=""
                for i in liste:
                    bos+=i
                os.system(bos)
                time.sleep(2)
                #print("[+]Hesap başarılı şekilde eklendi.")
                #print("[+]{} kullanıcısı /administrators grubuna dahil edildi".format(hesap_isim))
                #print("[+]{} kullanıcısı /users grubundan çıkarıldı".format(hesap_isim))
            else:
                print("[!]Administrator veya Users grubuna ekleyiniz...")
        elif hesap=="2":
            kullanicilar = subprocess.Popen(["net","user"])
            output,error = kullanicilar.communicate()
            print(output)
            
            hesap_isim2=input("Silinecek hesap :")
            liste=[]
            komut="net user /delete "
            liste.append(komut)
            liste.append(hesap_isim2)
            bos=""
            for i in liste:
                bos+=i
            os.system(bos)
            time.sleep(1)
            #print("[+]Hesap başarılı şekilde silindi.")

def win_update():
    time.sleep(1.5)
    os.system(r"reg add HKLM\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU")
    os.system(r"reg add HKLM\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU /v NoAutoUpdate /t reg_dword /d 0")
    os.system(r"reg add HKLM\SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU /v AUOptions /t reg_dword /d 2")
    
def adobe_update():
    time.sleep(1.5)
    os.system(r'reg add "HKLM\SOFTWARE\Policies\Adobe\Acrobat Reader\10.0\FeatureLockDown"')
    os.system(r'reg add "HKLM\SOFTWARE\Policies\Adobe\Acrobat Reader\10.0\FeatureLockDown" /v bUpdater /t reg_dword /d 00000000')

def tw_update():
    time.sleep(1.5)
    os.system(r'reg add "HKLM\SOFTWARE\TeamViewer" /v UpdateChannel /t reg_dword /d 0')


def main():
    print_banner()

    while True:
        print("""\n\n
        1-)Kullanıcı Hesaplarını Ayarla
        2-)Windows Auto-Update Disable
        3-)Adobe Flash Updater Disable
        4-)Team Viewer 12 İndir (doğrudan link)
        5-)Team Viewer 12 İndir (indirme sayfası)
        6-)Team Viewer Auto-Update Disable
        7-)Çıkış

        """)


        secim=input("Seçim yapınız :")

        if secim=="1":
            account()
        elif secim=="2":
            win_update()
        elif secim=="3":
            adobe_update()
        elif secim=="4":
            webbrowser.open_new_tab("https://dl.tvcdn.de/download/version_12x/TeamViewer_Setup.exe")
        elif secim=="5":
            webbrowser.open_new_tab("https://www.teamviewer.com/tr/download/previous-versions/")
        elif secim=="6":
            tw_update()
        elif secim=="7":
            print("Programı kullandığınız için teşekkürler")
            time.sleep(2)
            sys.exit()
        else:
            print("Doğru seçim yapınız...")

if __name__ == "__main__":
    main()
