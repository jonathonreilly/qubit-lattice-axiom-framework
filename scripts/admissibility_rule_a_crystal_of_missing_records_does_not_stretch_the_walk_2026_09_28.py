#!/usr/bin/env python3
"""Exact checks: a lower density of records at held sites, read as a crystal of sites with no record, does not act on the walk as a stretch.
Rule R1 (the walker's amplitude lives only on sites with a record; bonds to a site with no record are cut). (T1) For a vacancy crystal whose
period lattice lies in 2Z^3, the eight species fold to one point; at first order the long waves are the taste cube h(q) = sum_a q_a A_a x sigma_a
on the corners of {0,1}^3 not occupied by the vacancies' parity classes (A_a the direction-a adjacency of the remaining corners); for period 2
this holds at every wave number with q_a -> sin(Q_a/2). (T2) For every one of the 256 corner sets, every long-wave speed along a coordinate
axis is exactly 1 or 0; for 232 sets every moving wave has group speed exactly 1 within a coordinate line, plane or all of space
(characteristic polynomial lambda^(2z) prod (lambda^2 - q_S^2)^(m_S)); the other 24 sets (one class: four remaining corners on a path that
turns through all three axes) slow oblique waves only. (T3) Sublattice-imbalanced vacancies leave exact zero-energy flat bands (named import);
an odd period removes every species' zero-energy doublet. (T4) Rule R3 (hop to the nearest record) is a relabelling: the walk on the records is
the undiluted walk, so long waves outrun the grid by the mean spacing. The supervisor's own derivation, unrefereed. Block 54's walk as landed.

A (premises): the axioms' Record text; landed block 135's statement of the walk.
B (T1): the taste-cube reduction; period-4 kernels and first-order velocities.
C (T1): period 2 at every wave number.
D (T2): all 256 corner sets: axis speeds, factorisation, the exceptional class.
E (T3): flat bands at a generic wave number; odd period.
F (T4): rule R3 is a relabelling.
R (T5): one vacancy exactly (the local scalar T-matrix on the 4^3 torus); random vacancies at first order in the concentration.
Exact (sympy, Gaussian rationals). The runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import itertools
import re
import sys
import time
from pathlib import Path

import sympy as sp
from sympy import QQ_I
from sympy.polys.matrices import DomainMatrix


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_A_CRYSTAL_OF_MISSING_RECORDS_DOES_NOT_STRETCH_THE_WALK_ALONG_EVERY_AXIS_A_LONG_WAVE_KEEPS_SPEED_ONE_OR_STOPS_BOUNDED_THEOREM_NOTE_2026-09-28.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
    "docs/ADMISSIBILITY_RULE_ONE_LIGHT_CONE_EXACTLY_ON_THE_LATTICE_THE_TWO_STEP_CONTENT_MEETS_THE_MEMBERS_IDENTITY_FOR_EVERY_STATE_IFF_ALPHA_EQUALS_K_OVER_FOUR_BOUNDED_THEOREM_NOTE_2026-09-25.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_a_crystal_of_missing_records_does_not_stretch_the_walk_along_every_axis_a_long_wave_keeps_speed_one_or_stops_bounded_theorem_note_2026-09-28"
AXIOM_NEEDLES = (
    "Records form.",
    "A site never carries more than one record; records are permanent.",
    "A site with no record cannot be read.",
)
LANDED135 = (
    "`S_a = (T_a − T_a⁻¹)/(2i)`",
    "`H = Σ_aσ_aS_a`",
)

MUTATION_GATE = {
    "landed_quote_forged": "A",
    "reduction_forged": "B",
    "period2_forged": "C",
    "table_forged": "D",
    "flat_band_forged": "E",
    "relabelling_forged": "F",
    "vacancy_matrix_forged": "R",
    "claim_transition_injected": "G",
    "claim_classical_name_in_theorem": "G",
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
I_ = sp.I
SIG = (sp.Matrix([[0, 1], [1, 0]]), sp.Matrix([[0, -I_], [I_, 0]]), sp.Matrix([[1, 0], [0, -1]]))
LAM = sp.Symbol("lambda")
QS = sp.symbols("q1:4", positive=True)
CORNERS = list(itertools.product((0, 1), repeat=3))
AXIS_SETS = [S for r in (3, 2, 1) for S in itertools.combinations(range(3), r)]
NAMES = {(0, 1, 2): "xyz", (0, 1): "xy", (0, 2): "xz", (1, 2): "yz", (0,): "x", (1,): "y", (2,): "z"}
# exact phases e^{iQ_a} on the unit circle (Pythagorean), so every Bloch matrix has Gaussian-rational entries
PHASES = (sp.Rational(3, 5) + sp.Rational(4, 5) * I_, sp.Rational(5, 13) + sp.Rational(12, 13) * I_, sp.Rational(-7, 25) + sp.Rational(24, 25) * I_)


def cube_h(removed, q):
    """the taste cube: sum_a q_a A_a (x) sigma_a on the corners not in `removed`"""
    keep = [c for c in CORNERS if c not in removed]
    idx = {c: i for i, c in enumerate(keep)}
    h = sp.zeros(2 * len(keep), 2 * len(keep))
    for c in keep:
        for a in range(3):
            d = list(c)
            d[a] ^= 1
            d = tuple(d)
            if d in idx:
                i, j = idx[c], idx[d]
                h[2 * i:2 * i + 2, 2 * j:2 * j + 2] += q[a] * SIG[a]
    return h


def bloch(L, vac, ph, deriv=None):
    """rule R1 on an L^3 cell: the walk H = sum_a sigma_a S_a with the sites in `vac` removed; ph[a] = e^{iQ_a}; deriv = a gives dH/dQ_a"""
    sites = [s for s in itertools.product(range(L), repeat=3) if s not in vac]
    idx = {s: i for i, s in enumerate(sites)}
    n = len(sites)
    h = sp.zeros(2 * n, 2 * n)
    for s in sites:
        for a in range(3):
            t = list(s)
            t[a] += 1
            wrap = t[a] // L
            t[a] %= L
            t = tuple(t)
            if t not in idx:
                continue
            i, j = idx[s], idx[t]
            f = ph[a] ** wrap
            if deriv is not None:
                f = (I_ * wrap * f) if deriv == a else 0
            blk = SIG[a] * f / (2 * I_)
            h[2 * i:2 * i + 2, 2 * j:2 * j + 2] += blk
            h[2 * j:2 * j + 2, 2 * i:2 * i + 2] += blk.H
    return h.applyfunc(sp.expand)


def dm(M):
    return DomainMatrix.from_Matrix(M.applyfunc(sp.expand)).convert_to(QQ_I)


def charpoly_exact(M):
    return sp.Poly([QQ_I.to_sympy(c) for c in dm(M).charpoly()], LAM)


def kernel_dim(M):
    return M.shape[0] - dm(M).rank()


def split(poly):
    """divide out (lambda^2 - q_S^2) for every axis set S, then lambda^2; return multiplicities and the remainder"""
    rem = poly
    ms = {}
    for S in AXIS_SETS + [()]:
        f = sp.Poly(LAM ** 2 - sum(QS[a] ** 2 for a in S), LAM) if S else sp.Poly(LAM ** 2, LAM)
        m = 0
        while rem.degree() >= 2:
            quo, r = sp.div(rem, f)
            if r.is_zero:
                rem, m = quo, m + 1
            else:
                break
        if m:
            ms[S] = m
    return ms, rem


def orbit_key(removed):
    best = None
    for perm in itertools.permutations(range(3)):
        for fl in itertools.product((0, 1), repeat=3):
            img = tuple(sorted(tuple(c[perm[a]] ^ fl[a] for a in range(3)) for c in removed))
            if best is None or img < best:
                best = img
    return best


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms, t135 = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note and len(CLAIM_ID) <= 195, f"the note is present and carries its claim id ({len(CLAIM_ID)} characters) and type")
    na = normalize_text(axioms)
    checks.check("A2", all(normalize_text(s) in na for s in AXIOM_NEEDLES), "the axioms memo: records form, at most one per site and permanent; a site with no record cannot be read")
    quotes = list(LANDED135)
    if mut("landed_quote_forged"):
        quotes[1] = "`H = Σ_aσ_aC_a`"
    checks.check("A3", all(q_ in t135 for q_ in quotes), "landed block 135 states the walk: S_a = (T_a − T_a⁻¹)/(2i), H = Σ_a σ_a S_a")


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    # B1: at the eight species points K in {0,pi}^3 the walk is sum_a cos(K_a) q_a sigma_a; in the parity basis |p> = 8^{-1/2} sum_K e^{-iK.p}|K> this is sum_a q_a X_a (x) sigma_a
    Ks = CORNERS
    Hspec = sp.zeros(16, 16)
    for i, K in enumerate(Ks):
        blk = sum((((-1) ** K[a]) * QS[a] * SIG[a] for a in range(3)), sp.zeros(2, 2))
        if mut("reduction_forged"):
            blk = sum((QS[a] * SIG[a] for a in range(3)), sp.zeros(2, 2))
        Hspec[2 * i:2 * i + 2, 2 * i:2 * i + 2] = blk
    F = sp.zeros(8, 8)
    for i, K in enumerate(Ks):
        for j, p in enumerate(CORNERS):
            F[i, j] = (-1) ** sum(K[a] * p[a] for a in range(3))
    U = sp.kronecker_product(F, sp.eye(2))
    Hpar = (U.T * Hspec * U / 8).applyfunc(sp.expand)
    checks.check("B1", Hpar == cube_h(set(), QS).applyfunc(sp.expand), "in the parity basis the eight species' long waves are the taste cube sum_a q_a X_a (x) sigma_a exactly")
    full = cube_h(set(), QS)
    checks.check("B2", (full * full - sum(x ** 2 for x in QS) * sp.eye(16)).applyfunc(sp.expand) == sp.zeros(16, 16), "on the full cube h(q)^2 = |q|^2: all sixteen long waves move at speed one")
    # B3: a site's component in the species space depends only on its parity class
    comp = lambda x: sp.Matrix([sp.exp(-I_ * sp.pi * sum(K[a] * x[a] for a in range(3))) for K in Ks]).applyfunc(sp.simplify)
    checks.check("B3", comp((0, 0, 0)) == comp((2, 2, 2)) and comp((1, 0, 0)) == comp((3, 2, 0)) and comp((1, 0, 0)) != comp((0, 0, 0)), "a vacancy's constraint on the species space depends only on its parity class (x mod 2)")
    # B4: period 4, exact kernels at Q = 0 and the first-order velocities on them versus the taste cube (direction n = (1,2,3))
    cases = [({(0, 0, 0)}, 0), ({(0, 0, 1), (2, 2, 0)}, 0), ({(0, 0, 0), (1, 0, 0)}, 0), ({(0, 0, 0), (1, 1, 0), (1, 0, 1), (0, 1, 1)}, 0), ({(0, 0, 0), (2, 2, 2)}, 2)]
    n = (1, 2, 3)
    rows = []
    ok_all = True
    for vac, extra in cases:
        cls = set(tuple(x % 2 for x in v) for v in vac)
        H0 = bloch(4, vac, (1, 1, 1))
        kd = kernel_dim(H0)
        Kb = dm(H0).nullspace().to_Matrix().T
        V = sum((n[a] * bloch(4, vac, (1, 1, 1), deriv=a) for a in range(3)), sp.zeros(H0.shape[0], H0.shape[0])) * 4
        G = (Kb.H * Kb).applyfunc(sp.expand)
        Mproj = (G.inv() * (Kb.H * V * Kb)).applyfunc(sp.expand)
        cp = charpoly_exact(Mproj)
        target = sp.Poly(sp.expand(cube_h(cls, n).charpoly(LAM).as_expr() * LAM ** extra), LAM)
        ok = kd == 2 * (8 - len(cls)) + extra and sp.expand(cp.as_expr() - target.as_expr()) == 0
        ok_all &= ok
        rows.append(f"{sorted(vac)}: classes {len(cls)}, kernel {kd}, velocity charpoly {'=' if ok else '!='} taste cube{' x lambda^2' if extra else ''}")
    for r in rows:
        print("   " + r)
    checks.check("B4", ok_all, "period 4: the Q = 0 kernel is the constrained taste space (plus two exact zero modes for two vacancies of one class) and the first-order velocity is the taste cube's")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    s2 = [(1 - sp.re(p)) / 2 for p in PHASES]
    if mut("period2_forged"):
        s2 = [1 - sp.re(p) ** 2 for p in PHASES]
    reps = sorted(set(orbit_key(set(R)) for r in range(8) for R in itertools.combinations(CORNERS, r)), key=lambda t: (len(t), t))
    ok = True
    for rep in reps:
        cp = charpoly_exact(bloch(2, set(rep), PHASES))
        tp = sp.Poly(sp.expand(cube_h(set(rep), QS).charpoly(LAM).as_expr()), LAM)
        coeffs = [sp.expand(c.subs({QS[a]: sp.sqrt(s2[a]) for a in range(3)})) for c in tp.all_coeffs()]
        ok &= [sp.simplify(x - y) for x, y in zip(cp.all_coeffs(), coeffs)] == [0] * len(coeffs)
    checks.check("C1", ok and len(reps) == 21, f"period 2: at the wave number with phases (3+4i)/5, (5+12i)/13, (-7+24i)/25 the band structure is the taste cube with q_a = sin(Q_a/2), for all {len(reps)} classes of vacancy sets")
    H = bloch(2, {(0, 0, 0)}, (-1, -1, -1))
    ev = {sp.nsimplify(k): v for k, v in H.eigenvals().items()}
    checks.check("C2", ev == {sp.sqrt(3): 6, -sp.sqrt(3): 6, 0: 2}, f"period 2, one vacancy: at Q = (pi,pi,pi) the band top sqrt(3) survives (eigenvalues {ev})")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    axis_ok = True
    table = {}
    exceptions = {}
    for r in range(8):
        for R in itertools.combinations(CORNERS, r):
            R = set(R)
            for a in range(3):
                e = [0, 0, 0]
                e[a] = 1
                if mut("table_forged"):
                    e[(a + 1) % 3] = 1
                h = cube_h(R, e)
                axis_ok &= (h ** 3 - h) == sp.zeros(*h.shape)
            ms, rem = split(sp.Poly(sp.expand(cube_h(R, QS).charpoly(LAM).as_expr()), LAM))
            key = orbit_key(R)
            if rem.degree() > 0:
                exceptions.setdefault(key, []).append((R, rem))
            else:
                table.setdefault(key, ms)
    checks.check("D1", axis_ok, "all 256 corner sets: along every axis h^3 = h, so every long-wave speed along an axis is exactly 1 or 0")
    n_exc = sum(len(v) for v in exceptions.values())
    checks.check("D2", n_exc == 24 and len(exceptions) == 1 and len(table) == 20, f"of the 255 sets that leave a corner, 231 factor into lambda^(2z) prod (lambda^2 - q_S^2)^(m_S) ({len(table)} classes); {n_exc} sets in {len(exceptions)} class do not")
    for key, ms in sorted(table.items(), key=lambda t: (len(t[0]), t[0])):
        print(f"   removed {len(key)} {key}: " + ", ".join(f"{NAMES.get(S, 'frozen')} x{m}" for S, m in ms.items()))
    (key, lst), = exceptions.items()
    R, rem = lst[0]
    keep = [c for c in CORNERS if c not in R]
    print(f"   exceptional class: removed {key}; e.g. remaining corners {keep}; factor {sp.factor(rem.as_expr())}")
    # D3: its group speeds at q = (1,2,3) for the representative orientation (remaining corners 011, 100, 110, 111)
    Rrep = {(0, 0, 0), (0, 0, 1), (0, 1, 0), (1, 0, 1)}
    x = sp.Symbol("x", positive=True)
    quart = sp.expand(sp.factor_list(cube_h(Rrep, QS).charpoly(LAM).as_expr())[1][0][0])
    roots = sp.solve(quart.subs(LAM, sp.sqrt(x)), x)
    speeds = []
    for rt in roots:
        g = sum(sp.diff(rt, v) ** 2 for v in QS) / (4 * rt)
        speeds.append(sp.radsimp(sp.simplify(g.subs({QS[0]: 1, QS[1]: 2, QS[2]: 3}))))
    expect = {sp.Rational(13, 20) - 3 * sp.sqrt(5) / 20, sp.Rational(13, 20) + 3 * sp.sqrt(5) / 20}
    checks.check("D3", sp.expand(quart - (LAM ** 4 - (QS[0] ** 2 + QS[1] ** 2 + QS[2] ** 2) * LAM ** 2 + QS[0] ** 2 * QS[1] ** 2)) == 0 and set(sp.nsimplify(s) for s in speeds) == expect and all(sp.simplify(s - 1) < 0 for s in speeds),
                 f"the exceptional class: lambda^4 - |q|^2 lambda^2 + q1^2 q2^2 = 0; at q = (1,2,3) the squared group speeds are {sorted(speeds, key=sp.default_sort_key)}, both below one")
    # D4: everything frozen exactly when the remaining corners are pairwise non-adjacent; the fewest classes that do it is four
    frozen_sizes = []
    for r in range(8):
        for R in itertools.combinations(CORNERS, r):
            if cube_h(set(R), QS) == sp.zeros(2 * (8 - r), 2 * (8 - r)):
                frozen_sizes.append(r)
    checks.check("D4", min(frozen_sizes) == 4 and frozen_sizes.count(4) == 2, f"every long wave is frozen only when the remaining corners are pairwise non-adjacent; the fewest occupied classes that do it is {min(frozen_sizes)} (the two sublattices' four classes)")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    cases = [({(0, 0, 0)}, 2), ({(0, 0, 0), (2, 2, 2)}, 4), ({(0, 0, 0), (2, 2, 1)}, 0), ({(0, 0, 0), (1, 1, 0), (1, 0, 1), (0, 1, 1)}, 8)]
    if mut("flat_band_forged"):
        cases[1] = ({(0, 0, 0), (2, 2, 2)}, 2)
    ok = True
    for vac, want in cases:
        kd = kernel_dim(bloch(4, vac, PHASES))
        print(f"   period 4, vacancies {sorted(vac)}: exact zero modes at the generic wave number: {kd} (sublattice imbalance x 2 = {want})")
        ok &= kd == want
    checks.check("E1", ok, "period 4 at a generic wave number: the exact zero-energy states number twice the sublattice imbalance (flat bands); a balanced pair has none")
    base = []
    dil = []
    for K in itertools.product((1, -1), repeat=3):
        base.append(kernel_dim(bloch(3, set(), K)))
        dil.append(kernel_dim(bloch(3, {(0, 0, 0)}, K)))
    checks.check("E2", base == [2] * 8 and dil == [0] * 8, f"period 3: each species point carries its zero-energy doublet ({base}); one vacancy per cell removes all eight ({dil})")


# ============================================================================================ family F
def family_f(checks: Checks) -> None:
    ok = True
    for nper in (2, 3, 4, 6):
        N = 12
        recs = [x for x in range(N) if x % nper != 0]
        R = len(recs)
        # rule R3: the hop goes to the nearest record along the axis
        S3 = sp.zeros(R, R)
        for j in range(R):
            S3[j, (j + 1) % R] += sp.Rational(1, 2) / I_
            S3[(j + 1) % R, j] -= sp.Rational(1, 2) / I_
        # undiluted walk on a ring of R sites
        S0 = sp.zeros(R, R)
        for j in range(R):
            t = (j + 1) % R
            if mut("relabelling_forged") and j == 0:
                continue
            S0[j, t] += sp.Rational(1, 2) / I_
            S0[t, j] -= sp.Rational(1, 2) / I_
        spacing = sp.Rational(N, R)
        ok &= S3 == S0 and spacing == sp.Rational(nper, nper - 1)
        print(f"   one vacancy per {nper} sites: the walk on the {R} records is the undiluted walk; mean spacing {spacing}")
    checks.check("F1", ok, "rule R3 is a relabelling: in record labels the walk is unchanged, so in grid units its long waves move at the mean spacing n/(n-1) > 1")


# ============================================================================================ family R
def family_r(checks: Checks) -> None:
    L = 4
    Nsites = L ** 3
    H = bloch(L, set(), (1, 1, 1))
    n = H.shape[0]
    E = sp.Rational(1, 2) + sp.Rational(1, 3) * I_
    G = dm(E * sp.eye(n) - H).inv().to_Matrix()
    s2 = {m: sp.nsimplify(sp.sin(sp.pi * sp.Rational(2, L) * m) ** 2) for m in range(L)}

    def gbar(En):
        return sum((1 / (En ** 2 - (s2[a] + s2[b] + s2[c])) for a in range(L) for b in range(L) for c in range(L)), sp.Integer(0)) / Nsites

    G00 = G[0:2, 0:2]
    Gvv = G[2 * 21:2 * 21 + 2, 2 * 21:2 * 21 + 2]
    if mut("vacancy_matrix_forged"):
        G00 = G00 + sp.Matrix([[sp.Rational(1, 100), 0], [0, -sp.Rational(1, 100)]])
    ok1 = G00[0, 1] == 0 and G00[1, 0] == 0 and sp.simplify(G00[0, 0] - E * gbar(E)) == 0 and sp.simplify(G00[1, 1] - E * gbar(E)) == 0 and (Gvv - G[0:2, 0:2]).applyfunc(sp.simplify) == sp.zeros(2, 2)
    checks.check("R1", ok1, "4^3 torus at E = 1/2 + i/3: the walk's resolvent at a site is E gbar(E) times the coin identity, gbar(E) = mean over k of 1/(E^2 - eps_k^2), the same at every site")
    Hd = bloch(L, {(0, 0, 0)}, (1, 1, 1))
    Gd = dm(E * sp.eye(n - 2) - Hd).inv().to_Matrix()
    Gs = G[2:, 2:] - G[2:, 0:2] * G[0:2, 0:2].inv() * G[0:2, 2:]
    checks.check("R2", (Gd - Gs).applyfunc(sp.simplify) == sp.zeros(n - 2, n - 2), "removing one site (rule R1) changes the resolvent by G T G exactly, with the local coin-scalar T = -(E gbar(E))^-1")
    pair = []
    for sv in ([sp.Integer(1), sp.Integer(0), sp.Integer(0)], [sp.Rational(1, 3)] * 3):
        e2 = sum(sv, sp.Integer(0))
        v2 = sum((x * (1 - x) for x in sv), sp.Integer(0)) / e2
        pair.append((e2, v2))
    ok3 = pair[0][0] == pair[1][0] == 1 and pair[0][1] == 0 and pair[1][1] == sp.Rational(2, 3)
    checks.check("R3", ok3, f"two waves of bare energy 1 with squared speeds {pair[0][1]} and {pair[1][1]}: a shift that depends only on the bare energy moves them alike, which the free-particle rule's law forbids")
    r1 = sp.simplify(E ** 2 * gbar(E))
    E2 = 1 + sp.Rational(1, 3) * I_
    r2 = sp.simplify(E2 ** 2 * gbar(E2))
    checks.check("R4", sp.simplify(r1 - r2) != 0, f"the relative shift p/(E^2 gbar(E)) is not one number: E^2 gbar = {sp.nsimplify(r1)} at E = 1/2 + i/3 and {sp.nsimplify(r2)} at E = 1 + i/3, where the frame needs a constant")


# ============================================================================================ family G
FENCES = (
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
    "nothing is adopted and no gravitational claim is made.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
    "time dilation", "equivalence principle", "general relativity", "horizon", "gravitational wave", "gravitational lens",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at four vacancies."}
CLASSICAL_NAMES = ("Newton", "Weyl", "Noether", "Dirac", "Lorentz", "Einstein", "Hilbert", "Deser", "Fock", "Taylor", "Fourier", "Euler", "Lagrange", "Laplace",
                   "Poisson", "Gauss", "Planck", "Green", "Hamilton", "Riemann", "Christoffel", "Lie", "Levi-Civita", "Schur", "Fermi", "Chebyshev", "Fermat", "Snell",
                   "Burgers", "Hopf", "Jacobi", "Ward", "Takahashi", "Wilson", "Kepler", "Bessel", "Liouville", "Paley", "Wiener", "Bloch", "Cauchy", "Berry", "Zak", "Hellmann", "Feynman",
                   "Lieb", "Kogut", "Susskind", "Hadamard", "Walsh", "Pythagoras", "Pythagorean")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_g(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T1", phrase + "\n\n## Theorem T1", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1 —", "## Theorem T1 (after Lieb) —", 1)
    norm = normalize_text(text)
    checks.check("G1", all(normalize_text(f) in norm for f in FENCES), "the note carries the three fence sentences verbatim")
    hits = [p_ for p_ in FORBIDDEN if p_ in text]
    checks.check("G2", not hits, f"the note contains no forbidden phrase ({len(hits)} hits)")
    src = Path(__file__).read_text(encoding="utf-8")
    body = src.split(SCAN_MARKER)[0]
    float_hits = re.findall(r"(?<![\w.])\d+\.\d+(?![\w.])|\bfloat\(|\.evalf\(|\bN\(", body)
    checks.check("G3", not float_hits, f"runner source: no floating-point literal or conversion call ({len(float_hits)} hits)")
    sections = re.split(r"^## ", text, flags=re.M)
    offenders = []
    for sec in sections[1:]:
        title = sec.split("\n", 1)[0].strip()
        if any(title.startswith(a_) for a_ in ALLOWED_NAME_SECTIONS):
            continue
        for nm in CLASSICAL_NAMES:
            if re.search(r"\b" + re.escape(nm) + r"\b", sec):
                offenders.append((title[:40], nm))
    offenders += [("front matter", nm) for nm in CLASSICAL_NAMES if re.search(r"\b" + re.escape(nm) + r"\b", sections[0])]
    checks.check("G4", not offenders, f"the authors' names appear only under Prior art, Imports, the Premises and the Review record ({len(offenders)} offenders)")


# ============================================================================================ family H
N5_LINES = (
    "per_element: executed - the taste-cube reduction of the eight species' long waves",
    "per_site: executed - period-4 kernels and first-order velocities for five vacancy sets; period 3 kernels at all eight species points",
    "per_mode: executed - all 256 corner sets: axis speeds, factorisation of every characteristic polynomial, the exceptional class",
    "per_block: executed - period 2 at a generic wave number for all 21 classes; flat bands at a generic wave number for period 4; one vacancy's exact scalar T-matrix on the 4^3 torus",
    "lattice_wide: checked and not executed - random vacancy patterns beyond first order in the concentration; periods whose lattice is not in 2Z^3 other than period 3; rules other than R1 and R3; the member's coupling to a diluted walk",
)


def family_h(checks: Checks) -> None:
    for line in N5_LINES:
        print(line)
    checks.check("H1", len(N5_LINES) == 5, "the five N5 resolution lines are printed")


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
    for p_ in AUDIT_INPUT_PATHS:
        print(f"  {p_}")
    texts = [Path(ROOT, p_).read_text(encoding="utf-8") if Path(ROOT, p_).exists() else "" for p_ in AUDIT_INPUT_PATHS]
    checks = Checks()
    family_a(checks, texts)
    family_b(checks)
    family_c(checks)
    family_d(checks)
    family_e(checks)
    family_f(checks)
    family_r(checks)
    family_g(checks, texts[0])
    family_h(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print(f"scope: under rule R1 a crystal of sites with no record acts on the walk's eight species as the taste cube with corners removed; along every axis a long wave keeps speed one or stops; waves are removed, confined to lines or planes, or frozen, and only one class of 24 sets slows oblique waves; under R3 the walk is relabelled; random vacancies at first order in the concentration shift energies by a function of the bare energy alone and damp the waves; the supervisor's own derivation, unrefereed; nothing adopted ({time.time() - T0:.0f}s)")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
