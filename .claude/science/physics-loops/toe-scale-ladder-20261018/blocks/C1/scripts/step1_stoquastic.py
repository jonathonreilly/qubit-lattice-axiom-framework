#!/usr/bin/env python3
"""Step 1: stoquasticity of H = -g sum_p F_p + V sum_p n_p on the Gauss sector (rho=0), cubic L^3 torus.

Checks:
 A. structural (all L tested): every off-diagonal element of H in the sigma^z (E) basis is -g times a
    nonnegative integer (U_p = s+ s+ s- s- has matrix elements in {0,1}); distinct plaquettes never act as
    the same configuration change (distinct link sets) for L >= 2.
 B. the diagonal +-1 gauge D = prod_{l in Lambda} sigma^z_l with
    Lambda = {x-links, y+z even} U {y-links, z even} anticommutes with every F_p (each plaquette contains
    an odd number of Lambda links) for even L -> D H(g,V) D = H(-g,V) on every Gauss/winding sector.
 C. independent F2 certificate: solve delta(Lambda) = 1 (all plaquettes) over GF(2) for L=2..6;
    for odd L show no solution (the all-ones 2-cochain pairs to L^2 = 1 mod 2 with a torus plane cycle).
 D. exact L=2: Gauss census 9600 / 937 components / largest 864; D H(g) D == H(-g) as sparse matrices;
    spectra of H(+g) and H(-g) agree on the 864 component and on the full sector (all components), V in
    {0, 0.5, 0.9}; E0 at V=0 reproduces the repo value -9.0267209135; ground state in the 864 component.
"""
import os, sys, time
for _v in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_v, "2")
import numpy as np
from scipy.sparse import csr_matrix, diags
from scipy.sparse.csgraph import connected_components

sys.path.insert(0, os.path.dirname(__file__))
from lattice import Lattice

RES = []


def check(name, ok, detail=""):
    RES.append(bool(ok))
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f" :: {detail}" if detail else ""), flush=True)


# ---------------- A/B structural, several L
for L in (2, 3, 4, 6, 8, 10, 12):
    lat = Lattice(L)
    keys = {tuple(sorted(x)) for x in lat.plinks.tolist()}
    distinct = len(keys) == lat.np and all(len(set(x)) == 4 for x in lat.plinks.tolist())
    check(f"A L={L}: {lat.np} plaquettes have pairwise distinct 4-link sets", distinct)
    if L % 2 == 0:
        lam = lat.gauge_set()
        cnt = lam[lat.plinks].sum(axis=1)
        check(f"B L={L}: every plaquette contains an odd number of Lambda links", np.all(cnt % 2 == 1),
              f"counts present {sorted(set(cnt.tolist()))}, |Lambda|={lam.sum()}")


# ---------------- C. GF(2) certificate
def gf2_solve(A, b):
    A = A.copy() % 2
    b = b.copy() % 2
    m, n = A.shape
    M = np.concatenate([A, b[:, None]], axis=1).astype(np.uint8)
    r = 0
    piv = []
    for c in range(n):
        rows = np.nonzero(M[r:, c])[0]
        if len(rows) == 0:
            continue
        k = r + rows[0]
        M[[r, k]] = M[[k, r]]
        nz = np.nonzero(M[:, c])[0]
        nz = nz[nz != r]
        M[nz] ^= M[r]
        piv.append(c)
        r += 1
        if r == m:
            break
    # inconsistent if a zero row has rhs 1
    incons = np.any((M[:, :n].sum(axis=1) == 0) & (M[:, n] == 1))
    if incons:
        return None, r
    x = np.zeros(n, dtype=np.uint8)
    for i, c in enumerate(piv):
        x[c] = M[i, n]
    return x, r


for L in (2, 3, 4, 5, 6):
    lat = Lattice(L)
    A = np.zeros((lat.np, lat.nl), dtype=np.uint8)
    for p in range(lat.np):
        A[p, lat.plinks[p]] = 1
    x, rank = gf2_solve(A, np.ones(lat.np, dtype=np.uint8))
    if L % 2 == 0:
        ok = x is not None and np.all((A.astype(int) @ x.astype(int)) % 2 == 1)
        check(f"C L={L}: GF(2) solution of delta(Lambda)=1 exists (uniform g -> -g is a diagonal gauge)", ok,
              f"rank {rank}, |Lambda_sol| = {int(x.sum()) if x is not None else None}")
    else:
        # plane cycle: all xy plaquettes with z=0
        plane = np.array([(lat.coords[p // 3][2] == 0) and (p % 3 == 0) for p in range(lat.np)])
        bd = (A[plane].sum(axis=0) % 2 == 0).all()
        check(f"C L={L} (odd): no GF(2) solution; obstruction = xy-plane cycle (boundary 0: {bd}) meets all-ones "
              f"cochain in L^2={L*L} (odd) plaquettes", x is None and bd and (L * L) % 2 == 1, f"rank {rank}")

# ---------------- D. exact L = 2
t0 = time.time()
lat = Lattice(2)
idx = np.arange(2 ** 24, dtype=np.int64)
sig_all = None
states = []
for ch in range(16):
    ii = idx[ch * 2 ** 20:(ch + 1) * 2 ** 20]
    bits = (((ii[:, None] >> np.arange(24)) & 1) * 2 - 1).astype(np.int8)
    d = np.zeros((len(ii), lat.nv), dtype=np.int64)
    for l in range(24):
        d[:, lat.tail[l]] += bits[:, l]
        d[:, lat.head[l]] -= bits[:, l]
    states.append(bits[np.all(d == 0, axis=1)])
S = np.vstack(states).astype(np.int64)
ns = len(S)
code = {tuple(s): i for i, s in enumerate(S)}
circ = (S[:, lat.plinks] * lat.psign).sum(axis=2)
flip = np.abs(circ) == 4
nflip = flip.sum(axis=1)
rows, cols, ps = [], [], []
for i in range(ns):
    for p in np.flatnonzero(flip[i]):
        t = S[i].copy()
        t[lat.plinks[p]] *= -1
        rows.append(i)
        cols.append(code[tuple(t)])
        ps.append(p)
rows, cols, ps = map(np.array, (rows, cols, ps))
A = csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(ns, ns))
maxmult = A.max()
ncomp, lab = connected_components(A, directed=False)
sizes = np.bincount(lab)
check("D L=2: Gauss census 9600 states, 937 flip components, largest 864 (repo values)",
      ns == 9600 and ncomp == 937 and sizes.max() == 864, f"{ns}, {ncomp}, {sizes.max()}")
offd = -A  # H off-diagonal part at g = 1
check("D L=2: all off-diagonal entries of H(g=1) are <= 0 and equal to -1 (no multiplicity)",
      offd.max() <= 0 and maxmult == 1 and (A != A.T).nnz == 0, f"max multiplicity {maxmult}")
lam = lat.gauge_set()
dsign = np.where((S[:, lam] == -1).sum(axis=1) % 2 == 1, -1.0, 1.0)  # sigma^z_l = sigma_l
D = diags(dsign)
for V in (0.0, 0.5, 0.9):
    Hp = (-1.0) * A + V * diags(nflip.astype(float))
    Hm = (+1.0) * A + V * diags(nflip.astype(float))
    diff = abs(D @ Hp @ D - Hm).max()
    check(f"D L=2 V={V}: D H(+g) D == H(-g) exactly", diff == 0, f"max |diff| {diff}")
    # spectra: all components with size > 1, both signs
    maxdev = 0.0
    e0 = np.inf
    e0lab = None
    for c in range(ncomp):
        mem = np.flatnonzero(lab == c)
        if len(mem) == 1:
            e = np.array([V * nflip[mem[0]]])
            ep = em = e
        else:
            hp = Hp[mem][:, mem].toarray()
            hm = Hm[mem][:, mem].toarray()
            ep = np.linalg.eigvalsh(hp)
            em = np.linalg.eigvalsh(hm)
        maxdev = max(maxdev, np.abs(ep - em).max())
        if ep[0] < e0 - 1e-12:
            e0, e0lab = ep[0], c
    extra = ""
    ok = maxdev < 1e-9
    if V == 0.0:
        ok = ok and abs(e0 - (-9.0267209135)) < 1e-9 and sizes[e0lab] == 864
        extra = f"; E0 = {e0:.10f} (repo -9.0267209135) in component of size {sizes[e0lab]}"
    check(f"D L=2 V={V}: spectra of H(+g) and H(-g) agree on all 937 components", ok,
          f"max |dE| {maxdev:.2e}; global E0 = {e0:.10f}{extra}")

print(f"elapsed {time.time()-t0:.1f}s")
print(f"TOTAL: PASS={sum(RES)} FAIL={len(RES)-sum(RES)}")
