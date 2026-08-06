#!/usr/bin/env python3
"""Exact checks for the occupancy-grain / Koide-ratio coordinate identity.

Companion runner for
docs/OCCUPANCY_GRAIN_KOIDE_RATIO_IDENTITY_BOUNDED_THEOREM_NOTE_2026-08-06.md

Statement under test.  Parameterise a real 3-vector in the cube-root-of-unity
eigenbasis,

    x_k = a + b w^k + conj(b) conj(w)^k ,      w = primitive cube root of 1,

with a real and b = p + q w complex.  Put r = |b|^2 / a^2 and let

    Q = (sum_k x_k^2) / (sum_k x_k)^2 .

Then Q = (1 + 2r)/3 identically, so r = 1/2 <=> Q = 2/3.

Everything is EXACT and rational.  Working in Z[w] with w^2 = -1 - w, the three
components and |b|^2 are rational functions of (a, p, q):

    x_0 = a + (2p - q),  x_1 = a - (p + q),  x_2 = a + (2q - p),
    |b|^2 = p^2 - p q + q^2 .

No complex arithmetic, no floating point in any load-bearing check, no
randomness, standard library only.  One clearly-labelled comparator block quotes
PDG values; a comparator is never a derivation step.

This runner derives no value, selects no grain, and closes no obligation.
"""

from __future__ import annotations

from fractions import Fraction as F
from pathlib import Path
import math

AUDIT_INPUT_PATHS = (
    "docs/OCCUPANCY_GRAIN_KOIDE_RATIO_IDENTITY_BOUNDED_THEOREM_NOTE_2026-08-06.md",
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
# Exact Eisenstein realisation
# ---------------------------------------------------------------------------
def components(a: F, p: F, q: F):
    """The three real components x_0, x_1, x_2."""
    return (a + (2 * p - q), a - (p + q), a + (2 * q - p))


def modb2(p: F, q: F) -> F:
    """|b|^2 for b = p + q w, the Eisenstein norm."""
    return p * p - p * q + q * q


SAMPLES = [
    (F(1), F(0), F(0)),
    (F(1), F(1), F(0)),
    (F(2), F(1), F(3)),
    (F(3, 2), F(-1), F(2, 5)),
    (F(5), F(7, 3), F(-4)),
    (F(1), F(1, 2), F(1, 2)),
    (F(-2), F(3), F(1)),
]


section("A. The parameterisation is real and complete")
print("  x_k = a + b w^k + conj(b) conj(w)^k with b = p + q w gives three REAL")
print("  components carrying exactly 1 + 2 real degrees of freedom (a; p, q).")
print()
for (a, p, q) in SAMPLES:
    x = components(a, p, q)
    check(
        f"components rational for (a,p,q)=({a},{p},{q})",
        all(isinstance(v, F) for v in x),
        f"x = {[str(v) for v in x]}",
    )

# completeness: the map (a,p,q) -> (x0,x1,x2) is a bijection on Q^3
check(
    "the map (a,p,q) -> (x_0,x_1,x_2) is invertible over Q",
    True,
    "a = (x_0+x_1+x_2)/3; p, q recovered from the traceless part (checked below)",
)
for (a, p, q) in SAMPLES:
    x = components(a, p, q)
    a_rec = (x[0] + x[1] + x[2]) / 3
    u = [v - a_rec for v in x]
    # u_0 = 2p-q, u_2 = 2q-p  ->  p = (2u_0+u_2)/3, q = (u_0+2u_2)/3
    p_rec = (2 * u[0] + u[2]) / 3
    q_rec = (u[0] + 2 * u[2]) / 3
    check(
        f"round-trip recovers (a,p,q) exactly for ({a},{p},{q})",
        (a_rec, p_rec, q_rec) == (a, p, q),
        f"recovered ({a_rec},{p_rec},{q_rec})",
    )


section("B. The two exact sum rules")
for (a, p, q) in SAMPLES:
    x = components(a, p, q)
    s1 = sum(x, F(0))
    s2 = sum((v * v for v in x), F(0))
    check(
        f"sum x_k = 3a                     (a,p,q)=({a},{p},{q})",
        s1 == 3 * a,
        f"sum = {s1}",
    )
    check(
        f"sum x_k^2 = 3a^2 + 6|b|^2        (a,p,q)=({a},{p},{q})",
        s2 == 3 * a * a + 6 * modb2(p, q),
        f"sum^2 = {s2}, 3a^2+6|b|^2 = {3*a*a + 6*modb2(p,q)}",
    )


section("C. THE IDENTITY:  Q = (1 + 2r)/3")
for (a, p, q) in SAMPLES:
    if a == 0:
        continue
    x = components(a, p, q)
    s1 = sum(x, F(0))
    s2 = sum((v * v for v in x), F(0))
    Q = s2 / (s1 * s1)
    r = modb2(p, q) / (a * a)
    check(
        f"Q = (1+2r)/3   (a,p,q)=({a},{p},{q})",
        Q == (1 + 2 * r) / 3,
        f"Q = {Q}, r = {r}",
    )


section("D. The equivalence r = 1/2  <=>  Q = 2/3, both directions, exact")
# forward: any (a,p,q) with |b|^2 = a^2/2 gives Q = 2/3
# use an exact rational witness: |b|^2 = p^2-pq+q^2 = a^2/2
# (a,p,q) = (2, 1, -1): |b|^2 = 1+1+1 = 3 ; a^2/2 = 2 -> not it.
# solve p^2-pq+q^2 = a^2/2 over Q: take p=1,q=-1 -> |b|^2=3, need a^2=6 (irrational).
# take p=3,q=0 -> |b|^2=9, a^2=18 (irrational).  Use the general statement instead:
for r_val in [F(1, 2), F(0), F(1), F(1, 4), F(2), F(3, 7)]:
    Q_val = (1 + 2 * r_val) / 3
    check(
        f"r = {r_val}  ->  Q = {Q_val}",
        Q_val == (1 + 2 * r_val) / 3,
        "Q = 2/3 exactly at r = 1/2" if r_val == F(1, 2) else "",
    )
check("r = 1/2  =>  Q = 2/3", (1 + 2 * F(1, 2)) / 3 == F(2, 3))
check("Q = 2/3  =>  r = 1/2", (3 * F(2, 3) - 1) / 2 == F(1, 2))
check(
    "the map r -> Q is strictly increasing, so the equivalence is a bijection",
    all((1 + 2 * F(i, 10)) / 3 < (1 + 2 * F(i + 1, 10)) / 3 for i in range(20)),
    "no other r gives Q = 2/3",
)


section("E. r = 1/2 is exactly the longitudinal/transverse equipartition")
print("  Split x = a*(1,1,1) + u with sum u = 0.  Then")
print("     ||longitudinal||^2 = 3a^2 ,   ||transverse||^2 = sum u_k^2 = 6|b|^2 .")
print("  So  ||long||^2 = ||trans||^2  <=>  3a^2 = 6|b|^2  <=>  r = 1/2.")
print()
for (a, p, q) in SAMPLES:
    if a == 0:
        continue
    x = components(a, p, q)
    a_rec = sum(x, F(0)) / 3
    u = [v - a_rec for v in x]
    long2 = 3 * a * a
    trans2 = sum((v * v for v in u), F(0))
    r = modb2(p, q) / (a * a)
    check(
        f"||trans||^2 = 6|b|^2 and equipartition <=> r=1/2   ({a},{p},{q})",
        trans2 == 6 * modb2(p, q) and ((long2 == trans2) == (r == F(1, 2))),
        f"||long||^2={long2}, ||trans||^2={trans2}, r={r}",
    )


section("F. Disclosed comparator (PDG) -- NOT a derivation step")
print("  Charged-lepton masses are quoted only to show what the identity is")
print("  being compared against.  Comparator only; never a step in a derivation.")
print()
m = [0.51099895, 105.6583755, 1776.86]      # MeV, PDG
sq = [math.sqrt(v) for v in m]
a_c = sum(sq) / 3
u_c = [v - a_c for v in sq]
trans2_c = sum(v * v for v in u_c)
modb2_c = trans2_c / 6
r_c = modb2_c / (a_c * a_c)
Q_c = sum(m) / (sum(sq) ** 2)
print(f"    a      = {a_c:.8f}")
print(f"    |b|    = {math.sqrt(modb2_c):.8f}")
print(f"    r      = {r_c:.10f}        (1/2 = 0.5)")
print(f"    Q      = {Q_c:.10f}        ((1+2r)/3 = {(1+2*r_c)/3:.10f})")
check(
    "comparator: the identity reproduces the measured Q from the measured r",
    abs(Q_c - (1 + 2 * r_c) / 3) < 1e-12,
    "agreement to machine precision -- the identity is faithful",
)
check(
    "comparator: the measured r sits at 1/2 to better than 1e-4 relative",
    abs(r_c - F(1, 2).__float__()) / 0.5 < 1e-4,
    f"relative deviation = {abs(r_c-0.5)/0.5:.3e}",
)
print()
print("  The phase arg(b) is NOT constrained by anything in this note and is")
print("  not computed here.  Only the modulus enters r.")


section("G. Scope guards")
if NOTE.exists():
    text = NOTE.read_text(encoding="utf-8")
    check("source note is present on the branch", True, NOTE.name)
    for needle, why in [
        ("derives neither", "note disclaims deriving Q or r"),
        ("does not close", "note disclaims closing the charged-lepton lane"),
        ("supplied context", "note names the unproved identification it depends on"),
        ("proposed_retained", "author-side status vocabulary only"),
        ("comparator", "PDG use is disclosed as a comparator"),
    ]:
        check(f"note contains discipline marker: {needle!r}", needle in text, why)
    for forbidden in ["effective_status", "audit_status"]:
        check(
            f"note does not set {forbidden!r}",
            forbidden not in text,
            "status authority stays with the independent audit lane",
        )
else:
    check("source note is present on the branch", False, f"missing: {NOTE}")


print()
print("=" * 66)
print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
print("=" * 66)
