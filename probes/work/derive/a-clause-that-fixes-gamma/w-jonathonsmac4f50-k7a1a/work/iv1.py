import time
from mpmath import iv, mp
iv.prec=120
def I01(x):
    # interval x>0: I0(x), I1(x) by series with rigorous tail (terms positive, ratio<=1/2 after n>=x)
    # I0 = sum (x/2)^(2n)/(n!)^2 ; I1 = sum (x/2)^(2n+1)/(n!(n+1)!)
    h=x/2; h2=h*h
    term0=iv.mpf(1); term1=h
    s0=term0; s1=term1
    n=0
    hmax=h.b
    while True:
        n+=1
        term0=term0*h2/(n*n)
        term1=term1*h2/(n*(n+1))
        s0+=term0; s1+=term1
        # ratio bound for later terms: h2max/((n+1)^2) 
        if n+1>2*float(hmax)+4 and float(term0.b)<1e-30*float(s0.a):
            # tail <= term*(r/(1-r)) with r=hmax^2/(n+1)^2 <= 1/4
            r=iv.mpf(hmax)**2/((n+1)**2)
            tail0=term0*r/(1-r)
            tail1=term1*r/(1-r)*2
            s0+=iv.mpf([0,tail0.b]); s1+=iv.mpf([0,tail1.b])
            return s0,s1
def G_Gp_psi(t):
    # t interval >0 ; x=t/2
    x=t/2
    I0,I1=I01(x)
    ex=iv.exp(-x)
    g=ex*I0
    gp=ex*(I1-I0)/2        # dg/dt
    G=g**3
    Gp=3*g**2*gp
    psi=(1-G)/t
    psip=(-Gp*t-(1-G))/(t*t)
    return G,Gp,psi,psip
t0=time.time()
for tt in [1e-8,0.5,5,50,400]:
    G,Gp,psi,psip=G_Gp_psi(iv.mpf(tt))
    print(tt,psi,psip,time.time()-t0)
