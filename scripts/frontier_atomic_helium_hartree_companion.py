#!/usr/bin/env python3
"""Helium Hartree companion on the retained Cl(3)/Z³ lattice Hamiltonian surface.

==========================================================================
NUMERICAL VARIATIONAL COMPANION ON THE LATTICE HAMILTONIAN SURFACE
==========================================================================

Framework surface: current minimal Cl(3)/Z³ primitives plus the narrowed
scalar graph-Laplacian and lattice Green-kernel dependency repair.
Sources: MINIMAL_AXIOMS_2026-06-04.md;
HYDROGEN_HELIUM_ATOMIC_LATTICE_KINETIC_DEPENDENCY_NARROW_REPAIR_NOTE_2026-06-02.md;
LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md.

Steps 1–3: Same as hydrogen
(`frontier_atomic_hydrogen_lattice_companion.py`).
    H_free = -Δ_Z³   [narrowed scalar graph-Laplacian surface]
    V(r) = -g/|r|     [lattice Green-kernel repair]

--------------------------------------------------------------------------
STEP 4: TWO-BODY HAMILTONIAN  [extension, same kernel]
--------------------------------------------------------------------------
Helium has two electrons. The EXACT two-body Hamiltonian on Z³×Z³ is:

    H₂ = H_1 + H_2 + V_ee

where:
    H_i = -Δ_{Z³,i} + V_nuc(rᵢ)     (single-particle terms, one per electron)
    V_nuc(r) = -Z × g_EM / |r|        (nuclear attraction; Z=2, g_EM = 4π × α_EM)
    V_ee(r₁, r₂) = +g_EM / |r₁ - r₂| (electron-electron repulsion)

Crucially: V_ee uses the SAME Z³ Green's function kernel as V_nuc.
There is no new assumption. Both potentials are 1/r from the same
lattice potential theory theorem.

Coupling ratio: g_ee / g_nuc = g_EM / (Z × g_EM) = 1/Z.
For Z=2: the e-e repulsion is half the e-nucleus attraction in coupling
units. This ratio is EXACT and coupling-independent — it is pure charge
arithmetic from the Green's function kernel.

BLOCKER: The full two-body problem H₂ acts on l²(Z³ × Z³).
For N³ sites, this is an N⁶ problem. N=10 → 10⁶ sites: already large.
We cannot solve this exactly for useful grid sizes.

--------------------------------------------------------------------------
STEP 5: VARIATIONAL BOUND  [DERIVED — variational principle on the lattice]
--------------------------------------------------------------------------
The variational principle on the lattice Hilbert space states:

    ⟨ψ | H₂ | ψ⟩ ≥ E_exact   for any normalized ψ

This is a theorem of linear algebra (Rayleigh-Ritz), NOT imported from
quantum mechanics. The Hilbert space here is l²(Z³ × Z³); the inner
product and norm are the standard ℓ² ones.

We restrict to SEPARABLE (product) states:

    ψ(r₁, r₂) = φ(r₁) × φ(r₂)   with ‖φ‖ = 1

This is the SINGLE ANSATZ CLASS we optimize over. Minimizing:

    E[φ] = ⟨φ⊗φ | H₂ | φ⊗φ⟩

over all normalized φ ∈ l²(Z³) yields the self-consistency equation:

    [-Δ + V_nuc + V_H[φ]] φ = ε φ

where V_H[φ](r) = g_EM Σ_{r'} |φ(r')|² / max(|r - r'|, 0.5)
(Hartree potential, using the same finite-box kernel as V_ee).

This is the Hartree stationarity equation for the product-state ansatz on
the lattice Hamiltonian surface. Mathematically it is the same variational
structure used in standard atomic numerics; the point here is that it is
applied to the already-retained lattice kinetic+kernel operator.

Density convention and total energy from the variational ansatz:

    ρ(r) = |φ(r)|²,        Σ_r ρ(r) = 1        (one-electron density)
    V_H[ρ](r) = Σ_r' ρ(r') g_EM / max(|r-r'|, 0.5)
    E_pair = Σ_r ρ(r) V_H[ρ](r)
           = Σ_{r,r'} ρ(r)ρ(r') g_EM / max(|r-r'|, 0.5)

`E_pair` is already the single unordered electron-electron pair integral
for the product state φ(r₁)φ(r₂).  The familiar total-density Hartree
factor 1/2 is not applied to this one-density expression; if n=2ρ is used
instead, the same one-pair integral is (1/4)Σ_r n(r)V_H[n](r).

    E_var = 2ε - E_pair

where E_pair = ⟨φ⊗φ | V_ee | φ⊗φ⟩ = Σ_r |φ(r)|² V_H(r).
The factor 2ε counts each electron's orbital energy; E_pair is
subtracted once because 2ε counts the same electron-electron pair twice.

This formula is DERIVED from the product-state ansatz, not postulated.

--------------------------------------------------------------------------
STEP 6: WHAT THE VARIATIONAL BOUND GIVES
--------------------------------------------------------------------------
The variational energy E_var ≥ E_exact(He). It is an UPPER BOUND.
The quality depends on how well the separable ansatz captures the
true two-electron ground state.

The DIMENSIONLESS RATIO E_var / E(He⁺) is coupling-independent:
both energies scale as g² (same coupling, same kernel), so the ratio
is a pure number determined by Z and the lattice geometry.

Continuum Hartree checkpoint:
    E(He) / E(He⁺) ~ 1.424
Exact (full CI): E(He) / E(He⁺) ~ 1.452

This companion reports a finite-grid upper bound, not a theorem-grade
closure of the helium problem.

==========================================================================
WHAT THIS EXPERIMENT COMPUTES
==========================================================================
1. He⁺ exact: E₁(He⁺) = -Z² × E₀ = -g²  (Z=2, same as H with Z=2)
2. He variational: minimize E[φ] over product states → E_var
3. Key ratio: E_var / E₁(He⁺) (coupling-independent prediction)
4. Ionization energies: IE₁ = E(He⁺) - E(He), IE₂ = 0 - E(He⁺)
5. Ratio IE₁/IE₂ (coupling-independent)
6. SCF convergence: verify the self-consistency equation converges

HISTORICAL COMPARISON (checkpoint, not foundation):
  Hartree approx: E(He) ≈ -5.696 Ry,  E(He⁺) = -4.0 Ry  →  ratio ≈ 1.424
  Full CI exact:  E(He) = -5.807 Ry,  E(He⁺) = -4.0 Ry  →  ratio = 1.452
  Framework (variational bound): should give ~1.424 (product-state quality)
  Note: we compare ratios, not absolute Ry values.

BLOCKERS:
  1. Absolute eV conversion still needs the electron-mass lane
  2. Exact two-body solution: N⁶ problem, not tractable here
  3. Exchange-correlation beyond product-state ansatz is handled only by the
     separate Jastrow companion, not closed here
==========================================================================
"""

from __future__ import annotations

import os

import numpy as np
from scipy import sparse
from scipy.signal import fftconvolve
from scipy.sparse.linalg import eigsh


# ---------------------------------------------------------------------------
# Lattice operators (same as hydrogen; repeated here for self-containment)
# ---------------------------------------------------------------------------

def build_graph_laplacian(N: int) -> sparse.csr_matrix:
    """Negative graph Laplacian -Δ_Z³ on N³ grid (Dirichlet BCs).

    Derived from Cl(3) on Z³ via KS construction.
    """
    diag = 2.0 * np.ones(N)
    off  = -1.0 * np.ones(N - 1)
    T1d  = sparse.diags([off, diag, off], [-1, 0, 1], shape=(N, N), format='csr')
    I    = sparse.eye(N, format='csr')
    T3 = (sparse.kron(sparse.kron(T1d, I), I) +
          sparse.kron(sparse.kron(I, T1d), I) +
          sparse.kron(sparse.kron(I, I), T1d))
    return T3.tocsr()


def build_coulomb_potential(N: int, g: float) -> np.ndarray:
    """Nuclear attraction V(r) = -g/|r| from Z³ Green's function.

    g here is the nuclear coupling: g = Z × g_EM where g_EM = 4π × α_EM.
    """
    center = (N - 1) / 2.0
    ix, iy, iz = np.indices((N, N, N))
    r = np.sqrt((ix - center)**2 + (iy - center)**2 + (iz - center)**2).ravel()
    return -g / np.maximum(r, 0.5)


def solve_single_particle(T: sparse.csr_matrix,
                           V_nuc: np.ndarray,
                           V_hartree: np.ndarray | None = None,
                           n_eig: int = 5) -> tuple[np.ndarray, np.ndarray]:
    """Eigenvalue problem for one electron in V_nuc + V_hartree."""
    V = V_nuc.copy()
    if V_hartree is not None:
        V = V + V_hartree
    H = T + sparse.diags(V, 0, format='csr')
    k = min(n_eig, T.shape[0] - 2)
    evals, evecs = eigsh(H, k=k, which='SA')
    idx = np.argsort(evals)
    return evals[idx], evecs[:, idx]


# ---------------------------------------------------------------------------
# Direct finite-box Hartree potential (derived from V_ee = g_EM/|r₁-r₂|)
# ---------------------------------------------------------------------------

def solve_poisson_for_hartree(N: int, rho: np.ndarray,
                               T: sparse.csr_matrix,
                               g_em: float) -> np.ndarray:
    """Build V_H(r)=Σ_r' rho(r') g_EM/max(|r-r'|, 0.5) by convolution.

    The function name is kept for packet compatibility with the previous
    audit surface, but the computation is now the direct finite-box Coulomb
    kernel used by V_nuc and V_ee.  This removes the old normalization
    ambiguity between a Dirichlet Poisson surrogate and the stated two-body
    Hamiltonian.
    """
    _ = T  # The direct kernel fixes the finite-box operator convention.
    rho_3d = rho.reshape(N, N, N)
    offsets = np.arange(-(N - 1), N, dtype=float)
    dx, dy, dz = np.meshgrid(offsets, offsets, offsets, indexing="ij")
    r = np.sqrt(dx * dx + dy * dy + dz * dz)
    kernel = g_em / np.maximum(r, 0.5)
    return fftconvolve(rho_3d, kernel, mode="same").reshape(-1)


def hartree_energy(rho: np.ndarray, V_H: np.ndarray) -> float:
    """E_pair = sum_r rho(r) V_H(r), the one electron-electron pair integral."""
    return float(np.sum(rho * V_H))


def direct_pair_integral(N: int, rho: np.ndarray, g_em: float) -> float:
    """Brute-force one-pair Coulomb integral for small-grid normalization checks."""
    coords = np.array(np.unravel_index(np.arange(N**3), (N, N, N))).T
    total = 0.0
    for a, ra in enumerate(coords):
        for b, rb in enumerate(coords):
            dist = float(np.linalg.norm(ra - rb))
            total += rho[a] * rho[b] * g_em / max(dist, 0.5)
    return float(total)


def pair_integral_normalization_certificate() -> dict[str, float]:
    """Certify the one-density Hartree convention against direct summation.

    The audit-relevant point is the factor of two: this runner uses
    ρ=|φ|² with Σρ=1, so ΣρV_H[ρ] is the one electron-pair energy.  If a
    total density n=2ρ is used, the equivalent expression is
    (1/4)Σ n V_H[n], while the common (1/2)Σ n V_H[n] total-density
    Hartree functional counts twice the single pair represented here.
    """
    N = 4
    g_em = 0.5
    raw = np.arange(1, N**3 + 1, dtype=float)
    rho = raw / np.sum(raw)
    T = build_graph_laplacian(N)

    V_one = solve_poisson_for_hartree(N, rho, T, g_em)
    one_density_pair = hartree_energy(rho, V_one)
    direct_pair = direct_pair_integral(N, rho, g_em)

    n_total = 2.0 * rho
    V_total = solve_poisson_for_hartree(N, n_total, T, g_em)
    quarter_total_density_form = 0.25 * float(np.sum(n_total * V_total))
    half_total_density_form = 0.5 * float(np.sum(n_total * V_total))

    return {
        "N": float(N),
        "g_em": g_em,
        "one_density_pair": one_density_pair,
        "direct_pair": direct_pair,
        "quarter_total_density_form": quarter_total_density_form,
        "half_total_density_form": half_total_density_form,
        "direct_ratio": one_density_pair / direct_pair,
        "half_total_to_pair": half_total_density_form / one_density_pair,
    }


# ---------------------------------------------------------------------------
# He⁺ exact solution (Z=2, one electron)
# ---------------------------------------------------------------------------

def solve_he_plus(N: int, g_nuc: float) -> dict:
    """He⁺ ground state: exactly H_g with g = g_nuc.

    g_nuc = Z × g_EM. For Z=2 and g_EM = 4π × α_EM: g_nuc = 2 × g_EM.
    Exact (continuum): E₁(He⁺) = -Z² × E₀ = -(g_nuc/2)² (in g_EM units)
    Or directly: E₁ = -g_nuc²/4 (lattice spectral units, Z² absorbed).

    We use g_nuc = Z × g_EM = 2 × g_EM. Let g_EM = g_nuc / 2.
    Then E₁(He⁺) = -(g_nuc)²/4 = -g_nuc²/4 (consistent with scaling).
    """
    T = build_graph_laplacian(N)
    V_nuc = build_coulomb_potential(N, g_nuc)
    evals, evecs = solve_single_particle(T, V_nuc, n_eig=5)
    # Exact continuum prediction: E₁ = -g_nuc²/4
    E1_exact = -(g_nuc**2) / 4.0
    return {
        "E1_lat": float(evals[0]),
        "E1_exact_continuum": E1_exact,
        "error_pct": 100.0 * (evals[0] - E1_exact) / abs(E1_exact),
        "evecs": evecs,
        "T": T,
        "V_nuc": V_nuc,
        "g_nuc": g_nuc,
        "N": N,
    }


# ---------------------------------------------------------------------------
# Helium variational SCF
# ---------------------------------------------------------------------------

def helium_variational_scf(N: int,
                            g_nuc: float,
                            g_em: float,
                            max_iter: int = 60,
                            tol: float = 1e-6,
                            mix: float = 0.5) -> dict:
    """Minimize E[φ] = ⟨φ⊗φ | H₂ | φ⊗φ⟩ over separable states.

    This is the variational bound for the two-electron ground state.
    The Hartree equation is derived as the stationarity condition of E[φ],
    not imported from standard QM.

    Parameters
    ----------
    g_nuc : coupling for nucleus-electron, = Z × g_EM
    g_em  : bare EM coupling = 4π × α_EM (same for both electrons)
    Coupling ratio: g_ee / g_nuc = g_em / (Z × g_em) = 1/Z  [EXACT]
    """
    T = build_graph_laplacian(N)
    V_nuc = build_coulomb_potential(N, g_nuc)

    # Initialize: φ₀ = He⁺ ground state orbital
    _, evecs_init = solve_single_particle(T, V_nuc, n_eig=3)
    phi = evecs_init[:, 0].copy()
    phi /= np.sqrt(np.sum(phi**2))
    rho = phi**2

    V_H = np.zeros(N**3)
    history: list[dict] = []
    delta_rhos = []

    for iteration in range(max_iter):
        # Step A: compute V_H from the same finite-box Coulomb kernel as V_ee
        V_H_new = solve_poisson_for_hartree(N, rho, T, g_em)

        # Step B: Mix for stability
        V_H_mix = mix * V_H_new + (1.0 - mix) * V_H

        # Step C: Solve stationarity equation for φ
        evals_new, evecs_new = solve_single_particle(T, V_nuc, V_H_mix, n_eig=3)
        phi_new = evecs_new[:, 0].copy()
        phi_new /= np.sqrt(np.sum(phi_new**2))
        rho_new = phi_new**2

        # Convergence measure
        delta_rho = float(np.sqrt(np.sum((rho_new - rho)**2)))
        delta_rhos.append(delta_rho)

        # Variational energy E_var = 2ε - E_pair (DERIVED from product ansatz)
        eps = float(evals_new[0])
        E_J = hartree_energy(rho_new, V_H_mix)
        E_var = 2.0 * eps - E_J

        history.append({
            "iter": iteration + 1,
            "eps": eps,
            "E_J": E_J,
            "E_var": E_var,
            "delta_rho": delta_rho,
        })

        if iteration < 5 or (iteration + 1) % 10 == 0:
            print(f"    iter {iteration+1:3d}: ε={eps:.5f}  E_pair={E_J:.5f}  "
                  f"E_var={E_var:.5f}  Δρ={delta_rho:.2e}")

        phi = phi_new
        rho = rho_new
        V_H = V_H_mix

        if delta_rho < tol:
            print(f"    Converged at iteration {iteration+1}")
            break
    else:
        print(f"    Did NOT converge ({max_iter} iters, Δρ={delta_rhos[-1]:.2e})")

    final = history[-1]
    return {
        "E_var": final["E_var"],
        "eps": final["eps"],
        "E_J": final["E_J"],
        "n_iter": len(history),
        "converged": delta_rhos[-1] < tol,
        "history": history,
        "phi": phi,
        "rho": rho,
        "g_nuc": g_nuc,
        "g_em": g_em,
        "N": N,
    }


# ---------------------------------------------------------------------------
# Main experiment
# ---------------------------------------------------------------------------

LOG: list[str] = []


def log(msg: str = "") -> None:
    LOG.append(msg)
    print(msg)


def run_experiment() -> None:
    log("=" * 72)
    log("HELIUM HARTREE COMPANION ON THE Cl(3)/Z³ SURFACE")
    log("Product-state upper bound on the retained lattice two-electron Hamiltonian")
    log("=" * 72)
    log()
    log("Derivation chain:")
    log("  Cl(3)/Z³  →  H₂ = (-Δ₁) + (-Δ₂) + V_nuc(r₁) + V_nuc(r₂) + V_ee(r₁,r₂)")
    log("  V_nuc = -Z×g_EM/|r|,  V_ee = +g_EM/|r₁-r₂|  [same Z³ Green's function]")
    log("  Coupling ratio: g_ee/g_nuc = 1/Z = 1/2  [exact, charge arithmetic]")
    log("  Variational ansatz: ψ(r₁,r₂) = φ(r₁)×φ(r₂)  [separable, not assumed]")
    log("  Stationarity → Hartree equation  [DERIVED, not imported]")
    log("  E_var = 2ε - E_pair  [DERIVED from product ansatz]")
    log()

    # ------------------------------------------------------------------
    # Coupling setup
    # ------------------------------------------------------------------
    # Choose computational coupling: g_EM = 1.0 for tractable Bohr radius.
    # g_nuc = Z × g_EM = 2.0  (Z=2 for helium)
    # The Bohr radius of He⁺ (in lattice units) = 2/g_nuc = 1.0
    # To resolve this, need N >> 1/g_nuc = 1; use N=30 with g_EM=0.5 → r_0=2.
    # All results reported as dimensionless ratios (coupling-independent).
    G_EM = 0.5           # bare EM coupling (free parameter in framework)
    G_NUC = 2.0 * G_EM  # He Z=2 nuclear coupling
    N = 30               # 30³ = 27000 sites; He⁺ Bohr radius = 2/G_NUC = 2 sites

    log(f"  Computational parameters:")
    log(f"    N = {N}  ({N**3} sites),  g_EM = {G_EM},  g_nuc = {G_NUC}")
    log(f"    He⁺ Bohr radius = 2/g_nuc = {2/G_NUC:.1f} lattice units")
    log(f"    All ratios are g-independent; absolute energies are g-relative.")
    log()

    # ------------------------------------------------------------------
    # STEP 1: He²⁺ (trivial reference)
    # ------------------------------------------------------------------
    log("─" * 60)
    log("STEP 1: He²⁺ — bare nucleus (trivial reference)")
    log("─" * 60)
    log()
    log("  E(He²⁺) = 0 by definition (no electrons, only nucleus).")
    log()

    # ------------------------------------------------------------------
    # STEP 2: He⁺ — one electron, Z=2 exact
    # ------------------------------------------------------------------
    log("─" * 60)
    log("STEP 2: He⁺ — one electron, Z=2")
    log("─" * 60)
    log()

    hep = solve_he_plus(N, G_NUC)
    log(f"  E₁(He⁺) lattice:   {hep['E1_lat']:.6f}  [lattice spectral units]")
    log(f"  E₁(He⁺) continuum: {hep['E1_exact_continuum']:.6f}  [= -g_nuc²/4]")
    log(f"  Lattice error: {hep['error_pct']:+.3f}%")
    log("  Compute timing: omitted from audit cache for deterministic replay.")
    log()
    log("  Note: E₁(He⁺) = -g_nuc²/4 = -Z² × (g_EM²/4) = -Z² × E₀(H)")
    log("  → He⁺ binds Z² times more than H. This is the scaling prediction.")
    log()

    # ------------------------------------------------------------------
    # STEP 3: He — two electrons, variational SCF
    # ------------------------------------------------------------------
    log("─" * 60)
    log("STEP 3: He — two electrons, variational bound")
    log("─" * 60)
    log()
    log("  Minimizing E[φ] = ⟨φ⊗φ | H₂ | φ⊗φ⟩ over separable φ.")
    log(f"  Building Laplacian ({N}³ = {N**3} sites) ...")

    he = helium_variational_scf(N, G_NUC, G_EM, max_iter=60, tol=1e-6, mix=0.5)
    norm = pair_integral_normalization_certificate()
    log()
    log(f"  Variational result:")
    log(f"    SCF orbital energy: ε   = {he['eps']:.6f}")
    log(f"    Coulomb pair integral: E_pair = {he['E_J']:.6f}")
    log(f"    Variational energy: E_var = 2ε - E_pair = {he['E_var']:.6f}")
    log(f"    Iterations: {he['n_iter']},  converged: {he['converged']}")
    log("    Compute timing: omitted from audit cache for deterministic replay.")
    log()

    # ------------------------------------------------------------------
    # STEP 4: Dimensionless ratios (coupling-independent predictions)
    # ------------------------------------------------------------------
    log("─" * 60)
    log("STEP 4: Coupling-independent predictions")
    log("─" * 60)
    log()

    E_he2plus = 0.0
    E_heplus = hep["E1_lat"]
    E_he = he["E_var"]
    E_he_exact_scale = hep["E1_exact_continuum"]

    IE2 = E_he2plus - E_heplus
    IE1 = E_heplus - E_he

    # Dimensionless ratios (g-independent)
    ratio_he_heplus = abs(E_he) / abs(E_heplus)          # should be ~1.424 (Hartree)
    ratio_IE1_IE2   = IE1 / IE2                           # should be ~0.424

    # Predictions in units of E₀ = g_EM²/4 (natural energy unit)
    E0 = G_EM**2 / 4.0
    log(f"  Natural energy unit: E₀ = g_EM²/4 = {E0:.5f}  (lattice spectral units)")
    log()
    log(f"  In units of E₀:")
    log(f"    E(He²⁺) / E₀ = {E_he2plus/E0:.4f}  (= 0, trivial)")
    log(f"    E(He⁺)  / E₀ = {E_heplus/E0:.4f}  (continuum: -Z² = -{2**2:.1f})")
    log(f"    E(He)   / E₀ = {E_he/E0:.4f}  (variational bound)")
    log()
    log(f"  Dimensionless ratios (pure Z³-geometry predictions):")
    log(f"    |E(He)| / |E(He⁺)|  = {ratio_he_heplus:.5f}")
    log(f"    Hartree checkpoint:   ~1.424")
    log(f"    Historical (full CI):   1.452  (upper checkpoint)")
    log()
    log(f"    IE₁ / IE₂ = {ratio_IE1_IE2:.5f}")
    log(f"    Historical (Hartree):  ~0.424")
    log()

    # ------------------------------------------------------------------
    # STEP 5: Energy decomposition (from variational formula, not QM)
    # ------------------------------------------------------------------
    log("─" * 60)
    log("STEP 5: Variational energy decomposition")
    log("─" * 60)
    log()
    log("  From the product-state ansatz (DERIVED, not assumed):")
    log("    ρ = |φ|² is a one-electron density with Σρ = 1")
    log("    E_pair = Σρ V_H[ρ] = Σρ(r)ρ(r') g_EM/max(|r-r'|, 0.5)")
    log("    E_var = 2ε - E_pair")
    log()
    log(f"    2ε  = {2*he['eps']:.5f}  [two orbital energies, each includes V_H]")
    log(f"    E_pair = {he['E_J']:.5f}   [one e-e pair integral; double-counting removed]")
    log(f"    E_var = {he['E_var']:.5f}")
    log()
    log("  Normalization guard (small-grid direct certificate):")
    log(f"    pair_norm_direct_ratio={norm['direct_ratio']:.6f}")
    log(f"    one_density_pair={norm['one_density_pair']:.12f}")
    log(f"    direct_pair={norm['direct_pair']:.12f}")
    log(f"    quarter_total_density_form={norm['quarter_total_density_form']:.12f}")
    log(f"    half_total_to_pair={norm['half_total_to_pair']:.6f}  [total-density 1/2 form counts two pairs here]")
    log()
    log("  Independent-electron limit (no e-e, same g_nuc):")
    log(f"    E_indep = 2 × E₁(He⁺) = {2*E_heplus:.5f}")
    log(f"    Repulsion cost: E_var - E_indep = {E_he - 2*E_heplus:+.5f}")
    log()

    # ------------------------------------------------------------------
    # STEP 6: SCF convergence
    # ------------------------------------------------------------------
    log("─" * 60)
    log("STEP 6: SCF convergence history")
    log("─" * 60)
    log()
    log(f"  {'Iter':>5}  {'ε':>10}  {'E_pair':>9}  {'E_var':>10}  {'Δρ':>9}")
    log("  " + "─" * 46)
    for h in he["history"][:10]:
        log(f"  {h['iter']:5d}  {h['eps']:10.5f}  {h['E_J']:9.5f}  "
            f"{h['E_var']:10.5f}  {h['delta_rho']:.2e}")
    if len(he["history"]) > 10:
        log(f"  ... ({len(he['history'])} total iterations)")
        last = he["history"][-1]
        log(f"  {last['iter']:5d}  {last['eps']:10.5f}  {last['E_J']:9.5f}  "
            f"{last['E_var']:10.5f}  {last['delta_rho']:.2e}")
    log()

    # ------------------------------------------------------------------
    # Summary
    # ------------------------------------------------------------------
    log("=" * 72)
    log("SUMMARY: HELIUM HARTREE COMPANION")
    log("=" * 72)
    log()
    log("  STRUCTURAL PREDICTIONS (coupling-independent):")
    log()

    rows = [
        ("E(He²⁺)/E₀", E_he2plus/E0, 0.0, "trivial"),
        ("E(He⁺)/E₀", E_heplus/E0, -4.0, "= -Z²  [exact from H-like Z=2]"),
        ("E(He)/E₀", E_he/E0, None, "variational bound"),
        ("|E(He)|/|E(He⁺)|", ratio_he_heplus, 1.424, "Hartree target"),
        # IE₁/IE₂ = |E(He)|/|E(He⁺)| - 1: a difference, so lattice error amplifies.
        # At 5% error in each energy, IE₁/IE₂ can be off by ~20%.
        ("IE₁/IE₂", ratio_IE1_IE2, 0.424, "Hartree; lattice error amplified (small diff)"),
    ]

    log(f"  {'Quantity':>22}  {'Lattice':>9}  {'Target':>9}  {'err%':>7}  Readout")
    log("  " + "─" * 62)
    for label, val, ref, note in rows:
        if ref is not None and abs(ref) > 1e-10:
            err = 100.0 * (val - ref) / abs(ref)
            log(f"  {label:>22}  {val:9.4f}  {ref:9.4f}  {err:+7.2f}%  "
                f"[cmp]  ({note})")
        elif ref == 0.0:
            log(f"  {label:>22}  {val:9.4f}  {ref:9.4f}  {'n/a':>7}  "
                f"[id]   ({note})")
        else:
            log(f"  {label:>22}  {val:9.4f}  {'n/a':>9}  {'n/a':>7}  "
                f"[bound]  ({note})")
    log()
    log("  DERIVATION STATUS:")
    log("  ✓ H₂ = H_1 + H_2 + V_ee follows from Z³ axioms (same Green's function)")
    log("  ✓ Hartree equation derived as stationarity of E[φ] (variational math)")
    log("  ✓ E_var = 2ε - E_pair derived from product-state ansatz")
    log("  ✓ Coupling ratio g_ee/g_nuc = 1/Z follows from charge arithmetic")
    log("  ✓ Helium is bound: E_var < E(He⁺)  (IE₁ > 0)")
    log()
    log("  BLOCKED:")
    log("  ✗ Absolute energy in eV still needs the electron-mass lane")
    log("  ✗ Exchange-correlation goes beyond the product-state ansatz")
    log("  ✗ Exact two-body solution remains N⁶ and is not attempted here")
    log()
    log("  CHECKPOINTS:")
    log(f"  |E(He)|/|E(He⁺)| = {ratio_he_heplus:.4f}  vs Hartree ~1.424  "
        f"(full CI 1.452)")
    log(f"  IE₁/IE₂           = {ratio_IE1_IE2:.4f}  vs Hartree ~0.424")
    log("=" * 72)

    audit_checks = [
        (
            "hartree_he2plus_identity",
            abs(E_he2plus) < 1e-12,
            f"E_he2plus={E_he2plus:.6f}",
        ),
        (
            "hartree_heplus_finite_box_row",
            abs(E_heplus / E0 - (-3.7908)) < 5e-4,
            f"E_heplus_over_E0={E_heplus / E0:.4f}",
        ),
        (
            "hartree_helium_bound_product_state",
            E_he < E_heplus,
            f"E_he={E_he:.6f}, E_heplus={E_heplus:.6f}",
        ),
        (
            "hartree_ratio_pin",
            abs(ratio_he_heplus - 1.43102) < 5e-5,
            f"ratio={ratio_he_heplus:.5f}",
        ),
        (
            "hartree_ie_ratio_pin",
            abs(ratio_IE1_IE2 - 0.43102) < 5e-5,
            f"ratio_IE1_IE2={ratio_IE1_IE2:.5f}",
        ),
        (
            "hartree_scf_converged",
            bool(he["converged"]),
            f"iterations={he['n_iter']}",
        ),
        (
            "hartree_pair_integral_direct_normalization",
            abs(norm["one_density_pair"] - norm["direct_pair"]) < 1e-12,
            f"pair_norm_direct_ratio={norm['direct_ratio']:.6f}",
        ),
        (
            "hartree_total_density_conversion_guard",
            abs(norm["quarter_total_density_form"] - norm["one_density_pair"]) < 1e-12
            and abs(norm["half_total_to_pair"] - 2.0) < 1e-12,
            f"quarter_total={norm['quarter_total_density_form']:.12f}, "
            f"half_total_to_pair={norm['half_total_to_pair']:.6f}",
        ),
    ]
    pass_count = 0
    fail_count = 0
    log()
    log("AUDIT CHECK SUMMARY")
    for name, ok, detail in audit_checks:
        if ok:
            pass_count += 1
            log(f"PASS: {name} -- {detail}")
        else:
            fail_count += 1
            log(f"FAIL: {name} -- {detail}")
    total_line = f"TOTAL: PASS={pass_count}, FAIL={fail_count}"

    os.makedirs("logs", exist_ok=True)
    log_path = "logs/frontier_atomic_helium_hartree_companion.latest.txt"
    try:
        with open(log_path, "w") as f:
            f.write("\n".join(LOG + [total_line]) + "\n")
    except Exception:
        pass
    print(total_line)
    if fail_count:
        raise SystemExit(1)


if __name__ == "__main__":
    run_experiment()
