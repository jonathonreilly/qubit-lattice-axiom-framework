#!/usr/bin/env python3
"""The force of second order in the capture rates (blocks 44-49), independent attempt 1 of 3: checks for ATTEMPT.md.

Worker w-macbookpro90c72-j5f35 (claude-opus-5-5).
Exact (sympy, Fractions, the cyclotomic field Q(z), z = e^{2 pi i/12}):
  Q  quoted source lines at pinned heads (blocks 44, 45, 49; the simulator in probes/lib);
  H  the linearized hydrodynamics of the sphere-menu gas: sound speed, transverse mode, the inverse-square wind of a sink;
  S  the Stokeslet of a point momentum sink (field equations and normalization) and the second-order force on a capturing body;
  D  the lattice Green function of the steady equations against a direct solve on the periodic boxes L = 3 and 4.
Floating point, labelled executed/numerical (not claimed): N reads the committed outputs shear_*.txt (nu_T from block 44's own
simulator) and box_green.txt (the box factor of block 49's geometry) and evaluates the force at block 49's parameters.
"""
from __future__ import annotations

import re
import subprocess
import sys
from fractions import Fraction as Fr
from pathlib import Path

import sympy as sp

HERE = Path(__file__).resolve().parent
OUT: list[str] = []
FAILS: list[str] = []
NCHECK = [0]


def check(tag: str, ok: bool, msg: str) -> None:
    OUT.append(f"{'ok  ' if ok else 'FAIL'} {tag}: {msg}")
    NCHECK[0] += 1
    if not ok:
        FAILS.append(tag)


# ------------------------------------------------------------------------------------------------ Q: sources
PIN = {
    "b44": ("502a7a2149a88543c2507b42ce7eec265e6b840e",
            "physics-loop/admissibility-induced-law-block44-records-with-inertia-sound-and-forces-between-bodies-20260920"),
    "b45": ("e07ae767d484763bd9446eb2d5c4c9b05643dd1c", "physics-loop/admissibility-induced-law-block45-the-wind-law-of-capturing-bodies-20260920"),
    "b49": ("589280e3798ef2e39433fad5248c37cc89aed712", "physics-loop/admissibility-induced-law-block49-the-attraction-is-tied-to-growth-20260921"),
}


def git_show(pin: str, path: str) -> str | None:
    sha, branch = PIN[pin]
    r = subprocess.run(["git", "show", f"{sha}:{path}"], capture_output=True, text=True)
    if r.returncode != 0:
        subprocess.run(["git", "fetch", "-q", "origin", branch], capture_output=True, text=True)
        r = subprocess.run(["git", "show", f"{sha}:{path}"], capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None


NOTES = {
    "b44": "docs/ADMISSIBILITY_RULE_RECORDS_WITH_INERTIA_CONTENT_AS_DIRECTION_OF_TRAVEL_CONSERVED_MOMENTUM_STRUCTURELESS_EQUILIBRIUM_"
           "SOUND_SPEED_FORCES_NEED_CAPTURE_OR_EMISSION_BOUNDED_THEOREM_NOTE_2026-09-20.md",
    "b45": "docs/ADMISSIBILITY_RULE_THE_WIND_LAW_FLUX_THEOREMS_INVERSE_SQUARE_WIND_OF_A_CAPTURING_BODY_SECOND_ORDER_MOMENTUM_FLUX_"
           "FORCE_PROPORTIONAL_TO_PRODUCT_OF_CAPTURE_RATES_BOUNDED_THEOREM_NOTE_2026-09-20.md",
    "b49": "docs/ADMISSIBILITY_RULE_THE_ATTRACTION_IS_TIED_TO_GROWTH_A_BODY_IN_BALANCE_DRAWS_NO_WIND_PULL_PROPORTIONAL_TO_NET_UPTAKE_"
           "GROWTH_RATE_FIXED_BY_THE_FORCE_COEFFICIENT_BOUNDED_THEOREM_NOTE_2026-09-21.md",
}


def note_path(pin: str) -> str:
    return NOTES[pin]


QUOTES = [
    ("b44", 113, "With T3's exact relation `J = (1 − ρ) g/√3`"),
    ("b44", 56, "sphere menu: `x → x + e_k` with probability `max(0, s·e_k)/√3`"),
    ("b45", 58, "the simple estimate is `K₀ = √3/(4π ρ(1−ρ))`"),
    ("b49", 84, "in the closure every record that steps onto the body is a sample of the gas"),
    ("b49", 86, "At the next order a body that takes up momentum from a wind slows the gas around it"),
    ("b49", 96, "side 96 with a reservoir at the walls, density `0.3`, `γ = 1`; two solid balls of radius 3, 123 sites each, at separation 16"),
    ("b49", 101, "| body 1 in balance, body 2 captures | `7.24, 7.24` and `7.84, 0` | `0.095 ± 0.015`, `0.123 ± 0.011` | `0.022 ± 0.012`, `0.007 ± 0.018` | `0.146` |"),
    ("b49", 104, "the body in balance is pushed with `0.75 ± 0.06` and pulls the capturing body with `0.10 ± 0.07`"),
]
LIB_QUOTES = [
    ("inertial.py", "pred = np.sqrt((1 - rho0) / 3) if menu == \"six\" else np.sqrt(1 - rho0) / 3"),
    ("inertial_balanced.py", "c1, c2 = (c - sep // 2, c, c), (c - sep // 2 + sep, c, c)"),
    ("inertial_balanced.py", "edge |= (idx[a] < 2) | (idx[a] >= L - 2)"),
]


def family_q() -> None:
    found, missing = 0, []
    cache: dict = {}
    for pin, ln, needle in QUOTES:
        if pin not in cache:
            p = note_path(pin)
            cache[pin] = git_show(pin, p) if p else None
        txt = cache[pin] or ""
        lines = txt.splitlines()
        ok = (needle in txt) if ln is None else (len(lines) >= ln and needle in lines[ln - 1])
        found += ok
        if not ok:
            missing.append(f"{pin}:L{ln}")
    lib = HERE.parents[3] / "lib"
    for fn, needle in LIB_QUOTES:
        ok = (lib / fn).exists() and needle in (lib / fn).read_text()
        found += ok
        if not ok:
            missing.append(fn)
    n = len(QUOTES) + len(LIB_QUOTES)
    check("Q", not missing, f"{found}/{n} quoted source lines verbatim (b44 502a7a21, b45 e07ae767, b49 589280e3, probes/lib)"
          f"{'; missing ' + ','.join(missing) if missing else ''}")


# ------------------------------------------------------------------------------------------------ H: hydrodynamics
rho, nu, nub, k, lam = sp.symbols("rho nu nu_b k lambda", positive=True)
A_NUM = (1 - rho) / sp.sqrt(3)        # number current J = (1 - rho) g / sqrt 3
B_P = 1 / (3 * sp.sqrt(3))            # pressure p = n/(3 sqrt 3)
K0 = sp.sqrt(3) / (4 * sp.pi * rho * (1 - rho))


def family_h() -> None:
    # plane wave e^{ikx + lambda t}: longitudinal (n, g_x) and transverse (g_y)
    Ml = sp.Matrix([[0, -sp.I * k * A_NUM], [-sp.I * k * B_P, -(nu + nub) * k ** 2]])
    cp = sp.expand((Ml - lam * sp.eye(2)).det())
    ok = sp.simplify(cp - (lam ** 2 + (nu + nub) * k ** 2 * lam + k ** 2 * (1 - rho) / 9)) == 0
    c2 = sp.simplify(A_NUM * B_P)
    ok &= sp.simplify(c2 - (1 - rho) / 9) == 0
    lam_t = -nu * k ** 2  # transverse: d_t g_y = nu d_x^2 g_y
    check("H1", ok, "linearized equations dn/dt = -((1-rho)/sqrt3) div g, dg/dt = -(1/(3 sqrt3)) grad n + nu lap g + nu_b grad div g: "
          "longitudinal lambda^2 + (nu+nu_b)k^2 lambda + (1-rho)k^2/9 = 0, sound speed sqrt(1-rho)/3 (the simulator's own prediction); "
          f"transverse lambda = {lam_t} (pure diffusion: what shear_wave.py measures)")
    # steady number sink N: g = -(sqrt3 N/(4 pi (1-rho))) x/r^3, u = g/rho = -K0 N rhat/r^2; flux of J through a sphere = -N
    x, y, z, R, N = sp.symbols("x y z R N", positive=True)
    r = sp.sqrt(x ** 2 + y ** 2 + z ** 2)
    g = [-sp.sqrt(3) * N / (4 * sp.pi * (1 - rho)) * c / r ** 3 for c in (x, y, z)]
    div = sp.simplify(sum(sp.diff(gi, c) for gi, c in zip(g, (x, y, z))))
    g_r = sp.simplify(sum(gi * c for gi, c in zip(g, (x, y, z))) / r)       # radial component, a function of r only
    gr2 = sp.simplify(g_r * (x ** 2 + y ** 2 + z ** 2))                    # r^2 g_r: must be a constant
    flux = sp.simplify(4 * sp.pi * A_NUM * gr2) if not (gr2.free_symbols & {x, y, z}) else sp.oo
    u_mag = sp.simplify(sp.sqrt(3) * N / (4 * sp.pi * (1 - rho)) / R ** 2 / rho)
    ok = div == 0 and sp.simplify(flux + N) == 0 and sp.simplify(u_mag - K0 * N / R ** 2) == 0
    check("H2", ok, "a sink of N records per tick: g = -(sqrt3 N/(4 pi (1-rho))) x/r^3 is divergence-free off 0 with number flux -N "
          "through every sphere, so u = g/rho = -K0 N rhat/r^2 with K0 = sqrt3/(4 pi rho (1-rho)) (block 45's wind)")


# ------------------------------------------------------------------------------------------------ S: Stokeslet and the force
def family_s() -> None:
    x, y, z, R = sp.symbols("x y z R", positive=True)
    X = (x, y, z)
    r = sp.sqrt(x ** 2 + y ** 2 + z ** 2)
    G = [[(sp.KroneckerDelta(i, j) / r + X[i] * X[j] / r ** 3) / (8 * sp.pi * nu) for j in range(3)] for i in range(3)]
    P = [X[j] / (4 * sp.pi * r ** 3) for j in range(3)]
    lap = lambda f: sum(sp.diff(f, c, 2) for c in X)
    ok = True
    for i in range(3):
        for j in range(3):
            ok &= sp.simplify(nu * lap(G[i][j]) - sp.diff(P[j], X[i])) == 0
    for j in range(3):
        ok &= sp.simplify(sum(sp.diff(G[i][j], X[i]) for i in range(3))) == 0
    # normalization. G is homogeneous of degree -1 (x.grad G = -G), so on |x| = R: d_r G = -G/R with G = (I + n n^T)/(8 pi nu R),
    # P_j n_i = n_i n_j/(4 pi R^2); the sphere integral of nu d_r G_ij - P_j n_i must be -delta_ij (unit force e_j on the gas)
    ok_h = all(sp.simplify(sum(c * sp.diff(G[i][j], c) for c in X) + G[i][j]) == 0 for i in range(3) for j in range(3))
    ok_h &= all(sp.simplify(sum(c * sp.diff(P[j], c) for c in X) + 2 * P[j]) == 0 for j in range(3))
    th, ph = sp.symbols("theta phi", real=True)
    nvec = [sp.sin(th) * sp.cos(ph), sp.sin(th) * sp.sin(ph), sp.cos(th)]
    ok2 = ok_h
    for i in range(3):
        for j in range(3):
            Gs = (sp.KroneckerDelta(i, j) + nvec[i] * nvec[j]) / (8 * sp.pi * nu * R)
            integrand = nu * (-Gs / R) - nvec[i] * nvec[j] / (4 * sp.pi * R ** 2)
            val = sp.integrate(sp.integrate(sp.expand(integrand * R ** 2 * sp.sin(th)), (ph, 0, 2 * sp.pi)), (th, 0, sp.pi))
            ok2 &= sp.simplify(val + (1 if i == j else 0)) == 0
    check("S1", ok and ok2, "Stokeslet G = (I/r + x x^T/r^3)/(8 pi nu), pressure x/(4 pi r^3): nu lap G - grad P = 0 and div G = 0 off 0, and "
          "the sphere integral of nu d_r G - P n is -I (unit point force on the gas); so a momentum sink F leaves g = -G F, "
          "p = -F.x/(4 pi r^3), density change 3 sqrt3 p")
    # the force on a capturing body 2 at x2 = r rhat from the sink F1 at the origin: F2 = (C2/rho) g(x2) = -(C2/rho) G(x2) F1
    C1, C2, N2, rr, f = sp.symbols("C1 C2 N2 r f", positive=True)
    rhat = sp.Matrix([1, 0, 0])
    Gx = sp.Matrix(3, 3, lambda i, j: (sp.KroneckerDelta(i, j) + rhat[i] * rhat[j]) / (8 * sp.pi * nu * rr))
    F_axis = -(C2 / rho) * Gx * (f * rhat)
    F_trans = -(C2 / rho) * Gx * (f * sp.Matrix([0, 1, 0]))
    ok = sp.simplify(F_axis[0] + C2 * f / (4 * sp.pi * nu * rho * rr)) == 0 and F_axis[1] == 0 and F_axis[2] == 0
    ok &= sp.simplify(F_trans[1] + C2 * f / (8 * sp.pi * nu * rho * rr)) == 0 and F_trans[0] == 0
    F1 = K0 * C1 * N2 / rr ** 2
    F2mag = sp.simplify(C2 * F1 / (4 * sp.pi * nu * rho * rr))
    ok &= sp.simplify(F2mag - sp.sqrt(3) * C1 * C2 * N2 / (16 * sp.pi ** 2 * nu * rho ** 2 * (1 - rho) * rr ** 3)) == 0
    ref = K0 * C1 * C2 / rr ** 2
    ok &= sp.simplify(F2mag / ref - C2 * (F1 / ref) / (4 * sp.pi * nu * rho * rr)) == 0
    check("S2", ok, "F2 = (C2/rho) g(x2): on the axis, with body 1 pushed towards body 2 by F1, body 2 is pushed towards body 1 by "
          "C2 F1/(4 pi nu rho r) (attraction; half, antiparallel to F1, across the axis); with F1 = K0 C1 N2/r^2 it is "
          "K0 C1 C2 N2/(4 pi nu rho r^3) = sqrt3 C1 C2 N2/(16 pi^2 nu rho^2 (1-rho) r^3), i.e. (F1/ref) C2/(4 pi nu rho r) of K0 C1 C2/r^2")
    # the captured content is g/rho: for f = (rho/4pi)(1 + 3 u.s), <|s|_1> = 3/2, <|s|_1 s_x^2> = 1/2 (octant integrals)
    th1, ph1 = sp.symbols("t p", positive=True)
    sx, sy, szz = sp.sin(th1) * sp.cos(ph1), sp.sin(th1) * sp.sin(ph1), sp.cos(th1)
    oct_avg = lambda h: sp.simplify(8 * sp.integrate(sp.integrate(h * sp.sin(th1), (ph1, 0, sp.pi / 2)), (th1, 0, sp.pi / 2)) / (4 * sp.pi))
    l1 = sx + sy + szz
    ok = oct_avg(l1) == sp.Rational(3, 2) and oct_avg(l1 * sx ** 2) == sp.Rational(1, 2) and oct_avg(sx ** 2) == sp.Rational(1, 3)
    check("S3", ok, "capture in proportion to |s|_1: <|s|_1> = 3/2, <|s|_1 s_x^2> = 1/2, <s_x^2> = 1/3, so in a first-harmonic flow "
          "with momentum density g every captured record brings g/rho (the task's established statement, re-checked)")


def family_s4() -> None:
    """cubic viscosity: on transverse modes the viscous operator is c|k|^2 + d sum_n e_n^2 k_n^2 (c = axis shear viscosity, c + d/2 =
    the (1,1,0) shear viscosity). The axial Stokeslet component on a lattice axis is (1/(2 pi)^3)(pi/r) times the integral of
    Ghat_xx over the great circle n_x = 0 (the radial integral of e^{i k r n_x} is pi delta(r n_x) plus an odd part); on that circle x
    lies in the transverse plane of n and D is diagonal, so Ghat_xx = 1/c: the axial pull depends on c alone."""
    c, d, phi, r = sp.symbols("c d phi r", positive=True)
    n = sp.Matrix([0, sp.cos(phi), sp.sin(phi)])
    t = sp.Matrix([0, -sp.sin(phi), sp.cos(phi)])
    ex = sp.Matrix([1, 0, 0])
    D = c * sp.eye(3) + d * sp.diag(n[0] ** 2, n[1] ** 2, n[2] ** 2)
    ok = sp.simplify(n.dot(ex)) == 0 and sp.simplify(n.dot(t)) == 0 and sp.simplify(ex.dot(t)) == 0
    Nm = sp.Matrix([[ex.dot(D * ex), ex.dot(D * t)], [t.dot(D * ex), t.dot(D * t)]])
    ok &= sp.simplify(Nm[0, 1]) == 0 and sp.simplify(Nm[0, 0] - c) == 0
    Gxx = sp.simplify((Nm.inv())[0, 0])                      # x-component of the transverse inverse
    ok &= sp.simplify(Gxx - 1 / c) == 0
    val = sp.simplify(sp.pi / r / (2 * sp.pi) ** 3 * sp.integrate(Gxx, (phi, 0, 2 * sp.pi)))
    ok &= sp.simplify(val - 1 / (4 * sp.pi * c * r)) == 0
    # the transverse component does depend on d: t.D.t = c + (d/2) sin^2(2 phi)
    ok &= sp.simplify(Nm[1, 1] - (c + d * sp.sin(2 * phi) ** 2 / 2)) == 0
    check("S4", ok, "cubic viscosity (axis shear c, (1,1,0) shear c + d/2): the axial Stokeslet component on a lattice axis is exactly "
          "1/(4 pi c r) for every d (on the circle n_x = 0, x is transverse and D is diagonal, Ghat_xx = 1/c); block 49's on-axis pull "
          "needs only the axis shear viscosity")


# ------------------------------------------------------------------------------------------------ D: lattice Green function vs direct solve
class F:
    """a0 + a1 z + a2 z^2 + a3 z^3, z = e^{2 pi i/12}, z^4 = z^2 - 1."""
    __slots__ = ("c",)

    def __init__(self, c):
        self.c = tuple(Fr(v) for v in c)

    @staticmethod
    def of(q):
        return F((q, 0, 0, 0))

    def __add__(self, o):
        o = o if isinstance(o, F) else F.of(o)
        return F(a + b for a, b in zip(self.c, o.c))

    __radd__ = __add__

    def __sub__(self, o):
        o = o if isinstance(o, F) else F.of(o)
        return F(a - b for a, b in zip(self.c, o.c))

    def __mul__(self, o):
        if not isinstance(o, F):
            q = Fr(o)
            return F(a * q for a in self.c)
        p = [Fr(0)] * 7
        for i, a in enumerate(self.c):
            if a:
                for j, b in enumerate(o.c):
                    if b:
                        p[i + j] += a * b
        for n in range(6, 3, -1):
            a = p[n]
            if a:
                p[n] = Fr(0); p[n - 2] += a; p[n - 4] -= a
        return F(p[:4])

    __rmul__ = __mul__

    def __eq__(self, o):
        o = o if isinstance(o, F) else F.of(o)
        return self.c == o.c

    def conj(self):
        r = F.of(0)
        for j, a in enumerate(self.c):
            if a:
                r = r + ZP[(12 - j) % 12] * a
        return r

    def rational(self):
        return self.c[1] == self.c[2] == self.c[3] == 0


ZP = [F.of(1)]
for _m in range(11):
    ZP.append(ZP[-1] * F((0, 1, 0, 0)))


def fourier_green(L: int):
    """g_j(x), p(x) for the compensated force e_x (delta_{x,0} - 1/N), nu = 1, from ghat = (I - a a^H/|a|^2) e_x/|a|^2."""
    N = L ** 3
    e = 12 // L
    sites = [(i, j, l) for i in range(L) for j in range(L) for l in range(L)]
    g = [[F.of(0) for _ in range(N)] for _ in range(3)]
    p = [F.of(0) for _ in range(N)]
    for kv in sites:
        if kv == (0, 0, 0):
            continue
        a = [ZP[(e * kj) % 12] - 1 for kj in kv]
        a2 = sum((aj * aj.conj() for aj in a), F.of(0))
        assert a2.rational()
        inv = 1 / a2.c[0]
        gh = [((F.of(1) if j == 0 else F.of(0)) - a[j] * a[0].conj() * inv) * inv for j in range(3)]
        phat = a[0].conj() * inv
        for idx, xv in enumerate(sites):
            ph = ZP[(e * (kv[0] * xv[0] + kv[1] * xv[1] + kv[2] * xv[2])) % 12]
            for j in range(3):
                g[j][idx] = g[j][idx] + gh[j] * ph
            p[idx] = p[idx] + phat * ph
    g = [[v * Fr(1, N) for v in comp] for comp in g]
    p = [v * Fr(1, N) for v in p]
    return sites, g, p


def direct_solve(L: int):
    """The real-space steady equations lap g_j - grad+_j p + f_j = 0, div- g = 0 with sum g = 0, sum p = 0, solved by exact elimination."""
    N = L ** 3
    sites = [(i, j, l) for i in range(L) for j in range(L) for l in range(L)]
    ix = {s: n for n, s in enumerate(sites)}
    sh = lambda s, d, sgn: tuple((s[t] + (sgn if t == d else 0)) % L for t in range(3))
    var_g = lambda j, s: j * N + ix[s]
    var_p = lambda s: 3 * N + ix[s]
    rows = []
    for j in range(3):
        for s in sites[:-1]:
            row = {}
            for d in range(3):  # 7-point Laplacian of g_j
                for sgn in (1, -1):
                    v = var_g(j, sh(s, d, sgn)); row[v] = row.get(v, Fr(0)) + 1
            v = var_g(j, s); row[v] = row.get(v, Fr(0)) - 6
            v = var_p(sh(s, j, 1)); row[v] = row.get(v, Fr(0)) - 1   # - (p(x + e_j) - p(x))
            v = var_p(s); row[v] = row.get(v, Fr(0)) + 1
            fj = (Fr(1) if s == (0, 0, 0) else Fr(0)) - Fr(1, N) if j == 0 else Fr(0)
            rows.append((row, -fj))
        rows.append(({var_g(j, s): Fr(1) for s in sites}, Fr(0)))
    for s in sites[:-1]:
        row = {}
        for d in range(3):  # backward-difference divergence
            v = var_g(d, s); row[v] = row.get(v, Fr(0)) + 1
            v = var_g(d, sh(s, d, -1)); row[v] = row.get(v, Fr(0)) - 1
        rows.append((row, Fr(0)))
    rows.append(({var_p(s): Fr(1) for s in sites}, Fr(0)))
    # exact sparse elimination
    nvar = 4 * N
    rows = [({kk: vv for kk, vv in r.items() if vv}, b) for r, b in rows]
    pivots = {}
    for col in range(nvar):
        pr = None
        for idx, (r, b) in enumerate(rows):
            if col in r:
                if pr is None or len(r) < len(rows[pr][0]):
                    pr = idx
        assert pr is not None, "singular"
        prow, pb = rows.pop(pr)
        pv = prow[col]
        prow = {kk: vv / pv for kk, vv in prow.items()}; pb = pb / pv
        new = []
        for r, b in rows:
            if col in r:
                m = r[col]
                for kk, vv in prow.items():
                    nv = r.get(kk, Fr(0)) - m * vv
                    if nv:
                        r[kk] = nv
                    else:
                        r.pop(kk, None)
                b = b - m * pb
            new.append((r, b))
        rows = new
        pivots[col] = (prow, pb)
    sol = [Fr(0)] * nvar
    for col in range(nvar - 1, -1, -1):
        prow, pb = pivots[col]
        sol[col] = pb - sum((vv * sol[kk] for kk, vv in prow.items() if kk != col), Fr(0))
    g = [[sol[j * N + n] for n in range(N)] for j in range(3)]
    p = [sol[3 * N + n] for n in range(N)]
    return sites, g, p


def family_d() -> None:
    res = []
    ok = True
    for L in (3, 4):
        s1, gF, pF = fourier_green(L)
        s2, gD, pD = direct_solve(L)
        same = all(gF[j][n] == F.of(gD[j][n]) for j in range(3) for n in range(L ** 3)) and all(pF[n] == F.of(pD[n]) for n in range(L ** 3))
        ok &= same
        n1 = s2.index((1, 0, 0))
        res.append(f"L={L}: g_x(1,0,0) = {gD[0][n1]}")
    check("D1", ok, "periodic boxes L = 3, 4, force e_x at the origin (compensated): the direct exact solve of the real-space steady "
          "equations (forward-difference gradient, backward-difference divergence, 7-point Laplacian) equals the Fourier Green "
          "function (I - a a^H/|a|^2)/(nu |a|^2), a_j = e^{ik_j} - 1, at every site, component and in the pressure (" + "; ".join(res) + ")")


# ------------------------------------------------------------------------------------------------ N: numbers at block 49 (floating point)
def family_n() -> dict:
    rows, drows = [], []
    for fn in sorted(HERE.glob("shear_L*.txt")):
        t = fn.read_text()
        m1 = re.search(r"side (\d+), rho ([\d.]+), gamma ([\d.]+), mode (\d+) \(k = ([\d.]+)\)(?:, eps ([\d.]+))?", t)
        m2 = re.search(r"nu_T = ([\d.]+) \+- ([\d.]+)", t)
        if m1 and m2:
            row = (float(m1.group(5)), int(m1.group(1)), int(m1.group(4)), float(m1.group(6) or 0.3), float(m2.group(1)), float(m2.group(2)))
            (drows if ", diagonal" in t else rows).append(row)
    rows.sort(); drows.sort()
    bx = (HERE / "box_green.txt").read_text()
    box = float(re.search(r"walls at 1\.5, 93\.5 .*?\(([\d.]+) of free", bx).group(1))
    per = float(re.search(r"periodic side 96: G_xx = [\d.]+ \(([\d.]+) of free", bx).group(1))
    import math
    rho_, r_, C1, C2 = 0.3, 16.0, 7.24, 7.84
    K0v = math.sqrt(3) / (4 * math.pi * rho_ * (1 - rho_))
    ref = K0v * C1 * C2 / r_ ** 2
    nu_lo = min(v[4] for v in rows); nu_hi = max(v[4] for v in rows)
    nu_small_k = rows[0][4]
    push1 = 0.75                                        # executed push on the body in balance, fraction of ref (block 49)
    R = lambda nuv, f1: f1 * C2 / (4 * math.pi * nuv * rho_ * r_)
    # block 49's two seeds and the new seeds of the same control: pull on body 2 and push on body 1, as fractions of each run's reference
    runs = [(0.022, 0.012, 0.146, 0.095, 0.015, "b49-a"), (0.007, 0.018, 0.146, 0.123, 0.011, "b49-b")]
    c2s = [7.84]
    for fn in sorted(HERE.glob("balanced_bc_s*.txt")):
        t = fn.read_text()
        m = re.search(r"captures ([\d.]+), emits ([\d.]+).*?F1=([+-]?[\d.]+)\+-([\d.]+).*?captures ([\d.]+), emits ([\d.]+).*?"
                      r"F2=([+-]?[\d.]+)\+-([\d.]+).*?gross captures = ([\d.]+)", t)
        if m:
            runs.append((float(m.group(7)), float(m.group(8)), float(m.group(9)), float(m.group(3)), float(m.group(4)), fn.stem[-4:]))
            c2s.append(float(m.group(5)))
    def pool(vals):
        """run-to-run statistics: the mean over runs and its standard error from their scatter; and the chi-square of the runs about
        that mean with the within-run (ten-block) errors, which tests whether those errors describe the run-to-run scatter"""
        v = [a for a, _ in vals]
        m = sum(v) / len(v)
        sd = math.sqrt(sum((a - m) ** 2 for a in v) / (len(v) - 1))
        chi2 = sum(((a - m) / e) ** 2 for a, e in vals)
        return m, sd / math.sqrt(len(v)), chi2, len(v) - 1
    pull = pool([(a / ref_, e / ref_) for a, e, ref_, _, _, _ in runs])
    push = pool([(b / ref_, e / ref_) for _, _, ref_, b, e, _ in runs])
    newonly = [(a / ref_, e / ref_) for a, e, ref_, _, _, tag in runs if not tag.startswith("b49")]
    pull_new = pool(newonly) if len(newonly) > 1 else (float("nan"), float("nan"), float("nan"), 0)
    C2m = sum(c2s) / len(c2s)
    pred = push[0] * C2m * box / (4 * math.pi * nu_small_k * rho_ * r_)
    nu_err = max(abs(v[4] - nu_small_k) for v in rows[:2]) + rows[0][5]      # spread of the two smallest-k values plus the fit error
    pred_err = pred * math.sqrt((push[1] / push[0]) ** 2 + (nu_err / nu_small_k) ** 2 + 0.01 ** 2)
    out = {
        "runs": runs, "pull": pull, "push": push, "pull_new": pull_new, "pred": pred, "pred_err": pred_err, "C2m": C2m,
        "nu_rows": rows, "box": box, "per": per, "ref": ref, "nu_small_k": nu_small_k,
        "R_exec_free": R(nu_small_k, push1), "R_exec_box": R(nu_small_k, push1) * box,
        "R_first_box": R(nu_small_k, 1.0) * box, "R_range": (R(nu_hi, push1) * box, R(nu_lo, push1) * box),
    }
    tab = "; ".join(f"k={v[0]:.3f} (L={v[1]}, eps {v[3]}): {v[4]:.3f}+-{v[5]:.3f}" for v in rows)
    if drows:
        tab += "; k along (1,1,0), flow along (1,-1,0): " + "; ".join(f"k={v[0]:.3f} (L={v[1]}): {v[4]:.3f}+-{v[5]:.3f}" for v in drows)
    check("N1", abs(ref - 0.146) < 0.0015, f"[numerical] K0(0.3) = {K0v:.4f}; reference K0 C1 C2/r^2 with block 49's captures 7.24, 7.84 at "
          f"r = 16: {ref:.4f} (block 49: 0.146)")
    OUT.append(f"     [executed, block 44's simulator] nu_T from shear-wave decay at rho 0.3, gamma 1: {tab}")
    OUT.append(f"     [numerical] Stokeslet factor at body 2: block 49's walls {box:.3f}, periodic side 96 {per:.3f} (box_green.txt)")
    OUT.append("     [executed, block 49's control] runs (pull on body 2 / ref, push on body 1 / ref): " + "; ".join(
        f"{tag}: {a / ref_:+.3f}+-{e / ref_:.3f}, {b / ref_:.3f}+-{eb / ref_:.3f}" for a, e, ref_, b, eb, tag in runs))
    OUT.append(f"     [executed] {len(runs)} runs, mean +- run-to-run standard error: pull {pull[0]:.3f} +- {pull[1]:.3f} (new seeds alone "
               f"{pull_new[0]:.3f} +- {pull_new[1]:.3f}); push on the body in balance {push[0]:.3f} +- {push[1]:.3f}. Within-run block "
               f"errors: chi2 = {pull[2]:.1f} (pull), {push[2]:.1f} (push) for {pull[3]} dof - they understate the pull's run-to-run "
               f"scatter {math.sqrt(pull[2] / pull[3]):.1f}x")
    return out


def main() -> int:
    family_q()
    family_h()
    family_s()
    family_s4()
    family_d()
    n = family_n()
    print("Next-order force between capturing bodies - checks; worker w-macbookpro90c72-j5f35 (claude-opus-5-5)")
    for line in OUT:
        print(line)
    import math
    P, sP = n["pull"][:2]; pr, spr = n["pred"], n["pred_err"]
    z = (pr - P) / math.hypot(sP, spr)
    print(f"     [prediction] pull of the body in balance on body 2 / ref: {pr:.3f} +- {spr:.3f} (Stokeslet at nu_T = {n['nu_small_k']:.3f}, "
          f"walls {n['box']:.3f}, pooled push {n['push'][0]:.3f}, C2 = {n['C2m']:.2f}; free space {pr / n['box']:.3f}; with the "
          f"first-order push {n['R_first_box']:.3f}); executed, {len(n['runs'])} runs pooled: {P:.3f} +- {sP:.3f}; difference {z:+.1f} sigma")
    print(f"checks: {NCHECK[0] - len(FAILS)} ok, {len(FAILS)} fail{': ' + ', '.join(FAILS) if FAILS else ''}")
    if FAILS:
        print(f"SUMMARY: ROUTE FAILS AT {FAILS[0]}")
        return 1
    resolved = abs(P) > 2 * sP
    tail = "" if resolved else ", a pull the executed runs do not resolve from zero"
    if abs(z) <= 2:
        verdict = f"consistent within {abs(z):.1f} sigma{tail}"
        short = f"consistent with the executed {P:.2f} +- {sP:.2f} ({abs(z):.1f} sigma){tail}"
    elif z > 2:
        verdict = f"the Stokeslet value lies {z:.1f} sigma above it{tail}; the executed runs favour a smaller pull"
        short = f"{z:.1f} sigma above the executed {P:.2f} +- {sP:.2f}{tail}"
    else:
        verdict = f"the executed pull lies {-z:.1f} sigma above the Stokeslet value"
        short = f"{-z:.1f} sigma below the executed {P:.2f} +- {sP:.2f}"
    under = math.sqrt(n["pull"][2] / n["pull"][3])
    print("SUMMARY: PROVED within the linearized hydrodynamics (block 44's J = (1 - rho) g/sqrt3, pressure rho/(3 sqrt3), viscosity nu) "
          "and block 48's sampling closure: a momentum sink F1 leaves the Stokeslet g = -(I + rr) F1/(8 pi nu r) (div g = 0 exactly), "
          "so a capturing body 2 is pulled towards body 1 by C2 F1/(4 pi nu rho r) on the axis = K0 C1 C2 N2/(4 pi nu rho r^3): "
          "attractive, r^-3, 1/nu, pair forces unequal by K0 Q1 Q2 (Q2 - Q1)/(4 pi nu rho r^3); on a lattice axis only the axis shear "
          "viscosity enters (exact for any cubic viscosity); lattice Green function = exact direct solve (L = 3, 4). At block 49's "
          f"parameters: nu_T = {n['nu_small_k']:.2f} (block 44's simulator; 0.41 for the (1,1,0) shear), reservoir-wall factor "
          f"{n['box']:.2f}, predicted pull {pr:.2f} +- {spr:.2f} of the reference; executed over {len(n['runs'])} runs of block 49's "
          f"control {P:.2f} +- {sP:.2f} (run-to-run; its block errors understate that scatter {under:.1f}x): {verdict}.")
    print(f"HIT: the force of second order in the capture rates is the Stokeslet pull K0 C1 C2 N2/(4 pi nu rho r^3) (attractive, r^-3, "
          f"unequal pair forces; on a lattice axis nu = the axis shear viscosity); at block 49's parameters (measured nu_T = "
          f"{n['nu_small_k']:.2f}, reservoir walls) it is {pr:.2f} of the reference, {short}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
