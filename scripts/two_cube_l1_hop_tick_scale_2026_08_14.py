#!/usr/bin/env python3
"""Exact hop-to-tick scale on the two-cube L1 axis.

Paired note:
  docs/TWO_CUBE_L1_HOP_TICK_SCALE_BOUNDED_THEOREM_NOTE_2026-08-14.md

Occupancy ρ and first-lock times φ are computed from the saturated
nearest-neighbor causal front on the twelve-site two-cube. The integer a is
obtained by enumerating {1,2,3}; it is not inserted as a constant.
"""

from __future__ import annotations

from pathlib import Path


AUDIT_TIMEOUT_SEC = 120

ROOT = Path(__file__).resolve().parents[1]
NOTE_REL = "docs/TWO_CUBE_L1_HOP_TICK_SCALE_BOUNDED_THEOREM_NOTE_2026-08-14.md"
AXIOM_REL = "docs/MINIMAL_AXIOMS_2026-06-29.md"
AUDIT_INPUT_PATHS = (
    "docs/TWO_CUBE_L1_HOP_TICK_SCALE_BOUNDED_THEOREM_NOTE_2026-08-14.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)

NOTE_PATH = ROOT / NOTE_REL
AXIOM_PATH = ROOT / AXIOM_REL

Site = tuple[int, int, int]
SEED: Site = (0, 0, 0)
AXIS_D1: Site = (1, 0, 0)
AXIS_D2: Site = (2, 0, 0)
HORIZON = 2
SCALE_CANDIDATES = (1, 2, 3)
FORBIDDEN_PHRASES = ("G_N", "1/r", "1/r^2", "Lattice-named", "not a TOE")


def two_cube_sites() -> frozenset[Site]:
    return frozenset(
        (x, y, z) for x in (0, 1, 2) for y in (0, 1) for z in (0, 1)
    )


def l1(site: Site, origin: Site = SEED) -> int:
    return (
        abs(site[0] - origin[0])
        + abs(site[1] - origin[1])
        + abs(site[2] - origin[2])
    )


def neighbors(site: Site, carrier: frozenset[Site]) -> frozenset[Site]:
    x, y, z = site
    candidates = (
        (x + 1, y, z),
        (x - 1, y, z),
        (x, y + 1, z),
        (x, y - 1, z),
        (x, y, z + 1),
        (x, y, z - 1),
    )
    return frozenset(candidate for candidate in candidates if candidate in carrier)


def five_site_line() -> frozenset[Site]:
    return frozenset((k, 0, 0) for k in range(5))


def occupy(
    carrier: frozenset[Site], seed: Site, horizon: int
) -> tuple[tuple[frozenset[Site], ...], dict[Site, int | None]]:
    """Return occupancy sets ρ_t and first-lock times φ."""
    if seed not in carrier:
        raise ValueError("seed must lie in the carrier")
    locked = {seed}
    history = [frozenset(locked)]
    first_lock: dict[Site, int | None] = {
        site: (0 if site == seed else None) for site in carrier
    }
    for tick in range(1, horizon + 1):
        newly = {
            site
            for site in carrier
            if site not in locked
            and any(neighbor in locked for neighbor in neighbors(site, carrier))
        }
        locked = locked | newly
        for site in newly:
            first_lock[site] = tick
        history.append(frozenset(locked))
    return tuple(history), first_lock


def scale_holds(
    first_lock: dict[Site, int | None], axis: tuple[Site, ...], scale: int
) -> bool:
    return all(first_lock[site] == scale * l1(site) for site in axis)


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0

    def check(self, label: str, condition: bool, detail: str = "") -> None:
        ok = bool(condition)
        self.passed += int(ok)
        self.failed += int(not ok)
        suffix = f"  ({detail})" if detail else ""
        print(f"{'PASS' if ok else 'FAIL'}: {label}{suffix}")

    def finish(self) -> int:
        print(f"TOTAL: PASS={self.passed} FAIL={self.failed}")
        return 0 if self.failed == 0 else 1


def normalize(text: str) -> str:
    return " ".join(text.split())


def main() -> int:
    checks = Checks()
    note = NOTE_PATH.read_text(encoding="utf-8")
    axiom = AXIOM_PATH.read_text(encoding="utf-8")
    carrier = two_cube_sites()
    occupancy, first_lock = occupy(carrier, SEED, HORIZON)
    axis = (AXIS_D1, AXIS_D2)
    fitting = tuple(
        scale for scale in SCALE_CANDIDATES if scale_holds(first_lock, axis, scale)
    )

    print("Two-cube L1 hop-to-tick scale")
    print("AUDIT_INPUT_PATHS:")
    for path in AUDIT_INPUT_PATHS:
        print(f"  {path}")
    print(f"AUDIT_TIMEOUT_SEC: {AUDIT_TIMEOUT_SEC}")
    print("cache_write: false")
    print(
        "scope: supplied two-cube and saturated nearest-neighbor causal front; "
        "no physical clock metric"
    )
    print(f"computed_first_lock_axis: {AXIS_D1}->{first_lock[AXIS_D1]}, "
          f"{AXIS_D2}->{first_lock[AXIS_D2]}")
    print(f"fitting_scales_in_{SCALE_CANDIDATES}: {fitting}")

    checks.check(
        "audit-input-paths-exist",
        all((ROOT / path).is_file() for path in AUDIT_INPUT_PATHS),
    )
    checks.check(
        "audit-input-paths-unique-normalized",
        len(AUDIT_INPUT_PATHS) == len(set(AUDIT_INPUT_PATHS))
        and all(
            not Path(path).is_absolute() and ".." not in Path(path).parts
            for path in AUDIT_INPUT_PATHS
        ),
    )
    checks.check("audit-timeout-declared", AUDIT_TIMEOUT_SEC == 120)
    checks.check(
        "two-cube-has-twelve-sites",
        len(carrier) == 12 and SEED in carrier and set(axis) <= set(carrier),
        f"|S|={len(carrier)}",
    )
    checks.check(
        "axis-l1-distances",
        l1(AXIS_D1) == 1 and l1(AXIS_D2) == 2,
        f"d({AXIS_D1})={l1(AXIS_D1)}, d({AXIS_D2})={l1(AXIS_D2)}",
    )
    checks.check(
        "axis-are-nearest-neighbor-hops",
        AXIS_D1 in neighbors(SEED, carrier)
        and AXIS_D2 in neighbors(AXIS_D1, carrier)
        and AXIS_D2 not in neighbors(SEED, carrier),
    )
    checks.check(
        "theorem1-p1-unread-at-0-locked-at-1",
        AXIS_D1 not in occupancy[0]
        and AXIS_D1 in occupancy[1]
        and first_lock[AXIS_D1] == 1,
        f"rho0={int(AXIS_D1 in occupancy[0])} rho1={int(AXIS_D1 in occupancy[1])} "
        f"phi={first_lock[AXIS_D1]}",
    )
    checks.check(
        "theorem2-p2-unread-before-2-locked-at-2",
        AXIS_D2 not in occupancy[0]
        and AXIS_D2 not in occupancy[1]
        and AXIS_D2 in occupancy[2]
        and first_lock[AXIS_D2] == 2,
        f"phi={first_lock[AXIS_D2]}",
    )
    checks.check(
        "theorem3-a1-fits-both-axis-sites",
        scale_holds(first_lock, axis, 1),
    )
    checks.check(
        "theorem3-a2-would-lock-p1-at-tick-2",
        first_lock[AXIS_D1] != 2 * l1(AXIS_D1)
        and not scale_holds(first_lock, axis, 2),
    )
    checks.check(
        "theorem3-unique-a-in-1-2-3-is-1",
        fitting == (1,),
        f"fitting={fitting}",
    )
    checks.check(
        "never-earlier-than-l1",
        all(
            first_lock[site] is None or first_lock[site] >= l1(site)
            for site in carrier
        )
        and all(
            first_lock[site] == l1(site)
            for site in carrier
            if l1(site) <= HORIZON
        ),
    )
    checks.check(
        "rho-and-phi-are-history-not-line",
        len(occupancy) == HORIZON + 1
        and first_lock[SEED] == 0
        and len(carrier) != len(five_site_line())
        and any(site[1] != 0 or site[2] != 0 for site in carrier)
        and "pair `(ρ,φ)`" in note
        and "five-site line" in note,
    )
    checks.check(
        "not-single-snapshot-leftover",
        AXIS_D1 in occupancy[1]
        and AXIS_D2 not in occupancy[1]
        and first_lock[AXIS_D2] != (1 if AXIS_D2 in occupancy[1] else 0)
        and "leftover identity on one snapshot" in note
        and "whole occupancy history" in note,
    )

    lattice_sentence = (
        "Physical sites are the points of the cubic lattice `Z^3`, with "
        "nearest-neighbor adjacency, standard translations, and proper cubic "
        "rotations about each site."
    )
    lock_sentence = (
        "When present, a record locks exactly one admissible local possibility."
    )
    unread_sentence = "A site with no record cannot be read."
    checks.check(
        "source-lattice-sentence-current",
        lattice_sentence in normalize(axiom) and lattice_sentence in normalize(note),
    )
    checks.check(
        "source-record-unread-lock-current",
        "Records form." in axiom
        and lock_sentence in normalize(axiom)
        and unread_sentence in axiom
        and unread_sentence in note,
    )
    checks.check(
        "note-machine-status-complete",
        all(
            marker in note
            for marker in (
                "actual_current_surface_status: bounded-support",
                "target_claim_type: bounded_theorem",
                "trace_class: frontier_discovery",
                "target_claim_id: two_cube_l1_hop_tick_scale",
                "reachability_to_target: advances",
                'hypothetical_axiom_status: "no edit"',
                "audit_required_before_effective_retained: true",
                "bare_retained_allowed: false",
            )
        ),
    )
    checks.check(
        "import-boundary-and-no-axiom-edit",
        "## Inputs And Import Boundary" in note
        and "Explicit theorem-domain condition" in note
        and "No axiom, primitive, registry, or audit verdict is edited." in note
        and "upstream_dependencies:\n  - minimal_axioms" in note,
    )
    forbidden_hits = [phrase for phrase in FORBIDDEN_PHRASES if phrase in note]
    checks.check(
        "forbidden-phrases-absent",
        not forbidden_hits,
        f"hits={forbidden_hits}",
    )

    print(
        "per_element: checked — occupancy and first-lock time are evaluated "
        "at every two-cube site through tick 2"
    )
    print(
        "per_site: checked — seed, (1,0,0), and (2,0,0) are resolved on S"
    )
    print("per_mode: not applicable — no spectral decomposition is used")
    print(
        "per_block: checked — only the supplied two-cube and a in {1,2,3} "
        "are enumerated"
    )
    print(
        "lattice_wide: checked and not executed — no Z^3 formation kernel "
        "or physical clock is claimed"
    )
    return checks.finish()


if __name__ == "__main__":
    raise SystemExit(main())
