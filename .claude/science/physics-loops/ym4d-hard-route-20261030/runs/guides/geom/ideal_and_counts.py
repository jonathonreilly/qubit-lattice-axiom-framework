# GUIDE only. Ideal doubling map threshold and flat-connection counts for Q8 and 2T.
import itertools
from fractions import Fraction as Fr

def psi(r): return 2*r/(1+r*r)
def G_plane_first(r): return psi(psi(r))**4
def G_sheet_first(r): return psi(psi(r**4))
def root(G, lo, hi):
    for _ in range(200):
        mid = (lo+hi)/2
        if G(mid) - mid > 0: hi = mid
        else: lo = mid
    return (lo+hi)/2
print("G_plane_first(0.1)=%.6f  G(0.2)=%.6f  G(0.5)=%.6f" % (G_plane_first(0.1), G_plane_first(0.2), G_plane_first(0.5)))
print("threshold plane-first r* = %.6f" % root(G_plane_first, 0.05, 0.9))
print("threshold sheet-first r* = %.6f" % root(G_sheet_first, 0.05, 0.999))

# quaternion groups with exact rational coordinates
def qmul(a, b):
    a0,a1,a2,a3 = a; b0,b1,b2,b3 = b
    return (a0*b0-a1*b1-a2*b2-a3*b3, a0*b1+a1*b0+a2*b3-a3*b2,
            a0*b2-a1*b3+a2*b0+a3*b1, a0*b3+a1*b2-a2*b1+a3*b0)
def neg(a): return tuple(-x for x in a)
one = (Fr(1),Fr(0),Fr(0),Fr(0))
Q8 = []
for i in range(4):
    for s in (1,-1):
        v = [Fr(0)]*4; v[i] = Fr(s); Q8.append(tuple(v))
T24 = list(Q8) + [tuple(Fr(s,2) for s in signs) for signs in itertools.product((1,-1), repeat=4)]
def counts(G):
    comm = {}; anti = {}
    for a in G:
        for b in G:
            ab = qmul(a,b); ba = qmul(b,a)
            comm[(a,b)] = (ab == ba); anti[(a,b)] = (ab == neg(ba))
    n_per = 0; n_tw = 0
    for a in G:
        for b in G:
            c_ab = comm[(a,b)]; a_ab = anti[(a,b)]
            if not (c_ab or a_ab): continue
            # c, d must commute with a, b and with each other
            cs = [c for c in G if comm[(a,c)] and comm[(b,c)]]
            n_cd = sum(1 for c in cs for d in cs if comm[(c,d)])
            if c_ab: n_per += n_cd
            if a_ab: n_tw += n_cd
    return n_per, n_tw
for name, G in (("Q8", Q8), ("2T", T24)):
    assert len(set(G)) == len(G)
    # closure check
    S = set(G)
    assert all(qmul(a,b) in S for a in G for b in G)
    n_per, n_tw = counts(G)
    print(name, "order", len(G), "periodic flat 4-tuples", n_per, "twisted (n12) flat 4-tuples", n_tw, "ratio", Fr(n_tw, n_per), float(Fr(n_tw,n_per)))
