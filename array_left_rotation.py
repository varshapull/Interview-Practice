#Cracking the coding interview problem 1 : https://www.hackerrank.com/challenges/ctci-array-left-rotation


def array_left_rotation(a, n, k):
    new_arr = [0] * n
    for i in range(0,n):
        new_index = (i + k) % n
        new_arr[i] = a[new_index]
    return new_arr
        
        

n, k = map(int, raw_input().strip().split(' '))
a = map(int, raw_input().strip().split(' '))
answer = array_left_rotation(a, n, k);
print ' '.join(map(str,answer))
