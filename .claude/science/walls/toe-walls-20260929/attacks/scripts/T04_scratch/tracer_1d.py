#!/usr/bin/env python3
"""1D open chain: content-distinguishable tracer in a free-fermion sea vs identical fermions.
Exact evolution (no Bell sampling). See PREREG.md Addendum B."""
import itertools, numpy as np, scipy.sparse as sp
from scipy.sparse.linalg import expm_multiply

L, N0, P0 = 16, 7, 8
# free open-chain orbitals
j = np.arange(L)
orb = np.array([np.sqrt(2/(L+1))*np.sin(np.pi*(k+1)*(j+1)/(L+1)) for k in range(L)])  # orb[k, site]
sea_orb = orb[:N0]                         # lowest N0 orbitals
def sea_amp(S):                             # S sorted tuple of sites
    return np.linalg.det(sea_orb[:, list(S)])

# ---- distinguishable model: basis (tracer p, sea set S with |S|=N0, p not in S)
def bit(s): return 1 << s
basis = []
for p in range(L):
    others = [s for s in range(L) if s != p]
    for S in itertools.combinations(others, N0):
        basis.append((p, sum(bit(s) for s in S)))
idx = {b: i for i, b in enumerate(basis)}
rows, cols = [], []
for (p, m), i in idx.items():
    for q in (p-1, p+1):                    # tracer hop
        if 0 <= q < L and not (m & bit(q)):
            rows.append(idx[(q, m)]); cols.append(i)
    for s in range(L):                      # sea hops
        if m & bit(s):
            for q in (s-1, s+1):
                if 0 <= q < L and q != p and not (m & bit(q)):
                    rows.append(idx[(p, (m ^ bit(s)) | bit(q))]); cols.append(i)
n = len(basis)
Hd = sp.csr_matrix((-np.ones(len(rows)), (rows, cols)), shape=(n, n))
assert abs(Hd - Hd.T).max() == 0
psi0 = np.zeros(n)
for (p, m), i in idx.items():
    if p == P0:
        S = tuple(s for s in range(L) if m & bit(s))
        psi0[i] = sea_amp(S)
psi0 /= np.linalg.norm(psi0)

# ---- identical fermions (1D nearest neighbour hops: all amplitudes -1 on the ordered basis)
ib = list(itertools.combinations(range(L), N0+1))
iidx = {b: i for i, b in enumerate(ib)}
r2, c2 = [], []
for b, i in iidx.items():
    for s in b:
        for q in (s-1, s+1):
            if 0 <= q < L and q not in b:
                nb = tuple(sorted([x for x in b if x != s] + [q]))
                r2.append(iidx[nb]); c2.append(i)
Hi = sp.csr_matrix((-np.ones(len(r2)), (r2, c2)), shape=(len(ib), len(ib)))
phi0 = np.zeros(len(ib))
for b, i in iidx.items():
    if P0 in b:
        rest = tuple(s for s in b if s != P0)
        k = sum(1 for s in rest if s < P0)                 # c^dag_P0 c^dag_rest ordering sign
        phi0[i] = (-1) ** k * sea_amp(rest)
phi0 /= np.linalg.norm(phi0)

def dens_d(psi):
    d = np.zeros(L); pr = psi**2
    for (p, m), i in idx.items():
        w = pr[i]
        d[p] += w
        for s in range(L):
            if m & bit(s): d[s] += w
    return d
def tracer(psi):
    d = np.zeros(L); pr = psi**2
    for (p, m), i in idx.items(): d[p] += pr[i]
    return d
def dens_i(psi):
    d = np.zeros(L); pr = psi**2
    for b, i in iidx.items():
        for s in b: d[s] += pr[i]
    return d

# sea density (N0 fermions, free ground state)
nsea = (sea_orb**2).sum(axis=0)
x = np.arange(L)
times = [0.0, 0.75, 1.5, 2.25, 3.0]
pd, pi_ = psi0.astype(complex), phi0.astype(complex)
print(f"L={L} N0={N0} dim_dist={n} dim_ident={len(ib)}")
print(f"{'t':>5} {'max|n_d-n_i|':>13} {'excess_rms':>11} {'tracer_rms':>11} {'ratio':>7}")
tprev = 0.0
maxdiff = 0.0
for t in times:
    dt = t - tprev
    if dt > 0:
        pd = expm_multiply(-1j*Hd*dt, pd); pi_ = expm_multiply(-1j*Hi*dt, pi_)
    tprev = t
    nd = dens_d(np.abs(pd)); ni = dens_i(np.abs(pi_))
    tr = tracer(np.abs(pd))
    ex = nd - nsea
    exrms = np.sqrt(max(np.sum(ex*(x-P0)**2), 0.0))
    trrms = np.sqrt(np.sum(tr*(x-P0)**2))
    diff = np.max(np.abs(nd-ni)); maxdiff = max(maxdiff, diff)
    exi = ni - nsea
    exrms_i = np.sqrt(max(np.sum(exi*(x-P0)**2), 0.0))
    print(f"{t:5.2f} {diff:13.3e} {exrms:11.4f} {trrms:11.4f} {trrms/exrms if exrms>0 else float('nan'):7.3f}   identical: excess_rms {exrms_i:8.4f} ratio(tracer_d/excess_i) {trrms/exrms_i if exrms_i>0 else float('nan'):6.3f}")
print("max density difference over all times:", maxdiff)
