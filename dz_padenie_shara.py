H = float(input())
t = float(input())

g = 9.81 #ускорение
v0 = 0 #начальная скорость

t_padenia = (2 * H / g) ** 0.5 #время падения

vk = v0 + g * t_padenia #конечная скорость

vt = v0 + g * t #скорость в момент t
xt = H - (v0 * t + (g * t * t / 2) ) #кордината в момент t

if t_padenia < t or H < 0:
    print('некоректные значения')
else:
    print(t_padenia)
    print(vk)
    print(vt)
    print(xt)