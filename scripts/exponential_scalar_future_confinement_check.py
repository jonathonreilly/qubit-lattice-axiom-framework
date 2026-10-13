#!/usr/bin/env python3
"""Algebra and off-orbit action checks for a conditional future trapping proof.

No finite collection of checks proves global continuation. The source note
contains that argument. No observational data or fitted parameters are read.
"""
import json
import sys

import mpmath as mp
import sympy as sp

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/EXPONENTIAL_SCALAR_FUTURE_CONFINEMENT_BOUNDED_THEOREM_NOTE_2026-10-13.md",
)

# These are the claimed coefficients, compared with the action/conservation
# identities below. Actual damaged-copy controls change one at a time.
ENERGY_FRICTION = 3
SOURCE_SIGN = 1
COUPLING_DENOMINATOR = 3
PHI_NORMALIZATION = 3
DENSITY_RATE = 3
WORK_INTEGRAL_DENOMINATOR = 72
CONVERGENCE_NU_MULTIPLIER = 6


def run_checks():
    checks = []

    def exact(name, residual):
        reduced = sp.factor(sp.cancel(residual))
        checks.append({"name": name, "passed": bool(reduced == 0),
                       "residual": str(reduced)})

    k, E, chi, w, t, nu = sp.symbols("k E chi w t nu", positive=True)
    a = (1-k)*(1+3*k)/4
    s = (1+k)/(k*(1-3*k))
    F = 1+s*E
    J = 1+(1-3*a)*s*E
    C = (1+s)*E/F
    exact("coordinate.definition", s*(C-1)-s*(E-1)/F)
    inverse_E = (1+chi/s)/(1-chi)
    exact("coordinate.inverse", (s*(E-1)/F-chi).subs(E, inverse_E))
    exact("potential.barrier", (sp.Rational(3, 2)*s*(E-1)**2/F**2
          - sp.Rational(3, 2)*chi**2/s).subs(E, inverse_E))
    proposed_coupling = k*(1-chi)/(1-COUPLING_DENOMINATOR*k*chi)
    exact("coupling.action_identity", (a/J).subs(E, inverse_E)-proposed_coupling)
    exact("coupling.monotonic_derivative", sp.diff(proposed_coupling, chi)
          - k*(3*k-1)/(1-3*k*chi)**2)
    exact("coupling.safe_upper_bound_gap", k*(1+w)-proposed_coupling.subs(chi, -w)
          - 3*k*k*w*(1+w)/(1+3*k*w))
    exact("coordinate.s_greater_one", s-1-(1+3*k*k)/(k*(1-3*k)))
    exact("clock.a_less_one_third", sp.Rational(1, 3)-a-(1-3*k)**2/12)
    exact("convergence.nu_one_allowed", 6*a-1-(1+6*k-9*k*k)/2)

    H, r, f, N = sp.symbols("H r f N", positive=True)
    exact("energy.young_completion", -3*H**2*r**2+f*r
          - (f*f/(12*H**2)-3*H**2*(r-f/(6*H**2))**2))
    exact("energy.half_dissipation", -3*H**2*r**2+f*r
          - (-sp.Rational(3, 2)*H**2*r**2+f*f/(6*H**2)
             - sp.Rational(3, 2)*H**2*(r-f/(3*H**2))**2))
    exact("barrier.Phi_chain_derivative", sp.diff(PHI_NORMALIZATION*(w-sp.log(1+w)), w)
          - 3*w/(1+w))
    exact("barrier.integrated_work", sp.integrate(sp.exp(-6*N)/12, (N, 0, sp.oo))
          - sp.Rational(1, WORK_INTEGRAL_DENOMINATOR))
    # rho'_J=-3(rho_J+P_J) N'_J and C'/C=2 alpha_B p_u.
    sig, pressure, ap = sp.symbols("sigma pi alpha_times_p")
    density_from_conservation = 4*ap*sig - 3*(sig+pressure)*(1+ap)
    exact("fluid.conformal_conservation", density_from_conservation
          - (-DENSITY_RATE*(sig+pressure)+ap*(sig-3*pressure)))
    exact("fluid.dust_envelope", 4*ap-3*(1+ap)-(-3+ap))

    # Reconstruct U on x=y=0 using t=2 sqrt(a) u. Its positive factor
    # times U_u is G, without relying on a sign sample.
    Et = sp.exp(t)
    Ft = 1+s*Et
    U_line = sp.Rational(3, 2)+sp.Rational(3, 2)*s*(Et-1)**2/Ft**2 + nu*(1+s)*t*t/(8*a*Ft**2)
    G = 12*a*(Et-1)+nu*t*(1-t)+nu*t/(s*Et)
    exact("critical_point.exact_sign_factor", sp.diff(U_line, t)*4*a*Ft**3/(s*Et*(1+s))-G)
    taylor_bound = (12*a+nu)*t+(CONVERGENCE_NU_MULTIPLIER*a-nu)*t*t+nu*t/(s*Et)
    exact("critical_point.positive_remainder", G-taylor_bound-12*a*(Et-1-t-t*t/2))

    # Build the full finite-k action independently of an integrated history.
    u, x, y = sp.symbols("u x y", real=True)
    coordinates = [u, x, y]
    al = sp.sqrt(a)
    Eu = sp.exp(2*al*u)
    Fu = 1+s*Eu
    Ju = 1+(1-3*a)*s*Eu
    D = 1+2*(1+k)*(x*x+y*y)/3
    metric = [Ju/Fu**2, (1+s)*4*k/(9*Fu*D), (1+s)*k/(3*Fu*D)]
    U = sp.Rational(3, 2)+sp.Rational(3, 2)*s*(Eu-1)**2/Fu**2 + k*x*x*sp.exp(-(1-k)*u/al)/2 + k*y*y*sp.exp(-(1+k)*u/al)/3 + nu*(1+s)*u*u/(2*Fu**2)
    alpha_B = al/Fu
    metric_derivatives = [[sp.diff(q, c) for c in coordinates] for q in metric]
    potential_derivatives = [sp.diff(U, c) for c in coordinates]
    evaluate = sp.lambdify((k, nu, u, x, y), [metric, metric_derivatives, U, potential_derivatives, alpha_B], "mpmath")
    mp.mp.dps = 70
    samples = [
        # k, nu, fields, proper-time velocities, sigma, pi; none is a solution.
        (".000001", "1", [".2", "1.1", "-.7"], [".03", "-.04", ".02"], "1.3", ".2"),
        (".01", "1", ["-.6", ".4", ".9"], ["-.2", ".1", "-.08"], ".4", ".02"),
        (".2", "1", [".7", "-1.3", ".2"], [".3", "-.2", ".4"], "2.1", ".7"),
        (".32", "1", ["-2", "2.5", "-1.6"], ["-.5", ".2", "-.1"], "4", ".1"),
        (".1", "100", ["3", ".2", "1.4"], [".02", "-.03", ".08"], ".05", "0"),
    ]
    max_residual = mp.mpf(0)
    for index, (ks, ns, field, velocity, sigma_s, pi_s) in enumerate(samples):
        ks, ns = mp.mpf(ks), mp.mpf(ns)
        field, velocity = [mp.mpf(q) for q in field], [mp.mpf(q) for q in velocity]
        sigma, pi = mp.mpf(sigma_s), mp.mpf(pi_s)
        metric_v, dmetric_v, Uv, dUv, ab = evaluate(ks, ns, *field)
        norm = sum(metric_v[i]*velocity[i]**2 for i in range(3))
        H = mp.sqrt((norm+2*Uv+2*sigma)/3)
        connection = []
        for i in range(3):
            # Levi-Civita contraction for a diagonal metric.
            connection.append(sum(dmetric_v[i][j]*velocity[i]*velocity[j]/metric_v[i]
                              - dmetric_v[j][i]*velocity[j]**2/(2*metric_v[i]) for j in range(3)))
        acceleration = [-ENERGY_FRICTION*H*velocity[i]-connection[i]
                        -(dUv[i]+(SOURCE_SIGN*ab*(sigma-3*pi) if i == 0 else 0))/metric_v[i] for i in range(3)]
        energy_dot = sum(mp.mpf(".5")*dmetric_v[i][j]*velocity[j]*velocity[i]**2 for i in range(3) for j in range(3))
        energy_dot += sum(metric_v[i]*velocity[i]*acceleration[i]+dUv[i]*velocity[i] for i in range(3))
        target = -3*H*norm-ab*(sigma-3*pi)*velocity[0]
        residual = abs(energy_dot-target)/max(mp.mpf(1), abs(target))
        max_residual = max(max_residual, residual)
        checks.append({"name": "action.off_orbit_energy."+str(index), "passed": bool(residual < mp.mpf("1e-55")), "residual": mp.nstr(residual, 12)})
    return {"scope": "Exact model identities and arbitrary-state action energy balance; handwritten theorem remains essential; no empirical test or effective audit status.",
            "checks": checks, "counts": {"passed": sum(q["passed"] for q in checks), "failed": sum(not q["passed"] for q in checks)},
            "max_scaled_energy_residual": mp.nstr(max_residual, 12)}


if __name__ == "__main__":
    result = run_checks()
    print(json.dumps(result, indent=2))
    sys.exit(bool(result["counts"]["failed"]))
