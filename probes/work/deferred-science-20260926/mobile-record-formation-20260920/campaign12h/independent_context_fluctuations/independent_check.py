#!/usr/bin/env python3
"""Independent finite controls for an equilibrium Euler-fluctuation proof.

No primary campaign source is read. Exact arithmetic is used except for the
explicit finite-generator matrix exponentials and the constant-rate table.
"""
from __future__ import annotations

import itertools
import json
import math
from functools import lru_cache
from pathlib import Path

import numpy as np
import scipy
from scipy.linalg import expm
import sympy as sp

HERE = Path(__file__).resolve().parent
LOG = HERE / "PROGRESS.log"
LOG.write_text("")
checks = []


def check(name, condition, **evidence):
    if not bool(condition):
        raise AssertionError(name)
    checks.append({"name": name, "status": "PASS", **evidence})
    with LOG.open("a") as stream:
        stream.write(name + " PASS\n")


def same_matrix(left, right):
    return all(sp.simplify(value) == 0 for value in left-right)


R = sp.Rational
VECTORS = [(0, 0, 0), (1, 0, 0), (-1, 0, 0),
           (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
MODELS = {
    "context_tuned_rho_half": dict(u=-1, E=1, A=1, B=0, K0=4, floor=1),
    "axis_balanced": dict(u=0, E=R(1, 2), A=2, B=-3, K0=3, floor=1),
}


def fs(model, axis=0):
    f = [sp.Integer(v[axis]) for v in VECTORS]
    s = [sp.Integer(model["A"] * int(a != 0) + model["B"] * int(f[a] != 0))
         for a in range(7)]
    return f, s


def rate(model, implementation, word, axis=0):
    l, a, b, r = word
    f, s = fs(model, axis)
    h = (model["u"] * (f[a] - f[b]) + model["E"] *
         ((f[a] - f[b]) * (s[l] + s[r])
          + (s[a] - s[b]) * (f[l] + f[r])))
    if implementation == "linear":
        return sp.Rational(model["K0"]) + h / 2
    return sp.Rational(model["floor"]) + max(h, 0)


def flux(model, p, axis=0):
    f, s = fs(model, axis)
    mean_f = sum(p[a-1] * f[a] for a in range(1, 7))
    mean_s = sum(p[a-1] * s[a] for a in range(1, 7))
    U = model["u"] + 2 * model["E"] * mean_s
    Z = model["u"] + 4 * model["E"] * mean_s
    return sp.Matrix([p[a-1] * (U * f[a] +
                     (2 * model["E"] * s[a] - Z) * mean_f)
                     for a in range(1, 7)])


def current_jacobian(model, p, axis=0):
    f, s = fs(model, axis)
    mean_f = sum(p[a-1] * f[a] for a in range(1, 7))
    mean_s = sum(p[a-1] * s[a] for a in range(1, 7))
    E = model["E"]
    U, Z = model["u"] + 2*E*mean_s, model["u"] + 4*E*mean_s
    return sp.Matrix(6, 6, lambda a, b:
        int(a == b) * (U*f[a+1] + (2*E*s[a+1]-Z)*mean_f)
        + p[a] * (2*E*s[b+1]*f[a+1] - 4*E*s[b+1]*mean_f
                  + (2*E*s[a+1]-Z)*f[b+1]))


def canonical_phi(model, counts, target=1):
    """Exact canonical expectation of the oriented target-label current."""
    M = sum(counts)
    f, s = fs(model)
    mean_f = sum(counts[a] * f[a] for a in range(7)) / M
    mean_s = sum(counts[a] * s[a] for a in range(7)) / M
    mean_fs = sum(counts[a] * f[a] * s[a] for a in range(7)) / M
    fa, sa = f[target], s[target]
    rem_f = (M*mean_f-fa)/(M-1)
    rem_s = (M*mean_s-sa)/(M-1)
    rem_fs = ((M*mean_f-fa)*(M*mean_s-sa)
              - (M*mean_fs-fa*sa))/((M-1)*(M-2))
    return (sp.Rational(counts[target], M) *
            (model["u"]*(fa-rem_f) +
             2*model["E"]*(fa*rem_s+sa*rem_f-2*rem_fs)))


def without_replacement_current(model, implementation, counts, target=1):
    M = sum(counts)
    denominator = M*(M-1)*(M-2)*(M-3)
    numerator = sp.Integer(0)
    for word in itertools.product(range(7), repeat=4):
        multiplicity = 1
        used = [0]*7
        for a in word:
            multiplicity *= counts[a]-used[a]
            used[a] += 1
        if multiplicity:
            _, a, b, _ = word
            numerator += (multiplicity * rate(model, implementation, word) *
                          (int(a == target)-int(b == target)))
    return sp.cancel(numerator/denominator)


finite_generators = []
states = list(itertools.permutations((0, 1, 3, 4)))
state_index = {state: i for i, state in enumerate(states)}
nstate = len(states)
phase = [1, -sp.I, -1, sp.I]
for model_name, model in MODELS.items():
    for implementation in ("linear", "positive_part"):
        H = sp.zeros(nstate)
        F = sp.zeros(nstate, 1)
        Y = sp.zeros(nstate, 1)
        rates = []
        for row, state in enumerate(states):
            Y[row] = R(1, 2)*sum(phase[x]*int(state[x] == 1) for x in range(4))
            for x in range(4):
                word = tuple(state[(x+d) % 4] for d in (-1, 0, 1, 2))
                c = rate(model, implementation, word)
                rates.append(c)
                moved = list(state)
                moved[x], moved[(x+1) % 4] = moved[(x+1) % 4], moved[x]
                col = state_index[tuple(moved)]
                H[row, col] += c
                H[row, row] -= c
                F[row] += (phase[x]*c *
                           (int(state[x] == 1)-int(state[(x+1) % 4] == 1))/2)
        one = sp.ones(nstate, 1)
        prefix = model_name + "/" + implementation
        check(prefix + "/canonical_stationarity_and_floor",
              H*one == sp.zeros(nstate, 1) and
              H.T*one == sp.zeros(nstate, 1) and min(rates) > 0,
              state_count=nstate, minimum_rate=str(min(rates)),
              maximum_rate=str(max(rates)))
        check(prefix + "/nonreversible", H != H.T)
        check(prefix + "/exact_fourier_conservation_sign",
              same_matrix(H*Y, (-1-sp.I)*F))
        S = (H+H.T)/2
        Pi = sp.ones(nstate)/nstate
        h = ((-S+Pi).inv()*F).applyfunc(sp.simplify)
        norm = sp.simplify((F.conjugate().T*h)[0]/nstate)
        check(prefix + "/symmetric_poisson_identity",
              same_matrix(-S*h, F) and sp.simplify((one.T*h)[0]) == 0 and norm > 0,
              H_minus_one_norm_squared=str(norm))
        Hnp = np.array(H, dtype=float)
        Fnp = np.array(F, dtype=complex).reshape(-1)
        matrix = np.zeros((3*nstate, 3*nstate))
        matrix[:nstate, :nstate] = 4*Hnp
        matrix[:nstate, nstate:2*nstate] = np.eye(nstate)
        matrix[nstate:2*nstate, 2*nstate:] = np.eye(nstate)
        times = []
        for t in (0.2, 1.0, 2.0):
            B = expm(t*matrix)[:nstate, 2*nstate:]
            variance = float(2*np.vdot(Fnp, B@Fnp).real/nstate)
            bound = 2*t*float(norm)/4
            check(prefix + f"/forward_backward_bound_t_{t}",
                  variance >= -1e-10 and variance <= bound + 1e-10,
                  integrated_variance=variance, bound=bound)
            times.append(dict(time=t, variance=variance, bound=bound))
        finite_generators.append(dict(model=model_name,
            implementation=implementation, norm_squared=str(norm), times=times))


for model_name, model in MODELS.items():
    for implementation in ("linear", "positive_part"):
        for counts in ([2, 1, 1, 1, 1, 1, 1], [2]*7):
            exact = canonical_phi(model, counts)
            enumeration = without_replacement_current(model, implementation, counts)
            check(model_name + "/" + implementation +
                  f"/canonical_current_M_{sum(counts)}",
                  exact == enumeration, expectation=str(exact))


@lru_cache(None)
def stirling_second(n, k):
    if n == k == 0:
        return 1
    if n == 0 or k == 0 or k > n:
        return 0
    return k*stirling_second(n-1, k)+stirling_second(n-1, k-1)


def falling(n, k):
    value = 1
    for j in range(k):
        value *= n-j
    return value


count_variables = sp.symbols("k_plus k_minus k_transverse")
group_p = (R(1, 12), R(1, 12), R(1, 3))


@lru_cache(None)
def count_moment(M, powers):
    value = sp.Integer(0)
    for ks in itertools.product(*(range(power+1) for power in powers)):
        term = sp.Integer(falling(M, sum(ks)))
        for power, k, p in zip(powers, ks, group_p):
            term *= stirling_second(power, k)*p**k
        value += term
    return value


def multinomial_expectation(polynomial, M):
    poly = sp.Poly(sp.expand(polynomial), *count_variables)
    return sp.cancel(sum(coefficient*count_moment(M, powers)
                         for powers, coefficient in poly.terms()))


projection_results = []
q_variables = sp.symbols("q_plus q_minus q_transverse")
qp, qm, qt = q_variables
for model_name, model in MODELS.items():
    E, A, B, u = (model[key] for key in ("E", "A", "B", "u"))
    fmean = qp-qm
    smean = (A+B)*(qp+qm)+A*qt
    tau = (A+B)*fmean
    fa, sa = sp.Integer(1), sp.Integer(A+B)
    J = qp*((u+2*E*smean)*fa + (2*E*sa-u-4*E*smean)*fmean)
    substitution = dict(zip(q_variables, group_p))
    Jp = sp.cancel(J.subs(substitution))
    derivative = [sp.diff(J, q).subs(substitution) for q in q_variables]
    check(model_name + "/grouped_current_gradient",
          derivative == [R(1, 4), R(1, 12), R(1, 6)],
          gradient=[str(v) for v in derivative])
    values = []
    for M in (8, 16, 32, 64):
        rem_f, rem_s = (M*fmean-fa)/(M-1), (M*smean-sa)/(M-1)
        rem_fs = ((M*fmean-fa)*(M*smean-sa)-(M*tau-fa*sa))/((M-1)*(M-2))
        Phi = qp*(u*(fa-rem_f)+2*E*(fa*rem_s+sa*rem_f-2*rem_fs))
        linear = sum(d*(q-p) for d, q, p in zip(derivative, q_variables, group_p))
        to_counts = {q: k/M for q, k in zip(q_variables, count_variables)}
        residual = sp.expand((Phi-Jp-linear).subs(to_counts))
        residual_mean = multinomial_expectation(residual, M)
        orthogonal = [multinomial_expectation(residual*(k/M-p), M)
                      for k, p in zip(count_variables, group_p)]
        variance = multinomial_expectation(residual**2, M)
        projection_variance = multinomial_expectation(
            sp.expand((Phi-Jp).subs(to_counts))**2, M)
        check(model_name + f"/projection_centering_M_{M}",
              residual_mean == 0 and orthogonal == [0]*3)
        check(model_name + f"/projection_variance_split_M_{M}",
              projection_variance-variance == R(7, 864*M) and variance > 0,
              quadratic_residual_variance=str(variance),
              M_squared_times_variance=str(M*M*variance),
              linear_variance=str(R(7, 864*M)))
        values.append(dict(M=M, variance=str(variance),
                           M_squared_variance=str(M*M*variance)))
    projection_results.append(dict(model=model_name, values=values))


matrix_controls = []
profiles = {
    "balanced_rho_half": [R(1, 12)]*6,
    "biased_full_support": [R(1, 5), R(1, 10), R(3, 20), R(1, 10), R(3, 20), R(1, 10)],
}
balanced_matrices = {}
for model_name, model in MODELS.items():
    for profile_name, ps in profiles.items():
        p = sp.Matrix(ps)
        p0 = 1-sum(ps)
        C = sp.diag(*ps)-p*p.T
        S = sp.diag(*(1/q for q in ps))+sp.ones(6)/p0
        check(model_name + "/" + profile_name + "/susceptibility_inverse",
              S*C == sp.eye(6))
        matrices = [current_jacobian(model, ps, axis) for axis in range(3)]
        check(model_name + "/" + profile_name + "/entropy_symmetrization",
              all(Ai*C == C*Ai.T for Ai in matrices))
        if profile_name == "balanced_rho_half":
            balanced_matrices[model_name] = matrices
    C = sp.eye(6)/12-sp.ones(6)/144
    Ai = balanced_matrices[model_name]
    AK = 2*sp.pi*(Ai[0]+2*Ai[1]-Ai[2])
    omega = 2*sp.pi
    P = AK**2/omega**2
    check(model_name + "/six_field_acoustic_rank_and_minimal_polynomial",
          AK.rank() == 2 and same_matrix(AK**3, omega**2*AK) and P**2 == P)
    for t in (R(1, 8), R(1, 4)):
        U = sp.eye(6)+(sp.cos(omega*t)-1)*P-sp.I*sp.sin(omega*t)*AK/omega
        cov = sp.simplify(U*C*U.conjugate().T-C)
        density_cov = sp.simplify((sp.ones(1, 6)*U*C*sp.ones(6, 1))[0])
        check(model_name + f"/transported_covariance_t_{t}",
              cov == sp.zeros(6) and density_cov == sp.cos(omega*t)/4,
              density_covariance=str(density_cov))
        matrix_controls.append(dict(model=model_name, time=str(t),
                                    density_covariance=str(density_cov)))
check("two_generators_same_tuned_jacobians",
      balanced_matrices["context_tuned_rho_half"] == balanced_matrices["axis_balanced"])


constant_rate_control = []
for N in (8, 16, 32, 64, 128, 256):
    kappa, t = 1.5, 1.0
    omega_lattice = 2*(1-math.cos(2*math.pi/N))
    decay_euler = math.exp(-kappa*N*omega_lattice*t)
    decay_diffusive = math.exp(-kappa*N*N*omega_lattice*t)
    error_covariance_multiplier = 2*(1-decay_euler)
    upper = 2*kappa*(2*math.pi)**2*t/N
    check(f"constant_rate_exact_three_dimensional_control_N_{N}",
          0 <= error_covariance_multiplier <= upper,
          Euler_covariance_multiplier=decay_euler,
          error_covariance_multiplier=error_covariance_multiplier,
          diffusive_covariance_multiplier=decay_diffusive)
    constant_rate_control.append(dict(N=N,
        Euler_covariance_multiplier=decay_euler,
        error_covariance_multiplier=error_covariance_multiplier,
        upper_bound=upper, diffusive_covariance_multiplier=decay_diffusive))


result = {
    "scope": "Independent finite controls; not a finite-volume proof of the asymptotic theorem.",
    "dependencies": {"numpy": np.__version__, "scipy": scipy.__version__, "sympy": sp.__version__},
    "checks_passed": len(checks), "checks_failed": 0,
    "finite_generator_controls": finite_generators,
    "canonical_projection_controls": projection_results,
    "matrix_controls": matrix_controls,
    "constant_rate_three_dimensional_control": constant_rate_control,
    "checks": checks,
}
serialized = json.dumps(result, indent=2, sort_keys=True)+"\n"
(HERE / "RESULTS.json").write_text(serialized)
print(serialized, end="")
