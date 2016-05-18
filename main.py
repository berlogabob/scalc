IV_list=[]
SV_list=[]
def dialog():
  answer = input(" Добавить значения для жирной кислоты?  (да или нет)")
  if answer == "да" or answer == "Да" or answer == "д" or answer == "ДА" or answer == "Д" or answer == "Y" or answer == "y" or answer == "Yes" or answer == "yes" or answer == "YES":
    user_input_4one_acid()
    summa_IV()
    summa_SV()
    dialog()
  elif answer == "нет" or answer == "Нет" or answer == "Н" or answer == "н" or answer == "НЕТ" or answer == "N" or answer == "No" or answer == "n" or answer == "no" or answer == "NO":
    print("Йодное число равно: %f2 /n Степень омыления равна: %f2 ", sum(IV_list, sum(SV_list))
    #print(sum(IV_list), sum(SV_list))
  else:
    print("\n \n введено некорректное значение")
    dialog()
def user_input_4one_acid():
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
  Mi = float(C*n+H*2*(n-N)+O*2)
def odno_IV():
   odno_IV = (254 * N * Wi) / Mi
   return float(odno_IV)
def odno_SV():
  odno_SV = (560*Wi)/Mi
  return float(odno_SV)
def summa_IV():
  summ = odno_IV()
  IV_list.append(summ)
def summa_SV():
  summ = odno_SV()
  SV_list.append(summ)
def GO():
 dialog()
  

GO()
