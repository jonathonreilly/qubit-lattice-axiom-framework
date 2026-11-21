# GUIDE re-check of Lemma 1.5, Theorem 3.4 (v), Corollary 3.7 and h6 invariance (row 843). Decides nothing.
import math, itertools, cmath
def I(n,x,K=400):
    s=0.0; t=(x/2)**n/math.factorial(n)
    for k in range(K):
        s+=t; t*=(x/2)**2/((k+1)*(k+1+n))
        if t<1e-300*max(1,s): break
    return s
Q8=[(s*(i==0),s*(i==1),s*(i==2),s*(i==3)) for i in range(4) for s in (1,-1)]
T2=Q8+[tuple(x/2 for x in sg) for sg in itertools.product((1,-1),repeat=4)]
def chi(two_j,x):
    th=math.acos(max(-1,min(1,x)))
    if abs(math.sin(th))<1e-12: return (two_j+1)*(1 if x>0 else (-1)**two_j)
    return math.sin((two_j+1)*th)/math.sin(th)
for name,G in [("Q8",Q8),("2T",T2)]:
    m=[round(sum(chi(2*l,g[0]) for g in G)/len(G),6) for l in range(7)]
    n=[round(sum(chi(1,g[0])*chi(2*j2//2 if False else j2,g[0]) for g in G)/len(G),6) for j2 in (3,5,7,9,11)]
    print(name,"m(l), l=0..6:",m," n(j), j=3/2..11/2:",n)
# Theorem 3.4 (v) and Cor 3.7 on a grid
def U(nu,x): a=nu+0.5; return x/(a+math.sqrt(a*a+x*x))
def M(b): return min((b/2)**5/720, math.prod(U(n,b) for n in range(1,6)), 1-5.5/(11+b))
def r2T(b): s=b/2; return (math.sinh(b)+4*math.sinh(s))/(math.cosh(b)+3+8*math.cosh(s))
def rQ8(b): return math.sinh(b)/(math.cosh(b)+3)
worst={}
for k in range(1,6001):
    b=k*0.01
    r52=I(6,b)/I(1,b); r32=I(4,b)/I(1,b); u=I(1,b)/I(0,b)
    for key,val in [("r52<=M",r52-M(b)),("M<r2T",M(b)-r2T(b)),("r2T<=rQ8",r2T(b)-rQ8(b)),("M<I1/I0",M(b)-u),("r32<r2T",r32-r2T(b)),("r32<I1/I0",r32-u)]:
        worst[key]=max(worst.get(key,-9),val)
print("max over beta in (0,60] of (lhs-rhs); all must be <=0 (first) or <0:",{k:round(v,6) for k,v in worst.items()})
# h6 invariance under (1+i+j+k)/2 with q=a+bi+cj+dk -> [[a+bi, c+di],[-c+di, a-bi]]
a=(0.5,0.5,0.5,0.5)
Mt=[[complex(a[0],a[1]),complex(a[2],a[3])],[complex(-a[2],a[3]),complex(a[0],-a[1])]]
h6=lambda x,y: x*y*(x**4-y**4)
import random; random.seed(3)
for conv in ("row","col"):
    err=0
    for _ in range(5):
        x,y=complex(random.random(),random.random()),complex(random.random(),random.random())
        if conv=="row": X,Y=x*Mt[0][0]+y*Mt[1][0], x*Mt[0][1]+y*Mt[1][1]
        else: X,Y=Mt[0][0]*x+Mt[0][1]*y, Mt[1][0]*x+Mt[1][1]*y
        err=max(err,abs(h6(X,Y)-h6(x,y)))
    print("h6 invariance error under (1+i+j+k)/2,",conv,"convention:",err)
