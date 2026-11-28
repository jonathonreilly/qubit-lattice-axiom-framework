# GUIDE only (row 843). No proof step rests on this output.
import math, itertools, random
def I(n,x,K=200):
    s=0.0; t=(x/2)**n/math.factorial(n)
    for k in range(K):
        s+=t; t*= (x/2)**2/((k+1)*(k+1+n))
        if t<1e-300: break
    return s
def rj(j,b): return I(int(2*j+1),b)/I(1,b)
def rQ8(b): return math.sinh(b)/(math.cosh(b)+3)
def r2T(b): s=b/2; return (math.sinh(b)+4*math.sinh(s))/(math.cosh(b)+3+8*math.cosh(s))
def r2Tp(b): s=b/2; return (math.sinh(b)-2*math.sinh(s))/(math.cosh(b)+3+8*math.cosh(s))
print("beta r1/2 r3/2 r5/2 rQ8 r2T r2T' I1/I0 | r5/2/r2T r3/2/rQ8 r1/2-r2T")
for b in [0.25,0.5,1.0,1.15,1.5,2.0,2.15,2.5,3.0,3.2,5.7,10,20]:
    a=[rj(.5,b),rj(1.5,b),rj(2.5,b),rQ8(b),r2T(b),r2Tp(b),I(1,b)/I(0,b)]
    print(f"{b:5.2f} "+" ".join(f"{v:.4g}" for v in a)+f" | {a[2]/a[4]:.3g} {a[1]/a[3]:.3g} {a[0]-a[4]:.3g}")
# spin law of one plaquette: w_j = (2/b) d_j^2 I_{2j+1}(b) e^{-b}
print("spin law: beta, sum_w (check 1), P(j>=3/2 half-int), P(j>=5/2 half-int), P(j>=2 any), P(j>=5/2 any), P(j>=11/2 any)")
for b in [0.5,1.0,1.5,2.0,2.5,3.0]:
    w={n/2:(2/b)*(n+1)**2*I(n+1,b)*math.exp(-b) for n in range(0,60)}
    tot=sum(w.values())
    ho=lambda jm: sum(v for j,v in w.items() if j>=jm and (2*j)%2==1)
    an=lambda jm: sum(v for j,v in w.items() if j>=jm)
    print(f"{b:4.1f} {tot:.6f} {ho(1.5):.4g} {ho(2.5):.4g} {an(2):.4g} {an(2.5):.4g} {an(5.5):.3g}")
# groups as quaternion lists
Q8=[(s*(i==0),s*(i==1),s*(i==2),s*(i==3)) for i in range(4) for s in (1,-1)]
T2=Q8+[tuple(x/2 for x in sg) for sg in itertools.product((1,-1),repeat=4)]
def qm(a,b):
    a0,a1,a2,a3=a;b0,b1,b2,b3=b
    return (a0*b0-a1*b1-a2*b2-a3*b3,a0*b1+a1*b0+a2*b3-a3*b2,a0*b2-a1*b3+a2*b0+a3*b1,a0*b3+a1*b2-a2*b1+a3*b0)
def inv(a): return (a[0],-a[1],-a[2],-a[3])
a=(.5,.5,.5,.5); bq=(.5,.5,-.5,-.5)
print("[a,b] =",qm(qm(a,bq),inv(qm(bq,a))))
# sup covariance of q under exp(F.q)
def cov(G,F):
    ws=[math.exp(sum(f*x for f,x in zip(F,g))) for g in G]; Z=sum(ws)
    m=[sum(w*g[i] for w,g in zip(ws,G))/Z for i in range(4)]
    C=[[sum(w*g[i]*g[j] for w,g in zip(ws,G))/Z-m[i]*m[j] for j in range(4)] for i in range(4)]
    # largest eigenvalue by power iteration
    v=[1,0.3,0.2,0.1]
    for _ in range(200):
        u=[sum(C[i][j]*v[j] for j in range(4)) for i in range(4)]; n=math.sqrt(sum(x*x for x in u)); v=[x/n for x in u]
    return sum(v[i]*sum(C[i][j]*v[j] for j in range(4)) for i in range(4))
random.seed(1)
for name,G in [("Q8",Q8),("2T",T2)]:
    best=0;bF=None
    for _ in range(20000):
        r=random.expovariate(0.15); d=[random.gauss(0,1) for _ in range(4)]; n=math.sqrt(sum(x*x for x in d))
        F=[r*x/n for x in d]; c=cov(G,F)
        if c>best: best,bF=c,F
    print(name,"sup cov (random search) ~",round(best,5),"at |F| =",round(math.sqrt(sum(x*x for x in bF)),3))
for nm,m6 in [("SU2",5/64),("2T",3/32),("Q8",1/4)]:
    print(nm,"q6(1/2) =",m6**(1/6)*math.sinh(.5)*math.cosh(.5)**8)
