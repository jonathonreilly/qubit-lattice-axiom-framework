import itertools, math, random
from fractions import Fraction as Fr
# quaternions as 4-tuples of Fractions
def qmul(a,b):
    a0,a1,a2,a3=a; b0,b1,b2,b3=b
    return (a0*b0-a1*b1-a2*b2-a3*b3, a0*b1+a1*b0+a2*b3-a3*b2,
            a0*b2-a1*b3+a2*b0+a3*b1, a0*b3+a1*b2-a2*b1+a3*b0)
def neg(a): return tuple(-x for x in a)
one=(Fr(1),Fr(0),Fr(0),Fr(0))
Q8=[]
for s in (1,-1):
    for i in range(4):
        v=[Fr(0)]*4; v[i]=Fr(s); Q8.append(tuple(v))
T24=list(Q8)
for signs in itertools.product((1,-1),repeat=4):
    T24.append(tuple(Fr(s,2) for s in signs))
def counts(G,name):
    idx={g:n for n,g in enumerate(G)}
    n=len(G)
    # comm[a][b]= +1 if ab=ba, -1 if ab=-ba, 0 otherwise
    comm=[[0]*n for _ in range(n)]
    for a in range(n):
        for b in range(n):
            ab=qmul(G[a],G[b]); ba=qmul(G[b],G[a])
            comm[a][b]= 1 if ab==ba else (-1 if ab==neg(ba) else 0)
    def N(tw):  # tw = set of pairs (mu,nu) twisted, 4 directions
        c=0
        for t in itertools.product(range(n),repeat=4):
            ok=True
            for mu in range(4):
                for nu in range(mu+1,4):
                    want=-1 if (mu,nu) in tw else 1
                    if comm[t[mu]][t[nu]]!=want: ok=False;break
                if not ok:break
            if ok:c+=1
        return c
    N0=N(set()); N1=N({(0,1)}); N2=N({(0,1),(0,2)}); N3=N({(0,1),(0,2),(0,3)}); Nk=N({(0,1),(2,3)})
    x=N1/N0
    aE=(N0+N1)/(2*n); aO=(N0-N1)/(2*n)
    print(name,"|G|",n,"N0",N0,"N(12)",N1,"N(01,02)",N2,"N(01,02,03)",N3,"N(01,23)",Nk)
    print("  x_inf=%.4f F_v=%.4f F_e=%.4f  dim_even=%.1f dim_odd=%.1f D_even=%.4f  threshold 2D+1.1=%.3f"%(
        x,-math.log(x),math.log(aE/aO),aE,aO,math.log(aE),2*math.log(aE)+1.1))
counts(Q8,"Q8")
counts(T24,"2T")
# (2) Gaussian flux model for the Coulomb phase: weights q^{e^2}, q=exp(-1/(2 beta r))
def xq(q,N=200):
    s3=sum(q**(e*e) for e in range(-N,N+1)); s4=sum((-1)**(e%2)*q**(e*e) for e in range(-N,N+1))
    return s4/s3
print("Coulomb flux model: sheet doubling r->2r means q->sqrt(q)")
for q in (1e-2,1e-4,1e-8,1e-12):
    Fv1=-math.log(xq(q)); Fv2=-math.log(xq(math.sqrt(q)))
    print("  q=%.0e F_v=%.3e F_v(doubled)=%.3e ratio=%.3e  2*sqrt(F_v)=%.3e"%(q,Fv1,Fv2,Fv2/Fv1,2*math.sqrt(Fv1)))
# symmetric torus r=1: x as a function of beta
for beta in (0.5,1.0,2.0,4.0):
    q=math.exp(-1/(2*beta)); x=xq(q); print("  beta=%.1f r=1: x=%.5f F_e=%.5f F_v=%.4f"%(beta,x,-math.log((1-x)/(1+x)),-math.log(x)))
# (3) ladder algebra check with random spectra
random.seed(1)
bad=0
for trial in range(20000):
    ne=random.randint(1,6); no=random.randint(1,6); n=random.randint(1,5)
    ev=[1.0]+[random.random() for _ in range(ne-1)]
    od=[random.random()*random.random() for _ in range(no)]
    ap=lambda m: sum(v**m for v in ev); am=lambda m: sum(v**m for v in od)
    if am(n)>=ap(n): continue
    Fe=lambda m: -math.log(am(m)/ap(m))
    Dev=math.log(ap(n))
    if Fe(2*n) < 2*Fe(n)-2*Dev-1e-12: bad+=1
    # F1: n*E_odd >= Fe - D
    Eodd=-math.log(max(od))
    if n*Eodd < Fe(n)-Dev-1e-12: bad+=1
print("plane doubling / flux gap inequality violations:",bad)
# duality identity
for x in (0.01,0.3,0.414213562,0.9,0.999):
    Fv=-math.log(x); Fe=-math.log((1-x)/(1+x)); print("  x=%.3f sinh*sinh=%.12f"%(x,math.sinh(Fv)*math.sinh(Fe)))
