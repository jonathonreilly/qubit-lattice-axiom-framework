#!/usr/bin/env python3
"""Kill-check T04, k3: (a) verify the B1 explanation (distinguishable density = sum over
tracer-rank sectors evolved independently; identical density has cross terms) and
(b) scaling of tracer/excess ratio with L at t = L/4 (probe 8's protocol: 0.20, 0.10, 0.05
for L = 16, 32, 64) using the attacker's distinguishable-tracer model.
usage: k3_tracer.py L N0"""
import sys, itertools, numpy as np, scipy.sparse as sp
from scipy.sparse.linalg import expm_multiply

L = int(sys.argv[1]); N0 = int(sys.argv[2]); P0 = L // 2
tlist = [float(x) for x in sys.argv[3].split(',')]
j = np.arange(L)
orb = np.array([np.sqrt(2/(L+1))*np.sin(np.pi*(k+1)*(j+1)/(L+1)) for k in range(L)])
sea_orb = orb[:N0]
def sea_amp(S): return np.linalg.det(sea_orb[:, list(S)])
bit = lambda s: 1 << s
basis = []
for p in range(L):
    for S in itertools.combinations([s for s in range(L) if s != p], N0):
        basis.append((p, sum(bit(s) for s in S)))
idx = {b: i for i, b in enumerate(basis)}
rows, cols = [], []
for (p, m), i in idx.items():
    for q in (p-1, p+1):
        if 0 <= q < L and not (m & bit(q)): rows.append(idx[(q, m)]); cols.append(i)
    for s in range(L):
        if m & bit(s):
            for q in (s-1, s+1):
                if 0 <= q < L and q != p and not (m & bit(q)):
                    rows.append(idx[(p, (m ^ bit(s)) | bit(q))]); cols.append(i)
n = len(basis)
Hd = sp.csr_matrix((-np.ones(len(rows)), (rows, cols)), shape=(n, n))
psi0 = np.zeros(n)
for (p, m), i in idx.items():
    if p == P0:
        S = tuple(s for s in range(L) if m & bit(s)); psi0[i] = sea_amp(S)
psi0 /= np.linalg.norm(psi0)
ib = list(itertools.combinations(range(L), N0+1)); iidx = {b: i for i, b in enumerate(ib)}
r2, c2 = [], []
for b, i in iidx.items():
    for s in b:
        for q in (s-1, s+1):
            if 0 <= q < L and q not in b:
                nb = tuple(sorted([x for x in b if x != s] + [q])); r2.append(iidx[nb]); c2.append(i)
Hi = sp.csr_matrix((-np.ones(len(r2)), (r2, c2)), shape=(len(ib), len(ib)))
phi0 = np.zeros(len(ib))
sector = np.zeros(len(ib), dtype=int)
for b, i in iidx.items():
    if P0 in b:
        rest = tuple(s for s in b if s != P0); k = sum(1 for s in rest if s < P0)
        phi0[i] = (-1) ** k * sea_amp(rest); sector[i] = k
phi0 /= np.linalg.norm(phi0)
def dens_i(v):
    d = np.zeros(L)
    for b, i in iidx.items():
        w = abs(v[i])**2
        for s in b: d[s] += w
    return d
def dens_d(v):
    d = np.zeros(L); pr = np.abs(v)**2; tr = np.zeros(L)
    for (p, m), i in idx.items():
        w = pr[i]; d[p] += w; tr[p] += w
        for s in range(L):
            if m & bit(s): d[s] += w
    return d, tr
nsea = (sea_orb**2).sum(axis=0); x = np.arange(L)
pd = psi0.astype(complex); pi_ = phi0.astype(complex)
secs = {k: np.where(sector == k, phi0, 0).astype(complex) for k in range(N0+1)}
tprev = 0; print(f"L={L} N0={N0}")
for t in tlist:
    dt = t - tprev; tprev = t
    pd = expm_multiply(-1j*Hd*dt, pd); pi_ = expm_multiply(-1j*Hi*dt, pi_)
    for k in secs: secs[k] = expm_multiply(-1j*Hi*dt, secs[k])
    nd, tr = dens_d(pd); ni = dens_i(pi_)
    nsec = sum(dens_i(secs[k]) for k in secs)
    ex = nd - nsea
    exrms = np.sqrt(max(np.sum(ex*(x-P0)**2), 0)); trrms = np.sqrt(np.sum(tr*(x-P0)**2))
    print(f"t={t:5.2f}  |n_d - n_i|max={np.max(abs(nd-ni)):.3e}  |n_d - sum_k n_sector_k|max={np.max(abs(nd-nsec)):.2e}  excess_rms={exrms:.3f} tracer_rms={trrms:.3f} ratio={trrms/exrms:.3f}")
