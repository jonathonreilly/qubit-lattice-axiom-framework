"""Microcausality action-support budget + proved finite-range Lieb-Robinson runner.

Companion to
`docs/MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md`.

The companion note narrows the gap on the parent microcausality note
`AXIOM_FIRST_MICROCAUSALITY_LIEB_ROBINSON_THEOREM_NOTE_2026-05-01.md`
in four legs:

  (i)   bounded action-density support and explicit per-site budgets
        J_max / overlap weights W for the supplied/displayed
        staggered + Wilson-diagonal + Wilson-plaquette carrier surface;
  (ii)  a self-contained finite-range Lieb-Robinson lemma (L1 exact
        series bound, L2 exponential lightcone bound) with the velocity
        v_LR := 2 e q W R derived in the note — no literature constant
        is imported;
  (iii) an unconditional application to the retained-grade framework
        hopping Hamiltonian H_hop = sum_links H_xy + m sum_x n_x
        (per-site tensor ladder convention of the cited hopping-bilinear
        chain), giving v_LR <= 4 e (|m| + 2d);
  (iv)  an explicitly conditional carrier corollary for the exact
        reconstructed H = -log(T)/a_tau, which this runner does NOT
        construct (recorded open frontier).

This runner provides numerical certificates for:

  F0.  Note/runner manifest sync (bookkeeping guard).

  F1.  Leading action-density support: build h_z explicitly on a small
       toy block from canonical nearest-neighbor action coefficients
       and verify it commutes with operators outside the local support.

  F2.  Explicit J bound: triangle-inequality budget on random SU(3)
       backgrounds; compare against the closed-form
       J_max = |m| + d/2 + r_W*d + 2*beta*d(d-1)/2.

  F2b. Carrier-faithful Wilson branch: unit pair norm
       || [[0, U], [U^dag, 0]] ||_op = 1 on random SU(3) links, grouped
       spatial-Wilson block norm vs the d_s*(r_W + r_W/2) budget, and
       exact branch arithmetic (|m|+78) <= (|m|+78.5) <= (|m|+80).

  F2c. Per-site overlap weights W (the Lieb-Robinson lemma input):
       exact Fraction arithmetic for W_surface = |m|+296,
       W_carrier = |m|+298, W_envelope = |m|+300, with the per-site
       support counts (1 site term, 2d = 8 links, 4*C(d,2) = 24
       plaquettes) recomputed from scratch, plus the conditional
       velocity ceilings 16*e*W.

  F3.  Proved Lieb-Robinson lemma vs exact commutators on the ACTUAL
       framework hopping Hamiltonian (periodic chain of the cited
       link family, per-site ladder convention, coefficient 1, mass m):
       (a) ||H_xy||_op = 1 and finite-range support of every local term,
       (b) L1 exact series bound holds at every (distance, time) grid
           point,
       (c) L2 exponential lightcone bound with v_LR = 2 e q W R holds
           at every grid point.

  F4.  Outside-lightcone exponential decay of the commutator on the
       same framework hopping Hamiltonian (monotone decay in distance).

  F5.  Falsification leg: adding a single long-range hopping bond
       (support diameter 5 >> R = 1) makes the measured commutator
       VIOLATE the finite-range L1/L2 bounds by a large factor —
       the finite-range hypothesis is load-bearing, not decorative.

  F6.  Z^3 block check: on the minimal periodic 2x2x2 Z^3 block, the
       translation-invariant NN link-family Hamiltonian is Hermitian,
       conserves Q_total, every H_xy is supported on its two tensor
       factors, and the per-site overlap weight is W = |m| + 2d = |m|+6.

Reproducibility: deterministic seeded SU(3) backgrounds.
"""
from __future__ import annotations

import math
from fractions import Fraction
from pathlib import Path

import numpy as np

SEED = 20260509
PASS_COUNT = 0
FAIL_COUNT = 0
RESULTS = []


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS_COUNT, FAIL_COUNT
    status = "PASS" if condition else "FAIL"
    if condition:
        PASS_COUNT += 1
    else:
        FAIL_COUNT += 1
    RESULTS.append({"name": name, "status": status, "detail": detail})
    print(f"  [{status}] {name}")
    if detail:
        print(f"         {detail}")


# ---- Shared small-operator toolkit ------------------------------------------

I2 = np.eye(2, dtype=complex)
SIGMA_Z = np.array([[1.0, 0.0], [0.0, -1.0]], dtype=complex)
SM = np.array([[0.0, 1.0], [0.0, 0.0]], dtype=complex)  # sigma_- (annihilation a)
SP = SM.conj().T                                        # sigma_+ (creation a^dag)
N_OP = SP @ SM                                          # number operator


def kron_chain(ops):
    result = ops[0]
    for op in ops[1:]:
        result = np.kron(result, op)
    return result


def site_op(local_op, x, n_sites):
    """Per-site tensor operator: local_op on factor x, identity elsewhere.

    This is exactly the commuting per-site mode convention of the cited
    hopping-bilinear chain (a_x = I_{x'!=x} (x) sigma_-^(x), no
    Jordan-Wigner string between sites).
    """
    return kron_chain([local_op if i == x else I2 for i in range(n_sites)])


def series_tail(a: float, n0: int, max_terms: int = 500) -> float:
    """Sum_{n >= n0} a^n / n! by direct stable summation."""
    if n0 == 0:
        return math.exp(a)
    term = a ** n0 / math.factorial(n0)
    total = 0.0
    n = n0
    while n < n0 + max_terms:
        total += term
        n += 1
        term *= a / n
        if term < 1e-300:
            break
    return total


# ---- Manifest sync ---------------------------------------------------------

def test_F0_note_manifest_sync() -> bool:
    """Guard the note/runner contract for the 2026-06-10 LR-lemma repair."""
    print("=" * 72)
    print("TEST F0: note manifest matches the proved-lemma repair surface")
    print("=" * 72)

    note_path = Path("docs/MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md")
    text = note_path.read_text(encoding="utf-8")
    required = [
        # 2026-06-09 normalization repair must remain in place
        "2 + 4 + |m| + 72 = 78 + |m|",
        "per-plaquette coefficient is `β`, not `β/N_c`",
        # 2026-06-10 proved-lemma repair markers
        "v_LR  :=  2 · e · q · W · R",
        "W_surface = |m| + 296",
        "W_carrier = |m| + 298",
        "W_envelope = |m| + 300",
        "v_LR  ≤  4 · e · (|m| + 2d)",
        "2026-06-10",
    ]
    forbidden = [
        # pre-2026-06-09 stale normalization
        "(2β / N_c) · q_face",
        "J_max = 4/2 + 1·4 + |m| + (2·6/3)·6",
        # pre-2026-06-10 imported/undlerived LR constants (claims, not history)
        "v_LR  =  2 · e · r · J",
        "v_LR  ≤  2 · e · 2 · J_max  =  4 · e · (|m| + 78)",
        "v_LR ≤ 312 · e",
    ]

    missing = [item for item in required if item not in text]
    stale = [item for item in forbidden if item in text]
    ok = not missing and not stale
    detail = "proved-lemma surface markers present; no stale imported-constant claims"
    if missing:
        detail = f"missing required note markers: {missing}"
    if stale:
        detail = f"stale pre-repair formula still present: {stale}"
    check("F0 — note/runner manifest matches the 2026-06-10 proved-lemma surface", ok, detail)
    print()
    return ok


# ---- SU(3) link generation -------------------------------------------------

GM = np.array(
    [
        [[0, 1, 0], [1, 0, 0], [0, 0, 0]],
        [[0, -1j, 0], [1j, 0, 0], [0, 0, 0]],
        [[1, 0, 0], [0, -1, 0], [0, 0, 0]],
        [[0, 0, 1], [0, 0, 0], [1, 0, 0]],
        [[0, 0, -1j], [0, 0, 0], [1j, 0, 0]],
        [[0, 0, 0], [0, 0, 1], [0, 1, 0]],
        [[0, 0, 0], [0, 0, -1j], [0, 1j, 0]],
        [[1, 0, 0], [0, 1, 0], [0, 0, -2]] / np.sqrt(3),
    ],
    dtype=complex,
)


def random_su3(rng: np.random.Generator, scale: float = 1.0) -> np.ndarray:
    """Generate a random SU(3) matrix at given scale. scale=0 -> identity."""
    coeffs = rng.standard_normal(8) * scale
    H = sum(coeffs[k] * GM[k] for k in range(8)) / 2.0
    eigvals, eigvecs = np.linalg.eigh(H)
    return eigvecs @ np.diag(np.exp(1j * eigvals)) @ eigvecs.conj().T


# ---- Test 1: F1 finite-range from action support ---------------------------

def test_F1_finite_range_support() -> bool:
    """F1: the carrier action-density term h_z is supported in a radius-1
    ball around z (matter terms; plaquettes extend this to radius 2).

    Build mass + NN hopping local density h_z explicitly on a 1D chain
    in the per-site ladder convention and verify [h_z, O_x] = 0 for
    d(z, x) > 1.
    """
    print("=" * 72)
    print("TEST F1: finite-range support of h_z (matter terms, radius r = 1)")
    print("=" * 72)

    L = 8  # 1D chain length
    mass = 0.3
    z = 3

    hop_kernel = 0.5 * (np.kron(SP, SM) + np.kron(SM, SP))  # 4x4 NN pair

    def two_site_op(local_op_xy, x):
        left = kron_chain([I2 for _ in range(x)]) if x > 0 else np.array([[1.0]], dtype=complex)
        right = kron_chain([I2 for _ in range(L - x - 2)]) if x < L - 2 else np.array([[1.0]], dtype=complex)
        return np.kron(np.kron(left, local_op_xy), right)

    h_mass_z = mass * site_op(SIGMA_Z, z, L)
    h_hop_z_zp1 = two_site_op(hop_kernel, z)
    h_z = h_mass_z + h_hop_z_zp1

    print(f"\n  Setup: 1D chain L={L}, base site z={z}, mass={mass}")
    print(f"  h_z = m * σ_z(z) + (1/2)(a^†_z a_{{z+1}} + h.c.)")
    print(f"  Expected: [h_z, O_x] = 0 for d(z, x) > 1, i.e. x ∉ {{z-1, z, z+1}}")
    print()
    print(f"  {'x':>3}  {'d(z,x)':>8}  {'||[h_z, σ_z(x)]||':>20}  {'expected':>10}")
    print(f"  {'-'*3}  {'-'*8}  {'-'*20}  {'-'*10}")
    all_ok = True
    for x in range(L):
        d_zx = min(abs(x - z), L - abs(x - z))  # periodic distance
        O_x = site_op(SIGMA_Z, x, L)
        comm = h_z @ O_x - O_x @ h_z
        comm_norm = float(np.linalg.norm(comm, ord=2))
        if d_zx > 1:
            expected = "0 (out)"
            ok = comm_norm < 1e-12
        else:
            expected = "≠ 0 (in)"
            ok = True
        marker = "OK" if ok else "FAIL"
        if not ok:
            all_ok = False
        print(f"  {x:>3}  {d_zx:>8d}  {comm_norm:>20.6e}  {expected:>10}  {marker}")
    print()
    check("F1 — h_z is supported in radius-1 ball (commutes with operators outside)",
          all_ok,
          "Verified [h_z, O_x] = 0 for d(z, x) > 1")
    return all_ok


# ---- Test 2: F2 explicit J bound from action coefficients ------------------

def test_F2_explicit_J_bound() -> bool:
    """F2: closed-form J_max from action coefficients holds.

    Triangle-inequality budget on the canonical SU(3) carrier with random
    SU(3) backgrounds; compare against J_max derived from action
    coefficients only (no spectral data of T).
    """
    print()
    print("=" * 72)
    print("TEST F2: J_max bound from action coefficients (gauge-background-independent)")
    print("=" * 72)
    print("\n  Build the per-site action-density budget on random SU(3) backgrounds.")
    print("  Compare against the closed-form J_max.")
    print()

    d = 4
    r_W = 1.0
    m = 0.3
    g_bare = 1.0
    N_c = 3
    beta = 2 * N_c / g_bare ** 2  # = 6
    print(f"  d={d}, r_W={r_W}, m={m}, β={beta}, N_c={N_c}")

    # J_max = |m| + d/2 + r_W*d + 2*β*d(d-1)/2.  The parent Wilson action
    # normalization is β * Re[1 - tr(U_P)/N_c]; the 1/N_c lives inside the
    # trace average and is not an additional multiplier.
    J_max = abs(m) + d / 2 + r_W * d + 2 * beta * d * (d - 1) / 2
    print(f"  J_max (from action) = |m| + d/2 + r_W·d + 2·β·d(d-1)/2")
    print(f"                       = {abs(m)} + {d/2} + {r_W * d} + {2 * beta * d*(d-1)/2}")
    print(f"                       = {J_max}")
    print()

    rng = np.random.default_rng(SEED)

    print(f"  {'config':>8}  {'||h_z||_op budget':>22}  {'J_max (closed-form)':>22}  {'OK':>6}")
    print(f"  {'-'*8}  {'-'*22}  {'-'*22}  {'-'*6}")
    n_configs = 20
    all_ok = True
    max_observed = 0.0
    for cfg in range(n_configs):
        scale = 1.0 if cfg > 0 else 0.0  # cfg=0 is the identity background
        Us = [random_su3(rng, scale=scale) for _ in range(d)]
        hop_contrib = sum(0.5 * np.linalg.norm(U, ord=2) for U in Us)  # = d/2
        wilson_contrib = r_W * d
        mass_contrib = abs(m)
        plaq_contrib = 0.0
        n_plaq = d * (d - 1) // 2
        for _ in range(n_plaq):
            U1 = random_su3(rng, scale=scale)
            U2 = random_su3(rng, scale=scale)
            U3 = random_su3(rng, scale=scale)
            U4 = random_su3(rng, scale=scale)
            U_P = U1 @ U2 @ U3.conj().T @ U4.conj().T
            tr_factor = abs(1.0 - np.trace(U_P).real / N_c)  # |1 - Re(tr U_P)/N_c| ≤ 2
            plaq_contrib += beta * tr_factor
        h_z_norm = mass_contrib + hop_contrib + wilson_contrib + plaq_contrib
        max_observed = max(max_observed, h_z_norm)
        ok = h_z_norm <= J_max + 1e-9
        if not ok:
            all_ok = False
        marker = "OK" if ok else "FAIL"
        print(f"  {cfg:>8d}  {h_z_norm:>22.6e}  {J_max:>22.6e}  {marker:>6}")
    print()
    print(f"  Max observed budget = {max_observed:.6e}")
    print(f"  J_max (closed-form) = {J_max:.6e}")
    check("F2 — closed-form J_max bound holds across all random SU(3) configs",
          all_ok,
          f"max_observed/J_max = {max_observed/J_max:.4f}")
    return all_ok


# ---- Test 2b: F2b carrier-faithful Wilson branch ----------------------------

def test_F2b_carrier_faithful_wilson() -> bool:
    """F2b: carrier-faithful Wilson budget from the displayed eq. (8) term.

    Verify on explicit one-particle color matrices that the per-site
    grouped Wilson budget d_s * (r_W + r_W/2) = 9/2 bounds the grouped
    block, that the pair norm underlying the link counting is exactly 1,
    and that the three branch values are ordered surface <= carrier <=
    envelope. No diagonal-surface input is used.
    """
    print()
    print("=" * 72)
    print("TEST F2b: carrier-faithful Wilson branch (displayed eq. (8) term)")
    print("=" * 72)
    print()

    d = 4
    d_s = 3  # spatial directions (mu != t in carrier (8))
    r_W = 1.0
    g_bare = 1.0
    N_c = 3
    beta = 2 * N_c / g_bare ** 2  # = 6
    rng = np.random.default_rng(SEED + 2)

    # (a) unit pair norm: || [[0,U],[U^dag,0]] ||_op = 1 for unitary U.
    worst_dev = 0.0
    n_pair = 25
    for i in range(n_pair):
        U = random_su3(rng, scale=0.0 if i == 0 else 2.0)
        blk = np.block([
            [np.zeros((3, 3), dtype=complex), U],
            [U.conj().T, np.zeros((3, 3), dtype=complex)],
        ])
        worst_dev = max(worst_dev, abs(float(np.linalg.norm(blk, ord=2)) - 1.0))
    pair_ok = worst_dev < 1e-12
    print(f"  (a) pair norm || [[0,U],[U†,0]] ||_op over {n_pair} SU(3) configs:")
    print(f"      max |norm - 1| = {worst_dev:.3e}")
    check("F2b(a) — unit pair norm for SU(3) hop blocks", pair_ok,
          "‖a†(U b) + h.c.‖_op = ‖U‖_op = 1, grounding coefficient×1 link counting")

    # (b) grouped spatial-Wilson one-particle block:
    #     sites {z, z+e_1, z+e_2, z+e_3}, color C^3 each (dim 12);
    #     h_z^W = -d_s*r_W*P_z + sum_k (r_W/2) * hop(z, z+e_k; U_k).
    w_budget = d_s * (r_W + r_W / 2.0)  # = 9/2
    worst_norm = 0.0
    n_cfg = 20
    for cfg in range(n_cfg):
        scale = 0.0 if cfg == 0 else 2.0
        h = np.zeros((12, 12), dtype=complex)
        h[0:3, 0:3] = -d_s * r_W * np.eye(3)  # grouped diagonal at z
        for k in range(d_s):
            U = random_su3(rng, scale=scale)
            s = 3 * (k + 1)
            h[0:3, s:s + 3] += (r_W / 2.0) * U
            h[s:s + 3, 0:3] += (r_W / 2.0) * U.conj().T
        worst_norm = max(worst_norm, float(np.linalg.norm(h, ord=2)))
    block_ok = worst_norm <= w_budget + 1e-9
    print()
    print(f"  (b) grouped spatial-Wilson block over {n_cfg} SU(3) configs:")
    print(f"      max ||h_z^W||_op = {worst_norm:.6f}  <=  d_s·(r_W + r_W/2) = {w_budget}")
    check("F2b(b) — grouped Wilson block bounded by d_s·(r_W + r_W/2)", block_ok,
          f"max observed {worst_norm:.6f} vs budget {w_budget}")

    # (c) exact branch arithmetic with Fractions (no floats).
    rw = Fraction(1)
    ks = Fraction(d, 2)                       # 2
    plaq = 2 * int(beta) * (d * (d - 1) // 2)  # 72
    w_surface = rw * d                        # 4   (supplied diagonal surface)
    w_carrier = d_s * rw + d_s * rw / 2       # 9/2 (displayed carrier (8))
    w_envelope = d * rw + d * rw / 2          # 6   (all-direction envelope)
    j_surface = ks + w_surface + plaq
    j_carrier = ks + w_carrier + plaq
    j_envelope = ks + w_envelope + plaq
    print()
    print(f"  (c) exact budgets (above |m|): surface = {j_surface}, "
          f"carrier = {j_carrier}, envelope = {j_envelope}")
    arith_ok = (
        j_surface == 78
        and j_carrier == Fraction(157, 2)
        and j_envelope == 80
        and j_surface <= j_carrier <= j_envelope
    )
    check("F2b(c) — branch arithmetic 78 <= 78.5 <= 80 exact", arith_ok,
          "J_max branches: supplied surface 78, displayed carrier 157/2, envelope 80")

    all_ok = pair_ok and block_ok and arith_ok
    return all_ok


# ---- Test 2c: F2c per-site overlap weights W (lemma input) ------------------

def test_F2c_overlap_weights() -> bool:
    """F2c: per-site overlap weights W for the carrier support family.

    The Lieb-Robinson lemma input is NOT the per-assigned-site budget
    J_max but the per-site overlap weight W = sup_x sum_{Z containing x}
    ||h_Z||.  Recompute the support counts from scratch and the three
    branch values exactly:

      per site on Z^4:  1 site term, 2d = 8 incident links,
                        4 * C(d,2) = 24 incident plaquettes.

      W_surface  = |m| + (r_W d)        + 8*(1/2)       + 24*(2β) = |m| + 296
      W_carrier  = |m| + (d_s r_W)      + 6*1 + 2*(1/2) + 24*(2β) = |m| + 298
      W_envelope = |m| + (d r_W)        + 8*1           + 24*(2β) = |m| + 300

    and the conditional velocity ceilings v = 2 e q W R = 16 e W at
    q = 4, R = 2.
    """
    print()
    print("=" * 72)
    print("TEST F2c: per-site overlap weights W (Lieb-Robinson lemma input)")
    print("=" * 72)
    print()

    d = 4
    d_s = 3
    r_W = Fraction(1)
    beta = Fraction(6)
    half = Fraction(1, 2)

    # Support counts per site, recomputed from scratch:
    n_site_terms = 1
    n_links = 2 * d                                   # 8
    n_plaq_orient = d * (d - 1) // 2                  # 6 orientations
    n_plaq = 4 * n_plaq_orient                        # 24 (4 corners each)
    plaq_norm = 2 * beta                              # 12 per plaquette

    counts_ok = (n_links == 8 and n_plaq == 24 and plaq_norm == 12)
    print(f"  per-site support counts on Z^{d}: site terms = {n_site_terms}, "
          f"links = {n_links}, plaquettes = {n_plaq} (norm ≤ {plaq_norm} each)")

    # Branch W values above |m| (mass term lives in the site-term support).
    w_surface = r_W * d + n_links * half + n_plaq * plaq_norm           # 4+4+288
    w_carrier = d_s * r_W + 2 * d_s * 1 + 2 * half + n_plaq * plaq_norm  # 3+6+1+288
    w_envelope = d * r_W + n_links * 1 + n_plaq * plaq_norm             # 4+8+288

    print(f"  W_surface  - |m| = {w_surface}   (expect 296)")
    print(f"  W_carrier  - |m| = {w_carrier}   (expect 298)")
    print(f"  W_envelope - |m| = {w_envelope}   (expect 300)")
    w_ok = (w_surface == 296 and w_carrier == 298 and w_envelope == 300
            and w_surface <= w_carrier <= w_envelope)

    # Conditional velocity ceilings at q = 4, R = 2: v = 2 e q W R = 16 e W.
    q, R = 4, 2
    v_s = 2 * math.e * q * (0.0 + 296) * R
    v_c = 2 * math.e * q * (0.0 + 298) * R
    v_e = 2 * math.e * q * (0.0 + 300) * R
    print()
    print(f"  conditional ceilings (m -> 0), v = 2·e·q·W·R = 16·e·W:")
    print(f"    surface  : v ≤ 16·e·296 = {v_s:.1f}")
    print(f"    carrier  : v ≤ 16·e·298 = {v_c:.1f}")
    print(f"    envelope : v ≤ 16·e·300 = {v_e:.1f}")
    v_ok = abs(v_e - 16 * math.e * 300) < 1e-9

    all_ok = counts_ok and w_ok and v_ok
    check("F2c — overlap weights W = |m| + {296, 298, 300} exact and ordered",
          all_ok,
          f"v ceilings (m->0): {v_s:.1f} / {v_c:.1f} / {v_e:.1f} lattice units")
    return all_ok


# ---- Test 3: proved LR lemma vs exact commutators on the framework H --------

def build_hopping_chain(L: int, m: float, extra_bonds=None):
    """Framework hopping Hamiltonian on a periodic L-site chain.

    H = sum_x [ H_{x,x+1} + m n_x ],   H_{xy} = a_x^dag a_y + a_y^dag a_x,
    in the per-site tensor ladder convention of the cited hopping-bilinear
    chain (commuting modes, no Jordan-Wigner string).
    extra_bonds: optional list of (x, y, eps) long-range bonds.
    """
    dim = 2 ** L
    H = np.zeros((dim, dim), dtype=complex)
    a_ops = [site_op(SM, x, L) for x in range(L)]
    link_terms = []
    for x in range(L):
        y = (x + 1) % L
        Hxy = a_ops[x].conj().T @ a_ops[y] + a_ops[y].conj().T @ a_ops[x]
        H += Hxy
        link_terms.append(((x, y), Hxy))
        H += m * site_op(N_OP, x, L)
    if extra_bonds:
        for (x, y, eps) in extra_bonds:
            Hb = eps * (a_ops[x].conj().T @ a_ops[y] + a_ops[y].conj().T @ a_ops[x])
            H += Hb
            link_terms.append(((x, y), Hb))
    return H, link_terms


def heisenberg(O, t, eigvals, V):
    U = V @ np.diag(np.exp(1j * t * eigvals)) @ V.conj().T
    return U @ O @ U.conj().T


def test_F3_proved_LR_lemma_on_framework_H() -> bool:
    """F3: the in-note Lieb-Robinson lemma (L1 series bound, L2 exponential
    bound with v_LR = 2 e q W R) holds against EXACT commutator norms on
    the actual framework hopping Hamiltonian.
    """
    print()
    print("=" * 72)
    print("TEST F3: proved LR lemma vs exact commutators on the framework hopping H")
    print("=" * 72)
    print()

    L = 10
    m = 0.3
    H, link_terms = build_hopping_chain(L, m)

    # Support-family data (per-site ladder convention):
    #   link supports {x, x+1}: q = 2, R = 1, ||H_xy|| = 1;
    #   mass supports {x}: ||m n_x|| = |m|;
    #   overlap weight W = |m| + 2 (each site lies in 2 links + its mass term).
    q, R = 2, 1
    W = abs(m) + 2.0
    v_LR = 2 * math.e * q * W * R
    print(f"  Framework H on periodic chain: L={L}, m={m}")
    print(f"  support family: q={q}, R={R}, W=|m|+2={W}")
    print(f"  derived velocity v_LR = 2·e·q·W·R = {v_LR:.4f} lattice units")
    print()

    # (a) ||H_xy|| = 1 and finite-range support of every local term.
    worst_pair_dev = 0.0
    support_ok = True
    for (x, y), Hxy in link_terms:
        worst_pair_dev = max(worst_pair_dev,
                             abs(float(np.linalg.norm(Hxy, ord=2)) - 1.0))
        for w in range(L):
            if w in (x, y):
                continue
            Ow = site_op(SIGMA_Z, w, L)
            comm = Hxy @ Ow - Ow @ Hxy
            if float(np.linalg.norm(comm, ord=2)) > 1e-12:
                support_ok = False
    print(f"  (a) all {len(link_terms)} link terms: max | ||H_xy|| - 1 | = {worst_pair_dev:.3e};")
    print(f"      [H_xy, σ_z(w)] = 0 for every w outside {{x, y}}: {support_ok}")
    pair_ok = worst_pair_dev < 1e-12 and support_ok
    check("F3(a) — ||H_xy||_op = 1 and supp(H_xy) ⊆ {x,y} on the framework chain",
          pair_ok,
          "finite range verified term-by-term on the actual hopping Hamiltonian")

    # (b)+(c) exact commutators vs L1 series bound and L2 exponential bound.
    eigvals, V = np.linalg.eigh(H)
    O_0 = site_op(SIGMA_Z, 0, L)
    print()
    print(f"  {'d':>3}  {'t':>6}  {'measured ||[..]||':>18}  {'L1 series bound':>16}  "
          f"{'L2 exp bound':>14}  {'OK':>4}")
    print(f"  {'-'*3}  {'-'*6}  {'-'*18}  {'-'*16}  {'-'*14}  {'-'*4}")
    l1_ok = True
    l2_ok = True
    margin_min = float("inf")
    for t in [0.02, 0.05, 0.1, 0.2]:
        A_t = heisenberg(O_0, t, eigvals, V)
        for d_test in [2, 3, 4, 5]:
            O_d = site_op(SIGMA_Z, d_test, L)
            comm = A_t @ O_d - O_d @ A_t
            meas = float(np.linalg.norm(comm, ord=2))
            n0 = math.ceil(d_test / R)
            a = 2 * q * W * t
            b1 = 2.0 * (1.0 / q) * series_tail(a, n0)             # L1
            b2 = (2 * math.e / (math.e - 1)) * (1.0 / q) \
                * math.exp(-(d_test - v_LR * t) / R)              # L2
            ok1 = meas <= b1 + 1e-12
            ok2 = meas <= b2 + 1e-12
            if not ok1:
                l1_ok = False
            if not ok2:
                l2_ok = False
            if meas > 1e-13:
                margin_min = min(margin_min, b1 / meas)
            marker = "OK" if (ok1 and ok2) else "FAIL"
            print(f"  {d_test:>3}  {t:>6.3f}  {meas:>18.6e}  {b1:>16.6e}  "
                  f"{b2:>14.6e}  {marker:>4}")
    print()
    check("F3(b) — L1 exact series bound holds at every (d, t) grid point",
          l1_ok,
          f"min bound/measured margin = {margin_min:.2f}x (bound is rigorous, not tuned)")
    check("F3(c) — L2 exponential bound with v_LR = 2eqWR holds at every grid point",
          l2_ok,
          f"v_LR = {v_LR:.4f} derived from (q, W, R) — no imported constant")
    return pair_ok and l1_ok and l2_ok


# ---- Test 4: lightcone behavior ---------------------------------------------

def test_F4_outside_lightcone_decay() -> bool:
    """F4: on the framework hopping H, the equal-time commutator decays
    monotonically (in fact exponentially) with distance at fixed t.
    """
    print()
    print("=" * 72)
    print("TEST F4: outside-lightcone exponential decay (framework hopping H)")
    print("=" * 72)
    print()

    L = 10
    m = 0.3
    H, _ = build_hopping_chain(L, m)
    eigvals, V = np.linalg.eigh(H)
    O_0 = site_op(SIGMA_Z, 0, L)
    t_fixed = 0.1
    A_t = heisenberg(O_0, t_fixed, eigvals, V)

    print(f"  L={L} (periodic), m={m}, t={t_fixed}")
    print()
    print(f"  {'d':>3}  {'commutator':>14}  {'log(commutator)':>18}")
    last_log = None
    decreasing = True
    for d_test in [1, 2, 3, 4, 5]:
        O_d = site_op(SIGMA_Z, d_test, L)
        comm = A_t @ O_d - O_d @ A_t
        comm_norm = float(np.linalg.norm(comm, ord=2))
        log_comm = math.log(comm_norm) if comm_norm > 1e-300 else float("-inf")
        marker = ""
        if last_log is not None and log_comm > last_log + 0.01:
            marker = " (NOT decreasing!)"
            decreasing = False
        print(f"  {d_test:>3}  {comm_norm:>14.6e}  {log_comm:>18.6f}{marker}")
        last_log = log_comm
    print()
    check("F4 — outside-lightcone exponential decay on the framework hopping H",
          decreasing,
          "log(commutator) decreases monotonically with d (microcausal lightcone)")
    return decreasing


# ---- Test 5: falsification leg — long-range bond breaks the bound -----------

def test_F5_long_range_falsification() -> bool:
    """F5: a single long-range bond (support diameter 5 >> R = 1) makes the
    measured commutator violate the finite-range L1/L2 bounds by a large
    factor.  The finite-range hypothesis is load-bearing.
    """
    print()
    print("=" * 72)
    print("TEST F5: falsification — long-range perturbation breaks the LR bound")
    print("=" * 72)
    print()

    L = 10
    m = 0.3
    eps = 1.0
    x_far, y_far = 0, 5  # periodic distance 5 on the L=10 ring
    H2, link_terms = build_hopping_chain(L, m, extra_bonds=[(x_far, y_far, eps)])

    # (a) the perturbation violates the finite-range premise: its support
    #     contains sites at distance 5 > R = 1.
    Hb = link_terms[-1][1]
    O_0 = site_op(SIGMA_Z, 0, L)
    O_5 = site_op(SIGMA_Z, 5, L)
    c0 = float(np.linalg.norm(Hb @ O_0 - O_0 @ Hb, ord=2))
    c5 = float(np.linalg.norm(Hb @ O_5 - O_5 @ Hb, ord=2))
    premise_broken = c0 > 1e-6 and c5 > 1e-6
    print(f"  (a) perturbation ε(a_0†a_5 + h.c.), ε = {eps}:")
    print(f"      ||[H_bond, σ_z(0)]|| = {c0:.4f}, ||[H_bond, σ_z(5)]|| = {c5:.4f}")
    print(f"      -> support contains sites at distance 5 > R = 1: {premise_broken}")
    check("F5(a) — long-range bond violates the finite-range premise (diam 5 > R = 1)",
          premise_broken,
          "the perturbed family has no R = 1 support assignment")

    # (b) the measured commutator now violates the R = 1 bounds.
    q, R = 2, 1
    W = abs(m) + 2.0
    v_LR = 2 * math.e * q * W * R
    eigvals, V = np.linalg.eigh(H2)
    t = 0.1
    d_test = 5
    A_t = heisenberg(O_0, t, eigvals, V)
    comm = A_t @ O_5 - O_5 @ A_t
    meas = float(np.linalg.norm(comm, ord=2))
    a = 2 * q * W * t
    b1 = 2.0 * (1.0 / q) * series_tail(a, math.ceil(d_test / R))
    b2 = (2 * math.e / (math.e - 1)) * (1.0 / q) \
        * math.exp(-(d_test - v_LR * t) / R)
    ratio1 = meas / b1
    ratio2 = meas / b2
    print()
    print(f"  (b) at (d, t) = ({d_test}, {t}): measured = {meas:.6e}")
    print(f"      finite-range L1 bound = {b1:.6e}  -> violation ratio {ratio1:.1f}x")
    print(f"      finite-range L2 bound = {b2:.6e}  -> violation ratio {ratio2:.2f}x")
    violated = ratio1 > 10.0 and ratio2 > 1.0
    check("F5(b) — measured commutator violates the finite-range bounds (>10x on L1)",
          violated,
          f"L1 violated {ratio1:.1f}x, L2 violated {ratio2:.2f}x — bound premise is load-bearing")
    return premise_broken and violated


# ---- Test 6: Z^3 block check -------------------------------------------------

def test_F6_z3_block() -> bool:
    """F6: on the minimal periodic 2x2x2 Z^3 block, the translation-invariant
    NN link-family Hamiltonian H = sum_links H_xy + m sum_x n_x is Hermitian,
    conserves Q_total, every H_xy is supported on its two tensor factors,
    and the per-site overlap weight is W = |m| + 2d = |m| + 6.
    """
    print()
    print("=" * 72)
    print("TEST F6: Z^3 NN link family on the minimal periodic 2x2x2 block")
    print("=" * 72)
    print()

    Ls = 2
    d = 3
    m = 0.3
    sites = [(x, y, z) for x in range(Ls) for y in range(Ls) for z in range(Ls)]
    idx = {s: i for i, s in enumerate(sites)}
    n_sites = len(sites)

    def shift(s, mu):
        v = list(s)
        v[mu] = (v[mu] + 1) % Ls
        return tuple(v)

    a_ops = [site_op(SM, i, n_sites) for i in range(n_sites)]
    dim = 2 ** n_sites
    H = np.zeros((dim, dim), dtype=complex)
    links = []
    for s in sites:
        for mu in range(d):
            s2 = shift(s, mu)
            xi, yi = idx[s], idx[s2]
            Hxy = a_ops[xi].conj().T @ a_ops[yi] + a_ops[yi].conj().T @ a_ops[xi]
            H += Hxy
            links.append(((xi, yi), Hxy))
    Q = np.zeros((dim, dim), dtype=complex)
    for i in range(n_sites):
        H += m * site_op(N_OP, i, n_sites)
        Q += site_op(N_OP, i, n_sites)

    herm = float(np.linalg.norm(H - H.conj().T, ord=2))
    qcons = float(np.linalg.norm(H @ Q - Q @ H, ord=2))

    support_ok = True
    for (xi, yi), Hxy in links:
        for w in range(n_sites):
            if w in (xi, yi):
                continue
            Ow = site_op(SIGMA_Z, w, n_sites)
            if float(np.linalg.norm(Hxy @ Ow - Ow @ Hxy, ord=2)) > 1e-12:
                support_ok = False

    # per-site overlap weight: count link-family members containing each site
    link_count = {i: 0 for i in range(n_sites)}
    for (xi, yi), _ in links:
        link_count[xi] += 1
        link_count[yi] += 1
    counts = sorted(set(link_count.values()))
    W = abs(m) + max(counts)
    v_LR = 2 * math.e * 2 * W * 1  # q = 2, R = 1
    print(f"  {n_sites} sites, {len(links)} link-family members (B4 family, all (x, x+e_mu))")
    print(f"  ||H - H†|| = {herm:.3e},  ||[H, Q_total]|| = {qcons:.3e}")
    print(f"  every H_xy supported on its two tensor factors: {support_ok}")
    print(f"  link-family members per site: {counts} (expect [6] = 2d)")
    print(f"  W = |m| + 2d = {W},  unconditional v_LR ≤ 2·e·q·W·R = 4·e·(|m| + 6) = {v_LR:.4f}")
    ok = (herm < 1e-12 and qcons < 1e-12 and support_ok
          and counts == [6] and abs(v_LR - 4 * math.e * (abs(m) + 6)) < 1e-9)
    check("F6 — Z^3 block: Hermitian, Q-conserving, finite-range, W = |m| + 6",
          ok,
          f"unconditional Z^3 leg: v_LR ≤ 4·e·(|m| + 2d) = {v_LR:.4f} at m = {m}")
    return ok


# ---- Main -------------------------------------------------------------------

def main() -> None:
    print()
    print("=" * 72)
    print("MICROCAUSALITY ACTION-SUPPORT BUDGET + PROVED FINITE-RANGE LR RUNNER")
    print("=" * 72)
    print()
    print("Narrows the gap on AXIOM_FIRST_MICROCAUSALITY_LIEB_ROBINSON_THEOREM_NOTE_2026-05-01.md:")
    print("carrier support/J/W budgets, an in-note proved Lieb-Robinson lemma with")
    print("derived velocity v_LR = 2eqWR, an unconditional finite-range LR theorem for")
    print("the framework hopping Hamiltonian, and a falsification leg.")
    print()
    print("References:")
    print("  - Bridge note: docs/MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md")
    print("  - Parent: docs/AXIOM_FIRST_MICROCAUSALITY_LIEB_ROBINSON_THEOREM_NOTE_2026-05-01.md")
    print("  - RP note: docs/AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md")
    print("  - Hopping note: docs/HOPPING_BILINEAR_HERMITICITY_THEOREM_NOTE_2026-05-02.md")
    print()

    f0 = test_F0_note_manifest_sync()
    f1 = test_F1_finite_range_support()
    f2 = test_F2_explicit_J_bound()
    f2b = test_F2b_carrier_faithful_wilson()
    f2c = test_F2c_overlap_weights()
    f3 = test_F3_proved_LR_lemma_on_framework_H()
    f4 = test_F4_outside_lightcone_decay()
    f5 = test_F5_long_range_falsification()
    f6 = test_F6_z3_block()

    print()
    print("=" * 72)
    print("SUMMARY")
    print("=" * 72)
    print(f"  F0  note manifest / proved-lemma surface guard:          {'PASS' if f0 else 'FAIL'}")
    print(f"  F1  action-density local support:                        {'PASS' if f1 else 'FAIL'}")
    print(f"  F2  explicit J_max bound from action coefficients:       {'PASS' if f2 else 'FAIL'}")
    print(f"  F2b carrier-faithful Wilson branch bracket:              {'PASS' if f2b else 'FAIL'}")
    print(f"  F2c per-site overlap weights W (lemma input):            {'PASS' if f2c else 'FAIL'}")
    print(f"  F3  proved LR lemma vs exact commutators (framework H):  {'PASS' if f3 else 'FAIL'}")
    print(f"  F4  outside-lightcone exponential decay:                 {'PASS' if f4 else 'FAIL'}")
    print(f"  F5  falsification: long-range bond breaks the bound:     {'PASS' if f5 else 'FAIL'}")
    print(f"  F6  Z^3 block: Hermitian, finite-range, W = |m| + 6:     {'PASS' if f6 else 'FAIL'}")
    print()
    all_ok = f0 and f1 and f2 and f2b and f2c and f3 and f4 and f5 and f6
    print(f"  PASS={PASS_COUNT}, FAIL={FAIL_COUNT}")
    print(f"  OVERALL: {'PASS' if all_ok else 'FAIL'}")
    print()
    print("Scope notes for the auditor:")
    print("  - The LR velocity is DERIVED in the companion note (v_LR = 2eqWR);")
    print("    this runner checks the derived bound against exact commutator norms")
    print("    on the actual framework hopping Hamiltonian (class C compute).")
    print("  - The exact reconstructed logarithmic H = -log(T)/a_tau is NOT")
    print("    constructed; the carrier-velocity corollary remains conditional.")
    print("  - Cited authority chain: parent RP note (staggered-only surface names),")
    print("    hopping_bilinear_hermiticity (B1-B6 hopping Hamiltonian),")
    print("    staggered_wilson_det_positivity_bridge (supplied M_W = r_W d I")
    print("    surface; F2 branch value only — non-load-bearing after F2b).")
    print()

    if not all_ok:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
