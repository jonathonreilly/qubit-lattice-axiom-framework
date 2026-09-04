"""T7 -- the O(delta^2) conical term.  For a flat 2D cone of total angle theta = 2pi - delta
the heat-trace corner coefficient is c(theta) = (4 pi^2 - theta^2)/(24 pi theta)
                                             = delta/(12 pi) + delta^2/(48 pi^2) + ...
so for a piecewise-flat 4-manifold
    (4 pi s)^2 K = Vol + s [ (1/3) sum A_h delta_h  +  (1/(12 pi)) sum A_h delta_h^2 ] + O(s^2).
The first bracket is S_Regge/3.  Measure the size of the second relative to it."""
import math, itertools, numpy as np
from collections import defaultdict
from kuhn import W, simplex, hinge_area_angle, TRIPLES

def hinge_sums(L, eps, P, kk):
    ang=defaultdict(float); area={}
    for p0 in range(L):
        for wi in range(24):
            w=W[wi]; V,K5,Gt = simplex(p0,wi,eps,P,kk)
            for tri,rest in TRIPLES:
                A,th = hinge_area_angle(Gt,tri,rest)
                vs=sorted(tuple([int(p0+w[a][0])]+[int(x) for x in w[a][1:]]) for a in tri)
                v0=np.array(vs[0])
                key=(int(v0[0])%L, tuple(np.array(vs[1])-v0), tuple(np.array(vs[2])-v0))
                ang[key]+=th; area[key]=A
    d=np.array([2*math.pi-ang[k] for k in ang]); a=np.array([area[k] for k in ang])
    return float((a*d).sum())*L**3, float((a*d*d).sum())*L**3, np.abs(d).max(), len(ang)

print(" L   n  channel     S_Regge=sum A d     sum A d^2    max|deficit|   "
      "cone correction (1/12pi)sum A d^2 / (S_Regge/3)")
for L,n in ((16,1),(32,1),(64,1),(32,2)):
    for P,nm in (((0,1,-1,0),'traceless'),((1,1,1,1),'conformal')):
        kk=2*math.pi*n/L
        S,S2,dmax,nh = hinge_sums(L,eps:=0.05,P,kk)
        print(f"{L:3d} {n:3d}  {nm:10s} {S:14.5f} {S2:14.6e}  {dmax:11.4e}    "
              f"{(S2/(12*math.pi))/(S/3):+.5f}")
