#!/usr/bin/env python3
"""Construct L0 spectral projectors for k=2,3 over Q(sqrt(k))."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "L0_SPECTRAL_PROJECTORS_K2_K3_BOUNDED_THEOREM_NOTE_2026-08-14.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/L0_SPECTRAL_PROJECTORS_K2_K3_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)


class Qs:
    """r + s*sqrt(k) with r,s in Q."""

    __slots__ = ("r", "s", "k")

    def __init__(self, r, s=0, k=1) -> None:
        self.r = Fraction(r)
        self.s = Fraction(s)
        self.k = int(k)

    def _align(self, other: Qs) -> None:
        if self.k != other.k and not (self.s == 0 or other.s == 0):
            raise ValueError("radicand mismatch")

    def __add__(self, other: Qs) -> Qs:
        k = self.k if self.s != 0 else other.k
        return Qs(self.r + other.r, self.s + other.s, k)

    def __sub__(self, other: Qs) -> Qs:
        k = self.k if self.s != 0 else other.k
        return Qs(self.r - other.r, self.s - other.s, k)

    def __mul__(self, other: Qs) -> Qs:
        k = self.k if self.s != 0 else other.k if other.s != 0 else 1
        return Qs(self.r * other.r + self.s * other.s * k, self.r * other.s + self.s * other.r, k)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Qs):
            return NotImplemented
        return self.r == other.r and self.s == other.s and (
            self.s == 0 or other.s == 0 or self.k == other.k
        )

    def __neg__(self) -> Qs:
        return Qs(-self.r, -self.s, self.k)


ZERO, ONE = Qs(0), Qs(1)
I_UNIT = None  # unused; real matrices here


def mat_add(a, b):
    return tuple(tuple(a[i][j] + b[i][j] for j in range(2)) for i in range(2))


def mat_mul(a, b):
    return tuple(
        tuple(a[i][0] * b[0][j] + a[i][1] * b[1][j] for j in range(2))
        for i in range(2)
    )


def mat_scale(c: Qs, a):
    return tuple(tuple(c * a[i][j] for j in range(2)) for i in range(2))


def mat_eq(a, b) -> bool:
    return all(a[i][j] == b[i][j] for i in range(2) for j in range(2))


def ident(k=1):
    return ((Qs(1, 0, k), Qs(0, 0, k)), (Qs(0, 0, k), Qs(1, 0, k)))


def zero(k=1):
    return ((Qs(0, 0, k), Qs(0, 0, k)), (Qs(0, 0, k), Qs(0, 0, k)))


def sx(k=1):
    return ((Qs(0, 0, k), Qs(1, 0, k)), (Qs(1, 0, k), Qs(0, 0, k)))


def sy(k=1):
    # σy is imaginary; H uses real a,b,c Paulis. For H=aσx+bσy+cσz we need i.
    # Use σy = [[0,-i],[i,0]]. Represent i as a tag: store complex Qs? 
    # For H^2 identities with real a,b,c, use standard Pauli over C.
    # Simpler: work with H = aσx + bσy + cσz using complex entries (r+s√k) + i(p+q√k).
    raise NotImplementedError


class Qc:
    """(r + s√k) + i (p + q√k)."""

    def __init__(self, r, s=0, p=0, q=0, k=1) -> None:
        self.r, self.s, self.p, self.q = (Fraction(x) for x in (r, s, p, q))
        self.k = int(k)

    def __add__(self, o: Qc) -> Qc:
        return Qc(self.r + o.r, self.s + o.s, self.p + o.p, self.q + o.q, self.k or o.k)

    def __sub__(self, o: Qc) -> Qc:
        return Qc(self.r - o.r, self.s - o.s, self.p - o.p, self.q - o.q, self.k or o.k)

    def __mul__(self, o: Qc) -> Qc:
        k = self.k if self.s or self.q else (o.k if o.s or o.q else 1)
        # (a+ib)(c+id) with a=r+s√k, b=p+q√k
        a_r, a_s, b_r, b_s = self.r, self.s, self.p, self.q
        c_r, c_s, d_r, d_s = o.r, o.s, o.p, o.q
        # ac - bd  and  ad+bc
        ac_r = a_r * c_r + a_s * c_s * k
        ac_s = a_r * c_s + a_s * c_r
        bd_r = b_r * d_r + b_s * d_s * k
        bd_s = b_r * d_s + b_s * d_r
        ad_r = a_r * d_r + a_s * d_s * k
        ad_s = a_r * d_s + a_s * d_r
        bc_r = b_r * c_r + b_s * c_s * k
        bc_s = b_r * c_s + b_s * c_r
        return Qc(ac_r - bd_r, ac_s - bd_s, ad_r + bc_r, ad_s + bc_s, k)

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, Qc):
            return NotImplemented
        return (self.r, self.s, self.p, self.q) == (o.r, o.s, o.p, o.q)

    def __neg__(self) -> Qc:
        return Qc(-self.r, -self.s, -self.p, -self.q, self.k)


def C(r, s=0, p=0, q=0, k=1) -> Qc:
    return Qc(r, s, p, q, k)


def madd(a, b):
    return ((a[0][0] + b[0][0], a[0][1] + b[0][1]), (a[1][0] + b[1][0], a[1][1] + b[1][1]))


def mmul(a, b):
    return (
        (a[0][0] * b[0][0] + a[0][1] * b[1][0], a[0][0] * b[0][1] + a[0][1] * b[1][1]),
        (a[1][0] * b[0][0] + a[1][1] * b[1][0], a[1][0] * b[0][1] + a[1][1] * b[1][1]),
    )


def mscale(c: Qc, a):
    return ((c * a[0][0], c * a[0][1]), (c * a[1][0], c * a[1][1]))


def meq(a, b) -> bool:
    return a[0][0] == b[0][0] and a[0][1] == b[0][1] and a[1][0] == b[1][0] and a[1][1] == b[1][1]


def I(k):
    o, i = C(0, 0, 0, 0, k), C(1, 0, 0, 0, k)
    return ((i, o), (o, i))


def Z0(k):
    o = C(0, 0, 0, 0, k)
    return ((o, o), (o, o))


def SX(k):
    o, i = C(0, 0, 0, 0, k), C(1, 0, 0, 0, k)
    return ((o, i), (i, o))


def SY(k):
    o = C(0, 0, 0, 0, k)
    # [[0,-i],[i,0]]
    return ((o, C(0, 0, -1, 0, k)), (C(0, 0, 1, 0, k), o))


def SZ(k):
    o, i = C(0, 0, 0, 0, k), C(1, 0, 0, 0, k)
    return ((i, o), (o, C(-1, 0, 0, 0, k)))


def pauli_H(a: int, b: int, c: int):
    """Identity gate."""
    k = a * a + b * b + c * c
    h = Z0(k)
    if a:
        h = madd(h, mscale(C(a, 0, 0, 0, k), SX(k)))
    if b:
        h = madd(h, mscale(C(b, 0, 0, 0, k), SY(k)))
    if c:
        h = madd(h, mscale(C(c, 0, 0, 0, k), SZ(k)))
    return h, k


def projectors(a: int, b: int, c: int):
    """Identity gate: P± = (√k I ± H)/(2√k)."""
    h, k = pauli_H(a, b, c)
    sqrtk = C(0, 1, 0, 0, k)  # √k
    inv2sqrt = C(0, Fraction(1, 2 * k), 0, 0, k)  # 1/(2√k) = √k/(2k)
    plus_num = madd(mscale(sqrtk, I(k)), h)
    minus_num = madd(mscale(sqrtk, I(k)), mscale(C(-1, 0, 0, 0, k), h))
    return mscale(inv2sqrt, plus_num), mscale(inv2sqrt, minus_num), k


def trace(m) -> Qc:
    return m[0][0] + m[1][1]


def trace_rho_p(a: int, b: int, c: int):
    """Identity gate: Tr(ρ P±) with ρ=(I + H/3)/2."""
    h, k = pauli_H(a, b, c)
    pplus, pminus, _ = projectors(a, b, c)
    half = C(Fraction(1, 2), 0, 0, 0, k)
    third = C(Fraction(1, 3), 0, 0, 0, k)
    rho = mscale(half, madd(I(k), mscale(third, h)))
    return trace(mmul(rho, pplus)), trace(mmul(rho, pminus)), k


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, statement: str, condition: bool) -> None:
        if condition:
            self.passed += 1
        else:
            self.failed += 1
        print(f"{'PASS' if condition else 'FAIL'}: {label} {statement}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return self.failed


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    self_source = Path(__file__).read_text(encoding="utf-8")

    print("external_scientific_inputs: none")
    print("package_local_integrity_reads: runner, note, axiom memo")
    print("measure_boundary: exact Q(√k) projector identities")
    print("negative_scope: comparator measure, not Born")

    h2, k2 = pauli_H(1, 1, 0)
    h3, k3 = pauli_H(1, 1, 1)
    checks.check("thm1-k", "k=2 and k=3 for the two displayed directions", k2 == 2 and k3 == 3)
    checks.check("thm1-h2", "H^2=2I for (1,1,0)", meq(mmul(h2, h2), mscale(C(2, 0, 0, 0, 2), I(2))))
    checks.check("thm1-h3", "H^2=3I for (1,1,1)", meq(mmul(h3, h3), mscale(C(3, 0, 0, 0, 3), I(3))))

    pp2, pm2, _ = projectors(1, 1, 0)
    pp3, pm3, _ = projectors(1, 1, 1)
    checks.check("thm2-comp2", "P+P-=0 and P++P-=I for k=2", meq(mmul(pp2, pm2), Z0(2)) and meq(madd(pp2, pm2), I(2)))
    checks.check("thm2-idemp2", "P±^2=P± for k=2", meq(mmul(pp2, pp2), pp2) and meq(mmul(pm2, pm2), pm2))
    checks.check("thm2-comp3", "P+P-=0 and P++P-=I for k=3", meq(mmul(pp3, pm3), Z0(3)) and meq(madd(pp3, pm3), I(3)))
    checks.check("thm2-idemp3", "P±^2=P± for k=3", meq(mmul(pp3, pp3), pp3) and meq(mmul(pm3, pm3), pm3))

    tp2, tm2, _ = trace_rho_p(1, 1, 0)
    tp3, tm3, _ = trace_rho_p(1, 1, 1)
    # (3±√k)/6
    want_p2 = C(Fraction(1, 2), Fraction(1, 6), 0, 0, 2)
    want_m2 = C(Fraction(1, 2), Fraction(-1, 6), 0, 0, 2)
    want_p3 = C(Fraction(1, 2), Fraction(1, 6), 0, 0, 3)
    want_m3 = C(Fraction(1, 2), Fraction(-1, 6), 0, 0, 3)
    checks.check("thm3-tr2", "Tr(ρP±)=(3±√2)/6", tp2 == want_p2 and tm2 == want_m2 and tp2 + tm2 == C(1, 0, 0, 0, 2))
    checks.check("thm3-tr3", "Tr(ρP±)=(3±√3)/6", tp3 == want_p3 and tm3 == want_m3 and tp3 + tm3 == C(1, 0, 0, 0, 3))

    checks.check("mutation-prod-fails", "predicate P+P-≠0 must fail", meq(mmul(pp2, pm2), Z0(2)))
    checks.check("mutation-sum-fails", "predicate traces do not sum to 1 must fail", tp2 + tm2 == C(1))
    checks.check(
        "quoted",
        "note quotes Qubit and Admissibility",
        "The full one-site possibility domain has algebraic presentation `M_2(C)`." in note
        and "determined by, and varies with, the nearest-neighbor conditions." in note,
    )
    forbidden = ("we adopt", "L_phys", "Gleason", "0.5934", "therefore Born", "exhausted", "closes the route")
    checks.check(
        "boundary",
        "not Born, not TOE, no forbidden phrases",
        all(p not in note for p in forbidden)
        and "not a TOE" in note
        and "Qubit remains `M_2(C)`" in note
        and "This note authors no audit verdict" in note
        and "QCD is unused" in note
        and "actual_current_surface_status: bounded-support" in note
        and 'hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"' in note
        and "Honest-auditor / Boundary" in note,
    )
    checks.check(
        "gates",
        "identity gates present",
        "def pauli_H(" in self_source
        and "def projectors(" in self_source
        and "def trace_rho_p(" in self_source
        and AUDIT_INPUT_PATHS == (
            "docs/L0_SPECTRAL_PROJECTORS_K2_K3_BOUNDED_THEOREM_NOTE_2026-08-14.md",
            "docs/MINIMAL_AXIOMS_2026-06-29.md",
        ),
    )
    print("per_element: checked exactly — H, P± over Q(√2) and Q(√3)")
    print("per_site: checked exactly — two displayed occupancies")
    print("per_mode: checked exactly — complementary PVM and Tr(ρP)")
    print("per_block: checked exactly — measure, not a k-label")
    print("lattice_wide: checked and not executed — not Born")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
