"""
Condition-alphabet identification runner.

Sections:
- S0: shared signed-permutation and real-basis machinery
- A: the coupled action and the content law
- B: alphabet size: chirality threshold met, shortcut closed
- C: chiral channels: none below vector triples
- D: transport: one bit at every alphabet size

Expected close: TOTAL: PASS=16 FAIL=0
"""

import itertools

import numpy as np


PASS = 0
FAIL = 0
TOL = 1.0e-10
rng = np.random.default_rng(2)


def check(name, cond, detail=""):
    global PASS, FAIL
    if cond:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    suffix = f" | {detail}" if detail else ""
    print(f"{status}: {name}{suffix}")


def det3_int(A):
    return int(
        A[0, 0] * (A[1, 1] * A[2, 2] - A[1, 2] * A[2, 1])
        - A[0, 1] * (A[1, 0] * A[2, 2] - A[1, 2] * A[2, 0])
        + A[0, 2] * (A[1, 0] * A[2, 1] - A[1, 1] * A[2, 0])
    )


def perm_sign(p):
    inversions = 0
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[i] > p[j]:
                inversions += 1
    return -1 if inversions % 2 else 1


def all_signed_permutation_matrices():
    out = []
    for p in itertools.permutations(range(3)):
        for signs in itertools.product((-1, 1), repeat=3):
            S = np.zeros((3, 3), dtype=int)
            for row, col in enumerate(p):
                S[row, col] = signs[row]
            out.append(S)
    return out


mats = all_signed_permutation_matrices()
proper = [S for S in mats if det3_int(S) == 1]
improper = [S for S in mats if det3_int(S) == -1]
P = -np.eye(3, dtype=int)

I2 = np.eye(2, dtype=complex)
sigma1 = np.array([[0, 1], [1, 0]], dtype=complex)
sigma2 = np.array([[0, -1j], [1j, 0]], dtype=complex)
sigma3 = np.array([[1, 0], [0, -1]], dtype=complex)
sigmas = [sigma1, sigma2, sigma3]


def sigma_dot(v):
    return v[0] * sigma1 + v[1] * sigma2 + v[2] * sigma3


def su2_lift(R):
    R = np.asarray(R, dtype=float)
    cos_t = np.clip((np.trace(R) - 1.0) / 2.0, -1.0, 1.0)
    t = np.arccos(cos_t)
    if abs(t) < 1.0e-12:
        n = np.array([1.0, 0.0, 0.0])
    elif abs(np.pi - t) < 1.0e-8:
        B = R + np.eye(3)
        col = int(np.argmax(np.sum(B * B, axis=0)))
        n = B[:, col]
        n_norm = np.linalg.norm(n)
        assert n_norm > TOL, "axis-angle pi branch produced a zero axis"
        n = n / n_norm
    else:
        n = np.array(
            [
                R[2, 1] - R[1, 2],
                R[0, 2] - R[2, 0],
                R[1, 0] - R[0, 1],
            ]
        ) / (2.0 * np.sin(t))
        n = n / np.linalg.norm(n)
    return np.cos(t / 2.0) * I2 - 1j * np.sin(t / 2.0) * sigma_dot(n)


def compose(a, b, v, w):
    X = (a + 1j * b) * I2.copy()
    for i in range(3):
        X = X + (v[i] + 1j * w[i]) * sigmas[i]
    return X


def decompose(X):
    scalar = np.trace(X) / 2.0
    a = float(np.real(scalar))
    b = float(np.imag(scalar))
    v = np.zeros(3)
    w = np.zeros(3)
    for i in range(3):
        coeff = np.trace(sigmas[i] @ X) / 2.0
        v[i] = float(np.real(coeff))
        w[i] = float(np.imag(coeff))
    return a, b, v, w


def full_action(S, X):
    d = det3_int(S)
    if d == 1:
        u = su2_lift(S)
        return u @ X @ u.conj().T
    u = su2_lift(-S)
    return u @ (sigma2 @ np.conjugate(X) @ sigma2) @ u.conj().T


def fixed_axis_directions(S):
    count = 0
    for i in range(3):
        e = np.zeros(3, dtype=int)
        e[i] = 1
        if np.array_equal(S @ e, e):
            count += 1
        if np.array_equal(S @ (-e), -e):
            count += 1
    return count


def sign_multiplicity(chars, label):
    total = 0
    for S, chi in zip(mats, chars):
        total += det3_int(S) * int(chi)
    assert total % len(mats) == 0, f"{label} sign multiplicity is not integral"
    return total // len(mats), total


def vector_power_chars(n):
    return [int(np.trace(S)) ** n for S in mats]


def dir6_vector_power_chars(n):
    return [fixed_axis_directions(S) * (int(np.trace(S)) ** n) for S in mats]


def triple_det(v1, v2, v3):
    return float(np.linalg.det(np.column_stack((v1, v2, v3))))


def epsilon_tensor():
    eps = np.zeros((3, 3, 3))
    for p in itertools.permutations(range(3)):
        eps[p[0], p[1], p[2]] = perm_sign(p)
    return eps


def run():
    unique_count = len({tuple(S.reshape(-1).tolist()) for S in mats})
    basis_max = 0.0
    for _ in range(10):
        a, b = rng.normal(size=2)
        v = rng.normal(size=3)
        w = rng.normal(size=3)
        X = compose(a, b, v, w)
        aa, bb, vv, ww = decompose(X)
        X2 = compose(aa, bb, vv, ww)
        basis_max = max(
            basis_max,
            abs(aa - a),
            abs(bb - b),
            float(np.max(np.abs(vv - v))),
            float(np.max(np.abs(ww - w))),
            float(np.max(np.abs(X2 - X))),
        )
    check(
        "S0 generated group and real-basis extraction",
        unique_count == 48
        and len(proper) == 24
        and len(improper) == 24
        and any(np.array_equal(S, P) for S in mats)
        and basis_max < TOL,
        f"unique={unique_count}, proper={len(proper)}, improper={len(improper)}, "
        f"basis_max={basis_max:.3e}",
    )

    a1_max = 0.0
    for R in proper:
        u = su2_lift(R)
        for i in range(3):
            lhs = u @ sigmas[i] @ u.conj().T
            rhs = sum(R[j, i] * sigmas[j] for j in range(3))
            a1_max = max(a1_max, float(np.max(np.abs(lhs - rhs))))
    check(
        "A1 axis-angle SU(2) lift reproduces spatial adjoint",
        a1_max < TOL,
        f"proper_count={len(proper)}, max_err={a1_max:.3e}",
    )

    a2_max = 0.0
    for S in mats:
        d = det3_int(S)
        for _ in range(3):
            a, b = rng.normal(size=2)
            v = rng.normal(size=3)
            w = rng.normal(size=3)
            aa, bb, vv, ww = decompose(full_action(S, compose(a, b, v, w)))
            a2_max = max(
                a2_max,
                abs(aa - a),
                abs(bb - d * b),
                float(np.max(np.abs(vv - S @ v))),
                float(np.max(np.abs(ww - d * (S @ w)))),
            )
    check(
        "A2 content law: even scalar, pseudoscalar, polar vector, axial vector",
        a2_max < TOL,
        f"elements={len(mats)}, draws_per_element=3, max_err={a2_max:.3e}",
    )

    herm_max = 0.0
    pure_max = 0.0
    state_bw_max = 0.0
    for S in mats:
        for _ in range(3):
            a = rng.normal()
            v = rng.normal(size=3)
            X = compose(a, 0.0, v, np.zeros(3))
            Y = full_action(S, X)
            aa, bb, vv, ww = decompose(Y)
            herm_max = max(herm_max, float(np.max(np.abs(Y - Y.conj().T))))
            state_bw_max = max(state_bw_max, abs(bb), float(np.max(np.abs(ww))))

            n = rng.normal(size=3)
            n = n / np.linalg.norm(n)
            rho = (I2 + sigma_dot(n)) / 2.0
            rho2 = full_action(S, rho)
            aa2, bb2, vv2, ww2 = decompose(rho2)
            expected = (I2 + sigma_dot(S @ n)) / 2.0
            pure_max = max(
                pure_max,
                float(np.max(np.abs(rho2 - expected))),
                abs(aa2 - 0.5),
                abs(bb2),
                float(np.max(np.abs(vv2 - (S @ n) / 2.0))),
                float(np.max(np.abs(ww2))),
            )
    check(
        "A3 self-adjoint state content preserves the polar vector law",
        herm_max < TOL and pure_max < TOL and state_bw_max < TOL,
        f"hermitian_max={herm_max:.3e}, pure_state_max={pure_max:.3e}, "
        f"state_b_w_max={state_bw_max:.3e}",
    )

    readout_max = 0.0
    b_flip_max = 0.0
    b_improper_flips = 0
    for S in mats:
        d = det3_int(S)
        for _ in range(3):
            a, b = rng.normal(size=2)
            aa, bb, vv, ww = decompose(
                full_action(S, compose(a, b, np.zeros(3), np.zeros(3)))
            )
            readout = float(np.real(np.trace(compose(aa, bb, vv, ww))) / 2.0)
            readout_max = max(readout_max, abs(readout - a))
            b_flip_max = max(b_flip_max, abs(bb - d * b))
            if d == -1 and abs(bb + b) < TOL:
                b_improper_flips += 1
    readout_even = readout_max < TOL
    check(
        "A4 pseudoscalar coefficient is readout-invisible",
        readout_even and b_flip_max < TOL and b_improper_flips == 3 * len(improper),
        f"readout_max={readout_max:.3e}, b_law_max={b_flip_max:.3e}, "
        f"improper_flips={b_improper_flips}",
    )

    b1_inv_max = 0.0
    for S in mats:
        for _ in range(3):
            v = rng.normal(size=3)
            dvec = rng.normal(size=3)
            before = float(v @ dvec)
            after = float((S @ v) @ (S @ dvec))
            b1_inv_max = max(b1_inv_max, abs(after - before))
    ts = np.array([0.1, 0.2, 0.3, 0.4, 0.5])
    z_dir = np.array([0.0, 0.0, 1.0])
    separating_values = []
    for t in ts:
        v = np.array([0.0, np.sqrt(1.0 - t * t), t])
        separating_values.append(float(v @ z_dir))
    distinct_values = len({round(x, 12) for x in separating_values})
    check(
        "B1 covariant alphabet exceeds the chirality threshold",
        b1_inv_max < TOL and distinct_values == len(separating_values),
        f"joint_invariance_max={b1_inv_max:.3e}, values={separating_values}",
    )

    b2_max = 0.0
    p_values = []
    for t in ts:
        v = np.array([0.0, np.sqrt(1.0 - t * t), t])
        before = float(v @ z_dir)
        after = float((P @ v) @ (P @ z_dir))
        p_values.append(after)
        b2_max = max(b2_max, abs(after - before))
    check(
        "B2 separating values are even under inversion",
        b2_max < TOL and np.allclose(p_values, separating_values, atol=TOL, rtol=0.0),
        f"P_invariance_max={b2_max:.3e}, P_values={p_values}",
    )

    m_v, total_v = sign_multiplicity(vector_power_chars(1), "V")
    m_vv, total_vv = sign_multiplicity(vector_power_chars(2), "V tensor V")
    check(
        "C1 no sign character below vector pairs",
        m_v == 0 and m_vv == 0,
        f"mV={m_v} (sum={total_v}), mVV={m_vv} (sum={total_vv})",
    )

    m_vvv, total_vvv = sign_multiplicity(vector_power_chars(3), "V tensor V tensor V")
    check(
        "C2 vector triple has one sign character",
        m_vvv == 1,
        f"mVVV={m_vvv} (sum={total_vvv})",
    )

    m_dir, total_dir = sign_multiplicity(dir6_vector_power_chars(0), "dir6")
    m_dir_v, total_dir_v = sign_multiplicity(
        dir6_vector_power_chars(1), "dir6 tensor V"
    )
    m_dir_vv, total_dir_vv = sign_multiplicity(
        dir6_vector_power_chars(2), "dir6 tensor V tensor V"
    )
    check(
        "C3 direction alphabet channels first appear at vector pairs",
        m_dir == 0 and m_dir_v == 0 and m_dir_vv == 1,
        f"mDir={m_dir} (sum={total_dir}), mDirV={m_dir_v} "
        f"(sum={total_dir_v}), mDirVV={m_dir_vv} (sum={total_dir_vv})",
    )

    T = rng.normal(size=(3, 3, 3))
    projected = np.zeros((3, 3, 3))
    for S in mats:
        projected += det3_int(S) * np.einsum("ia,jb,kc,abc->ijk", S, S, S, T)
    projected = projected / len(mats)
    eps = epsilon_tensor()
    c = float(np.sum(projected * eps) / np.sum(eps * eps))
    c_err = float(np.max(np.abs(projected - c * eps)))
    check(
        "C4 epsilon uniqueness from projector and permutation signs",
        c_err < TOL and abs(c) > TOL,
        f"c={c:.16g}, max_err={c_err:.3e}",
    )

    b_basis_max = 0.0
    for S in mats:
        aa, bb, vv, ww = decompose(full_action(S, compose(0.0, 1.0, np.zeros(3), np.zeros(3))))
        b_basis_max = max(
            b_basis_max,
            abs(aa),
            abs(bb - det3_int(S)),
            float(np.max(np.abs(vv))),
            float(np.max(np.abs(ww))),
        )
    b_channel_odd = b_basis_max < TOL
    hermitian_b_zero = state_bw_max < TOL
    check(
        "C5 pseudoscalar odd channel is excluded from state readout",
        b_channel_odd and hermitian_b_zero and readout_even,
        f"b_channel_max={b_basis_max:.3e}, hermitian_b_w_max={state_bw_max:.3e}, "
        f"readout_even_max={readout_max:.3e}",
    )

    d1_proper_max = 0.0
    d1_improper_max = 0.0
    for S in mats:
        d = det3_int(S)
        for _ in range(20):
            v1, v2, v3 = rng.normal(size=(3, 3))
            before = triple_det(v1, v2, v3)
            after = triple_det(S @ v1, S @ v2, S @ v3)
            if d == 1:
                d1_proper_max = max(d1_proper_max, abs(after - before))
            else:
                d1_improper_max = max(d1_improper_max, abs(after + before))
    check(
        "D1 content triple product is conjugation-odd",
        d1_proper_max < TOL and d1_improper_max < TOL,
        f"proper_max={d1_proper_max:.3e}, improper_flip_max={d1_improper_max:.3e}",
    )

    d2_invariance_max = 0.0
    d2_real_max = 0.0
    for S in mats:
        d = det3_int(S)
        for _ in range(20):
            v1, v2, v3 = rng.normal(size=(3, 3))
            before = 1j * triple_det(v1, v2, v3)
            raw_after = 1j * triple_det(S @ v1, S @ v2, S @ v3)
            after = np.conjugate(raw_after) if d == -1 else raw_after
            d2_invariance_max = max(d2_invariance_max, abs(after - before))
            d2_real_max = max(d2_real_max, abs(float(np.real(after))))
    check(
        "D2 imaginary triple product is invariant and readout-blind",
        d2_invariance_max < TOL and d2_real_max < TOL,
        f"twisted_invariance_max={d2_invariance_max:.3e}, real_part_max={d2_real_max:.3e}",
    )

    d3_max = 0.0
    e1 = np.array([1.0, 0.0, 0.0])
    e2 = np.array([0.0, 1.0, 0.0])
    e3 = np.array([0.0, 0.0, 1.0])
    for S in mats:
        for _ in range(20):
            v1, v2, v3 = rng.normal(size=(3, 3))
            before = triple_det(e1, e2, e3) * triple_det(v1, v2, v3)
            after = triple_det(S @ e1, S @ e2, S @ e3) * triple_det(
                S @ v1, S @ v2, S @ v3
            )
            d3_max = max(d3_max, abs(after - before))
    check(
        "D3 relative orientation is invariant under all signed permutations",
        d3_max < TOL,
        f"relative_orientation_max={d3_max:.3e}",
    )

    d4_max = 0.0
    d4_min_abs = np.inf
    for _ in range(20):
        v1, v2, v3 = rng.normal(size=(3, 3))
        base_content = triple_det(v1, v2, v3)
        d4_min_abs = min(d4_min_abs, abs(base_content))
        for content_flip, direction_flip in itertools.product((1.0, -1.0), repeat=2):
            content_det = triple_det(content_flip * v1, content_flip * v2, content_flip * v3)
            direction_det = triple_det(direction_flip * e1, direction_flip * e2, direction_flip * e3)
            product_value = content_det * direction_det
            expected_content = content_flip * base_content
            expected_direction = direction_flip
            expected_product = content_flip * direction_flip * base_content
            d4_max = max(
                d4_max,
                abs(content_det - expected_content),
                abs(direction_det - expected_direction),
                abs(product_value - expected_product),
            )
    check(
        "D4 absolute orientation is one bit",
        d4_max < TOL and d4_min_abs > TOL,
        f"four_combinations=20, max_err={d4_max:.3e}, min_abs_triple={d4_min_abs:.3e}",
    )

    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")


if __name__ == "__main__":
    run()
