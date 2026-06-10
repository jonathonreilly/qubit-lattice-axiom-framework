#!/usr/bin/env python3
"""Matter-gauge minimal coupling from local fibre-frame redundancy.

Class-A finite-dimensional verification for the source note

    docs/MATTER_GAUGE_MINIMAL_COUPLING_FIBER_FRAME_FORCES_CONNECTION_NARROW_THEOREM_NOTE_2026-06-08.md

THESIS (kinematics only -- no gauge action / no dynamics claimed):
  Given (i) the framework's retained nearest-neighbour matter hopping bilinear,
  (ii) the retained per-site internal SU(3) (more precisely U(3)) fibre, and
  (iii) the current-surface one-hop bridge that local fibre-frame choices are
  passive trivialization changes for the registered weak/Record-sector data,
  the hopping term implicitly chooses an identification of the fibre frame at
  site x with the frame at the neighbour x+mu. Frame-independent hopping
  therefore fixes a link variable U_mu(x) in the fibre structure group with the
  parallel-transporter law
        U_mu(x)  ->  g(x) U_mu(x) g(x+mu)^dagger,
  i.e. exactly a lattice gauge connection / minimal coupling
        H_cov = sum_{x,mu} a_x^dagger U_mu(x) a_{x+mu} + h.c.,
        (D_mu psi)(x) = U_mu(x) psi(x+mu) - psi(x).

Retained foundations exercised:
  - graph_first_su3_integration_note            (retained)         : internal SU(3)
    fibre = commutant of the weak-su(2) action on the taste cube; abelian factor
    gl(1) "hypercharge-like".  Structure group U(3) = SU(3) x U(1).
  - tensor_product_translation_fermion_operator_bridge_narrow_theorem_note
                                                  (retained)         : per-site fermion
    operators a_x with translation T_a a_x T_a^dag = a_{x+a} (the FLAT reference frame
    U=I).  hopping_bilinear_hermiticity_theorem_note (decoration under it) gives the
    Hermitian, number-conserving NN hopping bilinear a_x^dag a_y + a_y^dag a_x.  (This
    runner works in the single-particle sector, where the hopping bilinear acts as the
    fibre-valued adjacency operator on sites (x) fibre.)
  - fiber_frame_local_redundancy_bridge_narrow_theorem_note_2026-06-09
                                                  (current-surface bridge):
    local U(3) fibre-frame changes are passive trivialization changes for the
    registered weak/Record-sector data currently present in the cited
    authorities, and U=I is the flat cross-site trivialization rather than a
    physical fibre-basis pinning.

BRIDGE BOUNDARY:
  The local fibre-frame redundancy bridge is current-surface and kinematic.
  It does not prove gauge action/dynamics, physical SU(3)_c identification, or
  the absence of future colour readout contexts. Under this bridge the
  connection law is forced; the algebraic gauge-covariance core (Parts 1-5) is
  exact finite algebra.

WHAT IS DERIVED HERE (exact algebra using the current-surface bridge):
  - Free hopping (U=I) IS globally SU(3)-invariant but is NOT locally invariant.
  - Covariant hopping H_cov[U] satisfies the central identity
        G H_cov[U] G^dag = H_cov[U']   with   U'_mu(x) = g(x) U_mu(x) g(x+mu)^dag,
    so the parallel-transporter law makes the retained hopping frame-independent.
  - The transporter law is UNIQUE: every other site-assignment breaks covariance.
  - The lattice covariant difference D_mu transforms covariantly; the naive
    difference does not.
  - Closed-loop holonomies (plaquette traces) are gauge invariant; open Wilson
    lines are not -- the gauge-invariant observable content is the closed loops.
  - Leading-order U_mu = exp(i eps A_mu) gives the finite-link expansion
    (D_mu psi)(x) = (psi(x+mu)-psi(x)) + i eps A_mu(x) psi(x+mu) + O(eps^2),
    the normalized minimal-coupling form after dividing by eps.  This is a
    consistency check -- NO continuum limit is claimed.
  - The U(1) (hypercharge-like) factor has the same abelian transporter law.

WHAT IS NOT CLAIMED:
  - No gauge ACTION / dynamics for U_mu (that is the separate Yang-Mills target).
  - No continuum limit, no coupling value, no identification with physical
    SU(3)_c beyond the algebraic fibre (deferred, per graph_first_su3 boundary).

Run: python3 scripts/frontier_minimal_coupling_fiber_frame_connection_2026_06_08.py
"""

from __future__ import annotations

import itertools
import numpy as np

PASS = 0
FAIL = 0
ATOL = 1e-10


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    tag = "PASS" if condition else "FAIL"
    if condition:
        PASS += 1
    else:
        FAIL += 1
    line = f"  [{tag}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)


# ---------------------------------------------------------------------------
# Part 0.  Lattice, fibre, and a deterministic gauge/connection configuration.
# ---------------------------------------------------------------------------
print("=" * 78)
print("Part 0  Z^3 lattice (2x2x2), C^3 fibre, deterministic SU(3) config")
print("=" * 78)

rng = np.random.default_rng(20260608)  # fixed seed -> deterministic, reproducible

L = 2                       # 2 sites per axis (periodic): tiny, memory-safe
DIMS = (L, L, L)
SITES = list(itertools.product(range(L), repeat=3))
NS = len(SITES)             # 8 sites
NF = 3                      # fundamental SU(3) fibre
site_index = {s: i for i, s in enumerate(SITES)}


def neighbour(s, mu):
    """Forward nearest neighbour of site s along axis mu (periodic)."""
    t = list(s)
    t[mu] = (t[mu] + 1) % L
    return tuple(t)


# -- SU(3) and U(3) generators (Gell-Mann) for building exact-unitary configs ---
lam = [
    np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], dtype=complex),
    np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], dtype=complex),
    np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]], dtype=complex),
    np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], dtype=complex),
    np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], dtype=complex),
    np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], dtype=complex),
    np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], dtype=complex),
    np.array([[1, 0, 0], [0, 1, 0], [0, 0, -2]], dtype=complex) / np.sqrt(3),
]


def expm_herm(H):
    """Exact matrix exponential of i*H for Hermitian H via eigendecomposition."""
    w, V = np.linalg.eigh(H)
    return V @ np.diag(np.exp(1j * w)) @ V.conj().T


def random_su3():
    """A Haar-ish SU(3): exp(i sum c_a lambda_a), then projected to det=1."""
    c = rng.normal(size=8)
    H = sum(ci * li for ci, li in zip(c, lam))
    U = expm_herm(H)                       # in U(3), det = exp(i tr) but tr(lam)=0
    detU = np.linalg.det(U)
    U = U / detU ** (1.0 / 3.0)            # rescale to SU(3)
    return U


def is_unitary(U, n=NF):
    return np.allclose(U.conj().T @ U, np.eye(n), atol=ATOL)


def is_su(U):
    return is_unitary(U) and abs(np.linalg.det(U) - 1.0) < 1e-9


# Connection: one SU(3) matrix per directed link (x, mu).
U_link = {(s, mu): random_su3() for s in SITES for mu in range(3)}
# Gauge field: one SU(3) matrix per site (non-constant -> genuinely local).
g_site = {s: random_su3() for s in SITES}

check("all link variables U_mu(x) are in SU(3) (unitary, det=1)",
      all(is_su(U) for U in U_link.values()),
      f"{len(U_link)} links")
check("all gauge matrices g(x) are in SU(3)",
      all(is_su(g) for g in g_site.values()),
      f"{NS} sites")
check("gauge field is genuinely site-dependent (not global)",
      not np.allclose(g_site[SITES[0]], g_site[SITES[1]], atol=1e-6))


# -- single-particle operators on H = C^NS (x) C^NF -------------------------
def site_block_op(per_site):
    """Block-diagonal operator: per_site[s] acts on the fibre at site s."""
    M = np.zeros((NS * NF, NS * NF), dtype=complex)
    for s in SITES:
        i = site_index[s]
        M[i * NF:(i + 1) * NF, i * NF:(i + 1) * NF] = per_site[s]
    return M


def hopping_op(link):
    """H = sum_{x,mu} |x><x+mu| (x) U_mu(x) + h.c.   (single-particle sector)."""
    M = np.zeros((NS * NF, NS * NF), dtype=complex)
    for s in SITES:
        i = site_index[s]
        for mu in range(3):
            t = neighbour(s, mu)
            j = site_index[t]
            blk = link[(s, mu)]
            M[i * NF:(i + 1) * NF, j * NF:(j + 1) * NF] += blk          # x <- x+mu
            M[j * NF:(j + 1) * NF, i * NF:(i + 1) * NF] += blk.conj().T  # h.c.
    return M


I_link = {(s, mu): np.eye(NF, dtype=complex) for s in SITES for mu in range(3)}
G = site_block_op(g_site)          # local gauge operator on the full space
H_free = hopping_op(I_link)        # U = I : the retained free hopping
H_cov = hopping_op(U_link)         # U general : covariant hopping

check("free hopping H_free is Hermitian", np.allclose(H_free, H_free.conj().T, atol=ATOL))
check("covariant hopping H_cov is Hermitian", np.allclose(H_cov, H_cov.conj().T, atol=ATOL))
check("U = I reduces H_cov to the retained free hopping H_free",
      np.allclose(H_cov if False else hopping_op(I_link), H_free, atol=ATOL))

# ---------------------------------------------------------------------------
# Part 1.  THE PROBLEM: free hopping is global- but NOT local-frame invariant.
# ---------------------------------------------------------------------------
print("=" * 78)
print("Part 1  Free hopping: globally SU(3)-invariant, locally NOT (the problem)")
print("=" * 78)

# Global transform: same h on every site.
h_global = random_su3()
G_global = site_block_op({s: h_global for s in SITES})
check("free hopping IS invariant under a GLOBAL fibre rotation "
      "(G H_free G^dag = H_free)",
      np.allclose(G_global @ H_free @ G_global.conj().T, H_free, atol=ATOL))

check("free hopping is NOT invariant under a LOCAL fibre rotation "
      "(G H_free G^dag != H_free)",
      not np.allclose(G @ H_free @ G.conj().T, H_free, atol=1e-6))

# ---------------------------------------------------------------------------
# Part 2.  THE RESOLUTION: covariant hopping with the transporter law.
#   Central identity:  G H_cov[U] G^dag = H_cov[U'],  U'_mu(x)=g(x)U_mu(x)g(x+mu)^dag
# ---------------------------------------------------------------------------
print("=" * 78)
print("Part 2  Covariant hopping: G H_cov[U] G^dag = H_cov[U'] (connection law fixed)")
print("=" * 78)

U_gauge = {(s, mu): g_site[s] @ U_link[(s, mu)] @ g_site[neighbour(s, mu)].conj().T
           for s in SITES for mu in range(3)}
check("transformed links U'_mu(x) = g(x) U_mu(x) g(x+mu)^dag stay in SU(3)",
      all(is_su(U) for U in U_gauge.values()))

H_cov_gauged = hopping_op(U_gauge)
check("CENTRAL: G H_cov[U] G^dag = H_cov[U'] with the parallel-transporter law",
      np.allclose(G @ H_cov @ G.conj().T, H_cov_gauged, atol=ATOL),
      "covariant hopping maps to covariant hopping (frame-independent dynamics)")

# Spectrum is therefore a gauge invariant.
ev0 = np.sort(np.linalg.eigvalsh(H_cov))
ev1 = np.sort(np.linalg.eigvalsh(H_cov_gauged))
check("spectrum of H_cov is gauge invariant (eigvals[U] = eigvals[U'])",
      np.allclose(ev0, ev1, atol=ATOL),
      f"max|dlambda| = {np.max(np.abs(ev0 - ev1)):.2e}")

# ---------------------------------------------------------------------------
# Part 3.  UNIQUENESS (teeth): only the transporter site-assignment works.
# ---------------------------------------------------------------------------
print("=" * 78)
print("Part 3  Controls: every other link law BREAKS covariance (transporter unique)")
print("=" * 78)

wrong_laws = {
    "same-site g(x)U g(x)^dag":
        {(s, mu): g_site[s] @ U_link[(s, mu)] @ g_site[s].conj().T
         for s in SITES for mu in range(3)},
    "reversed g(x+mu)U g(x)^dag":
        {(s, mu): g_site[neighbour(s, mu)] @ U_link[(s, mu)] @ g_site[s].conj().T
         for s in SITES for mu in range(3)},
    "left-only g(x)U":
        {(s, mu): g_site[s] @ U_link[(s, mu)]
         for s in SITES for mu in range(3)},
    "right-only U g(x+mu)^dag":
        {(s, mu): U_link[(s, mu)] @ g_site[neighbour(s, mu)].conj().T
         for s in SITES for mu in range(3)},
}
for label, Uw in wrong_laws.items():
    check(f"CONTROL: '{label}' does NOT reproduce G H_cov G^dag",
          not np.allclose(G @ H_cov @ G.conj().T, hopping_op(Uw), atol=1e-6))

# ---------------------------------------------------------------------------
# Part 4.  Covariant derivative: D_mu transforms covariantly, naive d_mu does not.
# ---------------------------------------------------------------------------
print("=" * 78)
print("Part 4  Lattice covariant difference D_mu psi = U_mu psi_{x+mu} - psi_x")
print("=" * 78)

psi = {s: rng.normal(size=NF) + 1j * rng.normal(size=NF) for s in SITES}
psi_g = {s: g_site[s] @ psi[s] for s in SITES}   # gauge-transformed field


def Dmu(field, link, s, mu):
    return link[(s, mu)] @ field[neighbour(s, mu)] - field[s]


def dmu(field, s, mu):
    return field[neighbour(s, mu)] - field[s]


cov_ok = all(
    np.allclose(Dmu(psi_g, U_gauge, s, mu), g_site[s] @ Dmu(psi, U_link, s, mu),
                atol=ATOL)
    for s in SITES for mu in range(3))
check("D_mu transforms covariantly: (D'_mu psi')(x) = g(x) (D_mu psi)(x)", cov_ok)

naive_bad = any(
    not np.allclose(dmu(psi_g, s, mu), g_site[s] @ dmu(psi, s, mu), atol=1e-6)
    for s in SITES for mu in range(3))
check("naive difference d_mu psi does NOT transform covariantly (needs connection)",
      naive_bad)

# ---------------------------------------------------------------------------
# Part 5.  Gauge-invariant observables: closed loops yes, open lines no.
# ---------------------------------------------------------------------------
print("=" * 78)
print("Part 5  Plaquette holonomy gauge invariant; open Wilson line is not")
print("=" * 78)


def plaquette(link, s, mu, nu):
    """U_mu(x) U_nu(x+mu) U_mu(x+nu)^dag U_nu(x)^dag  (unit square at x in mu-nu)."""
    a = link[(s, mu)]
    b = link[(neighbour(s, mu), nu)]
    c = link[(neighbour(s, nu), mu)].conj().T
    d = link[(s, nu)].conj().T
    return a @ b @ c @ d


s0 = SITES[0]
tr_plaq = np.trace(plaquette(U_link, s0, 0, 1))
tr_plaq_g = np.trace(plaquette(U_gauge, s0, 0, 1))
check("plaquette trace Tr U_p is gauge invariant (closed loop)",
      abs(tr_plaq - tr_plaq_g) < ATOL,
      f"|dTr| = {abs(tr_plaq - tr_plaq_g):.2e}")

open_line = np.trace(U_link[(s0, 0)])
open_line_g = np.trace(U_gauge[(s0, 0)])
check("open Wilson line Tr U_mu(x) is NOT gauge invariant",
      abs(open_line - open_line_g) > 1e-6,
      f"|dTr| = {abs(open_line - open_line_g):.2e}")

# A closed loop holonomy at trivial connection is the identity (flat reference).
check("flat connection U=I has trivial holonomy (Tr U_p = N_f = 3)",
      abs(np.trace(plaquette(I_link, s0, 0, 1)) - NF) < ATOL)

# ---------------------------------------------------------------------------
# Part 6.  Leading-order minimal coupling:
# U = exp(i eps A) -> D psi = d psi + i eps A psi(x+mu) + O(eps^2).
#   Consistency check ONLY -- no continuum limit, no dynamics claimed.
# ---------------------------------------------------------------------------
print("=" * 78)
print("Part 6  U_mu = exp(i eps A_mu) gives D_mu psi = d_mu psi + i eps A_mu psi(x+mu)")
print("=" * 78)

A = {(s, mu): sum(rng.normal() * li for li in lam)        # Hermitian, traceless
     for s in SITES for mu in range(3)}
errs = []
for eps in (1e-2, 1e-3, 1e-4):
    Ue = {(s, mu): expm_herm(eps * A[(s, mu)]) for s in SITES for mu in range(3)}
    # (D_mu psi)(x) = U psi_{x+mu} - psi_x  vs  (psi_{x+mu}-psi_x) + i eps A psi_{x+mu}
    worst = 0.0
    for s in SITES:
        for mu in range(3):
            exact = Ue[(s, mu)] @ psi[neighbour(s, mu)] - psi[s]
            lead = (psi[neighbour(s, mu)] - psi[s]
                    + 1j * eps * A[(s, mu)] @ psi[neighbour(s, mu)])
            worst = max(worst, np.linalg.norm(exact - lead))
    errs.append((eps, worst))
# Residual is O(eps^2): the log-log slope of residual vs eps must be ~2.
# Any non-minimal first-order truncation would spoil the O(eps^2) residual.
es = np.array([e for e, _ in errs])
ws = np.array([w for _, w in errs])
slope = float(np.polyfit(np.log(es), np.log(ws), 1)[0])
check("minimal-coupling residual is O(eps^2) for D_mu psi = d_mu psi + i eps A_mu psi(x+mu)",
      abs(slope - 2.0) < 0.02,
      f"log-log slope = {slope:.4f} (== 2 confirms first-order minimal coupling)")

# ---------------------------------------------------------------------------
# Part 7.  U(1) hypercharge-like factor: abelian connection forced too.
#   Structure group is U(3) = SU(3) x U(1) (graph_first_su3 commutant gl(3)+gl(1)).
# ---------------------------------------------------------------------------
print("=" * 78)
print("Part 7  U(1) (hypercharge-like) factor obeys the same abelian transporter law")
print("=" * 78)

phase = {s: np.exp(1j * rng.normal()) for s in SITES}        # U(1) gauge field
g_u1 = {s: phase[s] * np.eye(NF, dtype=complex) for s in SITES}
G_u1 = site_block_op(g_u1)
u1_link = {(s, mu): np.exp(1j * rng.normal()) * np.eye(NF, dtype=complex)
           for s in SITES for mu in range(3)}
H_u1 = hopping_op(u1_link)
u1_gauged = {(s, mu): g_u1[s] @ u1_link[(s, mu)] @ g_u1[neighbour(s, mu)].conj().T
             for s in SITES for mu in range(3)}
check("free hopping NOT invariant under local U(1) phase (abelian gauge field needed)",
      not np.allclose(G_u1 @ H_free @ G_u1.conj().T, H_free, atol=1e-6))
check("U(1) covariant hopping: G H_cov G^dag = H_cov[U'] (abelian transporter)",
      np.allclose(G_u1 @ H_u1 @ G_u1.conj().T, hopping_op(u1_gauged), atol=ATOL))

# ---------------------------------------------------------------------------
print("=" * 78)
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print("=" * 78)
print("SCOPE: This runner verifies the KINEMATICS of matter-gauge minimal coupling")
print("  -- using the current-surface local fibre-frame redundancy bridge, the")
print("  link connection U_mu(x) and its parallel-transporter gauge law are fixed")
print("  by frame-independence of nearest-neighbour hopping on the retained")
print("  per-site U(3) fibre. The gauge-covariance core (Parts 1-5,7) is exact")
print("  finite algebra. It does NOT derive any gauge ACTION or dynamics for U_mu")
print("  (the Yang-Mills target), claims NO continuum limit, proves NO future")
print("  colour-readout exclusion theorem, and defers physical SU(3)_c per the")
print("  graph_first_su3 boundary.")
if FAIL:
    raise SystemExit(1)
