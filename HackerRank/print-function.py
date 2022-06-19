'''
The included code stub will read an integer, N, from STDIN.

Without using any string methods, try to print the following:
123...N

Note that "..." represents the consecutive values in between.

Example:
N = 5
Print the string
12345
'''

def print_fun(n):
    string = ''
    for i in range(1,n+1):
        string = string+str(i)
    return string

if __name__ == '__main__':
    n = int(input())
    var = print_fun(n)
    print(var)
    #print(print_fun(n))