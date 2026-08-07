#!/usr/bin/env python3
"""Exact checks: the C_3 sector dial is invariant under a common mass rescaling.

Companion runner for
docs/SECTOR_DIAL_SCALE_INVARIANCE_AND_COMMON_SCALE_COMPARATOR_BOUNDED_THEOREM_NOTE_2026-08-07.md

Load-bearing content is Parts A-C and is exact: `fractions.Fraction` and
integers only, no floating point, no randomness.

Part D is a COMPARATOR block.  It uses floating point and external PDG inputs
and is not a derivation step.  It exists only to show, numerically, what the
exact theorem of Parts A-C implies for the quark-sector comparators already
displayed in
docs/QUARK_MASS_SPECTRUM_KOIDE_SCHEME_OPEN_GATE_NOTE_2026-05-26.md.

This runner derives no quark mass, no mass scale, no phase law, and no sector
weight, and it closes no obligation.
"""

from __future__ import annotations

import math
from fractions import Fraction
from itertools import product
from pathlib import Path

AUDIT_INPUT_PATHS = (
    "docs/SECTOR_DIAL_SCALE_INVARIANCE_AND_COMMON_SCALE_COMPARATOR_BOUNDED_THEOREM_NOTE_2026-08-07.md",
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
# The dial, in exact rational coordinates.
#
# Generation coordinates are x_k = sqrt(m_k) >= 0 with sum S != 0.  Writing
#
#     x_k = a + 2 |b| cos(delta + 2 pi k / 3),      a = S/3,
#
# the C_3 Fourier coefficient is b = (1/3) sum_k x_k omega^{-k} with
# omega = exp(2 pi i / 3) = (-1 + i sqrt 3)/2.  Ordering x_0 >= x_1 >= x_2,
#
#     Re b = (x_0 - (x_1 + x_2)/2) / 3,
#     Im b = sqrt(3) * (x_2 - x_1) / 6.
#
# Both Re(b)/a and Im(b)/(a sqrt 3) are RATIONAL in the x_k, so the whole dial
#
#     r = |b|^2 / a^2 = (Re b / a)^2 + 3 * (Im b / (a sqrt 3))^2,
#     Q = sum_k x_k^2 / S^2 = (1 + 2 r) / 3,
#     delta = atan2(Im b, Re b),
#
# is pinned by the exact rational pair (C, J) below.  No square roots are taken
# anywhere in Parts A-C.
# ---------------------------------------------------------------------------
def dial_exact(x):
    """Exact dial invariants of a descending rational triple x = (x0>=x1>=x2).

    Returns (Q, r, C, J) with

        C = Re(b)/a,   J = Im(b)/(a*sqrt 3),   r = C^2 + 3 J^2,
        Q = (1 + 2r)/3 = sum x_k^2 / (sum x_k)^2 .

    delta = atan2(sqrt(3)*J, C) is a function of (C, J) alone, so invariance of
    the pair is invariance of delta.
    """
    x0, x1, x2 = x
    S = x0 + x1 + x2
    if S == 0:
        raise ValueError("sum of generation coordinates must be nonzero")
    a = Fraction(S, 1) / 3
    Q = (x0 * x0 + x1 * x1 + x2 * x2) / (S * S)
    C = (x0 - (x1 + x2) / 2) / 3 / a
    J = (x2 - x1) / 6 / a
    r = C * C + 3 * J * J
    return Q, r, C, J


def desc(t):
    return tuple(sorted((Fraction(v) for v in t), reverse=True))


# a spread of exact rational generation triples, all with distinct entries
TRIPLES = [
    (Fraction(1), Fraction(1, 2), Fraction(1, 5)),
    (Fraction(7, 3), Fraction(5, 4), Fraction(1, 9)),
    (Fraction(100), Fraction(3), Fraction(1, 100)),
    (Fraction(13, 2), Fraction(13, 3), Fraction(13, 7)),
    (Fraction(1), Fraction(1), Fraction(1)),          # degenerate, r = 0
    (Fraction(1), Fraction(1), Fraction(1, 10)),      # doubly degenerate
    (Fraction(1861), Fraction(97), Fraction(2)),
]

SCALES = [Fraction(2), Fraction(1, 3), Fraction(17, 5), Fraction(1000),
          Fraction(1, 1000), Fraction(11, 7)]


section("A. EXACT: the dial is homogeneous of degree 0 in the masses")

print("  A common mass rescaling m_k -> lam * m_k is x_k -> mu * x_k with")
print("  mu = sqrt(lam) > 0.  Both Q and (C, J) are ratios of forms of equal")
print("  degree in x, so every mu cancels identically.  The checks below are")
print("  exact in Q(x, mu): no square roots, no floating point.")
print()

for t in TRIPLES:
    x = desc(t)
    Q0, r0, C0, J0 = dial_exact(x)
    all_ok = True
    for mu in SCALES:
        # mu > 0 preserves the descending order, so the same convention applies
        xs = desc(tuple(mu * v for v in x))
        Q1, r1, C1, J1 = dial_exact(xs)
        if (Q1, r1, C1, J1) != (Q0, r0, C0, J0):
            all_ok = False
            break
    check(
        f"x={tuple(str(v) for v in x)}: dial fixed under all {len(SCALES)} rescalings",
        all_ok,
        f"Q={Q0}  r={r0}  C={C0}  J={J0}",
    )

# the identity Q = (1 + 2r)/3 is prior art; reproduced here only as a
# consistency check on the exact coordinates used above
for t in TRIPLES:
    x = desc(t)
    Q, r, _, _ = dial_exact(x)
    check(
        f"coordinate consistency Q = (1+2r)/3 on x={tuple(str(v) for v in x)}",
        Q == (1 + 2 * r) / 3,
        "prior art (charged-lepton DFT coordinate note); reproduced, not claimed",
    )


section("B. EXACT: flavour-universal running rescales a sector by ONE factor")

print("  Supplied condition (standard QCD, and already recorded in")
print("  docs/CKM_DOWN_TYPE_SCALE_CONVENTION_SUPPORT_NOTE_2026-04-22.md eq 5.6):")
print("  the MSbar mass anomalous dimension gamma_m depends on the coupling and")
print("  the active flavour number only -- not on which quark is being run.  So")
print("  on a fixed-flavour surface m_q(mu) = R(mu, mu_0) * m_q(mu_0) with ONE")
print("  R for every q in the sector.  Part A then applies with lam = R.")
print()

# exact rational stand-ins for R(mu, mu_0); the theorem is independent of R
R_FACTORS = [Fraction(9, 4), Fraction(4, 9), Fraction(121, 100), Fraction(1, 8)]

for t in TRIPLES[:4]:
    x = desc(t)
    m = tuple(v * v for v in x)                      # masses
    Q0, r0, C0, J0 = dial_exact(x)
    ok = True
    detail = ""
    for R in R_FACTORS:
        mr = tuple(R * v for v in m)                 # common-scale running
        # back to x-coordinates: x -> sqrt(R) * x.  Keep it exact by choosing
        # R = (p/q)^2 where possible; otherwise compare the mass-level ratios,
        # which is what the dial depends on.
        ratios0 = tuple(v / m[0] for v in m)
        ratios1 = tuple(v / mr[0] for v in mr)
        if ratios0 != ratios1:
            ok = False
            detail = f"R={R} changed the mass ratios"
            break
    check(
        f"x={tuple(str(v) for v in x)}: common R leaves every mass ratio fixed",
        ok,
        detail or "so the dial, a function of ratios alone, is fixed",
    )

# and the dial really is a function of the ratios alone: exact witness
for t in TRIPLES[:4]:
    x = desc(t)
    for mu in [Fraction(3, 2), Fraction(2, 7)]:
        xs = desc(tuple(mu * v for v in x))
        check(
            f"dial(x) == dial({mu}*x)",
            dial_exact(x) == dial_exact(xs),
            "the dial is a function of the mass ratios only",
        )


section("C. EXACT: unequal per-generation factors DO move the dial")

print("  A mixed-scale convention quotes different generations at different")
print("  reference scales.  That applies m_k -> lam_k m_k with lam_k NOT all")
print("  equal, which is outside Part A's hypothesis.  The converse below is")
print("  exact and constructive.")
print()

# Lemma (exact).  For x = (1, 1, 0) and factors mu_1, mu_2 on the first two
# coordinates, Q = (mu_1^2 + mu_2^2) / (mu_1 + mu_2)^2, which equals the
# unscaled value 1/2 iff (mu_1 - mu_2)^2 = 0, i.e. iff mu_1 = mu_2.
print("  Lemma.  On x = (1, 1, 0): Q(mu_1, mu_2) = (mu_1^2 + mu_2^2)/(mu_1+mu_2)^2,")
print("  and Q = 1/2 iff (mu_1 - mu_2)^2 = 0.  So ANY unequal pair of factors")
print("  moves Q on this triple.  Exact evaluations:")
print()

for mu1, mu2 in [(Fraction(1), Fraction(1)), (Fraction(1), Fraction(2)),
                 (Fraction(3, 2), Fraction(3, 2)), (Fraction(5, 4), Fraction(4, 5)),
                 (Fraction(10), Fraction(1))]:
    num = mu1 * mu1 + mu2 * mu2
    den = (mu1 + mu2) ** 2
    Qv = num / den
    equal = (mu1 == mu2)
    check(
        f"mu=({mu1},{mu2}): Q = {Qv}, unchanged from 1/2 -> {Qv == Fraction(1, 2)}",
        (Qv == Fraction(1, 2)) == equal,
        "witness triple x=(1,1,0); identity 2(mu1^2+mu2^2)-(mu1+mu2)^2 = (mu1-mu2)^2",
    )
    # the identity itself, exactly
    check(
        f"identity 2*num - den == (mu1-mu2)^2 at mu=({mu1},{mu2})",
        2 * num - den == (mu1 - mu2) ** 2,
    )

# a nondegenerate, strictly positive witness as well
xw = desc((Fraction(1), Fraction(1, 2), Fraction(1, 10)))
Qw, rw, Cw, Jw = dial_exact(xw)
for lam in [(Fraction(1), Fraction(2), Fraction(1)),
            (Fraction(1), Fraction(1), Fraction(4)),
            (Fraction(9, 4), Fraction(1), Fraction(1))]:
    xm = desc(tuple(l * v for l, v in zip(lam, xw)))
    Qm, rm, Cm, Jm = dial_exact(xm)
    check(
        f"unequal factors {tuple(str(l) for l in lam)} move the dial",
        (Qm, rm) != (Qw, rw),
        f"Q: {Qw} -> {Qm}   r: {rw} -> {rm}",
    )


section("D. COMPARATOR ONLY: what this means for the displayed quark numbers")

print("  Everything in Part D is a comparator.  It uses external PDG central")
print("  values and floating point, is not exact, is not a derivation step, and")
print("  supplies no premise.  Parts A-C stand without it.")
print()
print("  Inputs (PDG-style MSbar, as quoted -- i.e. at MIXED reference scales):")
print("    up-type   m_u(2 GeV)=2.16e-3, m_c(m_c)=1.27,  m_t(m_t)=162.5   GeV")
print("    down-type m_d(2 GeV)=4.67e-3, m_s(2 GeV)=93.4e-3, m_b(m_b)=4.18 GeV")
print("    alpha_s(M_Z) = 0.1180")
print()

Z3C = 1.2020569031595943
Z4C = math.pi ** 4 / 90
Z5C = 1.0369277551433699


def _beta(nf):
    return ((11 - 2 * nf / 3) / 4,
            (102 - 38 * nf / 3) / 16,
            (2857 / 2 - 5033 * nf / 18 + 325 * nf * nf / 54) / 64,
            (149753 / 6 + 3564 * Z3C
             - (1078361 / 162 + 6508 * Z3C / 27) * nf
             + (50065 / 162 + 6472 * Z3C / 81) * nf * nf
             + 1093 * nf ** 3 / 729) / 256)


def _gamma(nf):
    return (1.0,
            (202 / 3 - 20 * nf / 9) / 16,
            (1249 + (-2216 / 27 - 160 * Z3C / 3) * nf - 140 * nf * nf / 81) / 64,
            (4603055 / 162 + 135680 * Z3C / 27 - 8800 * Z5C
             + nf * (-91723 / 27 - 34192 * Z3C / 9 + 880 * Z4C + 18400 * Z5C / 9)
             + nf * nf * (5242 / 243 + 800 * Z3C / 9 - 160 * Z4C / 3)
             + nf ** 3 * (-332 / 243 + 64 * Z3C / 27)) / 256)


def _seg(a0, mu0, mu1, nf, steps=120):
    b = _beta(nf)
    g = _gamma(nf)

    def f(a):
        return (-a * a * (b[0] + b[1] * a + b[2] * a * a + b[3] * a ** 3),
                -(g[0] * a + g[1] * a * a + g[2] * a ** 3 + g[3] * a ** 4))

    t0, t1 = 2 * math.log(mu0), 2 * math.log(mu1)
    h = (t1 - t0) / steps
    a, lm = a0, 0.0
    for _ in range(steps):
        k1 = f(a)
        k2 = f(a + h * k1[0] / 2)
        k3 = f(a + h * k2[0] / 2)
        k4 = f(a + h * k3[0])
        a += h * (k1[0] + 2 * k2[0] + 2 * k3[0] + k4[0]) / 6
        lm += h * (k1[1] + 2 * k2[1] + 2 * k3[1] + k4[1]) / 6
    return a, lm


class _RG:
    """4-loop MSbar alpha_s and mass running with nf thresholds (comparator)."""

    def __init__(self, aS_MZ, mc, mb, mt, MZ=91.1876):
        self.mc, self.mb, self.mt, self.MZ = mc, mb, mt, MZ
        aZ = aS_MZ / math.pi
        self.aZ = aZ
        self.a_mb = _seg(aZ, MZ, mb, 5)[0]
        self.a_mc = _seg(self.a_mb, mb, mc, 4)[0]
        self.a_mt = _seg(aZ, MZ, mt, 5)[0]
        self._cache = {}

    def a_at(self, mu):
        if mu in self._cache:
            return self._cache[mu]
        if mu >= self.mt:
            v = _seg(self.a_mt, self.mt, mu, 6)[0]
        elif mu >= self.mb:
            v = _seg(self.a_mb, self.mb, mu, 5)[0]
        elif mu >= self.mc:
            v = _seg(self.a_mc, self.mc, mu, 4)[0]
        else:
            v = _seg(self.a_mc, self.mc, mu, 3)[0]
        self._cache[mu] = v
        return v

    def factor(self, mu0, mu1):
        lo, hi = min(mu0, mu1), max(mu0, mu1)
        pts = [lo] + [t for t in (self.mc, self.mb, self.mt) if lo < t < hi] + [hi]
        lnr = 0.0
        for i in range(len(pts) - 1):
            mid = math.sqrt(pts[i] * pts[i + 1])
            nf = 3 + sum(1 for t in (self.mc, self.mb, self.mt) if mid > t)
            lnr += _seg(self.a_at(pts[i]), pts[i], pts[i + 1], nf)[1]
        return math.exp(lnr if mu1 > mu0 else -lnr)


def _dial_f(masses):
    x = sorted((math.sqrt(m) for m in masses), reverse=True)
    S = sum(x)
    Q = sum(masses) / (S * S)
    a = S / 3
    C = (x[0] - (x[1] + x[2]) / 2) / 3 / a
    Jm = math.sqrt(3) * (x[2] - x[1]) / 6 / a
    return Q, C * C + Jm * Jm, math.atan2(Jm, C)


PARS = dict(aS=0.1180, mu=2.16e-3, md=4.67e-3, ms=93.4e-3,
            mc=1.27, mb=4.18, mt=162.5)
ERRS = dict(aS=0.0009, mu=0.38e-3, md=0.33e-3, ms=6.0e-3,
            mc=0.02, mb=0.025, mt=1.8)


def _sector_dials(p, mu_c):
    R = _RG(p['aS'], p['mc'], p['mb'], p['mt'])
    up = [p['mu'] * R.factor(2.0, mu_c),
          p['mc'] * R.factor(p['mc'], mu_c),
          p['mt'] * R.factor(p['mt'], mu_c)]
    dn = [p['md'] * R.factor(2.0, mu_c),
          p['ms'] * R.factor(2.0, mu_c),
          p['mb'] * R.factor(p['mb'], mu_c)]
    return _dial_f(up), _dial_f(dn)


print("  D1. The dial computed at SIX common scales spanning three decades:")
print(f"    {'mu [GeV]':>10} | {'Q_up':>9} {'r_up':>9} | {'Q_down':>9} {'r_down':>9}")
tab = []
for mu_c in (2.0, 4.18, 10.0, 91.1876, 162.5, 1000.0):
    (Qu, ru, du), (Qd, rd, dd) = _sector_dials(PARS, mu_c)
    tab.append((mu_c, Qu, ru, Qd, rd))
    print(f"    {mu_c:10.4f} | {Qu:9.6f} {ru:9.6f} | {Qd:9.6f} {rd:9.6f}")
spread_u = max(t[1] for t in tab) - min(t[1] for t in tab)
spread_d = max(t[3] for t in tab) - min(t[3] for t in tab)
check("comparator: Q_up spread over the six common scales is float noise",
      spread_u < 1e-10, f"spread = {spread_u:.2e}")
check("comparator: Q_down spread over the six common scales is float noise",
      spread_d < 1e-10, f"spread = {spread_d:.2e}")

print()
print("  D2. The SAME inputs read at their quoted (mixed) scales, which is the")
print("      convention of QUARK_MASS_SPECTRUM_KOIDE_SCHEME_OPEN_GATE_NOTE_2026-05-26:")
mixQu, mixru, _ = _dial_f([PARS['mu'], PARS['mc'], PARS['mt']])
mixQd, mixrd, _ = _dial_f([PARS['md'], PARS['ms'], PARS['mb']])
ogQu, ogru, _ = _dial_f([2.16e-3, 1.27, 173.0])       # note's own list, pole top
ogQd, ogrd, _ = _dial_f([4.67e-3, 93.4e-3, 4.18])
print(f"    mixed-scale, MSbar top : Q_up={mixQu:.6f} r_up={mixru:.6f} | "
      f"Q_down={mixQd:.6f} r_down={mixrd:.6f}")
print(f"    open-gate note's list  : Q_up={ogQu:.6f} r_up={ogru:.6f} | "
      f"Q_down={ogQd:.6f} r_down={ogrd:.6f}")
inv = tab[3]
print(f"    common-scale (invariant): Q_up={inv[1]:.6f} r_up={inv[2]:.6f} | "
      f"Q_down={inv[3]:.6f} r_down={inv[4]:.6f}")
check("comparator: the open-gate note's displayed r_up reproduces from its own list",
      abs(ogru - 0.773642) < 5e-4, f"recomputed {ogru:.6f} vs displayed 0.773642")
check("comparator: the open-gate note's displayed r_down reproduces from its own list",
      abs(ogrd - 0.597141) < 5e-4, f"recomputed {ogrd:.6f} vs displayed 0.597141")
check("comparator: mixed-scale and common-scale dials differ well beyond float noise",
      abs(ogru - inv[2]) > 1e-2 and abs(ogrd - inv[4]) > 1e-2,
      f"delta r_up = {inv[2]-ogru:+.4f}, delta r_down = {inv[4]-ogrd:+.4f}")

print()
print("  D3. Linear error propagation on the common-scale dial (mu = M_Z):")
base = _sector_dials(PARS, 91.1876)
var = {'Qu': 0.0, 'Qd': 0.0, 'ru': 0.0, 'rd': 0.0}
for k, e in ERRS.items():
    p = dict(PARS)
    p[k] = PARS[k] + e
    (Qu, ru, _), (Qd, rd, _) = _sector_dials(p, 91.1876)
    var['Qu'] += (Qu - base[0][0]) ** 2
    var['ru'] += (ru - base[0][1]) ** 2
    var['Qd'] += (Qd - base[1][0]) ** 2
    var['rd'] += (rd - base[1][1]) ** 2
sQu, sru = math.sqrt(var['Qu']), math.sqrt(var['ru'])
sQd, srd = math.sqrt(var['Qd']), math.sqrt(var['rd'])
print(f"    Q_up   = {base[0][0]:.6f} +- {sQu:.6f}      r_up   = {base[0][1]:.6f} +- {sru:.6f}")
print(f"    Q_down = {base[1][0]:.6f} +- {sQd:.6f}      r_down = {base[1][1]:.6f} +- {srd:.6f}")
print(f"    charged leptons (no QCD running): Q = {_dial_f([0.510998950e-3, 105.6583755e-3, 1.77686])[0]:.9f}")
pull_u = abs(base[0][1] - 0.5) / sru
pull_d = abs(base[1][1] - 0.5) / srd
print(f"    distance of r_up   from the leptonic 1/2: {pull_u:.0f} sigma")
print(f"    distance of r_down from the leptonic 1/2: {pull_d:.0f} sigma")
check("comparator: the three sector dials are not a common value",
      pull_u > 20 and pull_d > 5,
      "displayed as a comparator only; this runner asserts no no-go")


section("E. Scope guards")

if NOTE.exists():
    text = NOTE.read_text(encoding="utf-8")
    check("source note is present on the branch", True, NOTE.name)
    for needle, why in [
        ("derives no quark mass", "note disclaims a quark-mass derivation"),
        ("does not close", "note disclaims closing the open gate"),
        ("comparator", "note marks its numerics as comparators"),
        ("prior art", "note defers homogeneity and flavour-universality to prior art"),
        ("proposed_retained", "note uses author-side status vocabulary only"),
    ]:
        check(f"note contains discipline marker: {needle!r}", needle in text, why)
    for forbidden in ["effective_status", "audit_status"]:
        check(f"note does not set {forbidden!r}", forbidden not in text,
              "status authority stays with the independent audit lane")
else:
    check("source note is present on the branch", False, f"missing: {NOTE}")


print()
print("=" * 64)
print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
print("=" * 64)
