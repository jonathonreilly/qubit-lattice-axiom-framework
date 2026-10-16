"""Part 3 exact: build the exact orbit basis (entries 0,+-1) of covariant nearest-site walks for a
class, label each of the 11 orbits by its hop type relative to corner 0 (in/out/0 per axis), and
generate the exact unitarity equations  sum_n A_n^dag A_{n+d} = delta_{d0} I  (and A A^dag) as
polynomials in c_j, cbar_j (treated as independent symbols).  Prints the distinct equations."""
import numpy as np, sympy as sp, sys, itertools, pickle
from walks import *

ci = int(sys.argv[1]) if len(sys.argv) > 1 else 3
D = class_D(ci)
S = nn_support()
N = 27 * 64
P = np.zeros((N, N))
for R in ROTS:
    DR = D[rkey(R)].astype(float); Kr = np.kron(DR, DR)
    for n in OFFS:
        i, j = OIDX[tuple(n)], OIDX[tuple(R @ n)]
        P[j * 64:(j + 1) * 64, i * 64:(i + 1) * 64] += Kr
P /= 24
# orbit representatives: source corner vi = 0 (site parity 000), displacement d -> target corner, offset
v0 = np.zeros(3, int)
reps = []
for d in itertools.product([-1, 0, 1], repeat=3):
    d = np.array(d)
    tgt = v0 + d
    vo = np.mod(tgt, 2)
    # target site = 2m + vo with source at 2(m+n) + vi: d = vo - vi - 2n -> n = (vo - vi - d)/2
    n = (vo - v0 - d) // 2
    pos = OIDX[tuple(n)] * 64 + idx(vo) * 8 + idx(v0)
    col = P[:, pos]
    if np.abs(col).max() < 1e-12:
        print("killed orbit", d); continue
    b = col / np.abs(col[pos])
    assert np.allclose(np.abs(b[np.abs(b) > 1e-9]), 1)
    b = np.rint(b).astype(int)
    if not any((np.abs(np.abs(b) - np.abs(r[1])).sum() == 0) for r in reps):
        reps.append((d, b))
def htype(d):
    # corner 0: inward = +1 on every axis
    return "".join({1: "i", -1: "o", 0: "0"}[x] for x in d)
print(f"class {ci}: {len(reps)} orbits:", [htype(d) for d, b in reps])
B = np.array([b.reshape(27, 8, 8) for d, b in reps])
names = [htype(d) for d, b in reps]
c = sp.symbols("c0:%d" % len(reps)); cb = sp.symbols("cb0:%d" % len(reps))
def Asym(conj=False):
    out = []
    for i in range(27):
        M = sp.zeros(8, 8)
        for j in range(len(reps)):
            if B[j, i].any():
                M += (cb[j] if conj else c[j]) * sp.Matrix(B[j, i].tolist())
        out.append(M)
    return out
A = Asym(); Ab = Asym(True)
eqs = set()
for d in itertools.product(range(-2, 3), repeat=3):
    d = np.array(d)
    S1 = sp.zeros(8, 8); S2 = sp.zeros(8, 8)
    for i, n in enumerate(OFFS):
        j = OIDX.get(tuple(n + d))
        if j is not None:
            S1 += Ab[i].T * A[j]
            S2 += A[j] * Ab[i].T
    if not d.any():
        S1 -= sp.eye(8); S2 -= sp.eye(8)
    for e in list(S1) + list(S2):
        e = sp.expand(e)
        if e != 0:
            # normalise sign
            e2 = sp.expand(-e)
            eqs.add(min(e, e2, key=sp.default_sort_key))
eqs = sorted(eqs, key=sp.default_sort_key)
print(len(eqs), "distinct equations")
for e in eqs: print("  ", e)
pickle.dump(dict(names=names, B=B, eqs=[str(e) for e in eqs]), open(f"nn_eqs_class{ci}.pkl", "wb"))
