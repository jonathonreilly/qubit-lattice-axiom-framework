#!/usr/bin/env python3
"""Route-2 reciprocal-square dimension bridge packet.

Safe claim:
  The CKM inverse-square structural reading supplies the exact dimension
  components 1/N_pair^2=1/4 and 1/N_color^2=1/9.  Their ratio is 9/4, so a
  bridge identifying Route-2 lambda=q_E/q_T with that component ratio would
  close the exact endpoint target rho_E=21/4.

  The current bank does not supply that bridge.  This runner records the exact
  conditional support and the firewall: the CKM inverse-square reading is a
  CKM-side structural identity, not a Route-2 readout coefficient law.
"""

from __future__ import annotations

from fractions import Fraction as F
from pathlib import Path


PASS = 0
FAIL = 0


def check(label: str, cond: bool, detail: str = "") -> None:
    global PASS, FAIL
    ok = bool(cond)
    PASS += int(ok)
    FAIL += int(not ok)
    tag = "PASS" if ok else "FAIL"
    print(f"{tag}: {label}" + (f" -- {detail}" if detail else ""))


def read(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


def endpoint_from_lambda(lam: F) -> tuple[F, F, F]:
    q_t = F(5, 6)
    q_e = lam * q_t
    rho_e = 6 * (q_e - 1)
    c_te = -2 * q_t / q_e
    return q_e, rho_e, c_te


def main() -> int:
    print("=" * 88)
    print("ROUTE-2 RECIPROCAL-SQUARE DIMENSION BRIDGE PACKET")
    print("=" * 88)

    note = Path("docs/QUARK_ROUTE2_RECIPROCAL_SQUARE_DIMENSION_BRIDGE_PACKET_NOTE_2026-06-21.md")
    ckm_note = Path("docs/CKM_WOLFENSTEIN_ETA_INVERSE_SQUARE_GAP_THEOREM_NOTE_2026-04-26.md")
    ckm_runner = Path("scripts/frontier_ckm_wolfenstein_eta_inverse_square_gap.py")
    usable = Path("docs/publication/ci3_z3/USABLE_DERIVED_VALUES_INDEX.md")
    exact = Path("docs/QUARK_ROUTE2_EXACT_READOUT_MAP_NOTE_2026-04-19.md")
    covariance = Path("docs/QUARK_ROUTE2_QE_COVARIANCE_SCHUR_QUADRATIC_NO_GO_NARROW_NOTE_2026-06-14.md")
    parent = Path("docs/S3_TIME_THETA_TO_SLICE_COUPLING_NOTE.md")

    print("\nA. Authority surfaces")
    print("-" * 72)
    for label, path in (
        ("new note", note),
        ("CKM inverse-square note", ckm_note),
        ("CKM inverse-square runner", ckm_runner),
        ("usable values index", usable),
        ("Route-2 exact readout", exact),
        ("Route-2 covariance no-go", covariance),
        ("parent theta coupling", parent),
    ):
        check(f"{label} surface exists", path.exists(), str(path))

    n_pair = F(2)
    n_color = F(3)
    n_quark = n_pair * n_color
    inv_pair_sq = 1 / (n_pair * n_pair)
    inv_color_sq = 1 / (n_color * n_color)
    eta_sq = inv_pair_sq - inv_color_sq
    rho = 1 / n_quark
    a_sq = n_pair / n_color
    rho_a_sq = rho * a_sq
    w3 = eta_sq + rho_a_sq
    ratio = w3 / rho_a_sq

    print("\nB. CKM inverse-square components")
    print("-" * 72)
    check("N_pair=2 and N_color=3", (n_pair, n_color) == (F(2), F(3)))
    check("1/N_pair^2 is 1/4", inv_pair_sq == F(1, 4), f"1/N_pair^2={inv_pair_sq}")
    check("1/N_color^2 is 1/9", inv_color_sq == F(1, 9), f"1/N_color^2={inv_color_sq}")
    check("eta^2 inverse-square gap is 5/36", eta_sq == F(5, 36), f"eta^2={eta_sq}")
    check("rho A^2 component is 1/N_color^2", rho_a_sq == inv_color_sq, f"rho A^2={rho_a_sq}")
    check("eta^2 + rho A^2 is 1/N_pair^2", w3 == inv_pair_sq, f"W3={w3}")
    check("component ratio W3/W2 is 9/4", ratio == F(9, 4), f"(1/4)/(1/9)={ratio}")

    print("\nC. Conditional Route-2 endpoint closure")
    print("-" * 72)
    q_e, rho_e, c_te = endpoint_from_lambda(ratio)
    check("conditional lambda equals target 9/4", ratio == F(9, 4))
    check("conditional q_E is 15/8", q_e == F(15, 8), f"q_E={q_e}")
    check("conditional rho_E is 21/4", rho_e == F(21, 4), f"rho_E={rho_e}")
    check("conditional c_TE is -8/9", c_te == F(-8, 9), f"c_TE={c_te}")
    check("conditional readout triple would be (-1,-2,21/4)", (F(-1), F(-2), rho_e) == (F(-1), F(-2), F(21, 4)))

    print("\nD. Wrong-map falsifiers")
    print("-" * 72)
    for label, lam, expected_not_target in (
        ("gap-only eta^2", eta_sq, True),
        ("direct A^2", a_sq, True),
        ("color component alone", inv_color_sq, True),
        ("pair component alone", inv_pair_sq, True),
    ):
        q_bad, rho_bad, c_bad = endpoint_from_lambda(lam)
        check(
            f"{label} is not the Route-2 lambda target",
            (lam != F(9, 4)) == expected_not_target and rho_bad != F(21, 4),
            f"lambda={lam}, rho_E={rho_bad}, c_TE={c_bad}",
        )
    check("only the component ratio, not the gap itself, lands on 9/4", ratio == F(9, 4) and eta_sq != F(9, 4))

    print("\nE. Bridge firewall markers")
    print("-" * 72)
    note_text = read(str(note))
    ckm_text = read(str(ckm_note))
    usable_text = read(str(usable))
    exact_text = read(str(exact))
    covariance_text = read(str(covariance))
    parent_text = read(str(parent))
    check("new note declares bounded_theorem claim type", "Claim type: bounded_theorem" in note_text)
    check("new note says no audit verdict is applied", "No audit verdict is applied" in note_text)
    check("new note labels the bridge as conditional support", "conditional support" in note_text)
    check(
        "new note forbids treating CKM inverse-square as Route-2 proof",
        "ckm inverse-square row" in note_text.lower() and "route-2 readout theorem" in note_text.lower(),
    )
    check("new note does not treat CKM packet as retained Route-2 authority", "not as retained Route-2 authority" in note_text)
    check("CKM note frames inverse-square as CKM-side eta^2 reading", "CKM Wolfenstein" in ckm_text and "eta^2" in ckm_text)
    check("CKM note has no Route-2 readout bridge", "Route-2" not in ckm_text and "rho_E" not in ckm_text)
    check("usable index scopes eta^2 inverse-square to CKM bookkeeping", "`eta^2` inverse-square reading" in usable_text and "CKM CP-parameter bookkeeping" in usable_text)
    check("Route-2 exact readout still names beta_E/alpha_E=21/4 as missing", "beta_E / alpha_E = 21/4" in exact_text)
    check("covariance note says inverse-square is a future derivation target", "q_X" in covariance_text and "w_X" in covariance_text and "future derivation" in covariance_text)
    check("parent theta note keeps endpoint triple open", "readout-map endpoint triple is not yet derived" in parent_text)

    print("\nSummary")
    print("-" * 72)
    print(f"TOTAL: PASS={PASS}, FAIL={FAIL}")
    print(
        "VERDICT: conditional support plus bridge firewall. The CKM inverse-square components "
        "1/4 and 1/9 have ratio 9/4, and identifying Route-2 lambda=q_E/q_T with that ratio "
        "would close rho_E=21/4 exactly. The current bank does not supply that semantic bridge: "
        "the CKM inverse-square row is CKM CP bookkeeping, not a Route-2 readout coefficient law."
    )
    return 1 if FAIL else 0


if __name__ == "__main__":
    raise SystemExit(main())
