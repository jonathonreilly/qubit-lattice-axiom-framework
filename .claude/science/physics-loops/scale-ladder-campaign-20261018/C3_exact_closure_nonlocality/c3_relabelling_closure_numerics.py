#!/usr/bin/env python3
"""C3 part (a): local vs non-local (SLAC / band-limited) lattice relabellings of a scalar, 1D torus Z_L.

Generators G[xi] = pi^T X_xi phi; for such bilinears {G[xi],G[eta]} = +-G-matrix [X_xi, X_eta], so
(a) holds iff [X_xi, X_eta] lies in the image {X_zeta}.  Translation covariance => X_xi = sum_p xihat_p X_p with
X_p e_{k'} = f(k'+p, k') e_{k'+p} (momentum basis, k = 2 pi n / L), and by the grading the image test reduces to
[X_p, X_q] in span{X_{p+q}} (1-dim least squares per pair).  Floating point (numpy, complex128); every claimed
"exact" identity here is an identity to machine precision on the stated finite tori, i.e. a numerical check, the
general statements are proved in the hand-back (Theorems A, B).

Families:
  A  uniform-vs-nonuniform sub-bracket [X_0, X_p] in span X_p (Theorem A): fails for local/continuous symbols
     (B14 central G_m, 4th-order improved, random finite-range transport, SLAC symbol with aliased (full-support) f);
     holds exactly for SLAC with the no-wrap (band-limited) f.
  C  full closure for the SLAC/no-wrap ("projected continuum") transport of density weight w: fails for L >= 4
     (consistent with Theorem B); L=3, w=-1 closes (sl2 adjoint control); L=3, w=0 closes but degenerately
     ([X_1,X_-1]=0, outside Theorem B's hypothesis (S)).
  W  band-limited window: [X_xi,X_eta] phi = X_[xi,eta] phi exactly when spec(xi),spec(eta) in |n|<=nL and
     spec(phi) in |n| <= m - 2 nL (Shannon-sampling statement); fails for phi near the band edge.
  S  real-space SLAC kernel is not absolutely summable: sum_{|x|<=R} |D_0x| grows like log R (non-local, discontinuous symbol).
"""
import sys

import numpy as np

RES = {"pass": 0, "fail": 0}
TOL = 1e-10


def check(tag, ok, msg):
    RES["pass" if ok else "fail"] += 1
    print(("PASS" if ok else "FAIL") + f": {tag} {msg}", flush=True)


def nbar(n, L):
    """representative of n mod L in (-L/2, L/2] (for odd L symmetric)."""
    r = n % L
    return r - L if r > L // 2 else r


class Mom:
    def __init__(self, L):
        self.L = L
        self.m = L // 2
        self.ns = list(range(L))  # residues; index = residue

    def op(self, p, fn):
        """matrix in momentum basis (rows: outgoing residue): X_p e_{k'} = fn(k'bar, pbar) e_{k'+p}; fn returns None for 0."""
        L = self.L
        X = np.zeros((L, L), complex)
        for kp in range(L):
            v = fn(nbar(kp, L), nbar(p, L))
            if v is not None and v != 0:
                X[(kp + p) % L, kp] = v
        return X


def proj_resid(Y, X):
    """relative residual of Y after best fit by c X (1-dim least squares); returns (res, c)."""
    nx = np.vdot(X, X).real
    ny = np.linalg.norm(Y)
    if ny < 1e-14:
        return 0.0, 0.0
    if nx < 1e-28:
        return 1.0, 0.0
    c = np.vdot(X, Y) / nx
    return np.linalg.norm(Y - c * X) / ny, c


def realspace_to_mom(A):
    L = A.shape[0]
    F = np.exp(-2j * np.pi * np.outer(np.arange(L), np.arange(L)) / L) / np.sqrt(L)  # F[k,x]
    return F @ A @ F.conj().T


def local_X_family(L, which, rng=None):
    """real-space translation-covariant transport X_xi = sum_b xi_b T^b A T^-b; returns function p -> momentum matrix."""
    # A: finite-range matrix 'anchored' at bond 0 (sites 0..range)
    A = np.zeros((L, L))
    if which == "B14":  # G_m = sum xi_b (phi_{b+1}-phi_b)(pi_b+pi_{b+1})/2 -> delta phi_x
        A[0, 1] += .5; A[0, 0] -= .5; A[1, 1] += .5; A[1, 0] -= .5
    elif which == "imp4":  # bond-centred 4th-order improved difference, spread over the 2 endpoints
        for (r, c, v) in [(0, 1, 9 / 8), (0, 0, -9 / 8), (0, 2, -1 / 24), (0, L - 1, 1 / 24)]:
            A[r, c] += v / 2; A[(r + 1) % L, c] += v / 2
    elif which == "rand":
        for r in (L - 1, 0, 1, 2):
            for c in (L - 1, 0, 1, 2):
                A[r, c] = rng.normal()
        A -= np.diag(np.diag(A))  # keep generic
        A[:, 0] -= A.sum(axis=1)  # annihilate constants (scalar transport)
    T = np.roll(np.eye(L), 1, axis=0)  # T e_x = e_{x+1}
    mats = {}
    for p in range(L):
        Xp = np.zeros((L, L), complex)
        for b in range(L):
            Tb = np.linalg.matrix_power(T, b)
            Xp += np.exp(2j * np.pi * p * b / L) * (Tb @ A @ Tb.T)
        mats[p] = realspace_to_mom(Xp)
    return mats


def slac_family(L, w=0.0, wrap="none"):
    """projected-continuum transport: f = i (k'bar + w pbar) (2pi/L) on non-wrapping k', 0 on wrapping (wrap='none');
    wrap='alias' keeps f on all k' (aliased/folded continuum transport)."""
    M = Mom(L)
    s = 2 * np.pi / L

    def fn(kb, pb):
        if wrap == "none" and abs(kb + pb) > M.m:
            return None
        if L % 2 == 0 and wrap == "none" and (kb + pb) == -M.m:
            return None
        return 1j * s * (kb + w * pb)
    return {p: M.op(p, fn) for p in range(L)}


def famA(L, mats, tag, expect_ok):
    D = mats[0]
    worst = 0.0
    for p in range(1, L):
        Y = D @ mats[p] - mats[p] @ D
        r, _ = proj_resid(Y, mats[p])
        worst = max(worst, r)
    ok = (worst < TOL) if expect_ok else (worst > 1e-3)
    check(tag, ok, f"L={L}: max_p rel. residual of [X_0,X_p] off span(X_p) = {worst:.3e} ({'closes' if worst < TOL else 'does NOT close'})")


def full_closure_defect(L, mats):
    worst, where = 0.0, None
    for p in range(1, L):
        for q in range(1, L):
            if p == q:
                continue
            Y = mats[p] @ mats[q] - mats[q] @ mats[p]
            r, _ = proj_resid(Y, mats[(p + q) % L])
            if r > worst:
                worst, where = r, (nbar(p, L), nbar(q, L))
    return worst, where


def window_test(L, nL, w=0.0, rng=None):
    """band-limited window: xi, eta random with |n|<=nL; phi random with |n| <= m - 2 nL (inner) or only edge modes."""
    mats = slac_family(L, w)
    m = L // 2
    s = 2 * np.pi / L

    def rand_spec(nmax):
        v = np.zeros(L, complex)
        for n in range(-nmax, nmax + 1):
            v[n % L] = rng.normal() + 1j * rng.normal()
        return v
    xi, eta = rand_spec(nL), rand_spec(nL)
    Xxi = sum(xi[p] * mats[p] for p in range(L))
    Xeta = sum(eta[p] * mats[p] for p in range(L))
    # zeta = xi d eta - eta d xi computed in the continuum (band <= 2 nL, no wrap as 2 nL <= m)
    zeta = np.zeros(L, complex)
    for a in range(-nL, nL + 1):
        for b in range(-nL, nL + 1):
            zeta[(a + b) % L] += xi[a % L] * eta[b % L] * 1j * s * (b - a)
    Xz = sum(zeta[p] * mats[p] for p in range(L))
    Cm = Xxi @ Xeta - Xeta @ Xxi
    # sign: [xi d, eta d] = (xi eta' - eta xi') d  -> X_xi X_eta - X_eta X_xi = X_zeta (operators acting on phi)
    Dm = Cm - Xz
    inner = rand_spec(m - 2 * nL)
    edge = np.zeros(L, complex)
    edge[m % L] = 1.0; edge[(-m) % L] = 1.0
    e_in = np.linalg.norm(Dm @ inner) / max(np.linalg.norm(Cm @ inner), 1e-300)
    e_edge = np.linalg.norm(Dm @ edge) / max(np.linalg.norm(Cm @ edge), 1e-300)
    return e_in, e_edge


if __name__ == "__main__":
    rng = np.random.default_rng(20261018)
    Ls = [int(a) for a in sys.argv[1:]] or [5, 7, 9, 12, 16]
    # ---- A: Theorem A illustrations
    for L in Ls:
        famA(L, local_X_family(L, "B14"), f"A1_B14_L{L}", expect_ok=False)
        famA(L, local_X_family(L, "imp4"), f"A2_imp4_L{L}", expect_ok=False)
        famA(L, local_X_family(L, "rand", rng), f"A3_randlocal_L{L}", expect_ok=False)
        famA(L, slac_family(L, 0.0, wrap="alias"), f"A4_SLAC_aliased_L{L}", expect_ok=False)
        famA(L, slac_family(L, 0.0, wrap="none"), f"A5_SLAC_nowrap_w0_L{L}", expect_ok=True)
        famA(L, slac_family(L, 0.5, wrap="none"), f"A6_SLAC_nowrap_whalf_L{L}", expect_ok=True)
    # ---- C: full closure
    for L in Ls:
        for w in (0.0, 0.5, -1.0):
            d, wh = full_closure_defect(L, slac_family(L, w))
            check(f"C1_L{L}_w{w}", d > 1e-3, f"SLAC/no-wrap transport, weight w={w}: full closure FAILS, max rel. defect {d:.3e} at (pbar,qbar)={wh} (Theorem B: (S),(W) hold, so it must fail)")
        mats = slac_family(L, 0.0)
        r1 = mats[1] @ mats[0] - mats[0] @ mats[1]
        lam1 = proj_resid(mats[0] @ mats[1] - mats[1] @ mats[0], mats[1])[1]
        lam2 = proj_resid(mats[0] @ mats[2] - mats[2] @ mats[0], mats[2])[1]
        s11 = np.linalg.norm(mats[1] @ mats[L - 1] - mats[L - 1] @ mats[1])
        check(f"C2_L{L}", s11 > 1e-6 and abs(lam2 / lam1 - 2) < 1e-10,
              f"hypotheses of Theorem B hold for this realisation: |[X_1,X_-1]|={s11:.3e} != 0, Lam_2/Lam_1 = {(lam2/lam1).real:.12f}")
    d, _ = full_closure_defect(3, slac_family(3, -1.0))
    check("C3_L3_wm1", d < TOL, f"L=3, w=-1 (vector-field weight): closes exactly, defect {d:.1e} (sl2 = modes -1,0,1 in the adjoint rep; Theorem B's L>=4 bound is sharp)")
    m3 = slac_family(3, 0.0)
    d, _ = full_closure_defect(3, m3)
    s11 = np.linalg.norm(m3[1] @ m3[2] - m3[2] @ m3[1])
    check("C4_L3_w0", d < TOL and s11 < TOL, f"L=3, w=0: closes (defect {d:.1e}) only degenerately, [X_1,X_-1] = {s11:.1e} (hypothesis (S) fails)")
    # ---- W: band-limited window exactness
    for (L, nL) in [(9, 1), (13, 2), (17, 3), (25, 4), (33, 5)]:
        e_in, e_edge = window_test(L, nL, 0.0, rng)
        check(f"W_L{L}_n{nL}", e_in < 1e-12 and e_edge > 1e-3,
              f"spec(xi,eta) in |n|<={nL}: rel. defect on phi with |n|<={L//2-2*nL}: {e_in:.1e} (exact); on band-edge phi: {e_edge:.3e} (not exact)")
    # ---- S: SLAC real-space kernel non-summable
    L = 2001
    x = np.arange(1, L // 2 + 1)
    # SLAC on odd L: D_{0x} = (pi/L) (-1)^{x+1} / sin(pi x / L)
    Dx = (np.pi / L) * (-1.0) ** (x + 1) / np.sin(np.pi * x / L)
    sums = [np.abs(Dx[:R]).sum() for R in (10, 100, 1000)]
    check("S1", sums[2] - sums[1] > 1.5 and sums[1] - sums[0] > 1.5,
          f"SLAC kernel |D_0x| ~ 1/|x|: partial l1 sums R=10,100,1000: {sums[0]:.3f}, {sums[1]:.3f}, {sums[2]:.3f} (log growth; symbol discontinuous at the zone edge)")
    print(f"TOTAL: PASS={RES['pass']} FAIL={RES['fail']}")
