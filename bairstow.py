
import numpy as m_numpy

def b_c_calculation(k, n, a_b_list, r, s):

    if (k==n+1 or k==n+2):
        return 0

    else:
        return ( a_b_list[k] 
        + ( r * b_c_calculation(k+1, n, a_b_list, r, s) ) 
        + ( s * b_c_calculation(k+2, n, a_b_list, r, s) ) )
    

def det_calculation(x1, x2, x3, x4):
    return (x1*x4)-(x2*x3)


def r_s_calculation(r_s, d1_d2, d):
    return r_s + (d1_d2/d)


a_list = [6.0000, 4.0000, 3.0000, 1.0000, 1.0000]
b_list = [0, 0, 0, 0, 0]
c_list = [0, 0, 0, 0, 0]

i=0
while(i<5):
    b_list[i] = b_c_calculation(i, 4, a_list, -2.1, -1.9)
    i = i+1

i=0
while(i<5):
    c_list[i] = b_c_calculation(i, 4, b_list, -2.1, -1.9)
    i = i+1

print(a_list)
print(b_list)
print(c_list) 

print(det_calculation(-12.2740, 8.2300, 8.2300, -3.2000))

print(r_s_calculation(-2.1, -3.15001, -28.4561))

p2 = m_numpy.array([1, 1, 3, 4, 6])
p1 = m_numpy.array([1, 2, 2])
quotient, remainder = m_numpy.polydiv(p2, p1)
print(quotient)
print(remainder)
