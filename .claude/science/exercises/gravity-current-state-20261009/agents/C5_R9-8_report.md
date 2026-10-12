# C5 R9-8 report: non-minimal gauge-invariant couplings in box QED (the escape left by R8-5)

**Author.** Claude Opus 5.5 probe. Same family as the supervisor and every C5 worker. Unrefereed. 2026-10-12, 17:07Z to about 18:15Z. No repository file edited.

**Scratch.** `S/` = `.../scratchpad/C5/R9-8/`. Scripts and outputs in `S/scripts/`; `r98_run_all.sh` regenerates them (each python step under 1.5 min, `r98_straight.sh` about 8 min, `OMP_NUM_THREADS=2`).
- `r85_box_qed.py`: an unchanged copy of the refereed R8-5 runner (packet `scripts/C5/R8-5/r85_box_qed.py`), imported for the law's 1D functions.
- `r98_frame_qed.py`: the new law BQ-W (frame-rotated charge, staircase Wilson lines); photon and electron one-loop speeds.
- `r98_checks.{py,out}`: Ward identity, spectrum, limits, and the forward-vertex ratios of §4.3.
- `r98_validate.out`: BQ-W with no rotation reproduces R8-5's BQ to every printed digit.
- `r98_scan_S3.out`, `r98_scan2.out`: profile scans (shapes S3, S1; m = 0.2 and 0.1).
- `r98_paths.{py,out}`, `r98_paths_S3.out`, `r98_paths2.out`: photon speed with staircase versus straight-line Wilson lines.
- `r98_straight_e.py`, `r98_straight.{sh,out}`, `r98_straight_quadcheck.out`: electron speed with straight-line Wilson lines (sharp interpolation; §4.6).

**Read.**
- `docs/MINIMAL_AXIOMS_2026-06-29.md`, in full.
- `TESTS.md:2302-2420` (C5 method), `:3370-3620` (R7-5, R8-4, R8-5 items, round 9), `:3800-3862` (R8-4/R8-5 referee results, R9-7, R9-8 at `:3851-3860` as read at 17:45Z; the file was being edited concurrently and line numbers moved by 4).
- `agents/C5_R8-5_report.md` (all), `C5_R8-5_referee_verdict.md` and the detailed referee file `scratchpad/C5/ref_R8-5/R8-5_referee_verdict.md` (all).
- `agents/C5_R7-5_report.md:60-80,168-200,266-276`, `C5_R7-5_referee_verdict.md` (all).
- `agents/C5_R8-4_report.md:1-80`.
- Packet `scripts/C5/R8-5/` (`r85_box_qed.py`, `r85_gauge_check.py`, `r85_shapes.out`, `r85_run_all.sh`).

**Labels.** proved / checked (numerics here) / suggested / reading / comparator (V = verified on the web this session, abstract or search summary only; R = recalled).

---

## 0. In plain words

1. **What the Ward identity really pins.** In any quasi-local (ℓ¹) Hamiltonian lattice U(1) theory, adding gauge-invariant extras (Pauli-type couplings to E and B, any choice of Wilson-line path, any Lemma-C-allowed rotation of the charge) never changes the vertex at zero photon momentum. That zero-momentum vertex is fixed over the whole Brillouin zone, zone edges included: the charge (Lemma C) and the full velocity operator of the matter Hamiltonian in the chosen frame. (proved)
2. **The purely longitudinal part alone does nothing.** The component of the vertex along the photon's 4-momentum, the part the Ward identity literally fixes, drops out of both one-loop poles: the photon's through its physical polarizations, the electron's through gauge-parameter independence (Landau gauge). (proved)
3. **But a Hamiltonian vertex is never purely longitudinal.** The Ward-forced pieces a Hamiltonian law must carry (the frequency-independent charge vertex and the longitudinal 3-current) always leave a nonzero 4-transverse remainder, so they do feed the poles. (proved, elementary)
4. **"Invariant mass" cannot be imposed on the pinned vertex.** The only freedom Lemma C leaves for the pinned vertex is a one-body frame rotation W(k). I built the natural family: rotate toward the band frame outside an energy plateau, so that soft pair creation happens only inside the box with full QED strength. Requiring the forward pair vertex to be F(M²) × QED forces F' = 0: only F ≡ 1 (plain BQ) or F ≡ 0 (no pair creation at all) work. In the transition shell the radial pair current comes out 15–36 times QED's, not F times. (proved for this family; checked)
5. **The cheapest construction, computed.** BQ-W is that frame family with exact gauge invariance (staircase Wilson lines, exact telescoping Ward identity, checked to 9e-16). Every one of 12 rotated laws has a larger split than plain BQ: Δ from −33.6 to −635 (BQ: −20.3) in units of e²/16π², converged in N, similar at m = 0.1 and for a second box shape. (checked)
6. **New: the Wilson-line path is itself a large, frame-fixed magnetic coupling.** Once the charge is rotated, matter hops off-axis, and gauging needs a path. Straight-line (Terning/Mandelstam) paths instead of lattice staircases change the photon speed by −5.5 to −69 units: δc_γ·16π² falls from +6.8…+73.6 to +1.1…+4.4. It does not reach zero. (checked, photon side)
7. **The electron does not follow.** With straight paths the electron's shift stays −18 to −26 units. Its diamagnetic tadpole from the rotated edge modes dominates. The full split is Δ = −27.1 and −21.6 for two profiles, against −19.9 for BQ at the same grid. (checked; N = 48; power-law interpolation)
8. **Against the FIXED readings: INCONCLUSIVE, leaning FAIL (worker reading).**
   - PASS is not met: no law found whose cones agree. Every one of 17 computed laws (12 rotated staircase, 2 rotated straight, 3 BQ controls) has |Δ| ≥ 12.9·e²/16π², i.e. |c_e − c_γ| ≳ 7e-3.
   - The FAIL clause-2 computation is met for the cheapest exactly gauge-invariant, ℓ¹ construction (staircase BQ-W): an unsuppressed split in every law scanned.
   - But the stated-class argument does not close. INV-structured additions are Lorentz-neutral only if their own Wilson-line gauging is path-neutral, and item 6 shows path choice is an O(1–70) effect. A tuned zero also always exists (one gauge-invariant counterterm, R8-5 §7), so a class-wide "every vertex carries a split" proof is false for any class that keeps a free gauge-invariant coefficient.

---

## 1. Hypotheses and classes (stated before any title)

**H-lat.** As R8-5 (`C5_R8-5_report.md:116-138`): Z³ × ℝ, continuous time, one 4-component Dirac field per site, R8-5's BQ symbol h(k) = Σ_j S(k_j)α_j + M(k)β, M = m + Σ_j W(k_j), and R8-5's non-compact G-normalized photon with exact ω = |q| on its plateau. Euclidean Feynman gauge with photon mass λ = m, one loop, one species, Δ = (δc_e − δc_γ)·16π².

**Class 𝒢⁺ (for §§4.1–4.2).** R8-5's class 𝒢 (`C5_R8-5_report.md:69-77`: bilinear, translation-covariant, ℓ¹ charge densities ρ̂(q) with continuous kernel μ(k',k)), plus any gauge-invariant ℓ¹ couplings built from:
- Wilson-line-dressed bilinears ψ†(x)U_γ(x,y)K(x−y)ψ(y), along any lattice or interpolated paths γ;
- polarization and magnetization couplings P·E and M·B, with P and M neutral ℓ¹ bilinears;
- Hamiltonian, time-local.

**Class BQ-W (the construction, §3).** Charge on-site in a rotated frame ψ = W(k)ψ', with W in the Foldy–Wouthuysen (FW) family below; minimal coupling of ψ' through symmetrized axis-staircase Wilson lines (or straight lines, §4.5–4.6).

**Excluded outside realizations, named before any title:**
- Coulomb-kernel (power-law) couplings to the gauge-invariant transverse field A_T, i.e. Dirac-dressed matter (outside ℓ¹; §5);
- time-non-local covariant F(□) Lagrangians (not Hamiltonian; §5);
- non-bilinear charge generators;
- frames W outside the FW family;
- compact U(1) and link truncations;
- Z⁴; two loops; gravity; chiral matter.

## 2. Prior art (each counted once)

- **R8-5 (refereed, FAIL bounded).** Lemma C, Theorem B, the BQ law and its split Δ(S3) = −21.8 ± 0.15 (m → 0), −20.28 at m = 0.2 (`C5_R8-5_report.md:153-174,212-238`; verdict `:5-7`). Open items: frame-rotated densities plus INV transverse vertices (§4.2(b)–(c), `:183-193`). That is this item's starting point.
- **R7-5 (INV conditional lemma, refereed).** INV-s and INV-f: invariant-mass vertex functions with both orderings give Lorentz-invariant one-loop two-point functions inside a budget (`C5_R7-5_report.md:170-193`; verdict `:15-17`). Class FF (frame-fixed one-body windows) gives XI_FF ≈ 11 (verdict `:9`). Invariant-mass structure is an "imposed functional custodial condition" (verdict `:34`).
- **R8-4.** Fermion external lines need the frame-dependent factor h = (3W − E)/(W + E) (`C5_R8-4_report.md:34`).
- **Literature.**
  - **Terning, PRD 44 (1991) 887** (V, abstract via the UC Davis archive and INSPIRE): a method for introducing gauge fields into non-local Lagrangians with path-ordered exponentials, and deriving Feynman rules.
  - **Licht, arXiv:0802.4310, "The Mandelstam–Terning line integral in unparticle physics"** (V, search summary only): Terning's path is unspecified; straight-line paths give vertices considerably more complicated than Terning's. This is the path ambiguity quantified in §4.5.
  - **Mandelstam, Ann. Phys. 19 (1962) 1**, path-dependent formalism (R).
  - **Ball–Chiu, PRD 22 (1980) 2542** (V, abstract and secondary): the vertex splits into a longitudinal part fixed by the Ward–Takahashi identity from the propagator, and an undetermined transverse part free of kinematic singularities that vanishes at zero photon momentum. §4.1–4.2 is the lattice-Hamiltonian version of that split.

## 3. The construction BQ-W (proved properties; checked)

**Frame.** W(k) = exp(β α·Ŝ φ(k)/2) with φ = (1 − F(E))θ, tan θ = |S|/M, and E(k) = |h(k)|.
- This gives h_W = W†hW = E[β cos(Fθ) + α·Ŝ sin(Fθ)], still in span{α_x, α_y, α_z, β}, with the same spectrum ±E (checked to 4e-16, `r98_checks.out:2`).
- F is a C^∞ plateau in E: F = 1 for E ≤ E₁ and F = 0 for E ≥ E₂.
- At zero photon momentum the created pair (k, −k) has invariant mass 2E(k). So F is the invariant-mass form factor of the forward pairs, as far as a one-body frame can carry one.
- F ≡ 1 is BQ exactly (checked through the rotation code, 9e-16, `:3`). F = 0 is the full band (FW) frame, h_W = Eβ (checked, `:4`).
- With E₂ ≤ 1.9 < b₁ = 2 (shape S3), every forward pair-creating mode lies inside the fermion box.

**Charge.** On-site for ψ'. In the ψ frame μ(k',k) = W(k')W(k)†, a Lemma-C-allowed density: charge 1 at every k.

**Coupling.** Each ψ' hop carries the Wilson line along an axis staircase, averaged over the 6 axis orders (cubic symmetric, exactly gauge invariant for R8-5's forward-difference photon).
- The vertex is V_j = δ̄_j/D̂_j with δ̄_j = [2(h{j} − h{}) + (h{a,j} − h{a}) + (h{b,j} − h{b}) + 2(h{a,b,j} − h{a,b})]/6. Here h{B} is h_W at the momentum whose components in B come from the outgoing momentum and the rest from the incoming one.
- Σ_j D̂_jV_j = h_W(p) − h_W(k) exactly (telescoping; checked to 8.9e-16 on 2e4 random points, `r98_checks.out:1`).
- The same-axis seagull for (q, −q) is [h(p + q_jê_j) + h(p − q_jê_j) − 2h(p)]/d(q_j)² for every order.
- For separable h every rule reduces to R8-5's.

**Validation (checked).** With F ≡ 1, `r98_frame_qed.py` reproduces `r85_box_qed.py` digit for digit: P_E, P_M, A, B, tadpole, Δ = −20.4413 at N = 64 (`r98_validate.out`). Charge–current consistency (Ward): P_E from the charge response equals P_E from the forward current to ≤ 1.1e-5 (per e², every run; e.g. `r98_scan_S3.out`).

## 4. Results

### 4.1 Forward pinning in 𝒢⁺ (proved)

**Claim.** In 𝒢⁺, the full zero-momentum vertex is Γ⁰(k,k) = q(k), Lemma C's rigid charge. In the frame where the charge is on-site, it is Γ^j(k,k) = ∂_jh_W(k) for every k ∈ T³, whatever P, M and paths are chosen.

**Proof.**
1. A constant spatial A, and a constant A₀, are pure gauge on the infinite lattice: λ = A·x, generated by the charge.
2. So H(A = const) is unitarily h_W(k − eA) in the on-site frame. Its A-derivative at A = 0 is −e∂h_W.
3. A P·E coupling contributes ∝ q₀ (E = −Ȧ − ∇A₀) and an M·B coupling ∝ q. Two Wilson-line paths between the same endpoints differ by the flux through the loop they enclose, which is O(q) for smooth A.
4. ℓ¹ kernels make all vertices continuous in (q₀, q), so these terms vanish at zero photon momentum. ∎

**Meaning.** The pinned forward vertex lives on the whole Brillouin zone. The non-minimal freedom starts at O(q₀, q).

### 4.2 The longitudinal part: what drops out and what cannot (proved)

**(a) The strictly 4-longitudinal component drops out of both poles.** Write Γ = Γ_L + Γ_T with Γ_L ∥ (q₀, D̂(q)).
- **Photon.** The pole involves ε_μΠ^{μν}ε_ν with ε·q = 0. Each vertex enters as ε·Γ = ε·Γ_T, and likewise for the seagull's doubly contracted part.
- **Electron.** The one-loop pole is ξ-independent whenever the one- and two-photon Ward identities hold: the ξ-term factorizes as −(1−ξ)e²[aI₂ − aXa], a = S⁻¹(p). This is R8-5's derivation (`C5_R8-5_report.md:250-251`), which uses only the two identities, and both follow from exact gauge invariance of the action. In Landau gauge the propagator P_T/q² removes Γ_L and the longitudinal seagull. ∎
- **So the part the Ward identity literally fixes, q·Γ, cannot by itself regenerate any split.**

**(b) No Hamiltonian vertex is 4-longitudinal.**
- In a time-local Hamiltonian law, Γ⁰ (charge) and the 3-current are frequency independent. P·E terms add only matched pieces: Γ⁰ ∋ D̂·P with Γ ∋ −q₀P, which cancel in q·Γ.
- If Γ = (q₀, D̂)X, then X = Γ⁰/q₀ must be frequency independent times 1/q₀. That forces Γ⁰ = 0 and then Γ = 0.
- But the Ward identity requires D̂·Γ = h_W(p) − h_W(k) ≠ 0 at generic momenta. Contradiction. ∎
- The 4-transverse remainder of the Ward-forced Hamiltonian pieces is nonzero wherever h_W(p) ≠ h_W(k). It is the instantaneous (Coulomb-gauge) structure. So the Ward-forced Hamiltonian pieces do feed both poles, through the whole Brillouin zone (§4.1).

### 4.3 An invariant-mass forward vertex is impossible in the FW family (proved; checked)

**Claim.** In the FW family, the forward interband (pair-creation) current of the ψ-frame vertex equals F(4E²) × (BQ's) for every k and both directions (radial and tangential to S) only if F' ≡ 0, i.e. F ≡ 1 or F ≡ 0.

**Proof.**
1. With Θ = Fθ, h_W = E[β cos Θ + α·Ŝ sin Θ].
2. The radial pair current is ∝ E∂_rΘ = E(F∂_rθ + θF'(E)∂_rE). BQ's is E∂_rθ.
3. The ratio equals F only if θF'∂_rE = 0. Since θ > 0 and ∂_rE > 0 for S ≠ 0, F' = 0 for every E above m.
4. (The tangential ratio sin(Fθ)/sin θ also differs from F for 0 < F < 1.) ∎

**Checked** (`r98_checks.out:6-18`, profile E = (1.0, 1.8)): along the x axis the radial and tangential ratios are 1 on the plateau and 0 outside. In the shell they are 15.3 / 0.97, 31.9 / 0.75, 36.2 / 0.32 and 8.65 / 0.015, against F = 0.91, 0.59, 0.23, 0.01.

**Suggested (general W).** For a general frame the INV condition fixes the off-diagonal block of the flat connection dW W† (24 real functions). The Maurer–Cartan equations (48 real) leave only the 24 diagonal-block functions free, so the system is overdetermined. An abelian shift of the diagonal blocks cannot supply the needed real term −d ln(1 − F) ∧ A. Not proved for every W.

**Reading.** Lemma C allows only one-body (frame) data on the pinned vertex. An invariant-mass function of the pair is a two-body object, and a one-body frame window is R7-5's class FF moved into energy.

### 4.4 One-loop cones of BQ-W, staircase gauging (checked)

Shape S3 (b = (2, 3), r = 1, photon box (2, 3)), m = λ = 0.2. N = 128 rows; the N = 96 rows agree to ≤ 0.02, except the two steepest profiles (0.08 and 0.17). From `r98_scan_S3.out`; units e²/16π².

| frame profile (E₁, E₂) | P_E | P_M | δc_γ | δc_e | Δ |
|---|---|---|---|---|---|
| none (BQ, F ≡ 1) | 20.58 | 48.19 | +13.81 | −6.48 | **−20.28** |
| (1.0, 1.8) | 12.04 | 137.53 | +62.75 | −17.86 | −80.60 |
| (1.2, 1.9) | 14.60 | 262.63 | +124.02 | −15.18 | −139.19 |
| (0.6, 1.4) | 8.27 | 54.09 | +22.91 | −30.39 | −53.30 |
| (0.5, 1.9) | 7.47 | 28.79 | +10.66 | −22.93 | −33.59 |
| (0.3, 1.9) | 6.36 | 19.88 | +6.76 | −26.81 | −33.57 |
| (1.5, 1.95) | 22.49 | 1267.7 | +622.60 | −12.82 | −635.41 |
| (0.25, 0.5) | 2.75 | 24.06 | +10.66 | −141.35 | −152.01 |

- **Second shape S1** (b = (1, 2), photon box (1, 2), N = 128, `r98_scan2.out`): BQ −12.90; (0.5, 0.9) −100.41; (0.3, 0.9) −83.55; (0.6, 1.4) −57.83.
- **Lower mass m = λ = 0.1, S3** (N = 128 / 160 agree to 4e-3): BQ −21.08; (1.0, 1.8) −91.19; (0.5, 1.9) −34.78.

**What the numbers show.**
- The rotation does what it was built for on the electric side: removing forward pair creation outside the plateau lowers P_E from 20.6 to 2.8–14.6.
- But the shell's large radial pair current (§4.3) raises the orbital response P_M, and the electron's tadpole grows: the off-axis hops of h_W carry seagulls through the whole zone.
- In all 12 rotated laws |Δ| > |Δ_BQ|. **No zero was found. Sign-definiteness is not claimed.**

### 4.5 The Wilson-line path is a large magnetic coupling (checked, photon side)

Rotated hops are off-axis, so gauging them needs a path. Two exactly gauge-invariant choices:
- the lattice staircase (§3);
- the straight line, with A interpolated band-limited. This is valid as written for photon momenta in the photon box, which is all that P_E and P_M use.

For the straight line, V_y(k + q x̂, k) = ∫₀¹ ds ∂_yh_W(k + s q x̂), and the seagull is ∫∫ ds dt ∂²_yh_W(k + (s − t)q x̂), now q-dependent. P_M is then [seagull(q) − χ_yy(q)]/d², using the exact f-sum seagull(0) = χ_yy(0).

The table gives δc_γ·16π² for staircase / straight paths, from `r98_paths_S3.out` and `r98_paths2.out` (N = 128; the N = 96 and N = 160 rows agree to ≤ 1e-3).

| profile | m | staircase | straight | path shift |
|---|---|---|---|---|
| BQ | 0.2 | +13.806 | +13.806 | 0 (separable: paths coincide) |
| (1.0, 1.8) | 0.2 | +62.75 | +3.63 | −59.12 |
| (0.6, 1.4) | 0.2 | +22.91 | +2.21 | −20.69 |
| (0.5, 1.9) | 0.2 | +10.66 | +1.69 | −8.97 |
| (0.3, 1.9) | 0.2 | +6.76 | +1.27 | −5.49 |
| (0.3, 1.9) | 0.1 | +8.12 | +1.72 | −6.40 |
| (1.0, 1.8) | 0.1 | +73.64 | +4.35 | −69.29 |

- **Reading.** The path shift is a gauge-invariant magnetic (flux) coupling. Two Wilson lines differ by the flux through the area between them (§4.1, step 3).
- On Z³ every path family is a lattice-fixed choice, so the shift is a frame-fixed dimension-4 term of size O(5–70)·e²/16π².
- This is the lattice form of the Mandelstam/Terning path ambiguity that Licht flags (comparator V, search summary).
- The straight (rotation-covariant) path brings the photon within +1.3 to +4.4 units of zero, but not to zero. The remainder is the shell's one-body window (§4.3), suggested.

### 4.6 Electron speed with straight paths (checked, sharp interpolation; partial)

`r98_straight_e.py` uses straight lines with the photon momentum taken in the fundamental domain (sharp, alias-free interpolation of A).
- This is exactly gauge invariant: Σ_j δ_j = h_W(p) − h_W(k).
- But its matter–photon coupling has power-law tails (outside ℓ¹). The smooth-alias ℓ¹ version (a partition of unity in Q; §5) was not run.
- Path integrals use Gauss–Legendre quadrature. On BQ (where straight = staircase), at N = 32 the tadpole is −5.59 / −5.83 at 24 / 48 nodes, against the exact −5.97 (`r98_straight_quadcheck.out`). At 96 nodes and N = 48 the BQ control gives Δ = −19.944, against the exact −19.920 (`r98_straight.out:1-2`): a quadrature error of 0.024.

Shape S3, m = λ = 0.2, N = 48, 96 nodes (`r98_straight.out`); units e²/16π².

| profile | δc_γ (straight) | δc_e (straight) [tadpole] | Δ straight | Δ staircase (N = 128) |
|---|---|---|---|---|
| BQ | +13.43 | −6.51 [−6.04] | −19.94 | −20.28 |
| (0.3, 1.9) | +1.27 | −25.79 [−26.73] | **−27.06** | −33.57 |
| (1.0, 1.8) | +3.64 | −17.94 [−18.69] | **−21.58** | −80.60 |

- The straight path removes most of the photon's LV, but the electron's does not move much. Its tadpole (the diamagnetic seagull of the rotated, off-axis hops, sampled over the whole zone) stays −18 to −27.
- Outside the plateau the rotated symbol is Eβ: the edge modes couple like positive-energy "Salpeter" particles, whose seagull is ∂²E. Removing their pair creation (the purpose of the rotation) is paid for in the electron's diamagnetic term (reading).
- **Net: Δ ≈ −22 to −27, the same order as BQ.** No suppression from straight paths either.
- Scope: two profiles, one N, power-law interpolation. N-convergence of the rotated straight-path rows is not checked; the staircase electron converged to about 1e-2 between N = 48 and 128 for BQ.
- Photon side on S1 with straight paths (`r98_paths2.out`): (0.3, 0.9) +1.08, against staircase +9.50; (0.5, 0.9) +2.34, against +41.82.

## 5. Escapes outside the classes (named; not built)

- **Coulomb-kernel transverse couplings (power-law).** In Coulomb gauge, A_T is gauge invariant, so a coupling j'·A_T with any transverse current j' is gauge invariant. A literal "Ward-forced longitudinal part plus INV transverse part" vertex is of this type.
  - It is discontinuous at q = 0, so outside ℓ¹ (R8-5's open "power-law" route).
  - The instantaneous Coulomb term stays pinned to Lemma C's charge on all modes. With j' ≠ the Noether transverse current, Coulomb and transverse exchange no longer combine covariantly, so LV appears already in the continuum (suggested).
- **Time-non-local covariant F(□) (Terning/Efimov-type) actions.** These are not Hamiltonian laws on Z³ × ℝ.
  - Reading: for a multiplicative scalar form factor the fermion determinant factorizes as det(D̸ F(D²)) = det D̸ · det F(D²). The first factor is the unregulated lattice fermion loop, i.e. R8-5's BQ. This mirrors the known failure of higher-covariant-derivative regularization at one loop (comparator R: Slavnov).
- **Tuning.** One gauge-invariant κ_tr-type counterterm per species pair zeros Δ (R8-5 §7). Within BQ-W, the frame profile and the path family are continuous structural choices along which Δ varies by hundreds of units. A tuned zero may exist; none was found and none was sought.

## 6. Reading against the FIXED readings (`TESTS.md:3858-3860`)

**INCONCLUSIVE, leaning FAIL (worker reading, same family, unrefereed).**
- **PASS is not met.** No construction had cones agreeing within 1e-15 without tuning. The best photon-side value is +1.27·e²/16π², but the full split for that law is Δ = −27.1 (§4.6). Every one of 17 computed laws has |Δ| ≥ 12.9.
- **FAIL clause 1 is not met, and cannot be met as worded in any class that keeps a free gauge-invariant coefficient.** A tuned zero always exists (§5).
- **FAIL clause 2 is met only in part.**
  - The computation half holds: the cheapest exactly gauge-invariant ℓ¹ construction realizing as much invariant-mass structure as Lemma C allows (staircase BQ-W) has an unsuppressed split in every law scanned (12 rotated laws plus 3 BQ controls, 2 shapes, 2 masses; Δ from −33.6 to −635; with straight paths −21.6 and −27.1, §4.6).
  - The stated-class argument does not close. "INV-structured transverse additions contribute only Lorentz-invariant pieces, so Δ = Δ_minimal(W)" rests on R7-5's conditional INV lemma and R8-4's h factor. More importantly, those additions are themselves non-local, and their Wilson-line gauging carries the path ambiguity of §4.5, a non-INV effect of O(5–70). So the argument is SUGGESTED for a fixed path prescription, not proved.
- **Answer to the item's last question.**
  - The strictly 4-longitudinal part (q·Γ) alone cannot regenerate the split: it drops out of both poles (§4.2(a), proved).
  - The Ward-forced Hamiltonian pieces (the pinned forward vertex over the whole zone, the Lemma C charge, and the 3-longitudinal current: the Ball–Chiu-type minimal vertex of the chosen frame and path) do carry the whole computed split whenever the free transverse part is zero or INV-structured. Their size depends strongly on two non-INV choices, the frame (§4.4) and the Wilson-line path (§4.5).

**Scope that travels with any use of these numbers.**
- one loop; one Dirac species; non-compact U(1); continuous time; Feynman gauge;
- m = λ = 0.2 (spot checks at 0.1), not the m → 0 limit;
- the FW frame family and symmetrized staircase paths (§4.4). Straight paths at ℓ¹ only on the photon side (§4.5); the straight-path electron for two profiles at N = 48 with power-law (sharp) interpolation (§4.6);
- no ξ-scan for BQ-W. ξ-independence is argued from exact gauge invariance (§4.2(a)); R8-5 checked it numerically only for BQ.

## 7. Strong-word check

- **"Pinned"** (§4.1): exact, in 𝒢⁺, at zero photon momentum only. Non-minimal freedom starts at O(q₀, q).
- **"Drops out"** (§4.2(a)): the strictly 4-longitudinal component, at one loop, for the on-shell poles. It is not a statement about the Hamiltonian charge vertex or the longitudinal 3-current.
- **"Impossible"** (§4.3): only within the FW frame family, and only for exact F × QED on the forward pair current. The general-W statement is suggested.
- **"Unsuppressed"**: O(10–600)·e²/16π² in every BQ-W law scanned. Converged in N; not extrapolated to m → 0 (BQ's m-dependence from 0.2 to 0 is about 1.5 units, R8-5).
- **"Large path dependence"**: photon side only, at small q, ℓ¹-valid. Straight-path electron numbers use a power-law interpolation (§4.6).
- **"Exact gauge invariance / Ward identity"**: by construction (Wilson lines). The one-photon telescoping identity is checked to 9e-16; the charge-versus-current P_E agreement is checked to ≤ 1.1e-5 per e².
- **"No zero found"**: 14 rotated laws plus 3 controls, all Δ < 0. Not a sign theorem.

## 8. Price (named, not adopted)

"Within quasi-local gauge-invariant box QED on Z³ × ℝ, invariant-mass structure cannot be imposed on the vertex the Ward identity pins. That vertex is the full matter velocity at zero photon momentum over the whole Brillouin zone. The only Lemma-C freedom is a one-body frame, which cannot carry a pair invariant mass. Every non-local repair needs a Wilson-line path, and on Z³ the path is a lattice-fixed magnetic coupling worth O(5–70)·e²/16π² in the photon cone. Removing the e–γ split therefore needs a tuning, a time–space symmetry (Z⁴, F2), or a non-ℓ¹ (Coulomb-kernel) or time-non-local construction with its own Lorentz-invariance problems."

No axiom text changes: Admissibility does not choose dynamics (`MINIMAL_AXIOMS_2026-06-29.md:114-130`).

## 9. For the referee

1. **§4.1:** that a constant A is pure gauge for an arbitrary Lemma-C frame (the on-site frame of ψ'), and that P·E, M·B and path differences vanish at zero photon momentum under ℓ¹.
2. **§4.2(a):** that R8-5's ξ-factorization uses only WT₁ and WT₂, so it holds for BQ-W. **§4.2(b):** the elementary non-longitudinality argument.
3. **§4.3:** the radial-ratio identity ∂_rΘ/∂_rθ = F + θF'∂_rE/∂_rθ, and `r98_checks.out:6-18`.
4. **§3:** the symmetrized-staircase vertex, the same-axis seagull, and Hermiticity (δ̄(k,p) = −δ̄(p,k)). Also that R8-5's Clifford sunset and tadpole formulas apply unchanged to a general 4-component Clifford δ̄ (the F ≡ 1 reproduction to every digit tests the reduction, not the non-separable terms).
5. **§4.4:** independent recomputation of one rotated law, e.g. (0.5, 1.9) at N = 96: Δ = −33.586.
6. **§4.5:** the straight-path seagull's q-dependence, and the f-sum subtraction.
7. **Scope:** whether FAIL clause 2's "stated-class argument" can be met for a fixed path prescription, or whether INCONCLUSIVE is right.
