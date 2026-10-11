# Lane RV4, probe S1 (theorem): can a principle remove the free E_g shear term? (report)

Worker: Claude Opus 5.5. This is the same model family as the supervisor and as V1–V3 and P1. Run 22:44Z to about 23:20Z, 2026-10-11. No repository files were edited. Scratch: `.../scratchpad/RV4/S1/`; every number below is in a `.out` file there. **Not refereed.** The FAIL has to go to codex sol before it is recorded.

## Verdict against the FIXED reading: **FAIL (bounded)**

The FAIL clause is met. Within the classes examined, a local coupling with μ_E = μ_T2 = 0 needs one of three things:
- a tuning: a symbol tuned at one mass, a tuned density weight, or an E_g counterterm;
- the definition R₀;
- matched spectra (P1).

No principle examined fixes it. In particular:
- **(a)** No periodic momentum symbol, local or not, makes every shear flow divergence-free (Theorem A). Even SLAC fails on the torus: the zone faces act as a sink and a source, giving μ_E^SLAC = 1.48e-2 at m = 1. That is 7.5 times the nearest-neighbour value (§1.4).
- **Zeroing μ at all masses.** A zero of μ for every mass requires the strain flow to preserve the density of states (Theorem B). That is impossible for every Morse symbol (Theorem C) and for every analytic separable symbol (Theorem C′). Zeros at a single mass exist, but they are tunings: one is exhibited, and it moves with m.
- **(b)** Density weights (half-density, √J, Weyl volume form) either break RN L1's exact stress, when applied to the operator, or reduce to R₀ or a tuned weight, when applied to the vacuum c-number.
- **(c)** The Ward principle is a genuine principle: compact-gauge covariance would force μ_E = μ_T2. But no local metric coupling is covariant under the matter's own lattice diffeomorphisms e^{−iP[ξ]}, because the Jacobian is exactly that covariance defect (Theorem D). The eigenstate form only restates μ = 0.
- **(d)** R₀ is not derivable. Z³ has no uniform-strain relabelling, and constant h is pure gauge only through a non-compact ξ, whose implementation carries the seam. R₀ is an imposed rule.

**One named open escape.** Gauge generators that depend on the field, U_ξ = exp(−i(P[ξ] + Q[ξ,h])). This is RN L1's unsearched O(κ) completion with metric-dependent structure. It is the only route in this lane on which the Ward principle could still fix the E_g coefficient without tuning.

**Corrections to the supervisor's expectation and to earlier records:**
1. The divergence-free condition is sym(Dp) = λ(k)·I, the conformal Killing equation, not ∂_i p_j = λδ_ij: rotational parts are allowed. On the torus it forces p to be constant for **every** periodic p, including non-local ones.
2. SLAC does **not** cure μ_E on the torus (§1.4). V3's suggestion "a sawtooth f = k would remove it" is refuted. The FIXED disjunct "needs SLAC" is therefore not the operative one, since SLAC is not even sufficient. The operative disjuncts are tuning, R₀ and matched spectra.
3. V3's one-parameter root, f = sin k + a sin 2k with ω held fixed, uses a momentum density that is not the energy current. It therefore breaks RN L1 (E) Ṫ00 = div P, which linear first-class closure needs (§2.4). Tunings consistent with RN L1 do exist (§2.3), but they also depend on the mass.
4. "Non-separable symbols can zero E at the cost of T2" is confirmed, and can be stated sharply:
   - pointwise E_g protection holds iff the hopping is only along body diagonals (which gives four decoupled sublattices);
   - pointwise T_2g protection holds iff the hopping is only along the axes;
   - both hold only when there is no hopping at all.

## 0. Setting and the one formula

**The coupling class (RN L1, V3, P1).**
- Free quadratic matter with dispersion ω, and u = ω²/2.
- RN L1 linear first class needs (E) Ṫ00 = div P and (M) Ṗ = G[T] with the **same** P. (E) makes P the energy current, so its per-quantum symbol is p = ω∇ω = ∇u. Checks:
  - the KG scalar has sin k = ∇(Σ(1 − cos k));
  - the staggered fermion has ½ sin 2p = ∇(½Σ sin²p).
- The linear coupling is −½h_ij T_ij, the conserved stress.
- The uniform-strain completion is the bulk-local unitary first-moment flow K = ½h_ij Σ X_j P_i, whose flow velocity is v = ½h∇u.

**Formula** (V3 Jacobian, refereed; P1 integration by parts, refereed). In RN-L1 normalization, for bosons with ε_vac = ω/2:

  μ_h[u] = ⟨(L_v)² ε_vac⟩ = −⟨∇ε_vac · v (∇·v)⟩ = −(1/8)⟨φ_h ψ_h / ω⟩,
  where φ_h = ∇u·h∇u and ψ_h = h : Hess u.

- The E channel is h = diag(1, −1, 0). The T2 channel is h_xy = h_yx = 1, which has equal norm.
- CHECKED: F(1) = 1.9703886418785e-3, reproduced at N = 48, 64 and 96 (`s1_checks.out` §0).

**Robustness lemma.** PROVED as a sketch: it combines V3's refereed formula with the exact identity for translation-invariant S that the V2 referee confirmed. μ_h depends only on the dispersion u. It does not change under:
- local improvements of P or T00 (these change K only by translation-invariant totals);
- translation-invariant dressings S (vacuum energy density is invariant under quasi-local translation-invariant unitaries);
- T00 placement, as long as (E) holds.

The one-stress requirement also fixes the symbol (§1.3). So in this class **μ is a functional of the matter's dispersion alone**, and every "principle" has to act on u, on a c-number, or outside the class.

## 1. Candidate (a): divergence-free flows

### 1.1 Theorem A (PROVED; CHECKED)

Let p be any periodic vector field on T^d, d ≥ 2, in L¹ (no locality assumed), with derivatives taken in the sense of distributions. Then ∇·(h p) = 0 for every traceless symmetric h if and only if p is constant.

*Proof.*
- ∇·(hp) = h : sym(Dp). Vanishing for all traceless h means sym(Dp) = λ(k)·I: the conformal Killing equation.
- For each Fourier mode n ≠ 0 with coefficient a_n, this requires the traceless part of sym(n ⊗ a_n) to vanish. The real and imaginary parts of a_n separate.
- In d = 2 the condition reads (n_x, −n_y; n_y, n_x)·a = 0. The determinant is |n|² ≠ 0, so a = 0.
- In d ≥ 3: n⊗a + a⊗n has rank at most 2, so it cannot be proportional to I with a nonzero coefficient. Then n⊗a + a⊗n = 0 forces a ∥ n and then a = 0.
- So only the n = 0 mode survives.
- CHECKED: the linear map a ↦ traceless sym(n⊗a) has full rank d for every n ∈ [−3, 3]^d \ {0}, in d = 2 and 3.

**Open zone.** On the open zone (−π, π)^d the same equation allows the conformal Killing fields. In d ≥ 3 these are p = a + Bk + λ₀k + special conformal fields. In d = 2 they are holomorphic p_x + i p_y. For p = ∇u (the RN-L1 case) the condition is Hess u = λ(k)·I, which forces u = λ₀k²/2 + a·k + c: the SLAC form, with a jump on the zone boundary.

### 1.2 Corollary: the lattice-geometric form for p = ∇u (PROVED; CHECKED)

Write u = Σ_n u_n e^{in·k}. Then Hess u has modes −u_n n⊗n, and:

| Condition | Equivalent to | Allowed hopping vectors n |
|---|---|---|
| ψ_E ≡ 0 for all E_g h | n_x² = n_y² = n_z² | body diagonals (n, ±n, ±n) |
| ψ_T ≡ 0 for all T_2g h | n_i n_j = 0 for i ≠ j | axes only (separable u) |
| both | n = 0 | none (u constant) |

**Numbers at m = 1** (`s1_checks.out` §2):

| Symbol | μ_E | μ_T2 |
|---|---|---|
| Axis-only nearest-neighbour | +1.9704e-3 | 0 |
| Body-diagonal-only, u = 1 − cos x cos y cos z | 0 (exact) | +6.012e-4 |

The body-diagonal symbol is IR-normalized, u ≈ k²/2. It vanishes at Γ, (π,π,0), (π,0,π) and (0,π,π): four decoupled sublattices, a doubling. In 2D the E-protected class is diagonal-only hopping.

**Reading.** The Lattice and Admissibility axioms are nearest-neighbour. If the matter kinetic term is strictly nearest-neighbour, it is axis-only. Then T_2g is protected (Liouville) and μ_E is *fixed* with no free parameter: F(M) for the scalar, −½F(2m) for the staggered field. The axioms do not choose the matter Hamiltonian, so this is a reading, not a theorem about the axioms.

### 1.3 Different channels may not use different symbols (PROVED)

Suppose the E components of the linear coupling came from a symbol p^E and the T2 components from p^T, while there is a single symmetric T with Ṗ = −∂T for a single P (RN L1 (M)). The one-quantum uniform stress is τ_ij = p_i ∂_j ω.
- The off-diagonal components fix p_i ∂_j ω for i ≠ j.
- Symmetry forces p ∥ ∇ω.
- So p^E = f_E ∇ω and p^T = f_T ∇ω, with (f_E − f_T)((∂_xω)² − (∂_yω)²) = 0, hence f_E = f_T almost everywhere.
- (E) then fixes f = ω.

A channel-dependent first moment K = Σ h^E X P^E + Σ h^T X P^T would need two momentum densities, so it breaks (M) for any single P.

### 1.4 SLAC on the torus does not remove μ_E (PROVED limit formula; CHECKED)

For p = saw(k) = ∇(Σk_i²/2), periodically extended, the E flow v_x = ½saw(k_x) points *into* the faces k_x = ±π from both sides (a sink) and *away from* k_y = ±π (a source). Distributionally, ∇·v ∋ −π[δ(k_x − π) − δ(k_y − π)].
- ARGUED: the flow is incomplete, so the first-moment generator is not essentially self-adjoint. This is the k-space version of the position-space seam.
- **Regularization-independent limit.** Take any bounded local regularization g_r → k²/2 (sawtooth-squared). The zone-face layer contributes ∫ g″ F(g′) dx = ∫_π^{−π} F(s) ds, by the fundamental theorem of calculus. Hence

  μ_E^SLAC = (1/16π²) ∫∫_{[−π,π]²} (π²/3 − t²) / √(m² + π² + t² + s²) dt ds.

- CHECKED (`s1_checks.out` §3). Two smoothings (Lanczos, Fejér), r = 4 to 64, converge as 1/r. Richardson extrapolation of the Lanczos sequence:

| m | Richardson (Lanczos) | Formula | μ_T2 |
|---|---|---|---|
| 1 | 1.4815e-2 | 1.4833e-2 | 0 |
| 0.5 | 1.5884e-2 | 1.5901e-2 | 0 |

- The naive open-cube value, with φ = π² − t² on the faces, is 0.417. It is also nonzero; it is the ill-defined version.

So SLAC is 7.5 times *worse* than the nearest-neighbour value F(1) = 1.97e-3. The Jacobian is not removed; it is concentrated on the zone faces. "Needs SLAC" is not a valid way out.

## 2. Is μ = 0 per channel possible without divergence-free flows?

### 2.1 Theorem B: mass independence ⇔ DOS invariance (PROVED)

Write ω² = m² + 2ũ. Let ν_h be the pushforward of J″_h dk under ũ, the O(ε²) change of the density of states. Equivalently, ∫G(ũ) J″ = −∫G′(ũ) φψ/4 for every G.

Then μ_h(m) = ∫ ½√(m² + 2E) dν_h(E).

**Claim:** μ_h(m) = 0 for all m in any interval iff ν_h = 0. That is, the bulk strain must preserve the DOS of ũ at second order: E[φ_h ψ_h | ũ] = 0.

**Proof.**
- μ_h is analytic in s = m²/2 on s > 0.
- Its large-s expansion is √s Σ binom(½, n) s^{−n} ∫E^n dν.
- So all moments of the compactly supported ν vanish, and ν = 0.

The same holds for the fermion sign (−ω/2) and for any mass entering as a shift of u. DOS invariance would also give μ = 0 for every species with the same ũ, at any filling.

### 2.2 Theorems C and C′: DOS invariance is impossible

**Theorem C (Morse symbols, any d ≥ 2; PROVED, sketch).**
- A Morse ũ on T^d has a critical point c of index 0 < i < d, since the Morse inequalities give c_i ≥ b_i(T^d) > 0.
- Critical points are fixed points of v = h∇ũ, so J_ε(c) = e^{εψ_h(c)} exactly.
- The van Hove singular part of the DOS at level E_c (a logarithm in 2D, a √ kink in 3D) has coefficient Σ_c J_ε(c) |det Hess ũ(c)|^{−1/2} over the critical points of that index and level.
- Its O(ε²) term is ½Σ w_c ψ_h(c)² > 0 unless ψ_h(c) = 0 for all h, that is Hess ũ(c) ∝ I. A saddle's Hessian is indefinite, so it cannot be ∝ I.
- A smooth part cannot cancel a singular part, so ν_h ≠ 0 for some traceless h.
- By cubic symmetry, μ_h(h, h) = μ_E|h_E|² + μ_T|h_T|². So μ_E(m) or μ_T2(m) is not identically zero, and both cannot vanish on any mass interval.

**Numerically**, for the tuned symbol of §2.3:
- X = (π,0,0) is an index-1 saddle with ψ_E = −1.03.
- M = (π,π,0) is an index-2 saddle with ψ_{E,2} = −1.29.

**Theorem C′ (analytic separable ũ with a single minimum, no Morse assumption; PROVED).**
- Write F(a) = g′(k)² as a function of a = g(k). Then φ_E ψ_E = ½(F(a) − F(b))(F′(a) − F′(b)).
- Write F = 2a + F_n aⁿ + … with n the first nonlinear order. On the small-E level sets, the integrand ≈ n F_n (a − b)(a^{n−1} − b^{n−1}), which has a fixed sign.
- So ν_E ≠ 0 near the band bottom unless F ≡ 2a. That means g = k²/2 near 0, and by analyticity everywhere, which is not periodic.
- This covers every nearest-neighbour or longer-range axis-only symbol, including the staggered fermion (its doublers have the same local expansion).

### 2.3 What is achievable: zeros at one mass, which are tunings (CHECKED)

**A consistent non-separable family** (p = ∇u kept, `s1_tune.out`): u = [Σc_i + bΣc_ic_j + g(1 − Πcos k_i)]/(1 + g), with c = 1 − cos k.
- μ_E = μ_T2 = 0 at m = 1, to 1e-16, at g* = 1.02691, b* = 0.045202. min u > 0. The kernel is finite range (r ≤ 2).
- The same symbol at other masses:

| m | μ_E | μ_T2 |
|---|---|---|
| 0.05 | +2.45e-4 | +2.63e-4 |
| 0.5 | +1.62e-4 | +1.72e-4 |
| 2 | −2.19e-4 | −2.22e-4 |
| 4 | −2.66e-4 | −2.67e-4 |

- So it is two tunings per species, mass-dependent, as Theorem B requires.

**Separable class:**
- In the consistent family u = Σ(c + ac²), μ_E(m=1) stays positive for every monotone band, −¼ < a ≤ 0.6, falling to 3.2e-4 at a = −0.249. No root.
- Random analytic separable symbols with range ≤ 4 (`s1_sep_sign.out`): μ_E < 0 in only 0–3% of samples, depending on the mass. Roots exist, but rarely, and each is a single tuning at one mass.

### 2.4 V3's tuning lies outside the RN-L1 class (PROVED)

f_a = sin k + a sin 2k with ω held fixed is conserved but is not ∇u. So (E) Ṫ00 = div P fails, and the linear lapse/shift algebra no longer closes. Its root a* = −0.0757 is not a coupling of the kind the FIXED PASS clause requires.

## 3. Candidates (b), (c) and (d)

### (b) Half-density, √J and Weyl-volume couplings

Transport ε_vac as a density of weight w: the strained one-particle symbol is (ε J^{−w})∘Φ⁻¹.
- Vacuum energy: ∫ε J^{1−w}.
- μ^(w) = (1 − w)μ₀ − w(1 − w)⟨ε(∇·v)²⟩ (PROVED).
- Weight 0 is V3's scalar transport.
- The half-density Koopman unitary J^{1/2}ψ∘Φ⁻¹ of quantum wavefunctions transports *multiplication operators* as scalars, so it gives w = 0, not ½.

Nearest-neighbour scalar, m = 1 (`s1_checks.out` §6):

| w | μ_E | μ_T2 |
|---|---|---|
| 0 | +1.97e-3 | 0 |
| ½ (half-density) | −8.10e-2 | 0 |
| 1 | 0 by construction | 0 |
| 0.00597 (the zero) | 0 (tuned, mass-dependent) | 0 |

**Where the weight is applied decides what it is:**
- *On the operator (one-particle energies)*, w ≠ 0 adds −w·ε·(h : Hess u)/2 to the linear coupling. That term has a nonzero per-quantum uniform total, so it is not the conserved stress of P and not an improvement (improvements have zero totals). It **breaks RN L1's exact stress**: PROVED.
- *On the vacuum c-number only*, w = 1 is R₀, and other values of w are a tuned c-number. Either way it is an E_g counterterm with a chosen coefficient.

**"Equal to the formal unitary on the bulk, density of states included."**
- For every channel this requires volume-preserving flows, which Theorem A excludes for any periodic symbol.
- For the full spectral measure at O(ε²) it requires DOS invariance, which Theorems C and C′ exclude.
- For the vacuum energy only, it is R₀.
- The formal unitary reaches it only with the seam: in position space on finite boxes (V2/V3), or on the zone faces in k-space (SLAC, §1.4).

**Weyl / √g volume form.**
- In a unimodular parametrization it adds nothing at O(h²).
- In a linear parametrization it is √g Λ, which contributes equally to E and T2, so it cannot remove an E-only term (V3 referee).
- "The vacuum couples only through the volume form" is the statement e(h) = e₀ for unimodular h, which is R₀ restated.

**Classification of (b):** a tuning or a definition. The operator-level forms violate the FIXED requirement of exact stress.

### (c) Ward and eigenstate principles

**Theorem D (PROVED, sketch).** Hypotheses:
- H1: H[h] is a local metric coupling: finite range, depending on h(x) and finitely many differences, with a gapped vacuum (m > 0), so that slowly varying h gives E = ∫e(h(x)) + gradient terms.
- H2: H[h] is second-order covariant under compact gauge transformations, H[h_ξ] = U_ξ H[0] U_ξ† + O(ξ³), with U_ξ implementable and h_ξ geometric (its quadratic part rotation-covariant).

Then μ_E = μ_T2, each equal to the cosmological-constant value of the chosen parametrization (zero in the unimodular one).

*Proof.*
- U_ξ preserves the ground energy exactly. So ∫[e(h_ξ) − e₀] = o(L^d) for every slowly varying compact ξ.
- At O(ξ²) this is p|q|²|ξ̂|² + ½μ(2 sym(q⊗ξ̂)) = 0 for all q and ξ̂.
- The choice q ⊥ ξ̂ along (e_x, e_y) gives μ_T2 = −2p. The choice q = (e_x + e_y)/√2 with ξ̂ ∝ (e_x − e_y) gives μ_E = −2p.

**Consequence.** Take the matter's own lattice diffeomorphisms U_ξ = e^{−iP[ξ]}.
- For linear ξ, the bulk kernel of U_ξ H U_ξ† is the bulk-flow coupling, as V3 found (translation-invariant kernels).
- So any covariant local H would have e = e_flow, with μ_T2 = 0 ≠ μ_E.
- Therefore **no local metric coupling is second-order covariant under e^{−iP[ξ]}**.
- The missing energy sits in terms of the form ξ·∇∇ξ that depend explicitly on ξ: a seam distributed through the bulk.
- In other words, μ_E − μ_T2 *is* the Ward defect, and its vacuum witness is the Jacobian. This matches RN L1's {P[ξ], P[η]} non-closure and the C3 condition Hess u ∝ const.

**The eigenstate form.** "The vacuum stays an eigenstate of the strained Hamiltonian with the same energy density, built into the flow":
- The eigenstate part is automatic for free matter.
- By the robustness lemma, "built into the flow" can only mean choosing u.
- "Same energy density" is then μ = 0 restated: a tuning at one mass (§2.3), impossible at every mass (Theorems B, C, C′).

**Classification of (c):**
- The Ward identity is a **principle**. It is the right one, and it would fix μ_E = μ_T2.
- It is **not realizable** in the RN-L1 class with field-independent generators.
- Realizing it needs field-dependent generators Q[ξ, h] (open). Those would add bulk terms −⟨∇·(h q_h) ε⟩, a further Jacobian whose coefficient closure might or might not fix.
- The eigenstate form is a definition or a tuning.

### (d) R₀ as "strain is a relabelling"

**Not derivable from the axioms.**
- The Lattice axiom's symmetries are the translations and proper cubic rotations of Z³. The automorphism group is discrete, and no element implements a uniform E_g or T_2g strain (PROVED; elementary).
- Admissibility (a nearest-neighbour distribution rule) and Record (locking and readout) contain no metric and no strain.
- In the emergent linear gravity sector, constant h is pure gauge only through a linearly growing, non-compact ξ = ½hx. Its matter implementation is the formal first-moment unitary, which needs the seam (V2/V3) or zone-face singularities (§1.4). Compact gauge transformations cannot implement it covariantly (Theorem D).
- So "uniform strain is a relabelling" is a continuum premise imported onto the lattice, not a consequence of the axioms.

**READINGS:**
- R₀ in its operational form ("normal-order against the transported vacuum") makes the coupling law refer to a privileged state. That sits uneasily with the Qualification "A law privileges no states".
- In its c-number form, R₀ is an E_g counterterm whose coefficient is set to −μ_E.
- The 2026-08-13 revision removed the axiom-level scalar value for absence. R₀ would reintroduce a strain-independent energy for the empty vacuum, which the memo says needs a derivation or an approved-primitive registration.
- A variant, "only records gravitate, so vacuum energy does not", is also not in the axioms. Record governs readout, not what sources the metric.

**Classification of (d):** a definition, i.e. an imposed rule.

## 4. Map to the FIXED readings

| Candidate | Achieves μ_E = μ_T2 = 0? | Keeps RN L1 (exact stress, linear first class, P = energy current)? | Status |
|---|---|---|---|
| (a) one local symbol, all channels divergence-free | No for any periodic p (Thm A) | — | impossible |
| (a) SLAC | No: μ_E = 1.48e-2 at m = 1 (§1.4) | non-local; generator not self-adjoint | fails |
| (a) channel-dependent symbols | — | No (§1.3) | excluded |
| (a) one symbol, zero at one mass | Yes (§2.3) | Yes | **tuning** (2 per species; mass-dependent) |
| (a) one symbol, zero at all masses | No for Morse (Thm C) or separable (Thm C′) symbols | — | impossible in those classes |
| (b) operator-level density weights | for w = 1 (or a tuned w) | No (adds a non-stress term) | violates PASS requirements |
| (b) vacuum-level weight / formal unitary with DOS / Weyl volume form | Yes | Yes | **definition (R₀)** or tuned c-number |
| (c) Ward, field-independent generators | would force μ_E = μ_T2 | Yes | **principle, not realizable** (Thm D) |
| (c) Ward, field-dependent generators | open | open | **open escape** |
| (c) eigenstate / same energy density | restates μ = 0 | — | definition or tuning |
| (d) R₀ / relabelling | Yes, by fiat | Yes | **definition**; not derivable |
| P1 matched spectra | Yes | Yes | mass relations (P1) |

**Reading:** FAIL (bounded). The bound is:
- free quadratic single-band matter (scalar, staggered, naive);
- the RN-L1 coupling class with any translation-invariant dressing or improvement;
- density-weight variants;
- Ward analysis with field-independent generators;
- Theorem C restricted to Morse symbols (Theorem C′ covers the separable class without that restriction).

**Not covered:**
- field-dependent gauge generators, i.e. O(κ) first-class completions with metric-dependent structure functions;
- non-Morse, non-separable symbols with degenerate saddles, as candidates for a mass-independent zero;
- multi-band matter with interband or Berry-connection momenta;
- interactions (P1 estimate);
- non-flow metric couplings (P1 option B is larger: 0.71 for the photon).

## 5. Labels

**PROVED** (same family, unrefereed):
- Theorem A and the open-zone conformal-Killing form;
- the lattice-geometric corollary (body-diagonal vs axis hopping);
- the one-stress proposition;
- the robustness lemma (sketch, resting on refereed V3/V2 identities);
- the SLAC limit formula (sketch);
- Theorem B;
- Theorem C (sketch, standard van Hove and Morse facts);
- Theorem C′;
- the density-weight formula and its stress violation;
- Theorem D and its consequence (sketch, under H1–H2);
- that no Z³ automorphism implements a uniform strain;
- that V3's tuning breaks (E).

**CHECKED:**
- F(1) reproduced;
- Fourier ranks;
- body-diagonal μ_E = 0 and μ_T2 = 6.01e-4;
- SLAC convergence for two regularizations, to 0.1% after Richardson extrapolation;
- the two-parameter tuned root and its mass drift;
- TRIM Hessians;
- the cumulative O(ε²) DOS change is nonzero (nearest-neighbour E; tuned E and T2);
- the separable scans;
- the weight family.

**ARGUED:** the SLAC generator is not essentially self-adjoint (incomplete flow).

**SUGGESTED:** the field-dependent-generator route, if it exists, contributes a further first-moment Jacobian, so its coefficient would have to be fixed by closure and not chosen.

**READING:**
- the strictly nearest-neighbour axioms favour axis-only matter, which protects T_2g and fixes μ_E ≠ 0;
- R₀'s tension with "A law privileges no states" and with the 08-13 removal of the absence scalar.

## Files (`.../scratchpad/RV4/S1/`)

- `s1_checks.py` / `.out`: F(1); Theorem A ranks; protected classes; SLAC limit; density weights; nearest-neighbour DOS change. Its §4 (an (a, b)-family fsolve) did **not** converge: no joint root was found in that family; the residual stayed at 7.6e-5. It is superseded by `s1_tune.out`.
- `s1_tune.py` / `.out`: the consistent two-parameter root, its mass drift, TRIM Hessians, DOS change
- `s1_scan.py`: one-parameter scans (printed only)
- `s1_sep_sign.py` / `.out`: random separable symbols, sign of μ_E
- `s1_dilation.py` / `.out`: trace-channel linear response p (context for Theorem D's parametrization remark)
- `S1_report.md`: this report
