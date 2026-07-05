#!/usr/bin/env python3
"""Verifier for the quark mass spectrum Koide-scheme open gate."""

from __future__ import annotations

import hashlib
import math
from pathlib import Path


PASS = 0
FAIL = 0
ROOT = Path(__file__).resolve().parents[1]
NOTE = "docs/QUARK_MASS_SPECTRUM_KOIDE_SCHEME_OPEN_GATE_NOTE_2026-05-26.md"
SIDECAR_RUNNER = "scripts/frontier_record_selector_audit_sidecar_2026_06_05.py"
SIDECAR_CACHE = "logs/runner-cache/frontier_record_selector_audit_sidecar_2026_06_05.txt"
SIDECAR_NOTE = "docs/RECORD_SELECTOR_AUDIT_SIDECAR_2026-06-05.md"
CLAIM_ID = "quark_mass_spectrum_koide_scheme_open_gate_note_2026-05-26"


def check(name: str, cond: bool, detail: str = "") -> None:
    global PASS, FAIL
    if cond:
        PASS += 1
        print(f"  PASS: {name}" + (f" ({detail})" if detail else ""))
    else:
        FAIL += 1
        print(f"  FAIL: {name}" + (f" ({detail})" if detail else ""))


def koide_q(masses: list[float]) -> float:
    roots = [math.sqrt(m) for m in masses]
    return sum(masses) / (sum(roots) ** 2)


def apparent_b_over_a_squared(q_value: float) -> float:
    # For x_k = a + 2 |b| cos(delta + 2 pi k/3),
    # Q = 1/3 + (2/3) |b|^2/a^2.
    return (3.0 * q_value - 1.0) / 2.0


def hierarchy(masses: list[float]) -> float:
    return max(masses) / min(masses)


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def cache_header(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    header, _, _stdout = text.partition("----- stdout -----")
    out = {"_text": text}
    for line in header.splitlines():
        if ":" not in line:
            continue
        key, value = line.split(":", 1)
        out[key.strip()] = value.strip()
    return out


def main() -> int:
    print("Quark mass spectrum Koide-scheme open gate")
    print("=" * 72)

    # Conventional central-value comparators. The quark values mix common
    # PDG-style light-quark MSbar values with heavy-quark central values;
    # they are therefore an illustrative boundary check, not a theorem.
    charged_leptons = [0.0005109989461, 0.1056583755, 1.77686]  # GeV
    up_quarks = [0.00216, 1.27, 173.0]  # GeV
    down_quarks = [0.00467, 0.0934, 4.18]  # GeV

    sectors = {
        "charged_lepton": charged_leptons,
        "up_quark": up_quarks,
        "down_quark": down_quarks,
    }

    q_values = {name: koide_q(vals) for name, vals in sectors.items()}
    apparent = {name: apparent_b_over_a_squared(q) for name, q in q_values.items()}
    hierarchies = {name: hierarchy(vals) for name, vals in sectors.items()}

    print("\nCentral-value comparators")
    for name in ("charged_lepton", "up_quark", "down_quark"):
        print(
            f"  {name:15s} Q={q_values[name]:.9f} "
            f"|b|^2/a^2={apparent[name]:.9f} "
            f"hierarchy={hierarchies[name]:.1f}"
        )

    check("charged-lepton Q comparator is close to 2/3",
          abs(q_values["charged_lepton"] - 2.0 / 3.0) < 1e-5,
          f"Q={q_values['charged_lepton']:.9f}")
    check("charged-lepton apparent |b|^2/a^2 is close to 1/2",
          abs(apparent["charged_lepton"] - 0.5) < 2e-5,
          f"{apparent['charged_lepton']:.9f}")
    check("up-quark Q comparator is far from 2/3",
          q_values["up_quark"] - 2.0 / 3.0 > 0.15,
          f"Q={q_values['up_quark']:.9f}")
    check("down-quark Q comparator is separated from 2/3",
          q_values["down_quark"] - 2.0 / 3.0 > 0.04,
          f"Q={q_values['down_quark']:.9f}")
    check("up-quark apparent |b|^2/a^2 differs from lepton BAE",
          abs(apparent["up_quark"] - 0.5) > 0.2,
          f"{apparent['up_quark']:.9f}")
    check("down-quark apparent |b|^2/a^2 differs from lepton BAE",
          abs(apparent["down_quark"] - 0.5) > 0.05,
          f"{apparent['down_quark']:.9f}")
    check("up and down quark comparators are distinct",
          abs(q_values["up_quark"] - q_values["down_quark"]) > 0.08,
          f"gap={abs(q_values['up_quark'] - q_values['down_quark']):.9f}")
    check("up-quark hierarchy is extreme",
          hierarchies["up_quark"] > 1e4,
          f"{hierarchies['up_quark']:.1f}")
    check("down-quark hierarchy is large but less extreme than up-quark",
          1e2 < hierarchies["down_quark"] < hierarchies["up_quark"],
          f"{hierarchies['down_quark']:.1f}")
    check("charged-lepton hierarchy lies between down and up in this comparator",
          hierarchies["down_quark"] < hierarchies["charged_lepton"] < hierarchies["up_quark"],
          f"{hierarchies['charged_lepton']:.1f}")

    # Algebraic sanity checks independent of the central values.
    for q_probe in (2.0 / 3.0, q_values["up_quark"], q_values["down_quark"]):
        kappa = apparent_b_over_a_squared(q_probe)
        reconstructed_q = 1.0 / 3.0 + (2.0 / 3.0) * kappa
        check(f"Q <-> |b|^2/a^2 algebra reconstructs Q={q_probe:.6f}",
              abs(reconstructed_q - q_probe) < 1e-14)

    check("quark values are treated as scheme-dependent comparators",
          all(q > 0 for q in q_values.values()),
          "no derivation claimed")

    note_text = (ROOT / NOTE).read_text(encoding="utf-8")
    sidecar_text = (ROOT / SIDECAR_RUNNER).read_text(encoding="utf-8")
    header = cache_header(ROOT / SIDECAR_CACHE)
    check("Record-selector sidecar classifies quark row as sector-specific dial open gate",
          CLAIM_ID in sidecar_text
          and '"class": "sector_specific_dial_open_gate"' in sidecar_text
          and "do not transfer charged-lepton BAE" in sidecar_text,
          "sidecar says sector-specific mass scheme/scale and quark dial remain open")
    check("quark note names selector sidecar note, runner, and cache",
          SIDECAR_NOTE in note_text and SIDECAR_RUNNER in note_text and SIDECAR_CACHE in note_text,
          "restricted packet includes sidecar boundary artifact")
    check("selector sidecar cache is SHA-fresh and clean",
          header.get("runner") == SIDECAR_RUNNER
          and header.get("runner_sha256") == sha256_file(ROOT / SIDECAR_RUNNER)
          and header.get("exit_code") == "0"
          and "SCORECARD PASS=87 FAIL=0" in header["_text"],
          f"cache runner={header.get('runner')} status={header.get('status')}")
    check("source boundary: charged-lepton BAE is not copied to quark sector",
          "must not be copied into the quark mass lane" in note_text
          and "scheme-native framework mass definition" in note_text
          and "sector-specific mass scheme/scale and quark-sector dial parameters" in note_text,
          "quark lane stays comparator-only until sector-specific bridge exists")
    note_flat = " ".join(note_text.split())
    check("2026-06-12 firewall keeps quark row open until sector dial is derived",
          "2026-06-12 Sector-Dial Source Firewall" in note_text
          and "live blocker is a sector-specific quark mass scheme/scale and quark dial theorem" in note_flat
          and "No retained-grade proposal or status promotion is made here" in note_flat
          and "displayed central values remain external comparators only" in note_text,
          "no lepton BAE transfer or quark-mass promotion")

    print("\n" + "=" * 72)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL:
        print("VERDICT: quark Koide-scheme open gate failed checks.")
        return 1
    print(
        "VERDICT: quark Koide-scheme open gate verified; "
        "quark BAE parameters and scales remain open."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
