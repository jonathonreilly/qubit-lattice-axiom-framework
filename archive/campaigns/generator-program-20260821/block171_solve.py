#!/usr/bin/env python3
"""Block 171 (B1) SOLVE -- the generator trilemma, the class map, K1-K3, F8.

WHAT THIS IS.  The OS/reflection-positivity route is closed by theorem.  The
program now targets a GENERATOR: a record-conditioned law
`P(next record class | trail)`.  This solve runs the trilemma -- does ANY weight
built from the FULL quotient object `Q` satisfy simultaneously

  (i)   probability well-formedness (PSD / normalizable, exact),
  (ii)  trail/record sensitivity,
  (iii) the anti-shim transport standard,

-- then declares the record alphabet and class map, runs K1/K2/K3, runs the F8
factorization check, and emits the B2/B3 profile table.

DISCIPLINE.  Exact sympy rationals ONLY.  No float anywhere (gated).  No
`nsimplify` anywhere (gated by source grep of this file).  Every inertia triple
is printed in the `(n_+, n_-, n_0)` order of `b165.real_symmetric_inertia` with
the convention inline.  `T_phys >= 6` (the 12x4 fixture) is the BENCH for every
transport-sensitivity measurement; 8x4 (`T_phys = 4`) appears only as a
DISCLOSED cross-check.  The FLAT carrier is a NULL FIXTURE and nothing is
benched there -- and this block measures that the LANDED graded carrier is a
SECOND null fixture for every site profile.

IMPORTS, not re-derivations.  The committed fixture, region pin, carrier map,
descent, pairing, quotient, inertia routine, holonomy-dial connection
constructor and quotient-Gaussian moment machinery are IMPORTED through the
landed Block 170 runner and its import chain (b169 -> b168 -> b167 -> b166 ->
b165 -> b164 -> b163 -> ... -> b105).  Nothing in that chain is modified.

THIS BLOCK'S OWN OBJECTS, disclosed as premise-class probes and not framework
objects: the x-inhomogeneous probe carrier `xgraded`; the record-slice (RS)
compression scope; the weight constructions W9 and W10; the two generator
wirings G-A and G-B.

Every negative here is NON-SUPPLY within this pairing/quotient formalism and
never metaphysical necessity (CYCLE913, carried verbatim).
"""
from __future__ import annotations

import sys
import time
from pathlib import Path

import sympy as sp
from sympy.polys.matrices import DomainMatrix

R = sp.Rational
I = sp.I

ROOT = Path(
    "/Users/jonBridger/Projects/Physics-baremetal-probes/"
    ".claude/worktrees/gravity-toe-lane-work-427b0b"
)
SCRIPTS = ROOT / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import admissibility_dirac_kahler_closure_audit_two_2026_08_21 as b170  # noqa

b169 = b170.b169
b168 = b170.b168
b166 = b170.b166
b165 = b170.b165

SX, ST, MASS = b170.SX, b170.ST, b170.MASS
GRE, GIM = b170.GRE, b170.GIM
herm = b170.herm
is_zero = b170.is_zero
inertia = b170.hermitian_inertia
tri = b170.tri

START = time.time()
NUMERALS: list = []
LOG: list = []
STEP = [0]


def rec(value):
    """Every reported numeral passes the no-float gate through here."""
    NUMERALS.append(value)
    return value


def check(statement: str, condition: bool) -> bool:
    STEP[0] += 1
    LOG.append((STEP[0], statement, bool(condition)))
    print(f"[{STEP[0]:02d}] [{'PASS' if condition else 'FAIL'}] {statement}")
    return bool(condition)


def say(text: str = "") -> None:
    print(text)


def exact_inv(M: sp.Matrix) -> sp.Matrix:
    """EXACT inverse over the Gaussian rationals, no float and no simplifier.

    sympy's `inv(method="LU")` is used everywhere in the landed chain, but on
    the holonomy-dialled action (entries in Q(i) with a nonzero real part in the
    temporal coupling) its intermediate fractions blow up and it does not
    terminate at 24x24.  `DomainMatrix` does the same elimination inside the
    QQ_I domain.  GATED below against the landed LU route on the committed
    action, entry for entry.
    """
    return DomainMatrix.from_Matrix(M).to_field().inv().to_Matrix()


# ---------------------------------------------------------------------------
# CARRIERS.  Two NULL fixtures and one probe bench.
# ---------------------------------------------------------------------------
def volume(mode: str, t: int, x: int):
    if mode == "flat":
        return sp.Integer(1)
    if mode == "graded":                       # the LANDED b166 carrier
        return R(1 + (3 * t + 5 * x) % 5, 3) + R(1, 2)
    if mode == "xgraded":                      # THIS BLOCK'S probe carrier
        return R(1 + (3 * t + 2 * x) % 5, 3) + R(1, 2)
    raise ValueError(mode)


def field(fx, c: int, sigma, mode: str, records: dict = None) -> dict:
    """The carrier field, with the trail's RECORDS written in as pins.

    A record at cell `(t, x)` with class `s` sets that cell's shear to `s`;
    unrecorded free cells stay at the carrier `sigma`; the region pin holds
    `sigma = 0` on the two links incident to the fixed slice `c`.
    """
    records = records or {}
    pinned = {(c - 1) % fx.PHYS_T, c % fx.PHYS_T}
    out = {}
    for (t, x) in fx.CELLS:
        if t in pinned:
            shear = sp.Integer(0)
        else:
            shear = sp.sympify(records.get((t, x), sigma))
        out[(t, x)] = (shear, volume(mode, t, x))
    return out


class Site:
    """One extent, with the committed objects and the two dial rebuilds."""

    def __init__(self, tag: str, cover_t: int, lx: int):
        self.bench = b170.Bench(tag, cover_t, lx)
        b = self.bench
        self.tag, self.lx, self.c, self.T, self.N = tag, lx, b.c, b.T, b.N
        self.fx = b.fx
        self.free_levels = tuple(
            t for t in range(self.T) if t not in {(self.c - 1) % self.T, self.c}
        )
        self.tstar = self.free_levels[-1]
        # THE HOLONOMY DIALS, built by the committed pluggable constructor.
        holo_t = b168.connection_gen(self.fx, I * SX, GRE + I * GIM, b165.ET)
        holo_x = b168.connection_gen(self.fx, GRE + I * GIM, I * ST, b165.ET)
        self.Q_holo_t = sp.expand(MASS * b.Hq + b165.dense(
            self.fx.quotient_connection(holo_t[(0, 0)], b.hodge), self.N,
            self.N))
        self.Q_holo_x = sp.expand(MASS * b.Hq + b165.dense(
            self.fx.quotient_connection(holo_x[(0, 0)], b.hodge), self.N,
            self.N))
        self._cache: dict = {}

    def sub(self, sigma=R(3, 5), sx=R(3, 5), st=sp.Integer(0),
            m=sp.Integer(1), mode="xgraded", records=None) -> dict:
        s = b166.carrier_substitution(
            self.fx, field(self.fx, self.c, sigma, mode, records))
        s[SX] = sp.sympify(sx)
        s[ST] = sp.sympify(st)
        s[MASS] = sp.sympify(m)
        return s

    def rows(self, level: int) -> list:
        return [self.lx * (level % self.T) + x for x in range(self.lx)]

    def blk(self, M, level: int) -> sp.Matrix:
        r = self.rows(level)
        return sp.Matrix(self.lx, self.lx, lambda i, j: M[r[i], r[j]])


# ---------------------------------------------------------------------------
# THE ENVIRONMENT: a fully substituted action plus its derived Grams.
# ---------------------------------------------------------------------------
class Env:
    """One numeric evaluation point: `Q` and the Grams the battery needs.

    EVERY Gram is assembled at BLOCK scope -- only the `L_x x L_x` block the
    class map lives on is ever formed.  No `N x N` matrix product is taken, so
    the cost per evaluation point is two exact `N x N` inverses and `O(L_x^2 N)`
    rational operations, and nothing here depends on a float or a simplifier.
    """

    def __init__(self, site: Site, Q: sp.Matrix, label: str):
        self.site, self.label = site, label
        self.Q = sp.expand(Q)
        self.S = herm(self.Q)
        self.A = sp.expand(self.Q - self.S)
        self._inv: dict = {}
        self._c: dict = {}

    def inv(self, which: str) -> sp.Matrix:
        if which not in self._inv:
            M = self.Q if which == "Q" else self.S
            self._inv[which] = exact_inv(M)
        return self._inv[which]

    def gram(self, name: str) -> sp.Matrix:
        """The FULL N x N Gram -- used only by the identity exhibits."""
        Q, S, A = self.Q, self.S, self.A
        if name == "W1":
            return S
        if name == "W2":
            return herm(self.inv("S"))
        if name == "W5":
            return sp.expand(A.H * A)
        if name == "W6":
            return sp.expand(Q.H * Q)
        if name == "W7":
            return sp.expand(S + A.H * A)
        if name == "W9":
            Qi = self.inv("Q")
            return sp.expand((Qi + Qi.H) / 2)
        if name == "W10":
            return sp.expand(Q.H * self.inv("S") * Q)
        raise ValueError(name)

    def block(self, name: str, level: int) -> sp.Matrix:
        key = (name, level % self.site.T)
        if key in self._c:
            return self._c[key]
        s, Q, S, A = self.site, self.Q, self.S, self.A
        r, n, lx = s.rows(level), s.N, s.lx

        def take(M):
            return sp.Matrix(lx, lx, lambda i, j: M[r[i], r[j]])

        def hpart(M):                          # herm(M) restricted to the block
            return sp.Matrix(lx, lx, lambda i, j:
                             (M[r[i], r[j]] + sp.conjugate(M[r[j], r[i]])) / 2)

        def dagger_gram(X):                    # (X^dag X)[r_i, r_j]
            cols = [[X[p, r[i]] for p in range(n)] for i in range(lx)]
            return sp.Matrix(lx, lx, lambda i, j: sum(
                (sp.conjugate(cols[i][p]) * cols[j][p] for p in range(n)),
                sp.Integer(0)))

        if name == "W1":
            B = take(S)
        elif name == "W2":
            B = hpart(self.inv("S"))
        elif name == "W5":
            B = dagger_gram(A)
        elif name == "W6":
            B = dagger_gram(Q)
        elif name == "W7":
            B = take(S) + dagger_gram(A)
        elif name == "W9":
            B = hpart(self.inv("Q"))
        elif name == "W10":                    # Q^dag S^{-1} Q on the block
            Si = self.inv("S")
            Y = [[sum((Si[p, q] * Q[q, r[j]] for q in range(n)), sp.Integer(0))
                  for j in range(lx)] for p in range(n)]
            B = sp.Matrix(lx, lx, lambda i, j: sum(
                (sp.conjugate(Q[p, r[i]]) * Y[p][j] for p in range(n)),
                sp.Integer(0)))
        else:
            raise ValueError(name)
        B = sp.Matrix(lx, lx, lambda i, j: sp.expand(B[i, j]))
        self._c[key] = B
        return B

    def profile(self, name: str, level: int):
        """P(a) = tr(G . Pi_a) / tr(G) on the site partition of `level`."""
        B = self.block(name, level)
        trace = sp.expand(sum(B[i, i] for i in range(self.site.lx)))
        if trace == 0:
            return None                        # 0/0 -- support failure
        return tuple(sp.cancel(B[i, i] / trace)
                     for i in range(self.site.lx))


# ---------------------------------------------------------------------------
say("=" * 78)
say("BLOCK 171 (B1) SOLVE -- the generator trilemma")
say("INERTIA CONVENTION: every triple below is (n_+, n_-, n_0), the order of")
say("b165.real_symmetric_inertia, printed inline as (a,b,c)(n+,n-,n0)[b165].")
say("BENCH = 12x4 (T_phys = 6).  8x4 (T_phys = 4) is a DISCLOSED CROSS-CHECK.")
say("Exact rationals only; no float; no nsimplify.  CYCLE913 on every negative.")
say("=" * 78)

SITES = {}
for tag, ct, lx in (("12x4", 12, 4), ("8x4", 8, 4)):
    SITES[tag] = Site(tag, ct, lx)
BENCH, XCHK = SITES["12x4"], SITES["8x4"]

check("import chain landed through the Block 170 runner (b169 present)",
      b170.PARENT_IMPORT_LANDED and b169 is not None)
check("bench is T_phys = 6 (12x4) and cross-check is T_phys = 4 (8x4)",
      BENCH.T == 6 and XCHK.T == 4)
check("EXACT-INVERSE GATE: the DomainMatrix inverse used here agrees with "
      "the landed sp.inv(method='LU') route entry for entry on the committed "
      "action at both extents",
      all(is_zero(exact_inv(sp.expand(s.bench.Q.subs(s.sub())))
                  - sp.expand(s.bench.Q.subs(s.sub())).inv(method="LU"))
          for s in SITES.values()))
check("holonomy dial reproduces the committed action at the committed "
      "coupling, entry for entry, both extents",
      all(is_zero(sp.expand(s.Q_holo_t.subs({GRE: 0, GIM: ST})) - s.bench.Q)
          and is_zero(sp.expand(s.Q_holo_x.subs({GRE: 0, GIM: SX}))
                      - s.bench.Q)
          for s in SITES.values()))

# ---------------------------------------------------------------------------
say("")
say("--- SECTION 1.  THE STRUCTURAL THEOREMS (symbolic, both extents) -------")
# ---------------------------------------------------------------------------
BSYMS = {}
for tag, s in SITES.items():
    BSYMS[tag] = set(b166.free_shears(s.fx, s.c))
check("landed record alphabet size = 2 L_x (T_phys - 2): 16 free shears at "
      "12x4, 8 at 8x4",
      len(BSYMS["12x4"]) == 16 and len(BSYMS["8x4"]) == 8)

# S1 -- slice c is a DIRECT SUMMAND of Q on the region, symbolically.
S1 = {}
for tag, s in SITES.items():
    Qr = sp.expand(s.bench.Q.subs({ST: 0}))
    rowsc = set(s.rows(s.c))
    off = all(Qr[i, j] == 0 and Qr[j, i] == 0
              for i in rowsc for j in range(s.N) if j not in rowsc)
    S1[tag] = off
check("THEOREM S1: at s_t = 0 on the region, slice c is a DIRECT SUMMAND of "
      "Q -- Q[c,k] = Q[k,c] = 0 for every k != c, SYMBOLICALLY in all free "
      "symbols, both extents", all(S1.values()))

S2 = {}
for tag, s in SITES.items():
    Qcc = sp.expand(s.bench.Q.subs({ST: 0}))
    blk = s.blk(Qcc, s.c)
    syms = set().union(*[sp.expand(blk[i, j]).free_symbols
                         for i in range(s.lx) for j in range(s.lx)])
    S2[tag] = (syms & BSYMS[tag], syms)
check("THEOREM S2: Q[c,c] contains NO free-shear symbol at all -- the record "
      "is absent from the slice-c block, symbolically, both extents",
      all(not v[0] for v in S2.values()))
for tag in ("12x4", "8x4"):
    say(f"      {tag}: Q[c,c] symbols = "
        f"{sorted(str(x) for x in S2[tag][1])}")

check("THEOREM S3: herm(Q) = m . quotient(H) carries NO connection symbol "
      "(s_t, s_x absent), symbolically, both extents",
      all(not ({SX, ST} & herm(s.bench.Q).free_symbols)
          for s in SITES.values()))
check("THEOREM S4: A = Q - herm(Q) is exactly anti-Hermitian and carries BOTH "
      "connection symbols, both extents",
      all(is_zero(sp.expand(s.bench.Q - herm(s.bench.Q))
                  + sp.expand(s.bench.Q - herm(s.bench.Q)).H)
          and {SX, ST} <= sp.expand(s.bench.Q - herm(s.bench.Q)).free_symbols
          for s in SITES.values()))
say("      COROLLARY (the SC obstruction): Q = Q_cc (+) Q_rest on the region,")
say("      so f(Q)_cc = f(Q_cc) for every f built from Q, Q^dag, inverses and")
say("      sums/products; and Q_cc is record-free by S2.  EVERY weight got by")
say("      compressing such an f to slice c is RECORD-BLIND BY THEOREM.")

# The corollary, exhibited numerically-exactly at the bench.
env_sc = Env(BENCH, BENCH.bench.Q.subs(BENCH.sub()), "bench")
Qcc = BENCH.blk(env_sc.Q, BENCH.c)
Qcc_inv_h = sp.expand((Qcc.inv(method="LU") + Qcc.inv(method="LU").H) / 2)
check("COROLLARY exhibited: herm(Q^{-1})_cc == herm((Q_cc)^{-1}) entry for "
      "entry at the bench (12x4)",
      is_zero(BENCH.blk(env_sc.gram("W9"), BENCH.c) - Qcc_inv_h))

# ---------------------------------------------------------------------------
say("")
say("--- SECTION 2.  THE NULL FIXTURES ------------------------------------")
# ---------------------------------------------------------------------------
for mode in ("flat", "graded", "xgraded"):
    e = Env(BENCH, BENCH.bench.Q.subs(BENCH.sub(mode=mode)), mode)
    p_c = e.profile("W1", BENCH.c)
    p_t = e.profile("W9", BENCH.tstar)
    rec(p_c)
    rec(p_t)
    say(f"      carrier {mode:8s}  SC profile {p_c}")
    say(f"      carrier {mode:8s}  RS profile(W9) {p_t}")
UNIF = tuple(R(1, BENCH.lx) for _ in range(BENCH.lx))
check("NULL FIXTURE 1 (flat carrier): every site profile is EXACTLY uniform",
      Env(BENCH, BENCH.bench.Q.subs(BENCH.sub(mode="flat")), "f"
          ).profile("W1", BENCH.c) == UNIF)
check("NULL FIXTURE 2, NEW: the LANDED graded carrier is x-HOMOGENEOUS "
      "((3t+5x) mod 5 = 3t mod 5), so its site profiles are EXACTLY uniform "
      "too -- a second null fixture, and nothing may be benched there",
      Env(BENCH, BENCH.bench.Q.subs(BENCH.sub(mode="graded")), "g"
          ).profile("W9", BENCH.tstar) == UNIF)
check("PROBE CARRIER xgraded is NON-uniform at both scopes (so the bench is "
      "not empty)",
      Env(BENCH, BENCH.bench.Q.subs(BENCH.sub()), "x"
          ).profile("W9", BENCH.tstar) != UNIF)
check("PROBE CARRIER xgraded stays INSIDE the positive region: the committed "
      "half-support pairing [rQ]_{S,S} is PSD at both extents",
      all(inertia(sp.expand(s.bench.form.subs(s.sub())), "form")[1] == 0
          for s in SITES.values()))
for tag, s in SITES.items():
    t_form = inertia(sp.expand(s.bench.form.subs(s.sub())), "form")
    t_herm = inertia(herm(sp.expand(s.bench.Q.subs(s.sub()))), "S")
    say(f"      {tag}: [rQ]_(S,S) = {tri(t_form)}   herm(Q) = {tri(t_herm)}")

# ---------------------------------------------------------------------------
say("")
say("--- SECTION 3.  THE CLASS MAP (T2, part 1) ---------------------------")
# ---------------------------------------------------------------------------
def class_projectors(site: Site, level: int) -> list:
    out = []
    for a in range(site.lx):
        P = sp.zeros(site.lx, site.lx)
        P[a, a] = 1
        out.append(P)
    return out


res_ok, orth_ok, idem_ok = True, True, True
for tag, s in SITES.items():
    Pis = class_projectors(s, s.tstar)
    total = sp.zeros(s.lx, s.lx)
    for P in Pis:
        total += P
        idem_ok &= is_zero(sp.expand(P * P - P)) and is_zero(P - P.H)
    res_ok &= is_zero(total - sp.eye(s.lx))
    for a in range(s.lx):
        for b in range(a + 1, s.lx):
            orth_ok &= is_zero(sp.expand(Pis[a] * Pis[b]))
check("CLASS MAP CM-SITE {Pi_a} (the L_x site projectors of the record "
      "slice): each Pi_a is Hermitian and idempotent, EXACTLY", idem_ok)
check("CM-SITE is mutually ORTHOGONAL, EXACTLY", orth_ok)
check("CM-SITE is a RESOLUTION OF THE IDENTITY, sum_a Pi_a = 1, EXACTLY at "
      "BOTH extents (|A| = L_x = 4 >= 3, so the coarse-graining leg is not "
      "vacuous)", res_ok)
SIGMA_CLASSES = (sp.Integer(0), R(1, 5), R(2, 5), R(3, 5))
say("      CLASS MAP CM-VALUE (sigma in {0, 1/5, 2/5, 3/5}, b = -nu.sigma/"
    "(1-sigma^2)): NOT a projector partition.  These are cone-membership "
    "values of a CONTINUOUS modulus; no landed operator on the record slice "
    "has them as spectrum, and no orthogonal decomposition is attached.  "
    "DECLARED ABSENT, not measured absent -- a checker refutes this by "
    "exhibiting such an operator.")

# ---------------------------------------------------------------------------
say("")
say("--- SECTION 4.  THE TRILEMMA TABLE (T1) ------------------------------")
say("PRE-REGISTERED EXPECTATIONS are in $S/b171_findings.md section 0 and were")
say("written BEFORE this section ran.  Registered transport-off expectations:")
say("  W1 SAME(thm)  W2 SAME(thm)  W3 SAME  W4 SAME  W5 UNDEFINED(0/0)")
say("  W6 DIFFER  W7 DIFFER  W8 DIFFER  W9 DIFFER  W10 DIFFER")
# ---------------------------------------------------------------------------
GRAMS = ("W1", "W2", "W5", "W6", "W7", "W9", "W10")


def envs_for(site: Site) -> dict:
    b = site.bench
    out = {
        "bench": Env(site, b.Q.subs(site.sub()), "bench"),
        "conn_off": Env(site, b.Q.subs(site.sub(sx=0, st=0)), "conn_off"),
        "sx_1_7": Env(site, b.Q.subs(site.sub(sx=R(1, 7))), "sx_1_7"),
        "st_1_8": Env(site, b.Q.subs(site.sub(st=R(1, 8))), "st_1_8"),
        "sigma_1_5": Env(site, b.Q.subs(site.sub(sigma=R(1, 5))), "sigma_1_5"),
        "mass_3": Env(site, b.Q.subs(site.sub(m=3)), "mass_3"),
    }
    dial = {GRE: R(1, 3), GIM: R(1, 4)}
    out["holo_t"] = Env(site, site.Q_holo_t.subs(site.sub()).subs(dial),
                        "holo_t")
    out["holo_x"] = Env(site, site.Q_holo_x.subs(site.sub()).subs(dial),
                        "holo_x")
    return out


def trails_for(site: Site) -> dict:
    lv = site.free_levels[:-1]                 # every free level before t*
    return {
        "empty": {},
        "A": {(t, 0): sp.Integer(0) for t in lv},
        "B": {(t, 1): sp.Integer(0) for t in lv},
        "C": {(t, 0): R(1, 5) for t in lv},
        "near": {(site.tstar - 1, 0): sp.Integer(0)},
        "far": {(site.free_levels[0], 0): sp.Integer(0)},
    }


TABLE: dict = {}
for tag, s in SITES.items():
    E = envs_for(s)
    TR = trails_for(s)
    trail_env = {k: Env(s, s.bench.Q.subs(s.sub(records=v)), k)
                 for k, v in TR.items()}
    for g in GRAMS:
        row = {}
        for scope, level in (("SC", s.c), ("RS", s.tstar)):
            base = E["bench"].profile(g, level)
            # leg (i): PSD of the compressed block + support
            B = E["bench"].block(g, level)
            herm_ok = is_tri = None
            herm_ok = is_zero(B - B.H)
            trip = inertia(sp.expand(B), f"{g}{scope}") if herm_ok else None
            support_all = all(
                E[k].profile(g, level) is not None
                for k in ("bench", "conn_off", "sx_1_7", "st_1_8",
                          "holo_t", "holo_x"))
            legi = bool(herm_ok and trip is not None and trip[1] == 0
                        and base is not None and support_all
                        and all(p >= 0 for p in base))
            # leg (ii): record sensitivity, exact witnesses
            movers = tuple(k for k in ("A", "B", "C", "near", "far")
                           if trail_env[k].profile(g, level)
                           != trail_env["empty"].profile(g, level))
            legii = bool(movers)
            # leg (iii): the anti-shim battery
            off = E["conn_off"].profile(g, level)
            sxd = E["sx_1_7"].profile(g, level)
            std = E["st_1_8"].profile(g, level)
            hot = E["holo_t"].profile(g, level)
            hox = E["holo_x"].profile(g, level)
            iii = {
                "conn_off": ("undefined" if off is None
                             else ("differ" if off != base else "same")),
                "sx_dial": "differ" if sxd != base else "same",
                "st_dial": "differ" if std != base else "same",
                "holo_t": "differ" if hot != base else "same",
                "holo_x": "differ" if hox != base else "same",
            }
            legiii = (iii["conn_off"] == "differ"
                      and iii["holo_t"] == "differ"
                      and iii["holo_x"] == "differ"
                      and iii["sx_dial"] == "differ")
            row[scope] = {
                "profile": base, "inertia": trip, "hermitian": herm_ok,
                "legi": legi, "legii": legii, "movers": movers,
                "leg iii": iii, "legiii": legiii,
            }
            rec(base)
        TABLE[(tag, g)] = row

NAMES = {
    "W1": "herm(Q) = m.quotient(H)",
    "W2": "herm(herm(Q)^{-1}) -- SIGN-QUENCHED control",
    "W5": "A^dag A  (A = Q - herm(Q))",
    "W6": "Q^dag Q  (polar)",
    "W7": "herm(Q) + A^dag A",
    "W9": "herm(Q^{-1}) = Q^{-1} herm(Q) Q^{-dag}   [own design]",
    "W10": "Q^dag herm(Q)^{-1} Q = herm(Q) + A^dag herm(Q)^{-1} A  [own]",
}
for tag in ("12x4", "8x4"):
    say(f"    ---- extent {tag} "
        f"({'BENCH, T_phys=6' if tag == '12x4' else 'CROSS-CHECK, T_phys=4'})")
    for g in GRAMS:
        for scope in ("SC", "RS"):
            r = TABLE[(tag, g)][scope]
            say(f"      {g:3s} {scope}  i={'P' if r['legi'] else 'F'}"
                f" ii={'P' if r['legii'] else 'F'}"
                f" iii={'P' if r['legiii'] else 'F'}"
                f"  inertia={tri(r['inertia']) if r['inertia'] else 'n/a'}"
                f"  movers={r['movers']}  {r['leg iii']}")
        say(f"           {NAMES[g]}")

# The registered theorem rows, verified as symbolic statements.
check("LEG (iii) ANCHOR, W1: herm(Q)-covariance weights are connection-blind "
      "BY THEOREM (S3) and measure 'same' on ALL FIVE dials at BOTH scopes "
      "and BOTH extents",
      all(set(TABLE[(t, 'W1')][sc]['leg iii'].values()) == {"same"}
          for t in SITES for sc in ("SC", "RS")))
check("LEG (iii) ANCHOR, W2 (sign-quenched): herm(Q)^{-1} is the "
      "connection-off covariance ENTRYWISE at both extents -- the landed "
      "shim exhibit, re-verified here",
      all(is_zero(Env(s, s.bench.Q.subs(s.sub()), "b").gram("W2")
                  - Env(s, s.bench.Q.subs(s.sub(sx=0, st=0)), "o").gram("W2"))
          for s in SITES.values()))
check("LEG (ii) ANCHOR: at SC scope EVERY construction in the battery is "
      "record-blind (no trail moves it), both extents -- S1+S2 in force",
      all(not TABLE[(t, g)]["SC"]["legii"] for t in SITES for g in GRAMS))
check("W5 (pure A^dag A) FAILS leg (i) at connection-off: tr(G) = 0 there, so "
      "the ratio is 0/0 and K3 support fails",
      all(TABLE[(t, "W5")][sc]["leg iii"]["conn_off"] == "undefined"
          for t in SITES for sc in ("SC", "RS")))
check("W5 AFFINE/HOMOGENEITY BLINDNESS (PR-2): at s_t = 0, A = s_x . A_x, so "
      "A^dag A = s_x^2 . A_x^dag A_x and the NORMALIZED profile is invariant "
      "under rescaling s_x -- 'same' on the s_x dial although the raw matrix "
      "moves.  The shim signature at the weight level.",
      all(TABLE[(t, "W5")][sc]["leg iii"]["sx_dial"] == "same"
          for t in SITES for sc in ("SC", "RS")))

WINNERS = [g for g in GRAMS
           if TABLE[("12x4", g)]["RS"]["legi"]
           and TABLE[("12x4", g)]["RS"]["legii"]
           and TABLE[("12x4", g)]["RS"]["legiii"]]
say(f"      TRILEMMA WINNERS at the BENCH (12x4, RS scope): {WINNERS}")
check("THE TRILEMMA HAS AT LEAST ONE SOLUTION at T_phys = 6: some W passes "
      "legs (i), (ii) and (iii) simultaneously", bool(WINNERS))
check("THE WINNING SET IS EXACTLY {W6, W7, W9, W10} on the enumerated "
      "battery {W1, W2, W5, W6, W7, W9, W10} at RS scope, 12x4 -- scoped to "
      "this enumeration and no wider",
      set(WINNERS) == {"W6", "W7", "W9", "W10"})
BEST = "W9"
DEEP = [g for g in WINNERS if "far" in TABLE[("12x4", g)]["RS"]["movers"]]
check("MEMORY DEPTH splits the winning set at the bench: EXACTLY {W9, W10} "
      "move under a record at the FARTHEST free level; W6 and W7 see only the "
      "adjacent level (depth 1).  Scoped to the five declared trails.",
      set(DEEP) == {"W9", "W10"})
check("THE CANDIDATE is W9 = herm(Q^{-1}).  Selection criterion, stated: it "
      "has full memory depth; it is the Hermitian part of the covariance the "
      "committed Gaussian measure actually supplies (G = Q^{-1}); and its "
      "SHIM TWIN herm(Q)^{-1} = W2 differs from it by the order of two "
      "operations and is LANDED transport-blind -- so the anti-shim "
      "separation is exhibited inside one formula.",
      BEST_OK := (TABLE[("12x4", "W9")]["RS"]["legi"]
                  and TABLE[("12x4", "W9")]["RS"]["legii"]
                  and TABLE[("12x4", "W9")]["RS"]["legiii"]))
check("THE CANDIDATE IS SEPARATED FROM ITS SHIM TWIN: the W9 and W2 profiles "
      "at the bench differ at the record slice, both extents -- one formula, "
      "two orders of herm() and inverse, opposite anti-shim verdicts",
      all(TABLE[(t, "W9")]["RS"]["profile"]
          != TABLE[(t, "W2")]["RS"]["profile"] for t in SITES))
say("      MEMORY DEPTH (which trails move the profile), 12x4 RS scope:")
for g in GRAMS:
    say(f"        {g:3s} {TABLE[('12x4', g)]['RS']['movers']}")

# W9 / W10 leg (i) as a THEOREM, not a census.
say("      LEG (i) FOR W9 AND W10 IS A THEOREM, not a census:")
say("        herm(Q) > 0  =>  herm(Q^{-1}) = Q^{-1} herm(Q) Q^{-dag} > 0")
say("        herm(Q) > 0  =>  Q^dag herm(Q)^{-1} Q = herm(Q) + A^dag "
    "herm(Q)^{-1} A >= herm(Q) > 0   (A^dag = -A)")
ident_ok = True
for tag, s in SITES.items():
    e = Env(s, s.bench.Q.subs(s.sub()), "b")
    ident_ok &= is_zero(e.gram("W9")
                        - sp.expand(e.Q.inv(method="LU") * e.S
                                    * e.Q.inv(method="LU").H))
    ident_ok &= is_zero(e.gram("W10")
                        - sp.expand(e.S + e.A.H * e.S.inv(method="LU") * e.A))
check("the two identities behind that theorem verified entry for entry at "
      "both extents", ident_ok)
check("its hypothesis herm(Q) > 0 measured POSITIVE DEFINITE at the bench "
      "carrier and at m in {1, 3}, both extents (a CENSUS over the tested "
      "points, not a theorem in m and the moduli)",
      all(inertia(herm(sp.expand(s.bench.Q.subs(s.sub(m=mm)))), "S")[1:] ==
          (0, 0) for s in SITES.values() for mm in (1, 3)))

# ---------------------------------------------------------------------------
say("")
say("--- SECTION 4b.  W8, THE MOMENT-MATRIX WEIGHTS -----------------------")
# ---------------------------------------------------------------------------
W8: dict = {}
for tag, s in SITES.items():
    for lab, kw in (("bench", {}), ("conn_off", dict(sx=0, st=0)),
                    ("sx_1_7", dict(sx=R(1, 7)))):
        mm = b170.moment_matrices(s.bench, s.sub(**kw))
        fams, labs, n = mm["families"], mm["labels"], mm["n"]
        for which in ("connected", "full"):
            M = mm[which]
            diag = [sp.expand(M[i, i]) for i in range(n)]
            realdiag = all(sp.im(d) == 0 for d in diag)
            total = sp.expand(sum(diag))
            prof = tuple(sp.cancel(sum(diag[i] for i, l in enumerate(labs)
                                       if l.startswith(f + "+")) / total)
                         for f in fams)
            W8[(tag, lab, which)] = {
                "hermitian": is_zero(M - M.H),
                "inertia": inertia(herm(M), "mm"),
                "realdiag": realdiag, "profile": prof,
            }
            rec(prof)
for tag in ("12x4", "8x4"):
    for which in ("connected", "full"):
        d = W8[(tag, "bench", which)]
        say(f"      {tag} {which:9s} hermitian={d['hermitian']} "
            f"herm-part inertia={tri(d['inertia'])} "
            f"real diagonal={d['realdiag']}")
        say(f"           family profile (mass,thop,xhop,plaq) = {d['profile']}")
check("W8 leg (i) CONDITIONAL: the moment matrix over the b170 "
      "transport-sensitive basis is NOT Hermitian at either extent (G = "
      "Q^{-1} is not Hermitian), so it is not a state; its diagonal is real "
      "and positive so the ratio is still normalizable",
      all(not W8[(t, "bench", w)]["hermitian"]
          and W8[(t, "bench", w)]["realdiag"]
          for t in SITES for w in ("connected", "full")))
check("W8 leg (i) FAILS on the FULL matrix at the bench (12x4): herm(M) is "
      "NOT PSD, one negative direction -- the landed audit-two pattern "
      "reproduced on the region carrier",
      W8[("12x4", "bench", "full")]["inertia"][1] > 0)
check("W8 leg (iii) PASSES: the family profile moves under the connection-off "
      "control AND under the s_x dial, both matrices, at the bench",
      all(W8[("12x4", l, w)]["profile"] != W8[("12x4", "bench", w)]["profile"]
          for l in ("conn_off", "sx_1_7") for w in ("connected", "full")))

# ---------------------------------------------------------------------------
say("")
say("--- SECTION 4c.  W3 / W4, THE MARGIN AND INDUCED-STATE WEIGHTS -------")
# ---------------------------------------------------------------------------
for tag, s in SITES.items():
    sub = s.sub()
    D = b166.hodge_trace_D(s.fx)
    Dc_sym = [sp.expand(D[(s.c, x)]) for x in range(s.lx)]
    Dsyms = set().union(*[d.free_symbols for d in Dc_sym])
    form = sp.expand(s.bench.form.subs({ST: 0}))
    B = form[:s.lx, :s.lx]
    C = form[:s.lx, s.lx:]
    Dblk = form[s.lx:, s.lx:]
    corner_zero = is_zero(C)
    Bnum = sp.expand(B.subs(sub))
    trB = sp.expand(sum(Bnum[i, i] for i in range(s.lx)))
    prof4 = tuple(sp.cancel(Bnum[i, i] / trB) for i in range(s.lx))
    rec(prof4)
    say(f"      {tag}: D(c,.) symbols = {sorted(str(x) for x in Dsyms)}")
    say(f"      {tag}: corner C = s_t.C_1 vanishes at s_t = 0: {corner_zero}; "
        f"so the Schur complement W3 EQUALS B = m.diag(D(c,.)) = W4 exactly")
    say(f"      {tag}: W4 induced-state profile = {prof4}")
    if tag == "12x4":
        W34 = dict(corner_zero=corner_zero, Dsyms=Dsyms, prof=prof4,
                   Dnum=[sp.expand(d.subs(sub)) for d in Dc_sym],
                   diagB=is_zero(Bnum - sp.diag(*[Bnum[i, i]
                                                  for i in range(s.lx)])))
check("W3 == W4 ON THE REGION, exactly: at s_t = 0 the corner C = s_t . C_1 "
      "vanishes, so the Schur complement of [rQ]_(S,S) IS B = m.diag(D(c,.)) "
      "-- the margin weight and the b166 induced-state weight are the SAME "
      "object there, both extents",
      W34["corner_zero"] and W34["diagB"])
check("W3/W4 FAIL legs (ii) and (iii) BY THEOREM: D(c,.) is built from the "
      "cells of the two PINNED links c-1 and c and contains no shear symbol "
      "and no connection symbol at all",
      not (W34["Dsyms"] & BSYMS["12x4"]) and not (W34["Dsyms"] & {SX, ST}))
say("      This is the margin law's mechanism: m.kappa_2 = 57/160 with "
      "kappa_2 shear-blind BY FORCE, because kappa_2 = lambda_max(C_1^dag "
      "B^{-1} C_1) and B = m.diag(D(c,.)) is record-free.  No run needed.")

# ---------------------------------------------------------------------------
say("")
say("--- SECTION 5.  THE K-IDENTITIES (T2, part 2) ------------------------")
# ---------------------------------------------------------------------------
say("TWO GENERATOR WIRINGS, both declared and both run:")
say("  G-A  slots = the free TIME LEVELS; alphabet = the L_x SITES; the")
say("       record 'the entry forms at site x of level t' is implemented as")
say("       the DISCONNECTION PIN sigma_(t,x) -> 0 (N1: the recording rule IS")
say("       the disconnection rule).  Class map = CM-SITE.")
say("  G-B  slots = the free LINKS (L_x per level); alphabet = CM-VALUE,")
say("       sigma in {0, 1/5, 2/5, 3/5}.  No projector partition.")

# --- K1 ---------------------------------------------------------------------
gsym = sp.Matrix(4, 4, lambda i, j: sp.Symbol(f"G_{i}{j}", real=(i == j)))
gsym = sp.expand((gsym + gsym.H) / 2)
Pis = class_projectors(BENCH, BENCH.tstar)
k1_symbolic = sp.expand(sum((sp.trace(gsym * P) for P in Pis),
                            sp.Integer(0)) - sp.trace(gsym)) == 0
check("K1 (G-A) IS A THEOREM: sum_a tr(G . Pi_a) = tr(G) for a FULLY SYMBOLIC "
      "Hermitian G -- an identity in the free symbols, so it is trail-length "
      "independent and lifts by induction to every T", k1_symbolic)
k1_num = True
K1DEF: dict = {}
for tag, s in SITES.items():
    TR = trails_for(s)
    for name, recs in TR.items():
        e = Env(s, s.bench.Q.subs(s.sub(records=recs)), name)
        B = e.block(BEST, s.tstar)
        tot = sp.expand(sum(B[i, i] for i in range(s.lx)))
        parts = [sp.expand(sp.trace(B * class_projectors(s, s.tstar)[a]))
                 for a in range(s.lx)]
        k1_num &= sp.expand(sum(parts) - tot) == 0
check("K1 (G-A) re-verified numerically-exactly on the CANDIDATE W9 over all "
      "declared trails at BOTH extents (8x4 and 12x4), so the identity is not "
      "a single-size wrap artifact", k1_num)
for tag, s in SITES.items():
    e0 = Env(s, s.bench.Q.subs(s.sub()), "e")
    B0 = e0.block(BEST, s.tstar)
    w_empty = sp.expand(sum(B0[i, i] for i in range(s.lx)))
    tot_v = sp.Integer(0)
    for cls in SIGMA_CLASSES:
        ev = Env(s, s.bench.Q.subs(
            s.sub(records={(s.tstar, 0): cls})), "v")
        Bv = ev.block(BEST, s.tstar)
        tot_v += sp.expand(sum(Bv[i, i] for i in range(s.lx)))
    defect = sp.cancel(tot_v / w_empty - 1)
    rec(defect)
    K1DEF[tag] = defect
    num, den = sp.fraction(defect)
    say(f"      K1 (G-B) defect at {tag}: "
        f"sum_(a in A_v) W(t.a) / W(t) - 1 is an EXACT nonzero rational with "
        f"a {len(str(num))}-digit numerator over a {len(str(den))}-digit "
        f"denominator (full value in the numeral ledger); the four individual "
        f"ratios W(t.a)/W(t) are each near 1, so the sum is near |A_v| = 4 "
        f"and the forward normalization is off by about 3 -- not a small "
        f"defect, a structural one")
check("K1 (G-B) FAILS: the sigma-value alphabet has no projector partition, "
      "so the forward normalization is NOT an identity -- the exact defect is "
      "nonzero at BOTH extents.  Under G-B, normalization is an INPUT (by "
      "fiat P(a|t) = W(t.a)/sum_a' W(t.a')), not a theorem.",
      all(K1DEF[t] != 0 for t in SITES))

# --- K2 ---------------------------------------------------------------------
def record_sub(site: Site, cell, cls, mode="xgraded") -> dict:
    """The committed modulus map at ONE cell -- the record written in."""
    fx, shear = site.fx, sp.sympify(cls)
    v = volume(mode, cell[0], cell[1])
    return {fx.NU[cell]: v,
            fx.A[cell]: v / (1 - shear ** 2),
            fx.B[cell]: -v * shear / (1 - shear ** 2),
            fx.MU[cell]: 1 / v}


k2_sym, k2_num = True, True
K2DEF: dict = {}
for tag, s in SITES.items():
    lvl = s.tstar
    r1, r2 = (lvl, 0), (lvl, 1)
    # SYMBOLIC: append the two records SEQUENTIALLY in both orders to the
    # SYMBOLIC action; the results must agree in the remaining free symbols.
    d1 = record_sub(s, r1, R(1, 5))
    d2 = record_sub(s, r2, R(2, 5))
    Q12 = sp.expand(s.bench.Q.subs(d1).subs(d2))
    Q21 = sp.expand(s.bench.Q.subs(d2).subs(d1))
    k2_sym &= is_zero(Q12 - Q21) and bool(Q12.free_symbols)
    # numeric weights, both orders, via the recursive (Lueders) definition
    def w(order):
        acc = sp.Integer(1)
        recs = {}
        for cell, cls, site_idx in order:
            e = Env(s, s.bench.Q.subs(s.sub(records=dict(recs))), "w")
            B = e.block(BEST, lvl)
            tot = sp.expand(sum(B[i, i] for i in range(s.lx)))
            acc = sp.cancel(acc * B[site_idx, site_idx] / tot)
            recs[cell] = cls
        return acc
    o1 = [(r1, R(1, 5), 0), (r2, R(2, 5), 1)]
    o2 = [(r2, R(2, 5), 1), (r1, R(1, 5), 0)]
    j1, j2 = w(o1), w(o2)
    k2_num &= (j1 == j2)
    K2DEF[tag] = sp.cancel(j1 - j2)
    rec(K2DEF[tag])
    say(f"      K2 weight-level joint, {tag}: order (x=0 then x=1) gives "
        f"{j1}; order (x=1 then x=0) gives {j2}; exact defect "
        f"{K2DEF[tag]}")
check("K2 (permutation consistency across the L_x links of ONE slice) holds "
      "SYMBOLICALLY: appending the two records in either order gives the SAME "
      "action entry for entry, with free symbols still present, at BOTH "
      "extents -- so K2 is a THEOREM for any substitution-implemented trail, "
      "for every weight, at every trail length", k2_sym)
check("K2 FAILS AT THE WEIGHT LEVEL, and this is the block's sharpest "
      "negative: the JOINT weight of the same two records computed in the two "
      "slot orders differs by an exact nonzero rational at BOTH extents.  The "
      "action substitution commutes (check above) but the chain-rule product "
      "of conditionals does not, because G_t depends on the trail "
      "NON-LINEARLY.  Consequence, stated precisely: the finite-window family "
      "is NOT Kolmogorov-consistent under re-enumeration of the L_x links of "
      "one slice, so Kolmogorov's extension theorem does NOT apply; "
      "Ionescu-Tulcea still does, since it needs only K1 + K3 at a FIXED "
      "declared slot order.  THE SLOT ORDER IS THEREFORE AN INPUT TO THE "
      "GENERATOR, not a derived object, and must be declared with it.",
      not k2_num and all(K2DEF[t] != 0 for t in SITES))

# --- K3 ---------------------------------------------------------------------
k3 = True
K3MIN = {}
for tag, s in SITES.items():
    worst = None
    for name, recs in trails_for(s).items():
        e = Env(s, s.bench.Q.subs(s.sub(records=recs)), name)
        p = e.profile(BEST, s.tstar)
        k3 &= p is not None and all(x > 0 for x in p)
        lo = min(p)
        worst = lo if worst is None or lo < worst else worst
    K3MIN[tag] = worst
    rec(worst)
check("K3 (support): W(t) > 0 strictly, and every class weight is strictly "
      "positive, on every declared trail at BOTH extents -- no 0/0 anywhere "
      "in the tower for the candidate", k3)
say(f"      smallest class weight over the declared trails: "
    f"12x4 {K3MIN['12x4']}   8x4 {K3MIN['8x4']}")

# ---------------------------------------------------------------------------
say("")
say("--- SECTION 6.  F8 FACTORIZATION / TRAIL-BLINDNESS (T3) --------------")
# ---------------------------------------------------------------------------
F8: dict = {}
for tag, s in SITES.items():
    TE = {k: Env(s, s.bench.Q.subs(s.sub(records=v)), k)
          for k, v in trails_for(s).items()}
    pA = TE["A"].profile(BEST, s.tstar)
    pB = TE["B"].profile(BEST, s.tstar)
    pC = TE["C"].profile(BEST, s.tstar)
    p0 = TE["empty"].profile(BEST, s.tstar)
    D5 = max(sp.Abs(pA[i] - pB[i]) for i in range(s.lx))
    D5c = max(sp.Abs(pA[i] - pC[i]) for i in range(s.lx))
    # the blindness-transfer test against count-proportional rivals
    p15 = Env(s, s.bench.Q.subs(s.sub(sigma=R(1, 5))), "s15"
              ).profile(BEST, s.tstar)
    p35 = Env(s, s.bench.Q.subs(s.sub(sigma=R(3, 5))), "s35"
              ).profile(BEST, s.tstar)
    D2 = max(sp.Abs(p15[i] - p35[i]) for i in range(s.lx))
    F8[tag] = dict(D5=D5, D5c=D5c, D2=D2, pA=pA, pB=pB, p0=p0)
    for v in (D5, D5c, D2):
        rec(v)
    say(f"      {tag}: D5 (trail A vs trail B, same length, different "
        f"content) = {D5}")
    say(f"      {tag}: D5' (trail A vs trail C, same SITES, different recorded "
        f"VALUE) = {D5c}")
    say(f"      {tag}: D2 (carrier sigma = 1/5 vs 3/5, blindness transfer) "
        f"= {D2}")
check("F8 VERDICT at the BENCH (12x4, T_phys = 6): the candidate does NOT "
      "factorize over the record partition -- P(a|trail) MOVES between two "
      "equal-length trails of different content, so W(t.a) != W(t).W(a) and "
      "the law is NOT trail-blind", F8["12x4"]["D5"] != 0)
check("F8 also fires on the recorded VALUE at fixed record SITES, so the "
      "sensitivity is to the record's content and not only to its support",
      F8["12x4"]["D5c"] != 0)
check("BLINDNESS-TRANSFER (falsification lens R2): D2 != 0, so the candidate "
      "profile is NOT carrier-blind and therefore not count-proportional in "
      "disguise; it does not inherit the boundary note's many-to-one kill",
      F8["12x4"]["D2"] != 0)
check("F8 at SC scope (the calibrated scope the panel named) fires the OTHER "
      "way at both extents: D5 = 0 exactly, the law IS trail-blind there -- "
      "the panel's finding, reproduced, and now explained by S1+S2",
      all(Env(s, s.bench.Q.subs(s.sub(records=trails_for(s)["A"])), "a"
              ).profile(BEST, s.c)
          == Env(s, s.bench.Q.subs(s.sub(records=trails_for(s)["B"])), "b"
                 ).profile(BEST, s.c) for s in SITES.values()))

# ---------------------------------------------------------------------------
say("")
say("--- SECTION 7.  THE B2/B3 PROFILE TABLE (T4) -------------------------")
# ---------------------------------------------------------------------------
def frequency_profile(trail: tuple, lx: int) -> tuple:
    n = len(trail)
    return tuple(R(sum(1 for a in trail if a == x), n) for x in range(lx))


ROWS = []
for tag, s in SITES.items():
    lv = s.free_levels[:2]
    for x1 in range(s.lx):
        for x2 in range(s.lx):
            trail = (x1, x2)
            recs = {(lv[0], x1): sp.Integer(0), (lv[1], x2): sp.Integer(0)}
            e = Env(s, s.bench.Q.subs(s.sub(records=recs)), "tbl")
            w = e.profile(BEST, s.tstar)
            f = frequency_profile(trail, s.lx)
            rec(w)
            rec(f)
            ROWS.append((tag, trail, w, f))
say(f"      emitted {len(ROWS)} (trail, weight profile, frequency profile) "
    f"rows across both extents")
byw: dict = {}
byf: dict = {}
for tag, trail, w, f in ROWS:
    byw.setdefault((tag, w), []).append((trail, f))
    byf.setdefault((tag, f), set()).add(w)
coll = {k: v for k, v in byw.items() if len({x[1] for x in v}) > 1}
census_coll = {k: v for k, v in byf.items() if len(v) > 1}
check("PRE-CENSUS OBSERVATION for B2: within this 16-trail enumeration per "
      "extent, DISTINCT weight profiles are attained (the table is not "
      "constant), so B2's census fixture is non-empty",
      len({w for _, _, w, _ in ROWS if _ is not None}) > 1)
say(f"      distinct weight profiles at 12x4: "
    f"{len({w for t, _, w, _ in ROWS if t == '12x4'})} of 16")
say(f"      distinct frequency profiles at 12x4: "
    f"{len({f for t, _, _, f in ROWS if t == '12x4'})} of 16")
say(f"      weight profiles carrying more than one frequency profile: "
    f"{len(coll)}  (the bridge-as-a-function direction: 0 means W determines "
    f"the frequency profile on this enumeration)")
say(f"      CENSUS DIRECTION -- frequency profiles carrying more than one "
    f"WEIGHT profile: 12x4 "
    f"{len([k for k in census_coll if k[0] == '12x4'])} of "
    f"{len({f for t, _, _, f in ROWS if t == '12x4'})}")
check("PRE-CENSUS VERDICT FOR B2, and it is a design result: on the SITE "
      "alphabet the census WILL find collisions -- at 12x4, 6 of the 10 "
      "frequency profiles carry TWO distinct weight profiles -- for the "
      "purely combinatorial reason the boundary note already landed (the "
      "count map is many-to-one: trails (x1,x2) and (x2,x1) share a "
      "frequency profile and have different weights).  So B2's "
      "'zero collisions => theorem candidate' branch is UNREACHABLE on this "
      "alphabet, and B2 must run the REFINEMENT (Gleason-shaped) variant the "
      "synthesis specifies, not the profile-injectivity variant.",
      len([k for k in census_coll if k[0] == "12x4"]) == 6)

TABLE_PATH = Path(__file__).resolve().parent / "b171_profile_table.py"
with TABLE_PATH.open("w") as fh:
    fh.write('"""Block 171 (B1) -- the exact-rational profile table for B2/B3.'
             '\n\n')
    fh.write("Emitted by block171_solve.py.  Every entry is an exact sympy\n")
    fh.write("Rational literal written as a (numerator, denominator) pair.\n\n")
    fh.write("WEIGHT is the candidate W9 = herm(Q^{-1}) profile\n")
    fh.write("  P(a | trail) = tr(G . Pi_a) / tr(G), G = herm(Q^{-1})\n")
    fh.write("compressed to the record slice t* and read on the site class\n")
    fh.write("map {Pi_a}, at the region pin (s_t = 0), s_x = 3/5, m = 1,\n")
    fh.write("carrier sigma = 3/5 on the x-inhomogeneous probe carrier.\n")
    fh.write("FREQUENCY is the record-frequency profile of the trail itself.\n")
    fh.write("TRAIL is (x_1, x_2): the record sites at the first two free\n")
    fh.write("time levels, each implemented as the disconnection pin\n")
    fh.write("sigma -> 0 at that cell.\n")
    fh.write("BENCH = 12x4 (T_phys = 6); 8x4 (T_phys = 4) is a DISCLOSED\n")
    fh.write("cross-check and carries no verdict.\n")
    fh.write('"""\n\n')
    fh.write("SCHEMA = ('extent', 'trail', 'weight_profile', "
             "'frequency_profile')\n\n")
    fh.write("ROWS = (\n")
    for tag, trail, w, f in ROWS:
        wl = ", ".join(f"({sp.Integer(v.p)}, {sp.Integer(v.q)})" for v in w)
        fl = ", ".join(f"({sp.Integer(v.p)}, {sp.Integer(v.q)})" for v in f)
        fh.write(f"    ({tag!r}, {trail!r}, ({wl}), ({fl})),\n")
    fh.write(")\n\n")
    fh.write("NULL_FIXTURES = (\n")
    fh.write("    # carrier, why nothing may be benched there\n")
    fh.write("    ('flat', 'profile exactly uniform -- the landed null'),\n")
    fh.write("    ('graded', 'the LANDED b166 carrier is x-homogeneous, "
             "(3t+5x) mod 5 = 3t mod 5, so every site profile is exactly "
             "uniform -- a SECOND null fixture, measured in block 171'),\n")
    fh.write(")\n\n")
    fh.write("BENCH_CARRIER = 'xgraded: volume = (1 + (3t + 2x) mod 5)/3 + "
             "1/2, sigma = 3/5 off the region pin'\n")
say(f"      wrote {TABLE_PATH}")

# ---------------------------------------------------------------------------
say("")
say("--- SECTION 8.  EXACTNESS AND HYGIENE GATES --------------------------")
# ---------------------------------------------------------------------------
def has_float(v) -> bool:
    if isinstance(v, (tuple, list)):
        return any(has_float(x) for x in v)
    if isinstance(v, float):
        return True
    try:
        return bool(sp.sympify(v).atoms(sp.Float))
    except Exception:
        return False


check(f"NO-FLOAT GATE over all {len(NUMERALS)} reported numerals",
      not any(has_float(v) for v in NUMERALS))
src = Path(__file__).read_text()
# The forbidden token is assembled at runtime so that the gate does not
# match its own source line.
BANNED = "nsimpl" + "ify" + "("
check("NO-NSIMPLIFY GATE: no call to the banned simplifier occurs in this "
      "file (the bare word appears only in the discipline banners that name "
      "the ban)", BANNED not in src)
check("INERTIA-CONVENTION GATE: every triple printed here went through "
      "b170.tri, which stamps (n+,n-,n0)[b165] inline",
      "(n+,n-,n0)[b165]" in tri((1, 0, 0)))
elapsed = time.time() - START
check(f"RUNTIME {elapsed:.1f}s within the 200s budget", elapsed < 200)

say("")
say("=" * 78)
fails = [x for x in LOG if not x[2]]
say(f"CHECKS {len(LOG)}  PASS {len(LOG) - len(fails)}  FAIL {len(fails)}")
for n, s, _ in fails:
    say(f"  FAILED [{n:02d}] {s}")
say(f"ELAPSED {elapsed:.1f}s")
say("=" * 78)
sys.exit(1 if fails else 0)
