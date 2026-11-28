# GUIDE sanity check of Lemma P on small closed surfaces: Monte Carlo of E prod |x_p| (SU(2) Haar links)
import numpy as np, itertools
rng=np.random.default_rng(1)
def haar(n):
    v=rng.normal(size=(n,4)); return v/np.linalg.norm(v,axis=1,keepdims=True)
def qmul(a,b):
    a0,a1,a2,a3=a[...,0],a[...,1],a[...,2],a[...,3]; b0,b1,b2,b3=b[...,0],b[...,1],b[...,2],b[...,3]
    return np.stack([a0*b0-a1*b1-a2*b2-a3*b3, a0*b1+a1*b0+a2*b3-a3*b2, a0*b2-a1*b3+a2*b0+a3*b1, a0*b3+a1*b2-a2*b1+a3*b0],-1)
def qinv(a): return a*np.array([1,-1,-1,-1])
def plaq_x(U,x,mu,nu):
    # links keyed by (site tuple, dir); plaquette at site x in plane (mu,nu)
    def e(d): v=[0]*4; v[d]=1; return tuple(v)
    def add(a,b): return tuple(i+j for i,j in zip(a,b))
    l1=U[(x,mu)]; l2=U[(add(x,e(mu)),nu)]; l3=qinv(U[(add(x,e(nu)),mu)]); l4=qinv(U[(x,nu)])
    h=qmul(qmul(qmul(l1,l2),l3),l4); return h[...,0]
def run(faces,N=400000):
    links=set()
    def e(d): v=[0]*4; v[d]=1; return tuple(v)
    def add(a,b): return tuple(i+j for i,j in zip(a,b))
    for (x,mu,nu) in faces:
        links|={(x,mu),(add(x,e(mu)),nu),(add(x,e(nu)),mu),(x,nu)}
    U={l:haar(N) for l in links}
    prod=np.ones(N)
    for (x,mu,nu) in faces: prod*=np.abs(plaq_x(U,x,mu,nu))
    return prod.mean(), prod.std()/np.sqrt(N), len(links)
M1=4/(3*np.pi); M2=0.25; M3=8/(15*np.pi); M4=1/8
# unit cube boundary in dirs 0,1,2 at origin
o=(0,0,0,0); def_e=lambda d: tuple(1 if i==d else 0 for i in range(4))
cube=[(o,0,1),(def_e(2),0,1),(o,0,2),(def_e(1),0,2),(o,1,2),(def_e(0),1,2)]
m,se,L=run(cube); print("cube: E prod|x| =",m,"+-",se," Lemma P bound M2*M1^4 =",M2*M1**4," Finner 2^-6 =",2**-6)
# two cubes sharing only the edge from (0,0,0,0) dir 0: second cube in dirs 0,2,3 shifted to share edge: cube2 = [0,1]x{y in[-1,0]}... use dirs 0,3 and 1 negative side
c2o=(0,-1,0,-1)  # cube in dirs 0,1,3 at (0,-1,0,-1): contains edge (0,0,0,0)-(1,0,0,0)? its edges at y in{-1,0}, w in {-1,0}: yes edge at y=0,w=0
def ad(a,b): return tuple(i+j for i,j in zip(a,b))
cube2=[(c2o,0,1),(ad(c2o,def_e(3)),0,1),(c2o,0,3),(ad(c2o,def_e(1)),0,3),(c2o,1,3),(ad(c2o,def_e(0)),1,3)]
m2,se2,L2=run(cube+cube2); 
# Lemma P bound for this branched surface: BFS multiset depends on order; a safe upper bound uses worst-case k pattern; compute exact via simple BFS
print("two cubes glued at an edge: E prod|x| =",m2,"+-",se2," links",L2)
print(" candidate bounds: M2*M1^10 =",M2*M1**10,"  M2*M1^8*M2 =",M2*M1**8*M2, " Finner(per-face exp4 on 4 faces) =",2**-12*2)
