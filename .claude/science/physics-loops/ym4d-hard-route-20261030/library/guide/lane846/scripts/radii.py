import math
lam=lambda w: math.exp(2*w)*(1+2*w)
def bis(f,lo=0.0,hi=1.0):
    for _ in range(80):
        mid=(lo+hi)/2
        if f(mid): lo=mid
        else: hi=mid
    return lo
def astar(b):
    x=b/4; return 6*x*(1+x)/(1-4*x-6*x*x)
for b in [1/9,0.2]:
    print('DOB',b,bis(lambda w:(9*b/2)*lam(w)+w<1))
for b in [0.25,0.3]:
    print('LF',b,bis(lambda w:3*b*lam(w)+w<1))
for b in [0.25,0.3,0.35]:
    x=b/4;a=astar(b)
    print('ST',b,'alpha*',round(a,4),'thr',(1-a)*(1-6*x)/2,'w',bis(lambda w:6*(lam(w)-1)*x+w<(1-a)*(1-6*x)/2))
print('beta*',(math.sqrt(37)-5)/3, astar((math.sqrt(37)-5)/3))
# order-one band, two-loop ratio a(beta)/a(2.38)
f=lambda b:(6*math.pi**2*b/11)**(51/121)*math.exp(-3*math.pi**2*b/11)
for bt in [3.0,4.0]:
    r=f(bt)/f(2.38); R=10/r
    print('top',bt,'a m',round(r,4),'ratio',round(R,1),'steps L=3,5,7,9,25:',[round(math.log(R)/math.log(L),2) for L in (3,5,7,9,25)])
print('ratio 10 steps',[round(math.log(10)/math.log(L),2) for L in (3,5,7,9)])
print('4 ln 12',4*math.log(12), '11/(3pi^2)',11/(3*math.pi**2))
