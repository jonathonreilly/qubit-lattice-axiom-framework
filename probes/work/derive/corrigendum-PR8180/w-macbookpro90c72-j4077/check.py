#!/usr/bin/env python3
"""Corrigendum packet for PR #8180 (block 35), independent attempt 1 of 2: exact checks for ATTEMPT.md.

Worker w-macbookpro90c72-j4077 (claude-opus-5-5).  Every finite claim is checked with exact arithmetic:
Fractions; the cyclotomic field Q(z), z = e^{2 pi i/12}, z^4 = z^2 - 1 (class F below: it contains i = z^3 and
e^{2 pi i/3} = z^4, so every character of the tori L = 3, 4, 6); and sympy for identities between Laurent
polynomials in X_a = e^{iK_a}.  No floating point anywhere.

Conventions (ATTEMPT.md section 1): (P v)_(i,j) = (v_(i,j) + v_(i-1,j) + v_(i,j-1))/3; e_k(x) = e^{ik.x};
phi(k) = (1 + e^{ik1} + e^{ik2})/3; u = |phi|^2; block 34's transform th^_k = L^-1 sum_x e^{-ik.x} th_x ("minus");
the "+ik" transform th+_k = L^-1 sum_x e^{+ik.x} th_x; the pairing Cov(X, Y) = E[(X - EX) conj(Y - EY)].
For a real matrix M, qf(M, k) := e_k^H M e_k = sum_{x,y} M[x][y] e^{ik.(y - x)}; with the minus transform
Cov(th^_k(t), th^_k(t+s)) = L^-2 qf(Sigma_{t,t+s}, k), and with the +ik transform it is L^-2 qf(Sigma_{t,t+s}, -k).
"""
from __future__ import annotations

import subprocess
import sys
from fractions import Fraction as Fr

import sympy as sp

OUT: list[str] = []
FAILS: list[str] = []


def check(tag: str, ok: bool, msg: str) -> None:
    OUT.append(f"{'ok  ' if ok else 'FAIL'} {tag}: {msg}")
    if not ok:
        FAILS.append(tag)


# ------------------------------------------------------------------------------------------------ the field Q(z)
class F:
    """a0 + a1 z + a2 z^2 + a3 z^3, z = e^{2 pi i/12}, reduced with z^4 = z^2 - 1 (Phi_12(z) = 0)."""

    __slots__ = ("c",)

    def __init__(self, c):
        self.c = tuple(Fr(x) for x in c)

    @staticmethod
    def of(q) -> "F":
        return F((q, 0, 0, 0))

    def __add__(self, o):
        o = o if isinstance(o, F) else F.of(o)
        return F(a + b for a, b in zip(self.c, o.c))

    __radd__ = __add__

    def __neg__(self):
        return F(-a for a in self.c)

    def __sub__(self, o):
        o = o if isinstance(o, F) else F.of(o)
        return self + (-o)

    def __rsub__(self, o):
        return F.of(o) - self

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
        for n in range(6, 3, -1):  # z^n = z^(n-2) - z^(n-4)
            a = p[n]
            if a:
                p[n] = Fr(0)
                p[n - 2] += a
                p[n - 4] -= a
        return F(p[:4])

    __rmul__ = __mul__

    def __pow__(self, n: int):
        r = F.of(1)
        for _ in range(n):
            r = r * self
        return r

    def __eq__(self, o):
        o = o if isinstance(o, F) else F.of(o)
        return self.c == o.c

    def __hash__(self):
        return hash(self.c)

    def conj(self) -> "F":
        r = F.of(0)
        for j, a in enumerate(self.c):
            if a:
                r = r + ZP[(12 - j) % 12] * a
        return r

    def real(self) -> bool:
        return self == self.conj()

    def im(self) -> "F":
        return (self.conj() - self) * ZP[3] * Fr(1, 2)  # (x - conj x)/(2i)


ZP = [F.of(1)]
for _m in range(11):
    ZP.append(ZP[-1] * F((0, 1, 0, 0)))
I_ = ZP[3]


def char(L: int, n1: int, n2: int, i: int, j: int, sign: int = 1) -> F:
    return ZP[(sign * (12 // L) * (n1 * i + n2 * j)) % 12]


def phi_of(L: int, n1: int, n2: int) -> F:
    return (F.of(1) + ZP[((12 // L) * n1) % 12] + ZP[((12 // L) * n2) % 12]) * Fr(1, 3)


# ------------------------------------------------------------------------------------------------ source quotes
PIN = {
    "b35": ("7c844adf7555a3558729be69179646f6a83a1539",
            "physics-loop/admissibility-induced-law-block35-gravity-kernel-under-the-formation-reading-heat-kernel-times-plane-green-function-20260918"),
    "b34": ("e6ffae5b460b9ec0fd0d99c99f9784232bd225bd",
            "physics-loop/admissibility-induced-law-block34-sphere-formation-law-torus-memory-time-zero-mode-rate-and-stationary-modes-20260917"),
    "b13": ("9c364d1d6f7527e89fc47bffbe672440c5fa50bb",
            "physics-loop/admissibility-induced-law-block13-causal-gaussian-two-point-heat-kernel-20260915"),
    "b26": ("f9e1177003afa991ec87831d2be70611068a09ab",
            "physics-loop/admissibility-induced-law-block26-unsoldered-formation-law-level-time-gain-one-spin-waves-memory-decay-20260916"),
}
N35 = ("docs/ADMISSIBILITY_RULE_GRAVITY_NODE_KERNEL_UNDER_THE_FORMATION_READING_A_HEAT_KERNEL_IN_LEVEL_TIME_TIMES_A_PLANE_"
       "GREEN_FUNCTION_NOT_THE_COMPARATORS_THREE_DIMENSIONAL_GREEN_FUNCTION_BOUNDED_THEOREM_NOTE_2026-09-18.md")
R35 = ("scripts/admissibility_rule_gravity_node_kernel_under_the_formation_reading_heat_kernel_in_level_time_times_plane_"
       "green_function_2026_09_18.py")
C35 = ".claude/science/physics-loops/admissibility-induced-law-20260906/specs/supervisor_control_block35_kernel_sim.py"
N34 = ("docs/ADMISSIBILITY_RULE_UNSOLDERED_FORMATION_LAW_TORUS_MEMORY_TIME_ZERO_MODE_RATE_EXACTLY_STATIONARY_MODES_"
       "BRACKETED_AND_THE_NONLINEAR_LAW_MEASURED_AGAINST_IT_BOUNDED_THEOREM_NOTE_2026-09-17.md")
N13 = ("docs/ADMISSIBILITY_RULE_CAUSAL_GAUSSIAN_FORMATION_LAW_RECORD_TWO_POINT_FUNCTION_HEAT_KERNEL_NOT_LATTICE_GREEN_"
       "FUNCTION_BOUNDED_THEOREM_NOTE_2026-09-15.md")
N26 = ("docs/ADMISSIBILITY_RULE_UNSOLDERED_FORMATION_LAW_IN_LEVEL_TIME_GAIN_ONE_SPIN_WAVES_LOCAL_LIMIT_CONSTANT_FINITE_"
       "PLANES_FORGET_AND_THE_SIMULATED_ALGEBRAIC_DECAY_OF_THE_INITIAL_PLANE_MEMORY_BOUNDED_THEOREM_NOTE_2026-09-16.md")
QUOTES = [  # (pin, path, 1-based line, verbatim substring)
    ("b35", N35, 85, "the predecessors of `(i, j)` are `(i, j)`, `(i − 1, j)`, `(i, j − 1)`"),
    ("b35", N35, 86, "modes `θ̂_k`, multiplier `φ(k) = (1 + e^{ik₁} + e^{ik₂})/3`"),
    ("b35", N35, 87, "as an operator `C_s = Σ_x Cov(θ_{x,t}, θ_{x',t+s})`"),
    ("b35", N35, 88, "`C_s(k) = E[ŝ_⊥(k, t) ŝ_⊥(k, t+s)*]`"),
    ("b35", N35, 104, "`C_s(k) = σ² φ(k)^s/(1 − |φ(k)|²)`, i.e. `C_s = σ²(I − PP*)^{−1} P*^s`"),
    ("b35", N35, 106, "`θ̂_k(t+s) = φ^s θ̂_k(t) + (noise of levels t+1..t+s)`"),
    ("b35", N35, 106, "for every cosine character of a nonzero mode, `Cov/Var = Re φ(k)^s`"),
    ("b35", N35, 116, "The comparator's `1/E(k)` is not of the form `f(k₁, k₂) g(k₃)` in any direction"),
    ("b35", N35, 116, "The formation kernel is exactly of that form."),
    ("b35", R35, 13, "phi(k) = 1 - i(k1 + k2)/3 + O(k^2)"),
    ("b35", R35, 138, 'ph, u, s2 = sp.symbols("phi u sigma2", positive=True)'),
    ("b35", R35, 236, "(1 + sp.I * eps * (k1 + k2) / 3)"),
    ("b35", C35, 17, "S = s + np.roll(s, 1, axis=0) + np.roll(s, 1, axis=1)"),
    ("b35", C35, 27, "np.fft.fft2(s[..., 0])"),
    ("b35", C35, 37, "past[0] * np.conj(cur[0])"),
    ("b34", N34, 85, "`θ̂_k = L^{−1} Σ_x e^{−ik·x} θ_x`; `P` acts as multiplication by `φ(k) = (1 + e^{ik₁} + e^{ik₂})/3`"),
    ("b34", N34, 104, "`(Pθ)^_k = φ(k) θ̂_k`"),
    ("b34", N34, 108, "`θ̂_k(t+1) = φ(k) θ̂_k(t) + ξ̂_k(t)`"),
    ("b13", N13, 226, "`|k|⁴/36 + O(|k|⁶)`: parabolic"),
    ("b26", N26, 86, "`φ(θ) = (1 + e^{−iθ_1} + e^{−iθ_2})/3`"),
]


def git_show(pin: str, path: str) -> str | None:
    sha, branch = PIN[pin]
    r = subprocess.run(["git", "show", f"{sha}:{path}"], capture_output=True, text=True)
    if r.returncode != 0:
        subprocess.run(["git", "fetch", "-q", "origin", branch], capture_output=True, text=True)
        r = subprocess.run(["git", "show", f"{sha}:{path}"], capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None


def family_q() -> None:
    cache: dict = {}
    found = 0
    missing = []
    for pin, path, ln, needle in QUOTES:
        key = (pin, path)
        if key not in cache:
            cache[key] = git_show(pin, path)
        txt = cache[key]
        lines = txt.splitlines() if txt else []
        if len(lines) >= ln and needle in lines[ln - 1]:
            found += 1
        else:
            missing.append(f"{pin}:L{ln}")
    check("Q", not missing, f"{found}/{len(QUOTES)} quoted source lines verbatim at the pinned heads "
          f"(b35 7c844adf, b34 e6ffae5b, b13 9c364d1d, b26 f9e11770){'; missing ' + ','.join(missing) if missing else ''}")


# ------------------------------------------------------------------------------------------------ tori
def P_apply(L: int, v: list) -> list:
    return [(v[i * L + j] + v[((i - 1) % L) * L + j] + v[i * L + (j - 1) % L]) * Fr(1, 3) for i in range(L) for j in range(L)]


def PT_apply(L: int, v: list) -> list:
    return [(v[i * L + j] + v[((i + 1) % L) * L + j] + v[i * L + (j + 1) % L]) * Fr(1, 3) for i in range(L) for j in range(L)]


def sigma_sequence(L: int, T: int, smax: int):
    """the runner's recursion Sigma_{t+1} = P Sigma_t P^T + I (sigma^2 = 1) from Sigma_0 = 0; Sigma_{t,t+s} = Sigma_t (P^T)^s."""
    N = L * L
    S = [[Fr(0)] * N for _ in range(N)]
    out = []
    for t in range(1, T + 1):
        PS = [P_apply(L, [S[x][y] for x in range(N)]) for y in range(N)]  # columns of P S
        PS = [[PS[y][x] for y in range(N)] for x in range(N)]
        S = [P_apply(L, PS[x]) for x in range(N)]  # rows: (P S P^T)[x] = P applied to row x of P S
        S = [[S[x][y] + (1 if x == y else 0) for y in range(N)] for x in range(N)]
        cross = {}
        M = S
        for s in range(1, smax + 1):
            M = [P_apply(L, M[x]) for x in range(N)]  # (M P^T)[x][y] = (M[x][y] + M[x][y-e1] + M[x][y-e2])/3
            cross[s] = M
        out.append((S, cross))
    return out


def qf(L: int, M, n1: int, n2: int) -> F:
    acc = [Fr(0)] * 12
    for x in range(L * L):
        xi, xj = divmod(x, L)
        row = M[x]
        for y in range(L * L):
            if row[y]:
                yi, yj = divmod(y, L)
                acc[((12 // L) * (n1 * (yi - xi) + n2 * (yj - xj))) % 12] += row[y]
    r = F.of(0)
    for m, a in enumerate(acc):
        if a:
            r = r + ZP[m] * a
    return r


def hat(L: int, v: list, n1: int, n2: int, sign: int) -> F:
    acc = [Fr(0)] * 12
    for x in range(L * L):
        if v[x]:
            i, j = divmod(x, L)
            acc[(sign * (12 // L) * (n1 * i + n2 * j)) % 12] += v[x]
    r = F.of(0)
    for m, a in enumerate(acc):
        if a:
            r = r + ZP[m] * a
    return r


TORI = {3: 5, 4: 4, 6: 3}  # L -> number of levels t iterated exactly
SMAX = 3


def family_t1() -> dict:
    stats = {}
    ok_a = ok_b = ok_c = ok_d = ok_z = True
    for L, T in TORI.items():
        N = L * L
        modes = [(a, b) for a in range(L) for b in range(L) if (a, b) != (0, 0)]
        # T1a: P e_k = conj(phi) e_k and P^T e_k = phi e_k; the stated multiplier holds iff phi is real
        real_modes = 0
        for (a, b) in [(0, 0)] + modes:
            ph = phi_of(L, a, b)
            e = [char(L, a, b, i, j) for i in range(L) for j in range(L)]
            ok_a &= P_apply(L, e) == [ph.conj() * v for v in e] and PT_apply(L, e) == [ph * v for v in e]
            real_modes += (a, b) != (0, 0) and ph.real()
            # phi real  <=>  sin k1 + sin k2 = 0  <=>  k1 + k2 in 2 pi Z  or  k1 - k2 in pi + 2 pi Z
            ok_a &= ph.real() == ((a + b) % L == 0 or (L % 2 == 0 and (a - b) % L == L // 2))
        # a generic rational field: block 34's transform gives (P th)^_k = conj(phi) th^_k on every mode
        th = [Fr(((3 * i + 5 * j * j + 7 * i * j + 1) % 13) - 6) for i in range(L) for j in range(L)]
        Pth = P_apply(L, th)
        stated_fail = 0
        for (a, b) in [(0, 0)] + modes:
            ph, h = phi_of(L, a, b), hat(L, th, a, b, -1)
            ok_a &= h != F.of(0) and hat(L, Pth, a, b, -1) == ph.conj() * h
            stated_fail += hat(L, Pth, a, b, -1) != ph * h
        ok_a &= stated_fail == len(modes) - real_modes
        # T1b-T1d on the runner's own recursion
        seq = sigma_sequence(L, T, SMAX)
        real_pairs = 0
        ok_t = True
        for t, (S, cross) in enumerate(seq, 1):
            for s in range(1, SMAX + 1):  # zero mode: Cov of the plane sums = t L^2, i.e. t/L^2 for the average
                ok_z &= qf(L, cross[s], 0, 0) == F.of(t * N)
            for (a, b) in modes:
                ph = phi_of(L, a, b)
                u = ph * ph.conj()
                W = qf(L, S, a, b)
                ok_b &= W.real() and W * (1 - u) == (1 - u ** t) * N  # Var th^_k(t) = (1 - u^t)/(1 - u)
                for s in range(1, SMAX + 1):
                    X = qf(L, cross[s], a, b)       # minus transform, pairing E[X conj Y]: the display
                    Xp = qf(L, cross[s], -a, -b)    # +ik transform, same pairing; also E[th^(t+s) conj th^(t)] (minus)
                    ok_b &= X == ph ** s * W and Xp == ph.conj() ** s * W
                    ok_d &= (X == Xp) == (ph ** s).real()
                    # E[th^_k(t+s) conj th^_k(t)] (block 34's transform) = L^-2 e_k^H Sigma_{t,t+s}^T e_k
                    MT = [[cross[s][y][x] for y in range(N)] for x in range(N)]
                    Y = qf(L, MT, a, b)
                    ok_t &= Y == ph.conj() ** s * W and (Y == ph ** s * W) == (ph ** s).real()
                    if t == 1:
                        real_pairs += (ph ** s).real()
        # T1c: the gloss on a generic field: Sigma_{t,t+s} acts on the minus-mode k by phi^s (1-u^t)/(1-u), on the +ik mode by the conjugate
        S, cross = seq[-1]
        for s in range(1, SMAX + 1):
            v = [sum((cross[s][x][y] * th[y] for y in range(N)), Fr(0)) for x in range(N)]
            for (a, b) in [(0, 0)] + modes:
                ph = phi_of(L, a, b)
                u = ph * ph.conj()
                if (a, b) == (0, 0):
                    ok_c &= hat(L, v, 0, 0, -1) == hat(L, th, 0, 0, -1) * T
                    continue
                ok_c &= hat(L, v, a, b, -1) * (1 - u) == ph ** s * (1 - u ** T) * hat(L, th, a, b, -1)
                ok_c &= hat(L, v, a, b, 1) * (1 - u) == ph.conj() ** s * (1 - u ** T) * hat(L, th, a, b, 1)
        ok_d &= ok_t
        stats[L] = (len(modes), real_modes, stated_fail, 3 * len(modes), real_pairs, ok_t)
    s3, s4, s6 = stats[3], stats[4], stats[6]
    check("T1a", ok_a, "P e_k = conj(phi) e_k, P^T e_k = phi e_k on every mode of L = 3, 4, 6; with block 34's transform "
          f"(P th)^_k = conj(phi) th^_k for a generic rational field; the stated phi th^_k fails on {s3[2]}/{s3[0]+1}, "
          f"{s4[2]}/{s4[0]+1}, {s6[2]}/{s6[0]+1} modes, exactly those with phi not real, i.e. off k1 + k2 = 0 and k1 - k2 = pi")
    check("T1b", ok_b and ok_z, f"runner recursion (t <= {TORI[3]}, {TORI[4]}, {TORI[6]} on L = 3, 4, 6; s <= 3): minus transform + "
          "E[X conj Y] gives Cov(th^_k(t), th^_k(t+s)) = phi^s Var, Var = (1 - u^t)/(1 - u) (the display, verbatim); "
          "+ik transform, same pairing: conj(phi)^s Var; zero mode t/L^2")
    check("T1c", ok_c, "gloss: Sigma_{t,t+s} = Sigma_t (P^T)^s multiplies the minus-mode k by phi^s (1 - u^t)/(1 - u) and the "
          "+ik mode by conj(phi)^s (1 - u^t)/(1 - u) (generic rational field, all modes, s <= 3)")
    check("T1d", all(stats[L][5] for L in stats), "L106's first line: E[th^_k(t+s) conj th^_k(t)] / Var = conj(phi)^s (block "
          "34's transform, from Sigma_{t,t+s}^T), equal to the stated phi^s only where phi^s is real; with it, Cov = E[X conj Y] "
          "gives the display phi^s Var: the line's two slips cancel")
    check("T1f", ok_d, "in note L86's labelling (+ik: P acts by phi) the display phi^s and the gloss conj(phi)^s agree exactly on "
          f"the pairs with phi(k)^s real: {s3[4]}/{s3[3]} (L=3), {s4[4]}/{s4[3]} (L=4), {s6[4]}/{s6[3]} (L=6), k != 0, s = 1..3")
    return stats


def family_t1e() -> None:
    """B2 is blind; the sine-cosine cross covariance detects the conjugation (L = 4: characters are rational)."""
    L, T = 4, 4
    N = L * L
    S, cross = sigma_sequence(L, T, SMAX)[-1]
    ok = True
    detected = 0
    nonreal = 0
    re_of = {0: 1, 1: 0, 2: -1, 3: 0}
    im_of = {0: 0, 1: 1, 2: 0, 3: -1}
    for a in range(L):
        for b in range(L):
            if (a, b) == (0, 0):
                continue
            c = [Fr(re_of[(a * i + b * j) % 4]) for i in range(L) for j in range(L)]
            sn = [Fr(im_of[(a * i + b * j) % 4]) for i in range(L) for j in range(L)]
            bil = lambda p, M, q: sum((p[x] * M[x][y] * q[y] for x in range(N) for y in range(N) if p[x] and q[y]), Fr(0))
            W = bil(c, S, c) + bil(sn, S, sn)
            ph = phi_of(L, a, b)
            for s in range(1, SMAX + 1):
                M = cross[s]
                ps = ph ** s
                re_ps, im_ps = (ps + ps.conj()) * Fr(1, 2), ps.im()
                # runner B2: c^T S c / c^T Sigma c = Re phi^s = Re conj(phi)^s  (blind to the conjugation)
                ok &= F.of(bil(c, M, c)) == re_ps * bil(c, S, c)
                # the detector: c^T S s - s^T S c = Im(phi^s) W; the conjugate reading would give -Im(phi^s) W
                cross_term = bil(c, M, sn) - bil(sn, M, c)
                ok &= F.of(cross_term) == im_ps * W
                if not ps.real():
                    nonreal += 1
                    detected += cross_term != 0
    check("T1e", ok and detected == nonreal, "L = 4 real characters: B2's c^T S c / c^T Sigma c = Re phi^s holds and is the same "
          "for conj(phi) (blind); Cov(c.th_t, s.th_{t+s}) - Cov(s.th_t, c.th_{t+s}) = Im(phi^s) W exactly, nonzero on all "
          f"{nonreal} pairs with phi^s not real, sign flipped under the conjugate reading")


# ------------------------------------------------------------------------------------------------ T3 / D2
X1, X2, X3, Y1, Y2, W_ = sp.symbols("X1 X2 X3 Y1 Y2 W", nonzero=True)
E_lat = sum(2 - X - 1 / X for X in (X1, X2, X3))
z_lat = (X1 + X2 + X3) / 3
zc_lat = (1 / X1 + 1 / X2 + 1 / X3) / 3
D_lat = (1 - z_lat) * (1 - zc_lat)  # |1 - z|^2: sigma^2 / (the formation law's spectral density)
phi_k = (1 + X1 / X3 + X2 / X3) / 3  # phi at k = (K1 - K3, K2 - K3)
phic_k = (1 + X3 / X1 + X3 / X2) / 3


def zero(expr) -> bool:
    return sp.expand(expr) == 0 or sp.simplify(sp.together(expr)) == 0


def to_F(expr, exps: dict) -> F:
    tot = F.of(0)
    for term in sp.Add.make_args(sp.expand(expr)):
        c, rest = term.as_coeff_Mul()
        m = 0
        if rest != 1:
            for base, e in rest.as_powers_dict().items():
                m += exps[base] * int(e)
        tot = tot + ZP[m % 12] * Fr(int(sp.Rational(c).p), int(sp.Rational(c).q))
    return tot


def family_t3() -> None:
    # T3a: the exact identity and the zero set
    ok = zero(3 * D_lat - E_lat + 3 * (1 - phi_k * phic_k))
    ok &= zero(phi_k * phic_k - z_lat * zc_lat)  # u(K1 - K3, K2 - K3) = |z|^2
    ok &= zero(1 - z_lat * zc_lat - sp.Rational(2, 9) * sum(1 - (A / B + B / A) / 2 for A, B in ((X1, X2), (X1, X3), (X2, X3))))
    check("T3a", ok, "3|1 - z|^2 = E(K) - 3(1 - u(K1 - K3, K2 - K3)), z = (1/3) sum_a e^{iK_a}, u(K1-K3, K2-K3) = |z|^2, and "
          "1 - |z|^2 = (2/9) sum_{a<b} (1 - cos(K_a - K_b)) (identities in X_a = e^{iK_a}; the zero sets follow, S9)")
    # T3b: level coordinates X1 = Y1 W, X2 = Y2 W, X3 = W: both depend on w only through Re(phi e^{iw})
    lev = {X1: Y1 * W_, X2: Y2 * W_, X3: W_}
    ph, phc = (1 + Y1 + Y2) / 3, (1 + 1 / Y1 + 1 / Y2) / 3
    ReZ = (ph * W_ + phc / W_) / 2
    ok = zero(E_lat.subs(lev) - (6 - 6 * ReZ)) and zero(D_lat.subs(lev) - (1 - 2 * ReZ + ph * phc))
    check("T3b", ok, "level coordinates K = (k1 + w, k2 + w, w): E = 6 - 6 Re(phi(k) e^{iw}) and |1 - z|^2 = 1 - 2 Re(phi e^{iw}) "
          "+ |phi|^2: any phase along levels is common to both kernels")
    # T3c: the runner's D2 statistic f f_ab - f_a f_b (up to the sign from d/dK = i X d/dX) in two frames, exact points
    def stat(f, A, B):
        DA = lambda g: sp.expand(A * sp.diff(g, A))
        DB = lambda g: sp.expand(B * sp.diff(g, B))
        return sp.expand(f * DA(DB(f)) - DA(f) * DB(f))
    pt_lat = {X1: 3, X2: 2, X3: 1}          # K = (pi/2, pi/3, pi/6)
    pt_lev = {Y1: 2, Y2: 1, W_: 3}          # (k1, k2, w) = (pi/3, pi/6, pi/2)
    E_lev, D_lev = sp.expand(E_lat.subs(lev)), sp.expand(D_lat.subs(lev))
    vals = [to_F(stat(E_lat, X1, X3), pt_lat), to_F(stat(sp.expand(D_lat), X1, X3), pt_lat),
            to_F(stat(E_lev, Y1, W_), pt_lev), to_F(stat(D_lev, Y1, W_), pt_lev)]
    ok = all(v != F.of(0) and v.real() for v in vals)
    check("T3c", ok, "D2's mixed-derivative statistic is nonzero for E and for |1 - z|^2, in the lattice frame (K1, K3) at "
          "(pi/2, pi/3, pi/6) and the level frame (k1, w) at (pi/3, pi/6, pi/2): the test calls both kernels non-products")
    # T3d, T3e: Hessians at 0 and the parabolic leading part (trigonometric form of T3a)
    eps, b = sp.symbols("epsilon b", real=True)
    v = sp.symbols("v1 v2 v3", real=True)
    a1, a2 = sp.symbols("a1 a2", real=True)

    def E_tr(K):
        return sum(2 * (1 - sp.cos(k)) for k in K)

    def D3_tr(K):  # 3|1 - z|^2 via T3a with u in block 34's cosine form
        k1, k2 = K[0] - K[2], K[1] - K[2]
        return E_tr(K) - 3 * (1 - (3 + 2 * sp.cos(k1) + 2 * sp.cos(k2) + 2 * sp.cos(k1 - k2)) / 9)

    Kv = [eps * vi for vi in v]
    q_E = sp.series(E_tr(Kv), eps, 0, 3).removeO().coeff(eps, 2)
    q_D = sp.series(D3_tr(Kv), eps, 0, 3).removeO().coeff(eps, 2)
    HE, HD = sp.hessian(q_E, v), sp.hessian(q_D, v)
    ok = HE == 2 * sp.eye(3) and HD == sp.Rational(2, 3) * sp.ones(3, 3) and HE.rank() == 3 and HD.rank() == 1
    check("T3d", ok, "Hessians at K = 0: E -> 2I (rank 3, no distinguished direction); 3|1 - z|^2 -> (2/3)(1,1,1)^T(1,1,1) "
          "(rank 1, range spanned by the causal-cone axis (1,1,1))")
    a3 = -a1 - a2
    Kp = [eps * a1 + eps ** 2 * b, eps * a2 + eps ** 2 * b, eps * a3 + eps ** 2 * b]
    ser = sp.expand(sp.series(D3_tr(Kp), eps, 0, 5).removeO())
    serE = sp.expand(sp.series(E_tr(Kp), eps, 0, 3).removeO())
    na = a1 ** 2 + a2 ** 2 + a3 ** 2
    ok = all(sp.simplify(ser.coeff(eps, n)) == 0 for n in range(4))
    ok &= sp.simplify(ser.coeff(eps, 4) - (3 * b ** 2 + na ** 2 / 12)) == 0
    ok &= sp.simplify(serE.coeff(eps, 2) - na) == 0
    check("T3e", ok, "K = eps a + eps^2 b(1,1,1), a.(1,1,1) = 0: 3|1 - z|^2 = eps^4 (3b^2 + |a|^4/12) + O(eps^5) (parabolic; "
          "block 13's K^2/9 and |k|^4/36 for |1 - z|^2) while E = eps^2 |a|^2 + O(eps^3) (elliptic)")
    # T3f: (k, tau) at two L = 4 modes with rational y = sqrt(1 - u) = 2/3
    ok = True
    for (n1, n2) in ((1, 0), (1, 1)):
        ph_ = phi_of(4, n1, n2)
        u = ph_ * ph_.conj()
        y = Fr(2, 3)
        ok &= u == F.of(1 - y * y)
        zz = ph_.conj() * Fr(1, 1) * (1 / (1 + y))
        A = 1 / (6 * y)
        G = lambda tau: (zz ** tau if tau >= 0 else zz.conj() ** (-tau)) * A
        for tau in range(-4, 5):
            lhs = G(tau) * 6 - ph_ * 3 * G(tau + 1) - ph_.conj() * 3 * G(tau - 1)
            ok &= lhs == F.of(1 if tau == 0 else 0)
        ok &= zz * zz.conj() == F.of((1 - y) / (1 + y))
        for tau in range(0, 5):  # both propagators = positive rational x conj(phi)^tau
            ratio_G = G(tau) * (1 + y) ** tau
            ok &= ratio_G == ph_.conj() ** tau * A
    check("T3f", ok, "(k, tau), L = 4, k = 2pi(1,0)/4 and 2pi(1,1)/4 (u = 5/9, y = 2/3): the comparator's level recurrence "
          "6G(tau) - 3 phi G(tau+1) - 3 conj(phi) G(tau-1) = delta is solved by G = conj(phi)^tau (1+y)^-tau/(6y) (|z|^2 = 1/5), "
          "with T1b's formation coefficient conj(phi)^tau (1-u^t)/(1-u): the same phase")


def main() -> int:
    family_q()
    stats = family_t1()
    family_t1e()
    family_t3()
    print("Corrigendum PR #8180 (block 35) — exact checks; worker w-macbookpro90c72-j4077 (claude-opus-5-5)")
    for line in OUT:
        print(line)
    s3, s4, s6 = stats[3], stats[4], stats[6]
    print(f"checks: {len(OUT) - len(FAILS)} ok, {len(FAILS)} fail{': ' + ', '.join(FAILS) if FAILS else ''}")
    if FAILS:
        print(f"SUMMARY: ROUTE FAILS AT {FAILS[0]}")
        return 1
    print("SUMMARY: PROVED - corrigendum for PR #8180. T1: with block 34's transform L^-1 sum e^{-ik.x} th_x, P multiplies "
          "mode k by conj(phi(k)), not phi(k) (block 34 L85/L104/L108, block 35 L86 and L106's first line); with the executed "
          "pairing E[X conj Y] the display Cov = phi^s Var and the gloss C_s = sigma^2 (I - PP*)^-1 P*^s hold verbatim. In "
          "L86's labelling the two differ exactly where phi(k)^s is not real "
          f"({s3[3]-s3[4]}/{s3[3]}, {s4[3]-s4[4]}/{s4[3]}, {s6[3]-s6[4]}/{s6[3]} pairs on L = 3, 4, 6). B1/B2 cannot see it; "
          "the sine-cosine cross covariance can. T3/D2: the product test separates nothing (both kernels vanish only at 0, so "
          "neither is a product in any frame; in level time both depend on w through Re(phi e^{iw})); the frame-free "
          "separation is the Hessian of the inverse kernel at 0: 2I (elliptic) against (2/3)J (parabolic, range the "
          "causal-cone axis), with 3|1 - z|^2 = E - 3(1 - u) exactly.")
    print("HIT: block 35's T1 display and operator gloss hold with block 34's transform and the pairing E[X conj Y]; the "
          "defect is the multiplier: P acts on that mode k by conj(phi(k)) (block 34 L85/L104/L108, block 35 L86/L106); "
          "D2's product test fails for both kernels in every frame, and the separation is the Hessian of the inverse "
          "kernel at 0 - rank 3 for E, rank 1 along (1,1,1) for the formation law, where 3|1 - z|^2 = E - 3(1 - u).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
