'''
                                    Geometric Progression
The nth term of a GP series is Tn = arn-1, where a = first term and r = common ratio = Tn/Tn-1) . The sum of infinite terms of a GP series S∞= a/(1-r) where 0< r<1. If a is the first term, r is the common ratio of a finite G.P.


Given an integer N, we need to find the geometric sum of the following series using recursion. 

1 + 1/3 + 1/9 + 1/27 + … + 1/(3^n) 

Input N = 5 
Output: 1.49794

Input: N = 7
Output: 1.49977

Approach:
We will calculate the last term and call recursion on the remaining n-1 terms each time. The final sum returned is the result.
'''

def geo_sum(n):
    if n==0:
        return 1

    sum = 1/pow(2,n) + geo_sum(n-1)
    return sum

print(geo_sum(8)) #1.499923792104862