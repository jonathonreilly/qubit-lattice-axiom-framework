# Lane RC, probe C3: gravity-side O(κ) closure for the free lattice scalar

Worker: Claude Opus 5.5 (same family as the supervisor). Run 15:44Z–16:15Z, 2026-10-11. No repository files were edited. Scratch folder: `.../scratchpad/laneRC/C3/` (two scripts, two `.out` files, this report).

## Reading against the fixed line

**C-FAIL (proved within the stated ansatz, and the ansatz is wider than the brief's).** This must go to a codex referee before it is recorded.

No local metric-dependent completion closes the O(κ) constraint algebra for the free lattice scalar. The obstruction sits in a sector where every h- and E-dependent completion term vanishes identically: the Killing (global-charge) sector. There the algebra reduces to the lattice Poincaré relations {P, K} = δH and {P, L} = P. Both fail for any free one-band lattice scalar whose dispersion is a periodic analytic function.

So the result does not depend on the range r or on the polynomial order of the completion. It also does not need non-constant h. The supervisor expected C-FAIL "beyond uniform strain"; the outcome is the same, but the mechanism is different: the failure is h-blind.

## 1. Setup and closure conditions

Notation follows lane RN L1, with λ = √κ:

- C_s = S(q)/κ_s + T00 + λ·T00⁽¹⁾[h, E; φ, π] + …
- C_j = −(J/κ_s)·G_j(E) + P_j + λ·P_j⁽¹⁾[h, E; φ, π] + …
- The H_N gravity part is unchanged.
- T00 and P are L1's exact local energy density and momentum density. The momentum density is also the energy current; this is fixed by L1's O(√κ) closure.
- At leading order the gauge generators are the 09-14 stencils: the vector constraint shifts h → Gᵀξ, and the scalar constraint shifts E → SᵀN.

**Closure** means the brackets {C_s,C_s}, {C_j,C_s} and {C_j,C_j} are combinations of constraints with structure functions. Structure functions may depend on h, as in the linearized hypersurface-deformation algebra (HDA). "Brackets with H" are the special case of constant lapse.

**Lemma 1: field-content bookkeeping. PROVED** under the assumptions listed at the end.

At O(λ⁰), the terms bilinear in matter are:

- **{C_j[ξ], C_s[N]}:** {P[ξ], T00[N]} + T00⁽¹⁾[N; h → Gᵀξ] + P⁽¹⁾[ξ; E → SᵀN]. This must equal Σ(c-number structure functions)·(T00, P).
- **{C_j[ξ], C_j[η]}:** {P[ξ], P[η]} + P⁽¹⁾[η; Gᵀξ] − P⁽¹⁾[ξ; Gᵀη]. This must equal the same kind of span.
- **{C_s, C_s}:** {T00[N], T00[M]} plus E-variation terms.

Only c-number structure functions can produce matter-bilinear terms at this order. A structure function that depends on h or on the matter fields gives cubic terms instead. Terms in a completion that involve E drop out of {C_j, C_j}.

**Why the completions drop out (Killing blindness). PROVED.**

- Gᵀξ = 0 exactly when ξ is constant.
- Gᵀη = 0 exactly when η is a lattice rotation, η_i = A_ij·X_j with A antisymmetric, using edge-centred coordinates.
- SᵀN = 0 exactly when N is linear, because S is built from second differences.

In Fourier language: at ξ-momentum p_ξ = 0, and at first order in the momentum of N or η, every completion column is identically zero, for every range and every polynomial order. Taking this derivative is legitimate because, for local terms, the closure identity is an identity between trigonometric polynomials in the smearing momenta.

## 2. Linear system and obstruction

**Exact identities for the L1 scalar (CHECKED).** `c3_hblind_sector_exact.py` uses exact dyadic arithmetic, so residuals are exactly 0.0. The fields are compactly supported on Z³, and linear smearings x_b are used. Write K_b = Σ x_b T00 for the boost generator and L_ab = Σ(X_b P_a − X_a P_b) for the rotation generator.

- Zeroth order: Σ_x δ_c T00 = 0 and Σ_x δ_c P_a = 0. So structure functions at zeroth order vanish.
- **{K_b, H_m} = −P_tot,b exactly.** The Killing sector of {H, H} closes. This agrees with L1's exact T00–T00 bracket.
- **Boost sector:** {K_b, P_tot,c} = −δ_bc·E_c exactly, where E_c = Σ_k cos k_c × (energy of mode k).
  - Closure needs −δ_bc·C′·H_m + C·P_tot.
  - E_c contains the off-diagonal terms π_x·π_{x±e_c}. Neither H_m nor P_tot does.
  - Defect, exact: E_c − H_m = −¼ Σ_x [(d_cπ)² + d_cφ·d_c(ω²φ)].
  - Fitting by span{H, P_tot, K_e, Σ x P} leaves relative residual 0.37–0.40.
- **Rotation sector:** {L_ab, P_tot,c} = −(δ_bc·Q_ca − δ_ac·Q_cb) exactly, where Q_ca has symbol cos k_c·sin k_a. Continuum closure needs Q_ca → P_tot,a. The fit residual is 0.74–0.88.

**Fourier linear system for {C_j, C_s} (CHECKED).** This is in `c3_fourier_system_and_dispersions.py`.

- **Unknowns:**
  - structure functions C′(p) and C_j(p), trigonometric polynomials of degree ≤ r, shared by all matter momenta;
  - the image (1 − cos p)·Ξ(p, q) of any E-dependent completion. Ξ has degree ≤ r in p and is arbitrary in q, which is more general than any local ansatz;
  - the h-dependent completion is identically zero at p_ξ = 0.
- **Lattice L1:** rank[A|b] = rank A + 1 for r = 1, 2, 4, 8, 12 and 16. The system is inconsistent and the solution space is empty for every r.
  - The residual on the IR rows (|p| ≤ 0.1) is 0.77–1.0 at every r.
  - The residual over all momenta falls from 0.26 to 0.024 as r goes from 1 to 16.
- **Continuum control** (symbols k and k²): the system is consistent, with residual about 1e-14 at r = 1, 2, 4, and no completion is needed.
- **Certificate of infeasibility, independent of r:** take ℓ = the first Taylor coefficient at p = 0, after projecting out span{H, P_tot}. ℓ annihilates every completion column, and ℓ(b) = −δ_bc·(E_c − H_m) ≠ 0.

**General theorems.**

- **Boost theorem (PROVED).** Write u = ω²/2.
  - The flow generated by P_tot,c rotates mode phases by f_c = ∂_c u.
  - So the first-order part of {K_b, P_tot,c} is Hess u(q)_bc × (energy of mode q).
  - Closure, even with arbitrary constant deformations C′ of the structure function, needs Hess u to be constant.
  - A periodic u with constant Hessian is constant. Its only "solution" is the dispersionless, Carrollian case ω = const with C′ = 0, which is not GR.
  - This holds for any local or analytic single-band dispersion. No cubic symmetry is assumed.
- **Rotation theorem (PROVED).** Write M = Hess u(0), assumed positive definite.
  - Matching at small k forces Hess u = M + μ·∇u∇uᵀ wherever ∇u ≠ 0.
  - At the maximum of u the Hessian must be ≤ 0.
  - But on the plane ∇u^⊥ at nearby points the Hessian equals M > 0. Taking the limit gives a contradiction in d ≥ 2.
- **Dispersion scan (CHECKED).**
  - For every periodic u the zone average of u″ is 0. So the zone average of the anomaly symbol A = u″ − 1 is exactly −1 for every stencil range r_m.
  - Improved stencils give A = O(k^{2r_m}) in the IR; the measured exponents are 2.00, 4.00 and 6.00. Meanwhile A(π) grows from −1.5 to −2.5 as r_m goes from 1 to 5. The anomaly moves into the UV; it is not removed.
  - Random cubic dispersions with range 3, including face and body hops, give a Hessian zone average of exactly 0 on the grid, i.e. 100% non-constant.
  - SLAC (u = k²/2 on the lifted zone) has A = 0 inside the zone. Periodicity is then paid for by a delta function of weight −2π at the zone boundary.

**Which lattice identity blocks closure (READING, backed by the identities above).**

- P_tot,c does not generate a translation. It generates the central-difference derivation D_c applied factor by factor.
- In the continuum, the Killing relations follow from Leibniz plus integration by parts: Σ x_b·∂_c(F) = −δ_bc·ΣF.
- On the lattice, the first moment of the factorwise D_c is the cos-weighted density instead.
- This is the moment form of the Kato–Sakamoto–So Leibniz no-go: no local, translation-invariant difference operator obeys Leibniz.
- Equivalently, the free lattice scalar has H and an exactly conserved pseudo-momentum, but no boost or rotation generator that closes with them. The HDA's global-charge sector is the Poincaré algebra.

## 3. Prior art: what transfers

- **Bahr–Dittrich** ([0907.4323](https://arxiv.org/abs/0907.4323), PRD 80, 124030; [0905.1670](https://arxiv.org/abs/0905.1670); [0909.5688](https://arxiv.org/abs/0909.5688)).
  - Linearized Regge calculus on a flat background keeps an exact vertex-translation gauge symmetry.
  - That symmetry breaks on curved backgrounds and at higher order, where constraints become pseudo-constraints.
  - Perfect (coarse-grained) actions restore it, but are non-local in general.
  - **Transfer:** our breaking appears at the first nonlinear order, as theirs does. Here it is already present on a flat background, sourced by matter on a fixed lattice; Regge's flat vertices are free to move. Their perfect-action restoration corresponds to SLAC or infinite-band matter.
- **Dittrich–Höhn** ([0912.1817](https://arxiv.org/abs/0912.1817), [1108.1974](https://arxiv.org/abs/1108.1974)).
  - Local first-class constraints exist for linearized flat Regge. This matches L1's O(√κ) result.
  - Pseudo-constraints appear once the symmetry is broken.
  - **Transfer:** the C3 anomaly is a concrete matter-sector source of that breaking.
- **Gambini–Pullin, consistent discretizations** ([gr-qc/0206055](https://arxiv.org/abs/gr-qc/0206055)).
  - The constraint algebra "problem" is removed by letting the equations fix lapse and shift.
  - **Transfer:** this is the price route. It means part of the lapse freedom is lost and a preferred foliation appears.
- **Loll** ([gr-qc/9708025](https://arxiv.org/abs/gr-qc/9708025)): lattice spatial-diffeomorphism commutators are anomaly-free only as the lattice spacing goes to zero.
  - **Consistent:** our anomaly is O(k²a²) in the IR.
  - **But:** its zone average is −1, so it is O(1) on lattice-scale (loop) modes.
- **Kato–Sakamoto–So** ([0803.3121](https://arxiv.org/abs/0803.3121)): Leibniz is incompatible with translation invariance plus locality. Their escapes are an infinite-flavour extension or a matrix (non-local) form, which matches the escapes found here.
- **Continuum control (comparator, cited from memory, not re-fetched):** Teitelboim (1973) and Hojman–Kuchař–Teitelboim (1976) show the minimally coupled scalar closes the HDA. The h-blind sector of that control was checked here (residual 1e-14).

## 4. The referee's seagull, and the minimal non-locality

**The seagull is not touched by the obstruction.**

- The uniform-strain seagull H_sg = −½[K_h, [K_h, H_m]] lives in the symmetric (strain) part of the first-order {C_j, C_j} condition.
- That part depends on the completion: it fixes P⁽¹⁾_tot under uniform strain to be the K_h transform. The obstruction does not touch it. Its consistency with the rest of the algebra was **not checked**.
- So the zero uniform-strain TT response stands.
- But no first-class O(κ) algebra containing the seagull exists for this matter, so a closing gauge algebra does not protect it.
- Whether the anomaly forces a TT mass or Lorentz-violating graviton terms at O(κ) is **open**; it was not computed.

**SUGGESTED consequence.** Dirac's algorithm must then do one of two things, as in Bahr–Dittrich and Gambini–Pullin:

- fix part of the lapse, giving a preferred foliation (a projectable-Hořava direction, whose scalar sector L3 found unstable); or
- add secondary constraints.

The mode count was not computed.

**Minimal non-locality (SUGGESTED, from the system above).**

- **Gravity side:** range-r completions cancel the anomaly only for smearing momenta |p| ≳ 1/r. Exact cancellation needs Ξ ~ 1/p, i.e. a ∂Δ⁻¹ kernel decaying like a power, about 1/|x|².
- **Matter side:** the SLAC sawtooth (1/r hopping) or an infinite-band (perfect-action) tower. This is the same SLAC price that C1 targets.

**Residual size.**

- Anomaly operator: −¼Σ[(d_cπ)² + d_cφ·d_c(ω²φ)].
- IR: relative size k²a²/2, or O((ka)^{2r_m}) for improved stencils.
- Lattice-scale fields: median relative size 1.15.
- It does not shrink with the completion range r.

## Assumptions, scope and strong-word check

**Assumptions.**

- **A1:** L1's κ bookkeeping, with leading gauge generators Gᵀ and Sᵀ.
- **A2:** completions are polynomial in h and E. Matter enters at least quadratically (φ → −φ). Local means finite range or a smooth symbol (summable first moment).
- **A3:** structure functions are c-numbers on matter-bilinear terms (forced at this order). They may be non-local in the smearings.
- **A4:** T00 and P are fixed up to improvements. Improvements commute with P_tot, which was checked by argument.
- **A5:** classical brackets; quantum commutators of quadratic forms agree up to c-numbers.

**Scope.**

- The theorems cover single-band scalar lattice matter only.
- Multi-band matter (staggered fermions, Maxwell) is SUGGESTED to fail the same way, since the band-diagonal ∂f would have to equal δ. Not checked.

**Strong words.**

- "Proved" means a short algebraic argument under A1–A5, plus exact or numerical confirmation for L1.
- "Inconsistent for every r" rests on the r-independent certificate. Numerics were run for r ≤ 16.
- No claim is made about non-local completions, infinite-band matter, or abandoning GR's algebra. Those are the named escapes.

## Files

All in `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/laneRC/C3/`:

- `c3_hblind_sector_exact.py` / `.out`
- `c3_fourier_system_and_dispersions.py` / `.out`
- `C3_report.md`
