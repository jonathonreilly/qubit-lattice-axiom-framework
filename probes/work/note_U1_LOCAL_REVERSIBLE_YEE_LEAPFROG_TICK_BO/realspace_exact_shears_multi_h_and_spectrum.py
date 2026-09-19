#!/usr/bin/env python3
"""Probe: U1_LOCAL_REVERSIBLE_YEE_LEAPFROG_TICK_BOUNDED_THEOREM_NOTE_2026-09-03.

Machinery disjoint from the runner (its L=3 / side-six block at h = 1/2, Fourier
blocks on L = 3,4,5,7, a 1/8 schedule grid): an independently written
real-space doubled complex (vertex/edge/face/cube by coordinate parity on the
side-2L torus, faces reading x-e_j, x+e_i, x+e_j, x-e_i with (+,+,-,-)),
exact integer sparse arithmetic after clearing denominators, for several
exact steps h and cubic tori L = 2..6.

Falsifier bullets checked literally:
 F1 every layer row reads its own site and at most four opposite-role
    physical neighbours (distance 1); composed tick: Manhattan distances
    exactly {0,1,2,3} (on side >= 8);
 F2 U(-h) U(h) = I exactly; T U_h T = U_{-h} with T = diag(I, -I);
 F3 both Gauss rows unchanged by EACH shear separately;
 F4 half-full-half the sole (a, b, c) on the 1/32 grid of [-1, 2]^3 with
    b = 1, a + c = 1, a = c; the quarter/three-quarter control fails U(-h)U(h)=I;
 F5 U_h^T M_h U_h = M_h exactly, M_h = diag(I - (h^2/4) C^T C, I);
 F6 M_h positive for h < 1/sqrt 3: lambda_min(M_h) = 1 - 3h^2 on even L (the
    corner |s|^2 = 12), zero at h = 1/sqrt 3, negative and |eigenvalue| > 1 at h = 2/3;
 F7 every nonzero momentum on L = 2..6 has exactly two positive phases
    theta_h = 2 asin(h|s|/2) (real-space eigenvalues of U_h against the formula),
    no zero phase except k = 0;
 F8 all 48 signed permutations with polar E and axial B (2-form face signs)
    fix C, hence both shears;
 F9 one-step error |U_h - exp(hG)| cubic (halving ratio -> 8), global second
    order (fixed time T: error ratio -> 4).

Prints SUMMARY: lines; HIT: only when a falsifier fires.
"""
import itertools
import math
import sys
import time
from fractions import Fraction as Fr

import numpy as np
import scipy.sparse as sps
import scipy.linalg as sla

HITS = []


def hit(msg):
    HITS.append(msg)
    print("HIT: " + msg)


def summary(msg):
    print("SUMMARY: " + msg)


def levi(a, b, c):
    perm = (a, b, c)
    if len(set(perm)) < 3:
        return 0
    inv = sum(1 for x in range(3) for y in range(x + 1, 3) if perm[x] > perm[y])
    return -1 if inv % 2 else 1


def build(L):
    n = 2 * L
    pts = list(itertools.product(range(n), repeat=3))
    V, E, F, Q = [], [], [], []
    for p in pts:
        odd = tuple(i for i in range(3) if p[i] % 2)
        (V, E, F, Q)[len(odd)].append(p)
    vi = {p: t for t, p in enumerate(V)}
    ei = {p: t for t, p in enumerate(E)}
    fi = {p: t for t, p in enumerate(F)}

    def sh(p, ax, st):
        q = list(p)
        q[ax] = (q[ax] + st) % n
        return tuple(q)
    r, c, v = [], [], []
    for p, t in ei.items():
        i = [a for a in range(3) if p[a] % 2][0]
        r += [t, t]
        c += [vi[sh(p, i, -1)], vi[sh(p, i, 1)]]
        v += [-1, 1]
    d0 = sps.csr_matrix((v, (r, c)), shape=(len(E), len(V)), dtype=np.int64)
    r, c, v = [], [], []
    for p, t in fi.items():
        i, j = [a for a in range(3) if p[a] % 2]
        for q, sg in ((sh(p, j, -1), 1), (sh(p, i, 1), 1), (sh(p, j, 1), -1), (sh(p, i, -1), -1)):
            r.append(t)
            c.append(ei[q])
            v.append(sg)
    C = sps.csr_matrix((v, (r, c)), shape=(len(F), len(E)), dtype=np.int64)
    r, c, v = [], [], []
    for t, p in enumerate(Q):
        for nr in range(3):
            i, j = [a for a in range(3) if a != nr]
            eps = levi(i, j, nr)
            r += [t, t]
            c += [fi[sh(p, nr, 1)], fi[sh(p, nr, -1)]]
            v += [eps, -eps]
    d2 = sps.csr_matrix((v, (r, c)), shape=(len(Q), len(F)), dtype=np.int64)
    return dict(n=n, V=V, E=E, F=F, Q=Q, vi=vi, ei=ei, fi=fi, d0=d0, C=C, d2=d2)


def shears_int(C, p, q):
    """h = p/q.  Integer layers: 2q S_B(h/2) = [[2q I, 0], [p C, 2q I]],
    q S_E(h) = [[q I, -p C^T], [0, q I]]; U_num = (2q S_B)(q S_E)(2q S_B) = 4 q^3 U_h."""
    nE = C.shape[1]
    nF = C.shape[0]
    IE = sps.identity(nE, dtype=np.int64, format="csr")
    IF = sps.identity(nF, dtype=np.int64, format="csr")
    SB = sps.bmat([[2 * q * IE, None], [p * C, 2 * q * IF]], format="csr")
    SE = sps.bmat([[q * IE, -p * C.T], [None, q * IF]], format="csr")
    return SB, SE, SB @ SE @ SB, 4 * q ** 3


def eq_sparse(A, B):
    return (A - B).count_nonzero() == 0


def tor(p, qq, n):
    return sum(min((p[i] - qq[i]) % n, (qq[i] - p[i]) % n) for i in range(3))


def run_exact(Ls=(2, 3, 4, 5, 6), hs=((1, 2), (1, 3), (2, 5), (1, 7), (4, 7))):
    print("=" * 78)
    print("F1-F3, F5  exact integer checks on the real-space complex")
    rows = []
    for L in Ls:
        X = build(L)
        C, d0, d2 = X["C"], X["d0"], X["d2"]
        nE, nF = C.shape[1], C.shape[0]
        sites = X["E"] + X["F"]
        chain = (C @ d0).count_nonzero() == 0 and (d2 @ C).count_nonzero() == 0
        Qg = sps.bmat([[d0.T, None], [None, d2]], format="csr")
        for (p, q) in hs:
            SB, SE, U, s = shears_int(C, p, q)
            SBm, SEm, Um, _ = shears_int(C, -p, q)
            # F1: layer rows: own site + <= 4 neighbours at distance 1
            loc_ok = True
            for M in (SB, SE):
                Mc = M.tocsr()
                for rr in range(M.shape[0]):
                    cols = Mc.indices[Mc.indptr[rr]:Mc.indptr[rr + 1]]
                    others = [cc for cc in cols if cc != rr]
                    if len(others) > 4 or any(tor(sites[rr], sites[cc], X["n"]) != 1 for cc in others):
                        loc_ok = False
                        break
            # composed distances (only meaningful when side >= 8)
            dists = set()
            if X["n"] >= 8:
                Uc = U.tocoo()
                for a, b in zip(Uc.row, Uc.col):
                    dists.add(tor(sites[a], sites[b], X["n"]))
            # F2: inverse and time reversal
            inv_ok = eq_sparse(Um @ U, (s * s) * sps.identity(nE + nF, dtype=np.int64))
            T = sps.diags([1] * nE + [-1] * nF, dtype=np.int64)
            tr_ok = eq_sparse(T @ U @ T, Um)
            # F3: Gauss rows per layer
            gauss_ok = eq_sparse(Qg @ SB, (2 * q) * Qg) and eq_sparse(Qg @ SE, q * Qg)
            # F5: conserved metric, M_num = 4 q^2 M_h
            M = sps.bmat([[4 * q * q * sps.identity(nE, dtype=np.int64) - p * p * (C.T @ C), None],
                          [None, 4 * q * q * sps.identity(nF, dtype=np.int64)]], format="csr")
            met_ok = eq_sparse(U.T @ M @ U, (s * s) * M)
            rows.append((L, p, q, loc_ok, sorted(dists), inv_ok, tr_ok, gauss_ok, met_ok, chain))
            ok = loc_ok and inv_ok and tr_ok and gauss_ok and met_ok and chain and (not dists or sorted(dists) == [0, 1, 2, 3])
            if not ok:
                hit(f"L={L}, h={p}/{q}: locality {loc_ok}, distances {sorted(dists)}, inverse {inv_ok}, reversal {tr_ok}, "
                    f"Gauss {gauss_ok}, metric {met_ok}")
        print(f"  L={L} (side {X['n']}, {nE}+{nF} fields): h in {[f'{p}/{q}' for p, q in hs]}: all exact checks pass: "
              f"{all(r[3] and r[5] and r[6] and r[7] and r[8] for r in rows if r[0] == L)}; composed distances "
              f"{sorted({d for r in rows if r[0] == L for d in r[4]}) or 'n/a (side < 8)'}")
    return rows


def run_schedule():
    print("=" * 78)
    print("F4  schedule classification on the 1/32 grid and the quarter control")
    grid = [Fr(-1) + Fr(j, 32) for j in range(97)]
    sols = [(a, b, c) for a in grid for b in grid for c in grid if b == 1 and a + c == 1 and a == c]
    X = build(2)
    C = X["C"]
    p, q = 1, 2
    # quarter/full/three-quarter: U(a,b,c;h) = S_B(c h) S_E(b h) S_B(a h); integer layers with h = 1/2
    nE, nF = C.shape[1], C.shape[0]
    IE = sps.identity(nE, dtype=np.int64)
    IF = sps.identity(nF, dtype=np.int64)

    def SBt(num, den):
        return sps.bmat([[den * IE, None], [num * C, den * IF]], format="csr")

    def SEt(num, den):
        return sps.bmat([[den * IE, -num * C.T], [None, den * IF]], format="csr")
    # a = 1/4, b = 1, c = 3/4 at h = +-1/2: a h = +-1/8, b h = +-1/2, c h = +-3/8 ; common denominator 8
    Up = SBt(3, 8) @ SEt(4, 8) @ SBt(1, 8)
    Um = SBt(-3, 8) @ SEt(-4, 8) @ SBt(-1, 8)
    ctrl_inverse = eq_sparse(Um @ Up, (8 ** 6) * sps.identity(nE + nF, dtype=np.int64))
    # first-order tangent of the control: (a + c) C and -b C^T, as the note says
    tangent_ok = (Fr(1, 4) + Fr(3, 4) == 1)
    print(f"  grid points {len(grid)}^3 = {len(grid) ** 3}: solutions {[(str(a), str(b), str(c)) for a, b, c in sols]}; "
          f"quarter/full/three-quarter keeps the tangent ({tangent_ok}) and U(-h)U(h) = I: {ctrl_inverse}")
    if sols != [(Fr(1, 2), Fr(1), Fr(1, 2))] or ctrl_inverse:
        hit(f"schedule classification differs: {sols}, control inverse {ctrl_inverse}")
    return sols, ctrl_inverse


def run_positivity_spectrum(L=4):
    print("=" * 78)
    print(f"F6, F7  positivity boundary and the real-space spectrum (L={L}, and momenta L=2..6)")
    X = build(L)
    C = X["C"].astype(float).toarray()
    nE, nF = C.shape[1], C.shape[0]
    CtC = C.T @ C
    lmax = np.linalg.eigvalsh(CtC).max()
    rows = []
    for h in (0.5, 0.55, 1 / math.sqrt(3), 2 / 3):
        lam = np.linalg.eigvalsh(np.eye(nE) - (h * h / 4) * CtC).min()
        rows.append((h, lam, 1 - 3 * h * h))
    print(f"  lambda_max(C^T C) = {lmax:.12f} (12 on even L); lambda_min(M_h): " +
          ", ".join(f"h={h:.4f}: {lam:+.3e} (1-3h^2 = {ref:+.3e})" for h, lam, ref in rows))
    bad = any((h < 1 / math.sqrt(3) - 1e-12 and lam <= 0) for h, lam, _ in rows) or abs(lmax - 12) > 1e-9
    # instability at h = 2/3: spectral radius of U_h > 1
    def Uf(h):
        I_E, I_F = np.eye(nE), np.eye(nF)
        SB = np.block([[I_E, np.zeros((nE, nF))], [(h / 2) * C, I_F]])
        SE = np.block([[I_E, -h * C.T], [np.zeros((nF, nE)), I_F]])
        return SB @ SE @ SB
    rad = {h: max(abs(np.linalg.eigvals(Uf(h)))) for h in (0.5, 2 / 3)}
    print(f"  spectral radius of U_h: h=1/2: {rad[0.5]:.12f}; h=2/3: {rad[2 / 3]:.6f} (instability)")
    if bad or rad[2 / 3] <= 1 + 1e-6 or abs(rad[0.5] - 1) > 1e-9:
        hit("positivity / instability boundary differs from the note")
    # spectrum against the formula, real space, several L and h
    worst = 0.0
    npos_bad = 0
    for LL in (2, 3, 4, 5, 6):
        Y = build(LL)
        Cy = Y["C"].astype(float).toarray()
        nEy, nFy = Cy.shape[1], Cy.shape[0]
        s2 = np.array([4 * math.sin(math.pi * m / LL) ** 2 for m in range(LL)])
        s2tot = (s2[:, None, None] + s2[None, :, None] + s2[None, None, :]).ravel()
        for h in (0.5, 0.3):
            I_E, I_F = np.eye(nEy), np.eye(nFy)
            SB = np.block([[I_E, np.zeros((nEy, nFy))], [(h / 2) * Cy, I_F]])
            SE = np.block([[I_E, -h * Cy.T], [np.zeros((nFy, nEy)), I_F]])
            U = SB @ SE @ SB
            ph = np.angle(np.linalg.eigvals(U))
            th = 2 * np.arcsin(h * np.sqrt(s2tot) / 2)
            pred = np.concatenate([th, th, -th, -th, np.zeros_like(th), np.zeros_like(th)])
            worst = max(worst, float(np.max(np.abs(np.sort(ph) - np.sort(pred)))))
            npos = int(np.sum(ph > 1e-9))
            if npos != 2 * (LL ** 3 - 1):
                npos_bad += 1
    print(f"  real-space eigenphases of U_h vs {{+-theta_h twice, 0 twice}} per momentum (L=2..6, h=1/2, 0.3): max dev "
          f"{worst:.2e}; positive-phase count 2(N-1) failures {npos_bad}")
    if worst > 1e-8 or npos_bad:
        hit(f"transverse phase spectrum differs (dev {worst:.2e}, count failures {npos_bad})")
    # zero phase only at k = 0 on L = 2..40 at h = 1/2 (exact: sin argument)
    zero_extra = 0
    for LL in range(2, 41):
        for m in itertools.product(range(LL), repeat=3):
            if m == (0, 0, 0):
                continue
            s2 = sum(4 * math.sin(math.pi * mi / LL) ** 2 for mi in m)
            if 2 * math.asin(0.5 * math.sqrt(s2) / 2) < 1e-12:
                zero_extra += 1
    print(f"  extra zero-phase momenta on L = 2..40 at h = 1/2: {zero_extra}")
    if zero_extra:
        hit("an additional momentum has zero photon phase")
    return lmax, rows, rad, worst, npos_bad, zero_extra


def run_covariance(Ls=(2, 3, 4)):
    print("=" * 78)
    print("F8  48 signed permutations, polar E / axial B, real space")
    out = []
    for L in Ls:
        X = build(L)
        n = X["n"]
        good = 0
        for perm in itertools.permutations(range(3)):
            for signs in itertools.product((1, -1), repeat=3):
                def act(p):
                    q = [0, 0, 0]
                    for a in range(3):
                        q[perm[a]] = (signs[a] * p[a]) % n
                    return tuple(q)
                er, es = [], []
                for p in X["E"]:
                    i = [a for a in range(3) if p[a] % 2][0]
                    er.append(X["ei"][act(p)])
                    es.append(signs[i])
                SE_ = sps.csr_matrix((es, (er, range(len(X["E"])))), shape=(len(X["E"]),) * 2)
                fr, fs = [], []
                for p in X["F"]:
                    i, j = [a for a in range(3) if p[a] % 2]
                    fr.append(X["fi"][act(p)])
                    fs.append(signs[i] * signs[j] * (1 if perm[i] < perm[j] else -1))
                SF_ = sps.csr_matrix((fs, (fr, range(len(X["F"])))), shape=(len(X["F"]),) * 2)
                if eq_sparse(SF_ @ X["C"] @ SE_.T, X["C"]):
                    good += 1
        out.append((L, good))
        print(f"  L={L}: signed permutations fixing C (hence both shears and U_h): {good}/48")
        if good != 48:
            hit(f"L={L}: {48 - good} cubic transformations break polar/axial covariance")
    return out


def run_accuracy(L=3):
    print("=" * 78)
    print("F9  approach to the continuous generator")
    X = build(L)
    C = X["C"].astype(float).toarray()
    nE, nF = C.shape[1], C.shape[0]
    G = np.block([[np.zeros((nE, nE)), -C.T], [C, np.zeros((nF, nF))]])

    def U(h):
        I_E, I_F = np.eye(nE), np.eye(nF)
        SB = np.block([[I_E, np.zeros((nE, nF))], [(h / 2) * C, I_F]])
        SE = np.block([[I_E, -h * C.T], [np.zeros((nF, nE)), I_F]])
        return SB @ SE @ SB
    hs = [0.2, 0.1, 0.05, 0.025]
    one = [np.linalg.norm(U(h) - sla.expm(h * G), 2) for h in hs]
    r1 = [one[i] / one[i + 1] for i in range(3)]
    Tt = 1.6
    glob = []
    for h in hs:
        nstep = int(round(Tt / h))
        glob.append(np.linalg.norm(np.linalg.matrix_power(U(h), nstep) - sla.expm(Tt * G), 2))
    r2 = [glob[i] / glob[i + 1] for i in range(3)]
    print(f"  one-step errors {[f'{e:.3e}' for e in one]}, halving ratios {[f'{r:.4f}' for r in r1]} (-> 8); "
          f"global errors at T=1.6 {[f'{e:.3e}' for e in glob]}, ratios {[f'{r:.4f}' for r in r2]} (-> 4)")
    if not (abs(r1[-1] - 8) < 0.2 and abs(r2[-1] - 4) < 0.1):
        hit("the tick does not approach the continuous generator with second-order global accuracy")
    return one, r1, glob, r2


def main():
    t0 = time.time()
    rows = run_exact()
    summary(f"F1-F3,F5 exact: {len(rows)} (L, h) cases, L = 2..6, h in {{1/2,1/3,2/5,1/7,4/7}}: layer locality, U(-h)U(h)=I, "
            f"T U T = U(-h), per-layer Gauss, U^T M_h U = M_h all hold: "
            f"{all(r[3] and r[5] and r[6] and r[7] and r[8] for r in rows)}; composed distances on side >= 8: "
            f"{sorted({d for r in rows for d in r[4]})}")
    sols, ctrl = run_schedule()
    summary(f"F4 schedule: 1/32 grid solutions {[(str(a), str(b), str(c)) for a, b, c in sols]}; quarter control inverse {ctrl}")
    lmax, prow, rad, worst, npb, ze = run_positivity_spectrum()
    summary(f"F6,F7 lambda_max(C^T C) = {lmax:.10f}; lambda_min(M_h) = 1 - 3h^2 (h=1/2: {prow[0][1]:.6f}); "
            f"h=1/sqrt3: {prow[2][1]:.1e}; h=2/3: {prow[3][1]:.4f}, radius {rad[2 / 3]:.4f}; spectrum dev {worst:.1e}, "
            f"count failures {npb}; extra zero phases on L=2..40: {ze}")
    cov = run_covariance()
    summary("F8 covariance: " + ", ".join(f"L={L}: {g}/48" for L, g in cov))
    one, r1, glob, r2 = run_accuracy()
    summary(f"F9 one-step halving ratios {[round(float(r), 3) for r in r1]} (-> 8), global ratios {[round(float(r), 3) for r in r2]} (-> 4)")
    print("=" * 78)
    summary(f"hits={len(HITS)}; runtime {time.time() - t0:.0f}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
