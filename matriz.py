import pyautogui as aut
import time
import os


senha = aut.password(text='Insira sua senha', title='Login', default='', mask='*')


        #                                               Abrir o Corporate
os.startfile('K:\Div\CorporateUpdater\JBS.Updater.Corporate.exe')
time.sleep(6)


        #                                               colocar a senha

aut.moveTo(934,533)
aut.click()
time.sleep(1)
aut.write(senha)
time.sleep(2)
        #                                               mudar a matriz desejada

        #                                               entrar
aut.moveTo(1052,634)
aut.click()
time.sleep(20)
aut.moveTo(1797,0)
aut.click()

        #                                               loop1

        #                                               Abrir o Corporate
os.startfile('K:\Div\CorporateUpdater\JBS.Updater.Corporate.exe')
time.sleep(6)
        #                                               colocar o login

        #                                               colocar a senha
aut.moveTo(934,533)
aut.click()
aut.write(senha)
time.sleep(2)
        #                                               mudar a matriz desejada
aut.moveTo(983,570)
aut.click()
aut.write('Matriz')
time.sleep(1)
aut.press('Enter')
time.sleep(1)
        #                                               entrar
aut.moveTo(1052,634)
aut.click()
time.sleep(20)
        #                                               loop2
        #                                               Abrir o Corporate
os.startfile('K:\Div\CorporateUpdater\JBS.Updater.Corporate.exe')
time.sleep(6)


        #                                               colocar a senha

aut.moveTo(934,533)
aut.click()
time.sleep(1)
aut.write(senha)
time.sleep(2)
        #                                               mudar a matriz desejada
aut.moveTo(983,570)
aut.click()
aut.write('PRE JBS')
time.sleep(1)
aut.press('Enter')
time.sleep(1)
        #                                               entrar
aut.moveTo(1052,634)
aut.click()
time.sleep(20)
aut.moveTo(1797,0)
aut.click()

        #                                               loop3
        #                                               Abrir o Corporate
os.startfile('K:\Div\CorporateUpdater\JBS.Updater.Corporate.exe')
time.sleep(6)


        #                                               colocar a senha

aut.moveTo(934,533)
aut.click()
time.sleep(1)
aut.write(senha)
time.sleep(2)
        #                                               mudar a matriz desejada
aut.moveTo(983,570)
aut.click()
aut.write('LTZ JBS')
time.sleep(1)
aut.press('Enter')
time.sleep(1)
        #                                               entrar
aut.moveTo(1052,634)
aut.click()
time.sleep(20)
aut.moveTo(1797,0)
aut.click()

        #                                               loop4

        #                                               loop5

        #                                               loop6
aut.alert(text='Automação Finalizada', title='Login Automatico', button='OK')

