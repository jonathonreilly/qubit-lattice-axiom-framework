#!/usr/bin/env python3
"""B24_check part 2 (claim 3): letter identities and the on-site commutant, rebuilt in B7_check/chk_core's independent
gauge (own S letter by PSG symmetrisation, own link hopping, own symmetric on-site algebra), plus an exact structural
check of the B18_check/chk_model blocks (the model B24 actually uses).
Identities are reduced to exact structural statements about hopping blocks:
  S^n(k+t) = S^n(k) diag(e^{i n t.f_c})  <=>  S hops every corner c only by the displacement +f_c (diagonal in c);
  R_L(k+t) = D_t R_L(k) D_t^-1, D_t = diag(e^{-i t.f_c/2})  <=>  every R_L hop c -> c' has displacement (f_c - f_c')/2
  (i.e. it preserves the corner position v + f_c/2).  (signs as in chk_model's e^{+i k.d} convention; chk_core uses
  e^{-i k.d}, which flips the sign of t in both formulas.)"""
import sys, os, itertools
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', 'B7_check'))
import chk_core as cc
PASS = FAIL = 0
def check(name, ok, detail=""):
    global PASS, FAIL; PASS += bool(ok); FAIL += (not ok); print(f"[{'PASS' if ok else 'FAIL'}] {name}  {detail}", flush=True)
CORN = cc.CORN; F = np.array([np.add(*[np.array(d) for d in c]) for c in CORN])     # f_c = d + e
P = cc.PROPER

# ---- S letter in chk_core gauge: symmetrise |(1,1,0), c_xy><0, c_xy| over rotations (translations act trivially)
cxy = frozenset(((1, 0, 0), (0, 1, 0))); i0 = cc.CI[cxy]
hS = {}
for g in P:
    R = cc.OH[g]; c2 = cc.rcorn(R, cxy); d = tuple(int(x) for x in R @ np.array([1, 1, 0]))
    # G|v,c> = (-1)^{lam.v + tau(c)} |Rv,Rc|: conj of the hop gives sign (-1)^{lam.f + tau(c) + tau(c)} = (-1)^{lam.(1,1,0)}
    s = (-1.0) ** int(cc.LAM[g] @ np.array([1, 1, 0]))
    hS.setdefault(d, np.zeros((12, 12)))[cc.CI[c2], cc.CI[c2]] += s
hS = {d: M for d, M in hS.items() if np.abs(M).max() > 1e-12}
nz = [(d, a, b, M[a, b]) for d, M in hS.items() for a in range(12) for b in range(12) if abs(M[a, b]) > 1e-12]
check("S (chk_core gauge): symmetrisation does not cancel; 12 nonzero entries, one per corner, all equal modulus", len(nz) == 12 and
      len({abs(x[3]) for x in nz}) == 1 and sorted(x[1] for x in nz) == list(range(12)), f"{len(nz)} entries, |amp| {set(abs(x[3]) for x in nz)}")
check("S: every entry is diagonal (c -> c) with displacement +f_c (exact)", all(a == b and np.array_equal(np.array(d), F[a]) for d, a, b, _ in nz))
norm = abs(nz[0][3]); hS = {d: M / norm for d, M in hS.items()}
# numeric confirmation of the identity in chk_core convention (e^{-ik.d}):  S^n(k+t) = S^n(k) diag(e^{-i n t.f})
rng = np.random.default_rng(11); ok = True
for _ in range(6):
    k, t = rng.uniform(-np.pi, np.pi, 3), rng.uniform(-np.pi, np.pi, 3)
    for n in (1, -1, 2, -2, 4, -4):
        Sk = np.linalg.matrix_power(cc.Hk(hS, k)[0], n) if n > 0 else np.linalg.matrix_power(cc.Hk(hS, k)[0].conj().T, -n)
        Skt = np.linalg.matrix_power(cc.Hk(hS, k + t)[0], n) if n > 0 else np.linalg.matrix_power(cc.Hk(hS, k + t)[0].conj().T, -n)
        ok &= np.allclose(Skt, Sk @ np.diag(np.exp(-1j * n * F @ t)))
check("S^n(k+t) = S^n(k) diag(e^{-i n t.f_c}) numerically, n = +-1,+-2,+-4, random real t (chk_core sign convention)", ok)
# S symmetric under the PSG (covariance) -- sanity of the construction
ok = all(np.allclose(cc.UF[g] @ cc.Hk(hS, k)[0] @ cc.UF[g].T, cc.Hk(hS, cc.fibre_image(g, k))[0]) for g in P for k in rng.uniform(-3, 3, (3, 3)))
check("S is PSG-covariant: U_g S(k) U_g^T = S(R k + pi R lam)", ok)

# ---- link hopping R_L in chk_core gauge
hL = {}
for (i1, i2, s), e in cc.ETYPES.items():
    if s == (0, 0, 0): continue
    amp = (-1.0) ** int(cc.u[e]) / np.sqrt(2)
    hL.setdefault(tuple(s), np.zeros((12, 12)))[i2, i1] += amp
    hL.setdefault(tuple(-x for x in s), np.zeros((12, 12)))[i1, i2] += amp
nzL = [(d, a, b) for d, M in hL.items() for a in range(12) for b in range(12) if abs(M[a, b]) > 1e-12]
check("R_L: every hop c -> c' (block[c',c] at displacement d) has d = (f_c - f_c')/2 (position-preserving), exact",
      len(nzL) > 0 and all(np.array_equal(2 * np.array(d), F[b] - F[a]) for d, a, b in nzL), f"{len(nzL)} entries")
ok = True
for _ in range(6):
    k, t = rng.uniform(-np.pi, np.pi, 3), rng.uniform(-np.pi, np.pi, 3)
    D = np.diag(np.exp(1j * F @ t / 2))
    ok &= np.allclose(cc.Hk(hL, k + t)[0], D @ cc.Hk(hL, k)[0] @ np.linalg.inv(D))
check("R_L(k+t) = D_t R_L(k) D_t^-1 with D_t = diag(e^{+i t.f/2}) in chk_core convention (= e^{-i t.f/2} in chk_model's), random real t", ok)

# ---- symmetric on-site algebra in chk_core gauge
rows = []
for g in P:
    U = cc.UF[g]
    # vec(U B U^T - B) = (U (x) U - 1) vec(B)
    rows.append(np.kron(U, U) - np.eye(144))
A = np.vstack(rows); _, s, Vh = np.linalg.svd(A); null = Vh[np.sum(s > 1e-9):]
BAS = [n.reshape(12, 12) for n in null]
check("symmetric on-site algebra (commutant of the 24 site-0 PSG rotation matrices; translations trivial in this gauge) has dim 6", len(BAS) == 6, f"{len(BAS)}")
fI = F
Zs = [np.diag(np.where(fI[:, i] != 0, -1.0, 1.0)) for i in range(3)]
Ym = np.diag((-1.0) ** (fI.sum(1) // 2))
def sub_dim(ops):
    M = np.array([np.concatenate([(O @ B - B @ O).ravel() for O in ops]) for B in BAS]).T
    _, s_, Vh_ = np.linalg.svd(M); r = int(np.sum(s_ > 1e-9)); return len(BAS) - r, Vh_[r:]
dZ, coef = sub_dim(Zs); dZY, _ = sub_dim(Zs + [Ym])
check("commutant of {Z_x,Z_y,Z_z} in the symmetric algebra: dim 2; commutant of {Z_i, Y}: dim 1 (scalars)", dZ == 2 and dZY == 1, f"{dZ} {dZY}")
# identify the non-scalar element: Hermitian combination -> two eigenvalues, projectors
Xs = [sum(c * B for c, B in zip(cv, BAS)) for cv in coef]
# find a Hermitian traceless element of span(Xs)
Hs = [(Y + Y.conj().T) / 2 for Y in Xs] + [(Y - Y.conj().T) / 2j for Y in Xs]
Hs = [Y - np.trace(Y) / 12 * np.eye(12) for Y in Hs]
Hm = max(Hs, key=lambda Y: np.linalg.norm(Y))
w, V = np.linalg.eigh(Hm); lv = sorted(set(np.round(w / np.abs(w).max(), 6)))
Pc = V[:, w > 0] @ V[:, w > 0].conj().T
check("non-scalar part of the Z-commutant is a projector pair: two eigenvalues, ranks 6 + 6; so commutant = span{1, P} with rank-6 P",
      len(lv) == 2 and int(np.sum(w > 0)) == 6 and all(np.allclose(Z @ Pc, Pc @ Z) for Z in Zs), f"levels {lv}")
# within each corner plane, P has rank 2 (block diagonal over the 3 planes)
plane = [int(np.argmin(np.abs(F[c]))) for c in range(12)]   # axis missing from the corner = plane normal
ranks = [int(round(np.trace(Pc[np.ix_([c for c in range(12) if plane[c] == a], [c for c in range(12) if plane[c] == a])]).real)) for a in range(3)]
check("P is block diagonal over the 3 corner planes with rank 2 in each", ranks == [2, 2, 2] and
      all(abs(Pc[a, b]) < 1e-9 for a in range(12) for b in range(12) if plane[a] != plane[b]), f"{ranks}")
# unitaries in span{1,P}: alpha P + beta (1-P)  (trivial consequence) -- check B24 plane letters PP + e^{i phi}(1-PP) against chk_model
sys.path.insert(0, os.path.join(HERE, '..', 'B18_check'))
import chk_model as cm
PPm = cm.PLm[0] + cm.PLm[2]
# map corners between the two builds (both frozensets of direction tuples)
perm = [cc.CI[frozenset(tuple(int(x) for x in d) for d in c)] for c in cm.CORN]      # model index -> core index
Pc_m = Pc[np.ix_(perm, perm)]; Qc_m = np.eye(12) - Pc_m
match = [np.allclose(np.abs(X_), np.abs(PPm), atol=1e-9) for X_ in (Pc_m, Qc_m)]
# sign gauge: diagonal +-1 G with G X G = PPm
def find_gauge(X_, Y_):
    g = [0] * 12; g[0] = 1; changed = True
    while changed:
        changed = False
        for a in range(12):
            for b in range(12):
                if g[a] and not g[b] and abs(Y_[a, b]) > 1e-9:
                    r = Y_[a, b] / X_[a, b]; g[b] = int(np.sign(r.real)) * g[a]; changed = True
    for a in range(12):
        if not g[a]: g[a] = 1
    G = np.diag(g); return np.allclose(G @ X_ @ G, Y_)
gauge_ok = any(m and find_gauge(X_, PPm) for m, X_ in zip(match, (Pc_m, Qc_m)))
check("the chk_core commutant projector equals B24's PP = PLm[0]+PLm[2] (or 1-PP) up to a diagonal sign gauge (independent identification)",
      gauge_ok, f"|.| match (P, 1-P): {match}")

# ---- structural check of the chk_model blocks B24 actually uses (e^{+ik.sh} convention, bl[sh][c',c]: c at 0 -> c' at sh)
Fm = np.array([cm.FACE[c] for c in cm.CORN])
okS = all((a == b and np.array_equal(np.array(sh), Fm[a])) for sh, M in cm.blS.items() for a in range(12) for b in range(12) if abs(M[a, b]) > 1e-12)
nS_entries = sum(int(np.sum(np.abs(M) > 1e-12)) for M in cm.blS.values())
okL = all(np.array_equal(2 * np.array(sh), Fm[b] - Fm[a]) for sh, M in cm.blL.items() for a in range(12) for b in range(12) if abs(M[a, b]) > 1e-12)
check("chk_model blS: 12 diagonal entries at displacement +f_c (so S^n(k+t) = S^n(k) diag(e^{+i n t.f_c}) exactly)", okS and nS_entries == 12, f"{nS_entries}")
check("chk_model blL: all hops position-preserving, displacement (f_c - f_c')/2 (so R_L(k+t) = D_t R_L D_t^-1, D_t = diag(e^{-i t.f/2}) exactly)", okL)
print(f"\nTOTAL: PASS={PASS} FAIL={FAIL}")
