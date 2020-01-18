
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


def polynomial_roots(fun_a_list, roots_list, fun_r_s_list):

    if (len(fun_a_list) < 4):
        roots_list.append(numpy.roots(fun_a_list))
        print("roots: "+str(roots_list))

    else:
        r = random.random()
        s = random.random()

        deghat = 10**-6
        a_len = len(fun_a_list)

        b_list = list()
        c_list = list()
        initializeList(b_list, a_len)
        initializeList(c_list, a_len)

        r_prev = r

        b_c_list(fun_a_list, b_list, r, s)
        b_c_list(b_list, c_list, r, s)

        d = det_calculation(c_list[1], c_list[2], c_list[2], c_list[3])
        d1 = det_calculation(-b_list[0], c_list[2], -b_list[1], c_list[3])
        d2 = det_calculation(c_list[1], -b_list[0], c_list[2], -b_list[1])

        r = r_s_calculation(r, d1, d)
        s = r_s_calculation(s, d2, d)

        print("a: "+str(fun_a_list))
        print("b: "+str(b_list))
        print("c: "+str(c_list))
        print("d: "+str(d))
        print("d1: "+str(d1))
        print("d2: "+str(d2))
        print("r: "+str(r))
        print("s: "+str(s))
        print("r_prev: "+str(r_prev))
        print("---------------------------------------")

        while(abs(r_prev-r) > deghat):
            r_prev = r

            b_c_list(fun_a_list, b_list, r, s)
            b_c_list(b_list, c_list, r, s)

            d = det_calculation(c_list[1], c_list[2], c_list[2], c_list[3])
            d1 = det_calculation(-b_list[0], c_list[2], -b_list[1], c_list[3])
            d2 = det_calculation(c_list[1], -b_list[0], c_list[2], -b_list[1])

            r = r_s_calculation(r, d1, d)
            s = r_s_calculation(s, d2, d)

            print("a: "+str(fun_a_list))
            print("b: "+str(b_list))
            print("c: "+str(c_list))
            print("d: "+str(d))
            print("d1: "+str(d1))
            print("d2: "+str(d2))
            print("r: "+str(r))
            print("s: "+str(s))
            print("r_prev: "+str(r_prev))
            print("---------------------------------------")
    
        fun_r_s_list[0] = -r
        fun_r_s_list[1] = -s
        roots_list.append(numpy.roots([1, -r, -s]))

        print("roots: "+str(roots_list))

        polynomial_decomposition(fun_a_list, fun_r_s_list, roots_list)


def polynomial_decomposition(fun_a_list, fun_r_s_list, roots_list):
    p2 = numpy.array(list(reversed(fun_a_list)))
    p1 = numpy.array(list(reversed(fun_r_s_list)))
    quotient, remainder = numpy.polydiv(p2, p1)

    print("quotient: "+str(quotient))
    print("remainder: "+str(remainder))

    if( len(quotient) > 3 ):
        polynomial_roots(quotient, roots_list, fun_r_s_list)
    else:
        roots_list.append(numpy.roots(quotient))
        print("roots: "+str(roots_list))


a_list = [-3.000000, 2.000000, 1.000000, 0.000000, -1.000000, -1.000000]
#a_list = [1.000000, 0.000000, -4.000000]
roots = list()
r_s_list = [0, 0]
polynomial_roots(a_list, roots, r_s_list)
