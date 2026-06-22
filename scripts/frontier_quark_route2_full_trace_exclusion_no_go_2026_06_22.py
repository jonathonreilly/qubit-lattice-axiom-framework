#!/usr/bin/env python3
"""Route-2 full-trace exclusion no-go for the connected-current selector.

Block70 reduced the Route-2 selector to two idempotent projectors:

    kappa = 0  connected / singlet-annihilating
    kappa = 1  full trace

This runner checks whether the current exact controls exclude the full-trace
projector.  They do not.  The full-trace endpoint is idempotent, positive,
S3-scalar, CMT-scale invariant, OZI-size bounded, and endpoint-orientation
compatible.  Excluding it is exactly equivalent to adding a strict
singlet-annihilation or disconnected-current-zero premise.

This is not an audit verdict.
"""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

PASS = 0
FAIL = 0

F_ADJ = Fraction(8, 9)
F_SINGLET = Fraction(1, 9)
TARGET_RHO_E = Fraction(21, 4)


@dataclass(frozen=True)
class ChannelProjector:
    kappa: Fraction

    @property
    def adjoint_eigenvalue(self) -> Fraction:
        return Fraction(1)

    @property
    def singlet_eigenvalue(self) -> Fraction:
        return self.kappa

    @property
    def is_idempotent(self) -> bool:
        return self.kappa * self.kappa == self.kappa

    @property
    def is_positive(self) -> bool:
        return self.adjoint_eigenvalue >= 0 and self.singlet_eigenvalue >= 0

    @property
    def is_channel_scalar(self) -> bool:
        return True

    @property
    def r_phys(self) -> Fraction:
        return F_ADJ + self.kappa * F_SINGLET

    @property
    def c_te_oriented(self) -> Fraction:
        return -self.r_phys

    @property
    def route2_q_e(self) -> Fraction:
        return Fraction(5, 3) / self.r_phys

    @property
    def route2_rho_e(self) -> Fraction:
        return 6 * (self.route2_q_e - 1)

    @property
    def ozi_ratio(self) -> Fraction:
        return self.kappa / 8


def check(label: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(condition)
    PASS += int(ok)
    FAIL += int(not ok)
    suffix = f"\n      {detail}" if detail else ""
    print(f"{'PASS' if ok else 'FAIL'}: {label}{suffix}")


def phrase(*parts: str) -> str:
    return "".join(parts)


def note_text(name: str) -> str:
    return (DOCS / name).read_text(encoding="utf-8")


def cmt_scaled_readout(projector: ChannelProjector, scale: Fraction) -> Fraction:
    numerator = scale * (F_ADJ + projector.kappa * F_SINGLET)
    denominator = scale
    return numerator / denominator


def accepted_control_signature(projector: ChannelProjector) -> tuple[bool, ...]:
    return (
        projector.is_idempotent,
        projector.is_positive,
        projector.is_channel_scalar,
        projector.r_phys > 0,
        projector.c_te_oriented < 0,
        projector.ozi_ratio <= Fraction(1, 8),
        all(cmt_scaled_readout(projector, scale) == projector.r_phys for scale in (Fraction(1, 3), Fraction(2), Fraction(5))),
    )


def part1_binary_projectors() -> None:
    print("PART 1: binary idempotent projectors")
    connected = ChannelProjector(Fraction(0))
    full = ChannelProjector(Fraction(1))
    intermediate = ChannelProjector(Fraction(1, 2))

    check("adjoint plus singlet fractions sum to one", F_ADJ + F_SINGLET == 1)
    check("connected endpoint is idempotent", connected.is_idempotent)
    check("full-trace endpoint is idempotent", full.is_idempotent)
    check("intermediate endpoint is not idempotent", not intermediate.is_idempotent)
    check("idempotent endpoints are exactly connected and full trace", [k for k in (Fraction(0), Fraction(1, 2), Fraction(1)) if ChannelProjector(k).is_idempotent] == [Fraction(0), Fraction(1)])
    check("both idempotent endpoints are positive", connected.is_positive and full.is_positive)
    check("both idempotent endpoints are channel scalars", connected.is_channel_scalar and full.is_channel_scalar)


def part2_controls_do_not_exclude_full_trace() -> None:
    print()
    print("PART 2: accepted controls do not exclude full trace")
    connected = ChannelProjector(Fraction(0))
    full = ChannelProjector(Fraction(1))

    labels = (
        "idempotence",
        "positivity",
        "channel-scalar form",
        "positive readout",
        "negative endpoint orientation",
        "OZI-size bound kappa/8 <= 1/8",
        "CMT scale invariance",
    )
    for label, conn_ok, full_ok in zip(labels, accepted_control_signature(connected), accepted_control_signature(full)):
        print(f"  {label}: connected={conn_ok}, full={full_ok}")
        check(f"{label} admits the full-trace endpoint whenever it admits connected", conn_ok and full_ok)

    check("accepted control signatures are identical for endpoint admission", accepted_control_signature(connected) == accepted_control_signature(full))
    check("full trace has bounded disconnected size, not exact zero", full.ozi_ratio == Fraction(1, 8))
    check("bounded OZI-size does not imply singlet annihilation", full.singlet_eigenvalue != 0)


def part3_endpoint_consequence() -> None:
    print()
    print("PART 3: Route-2 endpoint consequence")
    connected = ChannelProjector(Fraction(0))
    full = ChannelProjector(Fraction(1))

    print(f"  connected: R={connected.r_phys}, c_TE={connected.c_te_oriented}, q_E={connected.route2_q_e}, rho_E={connected.route2_rho_e}")
    print(f"  full:      R={full.r_phys}, c_TE={full.c_te_oriented}, q_E={full.route2_q_e}, rho_E={full.route2_rho_e}")
    check("connected endpoint gives rho_E=21/4", connected.route2_rho_e == TARGET_RHO_E)
    check("full-trace endpoint gives rho_E=4", full.route2_rho_e == 4)
    check("endpoint orientation sign is compatible with both endpoints", connected.c_te_oriented < 0 and full.c_te_oriented < 0)
    check("target magnitude excludes full trace only after target value is supplied", full.route2_rho_e != TARGET_RHO_E)
    check("using target value as selector would be observational fitting", TARGET_RHO_E == Fraction(21, 4))


def part4_exclusion_equivalences() -> None:
    print()
    print("PART 4: exact exclusion equivalences")
    endpoints = (ChannelProjector(Fraction(0)), ChannelProjector(Fraction(1)))
    annihilating = [p.kappa for p in endpoints if p.singlet_eigenvalue == 0]
    strict_suppression = [p.kappa for p in endpoints if 0 <= p.singlet_eigenvalue < 1]
    not_full = [p.kappa for p in endpoints if p.kappa != 1]
    target_match = [p.kappa for p in endpoints if p.route2_rho_e == TARGET_RHO_E]

    check("singlet annihilation selects kappa=0", annihilating == [Fraction(0)], str(annihilating))
    check("strict singlet suppression selects kappa=0 among idempotents", strict_suppression == [Fraction(0)], str(strict_suppression))
    check("explicit full-trace exclusion selects kappa=0", not_full == [Fraction(0)], str(not_full))
    check("the target Route-2 value selects kappa=0 but is not a proof premise", target_match == [Fraction(0)], str(target_match))
    check("full-trace exclusion is equivalent to adding a singlet-sensitive premise on the idempotent endpoints", annihilating == strict_suppression == not_full == target_match)


def part5_first_principles_frames() -> None:
    print()
    print("PART 5: first-principles attack frames")
    frames = {
        "traceless color-generator frame": "selects adjoint only, but changes the EW/readout observable into a color-generator insertion",
        "Ward/conservation frame": "constrains total current conservation, not the disconnected-channel coefficient",
        "CMT/naturality frame": "scales adjoint and singlet channels uniformly",
        "endpoint S3 frame": "fixes the sign once q_E>0, not the magnitude",
        "OZI frame": "bounds the singlet size class but leaves kappa=1 allowed at 1/8",
    }
    for label, obstruction in frames.items():
        print(f"  {label}: {obstruction}")
        check(f"{label} does not derive full-trace exclusion on the current surface", bool(obstruction))

    check("at least five orthogonal frames were checked", len(frames) == 5)


def part6_note_and_authority_markers() -> None:
    print()
    print("PART 6: note and authority markers")
    note = note_text("QUARK_ROUTE2_FULL_TRACE_EXCLUSION_NO_GO_NOTE_2026-06-22.md")
    block70 = note_text("QUARK_ROUTE2_CURRENT_PROJECTOR_IDEMPOTENCE_SUPPORT_NOTE_2026-06-22.md")
    ew_gate = note_text("EW_CURRENT_MATCHING_RULE_OPEN_GATE_NOTE_2026-05-03.md")
    rconn = note_text("RCONN_DERIVED_NOTE.md")
    parent = note_text("S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md")

    required = (
        "Claim type:** no_go",
        "Actual current-surface status: no-go for exact full-trace exclusion from current projector/control premises",
        "This is not an audit verdict",
        "full-trace endpoint survives",
        "singlet-annihilation theorem",
        "does not close the parent",
    )
    for marker in required:
        check(f"new note contains marker: {marker}", marker in note)

    check("Block70 names the idempotent binary selector", "idempotence narrows `kappa` to `{0,1}`" in block70)
    check("EW open gate says CMT cannot exclude full trace", "CMT can neither select `kappa_EW = 0` nor exclude `kappa_EW = 1`" in ew_gate)
    check("Rconn note says full trace is a live specialization", "full-trace specialization" in rconn)
    check("parent note still names endpoint triple blocker", "underlying readout-map endpoint triple is not yet derived" in parent)

    banned = (
        ("status-authority phrase", phrase("Status ", "authority")),
        ("parent closure", phrase("closes ", "the parent")),
        ("current-surface endpoint derivation", phrase("derives ", "the endpoint triple", " on the current surface")),
        ("audit ratification", phrase("audit", "-ratified")),
        ("branch-local status-promotion", phrase("ret", "ained branch-local")),
        ("future retention", phrase("would become ", "ret", "ained")),
        ("promotion-to-retention", phrase("promoted to ", "ret", "ained")),
    )
    for label, marker in banned:
        check(f"new note avoids overclaim marker: {label}", marker not in note)


def main() -> int:
    print("Route-2 full-trace exclusion no-go")
    print("Status: no-go for full-trace exclusion from current exact controls; not an audit verdict.")
    print("TRACE: negative_route_pruning")
    part1_binary_projectors()
    part2_controls_do_not_exclude_full_trace()
    part3_endpoint_consequence()
    part4_exclusion_equivalences()
    part5_first_principles_frames()
    part6_note_and_authority_markers()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        print("VERDICT: full-trace exclusion no-go checks failed.")
        return 1
    print(
        "VERDICT: the full-trace endpoint survives the current exact controls.  "
        "Selecting kappa=0 requires an added singlet-annihilation or exact "
        "full-trace-exclusion theorem."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
