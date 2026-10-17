"""Item (4): direct pair tests in the full 5-qubit model (exact operator algebra).

For a C2 element g with lifts (link signed perm l, matter u in 2O), V = onsite o perm.
Pair state Psi = A|vac>, eigenvalue lambda = <A^dag (V A V^dag)> / <A^dag A> on the
code space (exact Majorana-monomial algebra; non-Clifford matter part expanded).
"""
import sys, itertools, numpy as np
from mj import *
from rot import *
import matter as MT

L = int(sys.argv[1]) if len(sys.argv) > 1 else 6
NGROUPS_FULL = int(sys.argv[2]) if len(sys.argv) > 2 else 6
lat = Lat(L); N = lat.N
g = generators(lat)
gens = g['D'] + g['Pu'] + g['Pd'] + g['W']
G = StabGroup(gens)
print(f'L={L} rank={G.rank} log2dim={5*N-G.rank}')

groups = consistent_link_groups()
print('consistent link groups (order 48):', len(groups))
ML = matter_lifts()

def link_lifts(Gp, R):
    p = tuple(dir_perm(R))
    return [x for x in Gp if x[0] == p]

def c2_class(R):
    if round(np.trace(R)) != -1: return None
    # axis C2 has the rotation axis along a coordinate axis
    ax = [a for a in range(3) if R[a, a] == 1]
    return 'axis' if ax else 'edge'

C2s = [(i, R, c2_class(R)) for i, R in enumerate(ROTS) if c2_class(R)]
print('C2 elements:', len(C2s), {c: sum(1 for x in C2s if x[2] == c) for c in ['axis', 'edge']})

POS = [(1, 2, 0), (2, 1, 1), (1, 0, 2), (0, 1, 1), (1, 1, 2)]
def positions(R):
    out = []
    for x in POS:
        Rx = tuple(int(v) for v in R @ np.array(x))
        if lat.idx(Rx) != lat.idx(x): out.append((x, Rx))
    return out[:2]

NOTEIG = [0]
_pe = pair_eig
def pair_eig(G, act, A):
    r = _pe(G, act, A)
    if abs(r[1] - 1) > 1e-8: NOTEIG[0] += 1
    return r

def check(val, tgt):
    return abs(val[1] - 1) < 1e-8 and abs(val[0] - tgt) < 1e-8

# ---- (a) link-only clean pair lambda_f in the 5-qubit model, all groups
summary = {}
for gi, Gp in enumerate(groups):
    for (ri, R, cls) in C2s:
        for ls in link_lifts(Gp, R):
            M4 = ML[ri][0][2]   # matter lift irrelevant for link-only pair
            act = Action(lat, R, ls, M4)
            for (x, Rx) in positions(R):
                A = path_string(lat, x, Rx)
                lam = pair_eig(G, act, A)
                key = ('lambda_f', cls)
                summary.setdefault(key, set()).add(complex(np.round(lam[0], 8)))
print('(a) link pair lambda_f in 5-qubit model, all groups/lifts/positions:',
      {k: v for k, v in summary.items()})

# ---- (b) doublet pairs, (c) local spinor pairs, (d) local link pairs
res = {}
for gi, Gp in enumerate(groups[:NGROUPS_FULL]):
    for (ri, R, cls) in C2s:
        for ls in link_lifts(Gp, R):
            for (q, D, M4) in ML[ri]:
                act = Action(lat, R, ls, M4)
                w, V = np.linalg.eig(D)
                for (x, Rx) in positions(R):
                    sx, sRx = lat.idx(x), lat.idx(Rx)
                    Sf = path_string(lat, x, Rx)
                    for ev in range(2):
                        e = V[:, ev]; m = w[ev]
                        # doublet pair c_e^dag(x) c_e^dag(Rx) S_f
                        A = poly_mul(poly_mul(c_dag(N, sx, e), c_dag(N, sRx, e)), Sf)
                        lam = pair_eig(G, act, A)
                        res.setdefault(('doublet', cls), set()).add(complex(np.round(lam[0], 8)))
                        res.setdefault(('m^2', cls), set()).add(complex(np.round(m * m, 8)))
                        # reversed operator order variant
                        A2 = poly_mul(Sf, poly_mul(c_dag(N, sRx, e), c_dag(N, sx, e)))
                        lam2 = pair_eig(G, act, A2)
                        res.setdefault(('doublet(alt order)', cls), set()).add(complex(np.round(lam2[0], 8)))
                        # local, D-neutral spinor objects: c_e^dag(x) b_{x,d}  (trivial anyon sector)
                        for d in range(6):
                            Rd = ls[0][d]
                            Lx = poly_mul(c_dag(N, sx, e), to_poly(mono(N, [(sx, d)])))
                            LRx = poly_mul(c_dag(N, sRx, e), to_poly(mono(N, [(sRx, Rd)])))
                            lam3 = pair_eig(G, act, poly_mul(Lx, LRx))
                            res.setdefault(('local c^dag b pair', cls), set()).add(complex(np.round(lam3[0], 8)))
                            # local link-only object b_{x,d} (D + 4W, trivial sector)
                            Bp = to_poly(mul(mono(N, [(sx, d)]), mono(N, [(sRx, Rd)])))
                            lam4 = pair_eig(G, act, Bp)
                            res.setdefault(('local b pair', cls), set()).add(complex(np.round(lam4[0], 8)))
                            # doublet + flux-dressing: doublet pair times local link pair
                for kk in []: pass
    print(f'  group {gi} done', flush=True)
print('pair states that were NOT eigenstates:', NOTEIG[0])
for k in sorted(res):
    print('(b-d)', k, sorted(res[k], key=lambda z: (z.real, z.imag)))
