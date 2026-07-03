#!/usr/bin/env python3
"""Native record-time/spatial split of the theta carrier.

Sections:
  A. Native carrier split with record-time as direction 0.
  B. Exact transformation law from cell pullbacks and flux matrices.
  C. Orientation non-supply of the named cubic structure.
  D. Cl(3,0) bridge: improper cubic maps are complex-antilinear.
  E. Seed direction, exclusion mechanism, and imported orientation.

Expected close: TOTAL: PASS=20 FAIL=0
"""

import itertools

import numpy as np


PASS = 0
FAIL = 0
RNG = np.random.default_rng(11)

DIM4 = 4
N4 = 4
PLANES4 = tuple(itertools.combinations(range(DIM4), 2))
PLANE_INDEX = {p: i for i, p in enumerate(PLANES4)}
SPATIAL = (1, 2, 3)


def check(name, cond, detail=""):
    global PASS, FAIL
    ok = bool(cond)
    if ok:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    print(f"  [{status}] {name}")
    if detail:
        print(f"         {detail}")


def permutation_sign(items):
    inv = 0
    for i in range(len(items)):
        for j in range(i + 1, len(items)):
            if items[i] > items[j]:
                inv += 1
    return 1 if inv % 2 == 0 else -1


def matrix_from_flux_values(values):
    m = np.zeros((DIM4, DIM4), dtype=np.int64)
    for pair, value in zip(PLANES4, values):
        mu, nu = pair
        v = int(value)
        m[mu, nu] = v
        m[nu, mu] = -v
    return m


def flux_values_from_matrix(m):
    return np.array([int(m[mu, nu]) for mu, nu in PLANES4], dtype=np.int64)


def q_reference(m):
    return int(m[0, 1] * m[2, 3] - m[0, 2] * m[1, 3] + m[0, 3] * m[1, 2])


def epsilon_from_frame(frame, a, b, c):
    if len({a, b, c}) != 3:
        return 0
    if set((a, b, c)) != set(frame):
        return 0
    positions = [frame.index(v) for v in (a, b, c)]
    return permutation_sign(positions)


def b_from_frame(frame, m):
    out = []
    for i in SPATIAL:
        total = 0
        for j in SPATIAL:
            for k in SPATIAL:
                total += epsilon_from_frame(frame, i, j, k) * int(m[j, k])
        if total % 2 != 0:
            raise ValueError("antisymmetric flux contraction was not even")
        out.append(total // 2)
    return np.array(out, dtype=np.int64)


def split_e_b(m):
    e = np.array([int(m[0, i]) for i in SPATIAL], dtype=np.int64)
    b = b_from_frame((1, 2, 3), m)
    return e, b


def transform_flux(m, lmat):
    return (lmat @ m @ lmat.T).astype(np.int64)


def signed_permutation_group(n):
    out = []
    for perm in itertools.permutations(range(n)):
        for signs in itertools.product((-1, 1), repeat=n):
            mat = np.zeros((n, n), dtype=np.int64)
            for row, col in enumerate(perm):
                mat[row, col] = signs[row]
            out.append(mat)
    return out


def det_int(mat):
    return int(round(float(np.linalg.det(mat))))


def embed_spatial(smat):
    lmat = np.zeros((DIM4, DIM4), dtype=np.int64)
    lmat[0, 0] = 1
    lmat[1:, 1:] = smat
    return lmat


GROUP3 = signed_permutation_group(3)


def sites(n, dim):
    return [tuple(int(v) for v in x) for x in np.ndindex(*(n,) * dim)]


def cells(n, dim, k):
    out = []
    all_sites = sites(n, dim)
    for axes in itertools.combinations(range(dim), k):
        for x in all_sites:
            out.append((x, axes))
    return out


CELL_DATA = {}
for _k in range(DIM4 + 1):
    _cells = cells(N4, DIM4, _k)
    CELL_DATA[_k] = (_cells, {cell: i for i, cell in enumerate(_cells)})


def shift_site(x, axis, n):
    y = list(x)
    y[axis] = (y[axis] + 1) % n
    return tuple(y)


def flux_cochain(m):
    c2, i2 = CELL_DATA[2]
    out = np.zeros(len(c2), dtype=np.int64)
    for (mu, nu) in PLANES4:
        value = int(m[mu, nu])
        for (x, axes), idx in i2.items():
            if axes == (mu, nu) and x[mu] == 0 and x[nu] == 0:
                out[idx] = value
    return out


def cup_sum_2_2(a, b):
    c4, i4 = CELL_DATA[4]
    c2, i2 = CELL_DATA[2]
    total = 0
    for (x, axes), _idx in i4.items():
        cell_total = 0
        for left_axes in itertools.combinations(axes, 2):
            right_axes = tuple(ax for ax in axes if ax not in left_axes)
            sign = permutation_sign(list(left_axes) + list(right_axes))
            y = x
            for ax in left_axes:
                y = shift_site(y, ax, N4)
            cell_total += sign * int(a[i2[(x, left_axes)]]) * int(b[i2[(y, right_axes)]])
        total += cell_total
    return int(total)


def shuffle_cup_factor():
    axes = tuple(range(DIM4))
    first = (0, 1)
    second = tuple(ax for ax in axes if ax not in first)
    total = 0
    for left_axes in itertools.combinations(axes, 2):
        right_axes = tuple(ax for ax in axes if ax not in left_axes)
        if (left_axes == first and right_axes == second) or (left_axes == second and right_axes == first):
            total += permutation_sign(list(left_axes) + list(right_axes))
    return int(total)


def unit_complementary_fluxes():
    configs = []
    for pair in PLANES4:
        comp = tuple(ax for ax in range(DIM4) if ax not in pair)
        comp = tuple(sorted(comp))
        vals = np.zeros(len(PLANES4), dtype=np.int64)
        vals[PLANE_INDEX[pair]] = 1
        vals[PLANE_INDEX[comp]] = 1
        configs.append(vals)
    return configs


def map_cell_for_pullback(x, axes, lmat, n):
    x_vec = np.array(x, dtype=np.int64)
    base = [int(v) % n for v in (lmat @ x_vec)]
    image_axes = []
    orient = 1
    for axis in axes:
        row = lmat[axis, :]
        nz = np.flatnonzero(row)
        if len(nz) != 1:
            raise ValueError("not a signed-permutation matrix")
        image_axis = int(nz[0])
        sign = int(row[image_axis])
        image_axes.append(image_axis)
        orient *= sign
        if sign < 0:
            base[image_axis] = (base[image_axis] - 1) % n
    orient *= permutation_sign(image_axes)
    return tuple(base), tuple(sorted(image_axes)), int(orient)


def pullback_2_cochain(cochain, lmat):
    c2, i2 = CELL_DATA[2]
    out = np.zeros_like(cochain)
    for (x, axes), idx in i2.items():
        image_cell = map_cell_for_pullback(x, axes, lmat, N4)
        y, image_axes, orient = image_cell
        out[idx] = orient * cochain[i2[(y, image_axes)]]
    return out


def sheet_count_for_corner_rep():
    unit = np.zeros((DIM4, DIM4), dtype=np.int64)
    unit[0, 1] = 1
    unit[1, 0] = -1
    c2, i2 = CELL_DATA[2]
    rep = flux_cochain(unit)
    return int(sum(int(rep[idx]) for (x, axes), idx in i2.items() if axes == (0, 1)))


SHEET_COUNT = sheet_count_for_corner_rep()


def extract_flux_matrix_from_totals(cochain):
    c2, i2 = CELL_DATA[2]
    out = np.zeros((DIM4, DIM4), dtype=np.int64)
    divisible = True
    for mu, nu in PLANES4:
        total = sum(int(cochain[idx]) for (x, axes), idx in i2.items() if axes == (mu, nu))
        if total % SHEET_COUNT != 0:
            divisible = False
        value = total // SHEET_COUNT
        out[mu, nu] = value
        out[nu, mu] = -value
    return out, divisible


def polynomial_cross_coefficients():
    coeffs = {}
    zero = np.zeros(len(PLANES4), dtype=np.int64)
    q0 = q_reference(matrix_from_flux_values(zero))
    for i, j in itertools.combinations(range(len(PLANES4)), 2):
        vi = np.zeros(len(PLANES4), dtype=np.int64)
        vj = np.zeros(len(PLANES4), dtype=np.int64)
        vij = np.zeros(len(PLANES4), dtype=np.int64)
        vi[i] = 1
        vj[j] = 1
        vij[i] = 1
        vij[j] = 1
        coeffs[(i, j)] = (
            q_reference(matrix_from_flux_values(vij))
            - q_reference(matrix_from_flux_values(vi))
            - q_reference(matrix_from_flux_values(vj))
            + q0
        )
    return coeffs


def complex_matrix():
    return RNG.normal(size=(2, 2)) + 1j * RNG.normal(size=(2, 2))


SIGMA1 = np.array([[0, 1], [1, 0]], dtype=np.complex128)
SIGMA2 = np.array([[0, -1j], [1j, 0]], dtype=np.complex128)
SIGMA3 = np.array([[1, 0], [0, -1]], dtype=np.complex128)
SIGMAS = (SIGMA1, SIGMA2, SIGMA3)
I2 = np.eye(2, dtype=np.complex128)
WORDS = ((), (0,), (1,), (2,), (0, 1), (0, 2), (1, 2), (0, 1, 2))


def word_matrix(word, generators):
    out = I2.copy()
    for idx in word:
        out = out @ generators[idx]
    return out


BASIS_MATS = [word_matrix(word, SIGMAS) for word in WORDS]


def flatten_real(mat):
    return np.concatenate((mat.real.reshape(-1), mat.imag.reshape(-1)))


BASIS_SOLVER = np.linalg.inv(np.column_stack([flatten_real(mat) for mat in BASIS_MATS]))


def decompose_real(mat):
    return BASIS_SOLVER @ flatten_real(mat)


def make_clifford_map(smat):
    gen_images = []
    for source in range(3):
        image = np.zeros((2, 2), dtype=np.complex128)
        for target in range(3):
            image += int(smat[target, source]) * SIGMAS[target]
        gen_images.append(image)
    image_basis = [word_matrix(word, gen_images) for word in WORDS]

    def phi(mat):
        coeffs = decompose_real(mat)
        out = np.zeros((2, 2), dtype=np.complex128)
        for coeff, image in zip(coeffs, image_basis):
            out += coeff * image
        return out

    return phi


def close_mat(a, b, tol=1e-10):
    return bool(np.allclose(a, b, atol=tol, rtol=0.0))


def automorphism_samples_ok(phi, count):
    for _ in range(count):
        x = complex_matrix()
        y = complex_matrix()
        if not close_mat(phi(x @ y), phi(x) @ phi(y)):
            return False
    return True


def measured_complex_verdict(phi, count):
    linear = True
    antilinear = True
    for _ in range(count):
        x = complex_matrix()
        linear = linear and close_mat(phi(1j * x), 1j * phi(x))
        antilinear = antilinear and close_mat(phi(1j * x), -1j * phi(x))
    if linear and not antilinear:
        return 1
    if antilinear and not linear:
        return -1
    return 0


def sample_su3():
    z = RNG.normal(size=(3, 3)) + 1j * RNG.normal(size=(3, 3))
    q, r = np.linalg.qr(z)
    diag = np.diag(r)
    phases = np.ones(3, dtype=np.complex128)
    mask = np.abs(diag) > 0
    phases[mask] = diag[mask] / np.abs(diag[mask])
    q = q * phases
    det_q = np.linalg.det(q)
    return q / (det_q ** (1.0 / 3.0))


def w_alpha(u, alpha, c=0.37):
    return 1.0 + c * (np.exp(1j * alpha) * np.trace(u) + np.exp(-1j * alpha) * np.trace(u.conj().T))


def odd_part(u, alpha=0.81, c=0.37):
    return 0.5 * (w_alpha(u, alpha, c) - w_alpha(u, -alpha, c))


def even_part(u, alpha=0.81, c=0.37):
    return 0.5 * (w_alpha(u, alpha, c) + w_alpha(u, -alpha, c))


def density_with_frame(frame, m):
    e, _b = split_e_b(m)
    return int(e @ b_from_frame(frame, m))


print("Section A: native carrier split (record-time = direction 0)")

ok_a1 = True
for vals in itertools.product(range(-2, 3), repeat=len(PLANES4)):
    m = matrix_from_flux_values(vals)
    e, b = split_e_b(m)
    ok_a1 = ok_a1 and (q_reference(m) == int(e @ b))
check("A1 record-time split gives Q = e dot b on integer fluxes", ok_a1)

factor = shuffle_cup_factor()
a2_configs = [RNG.integers(-3, 4, size=len(PLANES4), dtype=np.int64) for _ in range(20)]
a2_configs.extend(unit_complementary_fluxes())
ok_a2 = True
for vals in a2_configs:
    m = matrix_from_flux_values(vals)
    f = flux_cochain(m)
    ok_a2 = ok_a2 and (cup_sum_2_2(f, f) == factor * q_reference(m))
check(
    "A2 cochain cup product matches independent flux formula",
    ok_a2,
    f"integer cup factor={factor}; samples={len(a2_configs)}",
)

coeffs = polynomial_cross_coefficients()
electric = {idx for idx, pair in enumerate(PLANES4) if 0 in pair}
magnetic_planes = {idx for idx, pair in enumerate(PLANES4) if 0 not in pair}
expected_cross = set()
for eidx in electric:
    pair = PLANES4[eidx]
    comp = tuple(ax for ax in range(DIM4) if ax not in pair)
    expected_cross.add(tuple(sorted((eidx, PLANE_INDEX[tuple(sorted(comp))]))))
nonzero = {pair for pair, coeff in coeffs.items() if coeff != 0}
pure_zero = all(
    coeff == 0
    for pair, coeff in coeffs.items()
    if (pair[0] in electric and pair[1] in electric) or (pair[0] in magnetic_planes and pair[1] in magnetic_planes)
)
check(
    "A3 Q has only electric-magnetic cross-pairing",
    nonzero == expected_cross and pure_zero,
    f"nonzero coefficients={[(PLANES4[i], PLANES4[j], coeffs[(i, j)]) for i, j in sorted(nonzero)]}",
)

print("Section B: exact transformation law")

p_sp = np.diag([1, -1, -1, -1]).astype(np.int64)
t_rev = np.diag([-1, 1, 1, 1]).astype(np.int64)
rz90 = np.array(
    [
        [0, -1, 0],
        [1, 0, 0],
        [0, 0, 1],
    ],
    dtype=np.int64,
)
l_rz90 = embed_spatial(rz90)

ok_b1 = True
for lmat in (p_sp, t_rev, l_rz90):
    for _ in range(10):
        vals = RNG.integers(-3, 4, size=len(PLANES4), dtype=np.int64)
        m = matrix_from_flux_values(vals)
        pulled = pullback_2_cochain(flux_cochain(m), lmat)
        extracted, divisible = extract_flux_matrix_from_totals(pulled)
        ok_b1 = ok_b1 and divisible and np.array_equal(extracted, transform_flux(m, lmat))
check("B1 cell pullback totals agree with matrix flux action", ok_b1, f"sheet total normalization={SHEET_COUNT}")

ok_b2 = True
for _ in range(200):
    m = matrix_from_flux_values(RNG.integers(-4, 5, size=len(PLANES4), dtype=np.int64))
    e, b = split_e_b(m)
    e2, b2 = split_e_b(transform_flux(m, p_sp))
    ok_b2 = ok_b2 and np.array_equal(e2, -e) and np.array_equal(b2, b) and q_reference(transform_flux(m, p_sp)) == -q_reference(m)
check("B2 spatial inversion flips e and Q while preserving b", ok_b2)

ok_b3 = True
for _ in range(200):
    m = matrix_from_flux_values(RNG.integers(-4, 5, size=len(PLANES4), dtype=np.int64))
    e, b = split_e_b(m)
    e2, b2 = split_e_b(transform_flux(m, t_rev))
    ok_b3 = ok_b3 and np.array_equal(e2, -e) and np.array_equal(b2, b) and q_reference(transform_flux(m, t_rev)) == -q_reference(m)
check("B3 record-order reversal flips e and Q while preserving b", ok_b3)

ok_b4 = True
pt = p_sp @ t_rev
for _ in range(200):
    m = matrix_from_flux_values(RNG.integers(-4, 5, size=len(PLANES4), dtype=np.int64))
    ok_b4 = ok_b4 and q_reference(transform_flux(m, pt)) == q_reference(m)
check("B4 combined spatial and record reversal preserves Q", ok_b4)

ok_b5 = True
for smat in GROUP3:
    lmat = embed_spatial(smat)
    sdet = det_int(smat)
    for _ in range(20):
        m = matrix_from_flux_values(RNG.integers(-3, 4, size=len(PLANES4), dtype=np.int64))
        e, b = split_e_b(m)
        mt = transform_flux(m, lmat)
        et, bt = split_e_b(mt)
        ok_b5 = (
            ok_b5
            and np.array_equal(et, smat @ e)
            and np.array_equal(bt, sdet * (smat @ b))
            and q_reference(mt) == sdet * q_reference(m)
        )
check("B5 full cubic sweep gives vector and pseudovector laws", ok_b5)

print("Section C: orientation non-supply")

ok_c1 = True
for i in range(5):
    tmat = RNG.normal(size=(3, 3)) + (4.0 + i) * np.eye(3)
    tinv = np.linalg.inv(tmat)
    for smat in GROUP3:
        ok_c1 = ok_c1 and abs(float(np.linalg.det(tmat @ smat @ tinv)) - float(np.linalg.det(smat))) < 1e-9
check("C1 determinant is similarity-invariant for named cubic structure", ok_c1)

proper = [s for s in GROUP3 if det_int(s) == 1]
improper = [s for s in GROUP3 if det_int(s) == -1]
proper_keys = {s.tobytes() for s in proper}
ok_c2 = True
for hmat in improper:
    conj_keys = {(hmat @ smat @ hmat.T).astype(np.int64).tobytes() for smat in proper}
    ok_c2 = ok_c2 and (conj_keys == proper_keys)
check("C2 proper cubic subset is stable under improper conjugation", ok_c2, f"proper={len(proper)} improper={len(improper)}")


def canonical_edge(a, b):
    return (a, b) if a <= b else (b, a)


def spatial_site_map(smat, x, n):
    y = smat @ np.array(x, dtype=np.int64)
    return tuple(int(v % n) for v in y)


def nearest_edges(n):
    edge_set = set()
    for x in sites(n, 3):
        for axis in range(3):
            y = list(x)
            y[axis] = (y[axis] + 1) % n
            edge_set.add(canonical_edge(x, tuple(y)))
    return edge_set


edges5 = nearest_edges(5)
ok_c3 = True
for smat in [(-np.eye(3, dtype=np.int64))] + improper:
    mapped = {canonical_edge(spatial_site_map(smat, a, 5), spatial_site_map(smat, b, 5)) for a, b in edges5}
    ok_c3 = ok_c3 and (mapped == edges5)
check("C3 nearest-neighbor spatial edge set is invariant under improper maps", ok_c3, f"edges={len(edges5)}")

print("Section D: Cl(3,0) bridge")

omega = SIGMA1 @ SIGMA2 @ SIGMA3
ok_d1 = close_mat(omega, 1j * I2)
check("D1 orientation volume element supplies the complex unit", ok_d1)

alpha = make_clifford_map(-np.eye(3, dtype=np.int64))
ok_d2_product = automorphism_samples_ok(alpha, 20)
ok_d2_conj = True
sigma2_inv = np.linalg.inv(SIGMA2)
for _ in range(20):
    x = complex_matrix()
    ok_d2_conj = ok_d2_conj and close_mat(alpha(x), SIGMA2 @ np.conjugate(x) @ sigma2_inv)
check("D2 inversion extension matches conjugation model", ok_d2_product and ok_d2_conj)

ok_d3 = True
for _ in range(20):
    x = complex_matrix()
    ok_d3 = ok_d3 and close_mat(alpha(1j * x), -1j * alpha(x))
ok_d3 = ok_d3 and close_mat(alpha(omega), -omega)
check("D3 inversion is antilinear and flips omega", ok_d3)

reflection = make_clifford_map(np.diag([-1, 1, 1]).astype(np.int64))
ok_d4 = automorphism_samples_ok(reflection, 20)
for _ in range(20):
    x = complex_matrix()
    ok_d4 = ok_d4 and close_mat(reflection(1j * x), -1j * reflection(x))
check("D4 single reflection is automorphic and antilinear", ok_d4)

ok_d5 = True
for smat in GROUP3:
    phi = make_clifford_map(smat)
    sdet = det_int(smat)
    verdict = measured_complex_verdict(phi, 5)
    omega_verdict = 1 if close_mat(phi(omega), omega) else (-1 if close_mat(phi(omega), -omega) else 0)
    ok_d5 = ok_d5 and automorphism_samples_ok(phi, 5) and verdict == sdet and omega_verdict == sdet
check("D5 full sweep measures linear versus antilinear parity", ok_d5, f"group size={len(GROUP3)}")

print("Section E: seed direction and imported orientation")

c_seed = 0.37
alpha_seed = 0.81
ok_e1 = True
for _ in range(20):
    u = sample_su3()
    odd = odd_part(u, alpha_seed, c_seed)
    rhs = -2.0 * c_seed * np.sin(alpha_seed) * np.imag(np.trace(u))
    ok_e1 = ok_e1 and abs(float(np.imag(odd))) < 1e-12 and abs(float(np.real(odd)) - float(rhs)) < 1e-12
check("E1 alpha-odd SU(3) insertion equals trace-imaginary readout", ok_e1)

ok_e2 = True
for _ in range(20):
    u = sample_su3()
    odd = odd_part(u, alpha_seed, c_seed)
    ok_e2 = (
        ok_e2
        and abs(odd_part(np.conjugate(u), alpha_seed, c_seed) + odd) < 1e-12
        and abs(odd_part(u.conj().T, alpha_seed, c_seed) + odd) < 1e-12
    )
check("E2 conjugation and loop reversal flip the odd holonomy read", ok_e2)

ok_e3 = True
even_survival_count = 0
for _ in range(20):
    u = sample_su3()
    odd_sum = odd_part(u, alpha_seed, c_seed) + odd_part(np.conjugate(u), alpha_seed, c_seed)
    even_sum = even_part(u, alpha_seed, c_seed) + even_part(np.conjugate(u), alpha_seed, c_seed)
    ok_e3 = ok_e3 and abs(odd_sum) < 1e-12
    if abs(even_sum) > 1e-6:
        even_survival_count += 1
check("E3 swap-closed ensemble cancels odd part but leaves even part", ok_e3 and even_survival_count >= 15, f"even count={even_survival_count}/20")

ok_e4 = True
nonzero_density_count = 0
nonzero_choices = np.array([-3, -2, -1, 1, 2, 3], dtype=np.int64)
for _ in range(20):
    vals = nonzero_choices[RNG.integers(0, len(nonzero_choices), size=len(PLANES4))]
    m = matrix_from_flux_values(vals)
    d123 = density_with_frame((1, 2, 3), m)
    d213 = density_with_frame((2, 1, 3), m)
    ok_e4 = ok_e4 and (d123 == -d213)
    if d123 != 0:
        nonzero_density_count += 1
check("E4 imported orientation frame makes the odd pairing constructible", ok_e4 and nonzero_density_count >= 15, f"nonzero density count={nonzero_density_count}/20")

print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
