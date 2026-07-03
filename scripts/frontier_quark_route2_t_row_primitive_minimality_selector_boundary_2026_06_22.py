#!/usr/bin/env python3
"""Verify the Route-2 physical T-row primitive/minimality selector boundary."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from math import gcd
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]

NOTE = ROOT / "docs/QUARK_ROUTE2_T_ROW_PRIMITIVE_MINIMALITY_SELECTOR_BOUNDARY_NOTE_2026-06-22.md"
MIN_AXIOMS = ROOT / "docs/MINIMAL_AXIOMS_2026-06-05.md"
T_SIDE = ROOT / "docs/QUARK_ROUTE2_T_SIDE_ENDPOINT_THEOREM_ATTEMPT_BOUNDED_NOTE_2026-06-12.md"
S3 = ROOT / "docs/S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md"

TARGET_RHO_T = Fraction(-1)
TARGET_Q_T = Fraction(5, 6)
TARGET_S_TE = Fraction(-2)

passes = 0
fails = 0


@dataclass(frozen=True)
class Row:
    alpha_e: Fraction
    alpha_t: Fraction
    beta_t: Fraction

    def rho_t(self) -> Fraction:
        return self.beta_t / self.alpha_t

    def q_t(self) -> Fraction:
        return Fraction(1) + self.rho_t() / 6

    def s_te(self) -> Fraction:
        return self.alpha_t / self.alpha_e

    def frobenius_sq(self) -> Fraction:
        return self.alpha_e * self.alpha_e + self.alpha_t * self.alpha_t + self.beta_t * self.beta_t

    def center_deformation_abs(self) -> Fraction:
        return abs(self.beta_t / (6 * self.alpha_t))

    def full_gcd(self) -> int:
        vals = [abs(int(self.alpha_e)), abs(int(self.alpha_t)), abs(int(self.beta_t))]
        out = 0
        for val in vals:
            out = gcd(out, val)
        return out

    def t_gcd(self) -> int:
        return gcd(abs(int(self.alpha_t)), abs(int(self.beta_t)))


def compact(text: str) -> str:
    return " ".join(text.split())


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check(condition: bool, label: str, detail: str = "") -> None:
    global passes, fails
    suffix = f" -- {detail}" if detail else ""
    if condition:
        passes += 1
        print(f"PASS: {label}{suffix}")
    else:
        fails += 1
        print(f"FAIL: {label}{suffix}")


def shape_family(n: int) -> Row:
    return Row(Fraction(1), Fraction(-n), Fraction(n))


def scale_family(beta_t: int) -> Row:
    return Row(Fraction(1), Fraction(-2), Fraction(beta_t))


def main() -> int:
    print("Route-2 T-row primitive/minimality selector boundary")
    print("=" * 78)

    print("\nA. Source-note and premise boundary")
    note = read(NOTE)
    note_c = compact(note)
    note_l = note.lower()
    note_cl = note_c.lower()
    check(NOTE.exists(), "new source note exists", str(NOTE.relative_to(ROOT)))
    check("**Claim type:** no_go" in note, "new note declares no_go claim type")
    check("**Assessment role:** conditional primitive/minimality selector no-go." in note, "new note declares scoped no-go role")
    check("**Status authority:** independent audit lane only" in note, "new note leaves status authority to audit lane")
    check("`audit_status` and `effective_status` fields are pipeline-derived" in note_c, "new note leaves audit fields pipeline-derived")
    check("primitive/minimality selector boundary" in note, "new note names selector boundary")
    check("n=1" in note and "not `n=2`" in note, "new note records minimality miss")
    check("values reproduced only after a readout row is supplied" in note_c, "new note keeps endpoint target conditional")
    check("does not import an unlanded row-shape theorem" in note_l, "new note does not depend on an unlanded sibling block")
    authority_links = [
        "QUARK_ROUTE2_T_SIDE_ENDPOINT_THEOREM_ATTEMPT_BOUNDED_NOTE_2026-06-12.md](QUARK_ROUTE2_T_SIDE_ENDPOINT_THEOREM_ATTEMPT_BOUNDED_NOTE_2026-06-12.md)",
        "S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md](S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md)",
        "MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md)",
    ]
    missing_links = [link for link in authority_links if link not in note]
    check(not missing_links, "new note markdown-links load-bearing authorities", "; ".join(missing_links))
    check(
        "proposed_retained" not in note_c
        and "would become retained" not in note_c
        and "retained branch-local" not in note_c,
        "new note has no forbidden proposal wording",
    )

    authority_markers = [
        (MIN_AXIOMS, ["record supplies no readout context", "weighting, normalization"]),
        (T_SIDE, ["Missing T-row shape selector", "Missing E/T shell normalization selector"]),
        (S3, ["endpoint triple", "not yet derived"]),
    ]
    for path, markers in authority_markers:
        text = compact(read(path)).lower()
        missing = [marker for marker in markers if marker.lower() not in text]
        check(not missing, f"{path.name} contains required boundary markers", "; ".join(markers))

    print("\nB. Closed-form family identities")
    n = sp.symbols("n", integer=True, positive=True)
    beta = sp.symbols("beta_T", integer=True, nonnegative=True)

    shape_rho = sp.simplify(n / (-n))
    shape_q = sp.simplify(1 + shape_rho / 6)
    shape_s = sp.simplify((-n) / 1)
    shape_norm_minus_n1 = sp.factor((1 + 2 * n**2) - 3)
    shape_center_deformation = sp.simplify(abs(n / (6 * (-n))))
    check(shape_rho == sp.Rational(-1), "closed form: shape family keeps rho_T=-1 for every n>=1")
    check(shape_q == sp.Rational(5, 6), "closed form: shape family keeps q_T=5/6 for every n>=1")
    check(shape_s == -n, "closed form: shape family has s_TE=-n")
    check(sp.gcd(1, n, n) == 1, "closed form: full integer-row gcd leaves every n primitive")
    check(sp.gcd(n, n) == n, "closed form: T-subrow gcd selects n=1 as the primitive member")
    check(
        sp.simplify(shape_norm_minus_n1 - 2 * (n - 1) * (n + 1)) == 0,
        "closed form: Frobenius norm is minimized at n=1 for n>=1",
    )
    check(shape_center_deformation == sp.Rational(1, 6), "closed form: center deformation ties across n>=1")

    scale_rho = sp.simplify(beta / -2)
    scale_q = sp.simplify(1 + scale_rho / 6)
    scale_s = sp.simplify(sp.Rational(-2, 1) / 1)
    scale_norm_minus_beta0 = sp.factor((5 + beta**2) - 5)
    scale_norm_minus_beta1 = sp.factor((5 + beta**2) - 6)
    check(scale_s == -2, "closed form: fixed-shell beta family keeps s_TE=-2")
    check(scale_rho.subs(beta, 2) == sp.Rational(-1), "closed form: beta_T=2 gives target rho_T")
    check(scale_q.subs(beta, 2) == sp.Rational(5, 6), "closed form: beta_T=2 gives target q_T")
    check(scale_norm_minus_beta0 == beta**2, "closed form: fixed-shell Frobenius norm is minimized at beta_T=0")
    check(scale_norm_minus_beta1 == (beta - 1) * (beta + 1), "closed form: positive-beta minimality selects beta_T=1")

    print("\nC. Shape-supplied integer family witnesses")
    rows = [shape_family(n) for n in range(1, 6)]
    for n, row in enumerate(rows, start=1):
        check(row.rho_t() == TARGET_RHO_T, f"shape family n={n} keeps rho_T=-1")
        check(row.q_t() == TARGET_Q_T, f"shape family n={n} keeps q_T=5/6")
        check(row.s_te() == Fraction(-n), f"shape family n={n} has s_TE=-n")

    target = shape_family(2)
    primitive = shape_family(1)
    check(target.s_te() == TARGET_S_TE, "n=2 is the target shell quotient")
    check(primitive.s_te() == Fraction(-1), "n=1 misses target shell quotient")
    check(target.full_gcd() == 1, "target full triple is primitive as a three-entry row")
    check(primitive.full_gcd() == 1, "n=1 full triple is also primitive")
    check(target.t_gcd() == 2, "target T subrow is not primitive by gcd")
    check(primitive.t_gcd() == 1, "n=1 T subrow is primitive by gcd")

    print("\nD. Minimality selector witnesses miss n=2")
    min_norm = min(rows, key=lambda row: row.frobenius_sq())
    min_abs_shell = min(rows, key=lambda row: abs(row.alpha_t))
    check(min_norm == primitive, "minimal Frobenius selector picks n=1")
    check(
        all(row.center_deformation_abs() == primitive.center_deformation_abs() for row in rows),
        "minimal center-deformation selector leaves all sampled n tied",
    )
    check(min_abs_shell == primitive, "minimal shell magnitude selector picks n=1")
    check(target.frobenius_sq() == Fraction(9), "target n=2 Frobenius norm square is 9")
    check(primitive.frobenius_sq() == Fraction(3), "n=1 Frobenius norm square is 3")
    check(primitive.frobenius_sq() < target.frobenius_sq(), "minimal norm prefers n=1 over n=2")
    check("minimal frobenius norm" in note_l and "`n=1`" in note, "note records norm miss")
    check("primitive T-subrow gcd" in note and "selects `n=1`" in note, "note records gcd miss")

    print("\nE. Shell-scale supplied beta family witnesses")
    shell_rows = [scale_family(beta) for beta in range(0, 5)]
    for beta, row in enumerate(shell_rows):
        check(row.s_te() == TARGET_S_TE, f"shell family beta={beta} keeps s_TE=-2")
    check(scale_family(2).rho_t() == TARGET_RHO_T, "beta=2 gives target rho_T")
    check(scale_family(2).q_t() == TARGET_Q_T, "beta=2 gives target q_T")
    check(scale_family(0).rho_t() == Fraction(0), "beta=0 misses rho_T")
    check(scale_family(0).q_t() == Fraction(1), "beta=0 misses q_T")
    check(scale_family(1).rho_t() == Fraction(-1, 2), "beta=1 misses rho_T")
    check(scale_family(1).q_t() == Fraction(11, 12), "beta=1 misses q_T")
    check(min(shell_rows, key=lambda row: row.frobenius_sq()) == scale_family(0), "fixed-shell minimal norm picks beta=0")
    check(min([row for row in shell_rows if row.beta_t > 0], key=lambda row: abs(row.beta_t)) == scale_family(1), "smallest positive beta picks beta=1")

    print("\nF. Selector firewall")
    check("no approved premise supplies the multiplicity-two rule" in note_l, "note names missing multiplicity-two rule")
    check("evenness is not supplied" in note_l, "note blocks hidden parity import")
    check("the target `n=2` remains an extra selector" in note_cl, "note preserves target boundary")
    check("does not set, predict, or estimate any audit verdict" in note_cl, "note leaves audit authority untouched")
    check("the enumerated selectors do not derive the full t row" in note_cl, "note limits no-go to enumerated selectors")
    check("the enumerated minimality tests select `beta_T=0` or `beta_T=1`" in note_c, "note records fixed-shell beta-family miss")

    print("\n" + "=" * 78)
    print(f"TOTAL: PASS={passes}, FAIL={fails}")
    if fails:
        print("STATUS: failure in T-row primitive/minimality selector verifier.")
        return 1
    print(
        "STATUS: scoped no-go/exact support. The enumerated primitive-integer "
        "and minimality selectors do not select the full Route-2 T row (1,-2,2); "
        "the missing positive premise is a non-circular multiplicity-two or "
        "full-row selector."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
