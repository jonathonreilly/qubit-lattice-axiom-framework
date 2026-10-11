# C4 lane RK2, probe K1: what keeping the grid costs on Z⁴ (the tuning count)

**Worker:** Claude Opus 5.5 (same family as the supervisor). Not refereed. Run 2026-10-11 17:10Z to 17:53Z.
**Labels:** proved / checked / suggested / reading. "Comparator" means literature quoted from memory and not re-read.
**Scratch:** `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/C4/K1/`. No repository file was edited. Every run used OMP_NUM_THREADS=2 and took under 6 minutes.

## Plain summary

Put time on the grid with the same step as space (Z⁴). The question is how many hand-set numbers keep a graviton massless with a single light cone.

The symmetry of the 4D grid allows two kinds of unwanted term:
- 3 mass terms;
- 8 two-derivative terms that break the graviton's gauge symmetry. Five of these make the graviton's speed depend on direction or polarisation (the "5" of lane K). The other three are direction-blind but still break the gauge symmetry.

I computed the one-loop vacuum response of a staggered fermion plus a non-compact photon on Z⁴, each coupled to the metric in a natural, grid-symmetric way:
- All 3 masses come out nonzero.
- All 9 two-derivative coefficients come out nonzero, and their combination is far from the gauge-invariant (Einstein–Hilbert) form.
- Gravitational waves would travel at speeds that differ by a factor of about 2 across lattice directions and polarisations unless the terms are cancelled by hand.

So the count is 11 tunings (3 masses + 8 kinetic forms) for an exactly gauge-invariant graviton at quadratic order. Even the most lenient reading, which counts only the two physical polarisations, needs 5 (2 masses + 3 speed/birefringence numbers). Either way it is more than P0's two shear tunings.

**Lane K's question, "two shear tunings alone?", is answered NO.**

## Verdict against the FIXED reading (K1)

**N_tune(Z⁴) = 11**, under the registered definition: mass forms plus non-gauge-invariant kinetic forms that are generated nonzero.
- The tally is 3 masses + 3 O(4)-invariant non-gauge-invariant kinetic forms + 5 anisotropic ones.
- The cosmological-constant (tadpole) tuning is counted separately, as P0 does.
- Lower bracket (suggested): **5**, counting only the TT sector. That is 2 TT masses + 3 TT speed/birefringence structures. The K referee's warning applies: once the masses are tuned, TT–longitudinal mixing brings further forms into the TT dispersion, so 5 is a floor, not a sufficient set.
- **Both numbers are greater than 2. Lane K: NO** (checked at one loop, for the stated couplings).

## 1. The form space (proved by exact rank computations; `forms.py` / `forms.out`)

The h-components are acted on by all 384 signed permutations. Invariants come from Reynolds averaging and ranks from the SVD, where the gaps are 1e0 against 1e-15, i.e. exact.

**Masses, O(q⁰): 3 forms.**
- M1 = Σ h_μμ², M2 = Σ_{μ≠ν} h_μν², M3 = (tr h)².
- None is gauge invariant: the gauge map has rank 3.
- 2 are visible on TT modes (M1, M2). These are the Z⁴ analogues of P0's E_g/T_2g pair. M3 is the trace mass.

**Two-derivative forms, O(q²): 9 forms.**
- F1 = s²h:h, F2 = |hs|², F3 = (shs)tr h, F4 = s²(tr h)²;
- A1 = Σs_μ²h_μμ², A2 = Σ_μ s_μ² Σ_ν h_μν², A3 = (Σs_μ²h_μμ)tr h, A4 = Σ s_μ h_μμ (hs)_μ, A6 = Σ_{μ≠ν} s_μ² h_νν².

Their structure:
- The O(4)-invariant subspace has dimension 4 (F1–F4).
- The gauge map δh = sξ + ξs has rank 8. Its unique null vector is **EH = ¼(F1 − 2F2 + 2F3 − F4)**, the linearised Einstein–Hilbert / Fierz–Pauli kinetic form.
- The gauge images split into 3 from the O(4) block and 5 from the anisotropic block.
- Restricted to TT modes, the forms have rank 4: 1 isotropic + 3 anisotropic (A1, A2, A6; A3 and A4 vanish on TT).
- This reproduces K7a's and K-ana's 9/4/1 count, and the referee's rerun, independently.
- The O(4) Haar averages match K-ana's §3.1 exactly, e.g. ⟨A1⟩ = F1/24 + F2/6 + F3/12 + F4/48 (`count.out` header).

**What "the 5" means.** Lane K's "5 non-gauge-invariant forms" are the anisotropic (O(4)-breaking) directions. The full set of non-gauge-invariant kinetic directions is **8 = 3 O(4) + 5 anisotropic**. Adding the 3 masses gives **11 non-gauge-invariant W(B4) structures in all.**

## 2. One-loop induced coefficients (checked)

**Setting.**
- Euclidean Z⁴, ξ = a_s/a_t = 1, one loop (each sector's free loop, O(e⁰)).
- h is a symmetric tensor field. A cosine wave h = H cos(q·x) is used to read off Γ₂/V = ½[Σ c_Mk M_k(H) + Σ c_j K_j(H,H;q)] + O(q⁴), where c are action-density coefficients in lattice units.

**Fermion coupling** (`loop_fermion.py`).
- Naive fermions with a link-averaged vielbein: S_f = Σ_x Σ_μ ½[ψ̄(x)γ_a E_a^μ(x+μ/2)ψ(x+μ) − h.c.-partner] + m ψ̄ψ.
- E = (1 + h̄)^(−1/2), with h̄(x+μ/2) = ½[h(x) + h(x+μ)] and h site-placed.
- The fields are densitized, so there are no √g or ln det g measure terms.
- The coupling is W(B4)-covariant, exactly U(1)-gauge invariant, and correct in the continuum limit. Its stress is natural, not conserved.
- **Staggered proxy:** reported per 4D staggered field as naive/4. This is exact for the h-independent action. For the vielbein coupling, spin diagonalisation fails because a hop along μ carries γ_a with a ≠ μ. The proxy is therefore a 4-taste W(B4)-covariant regulator, not a one-component staggered action (reading).

**Photon coupling** (`loop_photon.py`).
- K-num's corner metric: S = Σ_{x,s} (1/64) √g g^{μρ}g^{νσ} F^s_μν F^s_ρσ over the 16 corners. The diagonal of h sits on sites and the off-diagonal on plaquette centres.
- An h-independent Feynman gauge fixing is exact, because S is U(1) invariant for every h.

**Numerics.**
- Periodic midpoint rule on L⁴ grids.
- On-grid momenta q = (2π/L)k·n with k = 1, 2, 3, and a 3-point Richardson step to remove q⁴ and q⁶.
- Six lattice directions n, fitted jointly to the 9 forms.

### 2a. Results (lattice units, per cell)

| | tadpole t (Γ₁/V = t tr h) | net masses M1, M2, M3 (after the CC cancels the tadpole) |
|---|---|---|
| 1 staggered field, m = 0.15, L = 80 | +0.1233 | −0.0512, −0.0365, −0.0182 |
| 1 staggered field, m = 0.10, L = 96 | +0.1242 | −0.0514, −0.0366, −0.0183 |
| photon, L = 48 (constant-metric code) / L = 32 (loop) | **0 exactly** (Weyl) | +0.1033, +0.2028, −0.0258 |
| QED content (m = 0.15) | +0.1233 | **+0.0521, +0.1663, −0.0441** |

| c_j | F1 | F2 | F3 | F4 | A1 | A2 | A3 | A4 | A6 |
|---|---|---|---|---|---|---|---|---|---|
| staggered, m = 0.15 | +4.17e-3 | 0 (1e-17) | 0 | −9.47e-4 | +3.88e-3 | +1.54e-2 | −1.66e-3 | 0 | +5.99e-4 |
| photon | +9.35e-3 | +6.56e-3 | +5.08e-3 | −7.27e-3 | +8.09e-2 | −2.53e-2 | +2.08e-3 | −6.04e-2 | +1.61e-2 |
| **QED total** | +1.35e-2 | +6.56e-3 | +5.08e-3 | −8.22e-3 | +8.48e-2 | −9.88e-3 | +4.3e-4 | −6.04e-2 | +1.67e-2 |

**Massless trend** (per naive fermion, m = 0.5 / 0.3 / 0.2 / 0.15 / 0.1). Every coefficient varies smoothly and stays finite and nonzero:
- A2: 0.0591 / 0.0610 / 0.0615 / 0.0615 / 0.0616;
- F1: 0.0127 / 0.0152 / 0.0163 / 0.0167 / 0.0170;
- A3: −0.0082 / −0.0075 / −0.0069 / −0.0066 / −0.0063.

The photon is massless with no regulator.

**Distance from the gauge-invariant form.**
- **QED total:** the O(4) part is not EH-shaped (non-EH residual / O(4) part = 0.84), and |anisotropic| / |O(4)| = 4.9 (coefficient norms in the canonical Â basis). The normalised O(s³) Ward violation is |Gc|/(|G||c|) = 0.15; it is 0 if and only if c ∝ EH.
- **Small coefficient:** the QED-total A3 (4.3e-4) is a partial cancellation between the fermion (−1.66e-3) and the photon (+2.08e-3). It moves with m (+2e-5 at m = 0.5, +4.3e-4 at m = 0.15, about +5e-4 as m → 0) and it is non-TT. It is nonzero, but small by accident, not by an identity.

### 2b. TT speeds (checked numbers; physical size is a reading)

The quantity reported is the TT stiffness per polarisation and direction, relative to ½q²h:h. An isotropic EH term gives one common value.

| Sector | Range of the TT stiffness | max/min |
|---|---|---|
| Fermion (m = 0.15) | 4.2e-3 to 1.02e-2 | 2.5 |
| Photon | 3.0e-3 to 2.55e-2 | 8.4 |
| QED total | 1.1e-2 to 3.3e-2 | 3.0 |

- **Tree EH term** (reading: K7a's Q × M̄²/2 with a = 1/M_Pl): TT stiffness M̄²/8 = 5.0e-3.
- **With the tree term added**, the TT stiffness still varies by a factor of about 2.4 across directions and polarisations.
- **Untuned, the graviton's speeds and birefringence are therefore O(1)** (suggested). Against GW170817 (|Δc/c| ≲ 1e-15; comparator), each of the 3 TT structures needs a tuning to roughly 1e-15 of its natural size. That is mild beside the masses' ~1e-99 (P0), but each is still a tuning.

### 2c. Checks (all checked)

**Constant metric = the q → 0 limit of the loop.**
- An independent constant-g free-energy code computes F(g) = −2∫ln(s̄g⁻¹s̄ + m²) for the fermion, and ½∫ln det′M_g for the photon.
- Its Hessian equals the loop's Π⁽⁰⁾:
  - fermion: to 9 digits, at every L;
  - photon: to 7 digits (0.1033910 against 0.103391038 at L = 8).
- Files: `loop_fermion_m*.out`, `photon_q0.out`.

**U(1) Ward identities.**
- The metric-coupled lattice Maxwell kernel annihilates the gauge mode for every h: |M(h)ŝ|/|M| ≤ 1e-15.
- The fermion vacuum polarisation Π_μν(0) → 0 exponentially in L: 2e-3, 1.5e-4, 1.2e-5, 1.0e-6 at L = 16, 24, 32, 40. The individual pieces are O(0.1). File: `ward_checks.out`.

**Gravitational Ward identity.** Violated at both orders by the natural stresses:
- at O(s): the net masses are nonzero;
- at O(s³): the kinetic vector is not EH-shaped (§2a).

**W(B4) covariance.**
- B(Rq) = ρ(R)ᵀB(q)ρ(R) to 5e-15, and B is even in q.
- The 9-form fits have residuals of 5e-5 (fermion, L = 80) and 1e-3 (photon, L = 32). This is the q⁸ / finite-L remainder.

**Photon Weyl identities (exact).** The corner action is unchanged under g_c → λ g_c, and T₁[φδ] = 0 for a site-placed trace. So:
- the photon tadpole is exactly 0, and Q(1) = 0;
- cM1 + 4cM3 = 1e-16;
- the O(q²) diagonal-trace identities hold to 1e-16: c_F1 + ½c_F3 + 4c_F4 + ½c_A3 + c_A6 = 0, and c_F2 + 2c_F3 + c_A4 + c_A1 + c_A2 + 2c_A3 − c_A6 = 0.

These two identities are a nontrivial end-to-end test of the photon q² code.

**Convergence.**
- Fermion: L 64 → 80 changes the coefficients by 2.8e-4 of the largest (m = 0.15).
- Photon: L 24 → 32 changes them by 7.2e-4; F2 itself moves 0.9%.

### 2d. A protected zero in the fermion sector (proved; checked to 1e-17)

The fermion's F2 = F3 = A4 = 0 is not an accident. These are exactly the forms whose monomials contain q_μq_ν with μ ≠ ν.

**The mechanism.**
- The naive action's doubler transformation ψ → (−1)^{x_μ}γ_μγ₅ψ, ψ̄ → (−1)^{x_μ}ψ̄γ₅γ_μ maps S_f[ψ, h] to S_f[ψ, R_μhR_μ] with positions unchanged: γ_a hopping along ν changes sign iff exactly one of a, ν equals μ.
- So Γ_f(H; q) = Γ_f(R_μHR_μ; q). Combined with W(B4) covariance, Γ_f is even in each q_μ separately.
- This holds for the fermion sector to every order in couplings that respect the transformation (the U(1) links do).
- The internal-reflection test: 4e-17 for the fermion; 7e-2 for the photon, which has no such symmetry (`doubler_check.out`).

**Consequences.**
- The photon generates all three cross forms. So does K-ana's free scalar.
- In the QED content, all 9 are generated.
- Mixed O(e²) diagrams, with a photon–h vertex inside a fermion loop, break the protection.
- Reading: this does not lower the count.

## 3. The count

| Tier | Mass tunings | Kinetic tunings | N_tune |
|---|---|---|---|
| **Registered definition:** all non-gauge-invariant W(B4) quadratic structures (exact linearised gauge invariance at quadratic order) | 3 (all generated) | 8: 3 O(4) + 5 anisotropic (all 9 coefficients nonzero; non-EH residual nonzero) | **11** |
| TT polarisations only, one light cone (suggested floor) | 2 (M1, M2 on TT) | 3 (TT images of A1, A2, A6, all nonzero) | **5** |
| Plus cosmological constant (separate, as in P0) | +1 | — | — |

**Notes on the count.**
- **(i)** "Independent counterterms" means symmetry-allowed, unprotected structures whose induced coefficients are nonzero. It is not the rank of one computed vector. The m-family spans a smooth curve (`span_check.out`), which does not measure that.
- **(ii)** The 3 O(4)-invariant non-gauge-invariant forms do not split the light cone. They give the vector and scalar parts of h kinetic terms, i.e. extra modes or ghosts.
  - A theory with only transverse diffeomorphisms (TDiff/WTDiff, unimodular-type; Álvarez et al.; comparator) might need fewer conditions in the O(4) block. That does not take the count to 2.
- **(iii)** An exactly conserved, W(B4)-covariant interacting stress with its gauge completion would remove all 11 together. Whether one exists is K2's question; it is not available here.

## 4. Comparison

**P0's stated 2** (Z³ with continuous time: two TT shear numbers, E_g and T_2g).
- On Z⁴ the TT mass count is the same, 2.
- But the graviton sector adds at least 3 TT speed/birefringence tunings (floor 5). With full gauge invariance it adds a trace mass and 8 kinetic tunings (11).
- So P0's "2" is incomplete on Z⁴ as well as on Z³ × ℝ.

**RF / F2.**
- F2 (refereed with corrections) found that matter speeds on Z⁴ need 0 tunings (exact W(B4)), against ≥ 1 (QED) to about 9 (SM) on Z³ × ℝ.
- K1 shows that Z⁴ moves the speed cost into the graviton sector: 3 TT structures, compared with R2's Z³ count of 2 isotropy + 1 match.
- For QED content:

| Setting | P0 on Z⁴ | P0 on Z³ × ℝ (F2 realisations A/B) |
|---|---|---|
| Total | 5 to 11 (+CC) | 2 TT masses + ≥ 1 matter speed + graviton isotropy (R2: 2 + 1) ≈ 6 or more (+CC), before any full gauge-invariance count |

- Reading: neither substrate keeps the grid for 2 tunings.

## 5. Scope and what is not done

- **Order:** one loop per sector (O(e⁰)). The interacting O(e²) cross-terms are not computed; they could only add structures.
- **Couplings:** one natural coupling per species, the "best available" in the sense that no conserved W(B4) stress with gauge completion exists in hand.
- **Fermion regulator:** the staggered result is the naive/4 proxy (§2).
- **Basis dependence:** while the masses are untuned, the individual q² coefficients depend on the h-placement basis (K-ana §3.7). The count does not, because the masses are themselves counted.
- **IR:** the masses and q² coefficients are IR-finite; the fermion is extrapolated in m, and the photon has no regulator.

## Files (scratch)

- `forms.py` / `.out`: the form space and ranks; `forms_data.npz`.
- `loop_fermion.py`, with `loop_fermion_m{0.5,0.3,0.2,0.15,0.1}.out/.json`: fermion masses, tadpole and kinetic coefficients, and the constant-metric check. m = 0.1 ran at L = 64 and 96 (change 6.5e-4 of the largest coefficient).
- `photon_q0.py` / `.out` / `.json`: photon constant-metric masses and the Weyl check.
- `loop_photon.py` / `.out` / `.json`: photon q² coefficients.
- `ward_checks.py` / `.out`, `doubler_check.py` / `.out`: the U(1), covariance, evenness and doubler checks.
- `count.py` / `.out` / `.json`: Haar projection, EH residual, TT spreads and totals.
- `span_check.py` / `.out`.
