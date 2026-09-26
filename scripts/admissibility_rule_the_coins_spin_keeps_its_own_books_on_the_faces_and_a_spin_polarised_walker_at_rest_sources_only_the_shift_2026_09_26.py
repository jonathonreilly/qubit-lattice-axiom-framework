#!/usr/bin/env python3
"""Exact checks: the coin's spin keeps its own books on the faces, and a spin-polarised walker at rest sources only the shift -
within block 54's walk and blocks 120, 136 and 138 as landed: for every state, dS~_l/dt + D(x) - D(x - e_l) = -sum_ij eps_lij
(Theta_ij - Theta_ji); a walker at rest (psi = f chi, f real) has zero energy, two-step momentum and currents, and sources the
shift through P^B = (1/4) curl S~; on the declared lattice reading of block 136 T4 the static shift is the lattice vector potential
of the magnetisation wbar S~/(16 alpha) (a harvest of probe #9214, confirmed by an other-family referee (a Grok worker, #9284); the
supervisor's port of its exact checks; not adopted).

B (the balance law): random exact states on the 5^3 and 6^3 tori; block 138 T1 reproduced; the beat identities.
C (the walker at rest): a 3^3 box of spin (3/5, 4i/5) in the 6^3 torus: zero energy and currents; P^B; the total face spin; the
       static shift by the exact inverse Laplacian; its divergence; the momentarily static source.
Exact rational and Gaussian-rational arithmetic only; the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import random
import re
import sys
from fractions import Fraction as F
from itertools import product
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 600
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_THE_COINS_SPIN_KEEPS_ITS_OWN_BOOKS_ON_THE_FACES_AND_A_SPIN_POLARISED_WALKER_AT_REST_SOURCES_ONLY_THE_SHIFT_BOUNDED_THEOREM_NOTE_2026-09-26.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_THE_COINS_SPIN_ENTERS_THE_SOURCE_LINK_THROUGH_ITS_CURL_THE_SYMMETRIC_MOMENTUM_IS_THE_TWO_STEP_MOMENTUM_PLUS_HALF_THE_CURL_OF_THE_SPIN_BOUNDED_THEOREM_NOTE_2026-09-25.md",
    "docs/ADMISSIBILITY_RULE_TWO_STEP_CONTENT_KEEPS_SYMMETRIC_BOOKS_WHERE_THE_MEMBER_KEEPS_ITS_FIELDS_AND_A_BOND_SHIFT_KEEPS_EVERY_CONSTRAINT_IFF_ALPHA_EQUALS_K_OVER_FOUR_BOUNDED_THEOREM_NOTE_2026-09-25.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_the_coins_spin_keeps_its_own_books_on_the_faces_and_a_spin_polarised_walker_at_rest_sources_only_the_shift_bounded_theorem_note_2026-09-26"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)

MUTATION_GATE = {
    "torque_sign_forged": "B",
    "magnetisation_factor_forged": "C",
    "box_spin_forged": "C",
    "claim_transition_injected": "F",
    "claim_classical_name_in_theorem": "F",
}
ACTIVE_MUTATION: str | None = None


def mut(name: str) -> bool:
    if name not in MUTATION_GATE:
        raise KeyError(name)
    return ACTIVE_MUTATION == name


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0
        self.failed_families: set[str] = set()

    def check(self, tag: str, ok: bool, msg: str) -> None:
        if ok:
            self.passed += 1
            print(f"PASS: {tag} {msg}")
        else:
            self.failed += 1
            self.failed_families.add(tag[0])
            print(f"FAIL: {tag} {msg}")


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text)


# ============================================================================================ the probe's lattice machinery (ported)
Z = (F(0), F(0))
def gm(a, b): return (a[0]*b[0] - a[1]*b[1], a[0]*b[1] + a[1]*b[0])
def ga(a, b): return (a[0] + b[0], a[1] + b[1])
def cj(a): return (a[0], -a[1])
ONE = (F(1), F(0)); MINUS = (F(-1), F(0)); MI2 = (F(0), F(-1, 2)); HALF = (F(1, 2), F(0))
SIG = [((Z, ONE), (ONE, Z)), ((Z, (F(0), F(-1))), ((F(0), F(1)), Z)), ((ONE, Z), (Z, MINUS))]
def sv(a, v): M = SIG[a]; return (ga(gm(M[0][0], v[0]), gm(M[0][1], v[1])), ga(gm(M[1][0], v[0]), gm(M[1][1], v[1])))
def vadd(u, v): return (ga(u[0], v[0]), ga(u[1], v[1]))
def vsc(u, c): return (gm(u[0], c), gm(u[1], c))
def inner(u, v): return ga(gm(cj(u[0]), v[0]), gm(cj(u[1]), v[1]))
EPS = {(0, 1, 2): 1, (1, 2, 0): 1, (2, 0, 1): 1, (0, 2, 1): -1, (2, 1, 0): -1, (1, 0, 2): -1}
class Lat:
    def __init__(self, L, ps):
        self.L = L; self.sites = list(product(range(L), repeat=3)); self.ps = ps
        self.Hp = self.Happ(ps); self.P = [self.Sapp(self.Capp(ps, j), j) for j in range(3)]; self._K = {}
    def sh(self, x, a, s=1): y = list(x); y[a] = (y[a] + s) % self.L; return tuple(y)
    def shv(self, x, v): return tuple((x[i] + v[i]) % self.L for i in range(3))
    def Happ(self, ps):
        out = {}
        for x in self.sites:
            acc = (Z, Z)
            for a in range(3):
                acc = vadd(acc, vsc(vadd(sv(a, ps[self.sh(x, a)]), vsc(sv(a, ps[self.sh(x, a, -1)]), MINUS)), MI2))
            out[x] = acc
        return out
    def Capp(self, ps, j): return {x: vsc(vadd(ps[self.sh(x, j)], ps[self.sh(x, j, -1)]), HALF) for x in self.sites}
    def Sapp(self, ps, j): return {x: vsc(vadd(ps[self.sh(x, j)], vsc(ps[self.sh(x, j, -1)], MINUS)), MI2) for x in self.sites}
    def re(self, u, a, v): return inner(u, v if a is None else sv(a, v))[0]           # Re u^dag coin v
    def dre(self, p, a, q):   # d/dt Re psi^dag(p) coin psi(q), i dpsi/dt = H psi
        A = (lambda v: v) if a is None else (lambda v: sv(a, v))
        return -inner(self.Hp[p], A(self.ps[q]))[1] + inner(self.ps[p], A(self.Hp[q]))[1]
    def energy(self, x): return inner(self.ps[x], self.Hp[x])[0]
    def pi(self, j, x): return inner(self.ps[x], self.P[j][x])[0]
    def K(self, a, j, x):
        key = (a, j, x)
        if key not in self._K:
            xa = self.sh(x, a)
            self._K[key] = (self.re(self.ps[xa], a, self.P[j][x]) + self.re(self.P[j][xa], a, self.ps[x])) / 2
        return self._K[key]
    def Th(self, i, j, y):
        ls = [m for m in range(3) if m != j]; tot = F(0)
        for s1, s2 in product((1, -1), repeat=2):
            yy = self.sh(self.sh(y, ls[0], s1), ls[1], s2); tot += self.K(i, j, yy) + self.K(i, j, self.sh(yy, j))
        return tot / 8
    def Pdd(self, j, y):
        ls = [m for m in range(3) if m != j]; tot = F(0)
        for s1, s2 in product((1, -1), repeat=2):
            yy = self.sh(self.sh(y, ls[0], s1), ls[1], s2); tot += self.pi(j, yy) + self.pi(j, self.sh(yy, j))
        return tot / 8
    def Qb(self, j, x):
        xj = self.sh(x, j)
        return (self.re(self.ps[xj], j, self.Hp[x]) + self.re(self.Hp[xj], j, self.ps[x])) / 2
    def Q(self, j, x): return sum(self.Qb(j, self.shv(x, sg)) for sg in product((1, -1), repeat=3)) / 8
    def Sface(self, l, x, rate=False):
        j, k = [m for m in range(3) if m != l]
        f = self.dre if rate else (lambda p, a, q: self.re(self.ps[p], a, self.ps[q]))
        return (f(x, l, self.sh(self.sh(x, j), k)) + f(self.sh(x, k), l, self.sh(x, j))) / 2
    def St(self, l, x, rate=False): return sum(self.Sface(l, self.shv(x, sg), rate) for sg in product((1, -1), repeat=3)) / 8
    def curl(self, j, x):
        return sum(e * (self.St(l, x) - self.St(l, self.sh(x, k, -1))) for (jj, k, l), e in EPS.items() if jj == j)
    def D0(self, x):
        pairs = [((0, 0, 0), (1, 1, 1)), ((0, 0, 1), (1, 1, 0)), ((0, 1, 0), (1, 0, 1)), ((1, 0, 0), (0, 1, 1))]
        return sum(self.re(self.ps[self.shv(x, a)], None, self.ps[self.shv(x, b)]) for a, b in pairs) / 4
    def D(self, x): return sum(self.D0(self.shv(x, sg)) for sg in product((1, -1), repeat=3)) / 8
    def torque(self, l, x): return -sum(e * (self.Th(i, j, x) - self.Th(j, i, x)) for (ll, i, j), e in EPS.items() if ll == l)

RND = random.Random(9200)
def rq(): return (F(RND.randint(-5, 5), RND.randint(1, 4)), F(RND.randint(-5, 5), RND.randint(1, 4)))



# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms, t138, t136 = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no possibility is privileged; no site is privileged; Admissibility is not a dynamics axiom (the walk, its densities, the member and the shift are supplied; the memo does not define a time metric)")
    ok138 = "*Statement.* For every state on `ℤ³` and `j = 1, 2, 3`: `Q_j − P″_j = ½Σ_klε_jkl∇̄_kS̃_l`." in t138 and "`Σ_i∇̄_i(Θ_ij − Θ_ji) = ½ d/dt(∇̄ × S̃)_j` for every state" in t138
    ok136 = "the shift constraints, `8αpφ̇/w̄ = P_z` along the wave vector and `4αp(pN_x − ċ_x)/w̄ = P_x` across it." in t136
    checks.check("A3", ok138 and ok136, "the landed texts carry block 138 T1 and T3 and block 136 T4's shift constraints, as used")


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    sign = -1 if mut("torque_sign_forged") else 1
    for tag, L, nst, stride in (("B1", 5, 2, 1), ("B2", 6, 1, 7)):
        ok_all = True
        cnt_tot = 0
        for s in range(nst):
            lat = Lat(L, {x: (rq(), rq()) for x in product(range(L), repeat=3)})
            res = F(0); nzr = nzt = nzd = 0; cnt = 0
            for x in lat.sites[::stride]:
                for l in range(3):
                    r = lat.St(l, x, True); dD = lat.D(x) - lat.D(lat.sh(x, l, -1)); tq = sign * lat.torque(l, x)
                    res = max(res, abs(r + dD - tq)); nzr += r != 0; nzt += tq != 0; nzd += dD != 0; cnt += 1
            ok_all = ok_all and res == 0 and nzr == cnt and nzt > cnt // 2 and nzd == cnt
            cnt_tot += cnt
        checks.check(tag, ok_all, f"on the {L}^3 torus ({nst} random Gaussian-rational state(s), {cnt_tot} site-direction pairs): dS~_l/dt + D(x) - D(x - e_l) = -sum_ij eps_lij (Theta_ij - Theta_ji) with zero residual and all three terms nonzero")
    lat5 = Lat(5, {x: (rq(), rq()) for x in product(range(5), repeat=3)})
    t1 = max(abs(lat5.Q(j, x) - lat5.Pdd(j, x) - lat5.curl(j, x) / 2) for x in lat5.sites[::9] for j in range(3))
    checks.check("B3", t1 == 0, "the same densities reproduce block 138 T1, Q_j - P''_j = (1/2)(curl S~)_j, on a random state of the 5^3 torus")
    s = sp.symbols("s1:4"); t = sp.symbols("t1:4")
    Pm = [sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -sp.I], [sp.I, 0]]), sp.Matrix([[1, 0], [0, -1]])]
    sd = lambda v: v[0] * Pm[0] + v[1] * Pm[1] + v[2] * Pm[2]
    bi = True
    for l in range(3):
        lhs = sd(t) * Pm[l] - Pm[l] * sd(s)
        rhs = (t[l] - s[l]) * sp.eye(2) + sp.I * sum((EPS.get((m, l, n), 0) * (s[m] + t[m]) * Pm[n] for m in range(3) for n in range(3)), sp.zeros(2))
        bi = bi and sp.simplify(lhs - rhs) == sp.zeros(2)
    kb, qq, a, b, c = sp.symbols("kb q a b c", real=True)
    trig = (sp.simplify(sp.sin(kb + qq / 2) - sp.sin(kb - qq / 2) - 2 * sp.cos(kb) * sp.sin(qq / 2)) == 0
            and sp.simplify((sp.sin(kb + qq / 2) + sp.sin(kb - qq / 2)) * sp.cos(kb) - sp.sin(2 * kb) * sp.cos(qq / 2)) == 0
            and sp.simplify(sp.expand_trig(4 * sp.cos(a) * sp.cos(b) * sp.cos(c) - sum(sp.cos(a + e1 * b + e2 * c) for e1 in (1, -1) for e2 in (1, -1)))) == 0)
    checks.check("B4", bi and trig, "the beat identities: (sigma.s') sigma_l - sigma_l (sigma.s) = (s'_l - s_l) + i eps_mln (s_m + s'_m) sigma_n; s_l - s'_l = 2 cos kb_l sin(q_l/2); (s_a + s'_a) cos kb_a = sin 2kb_a cos(q_a/2); the mean of the four body-diagonal cosines is the product of the three")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    L = 6
    box = {(x, y, z) for x in range(3) for y in range(3) for z in range(3)}
    chi = ((F(3, 5), F(0)), (F(0), F(4, 5)))
    n_chi = [inner(chi, sv(a, chi))[0] for a in range(3)]
    psr = {x: (chi if x in box else (Z, Z)) for x in product(range(L), repeat=3)}
    W = Lat(L, psr)
    zero_all = (all(W.energy(x) == 0 for x in W.sites) and all(W.pi(j, x) == 0 for x in W.sites for j in range(3))
                and all(W.K(a, j, x) == 0 for x in W.sites for a in range(3) for j in range(3)))
    checks.check("C1", n_chi == [F(0), F(24, 25), F(-7, 25)] and zero_all, "a 3^3 box of spin chi = (3/5, 4i/5), n = (0, 24/25, -7/25), at rest in the 6^3 torus: energy density, two-step momentum and every current K vanish at every site, so Theta = 0 and P'' = 0")
    PB = {(j, x): W.Q(j, x) / 2 for j in range(3) for x in W.sites}
    curl = {(j, x): W.curl(j, x) for j in range(3) for x in W.sites}
    nzPB = sum(1 for v in PB.values() if v != 0)
    checks.check("C2", all(PB[(j, x)] == curl[(j, x)] / 4 for j in range(3) for x in W.sites) and 0 < nzPB < 3 * W.L ** 3, f"P^B = (1/4)(curl S~) on every bond, nonzero on {nzPB} bonds of {3 * W.L ** 3}")
    StT = {l: sum(W.St(l, x) for x in W.sites) for l in range(3)}
    bcount = 12 if not mut("box_spin_forged") else 9
    checks.check("C3", [StT[l] for l in range(3)] == [bcount * v for v in n_chi], "the total face spin is b(b - 1)^2 n = 12 n at b = 3")
    lam = sp.symbols("lam")
    qpoly = sp.Poly(sp.interpolate([(0, 0)] + [(v, sp.Rational(1, v)) for v in range(1, 13)], lam), lam)
    coef = [F(int(sp.fraction(cc)[0]), int(sp.fraction(cc)[1])) for cc in qpoly.all_coeffs()]

    def mlap(f):
        return {x: sum(2 * f[x] - f[W.sh(x, i)] - f[W.sh(x, i, -1)] for i in range(3)) for x in W.sites}

    def G(f):
        acc = {x: F(0) for x in W.sites}
        for cc in coef:
            acc = mlap(acc)
            acc = {x: acc[x] + cc * f[x] for x in W.sites}
        return acc
    alpha, wbar = F(1, 4), F(1)
    N = {j: G({x: wbar * PB[(j, x)] / (4 * alpha) for x in W.sites}) for j in range(3)}
    solved = all(4 * alpha * mlap(N[j])[x] == wbar * PB[(j, x)] for j in range(3) for x in W.sites)
    fac = 16 if not mut("magnetisation_factor_forged") else 8
    GS = {l: G({x: W.St(l, x) - StT[l] / W.L ** 3 for x in W.sites}) for l in range(3)}
    A = {j: {x: wbar / (fac * alpha) * sum(e * (GS[l][x] - GS[l][W.sh(x, k, -1)]) for (jj, k, l), e in EPS.items() if jj == j) for x in W.sites} for j in range(3)}
    checks.check("C4", solved and all(N[j][x] == A[j][x] for j in range(3) for x in W.sites) and any(N[j][x] != 0 for j in range(3) for x in W.sites),
                 "4 alpha (-Lap) N = wbar P^B is solved exactly with the degree-12 inverse Laplacian of the 6^3 torus, and N equals the lattice vector potential curl (-Lap)^(-1) of the magnetisation wbar S~/(16 alpha) at every bond")
    divN = max(abs(sum(N[j][x] - N[j][W.sh(x, j, -1)] for j in range(3))) for x in W.sites)
    checks.check("C5", divN == 0, "the static shift has zero lattice divergence, so the longitudinal constraint is P^B_parallel = 0 and the clock is not driven")
    PH = [W.Sapp(W.Capp(W.Hp, j), j) for j in range(3)]
    dpi = max(abs(-inner(W.Hp[x], W.P[j][x])[1] + inner(W.ps[x], PH[j][x])[1]) for x in W.sites for j in range(3))
    spinrate = {(l, x): W.St(l, x, True) for l in range(3) for x in W.sites}
    gradD = all(spinrate[(l, x)] == -(W.D(x) - W.D(W.sh(x, l, -1))) for l in range(3) for x in W.sites)
    curlrate = max(abs(sum(e * (spinrate[(l, x)] - spinrate[(l, W.sh(x, k, -1))]) for (jj, k, l), e in EPS.items() if jj == j)) for j in range(3) for x in W.sites)
    checks.check("C6", dpi == 0 and gradD and curlrate == 0 and any(v != 0 for v in spinrate.values()), "at rest d pi/dt = 0 and dS~/dt = -grad D with zero torque, so the curl of the spin, and with it P^B, is momentarily static")


# ============================================================================================ family F
FENCES = (
    "This note works within blocks 54, 120, 136 and 138 as landed on main (the walk, the two-step stress, the momentum the shift sees, and the face spin); it reports the balance law of the coin's spin on the faces and what a spin-polarised walker at rest sources; nothing is adopted and no gravitational claim is made.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
    "time dilation", "equivalence principle", "general relativity", "horizon", "gravitational wave", "gravitational lens",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at b = 3."}
CLASSICAL_NAMES = ("Newton", "Weyl", "Noether", "Dirac", "Lorentz", "Belinfante", "Rosenfeld", "Biot", "Savart", "Ampere", "Ampère", "Maxwell", "Lense", "Thirring",
                   "Taylor", "Fourier", "Bloch", "Euler", "Laplace", "Poisson", "Gauss", "Einstein", "Planck", "Green", "Pauli", "Hamilton", "Wigner", "Riemann", "Hilbert", "Schur", "Fermi")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T1", phrase + "\n\n## Theorem T1", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T3 — the shift is the vector potential of a magnetisation", "## Theorem T3 — the shift is the vector potential of a magnetisation (after Maxwell)", 1)
    norm = normalize_text(text)
    checks.check("F1", all(normalize_text(f) in norm for f in FENCES), "the note carries the three fence sentences verbatim")
    hits = [p for p in FORBIDDEN if p in text]
    checks.check("F2", not hits, f"the note contains no forbidden phrase ({len(hits)} hits)")
    src = Path(__file__).read_text(encoding="utf-8")
    body = src.split(SCAN_MARKER)[0]
    float_hits = re.findall(r"(?<![\w.])\d+\.\d+(?![\w.])|\bfloat\(|\.evalf\(|\bN\(", body)
    checks.check("F3", not float_hits, f"runner source: no floating-point literal or conversion call ({len(float_hits)} hits)")
    sections = re.split(r"^## ", text, flags=re.M)
    offenders = []
    for sec in sections[1:]:
        title = sec.split("\n", 1)[0].strip()
        if any(title.startswith(a) for a in ALLOWED_NAME_SECTIONS):
            continue
        for nm in CLASSICAL_NAMES:
            if re.search(r"\b" + nm + r"\b", sec):
                offenders.append((title[:40], nm))
    offenders += [("front matter", nm) for nm in CLASSICAL_NAMES if re.search(r"\b" + nm + r"\b", sections[0])]
    checks.check("F4", not offenders, f"the authors' names appear only under Prior art, Imports, the Premises and the Review record ({len(offenders)} offenders)")


# ============================================================================================ family G
N5_LINES = (
    "per_element: executed - the coin identity and the beat identities symbolically",
    "per_site: executed - the balance law at every site and direction of the 5^3 torus on random exact states",
    "per_mode: executed - P^B = (1/4) curl S~ on every bond of the 6^3 torus for the box at rest",
    "per_block: executed - the exact inverse Laplacian of the 6^3 torus and the vector potential; the divergence; the momentary rates",
    "lattice_wide: checked and not executed - every state by proof; T3 on the declared lattice reading of block 136 T4",
)


def family_g(checks: Checks) -> None:
    for line in N5_LINES:
        print(line)
    checks.check("G1", len(N5_LINES) == 5, "the five N5 resolution lines are printed")


def main(argv) -> int:
    global ACTIVE_MUTATION
    if "--list-mutations" in argv:
        for name, fam in MUTATION_GATE.items():
            print(f"{name} {fam}")
        return 0
    if "--mutation" in argv:
        ACTIVE_MUTATION = argv[argv.index("--mutation") + 1]
        if ACTIVE_MUTATION not in MUTATION_GATE:
            print(f"unknown mutation {ACTIVE_MUTATION}")
            return 2
    print("AUDIT_INPUT_PATHS:")
    for p in AUDIT_INPUT_PATHS:
        print(f"  {p}")
    texts = [Path(ROOT, p).read_text(encoding="utf-8") if Path(ROOT, p).exists() else "" for p in AUDIT_INPUT_PATHS]
    checks = Checks()
    family_a(checks, texts)
    family_b(checks)
    family_c(checks)
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print("scope: block 54's walk with blocks 120, 136 and 138 as landed; the face spin's balance law for every state; a walker at rest with a real envelope sources only the shift, through P^B = (1/4) curl S~; the static shift is the lattice vector potential of wbar S~/(16 alpha) on the declared reading of block 136 T4; harvest of #9214 confirmed by a Grok referee (#9284); nothing adopted")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
