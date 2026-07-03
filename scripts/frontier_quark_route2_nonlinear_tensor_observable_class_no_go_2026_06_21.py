#!/usr/bin/env python3
"""
Route-2 nonlinear tensor-observable class no-go.

Safe claim:
  In the reduced Route-2 readout family

      P(rho_E) = [[1, 0, rho_E, 0],
                  [0,-2, 0,     2]],

  every finite tensor-polynomial observable generated only from the
  E-center-blind endpoint carrier columns

      E-shell, T-shell, T-center

  and scalar contractions of their readout images is invariant under changing
  rho_E.  Nonlinearity by itself therefore cannot select rho_E = 21/4 unless
  the observable supplies a new generator that evaluates the missing
  E-center direction, or an equivalent source/readout primitive.

  This does not prove an impossibility theorem for arbitrary future nonlinear
  observables.  It prunes the E-center-blind finite tensor-polynomial class
  and sharpens the positive target: a successful nonlinear Route-2 repair must
  include a nonblind E-center lift.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from itertools import combinations_with_replacement, product
from pathlib import Path


PASS_COUNT = 0
FAIL_COUNT = 0

Vector4 = tuple[Fraction, Fraction, Fraction, Fraction]
Vector2 = tuple[Fraction, Fraction]


E_SHELL: Vector4 = (Fraction(1), Fraction(0), Fraction(0), Fraction(0))
E_CENTER: Vector4 = (Fraction(1), Fraction(0), Fraction(1, 6), Fraction(0))
T_SHELL: Vector4 = (Fraction(0), Fraction(1), Fraction(0), Fraction(0))
T_CENTER: Vector4 = (Fraction(0), Fraction(1), Fraction(0), Fraction(1, 6))

BLIND_COLUMNS: tuple[tuple[str, Vector4], ...] = (
    ("E-shell", E_SHELL),
    ("T-shell", T_SHELL),
    ("T-center", T_CENTER),
)
ALL_COLUMNS: tuple[tuple[str, Vector4], ...] = (
    ("E-shell", E_SHELL),
    ("E-center", E_CENTER),
    ("T-shell", T_SHELL),
    ("T-center", T_CENTER),
)


@dataclass(frozen=True)
class ReducedReadout:
    rho_e: Fraction
    alpha_e: Fraction = Fraction(1)
    alpha_t: Fraction = Fraction(-2)
    beta_t: Fraction = Fraction(2)

    @property
    def beta_e(self) -> Fraction:
        return self.rho_e * self.alpha_e

    def apply(self, v: Vector4) -> Vector2:
        x_e, x_t, d_e, d_t = v
        return (
            self.alpha_e * x_e + self.beta_e * d_e,
            self.alpha_t * x_t + self.beta_t * d_t,
        )

    def affine_image_coefficients(
        self, v: Vector4
    ) -> tuple[tuple[Fraction, Fraction], tuple[Fraction, Fraction]]:
        """Return ((E constant, E rho coeff), (T constant, T rho coeff))."""
        x_e, x_t, d_e, d_t = v
        return ((self.alpha_e * x_e, d_e), (self.alpha_t * x_t + self.beta_t * d_t, Fraction(0)))

    @property
    def q_e(self) -> Fraction:
        return self.apply(E_CENTER)[0] / self.apply(E_SHELL)[0]

    @property
    def q_t(self) -> Fraction:
        return self.apply(T_CENTER)[1] / self.apply(T_SHELL)[1]

    @property
    def shell_te(self) -> Fraction:
        return self.apply(T_SHELL)[1] / self.apply(E_SHELL)[0]

    @property
    def center_te(self) -> Fraction:
        return self.apply(T_CENTER)[1] / self.apply(E_CENTER)[0]


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


def section(title: str) -> None:
    print("\n" + "=" * 78)
    print(title)
    print("=" * 78)


def rank(vectors: list[Vector4]) -> int:
    matrix = [list(v) for v in vectors if any(v)]
    if not matrix:
        return 0

    rows = len(matrix)
    cols = len(matrix[0])
    pivot_row = 0
    rank_count = 0

    for col in range(cols):
        pivot = None
        for row in range(pivot_row, rows):
            if matrix[row][col] != 0:
                pivot = row
                break
        if pivot is None:
            continue

        matrix[pivot_row], matrix[pivot] = matrix[pivot], matrix[pivot_row]
        pivot_val = matrix[pivot_row][col]
        matrix[pivot_row] = [x / pivot_val for x in matrix[pivot_row]]

        for row in range(rows):
            if row == pivot_row:
                continue
            factor = matrix[row][col]
            if factor:
                matrix[row] = [
                    matrix[row][i] - factor * matrix[pivot_row][i]
                    for i in range(cols)
                ]

        rank_count += 1
        pivot_row += 1
        if pivot_row == rows:
            break

    return rank_count


def in_span(v: Vector4, basis: list[Vector4]) -> bool:
    return rank(basis + [v]) == rank(basis)


def dot(a: Vector2, b: Vector2) -> Fraction:
    return a[0] * b[0] + a[1] * b[1]


def det2(a: Vector2, b: Vector2) -> Fraction:
    return a[0] * b[1] - a[1] * b[0]


def tensor_word(vectors: tuple[Vector2, ...]) -> tuple[Fraction, ...]:
    out: list[Fraction] = []
    for idxs in product((0, 1), repeat=len(vectors)):
        val = Fraction(1)
        for vec, idx in zip(vectors, idxs):
            val *= vec[idx]
        out.append(val)
    return tuple(out)


def blind_tensor_signature(readout: ReducedReadout) -> tuple[object, ...]:
    images = tuple((name, readout.apply(col)) for name, col in BLIND_COLUMNS)
    image_by_name = dict(images)

    scalar_contractions = tuple(
        (
            a,
            b,
            dot(image_by_name[a], image_by_name[b]),
            det2(image_by_name[a], image_by_name[b]),
        )
        for a, b in combinations_with_replacement(image_by_name, 2)
    )

    pure_powers = tuple(
        (degree, name, tensor_word((image,) * degree))
        for degree in range(1, 6)
        for name, image in images
    )

    mixed_words = []
    labels = [name for name, _ in BLIND_COLUMNS]
    for degree in range(2, 5):
        for word in product(labels, repeat=degree):
            mixed_words.append(
                (degree, word, tensor_word(tuple(image_by_name[name] for name in word)))
            )

    return (images, scalar_contractions, pure_powers, tuple(mixed_words))


def spacetime_prefactor_signature(readout: ReducedReadout, v_time: tuple[Fraction, ...]) -> tuple[object, ...]:
    """Exact outer-product signatures using a fixed universal time vector."""
    rows = []
    for name, col in BLIND_COLUMNS:
        left = readout.apply(col)
        outer = tuple(component * time for component in left for time in v_time)
        rows.append((name, outer, tensor_word((left, left))))
    return tuple(rows)


def polynomial_probes(readout: ReducedReadout) -> tuple[Fraction, ...]:
    e_shell = readout.apply(E_SHELL)
    t_shell = readout.apply(T_SHELL)
    t_center = readout.apply(T_CENTER)
    features = (e_shell, t_shell, t_center)
    return (
        dot(e_shell, e_shell) + dot(t_shell, t_shell),
        dot(t_center, t_center) - dot(t_shell, t_center),
        det2(e_shell, t_shell) ** 2 + det2(e_shell, t_center) ** 2,
        sum(tensor_word((e_shell, t_shell, t_center))),
        sum(tensor_word((t_center,) * 4)) - sum(tensor_word((t_shell,) * 2)),
        sum(dot(a, b) ** 3 for a, b in combinations_with_replacement(features, 2)),
    )


def solve_rho_for_q_e(target_q_e: Fraction) -> Fraction:
    # q_E = 1 + rho_E/6.
    return Fraction(6) * (target_q_e - Fraction(1))


def read_text(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


def part1_generator_geometry() -> None:
    section("PART 1: Reduced carrier geometry and rho_E coefficient scan")

    blind_basis = [col for _, col in BLIND_COLUMNS]
    full_basis = [col for _, col in ALL_COLUMNS]
    e_center_direction: Vector4 = tuple(E_CENTER[i] - E_SHELL[i] for i in range(4))  # type: ignore[assignment]

    print(f"  E-shell  = {E_SHELL}")
    print(f"  E-center = {E_CENTER}")
    print(f"  T-shell  = {T_SHELL}")
    print(f"  T-center = {T_CENTER}")
    print(f"  missing direction = E-center - E-shell = {e_center_direction}")

    check("Full endpoint carrier rank is 4", rank(full_basis) == 4, f"rank={rank(full_basis)}")
    check("E-center-blind carrier rank is 3", rank(blind_basis) == 3, f"rank={rank(blind_basis)}")
    check(
        "E-center direction is not in the blind carrier span",
        not in_span(e_center_direction, blind_basis),
        "adding E-center raises the rank",
    )

    probe = ReducedReadout(Fraction(0))
    blind_coeffs = {
        name: probe.affine_image_coefficients(col)
        for name, col in BLIND_COLUMNS
    }
    e_center_coeff = probe.affine_image_coefficients(E_CENTER)
    print("  blind generator affine coefficients:")
    for name, coeff in blind_coeffs.items():
        print(f"    {name}: {coeff}")
    print(f"    E-center: {e_center_coeff}")

    check(
        "Every blind generator has zero rho_E coefficient in both readout channels",
        all(coeff == ((coeff[0][0], Fraction(0)), (coeff[1][0], Fraction(0))) for coeff in blind_coeffs.values()),
    )
    check(
        "The E-center generator has the unique nonzero rho_E coefficient 1/6",
        e_center_coeff == ((Fraction(1), Fraction(1, 6)), (Fraction(0), Fraction(0))),
        f"E-center affine coefficients={e_center_coeff}",
    )


def part2_nonlinear_invariance() -> None:
    section("PART 2: Finite tensor-polynomial invariance on the blind class")

    rhos = (Fraction(-7, 3), Fraction(-1), Fraction(0), Fraction(1), Fraction(21, 4), Fraction(13, 2))
    reference = blind_tensor_signature(ReducedReadout(rhos[0]))
    signatures = []
    for rho in rhos:
        readout = ReducedReadout(rho)
        signature = blind_tensor_signature(readout)
        signatures.append(signature)
        print(
            f"  rho_E={str(rho):>5}: "
            f"E-shell={readout.apply(E_SHELL)}, "
            f"T-shell={readout.apply(T_SHELL)}, "
            f"T-center={readout.apply(T_CENTER)}, "
            f"E-center={readout.apply(E_CENTER)}"
        )
        check(
            f"rho_E={rho} has the same blind tensor-generator signature",
            signature == reference,
        )

    check(
        "All tested rho_E values have one identical blind tensor-polynomial generator tuple",
        len(set(signatures)) == 1,
        f"tested {len(rhos)} exact rho_E values",
    )

    e_center_values = tuple(ReducedReadout(rho).apply(E_CENTER)[0] for rho in rhos)
    check(
        "The E-center readout varies across the same rho_E values",
        len(set(e_center_values)) == len(e_center_values),
        f"E-center values={e_center_values}",
    )

    probe_values = tuple(polynomial_probes(ReducedReadout(rho)) for rho in rhos)
    check(
        "Representative nonlinear polynomial probes are invariant on the blind class",
        len(set(probe_values)) == 1,
        f"probe tuple={probe_values[0]}",
    )


def part3_tensor_powers_and_time_factor() -> None:
    section("PART 3: Tensor powers and Route-2 time-factor separation")

    rhos = (Fraction(-1), Fraction(0), Fraction(1), Fraction(21, 4))
    for degree in range(1, 7):
        powers = []
        for rho in rhos:
            readout = ReducedReadout(rho)
            degree_signature = tuple(
                (name, tensor_word((readout.apply(col),) * degree))
                for name, col in BLIND_COLUMNS
            )
            powers.append(degree_signature)
        check(
            f"Symmetric tensor powers degree {degree} of blind readout images are rho_E-invariant",
            len(set(powers)) == 1,
        )

    v_time = (Fraction(1), Fraction(2, 3), Fraction(5, 7), Fraction(11, 13))
    blind_spacetime = tuple(
        spacetime_prefactor_signature(ReducedReadout(rho), v_time)
        for rho in rhos
    )
    check(
        "Outer-product spacetime signatures with a universal time vector are invariant for blind columns",
        len(set(blind_spacetime)) == 1,
        "readout ambiguity is not in the right/time factor",
    )

    e_center_spacetime = []
    for rho in rhos:
        left = ReducedReadout(rho).apply(E_CENTER)
        e_center_spacetime.append(tuple(component * time for component in left for time in v_time))
    check(
        "The same spacetime construction varies as soon as E-center is evaluated",
        len(set(e_center_spacetime)) == len(e_center_spacetime),
    )


def part4_target_equivalence_and_firewall() -> None:
    section("PART 4: Target equivalence and nonblind primitive firewall")

    target_rho = Fraction(21, 4)
    target = ReducedReadout(target_rho)
    solved = solve_rho_for_q_e(Fraction(15, 8))
    print(f"  target rho_E = {target_rho}")
    print(f"  target q_E   = {target.q_e}")
    print(f"  target c_TE  = {target.center_te}")

    check(
        "rho_E=21/4 is exactly equivalent to q_E=15/8",
        target.q_e == Fraction(15, 8) and solved == target_rho,
        f"solved rho={solved}",
    )
    check(
        "rho_E=21/4 is exactly equivalent to center T/E=-8/9 under the granted T-side data",
        target.center_te == Fraction(-8, 9),
        f"center T/E={target.center_te}",
    )
    check(
        "A nonblind E-center selector can force the target only by supplying the missing generator",
        ReducedReadout(target_rho).apply(E_CENTER)[0] == Fraction(15, 8)
        and ReducedReadout(Fraction(0)).apply(E_CENTER)[0] != Fraction(15, 8),
        "this is the open E-center lift, not a blind nonlinear closure",
    )
    check(
        "T-side endpoint data remain fixed while rho_E changes",
        all(
            (ReducedReadout(rho).q_t, ReducedReadout(rho).shell_te)
            == (Fraction(5, 6), Fraction(-2))
            for rho in (Fraction(-2), Fraction(0), Fraction(21, 4), Fraction(8))
        ),
    )


def part5_parent_surface_anchors() -> None:
    section("PART 5: Parent-surface anchors and scope guards")

    theta_note = read_text("docs/S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md")
    exact_readout_note = read_text("docs/QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md")
    blindness_note = read_text("docs/QUARK_ROUTE2_E_CENTER_BLINDNESS_NO_GO_NOTE_2026-06-17.md")
    schur_note = read_text("docs/QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md")
    factor_note = read_text("docs/S3_TIME_THETA_TO_SLICE_COUPLING_FACTOR_RIGIDITY_NOTE_2026-05-17.md")

    check(
        "Parent theta-to-slice note names the readout-map endpoint triple as the open theorem target",
        "readout-map endpoint triple" in theta_note and "not yet derived" in theta_note,
    )
    check(
        "Exact readout note exposes rho_E as the irreducible missing map entry",
        "beta_E / alpha_E = 21/4" in exact_readout_note
        and "irreducible missing map entry" in exact_readout_note,
    )
    check(
        "E-center blindness note requires a genuine E-center lift or equivalent primitive",
        "A positive repair" in blindness_note
        and "must supply a genuine E-center lift" in blindness_note
        and "equivalent\nreadout primitive" in blindness_note,
    )
    check(
        "Quadratic Schur note leaves future nonlinear observables explicitly open",
        "does **not** prove impossibility over arbitrary" in schur_note
        and "future nonlinear observables" in schur_note,
    )
    check(
        "Factor-rigidity note localizes ambiguity in the spatial readout prefactor",
        "structurally localized in the spatial prefactor" in factor_note,
    )


def main() -> int:
    print("=" * 78)
    print("FRONTIER: Quark Route-2 nonlinear tensor-observable class no-go")
    print("=" * 78)

    part1_generator_geometry()
    part2_nonlinear_invariance()
    part3_tensor_powers_and_time_factor()
    part4_target_equivalence_and_firewall()
    part5_parent_surface_anchors()

    print("\n" + "=" * 78)
    print(f"TOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    print("=" * 78)
    print(
        "\nVERDICT: exact negative boundary / no-go for finite E-center-blind "
        "tensor-polynomial Route-2 observables. Nonlinearity does not by itself "
        "select rho_E=21/4; any successful nonlinear repair must introduce a "
        "nonblind E-center lift, source-domain rule, or equivalent readout "
        "primitive. This does not rule out arbitrary future nonlinear observables."
    )
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
