# def fnd_sum(n):
#     sum =0

#     for i in range(1,n+1):
#         sum += i
#     return sum

### Recursive

def fnd_sum(n):
    if n ==1:
        return 1

    return n + fnd_sum(n-1)
    
if __name__=='__main__':
    print(fnd_sum(3))