def threshold_function(y):
    if(y >= 0):
        return 1
    else:
        return 0

def scalar_product(u_list, w_list):
    suma = 0
    index = 0
    for u in u_list:
        suma = suma + u * w_list[index]
        index = index + 1

    return suma

def mcculloch_pitts(u, w):
    suma = scalar_product(u, w)
    y = threshold_function(suma)
    return y
        

def main():
    bias_u = float(1)
    bias_w = float(-3)
    
    u = []
    w = []
    
    print(mcculloch_pitts(u,w))

    print("Wybierz bramke: \n1. NOT\n2.AND")
    x = input()
    match x:
        case '1':
            u_1 = input()
            w_1 = float(-2)
            u.append(float(u_1))
            w.append(w_1)
            print(mcculloch_pitts(u, w))
        case '2':
            bias_u = float(1)
            bias_w = float(-3)
            u = [bias_u]
            w = [bias_w, 2.0, 2.0]
            u_1 = input()
            u.append(u_1)
            u.append(float(1))
            print(mcculloch_pitts(u, w))
        case _:
            print("NOT FOUND")



if __name__ == '__main__':
    main()
