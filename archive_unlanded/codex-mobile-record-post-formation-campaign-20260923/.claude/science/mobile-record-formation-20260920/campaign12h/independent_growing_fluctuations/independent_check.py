#!/usr/bin/env python3
"""Complete four-site generator controls for a nonstationary fluctuation proof.

All identities before the explicitly labelled reward-integral calculation
use integer/rational arithmetic. No primary or previous checker is imported.
"""
from __future__ import annotations

import itertools
import json
import math
from fractions import Fraction
from pathlib import Path

import numpy as np
import scipy
from scipy.sparse import bmat, csr_matrix, diags
from scipy.sparse.linalg import expm_multiply
import sympy as sp

HERE = Path(__file__).resolve().parent
(HERE / "PROGRESS.log").write_text("")
CHECKS = []


def check(name, condition, **evidence):
    if not bool(condition):
        raise AssertionError(name)
    CHECKS.append(dict(name=name, status="PASS", **evidence))
    with (HERE / "PROGRESS.log").open("a") as stream:
        stream.write(name+" PASS\n")


STATES = np.array(list(itertools.product(range(7), repeat=4)), dtype=np.int64)
SIZE = len(STATES)
POWERS = np.array([7**3, 7**2, 7, 1], dtype=np.int64)
VECTORS = [(0, 0, 0), (1, 0, 0), (-1, 0, 0),
           (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]
PHASE_R = np.array([1, 0, -1, 0], dtype=np.int64)
PHASE_I = np.array([0, -1, 0, 1], dtype=np.int64)
YR = np.column_stack([np.sum((STATES == a)*PHASE_R, axis=1) for a in range(1, 7)])
YI = np.column_stack([np.sum((STATES == a)*PHASE_I, axis=1) for a in range(1, 7)])
MODELS = {
    "old_context": dict(u=-1, twice_E=2, A=1, B=0, K=4, floor=1),
    "axis_balanced": dict(u=0, twice_E=1, A=2, B=-3, K=3, floor=1),
}
INITIAL = [Fraction(1, 2)]+[Fraction(a, 42) for a in range(1, 7)]
BETA = Fraction(1, 3)


def probabilities(survival):
    return [INITIAL[0]*survival]+[
        INITIAL[a]+INITIAL[0]*(1-survival)/6 for a in range(1, 7)]


def integer_weights(probs):
    den = math.lcm(*(p.denominator for p in probs))
    nums = np.array([int(p*den) for p in probs], dtype=np.int64)
    weights = np.prod(nums[STATES], axis=1)
    return den, nums, weights


def build_generator(model, implementation):
    """Store 3G=12H+B with integer edge rates: acceleration 4, beta=1/3."""
    f = np.array([v[0] for v in VECTORS], dtype=np.int64)
    content_s = np.array([model["A"]*int(a != 0)+model["B"]*int(f[a] != 0)
                          for a in range(7)], dtype=np.int64)
    src, dst, rates, birth = [], [], [], []
    fr, fi = np.zeros(SIZE, dtype=np.int64), np.zeros(SIZE, dtype=np.int64)
    for row, word in enumerate(STATES):
        for x in range(4):
            l, a, b, r = (int(word[(x+d) % 4]) for d in (-1, 0, 1, 2))
            h2 = (2*model["u"]*(f[a]-f[b])+model["twice_E"]*
                  ((f[a]-f[b])*(content_s[l]+content_s[r])
                   +(content_s[a]-content_s[b])*(f[l]+f[r])))
            if implementation == "linear":
                num = 12*model["K"]+3*h2
            else:
                num = 12*model["floor"]+6*max(h2, 0)
            if a != b:
                col = row+(b-a)*POWERS[x]+(a-b)*POWERS[(x+1) % 4]
                src.append(row); dst.append(col); rates.append(num); birth.append(False)
                fr[row] += PHASE_R[x]*num*(int(a == 1)-int(b == 1))
                fi[row] += PHASE_I[x]*num*(int(a == 1)-int(b == 1))
        for x in range(4):
            if word[x] == 0:
                for a in range(1, 7):
                    src.append(row); dst.append(row+a*POWERS[x]); rates.append(1); birth.append(True)
    src, dst, rates = (np.asarray(v, dtype=np.int64) for v in (src, dst, rates))
    birth = np.asarray(birth, dtype=bool)
    out = np.zeros(SIZE, dtype=np.int64)
    np.add.at(out, src, rates)
    Gnum = csr_matrix((rates, (src, dst)), shape=(SIZE, SIZE))-diags(out)
    return dict(src=src, dst=dst, rates=rates, birth=birth, out=out,
                Gnum=Gnum.tocsr(), F=(fr+1j*fi)/24)


def apply_edges(data, values, selector=None):
    if selector is None:
        selector = np.ones(len(data["src"]), dtype=bool)
    src, dst, rate = (data[key][selector] for key in ("src", "dst", "rates"))
    answer = np.zeros_like(values)
    differences = values[dst]-values[src]
    factor = rate if values.ndim == 1 else rate[:, None]
    np.add.at(answer, src, factor*differences)
    return answer


def weighted_dyad(real, imag, weights):
    re = real.T@(weights[:, None]*real)+imag.T@(weights[:, None]*imag)
    im = imag.T@(weights[:, None]*real)-real.T@(weights[:, None]*imag)
    return re, im


def jacobian(model, probs, axis):
    ps = [sp.Rational(p.numerator, p.denominator) for p in probs[1:]]
    E = sp.Rational(model["twice_E"], 2)
    f = [sp.Integer(v[axis]) for v in VECTORS[1:]]
    content_s = [sp.Integer(model["A"]+model["B"]*int(value != 0)) for value in f]
    m = sum(p*x for p, x in zip(ps, f))
    sigma = sum(p*x for p, x in zip(ps, content_s))
    U, Z = model["u"]+2*E*sigma, model["u"]+4*E*sigma
    return sp.Matrix(6, 6, lambda a, b:
        int(a == b)*(U*f[a]+(2*E*content_s[a]-Z)*m)
        +ps[a]*(2*E*content_s[b]*f[a]-4*E*content_s[b]*m
                +(2*E*content_s[a]-Z)*f[b]))


numerical_data = None
for model_name, model in MODELS.items():
    for implementation in ("linear", "positive_part"):
        prefix = model_name+"/"+implementation
        data = build_generator(model, implementation)
        src, dst, rate, birth = (data[key] for key in ("src", "dst", "rates", "birth"))
        check(prefix+"/complete_generator", SIZE == 2401 and min(rate) > 0
              and np.all(np.asarray(data["Gnum"].sum(axis=1)).reshape(-1) == 0),
              states=SIZE, transitions=len(rate))
        if model_name == "axis_balanced" and implementation == "positive_part":
            numerical_data = data
        for survival in (Fraction(1), Fraction(1, 2), Fraction(1, 4)):
            tag = prefix+"/survival_"+str(survival)
            probs = probabilities(survival)
            D, nums, weights = integer_weights(probs)
            incoming = np.zeros(SIZE, dtype=np.int64)
            np.add.at(incoming, dst, weights[src]*rate)
            forward = incoming-weights*data["out"]
            local_dot3 = np.array([-6*nums[0]]+[nums[0]]*6, dtype=np.int64)
            derivative = np.zeros(SIZE, dtype=np.int64)
            for x in range(4):
                other = np.prod(nums[STATES[:, [j for j in range(4) if j != x]]], axis=1)
                derivative += local_dot3[STATES[:, x]]*other
            check(tag+"/exact_product_forward_equation", np.array_equal(forward, derivative))
            check(tag+"/reverse_rates_and_score_correction",
                  np.all(weights[src[~birth]] == weights[dst[~birth]])
                  and np.all(weights[src[birth]]*nums[STATES[dst[birth],
                      np.argmax(STATES[src[birth]] != STATES[dst[birth]], axis=1)]]
                      == weights[dst[birth]]*nums[0])
                  and np.all(-weights*data["out"]-forward == -incoming)
                  and np.any(forward != 0),
                  reverse_birth_rate="beta p0(t)/pa(t)",
                  formal_adjoint_row_sums_nonzero=True)
            u = (np.sum(STATES == 1, axis=1)
                 +2*((STATES[:, 0] == 2)&(STATES[:, 2] == 3)).astype(np.int64)
                 -((STATES[:, 1] == 0)&(STATES[:, 3] == 4)).astype(np.int64))
            udot = np.sum(STATES == 2, axis=1)-np.sum(STATES == 5, axis=1)
            Gu_num = apply_edges(data, u)
            du = u[dst]-u[src]
            gamma_num = int(np.sum(weights[src]*rate*du**2))
            lhs = int(np.sum(forward*u*u)+6*np.sum(weights*u*udot))
            rhs = int(2*np.sum(weights*u*(3*udot+Gu_num))+gamma_num)
            unit_sum = int(np.sum(weights[src[~birth]]*du[~birth]**2))
            exchange_gamma = int(np.sum(weights[src[~birth]]*rate[~birth]*du[~birth]**2))
            check(tag+"/evolving_energy_and_floor", lhs == rhs and exchange_gamma >= 12*unit_sum)
            count = np.sum(STATES == 1, axis=1)
            negative_form = -int(np.sum(weights*count*apply_edges(data, count)))
            check(tag+"/naive_stationary_energy_counterexample",
                  negative_form == -12*int(nums[1])*int(nums[0])*D**2 and negative_form < 0,
                  minus_E_u_Gu=str(Fraction(negative_form, 3*D**4)))
            covariance_re, covariance_im = weighted_dyad(YR, YI, weights)
            expected_cov = 4*D**3*np.diag(nums[1:])-4*D**2*np.outer(nums[1:], nums[1:])
            covdot_re, covdot_im = weighted_dyad(YR, YI, forward)
            expected_dot = (4*int(nums[0])*D**3*np.eye(6, dtype=np.int64)
                 -4*int(nums[0])*D**2*(np.ones((6, 1), dtype=np.int64)*nums[None, 1:]
                                       +nums[1:, None]*np.ones((1, 6), dtype=np.int64)))
            check(tag+"/exact_one_time_six_field_covariance",
                  np.array_equal(covariance_re, expected_cov) and np.all(covariance_im == 0)
                  and np.array_equal(covdot_re, expected_dot) and np.all(covdot_im == 0))
            dyr, dyi = YR[dst]-YR[src], YI[dst]-YI[src]
            gamma_re, gamma_im = weighted_dyad(dyr, dyi, weights[src]*rate)
            gyr, gyi = apply_edges(data, YR), apply_edges(data, YI)
            drift_re = gyr.T@(weights[:, None]*YR)+gyi.T@(weights[:, None]*YI)
            drift_im = gyi.T@(weights[:, None]*YR)-gyr.T@(weights[:, None]*YI)
            check(tag+"/complete_generator_covariance_energy",
                  np.array_equal(drift_re+drift_re.T+gamma_re, expected_dot)
                  and np.all(drift_im-drift_im.T+gamma_im == 0))
            birth_gamma_re, birth_gamma_im = weighted_dyad(dyr[birth], dyi[birth],
                                                          weights[src[birth]]*rate[birth])
            by_r, by_i = apply_edges(data, YR, birth), apply_edges(data, YI, birth)
            check(tag+"/birth_drift_and_noise_normalization",
                  np.array_equal(birth_gamma_re, 4*int(nums[0])*D**3*np.eye(6, dtype=np.int64))
                  and np.all(birth_gamma_im == 0)
                  and np.array_equal(by_r, -np.repeat(np.sum(YR, axis=1)[:, None], 6, axis=1))
                  and np.array_equal(by_i, -np.repeat(np.sum(YI, axis=1)[:, None], 6, axis=1)),
                  noise_covariance="beta p0(t) I_6")
            ps = sp.Matrix([sp.Rational(p.numerator, p.denominator) for p in probs[1:]])
            p0 = sp.Rational(probs[0].numerator, probs[0].denominator)
            C = sp.diag(*ps)-ps*ps.T
            reaction = -sp.ones(6)/3
            Cdot = p0*(sp.eye(6)-sp.ones(6, 1)*ps.T-ps*sp.ones(1, 6))/3
            check(tag+"/limit_lyapunov_identity",
                  all(jacobian(model, probs, axis)*C == C*jacobian(model, probs, axis).T
                      for axis in range(3))
                  and Cdot == reaction*C+C*reaction.T+p0*sp.eye(6)/3)


for model_name, model in MODELS.items():
    drifts = []
    for survival in (Fraction(1), Fraction(1, 2)):
        A = sum((k*jacobian(model, probabilities(survival), axis)
                 for axis, k in enumerate((1, 2, -1))), sp.zeros(6))
        drifts.append(-2*sp.pi*sp.I*A-sp.ones(6)/3)
    commutator = (drifts[0]*drifts[1]-drifts[1]*drifts[0]).applyfunc(sp.simplify)
    check(model_name+"/time_ordering_needed", commutator != sp.zeros(6),
          example_commutator_entry=str(next(x for x in commutator if x != 0)))


# A constant-rate subfamily gives an exact finite-N covariance control.
constant = build_generator(dict(u=0, twice_E=0, A=1, B=0, K=1, floor=1), "linear")
constant_drift3 = -24*np.eye(6, dtype=np.int64)-np.ones((6, 6), dtype=np.int64)
check("constant_rate/full_generator_fourier_drift",
      np.array_equal(apply_edges(constant, YR), YR@constant_drift3.T)
      and np.array_equal(apply_edges(constant, YI), YI@constant_drift3.T),
      drift="-8 I_6-beta 11^T for the four-cycle mode pi/2, acceleration 4")
D, nums, weights = integer_weights(INITIAL)
src, dst, rate, birth = (constant[key] for key in ("src", "dst", "rates", "birth"))
gr, gi = weighted_dyad(YR[dst[~birth]]-YR[src[~birth]],
                       YI[dst[~birth]]-YI[src[~birth]],
                       weights[src[~birth]]*rate[~birth])
cov_num, _ = weighted_dyad(YR, YI, weights)
check("constant_rate/exact_exchange_bracket", np.array_equal(gr, 48*cov_num) and np.all(gi == 0),
      expected_exchange_bracket="16 C(t); finite-N stirring noise is not zero")


# Numerical test of the proved energy bound on the COMPLETE growing chain.
data = numerical_data
src, dst, rate, birth = (data[key] for key in ("src", "dst", "rates", "birth"))
out_exchange = np.zeros(SIZE)
np.add.at(out_exchange, src[~birth], rate[~birth]/12)
H = csr_matrix((rate[~birth]/12, (src[~birth], dst[~birth])), shape=(SIZE, SIZE))-diags(out_exchange)
S = (H+H.T)/2
Ffield = data["F"]
groups = {}
for row, state in enumerate(STATES):
    groups.setdefault(tuple(sorted(state)), []).append(row)
h = np.zeros(SIZE, dtype=complex)
max_residual = 0.0
for group in groups.values():
    indices = np.array(group)
    matrix = -S[indices][:, indices].toarray()+np.ones((len(group), len(group)))/len(group)
    assert abs(np.mean(Ffield[indices])) < 1e-12
    h[indices] = np.linalg.solve(matrix, Ffield[indices])
    max_residual = max(max_residual, float(np.max(np.abs((-S[indices][:, indices])@h[indices]-Ffield[indices]))))
check("nonstationary_energy/complete_count_sector_poisson_control",
      len(groups) == 210 and max_residual < 1e-11,
      count_sectors=len(groups), maximum_poisson_residual=max_residual)
G = data["Gnum"].astype(float)/3
Gt = G.T.tocsr().astype(complex)
DF, DFbar = diags(Ffield), diags(np.conjugate(Ffield))
zero = csr_matrix((SIZE, SIZE), dtype=complex)
reward_generator = bmat([[Gt, zero, zero, zero],
                         [DF, Gt, zero, zero],
                         [DFbar, zero, Gt, zero],
                         [zero, DFbar, DF, Gt]], format="csr")
initial_probabilities = np.array([float(p) for p in INITIAL])
mu0 = np.prod(initial_probabilities[STATES], axis=1)
reward_initial = np.concatenate((mu0, np.zeros(3*SIZE))).astype(complex)
nodes, quadrature_weights = np.polynomial.legendre.leggauss(24)
energy_results = []
for time in (0.1, 0.4, 0.8):
    evolved = expm_multiply(reward_generator*time, reward_initial)
    variance = float(np.sum(evolved[3*SIZE:]).real)
    mean = complex(np.sum(evolved[SIZE:2*SIZE]))
    values = []
    for node in nodes:
        t = time*(node+1)/2
        survival = math.exp(-2*t)
        ps = initial_probabilities.copy()
        ps[0] *= survival
        ps[1:] += initial_probabilities[0]*(1-survival)/6
        mu = np.prod(ps[STATES], axis=1)
        values.append(float(np.vdot(Ffield, mu*h).real))
    integrated_norm = time*np.dot(quadrature_weights, values)/2
    bound = 2*integrated_norm/4
    check(f"nonstationary_energy/full_reward_bound_t_{time}",
          variance >= 0 and variance <= bound+1e-9 and abs(mean) < 1e-10,
          additive_functional_variance=variance, energy_bound=float(bound),
          mean_abs=abs(mean), quadrature_nodes=24)
    energy_results.append(dict(time=time, variance=variance, bound=float(bound)))


RESULT = {
    "checks_passed": len(CHECKS), "checks_failed": 0,
    "complete_generator_state_count": SIZE,
    "models_and_implementations": 4,
    "exact_product_trajectory_samples": ["exp(-6 beta t)=1", "1/2", "1/4"],
    "checks": CHECKS,
    "numerical_energy_controls": energy_results,
    "software": {"numpy": np.__version__, "scipy": scipy.__version__, "sympy": sp.__version__},
    "scope": "Complete finite generators check exact nonstationary identities; one sparse reward calculation is numerical. The limiting theorem is proved separately.",
}
serialized = json.dumps(RESULT, indent=2, sort_keys=True)+"\n"
(HERE / "RESULTS.json").write_text(serialized)
print(serialized, end="")
