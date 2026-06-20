#!/usr/bin/env python3
"""Selector firewall for the DM leptogenesis PMNS transport interval row."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PARENT = ROOT / "docs" / "DM_LEPTOGENESIS_PMNS_TRANSPORT_EXTREMAL_SOURCE_CANDIDATE_NOTE_2026-04-16.md"
FIREWALL = ROOT / "docs" / "DM_LEPTOGENESIS_PMNS_TRANSPORT_SELECTOR_FIREWALL_NOTE_2026-06-17.md"

SEED_VALUE = 0.719082664368
OVERSHOOT_VALUE = 1.0522203130495849
ALT_OVERSHOOT_VALUE = 1.25


class Gate:
    def __init__(self) -> None:
        self.pass_count = 0
        self.fail_count = 0

    def check(self, label: str, condition: bool, detail: str = "") -> None:
        if condition:
            self.pass_count += 1
            status = "PASS"
        else:
            self.fail_count += 1
            status = "FAIL"
        suffix = f" -- {detail}" if detail else ""
        print(f"{status}: {label}{suffix}")


def linear_root(left: float, right: float, target: float = 1.0) -> float:
    return (target - left) / (right - left)


def linear_value(left: float, right: float, lam: float) -> float:
    return (1.0 - lam) * left + lam * right


def squash(text: str) -> str:
    return " ".join(text.split())


def main() -> int:
    gate = Gate()
    parent = PARENT.read_text(encoding="utf-8")
    firewall = FIREWALL.read_text(encoding="utf-8")
    parent_flat = squash(parent)

    print("DM leptogenesis PMNS transport selector firewall")

    root = linear_root(SEED_VALUE, OVERSHOOT_VALUE)
    alt_root = linear_root(SEED_VALUE, ALT_OVERSHOOT_VALUE)

    gate.check(
        "parent endpoint interval brackets eta/eta_obs = 1",
        SEED_VALUE < 1.0 < OVERSHOOT_VALUE,
        f"seed={SEED_VALUE:.12f}, overshoot={OVERSHOOT_VALUE:.12f}",
    )
    gate.check("linear crossing root lies in the open interval", 0.0 < root < 1.0, f"lambda={root:.12f}")
    gate.check(
        "linear crossing evaluates exactly to the target level",
        abs(linear_value(SEED_VALUE, OVERSHOOT_VALUE, root) - 1.0) < 1.0e-14,
        f"value={linear_value(SEED_VALUE, OVERSHOOT_VALUE, root):.12f}",
    )
    gate.check(
        "a different supplied overshoot endpoint gives a different root",
        0.0 < alt_root < 1.0 and abs(alt_root - root) > 1.0e-2,
        f"root={root:.12f}, alternate={alt_root:.12f}",
    )
    gate.check(
        "the equality point is target-defined unless an independent selector is supplied",
        "not a physical selector law" in firewall
        and "ETA_OBS" in firewall
        and "hidden\nselector" in firewall,
    )
    gate.check(
        "firewall forbids using the observed comparator as the selector",
        "treating `ETA_OBS` as a selected framework output" in firewall
        and "choosing the interpolation root because it equals the observed comparator" in firewall,
    )
    gate.check(
        "firewall preserves future positive selector routes",
        "This firewall does not rule those routes out" in firewall
        and "independent theorem deriving" in firewall,
    )
    gate.check(
        "parent cites the selector firewall companion",
        "DM_LEPTOGENESIS_PMNS_TRANSPORT_SELECTOR_FIREWALL_NOTE_2026-06-17.md" in parent,
    )
    gate.check(
        "parent scopes the exact root as diagnostic rather than selected",
        "intermediate-value diagnostic" in parent_flat
        and "not a physical selector" in parent_flat
        and "should not be cited as a framework prediction" in parent_flat,
    )
    gate.check(
        "parent keeps the bounded interval support claim",
        "seed endpoint below `1`" in parent
        and "sampled endpoint above `1`" in parent
        and "Bounded interval support" in parent,
    )
    gate.check(
        "parent out-of-scope list rejects lambda-star selection",
        "the interpolated value `lambda_*` is selected by the framework" in parent,
    )
    gate.check(
        "companion claims no audit status authority",
        "independent audit owns effective\nstatus" in firewall
        and "source-side selector firewall" in firewall,
    )

    print(f"PASS={gate.pass_count} FAIL={gate.fail_count}")
    return 0 if gate.fail_count == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
