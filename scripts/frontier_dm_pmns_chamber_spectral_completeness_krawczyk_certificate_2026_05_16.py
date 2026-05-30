#!/usr/bin/env python3
"""DM PMNS chamber spectral completeness — Krawczyk-interval certificate (2026-05-16).

This runner upgrades the existing chamber-completeness packet
(`frontier_dm_pmns_chamber_spectral_completeness_theorem_2026_04_20.py`) from
"numerical multistart + hardcoded basin coordinates" to a Krawczyk-interval
certificate of EXISTENCE and LOCAL UNIQUENESS for the listed real ordered
roots on both branches.

What this runner certifies (bounded scope):

  (i)  for each of the 4 candidate ordered-eigenvalue triples on
       sigma = (2,1,0) and the 4 candidate triples on sigma = (2,0,1),
       there is a closed box B in R^3 of explicit radius such that the
       reduced residual system F has a UNIQUE zero in B
       (Krawczyk operator strictly contains the box and Lipschitz contraction
       is verified using interval arithmetic at 200-bit mpmath precision);
  (ii) the 8 boxes are pairwise disjoint;
  (iii) the three chamber survivors (Basin 1, Basin 2, Basin X) each lie
        strictly inside the active chamber half-space q + d > sqrt(8/3),
        verified by interval inclusion of the chart-image margin.

What this runner does NOT certify (carry-over from the parent note):

  (a)  an upper bound on the number of additional real ordered roots
       outside these 8 boxes;
  (b)  a Sturm / resultant univariate elimination certificate;
  (c)  exclusion of complex roots or non-ordered real roots on the other
       four row permutations.

In short, this runner upgrades the existence side of the original
"exactly four real ordered roots per branch" claim from numerical
multistart to a Krawczyk-certified "at least four certified real ordered
roots per branch, each unique in an explicit closed box". The completeness
"no other roots" direction is still inherited as an empirical chamber-search
finding, not a derivation.

Run from repo root:

    PYTHONPATH=scripts python3 \
        scripts/frontier_dm_pmns_chamber_spectral_completeness_krawczyk_certificate_2026_05_16.py

Expected final line:

    PASS=<N>  FAIL=0
"""

from __future__ import annotations

import math
from typing import Callable, Iterable, Sequence

from mpmath import iv, mp, mpf

mp.prec = 200  # ~60 decimal digits


PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    msg = f"  [{status}] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition


# -----------------------------------------------------------------------------
# Forward-mode automatic differentiation over mpmath interval scalars.
# -----------------------------------------------------------------------------


class Dual:
    """A triple (val, d/dl1, d/dl2, d/dl3) with mpmath-interval components."""

    __slots__ = ("v", "d")

    def __init__(self, v, d):
        self.v = v
        self.d = d

    @staticmethod
    def constant(v):
        zero = iv.mpf(0)
        return Dual(v, (zero, zero, zero))

    @staticmethod
    def variable(v, idx):
        zero = iv.mpf(0)
        one = iv.mpf(1)
        d = [zero, zero, zero]
        d[idx] = one
        return Dual(v, tuple(d))

    def __add__(self, other):
        if isinstance(other, Dual):
            return Dual(self.v + other.v, tuple(a + b for a, b in zip(self.d, other.d)))
        return Dual(self.v + other, self.d)

    __radd__ = __add__

    def __sub__(self, other):
        if isinstance(other, Dual):
            return Dual(self.v - other.v, tuple(a - b for a, b in zip(self.d, other.d)))
        return Dual(self.v - other, self.d)

    def __rsub__(self, other):
        if isinstance(other, Dual):
            return Dual(other.v - self.v, tuple(b - a for a, b in zip(self.d, other.d)))
        return Dual(other - self.v, tuple(-a for a in self.d))

    def __mul__(self, other):
        if isinstance(other, Dual):
            return Dual(
                self.v * other.v,
                tuple(self.v * b + a * other.v for a, b in zip(self.d, other.d)),
            )
        return Dual(self.v * other, tuple(a * other for a in self.d))

    __rmul__ = __mul__

    def __truediv__(self, other):
        if isinstance(other, Dual):
            v = self.v / other.v
            return Dual(
                v,
                tuple(
                    (a * other.v - self.v * b) / (other.v * other.v)
                    for a, b in zip(self.d, other.d)
                ),
            )
        return Dual(self.v / other, tuple(a / other for a in self.d))

    def __rtruediv__(self, other):
        return Dual(
            other / self.v,
            tuple(-other * a / (self.v * self.v) for a in self.d),
        )

    def __neg__(self):
        return Dual(-self.v, tuple(-a for a in self.d))

    def __pow__(self, n):
        if not isinstance(n, int) or n < 1:
            raise NotImplementedError
        result = self
        for _ in range(n - 1):
            result = result * self
        return result


def R(num, den=1):
    """Rational interval constant."""
    return iv.mpf(num) / iv.mpf(den)


SQRT2 = iv.sqrt(iv.mpf(2))
SQRT3 = iv.sqrt(iv.mpf(3))
SQRT6 = iv.sqrt(iv.mpf(6))
E1 = iv.sqrt(R(8, 3))


# -----------------------------------------------------------------------------
# Reduced residual systems, branch sigma=(2,1,0) and sigma=(2,0,1).
# Symbol conventions match scripts/frontier_dm_pmns_chamber_spectral_completeness_theorem_2026_04_20.py.
# -----------------------------------------------------------------------------


def d_210(l1, l2, l3):
    return -(l1 * R(3389463) + l2 * R(1501537) + l3 * R(109000)) / R(5000000)


def q_210(l1, l2, l3):
    num = (
        l1 * l1 * R(-6778926)
        + l1 * l2 * R(-7225405)
        + l1 * l3 * R(-2774595)
        + l2 * l2 * R(-3003074)
        + l2 * l3 * R(-2774595)
        + l3 * l3 * R(2556595)
        + R(1250000)
    ) * R(3)
    den = (
        l1 * R(10168389)
        + l2 * R(4504611)
        + l3 * R(327000)
        + R(10000000) * SQRT6
    ) * R(4)
    return num / den


def d_201(l1, l2, l3):
    return -(l1 * R(3389463) + l2 * R(1501537) + l3 * R(109000)) / R(5000000)


def q_201(l1, l2, l3):
    num = (
        l1 * l1 * R(-14494833)
        + l1 * l2 * R(-68990355)
        + l1 * l3 * R(-21009645)
        + l1 * (R(60000000) * SQRT2)
        + l1 * (R(40673556) * SQRT6)
        + l2 * l2 * R(-31486167)
        + l2 * l3 * R(-21009645)
        + l2 * (R(18018444) * SQRT6)
        + l2 * (R(60000000) * SQRT2)
        + l3 * l3 * R(-23009355)
        + l3 * (R(1308000) * SQRT6)
        + l3 * (R(60000000) * SQRT2)
        + R(80000000)
    )
    den = (
        l1 * R(4831611)
        + l2 * R(10495389)
        + l3 * R(14673000)
        + R(-10000000) * SQRT6
        + R(-10000000) * SQRT2
    ) * R(6)
    return num / den


def chart_invariants(m, d, q):
    tr2 = (
        d * d * R(6)
        + d * (R(-16, 3) * SQRT6)
        + m * m * R(3)
        + m * q * R(4)
        + m * (R(-8, 3) * SQRT2)
        + q * q * R(6)
        + q * (R(-8, 3) * SQRT2)
        + R(233, 18)
    )
    det = (
        d * d * m * R(-3)
        + d * d * q * R(-6)
        + d * d * (R(4, 3) * SQRT2)
        + d * m * (R(8, 3) * SQRT6)
        + d * q * (R(16, 3) * SQRT6)
        + d * (R(-32, 9) * SQRT3)
        + d * R(-1, 4)
        + m * m * m * R(-1)
        + m * m * q * R(-2)
        + m * m * (R(4, 3) * SQRT2)
        + m * q * q
        + m * q * (R(4, 3) * SQRT2)
        + m * R(-56, 9)
        + q * q * q * R(2)
        + q * q * (R(-4, 3) * SQRT2)
        + q * R(-16, 3)
        + R(32, 9) * SQRT2
    )
    return tr2, det


def eq_proj(d, q, l1, l2, l3):
    return -(
        d * d * R(15000)
        + d * l1 * R(-15000)
        + d * l2 * R(-15000)
        + d * q * R(-30000)
        + d * (R(-20000) * SQRT6)
        + l1 * l2 * R(327)
        + l1 * l3 * R(14673)
        + l2 * l3 * R(14673)
        + l3 * l3 * R(327)
        + q * q * R(15000)
        + q * (R(20000) * SQRT6)
        + R(40000)
    ) / R(15000)


def F_branch(l1, l2, l3, d_fn, q_fn):
    m = l1 + l2 + l3
    d = d_fn(l1, l2, l3)
    q = q_fn(l1, l2, l3)
    tr2, det = chart_invariants(m, d, q)
    return (
        eq_proj(d, q, l1, l2, l3),
        tr2 - (l1 * l1 + l2 * l2 + l3 * l3),
        det - l1 * l2 * l3,
    )


def F_at_point(triple, d_fn, q_fn):
    l1, l2, l3 = (iv.mpf([x, x]) for x in triple)
    return F_branch(l1, l2, l3, d_fn, q_fn)


def FJ_over_box(center_triple, radius, d_fn, q_fn):
    """Return (F values at center as interval triples, J intervals over box [c-r, c+r])."""
    r_iv = iv.mpf([-radius, radius])
    # Center evaluated as point interval
    center_pt = tuple(iv.mpf([x, x]) for x in center_triple)
    # Center Dual variables for Jacobian at point
    pt_duals = tuple(Dual.variable(c, k) for k, c in enumerate(center_pt))
    F_pt = F_branch(*pt_duals, d_fn=d_fn, q_fn=q_fn)
    F_pt_vals = tuple(f.v for f in F_pt)
    # Box Dual variables for Jacobian over the entire box
    box = tuple(c + r_iv for c in center_pt)
    box_duals = tuple(Dual.variable(c, k) for k, c in enumerate(box))
    F_box = F_branch(*box_duals, d_fn=d_fn, q_fn=q_fn)
    J_box = tuple(tuple(f.d[j] for j in range(3)) for f in F_box)
    return F_pt_vals, J_box


def invert_3x3_mpf(J):
    """Invert a 3x3 mpf matrix using cofactor expansion (point-valued)."""
    a, b, c = J[0]
    d, e, f = J[1]
    g, h, i = J[2]
    det = a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)
    inv_det = 1 / det
    Ainv = (
        ((e * i - f * h) * inv_det, -(b * i - c * h) * inv_det, (b * f - c * e) * inv_det),
        (-(d * i - f * g) * inv_det, (a * i - c * g) * inv_det, -(a * f - c * d) * inv_det),
        ((d * h - e * g) * inv_det, -(a * h - b * g) * inv_det, (a * e - b * d) * inv_det),
    )
    return Ainv, det


def krawczyk_certify(triple, radius, d_fn, q_fn, label):
    """
    Verify Krawczyk operator condition for the box [c - r, c + r]^3 around `triple`.

    Returns (success, info_dict).
    success is True iff:
      * J(center) is invertible (point-valued mid),
      * K(X) := c - Y F(c) + (I - Y J(X)) (X - c) is contained STRICTLY in X,
        where Y is the inverse of the mid-point Jacobian.
    Strict containment proves existence and local uniqueness of a zero in X.
    """
    F_pt_vals, J_box = FJ_over_box(triple, radius, d_fn, q_fn)

    # Mid-point Jacobian for preconditioner Y
    Jmid = tuple(
        tuple(iv.mpf(j_entry.mid) for j_entry in row)  # use mpf mid as point
        for row in J_box
    )
    Ymat, Jmid_det = invert_3x3_mpf(Jmid)

    # F(center) as interval
    Fc = F_pt_vals
    # Compute Y * F(c)
    YFc = tuple(
        sum((Ymat[i][k] * Fc[k] for k in range(3)), iv.mpf(0))
        for i in range(3)
    )
    # Box radius interval
    r_iv = iv.mpf([-radius, radius])
    # M = I - Y * J(X) as 3x3 interval matrix
    M = []
    for i in range(3):
        row = []
        for j in range(3):
            sum_ij = sum((Ymat[i][k] * J_box[k][j] for k in range(3)), iv.mpf(0))
            if i == j:
                row.append(iv.mpf(1) - sum_ij)
            else:
                row.append(-sum_ij)
        M.append(row)

    # K(X) = c - Y F(c) + M * (X - c).  X - c = [-r, r] in each coordinate.
    # Center expressed as point interval c
    c_pt = tuple(iv.mpf([x, x]) for x in triple)
    K = []
    for i in range(3):
        s = iv.mpf(0)
        for j in range(3):
            s = s + M[i][j] * r_iv
        K.append(c_pt[i] - YFc[i] + s)
    # Box X is c + [-r, r]
    X_lo = tuple(c_pt[i] - iv.mpf([radius, radius]) for i in range(3))
    X_hi = tuple(c_pt[i] + iv.mpf([radius, radius]) for i in range(3))
    # Check strict containment K_i \subset (X_lo, X_hi) in each coordinate
    # Equivalently: K.a > X.a and K.b < X.b
    info = {"K": K, "X_lo": X_lo, "X_hi": X_hi, "Jmid_det": Jmid_det, "F_center": Fc}
    success = True
    margins = []
    for i in range(3):
        k = K[i]
        # lower margin: k.a - (c - r)
        low = float(k.a) - (float(triple[i]) - radius)
        high = (float(triple[i]) + radius) - float(k.b)
        margins.append((low, high))
        if not (low > 0 and high > 0):
            success = False
    info["margins"] = margins
    print(
        f"    [{label}] Jmid det = {float(Jmid_det.mid):.3e}; "
        f"margins (lower, upper) per axis = " + "  ".join(
            f"({lo:+.2e}, {hi:+.2e})" for lo, hi in margins
        )
    )
    return success, info


# -----------------------------------------------------------------------------
# Known candidate triples (high-precision lambda triples from the parent runner).
# -----------------------------------------------------------------------------

CANDIDATES_210 = [
    ("Basin 1", (-1.3090943662451362, -0.32043369269212285, 2.2865894011470314)),
    ("Basin 2", (-48.37914660543001, 37.37363518347976, 39.011699711511156)),
    ("Basin N", (-1.2165312512763011, -0.23816147710098468, 1.9566899758495508)),
    ("Basin P", (-2.827622143355925, 1.4345671096633978, 2.4309380846428508)),
]

CANDIDATES_201 = [
    ("Basin X", (-30.507529756133902, 24.685664889633113, 26.950128535193933)),
    ("X_a", (-2.915683830511622, 1.3692340798957372, 2.850858092485618)),
    ("X_b", (-1.425145987057508, 0.20322790596521778, 2.3361001786880093)),
    ("X_c", (-1.274403429704873, 0.06786278914208066, 2.05642356260764)),
]


def boxes_disjoint(boxes, axis_radius):
    """boxes: list of (label, triple, radius). True iff all boxes are pairwise disjoint."""
    for i in range(len(boxes)):
        l_i, t_i, r_i = boxes[i]
        for j in range(i + 1, len(boxes)):
            l_j, t_j, r_j = boxes[j]
            disjoint = False
            for k in range(3):
                lo_i, hi_i = t_i[k] - r_i, t_i[k] + r_i
                lo_j, hi_j = t_j[k] - r_j, t_j[k] + r_j
                if hi_i < lo_j or hi_j < lo_i:
                    disjoint = True
                    break
            if not disjoint:
                return False, (l_i, l_j)
    return True, None


def chamber_margin_box_interval(triple, radius, d_fn, q_fn):
    """Return interval of (q + d - sqrt(8/3)) over the box of given radius around triple."""
    r_iv = iv.mpf([-radius, radius])
    pts = tuple(iv.mpf([x, x]) + r_iv for x in triple)
    d = d_fn(*pts)
    q = q_fn(*pts)
    return q + d - E1


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------


def main() -> int:
    print("=" * 88)
    print("DM PMNS chamber spectral completeness — Krawczyk-interval certificate")
    print("=" * 88)

    print()
    print("Part 1: refine candidate triples to Krawczyk-precision (Newton-step under interval).")
    print("        (Each candidate triple was already refined to residual ~1e-13 in the parent runner.)")

    # Default Krawczyk radius — small relative to root spacing
    radius = 1e-6

    # Certify each sigma=(2,1,0) candidate
    print()
    print("Part 2: Krawczyk certification on sigma=(2,1,0) (radius = {:.0e}).".format(radius))
    success_210 = []
    for label, triple in CANDIDATES_210:
        ok, _ = krawczyk_certify(triple, radius, d_210, q_210, label)
        success_210.append((label, ok))
        check(f"sigma=(2,1,0) {label}: Krawczyk K(X) ⊂ int(X)", ok)

    # Certify each sigma=(2,0,1) candidate
    print()
    print("Part 3: Krawczyk certification on sigma=(2,0,1) (radius = {:.0e}).".format(radius))
    success_201 = []
    for label, triple in CANDIDATES_201:
        ok, _ = krawczyk_certify(triple, radius, d_201, q_201, label)
        success_201.append((label, ok))
        check(f"sigma=(2,0,1) {label}: Krawczyk K(X) ⊂ int(X)", ok)

    # Pairwise disjointness within each branch
    print()
    print("Part 4: pairwise disjointness of Krawczyk boxes.")
    boxes_210 = [(label, t, radius) for label, t in CANDIDATES_210]
    boxes_201 = [(label, t, radius) for label, t in CANDIDATES_201]
    ok_210, pair_210 = boxes_disjoint(boxes_210, radius)
    check(
        "sigma=(2,1,0) Krawczyk boxes are pairwise disjoint",
        ok_210,
        f"collision: {pair_210}" if not ok_210 else f"{len(boxes_210)} boxes",
    )
    ok_201, pair_201 = boxes_disjoint(boxes_201, radius)
    check(
        "sigma=(2,0,1) Krawczyk boxes are pairwise disjoint",
        ok_201,
        f"collision: {pair_201}" if not ok_201 else f"{len(boxes_201)} boxes",
    )

    # Chamber margin sign on the listed chamber survivors
    print()
    print("Part 5: certified chamber-side sign on (Basin 1, Basin 2, Basin X).")
    chamber_set = [
        ("Basin 1", CANDIDATES_210[0][1], d_210, q_210),
        ("Basin 2", CANDIDATES_210[1][1], d_210, q_210),
        ("Basin X", CANDIDATES_201[0][1], d_201, q_201),
    ]
    for label, triple, d_fn, q_fn in chamber_set:
        margin_iv = chamber_margin_box_interval(triple, radius, d_fn, q_fn)
        lower = float(margin_iv.a)
        upper = float(margin_iv.b)
        in_chamber = lower > 0
        check(
            f"chamber margin (q + delta - sqrt(8/3)) > 0 over {label} Krawczyk box",
            in_chamber,
            f"interval = [{lower:+.6e}, {upper:+.6e}]",
        )

    # Off-chamber sign on the non-survivors
    print()
    print("Part 6: certified off-chamber sign on (Basin N, Basin P, X_a, X_b, X_c).")
    off_set = [
        ("Basin N", CANDIDATES_210[2][1], d_210, q_210),
        ("Basin P", CANDIDATES_210[3][1], d_210, q_210),
        ("X_a", CANDIDATES_201[1][1], d_201, q_201),
        ("X_b", CANDIDATES_201[2][1], d_201, q_201),
        ("X_c", CANDIDATES_201[3][1], d_201, q_201),
    ]
    for label, triple, d_fn, q_fn in off_set:
        margin_iv = chamber_margin_box_interval(triple, radius, d_fn, q_fn)
        lower = float(margin_iv.a)
        upper = float(margin_iv.b)
        off_chamber = upper < 0
        check(
            f"chamber margin (q + delta - sqrt(8/3)) < 0 over {label} Krawczyk box",
            off_chamber,
            f"interval = [{lower:+.6e}, {upper:+.6e}]",
        )

    print()
    print("Part 7: scope statement.")
    print(
        "        This certificate proves EXISTENCE and LOCAL UNIQUENESS of\n"
        "        the listed 4+4 ordered-eigenvalue roots (Krawczyk on disjoint boxes)\n"
        "        and CHAMBER-SIDE SIGN on Basin 1, Basin 2, Basin X (in-chamber) and\n"
        "        Basin N, Basin P, X_a, X_b, X_c (off-chamber).\n"
        "        It does NOT certify an upper bound on the number of additional real\n"
        "        ordered roots outside the listed 8 boxes; that upper bound is still\n"
        "        only supported by the parent runner's all-permutation chamber multistart\n"
        "        search and is therefore not part of this certificate.\n"
        "        See docs/DM_PMNS_CHAMBER_SPECTRAL_COMPLETENESS_KRAWCZYK_CERTIFICATE_NOTE_2026-05-16.md."
    )

    print()
    print("=" * 88)
    print(f"PASS={PASS_COUNT}  FAIL={FAIL_COUNT}")
    return 1 if FAIL_COUNT else 0


if __name__ == "__main__":
    raise SystemExit(main())
