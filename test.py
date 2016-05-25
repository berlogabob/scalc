#
C = float(12.0107) #атомная масса углерода
O = float(15.9994) #атомная масса кислорода
H = float(1.008)#атомная масса водорода
n = 16
N = 1
#

#
def Fi2():
  Fi2 = -7.8 + 0.302 * 270 - 20 * 1
  print(Fi2)
  return Fi2


def Mi(C, n, H, N, O):#молекулярная масса эфира
    Mi = float((C * n + H * (2 * n - N) + O * 2 + H * 2))
    return Mi
    #
def Fi(Mi, N):
    Fi = float((-7.8) + (0.302 * Mi(C, n, H, N, O)) - (20 * N))
    return Fi
    #
#
#
"""
n = 16
N = 1
Wi = float(10.40)
CN_1 = Wi * Fi(Mi, N)
print("Mi is: ", Mi(C, n, H, N, O))
print("Fi is: ", Fi(Mi, N))
print("CN_1:  ", CN_1)
print("\n")
#
n = 18
N = 1
Wi = float(43.24)
CN_2 = Wi * Fi(Mi, N)
print("Mi is: ", Mi(C, n, H, N, O))
print("Fi is: ", Fi(Mi, N))
print("CN_2:  ", CN_2)
print("\n")
#
n = 18
N = 2
Wi = float(11.75)
CN_3 = Wi * Fi(Mi, N)
print("Mi is: ", Mi(C, n, H, N, O))
print("Fi is: ", Fi(Mi, N))
print("CN_3:  ", CN_3)
print("\n")
#
n = 18
N = 3
Wi = float(3.86)
CN_4 = Wi * Fi(Mi, N)
print("Mi is: ", Mi(C, n, H, N, O))
print("Fi is: ", Fi(Mi, N))
print(CN_4)
print("\n")
print(CN_1 + CN_2 + CN_3 + CN_4)
"""
#print(C * 17 + H * 34 + O * 2)
#print(Mi(C, n, H, N, O))
Fi2()


#print(Fi(Mi(C, n, H, N, O), N))
