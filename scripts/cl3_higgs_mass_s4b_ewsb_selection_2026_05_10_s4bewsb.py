#!/usr/bin/env python3
"""Supplied scalar/readout diagnostics only; no physical S4a support, vacuum selection,
causal S4/S7 localization or smaller established matching residual is certified.
The full historical note, runner and cache are preserved in the PR9848 archive.
All numerical expressions and thresholds are retained, including the explicitly
labelled legacy 2x proxy (the exact expansion coefficient is 3, not 2).
"""
from pathlib import Path
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
 "docs/HIGGS_MASS_S4B_EWSB_SELECTION_BOUNDED_NOTE_2026-05-10_s4bewsb.md",
 "docs/HIGGS_MASS_S4_BORN_EXTENSION_BOUNDED_NOTE_2026-05-10_higgsS4.md",
)
DOCUMENTARY = []
def documentary(label, legacy_value=None):
    DOCUMENTARY.append(label)
    print("UNSCORED historical assertion/diagnostic (not proof): " + label + " value=" + str(legacy_value))
    return None

def check(label, condition):
    print(("PASS " if condition else "FAIL ") + label)
    return bool(condition)

import math
import sys
P_PLAQUETTE = 0.5934
U_0 = P_PLAQUETTE ** 0.25
ALPHA_BARE = 1.0 / (4.0 * math.pi)
ALPHA_LM = ALPHA_BARE / U_0
ALPHA_S_V = ALPHA_BARE / U_0 ** 2
M_PL = 1.221e+19
C_APBC = (7.0 / 8.0) ** 0.25
V_EW = M_PL * C_APBC * ALPHA_LM ** 16
N_TASTE = 16
V_PRIME_PRIME_AT_ZERO = -N_TASTE / (4.0 * U_0 ** 2)
LAMBDA_SQ = 4.0 * U_0 ** 2
M_H_TREE_PER_TASTE = 1.0 / (4.0 * U_0 ** 2)
M_H_TREE = V_EW / (2.0 * U_0)
PDG_V_EW = 246.22
PDG_M_H = 125.25
PDG_ALPHA_S_MZ = 0.1179
PDG_INV_ALPHA_EM_MZ = 127.95
PDG_M_T_POLE = 172.69

def test_b1_1_v_ew_retained():
    rel_dev = (V_EW - PDG_V_EW) / PDG_V_EW
    passes = []
    passes.append(check('B1.1.a supplied hierarchy expression is near 246.28', abs(V_EW - 246.28) < 0.5))
    passes.append(check('B1.1.b supplied scale differs from comparator by at most 0.1%', abs(rel_dev) < 0.001))
    passes.append(documentary('B1.1.c', True))
    return passes

def test_b1_2_ewsb_q_not_operator():
    Q_dim = 2
    physical_higgs_hilbert_dim = 'infinite (post-EWSB physical scalar)'
    passes = []
    passes.append(documentary('B1.2.a', Q_dim == 2))
    passes.append(documentary('B1.2.b', True))
    passes.append(documentary('B1.2.c', True))
    passes.append(documentary('B1.2.d', True))
    return passes

def v_taste(m, lam_sq=LAMBDA_SQ, n_taste=N_TASTE):
    return -(n_taste / 2.0) * math.log(m ** 2 + lam_sq)

def v_taste_first_derivative(m, lam_sq=LAMBDA_SQ, n_taste=N_TASTE):
    return -n_taste * m / (m ** 2 + lam_sq)

def v_taste_second_derivative(m, lam_sq=LAMBDA_SQ, n_taste=N_TASTE):
    num = lam_sq - m ** 2
    den = (m ** 2 + lam_sq) ** 2
    return -n_taste * num / den

def test_b1_3_lattice_curvature_at_v_eq_at_zero():
    m_v_lattice = V_EW / M_PL
    v_pp_at_zero = v_taste_second_derivative(0.0)
    v_pp_at_v = v_taste_second_derivative(m_v_lattice)
    abs_diff = abs(v_pp_at_v - v_pp_at_zero)
    rel_diff = abs_diff / abs(v_pp_at_zero) if v_pp_at_zero != 0 else float('inf')
    leading_order_correction = 2.0 * m_v_lattice ** 2 / LAMBDA_SQ
    passes = []
    passes.append(check('B1.3.a supplied curvature at zero is negative', v_pp_at_zero < 0))
    passes.append(check('B1.3.b supplied derivative at zero equals -4/u_0²', abs(v_pp_at_zero - -4.0 / U_0 ** 2) < 1e-12))
    passes.append(check('B1.3.c supplied curvature at sampled dimensionless scale is negative', v_pp_at_v < 0))
    passes.append(documentary('B1.3.d', rel_diff < 1e-30))
    passes.append(documentary('B1.3.e', abs(rel_diff - leading_order_correction) < 1e-30 or rel_diff == 0.0))
    return passes

def test_b1_4_hypothesis_equation_tachyonic_on_retained():
    m_v_lattice = V_EW / M_PL
    v_pp_at_v = v_taste_second_derivative(m_v_lattice)
    m_H_squared_lattice = v_pp_at_v / N_TASTE
    m_H_squared_phys = m_H_squared_lattice * V_EW ** 2
    abs_per_channel = abs(v_pp_at_v) / N_TASTE
    m_H_alt_squared = abs_per_channel * V_EW ** 2
    m_H_alt = math.sqrt(m_H_alt_squared)
    passes = []
    passes.append(check('B1.4.a supplied signed curvature readout is negative', m_H_squared_phys < 0))
    passes.append(check('B1.4.b signed readout matches the supplied origin expression at legacy tolerance', abs(m_H_squared_phys - -1.0 / (4.0 * U_0 ** 2) * V_EW ** 2) < 0.001 * abs(m_H_squared_phys)))
    passes.append(check('B1.4.c absolute-value readout equals supplied v/(2u_0)', abs(m_H_alt - V_EW / (2.0 * U_0)) < 1e-06))
    passes.append(check('B1.4.d absolute-value readout is near supplied 140.31', abs(m_H_alt - 140.31) < 0.5))
    passes.append(check('B1.4.e supplied readout discrepancy is between 9 and 13 percent', 9.0 < (m_H_alt - PDG_M_H) / PDG_M_H * 100 < 13.0))
    return passes

def test_b1_5_m_h_v_self_reference():
    sym_curvature_abs = abs(V_PRIME_PRIME_AT_ZERO)
    per_channel_at_zero = sym_curvature_abs / N_TASTE
    m_h_over_v_sq_reconstructed = per_channel_at_zero
    m_h_over_v_reconstructed = math.sqrt(m_h_over_v_sq_reconstructed)
    one_over_2u0 = 1.0 / (2.0 * U_0)
    passes = []
    passes.append(check('B1.5.a absolute origin curvature divided by N equals 1/(4u_0²)', abs(per_channel_at_zero - 1.0 / (4.0 * U_0 ** 2)) < 1e-12))
    passes.append(check('B1.5.b square-root readout equals 1/(2u_0)', abs(m_h_over_v_reconstructed - one_over_2u0) < 1e-12))
    passes.append(documentary('B1.5.c', True))
    passes.append(documentary('B1.5.d', True))
    return passes

def test_b1_6_sharpened_decomposition():
    test_points = [0.1, 0.5, 1.0, 2.0, 5.0, 10.0, V_EW / M_PL]
    monotone_decreasing_for_m_positive = all((v_taste_first_derivative(m) < 0 for m in test_points))
    passes = []
    passes.append(check('B1.6.a supplied numerical evaluation point is near 246.28 (no physical selection)', abs(V_EW - 246.28) < 0.5))
    passes.append(check('B1.6.b first derivative is negative at the seven listed positive sample points', monotone_decreasing_for_m_positive))
    passes.append(documentary('B1.6.c', True))
    passes.append(documentary('B1.6.d', True))
    passes.append(documentary('B1.6.e', True))
    passes.append(documentary('B1.6.f', True))
    return passes

def test_b1_7_sister_precision_asymmetry():
    sister_predictions = [('v_EW', V_EW, PDG_V_EW, 'GeV'), ('alpha_s(M_Z)', 0.1181, PDG_ALPHA_S_MZ, ''), ('1/alpha_EM(M_Z)', 127.67, PDG_INV_ALPHA_EM_MZ, ''), ('m_t(pole, 2-loop)', 172.57, PDG_M_T_POLE, 'GeV'), ('m_H_tree (S4)', M_H_TREE, PDG_M_H, 'GeV')]
    deviations_pct = []
    for label, fw, pdg, units in sister_predictions:
        dev_pct = (fw - pdg) / pdg * 100
        deviations_pct.append((label, abs(dev_pct)))
    sister_only = [d for d in deviations_pct if not d[0].startswith('m_H')]
    higgs_dev = [d for d in deviations_pct if d[0].startswith('m_H')][0][1]
    sister_max = max((d[1] for d in sister_only))
    passes = []
    passes.append(check('B1.7.a four supplied comparison discrepancies are below one percent', sister_max < 1.0))
    passes.append(check('B1.7.b supplied Higgs-labelled discrepancy is between 9 and 13 percent', 9.0 < higgs_dev < 13.0))
    passes.append(check('B1.7.c ratio of supplied discrepancies exceeds ten; no causal localization', higgs_dev / sister_max >= 10.0))
    passes.append(documentary('B1.7.d', True))
    return passes

def test_no_pdg_consumed_as_input():
    passes = []
    passes.append(documentary('Firewall.a', True))
    passes.append(documentary('Firewall.b', True))
    passes.append(documentary('Firewall.c', True))
    passes.append(documentary('Firewall.d', True))
    return passes

def exact_supplied_controls():
    import sympy as sp
    m, lam, n, x = sp.symbols('m L N x', positive=True)
    potential = -n * sp.log(m**2 + lam) / 2
    first = -n * m / (m**2 + lam)
    second = -n * (lam - m**2) / (m**2 + lam)**2
    ratio = (1-x) / (1+x)**2
    relative = (3*x+x**2) / (1+x)**2
    checks = [
        ("exact first derivative of supplied potential", sp.simplify(sp.diff(potential,m)-first)==0),
        ("exact second derivative; original note factor-two transcription withdrawn", sp.simplify(sp.diff(potential,m,2)-second)==0),
        ("exact curvature ratio after x=m²/L", sp.simplify((second/(-n/lam)).subs(m**2,x*lam)-ratio)==0),
        ("exact relative curvature change", sp.simplify(1-ratio-relative)==0),
        ("linear expansion coefficient is 3", sp.diff(relative,x).subs(x,0)==3),
        ("positive exact tiny change is not floating-point zero", relative.subs(x,sp.Rational(1,10**34))>0),
        ("exact positive factor establishes relative change below 3x", sp.factor(3*x-relative)==x**2*(3*x+5)/(x+1)**2),
    ]
    return [check(label,ok) for label,ok in checks]


def main():
    results = []
    results.extend(test_b1_1_v_ew_retained())
    results.extend(test_b1_2_ewsb_q_not_operator())
    results.extend(test_b1_3_lattice_curvature_at_v_eq_at_zero())
    results.extend(test_b1_4_hypothesis_equation_tachyonic_on_retained())
    results.extend(test_b1_5_m_h_v_self_reference())
    results.extend(test_b1_6_sharpened_decomposition())
    results.extend(test_b1_7_sister_precision_asymmetry())
    results.extend(test_no_pdg_consumed_as_input())
    results.extend(exact_supplied_controls())
    arithmetic = [value for value in results if value is not None]
    root = Path(__file__).resolve().parents[1]
    own, parent = [(root/p).read_text() for p in AUDIT_INPUT_PATHS]
    documentary_checks = [
        "No physical S4a support" in own,
        "The discrepancy alone does not" in parent,
        "coefficient 3" in own,
    ]
    for i, ok in enumerate(documentary_checks):
        print(("DOCUMENTARY_PASS " if ok else "DOCUMENTARY_FAIL ") + str(i))
    failures = sum(not v for v in arithmetic) + sum(not v for v in documentary_checks)
    print(f"ARITHMETIC PASS={sum(arithmetic)} FAIL={sum(not v for v in arithmetic)}")
    print(f"DOCUMENTARY checks={len(documentary_checks)} unvalidated historical assertions={len(DOCUMENTARY)}")
    print("Scope: supplied arithmetic and source-boundary checks only; physical matching remains open.")
    return 1 if failures else 0

if __name__ == "__main__":
    sys.exit(main())
