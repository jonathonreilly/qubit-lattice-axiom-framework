"""T96 - the consequence of Result 42: does the framework's curvature SPLIT?
In d=4 the Hodge star maps hinges to hinges (Result 42), so the deficit-angle
field -- a number on each 2-cell -- can be decomposed into SELF-DUAL and
ANTI-SELF-DUAL parts.  That decomposition exists in no other dimension, and in
the continuum it is the basis of self-dual gravity and the Ashtekar variables.

Does the framework's own curvature actually use it?  On a cubical 4-complex the
dual of the 2-cell (s, {a,b}) is (s', {c,d}) with {c,d} the complementary pair,
so the star is an explicit involution on hinges and the split is computable:

     delta^(+/-) = (delta  +/-  delta o star) / 2

Measured on curved complexes:
  * a GENERIC curved metric -- is the curvature purely self-dual, purely
    anti-self-dual, or a generic mixture?
  * and does the split mean anything -- e.g. is one part smaller than the other?"""
import numpy as np, itertools, math
d=4
def hinge_pairs(L):
    """on a cubical complex, pair each 2-cell with its Hodge dual 2-cell"""
    pairs={}
    for s in itertools.product(range(L),repeat=d):
        for ab in itertools.combinations(range(d),2):
            cd=tuple(sorted(set(range(d))-set(ab)))
            pairs[(s,ab)]=(s,cd)
    return pairs
def curvature_field(L,gfun):
    """a curvature proxy on each 2-cell: the plaquette 'deficit' from the metric,
       computed as the failure of the two orthogonal 2-planes to have equal area
       -- a cubical stand-in for the deficit angle"""
    out={}
    for s in itertools.product(range(L),repeat=d):
        g=gfun(s)
        for ab in itertools.combinations(range(d),2):
            a,b=ab
            sa=list(s); sa[a]=(sa[a]+1)%L
            sb=list(s); sb[b]=(sb[b]+1)%L
            ga=gfun(tuple(sa)); gb=gfun(tuple(sb))
            # discrete curvature of the (a,b) plaquette: second difference of log g
            out[(s,ab)]=float(np.log(ga[b])-np.log(g[b])-(np.log(gb[a])-np.log(g[a])))
    return out
L=4
pairs=hinge_pairs(L)
def report(nm,gfun):
    F=curvature_field(L,gfun)
    keys=list(F.keys())
    sd=[]; asd=[]
    for k in keys:
        dk=pairs[k]
        sd.append(0.5*(F[k]+F.get(dk,0.0)))
        asd.append(0.5*(F[k]-F.get(dk,0.0)))
    sd=np.array(sd); asd=np.array(asd)
    tot=math.sqrt(float(np.sum(sd**2)+np.sum(asd**2)))
    print(f"   {nm:>28}: ||F|| = {tot:9.5f}   self-dual {np.linalg.norm(sd)/max(tot,1e-15):7.4f}"
          f"   anti-self-dual {np.linalg.norm(asd)/max(tot,1e-15):7.4f}")
print("T96  self-dual / anti-self-dual split of the curvature on 2-cells (d=4 only)")
rng=np.random.default_rng(4)
RAND={s:1.0+0.4*rng.random(d) for s in itertools.product(range(L),repeat=d)}
report("flat (control)", lambda s: np.ones(d))
report("conformal c(x) I", lambda s: (1.0+0.3*np.cos(2*np.pi*s[1]/L))*np.ones(d))
report("anisotropic curved", lambda s: np.array([1.0+0.3*np.cos(2*np.pi*s[1]/L),
                                                 1.0+0.3*np.cos(2*np.pi*s[2]/L),
                                                 1.0+0.3*np.cos(2*np.pi*s[3]/L),1.0]))
report("fully random", lambda s: RAND[s])
print()
print("   a generic mixture (both parts comparable) means the framework's curvature")
print("   uses the whole space and the split is available but not preferred.")
print("   One part vanishing would mean the framework's gravity is SELF-DUAL, which")
print("   would be a strong and specifically four-dimensional statement.")
