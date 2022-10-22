AND_value = 1.5
OR_value = 0.5

def threshold_function(input_sum, threshold_val):
    if(input_sum > threshold_val):
        return 1
    else:
        return 0

def dot_product(u_list, w_list):
    suma = 0
    index = 0
    for u in u_list:
        suma = suma + u * w_list[index]
        index = index + 1

    return suma

def mcculloch_pitts(threshold_val, u_list, w_list):
    suma = dot_product(u_list, w_list)
    y = threshold_function(suma, threshold_val)
    return y
        

def main():
    units = [1,1,1]
    weights = [0.9,0.6,0.7]

    print(mcculloch_pitts(2, units,weights))


if __name__ == '__main__':
    main()
