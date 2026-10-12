# C5 R11-2: producing the graviton (qubit realization of the weak N-type box graviton; WW on box domains)

**Worker.** Claude Opus 5.5 (same family as every C5 worker and the supervisor). 2026-10-12, 18:36Z to about 19:00Z. **Unrefereed.** No repository file was edited. Scripts and outputs are in `scratchpad/C5/R11-2/scripts/`. Each run took under 3 s on 2 threads.

**Paths.** `P/` = `.claude/science/exercises/gravity-current-state-20261009/`. `N0914` = `docs/LOCAL_FINITE_CLOCK_TENSOR_CONSTRAINTS_CUBIC_DISPERSION_AND_LINEAR_GRAVITY_BOUNDARIES_BOUNDED_THEOREM_NOTE_2026-09-14.md`. `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`. Bare `TESTS`/`SUMMARY` are in `P/`. TESTS line numbers are those of the current file (R11-2 is at `TESTS:4123-4155`; the file shifted by 16 lines during this run).

**Labels.** proved = derivation here (unrefereed); checked = numerics here; suggested = argument; reading = interpretation; comparator = literature (V = verified on the web in this run; RECALLED otherwise).

---

## 0. Plain words

- **The question.** Can one qubit per site, with local rules only, *produce* the weak N-type graviton (two light-like TT waves, exact linear constraints, exact coupling to matter's energy)?
- **What I found.** It cannot be done the straightforward way, and the reason is now sharp. There are two obstacles: one for the graviton itself, and one for its coupling to matter.
- **Obstacle 1: the graviton's speed counts its "non-local" sides.**
  - Written in its gauge-invariant local quantities (the curvature R and its conjugate curl C), the N-type graviton's energy is exactly the cubic-dispersion L-type energy with an inverse-Laplacian (1/r, Coulomb-like) kernel on *both* sides (checked to 1e-16).
  - Each side that keeps that kernel buys one power of k: ω_TT ∝ k³ (no side), k² (one side), k (both sides). The k² case is new.
  - A side can carry the kernel without non-local couplings only if its variable is unbounded along its gauge orbits.
  - Finite sites (qubits, clocks) have compact gauge orbits. On an exact constraint sector, averaging over those orbits turns any Hamiltonian into a strongly gauge-invariant local one, which gives k³ in the regular class (N0914's theorem).
  - Integer-valued (rotor) sites give k² at best.
  - Light-like needs continuous canonical variables on both sides, or instantaneous 1/r couplings between local curvature operators. That is Marolf's "kinematic non-locality".
- **Obstacle 2: an exact constraint that is sourced by energy freezes the matter.**
  - Take any realization in which the linear constraints include matter's energy density as their source, as in R9-9's target. Its physical states contain matter only in states that are simultaneously eigenstates of every local energy density (proved).
  - For free hopping fermions the only such states are the empty and the completely filled lattice. That is proved for one particle, and checked many-body in 1D (L = 6, 8) and on a 2D 3×3 torus.
  - So exact linear constraints plus mobile matter is impossible beyond first order in κ. Mobile matter needs the non-abelian constraint algebra of nonlinear gravity.
- **Weinberg–Witten on box domains.**
  - The "rapidity budget" does not shield composite gravitons. WW's decisive boost (to the brick-wall frame) never raises either leg's energy (proved, checked), so it stays inside the momentum box.
  - What decides whether WW binds composites of box matter is whether box matter has a Lorentz-covariant stress tensor. That is not established for interacting box laws.
  - For a gauge graviton: WW proper does not bind. But any exact finite-site sector has a gauge-invariant local energy density (Lemma A in its commuting scope), which is WW's Hamiltonian face. So "evades WW like GR" is unavailable on exact qubit sectors.
- **Readings.**
  - Overall **OPEN**.
  - (a) **SUGGESTED**.
  - Two stated-class no-gos (X1: never light-like; X2: never couples to mobile energy-momentum) go to the referee as EXCLUDED candidates.
  - **Registration note.** PRODUCED as worded (an exact N-type constraint algebra *and* a Ward-exact universal stress) cannot be met beyond O(κ) by any exact linear-constraint realization (X2). The clause can only be met at tree level, as R9-9 met it.

---

## 1. Hypotheses (stated before titles) and excluded outside realizations

- **H-sites.** ⊗_{Z³} M₂(C), local or super-polynomially quasi-local terms. Blocking sites into cells of b³ qubits gives finite local dimension 2^{b³}, so "finite-dimensional slots" covers ⊗M₂ up to quasi-local blocking. For comparison two infinite-dimensional slot types are also treated: ℓ²(Z) (a rotor: integer n, compact conjugate θ) and ℓ²(R) (a CCR pair). These are not ⊗M₂.
- **H-fields.** Symmetric h_ij and E_ij in N0914's staggered placement, with midpoint symbol q_i = 2 sin(k_i/2). The constraints are G = ∂_iE_ij (vector) and S = tr R(h) (scalar). G and S commute by the integer identity G Sᵀ = 0 (`N0914:91-104`, with G Sᵀ = 0 at `:101`; re-checked in `r112_symbols.out` §1).
- **H-exact.** "Exact" means the physical sector is the joint kernel (or joint +1 eigenspace) of local constraint generators with uniformly bounded support. Stabilizer, ice-rule and R9-5-type invariant-sector realizations are all of this form.
- **H-regular** (used only where stated). N0914's regular character class: a lifted Weyl-character expansion with Σ|c_a|[μ₂(m_a)² + μ₁(r_a)²] < ∞ (`N0914:239-249`). Super-polynomially quasi-local terms satisfy it, since all their moments are finite.
- **Excluded, as the registration requires:** nonlinear gravity, pair-creating matter, Λ.
- **Outside realizations not covered by any no-go here.** Each one is a live route:
  - (O1) emergent (not exact) constraints;
  - (O2) non-regular infrared maps: strong-coupling phases, singular semiclassics, aliased high-harmonic characters with no small-field expansion (qubits at N = 2 with no lifting), and gapless auxiliary sectors;
  - (O3) O(κ²)-deformed (non-abelian, field-dependent) constraint algebras;
  - (O4) instantaneous long-range couplings;
  - (O5) mixed per-component assignments of integer and compact variables (§4.3, partly analysed);
  - (O6) Goldstone-type tensor modes from exact internal symmetries (§4.6, suggested only).

## 2. Prior art (each counted once)

1. **N0914** (main): the integer clock complex with exact commuting G and S (`:88-112`), and the explicit finite-clock Hamiltonian (`:146-184`). Its regular compact-character theorem gives every frequency O(k³) (`:186-224`). H_N is local but noncompact and weak (`:72-84`). Named escapes: high harmonics, winding scaling with N, singular semiclassics, extra fields (`:218-224`). The source comparison (`:276-306`; the inverse-Laplacian kernel at `:290-292`).
2. **Lane R:**
   - R2 and its referee: the strong-class mode counts 5/4/3/2 with dispersions k, k, k², k³ (`TESTS:749-759`; `agents/R2_referee.md:3-8`).
   - The R2 referee's correction that the exact-constraint weak VS quotient has two positive linear TT modes (`R2_referee.md:16`).
   - R1: "a noncompact IR field can emerge from qubits" (`TESTS:741-746`).
   - R0's literature table: the only linear ±2-only case is weak invariance on noncompact variables (`agents/R0_report.md:158-168`).
   - PR #9363 probes 10, 13, 14, 15 as summarized in R0 (`R0_report.md:96-101`):
     - probe 13: "weak invariance adds nothing in lifted clock encodings";
     - probe 15: the swapped quantum-link assignment, with Einstein–Hilbert exactly invariant and TT f-sum ≤ Cq².

     These are the closest prior art to my §4.2 and §4.3. **I could not read them in full:** they are on unlanded branches and not on main (git grep found no file).
3. **R6-2:**
   - Lemma A (averaging), which the referee found false as stated but valid for support-preserving direct-product gauge actions (`agents/C5_R6-2_report.md:131-138`; `C5_R6-2_referee.md:33-50`).
   - HWW and the "Hamiltonian face of WW" (`C5_R6-2_report.md:140-197`).
   - The WW hypotheses table (`:201-209`).
4. **Lane RN L3:** a pointwise lapse constraint S(q) = κT₀₀ freezes T₀₀ via SK = −DG (`agents/RN_L3_referee.md:5,21`; `RN_L3_report.md:26`). My Lemma F (§6) is the quantum, realization-independent generalization. The freezing *phenomenon* is prior art and is counted once.
5. **The 09-30 mixed-constraint note:** the next mixed lapse/shift equation fails for regular finite-support canonical seeds (`docs/FINITE_RANGE_CANONICAL_TENSOR_MIXED_CONSTRAINT_BOUNDARY_BOUNDED_THEOREM_NOTE_2026-09-30.md:1-8`). This is related to O3.
6. **The C5 rounds:**
   - R9-9's tree-level box graviton (`TESTS:3939-3944` in S11's numbering; `vR9-9:3`);
   - R9-5's qubit box matter (`TESTS:3917-3923`);
   - S11 P41 (`agents/C5_S11_synthesis.md:228`).
7. **Literature:**
   - Gu–Wen, arXiv:0907.1203 (V): the L-type has ω ∝ k³; the N-type linear dispersion is "argued", with no reliable method; Nucl. Phys. B 863 (2012) 90.
   - Marolf, arXiv:1409.2509 (V; PRL 114, 031104): gravity with universal coupling to energy has an on-shell boundary Hamiltonian; local kinematics forces frozen bulk dynamics, and instantaneous long-range interactions are the only way out.
   - Jenkins, arXiv:0904.0453 (V via search summary): WW versus emergent gravitons, and a gauge-invariant conserved stress forcing graviton Lorentz non-covariance.
   - Weinberg–Witten, PLB 96 (1980) 59 (RECALLED; the proof structure below is standard).
   - Xu 2006 (soft gravitons), Pretko 2017 and Rasmussen–You–Xu 1601.08235: RECALLED; R2's referee verified Pretko and Xu–Hořava.

## 3. Probe (a): Weinberg–Witten on box domains

**The WW proof in five steps** (comparator, RECALLED structure):
- W1: massless one-particle states with helicity σ.
- W2: a Lorentz-covariant conserved T^μν with ∫T^{0ν} = P^ν.
- W3: forward continuity, lim_{p′→p}⟨p′σ|T^{μν}(0)|pσ⟩ = p^μp^ν/E.
- W4: for p ≠ p′, boost to the brick-wall frame (p⃗ + p⃗′ = 0); a rotation by φ about the axis gives phase e^{2iσφ} against tensor weights |m| ≤ 2, so the matrix element vanishes for |σ| > 1.
- W5: W4 at every θ > 0 plus W3 at θ → 0 is a contradiction.

**Lemma K (kinematics; proved, checked `r112_ww_kinematics.out`).** For massless legs (E₁, n̂₁) and (E₂, n̂₂) at angle θ, boost along u = P̂ with rapidity η ∈ [0, η*], tanh η* = |P⃗|/(E₁ + E₂). Then:
- Each leg's energy stays ≤ max(E₁, E₂) along the whole path.
- η* = artanh(cos θ/2) ≈ ln(4/θ) → ∞ as θ → 0 (equal energies).
- The brick-wall leg energy is E sin(θ/2) → 0.

*Proof.* E_i(η) = E_i(cosh η − sinh η cos α_i), which decreases while tanh η < cos α_i. For the harder leg, v* ≤ cos α₁ ⟺ E₂ ≤ E₁, so it decreases monotonically. The softer leg passes its minimum and ends at √(E₁E₂) sin(θ/2) ≤ E₁, so it never exceeds max(E₂, E₁). ∎

*Check.* 2.4 × 10⁶ path points give max E_leg/max(E₁, E₂) = 1.000000000000 (attained at η = 0). The η* table matches ln(4/θ) to three decimals. The θ = 1e-9 line prints inf, because cos(θ/2) rounds to 1 in double precision; that is a float artefact.

**Which step uses unbounded boosts.** Only W4 → W5 at small θ, through η* → ∞. Lemma K shows these boosts lower energies. So for legs inside the inscribed ball |k| < B of the momentum box (S11's "box domain", `C5_S11_synthesis.md:35`), the whole boost orbit stays inside the box. The C-box budget is a momentum budget; for massive particles it reads as a rapidity budget, ln(2B/m) (`SUMMARY:574`). **The budget does not block WW** (proved, for the kinematics).
- W4 also needs rotations about an arbitrary axis. These are exact on R9-6's ball sector (`C5_S11_synthesis.md:48`) and deformed off the cube (reading: the inscribed ball suffices).

**(i) A composite spin-2 state of box matter.**
- W1, W3, W4 and W5 go through inside the box, given Lemma K.
- **The open premise is W2.**
  - Interacting box laws are unitarily equivalent on the box sector to Bakamjian–Thomas-type direct-interaction charts (R8-1, R9-6).
  - The packet's stresses (R9-2, R9-10) satisfy Ward and moment identities box-to-box (`C5_S11_synthesis.md:56-69`) but have no finite-boost covariance of their form factors.
  - Free box matter has a covariant T (its free-field chart) but no bound states.
- **Reading: WW binds massless helicity-2 composites of box matter exactly when the box sector carries a covariant conserved T (W2). The rapidity budget is not an escape.** SUGGESTED, because W2 is not settled.

**(ii) A gauge graviton without a gauge-invariant stress.**
- WW proper does not bind (comparator: GR's pseudotensor loophole). R2 and its referee agree (`R2_referee.md:38`).
- **But on any exact finite-slot sector, a gauge-invariant local energy density exists.**
  - Lemma A in its referee-surviving scope applies to commuting generators: averaging a local term over the compact group generated by the finitely many *commuting* generators that overlap it gives a local, strongly invariant term with the same sector restriction (§4.1).
  - So the produced graviton would have a local, observable, gauge-invariant energy. That is WW's Hamiltonian face (R6-2 reading `:195-197`; Jenkins V; Marolf V).
- **So "WW does not bind a gauge graviton, as in GR" holds only for realizations without exact finite-slot sectors.** Those are noncompact, emergent, or non-regular routes (O1, O2, O4).

**(a) reading: SUGGESTED.** This matches the expectation on (i). On (ii) the expectation needs the qualifier above.

## 4. Probe (b): construction

### 4.1 The cheapest exact ⊗M₂ model with the N-type gauge structure, and why its sector is strong

- **Construction.** N0914's finite-clock Hamiltonian (`:146-176`):
  - N-level slots with commuting stabilizers X^{G-row} and Z^{S-row};
  - exact invariant zero-syndrome sector;
  - lifting for N > 36M;
  - each slot embedded in ⌈log₂ N⌉ qubits with a local penalty (`:180-184`).

  On ⊗M₂ this is quasi-local after blocking. For N = 64 it is 6 qubits per slot and 36 per cell. Its regular small-field symbol is H_L. At the Gaussian level this gives:
  - 2 TT modes, ω² = Jg k⁶ (`N0914:69-71`);
  - no helicity-1 or helicity-0 modes, which the exact constraints remove;
  - no claim of a gapless phase (`N0914:165-168`).
- **Lemma A_c (commuting scope; proved here, the same lemma as R6-2 Lemma A restricted to the scope its referee accepted).**
  - Setting: local constraint generators {g_y}, mutually commuting and of bounded support, on finite-dimensional sites. For a local term h_x, let K_x be the compact closure of the group generated by the finitely many g_y with [h_x, g_y] ≠ 0. Define h̄_x = ∫_{K_x} U h_x U† dU.
  - Claim 1: supp h̄_x ⊂ supp h_x ∪ ⋃ supp g_y.
  - Claim 2: [h̄_x, g_z] = 0 for every z. For z in the overlap set this is Haar invariance of K_x. For z outside it, every U ∈ K_x commutes with g_z (the generators commute), so [h̄_x, g_z] = ∫ U[h_x, g_z]U† = 0.
  - Claim 3: on the sector, P h_x P = P h̄_x P.
  - The referee's counterexample needs non-commuting overlapping generators, which this setting excludes. Since G Sᵀ = 0, the N-type stabilizers commute.
- **Consequence (proved, given N0914).**
  - Any Hamiltonian on an exact finite-slot N-type sector, including a wrapped polynomial copy of H_N's weak terms, has the same sector dynamics as a strongly invariant local Hamiltonian.
  - If that Hamiltonian is H-regular and lifted, every frequency is O(k³) (N0914 `:209-215`).
  - Mechanism: on a compact orbit E → E + Sᵀβ (mod N), the polynomial K_N(E) is constant only until the orbit wraps. The orbit average keeps only the S-invariant characters, which are O(k) by the E-side lemma (re-checked: no constant S-invariant symbol, `r112_symbols.out` §2).

### 4.2 The dressing law (proved; checked `r112_symbols.out` §4)

- **The identities.** On the TT subspace, for every k:
  - E:E − ½(tr E)² = |C(E)|²/q²;
  - h:R(h) = |R(h)|²/q².

  Both are checked to ≤ 2.4e-16 at random k, with C as in `N0914:55` and R with the Fourier sign of the real-space stencil.
- **So H_N|_TT = H_L|_TT composed with (−Δ)^{−1} on both the C side and the R side.**
- **Counting.**
  - Strongly invariant local symbols have H_EE^TT = O(k²) and H_hh^TT = O(k⁴) (N0914's lemma).
  - Each side that carries the inverse-Laplacian dressing loses two powers.
  - Hence ω_TT ∝ k^{3−n}, with n ∈ {0, 1, 2} the number of dressed sides.
- **Positivity.** The dressing is a *positive* 1/r kernel on gauge-invariant data. Static exchange of a dynamical mediator gives a *negative* kernel. A positive Coulomb-type kernel arises from a Gauss-law constraint whose charge is R (or C) (suggested). That route brings the mediator's own transverse sector, which was not analysed (open).

### 4.3 One noncompact side (rotor slots ℓ²(Z); proved at the symbol level, checked `r112_symbols.out` §1–3)

- **Class A (E integer-diagonal, h compact).**
  - G(E) is diagonal and integer-valued, so h-characters must satisfy Gm = 0 exactly, with no aliasing. Then m = O(k²) (cycling lemma, re-checked: free parameters = 0).
  - S generates integer shifts of E with non-compact Z-orbits.
  - A polynomial E-form K is allowed iff K s ∈ Im Gᵀ and sᵀKs = 0 for the S-shift vectors s. K_N satisfies this: residual ≤ 3.9e-16, while ‖K_N Sᵀ‖ = 0.16 to 1.85, so it is weak but not strong.
  - So H_EE = O(1) and H_hh = O(k⁴): **2 TT modes, ω = √(Jg) q² (exponent 2.000 checked), no extra modes.**
- **Class B (h integer, E compact).**
  - h:R is an exactly invariant global quadratic form (‖Q_N V‖ ≤ 5e-16).
  - E-characters must satisfy S r = 0 exactly, so r = O(k).
  - **ω ∝ q² (exponent 2.001 checked), 2 TT modes.**
- **Controls.** Both sides compact (class L) gives exponent 2.999. Both sides polynomial (ℓ²(R), H_N) gives 1.001.
  - In class A, a random positive E-form stands in for any allowed TT block; only its order matters.
- **Why these are not ⊗M₂.** With a bounded integer side (spin S), the shift-type gauge transformation of the other constraint is not unitary, so only one constraint can be exact. The other is then emergent (O1), and the theory reverts to R2's V-type (with the helicity-0 mode) or to the clock class.
- **Mixed per-component assignments (O5) are not covered.** For example h_diag integer and h_off compact. Reading: they lead to discrete (Z-valued) gauge groups and modular conditions, the aliasing escape of `N0914:218-224`.
- **Prior-art caveat.** PR #9363 probe 15 (the swapped quantum link, "Einstein–Hilbert exactly invariant, TT f-sum ≤ Cq²") is class B in quantum-link form. I have only R0's one-line summary. The exponent-2 statement for class B may therefore be partly prior art. Class A and the dressing law were not found in the repo.
- **Observational status.** ω ∝ k² is excluded by GW170817 (comparator; `C5_R6-2_report.md:169`, citing `C5_O2_report.md:48`).

### 4.4 Mode count and extra modes

| Class | TT modes | Extra gapless modes |
|---|---|---|
| Exact sectors (L, A, B) | exactly 2 TT | none at the Gaussian level |
| V-type (only G exact) | 2 TT | a gapless helicity-0 mode (R2) |
| S-type | 2 TT | ±1 and 0 partners, linear (R2) |

### 4.5 What would PRODUCE light-like TT (named, not adopted)

Both sides need the dressing:
- (i) continuous canonical pairs on h and E: H_N itself, i.e. the graviton supplied (P41);
- (ii) instantaneous positive 1/r couplings of local curvature operators on both sides (Marolf's non-locality);
- (iii) a non-regular strong-coupling phase that generates both kernels (Gu–Wen N-type, uncontrolled by its authors' own account, V).

### 4.6 A partial route (suggested only)

- An exact internal continuous symmetry of ⊗M₂ (an SU(2) acting on each site's spin) broken to a subgroup gives linear Goldstone modes. They need no tuning and are protected by Goldstone's theorem.
- Locking spin space to the lattice frame could give two of them helicity-±2 labels.
- They would couple to the broken symmetry's current, not to energy-momentum (lane R's failure mode). WW forbids a Lorentz-invariant infrared for them if a covariant T exists (Jenkins, as Goldstones of Lorentz violation).
- Not built.

## 5. Probe (c): the box symbol

- **Proved, in class H-exact ∩ H-regular, lifted.** R9-9's trick replaces q by a smooth non-analytic d(q) equal to q on the box.
  - It works for H_N because H_N's symbol is free at k → 0.
  - In the exact compact class, the TT symbol's vanishing order at k = 0 (O(k³), or O(k²) with one rotor side) is a Taylor statement that any C² symbol obeys. Super-polynomial locality keeps every moment finite (`N0914:239-249`).
  - A box symbol with ω = |q| on a neighbourhood of 0 contradicts that order.
- **So the emergent dispersion is fixed by the constraint structure, and the box trick cannot be applied to it.**
- The trick needs one of: a dressed side (§4.2), a non-regular infrared map (O2), or the supplied noncompact comparator.

## 6. Probe (d): the source

### 6.1 Lemma F, frozen sources

**Setting (proved).**
- ℋ = ℋ_g ⊗ ℋ_m, with constraints C_x = S_x ⊗ 1 − κ 1 ⊗ ρ_x and G_{x,i} = (Gp)_{x,i} ⊗ 1 − κ 1 ⊗ π_{x,i}, where κ ≠ 0 and ρ, π are matter energy and momentum densities.
- {S_x, (Gp)_{y,i}} is any commuting family of gravity operators. In the N-type case S_x depends on h only, Gp on E only, and [S, Gp] ∝ G Sᵀ = 0.
- 𝒦 = the joint kernel. This is exactly R9-9's target: linear constraints sourced by matter.

**Claims.** For every ψ ∈ 𝒦:
1. **Densities commute on 𝒦.** [ρ_x, ρ_y]ψ = [π_{x,i}, π_{y,j}]ψ = [ρ_x, π_{y,j}]ψ = 0.
   - *Proof.* [C_x, C_y] = κ²[ρ_x, ρ_y] and C_xC_yψ = C_yC_xψ = 0; the other pairs are the same. ∎
2. **Matter content is a joint eigenvector.** Resolve ψ along the joint spectral projectors P_s of {S_x}. Then (1⊗ρ_x)(P_s⊗1)ψ = κ^{−1}s_x(P_s⊗1)ψ. So every matter component of a physical state is a joint eigenvector of *all* local energy densities.
3. **The matter Hamiltonian moves no energy.** With H_m = Σρ_y, [H_m, ρ_x]ψ = 0. Whatever the gravity Hamiltonian is, matter's own Hamiltonian moves no energy in physical states.
   - This generalizes RN-L3's classical SK = −DG freezing, which used H_N's identity. F uses no property of the gravity Hamiltonian.

**Corollary F1 (proved).**
- Setting: free spinless fermions with ρ_x = ε n_x + ½(hopping bonds at x) on a connected graph of diameter ≥ 2, with t ≠ 0.
- Claim: there is no one-particle joint eigenvector of all ρ_x.
- *Proof.*
  - (ρ_x v)_y = −(t/2)v_x for y ~ x, and (ρ_x v)_z = 0 for d(x, z) ≥ 2.
  - Suppose v_x ≠ 0. Then λ_x ≠ 0 and every neighbour of x lies in supp v, so supp v is the whole graph.
  - A site z at distance ≥ 2 then forces λ_x v_z = 0. That is a contradiction. ∎

**Check (`r112_lemmaF.out`, `r112_lemmaF_2d.out`).**
- Joint-eigenvector dimension by particle number:
  - 1D ring, L = 6 and 8, site-symmetrized and bond-left densities: [1, 0, …, 0, 1];
  - 2D 3×3 torus, (ε, t) = (1, 1) and (0.3, 1): [1, 0, …, 0, 1].
- Control t = 0 (commuting on-site densities, no hopping, frozen): all 2^L states.

**Reading.**
- An exact linear-constraint sector sourced by matter's energy-momentum contains no mobile matter.
- The Schwinger term [ρ_x, ρ_y] ≠ 0 of any mobile matter is exactly the O(κ²) failure of the abelian linear constraint algebra (comparator: in the continuum {T⁰⁰(x), T⁰⁰(y)} ∝ (T⁰ⁱ(x) + T⁰ⁱ(y))∂_iδ, RECALLED).
- Its closure needs the field-dependent Dirac algebra of nonlinear gravity (O3, excluded here; cf. the 09-30 note). This is the linear-order lattice-quantum face of Marolf's "frozen bulk" (V).

### 6.2 Answer to (d)

- In exact linear-constraint realizations, matter can source the field in only two ways:
  - (i) as constraint violations, i.e. emergent defect charges. For integer-diagonal constraints these are integer-quantized: S(h)_x ∈ Z forces ρ_x ∈ κ^{−1}Z per cell, Planck-scale energy quanta for κ ~ ℓ_P (proved, for diagonal integer S);
  - (ii) at O(κ) only (tree level).
- **A universal, Ward-exact energy-momentum coupling to mobile matter exact to all orders is impossible in this class (Lemma F).** It needs O3.
- This sharpens lane R's failure mode ("an emergent charge rather than energy"). The emergent-charge outcome is forced, not merely likely, once the constraints are exact and linear.

## 7. Probe (e): prices (named, never adopted)

| Price | Axiom touched | What it buys |
|---|---|---|
| P-N1. Continuous canonical pairs (CCR, ℓ²(R)) on both h and E per slot, i.e. the supplied N-type graviton | Qubit (`AX:45-53`); S11's P41 | light-like TT at tree level (R9-9) |
| P-N1′. Rotor slots (ℓ²(Z)) on one side | Qubit | k² only (§4.3); not enough |
| P-N2. Instantaneous positive 1/r couplings between local curvature operators on both sides | Admissibility's nearest-neighbour rule (`AX:57-61`) | light-like TT. Marolf's kinematic non-locality |
| P-N3. A non-regular strong-coupling phase with both dressings | none named; an unbuilt mechanism | open |
| P-N4. A non-abelian, field-dependent constraint algebra at O(κ²), i.e. nonlinear gravity | the source/action gate (`AX:187`) | mobile matter in the sector (Lemma F) |
| P-N4′. Defect matter (quantized emergent charges) | none; fails universality and the energy scale | — |
| P-N5. For composite gravitons: no covariant stress for box matter | — | escapes WW's W2; not shown to exist |

## 8. Readings against the FIXED clauses (`TESTS:4147-4150`)

- **(a): SUGGESTED** (§3).
- **Overall: OPEN.**
  - **Not PRODUCED.** No ⊗M₂ model with light-like TT was built. The cheapest exact model gives k³; rotor slots give k².
  - **Not yet EXCLUDED.** No referee has seen this, and O1 to O6 remain open.
- **EXCLUDED candidates for the codex sol referee.** Each is a stated-class no-go.
  - **X1 (never light-like).**
    - Class: ⊗M₂, including quasi-local blocking to finite slots, with exact commuting bounded-support G and S stabilizers realizing the N-type linear algebra as a sector, whose sector Hamiltonian is H-regular and lifted after Lemma A_c averaging.
    - Claim: ω_TT = O(k³). Not light-like.
    - Ingredients: Lemma A_c (§4.1) plus N0914's theorem; the rotor extension (§4.3) gives O(k²).
    - Most of this is assembled prior art. The new parts are the commuting-scope repair of Lemma A, the dressing law, and class A.
  - **X2 (never couples to mobile energy-momentum).**
    - Class: any realization, any local dimension, whose physical sector is the exact joint kernel of linear constraints sourced by matter densities.
    - Claim: physical matter lies in joint eigenvectors of all local energy densities. For free hopping fermions that means only the empty and filled states (proved for one particle; checked many-body, 1D and 2D).
    - Caveat: X2 does not use ⊗M₂ at all. It constrains the registered target (exact linear constraints plus a Ward-exact universal stress) beyond O(κ).
- **Registration note (reading, for the supervisor).** By X2, the PRODUCED clause's conjunction can only be met at O(κ), as R9-9 met it. A future registration could ask for "tree-level Ward-exact coupling", or allow O3. This parallels R9-3's registration artefact. It does not change any reading here.

## 9. Against the registered expectation

- (a) SUGGESTED, as expected. Two corrections:
  - the rapidity budget is not where WW might fail for composites (Lemma K); W2 is;
  - "does not bind a gauge graviton" fails on exact finite-slot sectors (Lemma A_c gives a gauge-invariant local energy).
- (b)–(d) OPEN, as expected. The expected "k² or k³" is now a law, ω ∝ k^{3−n} with n the number of dressed sides. The expected "sourced by an emergent charge" is forced in the exact-linear class (Lemma F), not merely likely.

## 10. Strong-word check and scope

- **"Impossible"** is used only for X2's class (exact linear constraints sourced by matter densities, mobile matter beyond O(κ)), and there only via Lemma F. "Mobile" means some [ρ_x, ρ_y] ≠ 0 on the relevant states. F1 covers one density choice exactly and two choices numerically. Other improvement choices of ρ_x are not checked, though Lemma F's operator statement holds for any choice.
- **"Never light-like"** (X1) is bounded to exact, commuting, regular, lifted, finite-slot sectors.
- **"Exactly two TT modes"** in classes A, B and L is a Gaussian/symbol statement. No phase or gap is claimed (as `N0914:165-168`).
- **The dressing law** is exact on TT for the stated symbols. "Positive kernel needs a constraint" is suggested.
- **Lemma K** concerns kinematics only. Whether WW binds composites rests on W2, which is open.
- **No tail or decay clauses** were registered. The 1/r kernel in §4.2 is the full (−Δ)^{−1} with only the k = 0 mode removed (periodic boxes, as in `N0914:285`). No channel limit is subtracted.

## Files

- `scripts/r112_symbols.py` / `.out`:
  - §1: identities SV = 0, RV = 0, tr R = S, and K_N weak but not strong;
  - §2: the polynomial-system check (no O(1)/O(k) invariant characters);
  - §3: TT exponents for classes L, A, B, N (2.999, 2.000, 2.001, 1.001);
  - §4: the dressing identities.
- `scripts/r112_lemmaF.py` / `.out`: Lemma F, joint eigenvectors on 1D rings.
- `scripts/r112_lemmaF_2d.py` / `.out`: Lemma F on a 2D 3×3 torus.
- `scripts/r112_ww_kinematics.py` / `.out`: Lemma K.

Sources (web, this run): [Gu–Wen 0907.1203](https://arxiv.org/abs/0907.1203); [Marolf 1409.2509](https://arxiv.org/abs/1409.2509); [Jenkins 0904.0453](https://www.arxiv.org/abs/0904.0453).
