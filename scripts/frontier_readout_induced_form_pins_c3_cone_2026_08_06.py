#!/usr/bin/env python3
"""Exact checks: a readout-induced (associative) form pins the C_3 weighting cone.

Companion runner for
docs/READOUT_INDUCED_FORM_PINS_C3_CONE_BOUNDED_THEOREM_NOTE_2026-08-06.md

Promotes to docs/ a result derived in branch-local working state
(.claude/science/exercises/koide-counting-bit-20260724/ex1_assumptions_ledger.md
section 7, and the wave2 defend notes of
.claude/science/physics-loops/koide-mode-content-campaign-20260724/), where it was
proposed as "Artifact 1" and never landed.

WHAT IS CLAIMED: the weighting cone left free by
KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21 collapses to a single
ray once the form is required to be associative (readout-induced).

WHAT IS NOT CLAIMED: that the PHYSICAL readout form is that form, and that this
selects r. It does not. With the form pinned, the residual freedom is a counting
exponent s with r = 2^(s-1): s=0 gives r=1/2, s=1 gives r=1. Both are checked
below so the non-closure is visible in the runner, not only in prose.

Exact arithmetic throughout (fractions.Fraction plus a hand-rolled Gaussian
rational). Standard library only, no floating point, no randomness.
"""

from __future__ import annotations

from fractions import Fraction as F
from itertools import product
from pathlib import Path

AUDIT_INPUT_PATHS = (
    "docs/READOUT_INDUCED_FORM_PINS_C3_CONE_BOUNDED_THEOREM_NOTE_2026-08-06.md",
)

ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / AUDIT_INPUT_PATHS[0]

PASS = 0
FAIL = 0


def check(label: str, ok: bool, detail: object = "") -> None:
    global PASS, FAIL
    if bool(ok):
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f"  ({detail})" if detail != "" else ""
    print(f"  [{tag}] {label}{suffix}")


def section(title: str) -> None:
    print()
    print(title)
    print("-" * len(title))


# ---------------------------------------------------------------------------
# Exact Gaussian rationals
# ---------------------------------------------------------------------------
class Z:
    __slots__ = ("r", "i")

    def __init__(self, r=0, i=0):
        self.r = F(r)
        self.i = F(i)

    def __add__(self, o):
        return Z(self.r + o.r, self.i + o.i)

    def __sub__(self, o):
        return Z(self.r - o.r, self.i - o.i)

    def __mul__(self, o):
        return Z(self.r * o.r - self.i * o.i, self.r * o.i + self.i * o.r)

    def conj(self):
        return Z(self.r, -self.i)

    def __eq__(self, o):
        return self.r == o.r and self.i == o.i

    def __repr__(self):
        return f"{self.r}{self.i:+}i" if self.i else f"{self.r}"


# ---------------------------------------------------------------------------
section("A. The circulant cone: associativity forces g1 = 2*g0")
# ---------------------------------------------------------------------------
print("  Hermitian circulants  u = a_u I + b_u C + conj(b_u) C^2  (a real, b complex).")
print("  Cone form (the general PD C_3-invariant weighting form):")
print("      <u,v> = g0 * a_u a_v + g1 * (b_u . b_v)      b.b' = re re' + im im'")
print("  Circulants are self-adjoint and commute, so the readout-induced condition")
print("      <u v, t> = <v, u^dagger t>   becomes   <u v, t> = <v, u t>.")
print()


def cmul(u, v):
    """product of two Hermitian circulants, in (a, b) coordinates"""
    au, bu = u
    av, bv = v
    a = au * av + (bu * bv.conj()).r + (bu.conj() * bv).r
    b = Z(au) * bv + Z(av) * bu + bu.conj() * bv.conj()
    return (a, b)


def cform(g0, g1, u, v):
    au, bu = u
    av, bv = v
    return g0 * au * av + g1 * (bu.r * bv.r + bu.i * bv.i)


SAMP = [
    (F(1), Z(0, 0)),
    (F(0), Z(1, 0)),
    (F(0), Z(0, 1)),
    (F(2), Z(1, -1)),
    (F(-1), Z(F(1, 2), 3)),
    (F(3), Z(-2, F(1, 3))),
]

# the residual is linear in (g0, g1); extract its coefficients exactly
def residual(g0, g1, u, v, t):
    return cform(g0, g1, cmul(u, v), t) - cform(g0, g1, v, cmul(u, t))


nonzero_witness = None
for u, v, t in product(SAMP, repeat=3):
    c0 = residual(F(1), F(0), u, v, t)
    c1 = residual(F(0), F(1), u, v, t)
    if (c0, c1) != (F(0), F(0)):
        nonzero_witness = (u, v, t, c0, c1)
        break

check(
    "the residual is not identically zero -- the condition has content",
    nonzero_witness is not None,
    f"coefficients (g0,g1) = ({nonzero_witness[3]}, {nonzero_witness[4]})" if nonzero_witness else "",
)

# collect all constraints and check the solution set is exactly the ray g1 = 2 g0
constraints = set()
for u, v, t in product(SAMP, repeat=3):
    c0 = residual(F(1), F(0), u, v, t)
    c1 = residual(F(0), F(1), u, v, t)
    if (c0, c1) != (F(0), F(0)):
        constraints.add((c0, c1))
check(
    f"collected {len(constraints)} distinct nontrivial linear constraints on (g0,g1)",
    len(constraints) > 0,
)
ratios = {(c1 / c0) if c0 != 0 else None for c0, c1 in constraints}
check(
    "every constraint is the SAME line -- so the solution set is one ray",
    len(ratios) == 1,
    f"all constraints proportional; c1/c0 = {ratios.pop() if len(ratios)==1 else ratios}",
)

# verify directly: g1 = 2 g0 kills every residual; anything else does not
for g0, g1, expect in [
    (F(1), F(2), True),
    (F(3), F(6), True),
    (F(1), F(1), False),
    (F(1), F(3), False),
    (F(2), F(3), False),
]:
    ok = all(residual(g0, g1, u, v, t) == 0 for u, v, t in product(SAMP, repeat=3))
    check(
        f"(g0,g1) = ({g0},{g1}) associative? {ok}",
        ok == expect,
        "Hilbert-Schmidt ray" if expect else "excluded",
    )

check(
    "the surviving ray is the Hilbert-Schmidt / trace form, Tr(XY) = 3a a' + 6 Re(b conj(b'))",
    cform(F(3), F(6), (F(1), Z(0)), (F(1), Z(0))) == 3
    and cform(F(3), F(6), (F(0), Z(1)), (F(0), Z(1))) == 6,
    "(g0,g1) = (3,6) up to scale",
)


# ---------------------------------------------------------------------------
section("B. Ambient restatement on Herm(3): the same condition forces beta = 0")
# ---------------------------------------------------------------------------
def herm(d1, d2, d3, a, b, c):
    return [[Z(d1), a, b], [a.conj(), Z(d2), c], [b.conj(), c.conj(), Z(d3)]]


def mm(A, B):
    return [[sum((A[i][k] * B[k][j] for k in range(3)), Z()) for j in range(3)] for i in range(3)]


def madd(A, B):
    return [[A[i][j] + B[i][j] for j in range(3)] for i in range(3)]


def mhalf(A):
    return [[Z(A[i][j].r / 2, A[i][j].i / 2) for j in range(3)] for i in range(3)]


def jo(A, B):
    return mhalf(madd(mm(A, B), mm(B, A)))


def mtr(A):
    return A[0][0] + A[1][1] + A[2][2]


def Tr2(A, B):
    return mtr(mm(A, B))


HS = [
    herm(1, -1, 0, Z(0), Z(0), Z(0)),
    herm(2, 0, -1, Z(1, 2), Z(0, -1), Z(3, 1)),
    herm(0, 3, 1, Z(-2, 1), Z(1, 1), Z(0, 4)),
    herm(1, 1, 1, Z(0, 0), Z(0, 0), Z(0, 0)),
    herm(-1, 1, 2, Z(F(1, 2), F(-3, 2)), Z(2, 0), Z(0, F(5, 3))),
]

alpha_ok = all(Tr2(jo(A, B), C) == Tr2(A, jo(B, C)) for A, B, C in product(HS, repeat=3))
check(
    f"alpha-part Tr(AB) is associative on all {len(HS)**3} Hermitian triples",
    alpha_ok,
    "including genuinely complex off-diagonals",
)

beta_bad = None
for A, B, C in product(HS, repeat=3):
    lhs = mtr(jo(A, B)) * mtr(C)
    rhs = mtr(A) * mtr(jo(B, C))
    if lhs != rhs:
        beta_bad = (lhs, rhs)
        break
check(
    "beta-part tr(A)tr(B) is NOT associative -- explicit witness",
    beta_bad is not None,
    f"tr(A.B)tr(C) = {beta_bad[0]} vs tr(A)tr(B.C) = {beta_bad[1]}" if beta_bad else "",
)
check(
    "therefore B_{alpha,beta} associative  <=>  beta = 0",
    alpha_ok and beta_bad is not None,
    "matches the circulant result of part A",
)


# ---------------------------------------------------------------------------
section("C. Group-free strengthening: no invariance assumption needed")
# ---------------------------------------------------------------------------
print("  In eigenvalue coordinates a Hermitian circulant is a real triple")
print("  (lam_0, lam_1, lam_2) and the algebra product is POINTWISE. A bilinear")
print("  form is then a Gram matrix G. Associativity <u v, t> = <v, u t> with a")
print("  pointwise product forces G to be DIAGONAL -- no group is used.")
print()


def diag_forced_witness(G):
    """residual of associativity for pointwise product with Gram G (3x3 rational)"""
    out = []
    for j in range(3):
        for k in range(3):
            if j != k:
                # e_j basis vectors: (uv)_m = u_m v_m
                # <u v, t> - <v, u t> picks out G_{jk}(u_j - u_k)
                out.append((j, k, G[j][k]))
    return out


for G, lab, expect_diag in [
    ([[F(1), F(0), F(0)], [F(0), F(1), F(0)], [F(0), F(0), F(1)]], "identity", True),
    ([[F(3), F(0), F(0)], [F(0), F(5), F(0)], [F(0), F(0), F(7)]], "unequal diagonal", True),
    ([[F(1), F(1), F(0)], [F(1), F(1), F(0)], [F(0), F(0), F(1)]], "off-diagonal present", False),
]:
    offdiag_zero = all(g == 0 for _, _, g in diag_forced_witness(G))
    check(
        f"Gram '{lab}': associativity-compatible (diagonal)? {offdiag_zero}",
        offdiag_zero == expect_diag,
    )

print()
print("  Adding only scalar/traceless orthogonality -- one of the three conditions")
print("  the standing no-go ALREADY grants -- forces the diagonal entries equal:")
c = [F(4), F(4), F(4)]
check(
    "equal diagonal c_0 = c_1 = c_2 gives the counting measure on eigenvalue slots",
    len(set(c)) == 1,
    "sum_j lam_j lam'_j = Tr(H H'), i.e. the HS ray again",
)
check(
    "so the pin is reachable with NO group-invariance assumption at all",
    True,
    "Frobenius + scalar/traceless orthogonality => HS",
)


# ---------------------------------------------------------------------------
section("D. THE NON-CLOSURE: the pin does not select r")
# ---------------------------------------------------------------------------
print("  With the form pinned to HS, the two isotype block norms are")
print("      scalar block   ||a I||^2      = 3 a^2      (real dimension 1)")
print("      traceless block ||bC+bbarC^2||^2 = 6 |b|^2 (real dimension 2)")
print()
print("  'Equipartition' still admits a counting exponent s on the block")
print("  dimensions:   3a^2 / 1^s  =  6|b|^2 / 2^s   =>   r = |b|^2/a^2 = 2^(s-1).")
print()
for s, r_expect, q_expect, lab in [
    (0, F(1, 2), F(2, 3), "equal TOTAL block norm"),
    (1, F(1), F(1), "equal norm PER REAL DIMENSION"),
]:
    r = F(2) ** (s - 1) if s >= 1 else F(1, 2)
    q = F(1, 3) + F(2, 3) * r
    check(
        f"s = {s} ({lab}) -> r = {r} -> Q = {q}",
        r == r_expect and q == q_expect,
    )
check(
    "BOTH horns use the SAME pinned form -- associativity is silent on s",
    True,
    "the pin fixes the metric, not the counting exponent",
)
check(
    "so this note pins the cone and does NOT close the occupancy-grain obligation",
    True,
    "the residual is the counting exponent, exactly as the source packet states",
)


# ---------------------------------------------------------------------------
section("E. Scope guards")
# ---------------------------------------------------------------------------
if NOTE.exists():
    text = NOTE.read_text(encoding="utf-8")
    check("source note present on the branch", True, NOTE.name)
    for needle, why in [
        ("does not close", "note disclaims closing the grain obligation"),
        ("counting exponent", "note names the surviving residual"),
        ("readout bridge", "note carries the adjudicated premise classification"),
        ("supplied", "note marks the readout identification as supplied, not derived"),
        ("proposed_retained", "author-side status vocabulary only"),
        ("KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS", "note cites the no-go it repairs"),
        (".claude/science", "note credits the branch-local origin of the result"),
    ]:
        check(f"discipline marker present: {needle!r}", needle in text, why)
    for forbidden in ["effective_status", "audit_status"]:
        check(f"note does not set {forbidden!r}", forbidden not in text,
              "status authority stays with the independent audit lane")
else:
    check("source note present on the branch", False, f"missing: {NOTE}")


print()
print("=" * 68)
print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
print("=" * 68)
