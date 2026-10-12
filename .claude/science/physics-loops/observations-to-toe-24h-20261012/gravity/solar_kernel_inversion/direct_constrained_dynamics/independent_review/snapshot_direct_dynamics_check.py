#!/usr/bin/env python3
"""Checks for an explicitly supplied preferred-time gravity attempt.

No fit, observational score, physical speed calibration, or formal audit.
Proof domains are in DIRECT_DYNAMICS.md. Finite numeric diagnostics supplement,
and do not replace, those proofs.
"""
from __future__ import annotations
import argparse
from decimal import Decimal
from fractions import Fraction
import hashlib
import json
import math
from pathlib import Path
import sys
import traceback
import numpy as np
import scipy
from scipy.optimize import minimize, minimize_scalar
import sympy as s

HERE = Path(__file__).resolve().parent
E_FIXED = 1.4915242022774435e-10
STEP = math.log(10.0) / 4
KNOTS = 10.0 ** (-13.0 + np.arange(21) / 4)


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def ln_step_enclosure(terms=160):
    # ln(10)/4 = atanh(9/11)/2. Bound the positive remainder geometrically.
    z = Fraction(9, 11)
    lo = sum((z ** (2 * j + 1) / (2 * j + 1) for j in range(terms)),
             Fraction(0)) / 2
    tail = z ** (2 * terms + 1) / (2 * (2 * terms + 1) * (1 - z*z))
    return lo, lo + tail


def response(a, w):
    a = np.asarray(a, dtype=float)
    safe = np.maximum(a, np.finfo(float).tiny)
    b = np.clip((np.log(KNOTS[1:]) - np.log(safe)[..., None]) / STEP, 0, 1)
    return 1.0 + b @ w


def f_scaled(g, w, scale=1e-10):
    z = (scale * np.asarray(g)) ** 2
    answer = z.copy()
    for j, weight in enumerate(w):
        if weight == 0:
            continue
        low, high = KNOTS[j], KNOTS[j+1]
        middle = (z * np.log(high / np.sqrt(np.maximum(z, 1e-300)))
                  + (z - low*low) / 2) / STEP
        term = np.where(z <= low*low, z,
                        np.where(z >= high*high,
                                 (high*high-low*low)/(2*STEP), middle))
        answer = answer + weight * term
    return answer / (scale*scale)


def nonlinear_dirichlet(w):
    # Independent finite-dimensional optimization; no continuum inference.
    nodes = 65
    x = np.linspace(0, 1, nodes)
    h = x[1] - x[0]
    phi = np.sin(np.pi*x) + .13*np.sin(2*np.pi*x)
    phi[[0, -1]] = 0
    gp = np.diff(phi) / h
    nmax = 1 + np.sum(w)
    def objective(interior):
        psi = np.r_[0.0, interior, 0.0]
        g = np.diff(psi) / h
        val = h * np.sum(f_scaled(g, w) - 2 * gp*g)
        flux = response(1e-10*np.abs(g), w)*g - gp
        jac = 2 * (flux[:-1] - flux[1:])
        return float(val), jac
    result = minimize(objective, phi[1:-1]/nmax, method="L-BFGS-B", jac=True,
                      options={"gtol": 1e-10, "ftol": 1e-15,
                               "maxiter": 5000, "maxls": 60})
    val, grad = objective(result.x)
    energy = -val
    p2 = float(h*np.sum(gp*gp))
    # Minimizer is approximate: bounds and stationarity are only diagnostics.
    assert np.max(np.abs(grad)) < 2e-6
    assert p2/nmax-1e-9 <= energy <= p2+1e-9
    return {"nodes": nodes, "gradient_scale": 1e-10,
            "optimizer_success": bool(result.success),
            "optimizer_message": str(result.message),
            "iterations": int(result.nit),
            "max_stationarity_residual": float(np.max(np.abs(grad))),
            "J": float(energy), "lower": float(p2/nmax), "upper": p2}


def symbolic_checks():
    x, y, z, a, b, N, D = s.symbols("x y z a b N D", positive=True)
    h = (a*(x*x+y*y) + b*z*z) ** -s.Rational(1, 2)
    lap = lambda f: sum(s.diff(f, r, 2) for r in (x, y, z))
    on_axis = s.factor(lap(lap(h)).subs({x: 0, y: 0}))
    target = 24*(a-b)**2 / (b**s.Rational(5, 2)*z**5)
    assert s.simplify(on_axis-target) == 0
    kernel = s.simplify(-on_axis.subs({a: 1/N, b: 1/D})
                        / (4*s.pi*N*s.sqrt(D)))
    expected = -6*(N-D)**2/(s.pi*N**3*z**5)
    assert s.simplify(kernel-expected) == 0
    assert s.simplify(kernel.subs(D, N)) == 0

    kx, ky, kz = s.symbols("kx ky kz", real=True)
    k2 = kx*kx+ky*ky+kz*kz
    q = N*(kx*kx+ky*ky)+D*kz*kz
    omega = k2/s.sqrt(q)  # c_s=1
    grad = [s.diff(omega, k) for k in (kx, ky, kz)]
    norm2 = sum(v*v for v in grad)
    target_norm = k2*k2*(N*N*(kx*kx+ky*ky)+D*D*kz*kz)/q**3
    assert s.factor(norm2-target_norm) == 0

    r, ksq, qq, lam, ap, av, w2 = s.symbols(
        "r ksq qq lam ap av w2", real=True)
    mat = s.Matrix([[0, -ksq], [-ksq, qq]])
    vec = s.Matrix([ap, av])
    det = s.expand((mat+w2*lam*vec*vec.T).det())
    assert s.expand(det + ksq**2
                    - lam*w2*(ap*ap*qq+2*ap*av*ksq)) == 0

    u, v, c0, cs, rho = s.symbols("u v C cs rho")
    ut, ux, vx = s.symbols("ut ux vx")
    # Euler signs independently differentiated in a one-coordinate reduction.
    tt, xx = s.symbols("t x", real=True)
    phi = s.Function("phi")(tt, xx)
    psi = s.Function("psi")(tt, xx)
    ff = s.Function("F")
    lag = c0*(s.diff(phi, tt)**2/cs**2
              -2*s.diff(phi, xx)*s.diff(psi, xx)
              +ff(s.diff(psi, xx)**2)) - rho*phi
    elphi = s.diff(lag, phi) - s.diff(s.diff(lag, s.diff(phi, tt)), tt) \
        - s.diff(s.diff(lag, s.diff(phi, xx)), xx)
    assert s.simplify(elphi-(2*c0*(s.diff(psi, xx, 2)
                                   -s.diff(phi, tt, 2)/cs**2)-rho)) == 0
    elpsi = s.diff(lag, psi) - s.diff(s.diff(lag, s.diff(psi, xx)), xx)
    constitutive = s.diff(ff(s.diff(psi, xx)**2), s.diff(psi, xx))/2
    assert s.simplify(elpsi-2*c0*(s.diff(phi, xx, 2)
                                  -s.diff(constitutive, xx))) == 0

    # General convex radial Hessian at a smooth positive background.
    X, Y, Z, A = s.symbols("X Y Z A", real=True)
    f = s.Function("f")
    H = s.hessian(f(X*X+Y*Y+Z*Z), (X, Y, Z)).subs({X: 0, Y: 0, Z: A})
    assert H[0, 1] == H[0, 2] == H[1, 2] == 0
    assert s.simplify(H[2, 2]-H[0, 0]-4*A*A*
                     s.Subs(s.Derivative(f(s.Symbol("t")), (s.Symbol("t"), 2)),
                            s.Symbol("t"), A*A)) == 0
    return {"axis_bilaplacian": str(on_axis), "axis_acceleration_kernel_cs1": str(kernel),
            "group_norm_identity": True, "rank_one_determinant": str(det),
            "Euler_signs": True, "radial_Hessian": True}


def group_max(N, D):
    return (1/math.sqrt(D) if N <= 2*D else
            2*(N+D)**1.5/(3*math.sqrt(3)*N*D))


def candidate_checks(name, tokens, dlo, dhi):
    # Decimal tokens from the exact frozen JSON become rational numbers.
    exact = [Fraction(str(x)) for x in tokens]
    w = np.array([float(x) for x in exact])
    rows = []
    min_lower = Fraction(1)
    min_binary_lower = Fraction(1)
    binary = [Fraction.from_float(float(x)) for x in w]
    max_group_error = 0.0
    for j in range(20):
        n = 1 + sum(exact[j+1:], Fraction(0))
        d_lower = n-exact[j]/dlo
        d_upper = n-exact[j]/dhi
        assert d_lower > 0
        min_lower = min(min_lower, d_lower)
        binary_d_lower = 1 + sum(binary[j+1:], Fraction(0)) - binary[j]/dlo
        assert binary_d_lower > 0
        min_binary_lower = min(min_binary_lower, binary_d_lower)
        nv, dv = float(n), float(n)-float(exact[j])/STEP
        assert dv > 0 and dv <= nv+1e-14
        analytic = group_max(nv, dv)
        def speed2(t):
            mm = nv*(1-t)+dv*t
            return (nv*nv*(1-t)+dv*dv*t)/mm**3
        opt = minimize_scalar(lambda t: -speed2(t), bounds=(0, 1),
                              method="bounded", options={"xatol": 1e-14})
        independent = math.sqrt(max(speed2(0), speed2(1), -opt.fun))
        max_group_error = max(max_group_error, abs(independent-analytic))
        assert abs(independent-analytic) < 1e-9
        phase = 1/math.sqrt(dv)
        rows.append({"ramp": j, "upper_A_one_sided": float(KNOTS[j+1]),
                     "weight": float(exact[j]), "N_upper": nv,
                     "D_upper": dv, "D_certified_lower_float": float(d_lower),
                     "D_certified_upper_float": float(d_upper),
                     "phase_max_over_cs": phase,
                     "group_max_over_cs": analytic,
                     "axis_tail_cs1_z1": -6*(nv-dv)**2/(math.pi*nv**3)})
    worst = max(rows, key=lambda row: row["group_max_over_cs"])
    ext_n = float(response(E_FIXED, w))
    active = int(np.searchsorted(KNOTS, E_FIXED)-1)
    assert w[active] == 0
    # On this constant interval the auxiliary relation cancels the inverse.
    assert group_max(ext_n, ext_n) == 1/math.sqrt(ext_n)
    finite_energy = nonlinear_dirichlet(w)
    return {"name": name, "N_max": float(1+sum(exact)),
            "min_D_certified_positive": True,
            "min_D_lower_exact": str(min_lower),
            "min_D_lower_float": float(min_lower),
            "min_D_binary64_lower_exact": str(min_binary_lower),
            "min_D_binary64_lower_float": float(min_binary_lower),
            "worst_group_row": worst, "rows": rows,
            "max_group_optimization_difference": max_group_error,
            "external_E": E_FIXED, "external_N": ext_n,
            "external_D": ext_n, "external_active_weight": float(w[active]),
            "external_phase_over_cs": 1/math.sqrt(ext_n),
            "external_axis_tail": 0.0,
            "nonlinear_Dirichlet_diagnostic": finite_energy}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=HERE/"evidence_v2")
    args = parser.parse_args()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    frozen = HERE/"FROZEN_TRANSFER_INPUT.json"
    data = json.loads(frozen.read_text(), parse_float=Decimal)
    dlo, dhi = ln_step_enclosure()
    assert float(dlo) <= STEP <= float(dhi)
    out = {"scope": "conditional mathematics and finite diagnostics; no observational test",
           "identities": {p.name: digest(p) for p in [
               Path(__file__), HERE/"DIRECT_DYNAMICS.md", HERE/"PROTOCOL.md", frozen]},
           "environment": {"python": sys.version, "numpy": np.__version__,
                           "scipy": scipy.__version__, "sympy": s.__version__},
           "log_step_enclosure": {"terms": 160, "lower_exact": str(dlo),
                                  "upper_exact": str(dhi),
                                  "width_float": float(dhi-dlo)},
           "symbolic": symbolic_checks()}
    print("PASS symbolic Euler, radial Hessian, rank-one determinant, Green tail, group velocity")
    out["candidates"] = [candidate_checks(name, weights, dlo, dhi)
                         for name, weights in data["candidates"].items()]
    for cand in out["candidates"]:
        row = cand["worst_group_row"]
        print(f"PASS {cand['name']}: certified D>0; approximate inf D={cand['min_D_lower_float']:.12g}; "
              f"max group/c_s={row['group_max_over_cs']:.12g} at upper ramp {row['ramp']}")
        print(f"PASS {cand['name']}: nonlinear finite Dirichlet bounds; "
              f"fitted external plateau N=D={cand['external_N']:.12g}")
    print("per_element: checked the off-source continuum Green kernel on the distinguished axis.")
    print("per_site: checked and not executed — no discrete physical site model is proposed here.")
    print("per_mode: checked positive homogeneous mode and group formulas for the stated action.")
    print("per_block: checked finite Dirichlet diagnostics; the continuum energy proof is in the note.")
    print("lattice_wide: checked and not executed — no lattice-wide physical propagation claim is made.")
    print("NO_GO_PACKET: FAIL five-family quota; one kinetic family; preserve narrow partial attempt.")
    print("NO_OBSERVATIONAL_EXCLUSION: c_s is free; scalar is not identified with tensor radiation.")
    out["result"] = "PASS scoped mathematical diagnostics; no broad no-go packet PASS"
    (args.output_dir/"RESULTS.json").write_text(json.dumps(out, indent=2)+"\n")


if __name__ == "__main__":
    try:
        main()
    except Exception:
        traceback.print_exc()
        raise

