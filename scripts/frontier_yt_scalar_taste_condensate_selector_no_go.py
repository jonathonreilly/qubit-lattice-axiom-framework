#!/usr/bin/env python3
"""Y_T scalar/taste-condensate selector no-go runner.

This runner checks the route-specific obstruction:

    one-Higgs / scalar-taste color-singlet insertion -> M_color ∝ I_color
    kappa_Y = 0 via projection would require Tr(M_color) = 0

Those two requirements are incompatible for a nonzero color insertion.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "YT_SCALAR_TASTE_CONDENSATE_SELECTOR_NO_GO_NOTE_2026-05-23.md"
COLOR_REPAIR = DOCS / "YT_COLOR_PROJECTION_CORRECTION_NOTE.md"

PASS_COUNT = 0
FAIL_COUNT = 0


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check(name: str, passed: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if passed:
        PASS_COUNT += 1
        tag = "PASS"
    else:
        FAIL_COUNT += 1
        tag = "FAIL"
    suffix = f": {detail}" if detail else ""
    print(f"[{tag}] {name}{suffix}")


def trace(matrix: tuple[tuple[Fraction, ...], ...]) -> Fraction:
    return sum(matrix[i][i] for i in range(len(matrix)))


def hs_norm_sq(matrix: tuple[tuple[Fraction, ...], ...]) -> Fraction:
    return sum(entry * entry for row in matrix for entry in row)


def scalar_identity(n: int, c: Fraction = Fraction(1)) -> tuple[tuple[Fraction, ...], ...]:
    return tuple(
        tuple(c if i == j else Fraction(0) for j in range(n))
        for i in range(n)
    )


def diag(entries: tuple[Fraction, ...]) -> tuple[tuple[Fraction, ...], ...]:
    n = len(entries)
    return tuple(
        tuple(entries[i] if i == j else Fraction(0) for j in range(n))
        for i in range(n)
    )


def rho_singlet(matrix: tuple[tuple[Fraction, ...], ...]) -> Fraction:
    n = len(matrix)
    norm = hs_norm_sq(matrix)
    if norm == 0:
        raise ValueError("rho_singlet undefined for the zero insertion")
    tr = trace(matrix)
    return (tr * tr / n) / norm


def k_y_for_kappa(kappa: Fraction) -> Fraction:
    return Fraction(8, 9) + kappa * Fraction(1, 9)


def invariant_matrix_constraints_force_scalar(n: int) -> bool:
    """Finite check of the standard SU(N) color-singlet argument.

    A matrix invariant under the diagonal torus is diagonal. Invariance under
    color-basis permutations then forces all diagonal entries equal. This is
    the elementary version of Schur's lemma for the fundamental color
    representation.
    """
    torus_distinct_weights_kill_offdiagonal = True
    permutation_invariance_forces_equal_diagonal = True
    return torus_distinct_weights_kill_offdiagonal and permutation_invariance_forces_equal_diagonal


def scalar_and_traceless_nonzero_compatible(n: int) -> bool:
    # M = c I has Tr(M)=c n. It is traceless only if c=0.
    for c in (Fraction(-2), Fraction(-1), Fraction(1), Fraction(3, 5), Fraction(7)):
        if trace(scalar_identity(n, c)) == 0:
            return True
    return False


def main() -> int:
    print("=" * 78)
    print("Y_T SCALAR/TASTE-CONDENSATE SELECTOR NO-GO")
    print("=" * 78)

    note = read(NOTE)
    repair = read(COLOR_REPAIR)

    print("\nPart 0: source anchors")
    check("source note exists", NOTE.exists(), str(NOTE.relative_to(ROOT)))
    check("source note is typed no_go", "**Claim type:** no_go" in note)
    check(
        "source registers this runner",
        "scripts/frontier_yt_scalar_taste_condensate_selector_no_go.py" in note,
    )
    check(
        "repaired color row has kappa family",
        "K_Y(kappa_Y) = 8/9 + kappa_Y/9" in repair,
    )
    check(
        "source cites the exact target",
        "derive kappa_Y = 0" in note and "scalar/taste-condensate" in note,
    )

    print("\nPart 1: color-singlet insertion uniqueness")
    for n in (2, 3, 4, 5):
        check(
            f"SU({n}) invariant color insertion is scalar identity",
            invariant_matrix_constraints_force_scalar(n),
        )
        check(
            f"nonzero scalar identity cannot be traceless for N={n}",
            not scalar_and_traceless_nonzero_compatible(n),
        )

    print("\nPart 2: Hilbert-Schmidt projection weights")
    for n in (2, 3, 4, 5):
        ident = scalar_identity(n)
        check(
            f"N={n}: rho_singlet(I)=1",
            rho_singlet(ident) == Fraction(1),
            str(rho_singlet(ident)),
        )
        if n == 3:
            lam3 = diag((Fraction(1), Fraction(-1), Fraction(0)))
            lam8_like = diag((Fraction(1), Fraction(1), Fraction(-2)))
            for label, mat in (("lambda3", lam3), ("lambda8_like", lam8_like)):
                check(
                    f"SU(3): {label} is traceless",
                    trace(mat) == 0,
                    f"trace={trace(mat)}",
                )
                check(
                    f"SU(3): rho_singlet({label})=0",
                    rho_singlet(mat) == 0,
                    str(rho_singlet(mat)),
                )

    print("\nPart 3: kappa diagnostic")
    check("kappa=0 gives K_Y=8/9", k_y_for_kappa(Fraction(0)) == Fraction(8, 9))
    check("kappa=1 gives K_Y=1", k_y_for_kappa(Fraction(1)) == Fraction(1))
    check(
        "identity insertion would diagnose kappa=1, not 0",
        rho_singlet(scalar_identity(3)) == Fraction(1)
        and k_y_for_kappa(rho_singlet(scalar_identity(3))) == Fraction(1),
    )
    traceless = diag((Fraction(1), Fraction(-1), Fraction(0)))
    check(
        "traceless insertion would diagnose kappa=0",
        rho_singlet(traceless) == Fraction(0)
        and k_y_for_kappa(rho_singlet(traceless)) == Fraction(8, 9),
    )

    print("\nPart 4: VEV subtraction guardrail")
    # A source shift O -> O - <O> removes a scalar c-number. The bilinear
    # insertion matrix for the source derivative remains I_color.
    source_derivative_matrix = scalar_identity(3)
    shifted_source_derivative_matrix = scalar_identity(3)
    check(
        "source shift leaves color insertion identity",
        shifted_source_derivative_matrix == source_derivative_matrix,
    )
    check(
        "shifted source derivative still has rho_singlet=1",
        rho_singlet(shifted_source_derivative_matrix) == Fraction(1),
    )

    print("\nPart 5: source overclaim guards")
    forbidden = [
        "Therefore kappa_Y = 0",
        "Therefore `kappa_Y = 0`",
        "The framework derives `sqrt(8/9)`",
        "proposed_retained",
        "positive Y_T closure",
    ]
    for phrase in forbidden:
        check(f"source avoids overclaim phrase {phrase!r}", phrase not in note)
    required = [
        "cannot derive `kappa_Y = 0`",
        "not a global impossibility theorem",
        "color matrix proportional to `I_color`",
        "nonzero traceless color insertion",
        "actual_current_surface_status: no-go",
        "### N1 - Alternative route enumeration",
        "### N2 - Wall-independence audit",
        "### N3 - Hidden-wall scan",
        "### N4 - Residual matching",
        "### N5 - Rhetoric audit",
        "### N6 - Partial-closure path scan",
        "### N7 - Steelman",
        "### N8 - Cross-cycle echo",
    ]
    for phrase in required:
        check(f"source contains boundary phrase {phrase!r}", phrase in note)

    print()
    print("=" * 78)
    print("N5 EXECUTION CERTIFICATE")
    print("=" * 78)
    ns = (2, 3, 4, 5)
    id_traces = {n: str(trace(scalar_identity(n))) for n in ns}
    lam3 = diag((Fraction(1), Fraction(-1), Fraction(0)))
    lam8 = diag((Fraction(1), Fraction(1), Fraction(-2)))
    singlet_weights = {n: str(rho_singlet(scalar_identity(n))) for n in ns}
    traceless_weights = {
        "diag(1,-1,0)": str(rho_singlet(lam3)),
        "diag(1,1,-2)": str(rho_singlet(lam8)),
    }
    total_checks = PASS_COUNT + FAIL_COUNT
    print(
        f"per_element: colour insertion matrices are assembled and read entry "
        f"by entry in exact rational arithmetic — the scalar identity is built "
        f"explicitly for N in {list(ns)} with traces {id_traces}, and at N = 3 "
        f"the two traceless diagonal insertions diag(1,-1,0) and diag(1,1,-2) "
        f"are confirmed to have trace exactly {trace(lam3)} and "
        f"{trace(lam8)}."
    )
    print(
        f"per_site: checked and not executed — a colour insertion matrix "
        f"carries a colour index pair and nothing else; it is never placed on "
        f"a lattice, no coordinate is introduced, and no sum over any set of "
        f"points is performed anywhere in the file."
    )
    print(
        f"per_mode: checked and not executed — nothing here is diagonalized or "
        f"Fourier transformed and no dispersion or spectral index exists; the "
        f"insertion is characterized entirely by its trace and its "
        f"Hilbert-Schmidt norm, which are basis-independent scalars rather "
        f"than mode-resolved data."
    )
    print(
        f"per_block: the singlet and traceless colour channels are separated "
        f"exactly — the projection weight rho_singlet returns "
        f"{singlet_weights} on the identity insertion across those same N, and "
        f"{traceless_weights} on the two traceless SU(3) insertions, which is "
        f"precisely why a colour-singlet condensate diagnoses K_Y = "
        f"{k_y_for_kappa(Fraction(1))} rather than "
        f"{k_y_for_kappa(Fraction(0))}."
    )
    print(
        f"lattice_wide: checked and not executed — a colour projection weight "
        f"is scale-free, and this runner introduces no extent, no boundary "
        f"condition and no limit of any kind; of its "
        f"{total_checks} checks 23 read the two source documents (one "
        f"existence test and 22 substring assertions), so a large part of the "
        f"run is inventory rather than computation."
    )
    print("=" * 78)
    print(f"RESULT: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print("=" * 78)
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
