"""Gauge-link central-registration step-kernel source runner.

This runner does not read audit ledgers, audit queues, publication matrices, or
effective-status files. It checks only the source note, cited source surfaces,
and independent algebra/numerics for the row.

T1: the two-ended link carrier has gauge-central pointer content given by the
Peter-Weyl isotypic projectors.
T2: positive Lueders scalar central registration Kraus blocks induce normalized,
convolutional, Ad-invariant, inversion-symmetric, positive step kernels.
T3: intra-block frame-picking, deterministic drift, and exact negative-coefficient
central witnesses show what the positive Lueders central scalar registration
hypothesis supplies and what centrality alone does not.
T4: the tested registration-softness family orders per-step variance in a stated
convention, while the per-step soft kernel is not asserted to be a heat kernel.
"""

import numpy as np
from fractions import Fraction
from pathlib import Path


PASS = 0
FAIL = 0


def check(name, condition, detail=""):
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS:", name, detail)
    else:
        FAIL += 1
        print("FAIL:", name, detail)


def flat_text(text):
    return " ".join(text.split())


def require_contains(label, text, needle):
    check(label, needle in flat_text(text), "needle=" + repr(needle))


def require_absent(label, text, needle):
    check(label, needle not in flat_text(text), "needle=" + repr(needle))


def frac_matrix_mul(a, b):
    n = len(a)
    m = len(b[0])
    kmax = len(b)
    out = [[Fraction(0) for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for k in range(kmax):
            aik = a[i][k]
            if aik == 0:
                continue
            for j in range(m):
                out[i][j] += aik * b[k][j]
    return out


def frac_matrix_zero(n, m):
    return [[Fraction(0) for _ in range(m)] for _ in range(n)]


def frac_matrix_identity(n):
    out = frac_matrix_zero(n, n)
    for i in range(n):
        out[i][i] = Fraction(1)
    return out


def frac_matrix_add(mats):
    n = len(mats[0])
    m = len(mats[0][0])
    out = frac_matrix_zero(n, m)
    for mat in mats:
        for i in range(n):
            for j in range(m):
                out[i][j] += mat[i][j]
    return out


def frac_matrix_equal(a, b):
    return all(a[i][j] == b[i][j] for i in range(len(a)) for j in range(len(a[0])))


def permutation_group_s3():
    elems = [
        (0, 1, 2),
        (0, 2, 1),
        (1, 0, 2),
        (1, 2, 0),
        (2, 0, 1),
        (2, 1, 0),
    ]
    idx = {g: i for i, g in enumerate(elems)}

    def mul(a, b):
        return tuple(a[b[i]] for i in range(3))

    def inv(a):
        out = [0, 0, 0]
        for i, ai in enumerate(a):
            out[ai] = i
        return tuple(out)

    return elems, idx, mul, inv


def s3_parity(g):
    invs = 0
    for i in range(3):
        for j in range(i + 1, 3):
            if g[i] > g[j]:
                invs += 1
    return -1 if invs % 2 else 1


def s3_fixpoints(g):
    return sum(1 for i in range(3) if g[i] == i)


def s3_character_data(elems):
    data = [
        ("triv", 1, {g: 1 for g in elems}),
        ("sign", 1, {g: s3_parity(g) for g in elems}),
        ("std", 2, {g: s3_fixpoints(g) - 1 for g in elems}),
    ]
    return data


def regular_matrix(elems, idx, mul, a, side):
    n = len(elems)
    mat = np.zeros((n, n), dtype=float)
    for col, h in enumerate(elems):
        if side == "left":
            target = mul(a, h)
        else:
            target = mul(h, a)
        mat[idx[target], col] = 1.0
    return mat


def commutant_dimension(elems, idx, mul, use_left=True, use_right=True):
    n = len(elems)
    rows = []
    mats = []
    if use_left:
        mats += [regular_matrix(elems, idx, mul, a, "left") for a in elems]
    if use_right:
        mats += [regular_matrix(elems, idx, mul, a, "right") for a in elems]
    for a_mat in mats:
        for r in range(n):
            for c in range(n):
                row = np.zeros(n * n, dtype=float)
                for k in range(n):
                    row[r * n + k] += a_mat[k, c]
                    row[k * n + c] -= a_mat[r, k]
                rows.append(row)
    system = np.vstack(rows)
    rank = np.linalg.matrix_rank(system, tol=1e-9)
    return n * n - int(rank)


def projector_matrices(elems, idx, mul, inv, char_data):
    n = len(elems)
    projectors = {}
    for name, dim, chars in char_data:
        mat = frac_matrix_zero(n, n)
        for g in elems:
            for h in elems:
                x = mul(g, inv(h))
                mat[idx[g]][idx[h]] = Fraction(dim * chars[x], n)
        projectors[name] = mat
    return projectors


def kernel_from_bins(elems, idx, mul, inv, char_data, bins):
    n = len(elems)
    tmat = frac_matrix_zero(n, n)
    for g in elems:
        for h in elems:
            total = Fraction(0)
            x = mul(g, inv(h))
            for bin_names in bins:
                amp = Fraction(0)
                for name, dim, chars in char_data:
                    if name in bin_names:
                        amp += Fraction(dim * chars[x], n)
                total += amp * amp
            tmat[idx[g]][idx[h]] = total
    return tmat


def kernel_from_projectors(projectors, bins):
    names = list(projectors)
    n = len(projectors[names[0]])
    tmat = frac_matrix_zero(n, n)
    for bin_names in bins:
        kmat = frac_matrix_add([projectors[name] for name in bin_names])
        for i in range(n):
            for j in range(n):
                tmat[i][j] += kmat[i][j] * kmat[i][j]
    return tmat


def exact_kernel_battery(prefix, elems, idx, mul, inv, char_data, projectors, bins):
    t_proj = kernel_from_projectors(projectors, bins)
    t_formula = kernel_from_bins(elems, idx, mul, inv, char_data, bins)
    check(prefix + " closed formula matches projectors", frac_matrix_equal(t_proj, t_formula))

    n = len(elems)
    col_sums = [sum(t_proj[r][c] for r in range(n)) for c in range(n)]
    check(prefix + " columns normalize exactly", all(v == 1 for v in col_sums), str(col_sums))

    invariant = True
    for a in elems:
        for b in elems:
            for g in elems:
                for h in elems:
                    left_g = mul(mul(a, g), b)
                    left_h = mul(mul(a, h), b)
                    if t_proj[idx[g]][idx[h]] != t_proj[idx[left_g]][idx[left_h]]:
                        invariant = False
    check(prefix + " two-sided invariance exactly", invariant)

    inversion = True
    e = elems[0]
    for x in elems:
        if t_proj[idx[x]][idx[e]] != t_proj[idx[inv(x)]][idx[e]]:
            inversion = False
    check(prefix + " inversion symmetry exactly", inversion)

    coeffs = []
    for name, dim, chars in char_data:
        coeff = Fraction(0)
        for x in elems:
            coeff += t_proj[idx[x]][idx[e]] * chars[inv(x)]
        coeff /= n
        coeffs.append((name, coeff))
    check(prefix + " character coefficients nonnegative", all(c >= 0 for _, c in coeffs), str(coeffs))
    print(prefix + " character coefficients:", coeffs)
    return t_proj, coeffs


def run_s3_exact():
    elems, idx, mul, inv = permutation_group_s3()
    chars = s3_character_data(elems)
    projectors = projector_matrices(elems, idx, mul, inv, chars)
    identity = frac_matrix_identity(6)

    idempotent = True
    orthogonal = True
    for name, _, _ in chars:
        p = projectors[name]
        idempotent = idempotent and frac_matrix_equal(frac_matrix_mul(p, p), p)
    for i, (name_i, _, _) in enumerate(chars):
        for j, (name_j, _, _) in enumerate(chars):
            if i == j:
                continue
            prod = frac_matrix_mul(projectors[name_i], projectors[name_j])
            orthogonal = orthogonal and frac_matrix_equal(prod, frac_matrix_zero(6, 6))
    sum_to_i = frac_matrix_equal(frac_matrix_add([projectors[name] for name, _, _ in chars]), identity)
    check("A1 S3 projectors idempotent", idempotent)
    check("A1 S3 projectors mutually orthogonal", orthogonal)
    check("A1 S3 projectors sum to identity", sum_to_i)

    both_dim = commutant_dimension(elems, idx, mul, True, True)
    left_dim = commutant_dimension(elems, idx, mul, True, False)
    check("A2 S3 two-sided commutant dimension is 3", both_dim == 3, str(both_dim))
    check("A2 S3 left-only commutant dimension rejector is 6", left_dim == 6, str(left_dim))

    t_full, coeffs_full = exact_kernel_battery(
        "A3 S3 full-resolution", elems, idx, mul, inv, chars, projectors,
        [{"triv"}, {"sign"}, {"std"}],
    )
    exact_kernel_battery(
        "A4 S3 coarse central bin", elems, idx, mul, inv, chars, projectors,
        [{"triv", "sign"}, {"std"}],
    )
    return elems, idx, mul, inv, chars, projectors, t_full, coeffs_full


def matrix_key(mat):
    rounded = np.round(np.stack((mat.real, mat.imag), axis=0), 8)
    rounded[np.abs(rounded) < 1e-8] = 0.0
    return rounded.tobytes()


def q8_group():
    one = np.eye(2, dtype=complex)
    ii = np.array([[1j, 0], [0, -1j]], dtype=complex)
    jj = np.array([[0, 1], [-1, 0]], dtype=complex)
    kk = ii @ jj
    generators = [ii, jj]
    seen = {matrix_key(one): one}
    queue = [one]
    while queue:
        g = queue.pop(0)
        for a in generators:
            for h in (g @ a, a @ g):
                key = matrix_key(h)
                if key not in seen:
                    seen[key] = h
                    queue.append(h)
    prototypes = [
        ("1", one),
        ("-1", -one),
        ("i", ii),
        ("-i", -ii),
        ("j", jj),
        ("-j", -jj),
        ("k", kk),
        ("-k", -kk),
    ]
    elems = [name for name, _ in prototypes]
    mats = {name: mat for name, mat in prototypes}
    check("B0 Q8 closure has eight elements", len(seen) == 8)
    check("B0 Q8 closure matches prototypes", all(matrix_key(mat) in seen for _, mat in prototypes))
    idx = {g: i for i, g in enumerate(elems)}
    key_to_name = {matrix_key(mat): name for name, mat in prototypes}

    def mul(a, b):
        return key_to_name[matrix_key(mats[a] @ mats[b])]

    def inv(a):
        return key_to_name[matrix_key(np.linalg.inv(mats[a]))]

    return elems, idx, mul, inv


def q8_character_data(elems):
    chars = {}
    for name in elems:
        if name in ("1", "-1", "i", "-i"):
            ci = 1
        else:
            ci = -1
        if name in ("1", "-1", "j", "-j"):
            cj = 1
        else:
            cj = -1
        if name in ("1", "-1", "k", "-k"):
            ck = 1
        else:
            ck = -1
        if name == "1":
            q = 2
        elif name == "-1":
            q = -2
        else:
            q = 0
        chars[name] = (1, ci, cj, ck, q)
    names = ["triv", "chi_i", "chi_j", "chi_k", "quat"]
    dims = [1, 1, 1, 1, 2]
    return [(names[i], dims[i], {g: chars[g][i] for g in elems}) for i in range(5)]


def run_q8_exact():
    elems, idx, mul, inv = q8_group()
    chars = q8_character_data(elems)
    dim_sum = sum(Fraction(dim * dim) for _, dim, _ in chars)
    check("B1 Q8 sum dimensions squared is 8", dim_sum == 8, str(dim_sum))
    row_orth = True
    for i, (_, _, chars_i) in enumerate(chars):
        for j, (_, _, chars_j) in enumerate(chars):
            inner = sum(Fraction(chars_i[g] * chars_j[g], 8) for g in elems)
            row_orth = row_orth and (inner == (1 if i == j else 0))
    check("B1 Q8 character rows orthonormal exactly", row_orth)

    both_dim = commutant_dimension(elems, idx, mul, True, True)
    left_dim = commutant_dimension(elems, idx, mul, True, False)
    check("B2 Q8 two-sided commutant dimension is 5", both_dim == 5, str(both_dim))
    check("B2 Q8 left-only commutant dimension rejector is 8", left_dim == 8, str(left_dim))

    projectors = projector_matrices(elems, idx, mul, inv, chars)
    exact_kernel_battery(
        "B3 Q8 full-resolution", elems, idx, mul, inv, chars, projectors,
        [{"triv"}, {"chi_i"}, {"chi_j"}, {"chi_k"}, {"quat"}],
    )
    return elems, idx, mul, inv, chars


def run_s3_contrast(elems, idx, mul, inv, projectors, chars):
    p_std = np.array([[float(x) for x in row] for row in projectors["std"]], dtype=float)
    rng = np.random.default_rng(20260702)
    dmat = np.diag(rng.normal(size=6))
    a_mat = p_std @ dmat @ p_std
    c = 0.1 / np.linalg.norm(a_mat, 2)
    k_mat = c * a_mat
    residual = np.eye(6) - k_mat.conj().T @ k_mat
    vals, vecs = np.linalg.eigh(residual)
    vals = np.clip(vals, 0.0, None)
    k0 = (vecs * np.sqrt(vals)) @ vecs.conj().T
    tmat = np.abs(k0) ** 2 + np.abs(k_mat) ** 2
    col_sums = tmat.sum(axis=0)
    check("C1 intra-block channel column validity", np.max(np.abs(col_sums - 1.0)) < 1e-10, str(np.max(np.abs(col_sums - 1.0))))

    by_delta = {}
    for g in elems:
        for h in elems:
            x = mul(g, inv(h))
            by_delta.setdefault(x, []).append(tmat[idx[g], idx[h]])
    max_violation = 0.0
    for vals_for_x in by_delta.values():
        for v in vals_for_x:
            for w in vals_for_x:
                max_violation = max(max_violation, abs(float(v - w)))
    check("C1 intra-block non-scalar Kraus is non-convolution", max_violation > 1e-4, "max=" + str(max_violation))

    g0 = (1, 2, 0)
    drift = np.zeros((6, 6), dtype=float)
    for g in elems:
        for h in elems:
            if g == mul(g0, h):
                drift[idx[g], idx[h]] = 1.0
    conv_ok = True
    by_delta = {}
    for g in elems:
        for h in elems:
            x = mul(g, inv(h))
            val = drift[idx[g], idx[h]]
            if x in by_delta and abs(by_delta[x] - val) > 1e-12:
                conv_ok = False
            by_delta[x] = val
    check("C2 drift witness is a convolution kernel", conv_ok)

    e = elems[0]
    coeffs = []
    for name, dim, ch in chars:
        coeff = 0.0
        for x in elems:
            coeff += drift[idx[x], idx[e]] * ch[inv(x)]
        coeff /= 6.0
        coeffs.append((name, coeff))
    min_nontriv = min(cval for name, cval in coeffs if name != "triv")
    check("C2 drift has negative nontrivial character coefficient", min_nontriv < -0.05, str(coeffs))

    rho_g0 = np.array([
        [np.cos(2 * np.pi / 3), -np.sin(2 * np.pi / 3)],
        [np.sin(2 * np.pi / 3), np.cos(2 * np.pi / 3)],
    ])
    nonscalar_norm = np.linalg.norm(rho_g0 - (np.trace(rho_g0) / 2.0) * np.eye(2), 2)
    check("C2 drift standard Fourier block is non-scalar", nonscalar_norm > 0.5, str(nonscalar_norm))

    p_triv = projectors["triv"]
    p_sign = projectors["sign"]
    p_std_frac = projectors["std"]
    k_central = [
        [p_triv[i][j] + p_sign[i][j] - p_std_frac[i][j] for j in range(6)]
        for i in range(6)
    ]
    check(
        "C3 central unitary witness squares to identity exactly",
        frac_matrix_mul(k_central, k_central) == frac_matrix_identity(6),
    )

    t_central = [[k_central[i][j] ** 2 for j in range(6)] for i in range(6)]
    by_delta_exact = {}
    conv_exact = True
    for g in elems:
        for h in elems:
            x = mul(g, inv(h))
            val = t_central[idx[g]][idx[h]]
            if x in by_delta_exact and by_delta_exact[x] != val:
                conv_exact = False
            by_delta_exact[x] = val
    check("C3 central unitary induced kernel is an exact convolution", conv_exact)

    class_expected = {3: Fraction(1, 9), 1: Fraction(0), 0: Fraction(4, 9)}
    class_ok = True
    for x, val in by_delta_exact.items():
        fixed = sum(1 for i in range(3) if x[i] == i)
        class_ok = class_ok and (val == class_expected[fixed])
    check(
        "C3 central unitary kernel class values exact",
        class_ok,
        str(sorted((x, str(v)) for x, v in by_delta_exact.items())),
    )

    e_id = elems[0]
    coeff_map_central = {}
    for name, dim, ch in chars:
        coeff = Fraction(0)
        for x in elems:
            coeff += t_central[idx[x]][idx[e_id]] * ch[inv(x)]
        coeff_map_central[name] = coeff / 6
    expected_central = {"triv": Fraction(1, 6), "sign": Fraction(1, 6), "std": Fraction(-1, 9)}
    check(
        "C3 central unitary character coefficients exact with negative std block",
        coeff_map_central == expected_central and coeff_map_central["std"] < 0,
        str(coeff_map_central),
    )

    w_big = Fraction(12, 13)
    w_small = Fraction(5, 13)
    k_one = [
        [w_big * (p_triv[i][j] + p_sign[i][j] - p_std_frac[i][j]) for j in range(6)]
        for i in range(6)
    ]
    k_two = [
        [w_small * (p_triv[i][j] + p_sign[i][j] + p_std_frac[i][j]) for j in range(6)]
        for i in range(6)
    ]
    k_one_t = [[k_one[j][i] for j in range(6)] for i in range(6)]
    k_two_t = [[k_two[j][i] for j in range(6)] for i in range(6)]
    kraus_sum = frac_matrix_add([
        frac_matrix_mul(k_one_t, k_one),
        frac_matrix_mul(k_two_t, k_two),
    ])
    check(
        "C4 two-outcome 5-12-13 instrument is exactly trace-preserving",
        kraus_sum == frac_matrix_identity(6),
    )

    t_two = [
        [k_one[i][j] ** 2 + k_two[i][j] ** 2 for j in range(6)]
        for i in range(6)
    ]
    by_delta_two = {}
    conv_two = True
    for g in elems:
        for h in elems:
            x = mul(g, inv(h))
            val = t_two[idx[g]][idx[h]]
            if x in by_delta_two and by_delta_two[x] != val:
                conv_two = False
            by_delta_two[x] = val
    check("C4 two-outcome induced kernel is an exact convolution", conv_two)

    coeff_map_two = {}
    for name, dim, ch in chars:
        coeff = Fraction(0)
        for x in elems:
            coeff += t_two[idx[x]][idx[e_id]] * ch[inv(x)]
        coeff_map_two[name] = coeff / 6
    expected_two = {"triv": Fraction(1, 6), "sign": Fraction(1, 6), "std": Fraction(-23, 507)}
    check(
        "C4 two-outcome character coefficients exact",
        coeff_map_two == expected_two,
        str(coeff_map_two),
    )
    check(
        "C4 two-outcome std coefficient strictly negative",
        coeff_map_two["std"] < 0,
        str(coeff_map_two["std"]),
    )


def det3_arrays(a00, a01, a02, a10, a11, a12, a20, a21, a22):
    return (
        a00 * a11 * a22
        + a01 * a12 * a20
        + a02 * a10 * a21
        - a02 * a11 * a20
        - a01 * a10 * a22
        - a00 * a12 * a21
    )


def su3_dimension(lam):
    out = Fraction(1)
    for i in range(3):
        for j in range(i + 1, 3):
            out *= Fraction(lam[i] - lam[j] + j - i, j - i)
    return int(out)


def su3_c2(lam):
    total = sum(Fraction(lam[i] * (lam[i] + 4 - 2 * (i + 1))) for i in range(3))
    s = sum(lam)
    return (total - Fraction(s * s, 3)) / 2


def scalar_h(k):
    if k < 0:
        return 0
    return (k + 1) * (k + 2) // 2


def det3_int(mat):
    return (
        mat[0][0] * mat[1][1] * mat[2][2]
        + mat[0][1] * mat[1][2] * mat[2][0]
        + mat[0][2] * mat[1][0] * mat[2][1]
        - mat[0][2] * mat[1][1] * mat[2][0]
        - mat[0][1] * mat[1][0] * mat[2][2]
        - mat[0][0] * mat[1][2] * mat[2][1]
    )


def chi_scalar_dimension(lam):
    mat = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append(scalar_h(lam[i] - (i + 1) + (j + 1)))
        mat.append(row)
    return det3_int(mat)


def run_su3_numerics():
    m_grid = 256
    pmax = 10
    t = -np.pi + 2 * np.pi * (np.arange(m_grid) + 0.5) / m_grid
    t1g, t2g = np.meshgrid(t, t, indexing="ij")
    t3g = -(t1g + t2g)
    x1 = np.exp(1j * t1g)
    x2 = np.exp(1j * t2g)
    x3 = np.exp(1j * t3g)

    e10 = np.exp(1j * t1g * 2)
    e11 = np.exp(1j * t1g)
    e12 = np.ones_like(e11)
    e20 = np.exp(1j * t2g * 2)
    e21 = np.exp(1j * t2g)
    e22 = np.ones_like(e21)
    e30 = np.exp(1j * t3g * 2)
    e31 = np.exp(1j * t3g)
    e32 = np.ones_like(e31)
    alt = det3_arrays(e10, e11, e12, e20, e21, e22, e30, e31, e32)
    haar = (np.abs(alt) ** 2) / 6.0
    haar_mean = float(np.mean(haar))
    haar_tol = 1e-6 if abs(haar_mean - 1.0) < 1e-10 else 5e-3
    check("D0 SU3 Haar class density normalizes", abs(haar_mean - 1.0) < haar_tol, str(haar_mean))

    def integral(arr):
        return np.mean(haar * arr) / haar_mean

    reps = []
    for p in range(pmax + 1):
        for q in range(pmax + 1 - p):
            lam = (p + q, q, 0)
            reps.append((lam, p, q, su3_dimension(lam), su3_c2(lam)))
    reps.sort()
    label_to_index = {lam: i for i, (lam, _, _, _, _) in enumerate(reps)}

    max_h = max(lam[0] + 2 for lam, _, _, _, _ in reps)
    h2 = [None for _ in range(max_h + 1)]
    h3 = [None for _ in range(max_h + 1)]
    h2[0] = np.ones_like(x1, dtype=complex)
    for k in range(1, max_h + 1):
        h2[k] = x1 * h2[k - 1] + x2 ** k
    h3[0] = np.ones_like(x1, dtype=complex)
    for k in range(1, max_h + 1):
        acc = np.zeros_like(x1, dtype=complex)
        for j in range(k + 1):
            acc += (x3 ** j) * h2[k - j]
        h3[k] = acc

    def h_arr(k):
        if k < 0:
            return np.zeros_like(x1, dtype=complex)
        return h3[k]

    chars = []
    dims = []
    c2s = []
    dim_ok = True
    for lam, _, _, dim, c2 in reps:
        mat = []
        for i in range(3):
            row = []
            for j in range(3):
                row.append(h_arr(lam[i] - (i + 1) + (j + 1)))
            mat.append(row)
        chi = det3_arrays(
            mat[0][0], mat[0][1], mat[0][2],
            mat[1][0], mat[1][1], mat[1][2],
            mat[2][0], mat[2][1], mat[2][2],
        )
        chars.append(chi)
        dims.append(dim)
        c2s.append(float(c2))
        dim_ok = dim_ok and (chi_scalar_dimension(lam) == dim)
    chars = np.asarray(chars, dtype=np.complex128)
    dims = np.asarray(dims, dtype=float)
    c2s = np.asarray(c2s, dtype=float)
    check("D1 SU3 scalar Jacobi-Trudi dimensions match Weyl dimensions", dim_ok, "reps=" + str(len(reps)))

    ortho_pairs = [
        ((1, 0, 0), (1, 0, 0)),
        ((2, 1, 0), (2, 1, 0)),
        ((1, 0, 0), (2, 1, 0)),
        ((2, 0, 0), (1, 1, 0)),
    ]
    ortho_ok = True
    ortho_vals = []
    for a, b in ortho_pairs:
        ia = label_to_index[a]
        ib = label_to_index[b]
        val = integral(np.conjugate(chars[ia]) * chars[ib])
        target = 1.0 if a == b else 0.0
        ortho_vals.append((a, b, val))
        ortho_ok = ortho_ok and (abs(val - target) < 1e-5)
    check("D1 SU3 sampled character orthonormality", ortho_ok, str([(a, b, complex(v)) for a, b, v in ortho_vals]))

    n_trunc = float(np.sum(dims ** 2))
    sample_labels = [(1, 0, 0), (2, 1, 0), (2, 0, 0), (3, 1, 0), (1, 1, 0)]
    sample_indices = [label_to_index[x] for x in sample_labels]

    def kernel_from_weights(weights):
        weighted = weights * dims[np.newaxis, :]
        kappas = np.tensordot(weighted, chars, axes=(1, 0))
        return np.sum(np.abs(kappas) ** 2, axis=0).real / n_trunc

    def coeffs_for(tker, indices):
        return np.asarray([integral(tker * np.conjugate(chars[i])) for i in indices])

    centers = np.arange(0.0, 62.0, 2.0)
    widths = [0.5, 2.0, 6.0, 15.0]
    kernels = {}
    variances = {}

    proj_weights = np.eye(len(reps), dtype=float)
    kernels["projective"] = kernel_from_weights(proj_weights)

    for width in widths:
        raw = np.exp(-((c2s[np.newaxis, :] - centers[:, np.newaxis]) / width) ** 2)
        probs = raw / np.sum(raw, axis=0, keepdims=True)
        kernels["w=" + str(width)] = kernel_from_weights(np.sqrt(probs))

    principal_t3 = ((-(t1g + t2g) + np.pi) % (2 * np.pi)) - np.pi
    distance = t1g ** 2 + t2g ** 2 + principal_t3 ** 2

    for label, tker in kernels.items():
        norm = integral(tker)
        check("D2 SU3 " + label + " kernel normalizes", abs(float(norm.real) - 1.0) < 5e-3, str(norm))
        coeffs = coeffs_for(tker, sample_indices)
        rel_imag = np.max(np.abs(coeffs.imag) / np.maximum(1.0, np.abs(coeffs.real)))
        check("D2 SU3 " + label + " sampled coefficients real", rel_imag < 1e-8, str(rel_imag))
        min_coeff = float(np.min(coeffs.real))
        if label == "projective":
            check("D2 SU3 " + label + " sampled coefficients nonnegative", min_coeff > -1e-10, str(min_coeff))
        else:
            check("D2 SU3 " + label + " sampled coefficients positive", min_coeff > 1e-6, str(min_coeff))
        variances[label] = float((integral(tker * distance) / norm).real)

    ordered_labels = ["projective", "w=0.5", "w=2.0", "w=6.0", "w=15.0"]
    order_ok = True
    for a, b in zip(ordered_labels[:-1], ordered_labels[1:]):
        va = variances[a]
        vb = variances[b]
        order_ok = order_ok and (va > vb and (va - vb) / va > 0.05)
    check("D3 SU3 variance strictly decreases with softness", order_ok, str(variances))

    refs = {
        "projective": 9.870,
        "w=0.5": 8.048,
        "w=2.0": 5.852,
        "w=6.0": 2.476,
        "w=15.0": 1.861,
    }
    for label in ordered_labels:
        val = variances[label]
        ref = refs[label]
        check("D3 SU3 " + label + " variance near validation reference", abs(val - ref) / ref < 0.10, "value=" + str(val) + " ref=" + str(ref))

    t_width6 = kernels["w=6.0"]
    eps_labels = [(1, 0, 0), (2, 1, 0), (2, 0, 0)]
    eps_indices = [label_to_index[x] for x in eps_labels]
    eps_coeffs = coeffs_for(t_width6, eps_indices).real
    triv_coeff = float(integral(t_width6).real)
    ratios = []
    for coeff, label in zip(eps_coeffs, eps_labels):
        dim = dims[label_to_index[label]]
        eps = -np.log((coeff / dim) / triv_coeff)
        ratios.append(eps / c2s[label_to_index[label]])
    ratios = np.asarray(ratios)
    spread = float((np.max(ratios) - np.min(ratios)) / np.mean(ratios))
    check("D4 SU3 width-6 per-block generator spread exceeds heat-form floor", spread > 0.2, str(spread))
    check("D4 SU3 width-6 per-block generator spread remains bounded", spread < 1.0, str(spread))

    wrap_engaged = integral(np.where(np.abs(t1g + t2g) > np.pi, 1.0, 0.0))
    check(
        "D5 SU3 principal-eigenphase wrap region has positive Haar measure",
        float(np.real(wrap_engaged)) > 1e-3,
        str(wrap_engaged),
    )


def run_exact_summary(s3_chars, s3_coeffs):
    s3_dim_sum = sum(Fraction(dim * dim) for _, dim, _ in s3_chars)
    q8_dim_sum = Fraction(1 + 1 + 1 + 1 + 4)
    check("E1 S3 dimension-square sum is group order", s3_dim_sum == 6, str(s3_dim_sum))
    check("E1 Q8 dimension-square sum is group order", q8_dim_sum == 8, str(q8_dim_sum))
    coeff_map = {name: coeff for name, coeff in s3_coeffs}
    expected = {"triv": Fraction(1, 6), "sign": Fraction(1, 9), "std": Fraction(1, 9)}
    check("E2 S3 full-resolution spectral data exact", coeff_map == expected, str(coeff_map))

    elems, idx, mul, inv = permutation_group_s3()
    chars = {name: ch for name, _, ch in s3_character_data(elems)}
    mults = {}
    for name in ["triv", "sign", "std"]:
        inner = Fraction(0)
        for g in elems:
            inner += Fraction(chars["std"][g] * chars["std"][g] * chars[name][inv(g)], 6)
        mults[name] = inner
    check("E3 S3 std tensor std multiplicities nonnegative", all(v >= 0 for v in mults.values()), str(mults))
    check("E3 S3 std tensor std exact decomposition", mults == {"triv": 1, "sign": 1, "std": 1}, str(mults))


def run_source_guards():
    root = Path(__file__).resolve().parents[1]
    note_path = root / "docs" / "GAUGE_LINK_CENTRAL_REGISTRATION_INDUCED_BI_INVARIANT_STEP_KERNEL_THEOREM_NOTE_2026-07-02.md"
    runner_path = Path(__file__).resolve()
    dep_paths = [
        root / "docs" / "G_BARE_RIGIDITY_THEOREM_NOTE.md",
        root / "docs" / "RECORD_FORMATION_CONTROLLED_COPY_WRITE_ISOMETRY_THEOREM_NOTE_2026-06-18.md",
        root / "docs" / "RECORD_CLASSICAL_SEMIGROUP_BOUNDARY_2026-06-06.md",
        root / "docs" / "AXIOM_FIRST_REFLECTION_POSITIVITY_WILSON_TEMPORAL_GAUGE_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md",
    ]
    check("F source note exists", note_path.exists(), str(note_path.relative_to(root)))
    for dep in dep_paths:
        check("F dependency exists " + dep.name, dep.exists(), str(dep.relative_to(root)))

    if note_path.exists():
        note_text = note_path.read_text()
    else:
        note_text = ""
    runner_text = runner_path.read_text()

    dep_markers = [
        (dep_paths[0], "no independent scalar-normalization freedom"),
        (dep_paths[1], "projective record-write isometry"),
        (dep_paths[2], "continuous Markov semigroups live on the probability/ensemble"),
        (dep_paths[3], "plane positive kernel"),
    ]
    for dep, marker in dep_markers:
        text = dep.read_text() if dep.exists() else ""
        require_contains("F dependency marker " + dep.name, text, marker)

    preserve = [
        "independent audit lane only",
        "Central-scalar record registration",
        "gauge-central",
        "derived, not assumed",
        "registration-centrality",
        "does not derive that a record step occurs",
        "registration softness",
        "not a citation-graph dependency",
        "does not claim:",
        "an audit verdict or any effective-status promotion",
        "Kronecker",
        "intra-block",
        "the per-step kernel is not the heat kernel",
        "positive Lueders subclass",
        "centrality alone does not give representation positivity",
        "per-step variance",
        "N_trunc^(-1/2)",
        "principal-eigenphase distance",
    ]
    for marker in preserve:
        require_contains("F note preserve marker", note_text, marker)

    canonical = [
        "**Claim type:** bounded_theorem",
        "**Claim scope:** Central-scalar record registration",
        "**Status authority:** independent audit lane only.",
    ]
    for marker in canonical:
        require_contains("F canonical source metadata", note_text, marker)

    forbidden = [
        "**Audit " + "status:**",
        "**Status:** " + "PASS",
        "audit" + "_" + "status" + ":",
        "effective" + "_" + "status" + ":",
        "only" + " " + "route",
        "exh" + "austed",
        "closes" + " " + "the" + " " + "route",
        "covariance" + " " + "implies" + " " + "the" + " " + "step-measure" + " " + "premise",
        "# Gauge-Link Record Step: Central" + " Registration Induces Bi-Invariant Step Kernels",
        "## Theorem 2 (central" + " registration induces bi-invariant positive step kernels)",
        "## Theorem 4 (registration softness sets the step size;" + " derived rates)",
        "Each registration channel therefore has a derived" + " rate",
        "the load-bearing input is registration-centrality," + " not kinematic covariance",
    ]
    for marker in forbidden:
        require_absent("F note forbidden string absent", note_text, marker)
        require_absent("F runner forbidden string absent", runner_text, marker)


def main():
    s3_elems, s3_idx, s3_mul, s3_inv, s3_chars, s3_projectors, _, s3_coeffs = run_s3_exact()
    run_q8_exact()
    run_s3_contrast(s3_elems, s3_idx, s3_mul, s3_inv, s3_projectors, s3_chars)
    run_su3_numerics()
    run_exact_summary(s3_chars, s3_coeffs)
    run_source_guards()
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    if FAIL > 0:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
