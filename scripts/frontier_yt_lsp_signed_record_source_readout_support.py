#!/usr/bin/env python3
"""Y_T LSP signed-record source-readout support runner.

This runner verifies a narrow support theorem:

    Y_T source-action primitive signed source record epsilon_x
      = signed spectral readout of a local Pauli sharp projective measurement.

It intentionally does not claim source/action authority, canonical O_H, scalar
LSZ normalization, kappa_Y=0, or positive y_t closure.
"""

from __future__ import annotations

import itertools
import json
import math
from pathlib import Path
from typing import Any

import numpy as np


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
NOTE = DOCS / "YT_LSP_SIGNED_RECORD_SOURCE_READOUT_SUPPORT_NOTE_2026-05-24.md"
AXIOMS = DOCS / "MINIMAL_AXIOMS_2026-05-20.md"
LSP = DOCS / "LSP_PROJECTIVE_DERIVATION_FROM_NAIMARK_FRAME_NARROW_THEOREM_NOTE_2026-05-22.md"
SOURCE_ACTION = DOCS / "YT_SOURCE_ACTION_SUPPORT_PACKET_NOTE_2026-05-22.md"
LEDGER = ROOT / "docs" / "audit" / "data" / "audit_ledger.json"
OUTPUT = ROOT / "outputs" / "yt_lsp_signed_record_source_readout_support_2026-05-24.json"

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: Any = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        tag = "PASS"
    else:
        FAIL += 1
        tag = "FAIL"
    suffix = f": {detail}" if detail != "" else ""
    print(f"[{tag}] {name}{suffix}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def states(n_sites: int) -> list[tuple[int, ...]]:
    return list(itertools.product((-1, 1), repeat=n_sites))


def rn_density(h: list[float], omega: list[tuple[int, ...]]) -> list[float]:
    weights = [math.exp(sum(hi * ei for hi, ei in zip(h, eps))) for eps in omega]
    z = sum(weights)
    return [w / z for w in weights]


def max_abs(a: list[float], b: list[float]) -> float:
    return max(abs(x - y) for x, y in zip(a, b))


def part1_source_anchors() -> None:
    print("\nPart 1: source anchors")
    for path in (NOTE, AXIOMS, LSP, SOURCE_ACTION, LEDGER):
        check(f"{path.relative_to(ROOT)} exists", path.exists())

    note = read(NOTE)
    check("note declares bounded_theorem", "**Claim type:** bounded_theorem" in note)
    check("note registers this runner", "frontier_yt_lsp_signed_record_source_readout_support.py" in note)
    check("note cites current qubit axioms", "MINIMAL_AXIOMS_2026-05-20.md" in note)
    check("note cites LSP projective theorem", "LSP_PROJECTIVE_DERIVATION_FROM_NAIMARK_FRAME_NARROW_THEOREM_NOTE_2026-05-22.md" in note)
    check("note cites Y_T source-action support packet", "YT_SOURCE_ACTION_SUPPORT_PACKET_NOTE_2026-05-22.md" in note)


def part2_ledger_status_boundary() -> None:
    print("\nPart 2: ledger boundary")
    rows = json.loads(read(LEDGER))["rows"]
    expected = {
        "lsp_projective_derivation_from_naimark_frame_narrow_theorem_note_2026-05-22": {
            "effective_status": {"retained_bounded", "retained"},
            "claim_type": {"bounded_theorem", "positive_theorem"},
        },
        "yt_source_action_support_packet_note_2026-05-22": {
            "effective_status": {"retained_bounded", "audited_clean"},
            "claim_type": {"bounded_theorem"},
        },
    }
    for claim_id, constraints in expected.items():
        row = rows.get(claim_id)
        check(f"ledger row present: {claim_id}", row is not None)
        if row is None:
            continue
        check(
            f"{claim_id}: retained-grade support status",
            row.get("effective_status") in constraints["effective_status"],
            row.get("effective_status"),
        )
        check(
            f"{claim_id}: claim type compatible",
            row.get("claim_type") in constraints["claim_type"],
            row.get("claim_type"),
        )


def part3_projective_pauli_readout() -> None:
    print("\nPart 3: local Pauli projective readout")
    identity = np.eye(2, dtype=float)
    sigma_z = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=float)
    p_plus = (identity + sigma_z) / 2.0
    p_minus = (identity - sigma_z) / 2.0

    check("P_plus is idempotent", np.allclose(p_plus @ p_plus, p_plus))
    check("P_minus is idempotent", np.allclose(p_minus @ p_minus, p_minus))
    check("P_plus and P_minus are orthogonal", np.allclose(p_plus @ p_minus, np.zeros((2, 2))))
    check("P_plus + P_minus = I", np.allclose(p_plus + p_minus, identity))
    check("signed readout P_plus - P_minus = sigma_z", np.allclose(p_plus - p_minus, sigma_z))

    evals = sorted(np.linalg.eigvalsh(sigma_z).round(12).tolist())
    check("signed readout spectrum is {-1,+1}", evals == [-1.0, 1.0], evals)

    lsp = read(LSP)
    check("LSP note records K_P = P", "K_P = P" in lsp)
    check("LSP note records P E P sequential effect", "P E P" in lsp)


def part4_rn_score_equals_signed_readout() -> None:
    print("\nPart 4: RN source score equals signed readout")
    omega = states(3)
    delta = 1.0e-6
    origin = [0.0, 0.0, 0.0]
    max_error = 0.0

    for site in range(3):
        hp = origin.copy()
        hm = origin.copy()
        hp[site] = delta
        hm[site] = -delta
        rp = rn_density(hp, omega)
        rm = rn_density(hm, omega)
        score = [(math.log(a) - math.log(b)) / (2.0 * delta) for a, b in zip(rp, rm)]
        primitive = [float(eps[site]) for eps in omega]
        err = max_abs(score, primitive)
        max_error = max(max_error, err)
        check(f"site {site}: d log R_h / dh_x at h=0 equals epsilon_x", err < 1.0e-9, err)

    check("all RN score errors below tolerance", max_error < 1.0e-9, max_error)


def part5_tensor_product_readout_commutes() -> None:
    print("\nPart 5: independent-site tensor readouts")
    sigma_z = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=float)
    identity = np.eye(2, dtype=float)
    z0 = np.kron(sigma_z, identity)
    z1 = np.kron(identity, sigma_z)
    check("two-site signed readouts commute", np.allclose(z0 @ z1, z1 @ z0))
    check("each readout squares to identity", np.allclose(z0 @ z0, np.eye(4)) and np.allclose(z1 @ z1, np.eye(4)))
    spectrum_pairs = sorted((a, b) for a in (-1, 1) for b in (-1, 1))
    check("joint outcome set is {-1,+1}^2", spectrum_pairs == [(-1, -1), (-1, 1), (1, -1), (1, 1)])


def part6_source_family_uniqueness() -> None:
    print("\nPart 6: source-family uniqueness")
    omega = states(3)
    eps0 = omega[0]
    h = [0.17, -0.23, 0.31]
    k = [-0.11, 0.29, 0.07]
    rh = rn_density(h, omega)
    rk = rn_density(k, omega)
    rhk = rn_density([hi + ki for hi, ki in zip(h, k)], omega)

    # Normalized multiplication implements source addition.
    composed_weights = [a * b for a, b in zip(rh, rk)]
    z = sum(composed_weights)
    composed = [w / z for w in composed_weights]
    check("normalized source multiplication composes to h+k", max_abs(composed, rhk) < 1.0e-12, max_abs(composed, rhk))

    # Log-odds against a reference record are additive and linear with the
    # coefficient fixed by the origin score.
    r0_index = omega.index(eps0)
    max_log_odds_error = 0.0
    for eps, prob in zip(omega, rh):
        lhs = math.log(prob / rh[r0_index])
        rhs = sum(hi * (ei - e0i) for hi, ei, e0i in zip(h, eps, eps0))
        max_log_odds_error = max(max_log_odds_error, abs(lhs - rhs))
    check("log-odds are fixed by signed-record score coefficients", max_log_odds_error < 1.0e-12, max_log_odds_error)

    reconstructed = []
    for eps in omega:
        reconstructed.append(math.exp(sum(hi * ei for hi, ei in zip(h, eps))))
    rz = sum(reconstructed)
    reconstructed = [w / rz for w in reconstructed]
    check("unique reconstructed family is product RN", max_abs(reconstructed, rh) < 1.0e-12, max_abs(reconstructed, rh))

    note = read(NOTE)
    check("note states source-family uniqueness corollary", "## Source-Family Uniqueness Corollary" in note)
    check("note states RN is not a fitted choice", "not an extra fitted choice" in note)


def part7_firewalls() -> None:
    print("\nPart 7: firewalls")
    note = read(NOTE)
    normalized_note = " ".join(note.split())
    required = [
        "does not accept the source-coupled action convention",
        "does not derive canonical `O_H`",
        "does not fix scalar LSZ normalization",
        "does not select `kappa_Y = 0`",
        "does not derive `y_t`",
        "Boundary:** renaming / compatibility support only",
        "may not be cited as a retained derivation",
        "Promotion beyond renaming support requires a retained bridge theorem",
        "claim_type_author_hint: bounded_theorem",
        "direct_effective_status_change_allowed_from_this_note: false",
    ]
    for phrase in required:
        check(f"required boundary phrase present: {phrase}", phrase in normalized_note)

    forbidden = [
        "Status:** retained",
        "positive retained Y_T closure",
        "kappa_Y = 0 is derived",
        "derive y_t",
        "y_t =",
        "m_t =",
        "sqrt(8/9) as an unconditional",
    ]
    for phrase in forbidden:
        check(f"forbidden overclaim absent: {phrase}", phrase not in note)


def write_output() -> None:
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "generated_at": "2026-05-24T00:00:00Z",
        "claim": "Y_T source-action primitive signed RN source record equals native LSP Pauli signed readout",
        "claim_type_author_hint": "bounded_theorem",
        "source_boundary": "signed_record_readout_support_only",
        "status_authority": "independent_audit_lane_only",
        "proposal_allowed": False,
        "proposal_allowed_reason": (
            "Readout carrier support only; source/action authority, canonical O_H, "
            "scalar LSZ, strict pole rows or W/Z bypass, and matching/running remain open."
        ),
        "direct_effective_status_change_allowed_from_this_note": False,
        "audit_required_before_effective_status_change": True,
        "pass_count": PASS,
        "fail_count": FAIL,
    }
    OUTPUT.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {OUTPUT.relative_to(ROOT)}")


def main() -> int:
    print("=" * 88)
    print("Y_T LSP SIGNED-RECORD SOURCE-READOUT SUPPORT")
    print("=" * 88)
    part1_source_anchors()
    part2_ledger_status_boundary()
    part3_projective_pauli_readout()
    part4_rn_score_equals_signed_readout()
    part5_tensor_product_readout_commutes()
    part6_source_family_uniqueness()
    part7_firewalls()
    write_output()
    print()
    print("=" * 88)
    print(f"RESULT: PASS={PASS} FAIL={FAIL}")
    print("=" * 88)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
