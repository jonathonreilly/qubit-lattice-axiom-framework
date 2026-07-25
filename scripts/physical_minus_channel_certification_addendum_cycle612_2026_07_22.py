#!/usr/bin/env python3
"""Cycle 612 addendum: minus-channel certification and the autonomous
channel-selection rule (frozen contract addendum 2).

The declared plus-sign aggregate suppresses this species' bound line by
|1 + e^{-i theta_b}|^2/2 = 0.0138 on mixed states; the minus channel enhances
it by 1.972/2.  These rows certify the Cycle-611 P-A state, the raw source,
and the exact bound eigenvector through the minus channel with raw rays, and
test the derived channel-selection rule CT-1'': keep the channel sign whose
word passes lock AND convention independence (local, spectral-data-free).

Authority: none.  Audit: unset.  Constitutional effect: none.
"""

from __future__ import annotations

import importlib.util
import json
import math
import sys
import time
from hashlib import sha256
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

FROZEN_CONTRACT_SHA256 = (
    "d45cad77c7d74df1951930ae796295fd8c405cc59d668f2fda98ca430b32cea1"
)
C610_SHA256 = "36fcb1655bbdcd758b69ea1e273821e5c820f738eb63199570c8f36c7e294bac"
C611_SHA256 = "15db2200b08bc4a5d7669975806fe51e9b8a55049f0660969d427332602bf9e8"
RECEIPT = ROOT / (
    "outputs/physical_minus_channel_certification_addendum_"
    "cycle612_receipt_2026_07_22.json"
)

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def load_module(name: str):
    path = ROOT / "scripts" / (name + ".py")
    digest = sha256(path.read_bytes()).hexdigest()
    spec = importlib.util.spec_from_file_location(name, path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)
    return module, digest


C610, C610_SHA = load_module(
    "physical_intrinsic_tick_event_relational_duration_tournament_cycle610_2026_07_22"
)
C611, C611_SHA = load_module(
    "physical_autonomous_bound_branch_preparation_tournament_cycle611_2026_07_22"
)

Q_CERT = 2048
Q_SKIP = 64


def channel_word(engine, state, sign: int, contact: float) -> np.ndarray:
    """Raw-ray two-channel word with channel weights (1, sign)/sqrt(2)."""
    bra = engine.source()
    u = np.empty(Q_CERT + 1, complex)
    current = state.copy()
    for q in range(Q_CERT + 1):
        u[q] = np.vdot(bra, current)
        if q < Q_CERT:
            current = engine.step(current, contact)
    word = np.empty(Q_CERT + 1, complex)
    word[0] = (u[0] + sign * np.conj(u[1])) / math.sqrt(2)
    word[1:] = (u[1:] + sign * u[:-1]) / math.sqrt(2)
    return word


def certify_word(word: np.ndarray, theta: float) -> dict[str, object]:
    row_t1 = C610.clock_row(word, Q_SKIP, "T1")
    row_t2 = C610.clock_row(word, Q_SKIP, "T2")
    predicted = C610.wrap_angle(theta) / (2 * math.pi)
    bound = 2 / (Q_CERT - Q_SKIP)
    convention_ok = (
        abs(row_t1["rate"] - row_t2["rate"]) < 2 * bound
        and abs(row_t1["count"] - row_t2["count"])
        <= max(4, 0.01 * max(row_t1["count"], 1))
    )
    return {
        "rate": row_t1["rate"], "rate_T2": row_t2["rate"],
        "fine_rate": row_t1["fine_rate"], "locked": bool(row_t1["locked"]),
        "convention_independent": bool(convention_ok),
        "rate_matches": bool(abs(row_t1["rate"] - predicted) < bound + 1e-9),
        "certified": bool(
            row_t1["locked"] and convention_ok
            and abs(row_t1["rate"] - predicted) < bound + 1e-9
        ),
        "predicted": predicted,
    }


def main() -> int:
    start = time.time()
    observed_dependencies = {
        "cycle610_runner": C610_SHA,
        "cycle611_runner": C611_SHA,
    }
    expected_dependencies = {
        "cycle610_runner": C610_SHA256,
        "cycle611_runner": C611_SHA256,
    }
    if observed_dependencies != expected_dependencies:
        raise RuntimeError(
            "byte-pinned predecessor mismatch: "
            f"observed={observed_dependencies!r}"
        )
    receipt: dict[str, object] = {
        "cycle": "612-addendum",
        "authority": "none",
        "audit": "unset",
        "frozen_contract_sha256": FROZEN_CONTRACT_SHA256,
        "consumed": observed_dependencies,
    }
    engine = C611.PositionEngine(C611.L_TRAIN, C611.BETA)
    root = C610.bs_root(C611.L_TRAIN, C610.K_TRAIN_0, C611.BETA)
    theta0 = float(root["theta"])
    suppression = abs(1 + np.exp(-1j * theta0)) ** 2 / 2
    enhancement = abs(1 - np.exp(-1j * theta0)) ** 2 / 2
    receipt["channel_factors"] = {
        "plus_bound_factor": float(suppression),
        "minus_bound_factor": float(enhancement),
    }
    check(
        "channel reweighting factors at this species: the plus aggregate "
        "suppresses the bound line (0.0138) and the minus channel enhances it "
        "(1.97)",
        suppression < 0.02 and enhancement > 1.9,
        receipt["channel_factors"],
    )

    pa_state, _ = C611.route_pa(engine, 16, 4)
    psi_b_mom, _ = C610.bound_state(C611.L_TRAIN, C610.K_TRAIN_0, C611.BETA, root)
    psi_b_pos = C611.momentum_to_position(psi_b_mom, C611.L_TRAIN)
    raw = engine.source()

    rows = {}
    for label, state in (("pa_state", pa_state), ("raw_source", raw),
                         ("bound_eigenvector", psi_b_pos)):
        for sign, sign_label in ((-1, "minus"), (+1, "plus")):
            word = channel_word(engine, state, sign, C611.CONTACT)
            rows[f"{label}_{sign_label}"] = certify_word(word, theta0)
    receipt["rows"] = rows

    check(
        "(a) the Cycle-611 P-A state certifies through the minus channel with "
        "raw rays (frozen prediction)",
        rows["pa_state_minus"]["certified"],
        rows["pa_state_minus"],
    )
    check(
        "(c) the exact bound eigenvector certifies through the minus channel",
        rows["bound_eigenvector_minus"]["certified"],
        rows["bound_eigenvector_minus"],
    )
    raw_minus = rows["raw_source_minus"]
    check(
        "(b) the raw onsite-A2 source remains uncertified through the minus "
        "channel, so preparation remains necessary",
        not raw_minus["certified"],
        raw_minus,
    )
    receipt["open_row_raw_minus_certified"] = bool(raw_minus["certified"])

    # (d) channel-selection rule CT-1'': certificates select the channel.
    selection = {}
    for label in ("pa_state", "raw_source", "bound_eigenvector"):
        minus_pass = rows[f"{label}_minus"]["locked"] and rows[
            f"{label}_minus"]["convention_independent"]
        plus_pass = rows[f"{label}_plus"]["locked"] and rows[
            f"{label}_plus"]["convention_independent"]
        if minus_pass and not plus_pass:
            selection[label] = "minus"
        elif plus_pass and not minus_pass:
            selection[label] = "plus"
        elif minus_pass and plus_pass:
            selection[label] = "both"
        else:
            selection[label] = "none"
    contact_off_word = channel_word(engine, raw, -1, 0.0)
    off_row = certify_word(contact_off_word, theta0)
    selection["contact_off"] = (
        "minus" if off_row["locked"] and off_row["convention_independent"]
        else "none"
    )
    receipt["channel_selection"] = selection
    check(
        "(d) the certificate-based selector uniquely picks minus for the P-A "
        "mixed state, picks neither for the raw source, permits both signs for "
        "the exact eigenvector, and the contact-off deletion fails "
        "certification",
        selection["pa_state"] == "minus"
        and selection["raw_source"] == "none"
        and selection["bound_eigenvector"] == "both"
        and not off_row["certified"],
        {"selection": selection, "contact_off_certified": off_row["certified"]},
    )

    receipt["interpretation_firewall"] = [
        "the channel sign is apparatus structure within the declared "
        "two-channel family, selected by the law's own certificates, not by "
        "spectral data",
        "a certified rate is a dimensionless relational candidate, not proper "
        "time, lapse, or energy",
        "the plus-channel falsification rows of Cycles 610-612 stand "
        "unchanged; this addendum refines the candidate law, it does not "
        "repair preregistered failures",
    ]

    elapsed = time.time() - start
    receipt["elapsed_seconds"] = elapsed
    receipt["pass_count"] = PASS
    receipt["fail_count"] = FAIL
    receipt["pass"] = FAIL == 0
    RECEIPT.parent.mkdir(parents=True, exist_ok=True)
    RECEIPT.write_text(
        json.dumps(receipt, indent=1, default=float) + "\n", encoding="utf-8"
    )
    print("RESULT", PASS, FAIL, "elapsed", round(elapsed, 2), "s")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
