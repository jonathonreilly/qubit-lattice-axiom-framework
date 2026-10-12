# C4 lane RF, probe F2: the matter sector with a preferred foliation

**Worker:** Claude Opus 5.5 (same family as the supervisor). Not refereed. Run 2026-10-11 16:23Z to 16:50Z.
**Labels:** proved / checked / suggested / reading / comparator. Literature bounds are quoted from memory (COMPARATOR) and were not re-verified.
**Scratch:** `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C4/F2/`. No repository file was edited.

## Plain summary

If the grid's own time slicing is the preferred frame (Z³ with continuous time), lattice-scale loops leave the electron slower than light by about 1% (−8.5e-3 at α = 1/137). With that split, photons above about 8 MeV would decay into electron–positron pairs. Photons of 1.4 PeV are observed, so the split must be below about 3e-19. Each pair of species needs its own hand-set cancellation, to about 1 part in 3e16 for e/γ. That is at least 1 tuning for QED and about 9 for the Standard Model, against P0's refereed 2. With time on the lattice and a step equal to the space step (Z⁴), symmetry sets all these splits to exactly zero. But there is then no preferred slicing in the matter sector, so that construction is not lane RF. Any foliation the gravity sector adds leaks into matter through graviton loops unless its scale is at least 9 decades below the lattice scale. **Matter-sector verdict: FAIL (bounded)**, pending the other-vendor referee.

## 1. What is generated, and how large

### 1a. Which dimension-4 Lorentz-violating coefficients exist (proved, representation theory)
- **The axioms give only proper cubic rotations O.** Under O:
  - spin 1 → T1;
  - spin 2 → E ⊕ T2.

  Neither contains the trivial rep A1. So in the grid frame, every rank-2 dimension-4 coefficient reduces to its isotropic part.
- **Per fermion multiplet:** one isotropic c₀₀ ("c_TT"). This is also a separate speed per chirality if parity is not supplied (d₀₀).
- **Per gauge field:** κ_tr only. All 10 birefringent components of k_F are spin-2 objects, and κ̃_o+ is spin-1.
- **Per scalar:** k₀₀.
- **No dimension-4 vacuum birefringence.** κ_tr is non-birefringent in every frame, so a boost to the lab frame cannot create it.
- **The graviton is the exception.** Its rank-4 kinetic structure keeps cubic anisotropy (R2: 2 isotropy tunings plus 1 match).
- **Dimension 3 (if not forbidden).** Since O contains no inversion, the CPT-odd rotation scalars b₀ (fermion) and (k_AF)₀ (Chern–Simons) are not forbidden by the Lattice axiom.
  - Their natural size is ~(g²/16π²)·a⁻¹ ~ 1e16 GeV. The bounds are ≲1e-27 to 1e-43 GeV.
  - They must be forbidden by C/P/T structure that the matter law supplies. For vector-like staggered QED that structure exists (comparator: staggered C, T and shift-parity; Golterman–Smit). For chiral SM matter it is open, tied to the chirality wall (suggested).

### 1b. One-loop QED on Z³ with continuous time (checked)
**Model:** Kogut–Susskind-type naive fermions, which are 4 × staggered (3D staggered = 2 tastes), with a non-compact U(1) photon.
- Self-energy in Feynman gauge.
- k₀ integrals in closed form.
- Midpoint Brillouin zone up to L = 800.
- m, λ → 0 by fits.

| Quantity, in units of e²/16π² | Value |
|---|---|
| δc_f (fermion; staggered = naive per taste) | **−16.06 ± 0.01**, of which the link tadpole is −17.97 and the rainbow +1.9 |
| δc_γ per Dirac taste in the loop | **−0.671 ± 0.001** (−1.34 for one 3D staggered field) |
| **Δ_QED = δc_e − δc_γ** (3D staggered) | **−14.7** |

**Checks:**
- **Brute-force 4×4 Dirac algebra agrees with the closed form to 1e-6.**
- **The speed does not depend on the gauge choice (ξ = 0, 1, 3).** The residual is ∝ m²: 0.075 at m = 0.2 and 0.0027 at m = 0.02. It is an off-shell mass artefact.
- **The Ward identity Π_xx(0,0) = 0 holds** to 3e-16.
- **The vacuum-polarization log matches the continuum** e²/6π² ln(1/m) per Dirac doubler.
- **An independent 4D anisotropic-lattice code reproduces the continuous-time values as ξ = a_s/a_t → ∞**, approaching as ξ⁻². At m = λ = 0.3, ξ = 8 → ∞ extrapolates to −16.03 against the closed form's −16.01. For the photon per Dirac taste it gives −0.585 against −0.587.

**Physical size (checked arithmetic):** c_e − c_γ = −8.5e-3 (α = 1/137) to −1.2e-2 (α = 1/100).
- **The lattice sign is c_γ > c_e.** Photon decay γ → e⁺e⁻ is then open above 7.8 MeV.
- **Bound:** one 1.4 PeV photon (LHAASO; comparator) gives c_γ − c_e < 2m_e²/E² = 2.7e-19. The untuned value is about 3e16 times too large.

**Yukawa comparison:** T1's nearest-neighbour Z³ value (Wilson fermion plus scalar) was −2.50.
- **Reading:** the coefficient depends on the species pair and on the regulator, and is O(1–15) × g²/16π². There is no sign pattern that makes them cancel.
- **Not computed:** compact U(1) or SU(N) links. They add self-interaction and plaquette tadpoles to the gauge boson's speed.

### 1c. Time on a lattice, a_s/a_t = ξ (checked; IR-resolved at m = λ = 0.3, L = 40 and 56 agree)

| ξ | 1 (hypercubic Z⁴) | 1.5 | 2 (K7a's stable τ = a_s/2) | 4 | 8 | ∞ (continuous time) |
|---|---|---|---|---|---|---|
| δc_f | 2e-12 (roundoff) | −8.04 | −11.50 | −14.99 | −15.77 | −16.01 |
| Δ (4D staggered, 4 tastes) | 0 | −7.30 | −10.26 | −13.00 | −13.52 | — |

- **Hypercubic Z⁴:** the zero is forced by W(B4), which maps the time coefficient onto a space coefficient (proved). The same holds for every rank-2 dimension-4 term.
- **Only ξ = 1 is protected.** At the stable leapfrog tick the split is already −10 × e²/16π².

### 1d. Bounds and tuning count (Z³ × continuous time, or any ξ ≠ 1)
**Natural size:** O(1–20) × g²/16π² ≈ 1e-3 to 1e-2 per species pair. The size is set at the cutoff.
- **Running cannot fix it.** Below the cutoff, Chadha–Nielsen-type logarithmic running reduces it by about 0.89 over M_Pl → m_e (suggested estimate, b = 1).

**Bounds (comparator):**
- **e/γ:** < 2.7e-19 for the lattice sign (photon decay). With the opposite sign, laboratory bounds are ~1e-15 (LEP or Compton edge).
- **p/γ:** < 4e-23 if c_p > c_γ (GZK protons, vacuum Cherenkov); < 9e-13 for the lattice-like sign.
- **ν:** ≲ 1e-19 to 1e-20 (IceCube PeV neutrinos).
- **graviton/γ:** −3e-15 to 7e-16 (GW170817).
- **Boosted clock comparisons** constrain β·c₀₀ and β²·c₀₀ for p and n, if the grid frame moves at β ~ 1e-3 relative to Earth.

**Tunings needed:** one isotropic speed per irreducible field, minus one overall time unit (the Coleman–Glashow counting).

| Matter content | Relative speeds to tune |
|---|---|
| Minimal staggered QED | **1**, at ≤ 3e-17 of its natural size (+1 chiral d₀₀ if P is not supplied) |
| SM, first generation, flavour-universal: B, W, G, H, Q, u, d, L, e, plus a supplied graviton | **9** relative speeds; at least 6 bounded below 1e-15 (γ, e, the u/d/G combinations in p and n, L via ν, graviton). The graviton adds R2's 2 isotropy tunings |
| With flavour matrices | up to 49 |

The precision required is 1e-12 to 1e-20 of natural size. That is mild beside P0's 1e-99, but there are more of them.

**Tadpole improvement does not count as protection.** Mean-field links remove the −18 part, but that is a choice of the bare speed, i.e. a tuning. The +1.9 rainbow remains.

## 2. Known escapes, tried on this lattice

| Escape | On this lattice | Status |
|---|---|---|
| **Supersymmetry** (Groot Nibbelink–Pospelov: SUSY forces dimension-4 c_μν to be universal, hence removable; breaking leaves ~(m_soft/M_Pl)² ~ 1e-32) | Needs {Q, Q̄} ∝ P_μ with an exact spatial momentum generator. Z³ has none: the lattice Leibniz-rule no-go (Kato–Sakamoto–So, comparator) and the packet's own no-exact-local-momentum results (Lemma R, lanes RS/RG/RC). Q-exact lattice SUSY (Kaplan–Ünsal, Catterall) and Hamiltonian H = {Q, Q†} lattice models have no P in the algebra, so they do not relate boson and fermion speeds | **Fails** (suggested) |
| **Separation of scales** (Pospelov–Shang; Hořava with M_* ≪ M_Pl) | Needs matter that is Lorentz-invariant up to its own cutoff. On Z³ × R, matter's own loops already give 1e-2 (§1b), so it fails there. With matter protected by Z⁴, graviton loops give ~(M_*/M_Pl)²/16π². Meeting 1e-20 needs **M_* < 1.5e10 GeV = 1.3e-9 M_Pl** (checked arithmetic). That conflicts with a⁻¹ = M_Pl unless the gravity law supplies an unexplained hierarchy (z = 3 coefficients ~(M_Pl/M_*)⁴ ~ 1e36 in lattice units) or the scale-reference primitive is given up | **Fails** within the axioms and primitives; it is a price otherwise (suggested) |
| **Custodial internal symmetries** (staggered shift or taste symmetry; GUT multiplets) | They make speeds equal within a multiplet: all tastes share one speed (Golterman–Smit, comparator), and a GUT multiplet shares one. Only SUSY relates different spins (Coleman–Mandula / HLS, comparator). At least 3–4 relative speeds remain (spin 0, ½, 1, 2) | **Partial**: reduces the count, not to zero (suggested) |
| **Hypercubic Z⁴ block** (T1, K7a) | Kills every rank-2 dimension-4 split exactly, with no tuning, because ξ = 1 is a symmetry point (proved; checked §1c) | **Works for matter.** But: (i) there is no preferred slicing at dimension 4, so it is **not RF**; (ii) K7a: A25's leapfrog is unstable at the hypercubic tick, and the stable τ = a_s/2 gives Δ = −10.3 (checked); (iii) 4 tastes, not the 2 of H_ψ; (iv) time on a lattice with a_t = a_s is supplied structure, since the axioms carry no time metric; (v) the graviton's 5 anisotropic forms remain open (lane K) |
| **IR attraction** (Chadha–Nielsen; Anber–Donoghue) | Logarithmic running gives a factor of about 0.89 for QED. Strong-coupling emergent Lorentz invariance (Bednik–Pujolàs–Sibiryakov) needs a strongly coupled sector spanning many decades; the framework's matter has none | **Fails** (suggested / reading) |
| **Integral Lorentz group** O(3,1;ℤ) on a Lorentzian ℤ⁴ | It is Zariski-dense, so its invariant tensors are Lorentz-invariant at every rank. But its orbits are infinite, so no finite neighbourhood is invariant: locality fails, as in Dowker–Henson–Sorkin | **Fails** on locality (suggested) |
| **D4 / F4 (24-cell) lattice** | Its 4th-rank tensors are isotropic (as in the FCHC lattice-gas). That is relevant to the graviton's rank-4 anisotropy, not to matter. It is Euclidean, so it has no foliation; a degree-6 invariant remains. Not checked | Aside (suggested) |

**Result of trying:** no escape removes the matter splits on a lattice with a preferred slicing without tunings beyond P0. The only tuning-free mechanism is time–space hypercubic symmetry, and that mechanism removes the preferred slicing itself.

## 3. Verdict against the FIXED readings (matter sector)

| Realization | Untuned | Tuned | Reading |
|---|---|---|---|
| A. The grid's own slicing, Z³ × continuous time | Violates the photon-decay bound by about 16 orders; the p/n, ν and GW bounds are similar | Needs ≥1 (QED) to about 9 (SM) speed tunings; P0 refereed has 2 | **FAIL** |
| B. Time lattice with ξ ≠ 1 (including K7a's stable tick) | Same: Δ = −10.3 at ξ = 2 | Same | **FAIL** |
| C. Hypercubic Z⁴ (ξ = 1) | Matter passes at dimension 4, with 0 tunings | — | **Not an RF realization** (no preferred foliation in matter). Adding RF's foliation via gravity percolates violation unless M_* ≲ 1.5e10 GeV, which conflicts with a⁻¹ = M_Pl. INCONCLUSIVE at best, decided by F1 |

**Matter-sector verdict: FAIL (bounded)** to:
- one loop;
- the U(1) non-compact photon plus naive/staggered fermions (and T1's Yukawa);
- realizations A–C.

The other-vendor referee is still required.

**Relation to P0.** On a continuous-time grid, this quantifies lane K's "generically expected" speed cost: P0 there is 2 + ≥1 (QED) to about 9 (SM). On Z⁴, P0's matter speed cost is 0. So lane RF's matter sector is never cheaper than P0 on Z⁴ for matter speeds. This matches the supervisor's expectation (FAIL on tunings).

## Files (scratch)
- **`f2_qed_speeds.py/.out`:** first pass, with the closed-form k₀ check.
  - Its m = 0.05, L = 64 photon row is unresolved; use `f2_ir_photon.out`.
- **`f2_ir.py/.out`:** the fermion IR series.
  - Its photon rows are contaminated (k_x ~ m); superseded.
- **`f2_ir_photon.py/.out`:** the photon IR series (fits in the summary).
- **`f2_gauge_check.py`, with `f2_gauge_check.out`, `_L16.out` and `_scan.out`:** brute-force Dirac algebra and gauge independence.
- **`f2_aniso.py`:** the ξ scan.
  - Its `.out` is under-resolved at m = 0.1; use `f2_aniso_resolved.py/.out`.
  - `f2_aniso_xi16.py/.out`: the exact zero at ξ = 1, and ξ = 16.
- **`f2_numbers.py/.out`:** physical sizes, bounds, the Pospelov–Shang M_*, and the running factor.
