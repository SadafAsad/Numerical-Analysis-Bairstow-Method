def b_c_calculation(k, n, a_b_list, r, s):

    if (k==n+1 or k==n+2):
        return 0

    else:
        return ( a_b_list[k] 
        + ( r * b_c_calculation(k+1, n, a_b_list, r, s) ) 
        + ( s * b_c_calculation(k+2, n, a_b_list, r, s) ) )
    
a_list = [1.0000, 1,0000, 3.0000, 4.0000, 6.0000]
b_list = [0, 0, 0, 0, 0]
c_list = [0, 0, 0, 0, 0]

i=0
while(i<7):
    b_list[i] = b_c_calculation(i, 4, a_list, -2.1, -1.9)

i=0
while(i<7):
    c_list[i] = b_c_calculation(i, 4, b_list, -2.1, -1.9)

print(a_list)
print(b_list)
print(c_list) 