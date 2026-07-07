"""Presentation-gauge localization runner.

Sections:
A - presentation-gauge group and cubic relation
B - gauge invariants are the all-even-exponent functions
C - gauge-definable sets are automatically achiral
D - residual bit as the orientation bit, including antilinear Clifford maps

Expected close: TOTAL: PASS=15 FAIL=0
"""

import itertools

import numpy as np


rng = np.random.default_rng(3)
PASS = 0
FAIL = 0


def check(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    suffix = f" :: {detail}" if detail else ""
    print(f"{status} {name}{suffix}")


def mat_key(mat):
    return tuple(int(round(x)) for x in np.asarray(mat).reshape(-1))


def det_sign(mat):
    return int(round(np.linalg.det(np.asarray(mat, dtype=float))))


def generated_signed_permutation_matrices():
    out = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((1, -1), repeat=3):
            mat = np.zeros((3, 3), dtype=int)
            for row, col in enumerate(perm):
                mat[row, col] = signs[row]
            out.append(mat)
    uniq = {}
    for mat in out:
        uniq[mat_key(mat)] = mat
    return list(uniq.values())


def generated_gauge_matrices():
    return [np.diag(signs).astype(int) for signs in itertools.product((1, -1), repeat=3)]


def monomial_value(exp, point):
    val = 1.0
    for power, coord in zip(exp, point):
        val *= coord ** power
    return float(val)


def all_even(exp):
    return all(power % 2 == 0 for power in exp)


def monomials_total_degree(max_degree):
    return [
        exp
        for exp in itertools.product(range(max_degree + 1), repeat=3)
        if sum(exp) <= max_degree
    ]


def poly_value(coeffs, exps, point):
    return float(sum(c * monomial_value(e, point) for c, e in zip(coeffs, exps)))


def psi9(point):
    x, y, z = point
    return float(x * y * z * (x * x - y * y) * (y * y - z * z) * (z * z - x * x))


def unique_points(points, tol=1e-9):
    uniq = []
    for point in points:
        if not any(np.linalg.norm(point - old) <= tol for old in uniq):
            uniq.append(point)
    return np.array(uniq, dtype=float)


def orbit(point):
    return unique_points([mat @ point for mat in proper])


def transform_monomial(exp, mat):
    sign = 1
    out = [0, 0, 0]
    for row, power in enumerate(exp):
        col = int(np.flatnonzero(mat[row])[0])
        entry = int(mat[row, col])
        if power % 2:
            sign *= entry
        out[col] += power
    return sign, tuple(out)


def det_projection_matrix(max_degree):
    exps = monomials_total_degree(max_degree)
    idx = {exp: i for i, exp in enumerate(exps)}
    proj = np.zeros((len(exps), len(exps)))
    for col, exp in enumerate(exps):
        for mat in mats:
            sign, new_exp = transform_monomial(exp, mat)
            row = idx[new_exp]
            proj[row, col] += det_sign(mat) * sign / len(mats)
    return proj


def poly_add(left, right, scale_right=1):
    out = dict(left)
    for exp, coeff in right.items():
        out[exp] = out.get(exp, 0) + scale_right * coeff
        if out[exp] == 0:
            del out[exp]
    return out


def poly_mul(left, right):
    out = {}
    for exp_a, coeff_a in left.items():
        for exp_b, coeff_b in right.items():
            exp = tuple(exp_a[i] + exp_b[i] for i in range(3))
            out[exp] = out.get(exp, 0) + coeff_a * coeff_b
    return {exp: coeff for exp, coeff in out.items() if coeff != 0}


def var_poly(axis, power=1):
    exp = [0, 0, 0]
    exp[axis] = power
    return {tuple(exp): 1}


def psi9_poly():
    x = var_poly(0)
    y = var_poly(1)
    z = var_poly(2)
    x2 = var_poly(0, 2)
    y2 = var_poly(1, 2)
    z2 = var_poly(2, 2)
    poly = poly_mul(poly_mul(x, y), z)
    poly = poly_mul(poly, poly_add(x2, y2, scale_right=-1))
    poly = poly_mul(poly, poly_add(y2, z2, scale_right=-1))
    poly = poly_mul(poly, poly_add(z2, x2, scale_right=-1))
    return poly


def second_derivative(poly, axis):
    out = {}
    for exp, coeff in poly.items():
        if exp[axis] >= 2:
            new_exp = list(exp)
            factor = new_exp[axis] * (new_exp[axis] - 1)
            new_exp[axis] -= 2
            out[tuple(new_exp)] = out.get(tuple(new_exp), 0) + coeff * factor
    return {exp: coeff for exp, coeff in out.items() if coeff != 0}


def laplacian(poly):
    out = {}
    for axis in range(3):
        out = poly_add(out, second_derivative(poly, axis))
    return out


def sign_nonzero(value, tol=1e-12):
    if abs(value) <= tol:
        return 0
    return 1 if value > 0 else -1


def projection_check(max_degree):
    exps = monomials_total_degree(max_degree)
    coeffs = rng.normal(size=len(exps))
    errors = []
    for _ in range(20):
        point = rng.normal(size=3)
        projected = sum(poly_value(coeffs, exps, mat @ point) for mat in gauge) / len(gauge)
        truncated = sum(
            coeff * monomial_value(exp, point)
            for coeff, exp in zip(coeffs, exps)
            if all_even(exp)
        )
        errors.append(abs(projected - truncated))
    kept = sum(1 for exp in exps if all_even(exp))
    return max(errors), len(exps), kept


def all_even_function(point):
    return poly_value(all_even_coeffs, all_even_exps, point)


mats = generated_signed_permutation_matrices()
gauge = generated_gauge_matrices()
proper = [mat for mat in mats if det_sign(mat) == 1]
improper = [mat for mat in mats if det_sign(mat) == -1]

id3 = np.eye(3, dtype=int)
gauge_keys = {mat_key(mat) for mat in gauge}
proper_keys = {mat_key(mat) for mat in proper}
all_keys = {mat_key(mat) for mat in mats}
even_gauge = [mat for mat in gauge if det_sign(mat) == 1]
odd_gauge = [mat for mat in gauge if det_sign(mat) == -1]
even_gauge_keys = {mat_key(mat) for mat in even_gauge}
odd_gauge_keys = {mat_key(mat) for mat in odd_gauge}
generic = np.array([0.41, 1.37, 2.23])


gauge_closed = all(mat_key(a @ b) in gauge_keys for a in gauge for b in gauge)
gauge_involutions = all(np.array_equal(a @ a, id3) for a in gauge)
gauge_abelian = all(np.array_equal(a @ b, b @ a) for a in gauge for b in gauge)
diag_sign_patterns = {tuple(int(x) for x in np.diag(mat)) for mat in gauge}
check(
    "A1 gauge group is Z2^3",
    len(gauge_keys) == 8
    and gauge_closed
    and gauge_involutions
    and gauge_abelian
    and len(diag_sign_patterns) == 8,
    f"order={len(gauge_keys)} closed={gauge_closed} involutions={gauge_involutions}",
)

all_minus = [mat for mat in gauge if np.array_equal(mat, -id3)]
even_subset_proper = even_gauge_keys <= proper_keys
odd_outside_proper = odd_gauge_keys.isdisjoint(proper_keys)
even_closed = all(mat_key(a @ b) in even_gauge_keys for a in even_gauge for b in even_gauge)
check(
    "A2 gauge determinant split",
    len(even_gauge) == 4
    and len(odd_gauge) == 4
    and even_subset_proper
    and odd_outside_proper
    and even_closed
    and len(all_minus) == 1
    and det_sign(all_minus[0]) == -1,
    (
        f"det+={len(even_gauge)} det-={len(odd_gauge)} "
        f"all_minus_det={det_sign(all_minus[0]) if all_minus else 'none'}"
    ),
)

products = {mat_key(rot @ flip) for rot in proper for flip in gauge}
intersection_size = len(proper_keys & gauge_keys)
check(
    "A3 cubic group generated by proper rotations and gauge",
    products == all_keys and intersection_size == 4 and len(products) == 48,
    f"products={len(products)} cubic={len(all_keys)} intersection={intersection_size}",
)


monomial_mismatches = []
for exp in itertools.product(range(6), repeat=3):
    base = monomial_value(exp, generic)
    invariant = all(
        abs(monomial_value(exp, flip @ generic) - base) <= 1e-9 for flip in gauge
    )
    parity = all_even(exp)
    if invariant != parity:
        monomial_mismatches.append((exp, invariant, parity))
check(
    "B1 gauge invariants match all-even monomials",
    not monomial_mismatches,
    f"scanned=216 mismatches={len(monomial_mismatches)}",
)

err2, count2, kept2 = projection_check(2)
check(
    "B2 all-even projection degree 2",
    err2 < 1e-9,
    f"monomials={count2} kept={kept2} max_error={err2:.3e}",
)

err3, count3, kept3 = projection_check(3)
check(
    "B2 all-even projection degree 3",
    err3 < 1e-9,
    f"monomials={count3} kept={kept3} max_error={err3:.3e}",
)

proj8 = det_projection_matrix(8)
proj9 = det_projection_matrix(9)
rank8 = int(np.linalg.matrix_rank(proj8, tol=1e-10))
rank9 = int(np.linalg.matrix_rank(proj9, tol=1e-10))
check(
    "B3 det character first appears at degree 9",
    rank8 == 0 and rank9 > 0,
    f"rank_le_8={rank8} rank_le_9={rank9} max_le_8={np.max(np.abs(proj8)):.3e}",
)

single_axis_flips = [
    mat for mat in odd_gauge if np.count_nonzero(np.diag(mat) == -1) == 1
]
single_flip = single_axis_flips[0]
psi_poly = psi9_poly()
psi_terms_odd = all(sum(exp) == 9 and all(power % 2 == 1 for power in exp) for exp in psi_poly)
psi_harmonic = laplacian(psi_poly) == {}
psi_det_covariant = all(
    abs(psi9(mat @ generic) - det_sign(mat) * psi9(generic)) <= 1e-9 for mat in mats
)
psi_not_gauge_invariant = psi9(single_flip @ generic) == -psi9(generic)
check(
    "B3 Psi9 gauge-odd cubic harmonic",
    psi_terms_odd and psi_harmonic and psi_det_covariant and psi_not_gauge_invariant,
    (
        f"terms={len(psi_poly)} harmonic={psi_harmonic} "
        f"single_flip_delta={psi9(single_flip @ generic) + psi9(generic):.3e}"
    ),
)


all_even_exps = [exp for exp in monomials_total_degree(6) if all_even(exp)]
all_even_coeffs = rng.normal(size=len(all_even_exps))
inversion_errors = []
for _ in range(20):
    point = rng.normal(size=3)
    inversion_errors.append(abs(all_even_function(point) - all_even_function(-point)))
check(
    "C1 gauge-invariant functions are inversion-even",
    max(inversion_errors) < 1e-9,
    f"points=20 max_error={max(inversion_errors):.3e}",
)

# C2: independent of any single coefficient draw or base point, no all-even
# (flip-invariant) function separates a generic orbit from its twin. Scan
# several independently seeded all-even functions over several generic base
# points; the multisets must coincide for every one. (Discrimination that
# the coincidence test CAN fail is provided by C3: the flip-odd Psi9 DOES
# separate the same orbit from its twin.)
c2_seeds = list(range(11, 19))
c2_bases = [generic, np.array([0.29, 1.11, 2.57]), np.array([0.7, 1.9, 0.13])]
c2_multiset_err = 0.0
c2_orbit_sizes = set()
for seed in c2_seeds:
    coeffs = np.random.default_rng(seed).normal(size=len(all_even_exps))
    f_even = lambda p, c=coeffs: poly_value(c, all_even_exps, p)
    for base in c2_bases:
        orb = orbit(base)
        twin = orbit(-base)
        c2_orbit_sizes.add(len(orb))
        c2_orbit_sizes.add(len(twin))
        ov = np.sort(np.array([f_even(p) for p in orb]))
        tv = np.sort(np.array([f_even(p) for p in twin]))
        c2_multiset_err = max(c2_multiset_err, float(np.max(np.abs(ov - tv))))
check(
    "C2 no all-even function separates a generic orbit from its twin",
    c2_orbit_sizes == {24} and c2_multiset_err < 1e-9,
    f"functions={len(c2_seeds)} bases={len(c2_bases)} orbit_sizes={sorted(c2_orbit_sizes)} "
    f"max_multiset_err={c2_multiset_err:.3e}",
)

psi_orb_sum = float(sum(psi9(point) for point in orb))
psi_twin_sum = float(sum(psi9(point) for point in twin))
psi_single_flip = psi9(single_flip @ generic)
check(
    "C3 Psi9 separates twins and is gauge-odd",
    abs(psi_orb_sum) > 1e-9
    and abs(psi_twin_sum) > 1e-9
    and abs(psi_orb_sum + psi_twin_sum) < 1e-9
    and psi_single_flip == -psi9(generic),
    f"sum_orbit={psi_orb_sum:.12g} sum_twin={psi_twin_sum:.12g}",
)


odd_rep = odd_gauge[0]
odd_coset = {mat_key(odd_rep @ mat) for mat in even_gauge}
det_detects_even = all(det_sign(mat) == 1 for mat in even_gauge)
det_detects_odd = all(det_sign(mat) == -1 for mat in odd_gauge)
check(
    "D1 gauge quotient has one determinant bit",
    even_closed
    and odd_coset == odd_gauge_keys
    and even_gauge_keys.isdisjoint(odd_gauge_keys)
    and det_detects_even
    and det_detects_odd,
    f"even_subgroup={len(even_gauge)} odd_coset={len(odd_coset)} quotient=2",
)

transport_points = [generic] + [rng.normal(size=3) for _ in range(20)]
transport_ok = True
transport_cases = 0
control_cases = 0
control_ok = True
for point in transport_points:
    if sign_nonzero(psi9(point)) == 0:
        transport_ok = False
    for choice in gauge:
        before_gauge = det_sign(choice)
        before_orient = sign_nonzero(psi9(choice @ point))
        before_product = before_gauge * before_orient
        for flip in odd_gauge:
            after = flip @ choice
            after_gauge = det_sign(after)
            after_orient = sign_nonzero(psi9(after @ point))
            transport_cases += 1
            # odd flip flips BOTH bits; their product is invariant (the lock)
            if after_gauge != -before_gauge:
                transport_ok = False
            if after_orient != -before_orient:
                transport_ok = False
            if after_gauge * after_orient != before_product:
                transport_ok = False
        # negative control: an EVEN flip moves NEITHER bit -- proving the lock
        # detects the odd/even parity, not passing vacuously
        for flip in even_gauge:
            after = flip @ choice
            control_cases += 1
            if det_sign(after) != before_gauge:
                control_ok = False
            if sign_nonzero(psi9(after @ point)) != before_orient:
                control_ok = False
check(
    "D2 transport locks the gauge det-bit to sign(Psi9)",
    transport_ok and control_ok,
    f"points={len(transport_points)} odd_flip_cases={transport_cases} "
    f"even_flip_control_cases={control_cases}",
)


sigma1 = np.array([[0, 1], [1, 0]], dtype=complex)
sigma2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
sigma3 = np.array([[1, 0], [0, -1]], dtype=complex)
sigmas = [sigma1, sigma2, sigma3]
id2 = np.eye(2, dtype=complex)
clifford_labels = [(), (0,), (1,), (2,), (0, 1), (0, 2), (1, 2), (0, 1, 2)]


def clifford_basis_matrix(label):
    mat = id2.copy()
    for axis in label:
        mat = mat @ sigmas[axis]
    return mat


clifford_basis = [clifford_basis_matrix(label) for label in clifford_labels]
clifford_vecs = np.column_stack(
    [np.concatenate((mat.reshape(-1).real, mat.reshape(-1).imag)) for mat in clifford_basis]
)
omega = sigma1 @ sigma2 @ sigma3


def clifford_from_coeffs(coeffs):
    out = np.zeros((2, 2), dtype=complex)
    for coeff, basis_mat in zip(coeffs, clifford_basis):
        out = out + coeff * basis_mat
    return out


def clifford_coeffs(mat):
    vec = np.concatenate((mat.reshape(-1).real, mat.reshape(-1).imag))
    return np.linalg.solve(clifford_vecs, vec)


def clifford_phi(mat, signs):
    coeffs = clifford_coeffs(mat)
    out = np.zeros((2, 2), dtype=complex)
    for coeff, label, basis_mat in zip(coeffs, clifford_labels, clifford_basis):
        factor = 1
        for axis in label:
            factor *= signs[axis]
        out = out + coeff * factor * basis_mat
    return out


def clifford_errors(signs):
    a = clifford_from_coeffs(rng.normal(size=8))
    b = clifford_from_coeffs(rng.normal(size=8))
    phi_a = clifford_phi(a, signs)
    auto_error = np.max(np.abs(clifford_phi(a @ b, signs) - phi_a @ clifford_phi(b, signs)))
    anti_error = np.max(np.abs(clifford_phi(1j * a, signs) + 1j * phi_a))
    omega_error = np.max(np.abs(clifford_phi(omega, signs) + omega))
    gen_error = max(
        np.max(np.abs(clifford_phi(sigmas[axis], signs) - signs[axis] * sigmas[axis]))
        for axis in range(3)
    )
    return max(auto_error, anti_error, omega_error, gen_error)


single_signs = tuple(int(x) for x in np.diag(single_flip))
single_clifford_error = clifford_errors(single_signs)
check(
    "D3 single-axis antilinear Clifford map",
    np.allclose(omega, 1j * id2) and single_clifford_error < 1e-9,
    f"signs={single_signs} max_error={single_clifford_error:.3e}",
)

odd_clifford_errors = [
    clifford_errors(tuple(int(x) for x in np.diag(mat))) for mat in odd_gauge
]
check(
    "D3 odd gauge antilinear Clifford maps",
    max(odd_clifford_errors) < 1e-9,
    f"odd_checked={len(odd_clifford_errors)} max_error={max(odd_clifford_errors):.3e}",
)

print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
