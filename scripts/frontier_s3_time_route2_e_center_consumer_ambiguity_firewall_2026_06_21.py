#!/usr/bin/env python3
r"""Exact S3/Route-2 consumer ambiguity firewall.

This runner checks the narrow downstream consequence of the unresolved
Route-2 readout endpoint after the T-side entries are granted.  On the
reduced one-parameter family

    P(rho_E) = [[1, 0, rho_E, 0],
                [0, -2, 0, 2]],

the difference between two admissible maps is supported only on the
E-center/center-excess carrier coordinate.  The result is exact support for
the S3-time `Theta_R -> Lambda_R` consumer boundary, not a derivation of
rho_E = 21/4.
"""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
NOTE = REPO_ROOT / "docs" / "S3_TIME_ROUTE2_E_CENTER_CONSUMER_AMBIGUITY_FIREWALL_NOTE_2026-06-21.md"
PARENT_NOTE = REPO_ROOT / "docs" / "S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md"
READOUT_NOTE = REPO_ROOT / "docs" / "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md"
TIME_NOTE = REPO_ROOT / "docs" / "QUARK_ROUTE2_EXACT_TIME_COUPLING_NOTE_2026-04-19.md"

Vector4 = tuple[Fraction, Fraction, Fraction, Fraction]
Vector2 = tuple[Fraction, Fraction]
Vector3 = tuple[Fraction, Fraction, Fraction]
Tensor23 = tuple[tuple[Fraction, Fraction, Fraction], tuple[Fraction, Fraction, Fraction]]

PASS_COUNT = 0
FAIL_COUNT = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"
    line = f"  [{status}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)


def text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def p_rho(rho_e: Fraction) -> tuple[Vector4, Vector4]:
    return (
        (Fraction(1), Fraction(0), rho_e, Fraction(0)),
        (Fraction(0), Fraction(-2), Fraction(0), Fraction(2)),
    )


def mat_vec(matrix: tuple[Vector4, Vector4], carrier: Vector4) -> Vector2:
    return tuple(sum(row[i] * carrier[i] for i in range(4)) for row in matrix)  # type: ignore[return-value]


def vec2_sub(left: Vector2, right: Vector2) -> Vector2:
    return (left[0] - right[0], left[1] - right[1])


def tensor(readout: Vector2, slice_vector: Vector3) -> Tensor23:
    return (
        tuple(readout[0] * entry for entry in slice_vector),  # type: ignore[return-value]
        tuple(readout[1] * entry for entry in slice_vector),  # type: ignore[return-value]
    )


def tensor_sub(left: Tensor23, right: Tensor23) -> Tensor23:
    return (
        tuple(left[0][i] - right[0][i] for i in range(3)),  # type: ignore[return-value]
        tuple(left[1][i] - right[1][i] for i in range(3)),  # type: ignore[return-value]
    )


def apply_functional(functional: Vector2, readout: Vector2) -> Fraction:
    return functional[0] * readout[0] + functional[1] * readout[1]


def expected_readout_delta(rho_a: Fraction, rho_b: Fraction, carrier: Vector4) -> Vector2:
    delta_e = carrier[2]
    return ((rho_b - rho_a) * delta_e, Fraction(0))


def carriers() -> dict[str, Vector4]:
    return {
        "E-shell": (Fraction(1), Fraction(0), Fraction(0), Fraction(0)),
        "E-center": (Fraction(1), Fraction(0), Fraction(1, 6), Fraction(0)),
        "T-shell": (Fraction(0), Fraction(1), Fraction(0), Fraction(0)),
        "T-center": (Fraction(0), Fraction(1), Fraction(0), Fraction(1, 6)),
        "mixed": (Fraction(3, 2), Fraction(-5, 3), Fraction(7, 11), Fraction(-2, 13)),
        "delta-E-blind": (Fraction(2), Fraction(-3), Fraction(0), Fraction(5, 7)),
    }


def part1_note_and_authority_boundary() -> None:
    print("\n" + "=" * 72)
    print("PART 1: source-note and authority boundary")
    print("=" * 72)

    note = text(NOTE)
    parent = text(PARENT_NOTE)
    readout = text(READOUT_NOTE)
    time = text(TIME_NOTE)

    check(
        "firewall note is exact-support and not endpoint closure",
        "**Claim type:** bounded_theorem" in note
        and "bounded support boundary" in note
        and "does not derive `rho_E = 21/4`" in note
        and "unique" in note
        and "exact `Theta_R -> Lambda_R` coupling theorem" in note,
        "status and scope firewall are explicit",
    )
    check(
        "parent consumer still names the missing readout-map endpoint triple",
        "readout-map endpoint triple" in parent
        and "remains `open_gate` until that target closes upstream" in parent,
        "block08 does not edit the parent open gate",
    )
    check(
        "upstream readout authority exposes the one-parameter family P(rho_E)",
        "P(rho_E) = [[1, 0, rho_E, 0]," in readout
        and "beta_E / alpha_E = 21/4" in readout,
        "one missing E-channel map entry is the source ambiguity",
    )
    check(
        "upstream time authority supplies the conditional Xi_P family",
        "Xi_P(t ; c) = (P_R c)" in time
        and "does **not** determine one\nunique exact `Theta_R -> Lambda_R`" in time,
        "time dynamics are conditional on the readout map",
    )


def part2_exact_readout_support_formula() -> None:
    print("\n" + "=" * 72)
    print("PART 2: exact readout support formula")
    print("=" * 72)

    rho_zero = Fraction(0)
    rho_target = Fraction(21, 4)
    p_zero = p_rho(rho_zero)
    p_target = p_rho(rho_target)

    all_formula_ok = True
    all_t_components_zero = True
    for name, carrier in carriers().items():
        diff = vec2_sub(mat_vec(p_target, carrier), mat_vec(p_zero, carrier))
        expected = expected_readout_delta(rho_zero, rho_target, carrier)
        print(f"  {name:<13s} delta = {diff}, expected = {expected}")
        all_formula_ok = all_formula_ok and diff == expected
        all_t_components_zero = all_t_components_zero and diff[1] == 0

    e_shell = carriers()["E-shell"]
    e_center = carriers()["E-center"]
    shell_readout_zero = mat_vec(p_zero, e_shell)
    shell_readout_target = mat_vec(p_target, e_shell)
    center_readout_zero = mat_vec(p_zero, e_center)
    center_readout_target = mat_vec(p_target, e_center)

    q_e_zero = center_readout_zero[0] / shell_readout_zero[0]
    q_e_target = center_readout_target[0] / shell_readout_target[0]

    check(
        "for every checked carrier, P(rho_target)c - P(rho_zero)c = ((rho_target-rho_zero) delta_E, 0)",
        all_formula_ok,
        "the ambiguity is supported only on the E-center/center-excess coordinate",
    )
    check(
        "changing rho_E never changes the T-readout row on the restricted carrier class",
        all_t_components_zero,
        "the unresolved endpoint is an E-channel ambiguity, not a T-channel ambiguity",
    )
    check(
        "rho_E=0 and rho_E=21/4 agree at E-shell but differ at E-center by 7/8",
        shell_readout_zero == shell_readout_target
        and vec2_sub(center_readout_target, center_readout_zero) == (Fraction(7, 8), Fraction(0)),
        "E-shell normalization cannot select the endpoint value",
    )
    check(
        "rho_E=21/4 gives q_E=15/8 while rho_E=0 gives q_E=1",
        q_e_target == Fraction(15, 8) and q_e_zero == Fraction(1),
        "the target lift is exactly the unresolved E-channel ratio",
    )


def part3_exact_consumer_factorization() -> None:
    print("\n" + "=" * 72)
    print("PART 3: exact Theta_R -> Lambda_R consumer factorization")
    print("=" * 72)

    rho_a = Fraction(-3, 5)
    rho_b = Fraction(21, 4)
    slice_vector = (Fraction(2), Fraction(-1, 3), Fraction(5, 7))
    all_tensor_ok = True

    for name, carrier in carriers().items():
        xi_a = tensor(mat_vec(p_rho(rho_a), carrier), slice_vector)
        xi_b = tensor(mat_vec(p_rho(rho_b), carrier), slice_vector)
        observed = tensor_sub(xi_b, xi_a)
        expected = tensor(expected_readout_delta(rho_a, rho_b, carrier), slice_vector)
        print(f"  {name:<13s} tensor delta = {observed}")
        all_tensor_ok = all_tensor_ok and observed == expected

    check(
        "Delta Xi_P(t;c) factorizes as ((rho_b-rho_a) delta_E, 0) tensor V_R(t)",
        all_tensor_ok,
        "the downstream ambiguity is rank-one in the E-readout amplitude",
    )


def part4_blind_and_sensitive_sectors() -> None:
    print("\n" + "=" * 72)
    print("PART 4: blind and sensitive consumer sectors")
    print("=" * 72)

    rho_a = Fraction(0)
    rho_b = Fraction(21, 4)
    p_a = p_rho(rho_a)
    p_b = p_rho(rho_b)
    e_blind_functional = (Fraction(0), Fraction(1))
    e_sensitive_functional = (Fraction(1), Fraction(0))

    delta_e_zero_ok = True
    for name in ("E-shell", "T-shell", "T-center", "delta-E-blind"):
        carrier = carriers()[name]
        delta = vec2_sub(mat_vec(p_b, carrier), mat_vec(p_a, carrier))
        delta_e_zero_ok = delta_e_zero_ok and delta == (Fraction(0), Fraction(0))

    functional_blind_ok = True
    functional_sensitive_hit = False
    for carrier in carriers().values():
        delta = vec2_sub(mat_vec(p_b, carrier), mat_vec(p_a, carrier))
        functional_blind_ok = functional_blind_ok and apply_functional(e_blind_functional, delta) == 0
        functional_sensitive_hit = (
            functional_sensitive_hit or apply_functional(e_sensitive_functional, delta) != 0
        )

    check(
        "all carriers with delta_E=0 are invariant under changes of rho_E",
        delta_e_zero_ok,
        "shell columns and T-only center columns cannot see the missing E endpoint",
    )
    check(
        "readout post-functionals with zero E-readout component are blind for all carriers",
        functional_blind_ok,
        "T-only downstream consumers are rho_E-independent",
    )
    check(
        "an E-readout-sensitive consumer on a carrier with delta_E != 0 distinguishes rho_E values",
        functional_sensitive_hit,
        "unique E-center coupling still needs rho_E=21/4 or an equivalent primitive",
    )


def part5_n5_execution_certificate() -> None:
    """Print-only record of what this runner resolves at each granularity.

    Adds no check and touches no counter.
    """
    print("\n" + "=" * 72)
    print("PART 5: N5 execution certificate (print-only; adds no check and no counter)")
    print("=" * 72)
    print(
        "per_element: resolved as exact rational entries -- Parts 2 through 4 run wholly in Fraction "
        "arithmetic with no floating point, and the ambiguity is pinned to one slot: subtracting "
        "P(rho_a)c from P(rho_b)c across the six named carriers returns "
        "((rho_b - rho_a) * delta_E, 0) in every case, so among the eight entries of the 2x4 readout "
        "only the one multiplying the third carrier coordinate is free to move. At the E-center "
        "carrier the two endpoints separate by exactly 7/8 while the E ratio q_E goes from 1 to 15/8; "
        "both are exact rationals and are printed literally."
    )
    print(
        "per_site: checked and not executed -- the four carrier coordinates are channel labels on an "
        "abstract readout column, and the words shell and center name two already-contracted "
        "amplitudes rather than enumerated lattice points. No coordinate, adjacency, or per-site "
        "value is constructed anywhere in the file, so there is no site-level quantity to report."
    )
    print(
        "per_mode: resolved by holding the two readout rows apart -- row 0 carries the E channel and "
        "row 1 the T channel, and the file's decisive negative result is that the second component of "
        "every computed difference vanishes on all six carriers. Moving rho_E is therefore an "
        "E-mode-only motion with the T mode pinned at its granted entries -2 and 2, and Part 4 "
        "re-derives the same split from the consumer side."
    )
    print(
        "per_block: resolved as a blind-versus-sensitive sector split -- the readout carries an E "
        "block on carrier coordinates 0 and 2 and a T block on coordinates 1 and 3, and Part 4 "
        "partitions downstream consumers along it: every post-functional whose E-readout component "
        "vanishes is verified blind to rho_E on all six carriers, while an E-sensitive functional on "
        "a carrier with nonzero center excess separates the endpoints. The four carriers carrying "
        "delta_E = 0 form the invariant block and are listed by name."
    )
    print(
        "lattice_wide: checked and not executed -- no grid, volume, or size parameter appears here; "
        "the entire run is one 2x4 rational matrix, six four-component carriers, and one "
        "three-component slice vector. The obstruction is the one the note names for itself: the "
        "endpoint rho_E is still open, so the exact Theta_R -> Lambda_R coupling theorem that any "
        "lattice-wide statement would have to consume does not yet exist to be tested."
    )
    print(
        "Scope of Part 1: those four checks are substring tests against source notes on disk. They "
        "resolve no matrix element, no mode, and no block -- they inventory authority text only, and "
        "every quantitative result certified above comes from Parts 2 through 4."
    )
    print(
        "Determinism: the run is exact rational arithmetic end to end -- no RNG, no optimizer, no "
        "root-finding, no grid scan, and no floating-point tolerance anywhere -- evaluated over a "
        "fixed insertion-ordered dictionary of six named carriers, so every equality is decided "
        "exactly and no value in this certificate is interpolated from a converged quantity."
    )


def main() -> int:
    print("S3-time Route-2 E-center consumer ambiguity firewall")
    print("=" * 72)

    part1_note_and_authority_boundary()
    part2_exact_readout_support_formula()
    part3_exact_consumer_factorization()
    part4_blind_and_sensitive_sectors()
    part5_n5_execution_certificate()

    print("\n" + "=" * 72)
    print("SUMMARY")
    print("=" * 72)
    print("Status: exact-support consumer firewall; endpoint rho_E remains open.")
    print(f"PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
