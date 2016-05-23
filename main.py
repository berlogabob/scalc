IV_sum_list = []
SV_sum_list = []
def qw():
    answer = input(" Добавить значения для жирной кислоты?  (да или нет)")
    if answer == "да" or answer == "Да" or answer == "д" or answer == "ДА" or answer == "Д" or answer == "Y" or answer == "y" or answer == "Yes" or answer == "yes" or answer == "YES":
        usinp()
        sum_IV()
        sum_SV()
        qw()
    elif answer == "нет" or answer == "Нет" or answer == "Н" or answer == "н" or answer == "НЕТ" or answer == "N" or answer == "No" or answer== "n" or answer == "no" or answer == "NO":
        #print("Йодное число равно: %f2 /n Степень омыления равна: %f2 ", sum(IV_sum_list), sum(SV_sum_list))
        print(sum(IV_sum_list), sum(SV_sum_list))
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
    global n
    n = float(input("Какое число атомов углерода? "))
    global N
    N = float(input("Какое количесто двойных связей в жирной кислоте? "))
    global Wi
    Wi = float(input("Каково содержание данной кислоты в сумме жирных кислот? (десятичную часть от целой отделять ТОЧКОЙ)  "))
    print("\n", "\n", "\n")
    global Mi
    Mi_acid = float(C*n+H*2*(n-N)+O*2)


def one_IV(N, Wi,Mi):
    one_IV = (254 * N * Wi) / Mi
    return float(one_IV)

def one_SV(Wi, Mi):
    one_SV = (560*Wi)/Mi
    return float(one_SV)

def sum_IV():
    onenew= one_IV(N, Wi, Mi)
    z = IV_sum_list.append(onenew)
    return z

def sum_SV():
    onenew = one_SV(Wi, Mi)
    z=SV_sum_list.append(onenew)
    return z



qw()
