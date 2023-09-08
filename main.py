#recursive function to calculate the factorial of a given number
def fact(n):
  if n==0 or n==1:
    return 1
  else:
    return n*fact(n-1)
num=int(input("enter the number :")) 3
3
result=fact(num)
print("the factorial of",num,"is", result)