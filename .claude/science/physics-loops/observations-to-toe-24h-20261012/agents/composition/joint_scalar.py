#!/usr/bin/env python3
"""A frozen, conditional scalar/metric joint forward model, not a TOE fit.

Run from any directory. All output paths are explicit. Sources are hash checked.
No network, fitting to held-out data, repo mutations, or large computation.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from decimal import Decimal, localcontext
import hashlib
import json
import math
from pathlib import Path
import sys

import numpy as np

BASELINE = "7f9fac6cb89c6c7b86cde4f5716870d0dfc4b9de"
ME_U = 5.485799090441e-4  # CODATA 2022, preserved NIST allascii table.
K_E3_E2 = -6.95  # d ln(nu_E3/nu_E2) / d ln(alpha), Lange Table II context.
EPSILON = 1.65e-10  # Positive solar depth cosine amplitude at perihelion.
G_SUN = 5.9e-3  # Measured solar orbital acceleration normalization, m/s^2.
MU_M, SIG_STAT_M, SIG_SYS_M = -1.5e-15, 2.3e-15, 1.5e-15
SIG_M = math.hypot(SIG_STAT_M, SIG_SYS_M)
MU_O, SIG_O = -9.7e-8, 7.7e-8
CHI2_CUT = 5.991464547107979  # P(chi2_2 <= c)=0.95.

# Atomic weights in u. Normal-material means/interval midpoints, not assay data.
# CIAAW 2024 source is preserved. Solar isotopes use rounded masses explicitly.
ELEMENTS = {
    "H": (1, 1.008), "He4": (2, 4.002602), "He3": (2, 3.016029),
    "C12": (6, 12.0), "N14": (7, 14.003074), "O16": (8, 15.994915),
    "O": (8, 15.9994), "Si": (14, 28.085), "Mg": (12, 24.3055),
    "Fe": (26, 55.845), "Be": (4, 9.0121831), "Ti": (22, 47.867),
    "Al": (13, 26.9815384), "V": (23, 50.9415),
    "Pt": (78, 195.084), "Rh": (45, 102.90549),
}


def charge(symbol: str) -> np.ndarray:
    """[electron-rest-mass, EM] sensitivities in the declared approximation.

    Electron binding is omitted. Qem is Damour--Donoghue eq. (76), F_A=1,
    using mean atomic weight in A as their natural-mixture approximation.
    This is not an exact nuclear/atomic response calculation.
    """
    z, a = ELEMENTS[symbol]
    return np.array([ME_U * z / a,
                     1e-4 * (-1.4 + 8.2*z/a + 7.7*z*(z-1)/a**(4/3))])


def mix(parts: dict[str, float]) -> np.ndarray:
    assert abs(sum(parts.values()) - 1) < 1e-12
    return sum((fraction * charge(name) for name, fraction in parts.items()),
               np.zeros(2))


def compound(numbers: dict[str, int]) -> np.ndarray:
    mass = sum(number * ELEMENTS[name][1] for name, number in numbers.items())
    return mix({name: number * ELEMENTS[name][1] / mass
                for name, number in numbers.items()})


def solar(path: Path, residual: str = "Fe") -> tuple[np.ndarray, dict]:
    rows = []
    for line in path.read_text().splitlines():
        try:
            numbers = [float(token) for token in line.split()]
        except ValueError:
            continue
        if len(numbers) == 12:
            rows.append(numbers)
    data = np.array(rows)
    assert len(data) > 1000 and np.all(np.diff(data[:, 0]) >= 0)
    # Extend missing central/tiny surface shells with adjacent composition.
    m = np.r_[0., data[:, 0], 1.]
    composition = np.vstack([data[0, 6:], data[:, 6:], data[-1, 6:]])
    integrals = np.trapezoid(composition, m, axis=0)
    # Independent explicit shell trapezoid sum, not a second library call.
    direct = sum((m[i+1]-m[i])*(composition[i+1]+composition[i])/2
                 for i in range(len(m)-1))
    assert np.max(np.abs(direct-integrals)) < 1e-13
    names = ["H", "He4", "He3", "C12", "N14", "O16"]
    parts = dict(zip(names, map(float, integrals)))
    remainder = 1 - sum(parts.values())
    assert 0 < remainder < 0.03
    parts[residual] = remainder
    q = mix(parts)
    return q, {
        "source_file": path.name,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "rows": len(data), "integrated_mass_fractions": parts,
        "central_missing_mass": float(data[0, 0]),
        "surface_missing_mass": float(1-data[-1, 0]),
        "surface_hydrogen": float(data[-1, 6]),
        "residual_metals_proxy": residual,
        "sensitivity": q.tolist(),
    }


def alpha(parameters, q) -> float:
    g, x, e = parameters
    return float(g + x*q[0] + e*q[1])


def observables(parameters, qearth, qsun, qti, qpt) -> dict:
    """Newtonian scalar+metric observables, with explicit dynamical GM ruler.

    The common metric is universal. The source/test scalar product supplies
    the additional force. The Sun's GM ruler is fixed by the Earth orbit;
    D=1+alpha_E*alpha_S converts G_* M to this dynamical normalization.
    """
    g, x, e = parameters
    ae, ass = alpha(parameters, qearth), alpha(parameters, qsun)
    at, ap = alpha(parameters, qti), alpha(parameters, qpt)
    denominator = 1 + ae * (at + ap)/2
    dynamic = 1 + ae*ass
    # Compute the difference from charge contrast, avoiding cancellation of g.
    contrast = float((qti-qpt) @ np.array([x, e]))
    eta = ae * contrast / denominator
    ko = -K_E3_E2*e*ass/dynamic
    beta = {}
    for body in ["Ti", "Al"]:
        delta = float((charge("Be")-charge(body)) @ np.array([x, e]))
        beta["Be_"+body] = ass*delta/dynamic
    # This clock response is exact within the declared electronic approximation
    # only on e=0: no uncertain nuclear magnetic alpha slope is imported.
    kh = ass*x/dynamic if e == 0 else None
    return {
        "parameters_g_x_e": list(map(float, parameters)),
        "alpha_Earth": ae, "alpha_Sun": ass,
        "microscope_eta": eta, "clock_k_E3_E2": ko,
        "clock_annual_E3_E2": EPSILON*ko,
        "clock_k_optical_hyperfine_e0": kh,
        "clock_annual_optical_hyperfine_e0": None if kh is None else EPSILON*kh,
        "Sun_Earth_GM_conversion": dynamic,
        "solar_BeTi_fraction": beta["Be_Ti"],
        "solar_BeAl_fraction": beta["Be_Al"],
        "solar_BeAl_acceleration_fm_s2": G_SUN*beta["Be_Al"]*1e15,
        "chi2_calibration": ((eta-MU_M)/SIG_M)**2 + ((ko-MU_O)/SIG_O)**2,
    }


def central_fiber(r: float, p: float, k: float,
                  qearth, qsun, qti, qpt):
    """Exact analytic chart for e != 0, p != 0, S != 0.

    Let x=r e, a=alpha_E, w=a e, v=e^2. A=deltaQ dot(r,1),
    B=(Qbar-QE) dot(r,1), S=(QS-QE) dot(r,1), Q=QE dot(r,1).
    p = w A/(1+w^2/v+w B)
    z = k/(-K) = (w+v S)/(1+w^2/v+w S).
    Thus v=w H, H=[z(A/p+S-B)-1]/S,
    w=1/(A/p-B-1/H).  Reflection of all couplings is a second point.
    Decimal avoids cancellation on the very thin calibrated surfaces.
    """
    with localcontext() as context:
        context.prec = 60
        d = lambda z: Decimal(str(float(z)))
        rr, pp, zz = d(r), d(p), d(k)/d(-K_E3_E2)
        dot = lambda arr: d(arr[0])*rr+d(arr[1])
        aa = dot(qti-qpt)
        bb = dot((qti+qpt)/2-qearth)
        ss = dot(qsun-qearth)
        qq = dot(qearth)
        if pp == 0 or ss == 0:
            return None
        hh = (zz*(aa/pp+ss-bb)-1)/ss
        if hh == 0:
            return None
        denom = aa/pp-bb-1/hh
        if denom == 0:
            return None
        ww = 1/denom
        vv = ww*hh
        if vv <= 0:
            return None
        ee = vv.sqrt()
        gg = ww/ee-qq*ee
        return np.array([float(gg), float(rr*ee), float(ee)])


def checked_sources(source_dir: Path) -> dict:
    manifest = json.loads((source_dir/"download_manifest.json").read_text())
    for row in manifest["sources"]:
        path = source_dir/row["file"]
        assert hashlib.sha256(path.read_bytes()).hexdigest() == row["sha256"], path
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    runtime = args.source_dir.parent
    deadline = json.loads((runtime/"DEADLINE.json").read_text())
    if datetime.now(timezone.utc).timestamp() >= deadline["deadline_epoch"]:
        raise RuntimeError("Campaign deadline reached")
    for stop in ["STOP_REQUESTED", "USER_STOP_REQUESTED"]:
        if (runtime/stop).exists():
            raise RuntimeError(f"Campaign stop marker: {stop}")
    manifest = checked_sources(args.source_dir)

    qti = mix({"Ti": .90, "Al": .06, "V": .04})
    qpt = mix({"Pt": .90, "Rh": .10})
    qearth = .32*charge("Fe") + .68*compound({"Si": 1, "O": 2})
    solar_variants = [solar(args.source_dir/name, residual)
                      for name in ["bs05op.dat", "bs05_agsop.dat"]
                      for residual in ["Fe", "O"]]
    qsun = solar_variants[0][0]
    sm, se = qsun-qearth
    bm = (charge("Be")-charge("Al"))[0]
    bm_ti = (charge("Be")-charge("Ti"))[0]
    assert sm > 0 and bm < 0

    witnesses = []
    for t in [0., .001, .01, .03, .1]:
        params = [-qearth[0]*t, t, 0.]
        row = observables(params, qearth, qsun, qti, qpt)
        assert abs(row["microscope_eta"]) < 1e-28
        assert row["clock_k_E3_E2"] == 0
        assert abs(row["solar_BeAl_fraction"]-sm*bm*t*t) < 1e-24
        assert abs(row["clock_k_optical_hyperfine_e0"]-sm*t*t) < 1e-20
        row["Ross_summary_pull"] = (row["solar_BeAl_acceleration_fm_s2"]-.66)/.61
        row["older_BeTi_Sun_summary_pull"] = (row["solar_BeTi_fraction"]+3.1e-13)/4.7e-13
        row["E3Cs_marginal_summary_pull"] = (row["clock_k_optical_hyperfine_e0"]+4e-8)/4.4e-7
        witnesses.append(row)

    # Pointwise allowed-set chart samples: genuine simultaneous central fits.
    # The actual continuous chart is the formula, not this finite list.
    center = []
    for r in [-100., -10., 0., 1., 3., 5., 6., 10., 30., 50., 60., 100.]:
        params = central_fiber(r, MU_M, MU_O, qearth, qsun, qti, qpt)
        if params is None:
            continue
        if abs(params[0]) > .001 or max(abs(params[1:])) > .1:
            continue
        row = observables(params, qearth, qsun, qti, qpt)
        assert abs(row["microscope_eta"]-MU_M) < 5e-23
        assert abs(row["clock_k_E3_E2"]-MU_O) < 1e-19
        reflected = observables(-params, qearth, qsun, qti, qpt)
        for key in ["microscope_eta", "clock_k_E3_E2", "solar_BeAl_fraction"]:
            assert row[key] == reflected[key]
        row["r_x_over_e"] = r
        row["Ross_summary_pull"] = (row["solar_BeAl_acceleration_fm_s2"]-.66)/.61
        center.append(row)

    # Analytic profile of additive MICROSCOPE systematic, verified by stationary
    # point and its separate measurement+prior cost.
    profile_checks = []
    for prediction in [0., -1e-14, 1e-14]:
        b = (MU_M-prediction)*SIG_SYS_M**2/(SIG_STAT_M**2+SIG_SYS_M**2)
        profile = ((MU_M-prediction-b)/SIG_STAT_M)**2 + (b/SIG_SYS_M)**2
        shortcut = ((MU_M-prediction)/SIG_M)**2
        assert abs(profile-shortcut) < 1e-13
        profile_checks.append({"prediction": prediction, "systematic_hat": b, "cost": profile})

    # The Earth-neutral electron branch has a fixed sign, and an exact full
    # interval image as t^2 ranges from 0 to L^2.  No grid is used for bounds.
    branch_coefficient = G_SUN*sm*bm*1e15  # acceleration fm/s^2 per t^2
    ross_lower, ross_upper = .66-1.96*.61, .66+1.96*.61
    t_ross = math.sqrt(ross_lower/branch_coefficient)
    # The nuisance sensitivity model does not assign these variants probabilities.
    variants = []
    for core in [.30, .32, .34]:
        for mantle_name, mantle in [
            ("SiO2", compound({"Si": 1, "O": 2})),
            ("MgSiO3", compound({"Mg": 1, "Si": 1, "O": 3}))]:
            earth_var = core*charge("Fe")+(1-core)*mantle
            for solar_q, solar_info in solar_variants:
                delta = solar_q[0]-earth_var[0]
                coeff = G_SUN*delta*bm*1e15
                variants.append({
                    "core_mass_fraction": core, "mantle": mantle_name,
                    "solar_file": solar_info["source_file"],
                    "solar_residual": solar_info["residual_metals_proxy"],
                    "Earth_Qme": float(earth_var[0]),
                    "Sun_Qme": float(solar_q[0]),
                    "source_difference_Qme": float(delta),
                    "solar_BeAl_fm_s2_per_t_squared": float(coeff),
                    "Ross_marginal_95_t_max": math.sqrt(ross_lower/coeff),
                })

    # Data-independent relation on e=0: h_BeAl = DeltaQme * k_opt/hyp.
    # Its inferred clock bound therefore cancels source-model uncertainty.
    clock_upper_from_ross = (ross_lower/(G_SUN*1e15))/bm
    # Nominal full-box (deliberately loose) guaranteed outer interval for full
    # three-coupling forward image: actual calibrated image is a subset.
    max_ass = .001+.1*(abs(qsun[0])+abs(qsun[1]))
    max_ae = .001+.1*(abs(qearth[0])+abs(qearth[1]))
    max_diff = .1*sum(abs(charge("Be")-charge("Al")))
    full_box_bound = max_ass*max_diff/(1-max_ass*max_ae)

    out = {
        "status": "conditional on accepted new axiom; not retained on the actual current surface",
        "target_claim_type": "bounded_theorem",
        "baseline": BASELINE, "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "numpy_version": np.__version__, "python_version": sys.version.split()[0],
        "data_sources": manifest["sources"],
        "charges": {"Earth": qearth.tolist(), "Sun": qsun.tolist(),
                    "TiAlV": qti.tolist(), "PtRh": qpt.tolist(),
                    "TiAlV_minus_PtRh": (qti-qpt).tolist(),
                    "Be_minus_Al": (charge("Be")-charge("Al")).tolist(),
                    "Be_minus_Ti": (charge("Be")-charge("Ti")).tolist()},
        "solar_integrals": [row[1] for row in solar_variants],
        "calibration": {"eta_mean": MU_M, "eta_combined_sigma": SIG_M,
                        "clock_ratio_k_mean": MU_O, "clock_ratio_k_sigma": SIG_O,
                        "two_observable_95_acceptance_cut": CHI2_CUT,
                        "null_chi2": witnesses[0]["chi2_calibration"]},
        "earth_neutral_electron_branch": {
            "t_interval": [-.1, .1],
            "g_rule": "-Earth_Qme*t", "x_rule": "t", "e": 0,
            "solar_BeAl_fraction_interval": [float(sm*bm*.1**2), 0.],
            "solar_BeAl_acceleration_fm_s2_interval": [float(branch_coefficient*.1**2), 0.],
            "optical_hyperfine_k_interval": [0., float(sm*.1**2)],
            "optical_hyperfine_annual_interval": [0., float(EPSILON*sm*.1**2)],
            "witnesses": witnesses,
        },
        "central_fiber_samples": center,
        "full_three_parameter_region": {
            "representation": "Exact inequality and analytic nonsingular fibers in note/code; singular fibers specified in note. No claim of globally sharp numerical projection.",
            "BeAl_fraction_guaranteed_outer_interval_from_full_box": [-full_box_bound, full_box_bound],
            "BeAl_fraction_attainable_subinterval_from_blind_branch": [float(sm*bm*.1**2),0.],
        },
        "heldout_Ross": {
            "direct_acceleration_fm_s2_mean": .66, "sigma": .61,
            "marginal_central_95_interval_fm_s2": [ross_lower, ross_upper],
            "not_used": "paper's 2.1e-13 magnitude headline is not reconstructed as a central-value Gaussian confidence bound",
            "earth_neutral_electron_branch_t_absolute_upper_95": t_ross,
            "optical_hyperfine_k_upper_on_branch": clock_upper_from_ross,
            "optical_hyperfine_annual_upper_on_branch": EPSILON*clock_upper_from_ross,
        },
        "source_model_sensitivity_not_probability": variants,
        "profiled_microscope_systematic_checks": profile_checks,
        "checks": {
            "source_hashes": "pass", "solar_shell_quadrature": "pass",
            "blind_branch_equations_and_interval": "pass", "central_fiber_substitution": "pass",
            "common_sign_reflection": "pass", "profile_systematic": "pass",
            "independent_review": "pending", "raw_experiment_likelihood": "not run",
        },
    }
    args.output.write_text(json.dumps(out, indent=2, allow_nan=False)+"\n")
    print("conditional on accepted new axiom; not retained on the actual current surface")
    print("source model and observations are imports; this is an explicit joint calculation")
    print("Earth/Sun Qme:", qearth[0], qsun[0], "difference:", sm)
    print("MICROSCOPE alloy DeltaQ:", qti-qpt)
    print("null calibration chi2:", witnesses[0]["chi2_calibration"], "cut:", CHI2_CUT)
    for row in witnesses:
        print("t=%g eta=% .3e clock=% .3e Sun BeAl=% .6g fm/s2, Ross pull=% .4f" %
              (row["parameters_g_x_e"][1], row["microscope_eta"], row["clock_k_E3_E2"],
               row["solar_BeAl_acceleration_fm_s2"], row["Ross_summary_pull"]))
    print("central-fiber joint fits:", len(center), "; exact region given parametrically")
    print("Ross marginal 95% electron-branch |t| <=", t_ross)
    print("source-cancelled optical/hyperfine annual upper:", EPSILON*clock_upper_from_ross)
    print("TOTAL: PASS=6 FAIL=0; author checks only, independent review pending")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
