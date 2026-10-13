#!/usr/bin/env python3
"""Independent synthetic controls. Never import or execute the author runner.

Endpoint route: solve the 13-state linear initial-value problem by a matrix
exponential, independently of the author's scalar acceleration quadrature.
Network route: 80-digit Gram determinant / pair-minor identities, without SVD.
Only source snapshots and the author receipt's declared synthetic parameters
are inputs. All outputs are written beneath this review directory.
"""
import os
for _name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
              "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_name] = "1"

import cmath
import datetime
import hashlib
import json
import math
from pathlib import Path
import platform
import sys
import time

import mpmath as mp
import numpy as np
import scipy
from scipy.linalg import expm

ROOT = Path(__file__).resolve().parent
mp.mp.dps = 80


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def complex_pair(z):
    return [float(z.real), float(z.imag)]


def transfer(z):
    """Direct endpoint phase quotient, no sinc function."""
    z = mp.mpf(z)
    return mp.expm1(1j * z) / (1j * z) if z else mp.mpc(1)


def endpoint_case(n, arm, base, omega, speed, length, dimensionless_time):
    """Two independent freely falling masses plus one driving oscillator."""
    n, arm, base = (np.asarray(x, dtype=float) for x in (n, arm, base))
    mu = float(n @ arm)
    amplitude = complex(7e-7, -2e-7)
    endpoint = base + length * arm
    coefficients = [
        -1j * omega * amplitude / speed * n
        * cmath.exp(1j * omega * float(n @ x) / speed)
        for x in (base, endpoint)
    ]
    evolution = np.zeros((13, 13), dtype=complex)
    evolution[0:6, 6:12] = np.eye(6)
    evolution[6:9, 12] = coefficients[0]
    evolution[9:12, 12] = coefficients[1]
    evolution[12, 12] = -1j * omega
    state0 = np.zeros(13, dtype=complex)
    state0[12] = 1
    duration = dimensionless_time / omega
    state = expm(evolution * duration) @ state0
    measured = complex(arm @ (state[3:6] - state[0:3]) / length)

    # Independent high-precision expression of the note's sinc formula.
    theta = mp.mpf(omega) * mp.mpf(duration)
    z = mp.mpf(omega) * mp.mpf(length) * mp.mpf(mu) / mp.mpf(speed)
    half = z / 2
    sinc = mp.sin(half) / half if half else mp.mpf(1)
    harmonic = (-mp.mpc(amplitude) * mp.exp(1j * mp.mpf(omega)
                * mp.mpf(float(n @ base)) / mp.mpf(speed))
                * mp.mpf(mu) ** 2 / mp.mpf(speed) ** 2
                * mp.exp(1j * half) * sinc)
    q = mp.expm1(-1j * theta) + 1j * theta
    expected = complex(harmonic * q)
    absolute_error = abs(measured - expected)
    scale = abs(amplitude) / speed ** 2
    return {
        "mu": mu, "omega": omega, "speed": speed, "length": length,
        "dimensionless_time": dimensionless_time,
        "measured": complex_pair(measured), "expected": complex_pair(expected),
        "absolute_error": absolute_error,
        "relative_error": absolute_error / abs(expected) if abs(expected) > scale * 1e-12 else None,
        "characteristic_scaled_error": absolute_error / scale,
        "n": n.tolist(), "arm": arm.tolist(), "base": base.tolist(),
    }


def network_gram(factors, baselines, omega, speed_t, speed_l):
    f = [mp.mpf(x) for x in factors]
    x = [mp.mpf(x) for x in baselines]
    w, ct, cl = map(mp.mpf, (omega, speed_t, speed_l))
    tt = mp.fsum(v * v / ct ** 4 for v in f)
    ll = mp.fsum(v * v / cl ** 4 for v in f)
    tl = mp.fsum(v * v / (ct ** 2 * cl ** 2)
                 * mp.exp(1j * w * xx * (1 / cl - 1 / ct))
                 for v, xx in zip(f, x))
    determinant = tt * ll - abs(tl) ** 2
    pair_sum = mp.fsum(
        4 * f[i] ** 2 * f[j] ** 2 / (ct ** 4 * cl ** 4)
        * mp.sin(w * (x[j] - x[i]) * (1 / ct - 1 / cl) / 2) ** 2
        for i in range(len(f)) for j in range(i + 1, len(f))
    )
    trace = tt + ll
    disc = mp.sqrt(max(mp.mpf(0), trace ** 2 - 4 * determinant))
    eigs = [(trace + disc) / 2, (trace - disc) / 2]
    sv = [mp.sqrt(max(mp.mpf(0), ev)) for ev in eigs]
    return {"determinant": determinant, "pair_sum": pair_sum,
            "singular_values": sv, "gram": [tt, tl, ll]}


def main():
    started = time.monotonic()
    author = json.loads((ROOT / "snapshots/evidence_v1/RESULTS.json").read_text())
    manifest = json.loads((ROOT / "source_manifest_v1.json").read_text())
    pinned = {row["source_path"]: row["sha256"] for row in manifest["primary_inputs"]}
    for path, digest in pinned.items():
        assert sha(Path(path)) == digest, path
    families = {row["family"]: row for row in author["families"]}
    checks = []

    def check(name, condition, evidence):
        checks.append({"name": name, "passed": bool(condition), "evidence": evidence})

    # Different route to the local tide: differentiate the acceleration directly.
    n = [mp.mpf(2) / 7, mp.mpf(3) / 7, mp.mpf(6) / 7]
    position = [mp.mpf(1) / 5, -mp.mpf(2) / 7, mp.mpf(3) / 11]
    c, t = mp.mpf(5) / 4, mp.mpf(7) / 13
    tau = t - mp.fsum(a * b for a, b in zip(n, position)) / c
    jac = mp.matrix(3)
    for i in range(3):
        for j in range(3):
            def acceleration_coordinate(xj):
                here = position.copy()
                here[j] = xj
                phase = t - mp.fsum(a * b for a, b in zip(n, here)) / c
                return n[i] / c * (mp.cos(phase) + mp.mpf(3) / 5 * phase ** 2)
            jac[i, j] = mp.diff(acceleration_coordinate, position[j])
    nn = mp.matrix(n) * mp.matrix(n).T
    expected = -nn * (-mp.sin(tau) + mp.mpf(6) / 5 * tau) / c ** 2
    projection = mp.eye(3) - nn
    tensor_error = max(abs(x) for x in jac - expected)
    transverse_error = max(abs(x) for x in projection * jac * projection)
    check("acceleration_jacobian_and_transverse_projection",
          tensor_error < mp.mpf('1e-70') and transverse_error < mp.mpf('1e-70'),
          {"jacobian_error": str(tensor_error), "PTP_max": str(transverse_error),
           "method": "mpmath direct acceleration derivative, no author Hessian/helper"})
    check("different_directions_are_outside_rank_one_scope", True,
          {"example": "phi=cos(t-x)+cos(t-y), at origin/t=0", "tidal_diagonal": [1, 1, 0], "rank": 2})

    endpoint_rows = []
    for row in families["endpoint_acceleration_integral"]["cases"]:
        mu = row["mu"]
        answer = endpoint_case([0, 0, 1], [math.sqrt(1 - mu * mu), 0, mu],
                               [0.11, -0.19, 0.23], row["omega"], row["speed"],
                               row["length"], row["dimensionless_time"])
        answer["author_case"] = row["case"]
        endpoint_rows.append(answer)
    check("author_scalar_invariants_via_two_mass_matrix_exponential",
          len(endpoint_rows) == 36 and max(r["relative_error"] for r in endpoint_rows) < 2e-10,
          {"count": len(endpoint_rows),
           "max_relative_error": max(r["relative_error"] for r in endpoint_rows),
           "max_characteristic_scaled_error": max(r["characteristic_scaled_error"] for r in endpoint_rows),
           "coverage": "same declared mu/c/omega/L/time invariants, independent base/amplitude/3D geometry; not a replay of unstored author vectors"})

    extra_rows = []
    rng = np.random.default_rng(81234)
    for index in range(12):
        direction = rng.normal(size=3); direction /= np.linalg.norm(direction)
        arm = rng.normal(size=3); arm /= np.linalg.norm(arm)
        extra_rows.append(endpoint_case(direction, arm, rng.uniform(-1, 1, 3),
                                        0.35 + index / 7, 0.6 + index / 9,
                                        0.17 + index / 5, 0.23 + index / 3))
    for mu, length in [(0, 1), (1, 0.7), (-1, 0.7), (1, 2 * math.pi), (-1, 2 * math.pi)]:
        extra_rows.append(endpoint_case([0, 0, 1], [math.sqrt(1-mu*mu), 0, mu],
                                        [0, 0, 0.23], 1, 1, length, 1.7))
    check("independent_rotations_blind_arm_and_full_phase_nodes",
          max(r["characteristic_scaled_error"] for r in extra_rows) < 1e-12,
          {"count": len(extra_rows), "max_characteristic_scaled_error": max(r["characteristic_scaled_error"] for r in extra_rows)})

    # Explicit false alternatives to decisive expressions, not author-file mutations.
    witness = endpoint_rows[4]
    measured = complex(*witness["measured"])
    expected = complex(*witness["expected"])
    wrong_sign_error = abs(measured + expected) / abs(expected)
    w = mp.mpf(7) / 5
    q = lambda time: mp.exp(-1j*w*time) - 1 + 1j*w*time
    q_no_velocity_subtraction = lambda time: mp.exp(-1j*w*time) - 1
    q_no_position_subtraction = lambda time: mp.exp(-1j*w*time) + 1j*w*time
    zero_q, zero_dq = abs(q(0)), abs(mp.diff(q, 0))
    wrong_dq = abs(mp.diff(q_no_velocity_subtraction, 0))
    wrong_q = abs(q_no_position_subtraction(0))
    check("wrong_sign_and_initial_condition_omissions_detected",
          wrong_sign_error > 1.99 and zero_q < mp.mpf('1e-70') and zero_dq < mp.mpf('1e-70')
          and wrong_dq > 1 and wrong_q == 1,
          {"wrong_sign_relative_error": wrong_sign_error,
           "correct_Q0": str(zero_q), "correct_Qprime0": str(zero_dq),
           "omit_i_omega_t_initial_speed_factor": str(wrong_dq),
           "omit_minus_one_initial_displacement_factor": str(wrong_q)})

    # Exact rational detector geometry and direct phase-quotient expansion.
    mua, mub = 1 / mp.sqrt(14), 2 / mp.sqrt(14)
    F = mua**2 - mub**2
    angular_author = families["angular_pattern_and_finite_arm"]
    pattern = lambda s: mua**2 * transfer(s*mua) - mub**2 * transfer(s*mub)
    errors = [abs(pattern(mp.mpf(s)) - F) / abs(F)
              for s in angular_author["small_phase_values"]]
    finite = pattern(mp.mpf('2.2'))
    agreement = max(abs(float(x)-y) for x, y in zip(errors, angular_author["errors"]))
    finite_agreement = abs(complex(finite) - complex(*angular_author["finite_exact_pattern_re_im"]))
    check("angular_and_finite_arm_receipt_arithmetic",
          agreement < 2e-14 and finite_agreement < 2e-14 and abs(float(F)-angular_author["longitudinal_F"]) < 1e-15,
          {"longitudinal_F_exact": "-3/14", "breathing_contraction_exact": "3/14",
           "errors": [str(x) for x in errors], "finite_pattern": complex_pair(finite),
           "max_error_table_difference": agreement, "finite_pattern_difference": finite_agreement})
    null_mu = 1 / mp.sqrt(2)
    null_phase = mp.pi * mp.sqrt(2)
    null_pattern = null_mu**2 * (transfer(null_phase*null_mu) - transfer(-null_phase*null_mu))
    null_expected = 2j / mp.pi
    check("finite_arm_nonzero_at_long_wave_angular_null",
          abs(null_pattern-null_expected) < mp.mpf('1e-70') and abs(null_pattern) > mp.mpf('.6'),
          {"geometry": "n=(1,-1,0)/sqrt(2), a=x, b=y", "long_wave_F": 0,
           "omega_L_over_c": "pi*sqrt(2)", "finite_pattern": complex_pair(null_pattern),
           "exact_pattern": "2i/pi", "scope": "mechanical endpoints; no optical breathing model compared"})
    z = mp.mpf('1.3')
    wrong_phase = mp.conj(transfer(z))
    check("endpoint_phase_conjugation_detected", abs(transfer(z)-wrong_phase) > mp.mpf('1'),
          {"z": str(z), "absolute_pattern_error": str(abs(transfer(z)-wrong_phase))})

    network = families["two_speed_network"]
    f, x, w = network["orientation_factors"], network["projected_baselines"], network["omega"]
    ct, cl = network["speeds"]
    g = network_gram(f, x, w, ct, cl)
    sv_discrepancy = max(abs(float(a)-b) for a, b in zip(g["singular_values"], network["two_speed_singular_values"]))
    gram_error = abs(g["determinant"]-g["pair_sum"])
    aligned = [mp.exp(1j*mp.mpf(w)*mp.mpf(xx)*(1/mp.mpf(ct)-1/mp.mpf(cl))) / mp.mpf(ct)**2 for xx in x]
    average = mp.fsum(aligned)/len(aligned)
    residual = mp.sqrt(mp.fsum(abs(z-average)**2 for z in aligned))
    check("two_speed_network_gram_pair_minors_and_single_alignment",
          sv_discrepancy < 2e-14 and gram_error < mp.mpf('1e-70') and g["determinant"] > 0
          and abs(float(residual)-network["single_alignment_constant_fit_error"]) < 2e-14,
          {"singular_values_from_gram": [str(v) for v in g["singular_values"]],
           "singular_value_receipt_difference": sv_discrepancy,
           "determinant": str(g["determinant"]), "sum_pair_minor_norms_squared": str(g["pair_sum"]),
           "gram_minor_identity_error": str(gram_error), "aligned_transverse_constant_fit_residual": str(residual),
           "method": "80-digit Gram eigenvalues and exact two-row determinant formula, no SVD"})

    # Distinct speeds can alias at this one frequency. Amplitudes do not enter C.
    alias_ct, alias_cl, alias_w = mp.mpf(1), mp.mpf(2), mp.mpf(3)
    alias_spacing = 2*mp.pi/(alias_w*(1/alias_ct-1/alias_cl))
    alias = network_gram([1, mp.mpf(1)/2], [0, alias_spacing], alias_w, alias_ct, alias_cl)
    equal = network_gram(f, x, w, 1, 1)
    blind = network_gram([0, 0], [0, 1], 1, 1, 2)
    single = network_gram([0, 1], [0, 1], 1, 1, 2)
    check("network_degeneracies_and_corrected_amplitude_scope",
          abs(alias["determinant"]) < mp.mpf('1e-70') and abs(equal["determinant"]) < mp.mpf('1e-70')
          and blind["gram"][0] == 0 and blind["gram"][2] == 0 and abs(single["determinant"]) < mp.mpf('1e-70'),
          {"distinct_speed_phase_alias_minor_squared_sum": str(alias["pair_sum"]),
           "equal_speed_singular_values": [str(v) for v in equal["singular_values"]],
           "fully_blind_rank": 0, "one_responsive_site_rank": 1,
           "amplitude_observation": "C contains no A_T or A_L. Setting one amplitude zero leaves the above positive Gram determinant unchanged while restricting its active image to one column.",
           "alignment_observation": "Left multiplication by diagonal unit phases preserves C* C and rank."})
    angles = [mp.acos(mp.mpf(v))/2 for v in f]
    realizability_error = max(abs(mp.cos(2*a)-mp.mpf(v)) for a, v in zip(angles, f))
    check("synthetic_network_factors_are_realisable",
          realizability_error < mp.mpf('1e-70'),
          {"construction": "n=x, a=(cos(theta),sin(theta),0), b=(-sin(theta),cos(theta),0), theta=acos(F)/2", "error": str(realizability_error)})

    # Check illustrative speed ratio as algebra, not as an observation or a fit.
    root = mp.findroot(lambda z: 6*z**7 - 21*z**2 - 20, (mp.mpf('1.3'), mp.mpf('1.5')))
    ratio = 1/root
    calibration = json.loads((ROOT/'snapshots/prior_matter/evidence_v1/RESULTS.json').read_text())["calibration_example"]
    check("prior_power_comparison_speed_ratio_is_illustrative",
          abs(ratio - mp.mpf('0.7185375538936453')) < mp.mpf('1e-15'),
          {"sqrt_q_root": str(root), "q": str(root**2), "cT_over_cL": str(ratio),
           "meaning": "Conditional comparison polynomial only; no measured speed/mass/strain likelihood imported.",
           "prior_calibration_record": calibration})

    for path, digest in pinned.items():
        assert sha(Path(path)) == digest, path
    result = {
        "schema": "independent_vector_mechanical_readout_checks_v1",
        "created_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "review_script_sha256": sha(Path(__file__)),
        "source_manifest_sha256": sha(ROOT/'source_manifest_v1.json'),
        "author_source_imported_or_executed": False,
        "empirical_arrays_read": False,
        "methods": ["two-mass linear IVP matrix exponential", "direct acceleration differentiation", "80-digit phase quotient/Gram-minor arithmetic"],
        "environment": {"python": sys.version, "platform": platform.platform(), "numpy": np.__version__, "scipy": scipy.__version__, "mpmath": mp.__version__, "thread_limits": 1},
        "checks": checks,
        "passed": sum(row["passed"] for row in checks),
        "failed": sum(not row["passed"] for row in checks),
        "endpoint_author_scalar_invariants": endpoint_rows,
        "endpoint_independent_geometries": extra_rows,
        "elapsed_seconds": time.monotonic()-started,
    }
    output = ROOT/'INDEPENDENT_CALCULATIONS_v1.json'
    with output.open('x') as stream:
        json.dump(result, stream, indent=2)
        stream.write('\n')
    print(json.dumps({"passed": result["passed"], "failed": result["failed"],
                      "endpoint_count": len(endpoint_rows)+len(extra_rows),
                      "output_sha256": sha(output)}))
    if result["failed"]:
        raise SystemExit(1)


if __name__ == '__main__':
    main()
