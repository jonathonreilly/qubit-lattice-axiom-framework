#!/usr/bin/env python3
"""Exact algebraic and Fock-space controls for the U(5) three-plus-two FMS
projector calculus and native determinant-square stabilizer carrier note.

All calculations use exact rational (fractions.Fraction) and integer bitmask
arithmetic. General proofs are in the paired theorem note; these finite
controls verify every operator identity, noncommuting CAR relation, Lie-algebra
centralizer dimension, and link-register commutator on explicit noncommuting
representations without sampling or floating-point approximations.
"""
from fractions import Fraction as Q
from itertools import combinations, permutations
from pathlib import Path
import hashlib

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/U5_THREE_PLUS_TWO_FMS_PROJECTOR_CARRIER_BOUNDED_THEOREM_NOTE_2026-11-09.md",
)

PASS_COUNT = 0


def check(name: str, condition: bool) -> None:
    global PASS_COUNT
    if not condition:
        raise AssertionError(name)
    PASS_COUNT += 1
    print(f"PASS: {name}")


# ---------------------------------------------------------------------------
# Exact Gaussian rational Q(i) and matrix algebra utilities
# ---------------------------------------------------------------------------


class Qi:
    """Exact Gaussian rational a + b*i with a, b in fractions.Fraction."""

    __slots__ = ("re", "im")

    def __init__(self, re=0, im=0):
        self.re = re if isinstance(re, Q) else Q(re)
        self.im = im if isinstance(im, Q) else Q(im)

    def __add__(self, other):
        other = other if isinstance(other, Qi) else Qi(other)
        return Qi(self.re + other.re, self.im + other.im)

    def __radd__(self, other):
        return self.__add__(other)

    def __sub__(self, other):
        other = other if isinstance(other, Qi) else Qi(other)
        return Qi(self.re - other.re, self.im - other.im)

    def __rsub__(self, other):
        other = other if isinstance(other, Qi) else Qi(other)
        return other.__sub__(self)

    def __neg__(self):
        return Qi(-self.re, -self.im)

    def __mul__(self, other):
        other = other if isinstance(other, Qi) else Qi(other)
        return Qi(
            self.re * other.re - self.im * other.im,
            self.re * other.im + self.im * other.re,
        )

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        other = other if isinstance(other, Qi) else Qi(other)
        denom = other.re * other.re + other.im * other.im
        if denom == 0:
            raise ZeroDivisionError("division by zero in Qi")
        return Qi(
            (self.re * other.re + self.im * other.im) / denom,
            (self.im * other.re - self.re * other.im) / denom,
        )

    def conj(self):
        return Qi(self.re, -self.im)

    def __eq__(self, other):
        if isinstance(other, Qi):
            return self.re == other.re and self.im == other.im
        return self.re == Q(other) and self.im == 0

    def __repr__(self):
        if self.im == 0:
            return f"{self.re}"
        return f"({self.re}+{self.im}i)"


ZERO = Qi(0, 0)
ONE = Qi(1, 0)
IMAG = Qi(0, 1)


def mat_zero(n: int, m: int | None = None):
    if m is None:
        m = n
    return [[ZERO for _ in range(m)] for _ in range(n)]


def mat_eye(n: int):
    out = mat_zero(n)
    for i in range(n):
        out[i][i] = ONE
    return out


def mat_add(a, b):
    return [[x + y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def mat_sub(a, b):
    return [[x - y for x, y in zip(ra, rb)] for ra, rb in zip(a, b)]


def mat_scale(c, a):
    c = c if isinstance(c, Qi) else Qi(c)
    return [[c * x for x in row] for row in a]


def mat_mul(a, b):
    n = len(a)
    k = len(b)
    m = len(b[0])
    out = mat_zero(n, m)
    for i in range(n):
        for r in range(k):
            air = a[i][r]
            if air != ZERO:
                for j in range(m):
                    if b[r][j] != ZERO:
                        out[i][j] = out[i][j] + air * b[r][j]
    return out


def mat_adj(a):
    n = len(a)
    m = len(a[0])
    return [[a[i][j].conj() for i in range(n)] for j in range(m)]


def mat_eq(a, b) -> bool:
    return all(x == y for ra, rb in zip(a, b) for x, y in zip(ra, rb))


def mat_comm(a, b):
    return mat_sub(mat_mul(a, b), mat_mul(b, a))


def mat_kron(a, b):
    na, ma = len(a), len(a[0])
    nb, mb = len(b), len(b[0])
    out = mat_zero(na * nb, ma * mb)
    for i in range(na):
        for j in range(ma):
            aij = a[i][j]
            if aij != ZERO:
                for p in range(nb):
                    for q in range(mb):
                        out[i * nb + p][j * mb + q] = aij * b[p][q]
    return out


def partial_trace_internal(m, d_alg: int, d_int: int):
    """Return Tr_{M_{d_int}}(m) as a d_alg x d_alg matrix."""
    out = mat_zero(d_alg)
    for i in range(d_alg):
        for j in range(d_alg):
            s = ZERO
            for alpha in range(d_int):
                s = s + m[i * d_int + alpha][j * d_int + alpha]
            out[i][j] = s
    return out


def internal_hs_square(m, d_alg: int, d_int: int):
    """Return |m|_{HS}^2 = Tr_{M_{d_int}}(m^* m) in M_{d_alg}."""
    return partial_trace_internal(mat_mul(mat_adj(m), m), d_alg, d_int)


def mat_tr(m):
    return sum((m[i][i] for i in range(len(m))), ZERO)


def pauli_matrices():
    s1 = [[ZERO, ONE], [ONE, ZERO]]
    s2 = [[ZERO, -IMAG], [IMAG, ZERO]]
    s3 = [[ONE, ZERO], [ZERO, -ONE]]
    return s1, s2, s3


# ---------------------------------------------------------------------------
# 1. Theorem 1 controls: noncommuting SU(2) adjoint projector defect & strings
# ---------------------------------------------------------------------------


def theorem1_su2_projector_controls() -> None:
    sigma1 = [[ZERO, ONE], [ONE, ZERO]]
    sigma2 = [[ZERO, -IMAG], [IMAG, ZERO]]
    sigma3 = [[ONE, ZERO], [ZERO, -ONE]]
    sigmas = (sigma1, sigma2, sigma3)
    eye2 = mat_eye(2)

    # Noncommuting self-adjoint operators Phi^1, Phi^2, Phi^3 in M_3(Q(i))
    # with non-spherical sum_a (Phi^a)^2 != r^2 I_3 and nonvanishing commutators.
    phi1 = [
        [Qi(1), Qi(1, 1), Qi(0)],
        [Qi(1, -1), Qi(-1), Qi(1, 0)],
        [Qi(0), Qi(1, 0), Qi(2)],
    ]
    phi2 = [
        [Qi(0), Qi(0, -1), Qi(1)],
        [Qi(0, 1), Qi(2), Qi(0, 1)],
        [Qi(1), Qi(0, -1), Qi(-1)],
    ]
    phi3 = [
        [Qi(2), Qi(1, 0), Qi(0, -1)],
        [Qi(1, 0), Qi(0), Qi(1, 1)],
        [Qi(0, 1), Qi(1, -1), Qi(-2)],
    ]
    phis = (phi1, phi2, phi3)
    d_alg = 3
    eye_alg = mat_eye(d_alg)
    eye_full = mat_kron(eye_alg, eye2)

    check(
        "Theorem 1 input operators are self-adjoint and mutually noncommuting",
        all(mat_eq(p, mat_adj(p)) for p in phis)
        and not mat_eq(mat_comm(phi1, phi2), mat_zero(d_alg))
        and not mat_eq(mat_comm(phi2, phi3), mat_zero(d_alg))
        and not mat_eq(mat_comm(phi3, phi1), mat_zero(d_alg)),
    )

    r = Q(3, 2)
    a_op = mat_zero(d_alg * 2)
    for phi_a, sig_a in zip(phis, sigmas):
        a_op = mat_add(a_op, mat_kron(phi_a, sig_a))

    p_plus = mat_scale(Q(1, 2), mat_add(eye_full, mat_scale(Q(1) / r, a_op)))
    p_minus = mat_scale(Q(1, 2), mat_sub(eye_full, mat_scale(Q(1) / r, a_op)))

    defect_plus = mat_sub(mat_mul(p_plus, p_plus), p_plus)
    defect_minus = mat_sub(mat_mul(p_minus, p_minus), p_minus)
    prod_pm = mat_mul(p_plus, p_minus)
    prod_mp = mat_mul(p_minus, p_plus)
    a2_minus_r2 = mat_sub(mat_mul(a_op, a_op), mat_scale(r * r, eye_full))
    rhs_defect = mat_scale(Q(1) / (4 * r * r), a2_minus_r2)

    check(
        "Theorem 1(1) resolution and P_+^2 - P_+ = P_-^2 - P_- = -P_+ P_- = (A^2 - r^2 I)/(4 r^2)",
        mat_eq(mat_add(p_plus, p_minus), eye_full)
        and mat_eq(partial_trace_internal(p_plus, d_alg, 2), eye_alg)
        and mat_eq(partial_trace_internal(p_minus, d_alg, 2), eye_alg)
        and mat_eq(defect_plus, rhs_defect)
        and mat_eq(defect_minus, rhs_defect)
        and mat_eq( mat_scale(-1, prod_pm), rhs_defect)
        and mat_eq(mat_scale(-1, prod_mp), rhs_defect),
    )

    # Radial and commutator defect components R_r and C_c
    r_op = mat_scale(-r * r, eye_alg)
    for phi_a in phis:
        r_op = mat_add(r_op, mat_mul(phi_a, phi_a))
    c1 = mat_scale(IMAG, mat_comm(phi2, phi3))
    c2 = mat_scale(IMAG, mat_comm(phi3, phi1))
    c3 = mat_scale(IMAG, mat_comm(phi1, phi2))
    cs = (c1, c2, c3)

    decomp = mat_kron(r_op, eye2)
    for c_op, sig_c in zip(cs, sigmas):
        decomp = mat_add(decomp, mat_kron(c_op, sig_c))

    check(
        "Theorem 1(1) Pauli expansion A^2 - r^2 I = R_r x I_2 + sum_c C_c x sigma_c",
        mat_eq(a2_minus_r2, decomp),
    )

    # Internal Hilbert-Schmidt square identity
    hs_direct = internal_hs_square(a2_minus_r2, d_alg, 2)
    comm_sq_sum = mat_zero(d_alg)
    for phi_a in phis:
        for phi_b in phis:
            comm_ab = mat_comm(phi_a, phi_b)
            comm_sq_sum = mat_add(comm_sq_sum, mat_mul(mat_adj(comm_ab), comm_ab))
    hs_formula = mat_add(mat_scale(2, mat_mul(r_op, r_op)), comm_sq_sum)

    check(
        "Theorem 1(2) exact operator identity |A^2 - r^2 I|_HS^2 = 2 R_r^2 + sum_{a,b} |[Phi^a, Phi^b]|^2",
        mat_eq(hs_direct, hs_formula),
    )

    # State-L^2 equality on a faithful mixed state omega(X) = sum_k w_k X_{kk}
    weights = (Q(1, 2), Q(1, 3), Q(1, 6))

    def omega(op):
        return sum(Qi(weights[k]) * op[k][k] for k in range(d_alg))

    lhs_state = omega(internal_hs_square(defect_plus, d_alg, 2))
    rhs_state = (
        Qi(Q(1) / (8 * r**4)) * omega(mat_mul(r_op, r_op))
        + Qi(Q(1) / (16 * r**4)) * omega(comm_sq_sum)
    )
    check(
        "Theorem 1(2) state-L^2 equality with zero radial-commutator cross term",
        lhs_state == rhs_state and lhs_state.re > 0 and lhs_state.im == 0,
    )

    # Theorem 1(3): Exact SU(2)_X x SU(2)_Y gauge invariance and 4-channel sum
    # Use exact rational SU(2) matrices g = (a I_2 + i b_c sigma_c) with a^2 + b^2 = 1.
    # Specifically, Pythagorean quaternion (3/5, 4/5, 0, 0) and (5/13, 0, 12/13, 0).
    gx = [[Qi(Q(3, 5), Q(0)), Qi(Q(0), Q(4, 5))], [Qi(Q(0), Q(4, 5)), Qi(Q(3, 5), Q(0))]]
    gy = [[Qi(Q(5, 13), Q(0)), Qi(Q(12, 13), Q(0))], [Qi(Q(-12, 13), Q(0)), Qi(Q(5, 13), Q(0))]]
    check(
        "Exact rational SU(2) test elements gx, gy are unitary with determinant 1",
        mat_eq(mat_mul(mat_adj(gx), gx), eye2)
        and mat_eq(mat_mul(mat_adj(gy), gy), eye2)
        and (gx[0][0] * gx[1][1] - gx[0][1] * gx[1][0]) == ONE
        and (gy[0][0] * gy[1][1] - gy[0][1] * gy[1][0]) == ONE,
    )

    def adjoint_rot(g, phi_tuple):
        # Compute Ad_g^{ab} = (1/2) Tr(sigma_a g sigma_b g^*)
        out = []
        for a in range(3):
            comb = mat_zero(d_alg)
            for b in range(3):
                prod_mat = mat_mul(sigmas[a], mat_mul(g, mat_mul(sigmas[b], mat_adj(g))))
                coeff = (prod_mat[0][0] + prod_mat[1][1]) / Qi(2)
                comb = mat_add(comb, mat_scale(coeff, phi_tuple[b]))
            out.append(comb)
        return tuple(out)

    # Distinct composite tuple at Y, non-unitary link transporter U_{XY}, and doublets Psi_X, Psi_Y
    phis_y = (phi2, phi3, phi1)
    a_op_y = mat_zero(d_alg * 2)
    for phi_a, sig_a in zip(phis_y, sigmas):
        a_op_y = mat_add(a_op_y, mat_kron(phi_a, sig_a))
    py_plus = mat_scale(Q(1, 2), mat_add(eye_full, mat_scale(Q(1) / r, a_op_y)))
    py_minus = mat_scale(Q(1, 2), mat_sub(eye_full, mat_scale(Q(1) / r, a_op_y)))

    # Non-unitary transporter U_{XY} in M_3 x M_2 and endpoint doublets Psi_X, Psi_Y in M_3 x C^2
    u_xy = mat_add(mat_kron(phi1, eye2), mat_kron(phi2, sigma1))
    psi_x = [[ ZERO for _ in range(d_alg)] for _ in range(d_alg * 2)]
    psi_y = [[ZERO for _ in range(d_alg)] for _ in range(d_alg * 2)]
    for i in range(d_alg):
        for j in range(d_alg):
            psi_x[i * 2 + 0][j] = phi1[i][j]
            psi_x[i * 2 + 1][j] = phi3[i][j]
            psi_y[i * 2 + 0][j] = phi2[i][j]
            psi_y[i * 2 + 1][j] = phi1[i][j]

    # Transform Phi_X, Phi_Y, U_{XY}, Psi_X, Psi_Y under (gx, gy)
    phis_x_rot = adjoint_rot(gx, phis)
    phis_y_rot = adjoint_rot(gy, phis_y)
    a_x_rot = mat_zero(d_alg * 2)
    a_y_rot = mat_zero(d_alg * 2)
    for phi_a, sig_a in zip(phis_x_rot, sigmas):
        a_x_rot = mat_add(a_x_rot, mat_kron(phi_a, sig_a))
    for phi_a, sig_a in zip(phis_y_rot, sigmas):
        a_y_rot = mat_add(a_y_rot, mat_kron(phi_a, sig_a))
    px_plus_rot = mat_scale(Q(1, 2), mat_add(eye_full, mat_scale(Q(1) / r, a_x_rot)))
    px_minus_rot = mat_scale(Q(1, 2), mat_sub(eye_full, mat_scale(Q(1) / r, a_x_rot)))
    py_plus_rot = mat_scale(Q(1, 2), mat_add(eye_full, mat_scale(Q(1) / r, a_y_rot)))
    py_minus_rot = mat_scale(Q(1, 2), mat_sub(eye_full, mat_scale(Q(1) / r, a_y_rot)))

    gx_full = mat_kron(eye_alg, gx)
    gy_full = mat_kron(eye_alg, gy)
    u_xy_rot = mat_mul(gx_full, mat_mul(u_xy, mat_adj(gy_full)))
    psi_x_rot = mat_mul(gx_full, psi_x)
    psi_y_rot = mat_mul(gy_full, psi_y)

    channels = []
    channels_rot = []
    for px, px_r in ((p_plus, px_plus_rot), (p_minus, px_minus_rot)):
        for py, py_r in ((py_plus, py_plus_rot), (py_minus, py_minus_rot)):
            s_op = mat_mul(mat_adj(psi_x), mat_mul(px, mat_mul(u_xy, mat_mul(py, psi_y))))
            s_op_rot = mat_mul(
                mat_adj(psi_x_rot), mat_mul(px_r, mat_mul(u_xy_rot, mat_mul(py_r, psi_y_rot)))
            )
            channels.append(s_op)
            channels_rot.append(s_op_rot)

    total_channel = mat_zero(d_alg)
    for ch in channels:
        total_channel = mat_add(total_channel, ch)
    unprojected = mat_mul(mat_adj(psi_x), mat_mul(u_xy, psi_y))

    check(
        "Theorem 1(3) four projected strings are SU(2)_X x SU(2)_Y invariant and sum to Psi_X^* U_{XY} Psi_Y",
        all(mat_eq(ch, ch_r) for ch, ch_r in zip(channels, channels_rot))
        and mat_eq(total_channel, unprojected),
    )


# ---------------------------------------------------------------------------
# 2. Theorem 2 controls: U(5) 3+2 projectors, CAR bilinear C^2=(6-n)C, rank witness
# ---------------------------------------------------------------------------


def fermion_sign(mask: int, mode: int) -> int:
    """Return (-1)^(# occupied modes strictly below `mode` in `mask`)."""
    lower = mask & ((1 << mode) - 1)
    return -1 if (lower.bit_count() & 1) else 1


def theorem2_u5_projector_and_car_controls() -> None:
    a_val = Q(-2)
    b_val = Q(3)
    gap = a_val - b_val  # -5
    eye5 = mat_eye(5)

    # First check polynomial identities on a generic self-adjoint 5x5 matrix with off-diagonal entries
    h5 = [
        [Qi(-2), Qi(1, 1), Qi(0), Qi(1, 0), Qi(0)],
        [Qi(1, -1), Qi(-2), Qi(1), Qi(0), Qi(0, 1)],
        [Qi(0), Qi(1), Qi(-2), Qi(0, -1), Qi(1)],
        [Qi(1, 0), Qi(0), Qi(0, 1), Qi(3), Qi(2)],
        [Qi(0), Qi(0, -1), Qi(1), Qi(2), Qi(3)],
    ]
    p3 = mat_scale(Q(1) / gap, mat_sub(h5, mat_scale(b_val, eye5)))
    p2 = mat_scale(Q(1) / gap, mat_sub(mat_scale(a_val, eye5), h5))
    defect_p3 = mat_sub(mat_mul(p3, p3), p3)
    defect_p2 = mat_sub(mat_mul(p2, p2), p2)
    rhs_quad = mat_scale(
        Q(1) / (gap * gap),
        mat_mul(mat_sub(h5, mat_scale(a_val, eye5)), mat_sub(h5, mat_scale(b_val, eye5))),
    )
    tr_p3 = sum((p3[i][i] for i in range(5)), ZERO)
    tr_p2 = sum((p2[i][i] for i in range(5)), ZERO)

    # Also test a shifted matrix h5_shifted = h5 + I_5 with nonzero trace residual Tr(A) - (3a+2b) = 5
    h5_shifted = mat_add(h5, eye5)
    p3_shifted = mat_scale(Q(1) / gap, mat_sub(h5_shifted, mat_scale(b_val, eye5)))
    p2_shifted = mat_scale(Q(1) / gap, mat_sub(mat_scale(a_val, eye5), h5_shifted))
    tr_h5_shifted = sum((h5_shifted[i][i] for i in range(5)), ZERO)
    tr_p3_shifted = sum((p3_shifted[i][i] for i in range(5)), ZERO)
    tr_p2_shifted = sum((p2_shifted[i][i] for i in range(5)), ZERO)
    expected_p3_res = (tr_h5_shifted - Qi(3 * a_val + 2 * b_val)) / Qi(gap)

    check(
        "Theorem 2(1) U(5) 3+2 resolution, quadratic defect (A-aI)(A-bI)/(a-b)^2, and trace identities",
        mat_eq(mat_add(p3, p2), eye5)
        and mat_eq(mat_add(mat_scale(a_val, p3), mat_scale(b_val, p2)), h5)
        and mat_eq(defect_p3, rhs_quad)
        and mat_eq(defect_p2, rhs_quad)
        and mat_eq(mat_scale(-1, mat_mul(p3, p2)), rhs_quad)
        and tr_p3 == Qi(3)
        and tr_p2 == Qi(2)
        and expected_p3_res != ZERO
        and (tr_p3_shifted - Qi(3)) == expected_p3_res
        and (tr_p2_shifted - Qi(2)) == -expected_p3_res,
    )

    # Theorem 2(2): Exact 5-flavor CAR algebra on Lambda(C^5) (dim = 32)
    # Verify C^2 = (6 I - N) C and (P_CAR^{(n)})^2 = P_CAR^{(n)} on every sector n = 0..5.
    for n in range(6):
        basis = [mask for mask in range(32) if mask.bit_count() == n]
        idx_of = {mask: idx for idx, mask in enumerate(basis)}
        d_sec = len(basis)

        # Build C in End(Lambda^n C^5) x M_5(C) of size (5 * d_sec) x (5 * d_sec)
        # Entry (i, k) in M_5 is c_i^dagger c_k on Lambda^n C^5.
        c_op = [[Q(0) for _ in range(5 * d_sec)] for _ in range(5 * d_sec)]
        for i in range(5):
            for k in range(5):
                for col_s, mask in enumerate(basis):
                    if not (mask & (1 << k)):
                        continue
                    s1 = fermion_sign(mask, k)
                    mask1 = mask ^ (1 << k)
                    if mask1 & (1 << i):
                        continue
                    s2 = fermion_sign(mask1, i)
                    mask2 = mask1 | (1 << i)
                    row_s = idx_of[mask2]
                    c_op[row_s * 5 + i][col_s * 5 + k] += Q(s1 * s2)

        # Compute C^2 by exact rational matrix multiplication
        dim_total = 5 * d_sec
        c_sq = [[Q(0) for _ in range(dim_total)] for _ in range(dim_total)]
        for r_idx in range(dim_total):
            for m_idx in range(dim_total):
                val = c_op[r_idx][m_idx]
                if val != 0:
                    for c_idx in range(dim_total):
                        if c_op[m_idx][c_idx] != 0:
                            c_sq[r_idx][c_idx] += val * c_op[m_idx][c_idx]

        expected_c_sq = [
            [Q(6 - n) * c_op[r_idx][c_idx] for c_idx in range(dim_total)]
            for r_idx in range(dim_total)
        ]

        # Internal trace Tr_{M_5}(C) on Lambda^n C^5
        tr_c = [[Q(0) for _ in range(d_sec)] for _ in range(d_sec)]
        for s_r in range(d_sec):
            for s_c in range(d_sec):
                tr_c[s_r][s_c] = sum(c_op[s_r * 5 + i][s_c * 5 + i] for i in range(5))
        expected_tr_c = [
            [Q(n) if s_r == s_c else Q(0) for s_c in range(d_sec)] for s_r in range(d_sec)
        ]

        if n >= 1:
            scale = Q(1, 6 - n)
            p_car = [[scale * x for x in row] for row in c_op]
            p_car_sq = [[scale * scale * x for x in row] for row in c_sq]
            tr_p_car = [[scale * x for x in row] for row in tr_c]
            expected_tr_p = [
                [Q(n, 6 - n) if s_r == s_c else Q(0) for s_c in range(d_sec)]
                for s_r in range(d_sec)
            ]
            check(
                f"Theorem 2(2) 5-mode CAR sector n={n} (dim={d_sec}): C^2={6-n}C, P_CAR^2=P_CAR, Tr(P_CAR)={Q(n, 6-n)} I",
                c_sq == expected_c_sq
                and p_car_sq == p_car
                and tr_p_car == expected_tr_p,
            )
        else:
            check(
                "Theorem 2(2) 5-mode CAR vacuum sector n=0 (dim=1): C=0 and C^2=6C",
                c_sq == expected_c_sq and tr_c == expected_tr_c,
            )

    # Theorem 2(3): Rank-separation witness A_mix = (A_(4), A_(2)) and joint defect D_{3+2}
    strata_defects = []
    for k in range(6):
        diag_k = [a_val if m < k else b_val for m in range(5)]
        quad_k = sum(((lam - a_val) ** 2) * ((lam - b_val) ** 2) / (gap**4) for lam in diag_k)
        tr_k = sum((lam - b_val) / gap for lam in diag_k)
        d32_k = quad_k + (tr_k - 3) ** 2
        strata_defects.append((quad_k, tr_k, d32_k))

    # Witness A_mix = (A_(4), A_(2)) under omega_mix = (1/2, 1/2)
    quad_mix = Q(1, 2) * strata_defects[4][0] + Q(1, 2) * strata_defects[2][0]
    mean_tr_defect_mix = Q(1, 2) * (strata_defects[4][1] - 3) + Q(1, 2) * (strata_defects[2][1] - 3)
    d32_mix = Q(1, 2) * strata_defects[4][2] + Q(1, 2) * strata_defects[2][2]

    check(
        "Theorem 2(3) rank-separation witness A_mix=(A_(4),A_(2)) and D_{3+2}(A_(k))=(k-3)^2",
        all(strata_defects[k] == (Q(0), Q(k), Q((k - 3) ** 2)) for k in range(6))
        and quad_mix == 0
        and mean_tr_defect_mix == 0
        and d32_mix == 1,
    )


# ---------------------------------------------------------------------------
# 3. Theorem 3 controls: Spin(10)/so(10) 6+4 projectors, J_A factorization, centralizer
# ---------------------------------------------------------------------------


def rational_rank(matrix_rows: list[list[Q]]) -> int:
    """Compute the exact rank over Q of a rectangular matrix by Gaussian elimination."""
    if not matrix_rows or not matrix_rows[0]:
        return 0
    rows = [list(map(Q, r)) for r in matrix_rows]
    n_rows = len(rows)
    n_cols = len(rows[0])
    rank = 0
    for col in range(n_cols):
        pivot = None
        for r in range(rank, n_rows):
            if rows[r][col] != 0:
                pivot = r
                break
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        piv_val = rows[rank][col]
        rows[rank] = [x / piv_val for x in rows[rank]]
        for r in range(n_rows):
            if r != rank and rows[r][col] != 0:
                factor = rows[r][col]
                rows[r] = [x - factor * y for x, y in zip(rows[r], rows[rank])]
        rank += 1
        if rank == n_rows:
            break
    return rank


def theorem3_orthogonal_projector_and_centralizer_controls() -> None:
    a_val = Q(-2)
    b_val = Q(3)
    a2_minus_b2 = a_val * a_val - b_val * b_val  # 4 - 9 = -5
    eye10 = [[Q(1) if i == j else Q(0) for j in range(10)] for i in range(10)]

    def rmat_add(x, y):
        return [[u + v for u, v in zip(rx, ry)] for rx, ry in zip(x, y)]

    def rmat_sub(x, y):
        return [[u - v for u, v in zip(rx, ry)] for rx, ry in zip(x, y)]

    def rmat_scale(c: Q, x):
        return [[c * u for u in rx] for rx in x]

    def rmat_mul(x, y):
        n = len(x)
        out = [[Q(0) for _ in range(n)] for _ in range(n)]
        for i in range(n):
            for k in range(n):
                if x[i][k] != 0:
                    for j in range(n):
                        out[i][j] += x[i][k] * y[k][j]
        return out

    # Build a generic skew-symmetric 10x10 matrix A in so(10) off the classical orbit
    a_skew = [[Q(0) for _ in range(10)] for _ in range(10)]
    for b_idx in range(5):
        coeff = a_val if b_idx < 3 else b_val
        a_skew[2 * b_idx][2 * b_idx + 1] = -coeff
        a_skew[2 * b_idx + 1][2 * b_idx] = coeff
    # Add skew-symmetric off-block perturbations so Q_6(A)^2 - Q_6(A) != 0
    perturb_pairs = ((0, 6, Q(1, 2)), (1, 7, Q(-1, 3)), (2, 8, Q(1, 4)), (4, 9, Q(2, 5)))
    for i, j, val in perturb_pairs:
        a_skew[i][j] += val
        a_skew[j][i] -= val

    a2 = rmat_mul(a_skew, a_skew)
    q6 = rmat_scale(
        Q(1) / a2_minus_b2,
        rmat_sub(rmat_scale(Q(-1), a2), rmat_scale(b_val * b_val, eye10)),
    )
    q4 = rmat_sub(eye10, q6)
    j_a = rmat_mul(
        a_skew, rmat_add(rmat_scale(Q(1) / a_val, q6), rmat_scale(Q(1) / b_val, q4))
    )

    d_q6 = rmat_sub(rmat_mul(q6, q6), q6)
    rhs_d_q6 = rmat_scale(
        Q(1) / (a2_minus_b2 * a2_minus_b2),
        rmat_mul(
            rmat_add(a2, rmat_scale(a_val * a_val, eye10)),
            rmat_add(a2, rmat_scale(b_val * b_val, eye10)),
        ),
    )

    check(
        "Theorem 3(1) orthogonal Q_6, Q_4 commutation with A and quartic defect identity",
        rmat_mul(a_skew, q6) == rmat_mul(q6, a_skew)
        and rmat_mul(a_skew, j_a) == rmat_mul(j_a, a_skew)
        and d_q6 == rhs_d_q6
        and d_q6 != [[Q(0) for _ in range(10)] for _ in range(10)],
    )

    # Theorem 3(2): Exact polynomial factorizations of J_A^2 + I_10 and A - (a Q_6 + b Q_4) J_A
    ja_sq_plus_eye = rmat_add(rmat_mul(j_a, j_a), eye10)
    prefactor = rmat_scale(
        Q(1) / (a_val * a_val * b_val * b_val),
        rmat_add(
            rmat_scale((a_val - b_val) ** 2, a2),
            rmat_scale(a2_minus_b2**2, eye10),
        ),
    )
    rhs_ja_defect = rmat_mul(prefactor, d_q6)

    recon_lhs = rmat_sub(
        a_skew,
        rmat_mul(rmat_add(rmat_scale(a_val, q6), rmat_scale(b_val, q4)), j_a),
    )
    recon_rhs = rmat_scale(
        ((a_val - b_val) ** 2) / (a_val * b_val),
        rmat_mul(a_skew, d_q6),
    )

    check(
        "Theorem 3(2) exact factorizations of J_A^2 + I_10 and A - (a Q_6 + b Q_4) J_A through Q_6^2 - Q_6",
        ja_sq_plus_eye == rhs_ja_defect and recon_lhs == recon_rhs,
    )

    # Theorem 3(3): Centralizer dimensions in so(10) (dim = 45)
    a0_orth = [[Q(0) for _ in range(10)] for _ in range(10)]
    for b_idx in range(5):
        coeff = a_val if b_idx < 3 else b_val
        a0_orth[2 * b_idx][2 * b_idx + 1] = -coeff
        a0_orth[2 * b_idx + 1][2 * b_idx] = coeff
    a0_sq = rmat_mul(a0_orth, a0_orth)
    q6_0 = rmat_scale(
        Q(1) / a2_minus_b2,
        rmat_sub(rmat_scale(Q(-1), a0_sq), rmat_scale(b_val * b_val, eye10)),
    )
    q4_0 = rmat_sub(eye10, q6_0)
    ja_0 = rmat_mul(
        a0_orth, rmat_add(rmat_scale(Q(1) / a_val, q6_0), rmat_scale(Q(1) / b_val, q4_0))
    )

    # Build the 45 basis matrices E_{pq} - E_{qp} (0 <= p < q < 10) of so(10)
    so10_basis = []
    for p in range(10):
        for q in range(p + 1, 10):
            b_mat = [[Q(0) for _ in range(10)] for _ in range(10)]
            b_mat[p][q] = Q(1)
            b_mat[q][p] = Q(-1)
            so10_basis.append(b_mat)

    def flatten(m):
        return [m[i][j] for i in range(10) for j in range(10)]

    # Linear map X -> [X, Q_6(A_0)]
    cols_q6 = [flatten(rmat_sub(rmat_mul(b_mat, q6_0), rmat_mul(q6_0, b_mat))) for b_mat in so10_basis]
    rank_q6 = rational_rank([ [cols_q6[col][row] for col in range(45)] for row in range(100) ])
    dim_cent_real = 45 - rank_q6

    # Linear map X -> ([X, Q_6(A_0)], [X, J_{A_0}])
    cols_joint = [
        flatten(rmat_sub(rmat_mul(b_mat, q6_0), rmat_mul(q6_0, b_mat)))
        + flatten(rmat_sub(rmat_mul(b_mat, ja_0), rmat_mul(ja_0, b_mat)))
        for b_mat in so10_basis
    ]
    rank_joint = rational_rank([[cols_joint[col][row] for col in range(45)] for row in range(200)])
    dim_cent_joint = 45 - rank_joint

    # Linear map X -> [X, A_0^orth]
    cols_a0 = [flatten(rmat_sub(rmat_mul(b_mat, a0_orth), rmat_mul(a0_orth, b_mat))) for b_mat in so10_basis]
    rank_a0 = rational_rank([[cols_a0[col][row] for col in range(45)] for row in range(100)])
    dim_cent_a0 = 45 - rank_a0

    check(
        "Theorem 3(3) centralizer dimensions in so(10): dim so(10)=45, dim cent(Q_6)=21, dim cent(Q_6, J_A)=dim cent(A_0)=13",
        len(so10_basis) == 45
        and dim_cent_real == 21
        and dim_cent_joint == 13
        and dim_cent_a0 == 13,
    )


# ---------------------------------------------------------------------------
# 4. Theorem 4 controls: H = S(U(3)xU(2)) = (SU(3)xSU(2)xU(1))/Z_6 and K_{U(5)} = H{+-I_5}
# ---------------------------------------------------------------------------


def theorem4_stabilizer_and_z6_kernel_controls() -> None:
    # Work in the exact cyclotomic ring Q[zeta_6] where zeta_6^2 - zeta_6 + 1 = 0
    # Represent elements as (a, b) = a + b * zeta_6 with a, b in Q.
    def z6_mul(x, y):
        # (a + b z)(c + d z) = a c + (a d + b c) z + b d (z - 1) = (ac - bd) + (ad + bc + bd) z
        a, b = x
        c, d = y
        return (a * c - b * d, a * d + b * c + b * d)

    def z6_pow(x, k: int):
        res = (Q(1), Q(0))
        for _ in range(k):
            res = z6_mul(res, x)
        return res

    zeta6 = (Q(0), Q(1))  # e^{i pi / 3}
    omega3 = z6_pow(zeta6, 2)  # e^{2 pi i / 3} = -1 + zeta_6
    minus1 = z6_pow(zeta6, 3)  # -1

    # Verify the 6 powers of gamma_6 = (omega3 I_3, -I_2, zeta_6) and the homomorphism pi
    kernel_elements = []
    for k in range(6):
        u3_scalar = z6_pow(omega3, k)
        u2_scalar = z6_pow(minus1, k)
        z_scalar = z6_pow(zeta6, k)
        # In pi(U_3, U_2, z) = diag(z^{-2} U_3, z^3 U_2), note z^{-2} = z^4 and z^3:
        block3_scalar = z6_mul(z6_pow(z_scalar, 4), u3_scalar)
        block2_scalar = z6_mul(z6_pow(z_scalar, 3), u2_scalar)
        # Also verify det(U_3) = u3_scalar^3 = 1 and det(U_2) = u2_scalar^2 = 1
        det_u3 = z6_pow(u3_scalar, 3)
        det_u2 = z6_pow(u2_scalar, 2)
        kernel_elements.append((u3_scalar, u2_scalar, z_scalar, block3_scalar, block2_scalar, det_u3, det_u2))

    distinct_triples = {(e[0], e[1], e[2]) for e in kernel_elements}
    check(
        "Theorem 4(1) Z_6 kernel of pi: 6 distinct triples in SU(3)xSU(2)xU(1) all mapping to I_3 (+) I_2",
        len(distinct_triples) == 6
        and all(
            e[3] == (Q(1), Q(0))
            and e[4] == (Q(1), Q(0))
            and e[5] == (Q(1), Q(0))
            and e[6] == (Q(1), Q(0))
            for e in kernel_elements
        ),
    )

    # Check the two connected components of K_{U(5)} = H{+-I_5} and exclusion of det g = i
    # Represent test diagonal elements g = diag(d_1,...,d_5) in U(3) x U(2) with entries in Q(i)
    g_plus = [ONE, ONE, ONE, -ONE, -ONE]       # in H: det = +1, det^2 = +1
    g_minus = [-ONE, -ONE, -ONE, -ONE, -ONE]   # -I_5 in (-I_5)H: det = -1, det^2 = +1
    g_quarter = [IMAG, ONE, ONE, ONE, ONE]     # in U(3)xU(2) \ K_{U(5)}: det = i, det^2 = -1

    def det_diag(diag_entries):
        res = ONE
        for d in diag_entries:
            res = res * d
        return res

    det_plus = det_diag(g_plus)
    det_minus = det_diag(g_minus)
    det_quarter = det_diag(g_quarter)

    # Product (-I_5) * g_minus lies in H
    g_minus_shifted = [(-ONE) * d for d in g_minus]

    check(
        "Theorem 4(2) K_{U(5)} = H{+-I_5} has two determinant components det=+-1 and excludes det=i",
        det_plus == ONE
        and det_plus * det_plus == ONE
        and det_minus == -ONE
        and det_minus * det_minus == ONE
        and det_diag(g_minus_shifted) == ONE
        and det_quarter == IMAG
        and det_quarter * det_quarter == -ONE,
    )


# ---------------------------------------------------------------------------
# 5. Theorem 5 controls: 252-dim link register Lambda^5(C^10) and O_{xy}^{(10)}
# ---------------------------------------------------------------------------


def apply_creator(mask: int, mode: int) -> tuple[int, int]:
    """Apply f_{mode}^dagger to Fock state `mask`. Return (sign, new_mask) or (0, 0)."""
    if mask & (1 << mode):
        return 0, 0
    return fermion_sign(mask, mode), mask | (1 << mode)


def apply_annihilator(mask: int, mode: int) -> tuple[int, int]:
    """Apply f_{mode} to Fock state `mask`. Return (sign, new_mask) or (0, 0)."""
    if not (mask & (1 << mode)):
        return 0, 0
    return fermion_sign(mask, mode), mask ^ (1 << mode)


def apply_monomial(mask: int, ops: list[tuple[str, int]]) -> tuple[int, int]:
    """Apply a sequence of ('c', mode) or ('a', mode) operators right-to-left on `mask`."""
    sign = 1
    cur = mask
    for kind, mode in reversed(ops):
        if kind == "c":
            s, cur = apply_creator(cur, mode)
        else:
            s, cur = apply_annihilator(cur, mode)
        if s == 0:
            return 0, 0
        sign *= s
    return sign, cur


def perm_sign(p: tuple[int, ...]) -> int:
    inversions = 0
    for i in range(len(p)):
        for j in range(i + 1, len(p)):
            if p[i] > p[j]:
                inversions += 1
    return -1 if (inversions & 1) else 1


def theorem5_native_determinant_carrier_controls() -> None:
    # Link modes: 0..4 are r_{x,1}..r_{x,5}; 5..9 are r_{y,1}..r_{y,5}.
    link_basis = [mask for mask in range(1 << 10) if mask.bit_count() == 5]
    link_idx = {mask: idx for idx, mask in enumerate(link_basis)}
    check("Lambda^5(C^10) link register has dimension C(10,5) = 252", len(link_basis) == 252)

    # Represent each operator on Lambda^5(C^10) as a sparse column map: col_idx -> dict[row_idx, int]
    # U_ell^{ij} = r_{y,i} r_{x,j}^dagger (i, j in 0..4)
    u_link = {}
    for i in range(5):
        for j in range(5):
            col_map = {}
            ops = [("a", 5 + i), ("c", j)]
            for c_idx, mask in enumerate(link_basis):
                s, new_mask = apply_monomial(mask, ops)
                if s != 0:
                    col_map[c_idx] = (link_idx[new_mask], s)
            u_link[(i, j)] = col_map

    def mul_link_ops(op_list):
        """Multiply a list of sparse link operators right-to-left on the 252-dim basis."""
        result = {}
        for c_idx in range(252):
            cur_row = c_idx
            cur_sign = 1
            for op in reversed(op_list):
                entry = op.get(cur_row)
                if entry is None:
                    cur_sign = 0
                    break
                cur_row, s = entry
                cur_sign *= s
            if cur_sign != 0:
                result[c_idx] = (cur_row, cur_sign)
        return result

    # Direct construction of D_{xy} = (r_{y,1}...r_{y,5})(r_{x,5}^dagger...r_{x,1}^dagger)
    d_xy_ops = [("a", 5 + i) for i in range(5)] + [("c", 4 - j) for j in range(5)]
    d_xy = {}
    for c_idx, mask in enumerate(link_basis):
        s, new_mask = apply_monomial(mask, d_xy_ops)
        if s != 0:
            d_xy[c_idx] = (link_idx[new_mask], s)

    state_0x_5y = link_idx[0b11111_00000]
    state_5x_0y = link_idx[0b00000_11111]

    check(
        "Theorem 5(2) D_{xy} = -|5_x, 0_y><0_x, 5_y| is rank-1 on Lambda^5(C^10) with Tr(D_{xy}^* D_{xy}) = 1",
        d_xy == {state_0x_5y: (state_5x_0y, -1)},
    )

    # Check U^{i_1,1}...U^{i_5,5} = sgn(i) D_{xy} for all 120 permutations and repeated-index tuples
    all_perms_match = True
    for p in permutations(range(5)):
        prod_op = mul_link_ops([u_link[(p[k], k)] for k in range(5)])
        expected = {state_0x_5y: (state_5x_0y, -perm_sign(p))}
        if prod_op != expected:
            all_perms_match = False
            break

    # Also check permutations on BOTH row and column indices and repeated-index vanishing
    both_perms_match = True
    for p in permutations(range(5)):
        for q in ((0, 1, 2, 3, 4), (4, 3, 2, 1, 0), (1, 0, 2, 4, 3)):
            prod_op = mul_link_ops([u_link[(p[k], q[k])] for k in range(5)])
            expected = {state_0x_5y: (state_5x_0y, -perm_sign(p) * perm_sign(q))}
            if prod_op != expected:
                both_perms_match = False
                break

    repeated_tuples = [
        ((0, 0, 1, 2, 3), (0, 1, 2, 3, 4)),
        ((0, 1, 2, 3, 4), (0, 1, 2, 2, 4)),
        ((1, 1, 2, 2, 3), (0, 1, 1, 3, 4)),
    ]
    repeated_vanish = all(
        mul_link_ops([u_link[(ri[k], cj[k])] for k in range(5)]) == {}
        for ri, cj in repeated_tuples
    )

    check(
        "Theorem 5(1) U_ell^{i_1,j_1}...U_ell^{i_5,j_5} = eps(i) eps(j) D_{xy} across all 120 permutations and repeated indices",
        all_perms_match and both_perms_match and repeated_vanish,
    )

    # Theorem 5(3): Support-reduced 20-mode two-site + link Fock verification of O_{xy}^{(10)} = B_x D_{xy} B_y
    # Mode numbering in 20-bit Fock space:
    #   0..4:   c_{x,1}..c_{x,5}
    #   5..9:   r_{x,1}..r_{x,5}
    #   10..14: r_{y,1}..r_{y,5}
    #   15..19: c_{y,1}..c_{y,5}
    b_x_ops = [("c", i) for i in range(5)]
    d_xy_20_ops = [("a", 10 + i) for i in range(5)] + [("c", 5 + (4 - j)) for j in range(5)]
    b_y_ops = [("c", 15 + i) for i in range(5)]
    o_xy_ops = b_x_ops + d_xy_20_ops + b_y_ops

    check(
        "Theorem 5(3) O_{xy}^{(10)} has 20 fermion letters (strictly fermion-even)",
        len(o_xy_ops) == 20 and (len(o_xy_ops) % 2 == 0),
    )

    # O_{xy}^{(10)} acts on the entire 2^10 * 252 = 258,048-dimensional physical state space
    # (arbitrary matter occupation at x and y, and 5 link rishons).
    # Notice B_x requires x-matter empty (bits 0..4 == 0), B_y requires y-matter empty (bits 15..19 == 0),
    # and D_{xy} requires link in state |0_x, 5_y> (bits 5..9 == 0, bits 10..14 == 0b11111).
    # These support conditions give a unique possible nonzero transition. Verify that
    # transition and the Gauss commutators on its support, output, and generator preimages
    # below; the remaining basis states vanish by the support argument. This is a
    # support-reduced check, not enumeration of all 258,048 basis states.
    in_mask = 0b00000_11111_00000_00000
    out_mask = 0b11111_00000_11111_11111

    s_in, target_in = apply_monomial(in_mask, o_xy_ops)
    check(
        "Theorem 5(2)-(3) O_{xy}^{(10)} maps |0_mx, 0_rx, 5_ry, 0_my> to |5_mx, 5_rx, 0_ry, 5_my> with norm 1",
        s_in == 1 and target_in == out_mask,
    )

    def apply_gauss_z(mask: int, z: str, i: int, j: int) -> list[tuple[int, int]]:
        """Apply G_z^{ij} = c_{z,i}^dagger c_{z,j} + r_{z,i}^dagger r_{z,j} to `mask`."""
        if z == "x":
            c_ops = [("c", i), ("a", j)]
            r_ops = [("c", 5 + i), ("a", 5 + j)]
        else:
            c_ops = [("c", 15 + i), ("a", 15 + j)]
            r_ops = [("c", 10 + i), ("a", 10 + j)]
        terms = []
        for ops in (c_ops, r_ops):
            s, m_new = apply_monomial(mask, ops)
            if s != 0:
                terms.append((s, m_new))
        return terms

    def apply_commutator_on_mask(mask: int, z: str, i: int, j: int) -> dict[int, int]:
        """Compute [G_z^{ij}, O_{xy}^{(10)}] |mask> as a dict {out_state: coeff}."""
        res: dict[int, int] = {}
        # Term 1: G_z^{ij} (O_{xy}^{(10)} |mask>)
        s_o, m_o = apply_monomial(mask, o_xy_ops)
        if s_o != 0:
            for s_g, m_go in apply_gauss_z(m_o, z, i, j):
                res[m_go] = res.get(m_go, 0) + s_o * s_g
        # Term 2: - O_{xy}^{(10)} (G_z^{ij} |mask>)
        for s_g, m_g in apply_gauss_z(mask, z, i, j):
            s_og, m_og = apply_monomial(m_g, o_xy_ops)
            if s_og != 0:
                res[m_og] = res.get(m_og, 0) - s_g * s_og
        return {k: v for k, v in res.items() if v != 0}

    # Test states covering the active domain of O_{xy}^{(10)} and all single-exchange neighbors
    # where G_z^{ij} can move a state into in_mask.
    test_masks = {in_mask, out_mask}
    for z in ("x", "y"):
        for i in range(5):
            for j in range(5):
                # States that G_z^{ji} (adjoint of G_z^{ij}) maps from in_mask
                for _, m_neighbor in apply_gauss_z(in_mask, z, j, i):
                    test_masks.add(m_neighbor)

    gx_comm_ok = True
    gy_comm_ok = True
    for i in range(5):
        for j in range(5):
            for m in test_masks:
                comm_x = apply_commutator_on_mask(m, "x", i, j)
                s_o, m_o = apply_monomial(m, o_xy_ops)
                expected_x = {m_o: 2 * s_o} if (i == j and s_o != 0) else {}
                if comm_x != expected_x:
                    gx_comm_ok = False
                comm_y = apply_commutator_on_mask(m, "y", i, j)
                if comm_y != {}:
                    gy_comm_ok = False

    check(
        "Theorem 5(3) [G_x^{ij}, O_{xy}^{(10)}] = 2 delta_{ij} O_{xy}^{(10)} for all 25 gl(5)_x generators",
        gx_comm_ok,
    )
    check(
        "Theorem 5(3) [G_y^{ij}, O_{xy}^{(10)}] = 0 for all 25 gl(5)_y generators",
        gy_comm_ok,
    )


# ---------------------------------------------------------------------------
# 6. Theorem 6 controls: Global quartic su(5) 3+2 orbit selection via cubic discriminant
# ---------------------------------------------------------------------------


def theorem6_su5_quartic_orbit_selection_controls() -> None:
    # Theorem 6(1): 3-variable cubic discriminant identity
    test_triples = [
        (Q(-3), Q(1), Q(5)),
        (Q(-2), Q(-2), Q(7)),
        (Q(4), Q(-1), Q(4)),
        (Q(0), Q(0), Q(0)),
        (Q(-7, 3), Q(2, 5), Q(11, 4)),
        (Q(5, 2), Q(5, 2), Q(-3, 4)),
    ]
    disc_identities_ok = True
    for x, y, z in test_triples:
        x_bar = (x + y + z) / 3
        u = x - x_bar
        v = y - x_bar
        w = z - x_bar
        r2 = u * u + v * v + w * w
        u4_sum = u**4 + v**4 + w**4
        x4_sum = x**4 + y**4 + z**4
        rhs_x4 = 3 * (x_bar**4) + 6 * (x_bar**2) * r2 + Q(1, 2) * (r2**2) + 12 * x_bar * u * v * w
        disc_lhs = ((u - v) ** 2) * ((v - w) ** 2) * ((w - u) ** 2)
        disc_rhs = Q(1, 2) * (r2**3) - 27 * ((u * v * w) ** 2)
        two_equal = (x == y) or (y == z) or (z == x)
        if not (
            u + v + w == 0
            and u4_sum == Q(1, 2) * (r2**2)
            and x4_sum == rhs_x4
            and disc_lhs == disc_rhs
            and disc_rhs >= 0
            and ((disc_rhs == 0) == two_equal)
        ):
            disc_identities_ok = False
            break

    check(
        "Theorem 6(1) 3-variable cubic discriminant identity Delta(u,v,w) = (1/2) r^6 - 27 (uvw)^2 >= 0",
        disc_identities_ok,
    )

    # Theorem 6(2): Exact fourth-moment ratios on the four symmetry strata and off-stratum perturbations
    def diag_su5(vals: list[Q]):
        assert len(vals) == 5 and sum(vals) == 0
        m = mat_zero(5)
        for idx, val in enumerate(vals):
            m[idx][idx] = Qi(val, 0)
        return m

    def tr_q(m) -> Q:
        t = mat_tr(m)
        assert t.im == 0
        return t.re

    def tr2_and_tr4(m) -> tuple[Q, Q]:
        m2 = mat_mul(m, m)
        m4 = mat_mul(m2, m2)
        return tr_q(m2), tr_q(m4)

    a_32 = diag_su5([Q(-2), Q(-2), Q(-2), Q(3), Q(3)])
    a_212 = diag_su5([Q(-1), Q(-1), Q(0), Q(1), Q(1)])
    a_131 = diag_su5([Q(-1), Q(0), Q(0), Q(0), Q(1)])
    a_41 = diag_su5([Q(1), Q(1), Q(1), Q(1), Q(-4)])

    s_32, f_32 = tr2_and_tr4(a_32)
    s_212, f_212 = tr2_and_tr4(a_212)
    s_131, f_131 = tr2_and_tr4(a_131)
    s_41, f_41 = tr2_and_tr4(a_41)

    ratio_32 = f_32 / (s_32**2)
    ratio_212 = f_212 / (s_212**2)
    ratio_131 = f_131 / (s_131**2)
    ratio_41 = f_41 / (s_41**2)

    check(
        "Theorem 6(2) exact fourth-moment ratios 7/30 < 1/4 < 1/2 < 13/20 across all four symmetry strata",
        ratio_32 == Q(7, 30)
        and ratio_212 == Q(1, 4)
        and ratio_131 == Q(1, 2)
        and ratio_41 == Q(13, 20)
        and ratio_32 < ratio_212 < ratio_131 < ratio_41
        and (ratio_41 - ratio_32 == Q(5, 12))
        and (ratio_212 - ratio_32 == Q(1, 60)),
    )

    # Off-stratum diagonal and non-diagonal Hermitian matrices in su(5)_sa
    off_stratum_matrices = [
        diag_su5([Q(-2) + Q(1, 5), Q(-2) - Q(1, 5), Q(-2), Q(3), Q(3)]),
        diag_su5([Q(-2), Q(-2), Q(-2) + Q(1, 7), Q(3) - Q(1, 7), Q(3)]),
        diag_su5([Q(-5), Q(-1), Q(0), Q(2), Q(4)]),
        diag_su5([Q(-3), Q(-2), Q(1), Q(1), Q(3)]),
    ]
    # Add non-diagonal Hermitian perturbations with complex off-diagonal entries
    m_nondiag_1 = diag_su5([Q(-2), Q(-2), Q(-2), Q(3), Q(3)])
    m_nondiag_1[0][1] = Qi(Q(1, 3), Q(1, 4))
    m_nondiag_1[1][0] = m_nondiag_1[0][1].conj()
    off_stratum_matrices.append(m_nondiag_1)

    m_nondiag_2 = diag_su5([Q(-2), Q(-2), Q(-2), Q(3), Q(3)])
    m_nondiag_2[2][3] = Qi(Q(2, 5), Q(-1, 2))
    m_nondiag_2[3][2] = m_nondiag_2[2][3].conj()
    m_nondiag_2[0][4] = Qi(Q(1, 3), Q(0))
    m_nondiag_2[4][0] = m_nondiag_2[0][4].conj()
    m_nondiag_2[0][0] = Qi(Q(-2) + Q(1, 2), Q(0))
    m_nondiag_2[1][1] = Qi(Q(-2) - Q(1, 2), Q(0))
    off_stratum_matrices.append(m_nondiag_2)

    bounds_strict_ok = True
    for m_test in off_stratum_matrices:
        s_val, f_val = tr2_and_tr4(m_test)
        if not (Q(7, 30) * (s_val**2) < f_val < Q(13, 20) * (s_val**2)):
            bounds_strict_ok = False
            break

    check(
        "Theorem 6(2) strict inequality (7/30) s^2 < Tr(A^4) < (13/20) s^2 for off-orbit su(5)_sa matrices",
        bounds_strict_ok,
    )

    # Theorem 6(3): Square-completed potential identity and unique 3+2 global minimum
    # Choose mu^2 = 15/2 > 0, lambda_1 = -1/10 < 0, lambda_2 = 3/2 > 0 so kappa_{3+2} = -1/10 + 7/20 = 1/4 > 0
    # and s_* = mu^2 / kappa_{3+2} = 30, which matches Tr(a_32^2) = 30!
    mu2 = Q(15, 2)
    lam1 = Q(-1, 10)
    lam2 = Q(3, 2)
    kappa_32 = lam1 + Q(7, 30) * lam2
    s_star = mu2 / kappa_32
    v_min = -(mu2**2) / (4 * kappa_32)

    def eval_potential(m) -> Q:
        s_val, f_val = tr2_and_tr4(m)
        return -Q(1, 2) * mu2 * s_val + Q(1, 4) * lam1 * (s_val**2) + Q(1, 4) * lam2 * f_val

    def eval_completed_square_rhs(m) -> Q:
        s_val, f_val = tr2_and_tr4(m)
        return (
            v_min
            + Q(1, 4) * kappa_32 * ((s_val - s_star) ** 2)
            + Q(1, 4) * lam2 * (f_val - Q(7, 30) * (s_val**2))
        )

    all_test_mats = [a_32, a_212, a_131, a_41] + off_stratum_matrices
    potential_ok = (
        kappa_32 == Q(1, 4)
        and s_star == Q(30)
        and eval_potential(a_32) == v_min
        and all(eval_potential(m) == eval_completed_square_rhs(m) for m in all_test_mats)
        and all(eval_potential(m) > v_min for m in all_test_mats[1:])
    )

    check(
        "Theorem 6(3) exact square-completed quartic potential identity and strict global minimum on 3+2 orbit",
        potential_ok,
    )


# ---------------------------------------------------------------------------
# 7. Theorem 7 controls: 25x25 Higgs Gram matrix, Pi_{Lie(H)} projector, and pinch identity
# ---------------------------------------------------------------------------


def theorem7_higgs_gram_and_pinch_controls() -> None:
    a_val = Q(-2)
    b_val = Q(3)
    gap = a_val - b_val  # -5
    gap_sq = gap * gap   # 25
    kappa = Q(3, 2)
    four_kappa_sq = 4 * kappa * kappa  # 9
    twenty_kappa_sq = 20 * kappa * kappa  # 45

    a0 = mat_zero(5)
    for i in range(5):
        a0[i][i] = Qi(a_val if i < 3 else b_val, 0)
    eye5 = mat_eye(5)

    def sym_basis(p: int, q: int):
        m = mat_zero(5)
        m[p][q] = ONE
        m[q][p] = ONE
        return m

    def asym_basis(p: int, q: int):
        m = mat_zero(5)
        m[p][q] = -IMAG
        m[q][p] = IMAG
        return m

    def diag_basis(vals: list[Q]):
        m = mat_zero(5)
        for idx, val in enumerate(vals):
            m[idx][idx] = Qi(val, 0)
        return m

    # 12 basis matrices for Lie(H) = su(3) (+) su(2) (+) u(1)_Y
    lie_h_basis = [
        # su(3): 6 off-diagonal + 2 Cartan
        sym_basis(0, 1),
        asym_basis(0, 1),
        sym_basis(0, 2),
        asym_basis(0, 2),
        sym_basis(1, 2),
        asym_basis(1, 2),
        diag_basis([Q(1), Q(-1), Q(0), Q(0), Q(0)]),
        diag_basis([Q(1), Q(1), Q(-2), Q(0), Q(0)]),
        # su(2): 2 off-diagonal + 1 Cartan
        sym_basis(3, 4),
        asym_basis(3, 4),
        diag_basis([Q(0), Q(0), Q(0), Q(1), Q(-1)]),
        # u(1)_Y
        diag_basis([Q(-2), Q(-2), Q(-2), Q(3), Q(3)]),
    ]

    # 12 basis matrices for the broken coset m_{3x2}
    coset_basis = []
    for p in range(3):
        for q in (3, 4):
            coset_basis.append(sym_basis(p, q))
            coset_basis.append(asym_basis(p, q))

    # 1 central generator I_5
    central_basis = [eye5]

    full_u5_basis = lie_h_basis + coset_basis + central_basis

    def inner_tr(x, y) -> Q:
        t = mat_tr(mat_mul(x, y))
        assert t.im == 0
        return t.re

    # Verify mutual orthogonality of the 25 basis elements (diagonal Gram matrix with positive diagonal)
    gram_25 = [[inner_tr(b1, b2) for b2 in full_u5_basis] for b1 in full_u5_basis]
    basis_orthogonal_and_complete = (
        len(lie_h_basis) == 12
        and len(coset_basis) == 12
        and len(full_u5_basis) == 25
        and all(gram_25[i][i] > 0 for i in range(25))
        and all(gram_25[i][j] == 0 for i in range(25) for j in range(25) if i != j)
    )

    def apply_higgs_gram(y):
        comm1 = mat_comm(a0, y)
        comm2 = mat_comm(a0, comm1)
        tr_y = mat_tr(y)
        return mat_add(comm2, mat_scale(Qi(four_kappa_sq, 0) * tr_y, eye5))

    lie_h_in_ker = all(apply_higgs_gram(b) == mat_zero(5) for b in lie_h_basis)
    coset_eig_ok = all(
        apply_higgs_gram(b) == mat_scale(Qi(gap_sq, 0), b) for b in coset_basis
    )
    central_eig_ok = apply_higgs_gram(eye5) == mat_scale(Qi(twenty_kappa_sq, 0), eye5)

    # Also build the 25x25 matrix of M^2 in the basis to check rank, trace, and nonzero determinant
    m2_diag_eigs = [
        inner_tr(b, apply_higgs_gram(b)) / inner_tr(b, b) for b in full_u5_basis
    ]
    rank_m2 = sum(1 for ev in m2_diag_eigs if ev != 0)
    tr_m2 = sum(m2_diag_eigs)
    det_nonzero_part = Q(1)
    for ev in m2_diag_eigs:
        if ev != 0:
            det_nonzero_part *= ev

    check(
        "Theorem 7(1) 25x25 Higgs Gram matrix M^2 spectrum: dim ker=12 (Lie(H)), 12x(a-b)^2 on m_{3x2}, 1x(20 kappa^2) on T_0",
        basis_orthogonal_and_complete
        and lie_h_in_ker
        and coset_eig_ok
        and central_eig_ok
        and rank_m2 == 13
        and tr_m2 == 12 * gap_sq + twenty_kappa_sq
        and det_nonzero_part == twenty_kappa_sq * (gap_sq**12),
    )

    # Theorem 7(2): Exact polynomial projector Pi_{Lie(H)} on all 25 basis elements
    p3_0 = mat_scale(Qi(Q(1) / gap, 0), mat_sub(a0, mat_scale(Qi(b_val, 0), eye5)))
    p2_0 = mat_sub(eye5, p3_0)

    def pi_commutator_form(x):
        double_comm = mat_comm(a0, mat_comm(a0, x))
        tr_x = mat_tr(x)
        return mat_sub(
            mat_sub(x, mat_scale(Qi(Q(1) / gap_sq, 0), double_comm)),
            mat_scale(Qi(Q(1, 5), 0) * tr_x, eye5),
        )

    def pi_pinch_form(x):
        pinched = mat_add(mat_mul(mat_mul(p3_0, x), p3_0), mat_mul(mat_mul(p2_0, x), p2_0))
        tr_x = mat_tr(x)
        return mat_sub(pinched, mat_scale(Qi(Q(1, 5), 0) * tr_x, eye5))

    proj_forms_equal = all(pi_commutator_form(b) == pi_pinch_form(b) for b in full_u5_basis)
    proj_fixes_lie_h = all(pi_commutator_form(b) == b for b in lie_h_basis)
    proj_kills_perp = all(
        pi_commutator_form(b) == mat_zero(5) for b in (coset_basis + central_basis)
    )
    proj_idempotent = all(
        pi_commutator_form(pi_commutator_form(b)) == pi_commutator_form(b)
        for b in full_u5_basis
    )

    check(
        "Theorem 7(2) exact polynomial unbroken-subalgebra projector Pi_{Lie(H)} on all 25 basis elements of u(5)_sa",
        proj_forms_equal and proj_fixes_lie_h and proj_kills_perp and proj_idempotent,
    )

    # Theorem 7(3): Universal noncommuting pinch-commutator identity on A = M_2(C), A, X in A (x) M_5(C)
    # Build noncommuting 10x10 matrices A_op and X_op where [A_op, X_op] != 0 and D_A != 0
    s1, s2, s3 = pauli_matrices()
    i2 = mat_eye(2)
    i10 = mat_eye(10)

    a_op = mat_zero(10)
    for idx in range(5):
        lam = a_val if idx < 3 else b_val
        e_ii = mat_zero(5)
        e_ii[idx][idx] = ONE
        a_op = mat_add(a_op, mat_kron(mat_scale(Qi(lam, 0), i2), e_ii))
    # Add noncommuting operator perturbations to A_op so D_A = P_3(A)^2 - P_3(A) != 0
    a_op = mat_add(a_op, mat_kron(mat_scale(Qi(Q(1, 2), 0), s1), sym_basis(0, 3)))
    a_op = mat_add(a_op, mat_kron(mat_scale(Qi(Q(1, 3), 0), s2), asym_basis(2, 4)))

    # Build a generic noncommuting X_op in M_2(C) (x) M_5(C)
    x_op = mat_add(
        mat_kron(s1, sym_basis(0, 1)),
        mat_add(
            mat_kron(s2, sym_basis(1, 3)),
            mat_kron(s3, asym_basis(2, 4)),
        ),
    )

    p3_op = mat_scale(Qi(Q(1) / gap, 0), mat_sub(a_op, mat_scale(Qi(b_val, 0), i10)))
    p2_op = mat_sub(i10, p3_op)
    d_a_op = mat_sub(mat_mul(p3_op, p3_op), p3_op)

    pinch_x = mat_add(mat_mul(mat_mul(p3_op, x_op), p3_op), mat_mul(mat_mul(p2_op, x_op), p2_op))
    comm_x = mat_sub(
        x_op,
        mat_scale(Qi(Q(1) / gap_sq, 0), mat_comm(a_op, mat_comm(a_op, x_op))),
    )
    lhs_diff = mat_sub(pinch_x, comm_x)
    rhs_anti = mat_add(mat_mul(d_a_op, x_op), mat_mul(x_op, d_a_op))

    check(
        "Theorem 7(3) universal noncommuting pinch-commutator identity (P_3 X P_3 + P_2 X P_2) - (X - (a-b)^{-2}[A,[A,X]]) = D_A X + X D_A",
        d_a_op != mat_zero(10) and lhs_diff != mat_zero(10) and lhs_diff == rhs_anti,
    )


# ---------------------------------------------------------------------------
# 8. Theorem 8 controls: Single-link transport floor and K-copy coherent FMS scaling
# ---------------------------------------------------------------------------


def theorem8_transport_floor_and_coherent_scaling_controls() -> None:
    # Theorem 8(1): Exact single-link two-sided transport defect identity on Lambda^5(C^10)
    # In the 3-state decomposition { |0_x,5_y>, |5_x,0_y>, |perp> } of Lambda^5(C^10),
    # D_{xy} = -|5_x,0_y><0_x,5_y|, P_0 = D_{xy}^* D_{xy} = diag(1,0,0), P_5 = D_{xy} D_{xy}^* = diag(0,1,0).
    d_xy_3 = mat_zero(3)
    d_xy_3[1][0] = -ONE
    i3 = mat_eye(3)

    state_weight_triples = [
        (Q(0), Q(0), Q(1)),
        (Q(1, 2), Q(1, 2), Q(0)),
        (Q(1), Q(0), Q(0)),
        (Q(1, 3), Q(1, 4), Q(5, 12)),
        (Q(2, 5), Q(3, 5), Q(0)),
    ]
    gammas = [
        Qi(Q(0), Q(0)),
        Qi(Q(1), Q(0)),
        Qi(Q(3, 5), Q(4, 5)),  # |gamma|^2 = 1
        Qi(Q(2), Q(0)),        # |gamma|^2 = 4
        Qi(Q(1, 2), Q(-2, 3)),
    ]

    transport_floor_ok = True
    for p0, p5, p_perp in state_weight_triples:
        assert p0 + p5 + p_perp == 1
        for gam in gammas:
            t_gam = mat_scale(gam, d_xy_3)
            t_adj = mat_adj(t_gam)
            def_plus_mat = mat_mul(
                mat_sub(mat_mul(t_adj, t_gam), i3),
                mat_sub(mat_mul(t_adj, t_gam), i3),
            )
            def_minus_mat = mat_mul(
                mat_sub(mat_mul(t_gam, t_adj), i3),
                mat_sub(mat_mul(t_gam, t_adj), i3),
            )
            d_plus = (
                p0 * def_plus_mat[0][0].re
                + p5 * def_plus_mat[1][1].re
                + p_perp * def_plus_mat[2][2].re
            )
            d_minus = (
                p0 * def_minus_mat[0][0].re
                + p5 * def_minus_mat[1][1].re
                + p_perp * def_minus_mat[2][2].re
            )
            gam_sq = gam.re * gam.re + gam.im * gam.im
            rhs = 2 - (p0 + p5) + ((gam_sq - 1) ** 2) * (p0 + p5)
            attains_one = (p0 + p5 == 1) and (gam_sq == 1)
            if not (
                d_plus + d_minus == rhs
                and d_plus + d_minus >= 1
                and ((d_plus + d_minus == 1) == attains_one)
            ):
                transport_floor_ok = False
                break

    check(
        "Theorem 8(1) single-link two-sided transport defect D_+ + D_- = 2 - (p_0+p_5) + (|gamma|^2-1)^2 (p_0+p_5) >= 1",
        transport_floor_ok,
    )

    # Theorem 8(2a): Multi-copy coherent SU(2) FMS projector defect scaling on H_K = (C^2)^{otimes K}
    s1, s2, s3 = pauli_matrices()
    paulis = (s1, s2, s3)
    i2 = mat_eye(2)

    def kron_list(mats):
        res = mats[0]
        for m in mats[1:]:
            res = mat_kron(res, m)
        return res

    for k_copies in (1, 2, 3, 4):
        dim_k = 1 << k_copies
        ik = mat_eye(dim_k)
        phi_k = []
        for a_idx in range(3):
            sum_mat = mat_zero(dim_k)
            for nu in range(k_copies):
                factors = [paulis[a_idx] if slot == nu else i2 for slot in range(k_copies)]
                sum_mat = mat_add(sum_mat, kron_list(factors))
            phi_k.append(mat_scale(Qi(Q(1, k_copies), 0), sum_mat))

        # Casimir sum_a (Phi_K^a)^2
        casimir_k = mat_zero(dim_k)
        for a_idx in range(3):
            casimir_k = mat_add(casimir_k, mat_mul(phi_k[a_idx], phi_k[a_idx]))

        # Coherent state |psi_K> = |+>^{otimes K} corresponds to basis index 0
        # Check that column 0 of casimir_k is (1 + 2/K) e_0
        eig_val = Q(1) + Q(2, k_copies)
        casimir_col0 = [casimir_k[row][0] for row in range(dim_k)]
        expected_col0 = [Qi(eig_val, 0) if row == 0 else ZERO for row in range(dim_k)]

        # Commutator square sum at |psi_K> (entry (0,0))
        comm_sq_sum = mat_zero(dim_k)
        for a_idx in range(3):
            for b_idx in range(3):
                c_ab = mat_comm(phi_k[a_idx], phi_k[b_idx])
                comm_sq_sum = mat_add(comm_sq_sum, mat_mul(mat_adj(c_ab), c_ab))
        omega_comm_sq = comm_sq_sum[0][0]

        # Direct projector defect at r = 1: P_+(1) = (1/2)(I + sum_a Phi_K^a (x) sigma_a)
        a_op = mat_zero(2 * dim_k)
        for a_idx in range(3):
            a_op = mat_add(a_op, mat_kron(phi_k[a_idx], paulis[a_idx]))
        p_plus_1 = mat_scale(Qi(Q(1, 2), 0), mat_add(mat_eye(2 * dim_k), a_op))
        d_plus_1 = mat_sub(mat_mul(p_plus_1, p_plus_1), p_plus_1)
        hs_d_plus_1 = internal_hs_square(d_plus_1, dim_k, 2)
        omega_defect_r1 = hs_d_plus_1[0][0]

        # Defect at Casimir-matched radius r_K^2 = 1 + 2/K:
        # Note r_K^2 is rational, and |P_+(r_K)^2 - P_+(r_K)|_{HS}^2 = (1 / (16 r_K^4)) * (2 R_{r_K}^2 + comm_sq_sum)
        rk_sq = Q(1) + Q(2, k_copies)
        r_rk = mat_sub(casimir_k, mat_scale(Qi(rk_sq, 0), ik))
        r_rk_sq = mat_mul(r_rk, r_rk)
        omega_r_rk_sq = r_rk_sq[0][0]
        omega_defect_rk = (Qi(2, 0) * omega_r_rk_sq + omega_comm_sq) * Qi(
            Q(1) / (16 * rk_sq * rk_sq), 0
        )

        expected_defect_r1 = Q(k_copies + 1, k_copies**3)
        expected_defect_rk = Q(1, 2 * k_copies * (k_copies + 2))

        check(
            f"Theorem 8(2) K={k_copies} coherent SU(2) FMS defects: Casimir=1+2/{k_copies}, defect(r=1)={expected_defect_r1}, defect(r_K)={expected_defect_rk}",
            casimir_col0 == expected_col0
            and omega_comm_sq == Qi(Q(8 * (k_copies + 2), k_copies**3), 0)
            and omega_r_rk_sq == ZERO
            and omega_defect_r1 == Qi(expected_defect_r1, 0)
            and omega_defect_rk == Qi(expected_defect_rk, 0),
        )

    # Theorem 8(2b): Multi-copy coherent determinant transport defect on (Lambda^5 C^10)^{otimes K}
    # In the 2D basis {|0_x,5_y>, |5_x,0_y>} of each copy, D_{xy} = [[0, 0], [-1, 0]],
    # and |theta> = (1/sqrt(2))(1, -1)^T (so 2 D_{xy} |theta> = |theta> - |theta_perp>
    # and 2 D_{xy}^* |theta_perp> = -(|theta> + |theta_perp>)).
    # For K copies, |Theta_K> = 2^{-K/2} (1, -1)^{otimes K}, so varpi_K(X) = 2^{-K} <v_K, X v_K>
    # where v_K = (1, -1)^{otimes K} has exact integer entries!
    d_single = [[ZERO, ZERO], [-ONE, ZERO]]
    for k_copies in (1, 2, 3, 4):
        dim_k = 1 << k_copies
        ik = mat_eye(dim_k)
        d_hat_k = mat_zero(dim_k)
        for nu in range(k_copies):
            factors = [d_single if slot == nu else i2 for slot in range(k_copies)]
            d_hat_k = mat_add(d_hat_k, kron_list(factors))
        d_hat_k = mat_scale(Qi(Q(2, k_copies), 0), d_hat_k)
        d_hat_adj = mat_adj(d_hat_k)

        # Build unnormalized integer vector v_K = (1, -1)^{otimes K}: entry at bitmask m is (-1)^{popcount(m)}
        v_k = [Qi(Q(-1 if (m.bit_count() & 1) else 1), 0) for m in range(dim_k)]
        norm_sq_vk = Q(1 << k_copies)

        def varpi_expect(op_mat) -> Q:
            total = ZERO
            for r_idx in range(dim_k):
                row_sum = ZERO
                for c_idx in range(dim_k):
                    if op_mat[r_idx][c_idx] != ZERO:
                        row_sum = row_sum + op_mat[r_idx][c_idx] * v_k[c_idx]
                total = total + v_k[r_idx].conj() * row_sum
            assert total.im == 0
            return total.re / norm_sq_vk

        diff_d = mat_sub(d_hat_k, ik)
        diff_d_adj = mat_sub(d_hat_adj, ik)
        vec_def_1 = varpi_expect(mat_mul(mat_adj(diff_d), diff_d))
        vec_def_2 = varpi_expect(mat_mul(mat_adj(diff_d_adj), diff_d_adj))

        gram_plus = mat_sub(mat_mul(d_hat_adj, d_hat_k), ik)
        gram_minus = mat_sub(mat_mul(d_hat_k, d_hat_adj), ik)
        tr_def_plus = varpi_expect(mat_mul(gram_plus, gram_plus))
        tr_def_minus = varpi_expect(mat_mul(gram_minus, gram_minus))

        expected_vec_def = Q(1, k_copies)
        expected_tr_def = Q(3 * k_copies + 2, k_copies**3)

        check(
            f"Theorem 8(2) K={k_copies} coherent determinant transport defect: ||(D_hat_K - I)|Theta_K>||^2 = 1/{k_copies}, varpi_K((D_hat_K^* D_hat_K - I)^2) = {expected_tr_def}",
            vec_def_1 == expected_vec_def
            and vec_def_2 == expected_vec_def
            and tr_def_plus == expected_tr_def
            and tr_def_minus == expected_tr_def
            and ((k_copies < 3) or (tr_def_plus + tr_def_minus < 1)),
        )


def main() -> None:
    source = Path(__file__).resolve().parents[1] / AUDIT_INPUT_PATHS[0]
    print("Source SHA256:", hashlib.sha256(source.read_bytes()).hexdigest())
    print(
        "Exact rational and Fock-space controls for Theorems 1-8 of the U(5) 3+2 FMS projector and stabilizer carrier note."
    )
    theorem1_su2_projector_controls()
    theorem2_u5_projector_and_car_controls()
    theorem3_orthogonal_projector_and_centralizer_controls()
    theorem4_stabilizer_and_z6_kernel_controls()
    theorem5_native_determinant_carrier_controls()
    theorem6_su5_quartic_orbit_selection_controls()
    theorem7_higgs_gram_and_pinch_controls()
    theorem8_transport_floor_and_coherent_scaling_controls()
    print(f"TOTAL: PASS={PASS_COUNT} FAIL=0")


if __name__ == "__main__":
    main()
