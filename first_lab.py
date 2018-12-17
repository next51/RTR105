import math as m
x = 1.*input("ievadi argumentu(x):")
y = m.cos(x)**2
print "cos^2(%.2f)=%.2f"%(x,y)
k= 0
a = 1
S = a
print "a%d = %.2f S%d = %.2f"%(k,a,k,S)
while k <500:
    k += 1
    R = ((-1)*x**2)/((2*k-1)*(2*k))
    a *= R
    S += a
    if k >=499:
        print "a%d = %.2f S%d = %.2f"%(k,a,k,S)
print "\ncos^2(%.2f) caur summu:%.2f"%(x,S*S)
