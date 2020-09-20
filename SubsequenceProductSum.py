"""
link: https://www.codewars.com/kata/5d653190d94b3b0021ec8f2b/train/python
name: Subsequence Product Sum

Given an array of integers and an integer m, return the sum of the product of its subsequences of length m.

Ex1:

a = [1, 2, 3]
m = 2
the subsequences(of length 2) are (1,2) (1,3) (2,3), you should multiply the numbers of each subsequence and take their sum

product_sum = (1*2) + (1*3) + (2*3) #=> 11
Ex2:

a = [2,3,4,5]
m = 3

the subsequences(of length 3) are (2,3,4) (2,4,5) (2,3,5) (3,4,5)

product_sum = (2*3*4) + (2*3*5) + (2*4*5) + (3*4*5) #=> 154

"""


def product_sum(a, m):
    # your code here
    pass






tc = [
    ([2,3, 4, 5],3, 154 ),
    ([1, 2, 3], 2, 11),
    ([5, 7, 2, 3], 3, 247),
    ([3,10,7,9,1,4,5,2,8,6], 7, 8409500),
    ([10,7,8,5,6,9,4,1,2,3], 8, 12753576),
    ([1,7,6,10,21,5,9,8,5,4], 2, 2469),
    ([6,7,8,5,2,4,9,3,1,10], 6, 3416930),
    ([3,2,9,1,7,10,5,6,8,4], 4, 157773),
    ([9,8,10,4,2,7,5,1,3,6], 3, 18150),
    ([3,3,1,7,6,8,1,4,6,10], 4, 94837),
    ([6,8,1,7,2,10,5,9,3,4], 5, 902055),
    ([10,3,4,9,5,8,6,7,1,2], 1, 55),
    ([7,9,4,2,3,10,8,6,5,1], 9, 10628640)
]


for arr, m, res in tc:
    print(product_sum(arr,m), res, 'Wrong Value')
