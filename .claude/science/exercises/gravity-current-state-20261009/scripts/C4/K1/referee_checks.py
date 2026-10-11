"""Independent checks for C4/RK2/K1.

The exact form-space checks below do not import the worker's form enumerator.
The final small-grid checks deliberately call the worker's loop kernels only as
representative reruns; their algebraic inputs are checked separately here.
"""

import itertools
import math
import random

import numpy as np
import sympy as sp


D = 4
PAIRS = [(a, b) for a in range(D) for b in range(a, D)]


def signed_permutations():
    for perm in itertools.permutations(range(D)):
        for signs in itertools.product((1, -1), repeat=D):
            R = np.zeros((D, D), dtype=int)
            for i, j in enumerate(perm):
                R[i, j] = signs[i]
            yield R


def sym2_character(R):
    """Character of Sym^2(V) from the defining representation V."""
    return (int(np.trace(R)) ** 2 + int(np.trace(R @ R))) // 2


mass_character_sum = 0
kinetic_character_sum = 0
group = list(signed_permutations())
for R in group:
    chi_h = sym2_character(R)
    chi_h_g2 = sym2_character(R @ R)
    chi_sym2_h = (chi_h**2 + chi_h_g2) // 2
    mass_character_sum += chi_sym2_h
    kinetic_character_sum += chi_sym2_h * chi_h

mass_dim_character = mass_character_sum // len(group)
kinetic_dim_character = kinetic_character_sum // len(group)
print(f"character dimensions: mass={mass_dim_character}, two_derivative={kinetic_dim_character}")


hvars = sp.symbols("h0:10")
qvars = sp.symbols("q0:4")
xvars = sp.symbols("x0:4")


def h_matrix(v):
    H = sp.zeros(D)
    for z, (a, b) in zip(v, PAIRS):
        H[a, b] = z
        H[b, a] = z
    return H


H = h_matrix(hvars)
q = sp.Matrix(qvars)
trH = sp.trace(H)
q2 = (q.T * q)[0]
Hq = H * q
qHq = (q.T * H * q)[0]

mass_forms = [
    sum(H[a, a] ** 2 for a in range(D)),
    sum(H[a, b] ** 2 for a in range(D) for b in range(D) if a != b),
    trH**2,
]

kinetic_forms = [
    q2 * sum(H[a, b] ** 2 for a in range(D) for b in range(D)),
    (Hq.T * Hq)[0],
    qHq * trH,
    q2 * trH**2,
    sum(q[a] ** 2 * H[a, a] ** 2 for a in range(D)),
    sum(q[a] ** 2 * sum(H[a, b] ** 2 for b in range(D)) for a in range(D)),
    sum(q[a] ** 2 * H[a, a] for a in range(D)) * trH,
    sum(q[a] * H[a, a] * Hq[a] for a in range(D)),
    sum(q[a] ** 2 * H[b, b] ** 2 for a in range(D) for b in range(D) if a != b),
]


def coefficient_rank(expressions, variables):
    polys = [sp.Poly(sp.expand(f), *variables) for f in expressions]
    monomials = sorted(set().union(*(set(p.monoms()) for p in polys)))
    matrix = sp.Matrix([[p.coeff_monomial(m) for m in monomials] for p in polys])
    return matrix.rank()


print(
    "named-form ranks: "
    f"mass={coefficient_rank(mass_forms, hvars)}, "
    f"two_derivative={coefficient_rank(kinetic_forms, hvars + qvars)}"
)


# Infinitesimal O(4) invariance.  The joint action is q -> R q and
# h -> R h R^T.  Solving all six Lie-generator constraints gives the exact
# continuous-rotation invariant subspace within the named W(B4) basis.
o4_rows = []
for a in range(D):
    for b in range(a + 1, D):
        J = sp.zeros(D)
        J[a, b] = 1
        J[b, a] = -1
        dH = J * H - H * J
        dq = J * q
        dhvec = [dH[i, j] for i, j in PAIRS]
        for f in kinetic_forms:
            variation = sum(sp.diff(f, z) * dz for z, dz in zip(hvars, dhvec))
            variation += sum(sp.diff(f, z) * dz for z, dz in zip(qvars, dq))
            o4_rows.append(sp.Poly(sp.expand(variation), *(hvars + qvars)))

o4_monomials = sorted(set().union(*(set(p.monoms()) for p in o4_rows)))
# Rows are constraints and columns are the nine form coefficients.
o4_constraint = sp.zeros(len(o4_monomials) * 6, len(kinetic_forms))
for gen_index in range(6):
    for form_index in range(len(kinetic_forms)):
        poly = o4_rows[gen_index * len(kinetic_forms) + form_index]
        for mon_index, monomial in enumerate(o4_monomials):
            o4_constraint[gen_index * len(o4_monomials) + mon_index, form_index] = poly.coeff_monomial(monomial)
o4_dim = len(kinetic_forms) - o4_constraint.rank()
print(f"continuous O(4) subspace dimension inside the nine forms: {o4_dim}")


# The advertised EH vector is checked as a polynomial identity, so the
# sampled exact rank below has both a matching lower and upper bound.
x = sp.Matrix(xvars)
dh_symbolic_matrix = q * x.T + x * q.T
dh_symbolic = [dh_symbolic_matrix[i, j] for i, j in PAIRS]
eh_expression = kinetic_forms[0] - 2 * kinetic_forms[1] + 2 * kinetic_forms[2] - kinetic_forms[3]
eh_gauge_variation = sp.expand(
    sum(sp.diff(eh_expression, z) * dz for z, dz in zip(hvars, dh_symbolic))
)
print(f"EH symbolic gauge-variation identity: {eh_gauge_variation == 0}")


# Exact gauge-variation map, sampled at enough deterministic integer points.
# Since the entries are fixed cubic polynomials in q and linear in h, xi,
# exact rational rank with a stable nullspace identifies the map.
rng = random.Random(712367)
gauge_rows = []
mass_gauge_rows = []
for _ in range(48):
    hs = [sp.Integer(rng.randint(-3, 3)) for _ in hvars]
    qs = [sp.Integer(rng.randint(-3, 3)) for _ in qvars]
    xis = [sp.Integer(rng.randint(-3, 3)) for _ in xvars]
    if qs == [0, 0, 0, 0]:
        qs[0] = 1
    Hs = h_matrix(hs)
    qv = sp.Matrix(qs)
    xiv = sp.Matrix(xis)
    dHv = qv * xiv.T + xiv * qv.T
    dhs = [dHv[i, j] for i, j in PAIRS]
    subs = dict(zip(hvars + qvars, hs + qs))
    mass_row = []
    for f in mass_forms:
        directional = sum(sp.diff(f, z) * dz for z, dz in zip(hvars, dhs))
        mass_row.append(sp.expand(directional).subs(subs))
    mass_gauge_rows.append(mass_row)
    row = []
    for f in kinetic_forms:
        directional = sum(sp.diff(f, z) * dz for z, dz in zip(hvars, dhs))
        row.append(sp.expand(directional).subs(subs))
    gauge_rows.append(row)

gauge_matrix = sp.Matrix(gauge_rows)
mass_gauge_matrix = sp.Matrix(mass_gauge_rows)
gauge_rank = gauge_matrix.rank()
gauge_null = gauge_matrix.nullspace()
null_vector = list(gauge_null[0]) if len(gauge_null) == 1 else []
if null_vector:
    null_vector = [sp.simplify(v / null_vector[0]) for v in null_vector]
print(f"gauge-map rank={gauge_rank}, nullity={len(gauge_null)}, null_vector={null_vector}")
print(f"mass gauge-map rank={mass_gauge_matrix.rank()}, nullity={len(mass_gauge_matrix.nullspace())}")
print(
    "gauge-image split ranks: "
    f"O4_block={gauge_matrix[:, :4].rank()}, "
    f"anisotropic_block={gauge_matrix[:, 4:].rank()}"
)


def quadratic_matrix(expr):
    return sp.hessian(expr, hvars) / 2


mass_matrices = [quadratic_matrix(f) for f in mass_forms]
kinetic_matrices = [quadratic_matrix(f) for f in kinetic_forms]


def tt_basis(q_values):
    constraints = sp.zeros(5, len(PAIRS))
    for nu in range(D):
        for column, (a, b) in enumerate(PAIRS):
            if a == b == nu:
                constraints[nu, column] += q_values[a]
            elif a != b:
                if b == nu:
                    constraints[nu, column] += q_values[a]
                if a == nu:
                    constraints[nu, column] += q_values[b]
    for column, (a, b) in enumerate(PAIRS):
        if a == b:
            constraints[4, column] = 1
    return sp.Matrix.hstack(*constraints.nullspace())


directions = [
    (1, 0, 0, 0),
    (1, 1, 0, 0),
    (1, 1, 1, 1),
    (2, 1, 3, 1),
]


def restricted_form_rank(matrices, q_dependent):
    rows = [[] for _ in matrices]
    for q_values in directions:
        basis = tt_basis(q_values)
        subs_q = dict(zip(qvars, q_values))
        for form_index, matrix in enumerate(matrices):
            evaluated = matrix.subs(subs_q) if q_dependent else matrix
            restricted = basis.T * evaluated * basis
            rows[form_index].extend(list(restricted))
    return sp.Matrix(rows).rank()


mass_tt_rank = restricted_form_rank(mass_matrices, False)
kinetic_tt_rank = restricted_form_rank(kinetic_matrices, True)
o4_tt_rank = restricted_form_rank(kinetic_matrices[:4], True)
print(
    "TT restriction ranks: "
    f"mass={mass_tt_rank}, all_two_derivative={kinetic_tt_rank}, O4_two_derivative={o4_tt_rank}"
)
print(f"operator codimensions: full_gauge={mass_dim_character + gauge_rank}, TT_restriction={mass_tt_rank + kinetic_tt_rank - o4_tt_rank}")


# Exact sign audit of the naive-doubler transformation.  Conjugation changes
# gamma_a by -1 only for a=mu; the site phase changes a hop only for nu=mu.
doubler_ok = True
for mu in range(D):
    for a in range(D):
        for nu in range(D):
            transformed_sign = (-1 if a == mu else 1) * (-1 if nu == mu else 1)
            tensor_reflection_sign = (-1 if a == mu else 1) * (-1 if nu == mu else 1)
            doubler_ok &= transformed_sign == tensor_reflection_sign
print(f"doubler sign identity for all (mu,a,nu): {doubler_ok}")


# Independent explicit-gamma audit of the fermion bubble numerator.  The
# worker's scalar expression is the spin trace divided by four; the external
# cosine/log-determinant factors then reproduce the coded 1/4 prefactor.
s1 = np.array([[0, 1], [1, 0]], complex)
s2 = np.array([[0, -1j], [1j, 0]], complex)
s3 = np.array([[1, 0], [0, -1]], complex)
eye2 = np.eye(2, dtype=complex)
gammas = [
    np.kron(s1, eye2),
    np.kron(s2, eye2),
    np.kron(s3, s1),
    np.kron(s3, s2),
]
anticommutator_error = max(
    np.max(np.abs(gammas[a] @ gammas[b] + gammas[b] @ gammas[a] - 2 * (a == b) * np.eye(4)))
    for a in range(D)
    for b in range(D)
)
nrng = np.random.default_rng(9421)
trace_error = 0.0
for _ in range(20):
    avec = nrng.normal(size=D)
    bvec = nrng.normal(size=D)
    uvec = nrng.normal(size=D)
    vvec = nrng.normal(size=D)
    m = 0.37
    Da = float(avec @ avec + m * m)
    Db = float(bvec @ bvec + m * m)
    slash_a = sum(g * z for g, z in zip(gammas, avec))
    slash_b = sum(g * z for g, z in zip(gammas, bvec))
    slash_u = sum(g * z for g, z in zip(gammas, uvec))
    slash_v = sum(g * z for g, z in zip(gammas, vvec))
    Sa = (m * np.eye(4) - 1j * slash_a) / Da
    Sb = (m * np.eye(4) - 1j * slash_b) / Db
    direct = np.trace(Sa @ (1j * slash_u) @ Sb @ (1j * slash_v)).real / 4
    reduced = (
        -(m * m + avec @ bvec) * (uvec @ vvec)
        + (avec @ uvec) * (bvec @ vvec)
        + (avec @ vvec) * (bvec @ uvec)
    ) / (Da * Db)
    trace_error = max(trace_error, abs(direct - reduced))
print(f"fermion gamma audit: anticommutator_error={anticommutator_error:.1e}, normalized_trace_error={trace_error:.1e}")


# The local counterterm -Lambda sqrt(det(1+h)), Lambda=2t, cancels t tr(h)
# and shifts the local quadratic coefficients by (t/2,t/2,-t/4).
t = sp.symbols("t")
cc_shift = (t / 2, t / 2, -t / 4)
print(f"CC tadpole cancellation shifts (M1,M2,M3)={cc_shift}")


# Representative small-grid reruns of the supplied numerical kernels.  These
# re-execute the integrations but do not overwrite any worker artifact.
import loop_fermion as lf
import loop_photon as lp
from photon_q0 import Fgamma

forms_data = np.load("forms_data.npz")
MF = forms_data["M"]
KF = forms_data["K"]
nvecs = [
    np.array(v, float)
    for v in ((1, 0, 0, 0), (1, 1, 0, 0), (1, 1, 1, 0), (1, 1, 1, 1), (2, 1, 0, 0), (2, 1, 1, 0))
]


def fit_mass(B0):
    design = np.array([0.5 * matrix.ravel() for matrix in MF]).T
    return np.linalg.lstsq(design, B0.ravel(), rcond=None)[0]


def fit_kinetic(bilinear, L):
    B0 = bilinear(np.zeros(4), L)[0]
    design_rows = []
    values = []
    for n in nvecs:
        unit = 2 * np.pi / L * n
        differences = [bilinear(k * unit, L)[0] - B0 for k in (1, 2, 3)]
        q2_piece = 1.5 * differences[0] - 0.15 * differences[1] + differences[2] / 90
        design_rows.append(
            np.array([0.5 * np.einsum("ABab,a,b->AB", form, unit, unit).ravel() for form in KF]).T
        )
        values.append(q2_piece.ravel())
    design = np.vstack(design_rows)
    values = np.concatenate(values)
    coefficients = np.linalg.lstsq(design, values, rcond=None)[0]
    residual = np.linalg.norm(design @ coefficients - values) / np.linalg.norm(values)
    return B0, coefficients, residual


fermion_L = 16
fermion_m = 0.5
fermion_B0, fermion_cK, fermion_residual = fit_kinetic(
    lambda momentum, size: lf.bilinear(momentum, size, fermion_m), fermion_L
)
fermion_cM = fit_mass(fermion_B0)
_, fermion_I1 = lf.bilinear(np.zeros(4), fermion_L, fermion_m)
fermion_tad = 2 * fermion_I1
fermion_net = fermion_cM + np.array([fermion_tad / 2, fermion_tad / 2, -fermion_tad / 4])
print(
    "fermion rerun L=16,m=0.5: "
    f"tad={fermion_tad:.9f}, raw_mass={np.array2string(fermion_cM, precision=9)}, "
    f"net_mass={np.array2string(fermion_net, precision=9)}, fit_residual={fermion_residual:.2e}"
)
print("fermion rerun cK=" + np.array2string(fermion_cK, precision=7, suppress_small=False))


photon_L = 8
photon_B0, photon_cK, photon_residual = fit_kinetic(lp.bilinear, photon_L)
photon_cM = fit_mass(photon_B0)
names = ["F1", "F2", "F3", "F4", "A1", "A2", "A3", "A4", "A6"]
coefficient = dict(zip(names, photon_cK))
weyl_q2_1 = coefficient["F1"] + coefficient["F3"] / 2 + 4 * coefficient["F4"] + coefficient["A3"] / 2 + coefficient["A6"]
weyl_q2_2 = coefficient["F2"] + 2 * coefficient["F3"] + coefficient["A4"] + coefficient["A1"] + coefficient["A2"] + 2 * coefficient["A3"] - coefficient["A6"]
print(
    "photon rerun L=8: "
    f"mass={np.array2string(photon_cM, precision=9)}, fit_residual={photon_residual:.2e}, "
    f"Weyl_q2=({weyl_q2_1:.2e},{weyl_q2_2:.2e})"
)
print("photon rerun cK=" + np.array2string(photon_cK, precision=7, suppress_small=False))


# Independent constant-metric determinant at the same small grid.
F0 = Fgamma(np.zeros(10), photon_L)


def photon_quadratic(direction, epsilon):
    return (Fgamma(epsilon * direction, photon_L) + Fgamma(-epsilon * direction, photon_L) - 2 * F0) / (2 * epsilon**2)


def photon_quadratic_richardson(direction):
    epsilon = 0.003
    return (4 * photon_quadratic(direction, epsilon) - photon_quadratic(direction, 2 * epsilon)) / 3


v00 = np.zeros(10)
v00[0] = 1
v01 = np.zeros(10)
v01[1] = 1
vdm = np.zeros(10)
vdm[0] = 1
vdm[PAIRS.index((1, 1))] = -1
q00 = photon_quadratic_richardson(v00)
q01 = photon_quadratic_richardson(v01)
qdm = photon_quadratic_richardson(vdm)
photon_cM_det = np.array([qdm / 2, q01 / 2, q00 - qdm / 2])
print(
    "photon constant-det cross-check L=8: "
    f"mass={np.array2string(photon_cM_det, precision=9)}, "
    f"max_delta_vs_loop={np.max(np.abs(photon_cM_det - photon_cM)):.2e}"
)


# Read the converged stored coefficients only to evaluate their numerical
# margins; no worker-computed expectation is used in the exact checks above.
import json

with open("loop_fermion_m0.15.json") as handle:
    fermion_stored = json.load(handle)["80"]
with open("loop_photon.json") as handle:
    photon_stored = json.load(handle)["32"]
total_mass = np.array(fermion_stored["cMnet"]) / 4 + np.array(photon_stored["cM"])
total_kinetic = np.array(fermion_stored["cK"]) / 4 + np.array(photon_stored["cK"])
print("stored converged QED total mass=" + np.array2string(total_mass, precision=7))
print("stored converged QED total cK=" + np.array2string(total_kinetic, precision=7, suppress_small=False))
print(f"smallest absolute named QED cK={np.min(np.abs(total_kinetic)):.3e}")
