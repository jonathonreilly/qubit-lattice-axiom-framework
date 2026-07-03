"""Block-6 link-star frame-correlation gluing runner.

Sections:
A. Pair gluing as a single composite class function.
B. Link-star diagonal-conjugation invariance and independent-conjugation witness.
C. Dagger-evenness of stars (orientation reversal) and SU(2)
   pairwise reduction; the antisymmetric triple branch is invisible to
   real-weight gluing (refutes the pre-computation expectation).
D. Chain transport and loop difference.

Expected close: TOTAL: PASS=14 FAIL=0
"""

import numpy as np


PASS = 0
FAIL = 0
TOL_QUAD = 3.0e-3


def check(name, condition, detail=""):
    global PASS, FAIL
    if condition:
        PASS += 1
        mark = "PASS"
    else:
        FAIL += 1
        mark = "FAIL"
    suffix = f" | {detail}" if detail else ""
    print(f"{mark}: {name}{suffix}")


def su2(t, x, y, z):
    return np.array(
        [[t + 1j * z, 1j * x + y], [1j * x - y, t - 1j * z]],
        dtype=np.complex128,
    )


def normalize4(v):
    arr = np.array(v, dtype=np.float64)
    return arr / np.linalg.norm(arr)


def su2_from_vector(v):
    return su2(*normalize4(v))


def dagger(m):
    return np.conjugate(m.T)


def chi(j, m):
    tr = m[..., 0, 0] + m[..., 1, 1]
    cos_theta = np.clip(np.real(tr) / 2.0, -1.0, 1.0)
    theta = np.arccos(cos_theta)
    denom = np.sin(theta)
    numer = np.sin((2.0 * j + 1.0) * theta)
    out = np.empty_like(theta, dtype=np.float64)
    small = np.abs(denom) < 1.0e-12
    out[~small] = numer[~small] / denom[~small]
    out[small] = (2.0 * j + 1.0) * np.cos((2.0 * j) * theta[small])
    if np.ndim(out) == 0:
        return float(out)
    return out


def tr_real(m):
    return float(np.real(np.trace(m)))


def build_haar_grid():
    np_grid = 48
    nt_grid = 24
    nf_grid = 48
    psi = (np.arange(np_grid, dtype=np.float64) + 0.5) * np.pi / np_grid
    thet = (np.arange(nt_grid, dtype=np.float64) + 0.5) * np.pi / nt_grid
    phi = (np.arange(nf_grid, dtype=np.float64) + 0.5) * 2.0 * np.pi / nf_grid

    psi_m, thet_m, phi_m = np.meshgrid(psi, thet, phi, indexing="ij")
    radius = np.sin(psi_m)
    t = np.cos(psi_m)
    x = radius * np.sin(thet_m) * np.cos(phi_m)
    y = radius * np.sin(thet_m) * np.sin(phi_m)
    z = radius * np.cos(thet_m)

    mats = np.empty(t.shape + (2, 2), dtype=np.complex128)
    mats[..., 0, 0] = t + 1j * z
    mats[..., 0, 1] = 1j * x + y
    mats[..., 1, 0] = 1j * x - y
    mats[..., 1, 1] = t - 1j * z

    weights = (np.sin(psi_m) ** 2) * np.sin(thet_m)
    weights = weights.reshape(-1)
    weights = weights / np.sum(weights)
    mats = mats.reshape(-1, 2, 2)
    return mats, np.conjugate(np.swapaxes(mats, -1, -2)), weights


STAPLE_VECTORS = [
    (0.31, 0.72, -0.41, 0.46),
    (0.64, -0.22, 0.69, 0.27),
    (-0.18, 0.57, 0.33, 0.73),
    (0.49, 0.11, -0.81, 0.30),
    (-0.37, 0.66, 0.58, -0.30),
    (0.22, -0.74, 0.16, 0.62),
]
S = [su2_from_vector(v) for v in STAPLE_VECTORS]
S1, S2, S3, S4, S5, S6 = S

COEFFS = {
    0: {0.0: 1.0, 0.5: 0.7, 1.0: 0.3},
    1: {0.0: 1.0, 0.5: 0.5, 1.0: 0.2},
    2: {0.0: 1.0, 0.5: 0.4, 1.0: 0.25},
}
SPINS = (0.0, 0.5, 1.0)

V, VDAG, HAAR_W = build_haar_grid()


def weight(index, m):
    c = COEFFS[index]
    return c[0.0] + c[0.5] * chi(0.5, m) + c[1.0] * chi(1.0, m)


def integrate(values):
    return float(np.sum(HAAR_W * values))


def pair_same_quad(a, b):
    return integrate(weight(0, V @ a) * weight(1, V @ b))


def pair_opp_quad(a, b):
    return integrate(weight(0, V @ a) * weight(1, VDAG @ b))


def pair_same_formula(a, b):
    total = 0.0
    comp = dagger(b) @ a
    for j in SPINS:
        total += COEFFS[0][j] * COEFFS[1][j] * chi(j, comp) / (2.0 * j + 1.0)
    return float(total)


def pair_opp_formula(a, b):
    total = 0.0
    comp = b @ a
    for j in SPINS:
        total += COEFFS[0][j] * COEFFS[1][j] * chi(j, comp) / (2.0 * j + 1.0)
    return float(total)


def star_quad(a, b, c):
    return integrate(weight(0, V @ a) * weight(1, V @ b) * weight(2, VDAG @ c))


def transport_quad(j, a, b):
    return integrate(chi(j, a @ V) * chi(j, VDAG @ b))


def fmt(values):
    return ", ".join(f"{value:.12g}" for value in values)


# Section A
same_pairs = [(S1, S2), (S3, S4), (S5, S6)]
same_errors = [
    abs(pair_same_quad(a, b) - pair_same_formula(a, b)) for a, b in same_pairs
]
check(
    "pair same-orientation formula matches quadrature",
    max(same_errors) <= TOL_QUAD,
    f"errors=[{fmt(same_errors)}]",
)

opp_pairs = [(S1, S3), (S2, S5), (S4, S6)]
opp_errors = [abs(pair_opp_quad(a, b) - pair_opp_formula(a, b)) for a, b in opp_pairs]
check(
    "pair opposite-orientation formula matches quadrature",
    max(opp_errors) <= TOL_QUAD,
    f"errors=[{fmt(opp_errors)}]",
)

base_pair = pair_same_quad(S1, S2)
unitaries = [S4, S5]
a3_errors = [abs(pair_same_quad(u @ S1, u @ S2) - base_pair) for u in unitaries]
check(
    "pair composite-dependence under common left multiplication",
    max(a3_errors) <= TOL_QUAD,
    f"errors=[{fmt(a3_errors)}]",
)

a4_diffs = [abs(pair_same_quad(u @ S1, S2) - base_pair) for u in unitaries]
check(
    "pair one-staple rotation witness differs",
    max(a4_diffs) > 0.05,
    f"diffs=[{fmt(a4_diffs)}]",
)

# Section B
base_star = star_quad(S1, S2, S3)
diag_unitaries = [S5, S6]
b1_errors = [
    abs(star_quad(g @ S1 @ dagger(g), g @ S2 @ dagger(g), g @ S3 @ dagger(g)) - base_star)
    for g in diag_unitaries
]
check(
    "star diagonal-conjugation invariance of link star",
    max(b1_errors) <= TOL_QUAD,
    f"errors=[{fmt(b1_errors)}]",
)

b2_diffs = [
    abs(star_quad(g @ S1 @ dagger(g), S2, S3) - base_star) for g in diag_unitaries
]
check(
    "star independent conjugation witness differs",
    max(b2_diffs) > 0.02,
    f"diffs=[{fmt(b2_diffs)}]",
)

b3_trace_error = max(
    abs(np.trace(g @ S1 @ dagger(g)) - np.trace(S1)) for g in diag_unitaries
)
check(
    "star separate class unchanged by independent conjugation",
    b3_trace_error < 1.0e-12,
    f"max_trace_error={b3_trace_error:.12g}",
)

# Section C
S1_DAG, S2_DAG, S3_DAG = dagger(S1), dagger(S2), dagger(S3)
sep_trace_errors = [
    abs(np.trace(S1_DAG) - np.trace(S1)),
    abs(np.trace(S2_DAG) - np.trace(S2)),
    abs(np.trace(S3_DAG) - np.trace(S3)),
]
pair_original = [dagger(S2) @ S1, S3 @ S1, S3 @ S2]
pair_dagger = [S2 @ dagger(S1), dagger(S3) @ dagger(S1), dagger(S3) @ dagger(S2)]
pair_trace_errors = [
    abs(np.trace(pair_original[i]) - np.trace(pair_dagger[i])) for i in range(3)
]
c1_numbers = [
    tr_real(pair_original[0]),
    tr_real(pair_dagger[0]),
    tr_real(pair_original[1]),
    tr_real(pair_dagger[1]),
    tr_real(pair_original[2]),
    tr_real(pair_dagger[2]),
]
check(
    "dagger triple separate and pairwise traces match",
    max(sep_trace_errors + pair_trace_errors) < 1.0e-12,
    f"pair_traces=[{fmt(c1_numbers)}]",
)

triple_original = tr_real(S1 @ S2 @ S3)
triple_dagger = tr_real(S1_DAG @ S2_DAG @ S3_DAG)
c2_diff = abs(triple_original - triple_dagger)
check(
    "dagger triple-product trace witness differs",
    c2_diff > 0.05,
    f"original={triple_original:.12g}, dagger={triple_dagger:.12g}, diff={c2_diff:.12g}",
)

# The dagger triple does NOT change the star: substituting V -> V^dag and
# using w(X^dag) = w(X) for real class weights (plus cyclicity) gives the
# exact identity G(S^dag triple) = G(S triple) for ANY compact group and
# any star size. Combined with the triple-product witness this shows the star is EVEN under the
# orientation/branch reversal: the antisymmetric triple invariant
# tr(ABC) - tr(ACB) is invisible to real-weight gluing. The check below
# verifies the identity (the grid is exactly V -> V^dag symmetric, so the
# equality is exact on the grid), NOT a difference: the earlier design
# expectation of a difference was refuted by this computation.
star_dagger = star_quad(S1_DAG, S2_DAG, S3_DAG)
c3_diff = abs(base_star - star_dagger)
check(
    "dagger-evenness identity: the star is exactly invariant under the"
    " simultaneous dagger (orientation reversal); the antisymmetric triple"
    " branch is invisible, so it does NOT carry data beyond separate +"
    " pairwise classes here",
    c3_diff < 1.0e-12,
    f"original={base_star:.12g}, dagger={star_dagger:.12g}, diff={c3_diff:.12g}",
)

# SU(2) symmetric trace identity: the branch-symmetric combination is a
# polynomial in separate + pairwise traces, so dagger-even invariants of
# SU(2) triples reduce to separate + pairwise class data. Exact check.
c4_errors = []
for (a, b, c) in [(S1, S2, S3), (S4, S5, S6), (S2, S4, S6)]:
    lhs = tr_real(a @ b @ c) + tr_real(a @ c @ b)
    rhs = (tr_real(a) * tr_real(b @ c) + tr_real(b) * tr_real(a @ c)
           + tr_real(c) * tr_real(a @ b)
           - tr_real(a) * tr_real(b) * tr_real(c))
    c4_errors.append(abs(lhs - rhs))
check(
    "SU(2) symmetric trace identity: tr(ABC) + tr(ACB) is generated by"
    " separate + pairwise traces (so the SU(2) star is pairwise-reducible)",
    max(c4_errors) < 1.0e-12,
    f"errors=[{fmt(c4_errors)}]",
)

# Section D
d1_pairs = [(S1, S4), (S5, S6)]
d1_errors = []
for spin in (0.5, 1.0):
    dim = 2.0 * spin + 1.0
    for a, b in d1_pairs:
        d1_errors.append(abs(transport_quad(spin, a, b) - chi(spin, a @ b) / dim))
check(
    "transport single-gluing identity",
    max(d1_errors) <= TOL_QUAD,
    f"errors=[{fmt(d1_errors)}]",
)

# two-step chain = one-step transport through the composite middle: the
# W-integral collapses the middle pair to B C (by the single-gluing transport
# identity), so the remaining
# quadrature must reproduce chi(A B C)/d at fresh arguments — a quadrature
# vs closed-form check, not an algebraic identity.
d2_errors = []
for spin in (0.5, 1.0):
    dim = 2.0 * spin + 1.0
    for a, b, c in [(S1, S2, S3), (S4, S5, S6)]:
        lhs = transport_quad(spin, a, b @ c)
        rhs = chi(spin, a @ b @ c) / dim
        d2_errors.append(abs(lhs - rhs))
check(
    "transport chain through the composite middle matches the"
    " path-product closed form",
    max(d2_errors) <= TOL_QUAD,
    f"errors=[{fmt(d2_errors)}]",
)

chain_left = chi(0.5, S1 @ S2 @ S3)
chain_right = chi(0.5, S1 @ S4 @ S3)
loop_char = chi(0.5, dagger(S4) @ S2)
d3_diff = abs(chain_left - chain_right)
check(
    "transport loop difference witness",
    d3_diff > 0.05,
    f"left={chain_left:.12g}, right={chain_right:.12g}, diff={d3_diff:.12g}, loop_chi={loop_char:.12g}",
)

print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
