#!/usr/bin/env python3
"""Reviewer-owned check. Never imports or executes the author runner.

Read only exact source snapshots. Outputs are confined to this review directory.
Use one BLAS thread; no parameter fitting beyond recomputing the frozen intercepts.
"""
from pathlib import Path
import collections
import datetime
import gzip
import hashlib
import io
import json
import math
import sys
import time

import numpy as np
import scipy
from scipy.integrate import solve_ivp
from scipy.linalg import lu_factor, lu_solve, solve_triangular
from scipy.special import roots_legendre
import sympy as sy

ROOT = Path(__file__).resolve().parent
SNAP = ROOT / "snapshots_v1"
CHECKS = []


def digest(b):
    return hashlib.sha256(b).hexdigest()


def check(name, condition, **evidence):
    CHECKS.append({"name": name, "pass": bool(condition), **evidence})


def close(name, actual, expected, tol):
    a, b = np.asarray(actual), np.asarray(expected)
    error = float(np.max(np.abs(a-b))) if a.shape == b.shape else float("inf")
    check(name, a.shape == b.shape and error <= tol, max_absolute_error=error,
          tolerance=tol, shape=list(a.shape))
    return error


def symbolic_controls():
    # Start with the physical acceleration obtained by differentiating R_J=A R.
    a, y, s, r = sy.symbols("a y s r", real=True)
    numerator = sy.Rational(1, 2) + 3*a/2 + 2*y + 3*(1-a)*s/2 + (1-3*a)*r/2
    bound = (1+a)/(2*(1-a))
    perp = sy.symbols("perp", nonnegative=True)
    remainder = sy.expand((numerator-bound*(1+y)**2).subs(s, y*y/(3*a)+perp))
    coefficients = [sy.factor(remainder.coeff(y, k)) for k in (0, 1, 2)]
    completed = (1-3*a)*(y+a)**2/(2*a*(1-a)) + 3*(1-a)*perp/2 + (1-3*a)*r/2
    check("independent_polynomial_coefficients_complete_square", sy.factor(remainder-completed) == 0,
          coefficients=[str(v) for v in coefficients])
    qstar = (1+a)/2
    check("equality_velocity_evolution", sy.factor(-(qstar-2)-sy.Rational(3, 2)*(1-a/3)) == 0)
    power = 2*(1-a)/(3-a)
    check("equality_physical_power_q", sy.factor((1-power)/power-bound) == 0)
    # Full source exchange: use 8 pi G=1 and differentiate Friedmann.
    H, rm, rr, vv, zv = sy.symbols("H rm rr vv zv")
    density_derivative = (-3*H+zv)*rm - 4*H*rr - 6*H*vv - zv*rm
    hdot = -rm/2 - 2*rr/3 - vv
    check("friedmann_constraint_derivative_with_correct_source", sy.expand(density_derivative-6*H*hdot) == 0)
    wrong = (-3*H+zv)*rm - 4*H*rr - 6*H*vv + zv*rm
    check("wrong_scalar_trace_sign_rejected_by_energy_exchange", sy.factor(wrong-6*H*hdot) == 2*rm*zv)
    # Arbitrary non-diagonal positive K and unsourced directions.
    K = sy.Matrix([[2, 1, 0], [1, 3, 1], [0, 1, 2]])
    alpha = sy.Matrix([sy.Rational(1, 50), sy.Rational(-1, 100), sy.Rational(1, 100)])
    av = (alpha.T*K.inv()*alpha)[0]
    equality_x = -K.inv()*alpha
    check("non_diagonal_K_equality_has_required_y_s", (alpha.T*equality_x)[0] == -av and (equality_x.T*K*equality_x)[0] == av)
    trials = []
    for xi in [sy.Matrix([sy.Rational(i, 10), sy.Rational(j, 10), sy.Rational(k, 10)])
               for i, j, k in [(1, 2, -1), (0, 0, 1), (-2, 1, 1), (1, 2, 0)]]:
        sv, yv, rv = (xi.T*K*xi)[0]/3, (alpha.T*xi)[0], sy.Rational(1, 5)
        om = 1-sv-rv
        qv = (om/2+rv+2*sv+2*yv+3*av*om/2)/(1+yv)**2
        check("non_diagonal_K_Cauchy_and_bound_"+str(len(trials)), sv-yv*yv/(3*av) >= 0 and qv >= (1+av)/(2*(1-av)))
        trials.append({"x": [str(v) for v in xi], "a": str(av), "Omega_s": str(sv), "y": str(yv), "q_J": str(qv)})
    return {"coefficient_derivation": [str(v) for v in coefficients], "non_diagonal_K_cases": trials}


def grid_controls(f, author):
    # Reconstruct the complete frozen grid, not just rows that passed the author's check.
    rows = []
    for av in f["couplings"]:
        for i in range(21):
            for j in range(21-i):
                ss, rr = i/20, j/20
                for t in f["projection_fractions"]:
                    yy = t*math.sqrt(3*av*ss)
                    # Physical acceleration expression expanded in independent variables.
                    num = .5 + 1.5*av + 2*yy + 1.5*(1-av)*ss + .5*(1-3*av)*rr
                    qv = num/(1+yy)**2
                    bv = (1+av)/(2-2*av)
                    residual = num - bv*(1+yy)**2
                    sq = 1.5*ss+.5*rr if av == 0 else ((1-3*av)*(yy+av)**2/(2*av*(1-av)) + 1.5*(1-av)*(ss-yy*yy/(3*av)) + .5*(1-3*av)*rr)
                    row = [av, ss, rr, t, yy, qv, residual, sq]
                    expected = author["square_identity_grid"]["rows"][len(rows)]
                    check("complete_grid_row_"+str(len(rows)), max(abs(x-z) for x,z in zip(row, expected)) < 3e-12
                          and qv >= bv-3e-12 and 1+yy > 0)
                    rows.append(row)
    check("complete_grid_cardinality", len(rows) == author["square_identity_grid"]["row_count"] == 5775)
    return {"rows": rows, "maximum_author_difference": float(np.max(np.abs(np.array(rows)-author["square_identity_grid"]["rows"]))) }


def evolution_controls(f, author):
    # Different variables and integrator: dimensional scalar momenta and fluid
    # densities; H is recomputed from Friedmann, never evolved via q*. 8 pi G=1.
    evidence = []
    for fixture, auth in zip(f["evolution"], author["direct_evolution"]):
        av = fixture["a"]
        alpha = np.array([math.sqrt(av), 0.])
        proj = fixture["projection"]
        velocity = math.sqrt(3*fixture["omega_s"])*np.array([proj, math.sqrt(1-proj*proj)])
        state0 = np.r_[0., 0., velocity, 3*(1-fixture["omega_s"]-fixture["omega_r"]), 3*fixture["omega_r"], 0.]

        def rhs(n, u):
            phi, vel, rm, rr = u[:2], u[2:4], u[4], u[5]
            H = math.sqrt((rm+rr+vel@vel)/3)
            A = math.exp(alpha@phi)
            return np.r_[vel/H, -3*vel-.5*alpha*rm/H, (-3+alpha@vel/H)*rm, -4*rr, A/H]

        sols = [solve_ivp(rhs, (0., end), state0, method="Radau", rtol=1e-12, atol=1e-14,
                          max_step=.019, dense_output=True) for end in [-.5, .5]]
        check("Radau_dimensional_"+fixture["id"], all(s.success for s in sols))
        rows = []
        for k, n in enumerate(f["comparison_N"]):
            u = sols[0 if n < 0 else 1].sol(n)
            phi, vel, rm, rr = u[:2], u[2:4], u[4], u[5]
            H = math.sqrt((rm+rr+vel@vel)/3)
            A, zd = math.exp(alpha@phi), float(alpha@vel)
            hdot = -.5*rm - 2*rr/3 - vel@vel
            zddot = -3*H*zd-.5*av*rm
            RJ = A*math.exp(n)
            HJ = (H+zd)/A
            acceleration_J = (hdot+H*H+H*zd+zddot)/(A*A)
            qj = -acceleration_J/(HJ*HJ)
            auth_state = np.r_[phi, vel/H, rr/(3*H*H), math.log(H), u[6]]
            e1 = max(close("ODE_state_"+fixture["id"]+"_"+str(n)+"_"+str(level), auth_state, auth["levels"][level][k]["state"], 2e-10) for level in [0,1])
            for level in [0,1]:
                ar = auth["levels"][level][k]
                close("ODE_frame_q_"+fixture["id"]+"_"+str(n)+"_"+str(level), qj, ar["q_J"], 2e-10)
                close("ODE_frame_scale_"+fixture["id"]+"_"+str(n)+"_"+str(level), RJ, ar["scale_J"], 2e-10)
                close("ODE_Richardson_"+fixture["id"]+"_"+str(n)+"_"+str(level), qj, ar["richardson_q"], 3e-7)
                close("ODE_finite_difference_"+fixture["id"]+"_"+str(n)+"_"+str(level), [qj,qj], ar["finite_difference_q"], 9e-6)
                expected_scalars = [rm/(3*H*H), rr/(3*H*H), vel@vel/(3*H*H), zd/H, u[6]]
                close("ODE_fractions_time_"+fixture["id"]+"_"+str(n)+"_"+str(level), expected_scalars,
                      [ar[z] for z in ["Omega_m","Omega_r","Omega_s","y","time_J"]], 2e-10)
            # Independently conserved first integrals from particle mass A and radiation.
            close("dust_first_integral_"+fixture["id"]+"_"+str(n), rm*math.exp(3*n)/A, state0[4], 2e-10)
            close("radiation_first_integral_"+fixture["id"]+"_"+str(n), rr*math.exp(4*n), state0[5], 2e-10)
            if fixture["id"] in ["uncoupled_dust","weak_equality"]:
                exponent = (3+av)/2
                exact_t = math.expm1((exponent-av)*n)/(exponent-av)
                close("equality_exact_trajectory_"+fixture["id"]+"_"+str(n), [A,RJ,H,u[6]],
                      [math.exp(-av*n), math.exp((1-av)*n), math.exp(-exponent*n), exact_t], 2e-10)
            rows.append({"N":n, "physical_density_state":u.tolist(), "mapped_author_state":auth_state.tolist(),
                         "q_J_from_physical_acceleration":float(qj), "max_state_error":e1})
        evidence.append({"fixture":fixture, "rows":rows, "steps":[len(s.t) for s in sols]})
    return evidence


def distance_controls(f, author):
    nodes, weights = roots_legendre(80)
    results = []
    for row in author["distance_controls"]:
        q, k = row["q_lower"], row["q_extra_z_over_1plusz"]
        ratios = []
        for z in f["distance_grid"]:
            u = .5*z*(1+nodes)
            # Direct integration of d log H / dz from q(z)=q+k*z/(1+z).
            logH = (1+q)*np.log1p(u)+k*(np.log1p(u)+1/(1+u)-1)
            distance = .5*z*(weights@np.exp(-logH))
            baseline = .5*z*(weights@((1+u)**(-1-q)))
            ratios.append(float(distance/baseline))
        close("independent_Gauss_distance_"+str(q)+"_"+str(k), ratios, row["ratios"], 2e-13)
        check("independent_distance_order_"+str(q)+"_"+str(k), max(np.diff(ratios)) <= 2e-13)
        results.append({"q":q,"extra":k,"ratios":ratios})
    # Ordered weighted means fail with negative weights: explicit scope control.
    decreasing_low = np.array([2.,1.])
    decreasing_high = np.array([.8,.5])
    check("positive_group_weights_preserve_order", decreasing_high.mean()-decreasing_low.mean() <= 0)
    check("negative_GLS_like_weights_can_break_order", np.array([-2.,3.])@decreasing_high - np.array([-2.,3.])@decreasing_low > 0)
    return results


def full_data_controls(f, author):
    manifest = json.loads((SNAP/"PRIMARY_DATA.json").read_text())
    raw = {}
    for name, item in manifest["files"].items():
        zipped = (SNAP/item["local_gzip"]).read_bytes()
        raw[name] = gzip.decompress(zipped)
        check("primary_bytes_"+name, len(zipped) == item["gzip_bytes"] and digest(zipped) == item["gzip_sha256"]
              and len(raw[name]) == item["raw_bytes"] and digest(raw[name]) == item["raw_sha256"])
    # Manual whitespace parser preserves literal IDs; no genfromtxt dtype inference.
    lines = raw["table"].decode("utf-8").splitlines()
    header = lines[0].split()
    table = [dict(zip(header, line.split(), strict=True)) for line in lines[1:] if line.strip()]
    with io.BytesIO(raw["covariance"]) as stream:
        n = int(stream.readline())
        vals = np.loadtxt(stream)
    check("raw_dimensions", len(table) == n == 1701 and vals.shape == (n*n,))
    raw_cov = vals.reshape(n,n)
    asymmetry = float(np.max(np.abs(raw_cov-raw_cov.T)))
    diagonal_scale = float(np.max(np.diag(raw_cov)))
    check("raw_cov_finite_text_precision", bool(np.isfinite(raw_cov).all()) and asymmetry <= f["covariance_symmetry_relative_to_max_diagonal"]*diagonal_scale,
          asymmetry=asymmetry, maximum_diagonal=diagonal_scale)
    Cfull = raw_cov*.5 + raw_cov.T*.5
    factor = np.linalg.cholesky(Cfull)
    check("full_covariance_SPD_without_jitter", np.min(np.diag(factor)) > 0,
          minimum_cholesky_diagonal=float(np.min(np.diag(factor))))
    selected = [i for i,row in enumerate(table) if int(row["IS_CALIBRATOR"]) == 0 and .0233 <= float(row["zHD"]) <= 1.5]
    z = np.array([float(table[i]["zHD"]) for i in selected])
    zh = np.array([float(table[i]["zHEL"]) for i in selected])
    mag = np.array([float(table[i]["m_b_corr"]) for i in selected])
    ids = [table[i]["CID"] for i in selected]
    low = np.array([i for i,v in enumerate(z) if v < .1])
    test = np.array([i for i,v in enumerate(z) if v >= .1])
    high = np.array([i for i,v in enumerate(z) if .3 <= v <= 1.])
    C = Cfull[np.ix_(selected,selected)]
    a = author["processed_data"]
    for key, value in [("original_selected_row_indices_zero_based",selected),("calibration_indices_in_selection",low),
                       ("transfer_indices_in_selection",test),("contrast_high_indices_in_selection",high),("zHD",z),("zHEL",zh),("m_b_corr",mag)]:
        close("complete_selected_array_"+key, value, a[key], 0)
    check("complete_literal_CID_array", ids == a["selected_CID"])
    counts = {}
    for prefix, subset in [("all",list(range(n))),("selected",selected),("calibration",[selected[i] for i in low]),
                            ("transfer",[selected[i] for i in test]),("contrast_high",[selected[i] for i in high])]:
        counts[prefix+"_light_curve_rows"] = len(subset)
        counts[prefix+"_distinct_CID"] = len(set(table[i]["CID"] for i in subset))
    check("all_literal_counts", counts == a["counts"], counts=counts)
    close("covariance_reported_asymmetry", asymmetry, a["raw_covariance_asymmetry"], 0)
    close("covariance_reported_diagonal", diagonal_scale, a["covariance_diagonal_scale"], 0)
    L, T, TL = C[np.ix_(low,low)], C[np.ix_(test,test)], C[np.ix_(test,low)]
    # Solve with LU, form the complete intercept-annihilating residual map W.
    lf = lu_factor(L)
    qone = lu_solve(lf, np.ones(len(low)))
    u = qone/sum(qone)
    B = lu_solve(lf, TL.T).T
    v = np.ones(len(test))-B.sum(axis=1)
    predict_map = B + np.outer(v,u)
    W = np.zeros((len(test),len(selected)))
    W[:,test] = np.eye(len(test))
    W[:,low] = -predict_map
    S = W@C@W.T
    S = (S+S.T)/2
    sf = lu_factor(S)
    sq = np.linalg.cholesky(S)
    check("predictive_SPD_without_jitter", min(np.diag(sq)) > 0)
    check("transfer_residual_map_annihilates_intercept", float(np.max(np.abs(W.sum(axis=1)))) < 1e-12)
    VM = float(u@L@u)
    schur = T-B@TL.T
    close("full_residual_map_equals_posterior_marginalization", S, schur+VM*np.outer(v,v), 2e-13)
    cal_res_map = np.eye(len(low))-np.outer(np.ones(len(low)),u)
    cross = cal_res_map@C[np.ix_(low,range(len(selected)))]@W.T
    check("calibration_residuals_independent_of_transfer_residuals_given_Gaussian_model", float(np.max(np.abs(cross))) < 2e-13)
    # Omitting flat-prior intercept uncertainty changes the predictive covariance.
    check("reject_intercept_uncertainty_omission", float(np.max(np.abs(S-schur))) > 1e-5,
          maximum_covariance_difference=float(np.max(np.abs(S-schur))))
    # All fixed distances from 80-node Gauss-Legendre, rather than adaptive QUADPACK.
    nodes, weights = roots_legendre(80)
    zs = .5*z[:,None]*(1+nodes[None,:])
    ds = {}
    ds["q_half"] = .5*z*((1+zs)**(-1.5)@weights)
    qweak = (1+1/2499)/(2*(1-1/2499))
    ds["weak_equality"] = .5*z*((1+zs)**(-1-qweak)@weights)
    ds["supplied_LCDM_0.3"] = .5*z*((.3*(1+zs)**3+.7)**(-.5)@weights)
    curves = {}
    cholL = np.linalg.cholesky(L)
    cholC = np.linalg.cholesky(C)
    # Independent global identity via QR projection of the whitened intercept.
    whiten_one = solve_triangular(cholC, np.ones(len(selected)), lower=True)
    unit_intercept = whiten_one/np.linalg.norm(whiten_one)
    for name, distance in ds.items():
        shape = 5*np.log10((1+zh)*distance)
        residual0 = mag-shape
        intercept = float(u@residual0[low])
        residual_l = residual0[low]-intercept
        residual_t = W@residual0
        pred = mag[test]-residual_t
        whiten_l = solve_triangular(cholL,residual_l,lower=True)
        whiten_t = solve_triangular(sq,residual_t,lower=True)
        chi_l, chi_t = float(whiten_l@whiten_l),float(whiten_t@whiten_t)
        whiten_all = solve_triangular(cholC,residual0,lower=True)
        orthogonal = whiten_all-unit_intercept*(unit_intercept@whiten_all)
        global_chi = float(orthogonal@orthogonal)
        close("independent_global_projection_identity_"+name, chi_l+chi_t,global_chi,2e-8)
        out = {"intercept_calibration_only":intercept,"intercept_standard_error":math.sqrt(VM),
               "calibration_chi2":chi_l,"calibration_rank":len(low)-1,
               "conditional_transfer_chi2":chi_t,"transfer_dimension":len(test),
               "shape_all_selected":shape.tolist(),"prediction_transfer":pred.tolist(),
               "residual_calibration":residual_l.tolist(),"residual_transfer":residual_t.tolist(),
               "full_profile_identity_is_not_a_test_fit":global_chi}
        for key,value in out.items():
            tol = 2e-8 if "chi2" in key or key.startswith("full_profile") else 2e-11
            close("all_curve_rows_"+name+"_"+key,value,a["fixed_curves"][name][key],tol)
        curves[name] = out
    ghalf = np.array(curves["q_half"]["shape_all_selected"])
    differences = mag-ghalf
    contrast = float(np.mean(differences[high])-np.mean(differences[low]))
    variance = (np.sum(C[np.ix_(high,high)])/len(high)**2 + np.sum(L)/len(low)**2
                -2*np.sum(C[np.ix_(high,low)])/(len(high)*len(low)))
    sigma = math.sqrt(variance)
    lever = float(np.mean(np.log10(1+z[high]))-np.mean(np.log10(1+z[low])))
    c = np.zeros(len(selected)); c[high] = 1/len(high); c[low] = -1/len(low)
    contrast_out = {"observed_mag":contrast,"standard_error_full_covariance_mag":sigma,
                    "standardized_contrast":contrast/sigma,"high_rows":len(high),"low_rows":len(low),
                    "log_luminosity_lever":lever,"beta_to_cancel_single_contrast_calibration_only":contrast/lever,
                    "weights_all_selected":c.tolist()}
    for key,value in contrast_out.items():
        close("all_contrast_fields_"+key,value,a["class_contrast"][key],2e-11)
    close("class_mean_upper_bound",a["class_contrast"]["class_mean_upper_bound_mag"],0,0)
    nuisance = []
    for beta, ar in zip(f["luminosity_evolution_beta"],a["class_contrast"]["frozen_beta_sensitivity"]):
        corrected = differences-beta*np.log10(1+z)
        val = float(np.mean(corrected[high])-np.mean(corrected[low]))
        out = {"beta":beta,"corrected_contrast_mag":val,"standardized_contrast":val/sigma}
        for key,value in out.items():
            close("all_nuisance_rows_"+str(beta)+"_"+key,value,ar[key],2e-11)
        nuisance.append(out)
    contrast_out["frozen_beta_sensitivity"] = nuisance
    close("nuisance_cancellation",contrast-(contrast/lever)*lever,0,1e-14)
    # Mutations of readout conventions must not silently reproduce the same shape.
    wrong_z_factor = 5*np.log10((1+z)*ds["q_half"])
    check("reject_zHD_for_zHEL_prefactor", float(np.max(np.abs(wrong_z_factor-ghalf))) > .001,
          max_shape_difference=float(np.max(np.abs(wrong_z_factor-ghalf))))
    check("full_covariance_not_diagonal_errors", abs(variance-float(c@np.diag(np.diag(C))@c)) > 1e-5)
    # Hash provenance separately uses the author's declared operation order, without
    # importing helpers. The scientific recomputation above uses W C W^T instead.
    from scipy.linalg import cho_factor, cho_solve
    cf = cho_factor(L,lower=True)
    provenance_B = cho_solve(cf,TL.T).T
    provenance_v = np.ones(len(test))-provenance_B@np.ones(len(low))
    provenance_vm = 1/(np.ones(len(low))@cho_solve(cf,np.ones(len(low))))
    exact_S = T-provenance_B@TL.T+provenance_vm*np.outer(provenance_v,provenance_v)
    exact_S = (exact_S+exact_S.T)/2
    exact_hash = digest(np.asarray(exact_S,dtype='<f8').tobytes())
    check("declared_prediction_covariance_byte_hash", exact_hash == a["prediction_covariance_sha256_float64_C_order"],
          independently_reconstructed_sha256=exact_hash,declared_sha256=a["prediction_covariance_sha256_float64_C_order"])
    pair_counts = collections.Counter(ids)
    repeated_ids = {k:v for k,v in pair_counts.items() if v>1}
    return {"counts":counts,"selection":selected,"literal_CID":ids,"zHD":z.tolist(),"zHEL":zh.tolist(),"m_b_corr":mag.tolist(),
            "calibration_indices":low.tolist(),"transfer_indices":test.tolist(),"high_contrast_indices":high.tolist(),
            "raw_covariance_asymmetry":asymmetry,"maximum_covariance_diagonal":diagonal_scale,
            "predictive_covariance_sha256_independent_W_method":digest(np.asarray(S,dtype='<f8').tobytes()),
            "predictive_covariance_hash_provenance_method":exact_hash,
            "max_predictive_covariance_method_difference":float(np.max(np.abs(S-exact_S))),
            "fixed_curves":curves,"class_contrast":contrast_out,
            "repeated_literal_selected_CIDs":repeated_ids,
            "literal_CID_calibration_transfer_intersection":sorted(set(ids[i] for i in low)&set(ids[i] for i in test)),
            "physical_event_count_not_inferred_from_literal_CID":True}


def main():
    destination = ROOT/"INDEPENDENT_RESULTS_v2.json"
    if destination.exists():
        raise FileExistsError(destination)
    started = time.time()
    author = json.loads((SNAP/"evidence_v1/RESULTS.json").read_text())
    fixtures = json.loads((SNAP/"NUMERICAL_FIXTURES.json").read_text())
    pins = json.loads((ROOT/"SOURCE_PINS_v1.json").read_text())
    for item in pins["sources"]:
        check("source_snapshot_"+item["path"], digest((ROOT/item["snapshot"]).read_bytes()) == item["sha256"])
    for path, sha in author["source_hashes"].items():
        check("author_execution_source_"+path,digest((SNAP/path).read_bytes()) == sha)
    check("consume_all_author_trace_records",len(author["checks"]) == author["checks_count"] == 6120
          and len(set(row["name"] for row in author["checks"])) == 6120
          and all(row["pass"] is True for row in author["checks"]) and author["all_passed"] is True)
    out = {"reviewer":"independent direct_field_check","no_author_runner_import_or_execution":True,
           "script_sha256":digest(Path(__file__).read_bytes()),"numpy":np.__version__,"scipy":scipy.__version__,"sympy":sy.__version__,
           "symbolic":symbolic_controls(),"grid":grid_controls(fixtures,author),
           "evolution":evolution_controls(fixtures,author),"distance":distance_controls(fixtures,author),
           "processed_data":full_data_controls(fixtures,author)}
    out["checks"] = CHECKS
    out["checks_count"] = len(CHECKS)
    out["failures"] = [r for r in CHECKS if not r["pass"]]
    out["all_passed"] = not out["failures"]
    out["elapsed_seconds"] = time.time()-started
    out["completed_utc"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
    destination.write_text(json.dumps(out,indent=2,allow_nan=False)+"\n")
    print(json.dumps({"checks":out["checks_count"],"failures":out["failures"],"all_passed":out["all_passed"],
                      "elapsed_seconds":out["elapsed_seconds"],"data_counts":out["processed_data"]["counts"]},indent=2))
    return 0 if out["all_passed"] else 1


if __name__ == "__main__":
    sys.exit(main())
