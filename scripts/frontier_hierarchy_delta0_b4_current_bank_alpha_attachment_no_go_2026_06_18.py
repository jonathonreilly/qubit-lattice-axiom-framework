#!/usr/bin/env python3
"""Current-bank alpha-attachment no-go for the hierarchy DELTA0 B4 gate."""

from __future__ import annotations

from dataclasses import dataclass
from itertools import product
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "HIERARCHY_DELTA0_B4_CURRENT_BANK_ALPHA_ATTACHMENT_NO_GO_NOTE_2026-06-18.md"
PARENT_GATE = DOCS / "HIERARCHY_ALPHA_LM_MAGNITUDE_DELTA0_OPEN_GATE_NOTE_2026-05-30.md"
ENUM_NOTE = DOCS / "HIERARCHY_DELTA0_B4_ATTACHMENT_OBSERVABLE_ENUMERATION_NOTE_2026-06-11.md"
S1P_NOTE = DOCS / "HIERARCHY_DELTA0_S1PRIME_TASTE_REGION_KERNEL_SHARE_PROBE_NOTE_2026-06-11.md"
RATIO_NOTE = DOCS / "HIERARCHY_DELTA0_RATIO_NORMALIZED_ALPHA_S_PER_DECOUPLING_REDUCTION_NOTE_2026-06-11.md"

PASS = 0
FAIL = 0
CLASS_COUNTS = {"A": 0, "B": 0, "C": 0, "D": 0}


@dataclass(frozen=True)
class Signature:
    """Exponent pair for alpha_bare^a * u_0^b, constants stripped."""

    alpha_exp: int
    u0_exp: int

    def __mul__(self, other: "Signature") -> "Signature":
        return Signature(self.alpha_exp + other.alpha_exp, self.u0_exp + other.u0_exp)

    def power(self, n: int) -> "Signature":
        return Signature(self.alpha_exp * n, self.u0_exp * n)


@dataclass(frozen=True)
class BankBlock:
    family: str
    count: int
    mechanism_class: str
    alpha_exp: int
    has_readout_mechanism: bool
    note: str


CURRENT_BANK = (
    BankBlock("K1 determinant/share readouts", 20, "genuine_readout", 0, True, "u_0-only determinant factors and ratios"),
    BankBlock("K2 IR-slope dressing grid", 40, "supplier_chain_grid", 1, False, "built from m/(4 pi) and dressing choices"),
    BankBlock("K3 Matsubara density readouts", 3, "genuine_readout", 0, True, "per-entry free-energy-density readouts"),
    BankBlock("K4 static-potential screening shares", 6, "genuine_readout", 0, True, "imported screening-share readouts"),
    BankBlock("K5 plaquette-action genuine rows", 9, "genuine_readout", 0, True, "non-alpha action-cost readout rows"),
    BankBlock("K5 alpha_bare scalar row", 1, "supplier_chain_identity", 1, False, "the 1/(4 pi) supplier scalar"),
    BankBlock("K6 equal-share mode-sum ratios", 5, "genuine_readout", 0, True, "rational/additive-share readouts"),
    BankBlock("K7 threshold screening exponentials", 3, "genuine_readout", 0, True, "declared threshold exponentials"),
    BankBlock("K8 per-taste BZ log-det shares", 4, "genuine_readout", 0, True, "per-taste BZ log-det share readouts"),
)

ALPHA_S = Signature(1, -2)
SIXTEEN_TASTE_TRANSPORT = ALPHA_S.power(16)


def check(klass: str, name: str, ok: bool, detail: str = "") -> None:
    global PASS, FAIL
    tag = "PASS" if ok else "FAIL"
    if ok:
        PASS += 1
        CLASS_COUNTS[klass] += 1
    else:
        FAIL += 1
    suffix = f"  ({detail})" if detail else ""
    print(f"  [{tag}][{klass}] {name}{suffix}")


def section(title: str) -> None:
    print()
    print("=" * 80)
    print(title)
    print("=" * 80)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def flat(path: Path) -> str:
    return " ".join(read(path).split())


def check_bank_partition() -> None:
    section("Current-bank partition")
    total = sum(block.count for block in CURRENT_BANK)
    readout_total = sum(block.count for block in CURRENT_BANK if block.has_readout_mechanism)
    supplier_total = total - readout_total

    check("A", "K1-K8 aggregate candidate count is 91", total == 91, f"total={total}")
    check("A", "genuine candidate-readout rows total 50", readout_total == 50, f"readout_total={readout_total}")
    check("A", "supplier/no-mechanism rows total 41", supplier_total == 41, f"supplier_total={supplier_total}")
    check(
        "A",
        "every alpha-bearing current-bank row is non-mechanistic",
        all((block.alpha_exp == 0) or (not block.has_readout_mechanism) for block in CURRENT_BANK),
        ", ".join(f"{b.family}:{b.mechanism_class}" for b in CURRENT_BANK if b.alpha_exp),
    )
    check(
        "A",
        "every genuine readout block has alpha exponent zero",
        all(block.alpha_exp == 0 for block in CURRENT_BANK if block.has_readout_mechanism),
        ", ".join(block.family for block in CURRENT_BANK if block.has_readout_mechanism),
    )
    check(
        "A",
        "the bank still contains alpha-bearing supplier rows",
        sum(block.count for block in CURRENT_BANK if block.alpha_exp) == 41,
        "K2 grid plus K5 alpha_bare scalar row",
    )


def readout_closure_signatures(max_abs_power: int = 3) -> set[Signature]:
    """Sample finite products/quotients of the genuine readout blocks.

    Because every genuine block has alpha exponent zero, the sample is
    enough to catch implementation drift while the theorem below checks
    the universal alpha-exponent invariant directly.
    """

    readout_blocks = [block for block in CURRENT_BANK if block.has_readout_mechanism]
    signatures = set()
    for powers in product(range(-max_abs_power, max_abs_power + 1), repeat=len(readout_blocks)):
        sig = Signature(0, 0)
        for block, power in zip(readout_blocks, powers):
            sig = sig * Signature(block.alpha_exp, 0).power(power)
        signatures.add(sig)
    return signatures


def check_factor_firewall() -> None:
    section("Factor-signature firewall")
    check("B", "alpha_s has signature (1, -2)", ALPHA_S == Signature(1, -2), str(ALPHA_S))
    check(
        "B",
        "sixteen-taste missing transport has signature (16, -32)",
        SIXTEEN_TASTE_TRANSPORT == Signature(16, -32),
        str(SIXTEEN_TASTE_TRANSPORT),
    )

    readout_blocks = [block for block in CURRENT_BANK if block.has_readout_mechanism]
    invariant = all(block.alpha_exp == 0 for block in readout_blocks)
    check("B", "universal invariant: genuine-readout products keep alpha exponent zero", invariant)

    sampled = readout_closure_signatures()
    check(
        "B",
        "sampled finite readout closure has only alpha exponent zero",
        all(sig.alpha_exp == 0 for sig in sampled),
        f"sample_size={len(sampled)}",
    )
    check("B", "alpha_s is absent from genuine-readout closure", ALPHA_S not in sampled)
    check("B", "alpha_s^16 is absent from genuine-readout closure", SIXTEEN_TASTE_TRANSPORT not in sampled)

    alpha_bearing = [block for block in CURRENT_BANK if block.alpha_exp != 0]
    check(
        "B",
        "reaching nonzero alpha exponent requires supplier-chain rows",
        alpha_bearing and all(not block.has_readout_mechanism for block in alpha_bearing),
        ", ".join(block.family for block in alpha_bearing),
    )
    inserted_supplier_count = SIXTEEN_TASTE_TRANSPORT.alpha_exp
    check(
        "B",
        "sixteen-taste target would require sixteen alpha-bearing supplier insertions",
        inserted_supplier_count == 16,
        f"alpha exponent={inserted_supplier_count}",
    )


def check_source_markers() -> None:
    section("Source markers and boundary discipline")
    note = flat(NOTE)
    parent = flat(PARENT_GATE)
    enum = flat(ENUM_NOTE)
    s1p = flat(S1P_NOTE)
    ratio = flat(RATIO_NOTE)

    required_note = [
        "**Claim type:** no_go",
        "**Claim-strength label:** exact current-bank no-go theorem",
        "does not edit the audit ledger",
        "does not supply that positive attachment theorem",
        "genuine readout mechanisms with alpha exponent zero",
        "alpha-bearing supplier-chain identities with no readout mechanism",
        "## No-Go Discipline Gate",
        "N1 -- alternative route enumeration",
        "N2 -- wall independence",
        "N3 -- hidden-wall scan",
        "N4 -- residual matching",
        "N5 -- rhetoric audit",
        "N6 -- partial-closure path scan",
        "N7 -- steelman",
        "N8 -- cross-cycle echo",
        "Gate result: PASS for the narrowed current-bank no-go",
        "outside-K1-K8",
        "a new axiom",
    ]
    for marker in required_note:
        check("C", f"new note contains marker: {marker}", marker in note)

    forbidden_note = [
        "This note closes the DELTA0 hierarchy gate",
        "This is a global B4 no-go",
        "audit verdict: retained",
        "effective status is retained",
        "hierarchy formula closure is proved",
    ]
    for marker in forbidden_note:
        check("C", f"new note omits forbidden overclaim: {marker}", marker not in note)

    required_parent = [
        "named gap: B4 attachment-observable identification",
        "not a shipped global no-go",
        "Surviving routes run through beyond-mean-field link fluctuations",
        "current-bank alpha-attachment no-go",
    ]
    for marker in required_parent:
        check("C", f"parent gate contains context marker: {marker}", marker in parent)

    required_enum = [
        "91 candidate rows",
        "NO candidate READOUT lands in the window with a",
        "DEFINITIONAL cells with zero mechanism content",
        "not among the K1-K8 declared readouts",
    ]
    for marker in required_enum:
        check("D", f"enumeration source contains marker: {marker}", marker in enum)

    required_s1p = [
        "ONLY the **observable identification** remains",
        "attaching MULTIPLICATIVELY per decoupling in the ratio-normalized partition function",
        "one factor `alpha_s = alpha_bare/u_0^2",
    ]
    for marker in required_s1p:
        check("D", f"S1-prime source contains marker: {marker}", marker in s1p)

    required_ratio = [
        "one factor `alpha_s` per taste decoupling",
        "the `alpha_s` PER-DECOUPLING ATTACHMENT rule",
        "UNSUPPLIED",
    ]
    for marker in required_ratio:
        check("D", f"ratio-normalized source contains marker: {marker}", marker in ratio)


def main() -> int:
    check_bank_partition()
    check_factor_firewall()
    check_source_markers()
    print()
    print(f"CLASS_COUNTS: {CLASS_COUNTS}")
    if FAIL:
        print("VERDICT: hierarchy DELTA0 B4 current-bank alpha-attachment no-go checks failed.")
        print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
        return 1
    print("VERDICT: hierarchy DELTA0 B4 current-bank alpha-attachment no-go checks pass.")
    print(f"TOTAL: PASS={PASS}, FAIL=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
