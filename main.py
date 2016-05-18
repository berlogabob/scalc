acid_list=[]
###
def acidls():
    summ = one_acid()
    acid_list.append(summ)
    #print(acid_list)
def one_acid():
  C = float(12.0107) #атомная масса углерода
  O = float(15.9994) #атомная масса кислорода
  H = float(1.008)#атомная масса водорода
  n = float(input("Какое число атомов углерода? "))
  N = float(input("Какое количесто двойных связей в жирной кислоте? "))
  Wi = float(input("Каково содержание данной кислоты в сумме жирных кислот? (десятичную часть от целой отделять ТОЧКОЙ)  "))
  print("\n", "\n", "\n")
  Mi = float(C*n+H*2*(n-N)+O*2)
  odna_kislota = (254 * N * Wi) / Mi
  return(odna_kislota)
    ###
def question():
    answer = input(" Добавить значения для жирной кислоты?  (да или нет)")
    if answer == "да" or answer == "Да" or answer == "д" or answer == "ДА" or answer == "Д" or answer == "Y" or answer == "y" or answer == "Yes" or answer == "yes" or answer == "YES":
        acidls()
        question()
    elif answer == "нет" or answer == "Нет" or answer == "Н" or answer == "н" or answer == "НЕТ" or answer == "N" or answer == "No" or answer == "n" or answer == "no" or answer == "NO":
        print("Йодное число равно: ")
        print(sum(acid_list))
    else:
        print("\n \n введено некорректное значение")
        #print("\n")
        question()
question()
input("Для выхода нажмите клавишу Enter")
