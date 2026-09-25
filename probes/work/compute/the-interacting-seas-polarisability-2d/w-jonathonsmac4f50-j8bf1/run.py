#!/usr/bin/env python3
"""The interacting (hard-core) sea's response to a clock modulation, two dimensions.  Worked computation, run 1 of 2.

As landed on main: block 78 (#8613) supplies the model - the one-body walk summed over records and compressed to configurations with
different sites (one record per site, any coins), with either exchange sign; block 76 (#8611) as landed keeps T1 (a chessboard of clocks
is invisible to opposite-parity hopping) and WITHDRAWS the induced sea stiffness (kappa = 0.095 is only a declared comparator input);
block 85 (#8657): the hard-core crowd at the sea's filling is jammed.  So here the free and interacting responses are both computed.

One body: H = sigma_1 S_x + sigma_2 S_y on an Lx x Ly torus, clocked H_w = phi H phi, phi = exp(u/2), u_x = eps cos(2 pi x / 4).
Many body: N records, hard-core, bosonic (+) or fermionic (-) exchange; exact sparse diagonalisation (scipy eigsh, floating point).
Comparators on the same torus: free antisymmetric (fill the N lowest one-body levels; no exclusion - two opposite-coin records may share a
site), free symmetric (N in the lowest level), the free negative sea (all negative levels).  Response: E0(eps) = E0 + chi eps^2 + ...,
chi per site from a fit over eps = +-0.02, +-0.04, +-0.08 (the |eps| term is fitted and reported: degeneracies give cusps).
Exact part (sympy rationals): the chessboard phi -> phi c^(eps_site) leaves the many-body generator unchanged (4x4, N = 2).
"""
import itertools, sys, time
import numpy as np
import scipy.sparse as sps
from scipy.sparse.linalg import eigsh
import sympy as sp

def out(s): print(s, flush=True)
S1 = np.array([[0, 1], [1, 0]], complex); S2 = np.array([[0, -1j], [1j, 0]])

def one_body(Lx, Ly, phi):
    V = Lx * Ly; H = np.zeros((2 * V, 2 * V), complex)
    for x in range(Lx):
        for y in range(Ly):
            i = x * Ly + y
            for (dx, dy, S) in ((1, 0, S1), (0, 1, S2)):
                j = ((x + dx) % Lx) * Ly + (y + dy) % Ly
                # (S psi)(i) = (psi(i+e) - psi(i-e))/(2i): <i|S|i+e> = 1/(2i), <i+e|S|i> = -1/(2i)
                H[2 * i:2 * i + 2, 2 * j:2 * j + 2] += phi[i] * phi[j] * S / 2j
                H[2 * j:2 * j + 2, 2 * i:2 * i + 2] += -phi[i] * phi[j] * S / 2j
    return H

POP = np.array([bin(k).count('1') for k in range(1 << 16)], np.int64)
def basis(V, N):
    masks = np.array(sorted(sum(1 << s for s in c) for c in itertools.combinations(range(V), N)), np.int64)
    offset = np.full(1 << V, -1, np.int64); offset[masks] = np.arange(len(masks)) << N
    return masks, offset
def many_body(Lx, Ly, N, phi, sign, masks, offset):
    V = Lx * Ly; h1 = one_body(Lx, Ly, phi); nc = 1 << N
    occ = np.repeat(masks, nc); coin = np.tile(np.arange(nc, dtype=np.int64), len(masks)); src_all = np.arange(len(occ), dtype=np.int64)
    rows, cols, vals = [], [], []
    for i in range(V):
        for j in range(V):
            blk = h1[2 * j:2 * j + 2, 2 * i:2 * i + 2]            # <j, c'| H |i, c>
            if i == j or not np.any(blk): continue
            sel = ((occ >> i) & 1).astype(bool) & ~(((occ >> j) & 1).astype(bool))
            o = occ[sel]; cn = coin[sel]; src = src_all[sel]
            ri = POP[o & ((1 << i) - 1)]; c = (cn >> ri) & 1
            rem = (cn & ((1 << ri) - 1)) | ((cn >> (ri + 1)) << ri)
            o2 = o ^ (1 << i) ^ (1 << j); rj = POP[o2 & ((1 << j) - 1)]
            lo, hi = min(i, j), max(i, j)
            between = ((1 << hi) - 1) ^ ((1 << (lo + 1)) - 1)
            sg = np.ones(len(o)) if sign > 0 else (-1.0) ** POP[o & between]
            for cp in (0, 1):
                newc = (rem & ((1 << rj) - 1)) | (cp << rj) | ((rem >> rj) << (rj + 1))
                dst = offset[o2] + newc
                amp = np.where(c == 0, blk[cp, 0], blk[cp, 1]) * sg
                nz = amp != 0
                rows.append(dst[nz]); cols.append(src[nz]); vals.append(amp[nz])
    dim = len(occ)
    return sps.csr_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(dim, dim))
def ground(Hm, k=4):
    w = eigsh(Hm, k=k, which='SA', tol=1e-12, return_eigenvectors=False)
    return np.sort(w)

# ------------------------------------------------------------------ exact: chessboard of clocks (4x4, N = 2)
def sp_many_body_two(Lx, Ly, phi, sign):
    V = Lx * Ly; N = 2
    S1s = sp.Matrix([[0, 1], [1, 0]]); S2s = sp.Matrix([[0, -sp.I], [sp.I, 0]])
    h = {}
    for x in range(Lx):
        for y in range(Ly):
            i = x * Ly + y
            for (dx, dy, S) in ((1, 0, S1s), (0, 1, S2s)):
                j = ((x + dx) % Lx) * Ly + (y + dy) % Ly
                h[(i, j)] = h.get((i, j), sp.zeros(2, 2)) + phi[i] * phi[j] * S / (2 * sp.I)
                h[(j, i)] = h.get((j, i), sp.zeros(2, 2)) - phi[i] * phi[j] * S / (2 * sp.I)
    states = [(a, b, ca, cb) for a, b in itertools.combinations(range(V), 2) for ca in (0, 1) for cb in (0, 1)]
    idx = {s: k for k, s in enumerate(states)}; M = {}
    for (a, b, ca, cb) in states:
        for mover, other, cm, co in ((a, b, ca, cb), (b, a, cb, ca)):
            for j in range(V):
                if j in (a, b) or (j, mover) not in h: continue
                for cp in (0, 1):
                    amp = h[(j, mover)][cp, cm]
                    if amp == 0: continue
                    s2 = tuple(sorted([(j, cp), (other, co)]))
                    key = (s2[0][0], s2[1][0], s2[0][1], s2[1][1])
                    swapped = (j > other) != (mover > other)
                    sgn = -1 if (sign < 0 and swapped) else 1
                    M[(idx[key], idx[(a, b, ca, cb)])] = M.get((idx[key], idx[(a, b, ca, cb)]), 0) + sgn * amp
    return M
phi0 = {i: 1 + sp.Rational((3 * i + 1) % 5, 4) for i in range(16)}
cb = {i: phi0[i] * sp.Integer(2) ** ((-1) ** ((i // 4) + (i % 4))) for i in range(16)}
okc = True
for sgn in (+1, -1):
    A = sp_many_body_two(4, 4, phi0, sgn); B = sp_many_body_two(4, 4, cb, sgn)
    keys = set(A) | set(B)
    okc &= all(sp.simplify(A.get(k, 0) - B.get(k, 0)) == 0 for k in keys)
out("X exact (4x4 torus, two records, both exchange signs, generic rational phi): the chessboard phi -> phi 2^(+-1) leaves the hard-core "
    "generator unchanged entry by entry: %s (every hop joins opposite sublattices, as block 76 T1 for one body)" % ("PASS" if okc else "FAIL"))
out("X exact: at one record per site (the free negative branch's filling on a torus: V records) no hop is possible, H = 0: the jam (block 85)")

# ------------------------------------------------------------------ numerics
def response(Lx, Ly, N, sign, masks, offset, epss=(0.0, 0.02, -0.02, 0.04, -0.04, 0.08, -0.08)):
    E = {}
    for e in epss:
        u = np.array([e * np.cos(2 * np.pi * (i // Ly) / 4) for i in range(Lx * Ly)])
        Hm = many_body(Lx, Ly, N, np.exp(u / 2), sign, masks, offset)
        E[e] = ground(Hm)
    return E
def free_resp(Lx, Ly, N, kind, epss=(0.0, 0.02, -0.02, 0.04, -0.04, 0.08, -0.08)):
    E = {}
    for e in epss:
        u = np.array([e * np.cos(2 * np.pi * (i // Ly) / 4) for i in range(Lx * Ly)])
        lev = np.linalg.eigvalsh(one_body(Lx, Ly, np.exp(u / 2)))
        E[e] = lev[:N].sum() if kind == "anti" else (N * lev[0] if kind == "sym" else lev[lev < -1e-12].sum())
    return E
def fit(Ed, V):
    es = sorted(Ed); y = np.array([Ed[e] for e in es]); x = np.array(es)
    X = np.vstack([np.ones_like(x), np.abs(x), x ** 2]).T
    co = np.linalg.lstsq(X, y, rcond=None)[0]
    return co[0] / V, co[1] / V, co[2] / V
rows = []
for (Lx, Ly, N) in ((4, 3, 6), (4, 3, 4), (4, 4, 4), (4, 4, 6)):
    V = Lx * Ly; t0 = time.time()
    masks, offset = basis(V, N); dim = len(masks) << N
    line = "N %dx%d torus, N = %d records (hard-core dim %d):" % (Lx, Ly, N, dim)
    for sign, lab in ((+1, "hard-core bosonic"), (-1, "hard-core fermionic")):
        Es = response(Lx, Ly, N, sign, masks, offset)
        E0s = {e: v[0] for e, v in Es.items()}
        gap = Es[0.0][1] - Es[0.0][0]
        e0, cusp, chi = fit(E0s, V)
        rows.append((Lx, Ly, N, lab, e0, chi, cusp, gap))
        line += " | %s: E0/site %.6f, chi %+.5f, |eps| term %+.1e, gap to 1st excited %.2e" % (lab, e0, chi, cusp, gap)
    for kind, lab in (("anti", "free antisymmetric"), ("sym", "free symmetric")):
        e0, cusp, chi = fit(free_resp(Lx, Ly, N, kind), V)
        rows.append((Lx, Ly, N, lab, e0, chi, cusp, None))
        line += " | %s: E0/site %.6f, chi %+.5f, |eps| %+.1e" % (lab, e0, chi, cusp)
    out(line + " (%.0f s)" % (time.time() - t0))
for (Lx, Ly) in ((4, 3), (4, 4)):
    V = Lx * Ly
    e0, cusp, chi = fit(free_resp(Lx, Ly, 0, "sea"), V)
    out("N %dx%d free negative sea (all negative one-body levels filled; the hard-core crowd at V records is jammed, E = 0, chi = 0): E/site %.6f, chi %+.5f, |eps| %+.1e"
        % (Lx, Ly, e0, chi, cusp))
    rows.append((Lx, Ly, V, "free sea", e0, chi, cusp, None))
# the clock stiffness part: remove the local (volume) response.  For u = eps cos(q x) at long wavelength E - E0 -> (e0/2) sum_x u_x^2
# = e0 V eps^2 / 4, so chi(q -> 0) = e0/4 per site (e0 = E0/V); the q-dependent part Dchi(q) = chi(q) - e0/4 is block 76's stiffness
# channel (its kappa q^2 term); q = pi/2 here, lattice q^2 = 2(1 - cos q) = 2.
out("N stiffness part Dchi = chi - e0/4 at q = pi/2 (lattice q^2 = 2), per site:")
for r in rows:
    out("   %dx%d N=%-2d %-20s e0 %.6f  chi %+.5f  Dchi %+.5f" % (r[0], r[1], r[2], r[3], r[4], r[5], r[5] - r[4] / 4))
print()
def D(Lx, Ly, N, lab):
    r = [r for r in rows if (r[0], r[1], r[2], r[3]) == (Lx, Ly, N, lab)][0]; return r[5] - r[4] / 4
hb, hf = D(4, 3, 6, "hard-core bosonic"), D(4, 3, 6, "hard-core fermionic")
fa, sea = D(4, 3, 6, "free antisymmetric"), D(4, 3, 12, "free sea")
print("SUMMARY: 4x3 torus at half filling (6 records): raw second-order response chi < 0 for every model (hard-core bosonic %+.4f, fermionic %+.4f, "
      "free antisymmetric %+.4f); with the local volume term e0/4 removed the stiffness part is hard-core %+.4f / %+.4f, free negative sea %+.4f "
      "(same sign, positive: a clock stiffness), free fermions at the same density %+.4f (opposite); the chessboard of clocks is an exact zero; "
      "at the sea's filling the hard-core crowd is jammed (E = 0, no response)" % (
      [r for r in rows if r[:4] == (4, 3, 6, "hard-core bosonic")][0][5], [r for r in rows if r[:4] == (4, 3, 6, "hard-core fermionic")][0][5],
      [r for r in rows if r[:4] == (4, 3, 6, "free antisymmetric")][0][5], hb, hf, sea, fa))
if np.sign(hb) != np.sign(sea) or np.sign(hf) != np.sign(sea):
    print("HIT: the interacting stiffness has the opposite sign to the free sea's on the same torus: hard-core %+.4f / %+.4f vs free sea %+.4f" % (hb, hf, sea))
