
import numpy
import random
import cmath

#bk and ck calculation
#--each cell in b list and c list--
def b_c_calculation(k, n, a_b_list, r, s):
    if (k==n+1 or k==n+2):
        return 0

    else:
        return ( a_b_list[k] 
        + ( r * b_c_calculation(k+1, n, a_b_list, r, s) ) 
        + ( s * b_c_calculation(k+2, n, a_b_list, r, s) ) )
    

#b array and c array calculation
def b_c_list(a_b_list, b_c_list, r, s):
    n = len(a_b_list)
    i = 0
    while(i<n):
        b_c_list[i] = b_c_calculation(i, n-1, list(reversed(a_b_list)), r, s)
        i = i+1


#determinant calculation
#--4 values passed az determinant's arguments-- 
def det_calculation(x1, x2, x3, x4):
    return (x1*x4)-(x2*x3)


#r and s calculation
def r_s_calculation(r_s, d1_d2, d):
    return r_s + (d1_d2/d)


#initializing list with zeros
def initializeList(list, n):
    i=0
    while i<n:
        list.append([])
        j=0
        while j<n:
            list[i].append(0)
            j+=1
        i+=1


#calculates roots and calls polynomial decompoition to decompose the polynomial
def polynomial_roots(fun_a_list, roots_list, fun_r_s_list, fun_r_s_chosen):

    #if the polynomial's degree is less than 3
    if (len(fun_a_list) == 3):
        roots_list.append(round(list(numpy.roots(fun_a_list))[0], 6))
        roots_list.append(round(list(numpy.roots(fun_a_list))[1], 6))
    elif (len(fun_a_list) == 2):
        roots_list.append(round(list(numpy.roots(fun_a_list))[0], 6))

    else:
        r = fun_r_s_list[0]
        s = fun_r_s_list[1]

        deghat = 10**-6
        a_len = len(fun_a_list)

        b_list = list()
        c_list = list()
        initializeList(b_list, a_len)
        initializeList(c_list, a_len)

        r_prev = r
        s_prev = s

        b_c_list(fun_a_list, b_list, r, s)
        b_c_list(list(reversed(b_list)), c_list, r, s)
        d = det_calculation(c_list[1], c_list[2], c_list[2], c_list[3])
        d1 = det_calculation(-b_list[0], c_list[2], -b_list[1], c_list[3])
        d2 = det_calculation(c_list[1], -b_list[0], c_list[2], -b_list[1])

        r = r_s_calculation(r, d1, d)
        s = r_s_calculation(s, d2, d)

        while( (abs(r_prev-r) > deghat) and (abs(s_prev-s) > deghat) ):
            r_prev = r
            s_prev = s

            b_c_list(fun_a_list, b_list, r, s)
            b_c_list(list(reversed(b_list)), c_list, r, s)

            d = det_calculation(c_list[1], c_list[2], c_list[2], c_list[3])
            d1 = det_calculation(-b_list[0], c_list[2], -b_list[1], c_list[3])
            d2 = det_calculation(c_list[1], -b_list[0], c_list[2], -b_list[1])

            r = r_s_calculation(r, d1, d)
            s = r_s_calculation(s, d2, d)
            
        fun_r_s_chosen[0] = r
        fun_r_s_chosen[1] = s
        roots_list.append(round(list(numpy.roots([1, -r, -s]))[0], 6))
        roots_list.append(round(list(numpy.roots([1, -r, -s]))[1], 6))
        polynomial_decomposition(fun_a_list, fun_r_s_list, roots_list, fun_r_s_chosen)


def polynomial_decomposition(fun_a_list, fun_r_s_list, roots_list, fun_r_s_chosen):
    p2 = numpy.array(fun_a_list)
    p1 = numpy.array([1, -fun_r_s_chosen[0], -fun_r_s_chosen[1]])
    quotient, remainder = numpy.polydiv(p2, p1)

    #if polynomial's root is greater than 2, not only calculate roots but also decompose it
    if( len(quotient) > 3 ):
        polynomial_roots(quotient, roots_list, fun_r_s_list, fun_r_s_chosen)
    elif( len(quotient) == 3 ):
        roots_list.append(round(list(numpy.roots(quotient))[0], 6))
        roots_list.append(round(list(numpy.roots(quotient))[1], 6))
    else:
        roots_list.append(round(list(numpy.roots(quotient))[0], 6))


def roots_summation(fun_roots):
    i = 0
    positive_sum = [0, 0]
    while (i < len(fun_roots)):
        if (fun_roots[i].imag >= 0):
            positive_sum[0] = round((positive_sum[0] + fun_roots[i].real), 6)
            positive_sum[1] = round((positive_sum[1] + fun_roots[i].imag), 6)
        i = i + 1
    return positive_sum

continuation = 1
while(continuation == 1):
    n = int(input("Enter polynomial's degree: "))
    a_list_str = input("Enter coefficients: ").split()
    a_list = list()
    i = 0
    if(len(a_list_str) == n+1):
        while(i<len(a_list_str)):
            a_list.append(int(a_list_str[i]))
            i = i + 1
        roots = list()
        r_s_chosen = [0, 0]
        r_s_list = [random.random(), random.random()]
        polynomial_roots(a_list, roots, r_s_list, r_s_chosen)
        sums = roots_summation(roots)
        print("roots: " + str(roots))
        print("output: " + str(sums[0]) + " " + str(sums[1]))
        print("Do you want to continue?(enter 1 or 2)")
        continuation = int(input("1)YES 2)NO "))
    else:
        print("Incorrect input")
        print("Do you want to continue?(enter 1 or 2)")
        continuation = int(input("1)YES 2)NO "))
