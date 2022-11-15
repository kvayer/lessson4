# name = input("Введите имя: ")
# sename = input("Введите фамилию: ")
# group = input("Введите номер группы: ")
# print(name + " " + sename + " " + group)
# year = int(input("Введите год: "))
# if year % 4 == 0 and year % 100 != 0 or (year % 400 == 0 and year % 4 == 0):
#     print("Год является високосным")
# else:
#     print("Год не является високосным")
import math
def point_to_point(a,b):
    return math.dist(a,b)
kl_vo = int(input("Введите кол-во точек: "))
array=list()
min = 1000000000
max = -1000000000
t_max = list()
t_min = list()
for i in range(2):
    t_max.append(i)
    t_min.append(i)
for i in range(kl_vo):
    a = list(map(int, input("Введите точку "+str(i)+": ").split()))
    array.append(a)
for i in range(len(array)):
    for j in range(len(array)):
        dist = point_to_point(array[i],array[j])
        if i == j:
            continue
        if dist>max:
            max = dist
            t_max[0] = array[i]
            t_max[1] = array[j]
        else:
            continue
        if dist<min:
            min = dist
            t_min[0] = array[i]
            t_min[1] = array[j]
        else:
            continue
print("Минимальное расстояние от точки " + str(t_min[0]) + " до точки " + str(t_min[1]) + " = " + str(min))
print("Максимальное расстояние от точки " + str(t_max[0]) + " до точки " + str(t_max[1]) + " = " + str(max))