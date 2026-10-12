# Lane RK2, probe K2: discrete-time constraint algebra on Z⁴ (Euclidean, ξ = 1)

Worker: Claude Opus 5.5 (same family as the supervisor). Run 17:10Z–17:40Z, 2026-10-11. No repository files were edited.
Scratch folder: `.../scratchpad/C4/K2/` (six scripts, six `.out` files, this report). All "exact" checks use integer or dyadic data in float64 or sympy, so residuals of 0.0 are exact.

Read first, in full: `docs/MINIMAL_AXIOMS_2026-06-29.md`; TESTS.md "C4 third wave" and "Lane RK2"; SUMMARY.md §§5–6 and §§10–16; `agents/RC_C3_report.md` + `RC_C3_referee.md`; `agents/C4_I1_referee.md`; `agents/RN_L1_report.md`; the `kinetic_isotropy_primitive` entry in `PRIMITIVE_REGISTRY_CHECK.md`; and the K7a entry of `candidates/candidate-law-20261008/TEST_LOG.md`.

## Reading against the fixed line

**K2: INCONCLUSIVE.** The literal PASS object is mostly built, but the order that matters is a proved bounded no-go.

| Fixed-line clause | Status |
|---|---|
| Exact linearized (O(κ)) lattice diffeomorphism gauge symmetry for free matter plus graviton on Z⁴ | **Holds.** Scalar: CHECKED exactly, with an explicit symmetric stress. Naive or staggered fermion: PROVED through a lattice Calabi lemma plus exactly checked Killing symmetries; T is not written out |
| Positive transfer matrix at ξ = 1 | **Holds for the free sectors.** Scalar: CHECKED. Graviton after constraint reduction: CHECKED at the symbol level. Coupled O(κ) action: argued only in a fixed background; joint reflection positivity (RP) not shown |
| FAIL ("proved impossible in the stated class") | **Not met at O(κ).** It is met one order up |

**The key question, O(κ²).** The C3 obstruction does **not** go away on Z⁴. PROVED (same family, needs a referee): for strictly local free matter whose real Lorentzian mass shell is compact, the Killing-sector closure that O(κ²) gauge invariance needs is impossible. A finite-range Euclidean Z⁴ action has such a shell. The seagull cannot help, because its gauge variation vanishes on Killing fields.

The brief's premise is the error. The global algebra that matters is not the hypercubic group plus translations. It is the **continuous e(4)** of exact lattice Killing fields of the linearized gauge map, and that includes the three time–space rotations. Strict locality continues each of these analytically into a boost on the complex mass shell. There, compact band against non-compact boost is the obstruction: the Euclidean twin of C3 and of I1.

## 1. Free graviton: exact lattice linearized diffeomorphisms (CHECKED; reproduces K7a)

`k2_graviton_gauge_killing.py/.out`.

**Placement (K7a).**
- h_μν sits at x + (e_μ+e_ν)/2: diagonals on sites, off-diagonals on plaquette centres.
- ξ_μ sits at x + e_μ/2.
- ∇_μ is the difference between points one step apart in direction μ, so it is forward or backward depending on the object it acts on.
- Gauge map: δh_μν = ∇_μξ_ν + ∇_νξ_μ.

**Action.** The lattice Fierz–Pauli form:

S = ¼Σ(∇_ρh_μν)² − ½Σ(div_ν)² + ½Σ div_ν ∇_ν tr h − ¼Σ(∇_ρ tr h)².

**Checks.**
- S(h + δh) − S(h) = 0 and S(δh) = 0 exactly, on tori L = 3, 4, 5 with random integer h and ξ.
- Control: flipping the cross-term sign gives S(δh) ≈ −9.8e6.
- Symbolically, K(s)D(s) = 0 exactly (sympy), with s_μ = 2 sin(k_μ/2).
- Spectrum: s²·{−½, 0×4, ¼×5}, which is K7a's {−1, 0×4, ½×5} up to normalization.
- The −½ is the conformal mode.

**Placement note (SUGGESTED, from the symbol algebra).**
- With every h_μν on sites and forward differences only, the FP symbol picks up phases e^{ik_μ/2} that do not cancel.
- The staggered placement is the ultralocal way to remove them. This is consistent with Roček–Williams linearized Regge and with Bahr–Dittrich, where flat-background vertex translations are exact (COMPARATOR, from memory, not re-fetched).

**Killing fields of the lattice gauge map (CHECKED, exact rank).**
- On an open 4⁴ box, the kernel of ξ → ∇ξ + ∇ξ is exactly 10-dimensional: 768 unknowns, 1376 equations, singular-value gap 0 vs 0.76.
- It is spanned by the 4 translations and the 6 lattice rotations ξ_ν = ω_νμ x_μ, where x is the position of ξ_ν.
- The residual on the 10 explicit fields is 0.0.
- The reason: the differences commute and ∇_μ x_ν = δ_μν. So the Killing algebra of the background is the full continuous **e(4)**, including the (4, j) planes. The hypercubic group plays no role in this.
- On a finite torus the rotations are not periodic, but the gauge-invariance identity is local, so it must hold on the infinite lattice, where they are. The torus gives no escape.

## 2. Coupling free matter at O(κ): exact

### 2a. Scalar (CHECKED exactly; `k2_scalar_stress_exact.py/.out`)

**The construction.** Take S_m = ½Σ[Σ_μ(Δ_μφ)² + m²φ²] and E = δS_m/δφ. Define:
- **Matter transformation**, a lattice Lie derivative:
  L_ξφ(x) = ½Σ_ν[ξ_ν(x+e_ν/2)·Δ_νφ(x) + ξ_ν(x−e_ν/2)·Δ_νφ(x−e_ν)].
- **Stress, off-diagonal** (μ ≠ ν, on the face):
  T_μν = ¼(Δ_μφ(x) + Δ_μφ(x+e_ν))·(Δ_νφ(x) + Δ_νφ(x+e_μ)).
  This is symmetric: one object per face.
- **Stress, diagonal** (at site z):
  T_μμ = ½Δ_μφ(z)Δ_μφ(z−e_μ) − ¼Σ_{ρ≠μ}[(Δ_ρφ(z))² + (Δ_ρφ(z−e_ρ))²] − ½m²φ(z)².

This is RN L1's exact Hamiltonian stress with time made a grid direction. On Z⁴ the time direction is handled exactly like space.

**Off-shell identity.** For all φ and ξ:

Σ_x E·L_ξφ = ½Σ_{μν}(∇_μξ_ν + ∇_νξ_μ)T_μν.

The residual is exactly 0.0 for m² = 0, 0.75 and 3, and L = 3, 4, 6.

**Consequence (PROVED from the identity).** S = S_FP(h) + S_m − (κ/2)Σ h_μν T_μν is exactly gauge invariant at O(κ) under δh = ∇ξ + ∇ξ, δφ = κL_ξφ. The sign −½ matches L1.

**The Killing restriction is exact (CHECKED).**
- For ξ = c (constant), L_ξ is the pseudo-translation D_ν, the symmetric difference with symbol i sin k.
- For ξ = ωx, L_ξ = ω_νμ x_μ D_ν, which is an exact symmetry of S_m: δS_m = 0.0 on an open box with compact support, in the planes (0,1), (0,3) and (2,3).

**Lemma (lattice Calabi/Killing-cokernel; PROVED for degree 1, CHECKED by exact rank for degrees 2–6 in 3 and 4 variables, standard beyond; `k2_calabi_lemma.py/.out`).**
- A local vector R_ν is a divergence of a **symmetric local** T if and only if R is orthogonal to the 10 affine Killing fields. That means R(q=0) = 0 and ∂_[μR_ν](q=0) = 0.
- Localizing from polynomials in y = 1 − e^{−iq} to Laurent symbols keeps this, because the conditions are jets at q = 0, where 1 − y is a unit.
- **Corollary.** A symmetric conserved local stress, and hence exact O(κ) invariance, exists **if and only if** the matter's local gauge transformation restricts to exact symmetries on all 10 lattice Killing fields.

### 2b. Naive and staggered fermion (`k2_fermion.py/.out`)

**Exact pseudo-rotation (CHECKED exactly, real space, m = 0 and 0.5).** For the naive Dirac operator Σγ_μD_μ + m:

L_ω = Σ ω_ρσ x_ρ F_σ + ¼Σ_ab ω_ab γ_aγ_b S_aS_b

commutes with it exactly, in the planes (3,0), (0,1) and (2,3), with δψ = Lψ and δψ̄ = −ψ̄L. Here:
- F_σ is the **two-step** symmetric difference, with symbol (i/2) sin 2k_σ;
- S_a is the neighbour average, with symbol cos k_a.

The opposite spin sign gives a residual of 5.6.

**Staggered (CHECKED exactly).** Under spin diagonalization ψ = Γ(x)χ, every shift used by F and by the spin term (the diagonal shifts ±e_a ± e_b, and ±2e_σ) maps to a scalar phase. The deviation is 0.0 over all 16 parity classes. So the staggered fermion inherits both exact symmetries in a single component.

**Symmetric-stress criterion on shell (PROVED, Gordon identity; CHECKED to 4e-15).**
- On the complex shell, v γ_μ u = −i (sin k_μ / m)(v u).
- So the zero-momentum on-shell current of a translation with symbol f is proportional to (½ sin 2k_μ)·f_ν.
- This is symmetric exactly when f_ν ∝ sin 2k_ν: the staggered two-step pseudo-momentum, which is L1's measured spectrum ½ sin 2k_x.

**Corollary (PROVED via the lemma).** Let the local δ_ξ be the two-step local translation plus the spin term with ω → ∇_[aξ_b]. It restricts exactly to F and L_ω on Killing fields: ξ_ν = ω_νμ x_μ is constant along the ν-line, so the placement does not matter. Hence a symmetric local conserved T exists for naive and staggered fermions, and coupled O(κ) gauge invariance is exact. **T was not written out explicitly.**

## 3. Next order, O(κ²): the Killing sector, and why Z⁴ does not remove C3

### Bookkeeping (PROVED, same structure as C3's Lemma 1)

At O(κ²), order h¹·(matter)², take ξ to be a lattice Killing field. Then:
- δ⁰h = ∇ξ + ∇ξ = 0, so the variation of the seagull S₄(h, h, φ, φ) drops out (**Killing blindness**);
- so does any h-dependent completion.

What is left requires the matter Killing transformations (F_ν, L_ω) to form a representation of the Killing algebra modulo trivial symmetries N·E:
- the structure constants C(ξ, η) of Killing fields are themselves Killing fields;
- they are c-numbers at this order;
- the infrared fixes them to the e(4) bracket.

In particular:

[L_ω, F_ρ] = ω_ρσF_σ + (trivial).   (★)

### The explicit constructions fail (★) (CHECKED)

**Scalar.** [L_ω, D_ρ] = −ω_νρ S_ρD_ν exactly (real space, residual 0.0). This is a translation multiplied by cos k_ρ: the **Euclidean twin of C3's Q_ca = cos k_c sin k_a**.
- Since (A) is prime, membership in "translations + (A)" can be tested on the complex shell A = 0.
- The best constant-coefficient fit by translations over 400 shell points leaves a relative residual of 0.30–0.68, for m² = 0, 0.25, 1, in both a (4,1) plane and a spatial plane.

**Fermion.** [L_ω, F_ρ] = ω_ρσF_σ·cos 2k_ρ. The shell-fit residual is 0.40–0.98.

### General theorem: no local choice works (PROVED, same family, needs a referee)

**Hypotheses.** Let A be a real, strictly local (Laurent polynomial in e^{ik}), k₄-even kinetic symbol of finite-component matter on Z⁴. Let S_R = {k_j real, k₄ = iE, A = 0} be its real Lorentzian shell, and suppose the component containing the infrared is a compact smooth manifold. This holds for every nearest-neighbour Z⁴ action with a positive transfer matrix: S_R⁺ ≅ T³, with E ∈ [E_min, E_max]. Let F_ν (symbols i f_ν) and L_ω (V_ω·∂ + scalar) be any local translations and rotations obeying (★), with f ≈ k in the infrared.

**Proof.**
1. On S, (★) reads V_ω·∇f_ρ = ω_ρσf_σ.
2. For ω in a (4, j) plane on S_R, write f = (i g, f_j) with g and f_j real. Then ωf lies in i·(the real form). Where df|_{TS_R} is invertible, which is a dense set because it is invertible near the infrared, V = df⁻¹(ωf) lies in i·TS_R.
3. So V_boost = −iV is a real-analytic vector field tangent to the compact S_R. Its flow Φ_η is complete, and f(Φ_η k) = B_η f(k), where B_η is the Lorentz boost acting on (g, f_j).
4. f is bounded on compact S_R. But the boost orbit of any (g, f_j) ≠ 0 is unbounded in at least one direction of η; this includes null vectors.
5. Near the infrared, (g, f_j) ≠ 0. Contradiction. ∎

**What it uses and what it does not.**
- It uses only one time–space Killing rotation, strict locality, and a compact real shell. Neither the hypercubic group nor reflection positivity enters.
- It does not use the explicit stress. It holds for every choice of T and δ_ξ, every structure-constant choice fixed by the infrared, and both the scalar and fermion cases.

**Spatial rotations alone also obstruct (SUGGESTED).**
- The 2π flow of a spatial rotation is the identity near k = 0, and by analyticity on all of S_R.
- That gives an effective circle action on S_R ≅ T³ with a fixed axis.
- This contradicts the Conner–Raymond theorem: effective torus actions on closed aspherical manifolds are injective, with finite isotropy (cited from memory).
- So the obstruction does not even need boosts. This matches C3's rotation theorem.

**What replaces C3's local (Hessian) obstruction (CHECKED on a cut; `k2_killing_closure.out` (iii)).**
- In continuous time, C3 fixed the time-translation symbol to be the true energy, which forced Hess(ω²/2) = const.
- On Z⁴ the pseudo-energy f₄ is free. The symmetric-stress condition fixes only f = λ∇A on the shell, with λ free.
- So a quasi-local λ can satisfy the local conditions: the Minkowski length f·f is exactly constant on S_R.
- Even so, the boost field needed blows up at an interior point of S_R:
  - |V| ≈ 1.3e4 on the grid at k₁ = 0.79 for the best λ;
  - |V| ≈ 3.8e4 at k₁ = π/2 for λ = ½.
- Only the **global** compactness obstruction remains, and it is enough.

**Escapes (each SUGGESTED or COMPARATOR).**

1. **Quasi-local actions** whose analyticity strip does not contain the band top, so that S_R is not compact.
   - The example is a perfect (RG-blocked) action. Its shell is the union of the images of the continuum hyperboloid, an unbounded tower E_n = √((k + 2πn)² + m²).
   - This is exactly I1's infinite-band tower, realized by couplings with exponential tails in time (Bietenholz–Wiese; Bahr–Dittrich perfect actions; COMPARATOR).
   - Blocking the interacting coupled theory is non-local in general.
2. **Removing the (4, j) Killing rotations from the gauge algebra.** That means foliation-preserving linearized diffeomorphisms (Hořava-type), which is RF/RF3 territory with its own costs. By the suggested spatial-rotation argument, the spatial sector would still obstruct, as C3's rotation theorem did.
3. **Accepting gauge invariance only at O(κ)**, which is lane RW's W2 question.
4. **Non-local matter** (SLAC; I1).

## 4. Reflection positivity and the transfer matrix at ξ = 1 (`k2_transfer_rp.py/.out`)

### K7a's "instability" is not a transfer-matrix failure (CHECKED)

At ξ = 1 the Euclidean one-step transfer eigenvalue is e^{−E} with cosh E = 1 + (ŝ² + m²)/2, which lies in (0, 1] at every momentum. At the corner ŝ² = 12 it is 0.0718.

The real-time leapfrog with the same stencil at τ = a has λ + 1/λ = 2 − ŝ², so |λ|max = 5 + 2√6 = **9.899** at the corner. That is **exactly K7a's 9.9**.

So K7a's number is the Courant–Friedrichs–Lewy failure of an explicit real-time integrator (stability needs τ² · 12 ≤ 4), not a property of the Z⁴ Euclidean theory.

**READING.** The positive transfer matrix generates a quasi-local H = arccosh(1 + ŝ²/2), not a finite-depth local real-time circuit. Whether the framework needs the latter is a separate question.

### Free graviton (CHECKED at the symbol level)

**Temporal gauge.** For s₄ ≠ 0, temporal gauge h_4μ = 0 is reachable exactly and is complete. The time-kinetic form on h_ij is the DeWitt form with eigenvalues {−½, ¼×5}. It is **indefinite**: this is the trace (conformal) mode, so the unreduced slice-to-slice kernel is not a bounded positive operator.

**Reduction to TT.**
- The constraint rows (from the h_4μ equations) have rank 3. Their kernel is the spatial-TT pair plus the longitudinal mode ŝŝa.
- On TT the form is exactly (s₄² + ŝ²)/4 per polarization, at three momenta to 1e-10. That is a nearest-neighbour Gaussian in time, so the transfer matrix is positive, with 4 sinh²(E/2) = ŝ².
- det K_temporal(x = s₄²) = −x⁴(4x + 5)²/4096 at ŝ² = 5/4. The only propagating pole is the TT double pole at x = −ŝ². Everything else sits at x = 0: constraint and zero modes.
- The trace–trace propagator is −(12x − 5)/(2x²). It has no propagating conformal ghost pole.

This settles the K7a referee's open item at the free level: **a positive physical transfer matrix exists after reduction.** The conformal-mode problem lives only in the unreduced form, as in the continuum (Gibbons–Hawking–Perry; COMPARATOR).

### Coupled theory (ARGUED, not computed)

- In temporal gauge only h_ij T_ij couples.
- T_ij uses matter at a single time slice, except the time-link squares in T_jj.
- So for fixed small h, the matter one-step kernels are Gaussian with positive-definite link weights 1 + O(κh), and are positive.
- Joint (h, φ) RP: holds to O(κ). At O(κ²) the link weight would have to factorize as e(h)e(h′), which is a seagull condition. Not shown.
- Staggered fermions: positive two-step transfer matrix (COMPARATOR: Sharatchandra–Thun–Weisz). They come in 4 tastes on Z⁴; K7a's condition (3) is unchanged.

## 5. Map to the fixed readings and the supervisor's expectation

**K2: INCONCLUSIVE** (see the top of this report). The FAIL clause is not met: the stated linearized object exists. PASS is not established: joint RP of the coupled action is unshown, and the fermion T is not written out. The physics answer to the lane's question is the O(κ²) theorem:

- **On Z⁴ the C3 obstruction persists, Euclidean form.** The relevant global sector is the continuous e(4) Killing algebra, not the hypercubic group.
- The lattice "boost" is the Wick continuation of a lattice time–space Killing rotation.
- It fails to close because the real Lorentzian shell of any strictly local action is compact.
- Spatial rotations likely obstruct as well.

**Supervisor's expectation, item by item.**

| Item | Outcome |
|---|---|
| (i) Exact free-graviton linearized diffeomorphisms | **Confirmed** |
| (ii) "Matter coupling breaks them by the discrete Leibniz failure" | **Refined.** Nothing breaks at O(κ): an exact symmetric stress exists for the scalar (built) and the fermion (proved). The Leibniz failure appears at O(κ²), in the Killing (global e(4)) sector, as cos k_ρ and cos 2k_ρ factors |
| (iii) "RP fails at ξ = 1 (K7a)" | **Not confirmed.** The free Euclidean transfer matrices are positive at ξ = 1, and K7a's 9.9 is the leapfrog root 5 + 2√6. Only the unreduced conformal mode is indefinite |

**For lane RK2.** On Z⁴, P0's graviton protection (K7a's "1 of 9 forms if the stress is exactly conserved") is available at O(κ) for free matter. Beyond that order, exact gauge invariance cannot hold for strictly local matter. The non-gauge-invariant forms (K1's count) therefore come back at O(κ²) unless they are tuned. **READING:** this supports K1's expectation of N_tune > 2.

## Assumptions, scope and strong-word check

**Assumptions.**
- **A1.** Euclidean Z⁴ with ξ = 1. This is the approved `kinetic_isotropy_primitive` regulator block, and is supplied structure: the axioms have no time lattice.
- **A2.** K7a's placement and the FP gauge map.
- **A3.** Local means finite range. The theorem extends to symbols analytic on a neighbourhood of the compact S_R.
- **A4.** At O(κ²), structure constants are c-numbers on the matter bilinear at h = 0. Matter-dependent structure functions enter only at O(κ³) there (the same argument as C3's Lemma 1).
- **A5.** The infrared normalization: f ≈ k, and C is the e(4) bracket. This is needed for universal coupling.
- **A6.** Classical (bilinear) identities. Fermion Grassmann signs do not affect bilinear identities.

**Scope.**
- Free matter only.
- The Conner–Raymond route for spatial rotations is SUGGESTED.
- The perfect-action escape is COMPARATOR.

**Strong words.**
- "Exact" means a 0.0 residual on integer or dyadic data, or a sympy identity.
- "Proved" means a short argument under A1–A6, not refereed.

## Files (all in this folder)

- `k2_graviton_gauge_killing.py` / `.out`: FP gauge invariance, KD = 0, spectrum, 10 Killing fields.
- `k2_scalar_stress_exact.py` / `.out`: exact symmetric stress and O(κ) identity; exact pseudo-rotation.
- `k2_killing_closure.py` / `.out`: [L_ω, D_ρ], shell certificate, the singular boost field on S_R.
- `k2_fermion.py` / `.out`: exact naive and staggered pseudo-rotation, spin diagonalization, fermion closure failure, Gordon identity.
- `k2_calabi_lemma.py` / `.out`: rank check of the Killing-cokernel lemma.
- `k2_transfer_rp.py` / `.out`: ξ = 1 transfer matrix vs leapfrog; graviton temporal-gauge reduction.
- `K2_report.md`: this report.
