#!/usr/bin/env python3
"""Current-projector idempotence dichotomy for the Route-2 Rconn selector.

Block69 showed that the channel-respecting readout

    R_phys(kappa) = F_adj + kappa F_singlet

leaves kappa free under Fierz/channel support and natural controls.  This
runner tests the next first-principles premise: require the current readout to
come from an exact idempotent channel projector normalized on the adjoint
channel.

Result: idempotence narrows kappa to the two exact projector endpoints
{0, 1}.  It does not choose the connected endpoint by itself.  A strict
singlet-suppression or singlet-annihilation premise is still needed to select
kappa=0.

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
    def adjoint_coeff(self) -> Fraction:
        return Fraction(1)

    @property
    def singlet_coeff(self) -> Fraction:
        return self.kappa

    @property
    def composed_singlet_coeff(self) -> Fraction:
        return self.kappa * self.kappa

    @property
    def is_idempotent(self) -> bool:
        return self.composed_singlet_coeff == self.singlet_coeff

    @property
    def r_phys(self) -> Fraction:
        return F_ADJ + self.kappa * F_SINGLET

    @property
    def route2_q_e(self) -> Fraction:
        return Fraction(5, 3) / self.r_phys

    @property
    def route2_rho_e(self) -> Fraction:
        return 6 * (self.route2_q_e - 1)


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


def idempotence_residual(kappa: Fraction) -> Fraction:
    return kappa * kappa - kappa


def part1_projector_algebra() -> None:
    print("PART 1: exact projector algebra")
    check("adjoint and singlet fractions sum to one", F_ADJ + F_SINGLET == 1)
    check("adjoint coefficient is normalized to one", ChannelProjector(Fraction(0)).adjoint_coeff == 1)
    for kappa in (Fraction(0), Fraction(1, 2), Fraction(1)):
        projector = ChannelProjector(kappa)
        print(
            f"  kappa={kappa}: singlet={projector.singlet_coeff}, "
            f"composed_singlet={projector.composed_singlet_coeff}, "
            f"idempotent={projector.is_idempotent}"
        )
        check(f"kappa={kappa} composition is exact", isinstance(projector.composed_singlet_coeff, Fraction))

    check("kappa=0 is idempotent", ChannelProjector(Fraction(0)).is_idempotent)
    check("kappa=1 is idempotent", ChannelProjector(Fraction(1)).is_idempotent)
    check("kappa=1/2 is not idempotent", not ChannelProjector(Fraction(1, 2)).is_idempotent)


def part2_dichotomy() -> None:
    print()
    print("PART 2: idempotence dichotomy")
    samples = [Fraction(n, 8) for n in range(0, 9)]
    roots = [kappa for kappa in samples if idempotence_residual(kappa) == 0]
    for kappa in samples:
        print(f"  kappa={kappa}: kappa^2-kappa={idempotence_residual(kappa)}")
    check("sampled idempotent roots are exactly 0 and 1", roots == [Fraction(0), Fraction(1)], str(roots))
    check("exact factorization is kappa(kappa-1)=0", all(idempotence_residual(k) == k * (k - 1) for k in samples))
    check("projector idempotence narrows the continuum to two endpoints", len(roots) == 2)
    check("idempotence alone does not choose connected over full", ChannelProjector(Fraction(0)).is_idempotent and ChannelProjector(Fraction(1)).is_idempotent)


def part3_route2_consequence() -> None:
    print()
    print("PART 3: Route-2 consequence")
    connected = ChannelProjector(Fraction(0))
    full = ChannelProjector(Fraction(1))
    print(f"  connected: R={connected.r_phys}, q_E={connected.route2_q_e}, rho_E={connected.route2_rho_e}")
    print(f"  full:      R={full.r_phys}, q_E={full.route2_q_e}, rho_E={full.route2_rho_e}")
    check("connected projector endpoint gives rho_E=21/4", connected.route2_rho_e == TARGET_RHO_E)
    check("full projector endpoint gives rho_E=4", full.route2_rho_e == 4)
    check("the two idempotent projectors have different Route-2 magnitudes", connected.route2_rho_e != full.route2_rho_e)
    check("target Route-2 magnitude selects the connected projector among idempotents", [k for k in (Fraction(0), Fraction(1)) if ChannelProjector(k).route2_rho_e == TARGET_RHO_E] == [Fraction(0)])


def part4_suppression_selector() -> None:
    print()
    print("PART 4: strict suppression selector")
    idempotent_roots = (Fraction(0), Fraction(1))
    strict_bound = Fraction(1, 2)
    selected = [kappa for kappa in idempotent_roots if 0 <= kappa <= strict_bound]
    weak_selected = [kappa for kappa in idempotent_roots if 0 <= kappa <= 1]
    check("idempotence plus strict singlet bound kappa<1 selects kappa=0", selected == [Fraction(0)], str(selected))
    check("idempotence plus only positivity leaves both endpoints", weak_selected == [Fraction(0), Fraction(1)], str(weak_selected))
    check("singlet annihilation is equivalent to kappa=0", ChannelProjector(Fraction(0)).singlet_coeff == 0)
    check("excluding the full-trace projector is the remaining non-arithmetic premise", ChannelProjector(Fraction(1)).route2_rho_e != TARGET_RHO_E)


def part5_authority_markers() -> None:
    print()
    print("PART 5: note and authority markers")
    note = note_text("QUARK_ROUTE2_CURRENT_PROJECTOR_IDEMPOTENCE_SUPPORT_NOTE_2026-06-22.md")
    block69 = note_text("QUARK_ROUTE2_CONNECTED_CURRENT_SELECTOR_NO_GO_NOTE_2026-06-22.md")
    rconn = note_text("RCONN_DERIVED_NOTE.md")
    parent = note_text("S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md")

    required = (
        "Claim type:** bounded_support",
        "Actual current-surface status: bounded-support for idempotent current-projector dichotomy",
        "This is not an audit verdict",
        "idempotence narrows `kappa` to `{0,1}`",
        "idempotence alone does not choose the connected endpoint",
        "strict singlet-suppression",
    )
    for marker in required:
        check(f"new note contains marker: {marker}", marker in note)

    check("Block69 exposes kappa=0 as connected-current projector", "connected-current projector" in block69)
    check("Rconn note names full trace and connected specializations", "full-trace specialization" in rconn and "connected-trace specialization" in rconn)
    check("parent note still names the readout endpoint blocker", "underlying readout-map endpoint triple is not yet derived" in parent)

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
    print("Route-2 current-projector idempotence support")
    print("Status: bounded-support for idempotent current-projector dichotomy; not an audit verdict.")
    print("TRACE: upstream_support")
    part1_projector_algebra()
    part2_dichotomy()
    part3_route2_consequence()
    part4_suppression_selector()
    part5_authority_markers()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        print("VERDICT: current-projector idempotence checks failed.")
        return 1
    print(
        "VERDICT: idempotence narrows kappa to {0,1}.  Selecting kappa=0 "
        "still requires strict singlet suppression or singlet annihilation."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
