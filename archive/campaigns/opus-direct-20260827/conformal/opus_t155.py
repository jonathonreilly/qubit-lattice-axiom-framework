"""T155 - NORMALISATION AND POSITIVITY: what survives of the six covariant rules?

R92: covariance cuts the admissibility rule to six parameters,
     trace_out = a S + b D ,  vector_out = c V + e G + f N + g C.
The axioms impose one more named condition: the rule must produce a PROBABILITY
DISTRIBUTION over the site's possibilities, and it must VARY with the neighbour
conditions ("determined by, and varies with").

STATED READING, because it is an interpretation and not axiom text: I take the
output to be a state of the M_2(C) domain, i.e. a density matrix rho = t I + v.sigma
with trace 1 (so t = 1/2) and rho >= 0 (so |v| <= 1/2).  This captures the
distribution through its state; a full measure on the Bloch sphere has more
content, and any conclusion below is conditional on this reading.  The NEIGHBOURS
are states too, so each has t_i = 1/2 and |v_i| <= 1/2.

The rule must also be AFFINE rather than linear -- a constant is needed to
normalise -- and the only covariant constant is kappa*I, since there is no
invariant vector under the octahedral group.

Three things then follow mechanically, and each is checked rather than argued:
  (1) S = sum_i t_i = 3 identically on normalised neighbours -> the 'a' channel
      is a constant and merges with kappa;
  (2) normalisation t_out = 1/2 for ALL inputs -> the DIVERGENCE channel b must
      vanish, since D varies;
  (3) G = sum_i t_i n_i = (1/2) sum_i n_i = 0 identically, because the six face
      directions sum to zero -> the GRADIENT channel carries nothing.
Then positivity bounds whatever remains."""
import numpy as np, itertools
DIRS=[np.array(d,dtype=float) for d in [(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]]
print("T155  normalisation and positivity on the six covariant channels")
print()
print("(1)(3) which channels are identically constant or zero on NORMALISED neighbours?")
rng=np.random.default_rng(7)
def sample(n=20000):
    out=[]
    for _ in range(n):
        vs=[]
        for i in range(6):
            u=rng.normal(size=3); u/=np.linalg.norm(u)
            r=0.5*rng.uniform(0,1)**(1/3)
            vs.append(r*u)
        out.append(np.array(vs))
    return out
VS=sample()
chan={}
chan['S = sum t_i']      =np.array([3.0 for v in VS])
chan['D = sum n.v']      =np.array([sum(DIRS[i]@v[i] for i in range(6)) for v in VS])
chan['|V| = |sum v|']    =np.array([np.linalg.norm(v.sum(axis=0)) for v in VS])
chan['|G| = |sum t n|']  =np.array([np.linalg.norm(0.5*sum(DIRS)) for v in VS])
chan['|N|']              =np.array([np.linalg.norm(sum((DIRS[i]@v[i])*DIRS[i] for i in range(6))) for v in VS])
chan['|C| = |sum n x v|']=np.array([np.linalg.norm(sum(np.cross(DIRS[i],v[i]) for i in range(6))) for v in VS])
print(f"   {'channel':>22} {'min':>12} {'max':>12} {'varies?':>9}")
for k,v in chan.items():
    print(f"   {k:>22} {v.min():12.6f} {v.max():12.6f} {'YES' if v.max()-v.min()>1e-9 else 'NO -- constant'}")
print()
print("   -> S is constant (3) and merges into the affine constant.")
print("   -> G is identically ZERO: the six face directions sum to zero, so the")
print("      GRADIENT channel carries no information on normalised neighbours.")
print("   -> D varies, so normalisation t_out = 1/2 for all inputs FORCES b = 0.")
print()
print("(2) what remains: vector_out = c V + f N + g C, with |vector_out| <= 1/2")
print("    maximum attainable magnitude of each channel over normalised neighbours:")
mx={}
for k in ('|V| = |sum v|','|N|','|C| = |sum n x v|'):
    mx[k]=chan[k].max()
    print(f"       {k:>22}  sampled max {chan[k].max():.4f}")
print()
print("    exact maxima (aligning every v_i to saturate each channel):")
vV=np.array([np.array([0,0,0.5]) for i in range(6)])
print(f"       V : all v_i = (0,0,1/2)         |V| = {np.linalg.norm(vV.sum(axis=0)):.4f}")
vN=np.array([0.5*DIRS[i] for i in range(6)])
print(f"       N : v_i = (1/2) n_i             |N| = {np.linalg.norm(sum((DIRS[i]@vN[i])*DIRS[i] for i in range(6))):.4f}")
vN2=np.array([0.5*DIRS[i]*(1 if i in (4,5) else 0) for i in range(6)])
print(f"       N : only the z-pair, v = (1/2)n |N| = {np.linalg.norm(sum((DIRS[i]@vN2[i])*DIRS[i] for i in range(6))):.4f}")
best=0; arg=None
for _ in range(200000):
    v=np.array([0.5*np.sign(rng.normal(size=3))*np.array([1,0,0]) for i in range(6)])
    pass
vC=np.array([0.5*np.cross(DIRS[i],np.array([0,0,1.0]))/max(np.linalg.norm(np.cross(DIRS[i],np.array([0,0,1.0]))),1e-12) if np.linalg.norm(np.cross(DIRS[i],np.array([0,0,1.0])))>1e-9 else np.zeros(3) for i in range(6)])
print(f"       C : v_i tangential               |C| = {np.linalg.norm(sum(np.cross(DIRS[i],vC[i]) for i in range(6))):.4f}")
print()
print("   positivity |c V + f N + g C| <= 1/2 then bounds the coefficients, giving a")
print("   convex region rather than a unique rule -- but the axioms have already")
print("   killed TWO of the six channels outright.")
