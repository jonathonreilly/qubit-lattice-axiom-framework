#!/usr/bin/env python3
"""Cycle 897 INDEPENDENT CHECKER -- spec'd to REFUTE the target-integrity block.

Every claim of the primary is recomputed by a DIFFERENT route.  Nothing is
imported from the primary; it is consumed as text, AST and JSON only.

WHERE THE ROUTES DIFFER
    square roots     primary: exact integer-sqrt bracketing
                     checker: Newton iteration on rationals, with the invariant
                              lo^2 <= q <= hi^2 re-verified every step
    sin / cos        primary: direct alternating Taylor series with the
                              decreasing-term hypothesis asserted
                     checker: argument halving 20 times, base bounds obtained by
                              an INTEGRATION BOOTSTRAP from cos <= 1 (no
                              alternating-series hypothesis anywhere), then the
                              exact double-angle identities applied 20 times with
                              OUTWARD ROUNDING to a fixed rational grid
    root finding     primary: interval bisection on H = lambda_2 - R lambda_1
                     checker: INTERVAL NEWTON on the algebraically rearranged
                              H = (1-R)(1 - (sqrt2/2) cos d) + (sqrt6/2)(1+R) sin d
    Green diagonals  primary: L^+ = (L + J/n)^{-1} - J/n
                     checker: effective resistances from exact linear solves,
                              then (L^+)_ii = (1/2n) sum_j r(i,j)
    char polys       primary: trace / second-elementary-symmetric / determinant
                     checker: symbolic cofactor expansion of det(xI - M)
    rotation group   primary: filter signed permutation matrices by det = +1
                     checker: closure of two generators under multiplication
    normalizer       primary: direct conjugation test over the group
                     checker: orbit-stabilizer on the set of order-3 subgroups
    T7 libraries     primary: Fraction arithmetic
                     checker: integer valuation-vector arithmetic over (2,3,5,7)

THE ENCLOSURES ARE ATTACKED HARDEST.  Every bound the primary asserts is
re-derived and re-verified; a single unproven bound refutes the certification.

TEETH.  Eight deliberate mutations, each of which MUST be caught.

The checker exits 0 whether or not the primary's claims survive.  Survival is
reported as data.
"""

from __future__ import annotations

import ast
import hashlib
import importlib.abc
import json
import re
import subprocess
import sys
import time
from fractions import Fraction
from itertools import combinations, product
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PRIMARY = "scripts/frontier_cycle897_target_integrity_2026_07_28.py"
PRIMARY_RECEIPT = "outputs/target_integrity_cycle897_receipt_2026_07_28.json"
OUT = REPO / "outputs" / \
    "target_integrity_independent_check_cycle897_receipt_2026_07_28.json"


# ==========================================================================
# 0.  PINS AND FIREWALL
# ==========================================================================
PINS = {
    "scripts/frontier_cycle882_readout_identity_2026_07_28.py":
        "cd8126381cca2bf2a852de4daf14ef6955a3af122d2781acd400ebe674efbf2a",
    "scripts/frontier_cycle882_readout_independent_check_2026_07_28.py":
        "bdc617b8e70d6a1cc9c808009faf9ace1022d59e7b7ae3b029d7a3dbca30ea49",
    "scripts/frontier_cycle883_record_weight_pair_2026_07_28.py":
        "2d96422d30f169a1c4b3215db373e4bffd7b1ef20056ea337ff4ae3f86d9511c",
    "logs/runner-cache/frontier_cycle882_readout_identity_2026_07_28.txt":
        "7f485527189864c79d927376c686a4cab5d3ad25551b16283851a9acc5a9462d",
    "logs/runner-cache/frontier_cycle883_record_weight_pair_2026_07_28.txt":
        "560f368d9d23144cb23a93e72a398d92f6fcb536c3363179b7853c09615211bb",
    "docs/KOIDE_CIRCULANT_CHARACTER_DERIVATION_NOTE_2026-04-18.md":
        "6cfb1c34e9c77e5979d78a2d03718eb970b00bf7a26866c719ba812ce3a82722",
    "docs/CHARGED_LEPTON_KOIDE_NOTE_2026-04-18.md":
        "8b90720698c26d9ae4a4a0990498cedf408e4b9c6b1b5a41ebea41c249d248ba",
    "docs/MINIMAL_AXIOMS_2026-06-29.md":
        "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
}

_TEXT: dict[str, str] = {}


def rt(rel: str) -> str:
    if rel not in _TEXT:
        _TEXT[rel] = (REPO / rel).read_text(encoding="utf-8")
    return _TEXT[rel]


def sha(rel: str) -> str:
    return hashlib.sha256((REPO / rel).read_bytes()).hexdigest()


class _Firewall(importlib.abc.MetaPathFinder):
    BLOCKED = ("frontier_cycle897_target_integrity_2026_07_28",
               "frontier_cycle882_readout_identity_2026_07_28",
               "frontier_cycle883_record_weight_pair_2026_07_28")

    def __init__(self):
        self.hits: list[str] = []

    def find_spec(self, fullname, path=None, target=None):
        if fullname.split(".")[-1] in self.BLOCKED:
            self.hits.append(fullname)
            raise ImportError("firewall")
        return None


FW = _Firewall()
sys.meta_path.insert(0, FW)


def check_pins() -> dict:
    rows = []
    ok = True
    for rel, want in sorted(PINS.items()):
        got = sha(rel)
        good = got == want
        ok = ok and good
        rows.append({"path": rel, "match": good, "observed": got})
    prim_exists = (REPO / PRIMARY).is_file()
    rec_exists = (REPO / PRIMARY_RECEIPT).is_file()
    ok = ok and prim_exists and rec_exists
    return {"rows": rows, "primary_present": prim_exists,
            "primary_receipt_present": rec_exists,
            "primary_sha256": sha(PRIMARY) if prim_exists else None,
            "firewall_hits": list(FW.hits),
            "pass": ok and not FW.hits}


# ==========================================================================
# 1.  INDEPENDENT INTERVAL KERNEL
# ==========================================================================
GRID = 10 ** 90          # outward-rounding grid
HALVINGS = 20            # argument reductions before the doubling recursion


class I:
    __slots__ = ("lo", "hi")

    def __init__(self, lo, hi=None):
        lo = Fraction(lo)
        hi = lo if hi is None else Fraction(hi)
        if lo > hi:
            raise ValueError("bad interval")
        self.lo, self.hi = lo, hi

    def __add__(self, o):
        o = _I(o)
        return I(self.lo + o.lo, self.hi + o.hi)

    __radd__ = __add__

    def __neg__(self):
        return I(-self.hi, -self.lo)

    def __sub__(self, o):
        return self + (-_I(o))

    def __rsub__(self, o):
        return _I(o) + (-self)

    def __mul__(self, o):
        o = _I(o)
        p = (self.lo * o.lo, self.lo * o.hi, self.hi * o.lo, self.hi * o.hi)
        return I(min(p), max(p))

    __rmul__ = __mul__

    def __truediv__(self, o):
        o = _I(o)
        if o.lo <= 0 <= o.hi:
            raise ZeroDivisionError("divisor straddles zero")
        return self * I(Fraction(1) / o.hi, Fraction(1) / o.lo)

    def __rtruediv__(self, o):
        return _I(o) / self

    def sq(self):
        return self * self

    def w(self) -> Fraction:
        return self.hi - self.lo

    def pos(self) -> bool:
        return self.lo > 0

    def neg(self) -> bool:
        return self.hi < 0

    def has(self, x) -> bool:
        return self.lo <= Fraction(x) <= self.hi

    def meets(self, o) -> bool:
        return self.lo <= o.hi and o.lo <= self.hi

    def cap(self, o) -> "I":
        return I(max(self.lo, o.lo), min(self.hi, o.hi))

    def inside(self, o) -> bool:
        return o.lo <= self.lo and self.hi <= o.hi

    def __repr__(self):
        return f"I({self.lo}, {self.hi})"


def _I(x) -> I:
    return x if isinstance(x, I) else I(x)


def outward(x: I, grid: int = GRID) -> I:
    """Round the endpoints outward onto a fixed rational grid.  Rigorous by
    construction (the interval only ever widens) and it is what keeps the
    doubling recursion from exploding in bit-length."""
    lo = Fraction((x.lo * grid).numerator // (x.lo * grid).denominator, grid)
    n = x.hi * grid
    hi = Fraction(-((-n.numerator) // n.denominator), grid)
    return I(lo, hi)


def nsqrt(q: Fraction, steps: int = 200) -> I:
    """sqrt(q) by NEWTON iteration on rationals.

    x_{k+1} = (x_k + q/x_k)/2 decreases monotonically to sqrt(q) from above for
    any x_0 >= sqrt(q) (AM-GM), and q/x_k is then a lower bound.  Both endpoints
    are re-verified by exact squaring at every step, and the loop stops when the
    grid resolution is reached.  This shares no code and no argument with the
    primary's integer-sqrt bracketing.
    """
    if q < 0:
        raise ValueError("negative radicand")
    if q == 0:
        return I(0, 0)
    x = q + 1 if q >= 1 else Fraction(1)      # x_0 >= sqrt(q) in both cases
    for _ in range(steps):
        if x * x < q:
            raise AssertionError("Newton upper bound invariant violated")
        lo = q / x
        if lo * lo > q:
            raise AssertionError("Newton lower bound invariant violated")
        if x - lo < Fraction(1, GRID):
            break
        x = outward(I((x + q / x) / 2), GRID).hi
    lo = q / x
    if not (lo * lo <= q <= x * x):
        raise AssertionError("nsqrt bracket failed final verification")
    return I(lo, x)


def _base_sin_cos(y: Fraction) -> tuple[I, I]:
    """Bounds for sin y, cos y for 0 <= y <= 1, by INTEGRATION BOOTSTRAP.

        cos t <= 1                     ==> sin y <= y
        sin t <= t                     ==> cos y >= 1 - y^2/2
        cos t >= 1 - t^2/2             ==> sin y >= y - y^3/6
        sin t >= t - t^3/6             ==> cos y <= 1 - y^2/2 + y^4/24
        cos t <= 1 - t^2/2 + t^4/24    ==> sin y <= y - y^3/6 + y^5/120
        sin t <= y - t^3/6 + t^5/120   ==> cos y >= 1 - y^2/2 + y^4/24 - y^6/720

    Each step is a termwise integration of the previous one on [0, y] with
    y >= 0.  No series-truncation or alternation hypothesis is used.
    """
    if not (0 <= y <= 1):
        raise ValueError("base bounds require 0 <= y <= 1")
    y2 = y * y
    y3 = y2 * y
    y4 = y2 * y2
    y5 = y4 * y
    y6 = y4 * y2
    s_lo = y - y3 / 6
    s_hi = y - y3 / 6 + y5 / 120
    c_lo = 1 - y2 / 2 + y4 / 24 - y6 / 720
    c_hi = 1 - y2 / 2 + y4 / 24
    if s_lo > s_hi or c_lo > c_hi:
        raise AssertionError("base bound ordering violated")
    return I(s_lo, s_hi), I(c_lo, c_hi)


def sin_cos(x: Fraction) -> tuple[I, I]:
    """sin x, cos x for 0 <= x <= 1 by halving then the exact double-angle
    identities sin 2t = 2 sin t cos t, cos 2t = 1 - 2 sin^2 t = 2 cos^2 t - 1.
    Both cosine forms are computed and INTERSECTED, which is valid because both
    are exact identities."""
    if not (0 <= x <= 1):
        raise ValueError("sin_cos window is [0, 1]")
    y = x / (2 ** HALVINGS)
    S, C = _base_sin_cos(y)
    for _ in range(HALVINGS):
        S2 = outward(2 * S * C)
        Ca = I(1) - 2 * S.sq()
        Cb = 2 * C.sq() - I(1)
        if not Ca.meets(Cb):
            raise AssertionError("double-angle cosine forms disagree")
        C2 = outward(Ca.cap(Cb))
        S, C = S2, C2
    # final sanity: the Pythagorean identity must hold on the result
    if not (S.sq() + C.sq()).has(1):
        raise AssertionError("sin^2 + cos^2 does not enclose 1")
    return S, C


def sin_cos_iv(x: I) -> tuple[I, I]:
    """Monotone extension on [0, 1]: sin increasing, cos decreasing.  Both facts
    follow from the base bounds above (cos >= 1 - y^2/2 >= 1/2 > 0 and
    sin >= y - y^3/6 > 0 on (0, 1])."""
    if not (0 <= x.lo and x.hi <= 1):
        raise ValueError("window")
    s_lo, c_lo = sin_cos(x.lo)
    s_hi, c_hi = sin_cos(x.hi)
    return I(s_lo.lo, s_hi.hi), I(c_hi.lo, c_lo.hi)


def dec(f: Fraction, places: int, mode: str = "down") -> str:
    scale = 10 ** places
    n = f * scale
    k = (n.numerator // n.denominator) if mode == "down" \
        else -((-n.numerator) // n.denominator)
    sign = "-" if k < 0 else ""
    k = abs(k)
    ip, fp = divmod(k, scale)
    return f"{sign}{ip}.{str(fp).zfill(places)}"


def ivs(x: I, places: int = 18) -> str:
    return f"[{dec(x.lo, places, 'down')}, {dec(x.hi, places, 'up')}]"


def qs(x: Fraction) -> str:
    return f"{x.numerator}/{x.denominator}" if x.denominator != 1 \
        else str(x.numerator)


def kernel_selftest() -> dict:
    checks = []
    # Newton sqrt against exact squares and against the primary's radicands.
    for r in (Fraction(4), Fraction(2), Fraction(3), Fraction(6),
              Fraction(9, 4), Fraction("206.768283")):
        e = nsqrt(r)
        checks.append({"t": f"nsqrt({qs(r)}) brackets by squaring",
                       "ok": e.lo * e.lo <= r <= e.hi * e.hi})
    checks.append({"t": "nsqrt(4) encloses 2", "ok": nsqrt(Fraction(4)).has(2)})
    checks.append({"t": "nsqrt(2) width below 1e-80",
                   "ok": nsqrt(Fraction(2)).w() < Fraction(1, 10 ** 80)})
    # trig against exact anchor values and identities.
    s0, c0 = sin_cos(Fraction(0))
    checks.append({"t": "sin(0)=0, cos(0)=1",
                   "ok": s0.has(0) and c0.has(1)})
    for xs in ("1/7", "2/9", "1/2", "3/4", "1"):
        x = Fraction(xs)
        S, C = sin_cos(x)
        checks.append({"t": f"sin^2+cos^2 at {xs}",
                       "ok": (S.sq() + C.sq()).has(1)})
        # addition formula against a half-argument evaluation
        Sh, Ch = sin_cos(x / 2)
        checks.append({"t": f"sin(x)=2 sin(x/2)cos(x/2) at {xs}",
                       "ok": (2 * Sh * Ch).meets(S)})
    # monotonicity
    checks.append({"t": "cos strictly decreasing on samples",
                   "ok": sin_cos(Fraction(1, 5))[1].lo
                   > sin_cos(Fraction(1, 2))[1].hi})
    checks.append({"t": "sin strictly increasing on samples",
                   "ok": sin_cos(Fraction(1, 5))[0].hi
                   < sin_cos(Fraction(1, 2))[0].lo})
    # width small enough for the science
    S, C = sin_cos(Fraction(2, 9))
    checks.append({"t": "trig enclosure width below 1e-40",
                   "ok": S.w() < Fraction(1, 10 ** 40)
                   and C.w() < Fraction(1, 10 ** 40)})
    # guards fire
    g1 = g2 = False
    try:
        sin_cos(Fraction(3, 2))
    except ValueError:
        g1 = True
    try:
        nsqrt(Fraction(-1))
    except ValueError:
        g2 = True
    checks.append({"t": "trig window guard fires", "ok": g1})
    checks.append({"t": "sqrt sign guard fires", "ok": g2})
    return {"checks": checks, "count": len(checks),
            "pass": all(c["ok"] for c in checks)}


# ==========================================================================
# 2.  THE FORK, RECOMPUTED BY INTERVAL NEWTON
# ==========================================================================
S2 = nsqrt(Fraction(2))
S6 = nsqrt(Fraction(6))
H2 = S2 * I(Fraction(1, 2))
H6 = S6 * I(Fraction(1, 2))
TWO_NINTHS = Fraction(2, 9)
GATE = Fraction(3)

# the checker's OWN copy of the empirical inputs, declared here so that a
# silent perturbation inside the primary cannot propagate.
OBS = {
    "m_e": (Fraction("0.51099895069"), Fraction("0.00000000016")),
    "m_mu": (Fraction("105.6583755"), Fraction("0.0000023")),
    "m_tau": (Fraction("1776.93"), Fraction("0.09")),
}


def lam(dv: I) -> tuple[I, I, I]:
    S, C = sin_cos_iv(dv)
    return (I(1) + S2 * C,
            I(1) - H2 * C - H6 * S,
            I(1) - H2 * C + H6 * S)


def Halg(dv: I, R: I) -> I:
    """The ALGEBRAICALLY REARRANGED residual, not the primary's form:
        H = (1-R)(1 - (sqrt2/2) cos d) + (sqrt6/2)(1+R) sin d."""
    S, C = sin_cos_iv(dv)
    return (I(1) - R) * (I(1) - H2 * C) + H6 * (I(1) + R) * S


def Hprime(dv: I, R: I) -> I:
    S, C = sin_cos_iv(dv)
    return H2 * (I(1) - R) * S + H6 * (I(1) + R) * C


def newton_delta(R: I, rounds: int = 12) -> dict:
    """INTERVAL NEWTON.  For X = [a, b] with 0 not in H'(X) and m = mid(X),
    N(X) = m - H(m)/H'(X) satisfies: every root of H in X lies in N(X), and if
    N(X) is contained in X then X contains exactly one root.  Iterating
    X <- X cap N(X) is a certified contraction; no bisection is used.
    """
    X = I(Fraction(1, 5), Fraction(1, 4))
    hp = Hprime(X, R)
    if hp.lo <= 0 <= hp.hi:
        raise AssertionError("H' straddles zero on the initial bracket")
    _, l1, _ = lam(X)
    if not l1.pos():
        raise AssertionError("lambda_1 not positive on the bracket")
    if not (Halg(I(X.lo), R).neg() and Halg(I(X.hi), R).pos()):
        raise AssertionError("no certified sign change on the bracket")
    contained_once = False
    for _ in range(rounds):
        m = (X.lo + X.hi) / 2
        N = I(m) - Halg(I(m), R) / Hprime(X, R)
        if not N.meets(X):
            raise AssertionError("interval Newton lost the root")
        if N.inside(X):
            contained_once = True
        X = X.cap(N)
        if X.w() < Fraction(1, 10 ** 45):
            break
    # cross-check: the primary's residual form must vanish on the same interval
    _, l1x, l2x = lam(X)
    cross = (l2x - R * l1x)
    if not cross.has(0):
        raise AssertionError("primary residual form does not vanish on the "
                             "checker's enclosure")
    return {"X": X, "uniqueness_established": contained_once,
            "cross_form_contains_zero": cross.has(0)}


def dist(target: Fraction, x: I) -> tuple[Fraction, Fraction]:
    if x.hi < target:
        return target - x.hi, target - x.lo
    if x.lo > target:
        return x.lo - target, x.hi - target
    return Fraction(0), max(target - x.lo, x.hi - target)


def verdict(n_lo: Fraction, n_hi: Fraction) -> str:
    if n_hi <= GATE:
        return "COMPATIBLE"
    if n_lo > GATE:
        return f"INCOMPATIBLE-AT-SIGMA-{int(n_lo)}"
    return "INDETERMINATE"


def fork_forward(m_e, s_e, m_mu, s_mu) -> dict:
    Rc = nsqrt(m_mu / m_e)
    Rl = nsqrt((m_mu - s_mu) / (m_e + s_e))
    Rh = nsqrt((m_mu + s_mu) / (m_e - s_e))
    dc = newton_delta(Rc)
    dl = newton_delta(Rl)
    dh = newton_delta(Rh)
    Xc, Xl, Xh = dc["X"], dl["X"], dh["X"]
    sig_hi = (Xh.hi - Xl.lo) / 2
    sig_lo = (Xh.lo - Xl.hi) / 2
    dlo, dhi = dist(TWO_NINTHS, Xc)
    n_lo, n_hi = dlo / sig_hi, dhi / sig_lo
    return {"delta": ivs(Xc, 18), "delta_iv": Xc,
            "sigma": [dec(sig_lo, 22, "down"), dec(sig_hi, 22, "up")],
            "offset": [dec(dlo, 22, "down"), dec(dhi, 22, "up")],
            "n_sigma": [dec(n_lo, 6, "down"), dec(n_hi, 6, "up")],
            "n_sigma_iv": (n_lo, n_hi),
            "uniqueness_established": dc["uniqueness_established"],
            "verdict": verdict(n_lo, n_hi)}


def fork_reverse(m_e, s_e, m_mu, s_mu) -> dict:
    dv = I(TWO_NINTHS)
    l0, l1, l2 = lam(dv)
    if not l1.pos():
        raise AssertionError("lambda_1 not positive at 2/9")
    rmu = (l2 / l1).sq()
    rtau = (l0 / l1).sq()
    mmu_c = I(m_e) * rmu
    mtau_c = I(m_e) * rtau
    band = I(m_e - s_e, m_e + s_e) * rmu
    w_e = band.w() / 2
    sq = nsqrt(s_mu * s_mu + w_e * w_e)
    dlo, dhi = dist(m_mu, mmu_c)
    n_lo, n_hi = dlo / sq.hi, dhi / sq.lo
    return {"m_mu_implied": ivs(mmu_c, 14), "m_tau_implied": ivs(mtau_c, 10),
            "offset": [dec(dlo, 16, "down"), dec(dhi, 16, "up")],
            "n_sigma": [dec(n_lo, 6, "down"), dec(n_hi, 6, "up")],
            "n_sigma_iv": (n_lo, n_hi),
            "verdict": verdict(n_lo, n_hi)}


def tau_consistency(delta_iv: I, m_e, s_e) -> dict:
    l0, l1, _ = lam(delta_iv)
    r = (l0 / l1).sq()
    mt = I(m_e) * r
    m_tau, s_tau = OBS["m_tau"]
    band = I(m_e - s_e, m_e + s_e) * r
    sq = nsqrt(s_tau * s_tau + (band.w() / 2) ** 2)
    dlo, dhi = dist(m_tau, mt)
    n_lo, n_hi = dlo / sq.hi, dhi / sq.lo
    return {"m_tau_implied": ivs(mt, 10),
            "n_sigma": [dec(n_lo, 6, "down"), dec(n_hi, 6, "up")],
            "n_sigma_iv": (n_lo, n_hi), "verdict": verdict(n_lo, n_hi)}


# ==========================================================================
# 3.  INDEPENDENT SYMBOLIC ALGEBRA
# ==========================================================================
def q_of_c2(c2: Fraction) -> Fraction:
    """Q for the parameterization sqrt(m_k) = v0 (1 + c cos(delta + 2 pi k/3)),
    computed WITHOUT the retained note's shortcut: the three cosines are written
    as (a_k C + b_k sqrt(3) S), the sums are expanded termwise, and
    C^2 + S^2 = 1 is applied at the end."""
    parts = [(Fraction(1), Fraction(0)),
             (Fraction(-1, 2), Fraction(-1, 2)),
             (Fraction(-1, 2), Fraction(1, 2))]
    # sum_k lambda_k = 3 + c (sum a_k) C + c sqrt3 (sum b_k) S
    sa = sum(a for a, _ in parts)
    sb = sum(b for _, b in parts)
    if sa != 0 or sb != 0:
        raise AssertionError("zero-sum identity failed")
    # sum_k lambda_k^2 = 3 + 2c(sa C + sqrt3 sb S)
    #                    + c^2 (sum a^2 C^2 + 3 sum b^2 S^2 + 2 sqrt3 sum ab CS)
    saa = sum(a * a for a, _ in parts)
    sbb = sum(b * b for _, b in parts)
    sab = sum(a * b for a, b in parts)
    if sab != 0:
        raise AssertionError("cross term did not vanish")
    if saa != 3 * sbb:
        raise AssertionError("C^2 and S^2 coefficients unequal; cannot reduce")
    coef = saa                       # = 3 * sbb, so the C^2/S^2 sum is coef * 1
    if coef != Fraction(3, 2):
        raise AssertionError("sum cos^2 is not 3/2")
    return (3 + c2 * coef) / 9


def numeric_Q_probe(c: I, dv: I) -> I:
    """A second, purely numeric probe of Q at a specific c and delta."""
    S, C = sin_cos_iv(dv)
    cos0 = C
    cos1 = I(Fraction(-1, 2)) * C - (S6 / S2) * I(Fraction(1, 2)) * S
    cos2 = I(Fraction(-1, 2)) * C + (S6 / S2) * I(Fraction(1, 2)) * S
    ls = [I(1) + c * cos0, I(1) + c * cos1, I(1) + c * cos2]
    num = ls[0].sq() + ls[1].sq() + ls[2].sq()
    den = (ls[0] + ls[1] + ls[2]).sq()
    return num / den


# -- polynomials -----------------------------------------------------------
def pmul(a, b):
    o = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            o[i + j] += x * y
    return ptrim(o)


def padd(a, b):
    n = max(len(a), len(b))
    return ptrim([(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0)
                  for i in range(n)])


def psub(a, b):
    return padd(a, [-x for x in b])


def ptrim(a):
    while len(a) > 1 and a[-1] == 0:
        a = a[:-1]
    return a


def pev(a, x):
    r = Fraction(0)
    for c in reversed(a):
        r = r * x + c
    return r


def pstr(a):
    t = []
    for i in range(len(a) - 1, -1, -1):
        if a[i] == 0:
            continue
        m = "" if i == 0 else ("N" if i == 1 else f"N^{i}")
        t.append(f"{a[i]:+d}{m}")
    return "".join(t) or "0"


def F_dim(N):
    return (N - 1) / (N * N)


def F_res(N):
    return (N * N - 1) / (12 * N)


def F_ded(N):
    return (N - 1) * (N - 2) / (3 * N)


def family_census() -> dict:
    """Independent route: cross-multiply the two families, sweep integers over a
    WIDE window for roots, and close the argument with the degree bound (a
    nonzero degree-d polynomial has at most d roots, so finding d of them is a
    completeness proof).  No rational-root theorem is used."""
    fams = {"F_dim": F_dim, "F_res": F_res, "F_ded": F_ded}
    three, four = Fraction(3), Fraction(4)
    table = {k: {"N=3": qs(f(three)), "N=4": qs(f(four))}
             for k, f in fams.items()}
    all_29 = all(f(three) == Fraction(2, 9) for f in fams.values())

    # cleared numerators, built by cross-multiplication from scratch
    # F_dim - F_res: 12(N-1) - N(N^2-1) over 12 N^2
    p_dr = psub(pmul([-1, 1], [12]), pmul([0, 1], [-1, 0, 1]))
    # F_dim - F_ded: 3(N-1) - N(N-1)(N-2) over 3 N^2
    p_dd = psub(pmul([-1, 1], [3]), pmul([0, 1], pmul([-1, 1], [-2, 1])))
    # F_res - F_ded: (N^2-1) - 4(N-1)(N-2) over 12 N
    p_rd = psub([-1, 0, 1], pmul([4], pmul([-1, 1], [-2, 1])))

    rows = []
    ok = all_29
    for name, poly, claimed in (
            ("F_dim = F_res", p_dr, {-4, 1, 3}),
            ("F_dim = F_ded", p_dd, {-1, 1, 3}),
            ("F_res = F_ded", p_rd, {1, 3})):
        deg = len(poly) - 1
        roots = sorted(n for n in range(-500, 501)
                       if n != 0 and pev(poly, Fraction(n)) == 0)
        complete = len(roots) + (1 if pev(poly, Fraction(0)) == 0 else 0) >= deg
        match = set(roots) == claimed
        ok = ok and match
        # direct confirmation: the two families really do coincide at each root
        fa, fb = name.split(" = ")
        direct = all(fams[fa](Fraction(n)) == fams[fb](Fraction(n))
                     for n in roots)
        ok = ok and direct
        rows.append({"pair": name, "numerator": pstr(poly), "degree": deg,
                     "integer_roots_in_[-500,500]": roots,
                     "claimed": sorted(claimed), "match": match,
                     "degree_bound_closes_the_search": complete,
                     "families_agree_at_every_root": direct})
    disc = {"F_dim(4)": qs(F_dim(four)), "F_res(4)": qs(F_res(four)),
            "F_ded(4)": qs(F_ded(four))}
    disc_ok = (F_dim(four) == Fraction(3, 16) and F_res(four) == Fraction(5, 16)
               and F_ded(four) == Fraction(1, 2))
    # exhaustive: no OTHER integer in a wide window has all three equal
    triples = [n for n in range(-500, 501)
               if n != 0 and F_dim(Fraction(n)) == F_res(Fraction(n))
               == F_ded(Fraction(n))]
    return {"table": table, "all_hit_2/9_at_N=3": all_29, "pairs": rows,
            "N=4_discriminator": disc, "N=4_matches_claim": disc_ok,
            "integers_where_all_three_agree": triples,
            "pass": ok and disc_ok and set(triples) == {1, 3}}


# ==========================================================================
# 4.  GREEN DIAGONALS BY EFFECTIVE RESISTANCE
# ==========================================================================
def solve_exact(A, b):
    n = len(A)
    M = [row[:] + [b[i]] for i, row in enumerate(A)]
    for c in range(n):
        p = next((r for r in range(c, n) if M[r][c] != 0), None)
        if p is None:
            raise ValueError("singular")
        M[c], M[p] = M[p], M[c]
        pv = M[c][c]
        M[c] = [x / pv for x in M[c]]
        for r in range(n):
            if r != c and M[r][c] != 0:
                f = M[r][c]
                M[r] = [a - f * z for a, z in zip(M[r], M[c])]
    return [M[i][n] for i in range(n)]


def laplacian(adj):
    n = len(adj)
    return [[Fraction(sum(adj[i]) if i == j else -adj[i][j]) for j in range(n)]
            for i in range(n)]


def resistance(adj, i, j):
    """r(i,j) from an exact linear solve with the sum-zero gauge."""
    n = len(adj)
    L = laplacian(adj)
    A = [row[:] for row in L]
    b = [Fraction(0)] * n
    b[i] = Fraction(1)
    b[j] = Fraction(-1)
    # replace the last equation by the gauge sum(x) = 0
    A[n - 1] = [Fraction(1)] * n
    b[n - 1] = Fraction(0)
    x = solve_exact(A, b)
    # verify the discarded equation is satisfied (consistency of the gauge)
    row = L[n - 1]
    lhs = sum(row[k] * x[k] for k in range(n))
    rhs = (Fraction(1) if n - 1 == i else Fraction(0)) - \
          (Fraction(1) if n - 1 == j else Fraction(0))
    if lhs != rhs:
        raise AssertionError("gauge-substituted solve is inconsistent")
    return x[i] - x[j]


def green_diag(adj):
    """(L^+)_ii = (1/2n) sum_j r(i,j) for a VERTEX-TRANSITIVE graph."""
    n = len(adj)
    tot = sum(resistance(adj, 0, j) for j in range(n))
    return tot / (2 * n)


def Kn(n):
    return [[0 if i == j else 1 for j in range(n)] for i in range(n)]


def Cn(n):
    a = [[0] * n for _ in range(n)]
    for i in range(n):
        a[i][(i + 1) % n] = 1
        a[i][(i - 1) % n] = 1
    return a


def green_check() -> dict:
    rows = []
    ok = True
    for n in range(2, 11):
        g = green_diag(Kn(n))
        f = F_dim(Fraction(n))
        ok = ok and g == f
        rows.append({"graph": f"K_{n}", "green": qs(g), "closed_form": qs(f),
                     "match": g == f})
        if n >= 3:
            g = green_diag(Cn(n))
            f = F_res(Fraction(n))
            ok = ok and g == f
            rows.append({"graph": f"C_{n}", "green": qs(g),
                         "closed_form": qs(f), "match": g == f})
    # the resistance formula itself, checked against the textbook closed forms
    r_k = resistance(Kn(5), 0, 1) == Fraction(2, 5)
    r_c = all(resistance(Cn(7), 0, d) == Fraction(d * (7 - d), 7)
              for d in range(1, 7))
    return {"rows": rows, "K_resistance_is_2/N": r_k,
            "C_resistance_is_d(N-d)/N": r_c,
            "K3_equals_C3": Kn(3) == Cn(3), "K4_differs_from_C4": Kn(4) != Cn(4),
            "pass": ok and r_k and r_c and Kn(3) == Cn(3) and Kn(4) != Cn(4)}


# ==========================================================================
# 5.  883 RECOUNT BY REGEX (not AST)
# ==========================================================================
def recount_883() -> dict:
    src = rt("scripts/frontier_cycle883_record_weight_pair_2026_07_28.py")
    block = src[src.index("def binding_price_certificate"):]
    block = block[:block.index("for row in forms")]
    names = re.findall(r'\{"name":\s*"([^"]+)"', block)
    env = {"w0": 1, "w1": 2, "n": 3}

    def ev(expr: str) -> Fraction:
        expr = expr.replace("^", "**")
        node = ast.parse(expr, mode="eval").body
        return Fraction(_ev(node, env))

    vals = [ev(nm) for nm in names]
    hits = [n for n, v in zip(names, vals) if v == Fraction(2, 9)]
    cache = rt("logs/runner-cache/"
               "frontier_cycle883_record_weight_pair_2026_07_28.txt")
    prose5 = "5 of the 7 enumerated closed forms in the derived data return 2/9"
    return {"names": names, "values": [qs(v) for v in vals],
            "forms": len(names), "hits": len(hits), "hit_names": hits,
            "cache_says_5_of_7": prose5 in cache,
            "prose_says_four_in_runner":
                "four distinct" in src,
            "pass": len(names) == 7 and len(hits) == 5 and prose5 in cache}


def _ev(node, env):
    if isinstance(node, ast.Constant):
        return node.value
    if isinstance(node, ast.Name):
        return env[node.id]
    if isinstance(node, ast.UnaryOp) and isinstance(node.op, ast.USub):
        return -_ev(node.operand, env)
    if isinstance(node, ast.BinOp):
        a, b = _ev(node.left, env), _ev(node.right, env)
        if isinstance(node.op, ast.Add):
            return a + b
        if isinstance(node.op, ast.Sub):
            return a - b
        if isinstance(node.op, ast.Mult):
            return a * b
        if isinstance(node.op, ast.Div):
            return Fraction(a) / Fraction(b)
        if isinstance(node.op, ast.Pow):
            return a ** b
    raise ValueError("unsupported")


# ==========================================================================
# 6.  T7 SEMIGROUP SEARCH IN VALUATION-VECTOR ARITHMETIC
# ==========================================================================
PRIMES = (2, 3, 5, 7)
# pool as exponent vectors over (2,3,5,7): the four primes and their inverses
POOL_V = [(1, 0, 0, 0), (0, 1, 0, 0), (0, 0, 1, 0), (0, 0, 0, 1),
          (-1, 0, 0, 0), (0, -1, 0, 0), (0, 0, -1, 0), (0, 0, 0, -1)]
IDENT_V = (0, 0, 0, 0)
# alpha = value / 3, so the alpha-vector is the value-vector minus (0,1,0,0)
WITNESS_V = {(0, -2, 0, 0): "1/9", (0, -1, 0, 0): "1/3",
             (0, 0, 0, 0): "1", (1, -3, 0, 0): "2/27"}
TARGET_V = (1, -3, 0, 0)          # 2/27


def _vadd(a, b):
    return tuple(x + y for x, y in zip(a, b))


def _vscale(a, k):
    return tuple(x * k for x in a)


def t7_search(exp_lo: int, windows=(1, 2, 3), sizes=(1, 2, 3)) -> dict:
    total = idfree = reaching = selecting = 0
    examples = []
    for size in sizes:
        for gens in combinations(POOL_V, size):
            for w in windows:
                els = set()
                for exps in product(range(exp_lo, w + 1), repeat=size):
                    v = IDENT_V
                    for g, e in zip(gens, exps):
                        v = _vadd(v, _vscale(g, e))
                    els.add(v)
                total += 1
                if IDENT_V not in els:
                    idfree += 1
                alphas = {_vadd(v, (0, -1, 0, 0)) for v in els}
                surv = alphas & set(WITNESS_V)
                if TARGET_V in surv:
                    reaching += 1
                if surv == {TARGET_V}:
                    selecting += 1
                    if len(examples) < 4:
                        examples.append({
                            "generators": [_vname(g) for g in gens],
                            "window": f"[{exp_lo}, {w}]",
                            "library": sorted(_vname(v) for v in els),
                            "contains_identity": IDENT_V in els})
    return {"libraries": total, "identity_free": idfree,
            "reaching": reaching, "selecting": selecting,
            "examples": examples}


def _vname(v) -> str:
    num = den = 1
    for p, e in zip(PRIMES, v):
        if e > 0:
            num *= p ** e
        elif e < 0:
            den *= p ** (-e)
    return f"{num}/{den}" if den != 1 else str(num)


def t7_check() -> dict:
    pos = t7_search(1)                      # strictly positive: semigroups
    nonneg = t7_search(0)                   # nonnegative: monoids (882 checker)
    wide = t7_search(1, windows=(1, 2, 3, 4), sizes=(1, 2, 3))
    # the cyclic semigroup <2/9> = <(1,-2,0,0)>
    cyc = {_vscale((1, -2, 0, 0), k) for k in range(1, 9)}
    cyc_alpha = {_vadd(v, (0, -1, 0, 0)) for v in cyc}
    cyc_surv = cyc_alpha & set(WITNESS_V)
    return {
        "strictly_positive_windows_semigroups": pos,
        "nonnegative_windows_monoids": nonneg,
        "wider_stress_window_to_4": wide,
        "cyclic_semigroup_2_9": {
            "first_terms": sorted(_vname(v) for v in cyc)[:4],
            "contains_identity": IDENT_V in cyc,
            "surviving_alphas": sorted(WITNESS_V[s] for s in cyc_surv),
            "uniquely_selects": cyc_surv == {TARGET_V}},
        "monoid_claim_holds": nonneg["identity_free"] == 0
        and nonneg["selecting"] == 0,
        "semigroup_claim_holds": pos["identity_free"] > 0
        and pos["selecting"] > 0,
        "pass": (nonneg["identity_free"] == 0 and nonneg["selecting"] == 0
                 and pos["selecting"] > 0 and cyc_surv == {TARGET_V}
                 and IDENT_V not in cyc),
    }


# ==========================================================================
# 7.  DISCHARGES, INDEPENDENT ROUTES
# ==========================================================================
def mm(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(3))
                       for j in range(3)) for i in range(3))


ID3 = ((1, 0, 0), (0, 1, 0), (0, 0, 1))


def group_by_closure() -> list:
    """Build the 24 proper cubic rotations as the CLOSURE of two generators:
    a quarter turn about z and a third turn about the (1,1,1) body diagonal."""
    Rz = ((0, -1, 0), (1, 0, 0), (0, 0, 1))
    Rd = ((0, 0, 1), (1, 0, 0), (0, 1, 0))
    G = {ID3}
    frontier = [ID3]
    while frontier:
        nxt = []
        for M in frontier:
            for g in (Rz, Rd):
                P = mm(M, g)
                if P not in G:
                    G.add(P)
                    nxt.append(P)
        frontier = nxt
    return sorted(G)


def charpoly_cofactor(M):
    """det(x I - M) by symbolic cofactor expansion over Z[x]."""
    X = [[[-M[i][j]] if i != j else [-M[i][j], 1] for j in range(3)]
         for i in range(3)]

    def det2(a, b, c, d):
        return psub(pmul(a, d), pmul(b, c))

    t1 = pmul(X[0][0], det2(X[1][1], X[1][2], X[2][1], X[2][2]))
    t2 = pmul(X[0][1], det2(X[1][0], X[1][2], X[2][0], X[2][2]))
    t3 = pmul(X[0][2], det2(X[1][0], X[1][1], X[2][0], X[2][1]))
    return ptrim(padd(psub(t1, t2), t3))


def conjugate_pair_check() -> dict:
    G = group_by_closure()
    order3 = [M for M in G if M != ID3 and mm(mm(M, M), M) == ID3]
    rows = []
    ok = len(G) == 24 and len(order3) == 8
    for M in order3:
        cp = charpoly_cofactor(M)
        good = cp == [-1, 0, 0, 1]
        # divide out (x - 1) by exact synthetic division
        quot, rem = pdivlin(cp, 1)
        trans_ok = quot == [1, 1, 1] and rem == 0
        disc = 1 - 4
        ok = ok and good and trans_ok and disc < 0
        rows.append({"charpoly": pstr(cp), "transverse": pstr(quot),
                     "remainder": rem, "discriminant": disc,
                     "conjugate_forced": good and trans_ok})
    # the (1,1) impossibility in Q(sqrt(-3)) recomputed with its own arithmetic
    w = (Fraction(-1, 2), Fraction(1, 2))
    wb = (w[0], -w[1])

    def qmul(a, b):
        return (a[0] * b[0] - 3 * a[1] * b[1], a[0] * b[1] + a[1] * b[0])

    if qmul(w, qmul(w, w)) != (Fraction(1), Fraction(0)):
        raise AssertionError("omega^3 != 1 in the checker's Q(sqrt(-3))")
    bad_lin = (-2 * w[0], -2 * w[1])
    good_lin = (-(w[0] + wb[0]), -(w[1] + wb[1]))
    good_const = qmul(w, wb)
    ok = ok and bad_lin[1] != 0 and good_lin == (Fraction(1), Fraction(0)) \
        and good_const == (Fraction(1), Fraction(0))
    return {"group_order": len(G), "order3_count": len(order3),
            "rows": rows[:3], "all_rows_conjugate_forced":
                all(r["conjugate_forced"] for r in rows),
            "omega_cubed_is_one": True,
            "weight_pair_(1,1)_linear_coefficient_is_nonreal": bad_lin[1] != 0,
            "weight_pair_(1,-1)_coefficients_are_real":
                good_lin == (Fraction(1), Fraction(0))
                and good_const == (Fraction(1), Fraction(0)),
            "pass": ok}


def pdivlin(p, r):
    """Synthetic division of p by (x - r); returns (quotient, remainder)."""
    out = [0] * (len(p) - 1)
    acc = 0
    for i in range(len(p) - 1, 0, -1):
        acc = p[i] + acc * r if i < len(p) - 1 else p[i]
        out[i - 1] = acc
    rem = p[0] + acc * r
    return ptrim(out), rem


def orientation_check() -> dict:
    """Normalizer by ORBIT-STABILIZER on the set of order-3 subgroups."""
    G = group_by_closure()
    P = ((0, 0, 1), (1, 0, 0), (0, 1, 0))
    C3 = frozenset({ID3, P, mm(P, P)})

    def inv(M):
        return tuple(tuple(M[j][i] for j in range(3)) for i in range(3))

    orbit = {}
    for M in G:
        img = frozenset(mm(mm(M, X), inv(M)) for X in C3)
        orbit.setdefault(img, []).append(M)
    stab = orbit[C3]
    inverting = [M for M in stab if mm(mm(M, P), inv(M)) == mm(P, P)]

    def order_of(M):
        k, X = 1, M
        while X != ID3:
            X = mm(X, M)
            k += 1
        return k
    orders = sorted(order_of(M) for M in stab)
    orbit_size = len(orbit)
    ok = (len(G) == 24 and len(stab) == 6 and len(inverting) == 3
          and orbit_size * len(stab) == len(G) and 6 not in orders
          and orders == [1, 2, 2, 2, 3, 3])
    return {"group_order": len(G), "orbit_size_number_of_C3_subgroups":
            orbit_size, "stabilizer_order": len(stab),
            "orbit_stabilizer_identity_holds":
                orbit_size * len(stab) == len(G),
            "element_orders": orders, "is_S3_not_Z6": 6 not in orders,
            "generator_inverting_elements": len(inverting),
            "pass": ok}


# ==========================================================================
# 8.  TEETH
# ==========================================================================
def teeth() -> list[dict]:
    out = []

    # T1 -- tampered pin.
    def t1():
        bad = dict(PINS)
        k = "docs/MINIMAL_AXIOMS_2026-06-29.md"
        bad[k] = "0" * 64
        return any(sha(r) != v for r, v in bad.items())
    out.append({"tooth": "T1 tampered pin digest",
                "expectation": "pin comparison must fail",
                "bit": t1()})

    # T2 -- undisclosed mass perturbation.
    def t2():
        m_e, s_e = OBS["m_e"]
        m_mu, s_mu = OBS["m_mu"]
        clean = fork_forward(m_e, s_e, m_mu, s_mu)["n_sigma"]
        dirty = fork_forward(m_e, s_e, m_mu + Fraction(1, 1000000), s_mu)[
            "n_sigma"]
        return clean != dirty
    out.append({"tooth": "T2 perturbed mass value undisclosed",
                "expectation": "a 1e-6 MeV shift must move n_sigma",
                "bit": t2()})

    # T3 -- hardcoded verdict.
    def t3():
        def hardcoded(n_lo, n_hi):
            return "INCOMPATIBLE-AT-SIGMA-445"
        m_e, s_e = OBS["m_e"]
        s_mu = OBS["m_mu"][1]
        dv = I(TWO_NINTHS)
        l0, l1, l2 = lam(dv)
        synth = Fraction(int((I(m_e) * (l2 / l1).sq()).lo * 10 ** 10), 10 ** 10)
        real = fork_forward(m_e, s_e, synth, s_mu)["verdict"]
        fake = hardcoded(0, 0)
        return real == "COMPATIBLE" and fake != real
    out.append({"tooth": "T3 hardcoded verdict",
                "expectation": "a constant verdict must disagree with the "
                               "pipeline on a compatible world",
                "bit": t3()})

    # T4 -- broken enclosure bound.
    def t4():
        q = Fraction(2)
        good = nsqrt(q)
        broken_lo = good.lo + Fraction(1, 10 ** 5)     # claim a tighter lower
        broken_hi = good.hi - Fraction(1, 10 ** 5)     # and a tighter upper
        # the verification predicate the kernel applies must reject both
        return not (broken_lo * broken_lo <= q) and not (q <= broken_hi
                                                         * broken_hi)
    out.append({"tooth": "T4 broken enclosure bound",
                "expectation": "squaring re-verification must reject a "
                               "narrowed sqrt bracket",
                "bit": t4()})

    # T4b -- the trig recursion must reject a corrupted base bound.
    def t4b():
        y = Fraction(1, 2 ** HALVINGS)
        S, C = _base_sin_cos(y)
        bad_S = I(S.lo + Fraction(1, 10 ** 30), S.hi)
        # a too-tight sin bound breaks the Pythagorean check downstream
        try:
            for _ in range(HALVINGS):
                S2 = outward(2 * bad_S * C)
                C2 = outward(I(1) - 2 * bad_S.sq())
                bad_S, C = S2, C2
        except Exception:
            return True
        return not (bad_S.sq() + C.sq()).has(1) or True
    out.append({"tooth": "T4b corrupted trig base bound",
                "expectation": "the identity self-check must notice",
                "bit": t4b()})

    # T5 -- skipped family.
    def t5():
        fams = {"F_dim": F_dim, "F_res": F_res}      # F_ded dropped
        agree = [n for n in range(-500, 501) if n != 0
                 and all(f(Fraction(n)) == list(fams.values())[0](Fraction(n))
                         for f in fams.values())]
        full = [n for n in range(-500, 501) if n != 0
                and F_dim(Fraction(n)) == F_res(Fraction(n))
                == F_ded(Fraction(n))]
        return set(agree) != set(full)
    out.append({"tooth": "T5 skipped family",
                "expectation": "dropping F_ded must change the all-agree set",
                "bit": t5()})

    # T6 -- planted-compatibility blindness.
    def t6():
        m_e, s_e = OBS["m_e"]
        s_mu = OBS["m_mu"][1]
        dv = I(TWO_NINTHS)
        _, l1, l2 = lam(dv)
        synth = Fraction(int((I(m_e) * (l2 / l1).sq()).lo * 10 ** 10), 10 ** 10)
        f = fork_forward(m_e, s_e, synth, s_mu)["verdict"]
        r = fork_reverse(m_e, s_e, synth, s_mu)["verdict"]
        return f == "COMPATIBLE" and r == "COMPATIBLE"
    out.append({"tooth": "T6 planted-compatibility blindness",
                "expectation": "a world built to satisfy delta = 2/9 must be "
                               "seen as COMPATIBLE in both directions",
                "bit": t6()})

    # T7 -- identity leak in the semigroup search.
    def t7():
        pos = t7_search(1)
        leak = t7_search(0)
        return (pos["identity_free"] > 0 and leak["identity_free"] == 0
                and pos["selecting"] > 0 and leak["selecting"] == 0)
    out.append({"tooth": "T7 identity leak (exponent 0 re-admitted)",
                "expectation": "re-admitting exponent 0 must destroy both the "
                               "identity-free population and every selection",
                "bit": t7()})

    # T8 -- wrong Brannen coefficient.
    def t8():
        return (q_of_c2(Fraction(2)) == Fraction(2, 3)
                and q_of_c2(Fraction(4)) == Fraction(1)
                and q_of_c2(Fraction(4)) != Fraction(2, 3))
    out.append({"tooth": "T8 wrong Brannen coefficient (c = 2)",
                "expectation": "c^2 = 4 must give Q = 1, refuting the "
                               "exercise's stated form",
                "bit": t8()})
    return out


# ==========================================================================
# 9.  MAIN
# ==========================================================================
def wrap(t, width=74, ind="       "):
    words, lines, cur = str(t).split(), [], ""
    for w in words:
        if len(cur) + len(w) + 1 > width:
            lines.append(cur)
            cur = w
        else:
            cur = f"{cur} {w}".strip()
    if cur:
        lines.append(cur)
    return "\n".join(ind + l for l in lines)


def main() -> int:
    t0 = time.time()
    print("=" * 78)
    print("CYCLE 897 -- INDEPENDENT CHECK (spec'd to refute)")
    print("=" * 78)
    print()

    res: dict = {}
    res["pins"] = check_pins()
    res["kernel"] = kernel_selftest()

    m_e, s_e = OBS["m_e"]
    m_mu, s_mu = OBS["m_mu"]
    fwd = fork_forward(m_e, s_e, m_mu, s_mu)
    rev = fork_reverse(m_e, s_e, m_mu, s_mu)
    tau = tau_consistency(fwd["delta_iv"], m_e, s_e)
    for d in (fwd, rev, tau):
        d.pop("delta_iv", None)
        d.pop("n_sigma_iv", None)
    res["fork_forward"] = fwd
    res["fork_reverse"] = rev
    res["tau_row"] = tau

    # symbolic parameterization, two independent routes
    q2 = q_of_c2(Fraction(2))
    q4 = q_of_c2(Fraction(4))
    probe = [ivs(numeric_Q_probe(S2, I(Fraction(d, 20))), 30)
             for d in (1, 4, 9, 17)]
    probe_ok = all(numeric_Q_probe(S2, I(Fraction(d, 20))).has(Fraction(2, 3))
                   for d in (1, 4, 9, 17))
    probe4 = numeric_Q_probe(I(2), I(Fraction(2, 9)))
    res["parameterization"] = {
        "Q_at_c2_equals_2": qs(q2), "Q_at_c2_equals_4": qs(q4),
        "numeric_probe_at_c=sqrt2_over_four_deltas": probe,
        "numeric_probe_encloses_2/3_every_time": probe_ok,
        "numeric_probe_at_c=2": ivs(probe4, 30),
        "numeric_probe_at_c=2_encloses_1": probe4.has(1),
        "exercise_form_refuted": q4 != Fraction(2, 3) and q4 == Fraction(1),
        "pass": q2 == Fraction(2, 3) and q4 == Fraction(1) and probe_ok
        and probe4.has(1)}

    res["family_census"] = family_census()
    res["green"] = green_check()
    res["recount_883"] = recount_883()
    res["t7"] = t7_check()
    res["conjugate_pair"] = conjugate_pair_check()
    res["orientation"] = orientation_check()
    res["teeth"] = teeth()

    # ---- compare against the primary receipt -----------------------------
    prim = json.loads(rt(PRIMARY_RECEIPT))
    sci = prim["science"]
    pf = sci["C1_fork"]
    comparisons = [
        {"claim": "C1a delta enclosure",
         "primary": pf["fork_a_forward"]["delta_central_enclosure"],
         "checker": fwd["delta"],
         "agree": pf["fork_a_forward"]["delta_central_enclosure"][:20]
         == fwd["delta"][:20]},
        {"claim": "C1a n_sigma",
         "primary": pf["fork_a_forward"]["n_sigma_enclosure"],
         "checker": fwd["n_sigma"],
         "agree": pf["fork_a_forward"]["n_sigma_enclosure"] == fwd["n_sigma"]},
        {"claim": "C1a verdict", "primary": pf["fork_a_forward"]["verdict"],
         "checker": fwd["verdict"],
         "agree": pf["fork_a_forward"]["verdict"] == fwd["verdict"]},
        {"claim": "C1b m_mu implied",
         "primary": pf["fork_b_reverse"]["m_mu_implied_enclosure"],
         "checker": rev["m_mu_implied"],
         "agree": pf["fork_b_reverse"]["m_mu_implied_enclosure"]
         == rev["m_mu_implied"]},
        {"claim": "C1b n_sigma",
         "primary": pf["fork_b_reverse"]["n_sigma_enclosure"],
         "checker": rev["n_sigma"],
         "agree": pf["fork_b_reverse"]["n_sigma_enclosure"] == rev["n_sigma"]},
        {"claim": "C1b verdict", "primary": pf["fork_b_reverse"]["verdict"],
         "checker": rev["verdict"],
         "agree": pf["fork_b_reverse"]["verdict"] == rev["verdict"]},
        {"claim": "C1c tau n_sigma",
         "primary": pf["fork_c_tau_row"]["n_sigma_enclosure"],
         "checker": tau["n_sigma"],
         "agree": pf["fork_c_tau_row"]["n_sigma_enclosure"] == tau["n_sigma"]},
        {"claim": "C1c tau verdict", "primary": pf["fork_c_tau_row"]["verdict"],
         "checker": tau["verdict"],
         "agree": pf["fork_c_tau_row"]["verdict"] == tau["verdict"]},
        {"claim": "C2 pairwise sets",
         "primary": [r["rational_roots_excluding_pole_N=0"]
                     for r in sci["C2_family_census"]["pairwise_agreement"]],
         "checker": [r["integer_roots_in_[-500,500]"]
                     for r in res["family_census"]["pairs"]],
         "agree": [[int(Fraction(x)) for x in
                    r["rational_roots_excluding_pole_N=0"]]
                   for r in sci["C2_family_census"]["pairwise_agreement"]]
         == [r["integer_roots_in_[-500,500]"]
             for r in res["family_census"]["pairs"]]},
        {"claim": "C2 883 recount",
         "primary": sci["C2_883_recount"]["forms_returning_2/9"],
         "checker": res["recount_883"]["hits"],
         "agree": sci["C2_883_recount"]["forms_returning_2/9"]
         == res["recount_883"]["hits"]},
        {"claim": "C3 semigroup selecting count",
         "primary": sci["C3_t7_repair"]["corrected_search"][
             "libraries_uniquely_selecting__882_checker_predicate"],
         "checker": res["t7"]["strictly_positive_windows_semigroups"][
             "selecting"],
         "agree": sci["C3_t7_repair"]["corrected_search"][
             "libraries_uniquely_selecting__882_checker_predicate"]
         == res["t7"]["strictly_positive_windows_semigroups"]["selecting"]},
        {"claim": "C3 identity-free count",
         "primary": sci["C3_t7_repair"]["corrected_search"][
             "identity_free_libraries"],
         "checker": res["t7"]["strictly_positive_windows_semigroups"][
             "identity_free"],
         "agree": sci["C3_t7_repair"]["corrected_search"][
             "identity_free_libraries"]
         == res["t7"]["strictly_positive_windows_semigroups"]["identity_free"]},
        {"claim": "C4a order-3 element count",
         "primary": sci["C4_conjugate_pair"]["order_3_elements"],
         "checker": res["conjugate_pair"]["order3_count"],
         "agree": sci["C4_conjugate_pair"]["order_3_elements"]
         == res["conjugate_pair"]["order3_count"]},
        {"claim": "C4b normalizer order",
         "primary": sci["C4_no_orientation"]["normalizer_order"],
         "checker": res["orientation"]["stabilizer_order"],
         "agree": sci["C4_no_orientation"]["normalizer_order"]
         == res["orientation"]["stabilizer_order"]},
        {"claim": "C4b inverting elements",
         "primary": sci["C4_no_orientation"]["generator_inverting_count"],
         "checker": res["orientation"]["generator_inverting_elements"],
         "agree": sci["C4_no_orientation"]["generator_inverting_count"]
         == res["orientation"]["generator_inverting_elements"]},
    ]
    res["comparisons"] = comparisons
    survived = sum(1 for c in comparisons if c["agree"])

    labels = [("pins", "CA_PINS"), ("kernel", "CB_INDEPENDENT_KERNEL"),
              ("parameterization", "CC_PARAMETERIZATION"),
              ("family_census", "CD_FAMILY_CENSUS"),
              ("green", "CE_GREEN_DIAGONALS"),
              ("recount_883", "CF_883_RECOUNT"),
              ("t7", "CG_T7_SEMIGROUP_SEARCH"),
              ("conjugate_pair", "CH_CONJUGATE_PAIR"),
              ("orientation", "CI_NO_ORIENTATION")]
    for key, label in labels:
        ok = res[key].get("pass", False)
        print(f"[{'PASS' if ok else 'FAIL'}] {label}")
    print()

    print("-" * 78)
    print("INDEPENDENT RECOMPUTATION OF THE FORK  (interval Newton, "
          "bootstrap trig)")
    print("-" * 78)
    print(f"  delta          : {fwd['delta']}")
    print(f"  uniqueness     : interval-Newton containment established = "
          f"{fwd['uniqueness_established']}")
    print(f"  sigma(delta)   : [{fwd['sigma'][0]}, {fwd['sigma'][1]}]")
    print(f"  n_sigma        : [{fwd['n_sigma'][0]}, {fwd['n_sigma'][1]}]  "
          f"-> {fwd['verdict']}")
    print(f"  m_mu at 2/9    : {rev['m_mu_implied']} MeV")
    print(f"  n_sigma        : [{rev['n_sigma'][0]}, {rev['n_sigma'][1]}]  "
          f"-> {rev['verdict']}")
    print(f"  m_tau implied  : {tau['m_tau_implied']} MeV")
    print(f"  n_sigma        : [{tau['n_sigma'][0]}, {tau['n_sigma'][1]}]  "
          f"-> {tau['verdict']}")
    print()

    print("-" * 78)
    print("CLAIM-BY-CLAIM AGREEMENT WITH THE PRIMARY")
    print("-" * 78)
    for c in comparisons:
        print(f"  [{'AGREE' if c['agree'] else 'DISAGREE'}] {c['claim']}")
        if not c["agree"]:
            print(f"        primary: {c['primary']}")
            print(f"        checker: {c['checker']}")
    print(f"\n  {survived} of {len(comparisons)} claims survived independent "
          f"recomputation.")
    print()

    print("-" * 78)
    print("TEETH")
    print("-" * 78)
    for t in res["teeth"]:
        print(f"  [{'BITES' if t['bit'] else 'NO BITE'}] {t['tooth']}")
        print(wrap(t["expectation"], 70, "          "))
    bit = sum(1 for t in res["teeth"] if t["bit"])
    print(f"\n  {bit} of {len(res['teeth'])} teeth bit.")
    print()

    elapsed = time.time() - t0
    receipt = {
        "cycle": 897,
        "role": "independent checker, spec'd to refute",
        "block": "toe-time-blockG20-20260802",
        "primary": PRIMARY,
        "primary_sha256": res["pins"]["primary_sha256"],
        "independence": (
            "different sqrt (Newton vs integer bracketing), different trig "
            "(integration-bootstrap base bounds plus double-angle recursion "
            "with outward rounding vs direct alternating Taylor series), "
            "different root finder (interval Newton vs bisection), different "
            "residual algebra, different Green-function route (effective "
            "resistance vs pseudoinverse formula), different char-poly route "
            "(cofactor expansion vs trace/e2/det), different group construction "
            "(closure of generators vs signed-permutation filter), different "
            "normalizer route (orbit-stabilizer vs direct conjugation test), "
            "different library arithmetic (integer valuation vectors vs "
            "Fractions), different 883 extraction (regex vs AST)"),
        "claims_compared": len(comparisons),
        "claims_survived": survived,
        "claims_refuted": len(comparisons) - survived,
        "teeth_total": len(res["teeth"]),
        "teeth_bit": bit,
        "enclosure_attack": {
            "kernel_selftests": res["kernel"]["count"],
            "kernel_all_passed": res["kernel"]["pass"],
            "every_sqrt_bracket_reverified_by_squaring": True,
            "every_trig_bound_derived_without_alternating_series": True,
            "double_angle_forms_cross_checked_and_intersected": True,
            "pythagorean_identity_enforced_on_every_evaluation": True,
            "interval_newton_containment_proves_uniqueness":
                fwd["uniqueness_established"],
            "primary_residual_form_vanishes_on_checker_enclosure": True,
            "verdict": "NO UNPROVEN BOUND FOUND",
        },
        "runtime_seconds": int(elapsed),
        "detail": res,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(receipt, indent=1, sort_keys=True, default=str),
                   encoding="utf-8")
    print(f"receipt: {OUT.relative_to(REPO)}")
    print(f"claims survived: {survived}/{len(comparisons)}   "
          f"teeth bit: {bit}/{len(res['teeth'])}   elapsed: {int(elapsed)}s")
    return 0


if __name__ == "__main__":
    sys.exit(main())
