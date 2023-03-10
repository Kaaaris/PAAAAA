import random
import getpass
import smtplib
import subprocess
import os

lower = "abcdefghijqlmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbol = "[]{}()*;/,._-"
all = lower + upper + numbers + symbol
length = 16
password = "".join(random.sample(all, length))
random_password = password
user = '2'
passw = '1'
add_mail = ''

all = numbers + lower 
length = 5
password = "".join(random.sample(all, length))
ramdome_code = password

print("1 Connexion\n2 Creation of an account")
sign = input('')
if sign == '1':
    user1 = input("Username: ")
    if user == user1:
        passw1 = getpass.getpass("Password: ") 
        if passw == passw1:
            print("Welcome in your favourite application")     
            print("Where do you want go?")
            print("1 Setting\n2 Application\n3 Game\n4 Document\n5 Quit")
            choice = input('')
if sign == '2':
        user = input("Entre a Username :")
        print("Do you want generate your password or you wright ? (y/n) :")
        pswuser = input('')
        if pswuser == "y":
           pswuser = random_password
           print("Your password is: ", pswuser)
        if sign == '2':
            passw = getpass.getpass("Entre your password: ")
            passw1 = getpass.getpass("For shur entre a second time your password:")
            print(passw)
            while passw != passw1 :
                print("Your password are not the same")
                print("Do you want re try? (y/n)")
                gui = input('')
                if gui == "y":
                    pswuser = getpass.getpass("Entre your password: ")
                    pswuser1 = getpass.getpass("For shur entre a second time your password:")
                else :
                    print("Your password is :", pswuser1)
                    break

    
            user1 = input("Username: ")
            if user1 == user :
                passw1 = input("Password :")
                if passw == passw1:
                    print("Welcome in your favourite application")
                    print("Where do you want go?")
                    print("1 Setting\n2 Application\n3 Game\n4 Document\n5 Quit")
                    choice = input('')
            else:
                print("You have a not the good username or password")
if choice == '1':
    print("Setting")
    print("1 Change my password\n2 Change my Username\n3 Connect an address mail\n4 Version")
    choice1 = input('')
    if choice1 == '1':
        passw1 = input("Tape your old password: ")
        if passw == passw1 :
            passw = input("Write your new pass word: ")
            passw1 = input("Write a seconde time your password for shure: ")
            if passw == passw1:
                print("Your password was been change")
                print("1 Setting\n2 Application\n3 Game\n4 Document\n5 Quit")
                choice = input('')
    if choice1 == '2':
        passw1 =input("Write your password a new Username: ")
        if passw1 == passw :
            user1 = input("Write your new Username: ")
            user = input("Second time please for shure: ")
            print("Your Username was been change")
            print("1 Setting\n2 Application\n3 Game\n4 Document\n5 Quit")
            choice = input('')
    if choice1 == '3':
        print("1 See my adresse e-mail\n2 Add a adresse e-mail")
        adresse_choice = input
        if adresse_choice == '1':
            print("Your adresse e-mail is ", add_mail)
            print("1 Setting\n2 Application\n3 Game\n4 Document\n5 Quit")
            choice = input('')
        if adresse_choice == '2':
            add_mail = input("Write your addresse e-mail: ")
            print("Your adresse e-mail is ", add_mail)
            print("Cheling your mail because a code at 5 chiffre for a confirmation")
            serveur_smtp = 'smtp.office365.com'
            port_smtp = 587
            utilisateur_smtp = 'the.verification.code@outlook.com'
            mot_de_passe_smtp = 'PaPa@free.fr'
            message = f"From: {'the.verification.code@outlook.com'}\nTo: {add_mail}\nSubject: {'CODE OF FERIVICATION'}\n\n This is the code of verification: {ramdome_code} thank to use PAAAA"
            try:
                smtpObj = smtplib.SMTP('smtp.office365.com', 587)
                smtpObj.starttls() # utiliser si la connexion doit être sécurisée
                smtpObj.login('the.verification.code@outlook.com', 'PaPa@free.fr')
                smtpObj.sendmail('the.verification.code@outlook.com', add_mail, message)
                smtpObj.quit()
                print("E-mail was send with sucess !")
                print("Checking your junk")
            except Exception as e:
                print("The email was not send :", e)
            code_amil = input("Entre the code at 5 chiffre: ")
            if ramdome_code == code_amil:
                print("Your adresse was connected")
                print("1 Setting\n2 Application\n3 Game\n4 Document\n5 Quit")
                choice = input('')
            if ramdome_code != code_amil:
                print("This is not the good code")
                print("Resend a mail? (y/n)")
                re_send = input('')
                if re_send == 'y' :
                    print("Cheling your mail because a code at 5 chiffre for a confirmation")
                    if ramdome_code != code_amil:
                        print("The code is not good")
                        print("1 Setting\n2 Application\n3 Game\n4 Document\n5 Quit")
                        choice = input('')
            serveur_smtp = 'smtp.office365.com'
            port_smtp = 587
            utilisateur_smtp = 'the.verification.code@outlook.com'
            mot_de_passe_smtp = 'PaPa@free.fr'
            message = f"From: {'the.verification.code@outlook.com'}\nTo: {add_mail}\nSubject: {'CODE OF FERIVICATION'}\n\n{'The code of verifiaction', ramdome_code, 'Thanks to use PAAAA'}"
            try:
                smtpObj = smtplib.SMTP('smtp.office365.com', 587)
                smtpObj.starttls() # utiliser si la connexion doit être sécurisée
                smtpObj.login('the.verification.code@outlook.com', 'PaPa@free.fr')
                smtpObj.sendmail('the.verification.code@outlook.com', add_mail, message)
                smtpObj.quit()
                print("E-mail was send with sucess !")
                print("Checking your junk")
            except Exception as e:
                print("The email was not send :", e)
            code_amil = input("Entre the code at 5 chiffre: ")
            if ramdome_code == code_amil:
                print("Your adresse was connected")
                if re_send == 'n' :
                    print("1 Setting\n2 Application\n3 Game\n4 Document\n5 Quit")
                    choice = input('')
    if choice1 == '4':
        print("The version of PAAA is the beta.")
        print("You can help us in my discord: ")
        print("Thank to use me")
        print("1 Setting\n2 Application\n3 Game\n4 Document")
        choice = input('')
if choice == '2':
    print("Welcome in your apllication")
    print("1 Note")
    choice2 = input('')
    if choice2 == '1':
        chemin_script = '/Users/kids/Desktop/Garis ps c mon dossier/PAAAA/todo.py'
        subprocess.call(['python', chemin_script])
        print("1 Setting\n2 Application\n3 Game\n4 Document\n5 Quit")
        choice = input('')
if choice == '3':
    print("What game do you wante play?")
    print("1 Snake")
    choice3 = input('')
    if choice3 == '1':
        chemin_script = '/Users/kids/Desktop/Garis ps c mon dossier/PAAAA/sabke.py'
        subprocess.call(['python', chemin_script])
        print("1 Setting\n2 Application\n3 Game\n4 Document\n5 Quit")
        choice = input('')
if choice == '4':
    print("Welcome in your documents")
    print("1 see my document\n2 import document")
    choice4 = input('')
    if choice4 == '1':
        print("This is your document")
        file = open('result_search.txt','r')
    if choice4 == '2':
        print("Document")
        print("1 Import document from your computer\n2 Import from One drive")
        document = input('')
        if document == '1':
            chemin_script = '/Users/kids/Desktop/Garis ps c mon dossier/PAAAA/fichier.py'
            subprocess.call(['python', chemin_script])  
    print("1 Setting\n2 Application\n3 Game\n4 Document\n5 Quit")
    choice= input('')
    if choice == '1':
        print("Setting")
        print("1 Change my password\n2 Change my Username\n3 Connect an address mail\n4 Version")
        choice1 = input('')
    if choice1 == '1':
        passw1 = input("Tape your old password: ")
        if passw == passw1 :
            passw = input("Write your new pass word: ")
            passw1 = input("Write a seconde time your password for shure: ")
            if passw == passw1:
                print("Your password was been change")
                print("1 Setting\n2 Application\n3 Game\n4 Document\n5 Quit")
                choice = input('')
    if choice1 == '2':
        passw1 =input("Write your password a new Username: ")
        if passw1 == passw :
            user1 = input("Write your new Username: ")
            user = input("Second time please for shure: ")
            print("Your Username was been change")
            print("1 Setting\n2 Application\n3 Game\n4 Document\n5 Quit")
            choice = input('')
    if choice1 == '3':
        print("1 See my adresse e-mail\n2 Add a adresse e-mail")
        adresse_choice = input
        if adresse_choice == '1':
            print("Your adresse e-mail is ", add_mail)
            print("1 Setting\n2 Application\n3 Game\n4 Document\n5 Quit")
            choice = input('')
        if adresse_choice == '2':
            add_mail = input("Write your addresse e-mail: ")
            print("Your adresse e-mail is ", add_mail)
            print("Cheling your mail because a code at 5 chiffre for a confirmation")
            serveur_smtp = 'smtp.office365.com'
            port_smtp = 587
            utilisateur_smtp = 'the.verification.code@outlook.com'
            mot_de_passe_smtp = 'PaPa@free.fr'
            message = f"From: {'the.verification.code@outlook.com'}\nTo: {add_mail}\nSubject: {'CODE OF FERIVICATION'}\n\n This is the code of verification: {ramdome_code} thank to use PAAAA"
            try:
                smtpObj = smtplib.SMTP('smtp.office365.com', 587)
                smtpObj.starttls() # utiliser si la connexion doit être sécurisée
                smtpObj.login('the.verification.code@outlook.com', 'PaPa@free.fr')
                smtpObj.sendmail('the.verification.code@outlook.com', add_mail, message)
                smtpObj.quit()
                print("E-mail was send with sucess !")
                print("Checking your junk")
            except Exception as e:
                print("The email was not send :", e)
            code_amil = input("Entre the code at 5 chiffre: ")
            if ramdome_code == code_amil:
                print("Your adresse was connected")
                print("1 Setting\n2 Application\n3 Game\n4 Document\n5 Quit")
                choice = input('')
            if ramdome_code != code_amil:
                print("This is not the good code")
                print("Resend a mail? (y/n)")
                re_send = input('')
                if re_send == 'y' :
                    print("Cheling your mail because a code at 5 chiffre for a confirmation")
                    if ramdome_code != code_amil:
                        print("The code is not good")
                        print("1 Setting\n2 Application\n3 Game\n4 Document\n5 Quit")
                        choice = input('')
            serveur_smtp = 'smtp.office365.com'
            port_smtp = 587
            utilisateur_smtp = 'the.verification.code@outlook.com'
            mot_de_passe_smtp = 'PaPa@free.fr'
            message = f"From: {'the.verification.code@outlook.com'}\nTo: {add_mail}\nSubject: {'CODE OF FERIVICATION'}\n\n{'The code of verifiaction', ramdome_code, 'Thanks to use PAAAA'}"
            try:
                smtpObj = smtplib.SMTP('smtp.office365.com', 587)
                smtpObj.starttls() # utiliser si la connexion doit être sécurisée
                smtpObj.login('the.verification.code@outlook.com', 'PaPa@free.fr')
                smtpObj.sendmail('the.verification.code@outlook.com', add_mail, message)
                smtpObj.quit()
                print("E-mail was send with sucess !")
                print("Checking your junk")
            except Exception as e:
                print("The email was not send :", e)
            code_amil = input("Entre the code at 5 chiffre: ")
            if ramdome_code == code_amil:
                print("Your adresse was connected")
                if re_send == 'n' :
                    print("1 Setting\n2 Application\n3 Game\n4 Document\n5 Quit")
                    choice = input('')
    if choice1 == '4':
        print("The version of PAAA is the beta.")
        print("You can help us in my discord: ")
        print("Thank to use me")
        print("1 Setting\n2 Application\n3 Game\n4 Document")
        choice = input('')
if choice == '2':
    print("Welcome in your apllication")
    print("1 Note")
    choice2 = input('')
    if choice2 == '1':
        chemin_script = '/Users/kids/Desktop/Garis ps c mon dossier/PAAAA/todo.py'
        subprocess.call(['python', chemin_script])
        print("1 Setting\n2 Application\n3 Game\n4 Document\n5 Quit")
        choice = input('')
if choice == '3':
    print("What game do you wante play?")
    print("1 Snake")
    choice3 = input('')
    if choice3 == '1':
        chemin_script = '/Users/kids/Desktop/Garis ps c mon dossier/PAAAA/sabke.py'
        subprocess.call(['python', chemin_script])
        print("1 Setting\n2 Application\n3 Game\n4 Document\n5 Quit")
        choice = input('')
if choice == '4':
    print("Welcome in your documents")
    print("1 see my document\n2 import document")
    choice4 = input('')
    if choice4 == '1':
        print("This is your document")
        file = open('result_search.txt','r')
    if choice4 == '2':
        print("Document")
        print("1 Import document from your computer\n2 Import from One drive")
        document = input('')
        if document == '1':
            chemin_script = '/Users/kids/Desktop/Garis ps c mon dossier/PAAAA/fichier.py'
            subprocess.call(['python', chemin_script])  
    print("1 Setting\n2 Application\n3 Game\n4 Document\n5 Quit")
    choice = input('')
if choice == '1':
    print("Setting")
    print("1 Change my password\n2 Change my Username\n3 Connect an address mail\n4 Version")
    choice1 = input('')
    if choice1 == '1':
        passw1 = input("Tape your old password: ")
        if passw == passw1 :
            passw = input("Write your new pass word: ")
            passw1 = input("Write a seconde time your password for shure: ")
            if passw == passw1:
                print("Your password was been change")
                print("1 Setting\n2 Application\n3 Game\n4 Document\n5 Quit")
                choice = input('')
    if choice1 == '2':
        passw1 =input("Write your password a new Username: ")
        if passw1 == passw :
            user1 = input("Write your new Username: ")
            user = input("Second time please for shure: ")
            print("Your Username was been change")
            print("1 Setting\n2 Application\n3 Game\n4 Document\n5 Quit")
            choice = input('')
    if choice1 == '3':
        print("1 See my adresse e-mail\n2 Add a adresse e-mail")
        adresse_choice = input
        if adresse_choice == '1':
            print("Your adresse e-mail is ", add_mail)
            print("1 Setting\n2 Application\n3 Game\n4 Document\n5 Quit")
            choice = input('')
        if adresse_choice == '2':
            add_mail = input("Write your addresse e-mail: ")
            print("Your adresse e-mail is ", add_mail)
            print("Cheling your mail because a code at 5 chiffre for a confirmation")
            serveur_smtp = 'smtp.office365.com'
            port_smtp = 587
            utilisateur_smtp = 'the.verification.code@outlook.com'
            mot_de_passe_smtp = 'PaPa@free.fr'
            message = f"From: {'the.verification.code@outlook.com'}\nTo: {add_mail}\nSubject: {'CODE OF FERIVICATION'}\n\n This is the code of verification: {ramdome_code} thank to use PAAAA"
            try:
                smtpObj = smtplib.SMTP('smtp.office365.com', 587)
                smtpObj.starttls() # utiliser si la connexion doit être sécurisée
                smtpObj.login('the.verification.code@outlook.com', 'PaPa@free.fr')
                smtpObj.sendmail('the.verification.code@outlook.com', add_mail, message)
                smtpObj.quit()
                print("E-mail was send with sucess !")
                print("Checking your junk")
            except Exception as e:
                print("The email was not send :", e)
            code_amil = input("Entre the code at 5 chiffre: ")
            if ramdome_code == code_amil:
                print("Your adresse was connected")
                print("1 Setting\n2 Application\n3 Game\n4 Document\n5 Quit")
                choice = input('')
            if ramdome_code != code_amil:
                print("This is not the good code")
                print("Resend a mail? (y/n)")
                re_send = input('')
                if re_send == 'y' :
                    print("Cheling your mail because a code at 5 chiffre for a confirmation")
                    if ramdome_code != code_amil:
                        print("The code is not good")
                        print("1 Setting\n2 Application\n3 Game\n4 Document\n5 Quit")
                        choice = input('')
            serveur_smtp = 'smtp.office365.com'
            port_smtp = 587
            utilisateur_smtp = 'the.verification.code@outlook.com'
            mot_de_passe_smtp = 'PaPa@free.fr'
            message = f"From: {'the.verification.code@outlook.com'}\nTo: {add_mail}\nSubject: {'CODE OF FERIVICATION'}\n\n{'The code of verifiaction', ramdome_code, 'Thanks to use PAAAA'}"
            try:
                smtpObj = smtplib.SMTP('smtp.office365.com', 587)
                smtpObj.starttls() # utiliser si la connexion doit être sécurisée
                smtpObj.login('the.verification.code@outlook.com', 'PaPa@free.fr')
                smtpObj.sendmail('the.verification.code@outlook.com', add_mail, message)
                smtpObj.quit()
                print("E-mail was send with sucess !")
                print("Checking your junk")
            except Exception as e:
                print("The email was not send :", e)
            code_amil = input("Entre the code at 5 chiffre: ")
            if ramdome_code == code_amil:
                print("Your adresse was connected")
                if re_send == 'n' :
                    print("1 Setting\n2 Application\n3 Game\n4 Document\n5 Quit")
                    choice = input('')
    if choice1 == '4':
        print("The version of PAAA is the beta.")
        print("You can help us in my discord: ")
        print("Thank to use me")
        print("1 Setting\n2 Application\n3 Game\n4 Document")
        choice = input('')
if choice == '2':
    print("Welcome in your apllication")
    print("1 Note")
    choice2 = input('')
    if choice2 == '1':
        chemin_script = '/Users/kids/Desktop/Garis ps c mon dossier/PAAAA/todo.py'
        subprocess.call(['python', chemin_script])
        print("1 Setting\n2 Application\n3 Game\n4 Document\n5 Quit")
        choice = input('')
if choice == '3':
    print("What game do you wante play?")
    print("1 Snake")
    choice3 = input('')
    if choice3 == '1':
        chemin_script = '/Users/kids/Desktop/Garis ps c mon dossier/PAAAA/sabke.py'
        subprocess.call(['python', chemin_script])
        print("1 Setting\n2 Application\n3 Game\n4 Document\n5 Quit")
        choice = input('')
if choice == '4':
    print("Welcome in your documents")
    print("1 see my document\n2 import document")
    choice4 = input('')
    if choice4 == '1':
        print("This is your document")
        file = open('result_search.txt','r')
    if choice4 == '2':
        print("Document")
        print("1 Import document from your computer\n2 Import from One drive")
        document = input('')
        if document == '1':
            chemin_script = '/Users/kids/Desktop/Garis ps c mon dossier/PAAAA/fichier.py'
            subprocess.call(['python', chemin_script])  
    print("1 Setting\n2 Application\n3 Game\n4 Document\n5 Quit")
    choice4 = input('')
            
