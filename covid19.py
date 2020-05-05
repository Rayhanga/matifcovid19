import math

def Nhx(Nh, R, P, x):
    h = 0
    while h != x:
        DNh = Nh*R*P
        Nh = Nh + DNh
        h = h + 1
    return Nh, h

if __name__ == "__main__":
    Nh = float(input('Jumlah kasus pertama (Nh): ') )
    R = float(input('Rata - rata orang yang bertemu dengan orang positif (R): '))
    P = float(input('Peluang tertularnya orang yang bertemu dengan orang positif (P): '))
    x = float(input('Hari yang dituju (x): '))

    Nh, h = Nhx(Nh,R,P,x)

    print('Pada hari ke-{}, akan ada pasien sebanyak {}'.format(h, math.floor(Nh)))