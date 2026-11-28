# Guide only. Independent data paths for S9:
# (a) f(1)/f(j) = K^4(u,u)/K^4(u,-u) from K^2(u,z) = 2 I_1(b|u+z|)/(b|u+z|) and a 1D quadrature in c = u.z;
# (b) Metropolis on the full eight-site graph (no reduction), with the conditional-mean estimator at y.
import math, random, sys
def besselI(nu, x, terms=80):
    s=0.0; t=(x/2)**nu/math.gamma(nu+1)
    for m in range(terms):
        s+=t; t*=(x/2)**2/((m+1)*(m+1+nu))
        if t<1e-18*abs(s): break
    return s
def K2(b, r):  # r = |u+z|
    x=b*r
    return 1.0 if x<1e-12 else 2*besselI(1,x)/x
def ratio(b, n=20000):
    sp=0.0; sm=0.0
    for k in range(n):  # midpoint rule in theta, c = cos(theta), density (2/pi) sin^2
        th=(k+0.5)*math.pi/n; c=math.cos(th); w=math.sin(th)**2
        kp=K2(b,math.sqrt(max(0.0,2+2*c))); km=K2(b,math.sqrt(max(0.0,2-2*c)))
        sp+=w*kp*kp; sm+=w*kp*km
    return sp/sm
for b in (1.0,2.6,5.0):
    print("b=%.2f  f(1)/f(j) by K^2 quadrature: %.6g"%(b,ratio(b)))
def mul(p,q):
    a1,b1,c1,d1=p; a2,b2,c2,d2=q
    return (a1*a2-b1*b2-c1*c2-d1*d2, a1*b2+b1*a2+c1*d2-d1*c2, a1*c2-b1*d2+c1*a2+d1*b2, a1*d2+b1*c2-c1*b2+d1*a2)
def Hmap(q): return (q[0],q[1],-q[2],-q[3])   # Ad_i
def Imap(q): return q
def run(b, twisted, sweeps, seed):
    rnd=random.Random(seed)
    T=Hmap if twisted else Imap
    edges=[(0,1,Imap),(0,2,Imap),(1,3,T),(2,3,Imap),(3,4,Imap),(4,5,T),(4,6,Imap),(5,7,Imap),(6,7,Imap)]
    nb=[[] for _ in range(8)]
    for a,c,R in edges:
        nb[a].append((c,R)); nb[c].append((a,R))   # R = R^-1 here
    s=[(1.0,0.0,0.0,0.0)]*8
    eps=0.9; acc=0; tot=0; acc_sum=0.0; nmeas=0
    for sw in range(sweeps):
        for v in range(8):
            h=[0.0]*4
            for c,R in nb[v]:
                t=R(s[c]); h=[h[i]+t[i] for i in range(4)]
            old=s[v]
            g=[old[i]+eps*rnd.gauss(0,1) for i in range(4)]; nn=math.sqrt(sum(x*x for x in g)); new=tuple(x/nn for x in g)
            dE=b*sum((new[i]-old[i])*h[i] for i in range(4))
            tot+=1
            if dE>=0 or rnd.random()<math.exp(dE):
                s[v]=new; acc+=1
        if sw>=1000:
            # conditional mean of s_y (site 4) given its neighbours, dotted with s_x (site 3)
            h=[0.0]*4
            for c,R in nb[4]:
                t=R(s[c]); h=[h[i]+t[i] for i in range(4)]
            k=b*math.sqrt(sum(x*x for x in h))
            m=besselI(2,k)/besselI(1,k)
            acc_sum+=m*sum(s[3][i]*h[i] for i in range(4))/math.sqrt(sum(x*x for x in h)); nmeas+=1
    return acc_sum/nmeas, acc/tot
b=float(sys.argv[1]); sweeps=int(sys.argv[2]); nb_=int(sys.argv[3])
for tw in (False,True):
    vals=[run(b,tw,sweeps,1000*tw+k)[0] for k in range(nb_)]
    mean=sum(vals)/nb_; sd=math.sqrt(sum((x-mean)**2 for x in vals)/(nb_-1))/math.sqrt(nb_)
    print("b=%.3f %s  MC E[s_x.s_y] = %.5f +- %.5f  (%d batches x %d sweeps)"%(b,"twisted" if tw else "flat   ",mean,sd,nb_,sweeps))
