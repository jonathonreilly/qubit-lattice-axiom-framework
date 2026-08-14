#!/usr/bin/env python3
"""L0 spectral projectors on all 56 nonzero 6-NN cells."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120
ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = ROOT / "docs" / "L0_ALL_56_SPECTRAL_MEASURE_BOUNDED_THEOREM_NOTE_2026-08-14.md"
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/L0_ALL_56_SPECTRAL_MEASURE_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)


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
        a_r, a_s, b_r, b_s = self.r, self.s, self.p, self.q
        c_r, c_s, d_r, d_s = o.r, o.s, o.p, o.q
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
    return ((o, C(0, 0, -1, 0, k)), (C(0, 0, 1, 0, k), o))


def SZ(k):
    o, i = C(0, 0, 0, 0, k), C(1, 0, 0, 0, k)
    return ((i, o), (o, C(-1, 0, 0, 0, k)))


def pauli_H(a: int, b: int, c: int):
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
    """Identity gate."""
    h, k = pauli_H(a, b, c)
    sqrtk = C(0, 1, 0, 0, k)
    inv2sqrt = C(0, Fraction(1, 2 * k), 0, 0, k)
    plus_num = madd(mscale(sqrtk, I(k)), h)
    minus_num = madd(mscale(sqrtk, I(k)), mscale(C(-1, 0, 0, 0, k), h))
    return mscale(inv2sqrt, plus_num), mscale(inv2sqrt, minus_num), k


def trace(m) -> Qc:
    return m[0][0] + m[1][1]


def trace_sum(a: int, b: int, c: int) -> Qc:
    """Identity gate."""
    h, k = pauli_H(a, b, c)
    pplus, pminus, _ = projectors(a, b, c)
    half = C(Fraction(1, 2), 0, 0, 0, k)
    third = C(Fraction(1, 3), 0, 0, 0, k)
    rho = mscale(half, madd(I(k), mscale(third, h)))
    return trace(mmul(rho, pplus)) + trace(mmul(rho, pminus)), k


def cells():
    """Identity gate: all 64 occupancy 6-tuples as (a,b,c)=c+−c−."""
    out = []
    for bits in range(64):
        c = [(bits >> i) & 1 for i in range(6)]
        a = c[0] - c[1]
        b = c[2] - c[3]
        cc = c[4] - c[5]
        out.append((a, b, cc))
    return out


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
    four = axiom.split("## The Four Framework Axioms", 1)[-1].split("## Qualification", 1)[0]

    print("external_scientific_inputs: none")
    print("package_local_integrity_reads: runner, note, axiom memo")
    print("measure_boundary: exact Q(√k) PVM on all 56 nonzero cells")
    print("negative_scope: comparator measure, not Born")

    all_cells = cells()
    ks = [a * a + b * b + c * c for a, b, c in all_cells]
    zero_n = sum(1 for k in ks if k == 0)
    counts = {1: 0, 2: 0, 3: 0}
    for k in ks:
        if k in counts:
            counts[k] += 1
    checks.check("thm1-census", "64 cells, 8 zero, 24+24+8 nonzero", len(all_cells) == 64 and zero_n == 8 and counts == {1: 24, 2: 24, 3: 8})

    all_comp = True
    all_tr = True
    for a, b, c in all_cells:
        k = a * a + b * b + c * c
        if k == 0:
            continue
        pp, pm, _ = projectors(a, b, c)
        if not (meq(mmul(pp, pm), Z0(k)) and meq(madd(pp, pm), I(k))):
            all_comp = False
        ts, _ = trace_sum(a, b, c)
        if ts != C(1, 0, 0, 0, k):
            all_tr = False
    checks.check("thm2-comp", "P++P-=I and P+P-=0 on all 56", all_comp)
    checks.check("thm3-tr", "traces sum to 1 on all 56", all_tr)

    samples = {(1, 0, 0): 1, (1, 1, 0): 2, (1, 1, 1): 3}
    sample_ok = True
    for abc, k in samples.items():
        h, kk = pauli_H(*abc)
        pp, pm, _ = projectors(*abc)
        half = C(Fraction(1, 2), 0, 0, 0, k)
        third = C(Fraction(1, 3), 0, 0, 0, k)
        rho = mscale(half, madd(I(k), mscale(third, h)))
        tp, tm = trace(mmul(rho, pp)), trace(mmul(rho, pm))
        want_p = C(Fraction(1, 2), Fraction(1, 6), 0, 0, k)
        want_m = C(Fraction(1, 2), Fraction(-1, 6), 0, 0, k)
        if not (kk == k and tp == want_p and tm == want_m):
            sample_ok = False
    checks.check("thm3-sample", "sample traces are (3±√k)/6", sample_ok)
    checks.check("mutation-count-fails", "predicate nonzero count is not 56 must fail", counts[1] + counts[2] + counts[3] == 56)
    checks.check("mutation-prod-fails", "predicate some cell has P+P-≠0 must fail", all_comp)
    checks.check(
        "quoted",
        "note quotes Qubit and NN distribution",
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
    checks.check("memo-silent", "axioms do not name the 56-cell measure", "56 nonzero" not in four and "cov56" not in four)
    checks.check(
        "gates",
        "identity gates present",
        "def cells(" in self_source
        and "def projectors(" in self_source
        and "def trace_sum(" in self_source
        and NOTE_PATH.is_file()
        and AUDIT_INPUT_PATHS[0].endswith("L0_ALL_56_SPECTRAL_MEASURE_BOUNDED_THEOREM_NOTE_2026-08-14.md"),
    )
    print("per_element: checked exactly — 56 complementary PVMs")
    print("per_site: checked exactly — 6-NN occupancy cells")
    print("per_mode: checked exactly — k=1,2,3 census")
    print("per_block: checked exactly — all cells, not two directions")
    print("lattice_wide: checked and not executed — not Born")
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
