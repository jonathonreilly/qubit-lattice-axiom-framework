#!/usr/bin/env python3
"""Static spin-2 (TT) vacuum stiffness of the supplied two-qubit cubic Dirac walk.

Source note:
  docs/TWO_QUBIT_CUBIC_DIRAC_WALK_INDUCED_TT_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-10-26.md

Supplied premises (not derived): the two-qubit site and walk family, the exact generator
H_a = i Log U, the midpoint metric couplings M1-M4 and the lapse couplings L1/L2, and the
identification of the static vacuum (filled lower band) energy with the induced action.

  A. exact identities (sympy): Einstein-Hilbert normalisation for TT modes, continuum minimal
     coupling of the half-density Dirac operator at O(h), heat-kernel coefficient with the
     determinant half-factor, the Clifford trace identity, the rho series, and the continuum
     sharp-cutoff value of the same bubble;
  B. an independent implementation of the response: exact diagonalisation of k-chains on an
     L = 6 periodic lattice against the second-order Clifford-trace formula;
  C. the O(h) vertices of M1-M4 converge to the continuum minimal-coupling vertex;
  D. Brillouin-zone coefficients: TT stiffness channels at b* (two resolutions) and b_iso,
     positivity, the O_h cubic fit and its (1,2,3) prediction, the isotropic projection,
     non-uniqueness across couplings, a plain-midpoint quadrature cross-check, and the exact
     zero of the O(q^2) lapse response.
Numbers are numerical with convergence estimates, not interval-certified.
"""
from __future__ import annotations

import itertools
import os
import sys

for _var in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS"):
    os.environ.setdefault(_var, "1")

import numpy as np
import sympy as sp
from scipy.linalg import expm

import two_qubit_cubic_dirac_walk_induced_tt_stiffness_2026_10_26_helpers as cc

AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/TWO_QUBIT_CUBIC_DIRAC_WALK_INDUCED_TT_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-10-26.md",
    "scripts/two_qubit_cubic_dirac_walk_induced_tt_stiffness_2026_10_26_helpers.py",
)

PASS = FAIL = 0


def check(name, ok, kind="numerical"):
    global PASS, FAIL
    ok = bool(ok)
    PASS += ok
    FAIL += (not ok)
    print(f"{'PASS' if ok else 'FAIL'} [{kind}] {name}", flush=True)


# ----------------------------------------------------------------- A. exact identities
def ricci_scalar(g, coords):
    n = len(coords)
    gi = g.inv()
    Gam = [[[sum(gi[a, d] * (sp.diff(g[d, b], coords[c]) + sp.diff(g[d, c], coords[b]) - sp.diff(g[b, c], coords[d]))
                 for d in range(n)) / 2 for c in range(n)] for b in range(n)] for a in range(n)]
    R = 0
    for b in range(n):
        for c in range(n):
            Rbc = 0
            for a in range(n):
                Rbc += sp.diff(Gam[a][b][c], coords[a]) - sp.diff(Gam[a][b][a], coords[c])
                for d in range(n):
                    Rbc += Gam[a][a][d] * Gam[d][b][c] - Gam[a][c][d] * Gam[d][b][a]
            R += gi[b, c] * Rbc
    return R


def part_a_exact():
    print("== A. exact identities", flush=True)
    x, y, z = X = sp.symbols("x y z", real=True)
    q, eps = sp.symbols("q epsilon", positive=True)
    for name, hmat in (("T2g (h_xy)", sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, 0]])),
                       ("Eg (h_xx = -h_yy)", sp.Matrix([[1, 0, 0], [0, -1, 0], [0, 0, 0]]))):
        h = hmat * eps * sp.cos(q * z)
        g = sp.eye(3) + h
        dens = sp.sqrt(g.det()) * ricci_scalar(g, X)
        d2 = sp.diff(dens, eps, 2).subs(eps, 0) / 2
        avg = sp.integrate(sp.simplify(d2), (z, 0, 2 * sp.pi / q)) * q / (2 * sp.pi)
        dh2 = sum(sp.diff(h[i, j], X[k]) ** 2 for i in range(3) for j in range(3) for k in range(3))
        target = -sp.Rational(1, 4) * sp.integrate(sp.diff(dh2, eps, 2).subs(eps, 0) / 2, (z, 0, 2 * sp.pi / q)) * q / (2 * sp.pi)
        check(f"EH normalisation {name}: cell average of sqrt(gamma) R at O(h^2) = -(1/4) <(d h)^2>",
              sp.simplify(avg - target) == 0, "exact")
        lin = sp.integrate(sp.diff(dens, eps).subs(eps, 0), (z, 0, 2 * sp.pi / q))
        check(f"EH normalisation {name}: O(h) term integrates to zero", sp.simplify(lin) == 0, "exact")
    # continuum minimal coupling at O(h), half-density form, arbitrary symmetric h(x)
    s1 = sp.Matrix([[0, 1], [1, 0]]); s2 = sp.Matrix([[0, -sp.I], [sp.I, 0]]); s3 = sp.Matrix([[1, 0], [0, -1]])
    Z2 = sp.zeros(2)
    alpha = [sp.Matrix(sp.BlockMatrix([[Z2, s], [s, Z2]])) for s in (s1, s2, s3)]
    beta = sp.Matrix(sp.BlockMatrix([[sp.eye(2), Z2], [Z2, -sp.eye(2)]]))
    gam = [beta * a for a in alpha]
    dl = sp.Symbol("delta")
    hf = [[sp.Function(f"h{min(i, j)}{max(i, j)}")(x, y, z) for j in range(3)] for i in range(3)]
    hm = sp.Matrix(3, 3, lambda i, j: hf[i][j])
    gmet = sp.eye(3) + dl * hm
    einv = sp.eye(3) - dl * hm / 2
    ecov = sp.eye(3) + dl * hm / 2
    gi = sp.eye(3) - dl * hm
    Chr = [[[sp.expand(sum(gi[a, l] * (sp.diff(gmet[l, b], X[c]) + sp.diff(gmet[l, c], X[b]) - sp.diff(gmet[b, c], X[l]))
                           for l in range(3)) / 2) for c in range(3)] for b in range(3)] for a in range(3)]
    omega = [[[sp.expand(sum(einv[a, j] * (sp.diff(ecov[b, j], X[i]) - sum(Chr[kk][i][j] * ecov[b, kk] for kk in range(3)))
                             for j in range(3))) for b in range(3)] for a in range(3)] for i in range(3)]
    omega = [[[sp.series(omega[i][a][b], dl, 0, 2).removeO() for b in range(3)] for a in range(3)] for i in range(3)]
    Gamma_sp = [-sum((omega[i][a][bb] * (gam[a] * gam[bb] - gam[bb] * gam[a]) for a in range(3) for bb in range(3)),
                     sp.zeros(4)) / 8 for i in range(3)]
    psi = sp.Matrix([sp.Function(f"psi{c}")(x, y, z) for c in range(4)])
    w = 1 + dl * (hm.trace()) / 4
    winv = 1 - dl * (hm.trace()) / 4
    chi = winv * psi
    Hcov = sp.zeros(4, 1)
    for a in range(3):
        for i in range(3):
            Hcov += -sp.I * alpha[a] * einv[a, i] * (sp.diff(chi, X[i]) + Gamma_sp[i] * chi)
    Hcov = w * Hcov
    Hsym = sp.zeros(4, 1)
    for a in range(3):
        for i in range(3):
            Hsym += (-sp.I / 2) * (alpha[a] * einv[a, i] * sp.diff(psi, X[i]) + sp.diff(alpha[a] * einv[a, i] * psi, X[i]))
    diff = (Hcov - Hsym).applyfunc(lambda e: sp.expand(sp.series(sp.expand(e), dl, 0, 2).removeO()))
    check("half-density covariant Dirac operator = (1/2){alpha^a e_a^i, p_i} + O(h^2) for arbitrary symmetric h(x)",
          all(sp.simplify(e) == 0 for e in diff), "exact")
    # heat kernel with the determinant half-factor
    Rs, Lam, sv = sp.symbols("R Lambda s", positive=True)
    tr_a1 = 4 * (Rs / 6 - Rs / 4)
    check("tr a1 = -R/3 for D^2 = -nabla^2 + R/4 (four spinor components)", sp.simplify(tr_a1 + Rs / 3) == 0, "exact")
    GammaR = sp.Rational(1, 2) * sp.integrate(sv ** -1 * (4 * sp.pi * sv) ** -2 * sv * tr_a1, (sv, 1 / Lam ** 2, sp.oo))
    coefEH = sp.simplify(-GammaR / Rs)
    check(f"Gamma_E = -(1/2) log det D^2 with proper-time cutoff gives 1/(16 pi G) = {coefEH} = Lambda^2/(96 pi^2) per Dirac fermion",
          sp.simplify(coefEH - Lam ** 2 / (96 * sp.pi ** 2)) == 0, "exact")
    # Clifford trace identity
    t1 = sp.Matrix([[0, 1], [1, 0]]); t2 = sp.Matrix([[0, -sp.I], [sp.I, 0]]); t3 = sp.Matrix([[1, 0], [0, -1]])
    kr = sp.kronecker_product
    G5 = [kr(t1, sp.eye(2)), kr(t2, sp.eye(2)), kr(t3, s1), kr(t3, s2), kr(t3, s3)]
    check("the walk's five Gammas are Hermitian anticommuting involutions",
          all((G5[i] * G5[j] + G5[j] * G5[i] - 2 * (1 if i == j else 0) * sp.eye(4)).is_zero_matrix
              for i in range(5) for j in range(5)), "exact")
    av = sp.symbols("a1:6", real=True); bv = sp.symbols("b1:6", real=True); ov = sp.symbols("o1:6", real=True)
    dot = lambda u, v: sum(ui * vi for ui, vi in zip(u, v))
    sl = lambda v: sum((vi * Gi for vi, Gi in zip(v, G5)), sp.zeros(4))
    O = sl(ov)
    rhs = sp.expand(dot(ov, ov) * (1 + dot(av, bv)) - 2 * dot(av, ov) * dot(bv, ov))
    lhs = sp.expand((((sp.eye(4) - sl(av)) / 2) * O * ((sp.eye(4) + sl(bv)) / 2) * O).trace())
    lhs2 = sp.expand((((sp.eye(4) + sl(av)) / 2) * O * ((sp.eye(4) - sl(bv)) / 2) * O).trace())
    check("Tr[P+(a) O P-(b) O] = Tr[P-(a) O P+(b) O] = o^2 (1 + a.b) - 2 (a.o)(b.o)",
          sp.simplify(lhs - rhs) == 0 and sp.simplify(lhs2 - rhs) == 0, "exact")
    u = sp.Symbol("u", positive=True)
    rho = sp.acos(1 - u) / sp.sqrt(1 - (1 - u) ** 2)
    ser = sp.series(rho, u, 0, 5).removeO()
    check("rho(1-u) = 1 + u/3 + 2u^2/15 + 2u^3/35 + 8u^4/315 + O(u^5)",
          sp.simplify(ser - (1 + u / 3 + 2 * u ** 2 / 15 + 2 * u ** 3 / 35 + 8 * u ** 4 / 315)) == 0, "exact")
    fs = sp.Symbol("f")
    serp = sp.series(sp.diff(sp.acos(fs) / sp.sqrt(1 - fs ** 2), fs).subs(fs, 1 - u), u, 0, 4).removeO()
    check("rho'(1-u) = -1/3 - 4u/15 - 6u^2/35 - 32u^3/315 + O(u^4)",
          sp.simplify(serp - (-sp.Rational(1, 3) - sp.Rational(4, 15) * u - sp.Rational(6, 35) * u ** 2
                              - sp.Rational(32, 315) * u ** 3)) == 0, "exact")
    # continuum sharp-cutoff value of the same bubble
    t, xx, yy, zz = sp.symbols("t x y z", real=True)
    n = sp.Matrix([xx, yy, zz])
    qh = sp.Matrix([0, 0, 1])
    epsm = sp.diag(1, -1, 0) / sp.sqrt(2)
    a = n + t * qh; b = n - t * qh
    na = sp.sqrt(1 + 2 * t * zz + t ** 2); nb = sp.sqrt(1 - 2 * t * zz + t ** 2)
    o = epsm * n / 2
    num = (o.T * o)[0] * (1 + (a.T * b)[0] / (na * nb)) - 2 * ((a.T * o)[0] / na) * ((b.T * o)[0] / nb)
    F = 2 * num / (na + nb)
    F2 = sp.expand(sp.series(F, t, 0, 3).removeO().coeff(t, 2))
    th, ph = sp.symbols("theta phi", real=True)
    e = sp.expand(F2.subs({xx: sp.sin(th) * sp.cos(ph), yy: sp.sin(th) * sp.sin(ph), zz: sp.cos(th)}))
    J = sp.simplify(sp.integrate(sp.integrate(e * sp.sin(th), (ph, 0, 2 * sp.pi)), (th, 0, sp.pi)))
    kG = sp.simplify(-J / (4 * (2 * sp.pi) ** 3))
    print(f"   continuum sharp cutoff: int dOmega F2 = {J}; c_G / Lambda^2 = {kG}", flush=True)
    check("continuum sharp-cutoff TT bubble: c_G = 13 Lambda^2/(840 pi^2) = (52/35) x the heat-kernel value",
          sp.simplify(kG - sp.Rational(13, 840) / sp.pi ** 2) == 0, "exact")


# ----------------------------------------------------------------- B. exact diagonalisation
I2 = np.eye(2)
T1 = np.array([[0, 1], [1, 0]], complex); T2 = np.array([[0, -1j], [1j, 0]]); T3 = np.diag([1.0, -1]).astype(complex)
TAU = [np.kron(T1, I2), np.kron(T2, I2)]
ALPHA = [-np.kron(T3, x) for x in (T1, T2, T3)]


def Umat(W, k):
    c = np.cos(k); sn = np.sin(k)
    ph = np.array([1.0, c.sum(), c[0] * c[1] + c[0] * c[2] + c[1] * c[2], c.prod()])
    f, h1, h2 = W.F @ ph
    b0, b1, b2 = W.b
    g = [sn[i] * (b0 + b1 * (c[(i + 1) % 3] + c[(i + 2) % 3]) + b2 * c[(i + 1) % 3] * c[(i + 2) % 3]) for i in range(3)]
    U0 = f * np.eye(4) + 1j * (h1 * TAU[0] + h2 * TAU[1]) - 1j * sum(g[i] * ALPHA[i] for i in range(3))
    M = expm(0.5j * W.theta * (np.cos(W.chi) * TAU[0] + np.sin(W.chi) * TAU[1]))
    return M @ U0 @ M, np.array(g)


def Hmat(W, k):
    U, _ = Umat(W, k)
    lam, V = np.linalg.eig(U)
    return 1j * (V @ np.diag(np.log(lam / np.abs(lam))) @ np.linalg.inv(V))


def Omat(W, coupling, eps, km, ka, kb):
    if coupling in ("M1", "M2"):
        U, g = Umat(W, km)
        f = np.real(np.trace(U)) / 4
        rho = np.arccos(f) / np.sqrt(1 - f * f) if coupling == "M1" else 1.0
        P = rho * g
        return -0.5 * sum(eps[i, j] * ALPHA[i] * P[j] for i in range(3) for j in range(3))
    if coupling == "M4":
        d = 1e-5
        E = np.eye(3)
        dH = [(Hmat(W, km + d * E[i]) - Hmat(W, km - d * E[i])) / (2 * d) for i in range(3)]
        return -0.5 * sum(eps[i, j] * np.sin(km[j]) * dH[i] for i in range(3) for j in range(3))
    if coupling == "L2":
        return 0.5 * (Hmat(W, ka) + Hmat(W, kb))
    raise ValueError(coupling)


def chain_energy(Hs, Os, lam):
    L = len(Hs)
    A = np.zeros((4 * L, 4 * L), complex)
    for j in range(L):
        A[4 * j:4 * j + 4, 4 * j:4 * j + 4] = Hs[j]
        jp = (j + 1) % L
        A[4 * jp:4 * jp + 4, 4 * j:4 * j + 4] += lam * Os[j]
        A[4 * j:4 * j + 4, 4 * jp:4 * jp + 4] += lam * Os[j].conj().T
    A = 0.5 * (A + A.conj().T)
    ev = np.linalg.eigvalsh(A)
    return ev[ev < 0].sum()


def ed_vs_formula(W, coupling, pol, L):
    qh, eps = cc.tt_eps("z", pol)
    q = 2 * np.pi / L
    grid = 2 * np.pi * np.arange(L) / L
    lams = (2e-3, 1e-3)
    tot = {l: 0.0 for l in lams}
    pert = 0.0
    for kx, ky in itertools.product(grid, grid):
        ks = [np.array([kx, ky, kz]) for kz in grid]
        Hs = [Hmat(W, k) for k in ks]
        Os = [Omat(W, coupling, eps, k + 0.5 * q * qh, k + q * qh, k) for k in ks]
        E0 = chain_energy(Hs, Os, 0.0)
        for l in lams:
            tot[l] += (chain_energy(Hs, Os, l) + chain_energy(Hs, Os, -l) - 2 * E0) / (2 * l * l)
        km = np.array([k + 0.5 * q * qh for k in ks])
        pert += -np.sum(cc.Fval(W, coupling, eps, qh, km, 0.5 * q))
    ed = (4 * tot[lams[1]] - tot[lams[0]]) / 3
    return ed, pert


def part_b_ed():
    print("== B. exact diagonalisation of k-chains vs the second-order formula (L = 6)", flush=True)
    cases = [("bstar", 0.3, np.pi / 2, c, p) for c, p in (("M1", "A"), ("M1", "B"), ("M2", "B"), ("M4", "A"), ("L2", "A"))]
    cases.append(("gold", 0.4, np.pi / 2, "M1", "A"))
    for name, theta, chi, coupling, pol in cases:
        W = cc.Walk(name, theta=theta, chi=chi)
        ed, pt = ed_vs_formula(W, coupling, pol, 6)
        rel = abs(ed - pt) / abs(pt)
        print(f"   {name} theta={theta} {coupling}{pol}: ED {ed:.12f} formula {pt:.12f} rel {rel:.1e}", flush=True)
        check(f"{name} {coupling}{pol} L=6: exact-diagonalisation lambda^2 coefficient = second-order formula (rel < 1e-6)",
              rel < 1e-6)


# ----------------------------------------------------------------- C. vertex continuum limit
def part_c_vertex():
    print("== C. O(h) vertices of M1-M4 converge to the minimal-coupling vertex", flush=True)
    W = cc.Walk("bstar")
    rng = np.random.default_rng(2)
    _, eps = cc.tt_eps("z", "A")
    pts = rng.normal(size=(40, 3))
    for coupling, want in (("M1", 2.0), ("M2", 2.0), ("M3", 2.0), ("M4", 1.0)):
        devs = []
        for a in (0.02, 0.01):
            km = a * pts
            o = cc.vertex(W, coupling, eps, km, km, km)
            target = np.zeros_like(o)
            target[:, 2:] = 0.5 * W.s * (pts @ eps.T)
            devs.append(np.abs(o / a - target).max())
        slope = np.log(devs[0] / devs[1]) / np.log(2)
        print(f"   {coupling}: max |o/a - (1/2) s eps.p| = {devs[0]:.2e} (a=0.02), {devs[1]:.2e} (a=0.01); slope {slope:.2f}",
              flush=True)
        check(f"{coupling}: (1/a) vertex -> continuum minimal-coupling vertex with error O(a^{want:.0f}) (slope {slope:.2f})",
              abs(slope - want) < 0.3 and devs[1] < 0.05)


# ----------------------------------------------------------------- D. Brillouin-zone coefficients
QDIR = {"z": np.array([0, 0, 1.0]), "f": np.array([1, 1, 0.0]) / np.sqrt(2), "d": np.ones(3) / np.sqrt(3),
        "g": np.array([1, 2, 3.0]) / np.sqrt(14)}
RECORDED_ISO = {("bstar", "M1"): 7.36673e-3, ("iso", "M1"): 6.63451e-3,
                ("bstar", "M2"): 3.60420e-3, ("bstar", "M4"): 9.52490e-3}


def cG_channel(walk, coupling, ch, N, inner):
    W = cc.Walk(walk, theta=0.0, chi=np.pi / 2)
    qh, eps = cc.tt_eps(ch[0], ch[1])
    nr, nmu, nph = inner
    I0, I2_, _ = cc.bz_integral(W, coupling, eps, qh, N, kap=1.0, nr=nr, nmu=nmu, nph=nph)
    c2 = -0.25 * I2_                       # q^2 coefficient of e2(q); F is evaluated at t = q/2
    return 2 * c2 / W.s                    # c_G = a^2/(16 pi G) per walk in c = 1 units (tick s a)


def cubic_iso(vals):
    K = {d: vals[d + "A"] + vals[d + "B"] for d in "zfd" if d + "A" in vals}
    B = 2 * (K["z"] - K["f"])
    A = K["z"] - B
    C = 27 * (K["d"] - A - B / 3)
    iso = 0.5 * (A + 0.6 * B + C / 105)
    pred = None
    if "gA" in vals:
        q = QDIR["g"]
        pred = (A + B * np.sum(q ** 4) + C * np.prod(q ** 2), vals["gA"] + vals["gB"])
    return A, B, C, iso, pred, K


def part_d_bz():
    print("== D. Brillouin-zone TT stiffness coefficients (theta = 0)", flush=True)
    chans = ["zA", "zB", "fA", "fB", "dA", "dB", "gA", "gB"]
    lo, hi = (64, (64, 24, 48)), (96, (96, 32, 64))
    res = {}
    for res_name, (N, inner) in (("N64", lo), ("N96", hi)):
        res[res_name] = {ch: cG_channel("bstar", "M1", ch, N, inner) for ch in chans}
        print(f"   b* M1 {res_name}: " + " ".join(f"{ch} {v:.7e}" for ch, v in res[res_name].items()), flush=True)
    dev = max(abs(res["N64"][c] - res["N96"][c]) / res["N96"][c] for c in chans)
    check(f"b* M1: two resolutions (N = 64/96 outer grid, finer inner rule) agree to rel {dev:.1e} < 1e-5", dev < 1e-5)
    vals = res["N96"]
    A, B, C, iso, pred, K = cubic_iso(vals)
    print(f"   b* M1 cubic fit: A = {A:.6e}, B = {B:.6e}, C = {C:.6e}; isotropic c_G = {iso:.7e}", flush=True)
    check(f"b* M1: O_h cubic form fitted on z, (110), (111) predicts the generic (1,2,3) direction (rel {abs(pred[0] - pred[1]) / pred[1]:.1e} < 2e-5)",
          abs(pred[0] - pred[1]) < 2e-5 * pred[1])
    check("b* M1: (111) TT polarisations are degenerate (C3 symmetry)", abs(vals["dA"] - vals["dB"]) < 1e-9 * vals["dA"])
    spread = (max(K.values()) - min(K.values())) / (2 * iso)
    print(f"   b* M1: polarisation-summed stiffness spans {100 * spread:.1f}% of 2 c_G^iso over z, (110), (111)", flush=True)
    check("b* M1: the induced TT stiffness is cubic-anisotropic (spread over directions > 10%)", spread > 0.10)
    check(f"b* M1: c_G^iso = {iso:.6e} reproduces the recorded production value 7.36673e-3 (same implementation; rel < 1e-5)",
          abs(iso - RECORDED_ISO[("bstar", "M1")]) < 1e-5 * iso)
    allpos = all(v > 0 for v in vals.values())
    isos = {("bstar", "M1"): iso}
    for walk, cp in (("iso", "M1"), ("bstar", "M2"), ("bstar", "M4")):
        v = {ch: cG_channel(walk, cp, ch, *lo) for ch in chans[:6]}
        allpos &= all(x > 0 for x in v.values())
        _, _, _, isos[(walk, cp)], _, _ = cubic_iso(v)
        print(f"   {walk} {cp} N64: " + " ".join(f"{ch} {x:.6e}" for ch, x in v.items())
              + f"; c_G^iso = {isos[(walk, cp)]:.6e}", flush=True)
        check(f"{walk} {cp}: c_G^iso = {isos[(walk, cp)]:.5e} reproduces the recorded value {RECORDED_ISO[(walk, cp)]:.5e} (rel < 1e-4)",
              abs(isos[(walk, cp)] - RECORDED_ISO[(walk, cp)]) < 1e-4 * RECORDED_ISO[(walk, cp)])
    check("sign: c_G > 0 in every computed TT channel (M1 at b* and b_iso; M2, M4 at b*)", allpos)
    ratio = isos[("bstar", "M4")] / isos[("bstar", "M2")]
    check(f"non-uniqueness: couplings with the same continuum vertex give c_G^iso differing by a factor {ratio:.2f} > 2", ratio > 2)
    # independent quadrature of one channel: plain periodic midpoint rule, no partition of unity
    W = cc.Walk("bstar", theta=0.0, chi=np.pi / 2)
    qh, eps = cc.tt_eps("z", "A")
    vals_plain = []
    for N in (96, 128):
        g1 = -np.pi + 2 * np.pi * (np.arange(N) + 0.5) / N
        KX, KY, KZ = np.meshgrid(g1, g1, g1, indexing="ij")
        Kp = np.stack([KX.ravel(), KY.ravel(), KZ.ravel()], 1)
        S2 = 0.0
        for i in range(0, Kp.shape[0], 1 << 15):
            _, F2, _ = cc.F2val(W, "M1", eps, qh, Kp[i:i + (1 << 15)])
            S2 += F2.sum()
        vals_plain.append(2 * (-0.25 * S2 / N ** 3) / W.s)
    # the 1/|k| node singularity makes the plain rule converge as O(h^2): extrapolate in h^2
    extrap = (128 ** 2 * vals_plain[1] - 96 ** 2 * vals_plain[0]) / (128 ** 2 - 96 ** 2)
    rel = abs(extrap - vals["zA"]) / vals["zA"]
    print(f"   plain midpoint rule zA: N=96 {vals_plain[0]:.7e}, N=128 {vals_plain[1]:.7e}, h^2-extrapolated {extrap:.7e};"
          f" partition-of-unity value {vals['zA']:.7e}", flush=True)
    check(f"b* M1 zA: plain midpoint quadrature (different rule, h^2-extrapolated) agrees with the partition-of-unity value"
          f" (rel {rel:.1e} < 1e-5)", rel < 1e-5)
    hk = 1 / (96 * np.pi ** 2)
    r = np.sqrt(iso / hk) / np.pi
    print(f"   heat-kernel-equivalent cutoff: Lambda_eff a = {np.sqrt(iso / hk):.4f} = {r:.4f} pi", flush=True)
    check(f"b* M1: Lambda_eff/(pi/a) = {r:.3f} lies in the pre-declared window [0.1, 10]", 0.1 <= r <= 10)
    # lapse: exact zero of the O(q^2) response
    for cp in ("L1", "L2"):
        for ch in ("zA", "dA"):
            cN = cG_channel("bstar", cp, ch, *lo)
            check(f"b* lapse {cp} q||{ch[0]}: O(q^2) lapse stiffness vanishes (|c_N| = {abs(cN):.1e} < 1e-10)", abs(cN) < 1e-10)


def main():
    part_a_exact()
    part_b_ed()
    part_c_vertex()
    part_d_bz()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
