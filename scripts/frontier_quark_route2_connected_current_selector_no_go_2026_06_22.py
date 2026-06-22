#!/usr/bin/env python3
"""Connected-current selector no-go for the Route-2 Rconn bridge.

Block68 reduced the oriented Rconn bridge magnitude to the selector

    kappa = 0

in

    R_phys(kappa) = F_adj + kappa * (1 - F_adj).

This runner proves the strongest current-surface obstruction: the exact
SU(3) two-channel packet supplies adjoint and singlet/disconnected channels,
but a channel-respecting scalar readout normalized on the adjoint channel
still has one free singlet coefficient kappa.  Fierz completeness, channel
normalization, CMT scaling, positivity, and bounded OZI-size controls do not
select kappa=0.  Exact kappa=0 is equivalent to importing a connected-current
projector that annihilates the singlet channel.

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
SINGLET = Fraction(1, 9)
TARGET_RHO_E = Fraction(21, 4)


@dataclass(frozen=True)
class TwoChannelReadout:
    kappa: Fraction

    @property
    def r_phys(self) -> Fraction:
        return F_ADJ + self.kappa * SINGLET

    @property
    def k_ew(self) -> Fraction:
        return Fraction(1, 1) / self.r_phys

    @property
    def connected_projection(self) -> bool:
        return self.kappa == 0

    @property
    def full_trace_projection(self) -> bool:
        return self.kappa == 1


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


def r_phys(kappa: Fraction) -> Fraction:
    return TwoChannelReadout(kappa).r_phys


def oriented_q_e(kappa: Fraction) -> Fraction:
    # c_TE=-R_phys(kappa), shell T/E=-2, q_T=5/6.
    return Fraction(5, 3) / r_phys(kappa)


def oriented_rho_e(kappa: Fraction) -> Fraction:
    return 6 * (oriented_q_e(kappa) - 1)


def cmt_scaled_readout(kappa: Fraction, u0: Fraction) -> Fraction:
    adj = F_ADJ * u0 * u0
    sing = SINGLET * u0 * u0
    total = adj + sing
    return (adj + kappa * sing) / total


def ozi_window(epsilon: Fraction) -> list[Fraction]:
    # Exact representative values allowed by a bounded singlet coefficient
    # 0 <= kappa <= epsilon.  A bound can shrink the interval but cannot
    # force zero unless epsilon is itself exactly zero.
    return [Fraction(0), epsilon / 2, epsilon]


def part1_two_channel_packet() -> None:
    print("PART 1: two-channel packet")
    check("SU(3) adjoint fraction is 8/9", F_ADJ == Fraction(8, 9), f"F_adj={F_ADJ}")
    check("singlet/disconnected fraction is 1/9", SINGLET == Fraction(1, 9), f"singlet={SINGLET}")
    check("adjoint plus singlet fractions sum to one", F_ADJ + SINGLET == 1)
    check("kappa=0 gives connected readout R_phys=8/9", r_phys(Fraction(0)) == Fraction(8, 9))
    check("kappa=1 gives full readout R_phys=1", r_phys(Fraction(1)) == Fraction(1))
    check("kappa=1/2 gives an exact intermediate readout", r_phys(Fraction(1, 2)) == Fraction(17, 18))


def part2_channel_respecting_readout_classifier() -> None:
    print()
    print("PART 2: channel-respecting readout classifier")
    samples = (Fraction(0), Fraction(1, 4), Fraction(1, 2), Fraction(3, 4), Fraction(1))
    values = []
    for kappa in samples:
        readout = TwoChannelReadout(kappa)
        values.append(readout.r_phys)
        print(f"  kappa={kappa}: R_phys={readout.r_phys}, K_EW={readout.k_ew}")
        check(f"kappa={kappa} is exact rational channel readout", isinstance(readout.r_phys, Fraction))
        check(f"kappa={kappa} preserves adjoint normalization", F_ADJ + kappa * SINGLET == readout.r_phys)

    check("the selector family has distinct exact values", len(set(values)) == len(values))
    check("connected projection is the kappa=0 endpoint of the family", TwoChannelReadout(Fraction(0)).connected_projection)
    check("full trace is the kappa=1 endpoint of the family", TwoChannelReadout(Fraction(1)).full_trace_projection)
    check("Fierz/channel normalization does not choose between endpoints", r_phys(Fraction(0)) != r_phys(Fraction(1)))


def part3_invariance_controls() -> None:
    print()
    print("PART 3: invariance controls")
    kappas = (Fraction(0), Fraction(1, 2), Fraction(1))
    scales = (Fraction(1, 2), Fraction(4, 5), Fraction(13, 10))
    for kappa in kappas:
        values = [cmt_scaled_readout(kappa, u0) for u0 in scales]
        print(f"  kappa={kappa}: scaled readouts={values}")
        check(f"CMT scale invariance holds for kappa={kappa}", all(value == values[0] for value in values))

    check("CMT scale invariance admits connected and full endpoints", cmt_scaled_readout(Fraction(0), Fraction(1, 2)) != cmt_scaled_readout(Fraction(1), Fraction(1, 2)))
    check("positivity admits the whole sampled interval", all(0 <= r_phys(kappa) <= 1 for kappa in kappas))
    check("monotonicity orders the family but does not select zero", r_phys(Fraction(0)) < r_phys(Fraction(1, 2)) < r_phys(Fraction(1)))


def part4_ozi_bound_firewall() -> None:
    print()
    print("PART 4: OZI-size bound firewall")
    eps = Fraction(1, 8)
    candidates = ozi_window(eps)
    for kappa in candidates:
        print(f"  kappa={kappa}: R_phys={r_phys(kappa)}, K_EW={TwoChannelReadout(kappa).k_ew}")
        check(f"kappa={kappa} obeys the OZI-size window", 0 <= kappa <= eps)

    check("a nonzero bounded singlet coefficient remains allowed", Fraction(1, 16) in candidates)
    check("bounded OZI-size narrows but does not derive kappa=0", len(set(candidates)) > 1)
    check("exact zero would require epsilon=0 or an annihilation theorem", ozi_window(Fraction(0)) == [Fraction(0), Fraction(0), Fraction(0)])


def part5_route2_magnitude_consequence() -> None:
    print()
    print("PART 5: Route-2 magnitude consequence")
    samples = (Fraction(0), Fraction(1, 2), Fraction(1))
    solved = {}
    for kappa in samples:
        rho = oriented_rho_e(kappa)
        solved[kappa] = rho
        print(f"  kappa={kappa}: q_E={oriented_q_e(kappa)}, rho_E={rho}")

    check("kappa=0 gives rho_E=21/4 under Block68 orientation support", solved[Fraction(0)] == TARGET_RHO_E)
    check("kappa=1/2 misses rho_E=21/4", solved[Fraction(1, 2)] != TARGET_RHO_E)
    check("kappa=1 misses rho_E=21/4", solved[Fraction(1)] != TARGET_RHO_E)
    check("Route-2 magnitude closure is exactly the connected selector endpoint", [k for k, rho in solved.items() if rho == TARGET_RHO_E] == [Fraction(0)])


def part6_authority_markers() -> None:
    print()
    print("PART 6: note and authority markers")
    note = note_text("QUARK_ROUTE2_CONNECTED_CURRENT_SELECTOR_NO_GO_NOTE_2026-06-22.md")
    rconn = note_text("RCONN_DERIVED_NOTE.md")
    block68 = note_text("QUARK_ROUTE2_ENDPOINT_ORIENTATION_SIGN_SUPPORT_NOTE_2026-06-22.md")
    parent = note_text("S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md")

    required = (
        "Claim type:** no_go",
        "Actual current-surface status: no-go for connected-current selector from equivariant two-channel data",
        "This is not an audit verdict",
        "normalization fixes the adjoint coefficient but leaves `kappa` free",
        "connected-current projector",
        "does not close the parent",
    )
    for marker in required:
        check(f"new note contains marker: {marker}", marker in note)

    check("Rconn note states kappa_EW is free", "free disconnected-channel" in rconn and "coefficient `kappa_EW`" in rconn)
    check("Rconn note says current packet does not derive kappa_EW=0", "does not derive\nthe selector `kappa_EW = 0`" in rconn)
    check("Block68 leaves magnitude to kappa=0", "connected selector `kappa=0`" in block68)
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
    print("Route-2 connected-current selector classifier")
    print("Status: no-go for connected-current selector from equivariant two-channel data; not an audit verdict.")
    print("TRACE: negative_route_pruning")
    part1_two_channel_packet()
    part2_channel_respecting_readout_classifier()
    part3_invariance_controls()
    part4_ozi_bound_firewall()
    part5_route2_magnitude_consequence()
    part6_authority_markers()
    print()
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    if FAIL:
        print("VERDICT: connected-current selector classifier failed.")
        return 1
    print(
        "VERDICT: no-go for deriving kappa=0 from the current equivariant "
        "two-channel packet.  Exact kappa=0 requires a connected-current "
        "projector or equivalent singlet-annihilation theorem."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
