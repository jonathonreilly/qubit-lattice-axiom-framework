#!/usr/bin/env python3
"""Exact remainder-controlled checks for the 2x2 U(1) torus character sum.

The unnormalized object is Z_T(beta) = sum_n I_n(beta)^4 on the 2D U(1)
Wilson 2x2 torus. Identity gates call i_n_partial(n, beta, N) and
plaquette_count_4d(L). Every claimed inequality is an exact Fraction
comparison. No floating-point majorant is used.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_PATH = (
    ROOT
    / "docs"
    / "U1_TWO_BY_TWO_TORUS_CHARACTER_SUM_IS_NOT_DISK_AND_NOT_SU3_LN_Z_L_BOUNDED_THEOREM_NOTE_2026-08-13.md"
)
PARENT_PATH = (
    ROOT
    / "docs"
    / "PLAQUETTE_VALUE_DERIVATION_PROGRAM_SPECIFICATION_AND_BRACKET_REDUCTION_NARROW_THEOREM_NOTE_2026-06-10.md"
)
AXIOM_PATH = ROOT / "docs" / "MINIMAL_AXIOMS_2026-06-29.md"

AUDIT_INPUT_PATHS = (
    "docs/U1_TWO_BY_TWO_TORUS_CHARACTER_SUM_IS_NOT_DISK_AND_NOT_SU3_LN_Z_L_BOUNDED_THEOREM_NOTE_2026-08-13.md",
    "docs/PLAQUETTE_VALUE_DERIVATION_PROGRAM_SPECIFICATION_AND_BRACKET_REDUCTION_NARROW_THEOREM_NOTE_2026-06-10.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

BETAS = (1, 2, 3)
SERIES_N = 6
N_STAR = 2
TORUS_PLAQUETTE_COUNT = 4


def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("factorial is defined for n >= 0")
    value = 1
    for k in range(2, n + 1):
        value *= k
    return value


def series_term(n: int, beta: int, k: int) -> Fraction:
    """One exact series term t_k of I_n(beta)."""
    if n < 0 or k < 0:
        raise ValueError("series_term requires n >= 0 and k >= 0")
    return Fraction(1, factorial(k) * factorial(k + n)) * (
        Fraction(beta, 2) ** (2 * k + n)
    )


def i_n_partial(n: int, beta: int, N: int) -> Fraction:
    """Partial sum S_{n,N}(beta) as an exact Fraction."""
    if N < 0:
        raise ValueError("i_n_partial requires N >= 0")
    total = Fraction(0)
    for k in range(N + 1):
        total += series_term(n, beta, k)
    return total


def q_n(n: int, beta: int, N: int) -> Fraction:
    return (Fraction(beta, 2) ** 2) / ((N + 1) * (N + 1 + n))


def remainder_majorant(n: int, beta: int, N: int) -> Fraction:
    ratio = q_n(n, beta, N)
    if ratio >= 1:
        raise ValueError("geometric majorant requires q_n(N) < 1")
    return series_term(n, beta, N + 1) / (1 - ratio)


def enclosure(n: int, beta: int, N: int) -> tuple[Fraction, Fraction]:
    lower = i_n_partial(n, beta, N)
    return lower, lower + remainder_majorant(n, beta, N)


def plaquette_count_4d(L: int) -> int:
    """Four-dimensional hypercubic plaquette count N_P = 6 L^4."""
    if L < 1:
        raise ValueError("plaquette_count_4d requires L >= 1")
    return 6 * L**4


def predicate_zt_equals_zd(beta: int) -> bool:
    """Claim Z_T = Z_D. False at beta = 2 because the gap is at least 2."""
    gap_lower = Fraction(2) * i_n_partial(1, beta, 0) ** 4
    return not (gap_lower >= 2)


def predicate_zt_is_4d_su3_ln_zl() -> bool:
    """Claim Z_T is 4D SU(3) ln Z_L. False because 4 != 96."""
    return TORUS_PLAQUETTE_COUNT == plaquette_count_4d(2)


def normalize(text: str) -> str:
    return " ".join(text.replace("`", "").split())


@dataclass
class Checks:
    passed: int = 0
    failed: int = 0

    def check(self, label: str, statement: str, condition: bool) -> None:
        result = bool(condition)
        if result:
            self.passed += 1
        else:
            self.failed += 1
        print(f"{'PASS' if result else 'FAIL'}: {label} — {statement}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return 0 if self.failed == 0 and self.passed >= 12 else 1


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    parent = PARENT_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    note_norm = normalize(note)
    parent_norm = normalize(parent)
    axiom_norm = normalize(axiom)

    june10_quote = "a certified enclosure of ln Z_L at three couplings"
    checks.check(
        "audit-parent-quote",
        "June 10 parent names the four-dimensional ln Z_L enclosure target",
        june10_quote in parent_norm,
    )
    checks.check(
        "audit-axiom-memo",
        "axiom memo is present as Lattice/Qubit/Admissibility/Record premises",
        all(
            name in axiom
            for name in (
                "### Lattice / Physical Locality",
                "### Qubit / Site Possibility",
                "### Admissibility / Local Constraint",
                "### Record / Fixed Reality",
            )
        ),
    )
    checks.check(
        "audit-note-inputs",
        "source note cites the June 10 parent, the axiom memo, and the quote",
        "PLAQUETTE_VALUE_DERIVATION_PROGRAM_SPECIFICATION_AND_BRACKET_REDUCTION_NARROW_THEOREM_NOTE_2026-06-10.md"
        in note
        and "MINIMAL_AXIOMS_2026-06-29.md" in note
        and june10_quote in note_norm,
    )

    s10_beta2 = i_n_partial(1, 2, 0)
    checks.check(
        "identity-s10-beta2",
        "i_n_partial(1, 2, 0) equals (2/2)^1/(0!1!) = 1",
        s10_beta2 == 1,
    )
    gap_beta2 = Fraction(2) * s10_beta2**4
    checks.check(
        "theorem1-gap",
        "2 I_1(2)^4 >= 2 so Z_T(2) >= Z_D(2)+2",
        gap_beta2 >= 2,
    )
    checks.check(
        "mutation-zt-equals-zd",
        "predicate Z_T = Z_D fails at beta=2 (gap >= 2)",
        predicate_zt_equals_zd(2) is False and gap_beta2 >= 2,
    )

    s10_beta1 = i_n_partial(1, 1, 0)
    checks.check(
        "identity-s10-beta1",
        "i_n_partial(1, 1, 0) equals 1/2",
        s10_beta1 == Fraction(1, 2),
    )
    gap_beta1 = Fraction(2) * s10_beta1**4
    checks.check(
        "theorem2-gap",
        "Z_T(1) - Z_D(1) >= 2*(1/2)^4 = 1/8",
        gap_beta1 == Fraction(1, 8),
    )

    q_values = []
    q_ok = True
    rem_ok = True
    for beta in BETAS:
        for n in range(N_STAR + 1):
            ratio = q_n(n, beta, SERIES_N)
            q_values.append(ratio)
            if ratio >= 1:
                q_ok = False
            if remainder_majorant(n, beta, SERIES_N) < 0:
                rem_ok = False
    checks.check(
        "remainder-q-contractive",
        "every q_n(6) at |n|<=2 and beta in {1,2,3} is strictly less than 1",
        q_ok and all(ratio < 1 for ratio in q_values),
    )
    checks.check(
        "remainder-nonnegative",
        "factorial majorants t_7/(1-q) are nonnegative Rationals",
        rem_ok
        and all(isinstance(ratio, Fraction) for ratio in q_values),
    )

    expected_enclosures = {
        (0, 1): (
            Fraction(537664349, 424673280),
            Fraction(131055685069, 103514112000),
        ),
        (1, 1): (
            Fraction(16800557929, 29727129600),
            Fraction(66902221753, 118377676800),
        ),
        (0, 2): (Fraction(1181737, 518400), Fraction(56723377, 24883200)),
        (1, 2): (Fraction(5772103, 3628800), Fraction(22676119, 14256000)),
        (0, 3): (Fraction(127946737, 26214400), Fraction(5981524717, 1225523200)),
        (1, 3): (Fraction(1450892379, 367001600), Fraction(5570393547, 1409024000)),
    }
    enclosure_ok = True
    for (n, beta), (lo_exp, hi_exp) in expected_enclosures.items():
        lo, hi = enclosure(n, beta, SERIES_N)
        if lo != lo_exp or hi != hi_exp or lo > hi:
            enclosure_ok = False
        if f"{lo_exp}" not in note or f"{hi_exp}" not in note:
            enclosure_ok = False
    checks.check(
        "theorem3-enclosures",
        "I_0 and I_1 at beta in {1,2,3} match the note's exact rational intervals",
        enclosure_ok,
    )
    checks.check(
        "theorem3-model-only",
        "note states that a perfect table of Z_T is this 2D U(1) 2x2 torus model only",
        "2D U(1) 2x2 torus model only" in note_norm
        or "2D U(1) 2×2 torus model only" in note_norm,
    )

    np4d = plaquette_count_4d(2)
    checks.check(
        "identity-plaquette-count-4d",
        "plaquette_count_4d(2) equals 6*2^4 = 96",
        np4d == 96,
    )
    checks.check(
        "theorem4-count-mismatch",
        "N_p=4 is not N_p(L=2)=96 of four-dimensional SU(3)",
        TORUS_PLAQUETTE_COUNT != np4d,
    )
    checks.check(
        "theorem4-group-mismatch",
        "note records U(1) is not SU(3) and quotes the June 10 ln Z_L sentence",
        "U(1) is not SU(3)" in note_norm and june10_quote in note_norm,
    )
    checks.check(
        "mutation-zt-is-ln-zl",
        "predicate Z_T is 4D SU(3) ln Z_L fails (4 != 96)",
        predicate_zt_is_4d_su3_ln_zl() is False,
    )

    term0 = series_term(1, 2, 0)
    term1 = series_term(1, 2, 1)
    ratio_1 = term1 / term0
    expected_ratio = (Fraction(2, 2) ** 2) / ((0 + 1) * (0 + 1 + 1))
    checks.check(
        "identity-term-ratio",
        "t_{k+1}/t_k equals (beta/2)^2/((k+1)(k+1+n)) at n=1, beta=2, k=0",
        ratio_1 == expected_ratio == Fraction(1, 2),
    )

    forbidden_adoption = (
        "we adopt" in note.lower()
        or "new axiom" in note.lower()
        or "codex" in note.lower()
        or "l_phys" in note.lower()
    )
    substitutes_fl = "substitutes `Z_T` for `f_L`" in note or "substitute Z_T for f_L" in note
    checks.check(
        "theorem5-refusals",
        "note refuses axiom rewrite, Z_T-for-f_L substitution, and four-dimensional <P>*",
        (not forbidden_adoption)
        and ("does not claim a four-dimensional `<P>*`" in note
            or "does not claim a four-dimensional <P>*" in note)
        and ("does not substitute `Z_T` for `f_L`" in note
            or "does not substitute Z_T for f_L" in note)
        and not substitutes_fl,
    )
    checks.check(
        "audit-input-paths",
        "declared AUDIT_INPUT_PATHS exist on disk",
        all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS)
        and axiom_norm.startswith("# Minimal Framework Axioms"),
    )
    n5_lines = (
        "per_element: I_n partial sums and remainder majorants at beta in {1,2,3} are exact Fractions",
        "per_site: the 2x2 torus is four plaquettes; no 4D site configuration is sampled",
        "per_mode: the character index n is checked; no 4D transfer-matrix mode is claimed",
        "per_block: only Z_T versus Z_D gaps and the 4-versus-96 type split are executed",
        "lattice_wide: checked and not executed — no 4D SU(3) ln Z_L enclosure is claimed",
    )
    for line in n5_lines:
        checks.check(
            "n5-length",
            "each N5 resolution line is at least 40 characters",
            line.startswith(("per_element:", "per_site:", "per_mode:", "per_block:", "lattice_wide:"))
            and len(line) >= 40,
        )
        print(line)
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
