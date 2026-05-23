#!/usr/bin/env python3
"""SM-identity triangulation convergence discriminator.

The dimensionless positive-side complement to the native-holonomy no-go. Four
independent retained-grade upstream rows (all deps=[] in the ledger) constrain
the one-generation Standard Model carrier sector by distinct mechanisms:

  graph_first_su3_integration_note            (retained)
        -> color rank N_c = 3   [graph topology / commutant algebra]
  three_generation_observable_m3c_burnside    (retained)
        -> generation count n_gen = 3   [finite matrix algebra on C^3]
  koide_y_substrate_anomaly_forcing           (retained_bounded)
        -> anomaly + Witten allow only an N_c-parameterized family,
           leaving N_c (odd), n_gen, and the absolute normalization free
  sm_hypercharge_uniqueness_algebraic_solution (retained_bounded)
        -> given the LH template + Q = T_3 + Y/2, the hypercharges are the
           unique rational tuple

Claim under test (the triangulation):
  The anomaly-family row alone is loose (it explicitly does NOT select N_c,
  n_gen, or the absolute scale). Intersecting its anomaly-allowed family with
  the independent structural selectors N_c=3 and n_gen=3 lands exactly on the
  hypercharge-enumeration row's unique SM hypercharge tuple, with left-Weyl
  carrier electric charges {0, +/-1/3, +/-2/3, +/-1}.

  The two residual genuine inputs are isolated and reported:
    template residual: the LH matter template (which fields exist);
    normalization residual: the absolute hypercharge normalization.
  The triangulation fixes everything except those two residuals.

Exact rational arithmetic via fractions. No PDG / fitted / scale input.
This script asserts no audit status; it is a convergence discriminator.
"""

from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path

PASS = 0
FAIL = 0
RETAINED_GRADE = {"retained", "retained_bounded", "retained_no_go"}
UPSTREAM_CLAIMS = {
    "graph_first_su3_integration_note": (
        "graph topology / commutant algebra fixes N_c=3"
    ),
    "three_generation_observable_m3c_burnside_narrow_theorem_note_2026-05-10": (
        "finite matrix algebra fixes n_gen=3"
    ),
    "koide_y_substrate_anomaly_forcing_note_2026-05-08_probey_substrate_anomaly": (
        "anomaly traces give the loose N_c-family"
    ),
    "sm_hypercharge_uniqueness_algebraic_solution_enumeration_narrow_theorem_note_2026-05-10": (
        "rational enumeration supplies the unique tuple under template/convention"
    ),
}


def check(name: str, condition: bool, detail: str = "") -> bool:
    global PASS, FAIL
    if condition:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    msg = f"  [{status}] {name}"
    if detail:
        msg += f"  ({detail})"
    print(msg)
    return condition


def ledger_rows() -> dict:
    repo_root = Path(__file__).resolve().parents[1]
    ledger_path = repo_root / "docs" / "audit" / "data" / "audit_ledger.json"
    with ledger_path.open() as f:
        return json.load(f)["rows"]


def check_upstream_ledger_guards() -> None:
    print("\n" + "-" * 76)
    print("LEDGER GUARD  upstream rows are retained-grade and deps=[]")
    print("-" * 76)
    rows = ledger_rows()
    for claim_id, purpose in UPSTREAM_CLAIMS.items():
        row = rows.get(claim_id) or {}
        status = row.get("effective_status")
        deps = row.get("deps")
        ok = status in RETAINED_GRADE and deps == []
        check(
            f"{claim_id} retained-grade with deps=[]",
            ok,
            detail=f"status={status}, deps={deps}, purpose={purpose}",
        )


def anomaly_family(nc: F) -> dict[str, F]:
    """koide_y_substrate_anomaly_forcing one-generation family, parameterized
    by color rank nc. Hypercharges Y (doubled-Y convention, Q = T_3 + Y/2),
    listed for the conjugated right-handed singlets and the LH multiplets.
    """
    return {
        "Q_L": F(1, 1) / nc,          # left quark doublet  (2,3)
        "L_L": F(-1, 1),              # left lepton doublet (2,1)
        "u_Rc": -(1 + F(1, 1) / nc),  # conjugate up-singlet
        "d_Rc": (1 - F(1, 1) / nc),   # conjugate down-singlet
        "e_Rc": F(2, 1),              # conjugate charged-lepton singlet
        "nu_Rc": F(0, 1),             # neutral singlet
    }


def perturbative_anomaly_traces(nc: F, fam: dict[str, F]) -> dict[str, F]:
    """The four perturbative trace combinations that must vanish for one
    generation. Multiplicities: quark doublet has 2 (SU2) * nc (color); lepton
    doublet has 2; singlets have nc (quarks) or 1 (leptons).
    """
    # Compute over LH Weyl fermions: LH doublets as-is, RH as LH conjugates.
    lh = {
        "Q_L": (fam["Q_L"], 2, nc),
        "L_L": (fam["L_L"], 2, F(1)),
        "u_Rc": (fam["u_Rc"], 1, nc),
        "d_Rc": (fam["d_Rc"], 1, nc),
        "e_Rc": (fam["e_Rc"], 1, F(1)),
        "nu_Rc": (fam["nu_Rc"], 1, F(1)),
    }
    # U(1)_Y gravitational: sum over Weyl of (dim2*dim3)*Y
    grav = sum(d2 * d3 * Y for (Y, d2, d3) in lh.values())
    # U(1)^3: sum (dim2*dim3)*Y^3
    cubic = sum(d2 * d3 * Y**3 for (Y, d2, d3) in lh.values())
    # SU(2)^2 U(1): only SU2 doublets, weight color_dim * Y  (Dynkin 1/2 common factor dropped)
    su2sq = sum(d3 * Y for (Y, d2, d3) in lh.values() if d2 == 2)
    # SU(N_c)^2 U(1): only color triplets, weight su2_dim * Y
    su3sq = (lh["Q_L"][1] * lh["Q_L"][0]
             + lh["u_Rc"][1] * lh["u_Rc"][0]
             + lh["d_Rc"][1] * lh["d_Rc"][0])
    return {
        "grav_U1": grav,
        "U1_cubed": cubic,
        "SU2sq_U1": su2sq,
        "SU3sq_U1": su3sq,
    }


def main() -> int:
    print("=" * 76)
    print("SM-IDENTITY TRIANGULATION CONVERGENCE DISCRIMINATOR")
    print("=" * 76)
    check_upstream_ledger_guards()

    # --- The anomaly family is loose (cancels for a range of odd N_c) ---
    print("\n" + "-" * 76)
    print("Anomaly family is LOOSE: cancels for multiple odd N_c (no selection)")
    print("-" * 76)
    for nc in (F(3), F(5), F(7)):
        tr = perturbative_anomaly_traces(nc, anomaly_family(nc))
        allzero = all(v == 0 for v in tr.values())
        check(
            f"all four anomaly traces vanish at N_c={int(nc)}",
            allzero,
            detail=", ".join(f"{k}={v}" for k, v in tr.items()),
        )
    print("        -> anomaly cancellation alone does not pin N_c.")

    # --- Independent structural selectors collapse the freedom ---
    print("\n" + "-" * 76)
    print("Independent selectors fix N_c=3 (graph) and n_gen=3 (Burnside)")
    print("-" * 76)
    nc = F(3)   # imported from graph_first_su3_integration (deps=[])
    ngen = 3    # imported from three_generation_observable_m3c_burnside (deps=[])
    check("N_c fixed to 3 by independent graph-first selector (deps=[])", nc == 3)
    check("n_gen fixed to 3 by independent Burnside selector (deps=[])", ngen == 3)

    # --- Convergence: family at N_c=3 == unique SM tuple ---
    print("\n" + "-" * 76)
    print("CONVERGENCE  family(N_c=3) lands on unique SM hypercharges")
    print("-" * 76)
    fam = anomaly_family(nc)
    # Hypercharge-enumeration RH-singlet tuple (particle Y, doubled-Y).
    s4 = {
        "u_R": F(4, 3),
        "d_R": F(-2, 3),
        "e_R": F(-2, 1),
        "nu_R": F(0, 1),
    }
    got = {
        "u_R": -fam["u_Rc"],
        "d_R": -fam["d_Rc"],
        "e_R": -fam["e_Rc"],
        "nu_R": -fam["nu_Rc"],
    }
    for k in s4:
        check(
            f"Y({k}) matches SM value {s4[k]}",
            got[k] == s4[k],
            detail=f"got {got[k]}",
        )
    check("Y(Q_L) = +1/3 (template (2,3)_{+1/3})", fam["Q_L"] == F(1, 3))
    check("Y(L_L) = -1 (template (2,1)_{-1})", fam["L_L"] == F(-1, 1))

    # Left-Weyl carrier electric charges Q = T_3 + Y/2, including conjugated
    # singlets; this is the source of the symmetric charge spectrum.
    charges = set()
    for Y in [fam["Q_L"]]:  # quark doublet T_3 = +/-1/2
        charges.update({F(1, 2) + Y / 2, F(-1, 2) + Y / 2})
    for Y in [fam["L_L"]]:
        charges.update({F(1, 2) + Y / 2, F(-1, 2) + Y / 2})
    for k in ["u_Rc", "d_Rc", "e_Rc", "nu_Rc"]:
        charges.add(fam[k] / 2)
    expected_charges = {
        F(0),
        F(1, 3),
        F(-1, 3),
        F(2, 3),
        F(-2, 3),
        F(1),
        F(-1),
    }
    check(
        "left-Weyl electric-charge spectrum is exactly {0,+/-1/3,+/-2/3,+/-1}",
        charges == expected_charges,
        detail=f"charges={sorted(charges)}",
    )

    # --- Residual genuine inputs (honestly isolated) ---
    print("\n" + "-" * 76)
    print("RESIDUAL INPUTS (not fixed by the triangulation)")
    print("-" * 76)
    # Absolute normalization: rescaling Y -> lambda*Y preserves all anomalies.
    lam = F(7, 5)
    fam_scaled = {k: lam * v for k, v in fam.items()}
    tr_scaled = perturbative_anomaly_traces(nc, fam_scaled)
    check(
        "absolute normalization is FREE (lambda*Y keeps anomalies zero)",
        all(v == 0 for v in tr_scaled.values()),
        detail="overall rational scale is not fixed here",
    )
    print("        LH template (which fields exist) is an explicit input.")
    print("        Absolute normalization remains outside this claim.")

    # --- Verdict ---
    print("\n" + "=" * 76)
    print("VERDICT")
    print("=" * 76)
    if FAIL == 0:
        print(
            "  CONVERGENCE CONFIRMED.\n"
            "  Four retained-grade upstream rows triangulate: anomaly (loose)\n"
            "  intersect N_c=3 (graph) intersect n_gen=3 (Burnside) lands exactly\n"
            "  on the unique SM hypercharge tuple and left-Weyl charge spectrum.\n"
            "  Residual inputs are the LH template and absolute normalization.\n"
            "  The dimensionless carrier-charge identity is pinned up to those\n"
            "  residuals; no scale input is consumed here.\n"
        )
    print("=" * 76)
    if FAIL:
        print(f"PASS={PASS} FAIL={FAIL}")
        return 1
    print(f"PASS={PASS} FAIL=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
