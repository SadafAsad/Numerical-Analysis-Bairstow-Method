
import numpy
import random

def b_c_calculation(k, n, a_b_list, r, s):
    if (k==n+1 or k==n+2):
        return 0

    else:
        return ( a_b_list[k] 
        + ( r * b_c_calculation(k+1, n, a_b_list, r, s) ) 
        + ( s * b_c_calculation(k+2, n, a_b_list, r, s) ) )
    

def b_c_list(a_b_list, b_c_list, r, s):
    n = len(a_b_list)
    i = 0
    while(i<n):
        b_c_list[i] = b_c_calculation(i, n-1, a_b_list, r, s)
        i = i+1


def det_calculation(x1, x2, x3, x4):
    return (x1*x4)-(x2*x3)


def r_s_calculation(r_s, d1_d2, d):
    return r_s + (d1_d2/d)


def initializeList(list, n):
    i=0
    while i<n:
        list.append([])
        j=0
        while j<n:
            list[i].append(0)
            j+=1
        i+=1


def polynomial_decomposition(a_list):
    r = random.random()
    s = random.random()

    deghat = 10**-6
    a_len = len(a_list)

    b_list = list()
    c_list = list()
    initializeList(b_list, a_len)
    initializeList(c_list, a_len)

    r_prev = r

    b_c_list(a_list, b_list, r, s)
    b_c_list(b_list, c_list, r, s)

    d = det_calculation(c_list[1], c_list[2], c_list[2], c_list[3])
    d1 = det_calculation(-b_list[0], c_list[2], -b_list[1], c_list[3])
    d2 = det_calculation(c_list[1], -b_list[0], c_list[2], -b_list[1])

    r = r_s_calculation(r, d1, d)
    s = r_s_calculation(s, d2, d)

    while(abs(r_prev-r) <= deghat):
        r = random.random()
        s = random.random()

        r_prev = r

        b_c_list(a_list, b_list, r, s)
        b_c_list(b_list, c_list, r, s)

        d = det_calculation(c_list[1], c_list[2], c_list[2], c_list[3])
        d1 = det_calculation(-b_list[0], c_list[2], -b_list[1], c_list[3])
        d2 = det_calculation(c_list[1], -b_list[0], c_list[2], -b_list[1])

        r = r_s_calculation(r, d1, d)
        s = r_s_calculation(s, d2, d)


a_list = [6.0000, 4.0000, 3.0000, 1.0000, 1.0000]

p2 = numpy.array([1, 1, 3, 4, 6])
p1 = numpy.array([1, 2, 2])
quotient, remainder = numpy.polydiv(p2, p1)
print(quotient)
print(remainder)
