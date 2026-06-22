#!/usr/bin/env python3
"""Verify the Route-2 T-side row-shape/shell-scale independence boundary."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

NOTE = ROOT / "docs/QUARK_ROUTE2_T_SIDE_ROW_SHAPE_SHELL_SCALE_INDEPENDENCE_NO_GO_NOTE_2026-06-22.md"
READOUT = ROOT / "docs/QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md"
T_SIDE = ROOT / "docs/QUARK_ROUTE2_T_SIDE_ENDPOINT_THEOREM_ATTEMPT_BOUNDED_NOTE_2026-06-12.md"
S3 = ROOT / "docs/S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md"
DIRECT_E = ROOT / "docs/QUARK_ROUTE2_DIRECT_E_CENTER_SELECTOR_BOUNDARY_NOTE_2026-06-22.md"

E_SHELL = (Fraction(1), Fraction(0), Fraction(0), Fraction(0))
E_CENTER = (Fraction(1), Fraction(0), Fraction(1, 6), Fraction(0))
T_SHELL = (Fraction(0), Fraction(1), Fraction(0), Fraction(0))
T_CENTER = (Fraction(0), Fraction(1), Fraction(0), Fraction(1, 6))

TARGET_RHO_T = Fraction(-1, 1)
TARGET_Q_T = Fraction(5, 6)
TARGET_S_TE = Fraction(-2, 1)

passes = 0
fails = 0


@dataclass(frozen=True)
class TSideRow:
    alpha_e: Fraction
    alpha_t: Fraction
    beta_t: Fraction

    def t_row(self) -> tuple[Fraction, ...]:
        return (Fraction(0), self.alpha_t, Fraction(0), self.beta_t)

    def e_shell_row(self) -> tuple[Fraction, ...]:
        return (self.alpha_e, Fraction(0), Fraction(0), Fraction(0))

    def t_shell(self) -> Fraction:
        return dot(self.t_row(), T_SHELL)

    def t_center(self) -> Fraction:
        return dot(self.t_row(), T_CENTER)

    def e_shell(self) -> Fraction:
        return dot(self.e_shell_row(), E_SHELL)

    def rho_t(self) -> Fraction:
        return self.beta_t / self.alpha_t

    def q_t(self) -> Fraction:
        return self.t_center() / self.t_shell()

    def s_te(self) -> Fraction:
        return self.t_shell() / self.e_shell()

    def scale_t_row(self, lam: Fraction) -> "TSideRow":
        return TSideRow(self.alpha_e, lam * self.alpha_t, lam * self.beta_t)

    def change_beta(self, beta_t: Fraction) -> "TSideRow":
        return TSideRow(self.alpha_e, self.alpha_t, beta_t)

    def change_alpha_e(self, alpha_e: Fraction) -> "TSideRow":
        return TSideRow(alpha_e, self.alpha_t, self.beta_t)


def dot(row: tuple[Fraction, ...], vector: tuple[Fraction, ...]) -> Fraction:
    return sum(a * b for a, b in zip(row, vector))


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


def main() -> int:
    print("Route-2 T-side row-shape/shell-scale independence")
    print("=" * 78)

    print("\nA. Source-note and dependency boundary")
    note = read(NOTE)
    note_c = compact(note)
    check(NOTE.exists(), "new source note exists", str(NOTE.relative_to(ROOT)))
    check("**Actual current-surface status:** no-go" in note, "new note declares scoped no-go status")
    check("**Claim type:** no_go" in note, "new note declares no_go claim type")
    check("row-shape/shell-scale independence" in note, "new note names independence boundary")
    check("beta_T = -alpha_T" in note, "new note states row-shape target")
    check("alpha_T / alpha_E = -2" in note, "new note states shell-scale target")
    check(
        "proposed_retained" not in note_c
        and "would become retained" not in note_c
        and "retained branch-local" not in note_c,
        "new note has no forbidden proposal wording",
    )

    authority_markers = [
        (READOUT, ["beta_T / alpha_T = -1", "alpha_T / alpha_E = -2", "s_TE = -2"]),
        (T_SIDE, ["W1", "W2", "Missing T-row shape selector"]),
        (S3, ["endpoint triple", "not yet derived", "unique exact `Theta_R -> Lambda_R`"]),
        (DIRECT_E, ["T-side candidates are granted", "rho_E = beta_E / alpha_E = 21/4"]),
    ]
    for path, markers in authority_markers:
        text = compact(read(path))
        missing = [marker for marker in markers if marker not in text]
        check(not missing, f"{path.name} contains required markers", "; ".join(markers))

    print("\nB. Exact target row")
    target = TSideRow(Fraction(1), Fraction(-2), Fraction(2))
    check(target.rho_t() == TARGET_RHO_T, "target row gives rho_T=-1")
    check(target.q_t() == TARGET_Q_T, "target row gives q_T=5/6")
    check(target.s_te() == TARGET_S_TE, "target row gives s_TE=-2")
    check(target.t_shell() == Fraction(-2), "target T shell readout is -2")
    check(target.t_center() == Fraction(-5, 3), "target T center readout is -5/3")
    check(target.e_shell() == Fraction(1), "target E shell readout is 1")

    print("\nC. Coordinate independence")
    scaled = target.scale_t_row(Fraction(3, 1))
    check(scaled.rho_t() == TARGET_RHO_T, "T-row scaling preserves rho_T")
    check(scaled.q_t() == TARGET_Q_T, "T-row scaling preserves q_T")
    check(scaled.s_te() == Fraction(-6, 1), "T-row scaling changes s_TE")

    beta_changed = target.change_beta(Fraction(0))
    check(beta_changed.s_te() == TARGET_S_TE, "beta change preserves s_TE")
    check(beta_changed.rho_t() == Fraction(0), "beta change moves rho_T")
    check(beta_changed.q_t() == Fraction(1), "beta change moves q_T")

    e_scaled = target.change_alpha_e(Fraction(2, 1))
    check(e_scaled.rho_t() == TARGET_RHO_T, "E-shell rescaling preserves rho_T")
    check(e_scaled.q_t() == TARGET_Q_T, "E-shell rescaling preserves q_T")
    check(e_scaled.s_te() == Fraction(-1, 1), "E-shell rescaling changes s_TE")

    print("\nD. Same-surface counter-witnesses")
    shape_only_wrong_scale = TSideRow(Fraction(2), Fraction(-2), Fraction(2))
    shape_only_sign_flip = TSideRow(Fraction(1), Fraction(2), Fraction(-2))
    scale_only_flat_shape = TSideRow(Fraction(1), Fraction(-2), Fraction(0))
    scale_only_wrong_shape = TSideRow(Fraction(1), Fraction(-2), Fraction(-2))

    check(shape_only_wrong_scale.rho_t() == TARGET_RHO_T, "shape-only wrong-scale witness keeps rho_T")
    check(shape_only_wrong_scale.q_t() == TARGET_Q_T, "shape-only wrong-scale witness keeps q_T")
    check(shape_only_wrong_scale.s_te() == Fraction(-1, 1), "shape-only wrong-scale witness breaks s_TE")

    check(shape_only_sign_flip.rho_t() == TARGET_RHO_T, "shape-only sign-flip witness keeps rho_T")
    check(shape_only_sign_flip.q_t() == TARGET_Q_T, "shape-only sign-flip witness keeps q_T")
    check(shape_only_sign_flip.s_te() == Fraction(2, 1), "shape-only sign-flip witness breaks s_TE")

    check(scale_only_flat_shape.s_te() == TARGET_S_TE, "scale-only flat-shape witness keeps s_TE")
    check(scale_only_flat_shape.rho_t() == Fraction(0), "scale-only flat-shape witness breaks rho_T")
    check(scale_only_flat_shape.q_t() == Fraction(1), "scale-only flat-shape witness breaks q_T")

    check(scale_only_wrong_shape.s_te() == TARGET_S_TE, "scale-only wrong-shape witness keeps s_TE")
    check(scale_only_wrong_shape.rho_t() == Fraction(1, 1), "scale-only wrong-shape witness breaks rho_T")
    check(scale_only_wrong_shape.q_t() == Fraction(7, 6), "scale-only wrong-shape witness breaks q_T")

    print("\nE. Selector firewall")
    check("two independent selectors" in note, "note records two-selector boundary")
    check("does not derive the other" in note, "note states no automatic cross-derivation")
    check("time factor cancels" in note, "note blocks time-factor selector")
    check("Carrier columns" in note and "do not fix either row ratio" in note, "note blocks carrier-column selector")
    check("The positive route left open" in note, "note records non-circular positive route")
    check("audit verdict" in note.lower() and "does not set" in note.lower(), "note leaves audit authority untouched")

    print("\n" + "=" * 78)
    print(f"TOTAL: PASS={passes}, FAIL={fails}")
    if fails:
        print("STATUS: failure in T-side independence verifier.")
        return 1
    print(
        "STATUS: scoped no-go/exact support. On the restricted Route-2 "
        "readout algebra, rho_T/q_T and s_TE are independent row coordinates; "
        "a theorem for beta_T=-alpha_T does not by itself derive "
        "alpha_T/alpha_E=-2, and the converse also fails."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
