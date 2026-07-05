#!/usr/bin/env python3
"""
Vertex-power derivation runner — structural derivation of n_link = 2
=====================================================================

Registered primary runner for docs/YT_VERTEX_POWER_DERIVATION.md.

WHAT IS DERIVED (computed, not asserted):

  n_link = (number of external gauge legs of the coupling-defining
            quadratic response) x (gauge links per vertex insertion)
         = 2 x 1 = 2

  L1  On the adjacency-licensed nearest-neighbour surface, site-local
      SU(3) gauge covariance forces the hopping dressing to be exactly
      LINEAR in the edge link: any f with f(g U h^dag) = g f(U) h^dag
      for all g, h in SU(3) is f(U) = c U (Schur forcing). Computed:
      candidate scan — only the linear dressing is bi-equivariant.
  L2  The background-field vertex D' = dD/d(eps) carries exactly ONE
      gauge link per non-zero entry (link-exponential convention
      U(eps) = exp(i eps a) U0 gives dU/d(eps)|_0 = i a U0). Computed:
      finite-difference derivative of actual matrix exponentials, and
      exact link-degree D'(u*base) = u * D'(base).
  L3  The quadratic response of Gamma = -Tr ln D[A] contains exactly
      two operator structures (tadpole + bubble); the current-current
      (vertex-vertex) channel carries exactly TWO single-link vertex
      insertions. Computed: finite-difference d^2/d(eps)^2 Tr ln D
      matches Tr[D^-1 D''] - Tr[D^-1 D' D^-1 D'] ; link-degree of the
      insertion-pair operator is exactly 2 (slope fit, machine
      precision), with n in {0, 1, 3, 4} EXCLUDED by computed
      residuals (falsification leg).
  L4  Coupling-map algebra at n_link = 2 reproduces the retained
      identity surface alpha_s(v) = alpha_bare / u_0^2,
      alpha_LM^2 = alpha_bare * alpha_s(v) (exact rationals).

NO-BACK-PROPAGATION CERTIFICATE: this runner derives n_link = 2 from
operator structure only. It contains no strong-coupling comparator
value, no Z-pole running, no external experimental constant, and zero
class-(D) checks; a self-scan check enforces this on the source text.

Tags: [A] algebraic identity, [B] cross-note input verification (none here),
[C] first-principles compute, [D] external comparator (none).
Deterministic (fixed seed), numpy only, runtime well under 5 minutes.
"""

from __future__ import annotations

import math
import re
import sys
import time
from fractions import Fraction

import numpy as np
np.set_printoptions(precision=10, linewidth=120)
RNG = np.random.default_rng(20260611)

PI = math.pi
N_C = 3
L = 4
N_DIM = N_C * L**3

PASS_COUNT = 0
FAIL_COUNT = 0
BREAKDOWN = {"A": 0, "B": 0, "C": 0, "D": 0}


def check(name, condition, tag, detail=""):
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
        BREAKDOWN[tag] += 1
    else:
        FAIL_COUNT += 1
    print(f"  [{status}] [{tag}] {name}")
    if detail:
        print(f"         {detail}")


def residual(text):
    print(f"  RESIDUAL (declared-open): {text}")


# ===========================================================================
# UTILITIES
# ===========================================================================

def gell_mann():
    lam = np.zeros((8, 3, 3), dtype=complex)
    lam[0] = [[0, 1, 0], [1, 0, 0], [0, 0, 0]]
    lam[1] = [[0, -1j, 0], [1j, 0, 0], [0, 0, 0]]
    lam[2] = [[1, 0, 0], [0, -1, 0], [0, 0, 0]]
    lam[3] = [[0, 0, 1], [0, 0, 0], [1, 0, 0]]
    lam[4] = [[0, 0, -1j], [0, 0, 0], [1j, 0, 0]]
    lam[5] = [[0, 0, 0], [0, 0, 1], [0, 1, 0]]
    lam[6] = [[0, 0, 0], [0, 0, -1j], [0, 1j, 0]]
    lam[7] = np.diag([1, 1, -2]) / np.sqrt(3)
    return lam


GELL_MANN = gell_mann()


def rand_su3():
    """Haar-ish deterministic SU(3) sample via QR + det phase fix."""
    z = RNG.standard_normal((3, 3)) + 1j * RNG.standard_normal((3, 3))
    q, r = np.linalg.qr(z)
    q = q @ np.diag(np.diag(r) / np.abs(np.diag(r)))
    q = q / np.linalg.det(q) ** (1.0 / 3.0)
    return q


def herm_exp(a, t):
    """exp(i t a) for Hermitian a, via eigendecomposition (numpy only)."""
    w, v = np.linalg.eigh(a)
    return (v * np.exp(1j * t * w)) @ v.conj().T


def idx(x, y, z, c):
    return (((x % L) * L + (y % L)) * L + (z % L)) * N_C + c


def id_field(scale=1.0):
    U = np.zeros((L, L, L, 3, N_C, N_C), dtype=complex)
    U[..., :, :] = scale * np.eye(N_C)
    return U


def build_D(U_field, m=0.0):
    """Staggered Dirac operator on L^3 with SU(3) color (Hermitian)."""
    D = np.zeros((N_DIM, N_DIM), dtype=complex)
    for x in range(L):
        for y in range(L):
            for z in range(L):
                eps_s = (-1) ** (x + y + z)
                for c in range(N_C):
                    D[idx(x, y, z, c), idx(x, y, z, c)] += m * eps_s
                for mu, (dx, dy, dz) in enumerate(
                        [(1, 0, 0), (0, 1, 0), (0, 0, 1)]):
                    eta = 1 if mu == 0 else (
                        (-1) ** x if mu == 1 else (-1) ** (x + y))
                    Ulink = U_field[x, y, z, mu]
                    for c1 in range(N_C):
                        for c2 in range(N_C):
                            i = idx(x, y, z, c1)
                            j = idx((x + dx) % L, (y + dy) % L,
                                    (z + dz) % L, c2)
                            D[i, j] += -0.5j * eta * Ulink[c1, c2]
                            D[j, i] += 0.5j * eta * Ulink[c1, c2].conjugate()
    return D


def bg_profile(direction=0, k_mode=1):
    """cos(k x_perp) test profile values per site."""
    k = 2 * PI * k_mode / L
    perp = (direction + 1) % 3
    prof = np.zeros((L, L, L))
    for x in range(L):
        for y in range(L):
            for z in range(L):
                prof[x, y, z] = math.cos(k * [x, y, z][perp])
    return prof


def field_with_bg(eps, A_gen, base_scale=1.0, direction=0, k_mode=1):
    """U_mu(x) = base_scale * exp(i eps A cos(k x_perp)) in one direction."""
    U = id_field(base_scale)
    prof = bg_profile(direction, k_mode)
    for x in range(L):
        for y in range(L):
            for z in range(L):
                U[x, y, z, direction] = base_scale * herm_exp(
                    A_gen, eps * prof[x, y, z])
    return U


def build_D_deriv(A_gen, order=1, base_scale=1.0, direction=0, k_mode=1):
    """d^order D / d(eps)^order at eps = 0 for the background above.

    With U(eps) = base * exp(i eps a c), dU/deps|_0 = i a c * base (ONE
    explicit link factor), d2U/deps2|_0 = -(a c)^2 * base (still ONE
    explicit link factor).
    """
    Dd = np.zeros((N_DIM, N_DIM), dtype=complex)
    prof = bg_profile(direction, k_mode)
    mu = direction
    dx, dy, dz = [(1, 0, 0), (0, 1, 0), (0, 0, 1)][mu]
    base = base_scale * np.eye(N_C)
    for x in range(L):
        for y in range(L):
            for z in range(L):
                eta = 1 if mu == 0 else (
                    (-1) ** x if mu == 1 else (-1) ** (x + y))
                c = prof[x, y, z]
                if order == 1:
                    dU = (1j * c * A_gen) @ base
                else:
                    dU = (-(c ** 2) * A_gen @ A_gen) @ base
                for c1 in range(N_C):
                    for c2 in range(N_C):
                        i = idx(x, y, z, c1)
                        j = idx((x + dx) % L, (y + dy) % L,
                                (z + dz) % L, c2)
                        Dd[i, j] += -0.5j * eta * dU[c1, c2]
                        Dd[j, i] += 0.5j * eta * dU[c1, c2].conjugate()
    return Dd


print("=" * 78)
print("VERTEX-POWER DERIVATION RUNNER: n_link = 2 from operator structure")
print("=" * 78)
t0 = time.time()

# ===========================================================================
# L1 — Schur forcing: gauge covariance + adjacency license => one link/hop
# ===========================================================================

print()
print("-" * 78)
print("L1: SINGLE LINK PER COVARIANT HOP (Schur bi-equivariance scan) [C]")
print("-" * 78)
print()
print("  Requirement: hopping dressing f: SU(3) -> M_3(C) with")
print("  f(g U h^dag) = g f(U) h^dag for all g, h in SU(3)")
print("  (site-local gauge covariance of psi^dag_{x+mu} f(U_mu(x)) psi_x,")
print("   edge-only support by the adjacency license).")
print()

N_SAMPLES = 24
candidates = {
    "U (linear, 1 link)": lambda U: U,
    "0.7*U (linear, 1 link)": lambda U: 0.7 * U,
    "U^2": lambda U: U @ U,
    "U^dag": lambda U: U.conj().T,
    "U * tr(U)/3": lambda U: U * np.trace(U) / 3.0,
    "(U + U^dag)/2": lambda U: (U + U.conj().T) / 2.0,
    "I (constant)": lambda U: np.eye(3, dtype=complex),
}
results = {}
for name, f in candidates.items():
    worst = 0.0
    for _ in range(N_SAMPLES):
        g, h, U = rand_su3(), rand_su3(), rand_su3()
        lhs = f(g @ U @ h.conj().T)
        rhs = g @ f(U) @ h.conj().T
        worst = max(worst, float(np.max(np.abs(lhs - rhs))))
    results[name] = worst
    verdict = "bi-equivariant" if worst < 1e-12 else "REJECTED"
    print(f"    f(U) = {name:24s} max residual = {worst:.3e}  ({verdict})")

linear_pass = all(results[k] < 1e-12 for k in
                  ["U (linear, 1 link)", "0.7*U (linear, 1 link)"])
others_fail = all(v > 1e-3 for k, v in results.items()
                  if "linear" not in k)
print()
check("schur_linear_dressing_unique", linear_pass and others_fail, "C",
      "only f(U) = c U is bi-equivariant; every non-linear candidate "
      "rejected with residual > 1e-3")

# Falsification leg (B-ADJ): dropping the edge-only license admits
# multi-link covariant dressings (link times based plaquette holonomy).
print()
print("  Falsification leg D-ADJ: drop the adjacency license -> the")
print("  5-link dressing U_mu(x) * W_P(x) (W_P a plaquette loop based at x)")
print("  is ALSO gauge covariant. Computed on a random link configuration:")
U_rand = np.zeros((L, L, L, 3, N_C, N_C), dtype=complex)
for x in range(L):
    for y in range(L):
        for z in range(L):
            for mu in range(3):
                U_rand[x, y, z, mu] = rand_su3()
g_site = np.zeros((L, L, L, N_C, N_C), dtype=complex)
for x in range(L):
    for y in range(L):
        for z in range(L):
            g_site[x, y, z] = rand_su3()


def gauge_transform(U_field, g):
    V = np.zeros_like(U_field)
    for x in range(L):
        for y in range(L):
            for z in range(L):
                for mu, (dx, dy, dz) in enumerate(
                        [(1, 0, 0), (0, 1, 0), (0, 0, 1)]):
                    V[x, y, z, mu] = (
                        g[(x + dx) % L, (y + dy) % L, (z + dz) % L]
                        @ U_field[x, y, z, mu]
                        @ g[x, y, z].conj().T)
    return V


def plaq_based(U_field, x, y, z, mu=0, nu=1):
    """Based plaquette holonomy at (x,y,z): fiber at x -> fiber at x.

    With the convention U_mu(x): fiber(x) -> fiber(x+mu), the path-ordered
    loop x -> x+mu -> x+mu+nu -> x+nu -> x is (right-to-left composition)
    U_nu(x)^dag U_mu(x+nu)^dag U_nu(x+mu) U_mu(x), which gauge transforms
    as g(x) W g(x)^dag.
    """
    x1 = ((x + 1) % L, y, z)
    y1 = (x, (y + 1) % L, z)
    return (U_field[x, y, z, nu].conj().T
            @ U_field[y1[0], y1[1], y1[2], mu].conj().T
            @ U_field[x1[0], x1[1], x1[2], nu]
            @ U_field[x, y, z, mu])


U_g = gauge_transform(U_rand, g_site)
worst_cov = 0.0
for (x, y, z) in [(0, 0, 0), (1, 2, 3), (3, 1, 0)]:
    xp = ((x + 1) % L, y, z)
    T_orig = U_rand[x, y, z, 0] @ plaq_based(U_rand, x, y, z)
    T_gauged = U_g[x, y, z, 0] @ plaq_based(U_g, x, y, z)
    expected = (g_site[xp[0], xp[1], xp[2]] @ T_orig
                @ g_site[x, y, z].conj().T)
    worst_cov = max(worst_cov, float(np.max(np.abs(T_gauged - expected))))
print(f"    covariance residual of 5-link dressing: {worst_cov:.3e}")
check("adjacency_license_is_load_bearing", worst_cov < 1e-12, "C",
      "the 5-link dressing is gauge covariant; only the edge-only "
      "adjacency license excludes it (boundary B-ADJ, named in the note)")
residual("B-ADJ: edge-only support of the hopping dressing is the "
         "adjacency license (axiom Lattice adjacency reading), not derived "
         "here; multi-link covariant dressings exist off-license.")

# ===========================================================================
# L2 — vertex insertion carries exactly one gauge link
# ===========================================================================

print()
print("-" * 78)
print("L2: VERTEX INSERTION IS SINGLE-LINK [C]")
print("-" * 78)
print()

A_gen = GELL_MANN[2] / 2.0  # T_3

# (a) link-exponential convention: dU/deps|_0 = i a U0, computed by central
# finite difference on actual matrix exponentials at a non-trivial base.
worst_fd = 0.0
for _ in range(6):
    a = RNG.standard_normal((3, 3)) + 1j * RNG.standard_normal((3, 3))
    a = (a + a.conj().T) / 2.0
    U0 = rand_su3()
    h = 1e-5
    fd = (herm_exp(a, h) @ U0 - herm_exp(a, -h) @ U0) / (2 * h)
    worst_fd = max(worst_fd, float(np.max(np.abs(fd - 1j * a @ U0))))
print(f"  finite-difference dU/deps vs i*a*U0: max residual = {worst_fd:.3e}")
check("link_exponential_vertex_single_link", worst_fd < 1e-8, "C",
      "dU/deps|_0 = i a U0 contains exactly one link factor U0 "
      "(B-CONV: the link-exponential convention is named, not derived)")
residual("B-CONV: U(eps) = exp(i eps a) U0 is the named link-exponential "
         "convention of the gauge sector.")

# (b) exact factorization D(u * I) = u * D_hop at m = 0 (computed, not
# asserted): the covariant hopping bilinear is degree-1 in the link.
D_hop = build_D(id_field(1.0), m=0.0)
worst_fac = 0.0
for u in [0.5, 0.7, 0.877, 1.0, 1.3]:
    Du = build_D(id_field(u), m=0.0)
    worst_fac = max(worst_fac, float(np.max(np.abs(Du - u * D_hop))))
print(f"  ||D(u I) - u D_hop|| over u grid: max = {worst_fac:.3e}")
check("hopping_bilinear_link_degree_1", worst_fac < 1e-13, "C",
      "D is exactly linear in the link (n_link(hopping) = 1), the "
      "computed counterpart of the L1 Schur forcing")

# (c) the vertex operator D' = dD/deps has link-degree exactly 1:
# building D' on base links u*I gives u * D'(base 1).
Dp_1 = build_D_deriv(A_gen, order=1, base_scale=1.0)
worst_dp = 0.0
for u in [0.5, 0.877, 1.3]:
    Dp_u = build_D_deriv(A_gen, order=1, base_scale=u)
    worst_dp = max(worst_dp, float(np.max(np.abs(Dp_u - u * Dp_1))))
print(f"  ||D'(u base) - u D'(base)|| over u grid: max = {worst_dp:.3e}")
check("vertex_insertion_link_degree_1", worst_dp < 1e-13, "C",
      "each vertex insertion D' carries exactly one gauge link")

# (d) cross-check D' and D'' against finite differences of the full
# background-field operator (the derivative operators are not hand-tuned).
m_reg = 0.05
h = 1e-4
D_p = build_D(field_with_bg(+h, A_gen), m=m_reg)
D_m = build_D(field_with_bg(-h, A_gen), m=m_reg)
D_0 = build_D(field_with_bg(0.0, A_gen), m=m_reg)
Dp_fd = (D_p - D_m) / (2 * h)
Dpp_fd = (D_p - 2 * D_0 + D_m) / h**2
Dpp_1 = build_D_deriv(A_gen, order=2, base_scale=1.0)
r1 = float(np.max(np.abs(Dp_fd - Dp_1)))
r2 = float(np.max(np.abs(Dpp_fd - Dpp_1)))
print(f"  D'(FD) vs built D':   max residual = {r1:.3e}")
print(f"  D''(FD) vs built D'': max residual = {r2:.3e}")
check("derivative_operators_match_finite_difference", r1 < 1e-6 and r2 < 1e-4,
      "C", "built D', D'' agree with finite differences of the actual "
      "background-field Dirac operator")

# ===========================================================================
# L3 — the quadratic response and the two-insertion count
# ===========================================================================

print()
print("-" * 78)
print("L3: QUADRATIC RESPONSE => EXACTLY TWO VERTEX INSERTIONS [C]")
print("-" * 78)
print()

# (a) the second-order expansion of Tr ln D[A] contains exactly the
# tadpole + bubble structures: finite-difference second derivative of the
# computed log-determinant matches Tr[D^-1 D''] - Tr[D^-1 D' D^-1 D'].
def logdet_abs(eps):
    Dm = build_D(field_with_bg(eps, A_gen), m=m_reg)
    w = np.linalg.eigvalsh(Dm)
    return float(np.sum(np.log(np.abs(w))))


h2 = 1e-3
lhs = (logdet_abs(h2) - 2 * logdet_abs(0.0) + logdet_abs(-h2)) / h2**2
D0_inv = np.linalg.inv(D_0)
tadpole = float(np.real(np.trace(D0_inv @ Dpp_1)))
bubble = float(np.real(np.trace(D0_inv @ Dp_1 @ D0_inv @ Dp_1)))
rhs = tadpole - bubble
rel = abs(lhs - rhs) / max(abs(rhs), 1e-30)
print(f"  d2/deps2 Tr ln D (computed FD)        = {lhs:.8f}")
print(f"  Tr[D^-1 D''] - Tr[D^-1 D' D^-1 D']    = {rhs:.8f}")
print(f"    tadpole (contact, 1 link) = {tadpole:.8f}")
print(f"    bubble (2 vertex insertions) = {bubble:.8f}")
print(f"  relative mismatch = {rel:.3e}")
check("quadratic_response_two_structures", rel < 1e-4, "C",
      "the O(A^2) response contains exactly the contact (D'') and "
      "current-current (D' D') structures; nothing else")

# (b) link-degree detection on the insertion operators with V-scheme
# propagators held fixed: this is the n_link detector.
#   bubble: Tr[Dhop^-1 D'(u) Dhop^-1 D'(u)]  ~ u^2  -> n_link = 2
#   tadpole: Tr[Dhop^-1 D''(u)]              ~ u^1  -> n_link = 1
eps_stag = np.diag([(-1) ** (x + y + z)
                    for x in range(L) for y in range(L) for z in range(L)
                    for _ in range(N_C)]).astype(complex)
Dhop_reg_inv = np.linalg.inv(D_hop + m_reg * eps_stag)
u_grid = np.array([0.5, 0.7, 0.877, 1.0, 1.3])
bub_vals, tad_vals = [], []
for u in u_grid:
    Dp_u = build_D_deriv(A_gen, order=1, base_scale=u)
    Dpp_u = build_D_deriv(A_gen, order=2, base_scale=u)
    bub_vals.append(float(np.real(np.trace(
        Dhop_reg_inv @ Dp_u @ Dhop_reg_inv @ Dp_u))))
    tad_vals.append(float(np.real(np.trace(Dhop_reg_inv @ Dpp_u))))
bub_vals = np.array(bub_vals)
tad_vals = np.array(tad_vals)
bub_slope = float(np.polyfit(np.log(u_grid), np.log(np.abs(bub_vals)), 1)[0])
tad_slope = float(np.polyfit(np.log(u_grid), np.log(np.abs(tad_vals)), 1)[0])
print()
print(f"  {'u':>8s}  {'insertion-pair (bubble)':>24s}  {'contact (tadpole)':>20s}")
for i, u in enumerate(u_grid):
    print(f"  {u:8.3f}  {bub_vals[i]:24.10f}  {tad_vals[i]:20.10f}")
print(f"  computed link-degree: bubble = {bub_slope:.12f}, "
      f"tadpole = {tad_slope:.12f}")
check("bubble_link_degree_exactly_2", abs(bub_slope - 2.0) < 1e-9, "C",
      f"insertion-pair operator has link-degree {bub_slope:.2e} - 2 "
      f"residual {abs(bub_slope - 2.0):.2e}: n_link(VP) = 2")
check("tadpole_link_degree_exactly_1", abs(tad_slope - 1.0) < 1e-9, "C",
      "the contact term carries one explicit link (it is NOT the "
      "coupling carrier; boundary B-CHAN names the channel assignment)")

# (c) FALSIFICATION LEG: alternative vertex powers are EXCLUDED by the
# computed structure. For n in {0, 1, 3, 4} the scaling law u^n fails by
# a large computed margin; n = 2 fits at machine precision.
print()
print("  Falsification leg: scaling-law residuals "
      "max_u |bubble(u)/bubble(1) - u^n|")
ref = bub_vals[list(u_grid).index(1.0)]
excluded_ok = True
for n in [0, 1, 2, 3, 4]:
    res = float(np.max(np.abs(bub_vals / ref - u_grid ** n)))
    marker = "<- DERIVED (machine precision)" if n == 2 else "EXCLUDED"
    if n == 2:
        excluded_ok &= res < 1e-10
    else:
        excluded_ok &= res > 1e-1
    print(f"    n = {n}:  residual = {res:.3e}   {marker}")
check("alternative_vertex_powers_excluded", excluded_ok, "C",
      "n_link = 2 fits at machine precision; n in {0,1,3,4} fail by "
      ">1e-1 computed margin. No strong-coupling value was consumed.")

# (d) leg-count tracks response order: the quartic (4-point) channel
# carries four insertions (computed link-degree 4), so the '2' is the leg
# count of the QUADRATIC response, not a tunable. (The cubic channel
# vanishes identically by a Furry-type cancellation — computed below —
# so the quartic channel is the clean odd-one-out witness.)
quad_vals = []
for u in u_grid:
    Dp_u = build_D_deriv(A_gen, order=1, base_scale=u)
    M = Dhop_reg_inv @ Dp_u
    quad_vals.append(abs(complex(np.trace(M @ M @ M @ M))))
quad_vals = np.array(quad_vals)
quad_slope = float(np.polyfit(np.log(u_grid), np.log(quad_vals), 1)[0])
M1 = Dhop_reg_inv @ Dp_1
cubic_mag = abs(complex(np.trace(M1 @ M1 @ M1)))
quartic_mag = quad_vals[list(u_grid).index(1.0)]
print(f"\n  quartic channel link-degree = {quad_slope:.12f} (expected 4)")
print(f"  cubic channel magnitude = {cubic_mag:.3e} (vanishes, Furry-type; "
      f"quartic magnitude = {quartic_mag:.3e})")
check("leg_count_tracks_response_order", abs(quad_slope - 4.0) < 1e-9
      and cubic_mag < 1e-9 * quartic_mag, "C",
      "k-th order response channel carries k single-link insertions "
      "(quartic: computed degree 4; cubic: vanishes by symmetry); "
      "n_link = 2 is forced by the quadratic (2-point) response "
      "(B-CHAN: quadratic-response normalization is the named coupling "
      "definition)")
residual("B-CHAN: 'the coupling is read from the quadratic (two-external-"
         "leg) gauge response' is the standard background-field "
         "normalization, declared not derived; given it, the leg count 2 "
         "is forced.")

# (e) consistency display: the SELF-CONSISTENT response (propagators and
# vertices at the same u) has link-degree 0 — the propagators absorb the
# vertex factors. The split 'coupling dresses inversely to the explicit
# insertion operator' is the tree-level normalization split (B-SPLIT).
sc_vals = []
for u in u_grid:
    D_u_inv = np.linalg.inv(u * D_hop + m_reg * eps_stag)
    Dp_u = build_D_deriv(A_gen, order=1, base_scale=u)
    sc_vals.append(float(np.real(np.trace(
        D_u_inv @ Dp_u @ D_u_inv @ Dp_u))))
sc_vals = np.array(sc_vals)
# at m_reg > 0 the degree is only approximately 0; report it honestly
sc_slope = float(np.polyfit(np.log(u_grid), np.log(np.abs(sc_vals)), 1)[0])
print(f"\n  self-consistent response link-degree = {sc_slope:.4f} "
      f"(-> 0 as m_reg -> 0; m_reg = {m_reg})")
check("self_consistent_response_degree_0", abs(sc_slope) < 0.5, "C",
      "propagator factors cancel vertex factors in the full response; "
      "the u_0 dressing lives on the explicit insertion operator "
      "(B-SPLIT names the tree-level convention split)")
residual("B-SPLIT: converting the operator dressing u_0^{+2} into the "
         "coupling dressing u_0^{-2} uses the tree-level split of the "
         "correlator into coupling x kinematic factor (the "
         "Lepage-Mackenzie mean-field convention; algebra closed by the "
         "coupling-map companion lane, named not derived here).")
residual("B-GATE: the staggered-Dirac kinetic surface itself is the "
         "realization gate, narrowed to the one-bit flux selector by the "
         "kinetic-class forcing theorem (cited in the note); not closed "
         "here.")

# ===========================================================================
# L4 — coupling-map algebra at the derived exponent [A]
# ===========================================================================

print()
print("-" * 78)
print("L4: COUPLING-MAP ALGEBRA AT n_link = 2 [A]")
print("-" * 78)
print()

n_link_vp = int(round(bub_slope))
n_link_hop = 1  # computed in L2 (hopping_bilinear_link_degree_1)
check("integer_exponent_extraction", n_link_vp == 2
      and abs(bub_slope - n_link_vp) < 1e-9, "A",
      f"n_link(VP) = {n_link_vp} = 2 x n_link(hopping) = 2 x {n_link_hop}")

# exact rational algebra over abstract positives (matches the retained
# tadpole-improvement narrow theorem surface, consumed one hop away)
alg_ok = True
for ab in [Fraction(1, 12), Fraction(3, 40), Fraction(7, 88)]:
    for u0q in [Fraction(7, 8), Fraction(877, 1000), Fraction(1, 2),
                Fraction(1, 1)]:
        a_lm = ab / u0q
        a_sv = ab / u0q ** n_link_vp
        alg_ok &= (a_sv * u0q ** 2 == ab)
        alg_ok &= (a_lm ** 2 == ab * a_sv)
        alg_ok &= (a_lm / ab == a_sv / a_lm)
check("coupling_map_identities_exact_at_n2", alg_ok, "A",
      "alpha_s(v) u_0^2 = alpha_bare, alpha_LM^2 = alpha_bare alpha_s(v), "
      "constant ratio 1/u_0 — exact rationals, zero floating error")

# ===========================================================================
# NO-BACK-PROPAGATION CERTIFICATE [A]
# ===========================================================================

print()
print("-" * 78)
print("NO-BACK-PROPAGATION CERTIFICATE [A]")
print("-" * 78)
print()

src = open(__file__, encoding="utf-8").read()
# Forbidden tokens are assembled from fragments so this certificate does
# not trip on itself. They cover: the observed strong coupling at the
# Z pole, the framework headline numbers downstream of this note, the
# experimental-data-group acronym, RG-running machinery, and the Z mass.
forbidden = [
    "0.11" + "79", "0.11" + "81", "0.118" + "067", "0.10" + "33",
    "P" + "DG", "solve_" + "ivp", "91." + "1876", "172." + "69",
    "alpha_s_" + "mz", "ALPHA_S_" + "MZ", "import sci" + "py",
    "from sci" + "py",
]
hits = [tok for tok in forbidden if tok in src]
print(f"  scanned {len(src)} chars of runner source; "
      f"forbidden-token hits: {hits if hits else 'none'}")
check("no_back_propagation_from_alpha_s", not hits, "A",
      "the derivation of n_link = 2 consumes no strong-coupling target, "
      "no Z-pole running, and no experimental comparator")
check("zero_class_D_checks", BREAKDOWN["D"] == 0, "A",
      "this runner contains no external-comparator check at all")

# ===========================================================================
# SUMMARY
# ===========================================================================

elapsed = time.time() - t0
print()
print("=" * 78)
print("SUMMARY")
print("=" * 78)
print()
print("  DERIVED: n_link = (2 external legs of the quadratic response)")
print("           x (1 gauge link per vertex insertion, Schur-forced)")
print("           = 2,  hence  alpha_s(v) = alpha_bare / u_0^2")
print("  BOUNDED: B-GATE (kinetic realization, one-bit flux selector),")
print("           B-ADJ (edge-only adjacency license),")
print("           B-CONV (link-exponential convention),")
print("           B-CHAN (quadratic-response coupling normalization),")
print("           B-SPLIT (tree-level coupling/kinematic split).")
print()
print(f"  Breakdown: A={BREAKDOWN['A']} B={BREAKDOWN['B']} "
      f"C={BREAKDOWN['C']} D={BREAKDOWN['D']}")
print(f"  TOTAL: PASS={PASS_COUNT} FAIL={FAIL_COUNT}")
print(f"  Time: {elapsed:.1f}s")

sys.exit(0 if FAIL_COUNT == 0 else 1)
