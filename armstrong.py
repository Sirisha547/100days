def sum_digits(n):
    arm=0
    n1=n
    while n>0:
        rem=n%10
        arm+=rem*rem*rem
        n=n//10
    if n1==arm:
        return('armstrong')
    else:
        return('not armstrong')
n=int(input("enter a number:"))
print(sum_digits(n))
