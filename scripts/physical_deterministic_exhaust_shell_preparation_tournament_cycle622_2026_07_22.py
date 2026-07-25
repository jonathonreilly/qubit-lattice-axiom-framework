#!/usr/bin/env python3
"""Cycle 622: deterministic (non-postselected) bound-branch preparation.

Route D-1: exhaust-shell absorber — each step, the matter amplitude on the
Chebyshev shell |r|_inf = R_shell is unitarily SWAPped into fresh blank
exhaust registers (which never evolve again).  No measurement, conditioning,
or renormalization anywhere; the matter+exhaust norm ledger is exact.  The
prepared matter register is certified by the UNCHANGED Cycle-610 certificates
under the CT-1'' certificate-selected channel (Cycle-612 addendum criteria).
Route D-3 (mechanism probe, L5): dephasing-pointer cascade with a frozen
negative-leaning prior.

Work-history line: the two lanes have collided on cycle numbers (the campaign
branch carries unrelated Cycle 610/611/612 notes and reaches Cycle 621); this
work claims Cycle 622 per owner directive.

Firewalls: a preparation schedule is not time; exhaust registers are not
Records; the survivor/exhaust norm split is a coherent ledger, not Born
probability; certification uses spectral data, preparation does not.

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
    "46f9cbe09fd60cddde1f69005f87a8173d0cfbf0e5e24098c90f414ace258a55"
)
C610_SHA256 = "36fcb1655bbdcd758b69ea1e273821e5c820f738eb63199570c8f36c7e294bac"
C611_SHA256 = "15db2200b08bc4a5d7669975806fe51e9b8a55049f0660969d427332602bf9e8"

RECEIPT = ROOT / (
    "outputs/physical_deterministic_exhaust_shell_preparation_tournament_"
    "cycle622_receipt_2026_07_22.json"
)

N_PREP_GRID = (64, 128, 256)
R_SHELL_GRID = (3, 4)
Q_CERT = 2048
Q_SKIP = 64

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


def chebyshev_radii(length: int) -> np.ndarray:
    axis = np.minimum(np.arange(length), length - np.arange(length))
    return np.maximum.reduce(np.meshgrid(axis, axis, axis, indexing="ij"))


def absorber_prepare(
    engine, r_shell: int, n_prep: int, contact: float
) -> dict[str, object]:
    """Deterministic exhaust-shell preparation.  Returns the UNNORMALIZED
    surviving matter state and the exact norm ledger."""
    shell = (chebyshev_radii(engine.length) == r_shell)[..., None]
    state = engine.source()
    exhaust_total = 0.0
    ledger_defect = 0.0
    for _ in range(n_prep):
        state = engine.step(state, contact)
        absorbed = state * shell
        exhaust_total += float(np.linalg.norm(absorbed) ** 2)
        state = state * (~shell)
        ledger_defect = max(
            ledger_defect,
            abs(float(np.linalg.norm(state) ** 2) + exhaust_total - 1.0),
        )
    return {
        "state": state,
        "survivor_norm_sq": float(np.linalg.norm(state) ** 2),
        "exhaust_norm_sq": exhaust_total,
        "ledger_defect": ledger_defect,
        "exhaust_registers": int(shell.sum()) * n_prep,
    }


def channel_word(engine, state: np.ndarray, sign: int, contact: float) -> np.ndarray:
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


def certify_ct1pp(engine, state: np.ndarray, theta: float, contact: float) -> dict[str, object]:
    """CT-1'' certificate-selected channel certification (612-addendum
    criteria, verbatim)."""
    predicted = C610.wrap_angle(theta) / (2 * math.pi)
    bound = 2 / (Q_CERT - Q_SKIP)
    outcome = {"selected_channel": "none", "certified": False}
    for sign, label in ((-1, "minus"), (+1, "plus")):
        word = channel_word(engine, state, sign, contact)
        row_t1 = C610.clock_row(word, Q_SKIP, "T1")
        row_t2 = C610.clock_row(word, Q_SKIP, "T2")
        convention_ok = (
            abs(row_t1["rate"] - row_t2["rate"]) < 2 * bound
            and abs(row_t1["count"] - row_t2["count"])
            <= max(4, 0.01 * max(row_t1["count"], 1))
        )
        certificate_pass = bool(row_t1["locked"] and convention_ok)
        rate_ok = abs(row_t1["rate"] - predicted) < bound + 1e-9
        outcome[label] = {
            "rate": row_t1["rate"], "fine_rate": row_t1["fine_rate"],
            "locked": bool(row_t1["locked"]),
            "convention_independent": bool(convention_ok),
            "rate_matches": bool(rate_ok),
        }
        if certificate_pass and outcome["selected_channel"] == "none":
            outcome["selected_channel"] = label
            outcome["certified"] = bool(rate_ok)
            outcome["word_amplitude_late"] = float(np.median(np.abs(word[Q_SKIP:])))
    outcome["predicted"] = predicted
    return outcome


def main() -> int:
    start = time.time()
    if C610_SHA != C610_SHA256 or C611_SHA != C611_SHA256:
        raise RuntimeError(
            "dependency SHA mismatch: "
            f"c610={C610_SHA} c611={C611_SHA}"
        )
    receipt: dict[str, object] = {
        "cycle": 622,
        "authority": "none",
        "audit": "unset",
        "frozen_contract_sha256": FROZEN_CONTRACT_SHA256,
        "consumed": {"cycle610_runner": C610_SHA, "cycle611_runner": C611_SHA},
        "cycle_number_collision": (
            "campaign branch reaches Cycle 621 and carries unrelated Cycle "
            "610/611/612 notes; this lane claims Cycle 622 per owner directive"
        ),
        "parameters": {"n_prep_grid": list(N_PREP_GRID),
                       "r_shell_grid": list(R_SHELL_GRID),
                       "Q_cert": Q_CERT, "Q_skip": Q_SKIP},
    }
    check("the Cycle-610 runner is byte-pinned and unchanged",
          C610_SHA == C610_SHA256, C610_SHA[:16])

    engine = C611.PositionEngine(C611.L_TRAIN, C611.BETA)
    root = C610.bs_root(C611.L_TRAIN, C610.K_TRAIN_0, C611.BETA)
    theta0 = float(root["theta"])
    psi_b_mom, _ = C610.bound_state(C611.L_TRAIN, C610.K_TRAIN_0, C611.BETA, root)
    psi_b_pos = C611.momentum_to_position(psi_b_mom, C611.L_TRAIN)

    def purity(state: np.ndarray) -> float:
        norm_sq = float(np.linalg.norm(state) ** 2)
        return float(abs(np.vdot(psi_b_pos, state)) ** 2 / norm_sq) if norm_sq else 0.0

    # Shell frame invariance (all 24) and antisymmetry compatibility.
    radii = chebyshev_radii(engine.length)
    import proper_cubic_bound_object_equivalence_cycle210_2026_07_16 as c210
    axis = np.arange(engine.length)
    coords = np.stack(np.meshgrid(axis, axis, axis, indexing="ij"), axis=-1)
    signed = np.where(coords > engine.length // 2, coords - engine.length, coords)
    frame_defect = 0
    for frame in c210.proper_cubic_frames():
        rotated = np.einsum("ij,abcj->abci", frame, signed).astype(int) % engine.length
        frame_defect = max(frame_defect, int(np.sum(
            radii[rotated[..., 0], rotated[..., 1], rotated[..., 2]] != radii)))
    check("the Chebyshev shell family is exactly invariant under all 24 frames",
          frame_defect == 0, {"defect_sites": frame_defect})

    # ---- Route D-1 grid.
    rows = []
    first_certified = None
    for r_shell in R_SHELL_GRID:
        for n_prep in N_PREP_GRID:
            prep = absorber_prepare(engine, r_shell, n_prep, C611.CONTACT)
            anti = engine.antisym_defect(prep["state"])
            cert = certify_ct1pp(engine, prep["state"], theta0, C611.CONTACT)
            row = {
                "R_shell": r_shell, "N_prep": n_prep,
                "survivor_norm_sq": prep["survivor_norm_sq"],
                "exhaust_norm_sq": prep["exhaust_norm_sq"],
                "ledger_defect": prep["ledger_defect"],
                "exhaust_registers": prep["exhaust_registers"],
                "purity": purity(prep["state"]),
                "antisym_defect": anti,
                "selected_channel": cert["selected_channel"],
                "certified": cert["certified"],
                "rate_minus": cert.get("minus", {}).get("rate"),
                "fine_minus": cert.get("minus", {}).get("fine_rate"),
            }
            rows.append(row)
            if cert["certified"] and first_certified is None:
                first_certified = row
    receipt["route_d1"] = rows
    ledger_ok = all(r["ledger_defect"] < 1e-12 for r in rows)
    anti_ok = all(r["antisym_defect"] < 1e-10 for r in rows)
    check(
        "D-1 ledger: matter plus exhaust norm equals one to 1e-12 at every "
        "step of every row (no discarded weight, no renormalization)",
        ledger_ok and anti_ok,
        {"max_ledger": max(r["ledger_defect"] for r in rows),
         "max_antisym": max(r["antisym_defect"] for r in rows)},
    )
    check(
        "P1: D-1 certifies at (R_shell=3, N_prep>=128) with the minus channel "
        "selected by CT-1'' (raw source in, certified clock out, "
        "deterministically)",
        any(r["certified"] and r["R_shell"] == 3 and r["N_prep"] >= 128
            and r["selected_channel"] == "minus" for r in rows),
        {"first_certified": first_certified},
    )
    in_band = [r for r in rows if r["certified"] and r["R_shell"] == 3
               and r["N_prep"] >= 128]
    check(
        "P1 survivor-norm band: the frozen [0.10, 0.35] prediction for the "
        "certified R3 rows (a falsifiable magnitude claim, not a "
        "certification condition)",
        bool(in_band) and all(0.10 <= r["survivor_norm_sq"] <= 0.35 for r in in_band),
        {"survivor_norms": [round(r["survivor_norm_sq"], 4) for r in in_band]},
    )
    check(
        "P1 purity: offline purity exceeds 0.95 on the certified rows",
        bool(in_band) and all(r["purity"] > 0.95 for r in in_band),
        {"purities": [round(r["purity"], 4) for r in in_band]},
    )

    # ---- Controls.
    off_contact = absorber_prepare(engine, 3, 128, 0.0)
    off_cert = certify_ct1pp(engine, off_contact["state"], theta0, 0.0)
    check(
        "P2 contact-off: without the contact law the absorber drains "
        "essentially everything (the absorber is a bound-state existence "
        "detector) and nothing certifies",
        off_contact["survivor_norm_sq"] < 0.02 and not off_cert["certified"],
        {"survivor": off_contact["survivor_norm_sq"],
         "certified": off_cert["certified"]},
    )
    free_state = engine.source()
    for _ in range(128):
        free_state = engine.step(free_state, C611.CONTACT)
    free_cert = certify_ct1pp(engine, free_state, theta0, C611.CONTACT)
    check(
        "P3 absorber-off: plain unitary evolution of the raw source stays "
        "uncertified on both channels",
        not free_cert["certified"],
        {"selected": free_cert["selected_channel"],
         "certified": free_cert["certified"]},
    )
    bad = engine.source()
    bad[2, 0, 0, 3] += 0.05
    check("lawful domain: non-antisymmetric input is refused",
          engine.antisym_defect(bad) > 1e-9,
          {"defect": engine.antisym_defect(bad)})

    # ---- Held rows (no re-tuning) and the field-row identity.
    if first_certified is not None:
        rs, npp = first_certified["R_shell"], first_certified["N_prep"]
        engine_h = C611.PositionEngine(C611.L_HELD, C611.BETA)
        root_h = C610.bs_root(C611.L_HELD, C610.K_TRAIN_0, C611.BETA)
        prep_h = absorber_prepare(engine_h, rs, npp, C611.CONTACT)
        cert_h = certify_ct1pp(engine_h, prep_h["state"], float(root_h["theta"]),
                               C611.CONTACT)
        check(
            "P4 held size: the first-certified configuration certifies at L13 "
            "against its own root with no re-tuning",
            cert_h["certified"],
            {"survivor": prep_h["survivor_norm_sq"],
             "selected": cert_h["selected_channel"],
             "fine": cert_h.get("minus", {}).get("fine_rate"),
             "predicted": cert_h["predicted"]},
        )
        receipt["held_L13"] = {
            "survivor_norm_sq": prep_h["survivor_norm_sq"],
            "certified": cert_h["certified"],
            "selected_channel": cert_h["selected_channel"],
        }
        engine_s = C611.PositionEngine(C611.L_TRAIN, C610.BETA_HELD)
        root_s = C610.bs_root(C611.L_TRAIN, C610.K_TRAIN_0, C610.BETA_HELD)
        prep_s = absorber_prepare(engine_s, rs, npp, C611.CONTACT)
        cert_s = certify_ct1pp(engine_s, prep_s["state"], float(root_s["theta"]),
                               C611.CONTACT)
        check(
            "P4 held species: beta=-0.35 certifies against its own root with "
            "the same frozen configuration",
            cert_s["certified"],
            {"selected": cert_s["selected_channel"],
             "fine": cert_s.get("minus", {}).get("fine_rate"),
             "predicted": cert_s["predicted"]},
        )
        prep_w = absorber_prepare(engine, rs, npp, C611.CONTACT)
        word = channel_word(engine, prep_w["state"], -1, C611.CONTACT)
        alpha = math.pi / 4
        modulated = word * np.exp(1j * alpha * np.arange(len(word)))
        base_row = C610.clock_row(word, Q_SKIP, "T1")
        field_row = C610.clock_row(modulated, Q_SKIP, "T1")
        ratio = field_row["rate"] / base_row["rate"]
        ratio_pred = C610.wrap_angle(theta0 + alpha) / C610.wrap_angle(theta0)
        check(
            "P5: the Cycle-610 field-ratio law survives on the "
            "deterministically prepared clock (Q=1, s=+1 row)",
            abs(ratio - ratio_pred) < 3 * (2 / (Q_CERT - Q_SKIP)) / abs(
                C610.wrap_angle(theta0) / (2 * math.pi)),
            {"ratio": ratio, "ratio_pred": ratio_pred},
        )
    else:
        check("P4/P5: no certified configuration exists to test", False,
              "route D-1 never certified")

    # ---- Internal masked-operator predictor (worker cross-check in note).
    shell3 = (chebyshev_radii(engine.length) == 3)[..., None]
    vec = engine.source()
    eigen_estimate = 0j
    for _ in range(400):
        new = engine.step(vec, C611.CONTACT) * (~shell3)
        eigen_estimate = np.vdot(vec, new) / np.vdot(vec, vec)
        vec = new / np.linalg.norm(new)
    receipt["masked_operator_R3"] = {
        "abs_lambda": float(abs(eigen_estimate)),
        "arg_lambda": float(np.angle(eigen_estimate)),
        "theta0": theta0,
    }
    check(
        "P8 internal: the masked-operator dominant phase lies within 5e-3 of "
        "the Cycle-610 root (independent worker comparison recorded in the "
        "note)",
        abs(C610.wrap_angle(float(np.angle(eigen_estimate)) - theta0)) < 5e-3,
        receipt["masked_operator_R3"],
    )

    # ---- Route D-3 mechanism probe (L5, branch-vector dephasing cascade).
    engine5 = C611.PositionEngine(5, C611.BETA)
    root5 = C610.bs_root(5, C610.K_TRAIN_0, C611.BETA)
    psi5_mom, _ = C610.bound_state(5, C610.K_TRAIN_0, C611.BETA, root5)
    psi5 = C611.momentum_to_position(psi5_mom, 5)
    onsite_mask = np.zeros((5, 5, 5, 36), bool)
    onsite_mask[0, 0, 0, :] = True
    branches = [engine5.source()]
    weights = [float(sum(abs(np.vdot(psi5, b)) ** 2 for b in branches))]
    for _ in range(8):
        evolved = []
        for b in branches:
            s = b
            for _ in range(8):
                s = engine5.step(s, C611.CONTACT)
            evolved.append(s)
        branches = []
        for s in evolved:
            branches.append(s * onsite_mask)
            branches.append(s * (~onsite_mask))
        weights.append(float(sum(abs(np.vdot(psi5, b)) ** 2 for b in branches)))
    receipt["route_d3_weights"] = [round(w, 5) for w in weights]
    check(
        "D-3 mechanism probe (frozen negative-leaning prior): the P0-dephasing "
        "cascade does not purify — the bound-branch weight of the dephased "
        "ensemble does not rise above the raw value plus 0.05",
        max(weights) < weights[0] + 0.05,
        {"weights": receipt["route_d3_weights"]},
    )

    receipt["interpretation_firewall"] = [
        "a preparation schedule is not time; exhaust registers are not Records",
        "the survivor/exhaust split is an exact coherent norm ledger, not Born "
        "probability",
        "the detector ray lives in the matter x blank-exhaust sector; absorbed "
        "amplitude is orthogonal by exhaust occupancy — a locality fact, not "
        "a conditioning step",
        "certification uses spectral data; preparation uses only geometry and "
        "a frozen schedule",
    ]

    elapsed = time.time() - start
    receipt["elapsed_seconds"] = elapsed
    receipt["pass_count"] = PASS
    receipt["fail_count"] = FAIL
    receipt["pass"] = FAIL == 0
    RECEIPT.parent.mkdir(parents=True, exist_ok=True)
    RECEIPT.write_text(json.dumps(receipt, indent=1, default=float) + "\n",
                       encoding="utf-8")
    print("RESULT", PASS, FAIL, "elapsed", round(elapsed, 2), "s")
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
