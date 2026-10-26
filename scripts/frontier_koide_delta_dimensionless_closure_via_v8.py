"""Supplied rational arithmetic and independent Fourier phase controls.
Historical text observations are unscored and are not scientific dependencies.
"""

from __future__ import annotations

import sys
from pathlib import Path

import numpy as np
import sympy as sp


REPO_ROOT = Path(__file__).resolve().parent.parent
DOCS_DIR = REPO_ROOT / "docs"

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ('docs/KOIDE_DELTA_DIMENSIONLESS_CLOSURE_VIA_V8_THEOREM_NOTE_2026-04-29.md', 'docs/KOIDE_A1_BRANNEN_PLANCHEREL_IDENTITY_SUPPORT_NOTE_2026-04-25.md', 'docs/KOIDE_Q_OP_LOCALITY_SOURCE_DOMAIN_CLOSURE_THEOREM_NOTE_2026-04-29.md', 'docs/KOIDE_BRANNEN_PHASE_REDUCTION_THEOREM_NOTE_2026-04-20.md', 'docs/KOIDE_Q_EQ_3DELTA_IDENTITY_NOTE_2026-04-21.md', 'docs/KOIDE_Z3_QUBIT_RADIAN_BRIDGE_NO_GO_NOTE_2026-04-20.md')

AUDIT_FAILS: list[str] = []


def audit(name: str, condition: bool, detail: str = "") -> None:
    status = "PASS" if condition else "FAIL"
    line = f"[{status}] {name}"
    if detail:
        line += f" — {detail}"
    print(line)
    if not condition:
        AUDIT_FAILS.append(name)


def historical(name: str, condition: bool, detail: str = "") -> None:
    print(f"HISTORICAL_UNSCORED old assertion={name!r}; observed={bool(condition)}; old detail={detail!r}")


def read_doc(path_rel: str) -> str:
    return (DOCS_DIR / path_rel).read_text(encoding="utf-8")


def main() -> int:
    AUDIT_FAILS.clear()
    for name in AUDIT_INPUT_PATHS:
        if not (REPO_ROOT / name).is_file():
            print(f"FAIL: missing declared input {name}")
            return 1
    print("=" * 72)
    print("Supplied rational scalar r and independent Fourier phase")
    print("=" * 72)

    # ---- Historical text observations, not prerequisites -----------------------------

    print()
    print("Historical documentary observations: no prerequisites or authority checks")
    print("-" * 72)

    v8_text = read_doc(
        "KOIDE_Q_OP_LOCALITY_SOURCE_DOMAIN_CLOSURE_THEOREM_NOTE_2026-04-29.md"
    )
    historical(
        "V8 note exists on disk",
        len(v8_text) > 0,
        "block 1 closure note found",
    )
    historical(
        "V8 carries support status",
        "actual_current_surface_status: support" in v8_text,
        "V8 firewall: support",
    )
    historical(
        "V8 carries audit-required-before-effective-retained flag",
        "audit_required_before_effective_retained: true" in v8_text,
        "V8 firewall: audit required",
    )
    historical(
        "V8 closes Q = 2/3 on A_min",
        ("Q = 2/3" in v8_text and "A_min" in v8_text),
        "V8 §2 theorem statement",
    )

    # ---- Historical Brannen text observations -------------------------------

    print()
    print("Historical text observations (unscored; old assertions quoted, not adopted)")
    print("-" * 72)

    brannen_text = read_doc("KOIDE_BRANNEN_PHASE_REDUCTION_THEOREM_NOTE_2026-04-20.md")
    historical(
        "Brannen phase reduction note exists",
        len(brannen_text) > 0,
        "retained on main",
    )
    historical(
        "n_eff = 2 from doublet conjugate-pair forcing",
        "n_eff = 2" in brannen_text and "conjugate-pair" in brannen_text,
        "Brannen §1.3",
    )
    historical(
        "d = 3 from |C_3|",
        "d     = 3" in brannen_text or "d = 3" in brannen_text,
        "Brannen §1",
    )
    historical(
        "δ = n_eff / d² = 2/9 (Brannen normalization)",
        ("delta = n_eff / d^2 = 2/9" in brannen_text)
        or ("delta = n_eff/d^2 = 2/9" in brannen_text),
        "Brannen §2.3",
    )
    historical(
        "δ = Q/d at d=3",
        "delta = Q/d" in brannen_text,
        "Brannen §2.4",
    )

    plancherel_text = read_doc(
        "KOIDE_A1_BRANNEN_PLANCHEREL_IDENTITY_SUPPORT_NOTE_2026-04-25.md"
    )
    historical(
        "Plancherel identity note exists",
        len(plancherel_text) > 0,
        "support-grade on main",
    )
    historical(
        "Plancherel: arg(b) = δ (mod 2π) inside Brannen parameterization",
        "arg(b) = δ" in plancherel_text or "arg(b) = `δ`" in plancherel_text,
        "Plancherel §1 lemma",
    )

    qpdelta_text = read_doc("KOIDE_Q_EQ_3DELTA_IDENTITY_NOTE_2026-04-21.md")
    historical(
        "Q = p·δ identity note exists",
        len(qpdelta_text) > 0,
        "retained on main",
    )
    historical(
        "Q = p·δ at p = d = 3 identity",
        "Q = p · δ" in qpdelta_text or "Q = p·δ" in qpdelta_text or "Q = 3·δ" in qpdelta_text,
        "Q = p·δ identity",
    )

    radian_no_go_text = read_doc(
        "KOIDE_Z3_QUBIT_RADIAN_BRIDGE_NO_GO_NOTE_2026-04-20.md"
    )
    historical(
        "Z_3 qubit radian-bridge no-go note exists",
        len(radian_no_go_text) > 0,
        "retained negative result on main",
    )
    historical(
        "Z_3 qubit no-go closes canonical R/Z → U(1) lift route",
        "qubit equator" in radian_no_go_text and "π/3" in radian_no_go_text,
        "no-go §2.1 candidate A",
    )

    # ---- Section 3: algebraic identities of the Block 2 composition --------

    print()
    print("Supplied rational and coordinate identities (sympy/numpy)")
    print("-" * 72)

    # Supply Q=2/3; historical OP text is not its proof.
    Q = sp.Rational(2, 3)
    historical(
        "Q = 2/3 (composed from V8)",
        Q == sp.Rational(2, 3),
        f"Q = {Q}",
    )

    # Chosen coordinate lift -2 theta has derivative -2; no topological index inferred.
    theta = sp.symbols("theta", real=True)
    zeta = sp.exp(-2 * sp.I * theta)
    arg_zeta_derivative = sp.diff(sp.simplify(sp.arg(zeta) if False else -2 * theta), theta)
    n_eff = abs(arg_zeta_derivative)
    audit(
        "Magnitude of derivative of chosen continuous coordinate lift -2 theta is 2",
        n_eff == 2,
        f"n_eff = {n_eff}",
    )

    # 3.3 d = |C_3| = 3
    d = 3
    historical(
        "d = |C_3| = 3",
        d == 3,
        f"d = {d}",
    )

    # 3.4 δ_dimensionless = n_eff / d² = 2/9
    delta_dim = sp.Rational(int(n_eff), d * d)
    audit(
        "Defined r=n/d² equals2/9 for supplied d=3 and coordinate n=2",
        delta_dim == sp.Rational(2, 9),
        f"δ = {delta_dim}",
    )

    # 3.5 δ = Q/d cross-check
    delta_via_Q = Q / d
    audit(
        "Defined r=Q/d equals2/9 for supplied Q=2/3,d=3",
        delta_via_Q == sp.Rational(2, 9),
        f"Q/d = {delta_via_Q}",
    )

    # 3.6 Q = p·δ identity (p = d = 3)
    p = d
    Q_via_pdelta = p * delta_dim
    audit(
        "Supplied p=d=3 gives p*r=Q by rational arithmetic",
        Q_via_pdelta == Q,
        f"p·δ = 3·(2/9) = {Q_via_pdelta} == Q = {Q}",
    )

    # 3.7 Plancherel: arg(b) = δ (mod 2π) inside Brannen parameterization
    # Brannen identity: b = (√3/2) V_0 c · exp(iδ); arg(b) = δ
    # Use a numerical witness over a representative range of δ values to
    # verify the identity holds, since sympy's symbolic arg simplification
    # is non-trivial without delta restricted to (-π, π].
    V0_num, c_num = 1.0, 1.0
    plancherel_match = True
    for delta_test in np.linspace(-np.pi + 0.01, np.pi - 0.01, 17):
        b_num = (np.sqrt(3) / 2) * V0_num * c_num * np.exp(1j * delta_test)
        arg_b_num = np.angle(b_num)
        if not np.isclose(arg_b_num, delta_test, atol=1e-10):
            plancherel_match = False
            break
    audit(
        "Principal argument of directly constructed positive-radius exponential at17 interior phases",
        plancherel_match,
        "17 sampled phases only; this fixture constructs b from the formula",
    )

    # ---- Supplied convention comparison ----------------

    print()
    print("Two supplied angle conventions: arithmetic comparison only")
    print("-" * 72)

    # Two supplied conventions give different numerical angles, not an exhaustive obstruction.
    delta_radians_standard = float(delta_dim) * 2 * np.pi
    expected_4pi_over_9 = 4 * np.pi / 9
    audit(
        "Standard 2π-radian conversion gives 4π/9 rad (NOT 2/9 rad)",
        np.isclose(delta_radians_standard, expected_4pi_over_9),
        f"2π·(2/9) = {delta_radians_standard:.6f} = 4π/9 = {expected_4pi_over_9:.6f}",
    )
    audit(
        "Two supplied angle conventions produce unequal numerical values",
        not np.isclose(delta_radians_standard, 2 / 9),
        f"2π·(2/9) = {delta_radians_standard:.6f} ≠ 2/9 = {2/9:.6f}",
    )

    # Historical assignment-only observation; no fitted data are evaluated here.
    pdg_match_value = 2.0 / 9.0  # rad
    historical(
        "Brannen-PDG match value δ_observed = 2/9 rad (support-grade witness)",
        np.isclose(pdg_match_value, 2 / 9),
        f"δ_observed ≈ 2/9 rad ≈ {pdg_match_value:.6f}",
    )
    historical(
        "Postulate P (literal 2/9 = 2/9 rad) NOT closed by V1",
        True,  # always passes; we explicitly flag P as open
        "radian-bridge postulate explicitly open per §4 of V1 note",
    )

    # ---- Historical metadata observations ----------------------------

    print()
    print("Historical old metadata observations (unscored)")
    print("-" * 72)

    own_text = read_doc(
        "KOIDE_DELTA_DIMENSIONLESS_CLOSURE_VIA_V8_THEOREM_NOTE_2026-04-29.md"
    )
    historical(
        "V1 carries actual_current_surface_status: support",
        "actual_current_surface_status: support" in own_text,
        "V1 firewall",
    )
    historical(
        "V1 carries audit_required_before_effective_retained: false",
        "audit_required_before_effective_retained: false" in own_text,
        "V1 firewall",
    )
    historical(
        "V1 carries bare_retained_allowed: false",
        "bare_retained_allowed: false" in own_text,
        "V1 firewall",
    )
    historical(
        "V1 records radian_bridge_postulate_P_status: open",
        "radian_bridge_postulate_P_status: open" in own_text,
        "V1 firewall: P explicitly open",
    )
    historical(
        "V1 records literal 2/9 rad PDG match as support_grade",
        "literal_2_over_9_rad_pdg_match_status: support_grade_numerical_witness"
        in own_text,
        "V1 firewall: PDG match support-grade",
    )

    # ---- Section 6: forbidden imports -------------------------------------

    print()
    print("Historical lexical observations (unscored; not proof of input independence)")
    print("-" * 72)

    forbidden_imports = ["m_e", "m_mu", "m_tau", "delta_obs"]
    body_only = own_text.split("## 7. Verification")[0]
    for token in forbidden_imports:
        is_load_bearing = (
            f"= {token}" in body_only or f"{token} = " in body_only
        )
        historical(
            f"forbidden import not used as proof input: {token}",
            not is_load_bearing,
            "no observed lepton mass enters proof",
        )

    # Independent amplitude construction separates the rational r from free phase.
    phases = [0.0, np.pi/24]
    control_values = []
    for phase in phases:
        amplitudes = np.array([1+np.sqrt(2)*np.cos(phase+2*np.pi*j/3) for j in range(3)])
        omega = np.exp(2j*np.pi/3)
        b = (amplitudes[0]+np.conj(omega)*amplitudes[1]+omega*amplitudes[2])/np.sqrt(3)
        Q_sample = np.sum(amplitudes**2)/np.sum(amplitudes)**2
        phase_error = np.angle(np.exp(1j*(np.angle(b)-phase)))
        audit(f"Positive amplitudes and Q=2/3 at supplied phase {phase}",
              bool(np.all(amplitudes>0)) and abs(Q_sample-2/3)<1e-12)
        audit(f"Independent Fourier sum recovers supplied phase {phase}",abs(phase_error)<1e-12)
        control_values.append(float(np.angle(b)))
    audit("Same Q admits distinct Fourier phases in the two positive fixtures",
          abs(control_values[1]-control_values[0])>0.1)
    print("Defined rational r=Q/d is distinct from free phase delta; delta=r would be an extra choice.")
    print("No physical phase, Berry holonomy, OP closure, or exhaustive route conclusion is certified.")
    print(f"FAIL count: {len(AUDIT_FAILS)}")
    return 1 if AUDIT_FAILS else 0


if __name__ == "__main__":
    sys.exit(main())
