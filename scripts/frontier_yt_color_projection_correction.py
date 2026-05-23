#!/usr/bin/env python3
"""Y_T color-projection matching no-go runner.

Authority note:
    docs/YT_COLOR_PROJECTION_CORRECTION_NOTE.md

The runner checks the repaired claim:

    K_Y(kappa_Y) = F_adj + kappa_Y * F_singlet
                 = 8/9 + kappa_Y/9  at N_c = 3.

The current retained Fierz/projection packet fixes F_adj and F_singlet, but it
does not select kappa_Y = 0. Two completions, kappa_Y=0 and kappa_Y=1, share
the same retained primitive data and produce different Yukawa corrections.
Therefore the historical sqrt(8/9) package value is conditional, not derived.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path
import sys


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "YT_COLOR_PROJECTION_CORRECTION_NOTE.md"
FIERZ = DOCS / "EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md"
RCONN_PROJECTION = DOCS / "RCONN_VERTEX_COLOR_SINGLET_PROJECTION_BOUNDED_NARROW_THEOREM_NOTE_2026-05-17.md"
EW_NO_GO = DOCS / "EW_CURRENT_MATCHING_RULE_OPEN_GATE_NOTE_2026-05-03.md"

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


def f_adj(n_c: int) -> Fraction:
    return Fraction(n_c * n_c - 1, n_c * n_c)


def f_singlet(n_c: int) -> Fraction:
    return Fraction(1, n_c * n_c)


def k_y(n_c: int, kappa_y: Fraction) -> Fraction:
    return f_adj(n_c) + kappa_y * f_singlet(n_c)


@dataclass(frozen=True)
class Completion:
    n_c: int
    kappa_y: Fraction
    color_blind_scale: Fraction

    @property
    def c(self) -> Fraction:
        return f_adj(self.n_c)

    @property
    def s(self) -> Fraction:
        return f_singlet(self.n_c)

    @property
    def scaled_c(self) -> Fraction:
        return self.color_blind_scale * self.c

    @property
    def scaled_s(self) -> Fraction:
        return self.color_blind_scale * self.s

    @property
    def k_unscaled(self) -> Fraction:
        return self.c + self.kappa_y * self.s

    @property
    def k_scaled_normalized(self) -> Fraction:
        return (self.scaled_c + self.kappa_y * self.scaled_s) / self.color_blind_scale

    @property
    def primitive_signature(self) -> tuple[Fraction, Fraction, Fraction, Fraction]:
        return (
            self.c,
            self.s,
            self.scaled_c / self.c,
            self.scaled_s / self.s,
        )


def rho_singlet_identity(n_c: int) -> Fraction:
    # rho_s(I) = (|Tr I|^2 / N_c) / Tr(I^2) = (N_c^2/N_c)/N_c = 1.
    return Fraction(1)


def rho_singlet_traceless() -> Fraction:
    # rho_s(t^A) = 0 because Tr t^A = 0.
    return Fraction(0)


def main() -> int:
    print("=" * 78)
    print("Y_T COLOR-PROJECTION MATCHING NO-GO")
    print("=" * 78)

    note = read(NOTE)
    fierz = read(FIERZ)
    rconn = read(RCONN_PROJECTION)
    ew_no_go = read(EW_NO_GO)

    print("\nPart 0: source and authority anchors")
    check("source note exists", NOTE.exists(), str(NOTE.relative_to(ROOT)))
    check("Fierz authority exists", FIERZ.exists(), str(FIERZ.relative_to(ROOT)))
    check("RCONN projection authority exists", RCONN_PROJECTION.exists(), str(RCONN_PROJECTION.relative_to(ROOT)))
    check("EW matching no-go authority exists", EW_NO_GO.exists(), str(EW_NO_GO.relative_to(ROOT)))
    check("source note is typed no_go", "**Claim type:** no_go" in note)
    check("source note registers this runner", "scripts/frontier_yt_color_projection_correction.py" in note)
    check(
        "Fierz authority exposes the adjoint channel fraction",
        "8/9" in fierz and "adjoint-channel fraction" in fierz,
    )
    check("projection authority classifies identity insertion", "rho_singlet(I_color) = 1" in rconn)
    check("EW no-go carries two-completion logic", "Completion A: kappa_EW = 0" in ew_no_go)

    print("\nPart 1: exact channel fractions")
    for n_c in (2, 3, 4, 5, 10):
        c = f_adj(n_c)
        s = f_singlet(n_c)
        check(f"N_c={n_c}: F_adj + F_singlet = 1", c + s == 1, f"{c} + {s}")
        check(f"N_c={n_c}: F_adj = (N_c^2-1)/N_c^2", c == Fraction(n_c * n_c - 1, n_c * n_c), str(c))
    check("N_c=3 gives F_adj=8/9", f_adj(3) == Fraction(8, 9), str(f_adj(3)))
    check("N_c=3 gives F_singlet=1/9", f_singlet(3) == Fraction(1, 9), str(f_singlet(3)))

    print("\nPart 2: corrected conditional family")
    check("K_Y(0)=8/9", k_y(3, Fraction(0)) == Fraction(8, 9), str(k_y(3, Fraction(0))))
    check("K_Y(1)=1", k_y(3, Fraction(1)) == Fraction(1), str(k_y(3, Fraction(1))))
    check("K_Y(1/2)=17/18", k_y(3, Fraction(1, 2)) == Fraction(17, 18), str(k_y(3, Fraction(1, 2))))
    check(
        "source states corrected K_Y formula",
        "K_Y(kappa_Y) = F_adj + kappa_Y * F_singlet" in note
        and "8/9 + kappa_Y/9" in note,
    )
    check(
        "source avoids stale reversed K_Y formula",
        "1/9 + 8 kappa_Y/9" not in note and "1/9 + kappa_Y * 8/9" not in note,
    )

    print("\nPart 3: two-completion independence witness")
    connected = Completion(n_c=3, kappa_y=Fraction(0), color_blind_scale=Fraction(77, 100))
    full_trace = Completion(n_c=3, kappa_y=Fraction(1), color_blind_scale=Fraction(77, 100))
    half_trace = Completion(n_c=3, kappa_y=Fraction(1, 2), color_blind_scale=Fraction(77, 100))
    check(
        "kappa=0 and kappa=1 share retained primitive signature",
        connected.primitive_signature == full_trace.primitive_signature,
        str(connected.primitive_signature),
    )
    check(
        "kappa=0 and kappa=1 disagree on K_Y",
        connected.k_unscaled != full_trace.k_unscaled,
        f"{connected.k_unscaled} != {full_trace.k_unscaled}",
    )
    for model in (connected, full_trace, half_trace):
        check(
            f"color-blind scaling cancels at kappa={model.kappa_y}",
            model.k_scaled_normalized == model.k_unscaled,
            f"scaled={model.k_scaled_normalized}, unscaled={model.k_unscaled}",
        )

    print("\nPart 4: vertex-projection guardrail")
    check("rho_singlet(I_color)=1", rho_singlet_identity(3) == Fraction(1))
    check("rho_singlet(traceless generator)=0", rho_singlet_traceless() == Fraction(0))
    check(
        "identity insertion would give K_Y=1 if kappa_Y=rho_singlet",
        k_y(3, rho_singlet_identity(3)) == Fraction(1),
        str(k_y(3, rho_singlet_identity(3))),
    )
    check(
        "traceless insertion would give K_Y=8/9 if kappa_Y=rho_singlet",
        k_y(3, rho_singlet_traceless()) == Fraction(8, 9),
        str(k_y(3, rho_singlet_traceless())),
    )

    print("\nPart 5: overclaim guards")
    forbidden = [
        "The framework derives the `sqrt(8/9)` correction",
        "ALL CHECKS PASSED",
        "m_t(pole, 2-loop) within",
        "Z_phi = Sigma_connected / Sigma_total = R_conn",
    ]
    for phrase in forbidden:
        check(f"source avoids overclaim phrase {phrase!r}", phrase not in note)
    required = [
        "not a derived theorem",
        "conditional support only",
        "derive kappa_Y = 0",
    ]
    for phrase in required:
        check(f"source contains boundary phrase {phrase!r}", phrase in note)

    print()
    print("=" * 78)
    print(f"RESULT: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
    print("=" * 78)
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
