# Independent validation of vacgas.c on the 2x2x2 torus (bond multiplicity 2, 24 bonds).
import itertools, math, random
from fractions import Fraction
# --- two-valued exact enumeration (float) ---
def nbrs(L):
    nb={}
    for x in range(L):
        for y in range(L):
            for w in range(L):
                i=(x*L+y)*L+w
                nb[i]=[(((x+1)%L)*L+y)*L+w,(((x-1)%L)*L+y)*L+w,(x*L+(y+1)%L)*L+w,(x*L+(y-1)%L)*L+w,(x*L+y)*L+(w+1)%L,(x*L+y)*L+(w-1)%L]
    return nb
L=2; V=8; nb=nbrs(L)
bonds=[(i,j) for i in range(V) for j in nb[i] if i<j]  # each pair appears twice (multiplicity 2) in nb lists -> count via list
allb=[]
for i in range(V):
    for j in nb[i]:
        allb.append((i,j))
# each unordered bond visited from both ends: keep i<j entries only -> 24 entries? check
ub=[(i,j) for (i,j) in allb if i<j]
print("bonds with multiplicity:",len(ub))
def exact_ising(beta,z,g):
    c0=1/math.cosh(beta); c=g*c0
    Z=0;R=0;M2=0;M4=0
    for cfg in itertools.product((-1,0,1),repeat=V):
        w=1.0
        for s in cfg:
            if s!=0: w*=z
        for i,j in ub:
            if cfg[i]!=0 and cfg[j]!=0: w*=c*math.exp(beta*cfg[i]*cfg[j])
        m=sum(cfg)/V**1
        M=sum(cfg)
        Z+=w; R+=w*sum(1 for s in cfg if s)/V; M2+=w*(M/V)**2; M4+=w*(M/V)**4
    R/=Z;M2/=Z;M4/=Z
    return R,M2,1-M4/(3*M2**2)
print("exact ising L=2 beta=.5 z=.5 g=1: rho,m2,U =",exact_ising(0.5,0.5,1.0))
# --- independent Metropolis for the sphere menu (generic proposals) ---
def metro_sphere(beta,z,g,nsweep=150000,ntherm=5000,seed=1):
    random.seed(seed)
    c0=beta/math.sinh(beta); c=g*c0
    n=[0]*V; s=[(0.0,0.0,1.0)]*V
    def rnd_dir():
        u=2*random.random()-1; ph=2*math.pi*random.random(); st=math.sqrt(1-u*u)
        return (st*math.cos(ph),st*math.sin(ph),u)
    def local_w(i,state):
        # weight of site i in state (None=empty or direction), given neighbours (with multiplicity)
        if state is None: return 1.0
        w=z
        for j in nb[i]:
            if n[j]:
                d=state[0]*s[j][0]+state[1]*s[j][1]+state[2]*s[j][2]
                w*=c*math.exp(beta*d)
        return w
    R=0;M2=0;M4=0;cnt=0
    for t in range(nsweep+ntherm):
        for i in range(V):
            cur = s[i] if n[i] else None
            r=random.random()
            if r<0.5:
                # toggle
                new = None if n[i] else rnd_dir()
            else:
                if not n[i]: continue
                # small rotation
                a=[s[i][k]+0.6*random.gauss(0,1) for k in range(3)]
                nn=math.sqrt(sum(x*x for x in a)); new=tuple(x/nn for x in a)
            # symmetric proposals w.r.t. reference measure; accept min(1,w_new/w_old)
            wo=local_w(i,cur); wn=local_w(i,new)
            if random.random()<wn/wo:
                if new is None: n[i]=0
                else: n[i]=1; s[i]=new
        if t>=ntherm:
            N=sum(n); M=[sum(s[i][k] for i in range(V) if n[i]) for k in range(3)]
            m2=sum(x*x for x in M)/V**2
            R+=N/V; M2+=m2; M4+=m2*m2; cnt+=1
    R/=cnt;M2/=cnt;M4/=cnt
    return R,M2,1-M4/(3*M2**2)
print("metropolis sphere L=2 beta=.8 z=.5 g=1: rho,m2,U =",metro_sphere(0.8,0.5,1.0,nsweep=60000))
