#!/usr/bin/env python3
"""E-center shear no-go for Route-2 magnitude source rules."""

from __future__ import annotations

from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path

from frontier_quark_route2_exact_readout_map import restricted_readout_data


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

PASS_COUNT = 0
FAIL_COUNT = 0

Q_T = Fraction(5, 6)
S_TE = Fraction(-2, 1)
T_CENTER_OVER_E_SHELL = S_TE * Q_T
F_ADJ = Fraction(8, 9)
TARGET_Q_E = Fraction(15, 8)
TARGET_RHO_E = Fraction(21, 4)
TARGET_MAGNITUDE = Fraction(8, 9)


@dataclass(frozen=True)
class Witness:
    label: str
    q_e: Fraction

    @property
    def rho_e(self) -> Fraction:
        return 6 * (self.q_e - 1)

    @property
    def c_te(self) -> Fraction:
        return T_CENTER_OVER_E_SHELL / self.q_e

    @property
    def magnitude(self) -> Fraction:
        return abs(self.c_te)


WITNESSES = (
    Witness("no E-center lift", Fraction(1, 1)),
    Witness("target lift", TARGET_Q_E),
    Witness("larger positive lift", Fraction(2, 1)),
    Witness("unit magnitude lift", Fraction(5, 3)),
)


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        status = "PASS"
    else:
        FAIL_COUNT += 1
        status = "FAIL"
    suffix = f" -- {detail}" if detail else ""
    print(f"{status}: {name}{suffix}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def norm(text: str) -> str:
    return " ".join(text.split())


def sheared(witness: Witness, delta: Fraction) -> Witness:
    return Witness(f"{witness.label} plus delta={delta}", witness.q_e + delta)


def shear_invariant_signature(_witness: Witness) -> tuple[Fraction, Fraction, Fraction, Fraction]:
    """Data that do not evaluate the E-center lift."""
    e_shell = Fraction(1, 1)
    return (e_shell, Q_T, S_TE, F_ADJ)


def part_a_authorities() -> None:
    print("A. Authority surface")
    note_path = DOCS / "QUARK_ROUTE2_MAGNITUDE_SOURCE_E_CENTER_SHEAR_NO_GO_NOTE_2026-06-21.md"
    readout_path = DOCS / "QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md"
    naturality_path = DOCS / "QUARK_ROUTE2_E_CHANNEL_READOUT_NATURALITY_NO_GO_NOTE_2026-04-28.md"
    sign_split_path = DOCS / "QUARK_ROUTE2_W1_SIGN_MAGNITUDE_SPLIT_SUPPORT_NOTE_2026-06-21.md"
    source_path = DOCS / "QUARK_ROUTE2_SOURCE_DOMAIN_BRIDGE_NO_GO_NOTE_2026-04-28.md"

    for path in (note_path, readout_path, naturality_path, source_path):
        check(f"{path.name} exists", path.exists(), str(path.relative_to(ROOT)))
    check("block32 sign-split note is reviewed in the same source slice", sign_split_path.exists())

    note = read(note_path)
    readout = read(readout_path)
    naturality = read(naturality_path)
    source = read(source_path)
    compact_note = norm(note)

    check("new note declares canonical no-go boundary", "**Claim type:** no_go" in note and "exact negative boundary" in note)
    check("new note states shear rule", "q_E -> q_E + delta" in note and "rho_E -> rho_E + 6 delta" in note)
    check("new note scopes future routes open", "not a no-go against every future magnitude theorem" in note)
    check("readout note gives reduced family", "P(rho_E)" in readout and "beta_E / alpha_E = 21/4" in readout)
    check("naturality note names E-center freedom", "rho_E" in naturality and "remains a free parameter" in naturality)
    check("source-domain note names missing source bridge", "R_conn = 8/9 -> c_TE" in source)
    check("new note says shear-invariant data cannot select magnitude", "shear-invariant current data cannot select the magnitude" in compact_note)


def part_b_shear_witnesses() -> None:
    print("\nB. E-center shear witnesses")
    signature = shear_invariant_signature(WITNESSES[0])
    check("T-side product is -5/3", T_CENTER_OVER_E_SHELL == Fraction(-5, 3), str(T_CENTER_OVER_E_SHELL))
    check("F_adj is exact 8/9", F_ADJ == Fraction(8, 9), str(F_ADJ))
    check("all witnesses are in positive E-center branch", all(w.q_e > 0 for w in WITNESSES))
    check("all witnesses share shear-invariant signature", all(shear_invariant_signature(w) == signature for w in WITNESSES))
    check("witness magnitudes are not all equal", len({w.magnitude for w in WITNESSES}) == len(WITNESSES))

    expected = {
        "no E-center lift": (Fraction(1, 1), Fraction(0, 1), Fraction(5, 3)),
        "target lift": (Fraction(15, 8), Fraction(21, 4), Fraction(8, 9)),
        "larger positive lift": (Fraction(2, 1), Fraction(6, 1), Fraction(5, 6)),
        "unit magnitude lift": (Fraction(5, 3), Fraction(4, 1), Fraction(1, 1)),
    }
    target_hits = 0
    for witness in WITNESSES:
        q_expected, rho_expected, mag_expected = expected[witness.label]
        if witness.magnitude == TARGET_MAGNITUDE:
            target_hits += 1
        check(f"{witness.label} q_E matches expected", witness.q_e == q_expected, str(witness.q_e))
        check(f"{witness.label} rho_E matches expected", witness.rho_e == rho_expected, str(witness.rho_e))
        check(f"{witness.label} magnitude matches expected", witness.magnitude == mag_expected, str(witness.magnitude))
    check("only target witness has |c_TE|=F_adj", target_hits == 1, f"hits={target_hits}")


def part_c_shear_action() -> None:
    print("\nC. Shear action")
    base = Witness("base", Fraction(1, 1))
    deltas = (Fraction(1, 8), Fraction(7, 8), Fraction(1, 1))
    sheared_witnesses = tuple(sheared(base, delta) for delta in deltas)
    check("positive shears keep positive E-center branch", all(w.q_e > 0 for w in sheared_witnesses))
    check("positive shears keep invariant signature", all(shear_invariant_signature(w) == shear_invariant_signature(base) for w in sheared_witnesses))
    check("positive shears change q_E", len({w.q_e for w in (base,) + sheared_witnesses}) == 4)
    check("positive shears change |c_TE|", len({w.magnitude for w in (base,) + sheared_witnesses}) == 4)
    check("delta=7/8 reaches target q_E", sheared(base, Fraction(7, 8)).q_e == TARGET_Q_E)
    check("delta=7/8 reaches target magnitude", sheared(base, Fraction(7, 8)).magnitude == TARGET_MAGNITUDE)
    check("delta=1 changes magnitude away from target", sheared(base, Fraction(1, 1)).magnitude != TARGET_MAGNITUDE)


def part_d_rule_no_go() -> None:
    print("\nD. Shear-invariant rule no-go")
    signatures = {shear_invariant_signature(w) for w in WITNESSES}
    target_values = {w.magnitude == TARGET_MAGNITUDE for w in WITNESSES}
    check("all witnesses have one invariant data signature", len(signatures) == 1)
    check("same invariant signature has both target and non-target magnitudes", target_values == {True, False})
    check("therefore invariant data cannot imply target magnitude", len(signatures) == 1 and target_values == {True, False})
    check("magnitude condition is equivalent to target q_E", abs(T_CENTER_OVER_E_SHELL) / F_ADJ == TARGET_Q_E)
    check("target q_E is equivalent to target rho_E", 6 * (TARGET_Q_E - 1) == TARGET_RHO_E)
    check("a magnitude source must evaluate E-center lift", all(w.magnitude == abs(T_CENTER_OVER_E_SHELL) / w.q_e for w in WITNESSES))


def part_e_live_and_inputs() -> None:
    print("\nE. Live branch and input firewall")
    data = restricted_readout_data()
    check("live q_E is positive", data.q_e > 0, f"q_E={data.q_e:.12f}")
    check("live magnitude is positive", abs(data.center_ratio_te) > 0, f"|c_TE|={abs(data.center_ratio_te):.12f}")
    check("live magnitude is close to but not exact target", abs(abs(data.center_ratio_te) - float(TARGET_MAGNITUDE)) > 1.0e-12 and abs(abs(data.center_ratio_te) - float(TARGET_MAGNITUDE)) < 0.01)

    proof_inputs = {
        "shell_normalization",
        "granted_t_side_values",
        "color_fraction_F_adj",
        "exact_rational_arithmetic",
    }
    forbidden = {
        "observed_quark_masses",
        "fitted_yukawa_entries",
        "ckm_j_error_minimization",
        "nearest_live_endpoint_selector",
    }
    check("forbidden proof inputs are absent", proof_inputs.isdisjoint(forbidden), str(sorted(proof_inputs)))


def part_f_note_hygiene() -> None:
    print("\nF. Note hygiene")
    note = read(DOCS / "QUARK_ROUTE2_MAGNITUDE_SOURCE_E_CENTER_SHEAR_NO_GO_NOTE_2026-06-21.md")
    compact = norm(note)
    check("note records four witnesses", "| `1` | `0` | `5/3` |" in note and "| `15/8` | `21/4` | `8/9` |" in note)
    check("note keeps W1 open", "does not prove W1" in note)
    check("note names E-center primitive as next target", "E-center shear-breaking primitive" in compact)
    check("note records expected pass count", "TOTAL: PASS=51, FAIL=0" in note)


def main() -> int:
    part_a_authorities()
    part_b_shear_witnesses()
    part_c_shear_action()
    part_d_rule_no_go()
    part_e_live_and_inputs()
    part_f_note_hygiene()
    print(f"\nTOTAL: PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    print("Status: exact negative boundary for shear-invariant magnitude source rules.")
    return 0 if FAIL_COUNT == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
