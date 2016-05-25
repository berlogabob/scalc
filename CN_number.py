# -*- coding: utf-8 -*-
#
CN_sum_list = []

def qw():
    answer = input(" Добавить значения для жирной кислоты?  (да или нет)")
    if answer == "да" or answer == "Да" or answer == "д" or answer == "ДА" or answer == "Д" or answer == "Y" or answer == "y" or answer == "Yes" or answer == "yes" or answer == "YES" or answer == "1":
        usinp()
        sum_CN()
        qw()
    elif answer == "нет" or answer == "Нет" or answer == "Н" or answer == "н" or answer == "НЕТ" or answer == "N" or answer == "No" or answer== "n" or answer == "no" or answer == "NO" or answer == "0":
        print("\n")
        print(CN_sum_list, "\n", "\n", sum(CN_sum_list))
    else:
        print("\n \n введено некорректное значение")
        qw()




def usinp():
    global C
    C = float(12.0107) #атомная масса углерода
    global O
    O = float(15.9994) #атомная масса кислорода
    global H
    H = float(1.008)#атомная масса водорода
    summa = int(1) #после отладки пекределать в список
    global n
    n = float(input("Какое число атомов углерода? "))
    global N
    N = float(input("Какое число двойных связей в молекуле? "))
    global Wi
    Wi = float(input("Каково содержание данной кислоты в сумме жирных кислот? (десятичную часть от целой отделять ТОЧКОЙ)  "))
    global Mi_ester
    Mi_ester = float(C * n + H * (2 * n - N) *O*2+C+H*2)
    global Fi
    Fi = -7.8 + 0.302 * Mi_ester - 20 * N #величина цетанового числа индивидуального метилового эфира жирной кислоты
    print("\n", "\n", "\n")
    print(CN_sum_list)
    print("\n", "\n", "\n")


#CN = summa * Wi*Fi
#//
#Mi_acid = float(C*n+H*2*(n-N)+O*2)

def one_CN(Wi, Fi):
    one_CN = Wi * Fi
    return float(one_CN)

def sum_CN():
    onenew= one_CN(Wi, Fi)
    z = CN_sum_list.append(onenew)
    return z
qw()
