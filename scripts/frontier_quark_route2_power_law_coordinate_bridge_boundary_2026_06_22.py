#!/usr/bin/env python3
"""Verify the Route-2 power-law coordinate bridge boundary."""

from __future__ import annotations

from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

NOTE = ROOT / "docs/QUARK_ROUTE2_POWER_LAW_COORDINATE_BRIDGE_BOUNDARY_NOTE_2026-06-22.md"
BLOCK103 = ROOT / "docs/QUARK_ROUTE2_HESSIAN_COORDINATE_WARP_NO_GO_NOTE_2026-06-22.md"
BLOCK102 = ROOT / "docs/QUARK_ROUTE2_RAY_QUOTIENT_HESSIAN_NO_SCALE_BOUNDARY_NOTE_2026-06-22.md"
BLOCK101 = ROOT / "docs/QUARK_ROUTE2_HESSIAN_COUNTERTERM_EXCLUSION_BOUNDARY_NOTE_2026-06-22.md"
BLOCK99 = ROOT / "docs/QUARK_ROUTE2_TYPED_METRIC_SOURCE_INVERSE_SQUARE_BOUNDARY_NOTE_2026-06-22.md"
S3 = ROOT / "docs/S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md"
MINIMAL = ROOT / "docs/MINIMAL_AXIOMS_2026-06-05.md"

passes = 0
fails = 0


def compact(text: str) -> str:
    return " ".join(text.split())


def check(condition: bool, label: str, detail: str = "") -> None:
    global passes, fails
    if condition:
        passes += 1
        suffix = f" -- {detail}" if detail else ""
        print(f"PASS: {label}{suffix}")
    else:
        fails += 1
        suffix = f" -- {detail}" if detail else ""
        print(f"FAIL: {label}{suffix}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def power_log_derivative(a: Fraction, w: Fraction) -> Fraction:
    return a / w


def pulled_hessian_power(c: Fraction, a: Fraction, w: Fraction) -> Fraction:
    return c * power_log_derivative(a, w) ** 2


def power_ratio(a: Fraction) -> Fraction:
    w_e = Fraction(1, 3)
    w_t = Fraction(1, 2)
    return pulled_hessian_power(Fraction(1), a, w_e) / pulled_hessian_power(Fraction(1), a, w_t)


def warp_log_elasticity(b: Fraction, w: Fraction) -> Fraction:
    # y_b = w exp(bw), so d log y / d log w = w * (1/w + b).
    return 1 + b * w


def warp_ratio(b: Fraction) -> Fraction:
    return ((Fraction(3) + b) / (Fraction(2) + b)) ** 2


def main() -> int:
    print("Route-2 power-law coordinate bridge boundary")
    print("=" * 78)

    print("\nA. Source-note and authority boundary")
    note = read(NOTE)
    note_c = compact(note)
    check(NOTE.exists(), "new source note exists", str(NOTE.relative_to(ROOT)))
    check("Actual current-surface status:** exact-support" in note, "new note declares exact-support/open boundary")
    check("y = K w^a" in note and "multiplicatively homogeneous" in note, "new note states the power-law coordinate bridge")
    check(
        "proposed_retained" not in note_c
        and "would become retained" not in note_c
        and "retained branch-local" not in note_c,
        "new note has no retained proposal wording",
    )

    authorities = [
        (BLOCK103, ["y_b", "positive monotone", "misses the endpoint"]),
        (BLOCK102, ["ray-quotient Hessian two-form", "epsilon=0"]),
        (BLOCK101, ["H_epsilon(w) = C/w^2 + epsilon", "The current surface does not exclude `epsilon > 0`"]),
        (BLOCK99, ["q_X w_X^2 = 5/24", "21/4"]),
        (S3, ["the underlying readout-map endpoint triple is not yet derived"]),
        (MINIMAL, ["Record", "supplies no readout context"]),
    ]
    for path, markers in authorities:
        text = compact(read(path))
        missing = [marker for marker in markers if marker not in text]
        check(not missing, f"{path.name} contains required boundary markers", "; ".join(markers))

    print("\nB. Exact power-law pullback theorem")
    samples = [Fraction(1), Fraction(2), Fraction(3, 2), Fraction(-1), Fraction(-2)]
    check(all(power_log_derivative(a, Fraction(1, 3)) == 3 * a for a in samples), "E-channel log derivative is a/w_E")
    check(all(power_log_derivative(a, Fraction(1, 2)) == 2 * a for a in samples), "T-channel log derivative is a/w_T")
    check(all(power_ratio(a) == Fraction(9, 4) for a in samples if a != 0), "all sampled nonzero power laws give ratio 9/4")
    check(power_ratio(Fraction(1)) == Fraction(9, 4), "identity coordinate is included", "a=1")
    check(power_ratio(Fraction(2)) == Fraction(9, 4), "quadratic coordinate is still sufficient", "a=2")
    check(power_ratio(Fraction(-1)) == Fraction(9, 4), "inverse coordinate is still sufficient as a local positive coordinate", "a=-1")
    check(
        pulled_hessian_power(Fraction(5, 24), Fraction(3), Fraction(1, 3))
        * Fraction(1, 3) ** 2
        == Fraction(5, 24) * 9,
        "prefactor changes but inverse-square structure remains",
    )
    check(
        len({power_ratio(a) for a in samples if a != 0}) == 1,
        "channel-uniform prefactor cancels from the E/T ratio",
    )

    print("\nC. Endpoint consequence")
    h_ratio = power_ratio(Fraction(7, 3))
    q_t = Fraction(5, 6)
    q_e = q_t * h_ratio
    rho_e = 6 * (q_e - 1)
    c_te = Fraction(-2) * q_t / q_e
    check(h_ratio == Fraction(9, 4), "power-law coordinate bridge gives H_E/H_T=9/4", f"ratio={h_ratio}")
    check(q_e == Fraction(15, 8), "T-normalized source gives q_E=15/8", f"q_E={q_e}")
    check(rho_e == Fraction(21, 4), "q_E=15/8 gives rho_E=21/4", f"rho_E={rho_e}")
    check(c_te == Fraction(-8, 9), "center ratio is -8/9 under shell ratio -2", f"c_TE={c_te}")
    check(
        (Fraction(-1), Fraction(-2), rho_e) == (Fraction(-1), Fraction(-2), Fraction(21, 4)),
        "endpoint triple follows under supplied power-law bridge premise",
    )

    print("\nD. Boundary against non-power coordinate warps")
    check(warp_log_elasticity(Fraction(0), Fraction(1, 3)) == 1, "unwarped log-elasticity is constant at E")
    check(warp_log_elasticity(Fraction(0), Fraction(1, 2)) == 1, "unwarped log-elasticity is constant at T")
    check(
        warp_log_elasticity(Fraction(1), Fraction(1, 3))
        != warp_log_elasticity(Fraction(1), Fraction(1, 2)),
        "b=1 warp has nonconstant log-elasticity across E/T weights",
    )
    check(warp_ratio(Fraction(1)) == Fraction(16, 9), "b=1 warp misses 9/4", f"R={warp_ratio(Fraction(1))}")
    check(warp_ratio(Fraction(2)) == Fraction(25, 16), "b=2 warp misses 9/4", f"R={warp_ratio(Fraction(2))}")
    check(all(warp_ratio(b) < Fraction(9, 4) for b in [Fraction(1), Fraction(2), Fraction(5)]), "positive non-power warps stay below target ratio")
    check("positive warps miss the endpoint" in note, "note ties back to Block103 no-go")
    check("arbitrary positive coordinates are too broad" in note_c, "note does not overgeneralize positive coordinates")

    print("\nE. Current-surface boundary")
    minimal = read(MINIMAL)
    check("supplies no readout context" in minimal and "weighting" in minimal, "minimal axioms do not supply coordinate homogeneity")
    check("does not derive a homogeneous physical source coordinate" in note, "new note leaves physical bridge open")
    check("not assert that the bridge is current framework content" in note, "note avoids closure rhetoric")
    check("No observed masses, fitted endpoint values" in note, "forbidden observed/fitted imports are excluded")
    check("exact support/open boundary" in note, "honest status boundary is present")
    check("constant log-elasticity" in note, "positive next theorem target is named")

    print("\n" + "=" * 78)
    print(f"TOTAL: PASS={passes}, FAIL={fails}")
    if fails:
        print("STATUS: failure in power-law coordinate bridge boundary verifier.")
        return 1
    print(
        "STATUS: exact-support/open boundary. Any nonzero power-law source "
        "coordinate pulls no-scale Hessian form back to the inverse-square "
        "Route-2 source law, but the current surface does not derive that "
        "homogeneous coordinate bridge."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
