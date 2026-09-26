#!/usr/bin/env python3
"""Exact checks: no local rule of any fixed radius sets the price of forming a record, under either reading; a point-equivalent
source has an exact local price (a harvest of probe #9175, confirmed by an other-family referee in #9311), within block 116's
held-wall law as landed: g = (1 - A)^-1 inside a held cube of odd side with zero wall values, k = gamma/12, the static law
((1 - A) + kK) psi = k e with phi = 1 - psi, and the ledger-keeping price E' = Lambda/(1 - k Lambda g_yy).

A (premises): the landed notes carry the quoted lines.
B (T1, the ledger): Lambda = sum e phi = sum K phi = Q, the total effective source; E' = Q/phi'_y; the post-event field is
   k Q g(., y); block 116's cube prices (four distinct, increasing towards the centre) and the star's 1188/1091 (side 7 and 9).
C (T2, records only): g at the centre of the held cubes of side 3, 5, 7, 9 is 1, 22/17, 136/99, 79271956/56195761, and the whole
   g(., y) grows with the box; one amplitude in the pairs of boxes has identical data within R = 0, 1, 2 and different prices.
D (T3, amplitude sourcing): the cage (1 - A)[g(., y) 1_(outside B_(R+1))] lies on the layers R+1, R+2 with total charge 1 and
   zero field inside; adding c of it as bodies at rest solves the law exactly, leaves every datum within radius R unchanged,
   and shifts the ledger by c (three pairs; a positivity certificate for uniqueness).
E (T4, point-equivalent sources): if s - Q delta_y = (1 - A)f with f finitely supported, E' = Q/(phi_y + k f_y) exactly in
   every held box (three asymmetric sources); the star is f = -6 s_1 delta_y; the discrete harmonic quartic separates the
   distance-two cross.
Exact rational arithmetic (a banded factorisation of 1 - A on the held cube; sympy). The probe's decimal comparisons and its
conditional part (b) are not used. The runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import itertools
import re
import sys
import time
from fractions import Fraction as F
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 600
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_NO_LOCAL_RULE_OF_ANY_FIXED_RADIUS_SETS_THE_PRICE_OF_FORMING_A_RECORD_UNDER_EITHER_READING_AND_A_POINT_EQUIVALENT_SOURCE_HAS_AN_EXACT_LOCAL_PRICE_BOUNDED_THEOREM_NOTE_2026-09-26.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_FORMING_ONE_RECORD_KEEPS_THE_LEDGER_ONLY_AT_A_PRICE_ONE_PRICE_SERVES_EVERY_SITE_ONLY_WITH_THE_AMBIENT_AT_INFINITY_AND_A_SOURCE_IN_TWO_PLACES_SEPARATES_THE_READINGS_BOUNDED_THEOREM_NOTE_2026-09-24.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_no_local_rule_of_any_fixed_radius_sets_the_price_of_forming_a_record_under_either_reading_and_a_point_equivalent_source_has_an_exact_local_price_bounded_theorem_note_2026-09-26"
AXIOM_NEEDLES = (
    "No possibility is privileged.",
    "No site is privileged.",
    "Admissibility is not a dynamics axiom.",
)
LANDED_NEEDLES = (
    (2, "has ledger `E'/(1 + kE' g_yy)`"),
    (2, "`g = (1 − A)⁻¹` inside, with zero wall values."),
    (2, "only records enter, and an unrecorded amplitude sources nothing."),
    (2, "`E' = c/(1 − kc)`, with `c = m₀/(1 + km₀) + 6m₁`"),
)

MUTATION_GATE = {
    "landed_quote_forged": "A",
    "ledger_identity_forged": "B",
    "green_growth_forged": "C",
    "cage_charge_forged": "D",
    "harmonic_quartic_forged": "E",
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
            print(f"PASS: {tag} {msg}", flush=True)
        else:
            self.failed += 1
            self.failed_families.add(tag[0])
            print(f"FAIL: {tag} {msg}", flush=True)


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text)


T0 = time.time()


# ============================================================================================ exact held-box machinery (probe #9175's, ported)
class HeldBox:
    """Held cube of odd side n: the boundary layer is the wall; (1 - A) on the interior with zero wall values."""

    def __init__(self, n):
        self.n, self.m = n, n - 2
        self.sites = list(itertools.product(range(1, n - 1), repeat=3))
        self.idx = {s: i for i, s in enumerate(self.sites)}
        self.N = len(self.sites)
        self.nb = [[self.idx.get(tuple(s[i] + (sg if i == j else 0) for i in range(3))) for j in range(3) for sg in (1, -1)]
                   for s in self.sites]
        bw = self.m * self.m
        U = [{i: F(1), **{j: F(-1, 6) for j in self.nb[i] if j is not None}} for i in range(self.N)]
        L = [dict() for _ in range(self.N)]
        for i in range(self.N):
            piv = U[i][i]
            for r2 in range(i + 1, min(self.N, i + bw + 1)):
                f = U[r2].get(i)
                if not f:
                    continue
                q = f / piv
                L[r2][i] = q
                for c, v in U[i].items():
                    if c > i:
                        U[r2][c] = U[r2].get(c, F(0)) - q * v
                del U[r2][i]
        self.L, self.U, self._cols = L, U, {}

    def solve(self, rhs):
        b = [F(x) for x in rhs]
        for i in range(self.N):
            for c, q in self.L[i].items():
                b[i] -= q * b[c]
        x = [F(0)] * self.N
        for i in range(self.N - 1, -1, -1):
            s = b[i] - sum(v * x[c] for c, v in self.U[i].items() if c > i)
            x[i] = s / self.U[i][i]
        return x

    def col(self, i):
        if i not in self._cols:
            e = [F(0)] * self.N
            e[i] = F(1)
            self._cols[i] = self.solve(e)
        return self._cols[i]

    def lap(self, v):
        return [v[i] - sum(v[j] for j in self.nb[i] if j is not None) / 6 for i in range(self.N)]

    def centre(self):
        return ((self.n - 1) // 2,) * 3


BOXES = {}


def box(n):
    if n not in BOXES:
        BOXES[n] = HeldBox(n)
    return BOXES[n]


def small_solve(A, b):
    n = len(A)
    M = [row[:] + [b[i]] for i, row in enumerate(A)]
    for c in range(n):
        p = next(r for r in range(c, n) if M[r][c] != 0)
        M[c], M[p] = M[p], M[c]
        M[c] = [x / M[c][c] for x in M[c]]
        for r in range(n):
            if r != c and M[r][c] != 0:
                f = M[r][c]
                M[r] = [x - f * y for x, y in zip(M[r], M[c])]
    return [M[i][n] for i in range(n)]


def static(B, masses, k):
    """Amplitude sourcing, bodies at rest (K = diag(m), e = m): ((1-A) + k diag m) psi = k m. Woodbury on the support."""
    S = sorted(masses)
    cols = {i: B.col(i) for i in S}
    A = [[(F(1) if a == b else F(0)) + k * cols[b][a] * masses[b] for b in S] for a in S]
    phiS = small_solve(A, [F(1)] * len(S))
    s = {j: masses[j] * p for j, p in zip(S, phiS)}
    psi = [k * sum(cols[j][x] * s[j] for j in S) for x in range(B.N)]
    return psi, s


def post_phi(B, Ep, iy, k):
    """Record at rest at y with bare energy Ep: phi'_y = 1/(1 + k Ep g_yy)."""
    g = B.col(iy)[iy]
    return 1 / (1 + k * Ep * g)


def residual_zero(B, masses, psi, k):
    L = B.lap(psi)
    return all(L[i] + k * masses.get(i, F(0)) * (psi[i] - 1) == 0 for i in range(B.N))


def cheb(a, b):
    return max(abs(a[i] - b[i]) for i in range(3))



# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts[0], texts[1]
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: no possibility is privileged; no site is privileged; Admissibility is not a dynamics axiom (the held-wall law and the readings are supplied)")
    needles = list(LANDED_NEEDLES)
    if mut("landed_quote_forged"):
        needles[0] = (2, "has ledger `E'/(1 − kE' g_yy)`")
    checks.check("A3", all(nd in texts[i] for i, nd in needles), "landed block 116 carries the ledger of a record at rest, the held-wall Green function, the records-only reading and the star's price c/(1 - kc)")


# ============================================================================================ family B (T1)
def family_b(checks: Checks) -> None:
    ok = True
    k = F(1, 12)
    B = box(7)
    cube = {B.idx[(x, y, z)]: F(1, 27) for x in (2, 3, 4) for y in (2, 3, 4) for z in (2, 3, 4)}
    psi, s = static(B, cube, k)
    ok &= residual_zero(B, cube, psi, k)
    phi = [1 - p for p in psi]
    Lam = sum(m * phi[i] for i, m in cube.items())
    Q = sum(s.values())
    ok &= (Lam == Q + (F(1, 10 ** 9) if mut("ledger_identity_forged") else 0))
    prices = []
    for y in [(2, 2, 2), (2, 2, 3), (2, 3, 3), (3, 3, 3)]:
        iy = B.idx[y]
        gyy = B.col(iy)[iy]
        Ep = Lam / (1 - k * Lam * gyy)
        php = post_phi(B, Ep, iy, k)
        ok &= Ep * php == Lam and Ep == Q / php
        post_psi = [k * Ep * php * B.col(iy)[x] for x in range(B.N)]
        ok &= residual_zero(B, {iy: Ep}, post_psi, k)
        prices.append(Ep)
    ok &= prices == sorted(prices) and len(set(prices)) == 4
    star_ok = True
    cross = {}
    for n in (7, 9):
        Bn = box(n)
        c = Bn.centre()
        iy = Bn.idx[c]
        star = [c] + [tuple(c[i] + (sg if i == j else 0) for i in range(3)) for j in range(3) for sg in (1, -1)]
        crs = [c] + [tuple(c[i] + (2 * sg if i == j else 0) for i in range(3)) for j in range(3) for sg in (1, -1)]
        for tag, pts in (("star", star), ("cross", crs)):
            ms = {Bn.idx[p]: F(1, 7) for p in pts}
            ps, ss = static(Bn, ms, k)
            Qn = sum(ss.values())
            Ep = Qn / (1 - k * Qn * Bn.col(iy)[iy])
            if tag == "star":
                star_ok &= Ep == F(1188, 1091)
            else:
                cross[n] = Ep
    checks.check("B1", ok and star_ok and cross[7] != cross[9], "held cube of side 7, a uniform 3x3x3 of rest energies 1/27 (gamma = 1): the ledger equals the total effective source, Lambda = sum e phi = sum K phi = Q; the four symmetry classes have four distinct prices, increasing towards the centre; each price satisfies E' phi'_y = Lambda and its post-event field k Lambda g(., y) solves the law exactly; the uniform star costs 1188/1091 in the cubes of side 7 and 9, while the distance-two cross's price differs between them")


# ============================================================================================ family C (T2)
def family_c(checks: Checks) -> None:
    ok = True
    k = F(1, 12)
    gc = {}
    for n in (3, 5, 7, 9):
        B = box(n)
        c = B.centre()
        gc[n] = B.col(B.idx[c])[B.idx[c]]
    want5 = F(23, 17) if mut("green_growth_forged") else F(22, 17)
    ok &= gc[3] == 1 and gc[5] == want5 and gc[7] == F(136, 99) and gc[9] == F(79271956, 56195761) and gc[3] < gc[5] < gc[7] < gc[9]
    for n in (5, 7):
        Bs, Bl = box(n), box(n + 2)
        cs, cl = Bs.centre(), Bl.centre()
        gs, gl = Bs.col(Bs.idx[cs]), Bl.col(Bl.idx[cl])
        ok &= all(gl[Bl.idx[tuple(x + 1 for x in s)]] > gs[Bs.idx[s]] for s in Bs.sites)
    E = F(1)
    pr = {n: E / (1 - k * E * gc[n]) for n in gc}
    ok &= len(set(pr.values())) == 4 and pr[3] == F(12, 11) and pr[5] == F(102, 91) and pr[7] == F(297, 263)
    checks.check("C1", ok, "records only (phi = 1 before the event): g at the centre of the held cubes of side 3, 5, 7, 9 is 1, 22/17, 136/99, 79271956/56195761, and the whole g(., y) of the larger cube exceeds the smaller's at every interior site; one amplitude with E = 1 at the centre has identical data within R = 0, 1, 2 in the pairs (3,5), (5,7), (7,9) and prices 12/11, 102/91, 297/263 and a fourth, all distinct")


# ============================================================================================ family D (T3)
def family_d(checks: Checks) -> None:
    ok = True
    k = F(1, 12)
    total = F(2) if mut("cage_charge_forged") else F(1)
    shifts = 0
    for n, R, A, c in ((7, 0, {(3, 3, 3): F(1, 2)}, F(1, 5)), (9, 1, {(4, 4, 4): F(1, 2), (5, 4, 4): F(1, 3)}, F(1, 4)),
                       (9, 1, {(4, 4, 4): F(2, 3), (4, 3, 4): F(1, 6), (3, 4, 5): F(1, 5)}, F(-1, 7))):
        B = box(n)
        y = B.centre()
        iy = B.idx[y]
        masses = {B.idx[p]: v for p, v in A.items()}
        psi1, s1 = static(B, masses, k)
        phi1 = [1 - p for p in psi1]
        Lam1 = sum(s1.values())
        g = B.col(iy)
        v = [g[i] if cheb(B.sites[i], y) > R + 1 else F(0) for i in range(B.N)]
        cage = B.lap(v)
        ok &= sum(cage) == total and all(cheb(B.sites[i], y) in (R + 1, R + 2) for i in range(B.N) if cage[i] != 0)
        phi2 = [phi1[i] - k * c * v[i] for i in range(B.N)]
        m2 = dict(masses)
        for i in range(B.N):
            if cage[i] != 0:
                m2[i] = c * cage[i] / phi2[i]
        psi2 = [1 - p for p in phi2]
        ok &= residual_zero(B, m2, psi2, k)
        x = F(3, B.m + 1)
        lam_low = x * x / 2 - x ** 4 / 24
        ok &= lam_low + k * min(min(m2.values()), F(0)) > 0
        win = [i for i in range(B.N) if cheb(B.sites[i], y) <= R]
        ok &= all(phi1[i] == phi2[i] and masses.get(i, 0) == m2.get(i, 0) for i in win)
        Lam2 = sum(m2[i] * phi2[i] for i in m2)
        ok &= Lam2 - Lam1 == c
        gyy = g[iy]
        E1, E2 = Lam1 / (1 - k * Lam1 * gyy), Lam2 / (1 - k * Lam2 * gyy)
        shifts += E1 != E2
    checks.check("D1", ok and shifts == 3, "amplitude sourcing: the cage (1 - A)[g(., y) 1_(outside B_(R+1))] lies on the Chebyshev layers R+1, R+2 with total charge exactly 1 and field g(., y) outside B_(R+1), zero inside; adding c of it as bodies at rest solves the static law with zero residual (positive definite, so unique), leaves the amplitude and every rate within radius R unchanged, shifts the ledger by exactly c, and changes the price: side 7 with R = 0, c = 1/5; side 9 with R = 1, c = 1/4 and c = -1/7")


# ============================================================================================ family E (T4)
def family_e(checks: Checks) -> None:
    ok = True
    k = F(1, 12)

    def lap_sparse(B, f):
        o = {}
        for i, v in f.items():
            o[i] = o.get(i, F(0)) + v
            for j in B.nb[i]:
                if j is not None:
                    o[j] = o.get(j, F(0)) - v / 6
        return o
    for n, y, Q, fsh in ((7, (3, 3, 3), F(9, 10), {(0, 0, 0): F(-1, 5), (1, 0, 0): F(1, 10), (0, -1, 0): F(1, 20)}),
                         (9, (4, 3, 5), F(9, 10), {(0, 0, 0): F(-1, 5), (1, 0, 0): F(1, 10), (0, -1, 0): F(1, 20)}),
                         (9, (4, 4, 4), F(3, 4), {(0, 0, 0): F(1, 3), (0, 1, 1): F(-1, 4), (-1, 0, 0): F(1, 6)})):
        B = box(n)
        iy = B.idx[y]
        f = {B.idx[tuple(y[i] + d[i] for i in range(3))]: v for d, v in fsh.items()}
        w = lap_sparse(B, f)
        s = dict(w)
        s[iy] = s.get(iy, F(0)) + Q
        s = {i: v for i, v in s.items() if v != 0}
        psi = B.solve([k * s.get(i, F(0)) for i in range(B.N)])
        phi = [1 - p for p in psi]
        masses = {i: v / phi[i] for i, v in s.items()}
        psi_chk, s_chk = static(B, masses, k)
        ok &= psi_chk == psi and sum(s_chk.values()) == Q
        Ep = Q / (1 - k * Q * B.col(iy)[iy])
        rule = Q / (phi[iy] + k * f[iy])
        ok &= rule == Ep and post_phi(B, Ep, iy, k) == phi[iy] + k * f[iy]
    m0, m1, kk, a, b = sp.symbols("m0 m1 k a b", positive=True)
    Qs = m0 * a + 6 * m1 * b
    c_ = m0 / (1 + kk * m0) + 6 * m1
    rule_star = (Qs / (a - 6 * kk * m1 * b)).subs(a, b / (1 + kk * m0))
    ok &= sp.simplify(rule_star - c_ / (1 - kk * c_)) == 0
    X, Y, Z = sp.symbols("X Y Z")
    P = X ** 4 - 6 * X ** 2 * Y ** 2 + Y ** 4 - 2 * Z ** 2
    lapP = sum(P.subs(v, v + 1) + P.subs(v, v - 1) - 2 * P for v in (X, Y, Z))
    ok &= sp.expand(lapP) == 0
    pairP = lambda pts, scale: sum(P.subs({X: scale * p[0], Y: scale * p[1], Z: scale * p[2]}) for p in pts)
    unit = [tuple(sg if i == j else 0 for i in range(3)) for j in range(3) for sg in (1, -1)]
    star_pair = pairP(unit, 1) - 6 * P.subs({X: 0, Y: 0, Z: 0})
    cross_pair = pairP(unit, 2) - 6 * P.subs({X: 0, Y: 0, Z: 0})
    want = 24 if mut("harmonic_quartic_forged") else 48
    ok &= star_pair == 0 and cross_pair == want
    checks.check("E1", ok, "point-equivalent sources (s - Q delta_y = (1 - A)f, f finitely supported): in every checked held box the price is E' = Q/(phi_y + k f_y) and the post-event clock is phi'_y = phi_y + k f_y exactly (three asymmetric sources, sides 7 and 9); block 116's star is f = -6 s_1 delta_y and the rule reduces to c/(1 - kc); the discrete harmonic quartic x^4 - 6x^2y^2 + y^4 - 2z^2 pairs to 0 with the star's excess and to 48 with the distance-two cross's, so the cross is not point-equivalent")


# ============================================================================================ family F
FENCES = (
    "This note works within block 116 as landed on main (the held-wall law, the two readings and the price that keeps the ledger when one record forms); it reports whether that price can be set from data near the record; nothing is adopted and no gravitational claim is made.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
    "time dilation", "equivalence principle", "general relativity", "horizon", "gravitational wave", "gravitational lens",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at the cage."}
CLASSICAL_NAMES = ("Newton", "Weyl", "Noether", "Dirac", "Lorentz", "Einstein", "Hilbert", "Deser", "Fock", "Ivanenko", "Belinfante", "Rosenfeld", "Cartan", "Kibble",
                   "Sciama", "Hehl", "Wilson", "Pauli", "Fierz", "Taylor", "Fourier", "Euler", "Lagrange", "Laplace", "Poisson", "Gauss", "Planck", "Green", "Hamilton",
                   "Riemann", "Christoffel", "Lie", "Levi-Civita", "Schur", "Fermi", "Faraday", "Chebyshev", "Woodbury")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T1", phrase + "\n\n## Theorem T1", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1 —", "## Theorem T1 (after Weyl) —", 1)
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
            if re.search(r"\b" + re.escape(nm) + r"\b", sec):
                offenders.append((title[:40], nm))
    offenders += [("front matter", nm) for nm in CLASSICAL_NAMES if re.search(r"\b" + re.escape(nm) + r"\b", sections[0])]
    checks.check("F4", not offenders, f"the authors' names appear only under Prior art, Imports, the Premises and the Review record ({len(offenders)} offenders)")


# ============================================================================================ family G
N5_LINES = (
    "per_element: executed - the static law's exact solution and residual in held cubes of side 3 to 9",
    "per_site: executed - the Green function's growth at every interior site of the smaller cube, and the cage's layers site by site",
    "per_mode: executed - the ledger identity and the prices at the four symmetry classes; the star and the cross",
    "per_block: executed - three cage pairs and three point-equivalent sources; the harmonic quartic",
    "lattice_wide: checked and not executed - window-confined sources that are not point-equivalent, crowds of records, and the delayed law (b)",
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
    family_d(checks)
    family_e(checks)
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print(f"scope: block 116's held-wall law: no rule of any fixed radius sets the formation price in every held box (records only: one amplitude in two boxes; amplitude sourcing: a charged cage outside the window); point-equivalent sources have the exact local price Q/(phi_y + k f_y); harvest of #9175 (confirmed by #9311); nothing adopted ({time.time() - T0:.0f}s)")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
