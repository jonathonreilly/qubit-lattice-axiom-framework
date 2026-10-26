import time
from mpmath import iv, mp
exec(open('iv1.py').read().split("t0=time.time()")[0])
def bracket(hn, taumax):
    # tau grid i/hn exact rationals -> iv
    N=taumax*hn
    lo=iv.mpf(0); hi=iv.mpf(0)
    prev=None
    for i in range(N):
        ta=iv.mpf(i)/hn; tb=iv.mpf(i+1)/hn
        a=ta*ta; b=tb*tb
        h=tb-ta
        if i==0:
            psa=iv.mpf(3)/2; dpa=-iv.mpf(21)/16
        else:
            psa,dpa=prev
        _,_,psb,dpb=G_Gp_psi(b)
        prev=(psb,dpb)
        c1=2*h; c2=iv.mpf(2)/3*(b**1.5 - a**1.5) if False else iv.mpf(2)/3*(tb**3-ta**3)
        m=(psb-psa)/(b-a)
        up=(psa-m*a)*c1+m*c2
        lw=(psa-dpa*a)*c1+dpa*c2
        hi+=up; lo+=lw
    T=iv.mpf(taumax)**2
    G,_,_,_=G_Gp_psi(T)
    tail_lo=2*(1-G)/taumax; tail_hi=iv.mpf(2)/taumax
    lo+=tail_lo; hi+=tail_hi
    return lo,hi
t0=time.time()
for hn,tm in [(20,20),(50,20),(100,25)]:
    lo,hi=bracket(hn,tm)
    c=1/(2*iv.sqrt(iv.pi))
    I=iv.mpf([lo.a,hi.b])*c
    print(hn,tm,I, "width",I.b-I.a, "gamma",12/I, time.time()-t0)
