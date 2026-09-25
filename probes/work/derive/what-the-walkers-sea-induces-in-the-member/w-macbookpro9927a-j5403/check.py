#!/usr/bin/env python3
"""check.py for J:derive:what-the-walkers-sea-induces-in-the-member:a2 (worker w-macbookpro9927a-j5403, claude-opus-5-5).

Setting (block 62 as landed): H = (1/2) sum_j {E^j(x).sigma, S_j}, S_j = (T_j - T_j^dag)/(2i); for a uniform frame
H(k) = sigma.v, v_a = sum_j E^j_a sin k_j, H^2 = g^{ij} s_i s_j. The free sea fills every negative-energy state (wbar = 1).
Symmetric strain E = 1 + eps, h = -(eps + eps^T) = -2 eps; s = (sin k_1, sin k_2, sin k_3), r = |s|, <.> = zone average.
Lattice constants: I = <r>, A = <s1^2 s2^2/r^3>, B = <s1^4/r^3>, J = <1/r>, A' = <s1^2 s2^2/r^5>, B' = <s1^4/r^5>.

Families
  Q  pinned sources (block 62 on main; the task)
  E  (b) exact: the uniform-strain sea energy per site to second order is
     (I/6) tr h - (B/8) tr h^2 + (A/8)(tr h)^2 + ((B-3A)/8) sum h_ii^2, with 3B + 6A = I pointwise; a dilation h = lambda 1
     gives exactly -I(1 - lambda/2) = -I (det g)^(-1/6), so no constant plus multiple of sqrt(det g) matches; on traceless
     h the second-order part is -(3A/8) sum h_ii^2 - (B/4) sum_{i<j} h_ij^2 (negative definite), with no trace cross terms
  K  (c) exact: the adiabatic energy per site is (1/32) <[s.hdot^2.s - (s.hdot.s)^2/r^2]/r^3>
     = (1/32)[B' tr hdot^2 - A'(tr hdot)^2 - (B'-3A') sum hdot_ii^2], i.e. block 62's M1 = A'/16, M2 = -A'/16, M3 = B'/16;
     a dilation has zero inertia; beta = -alpha (M1 = 0) is impossible since A' > 0; B' > A' exactly; the two-level
     matrix elements used, exactly at rational unit vectors
  C  [float] the constants as 1D Bessel integrals (log substitution) and on a zone grid; identities to 1e-12; B - 3A < 0,
     B' - 3A' < 0 (cubic anisotropy of both responses)
  T  [float] validation: the second-order formula for eps cos(q.x) equals exact diagonalisation of the strained walk on an
     antiperiodic 6^3 torus; the adiabatic excess |<+|Hdot|->|^2/Delta^3 at one k by direct time evolution
  A  [float] (a) the static q^2 coefficient: q^0 parts -B/8 and -A/2; TT stiffness per channel (three directions, two
     polarisations each), K = 8 c2/sum h^2 > 0 and direction dependent; relabelling modes h = n xi^T + xi n^T carry
     nonzero q^2 energy (not relabelling-invariant); alpha/K per channel versus 1/4
"""
import hashlib
import itertools
import json
import os
import subprocess
import sys
import time
from fractions import Fraction as Fr

import mpmath as mp
import numpy as np
import sympy as sp

T0 = time.time()
REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), *([os.pardir] * 5)))
FAILS = []
ONLY = set(sys.argv[1:])


def rep(fam, ok, msg):
    if not ok:
        FAILS.append(fam)
    print(f"[{fam}] {'PASS' if ok else 'FAIL'} {msg}")
    sys.stdout.flush()


# ------------------------------------------------------------------ Q
N62 = ("docs/ADMISSIBILITY_RULE_ANGLES_ARE_THE_TILT_OF_THE_COINS_FRAME_WITH_THEM_TWO_DISTURBANCES_TRAVEL_AT_ONE_DIRECTION"
       "_FREE_SPEED_AND_THE_PRICE_IS_A_CONSERVED_STRESS_BOUNDED_THEOREM_NOTE_2026-09-21.md")
SRC = [("block62", "60c5f194d940a7bbaf1cdd545296e31d74a02f1a", N62,
        "0d631bc3e1ceaabca7f8bf37cfa8a463cb8ec4b97c512b14cccfc297790315f6",
        ["**Generator** `H = ½ Σ_j {E^j(x)·σ, S_j}`, `S_j = (T_j − T_j†)/(2i)`, `(T_jψ)(x) = ψ(x + e_j)`: the bond from `x` "
         "along `j` carries the mean of its two ends' coin vectors.",
         "`R_2=-(p^2/4) tr(h^T h)+(1/2)|h p|^2-(1/2)(p^T h p)tr(h)+(p^2/4)tr(h)^2`; `F_2 = −K w̄ (u R_1 + R_2)` summed over "
         "wave vectors.",
         "- **Kinetic terms** `(1/w̄)[α ḣ_ij ḣ_ij + β ḣ²]` (rotation-invariant), and `(1/w̄)[M_1 Σ ḣ_jj² + M_2 Σ_{i<j} ḣ_ii "
         "ḣ_jj + M_3 Σ_{i<j} ḣ_ij²]` (the cube's symmetry only); the first is `M_3 = 2M_1 − M_2`.",
         "*Statement.* (a) For a uniform frame, `H(k) = Σ_j (E^j·σ) sin k_j` and `H(k)² = (Σ_ij g^{ij} sin k_i sin k_j)·1`.",
         "With `α = K/4` the disturbances' speed at long wavelength is the walker's top speed, one site per ambient tick; "
         "nothing here forces that value."], "main")]
TASKQ = ("92631f30519815c72f4703011c12669d49a71e1e", "J:derive:what-the-walkers-sea-induces-in-the-member:a2",
         ["take the free sea of block 62's framed walk on Z^3 (every negative-energy state filled, wbar = 1)",
          "(b) The order-q^0 part: the sea's response to a uniform strain, and whether it is the expansion of a multiple of "
          "sqrt(det g).",
          "(c) Its energy to second order in a uniform time-dependent strain at small frequency: the induced alpha and beta.",
          "(d) Compare the induced alpha/K with 1/4 and beta/alpha with -1.",
          "a proof that the order-|q|^2 response is not relabelling-invariant is also a HIT."])


def git_show(spec, branch=None):
    r = subprocess.run(["git", "show", spec], cwd=REPO, capture_output=True)
    if r.returncode != 0:
        subprocess.run(["git", "fetch", "--quiet", "origin", branch or spec.split(":")[0]], cwd=REPO, capture_output=True)
        r = subprocess.run(["git", "show", spec], cwd=REPO, capture_output=True)
    return r.stdout if r.returncode == 0 else None


def fam_Q():
    ok, msg = True, []
    for tag, c, p, h, quotes, br in SRC:
        b = git_show(f"{c}:{p}", br)
        if b is None:
            rep("Q", False, f"{tag} unreadable")
            return
        good = hashlib.sha256(b).hexdigest() == h
        n = sum(q in b.decode() for q in quotes)
        ok &= good and n == len(quotes)
        msg.append(f"{tag}@{c[:8]} {'sha ok' if good else 'SHA MISMATCH'} {n}/{len(quotes)}")
    b = git_show(f"{TASKQ[0]}:probes/TASKS.json", "ai/probes")
    what = next((t["what"] for t in json.loads(b.decode()) if t["id"] == TASKQ[1]), "") if b else ""
    n = sum(q in what for q in TASKQ[2])
    ok &= n == len(TASKQ[2])
    msg.append(f"task@{TASKQ[0][:8]} {n}/{len(TASKQ[2])}")
    rep("Q", ok, "; ".join(msg))


# ------------------------------------------------------------------ exact averaging machinery
S1, S2, S3, R = sp.symbols("s1 s2 s3 r", positive=True)
SV = sp.Matrix([S1, S2, S3])
Isym, Asym, Bsym, Jsym, Apsym, Bpsym = sp.symbols("I A B J Ap Bp", positive=True)


def hsym():
    hs = sp.symbols("h11 h22 h33 h12 h13 h23")
    h11, h22, h33, h12, h13, h23 = hs
    return sp.Matrix([[h11, h12, h13], [h12, h22, h23], [h13, h23, h33]]), hs


def zone_average(expr, table):
    """expr: polynomial in s1,s2,s3 times powers of r (r = |s|). table[(m, sorted exps)] -> average of s^e / r^m."""
    expr = sp.expand(expr)
    out = 0
    for term in sp.Add.make_args(expr):
        coeff, rest = term.as_independent(S1, S2, S3, R)
        pw = sp.Poly(rest * R ** 20, S1, S2, S3, R)
        (e1, e2, e3, er), = pw.monoms()
        m = 20 - er
        c = pw.coeffs()[0] * coeff
        if e1 % 2 or e2 % 2 or e3 % 2:
            continue
        key = (m, tuple(sorted((e1, e2, e3), reverse=True)))
        out += c * table[key]
    return sp.expand(out)


def fam_E():
    h, hs = hsym()
    eps = sp.symbols("epsilon")
    X = -eps * (SV.T * h * SV)[0] + eps ** 2 * (SV.T * h * h * SV)[0] / 4
    Ek = sp.series(-sp.sqrt(R ** 2 + X), eps, 0, 3).removeO()          # per k, h -> eps h
    Ek = sp.expand(Ek.subs(eps, 1))
    table = {(-1, (0, 0, 0)): Isym,                                     # <r>
             (1, (2, 0, 0)): Isym / 3,                                  # <s_i^2/r> = I/3 (sum s_i^2/r = r)
             (3, (4, 0, 0)): Bsym, (3, (2, 2, 0)): Asym}
    # the zeroth-order term -r averages to -I; handle it apart (it carries r^{+1})
    Ek0 = sp.expand(Ek + R)
    avg = -Isym + zone_average(Ek0, table)
    trh, trh2, sq = h.trace(), (h * h).trace(), sum(h[i, i] ** 2 for i in range(3))
    claim = -Isym + Isym / 6 * trh - Bsym / 8 * trh2 + Asym / 8 * trh ** 2 + (Bsym - 3 * Asym) / 8 * sq
    ok1 = sp.simplify((avg - claim).subs(Isym, 3 * Bsym + 6 * Asym)) == 0
    ident = sp.simplify(((S1 ** 2 + S2 ** 2 + S3 ** 2) ** 2 / R ** 3).subs(R, sp.sqrt(S1 ** 2 + S2 ** 2 + S3 ** 2))
                        - sp.sqrt(S1 ** 2 + S2 ** 2 + S3 ** 2)) == 0                 # sum_ij s_i^2 s_j^2/r^3 = r
    lam, C, c0 = sp.symbols("lambda C c0")
    dil_exact = sp.simplify(sp.sqrt(((1 - lam / 2) * SV).dot((1 - lam / 2) * SV)).subs(
        sp.sqrt(S1 ** 2 + S2 ** 2 + S3 ** 2), R) - (1 - lam / 2) * sp.sqrt(S1 ** 2 + S2 ** 2 + S3 ** 2)).subs(lam, sp.Rational(1, 3)) == 0
    # sqrt(det g) for h = lambda 1: g^{-1} = (1 - h/2)^2, det g = (1 - lambda/2)^{-6}
    sdg = (1 - lam / 2) ** -3
    ser = sp.series(c0 + C * sdg - (-Isym * (1 - lam / 2)), lam, 0, 3).removeO()
    sol = sp.solve([ser.coeff(lam, 0), ser.coeff(lam, 1)], [c0, C], dict=True)
    no_sqrt = len(sol) == 1 and sp.simplify(ser.coeff(lam, 2).subs(sol[0])) != 0
    # traceless part and no cross terms
    E2 = claim + Isym - Isym / 6 * trh
    lam0 = sp.symbols("mu")
    htl = h.subs(hs[2], -hs[0] - hs[1])
    E2tl = sp.expand(E2.subs(hs[2], -hs[0] - hs[1]))
    target = sp.expand(-(3 * Asym / 8) * (hs[0] ** 2 + hs[1] ** 2 + (hs[0] + hs[1]) ** 2)
                       - (Bsym / 4) * (hs[3] ** 2 + hs[4] ** 2 + hs[5] ** 2))
    ok_tl = sp.expand(E2tl - target) == 0
    hmix = htl + lam0 * sp.eye(3)
    E2mix = sp.expand((-(Bsym / 8) * (hmix * hmix).trace() + Asym / 8 * hmix.trace() ** 2
                       + (Bsym - 3 * Asym) / 8 * sum(hmix[i, i] ** 2 for i in range(3))))
    no_cross = sp.expand(E2mix - E2tl) == 0
    rep("E", ok1 and ident and dil_exact and no_sqrt and ok_tl and no_cross,
        "(b) uniform strain, per site: -I + (I/6)tr h - (B/8)tr h^2 + (A/8)(tr h)^2 + ((B-3A)/8)sum h_ii^2 (sympy, cubic "
        "averages, 3B+6A = I pointwise); dilation h = lambda 1: exactly -I(1-lambda/2) = -I(det g)^(-1/6); c0 + C sqrt(det g) "
        "matching orders 0 and 1 fails at order 2; traceless h: -(3A/8)sum h_ii^2 - (B/4)sum_{i<j} h_ij^2 (negative "
        "definite), no trace cross terms")


def fam_K():
    h, hs = hsym()
    num = (SV.T * h * h * SV)[0] / (32 * R ** 3) - ((SV.T * h * SV)[0]) ** 2 / (32 * R ** 5)
    table = {(3, (2, 0, 0)): Jsym / 3, (5, (4, 0, 0)): Bpsym, (5, (2, 2, 0)): Apsym}
    T = zone_average(num, table)
    trh, trh2, sq = h.trace(), (h * h).trace(), sum(h[i, i] ** 2 for i in range(3))
    claim = (Bpsym * trh2 - Apsym * trh ** 2 - (Bpsym - 3 * Apsym) * sq) / 32
    ok1 = sp.simplify((T - claim).subs(Jsym, 3 * Bpsym + 6 * Apsym)) == 0
    # block 62's cubic form: M1 sum hd_jj^2 + M2 sum_{i<j} hd_ii hd_jj + M3 sum_{i<j} hd_ij^2
    h11, h22, h33, h12, h13, h23 = hs
    cub = sp.expand(claim)
    M1 = cub.coeff(h11, 2)
    M2 = sp.expand(cub).coeff(h11, 1).coeff(h22, 1)
    M3 = cub.coeff(h12, 2)
    okM = sp.simplify(M1 - Apsym / 16) == 0 and sp.simplify(M2 + Apsym / 16) == 0 and sp.simplify(M3 - Bpsym / 16) == 0
    bulk = sp.simplify(claim.subs({h11: 1, h22: 1, h33: 1, h12: 0, h13: 0, h23: 0})) == 0
    # B' - A' = (1/2)<(s1^2 - s2^2)^2 / r^5> > 0 (swap symmetry)
    sym_ok = sp.expand((S1 ** 4 + S2 ** 4) / 2 - S1 ** 2 * S2 ** 2 - (S1 ** 2 - S2 ** 2) ** 2 / 2) == 0
    # two-level matrix elements at rational unit vectors, exactly
    sig = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
    dot = lambda a, b: sum(x * y for x, y in zip(a, b))
    sv = lambda v: sum((v[i] * sig[i] for i in range(3)), sp.zeros(2))
    okme = True
    for n, n2, w in (((sp.Rational(1, 3), sp.Rational(2, 3), sp.Rational(2, 3)), (sp.Rational(2, 7), sp.Rational(3, 7), sp.Rational(6, 7)), (1, -1, 2)),
                     ((sp.Rational(2, 3), sp.Rational(-1, 3), sp.Rational(2, 3)), (sp.Rational(1, 3), sp.Rational(2, 3), sp.Rational(2, 3)), (3, 0, -1))):
        Pp = (sp.eye(2) + sv(n2)) / 2
        Pm = (sp.eye(2) - sv(n)) / 2
        val = sp.simplify((Pp * sv(w) * Pm * sv(w)).trace())
        okme &= sp.simplify(val - (dot(w, w) * (1 + dot(n, n2)) - 2 * dot(n, w) * dot(n2, w)) / 2) == 0
        Pp1 = (sp.eye(2) + sv(n)) / 2
        okme &= sp.simplify((Pp1 * sv(w) * Pm * sv(w)).trace() - (dot(w, w) - dot(n, w) ** 2)) == 0
    rep("K", ok1 and okM and bulk and sym_ok and okme,
        "(c) adiabatic energy per site (1/32)<[s.hd^2.s - (s.hd.s)^2/r^2]/r^3> = (1/32)[B' tr hd^2 - A'(tr hd)^2 - "
        "(B'-3A') sum hd_ii^2] (J = 3B'+6A'): M1 = A'/16, M2 = -A'/16, M3 = B'/16; a dilation has zero inertia; beta = -alpha "
        "needs M1 = 0, impossible as A' > 0; B' - A' = (1/2)<(s1^2-s2^2)^2/r^5> > 0; |<+,n'|s.w|-,n>|^2 = "
        "[|w|^2(1+n.n') - 2(n.w)(n'.w)]/2 exactly at rational unit vectors")


# ------------------------------------------------------------------ C [float]
def constants():
    mp.mp.dps = 40
    phi = lambda t: mp.exp(-t / 2) * mp.besseli(0, t / 2)
    ph1 = lambda t: mp.exp(-t / 2) * (mp.besseli(1, t / 2) - mp.besseli(0, t / 2)) / 2
    ph2 = lambda t: mp.exp(-t / 2) * (mp.besseli(0, t / 2) - 2 * mp.besseli(1, t / 2)
                                      + (mp.besseli(0, t / 2) + mp.besseli(2, t / 2)) / 2) / 4
    U = [-60, -20, -5, 0, 2, 4, 6, 8, 10, 12, 15, 20, 30, 45, 60]
    Q = lambda f: mp.quad(lambda u: f(mp.e ** u) * mp.e ** u, U)
    c = {"I": Q(lambda t: t ** mp.mpf(-1.5) * (1 - phi(t) ** 3)) / (2 * mp.sqrt(mp.pi)),
         "A": Q(lambda t: t ** mp.mpf(0.5) * ph1(t) ** 2 * phi(t)) / mp.gamma(1.5),
         "B": Q(lambda t: t ** mp.mpf(0.5) * ph2(t) * phi(t) ** 2) / mp.gamma(1.5),
         "J": Q(lambda t: t ** mp.mpf(-0.5) * phi(t) ** 3) / mp.gamma(0.5),
         "Ap": Q(lambda t: t ** mp.mpf(1.5) * ph1(t) ** 2 * phi(t)) / mp.gamma(2.5),
         "Bp": Q(lambda t: t ** mp.mpf(1.5) * ph2(t) * phi(t) ** 2) / mp.gamma(2.5)}
    return {k: float(v) for k, v in c.items()}, c


CONST = {}


def fam_C():
    t0 = time.time()
    c, cm = constants()
    CONST.update(c)
    N = 160
    k = (np.arange(N) + 0.5) * 2 * np.pi / N - np.pi
    s = np.sin(k)
    g = {}
    acc = dict(I=0.0, A=0.0, B=0.0, J=0.0, Ap=0.0, Bp=0.0)
    for i in range(N):
        s1 = s[i]
        s2, s3 = np.meshgrid(s, s, indexing="ij")
        r2 = s1 * s1 + s2 * s2 + s3 * s3
        r = np.sqrt(r2)
        acc["I"] += r.sum(); acc["A"] += (s1 * s1 * s2 * s2 / r ** 3).sum(); acc["B"] += (s1 ** 4 / r ** 3).sum()
        acc["J"] += (1 / r).sum(); acc["Ap"] += (s1 * s1 * s2 * s2 / r ** 5).sum(); acc["Bp"] += (s1 ** 4 / r ** 5).sum()
    g = {kk: v / N ** 3 for kk, v in acc.items()}
    ids = (abs(3 * cm["B"] + 6 * cm["A"] - cm["I"]) < 1e-12, abs(3 * cm["Bp"] + 6 * cm["Ap"] - cm["J"]) < 1e-12,
           abs(3 * g["B"] + 6 * g["A"] - g["I"]) < 1e-12, abs(3 * g["Bp"] + 6 * g["Ap"] - g["J"]) < 1e-12)
    close = all(abs(g[kk] - c[kk]) < 2e-3 * abs(c[kk]) for kk in c)
    ok = all(ids) and close and c["B"] - 3 * c["A"] < 0 and c["Bp"] - 3 * c["Ap"] < 0
    rep("C", ok, f"[float] 1D Bessel integrals: I = {c['I']:.12f}, A = {c['A']:.12f}, B = {c['B']:.12f}, J = {c['J']:.12f}, "
        f"A' = {c['Ap']:.12f}, B' = {c['Bp']:.12f}; identities 3B+6A = I, 3B'+6A' = J to 1e-12; zone grid N=160 within "
        f"0.2%; B-3A = {c['B'] - 3 * c['A']:.5f}, B'-3A' = {c['Bp'] - 3 * c['Ap']:.5f} (cubic anisotropy)  ({time.time() - t0:.0f}s)")


# ------------------------------------------------------------------ T [float]
SIG = [np.array([[0, 1], [1, 0]], complex), np.array([[0, -1j], [1j, 0]]), np.array([[1, 0], [0, -1]], complex)]


def hamiltonian(L, Efield):
    n = L ** 3
    idx = lambda x: (x[0] % L) * L * L + (x[1] % L) * L + (x[2] % L)
    H = np.zeros((2 * n, 2 * n), complex)
    for x in itertools.product(range(L), repeat=3):
        Ex = Efield(x)
        for j in range(3):
            y = list(x)
            y[j] += 1
            sign = -1.0 if y[j] == L else 1.0
            Ey = Efield(tuple(v % L for v in y))
            A = sum(0.5 * (Ex[j, a] + Ey[j, a]) * SIG[a] for a in range(3))
            blk = sign * A / (2j)
            i0, i1 = 2 * idx(x), 2 * idx(y)
            H[i0:i0 + 2, i1:i1 + 2] += blk
            H[i1:i1 + 2, i0:i0 + 2] += blk.conj().T
    return H


def Fint(s, c, h, n, tau):
    sq = s * np.cos(tau * n)[:, None] + c * np.sin(tau * n)[:, None]
    a = np.sqrt((s * s).sum(0))
    b = np.sqrt((sq * sq).sum(0))
    w = -(h @ (s + sq)) / 8.0
    ww, sw, qw, ss = (w * w).sum(0), (s * w).sum(0), (sq * w).sum(0), (s * sq).sum(0)
    return (ww * (a * b + ss) - 2 * sw * qw) / (a * b * (a + b))


def fam_T():
    t0 = time.time()
    L = 6
    q = 2 * np.pi / L * np.array([0., 0., 1.])
    h = np.array([[0.3, 0.7, -0.2], [0.7, -0.5, 0.4], [-0.2, 0.4, 0.9]])
    E0 = np.linalg.eigvalsh(hamiltonian(L, lambda x: np.eye(3)))
    E0 = E0[E0 < 0].sum()
    res = []
    for d in (1e-3, 2e-3):
        ev = np.linalg.eigvalsh(hamiltonian(L, lambda x, d=d: np.eye(3) - d * (h / 2) * np.cos(q @ np.array(x))))
        res.append((ev[ev < 0].sum() - E0) / d ** 2)
    ks = np.array([2 * np.pi * (np.array(m) + 0.5) / L for m in itertools.product(range(L), repeat=3)]).T
    form = -Fint(np.sin(ks), np.cos(ks), h, np.array([0., 0., 1.]), 2 * np.pi / L).sum()
    ok_t = all(abs(v - form) < 1e-6 * abs(form) for v in res)
    # adiabatic excess at one k
    from scipy.linalg import expm
    rng = np.random.default_rng(0)
    s = rng.normal(size=3)
    hd = rng.normal(size=(3, 3))
    hd = (hd + hd.T) / 2
    Hs = lambda v: sum(v[a] * SIG[a] for a in range(3))
    ratios = []
    for rate in (1e-2, 5e-3):
        dt, nt = 0.005, 8000
        U = np.linalg.eigh(Hs(s))[1]
        psi, gacc, t = U[:, 0].copy(), 0.0, 0.0
        for _ in range(nt):
            ramp = np.sin(min(t / 20.0, 1) * np.pi / 2) ** 2
            vmid = (np.eye(3) - rate * (gacc + 0.5 * dt * ramp) * hd / 2) @ s
            psi = expm(-1j * Hs(vmid) * dt) @ psi
            gacc += dt * ramp
            t += dt
        v = (np.eye(3) - rate * gacc * hd / 2) @ s
        e = np.real(np.conj(psi) @ Hs(v) @ psi) + np.linalg.norm(v)
        wd = -(rate * hd / 2) @ s
        vh = v / np.linalg.norm(v)
        ratios.append(e / ((wd @ wd - (vh @ wd) ** 2) / (2 * np.linalg.norm(v)) ** 3))
    ok_a = all(abs(r_ - 1) < 0.03 for r_ in ratios)
    rep("T", ok_t and ok_a, f"[float] eps cos(q.x) on the antiperiodic 6^3 torus: exact diagonalisation gives "
        f"{res[0]:.8f}, {res[1]:.8f}, the second-order formula {form:.8f}; one-k adiabatic excess / (|<+|Hdot|->|^2/Delta^3) "
        f"= {ratios[0]:.4f}, {ratios[1]:.4f} at two ramp rates  ({time.time() - t0:.0f}s)")


# ------------------------------------------------------------------ A [float]
def c2(h, n, N, tau=1e-3, chunk=16):
    k = (np.arange(N) + 0.5) * 2 * np.pi / N - np.pi
    K2, K3 = np.meshgrid(k, k, indexing="ij")
    tot = 0.0
    for i0 in range(0, N, chunk):
        K1 = k[i0:i0 + chunk][:, None, None] * np.ones((1, N, N))
        kk = np.stack([K1.ravel(), np.broadcast_to(K2, K1.shape).ravel(), np.broadcast_to(K3, K1.shape).ravel()])
        s, c = np.sin(kk), np.cos(kk)
        f0, fp, fm = Fint(s, c, h, n, 0.0), Fint(s, c, h, n, tau), Fint(s, c, h, n, -tau)
        tot += ((fp + fm - 2 * f0) / (2 * tau * tau)).sum()
    return -tot / N ** 3


def c0(h, n, N):
    k = (np.arange(N) + 0.5) * 2 * np.pi / N - np.pi
    kk = np.stack([m.ravel() for m in np.meshgrid(k, k, k, indexing="ij")])
    return -Fint(np.sin(kk), np.cos(kk), h, n, 0.0).mean()


def symm(i, j):
    m = np.zeros((3, 3))
    m[i, j] = m[j, i] = 1.0
    return m


def fam_A():
    t0 = time.time()
    if not CONST:
        CONST.update(constants()[0])
    Ap, Bp, A, B = CONST["Ap"], CONST["Bp"], CONST["A"], CONST["B"]
    Tk = lambda h: (Bp * np.trace(h @ h) - Ap * np.trace(h) ** 2 - (Bp - 3 * Ap) * np.sum(np.diag(h) ** 2)) / 32
    e3, d110, d111 = np.array([0., 0., 1.]), np.array([1., 1., 0.]) / np.sqrt(2), np.ones(3) / np.sqrt(3)
    u, v = np.array([1., -1., 0.]) / np.sqrt(2), np.array([1., 1., -2.]) / np.sqrt(6)
    # q^0 parts
    okc0 = abs(c0(symm(0, 1), e3, 96) + B / 8) < 5e-4 and abs(c0(2 * np.diag([0., 0., 1.]), e3, 96) + A / 2) < 5e-4
    cases = [("e3 h12", e3, symm(0, 1)), ("e3 diag(1,-1,0)", e3, np.diag([1., -1., 0.])),
             ("110 u e3", d110, np.outer(u, e3) + np.outer(e3, u)), ("110 uu-e3e3", d110, np.outer(u, u) - np.outer(e3, e3)),
             ("111 uv", d111, np.outer(u, v) + np.outer(v, u))]
    rows, oks, Ks, ratios = [], True, [], []
    for name, n, h in cases:
        a, b = c2(h, n, 128), c2(h, n, 192)
        rich = (b * 192 ** 2 - a * 128 ** 2) / (192 ** 2 - 128 ** 2)
        oks &= abs(a - b) < 2e-5 and rich > 0
        K = 8 * rich / np.sum(h * h)
        al = Tk(h) / np.sum(h * h)
        Ks.append(K)
        ratios.append(al / K)
        rows.append(f"{name}: K {K:.4f}, alpha/K {al / K:.3f}")
    g1 = c2(symm(0, 2), e3, 192)
    g3 = c2(2 * np.diag([0., 0., 1.]), e3, 192)
    gauge = g1 > 1e-3 and g3 > 1e-3
    aniso = max(Ks) / min(Ks) > 1.2
    rep("A", okc0 and oks and gauge and aniso and min(ratios) > 0.25,
        f"[float] q^0 parts -B/8 (shear h12=1) and -A/2 (h33=2) reproduced; TT stiffness K = 8 c2/sum h^2 (N = 128, 192, "
        f"Richardson): " + "; ".join(rows) + f"; relabelling modes at q || e3 carry q^2 energy c2 = {g1:.5f} (h13) and "
        f"{g3:.5f} (h33 = 2), where R_2 gives 0: the q^2 part is not relabelling-invariant; K varies by a factor "
        f"{max(Ks) / min(Ks):.2f} over channels; every alpha/K > 1/4  ({time.time() - t0:.0f}s)")


if __name__ == "__main__":
    for tag, fn in (("Q", fam_Q), ("E", fam_E), ("K", fam_K), ("C", fam_C), ("T", fam_T), ("A", fam_A)):
        if not ONLY or tag in ONLY:
            fn()
    print(f"total {time.time() - T0:.0f}s; failing families: {sorted(set(FAILS)) or 'none'}")
    if FAILS:
        print("SUMMARY: ROUTE FAILS AT " + ",".join(sorted(set(FAILS))))
    else:
        print("SUMMARY: PARTIAL exact: the sea's uniform-strain energy to second order in closed form (I, A, B lattice "
              "constants, 3B+6A = I); dilations give -I(det g)^(-1/6), so the q^0 part is no multiple of sqrt(det g), and it "
              "is negative definite on shear; the induced kinetic form M1 = -M2 = A'/16, M3 = B'/16 with zero dilation "
              "inertia, so never beta = -alpha. [float]: the q^2 part is not relabelling-invariant, K_TT > 0 and "
              "direction dependent, alpha/K = 0.29-0.39 > 1/4")
        print("HIT: free sea of block 62's framed walk on Z^3 (wbar = 1): (b) exactly, a uniform strain changes the sea "
              "energy per site by (I/6)tr h - (B/8)tr h^2 + (A/8)(tr h)^2 + ((B-3A)/8)sum h_ii^2, I = <|s|>, A = "
              "<s1^2 s2^2/|s|^3>, B = <s1^4/|s|^3>, 3B+6A = I; a dilation gives exactly -I(det g)^(-1/6), so no multiple of "
              "sqrt(det g), and shear lowers it; (c) exactly, the induced kinetic term is M1 = -M2 = A'/16, M3 = B'/16 "
              "(A' = <s1^2 s2^2/|s|^5>, B' = <s1^4/|s|^5>), zero for dilation, so beta = -alpha is impossible; [float] the "
              "q^2 part is not relabelling-invariant and alpha/K > 1/4 in every channel computed")
