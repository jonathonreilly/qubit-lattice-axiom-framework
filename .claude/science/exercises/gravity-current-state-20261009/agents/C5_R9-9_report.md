# C5 R9-9 report: a box-confined graviton. Does the TT mass stay zero under box-matter loops?

**Author.** Claude Opus 5.5 probe (same family as the supervisor and every C5 worker). Unrefereed. 2026-10-12, 17:07Z to 17:36Z. No repository file edited.
**Scratch.** `S/` = `.../scratchpad/C5/R9-9/`. Scripts and outputs in `S/scripts/` (each under 10 s at `OMP_NUM_THREADS=2`):
- `r99_profiles.py`: the band profiles L, G (R8-2's, B = 2.0, B₂ = 3.1) and the NN control;
- `r99_graviton.py` → `.out`: parts A (box graviton, tree level) and B (coupling to R8-2's stress);
- `r99_tt_selfenergy.py` → `.out`: part C, one-loop TT self-energy, the speed identity, sign tests, metric-seagull masses;
- `r99_edge_family.py` → `.out`: one-parameter edge family, zeros of the speed shifts and of the mass;
- `r99_inv.py` → `.out`: the invariant-mass (INV) control;
- `r99_numbers.py` → `.out`: physical sizes (readings);
- `r99_exact_norm.py` → `.out`: exact-diagonalization check of the self-energy normalization.

**Read.** `docs/MINIMAL_AXIOMS_2026-06-29.md` in full (`AX`). `TESTS.md`: C5 method and round 1 (`:2302-2420`), rounds 7–9 and all referee lines through `:3876`; R9-9 is `:3866-3876`. `SUMMARY.md` §§15–20 (`:334-532`). `PRICE_NOTE.md` v6 delta (`:251-413`; V3 at `:290-295`, the RN L1 correction at `:339-352`). The 09-14 note (`N0914` below). Agents: `C5_R8-2_report.md` and verdict; `C5_R7-4_report.md` and verdict; `C5_R8-5_report.md` and verdict; `C4_V3_report.md` (§1) and `C4_V3_referee.md`. `scripts/C5/R8-2/r82_edge.py`. The scratch R9-2 report (`.../scratchpad/C5/R9-2/R9-2_report.md`, unrefereed, present at 17:12Z). R3-2 (LRL graviton count) was not needed and not used.
**Labels.** proved / checked (numerics here) / suggested / reading / comparator / RECALLED (from memory, not verified).

---

## 0. In plain words

- **The box graviton exists at tree level.** Take the 09-14 linear graviton (two exact commuting constraints, two TT modes) and replace its lattice derivative by R8-5's photon trick: a smooth, non-analytic symbol equal to q on a box. The gauge structure stays exact, the TT waves have ω = |q| exactly on the box, and nothing else on the zone is massless (checked to 1e-15). R8-2’s universal box⊕edge stress, rebuilt with this graviton’s divergence symbol d(q)e^{iq/2} (midpoint phases on spatial indices), obeys exactly the Ward identity the graviton needs (checked to 3e-15). So "an explicit box graviton coupled to universal box matter" is built.
- **With R8-2's matter as specified (number-conserving, empty vacuum), matter loops vanish identically.** The vacuum has no particles and the stress cannot create any, so the graviton's self-energy from matter is exactly zero at every order. The TT mass stays zero and the TT speed stays exactly the matter speed. This is true but empty: nothing is tested.
- **Give the matter a vacuum that can create pairs (a free scalar field with the same box dispersion), and both protections fail, through the edge.**
  - **Speed (new, proved identity).** The TT speed shift equals a vacuum-weighted zone average of the same boost anomaly A = Hess(ε²/2) − 1 that makes edge quanta fall wrongly (R8-2 Theorem E): c_T² − 1 = (2/M²)·(1/32)⟨|V|² A_zz/ε⁵⟩ for every TT vertex that depends only on the pair's transverse momenta. On the box A = 0, so the box contributes exactly nothing; the edge contributes everything. For the gapped edge A_zz ≤ 0 everywhere, so the graviton is slower than matter for **every** such vertex (proved). The literal edge gives the opposite sign (checked).
  - **Mass.** R9-2 (unrefereed) finds the E_g shear mass on the edge with its flow seagull. With the minimal metric seagull used here, the two TT polarizations get different masses (a CC-independent split), and 13–30% of it even comes from inside the box, because the box is a cube.
  - **One knob cannot fix it.** Along the L→G edge family, the speed shift vanishes at t* = 0.230 (T_2g) and 0.263 (E_g), R9-2's mass at 0.288, and the metric-seagull mass split never. All move with the matter mass.
- **Sizes.** At a = ℓ_P, one scalar species with the metric vertex gives |c_T − 1| ≈ 1.3e-2 to 6e-2 (4e12–9e13 times the GW170817 band). The speed shift scales as (ℓ_P/a)², so it is harmless for a ≳ 1e7 ℓ_P. The TT mass split is not: for any a ≤ 1e-19 m it is at least about 3e-4 eV, about 1e19 times the graviton-mass bound (bound RECALLED).
- **The INV route (invariant-mass pair vertices) protects the speed exactly** (checked to 1e-12) but leaves the mass equal to one seagull number that nothing built here fixes.

**Against the FIXED readings (worker reading; referee required).** FAIL (bounded) for pair-creating free scalar box matter in the class of §1. In R8-2's empty-vacuum class the PASS clause is met on the letter, vacuously. The INV variant is INCONCLUSIVE.

---

## 1. Hypotheses and classes (stated before any title)

- **H-grav (the box graviton).** N0914's weakly gauge-invariant H_N (`N0914:72-74`):
  - H_N = (J/2)∫[E:E − (tr E)²/2] + (g/2)∫h:R(h), with R_ij = −ε_iab ε_jcd d_a d_c h_bd in midpoint variables;
  - constraints G_j = d_i E_ij and S = tr R;
  - the midpoint symbol q̂ = 2 sin(q/2) of `N0914:138-140,300-301` is replaced by d(q) = ρ(q)q + (1 − ρ(q))·2 sin(q/2), with ρ = 1 on |q| ≤ c₁ = 1 and 0 on |q| ≥ c₂ = 2.5 (R8-5's photon symbol, `C5_R8-5_report.md:126-131`). In R8-2 form the divergence symbol is D(q) = d(q)e^{iq/2}.
  - Fields h, E are non-compact canonical pairs, as in N0914's H_N comparator (`N0914:75-83`). Jg = 1.
- **H-mat.** Two matter classes:
  - (F) R8-2's class: one CAR mode per site, H₀ = Σε(k)n_k, number-conserving stress T = ΣF a†a (Construction A), empty Fock vacuum (`C5_R8-2_report.md:25-34`);
  - (Z) a free real scalar field with the same dispersion, ε² = m² + Σ_i u(k_i), profiles L and G of R8-2 (`C5_R8-2_report.md:26-28`), plus an NN control. Its vacuum has zero-point energy and the stress creates pairs. This is the "vacuum with energy" of R9-2 (`R9-2_report.md:225-227`).
- **H-couple.** GR normalization: L_TT = (M²/4)(ḣ² − (∇h)²) for one TT polarization, coupling ½h_μνT^μν; M is the reduced Planck mass, κ_lat := 1/(Ma)² = 8π(ℓ_P/a)².
- **H-TT (class 𝒱).** q along a cubic axis (z). TT polarizations T_2g (h_xy) and E_g (h_xx = −h_yy). The TT pair vertex |V|² depends only on the pair's transverse momenta (k_x, k_y), not on k_z or q. Two members are evaluated:
  - M (minimal metric coupling √g g^{ij}∇_iφ∇_jφ): |V|² = 4u_xu_y (T_2g), (u_x − u_y)² (E_g);
  - U (forward value equal to R8-2's F^{ij}(k,k) = εv_iv_j): the same with u → p² where p = u′/2.
- **Completion assumed, not built.** For q ∥ axis, W1 does not constrain the TT components. The field-theory stress is assumed to be completed by longitudinal and time components that obey W1 with D = d e^{iq/2}. For the pair-creating field that completion is not constructed here; R8-2 built it only for the number-conserving class.
- **H-seagull.** The O(h²) term is ultralocal in h (h(x)² times a local matter operator), as in the metric coupling. It then shifts the TT mass but not the speed.
- **Excluded, not addressed:**
  - matter's own one-loop speed shift from graviton loops (O(κ_lat), same order as the TT shift);
  - graviton self-interaction and graviton loops;
  - fermion (Dirac-sea) matter in class (Z);
  - q along non-axis directions;
  - TT vertices depending on k_z or q, except the INV control;
  - non-ultralocal seagulls (a q²-dependent seagull is exactly a TT speed counterterm);
  - two loops;
  - compact or finite-dimensional link variables;
  - ⊗M₂ realizations.

## 2. Prior art (each counted once)

- **N0914.** The N-type theory, its exact commuting constraints and two TT modes; ω² = Jg k²; the regular compact-character bound forcing O(k³) for compact characters; the non-compact H_N as the escape (`N0914:69-83,186-216`). Part A is N0914 with one symbol changed.
- **R8-5** (refereed FAIL, bounded; `TESTS.md:3807-3813`). The non-analytic box symbol for a gauge field, and the one-loop cone split for QED. Part A borrows its symbol; part C is the gravitational analogue of its computation.
- **R8-2** (CWC, INCONCLUSIVE; `TESTS.md:3550-3557`). Construction A, W1 with any single-zero D, Lemma U, Theorem E and its anomaly A = Hess(ε²/2) − I with zone mean −I (`C5_R8-2_referee_verdict.md:31-47`).
- **R9-2** (scratch, unrefereed). Part (a): R8-2's empty vacuum gives μ = 0 trivially. A zero-point vacuum gives μ_E = −2.0565e-1 (L), +7.9761e-3 (G) at m = 1, edge-carried, μ_T2 = 0. Along u_t = (1 − t)u_L + t u_G the zero is at t* = 0.287922 (m = 1) and 0.297708 (m = 0.3) (`R9-2_report.md:30,217-252`; `r92_shear_tune.out`). **I do not recompute this.** §3.4 uses a different seagull, as a second prescription.
- **V3** (CWC). μ_E = +1.97038864e-3 for the NN scalar in RN-L1 normalization. √g·Λ enters E_g and T_2g equally, so a split between them is CC-independent (`C4_V3_referee.md:3,25-27`; `PRICE_NOTE.md:290-295`).
- **R7-4** (CWC). The linear lapse/shift bridge and the named tunings: T1 (c_g = c), T2, T3 (`C5_R7-4_report.md:99-106`). The GW170817 band −3e-15 ≤ Δc/c ≤ 7e-16 (`C5_R7-4_report.md:46`).
- **TT speed splits from lattice matter (count once).**
  - C3 K-num, ARGUED: "A ≥10% relative splitting of the induced TT speed²" for its coupling (`agents/C3_K-num_report.md:219`);
  - C3 K-ana and C4 K1: 3 TT speed/birefringence structures (`agents/C3_K-ana_report.md:113`; `agents/C4_K1_report.md:29`);
  - C4 E1 (CWC): matter RG does not attract the graviton speed (`agents/C4_E1_referee.md:19`).

  §3.4's NN control (16π|Ξ| ≈ 0.096 at a = ℓ_P, i.e. a 10% speed² shift) agrees in size with C3 K-num. That is a comparator only: different coupling and normalization.
- **R7-5 / R8-4** (INV lemma, conditional; two-loop non-closure in toy N, refereed; `TESTS.md:3500-3504,3815-3821`).
- **Repo search.** I grepped TESTS and agents for "graviton speed", "TT speed", "c_T" and A_zz-type identities. No prior identity links the one-loop TT speed shift to Hess(ε²/2) − 1.

---

## 3. Results

### 3.1 A: the box graviton at tree level. Proved; checked (`r99_graviton.out:1-15`)

- **Why the algebra survives (proved).** Every N0914 identity used is algebraic in the midpoint symbols: R symmetric, R(d⊗ξ + ξ⊗d) = 0, Bianchi d_iR_ij = 0, {G, S} = 0. Each needs only that the symbols are real and commute (`N0914:145-147`). Replacing q̂ by a real d keeps all of them.
- **The periodic divergence symbol.** D = d e^{iq/2} is smooth and periodic, satisfies D* = −D(−q), and vanishes only at q = 0. These are R8-2's conditions (`C5_R8-2_report.md:88,92-94`).
- **Checks over 5000 random q.**
  - R symmetric: 0;
  - gauge invariance 1.8e-15; Bianchi 2.7e-15; {G, S} = 6.2e-15;
  - TT ω²/(Jg|d|²) − 1 = 2.0e-15;
  - the transverse spatial form has eigenvalues |d|²(1, 1, −1). The −1 is N0914's −k²|tr h_T|²/2, removed by S.
  - D periodic at the face (2e-9) with matching first and second derivatives; |D* + D(−q)| = 1.1e-15.
- **Box.** On |q_a| ≤ c₁, max |ω_TT − |q|| = 1.8e-15.
- **No graviton doublers.** min |d| = 0.0500 on |q| ≥ 0.05, and d(π) = 2.
- **Prices of A (reading):**
  - non-compact (infinite-dimensional) h, E per face/site, the same escape N0914 names from its compact-character bound (`N0914:75-83,218-223`);
  - a non-analytic symbol with super-polynomial tails (R7-1/R8-5's price);
  - Jg = 1 = the matter box speed, which is R7-4's T1, here imposed by the registered setting "ω = |k| in a box" (`TESTS.md:3867`).

### 3.2 B: the coupling to R8-2's universal stress. Proved; checked (`r99_graviton.out:17-30`)

- **What changes in R8-2.** Construction A with D = d e^{iq/2}. The continuum kernel F_c carries a midpoint phase e^{−iq_j/2} per spatial index, i.e. T^{0j} at link midpoints and T^{jl} at (e_j + e_l)/2, the 09-14 placement. On supp φ (|q_i| ≤ 0.9 < c₁), d = q, so ω F_c^{0ν} = Σ q_j F_c^{jν} becomes ωF^{0ν} = ΣD_jF^{jν} (proved, one line). The dust part needs only a single-zero D (R8-2).
- **Why this is the graviton's own Ward identity (proved).** With δh_ij = i(D_i*ξ_j + D_j*ξ_i), the midpoint variables h̃_ij = e^{i(q_i+q_j)/2}h_ij turn this into N0914's δh̃ = i(d_iξ̃_j + d_jξ̃_i). The variation of Σh*T is −2iΣξ_j* D_iT^{ij} = −2iΣξ_j* ωT^{0j}, which the lapse/shift terms absorb, exactly as in RN L1 / R7-4 Result A (`C5_R7-4_referee_verdict.md:79`).
- **Checks (profiles L and G, d = 2):**
  - Ward residual ≤ 2.7e-15 on all four sets (random, box pairs, box→edge, edge→edge);
  - Hermiticity ≤ 2.7e-11; symmetry ≤ 1.8e-15;
  - forward values ε(1,v)(1,v)ᵀ to 3e-8.
- **Scope.** Linear order. Universal coupling among free species is a choice (R7-4's T2), as in R8-2. Lemma U (box–edge matrix elements at the face) is inherited.

### 3.3 C(F): R8-2's class. The TT self-energy from matter vanishes identically. Proved

- **Proof.** T^{μν}(q) = ΣF a†_{k+q}a_k annihilates the empty vacuum, and any number-conserving seagull has ⟨0|S₂|0⟩ = 0. So the vacuum is an exact eigenstate of H₀ + h·T + O(h²) for every h, and the matter-induced effective action of h is identically zero, at every loop order. R9-2 records the same zero for uniform strain (`R9-2_report.md:225`).
- **Consequence.** The TT mass is 0, and the TT dispersion is the bare ω = |q| on the graviton box. Matter's is ω = √(m² + k²) on its box. The TT speed equals the matter speed exactly (difference 0, not merely below 1e-15), at tree level on the overlap of the two boxes.
- **Why it is empty (reading).** Nothing in (F) can polarize the vacuum, so no loop tests gauge protection. Matter's own one-loop shift from graviton emission (nonzero in (F): a particle emits and reabsorbs a graviton) is not computed here.

### 3.4 C(Z): pair-creating box matter (free scalar field)

**The one-loop formula (standard second order; static normalization checked by exact diagonalization).** `r99_exact_norm.out`: for a central-difference scalar on L = 6, 8 tori, the exact zero-point energy ½tr√K under a static T_2g perturbation reproduces the paramagnetic formula below with ratio 1.0000002 at three (L, q) (the residual is the O(h⁴) finite-difference error). Per volume, with ⟨·⟩ = ∫d³k/(2π)³:

  Π(ω, q) = S₂ − ¼⟨|V|²/(εε′) · E/(E² − ω²)⟩, ε′ = ε(k_⊥, k_z − q), E = ε + ε′.

The dispersion is (M²/2)(ω² − q²) = Π, so c_T² − 1 = (2/M²)Ξ with Ξ := ∂_{q²}Π + ∂_{ω²}Π, and the TT mass² is 2Π(0, 0)/M².

**Theorem T (speed identity). Proved; checked.**
- **Statement.** In class 𝒱 with an ultralocal seagull, on any periodic C² separable band,

  **Ξ = (1/32)⟨|V|²·A_zz/ε⁵⟩, with A_zz = Hess_zz(ε²/2) − 1.**
- **Proof.**
  1. β = ∂_{ω²}Π = −(1/32)⟨|V|²/ε⁵⟩.
  2. α = ∂_{q²}Π(0, q) = −(1/8)⟨|V|²[(7/4)(∂_zε)²/ε⁵ − (3/4)∂_z²ε/ε⁴]⟩. Integrating by parts in k_z (periodic; |V|² is k_z-independent) gives α = (5/32)⟨|V|²(∂_zε)²/ε⁵⟩.
  3. ∂_z(∂_zε/ε⁴) = [Hess_zz(ε²/2) − 5(∂_zε)²]/ε⁵ integrates to zero on the torus. Hence α + β = (1/32)⟨|V|²(Hess_zz − 1)/ε⁵⟩. ∎
  4. The seagull is ω- and q-independent, so it drops out.
- **In the continuum,** Hess = 1 and Ξ ≡ 0 for every vertex. That is the Lorentz control.
- **Checked** (`r99_tt_selfenergy.out`). α is computed directly by exact grid shifts plus Richardson, independently of the identity. α + β agrees with the formula to 1e-10 – 1e-9 at N = 128 (G, NN), and to 2e-7 – 1e-5 for L, whose u″ is a finite-difference surrogate. The box part of the integrand (|k_z| ≤ B) is ≤ 1e-14 (G) and 4e-11 (L).

**Numbers** (Ξ per scalar species, lattice units, N = 128):

| profile, m | M, T_2g | M, E_g | U, T_2g | U, E_g |
|---|---|---|---|---|
| G, 1.0 | −9.602e-4 | −5.292e-4 | −4.840e-4 | −2.521e-4 |
| G, 0.3 | −1.112e-3 | −6.279e-4 | −5.723e-4 | −3.042e-4 |
| L, 1.0 | +2.409e-3 | +2.319e-3 | +2.688e-2 | +9.055e-2 |
| L, 0.3 | +5.276e-3 | +5.519e-3 | +6.070e-2 | +2.477e-1 |
| NN control, 1.0 | −1.903e-3 | −8.302e-4 | −2.289e-4 | −6.883e-5 |

- **Edge-carried (proved for box bands).** A_zz = u″(k_z)/2 − 1 = 0 for |k_z| < B, so only k_z beyond the box face contributes. The pair's transverse momenta may lie in the box.
- **Birefringent.** T_2g ≠ E_g in every row.

**Sign-definiteness.**
- **Proved for G-type edges.** If A_zz ≤ 0 on the whole zone, then Ξ < 0 for every nonzero vertex in 𝒱. On each k_⊥ line ∫A_zz dk_z = −2π, so A_zz < 0 on a set of positive measure.
- **G satisfies the hypothesis (proved).** On [B, π], u″ = ρ′(2k − C sin k) + 2ρ + (1 − ρ)C cos k ≤ 2, because ρ′ ≤ 0, 2k − C sin k ≥ 0 there, and cos k < 0. Checked: max A_zz = 0.000.
- **NN satisfies it too:** A_zz = cos k_z − 1.
- **L (checked, not proved).** A_zz ranges over [−33.0, +19.8]. Yet I(B) = ∫A_zz(B + u)^{−5/2}dk_z > 0 for every B in [m², m² + 2 max u]. So Ξ > 0 for every vertex in 𝒱 (`r99_tt_selfenergy.out`, last block).
- **Lemma N (proved, sketch).** No band in this class has Ξ = 0 for all vertices in 𝒱.
  - That would need I(B) = 0 on an interval of B, hence for all B > −min u by analyticity.
  - Writing (B + u)^{−5/2} as a Laplace integral, the pushforward of A_zz dk_z to u-space would have to vanish.
  - But its total mass is −2π.

**One edge knob cannot remove speed (both polarizations) and mass together** (`r99_edge_family.out`). Along R9-2's family u_t = (1 − t)u_L + t u_G (box fixed):

| m | speed zero, M T_2g | speed zero, M E_g | U T_2g / U E_g | mass zero (R9-2 flow seagull) | metric-seagull mass split |
|---|---|---|---|---|---|
| 1.0 | t* = 0.23014 | 0.26251 | 0.22080 / 0.25054 | 0.287922 | no zero in [0, 1] (+2.3e-2 … +4.9e-2) |
| 0.3 | 0.25547 | 0.29011 | 0.24596 / 0.27537 | 0.297708 | no zero (+2.6e-2 … +5.3e-2) |

**TT mass, second prescription (checked).**
- **Setting.** The minimal metric coupling's seagull, (h²/2)·½[π² + (∇_xφ)² + (∇_yφ)² − (∇_zφ)² − m²φ²], is the same in both channels. So the CC-independent split is Δμ = μ_E − μ_T2 = −(1/8)⟨(u_x² + u_y² − 6u_xu_y)/ε³⟩. Its continuum angular average is zero.
- **Values:** G: +4.874e-2 (m = 1), +5.335e-2 (m = 0.3). L: +2.311e-2, +2.559e-2. NN: +5.248e-2.
- **Not edge-confined.** The region with all |k_i| ≤ B contributes +6.3e-3 to +7.7e-3 of it (N = 128), i.e. 13–30%: the box is a cube, and this seagull is not R9-2's flow.
- **Reading.** "The shear mass reappears through the edge" is prescription-dependent. With R9-2's flow seagull it is purely edge-carried. With the minimal metric seagull, the box's cubic shape adds to it. In both prescriptions it is nonzero untuned.
- **Lower bound (proved, elementary).** One polarization has |m_T²| ≥ |Δμ|/M² whatever CC counterterm is chosen.

### 3.5 INV control: invariant-mass TT pair vertices. Checked; partly proved (`r99_inv.out`)

- **The construction.** Multiply the TT pair vertex by a compact C^∞ plateau f(s), s = E² − q², with support chosen so both legs stay inside the box (max |k_i| on support 1.73).
- **Proved (Källén–Lehmann).** On that support the continuum ε, the z-boost-invariant |V|² and f(s) make Π_para(ω, q) = −∫ds ρ̃(s)/(s + q² − ω²). Hence Ξ_para = 0 exactly.
- **Checked:** α + β = 1.8e-12 (T_2g) and −3.8e-11 (E_g) at N = 160 (G, m = 1), against α = 7.1e-5. Control: the same f on the NN band gives −5.2e-5, so the box is what does it.
- **But** Π_para(0, 0) = −6.8201e-4 (m = 1), equal in E_g and T_2g. The TT mass vanishes only if the seagull equals +6.82e-4 in both channels.
  - The INV pair vertex keeps W1 (f is a scalar multiplying every pair component; pair and scattering parts are separately conserved for free fields).
  - Whether the O(hξ) Ward identity plus cubic symmetry fixes the TT seagull to this value, after tadpole (CC) cancellation, is not settled. No seagull for the INV vertex was built.
- **Further risks (comparator/suggested).**
  - R8-4's refereed two-loop non-closure of invariant-mass plateaus (toy N; `TESTS.md:3815-3821`).
  - R7-5's "imposed functional custodial condition" (`TESTS.md:3504`).
  - The gravitational pair vertex becomes non-universal outside the window (reading).

### 3.6 Physical sizes (reading; `r99_numbers.out`)

- **Formulas.** c_T² − 1 = 2κ_lat Ξ, with κ_lat = 8π(ℓ_P/a)², per scalar species.
- **At a = ℓ_P:**
  - G (M, T_2g, m = 1): δc_T = −2.4e-2, 8.0e12 times the band;
  - L: +6.1e-2 (M) and +2.3 (U, E_g);
  - NN: −4.8e-2.
- **Scaling.** The shift scales as (ℓ_P/a)². One species needs a ≳ 2–9 × 10⁶ ℓ_P (about 5e-29 – 1.5e-28 m) to sit inside −3e-15 ≤ Δc ≤ 7e-16.
- **TT mass split (metric seagull).** |Δm_T²|^{1/2} = 1.9e28 eV at a = ℓ_P, and 5e-4 eV at a = 1e-19 m. That is about 4e19 times a 1.27e-23 eV graviton-mass bound (LVK GWTC-3, RECALLED, not verified). A tuning-free pass would need a ≳ 6e-10 m, far outside matter-locality bounds (reading).

---

## 4. Against the FIXED readings (`TESTS.md:3874-3876`)

**Worker reading: FAIL (bounded)**, for pair-creating free scalar box matter in class 𝒱 with ultralocal seagulls. Referee required. The FAIL clause reads "a computed nonzero one-loop TT mass or speed split that no choice in a stated class removes". It is met as follows:
- **Mass.**
  - Δμ = μ_E − μ_T2 ≠ 0 for the minimal metric coupling at every t in the edge family and both masses: CC-independent, computed.
  - μ_E ≠ 0 with R9-2's flow seagull except at its tuned t*.
- **Speed.**
  - Ξ < 0 for every vertex in 𝒱 on every A_zz ≤ 0 band, the gapped edge included (proved).
  - Ξ > 0 for every vertex in 𝒱 on the literal edge (checked).
  - No t in the edge family zeros both polarizations, or speed and mass together; each zero moves with m.
- **Caveat that must travel with the FAIL.** The speed split *relative to matter* also needs matter's own one-loop shift from graviton loops, which is the same order in κ_lat and is not computed. A cancellation would need two independent integrals to agree (suggested: no mechanism). The mass leg of the FAIL does not depend on this.

**PASS is met only on the letter, in R8-2's own empty-vacuum class (F).** The TT mass is 0 and c_T = c_m exactly, but only because there are no matter loops (§3.3). If the referee accepts (F) as the registered "free, number-conserving" case, the item splits: (F) PASS WITH SCOPE (vacuous) and (Z) FAIL (bounded). The strongest physical reading is FAIL (bounded).

**INV variant: INCONCLUSIVE.** The speed is exact at one loop. The mass reduces to one unbuilt seagull value. Two loops are unexamined.

## 5. Prices (named, not adopted)

- **Box graviton:**
  - non-compact h, E per face or site (N0914's escape from its compact-character bound);
  - a non-analytic symbol with super-polynomial tails;
  - c_g = c_m set by the law (T1).

  No axiom text changes: dynamics, stress and gravity bridges are downstream (`AX:114-130,173-190`). The infinite-dimensional link variables sit against Qubit's finite site domain (`AX:43-53`) in the same way as R8-5's non-compact photon.
- **To keep the TT massless and on the matter cone with pair-creating box matter**, one of:
  - a TT mass counterterm per polarization (P0; refereed residual 5.7e-99 of natural size, `PRICE_NOTE.md:356-358`) plus a TT speed counterterm (a non-ultralocal seagull), or edge-shape tunings per species and mass (§3.4 table);
  - an INV pair vertex plus a seagull fixed to −Π_para(0,0) (not built; two-loop risk);
  - a lattice spacing a ≳ 1e7 ℓ_P for the speed only. That does nothing for the mass.

## 6. Scope and strong-word check

- **"Exact"** is used for:
  - the tree-level graviton identities and ω = |q| on the graviton box;
  - the W1 identity with D = d e^{iq/2};
  - Π ≡ 0 in (F);
  - Theorem T as an identity of one-loop integrals;
  - Ξ_para = 0 for INV on its support.
- **"Proved"** is used for:
  - §3.1's algebra; §3.2's phase transfer; §3.3;
  - Theorem T; sign-definiteness for A_zz ≤ 0, and A_zz ≤ 0 for G; Lemma N (sketch);
  - the INV Källén–Lehmann step; the CC-independent lower bound.
- **Checked:** every number in the tables, at N = 64/96/128/160 with convergence shown in the `.out` files, plus the exact-diagonalization normalization check.
- **Normalization.** The static paramagnetic normalization (pair counting ½, |V_s|) is checked against exact diagonalization to 2e-7 (`r99_exact_norm.out`). The ω-coefficient uses the same matrix elements, and the link to M² is the stated GR convention. A convention error there would rescale the physical sizes only, not any sign, zero or edge statement.
- **Not claimed:**
  - fermion matter;
  - non-axis q;
  - matter-side speed shifts;
  - two loops;
  - a no-go for k_z- or q-dependent TT vertices beyond the INV control;
  - any statement about non-ultralocal seagulls other than that they are speed counterterms.
  - an explicit W1-exact stress with pair parts for the scalar field (only its TT components at q ∥ axis are used).
- **Unrefereed inputs.** R9-2 numbers are cited as unrefereed scratch results. The graviton-mass bound is RECALLED.

## 7. For the referee

1. Theorem T: the α derivative (g′ = −3/(4ε⁴), g″ = 7/(4ε⁵) at ε′ = ε), the integration by parts, and the total derivative ∂_z(∂_zε/ε⁴).
2. Whether class 𝒱 (TT vertex independent of k_z and q for q ∥ axis) plus ultralocal seagulls is a fair "stated class", and whether the mass leg alone carries the FAIL without the matter-side speed shift.
3. The sign proof for G (u″ ≤ 2 on [B, π]) and Lemma N's Laplace step.
4. The midpoint-phase transfer of Construction A (§3.2) and the gauge-variation bookkeeping with δh = i(D*ξ + ξD*).
5. The INV statement: Ξ_para = 0 holds; the mass is reduced to a seagull value. Is any lattice-consistent seagull forced to it?
6. Normalization of Π relative to (M²/2)(ω² − q²).

## 8. Files

All in `S/scripts/`: `r99_profiles.py`; `r99_graviton.py`/`.out`; `r99_exact_norm.py`/`.out`; `r99_tt_selfenergy.py`/`.out`; `r99_edge_family.py`/`.out`; `r99_inv.py`/`.out`; `r99_numbers.py`/`.out`.
