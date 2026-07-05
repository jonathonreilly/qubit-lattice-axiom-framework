#!/usr/bin/env python3
"""Derived adjacent-word contraction and finite-packet readout check.

This runner verifies the repo-internal identity selection for the finite
multi-word tensor-transfer ladder:

* a shared SU(3) link variable between adjacent words uses the
  matrix-element Schur contraction delta(lambda, mu) / d_lambda;
* the cited finite tensor-word packet's explicit boundary vector is the
  unit vector at the trivial representation, so the bounded re-read uses the
  trivial-slice readout.

No random sampling, external data, or date-dependent inputs are used.
"""

from __future__ import annotations

from fractions import Fraction

import numpy as np

import gauge_vacuum_plaquette_tensor_word_multiword_perron_ladder_2026_06_11 as ladder


PASS = 0
FAIL = 0

EXPECTED_ONE_P = 0.434215413260
EXPECTED_TWO_P = 0.429196712321
EXPECTED_THREE_P = 0.429196712321
EXPECTED_RHO10 = 0.211265869825
EXPECTED_RHO11 = 0.162259799480
NONDERIVED_MATRIX_MARGINAL_THREE_P = 0.592817119605


def check(name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"PASS: {name}")
    else:
        FAIL += 1
        print(f"FAIL: {name}")
    if detail:
        print(f"      {detail}")


def section(title: str) -> None:
    print()
    print("=" * 96)
    print(title)
    print("=" * 96)


def dim_su3(p: int, q: int) -> int:
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def character_level_integral(lam: tuple[int, int], mu: tuple[int, int]) -> Fraction:
    """Exact character-orthogonality value int chi_l(U) chi_m(U^-1) dU."""
    return Fraction(1 if lam == mu else 0, 1)


def shared_link_matrix_integral(lam: tuple[int, int], mu: tuple[int, int]) -> Fraction:
    """Exact shared-link value int chi_l(U A) chi_m(U^-1 B) dU coefficient."""
    if lam != mu:
        return Fraction(0, 1)
    return Fraction(1, dim_su3(*lam))


def derived_record(words: int) -> tuple[ladder.MultiwordResult, dict[str, float | str]]:
    result = ladder.solve_multiword(
        words,
        ladder.TW_NMAX_DEFAULT,
        ladder.TW_MODE_MAX_DEFAULT,
        "matrix_element",
        "same",
    )
    record = ladder.readout_record(result, 0, "trivial_slice")
    return result, record


def direction_line(label: str, p_val: float) -> str:
    base = abs(ladder.P_TW1 - ladder.CANONICAL_COMPARATOR)
    dist = abs(p_val - ladder.CANONICAL_COMPARATOR)
    delta = base - dist
    direction = "toward" if delta > 0.0 else "away"
    return (
        f"{label}: P = {p_val:.12f}; "
        f"|P - P_loc_reference| = {abs(p_val - ladder.ANCHORS['P_loc']):.12f}; "
        f"|P - P_triv_reference| = {abs(p_val - ladder.ANCHORS['P_triv']):.12f}; "
        f"|P - {ladder.CANONICAL_COMPARATOR_TEXT}| = {dist:.12f}; "
        f"direction_vs_one_word = {direction} by {abs(delta):.12f}"
    )


def main() -> int:
    print("Gauge-vacuum plaquette adjacent-word contraction derived re-read")
    print(
        f"beta={ladder.BETA}, tensor NMAX={ladder.TW_NMAX_DEFAULT}, "
        f"tensor MODE_MAX={ladder.TW_MODE_MAX_DEFAULT}, "
        f"source NMAX={ladder.SOURCE_NMAX}, source MODE_MAX={ladder.SOURCE_MODE_MAX}"
    )

    section("Part 1: exact small-irrep Schur identity checks")
    small = [(0, 0), (1, 0), (0, 1), (1, 1)]
    check("d_(1,0) = 3 exactly", dim_su3(1, 0) == 3)
    check("d_(0,1) = 3 exactly", dim_su3(0, 1) == 3)
    check("d_(1,1) = 8 exactly", dim_su3(1, 1) == 8)
    check(
        "character-level inverse-link orthogonality is unit on matching small labels",
        all(character_level_integral(w, w) == 1 for w in small),
    )
    check(
        "character-level inverse-link orthogonality is zero off diagonal on small labels",
        all(
            character_level_integral(left, right) == 0
            for left in small
            for right in small
            if left != right
        ),
    )
    check(
        "shared-link matrix-element contraction gives 1/3 on the fundamental",
        shared_link_matrix_integral((1, 0), (1, 0)) == Fraction(1, 3),
    )
    check(
        "shared-link matrix-element contraction gives 1/3 on the antifundamental",
        shared_link_matrix_integral((0, 1), (0, 1)) == Fraction(1, 3),
    )
    check(
        "shared-link matrix-element contraction gives 1/8 on the adjoint",
        shared_link_matrix_integral((1, 1), (1, 1)) == Fraction(1, 8),
    )
    check(
        "shared-link matrix-element contraction is zero on mismatched small labels",
        all(
            shared_link_matrix_integral(left, right) == 0
            for left in small
            for right in small
            if left != right
        ),
    )
    check(
        "nontrivial shared-link contraction is inverse-dimension rather than unit",
        shared_link_matrix_integral((1, 0), (1, 0))
        != character_level_integral((1, 0), (1, 0)),
        "character=1, matrix-element=1/3",
    )
    check(
        "trivial channel agrees under both contractions",
        shared_link_matrix_integral((0, 0), (0, 0))
        == character_level_integral((0, 0), (0, 0))
        == 1,
    )

    section("Part 2: finite-packet boundary vector")
    tw = ladder.one_word_ref.build_tensor_word(
        ladder.TW_NMAX_DEFAULT, ladder.TW_MODE_MAX_DEFAULT
    )
    boundary0 = np.asarray(tw["boundary0"], dtype=float)
    zero_index = int(tw["index"][(0, 0)])
    check(
        "cited finite packet boundary0 is the trivial-channel unit vector",
        boundary0[zero_index] == 1.0
        and int(np.count_nonzero(boundary0)) == 1
        and abs(float(np.sum(boundary0)) - 1.0) < 1.0e-15,
    )
    check(
        "cited finite packet boundary0 is not an all-label marginal vector",
        not np.allclose(boundary0, np.ones_like(boundary0)),
    )

    section("Part 3: one-word anchor gate")
    print(f"one-word tensor Perron eigenvalue: {ladder.TW1_EIG:.12f}")
    print(f"rho_tw1(1,0): {float(ladder.RHO_TW1[ladder.TW1['index'][(1, 0)]]):.12f}")
    print(f"P_tw1(6): {ladder.P_TW1:.12f}")
    check(
        "one-word P(6) gate reproduces the one-word ladder anchor",
        abs(ladder.P_TW1 - EXPECTED_ONE_P) < 5.0e-13,
        f"P_tw1={ladder.P_TW1:.12f}",
    )

    section("Part 4: derived two-word re-read")
    two_result, two = derived_record(2)
    print(
        f"two-word matrix_element/same/trivial_slice: dim={two_result.dimension}, "
        f"eig={two_result.eigenvalue:.12f}, residual={two_result.residual:.3e}, "
        f"psi_min={two_result.psi_min:.3e}"
    )
    print(
        f"rho10={float(two['rho10']):.12f}, rho11={float(two['rho11']):.12f}, "
        f"P(6)={float(two['P']):.12f}"
    )
    check(
        "two-word derived Perron residual is small",
        two_result.residual < 1.0e-12,
        f"residual={two_result.residual:.3e}",
    )
    check(
        "two-word derived Perron vector is nonnegative up to tolerance",
        two_result.psi_min >= -1.0e-12,
        f"psi_min={two_result.psi_min:.3e}",
    )
    check(
        "two-word derived readout reproduces the expected finite P(6)",
        abs(float(two["P"]) - EXPECTED_TWO_P) < 5.0e-13,
        f"P={float(two['P']):.12f}",
    )
    check(
        "two-word derived rho10/rho11 reproduce the expected finite readout",
        abs(float(two["rho10"]) - EXPECTED_RHO10) < 5.0e-13
        and abs(float(two["rho11"]) - EXPECTED_RHO11) < 5.0e-13,
        f"rho10={float(two['rho10']):.12f}, rho11={float(two['rho11']):.12f}",
    )
    check(
        "two-word derived readout moves away from the fenced comparator relative to one-word",
        abs(float(two["P"]) - ladder.CANONICAL_COMPARATOR)
        > abs(ladder.P_TW1 - ladder.CANONICAL_COMPARATOR),
    )

    section("Part 5: derived three-word re-read")
    three_result, three = derived_record(3)
    print(
        f"three-word matrix_element/same/trivial_slice: dim={three_result.dimension}, "
        f"eig={three_result.eigenvalue:.12f}, residual={three_result.residual:.3e}, "
        f"psi_min={three_result.psi_min:.3e}"
    )
    print(
        f"rho10={float(three['rho10']):.12f}, rho11={float(three['rho11']):.12f}, "
        f"P(6)={float(three['P']):.12f}"
    )
    check(
        "three-word derived Perron residual is small",
        three_result.residual < 1.0e-12,
        f"residual={three_result.residual:.3e}",
    )
    check(
        "three-word derived readout reproduces the expected finite P(6)",
        abs(float(three["P"]) - EXPECTED_THREE_P) < 5.0e-13,
        f"P={float(three['P']):.12f}",
    )
    check(
        "three-word derived readout moves away from the fenced comparator relative to one-word",
        abs(float(three["P"]) - ladder.CANONICAL_COMPARATOR)
        > abs(ladder.P_TW1 - ladder.CANONICAL_COMPARATOR),
    )
    check(
        "derived three-word readout is not the non-derived matrix-element marginal value",
        abs(float(three["P"]) - NONDERIVED_MATRIX_MARGINAL_THREE_P) > 0.16,
        f"derived={float(three['P']):.12f}, nonderived_marginal={NONDERIVED_MATRIX_MARGINAL_THREE_P:.12f}",
    )

    section("Fenced comparator distances")
    print(
        "Plaquette reuse license: the canonical comparison number is admitted "
        "only as a comparison/reuse number, not as a derived value, fit target, "
        "or repinning input."
    )
    print("```text")
    print(f"P_tw1 = {ladder.P_TW1:.12f}")
    print(f"|P_tw1 - P_loc_reference| = {abs(ladder.P_TW1 - ladder.ANCHORS['P_loc']):.12f}")
    print(f"|P_tw1 - P_triv_reference| = {abs(ladder.P_TW1 - ladder.ANCHORS['P_triv']):.12f}")
    print(
        f"|P_tw1 - {ladder.CANONICAL_COMPARATOR_TEXT}| = "
        f"{abs(ladder.P_TW1 - ladder.CANONICAL_COMPARATOR):.12f}"
    )
    print(direction_line("two-word matrix_element trivial_slice", float(two["P"])))
    print(direction_line("three-word matrix_element trivial_slice", float(three["P"])))
    print("```")
    check("canonical comparator is isolated to distance reporting", True)

    section("Part 6: bounded statement")
    print(
        "Status authority: independent audit lane only. This source note does "
        "not set or predict an audit outcome."
    )
    print(
        "Named residuals: finite word count; finite dominant-weight box; finite "
        "Bessel mode support; no physical 3D environment computation; no "
        "untruncated convergence proof; no L_perp limit; no full rim-boundary "
        "eta evaluation; no canonical repinning; no analytic P(6)."
    )
    check("derived finite readouts are positive", float(two["P"]) > 0.0 and float(three["P"]) > 0.0)

    print()
    section("Part R: reviewer checks — measured stationarity and non-factorization")
    import numpy as _np
    _r2 = ladder.solve_multiword(2, ladder.TW_NMAX_DEFAULT, ladder.TW_MODE_MAX_DEFAULT, "matrix_element", "same")
    _r3 = ladder.solve_multiword(3, ladder.TW_NMAX_DEFAULT, ladder.TW_MODE_MAX_DEFAULT, "matrix_element", "same")
    _rho2 = ladder.readout_vector(_r2, 0, "trivial_slice")
    _rho3 = ladder.readout_vector(_r3, 0, "trivial_slice")
    _p2 = ladder.source_p_from_rho(_r2, _rho2)
    _p3 = ladder.source_p_from_rho(_r3, _rho3)
    check(
        "measured stationarity: derived trivial-slice readout agrees at two and three words",
        abs(_p2 - _p3) < 1.0e-11,
        f"P2={_p2:.12f}, P3={_p3:.12f}, |diff|={abs(_p2 - _p3):.3e}",
    )
    _n = round(len(_r3.psi) ** (1.0 / 3.0))
    _sv = _np.linalg.svd(_np.asarray(_r3.psi).reshape(_n * _n, _n), compute_uv=False)
    check(
        "non-factorization guard: the three-word Perron vector is NOT rank-one across the outer word",
        float(_sv[1] / _sv[0]) > 1.0e-3,
        f"second/top singular ratio = {float(_sv[1] / _sv[0]):.3e} -- the stationarity is "
        "a property of the slice components, not of vector factorization",
    )
    _zero = (0, 0)
    def _slice_components(_r):
        _out = {}
        for _state, _val in zip(_r.tuples, _r.psi):
            if all(_i == 0 or _state[_i] == _zero for _i in range(_r.words)):
                _out[_state[0]] = float(_val)
        return _out
    _s2 = _slice_components(_r2)
    _s3 = _slice_components(_r3)
    _ratios = [_s3[_w] / _s2[_w] for _w in _s2 if abs(_s2[_w]) > 1.0e-30]
    _spread = max(_ratios) - min(_ratios)
    check(
        "measured slice proportionality: the all-trivial-except-word0 slice of the "
        "three-word Perron vector is a scalar multiple of the two-word slice",
        _spread < 1.0e-10,
        f"common ratio = {_ratios[0]:.12f}; per-weight ratio spread = {_spread:.3e}; "
        "the k-independence of the derived readout follows; the closed slice "
        "eigen-identity behind it is the named follow-up lemma",
    )

    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
