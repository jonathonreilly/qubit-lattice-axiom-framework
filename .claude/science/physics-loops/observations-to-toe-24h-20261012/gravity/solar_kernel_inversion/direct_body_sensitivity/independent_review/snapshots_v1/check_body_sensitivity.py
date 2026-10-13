#!/usr/bin/env python3
"""Frozen synthetic equilibrium controls and exposed LLR comparison."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

import numpy as np
import sympy as sp
from scipy.integrate import quad, solve_ivp
from scipy.optimize import brentq

ROOT = Path(__file__).resolve().parent
PI = math.pi
CHECKS = []


def require(name, condition, details=None):
    row = {"name": name, "passed": bool(condition)}
    if details is not None:
        row["details"] = details
    CHECKS.append(row)
    assert row["passed"], row


def close(name, actual, expected, rtol=2e-9, atol=1e-14):
    error = abs(float(actual) - float(expected))
    require(name, error <= atol + rtol * abs(float(expected)),
            {"actual": float(actual), "expected": float(expected), "abs_error": error})


def lane_emden(n, max_step):
    x0 = 1e-7
    y0 = [1-x0*x0/6+n*x0**4/120, x0**3/3-n*x0**5/30]

    def rhs(x, y):
        return [-y[1]/(x*x), x*x*max(y[0], 0.0)**n]

    def surface(x, y):
        return y[0]

    surface.terminal = True
    surface.direction = -1
    solution = solve_ivp(rhs, (x0, 50.0), y0, method="DOP853",
                         rtol=2e-13, atol=2e-14, dense_output=True,
                         events=surface, max_step=max_step)
    require(f"LE_surface_n{n}_step{max_step}", solution.success and
            len(solution.t_events[0]) == 1)
    x1 = float(solution.t_events[0][0])
    mu = float(solution.y_events[0][0][1])

    def tm(x):
        if x < x0:
            return 1-x*x/6+n*x**4/120, x**3/3-n*x**5/30
        theta, mass = solution.sol(x)
        return max(float(theta), 0.0), float(mass)

    integrate = lambda fun: quad(fun, 0, x1, epsabs=2e-12, epsrel=2e-12,
                                 limit=200)[0]
    im = integrate(lambda x: x*x*tm(x)[0]**n)
    iw = integrate(lambda x: x*tm(x)[1]*tm(x)[0]**n)
    ip = integrate(lambda x: x*x*tm(x)[0]**(n+1))
    close(f"LE_mass_n{n}_step{max_step}", im, mu, rtol=2e-10)
    if n == 1:
        close(f"LE_analytic_radius_step{max_step}", x1, PI, rtol=1e-11)
        close(f"LE_analytic_mass_step{max_step}", mu, PI, rtol=1e-11)
        for x in np.linspace(0.01, PI, 21):
            close(f"LE_analytic_profile_{x}_step{max_step}", tm(x)[0],
                  math.sin(x)/x, rtol=2e-10, atol=2e-12)
    return {"n": n, "x1": x1, "mu": mu, "im": im, "iw": iw,
            "ip": ip, "tm": tm}


def equilibrium(shape, g, eos, rho_guess):
    n, x1, mu = shape["n"], shape["x1"], shape["mu"]

    def at_density(logrho):
        rho = math.exp(logrho)
        length = math.sqrt((n+1)*eos*rho**(1/n-1)/(4*PI*g))
        mass = 4*PI*length**3*rho*mu
        return rho, length, mass

    center = math.log(rho_guess)
    root = brentq(lambda z: math.log(at_density(z)[2]), center-4, center+4,
                  xtol=2e-14, rtol=1e-14)
    rho, length, mass = at_density(root)
    radius = length*x1
    ug = -16*PI**2*g*length**5*rho**2*shape["iw"]
    ui = 4*PI*n*eos*rho**(1+1/n)*length**3*shape["ip"]
    binding = ug+ui
    total = mass+binding
    s = -ug/total
    return {"G": g, "rho_c": rho, "L": length, "R": radius,
            "M_b": mass, "U_G": ug, "U_int": ui, "binding": binding,
            "M_J": total, "s": s, "K_EOS": eos}


def radial_rayleigh(shape, body, coeffs):
    n, gamma = shape["n"], 1+1/shape["n"]
    length, rho_c, g = body["L"], body["rho_c"], body["G"]
    radius, eos = body["R"], body["K_EOS"]

    def fields(r):
        t, mu = shape["tm"](r/length)
        rho = rho_c*t**n
        pressure = eos*rho_c**(1+1/n)*t**(n+1)
        mass = 4*PI*length**3*rho_c*mu
        gradp = -g*mass*rho/r**2 if r else 0.0
        x = r/radius
        eta = sum(c*x**(2*j) for j, c in enumerate(coeffs))
        deta = sum(2*j*c*x**(2*j-1)/radius for j, c in enumerate(coeffs) if j)
        return rho, pressure, gradp, eta, deta

    def numerator(r):
        rho, pressure, gradp, eta, deta = fields(r)
        return gamma*pressure*r**4*deta**2 - (3*gamma-4)*r**3*gradp*eta**2

    def denominator(r):
        rho, pressure, gradp, eta, deta = fields(r)
        return rho*r**4*eta**2

    num = quad(numerator, 0, radius, epsabs=1e-15, epsrel=1e-10)[0]
    den = quad(denominator, 0, radius, epsabs=1e-14, epsrel=1e-11)[0]
    require(f"radial_energy_n{n}_G{g}_{coeffs}", num > 0 and den > 0)
    return {"coefficients": coeffs, "numerator": num, "denominator": den,
            "omega_squared_Rayleigh": num/den,
            "omega_squared_in_GM_over_R3": num/den/(g*body["M_b"]/radius**3)}


def structure_checks(fixtures):
    shapes = {}
    shape_rows = []
    for n in fixtures["polytrope_indices"]:
        coarse, fine = [lane_emden(n, step) for step in fixtures["Lane_Emden_max_steps"]]
        for key in ["x1", "mu", "im", "iw", "ip"]:
            close(f"LE_refinement_n{n}_{key}", coarse[key], fine[key], rtol=2e-10)
        shapes[n] = fine
        shape_rows.append({k: v for k, v in fine.items() if k != "tm"})
    rows, lookup = [], {}
    for n, shape in shapes.items():
        rho0 = shape["x1"]**3/(4*PI*shape["mu"])
        for g0 in fixtures["initial_G_J"]:
            eos = 4*PI*g0/((n+1)*shape["x1"]**2)*rho0**(1-1/n)
            body = equilibrium(shape, g0, eos, rho0)
            tag = f"n{n}_G{g0}"
            close(f"mass_{tag}", body["M_b"], 1, rtol=1e-12)
            close(f"radius_{tag}", body["R"], 1, rtol=1e-12)
            close(f"energy_integral_{tag}", body["U_G"], -3*g0/(5-n), rtol=2e-9)
            close(f"virial_{tag}", body["U_int"], -n*body["U_G"]/3, rtol=2e-9)
            require(f"weak_positive_mass_{tag}", body["M_J"] > 0.99)
            p = 3/(3-n)
            derivatives = []
            dlog = []
            for h in fixtures["zeta_steps"]:
                plus = equilibrium(shape, g0*math.exp(2*h), eos, rho0)
                minus = equilibrium(shape, g0*math.exp(-2*h), eos, rho0)
                for zeta, shifted in [(h, plus), (-h, minus)]:
                    close(f"profile_radius_{tag}_{zeta}", shifted["R"],
                          math.exp(-2*zeta*n/(3-n)), rtol=2e-11)
                    close(f"profile_gravity_energy_{tag}_{zeta}", shifted["U_G"],
                          body["U_G"]*math.exp(2*p*zeta), rtol=2e-11)
                # Subtract the constant baryon rest energy before differencing.
                derivative_binding = (plus["binding"]-minus["binding"])/(2*h)
                derivative_logmass = (math.log1p(plus["binding"])-
                                      math.log1p(minus["binding"]))/ (2*h)
                derivative_s = (plus["s"]-minus["s"])/(2*h)
                dlog.append(derivative_logmass)
                derivatives.append({"zeta_step": h, "plus": plus, "minus": minus,
                                    "d_binding_d_zeta": derivative_binding,
                                    "d_log_M_d_zeta": derivative_logmass,
                                    "d_s_d_zeta": derivative_s})
                close(f"envelope_fd_{tag}_{h}", derivative_binding,
                      2*body["U_G"], rtol=3e-5, atol=1e-14)
                close(f"s_response_fd_{tag}_{h}", derivative_s,
                      2*(p*body["s"]+body["s"]**2), rtol=3e-5, atol=1e-14)
            richardson = (4*dlog[2]-dlog[1])/3
            close(f"body_charge_richardson_{tag}", richardson,
                  -2*body["s"], rtol=3e-8, atol=1e-13)
            wrong = -body["binding"]/body["M_J"]
            close(f"binding_vs_gravity_factor_{tag}", body["s"]/wrong, p, rtol=2e-9)
            require(f"total_binding_false_control_{tag}", abs(wrong-body["s"]) > body["s"]*0.2)
            radial = [radial_rayleigh(shape, body, co) for co in
                      fixtures["radial_displacements_even_polynomial_coefficients"]]
            rows.append({"n": n, "base": body, "p": p,
                         "equilibrium_derivatives": derivatives,
                         "b_over_alpha_from_difference": 1+richardson,
                         "b_over_alpha_analytic": 1-2*body["s"],
                         "radial_Rayleigh_controls": radial})
            lookup[(n, g0)] = body
    return shape_rows, rows, lookup


def sphere(nz, nphi):
    z, w = np.polynomial.legendre.leggauss(nz)
    phi = 2*PI*np.arange(nphi)/nphi
    zz, pp = np.meshgrid(z, phi, indexing="ij")
    points = np.column_stack((np.sqrt(1-zz.ravel()**2)*np.cos(pp.ravel()),
                              np.sqrt(1-zz.ravel()**2)*np.sin(pp.ravel()), zz.ravel()))
    weights = np.repeat(w, nphi)*2*PI/nphi
    close(f"sphere_area_{nz}_{nphi}", sum(weights), 4*PI, rtol=1e-13)
    return points, weights


def angular_powers(m1, m2, b1, b2, Kinv, gs, r, omega, phase, grid):
    points, weights = grid
    mu = m1*m2/(m1+m2)
    radial = np.array([math.cos(phase), math.sin(phase), 0.0])
    tangent = np.array([-math.sin(phase), math.cos(phase), 0.0])
    third = -4*mu*r*r*omega**3*(np.outer(radial, tangent)+np.outer(tangent, radial))
    projector = np.eye(3)[None, :, :]-np.einsum("ni,nj->nij", points, points)
    pt = np.einsum("nij,jk,nkl->nil", projector, third, projector)
    trace = np.einsum("nij,ji->n", projector, third)
    tt = pt-0.5*projector*trace[:, None, None]
    tensor = gs/(8*PI)*np.dot(weights, np.einsum("nij,nij->n", tt, tt))
    d2 = -mu*r*omega**2*np.outer(b1-b2, radial)
    bq = (m2*b1+m1*b2)/(m1+m2)
    dip = points@d2.T
    quad_amplitude = 0.5*np.einsum("ni,ij,nj->n", points, third, points)[:, None]*bq
    norm = lambda field: np.einsum("ni,ij,nj->n", field, Kinv, field)
    dipole = gs/(4*PI)*np.dot(weights, norm(dip))
    scalar_quad = gs/(4*PI)*np.dot(weights, norm(quad_amplitude))
    cross = gs/(4*PI)*np.dot(weights, 2*np.einsum("ni,ij,nj->n", dip, Kinv, quad_amplitude))
    return {"tensor": float(tensor), "dipole": float(dipole),
            "scalar_quadrupole": float(scalar_quad), "interference": float(cross)}


def radiation_checks(fixtures, lookup):
    kinv = np.linalg.inv(np.array(fixtures["K"], float))
    d = np.array(fixtures["alpha_direction"], float)
    f = fixtures["f_for_binary_examples"]
    a = f/(1-f)
    alpha = d*math.sqrt(a/(d@kinv@d))
    close("scalar_force_normalization", alpha@kinv@alpha, a, rtol=1e-13)
    grids = [sphere(*g) for g in fixtures["sphere_quadratures"]]
    rows = []
    for index, pair in enumerate(fixtures["binary_profile_pairs"]):
        p1, p2 = lookup[(pair["n1"], pair["G_J"])], lookup[(pair["n2"], pair["G_J"])]
        m1, m2 = p1["M_J"], p2["M_J"]
        b1, b2 = alpha*(1-2*p1["s"]), alpha*(1-2*p2["s"])
        bq = (m2*b1+m1*b2)/(m1+m2)
        mutual = float(b1@kinv@b2)
        gs = pair["G_J"]/(1+a)
        g12 = gs*(1+mutual)
        mu = m1*m2/(m1+m2)
        require(f"attractive_binary_{index}", g12 > 0)
        for speed in fixtures["orbital_v_over_c"]:
            r = g12*(m1+m2)/(speed*speed)
            omega = speed/r
            norm_i3 = 32*mu**2*r**4*omega**6
            theory = {"tensor": gs*norm_i3/5,
                      "dipole": gs*mu**2*float((b1-b2)@kinv@(b1-b2))*r**2*omega**4/3,
                      "scalar_quadrupole": gs*float(bq@kinv@bq)*norm_i3/30}
            gr = g12*norm_i3/5
            computed = []
            for grid_index, grid in enumerate(grids):
                for phase_index in range(fixtures["orbital_phases"]):
                    phase = phase_index*2*PI/fixtures["orbital_phases"]
                    values = angular_powers(m1, m2, b1, b2, kinv, gs, r, omega, phase, grid)
                    tag = f"{index}_{speed}_{grid_index}_{phase_index}"
                    for channel, expected in theory.items():
                        # Compare normalized powers, never let a unit absolute tolerance hide tiny fluxes.
                        close(f"sphere_{channel}_{tag}", values[channel]/gr,
                              expected/gr, rtol=3e-11, atol=1e-18)
                    close(f"odd_interference_{tag}", values["interference"]/gr, 0,
                          atol=2e-13*max(1, sum(theory.values())/gr))
                    computed.append({"quadrature_index": grid_index, "phase_index": phase_index,
                                     "powers_over_same_orbit_GR": {k: val/gr for k, val in values.items()}})
            expected_ratio = (1+float(bq@kinv@bq)/6+
                              (5/96)*float((b1-b2)@kinv@(b1-b2))/speed**2)/(1+mutual)
            close(f"channel_ratio_{index}_{speed}", sum(theory.values())/gr, expected_ratio,
                  rtol=2e-13)
            size_ratio = max(p1["R"], p2["R"])/r
            adiabatic = max(omega*math.sqrt(p["R"]**3/(pair["G_J"]*p["M_b"])) for p in [p1,p2])
            require(f"synthetic_size_{index}_{speed}", size_ratio < 0.006)
            require(f"synthetic_adiabatic_{index}_{speed}", adiabatic < 0.001)
            rows.append({"fixture": index, "profile_pair": pair, "speed": speed,
                         "masses": [m1,m2], "sensitivities": [p1["s"],p2["s"]],
                         "b1": b1.tolist(), "b2": b2.tolist(), "G_star": gs, "G12": g12,
                         "separation": r, "omega": omega, "max_R_over_r": size_ratio,
                         "max_omega_t_internal": adiabatic, "analytic_powers": theory,
                         "same_orbit_GR_power": gr, "leading_channel_ratio": expected_ratio,
                         "direct_sphere_controls": computed})
    close("zero_sensitivity_recovery", (1+a/6)/(1+a), 1-5*f/6, rtol=1e-14)
    require("unequal_sensitivity_dipole_control", any(row["analytic_powers"]["dipole"] > 0 for row in rows))
    require("equal_sensitivity_zero_dipole_control", rows[0]["analytic_powers"]["dipole"] == 0)
    return {"K": fixtures["K"], "alpha": alpha.tolist(), "a": a, "f": f, "rows": rows}


def symbolic_and_observation_checks(inputs):
    s, p = sp.symbols("s p", positive=True)
    # The polytropic energy derivative, with total energy E=B+C*G**p and C<0.
    G, B, C = sp.symbols("G B C", nonzero=True)
    energy = B+C*G**p
    sens = -G*sp.diff(energy,G)/energy
    identity = sp.simplify(G*sp.diff(sens,G)-p*sens-sens**2)
    require("symbolic_polytropic_susceptibility", identity == 0)
    a, se, sm, ss, t = sp.symbols("a se sm ss t", real=True)
    delta = -2*a*(se-sm)*(1-2*ss)/(1+a*(1-se-sm)*(1-2*ss))
    first = sp.diff(delta.subs({se:t*se,sm:t*sm,ss:t*ss}), t).subs(t,0)
    require("symbolic_free_fall_leading", sp.simplify(first+2*a*(se-sm)/(1+a)) == 0)
    mean = sp.Rational(inputs["LLR_total_EP"]["Earth_minus_Moon_mean"])
    sigma = sp.Rational(inputs["LLR_total_EP"]["reported_uncertainty"])
    selfdiff = sp.Rational(inputs["geophysical_self_energy_difference"]["Earth_minus_Moon"])
    rows = []
    for fs in inputs["scalar_force_fraction"]["frozen_prediction_grid"]:
        fv = sp.Rational(fs)
        prediction = 2*fv*selfdiff
        residual = (mean-prediction)/sigma
        rows.append({"f":float(fv),"prediction":float(prediction),
                     "residual_observed_minus_prediction":float(mean-prediction),
                     "z_summary":float(residual),"z_exact":str(residual),
                     "composition_nuisance_matching_mean":float(mean-prediction)})
    upper = sp.Rational(inputs["scalar_force_fraction"]["earlier_working_interval"][1])
    windows = []
    for count in [1,2]:
        lo = max(sp.Rational(0), (mean+count*sigma)/(2*selfdiff))
        hi = min(upper, (mean-count*sigma)/(2*selfdiff))
        require(f"working_window_{count}", lo <= hi)
        windows.append({"reported_uncertainties":count,"lower":float(lo),"upper":float(hi),
                        "lower_exact":str(lo),"upper_exact":str(hi),
                        "interpretation":"Exposed summary working rectangle intersection, no confidence claim."})
    close("LLR_endpoint_prediction", rows[-1]["prediction"], -3.56e-13,
          rtol=1e-14, atol=1e-28)
    close("LLR_endpoint_residual", rows[-1]["z_summary"], 64/35, rtol=1e-14)
    return {"historical_summary":inputs,"frozen_predictions":rows,
            "working_intersections":windows,"fit_performed":False,
            "free_composition_nuisance":"d_comp=observed_mean+8.90e-10*f; one observation leaves a line of solutions."}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-json", type=Path, required=True)
    args = parser.parse_args()
    fixture = json.loads((ROOT/"NUMERICAL_FIXTURES.json").read_text())
    inputs = json.loads((ROOT/"OBSERVATION_INPUTS.json").read_text())
    shape, bodies, lookup = structure_checks(fixture)
    radiation = radiation_checks(fixture,lookup)
    observation = symbolic_and_observation_checks(inputs)
    names = ["PROTOCOL.md","NUMERICAL_FIXTURES.json","OBSERVATION_INPUTS.json",
             "DIRECT_BODY_SENSITIVITY.md","check_body_sensitivity.py"]
    result = {"scope":"Conditional Newtonian body sensitivity and separately leading circular radiation channels.",
              "source_sha256":{n:hashlib.sha256((ROOT/n).read_bytes()).hexdigest() for n in names},
              "Lane_Emden_shapes":shape,"equilibrium_bodies":bodies,
              "radiation":radiation,"observation":observation,"checks":CHECKS,
              "check_count":len(CHECKS),"all_checks_passed":all(x["passed"] for x in CHECKS),
              "limits":["Supplied EOS and EFT matching","Newtonian weak self-gravity",
                        "Leading channel sum is not complete next-order dipole radiation",
                        "Historical exposed summary, no raw likelihood or empirical fit",
                        "No actual Earth/Moon density reconstruction or TOE"]}
    with args.output_json.open("x") as handle:
        json.dump(result,handle,indent=2,allow_nan=False)
        handle.write("\n")
    print(json.dumps({"checks":len(CHECKS),"all_passed":True,"body_profiles":len(bodies),
                      "binary_rows":len(radiation["rows"]),"LLR":observation["frozen_predictions"]},indent=2))


if __name__ == "__main__":
    main()
