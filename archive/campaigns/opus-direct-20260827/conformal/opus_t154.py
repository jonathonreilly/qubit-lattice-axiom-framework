"""T154 - IDENTIFYING THE SIX COVARIANT RULES THE AXIOMS PERMIT.

T153: covariance under the axioms' own symmetry (proper cubic rotations acting on
the 6 neighbour directions AND on M_2(C) by spinor conjugation) cuts the space of
nearest-neighbour rules from 96 real dimensions to SIX.  Controls all passed.

Six is small enough to NAME.  Write each neighbour's state as (t_i, v_i) -- trace
part and Pauli-vector part -- attached to the unit direction n_i, and build the
natural covariant scalars and vectors out of them:

   scalars out:   S = sum_i t_i                 (average)
                  D = sum_i n_i . v_i           (DIVERGENCE of the spin field)
   vectors out:   V = sum_i v_i                 (average spin)
                  G = sum_i t_i n_i             (GRADIENT of the scalar)
                  N = sum_i (n_i . v_i) n_i
                  C = sum_i n_i x v_i           (CURL)

If these span the 6-dimensional space, then the axioms permit exactly:
   trace_out  <- a S + b D
   vector_out <- c V + e G + f N + g C
and the presence of a DIVERGENCE and a GRADIENT channel is the interesting part:
those two are precisely the ingredients of a first-order Dirac-type operator,
appearing here as a consequence of covariance alone, with no dynamics assumed.

Note sum_i n_i = 0 over the six faces, so any 'constant' channel drops out --
which is why the count is 6 and not larger."""
import numpy as np, itertools, sys
sys.path.insert(0,".")
from opus_t153 import ROT, herm_action, perm_action, DIRS, IN, OUT, equivariant_dim

d,Pj=equivariant_dim(IN,OUT)
print(f"T154  identifying the {d} covariant rules")
# candidate maps, each written as a 4 x 24 real matrix acting on (t_i, v_i) i=1..6
def build(fn):
    L=np.zeros((4,24))
    for i in range(6):
        for k in range(4):
            e=np.zeros((6,4)); e[i,k]=1.0
            L[:,i*4+k]=fn(e)
    return L
def parts(e):
    t=e[:,0]; v=e[:,1:]
    return t,v
NH=np.array([np.array(x,dtype=float) for x in DIRS])
def f_S(e):
    t,v=parts(e); return np.array([t.sum(),0,0,0])
def f_D(e):
    t,v=parts(e); return np.array([sum(NH[i]@v[i] for i in range(6)),0,0,0])
def f_V(e):
    t,v=parts(e); s=v.sum(axis=0); return np.array([0,*s])
def f_G(e):
    t,v=parts(e); s=sum(t[i]*NH[i] for i in range(6)); return np.array([0,*s])
def f_N(e):
    t,v=parts(e); s=sum((NH[i]@v[i])*NH[i] for i in range(6)); return np.array([0,*s])
def f_C(e):
    t,v=parts(e); s=sum(np.cross(NH[i],v[i]) for i in range(6)); return np.array([0,*s])
cands=[("S  = sum t_i          (scalar avg)",f_S),
       ("D  = sum n_i . v_i    (DIVERGENCE)",f_D),
       ("V  = sum v_i          (vector avg)",f_V),
       ("G  = sum t_i n_i      (GRADIENT)",f_G),
       ("N  = sum (n_i.v_i) n_i",f_N),
       ("C  = sum n_i x v_i    (CURL)",f_C)]
print(f"   {'candidate':>38} {'nonzero?':>9} {'equivariant?':>13}")
mats=[]
for nm,fn in cands:
    L=build(fn)
    nz=np.abs(L).max()
    res=max(np.abs(B@L@np.linalg.inv(A)-L).max() for A,B in zip(IN,OUT))
    print(f"   {nm:>38} {nz:9.3f} {res:13.2e}")
    if nz>1e-12: mats.append((nm,L))
M=np.array([L.ravel() for nm,L in mats])
r=np.linalg.matrix_rank(M,tol=1e-9)
print()
print(f"   these {len(mats)} candidates span {r} dimensions of the {d}-dimensional covariant space")
if r==d:
    print(f"   -> THEY ARE A COMPLETE BASIS: the axioms permit exactly")
    print(f"        trace_out  =  a*S + b*D")
    print(f"        vector_out =  c*V + e*G + f*N + g*C     (minus {len(mats)-d} relation(s))")
else:
    print(f"   -> incomplete; {d-r} covariant direction(s) are NOT among these natural forms")
    # find what's missing
    U,s,Vt=np.linalg.svd(M)
    print(f"      singular values of the candidate set: {np.round(s,6)}")
print()
print("   A DIVERGENCE channel and a GRADIENT channel both appearing means the")
print("   axioms' covariance alone already supplies the two ingredients of a")
print("   first-order Dirac-type operator -- with no dynamics assumed anywhere.")
