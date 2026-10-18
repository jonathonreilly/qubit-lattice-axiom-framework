#!/usr/bin/env python3
"""C3 part (b): the {G,C} bracket at order phi^2 for a 1D lattice scalar on Z_L (L odd), local vs non-local.

Quadratic forms Q_A = z^T A z / 2 in z = (phi, pi), {phi_x, pi_y} = delta_xy:  {Q_A, Q_B} = z^T (A J B - B J A) z / 2.
  G[xi]  = pi^T X_xi phi                         (relabelling, A_G = [[0, X^T],[X, 0]])
  H(N)   = sum_x N_x h_x,  h = pi*pi/2 + (c/2) (D_g phi)*(D_g phi)   with '*' either the ULTRALOCAL product or the
           ANTI-ALIASED product (u*v)^_K = sum_{k1+k2=K, no wrap} u^_k1 v^_k2  (band-limited / sampling-theory product).
(b) asks: {G[xi], H(N)} = H(N') + {G_grav[xi], coupling(N)}  with N' FREE.  For uniform xi, G_grav = 0 (it is built
from differences of xi), so the uniform part is   {P, H(N)} = H(N')  -- a lattice Leibniz rule (Theorem C).
Families (floating point; least squares over all N' in R^L; 'exact' = machine precision on the stated tori):
  U1-U4  uniform part: local D (central, 4th-order, random antisymmetric finite range) with ultralocal or anti-aliased
         density FAILS; SLAC D with ultralocal density FAILS; SLAC D with anti-aliased density CLOSES with N' = +D N (bracket order {P,H}).
  N1     non-uniform xi, SLAC transport (no-wrap) + anti-aliased H: residual after best N' (nonzero: needs coupling).
  N2-N4  ... absorbed by a coupling sum_x N_x sum_{|r|<=R} (E xi)_{x+r} T^(r)_x (E = SLAC; T^(r)_x = tau_x T^(r)_0 arbitrary,
         fully non-local quadratic forms in the fields), least squares over all T^(r)_0 and N' (per configuration) on
         2R+4 random configurations.  R = 0 is the B14 (N-local) placement; R = L//2 is the general translation-covariant
         coupling, exact by the factorisation lemma (the residual vanishes on uniform xi, ker E = constants).
First run (kept as c3_gc_leibniz_run1_Nprime_sign_BUG.log) had a sign error in the EXPECTED N' (= -D N); the
computed N' was +D N, which is the correct sign for {P,H} with {phi,pi}=1 (derivation in the hand-back).
"""
import sys

import numpy as np

RES = {"pass": 0, "fail": 0}


def check(tag, ok, msg):
    RES["pass" if ok else "fail"] += 1
    print(("PASS" if ok else "FAIL") + f": {tag} {msg}", flush=True)


def nbar(n, L):
    r = n % L
    return r - L if r > L // 2 else r


def shift(L):
    return np.roll(np.eye(L), 1, axis=0)  # (T u)_x = u_{x-1}


def circ(L, coeffs):
    """translation-invariant real-space operator (D u)_x = sum_r coeffs[r] u_{x+r}."""
    D = np.zeros((L, L))
    for r, v in coeffs.items():
        for x in range(L):
            D[x, (x + r) % L] += v
    return D


def slac(L):
    k = np.array([2 * np.pi * nbar(n, L) / L for n in range(L)])
    F = np.exp(-1j * np.outer(np.arange(L), np.arange(L)) * 2 * np.pi / L) / np.sqrt(L)  # F[n,x]
    D = F.conj().T @ np.diag(1j * k) @ F
    assert np.abs(D.imag).max() < 1e-12
    return D.real


def product_form(L, N, kind):
    """symmetric M with sum_x N_x (u*v)_x = u^T M v."""
    if kind == "ultralocal":
        return np.diag(N)
    F = np.exp(-1j * np.outer(np.arange(L), np.arange(L)) * 2 * np.pi / L) / L  # uhat = F u
    Nt = np.array([sum(N[x] * np.exp(2j * np.pi * K * x / L) for x in range(L)) for K in range(L)])
    W = np.zeros((L, L), complex)
    m = L // 2
    for a in range(L):
        for b in range(L):
            if abs(nbar(a, L) + nbar(b, L)) <= m:
                W[a, b] = Nt[(a + b) % L]
    M = F.T @ W @ F
    assert np.abs(M.imag).max() < 1e-10
    M = M.real
    return (M + M.T) / 2


def Hform(L, N, Dg, c, kind):
    M = product_form(L, N, kind)
    Z = np.zeros((L, L))
    return np.block([[c * Dg.T @ M @ Dg, Z], [Z, M]])  # z^T A z/2 = (c/2)(Dg phi)^T M (Dg phi) + pi^T M pi /2


def Gform(X):
    L = X.shape[0]
    Z = np.zeros((L, L))
    return np.block([[Z, X.T], [X, Z]])  # z^T A z /2 = pi^T X phi


def pb(A, B):
    L2 = A.shape[0]
    L = L2 // 2
    J = np.block([[np.zeros((L, L)), np.eye(L)], [-np.eye(L), np.zeros((L, L))]])
    return A @ J @ B - B @ J @ A


def sym_basis_vec(M):
    iu = np.triu_indices(M.shape[0])
    return M[iu]


def lsq_resid(target, cols):
    """relative residual of target (matrix) after least squares over span(cols)."""
    t = sym_basis_vec(target)
    if not cols:
        return 1.0, None
    A = np.stack([sym_basis_vec(c) for c in cols], axis=1)
    sol, *_ = np.linalg.lstsq(A, t, rcond=None)
    r = np.linalg.norm(A @ sol - t) / max(np.linalg.norm(t), 1e-300)
    return r, sol


def uniform_test(L, D, Dg, kind, c=0.7, rng=None):
    N = 1 + 0.3 * rng.normal(size=L)
    target = pb(Gform(D), Hform(L, N, Dg, c, kind))
    cols = [Hform(L, np.eye(L)[x], Dg, c, kind) for x in range(L)]
    r, sol = lsq_resid(target, cols)
    return r, sol, N


def slac_transport(L, w=0.0):
    """real-space X_xi builder for the no-wrap projected-continuum transport; returns function xi -> X."""
    s = 2 * np.pi / L
    m = L // 2
    F = np.exp(-1j * np.outer(np.arange(L), np.arange(L)) * 2 * np.pi / L) / np.sqrt(L)
    Xp = {}
    for p in range(L):
        Xm = np.zeros((L, L), complex)
        for kp in range(L):
            kb, pb_ = nbar(kp, L), nbar(p, L)
            if abs(kb + pb_) <= m:
                Xm[(kp + p) % L, kp] = 1j * s * (kb + w * pb_)
        Xp[p] = F.conj().T @ Xm @ F  # real-space matrix of X_p (xi = e^{i p x} normalised as sum_p xihat_p X_p)

    def build(xi):
        xh = np.fft.fft(xi) / L  # xi_x = sum_p xh_p e^{2 pi i p x/L}
        X = sum(xh[p] * Xp[p] for p in range(L))
        assert np.abs(X.imag).max() < 1e-10
        return X.real
    return build


if __name__ == "__main__":
    rng = np.random.default_rng(1018)
    Ls = [int(a) for a in sys.argv[1:]] or [7, 9, 11]
    for L in Ls:
        Dfw = circ(L, {1: 1, 0: -1})
        Dc = circ(L, {1: .5, -1: -.5})
        D4 = circ(L, {1: 2 / 3, -1: -2 / 3, 2: -1 / 12, -2: 1 / 12})
        R = rng.normal(size=4)
        Dr = circ(L, {1: R[0], -1: -R[0], 2: R[1], -2: -R[1], 3: R[2], -3: -R[2]})
        Ds = slac(L)
        for nm, D in (("central", Dc), ("imp4", D4), ("randlocal", Dr)):
            for kind in ("ultralocal", "antialiased"):
                r, _, _ = uniform_test(L, D, D if kind == "antialiased" else Dfw, kind, rng=rng)
                check(f"U_{nm}_{kind}_L{L}", r > 1e-3, f"uniform part {{P,H(N)}} = H(N'), D={nm} (local), {kind} density: FAILS, rel. residual {r:.3e}")
        r, _, _ = uniform_test(L, Ds, Ds, "ultralocal", rng=rng)
        check(f"U_SLAC_ultralocal_L{L}", r > 1e-3, f"D=SLAC (non-local) with ULTRALOCAL density: FAILS, rel. residual {r:.3e} (Theorem C: full-support kernel)")
        r, sol, N = uniform_test(L, Ds, Ds, "antialiased", rng=rng)
        dn = np.linalg.norm(sol - Ds @ N) / np.linalg.norm(Ds @ N)  # {P,h} = -(D h) by Leibniz => H(+D N)
        check(f"U_SLAC_antialiased_L{L}", r < 1e-10 and dn < 1e-8,
              f"D=SLAC with ANTI-ALIASED density: CLOSES, rel. residual {r:.1e}, N' = +D_SLAC N to {dn:.1e}")
        # ---- non-uniform xi
        build = slac_transport(L, 0.0)
        X1 = build(np.ones(L))
        check(f"N0_L{L}", np.abs(X1 - Ds).max() < 1e-10, "SLAC transport at uniform xi reproduces the SLAC derivative")
        c = 0.7
        confs = []
        for _ in range(4):
            N = 1 + 0.3 * rng.normal(size=L)
            xi = 0.5 * rng.normal(size=L)
            confs.append((N, xi))
        Hcols = [Hform(L, np.eye(L)[x], Ds, c, "antialiased") for x in range(L)]
        Szz = np.kron(np.eye(2), shift(L))
        # N1: no coupling
        worst = 0.0
        for N, xi in confs:
            tgt = pb(Gform(build(xi)), Hform(L, N, Ds, c, "antialiased"))
            r, _ = lsq_resid(tgt, Hcols)
            worst = max(worst, r)
        check(f"N1_L{L}", worst > 1e-3, f"non-uniform xi, no coupling: residual after best N' = {worst:.3e} (coupling needed, as in the continuum)")
        # N2(R): coupling with lapse-strain separation <= R:  sum_x N_x sum_{|r|<=R} (D xi)_{x+r} T^(r)_x,
        # T^(r)_x = tau_x T^(r)_0 arbitrary (fully non-local in the fields).  R = 0 is the B14 placement (N-local);
        # R = m = L//2 is the fully general translation-covariant coupling (factorisation lemma => exact).
        m = L // 2
        iu = np.triu_indices(2 * L)
        nT = len(iu[0])
        Sx_list = [np.linalg.matrix_power(Szz, x) for x in range(L)]
        Ebasis = []
        for j in range(nT):
            E = np.zeros((2 * L, 2 * L))
            E[iu[0][j], iu[1][j]] = 1
            E[iu[1][j], iu[0][j]] = 1
            Ebasis.append(E)
        trans = [[(Sx_list[x] @ E @ Sx_list[x].T)[iu] for x in range(L)] for E in Ebasis]  # trans[j][x]
        def scan(build_, Dg_, kind_, Rs):
          r_of_R = {}
          Hc = [Hform(L, np.eye(L)[x], Dg_, c, kind_) for x in range(L)]
          for Rr in Rs:
              offs = list(range(-Rr, Rr + 1))
              nconf = len(offs) + 3
              cf = [(1 + 0.3 * rng.normal(size=L), 0.5 * rng.normal(size=L)) for _ in range(nconf)]
              nunk = nT * len(offs) + L * nconf
              rows, rhs = [], []
              blockN = np.stack([h[iu] for h in Hc], axis=1)
              for ci, (N, xi) in enumerate(cf):
                  tgt = pb(Gform(build_(xi)), Hform(L, N, Dg_, c, kind_))
                  u = Ds @ xi
                  row = np.zeros((nT, nunk))
                  for oi, r in enumerate(offs):
                      wgt = N * np.roll(u, -r)  # N_x u_{x+r}
                      for j in range(nT):
                          col = np.zeros(nT)
                          for x in range(L):
                              if wgt[x] != 0:
                                  col += wgt[x] * trans[j][x]
                          row[:, oi * nT + j] = col
                  row[:, nT * len(offs) + L * ci: nT * len(offs) + L * (ci + 1)] = blockN
                  rows.append(row)
                  rhs.append(tgt[iu])
              A = np.vstack(rows)
              b = np.concatenate(rhs)
              sol, *_ = np.linalg.lstsq(A, b, rcond=None)
              r_of_R[Rr] = np.linalg.norm(A @ sol - b) / np.linalg.norm(b)
              print(f"   [{kind_}] L={L} R={Rr}: {A.shape[0]} eqs, {A.shape[1]} unknowns, rel. residual {r_of_R[Rr]:.3e}", flush=True)
          return r_of_R
        r_of_R = scan(build, Ds, "antialiased", range(0, m + 1))
        check(f"N2_L{L}", r_of_R[0] > 1e-3, f"N-LOCAL coupling (R=0, B14 placement) with arbitrary non-local T_0: NOT absorbed, rel. residual {r_of_R[0]:.3e}")
        check(f"N3_L{L}", r_of_R[m] < 1e-9, f"fully general coupling (lapse-strain separation up to R=L//2={m}): ABSORBED, rel. residual {r_of_R[m]:.1e} (factorisation lemma)")
        first = min([R_ for R_ in r_of_R if r_of_R[R_] < 1e-9], default=None)
        check(f"N4_L{L}", True, f"smallest lapse-strain separation that absorbs exactly: R = {first} (of m = {m}); residuals {', '.join(f'{v:.1e}' for v in r_of_R.values())} (informational)")
        # negative control: B14 local transport + ultralocal density (uniform part fails) is NOT absorbable even at R = m
        A14 = np.zeros((L, L)); A14[0, 1] += .5; A14[0, 0] -= .5; A14[1, 1] += .5; A14[1, 0] -= .5
        T1 = shift(L)

        def build14(xi):
            X = np.zeros((L, L))
            for b_ in range(L):
                Tb = np.linalg.matrix_power(T1, b_)
                X += xi[b_] * (Tb @ A14 @ Tb.T)
            return X
        rc = scan(build14, Dfw, "ultralocal", [m])
        check(f"N5_L{L}", rc[m] > 1e-3, f"negative control: B14 local G_m + ultralocal H_m, fully general coupling R={m}: NOT absorbed, rel. residual {rc[m]:.3e} (the uniform-xi part carries no strain, so no coupling can cancel it)")
    print(f"TOTAL: PASS={RES['pass']} FAIL={RES['fail']}")
