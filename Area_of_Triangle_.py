a,b,c=map(int,input().split())
# calculate the semi-perimeter using the formula  
s = (a + b + c) / 2.0  
  
# calculate the area  using Heron's formula
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
# display the result upto 2 decimal places
print('%0.2f' %area) 