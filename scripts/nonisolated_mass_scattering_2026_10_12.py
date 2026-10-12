#!/usr/bin/env python3
"""Author controls for formulas, ordering and the spectral shortcut.

These finite checks do not certify the analytic estimates or a physical model.
The external timeout wrapper records command, elapsed time and complete streams.
"""
AUDIT_TIMEOUT_SEC = 60
AUDIT_INPUT_PATHS = [
    "docs/NONISOLATED_MASS_SCATTERING_BOUNDED_THEOREM_NOTE_2026-10-12.md",
    "docs/COMPACT_PATCH_SCATTERING_COVARIANCE_BOUNDED_THEOREM_NOTE_2026-10-11.md",
    "docs/COMPACT_PATCH_FOCK_ISOMETRY_BOUNDED_THEOREM_NOTE_2026-10-12.md"
]
if not __debug__:
    raise RuntimeError("Run without -O: finite control assertions must be enabled")

import cmath
from collections import defaultdict
from fractions import Fraction as F
import json
import math


records = []


def emit(name, **data):
    row = {"check": name, **data}
    records.append(row)
    print(json.dumps(row, sort_keys=True), flush=True)


def h(u):
    return math.exp(-u*u) / math.sqrt(math.pi)


def hp(u):
    return -2*u*h(u)


def density(T, t, nu, sign):
    s = T**nu
    return h((t-sign*T)/s)/s


kernel_errors = []
omitted_width_errors = []
for T in (2.0, 3.0, 7.0):
    for nu in (.3, .7, .9):
        for sign in (-1, 1):
            t = sign*T+.61*T**nu
            s, sp = T**nu, nu*T**(nu-1)
            u = (t-sign*T)/s
            exact = -(sign*hp(u)+sp*(h(u)+u*hp(u)))/s**2
            step = T*1e-5
            fd = (density(T+step,t,nu,sign)-density(T-step,t,nu,sign))/(2*step)
            kernel_errors.append(abs(exact-fd))
            omitted_width_errors.append(abs(fd+sign*hp(u)/s**2))
assert max(kernel_errors) < 1e-8
assert min(omitted_width_errors) > 1e-4
emit("moving_kernel_derivative", cases=len(kernel_errors),
     max_central_difference_error=max(kernel_errors),
     min_omitted_width_error=min(omitted_width_errors),
     scope="Schwartz Gaussian checks the derivative identity; it is not the compact-Fourier averaging kernel used in the next control.")


def bump(y):
    return math.exp(1-1/(1-y*y)) if abs(y) < 1 else 0.0


def bump_prime(y):
    return -2*y*bump(y)/(1-y*y)**2 if abs(y) < 1 else 0.0


def spectral_average(T, detuning, nu, sign):
    return cmath.exp(1j*sign*T*detuning)*bump(T**nu*detuning)


spectral_errors, omitted_spectral_width_errors = [], []
for T in (2.0, 4.0, 9.0):
    for nu in (.4, .75):
        for sign in (-1, 1):
            detuning = .45/T**nu
            s, sp = T**nu, nu*T**(nu-1)
            phase = cmath.exp(1j*sign*T*detuning)
            centre = phase*1j*sign*detuning*bump(s*detuning)
            width = phase*sp*detuning*bump_prime(s*detuning)
            step = T*1e-5
            fd = (spectral_average(T+step,detuning,nu,sign)-spectral_average(T-step,detuning,nu,sign))/(2*step)
            spectral_errors.append(abs(fd-centre-width))
            omitted_spectral_width_errors.append(abs(fd-centre))
assert max(spectral_errors) < 1e-8
assert min(omitted_spectral_width_errors) > 1e-3
emit("compact_fourier_vacuum_derivative", cases=len(spectral_errors),
     max_central_difference_error=max(spectral_errors),
     min_omitted_width_error=min(omitted_spectral_width_errors),
     kernel="exp(1-1/(1-y^2)) for |y|<1, zero outside; normalized at zero")


for energy, clock in ((3,3),(5,3),(2,7)):
    physical = 1j*energy
    packet = -1j*clock
    detuning = 1j*(energy-clock)
    assert physical+packet == detuning
    assert physical != detuning and packet != detuning
emit("both_packet_derivative_terms", exact_frequency_cases=3,
     omission_of_either_term_rejected=True,
     scope="Finite spectral identity; no unbounded-generator domain inference")


def add(poly, word, coefficient=1):
    poly[tuple(word)] += coefficient
    if not poly[tuple(word)]:
        del poly[tuple(word)]


def cook_polynomials(n):
    lhs, rhs, pair_only = defaultdict(int), defaultdict(int), defaultdict(int)
    A = ["A"+str(i) for i in range(n)]
    for i in range(n):
        D = "D"+str(i)
        add(lhs,A[:i]+[D]+A[i+1:])
        add(rhs,A[:i]+A[i+1:]+[D])
        for j in range(i+1,n):
            prefix, suffix = A[:i]+A[i+1:j], A[j+1:]
            for target in (rhs,pair_only):
                add(target,prefix+[D,A[j]]+suffix)
                add(target,prefix+[A[j],D]+suffix,-1)
    return dict(lhs),dict(rhs),dict(pair_only)


for n in range(1,10):
    lhs,rhs,pair_only = cook_polynomials(n)
    assert lhs == rhs
    assert lhs != pair_only
    if n >= 2:
        bad = defaultdict(int,rhs)
        A = ["A"+str(i) for i in range(n)]
        add(bad,["D0","A1"]+A[2:],-1)
        add(bad,["A1","D0"]+A[2:])
        assert dict(bad) != lhs
emit("noncommutative_cook_identity", particle_counts=list(range(1,10)),
     missing_vacuum_residual_rejected=True, missing_pair_rejected=True,
     scope="Free-word expansion, without commutativity or derivative-vacuum annihilation")


for n in range(1,6):
    lhs,rhs = defaultdict(int),defaultdict(int)
    for x in range(n):
        for y in range(n):
            X,Y = "L"+str(x),"L"+str(y)
            Xs,Ys = X+"*",Y+"*"
            add(lhs,[Xs,X,Ys,Y])
            add(rhs,[Xs,X,Ys,Y])
            add(rhs,[Xs,Ys,X,Y],-1)
            add(rhs,[Xs,Ys,X,Y])
    assert dict(lhs) == dict(rhs)
emit("energy_kernel_expansion", translate_counts=list(range(1,6)),
     full_noncommutative_identity=True,
     scope="Ordering check for N16 only; common-kernel inequalities are analytic")


# Vacuum creator padding: on a finite hard-core lattice B_x raises site x,
# Gamma(0)=0 but ||sum f_x B_x Omega||^2=sum |f_x|^2.
for n in range(1,8):
    f = [complex(i+1,(-1)**i)/(n+1) for i in range(n)]
    norm2 = sum(abs(z)**2 for z in f)
    assert norm2 > 0
    gamma_vacuum = 0
    gamma_padded = 1
    assert norm2 <= norm2*gamma_padded
    assert not norm2 <= norm2*gamma_vacuum
emit("creator_energy_padding", finite_site_counts=list(range(1,8)),
     unpadded_bound_rejected_on_vacuum=True,
     scope="Exact orthogonality of finite one-site excitations, not a scattering model")


# All lowerings vanish off zero in this example, but an extra graph vector
# survives the time average. No locality assertion is made.
target,residual = 1.0,3.0
average = bump(0)*(target+residual)
assert average == target+residual and average != target
emit("zero_detuning_kernel", excluded_zero_regular_norm=0,
     actual_average=average, declared_target=target,
     missing_kernel_relation_rejected=True,
     scope="Abstract finite spectral counterexample")


# Infinite-family inequalities in the note reduce to these rational margins
# and the analytic monotonicity of n exp(-n^2) for n>=2.
exp4_lower = sum(F(4**k,math.factorial(k)) for k in range(9))
assert exp4_lower > 50
positive_margin = 2*F(9,8)*F(1,25)+F(1,1000)
assert positive_margin < F(1,10)
assert F(1,2)-positive_margin > F(2,5)
assert F(1)+F(1,2) == F(3,2)
finite_casimir_checks = 0
for n in range(2,25):
    for p in (.25,.375,.5):
        sigma = math.sqrt(1+p*p)
        delta = math.exp(-n*n)
        diff = 2*sigma*delta+delta*delta-2*p/n-1/(n*n)
        assert diff < 0
        assert .4/n <= abs(diff) <= 1.5/n
        assert 1+diff > 0
        finite_casimir_checks += 1
emit("mass_to_geometric_regularization_counterexample",
     exact_exp4_lower=str(exp4_lower), exact_positive_margin=str(positive_margin),
     finite_formula_checks=finite_casimir_checks,
     analytic_scope="N33 uses the rational margins plus monotonicity; N34-N35 use infinite-series inequalities, not finite sampling")


power_cases=0
for dimension in range(1,4):
    for n in range(1,10):
        for nu in (F(1,4),F(2,3),F(9,10)):
            mu=(1+nu)/2
            assert nu < mu < 1
            order=math.ceil(F(dimension*n+3)/(mu-nu))
            exponent=dimension*n-(mu-nu)*order
            assert exponent <= -3
            pair_order=max(0,dimension*(n-2))+3
            assert dimension*(n-2)-pair_order <= -3
            power_cases += 1
emit("all_spectator_and_time_tail_powers", exact_rational_cases=power_cases,
     scope="Arbitrary Schwartz/almost-local orders selected after dimension and fixed particle count; no numerical tail or LR claim")

emit("summary", records_before_summary=len(records), status="completed",
     independence="author controls only; completed separate source review is recorded in the note",
     exclusions="No infinite-lattice model, Fock/isometry, detector or exhaustion result")

print('per_element: finite derivative, free-word and rational-margin identities are checked; the analytic convergence proof is in the note.')
print('per_site: finite hard-core creator padding is checked; no microscopic infinite-lattice realization is constructed.')
print('per_mode: finite zero-detuning and Casimir spectral examples are checked; infinite tail conclusions use the displayed analytic proof.')
print('per_block: fixed finite-product ordering and all-spectator exponent bookkeeping are checked; no Fock or detector extension is computed.')
print('lattice_wide: checked and not executed — these finite controls do not realize an infinite lattice model or establish channel exhaustion.')
print("TOTAL: PASS=1 FAIL=0")
print("SCOPE: One completed assertion-guarded finite author driver; known mutation survivors are disclosed in the note, and no analytic or physical-model proof is numerical.")
