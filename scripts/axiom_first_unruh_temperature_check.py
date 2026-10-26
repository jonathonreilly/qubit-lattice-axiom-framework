"""Conditional KMS time-rescaling arithmetic on supplied inputs.

Finite consistency tests do not establish physical vacuum KMS or modular identity.
The arbitrary-algebra theorem is proved in the paired note.
"""
from __future__ import annotations

import math
from fractions import Fraction

AUDIT_INPUT_PATHS = ("docs/AXIOM_FIRST_UNRUH_TEMPERATURE_THEOREM_NOTE_2026-05-01.md",)
AUDIT_TIMEOUT_SEC = 120

import numpy as np


def unruh_temperature(a: float) -> float:
    """T_Unruh = a / (2 pi) (natural units)."""
    return a / (2 * math.pi)


def unruh_temperature_SI(a_SI: float) -> float:
    """T_Unruh in K for proper acceleration a_SI in m/s^2."""
    hbar = 1.054571817e-34  # J s
    c = 2.99792458e8  # m/s
    k_B = 1.380649e-23  # J/K
    return hbar * a_SI / (2 * math.pi * c * k_B)


def rescaled_beta(beta0, rate):
    if beta0 <= 0 or rate <= 0:
        raise ValueError("beta0 and rate must be positive")
    return beta0 / rate


def conditional_rescaling_checks():
    ok = True
    for beta0 in [Fraction(1, 3), Fraction(2), Fraction(7, 2)]:
        for rate in [Fraction(1, 5), Fraction(1), Fraction(9, 2)]:
            beta = rescaled_beta(beta0, rate)
            # Represent z=t+i*y by its exact rational components.
            for t in [Fraction(-3), Fraction(0), Fraction(5, 7)]:
                for y in [Fraction(0), beta/2, beta]:
                    ok = ok and 0 <= rate*y <= beta0
                ok = ok and (rate*t, rate*beta) == (rate*t, beta0)
            ok = ok and beta*rate == beta0
    for beta0, rate in [(0, 1), (-1, 1), (1, 0), (1, -1)]:
        try:
            rescaled_beta(beta0, rate)
        except ValueError:
            continue
        ok = False
    hbar, c, k_B = 1.054571817e-34, 2.99792458e8, 1.380649e-23
    acceleration = c/1e-9
    beta_time = 2*math.pi*c/acceleration
    beta_energy = beta_time/hbar
    kelvin = 1/(k_B*beta_energy)
    ok = ok and math.isclose(kelvin, unruh_temperature_SI(acceleration), rel_tol=1e-14)
    ok = ok and math.isclose(kelvin, 0.001215662471207031, rel_tol=1e-14)
    ok = ok and not math.isclose(kelvin, 200, rel_tol=1e-3)
    print(f"General positive rescaling, strip substitution, domain and SI controls: {'PASS' if ok else 'FAIL'}")
    print(f"Supplied formula at a=c/(1ns): {kelvin:.17g} K; historical 200 K rejected")
    return ok


def main() -> None:
    print("=" * 72)
    print("CONDITIONAL KMS TIME-RESCALING CHECK")
    print("=" * 72)
    print()
    print("Setup: supplied KMS state and positive time-rescaling premises")
    print("Supplied beta0=2pi specialization: T = a / (2 pi)")
    print()

    # ----- Test 1: Wick-rotation periodicity -----
    print("-" * 72)
    print("TEST 1: assigned-period consistency")
    print("-" * 72)
    print("The period is assigned here; this is not a geometry proof.")
    print("In Rindler coords (eta, xi), Euclidean continuation eta -> -i tau")
    print("has a supplied 2 pi angular convention; no state is constructed.")
    period_predicted = 2 * math.pi
    print(f"  predicted period = {period_predicted:.10f}")
    print(f"  expected         = {2 * math.pi:.10f}")
    t1_ok = abs(period_predicted - 2 * math.pi) < 1e-15
    print(f"  STATUS: {'PASS' if t1_ok else 'FAIL'}")
    print()

    # ----- Test 2: T_Unruh = a / (2 pi) sweep -----
    print("-" * 72)
    print("TEST 2: T_Unruh = a / (2 pi) across acceleration sweep")
    print("-" * 72)
    print(f"  {'a':>10}  {'T_Unruh':>16}  {'beta_th = 1/T':>16}  {'2 pi / a':>16}")
    max_diff_t2 = 0.0
    for a in [0.1, 0.5, 1.0, 2.0, 5.0, 10.0]:
        T_U = unruh_temperature(a)
        beta_th_from_T = 1.0 / T_U
        beta_predicted = 2 * math.pi / a
        diff = abs(beta_th_from_T - beta_predicted)
        max_diff_t2 = max(max_diff_t2, diff)
        print(f"  {a:>10.4f}  {T_U:>16.10e}  {beta_th_from_T:>16.10e}  {beta_predicted:>16.10e}")
    print()
    print(f"  max |beta_th(T) - 2 pi / a| = {max_diff_t2:.3e}")
    t2_ok = max_diff_t2 < 1e-15
    print(f"  STATUS: {'PASS' if t2_ok else 'FAIL'}")
    print()

    # ----- Test 3: SI numerical scale -----
    print("-" * 72)
    print("TEST 3: SI numerical scale at Earth gravity (a = 9.81 m/s^2)")
    print("-" * 72)
    a_earth = 9.81  # m/s^2
    T_earth = unruh_temperature_SI(a_earth)
    expected_earth = 4.06e-20  # K, well-known result
    print(f"  a = {a_earth} m/s^2 (Earth gravity)")
    print(f"  T_Unruh = {T_earth:.4e} K")
    print(f"  expected ~4 x 10^-20 K (textbook value)")
    rel_diff = abs(T_earth - expected_earth) / expected_earth
    print(f"  relative diff vs textbook = {rel_diff:.3f}")
    t3_ok = T_earth > 1e-21 and T_earth < 1e-19  # within order of magnitude
    print(f"  STATUS: {'PASS' if t3_ok else 'FAIL'}")
    print()

    # ----- Test 4: T_Unruh / a = 1 / (2 pi) universal -----
    print("-" * 72)
    print("TEST 4: T_Unruh / a = 1 / (2 pi) universal constant")
    print("-" * 72)
    universal = 1.0 / (2 * math.pi)
    print(f"  predicted constant = {universal:.10f}")
    max_resid_t4 = 0.0
    for a in np.linspace(0.01, 100.0, 20):
        ratio = unruh_temperature(a) / a
        resid = abs(ratio - universal)
        max_resid_t4 = max(max_resid_t4, resid)
    print(f"  max |T_Unruh/a - 1/(2 pi)| over sweep = {max_resid_t4:.3e}")
    t4_ok = max_resid_t4 < 1e-15
    print(f"  STATUS: {'PASS' if t4_ok else 'FAIL'}")
    print()

    # ----- Test 5: Bisognano-Wichmann Delta = exp(-2 pi K) -----
    print("-" * 72)
    print("TEST 5: two assigned finite diagonal matrices")
    print("        Delta = exp(-2 pi K)")
    print("-" * 72)
    print("Toy: K = diag(0, 1, 2, 3), a supplied matrix, not a boost realization.")
    K = np.diag([0.0, 1.0, 2.0, 3.0])
    Delta = np.diag([math.exp(-2 * math.pi * k) for k in [0.0, 1.0, 2.0, 3.0]])
    Delta_via_exp = np.diag([math.exp(-2 * math.pi * k) for k in K.diagonal()])
    diff_t5 = float(np.linalg.norm(Delta - Delta_via_exp))
    print(f"  K diagonal       = {K.diagonal()}")
    print(f"  Delta diagonal   = {Delta.diagonal()}")
    print(f"  exp(-2 pi K)     = {Delta_via_exp.diagonal()}")
    print(f"  ||Delta - exp(-2 pi K)|| = {diff_t5:.3e}")
    t5_ok = diff_t5 < 1e-15
    print(f"  STATUS: {'PASS' if t5_ok else 'FAIL'}")
    print()

    # ----- Summary -----
    print("=" * 72)
    print("SUMMARY")
    print("=" * 72)
    print(f"  Test 1 (assigned-period consistency):                {'PASS' if t1_ok else 'FAIL'}")
    print(f"  Test 2 (T_Unruh = a / (2 pi) sweep):               {'PASS' if t2_ok else 'FAIL'}")
    print(f"  Test 3 (SI scale at Earth gravity ~4e-20 K):       {'PASS' if t3_ok else 'FAIL'}")
    print(f"  Test 4 (T_Unruh / a = 1/(2 pi) universal):         {'PASS' if t4_ok else 'FAIL'}")
    print(f"  Test 5 (assigned diagonal equality):  {'PASS' if t5_ok else 'FAIL'}")
    print()
    rescaling_ok = conditional_rescaling_checks()
    all_ok = t1_ok and t2_ok and t3_ok and t4_ok and t5_ok and rescaling_ok
    print(f"  OVERALL: {'PASS' if all_ok else 'FAIL'}")
    print()
    print("Finite arithmetic and assigned-matrix consistency only.")
    print("No physical vacuum, boost realization or BW identity is established.")
    if not all_ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
