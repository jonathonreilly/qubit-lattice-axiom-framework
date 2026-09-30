"""Independent re-derivation of Test B (Bloch/function-space formulation, no U_g, no hop matrices).
H(k) = e(k) + d(k).sigma.  Covariance under rotation action g -> rho(g):  e(gk)=e(k), d(gk)=rho(g) d(k).
(rotation acts on momentum by g; on the Bloch vector by rho(g).)  Nearest-neighbour: basis {1, cos k_i, sin k_i}.
Range-1: basis {1, cos(k.v), sin(k.v)} for the 13 half-vectors v in {-1,0,1}^3.
"""
import itertools, sys
import numpy as np
sys.path.insert(0, '../../attacks/T20_scratch')

def cubic_rotations():
    out=[]
    for p in itertools.permutations(range(3)):
        for s in itertools.product([1,-1],repeat=3):
            M=np.zeros((3,3),int)
            for i in range(3): M[i,p[i]]=s[i]
            if round(np.linalg.det(M))==1: out.append(M)
    return out
O=cubic_rotations()
def psign(M): return int(round(np.linalg.det(np.abs(M))))
def rho(kind,g):
    if kind=='trivial': return np.eye(3)
    if kind=='sign':
        s=psign(g); return np.diag([1.,s,s])
    if kind=='axis':
        s=psign(g); return s*np.abs(g).astype(float)
    if kind=='full': return g.astype(float)
# homomorphism check (independent)
for kind in ['trivial','sign','axis','full']:
    for a in O:
        for b in O:
            assert np.allclose(rho(kind,a)@rho(kind,b),rho(kind,a@b)),kind

def half_vectors(R):
    vs=[]
    for v in itertools.product(range(-R,R+1),repeat=3):
        if any(v) and next(x for x in v if x)>0: vs.append(np.array(v))
    return vs
def nn_vectors():
    return [np.array(e) for e in np.eye(3,dtype=int)]

def basis_funcs(vs):
    # list of functions k-> value ; index 0 constant
    fs=[lambda k: 1.0]
    for v in vs:
        fs.append(lambda k,v=v: np.cos(k@v))
        fs.append(lambda k,v=v: np.sin(k@v))
    return fs

def family(kind, vs, nsamp=60, seed=0):
    rng=np.random.default_rng(seed)
    fs=basis_funcs(vs); nb=len(fs)
    # unknowns: e coeffs (nb), d coeffs (3*nb)
    nun=4*nb
    rows=[]
    ks=rng.uniform(-np.pi,np.pi,size=(nsamp,3))
    for g in O:
        R=rho(kind,g)
        for k in ks:
            gk=g@k     # momentum transforms with g
            fk=np.array([f(k) for f in fs]); fgk=np.array([f(gk) for f in fs])
            # e(gk)-e(k)=0
            r=np.zeros(nun); r[:nb]=fgk-fk; rows.append(r)
            # d(gk) - R d(k) = 0  (3 rows)
            for i in range(3):
                r=np.zeros(nun)
                r[nb*(1+i):nb*(2+i)]+=fgk
                for j in range(3):
                    r[nb*(1+j):nb*(2+j)]-=R[i,j]*fk
                rows.append(r)
    M=np.array(rows)
    u,s,vt=np.linalg.svd(M)
    rank=(s>1e-9*s[0]).sum()
    null=vt[rank:]
    return null,fs,nb

def evaluate(x,fs,nb,k):
    fk=np.array([f(k) for f in fs])
    e=x[:nb]@fk
    d=np.array([x[nb*(1+i):nb*(2+i)]@fk for i in range(3)])
    return e,d

if __name__=='__main__':
    for label,vs in [('NN',nn_vectors()),('range1',half_vectors(1)),('range2',half_vectors(2))]:
        print('==',label,'hops(half)=',len(vs))
        for kind in ['trivial','sign','axis','full']:
            null,fs,nb=family(kind,vs)
            print(f'  {kind:8s} covariant dimension (e and d together) = {len(null)}')
