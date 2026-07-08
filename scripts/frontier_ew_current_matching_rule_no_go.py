#!/usr/bin/env python3
"""EW current matching-rule kappa_EW parametrization runner.

This verifies the audited-conditional narrow repair: KAPPA-EW is a supplied
premise and the exact family is

    K_EW(kappa) = 1 / (F_adj + kappa * (1 - F_adj)).

Fatal/load-bearing checks drive the exit code. Motivation-tier downstream
wording checks are reported separately and never create a nonzero exit.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from fractions import Fraction
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "EW_CURRENT_MATCHING_RULE_OPEN_GATE_NOTE_2026-05-03.md"
FIERZ = DOCS / "EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md"
RUNNER = "scripts/frontier_ew_current_matching_rule_no_go.py"

FATAL_TIERS = ("LOAD_BEARING", "TEXT", "SELFTEST")
MOTIVATION_TIERS = ("MOTIVATION",)
ALL_TIERS = FATAL_TIERS + MOTIVATION_TIERS

KAPPA_BLOCK = """KAPPA-EW (named conditional premise):
the physical disconnected-current readout coefficient kappa_EW is
SUPPLIED; the connected-trace selector is the special case kappa_EW = 0.
Not derived: no landed route selects kappa_EW; this note's
parametrization covers every finite value exactly."""

KAPPA_EXPECTED = (
    ("0", Fraction(0), Fraction(9, 8)),
    ("1", Fraction(1), Fraction(1)),
    ("1/2", Fraction(1, 2), Fraction(18, 17)),
    ("-1/9", Fraction(-1, 9), Fraction(81, 71)),
    ("2", Fraction(2), Fraction(9, 10)),
)


@dataclass
class Ledger:
    passed: dict[str, int] = field(default_factory=dict)
    failed: dict[str, int] = field(default_factory=dict)
    failures: list[tuple[str, str, str]] = field(default_factory=list)

    def check(self, tier: str, name: str, ok: bool, detail: str = "") -> None:
        if tier not in ALL_TIERS:
            raise ValueError(f"unknown tier: {tier}")
        target = self.passed if ok else self.failed
        target[tier] = target.get(tier, 0) + 1
        if not ok:
            self.failures.append((tier, name, detail))

    def tier_counts(self, tiers: tuple[str, ...]) -> tuple[int, int]:
        pass_count = sum(self.passed.get(tier, 0) for tier in tiers)
        fail_count = sum(self.failed.get(tier, 0) for tier in tiers)
        return pass_count, fail_count

    def exit_code(self) -> int:
        _passed, fatal_fail = self.tier_counts(FATAL_TIERS)
        return 1 if fatal_fail else 0


def read_if_exists(path: Path) -> str:
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8")


def f_adj(n_c: int) -> Fraction:
    return Fraction(n_c * n_c - 1, n_c * n_c)


def singlet_fraction(n_c: int) -> Fraction:
    return Fraction(1, n_c * n_c)


def denominator(n_c: int, kappa: Fraction) -> Fraction:
    f = f_adj(n_c)
    return f + kappa * (1 - f)


def k_ew(n_c: int, kappa: Fraction) -> Fraction | None:
    denom = denominator(n_c, kappa)
    if denom == 0:
        return None
    return Fraction(1) / denom


@dataclass(frozen=True)
class Completion:
    n_c: int
    kappa: Fraction
    u0_squared: Fraction

    @property
    def c_v(self) -> Fraction:
        return f_adj(self.n_c)

    @property
    def s_v(self) -> Fraction:
        return singlet_fraction(self.n_c)

    @property
    def t_v(self) -> Fraction:
        return self.c_v + self.s_v

    @property
    def c_u(self) -> Fraction:
        return self.u0_squared * self.c_v

    @property
    def s_u(self) -> Fraction:
        return self.u0_squared * self.s_v

    @property
    def t_u(self) -> Fraction:
        return self.c_u + self.s_u

    @property
    def readout_v(self) -> Fraction:
        return self.c_v + self.kappa * self.s_v

    @property
    def readout_u(self) -> Fraction:
        return self.c_u + self.kappa * self.s_u

    @property
    def matching_v(self) -> Fraction | None:
        if self.readout_v == 0:
            return None
        return self.t_v / self.readout_v

    @property
    def matching_u(self) -> Fraction | None:
        if self.readout_u == 0:
            return None
        return self.t_u / self.readout_u

    @property
    def ozi_ratio(self) -> Fraction:
        return self.kappa * self.s_v / self.c_v


def primitive_signature(model: Completion) -> tuple[Fraction, ...]:
    return (
        f_adj(model.n_c),
        singlet_fraction(model.n_c),
        model.c_u / model.c_v,
        model.s_u / model.s_v,
    )


def markdown_note_links(markdown: str) -> list[str]:
    return re.findall(r"\]\(([^)]+\.md)\)", markdown)


def downstream_guard(
    ledger: Ledger,
    path: Path,
    required: tuple[str, ...],
    forbidden: tuple[str, ...],
) -> None:
    text = read_if_exists(path)
    rel = path.relative_to(ROOT).as_posix()
    ledger.check("MOTIVATION", f"{rel} exists", bool(text), rel)
    for needle in required:
        ledger.check(
            "MOTIVATION",
            f"{rel} contains {needle!r}",
            needle in text,
            "conditional downstream wording",
        )
    for phrase in forbidden:
        ledger.check(
            "MOTIVATION",
            f"{rel} avoids {phrase!r}",
            phrase not in text,
            "unconditional EW-retention wording absent",
        )


def accounting_self_test() -> bool:
    fatal_and_motivation = Ledger()
    fatal_and_motivation.check("LOAD_BEARING", "fatal sample", False)
    fatal_and_motivation.check("MOTIVATION", "nonfatal sample", False)

    motivation_only = Ledger()
    motivation_only.check("MOTIVATION", "nonfatal sample", False)

    return (
        fatal_and_motivation.exit_code() == 1
        and motivation_only.exit_code() == 0
        and fatal_and_motivation.tier_counts(FATAL_TIERS) == (0, 1)
        and fatal_and_motivation.tier_counts(MOTIVATION_TIERS) == (0, 1)
    )


def check_note_contract(ledger: Ledger, note: str, fierz: str) -> None:
    ledger.check(
        "TEXT",
        "note declares bounded_theorem",
        "**Claim type:** bounded_theorem" in note,
    )
    ledger.check(
        "TEXT",
        "note does not retain no_go claim header",
        "**Claim type:** no_go" not in note,
    )
    ledger.check("TEXT", "note registers primary runner", RUNNER in note)
    ledger.check("TEXT", "KAPPA-EW block is verbatim", KAPPA_BLOCK in note)
    ledger.check("TEXT", "KAPPA-EW is supplied", "SUPPLIED;" in note)
    ledger.check("TEXT", "FIERZ-ADJ surface feature named", "**FIERZ-ADJ:**" in note)
    ledger.check(
        "TEXT",
        "CMT-COLOR-BLIND feature named",
        "**CMT-COLOR-BLIND:**" in note,
    )
    ledger.check("TEXT", "OZI-BOUNDED feature named", "**OZI-BOUNDED:**" in note)
    ledger.check(
        "TEXT",
        "generic K_EW formula present",
        "K_EW(kappa_EW) = 1 / (F_adj + kappa_EW (1 - F_adj))" in note,
    )
    ledger.check(
        "TEXT",
        "N_c=3 K_EW formula present",
        "K_EW(kappa_EW) = 1 / (8/9 + kappa_EW/9)" in note,
    )
    ledger.check(
        "TEXT",
        "completion exhibit present",
        "Completion A: kappa_EW = 0,  K_EW = 9/8." in note
        and "Completion B: kappa_EW = 1,  K_EW = 1." in note,
    )
    ledger.check(
        "TEXT",
        "residual does not claim selector closure",
        "R-selector remains open" in note and "not as a claim of this note" in note,
    )
    ledger.check(
        "TEXT",
        "citation contract is audit-gated",
        "Citation is audit-gated" in note and "Forbidden uses:" in note,
    )
    ledger.check(
        "TEXT",
        "safe downstream wording retained",
        "The EW normalization lane is bounded by a named matching coefficient" in note
        and "not an unconditional retained theorem" in note,
    )
    ledger.check(
        "TEXT",
        "unsafe downstream wording retained",
        "The framework derives the exact `9/8` EW color-projection correction." in note,
    )
    ledger.check(
        "TEXT",
        "old theorem landing language absent",
        "No-go theorem (matching-rule underdetermination)" not in note
        and "close the former open gate negatively" not in note,
    )
    links = markdown_note_links(note)
    ledger.check(
        "TEXT",
        "only Fierz note is linked as dependency",
        links == ["EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md"],
        f"links={links}",
    )
    ledger.check(
        "TEXT",
        "Fierz authority leaves matching rule open",
        "The matching rule is **not derived in this note**" in fierz,
    )


def check_exact_algebra(ledger: Ledger) -> None:
    n_c = 3
    f = f_adj(n_c)
    s = singlet_fraction(n_c)
    ledger.check("LOAD_BEARING", "F_adj at N_c=3 is 8/9", f == Fraction(8, 9), str(f))
    ledger.check("LOAD_BEARING", "S at N_c=3 is 1/9", s == Fraction(1, 9), str(s))
    ledger.check("LOAD_BEARING", "channels sum to T=1", f + s == 1, str(f + s))

    for label, kappa, expected in KAPPA_EXPECTED:
        actual = k_ew(n_c, kappa)
        ledger.check(
            "LOAD_BEARING",
            f"K_EW({label}) exact value",
            actual == expected,
            f"got={actual} expected={expected}",
        )
        model = Completion(n_c=n_c, kappa=kappa, u0_squared=Fraction(77, 100))
        ledger.check(
            "LOAD_BEARING",
            f"CMT invariance at kappa={label}",
            model.matching_u == model.matching_v == expected,
            f"K_U={model.matching_u} K_V={model.matching_v}",
        )
        expected_ozi = kappa / Fraction(n_c * n_c - 1)
        ledger.check(
            "LOAD_BEARING",
            f"OZI ratio identity at kappa={label}",
            model.ozi_ratio == expected_ozi,
            f"got={model.ozi_ratio} expected={expected_ozi}",
        )

    ledger.check(
        "LOAD_BEARING",
        "zero-denominator pole is algebraically marked",
        denominator(n_c, Fraction(-8)) == 0 and k_ew(n_c, Fraction(-8)) is None,
    )

    connected = Completion(n_c=n_c, kappa=Fraction(0), u0_squared=Fraction(77, 100))
    full_trace = Completion(n_c=n_c, kappa=Fraction(1), u0_squared=Fraction(77, 100))
    ledger.check(
        "LOAD_BEARING",
        "two completions share primitive data",
        primitive_signature(connected) == primitive_signature(full_trace),
        f"signature={primitive_signature(connected)}",
    )
    ledger.check(
        "LOAD_BEARING",
        "two completions compute different K_EW values",
        connected.matching_v == Fraction(9, 8)
        and full_trace.matching_v == Fraction(1)
        and connected.matching_v != full_trace.matching_v,
    )

    for other_n in (2, 3, 4, 5, 10):
        model = Completion(
            n_c=other_n,
            kappa=Fraction(1),
            u0_squared=Fraction(3, 5),
        )
        bound = Fraction(1, other_n * other_n - 1)
        ledger.check(
            "LOAD_BEARING",
            f"full-trace OZI ratio at N_c={other_n}",
            model.ozi_ratio == bound,
            f"got={model.ozi_ratio} expected={bound}",
        )


def check_downstream_context(ledger: Ledger) -> None:
    downstream_guard(
        ledger,
        DOCS / "YT_EW_COLOR_PROJECTION_THEOREM.md",
        required=(
            "kappa_EW",
            "K_EW(kappa_EW)",
            'must say "conditional on the connected-trace specialization',
        ),
        forbidden=(
            "**Status:** " + "proposed" + "_retained EW normalization lane",
            "The correction 9/8 on the EW couplings is derived from",
        ),
    )
    downstream_guard(
        ledger,
        DOCS / "publication" / "ci3_z3" / "QUANTITATIVE_SUMMARY_TABLE.md",
        required=("matching-rule conditional", "kappa_EW"),
        forbidden=(
            "| `g_1(v)` | `0.4644` | `0.4640` | `+0.08%` | retained |",
            "| `g_2(v)` | `0.6480` | `0.6463` | `+0.26%` | retained |",
        ),
    )
    downstream_guard(
        ledger,
        DOCS / "publication" / "ci3_z3" / "USABLE_DERIVED_VALUES_INDEX.md",
        required=("K_EW(kappa_EW)", "conditional"),
        forbidden=(
            "| `g_1(v)` | `0.4644` | derived |",
            "| `g_2(v)` | `0.6480` | derived |",
        ),
    )
    downstream_guard(
        ledger,
        DOCS / "CANONICAL_HARNESS_INDEX.md",
        required=("frontier_ew_current_matching_rule_no_go.py",),
        forbidden=("EW current matching rule open main gate",
        "EW current matching rule no-go proposal",),
    )


def print_summary(ledger: Ledger) -> None:
    fatal_pass, fatal_fail = ledger.tier_counts(FATAL_TIERS)
    motivation_pass, motivation_fail = ledger.tier_counts(MOTIVATION_TIERS)
    print("=" * 78)
    print("EW CURRENT MATCHING-RULE KAPPA PARAMETRIZATION")
    print("=" * 78)
    print(f"runner: {RUNNER}")
    print("declaration: KAPPA-EW is supplied; no selector is derived")
    print(f"fatal: PASS={fatal_pass} FAIL={fatal_fail}")
    print(f"motivation: PASS={motivation_pass} FAIL={motivation_fail} (non-fatal)")
    for tier, name, detail in ledger.failures[:4]:
        suffix = f" -- {detail}" if detail else ""
        print(f"FAIL[{tier}] {name}{suffix}")
    print(f"RESULT: {'PASS' if fatal_fail == 0 else 'FAIL'}")


def main() -> int:
    ledger = Ledger()
    note = read_if_exists(NOTE)
    fierz = read_if_exists(FIERZ)

    ledger.check("LOAD_BEARING", "authority note exists", NOTE.exists(), str(NOTE))
    ledger.check("LOAD_BEARING", "Fierz authority exists", FIERZ.exists(), str(FIERZ))
    ledger.check("SELFTEST", "tier accounting self-test", accounting_self_test())

    check_note_contract(ledger, note, fierz)
    check_exact_algebra(ledger)
    check_downstream_context(ledger)
    print_summary(ledger)
    return ledger.exit_code()


if __name__ == "__main__":
    raise SystemExit(main())
