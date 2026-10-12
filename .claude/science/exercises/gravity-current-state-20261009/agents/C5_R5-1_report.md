# C5 R5-1: composite particles on an LRL realization

**Worker.** Claude Opus 5.5 (probe R5-1). Same model family as the supervisor and every C5 worker. **Not refereed.** Run 2026-10-12, 13:33Z to about 14:05Z. No repository file was edited.

**Scratch.** `scratchpad/C5/R5-1/`: this report, plus `scripts/`:
- `r51_stabilizers.py/.out`: which finite supports have infinite stabilizers (Lemma K). Exact membership checks, and a BFS ball of Γ.
- `r51_stab_offaxis.py/.out`: explicit loxodromic elements of Γ fixing an off-axis spacelike link and plane.
- `r51_diamond_link.py/.out`: Example D. Covariance at 60 digits; two-point decay; an independent lab-frame quadrature; Hermite weights.

**Read in full.**
- `docs/MINIMAL_AXIOMS_2026-06-29.md`.
- `TESTS.md:2302-2873`: C5 method, rounds 1–4 and their results, the R3-1 referee result, and R5-1 at `:2860-2873`.
- `agents/C5_R3-1_report.md` and `C5_R3-1_referee.md`.
- The R4-2 worker report, `scratchpad/C5/R4-2/R4-2_report.md` (unrefereed; its referee was still running at 13:34Z, with an empty `ref_R4-2/runner.out`).

**Read in part.**
- `agents/C5_R3-2_report.md` §§0–1 and 4–6, with `C5_R3-2_referee.md:1-130`.
- `agents/C5_O5_synthesis.md` §0.
- `SUMMARY.md` §§21–22.
- `PRICE_NOTE.md`, the v6 delta (`:251-413`).
- `scratchpad/C5/R4-3/R4-3_report.md` §§0–3.2 (Lemma Z).
- The R2-2 report and referee were used only through the refereed lines quoted in R3-1 and R3-2.

**Labels.**
- *proved*: a complete argument written here (same family, unrefereed).
- *proved mod RECALLED*: complete except for a named standard theorem.
- *checked*: computed in the scratch files.
- *suggested*: argued only.
- *reading*: an interpretation.
- *comparator*: an outside result.

**R4-2 claims used.** Only two R4-2 items enter, and both are re-proved here.
- The recurrence step of its Theorem S is re-derived inside Theorem W(iii).
- Its Corollary N a.c. part is the special case Δ = Γ of Theorem W(ii).

Example E/E′ (`R4-2_report.md:188-222`) is superseded by the explicit state-level Example D. Nothing here depends on R4-2's recalled Benoist–Quint/BFLM classification.

---

## 0. In plain words

**The question.** R4-2 found that on one LRL crystal, what a single site can do is frozen: it creates no particle. Can a multi-site object, such as a link between two events, a plaquette, or an orbit-smeared combination, carry a particle with a dispersion law and a momentum that boosts correctly? Or can a state that breaks the crystal's boost symmetry do it?

**Results.**
1. **Shape decides first.** A finite cluster of events is frozen exactly when infinitely many of the crystal's boosts leave it fixed. That happens when the cluster is a single event, or lies on a spacelike line or a spacelike plane. Such clusters create no particle of any mass. Their correlations live only along their own line or plane. Any boost-covariant momentum they carry is spacelike, so it is zero under positive energy (proved; checked).
   - Clusters with a timelike edge, or that span a spacelike 3-plane, have only finitely many such boosts. Symmetry alone puts no limit on them.
2. **A rule on events that depends continuously on its neighbours cannot depend on them at all.** Suppose the odds at an event are a continuous function of the surrounding records and respect the crystal's symmetry. Then they are the same whatever the neighbours are. The records are then independent from event to event, and nothing is correlated or propagates, composites included (proved).
   - This is the Admissibility axiom's own form ("varies with the nearest-neighbor conditions", `MINIMAL_AXIOMS_2026-06-29.md:61`).
   - So on LRL the axiom can hold only with a rule that depends on the far tails of the infinite neighbour families, not continuously on near ones.
3. **If all events' observables commute (as classical records do), every excitation's spectrum is time-symmetric.** Whatever a bounded object creates at positive frequency, its adjoint creates at negative frequency. A positive-energy particle of fixed mass then cannot be made by bounded objects (proved, under a stated spectrum hypothesis).
4. **A broken-symmetry state that picks a rest frame cannot be "restored in law."** The crystal's boosts move rest frames around without ever recurring. No probability mixture of frame-picking states, on one crystal or over the whole LRL ensemble, is boost-invariant (proved; it extends the Bombelli–Henson–Sorkin comparator to LRL with states).
5. **The escape exists, but only by supplying the continuum.** A link observable explicitly carries a mass-m particle with a decaying two-point function, a mass-shell dispersion and an exactly covariant, positive-energy momentum. It is the sign of a continuum free field smeared over the causal diamond between two timelike-separated events (Example D; checked: covariance to 1e-53, an independent frame check to 1e-14).
   - It escapes 1–4 in every way at once: the link has finitely many stabilizing boosts; its law is not a quasilocal rule on events; timelike links do not commute; its vacuum is invariant.
   - Its content is the continuum hyperboloid. The crystal supplies only labels. It is set A in lattice coordinates, as in R2-1 and R4-2's Example E.

**Reading: FAIL (bounded)**, pending the codex referee, in four stated classes (§6). The PASS wording is met only by Example D, which imports the continuum, so PASS is not claimed for LRL.

**What is left open.** The one class not closed: finite-dimensional degrees of freedom on timelike links, with non-commuting timelike structure and a Γ ⋉ L₇-covariant law that generates a mass shell. No such law is known.

---

## 1. Setting, hypotheses (stated before the titles), and exclusions

**Setting** (refereed: `C5_R3-1_referee.md:5-9`; `TESTS.md:2711-2718`).
- One realization X = L₇ = diag(√7,1,1,1)ℤ⁴. In lattice coordinates Q₇(n) = −7n₀² + n₁² + n₂² + n₃².
- Exact symmetry Γ ⋉ L₇, with Γ = SO⁺(Q₇,ℤ) cocompact and Q₇ anisotropic over ℚ (no null lattice vectors), so every nonzero Γ-orbit is infinite.
- Quasi-momenta p ∈ T⁴ = ℝ⁴/2πL₇*. Γ acts on T⁴ by β_γ.
- π: ℝ⁴ → T⁴ is the reduction. H_m^± are the mass shells (m > 0); C^± are the punctured null cones; Ω_m is the invariant measure.

**Hypotheses.** Each result names which it uses.
- **(U)** A unitary representation of Γ ⋉ L₇ on H, U(γ)T(a)U(γ)⁻¹ = T(γa), as R4-2 (U) (`R4-2_report.md:59`).
- **(V)** An invariant vacuum Ω. Site or cell operators transform geometrically.
- **(Dec/C)** For charges: P_μ decomposable over the translation spectrum with finite fibres a.e. and Γ-covariant (R4-2 (Dec), (C), `:60-63`). **(SC)** is the spectrum condition P ∈ V̄₊.
- **(SL)** Strict locality: a net of cell algebras A_ξ over a Γ ⋉ L₇-set of cells (events or links) with [A_ξ, A_ξ′] = 0 for ξ ≠ ξ′, including timelike-separated cells. Commutative record algebras satisfy it.
- **(Q)** A quasilocal law: the single-cell conditional law (or kernel) is a continuous function of the conditions in the product topology. This is the standard DLR requirement, met by every finite-range rule.

**Excluded (outside realizations).**
- continuum fields coupled to the point set, except where named as such (Example D);
- non-unitary or Krein implementations;
- curved realizations (R3-3);
- the gravity coupling itself (R4-2 §6);
- ensemble-only laws, except in Lemma H.

## 2. Prior art (each counted once)

- **R4-2 (unrefereed).**
  - Theorem S, Proposition I, Corollary N and Example E/E′ (`R4-2_report.md:97-222`).
  - Theorem W below is the extension of Proposition I(b) and Corollary N's a.c. part from W = 0 to every infinite stabilizer.
  - Example D is the state-level, bounded-observable form of E′.
- **R3-1 Lemma A / Lemma M** (refereed, `C5_R3-1_referee.md:5-9`): orbit-constant kernels, with no regular invariant symbol. Theorem Q is its many-body/specification analogue; the mechanism is the same.
- **O1 Lemma C′**: summable covariant laws are trivial (`C5_O1_report.md:120-141`).
- **E1/E1′**: link-propagated influence on sprinkled events (`TESTS.md:305-330`); Benincasa–Dowker kernels (`R3-1_report.md:130-134`).
- **Bombelli–Henson–Sorkin** (gr-qc/0605006) in the packet: `OUTSIDE_VIEW.md:48`; `B_referee.md:52`, which notes that it "does not prove the same statement for every Lorentz-invariant point process or a structure carrying additional marks/state". Lemma H is the LRL-with-states case.
- **Grep** of the packet for composite / link operator / de Finetti / monogamy / causal diamond: the hits are C3 M-D (composite centre-of-mass coherence on sprinkling links, `TESTS.md:577-614`) and C4 RM (composites on Z^d, `TESTS.md:1456-1476`). Neither concerns Γ-covariant cells.
- **Comparators (RECALLED).** Borel–Harish-Chandra (anisotropic ⇒ cocompact); Borel density; Selberg's lemma; B. H. Neumann's covering lemma; Halmos recurrence; Bochner–Herglotz; Wick/Hermite expansions for quasi-free states; the folklore result that commutativity at timelike separation plus the spectrum condition trivializes a Wightman field.

---

## 3. Lemma K: which supports are frozen (proved; checked)

**Statement.** Let S ∋ 0 be finite, W = span(S), and Γ_S the pointwise stabilizer. Then Γ_S is infinite iff W = 0, or W is a spacelike line, or W is a spacelike plane. It is finite iff W contains a timelike vector, or W is a spacelike 3-space.

**Proof.**
- Γ_S = Γ ∩ SO(W^⊥) acting trivially on W. W is rational and Q₇ is anisotropic, so W is nondegenerate and Q₇|W^⊥ is anisotropic over ℚ.
- **W spacelike line.** W^⊥ has signature (1,2), so Γ_S is a cocompact lattice in SO(1,2) (Borel–Harish-Chandra): infinite.
- **W spacelike plane.** W^⊥ has signature (1,1), so Γ_S is the norm-one unit group of a real quadratic order: infinite cyclic times finite.
- **W ∋ timelike vector.** W^⊥ is definite, so SO(W^⊥) is compact and Γ_S is finite.
- **W spacelike 3-space.** SO(W^⊥) is trivial on a timelike line. ∎

**Checked.**
- `r51_stabilizers.out:5-10`: counts in a BFS ball of 26,238 elements.
  - Growing counts: {0,e₁} 8 → 968; {0,e₁,e₂} 3 → 11 (linear, cyclic).
  - Saturated counts: {0,e₀} 24 (the exact signed permutations, `:1`); {0,(1,1,1,0)} 2; {0,e₀,e₁} 4; {0,e₁,e₂,e₃} 1; a generic 4-simplex 1.
- The axis ball does not reach the off-axis spacelike link (1,3,0,0), which shows a constant 4.
- `r51_stab_offaxis.out:1-2` therefore builds an explicit loxodromic element (Pell 15² − 14·4² = 1 on d^⊥; trace 32; integral; in SO⁺(Q₇,ℤ)) that fixes (1,3,0,0), and also fixes the plane span{(1,3,0,0), e₃}.

## 4. Theorem W: finite-dimensional families with an infinite stabilizer create nothing (proved)

**Statement.** Assume (U). Let Δ ⊂ Γ be infinite, and V ⊂ H a finite-dimensional U(Δ)-invariant subspace. Let ν_V = tr(P_V E(·) P_V); this is a finite Δ-invariant measure on T⁴. Then:
- **(i) No mass shell, of any mass.** ν_V has no component absolutely continuous with respect to π_*Ω_m^± (m > 0), nor with respect to π_*Ω_0 on C^±.
- **(ii) Correlations are confined.** For v, w ∈ V, the Haar-a.c. part of ⟨v, T(a)w⟩ vanishes unless a has a finite Δ-orbit. Such a lie in the fixed space of a loxodromic element, a spacelike sublattice of rank ≤ 2 (for Δ = Γ_S, exactly W ∩ L₇).
- **(iii) No physical charge.** Any (Dec/C) charge satisfies, ν_V-a.e., that τ(p) annihilates the axis plane of every loxodromic element of Δ. So τ(p) is spacelike or zero, and **(SC) forces P·V = 0**.

**Proof.**
- **Δ contains a loxodromic h.** By Selberg there is a torsion-free finite-index Γ₀; Δ ∩ Γ₀ is infinite. A cocompact lattice has no parabolics, and elliptics in a discrete group have finite order.
- **(i)** The Lebesgue decomposition of ν_V relative to the Γ-invariant σ-finite λ = π_*Ω_m^+ is Δ-equivariant, so ν_≪ = h_λ·λ with h_λ Δ-invariant.
  - Then ρ := h_λ∘π gives a finite ⟨h⟩-invariant measure ρΩ_m on H_m^+, since π_*((h_λ∘π)Ω) = h_λ·π_*Ω by change of variables; no injectivity of π is needed.
  - ⟨h⟩ acts properly on H_m^+ (a discrete subgroup acting on G/K), and also on C^+ minus h's two null axis rays (null coordinates scale by λ^{±k}).
  - Disjoint translates of a fundamental domain then give ρΩ = 0. The same holds for the other sheet and for m = 0.
- **(ii)** Write the a.c. density matrix as h(p), with h(β_γp) = ρ(γ)h(p)ρ(γ)*. Its norm truncations h_N stay equivariant.
  - The matrix coefficients of h_N span a ≤ (dim V)²-dimensional Δ-invariant subspace of L²(T⁴). Δ permutes the characters, so every element's Fourier support lies in finite Δ-orbits.
  - The bound used: m(a) = sup over the unit ball of |f̂(a)|² is Δ-invariant and summable.
  - Let N → ∞ in L¹. A finite-orbit a is fixed by a finite-index Δ′ ∋ loxodromic h′, and Fix(h′) ⊂ (axis plane)^⊥.
  - For Δ = Γ_S the Zariski closure is SO(W^⊥), whose fixed space is W.
- **(iii)** ν_V is ⟨h⟩-invariant and finite, so β_h is conservative ν_V-a.e.
  - R4-2's seminorm argument (`R4-2_report.md:106-116`) runs verbatim with ν_V in place of the conservative class: n_{β_h^k p}(e_±) = λ^{±k}n_p(e_±), and recurrence on A_R = {R⁻¹ ≤ n ≤ R} forces n_p(e_±) = 0.
  - The eigenvectors e_± of h are the null axis vectors. ∎

**Corollaries (proved).**
- **(W-a) Bounded supports.** For every S in Lemma K's infinite class, take V = A_SΩ (finite-dimensional for qubit sites, `MINIMAL_AXIOMS_2026-06-29.md:47`), or any finite Γ_S-stable family. This covers single sites (R4-2), spacelike links and spacelike planar plaquettes: no mass shell, correlations only along W, no positive-energy covariant charge.
- **(W-b) Orbit-smeared operators.** Any finite-variance Γ-covariant multiplet attached to a site (e.g. Σ_γ c(γ)O_{0,γd}) is covered with Δ = Γ. Smearing a link over its orbit to restore site covariance kills its particle content: the one-particle norm Σ_{γ,γ′}⟨F_{γd}, F_{γ′d}⟩ is infinite unless the orbit sum vanishes.
- **(W-c) Partially broken states.** If a state is invariant under L₇ ⋊ Δ with Δ ⊂ Γ infinite, on-site operators create no mass-shell content. So **on-site particles need the residual group at a site to be finite.** Then the state fixes a timelike direction or has no symmetry at all (any finite subgroup of SO⁺(1,3) fixes a timelike vector).

## 5. Three further no-gos and one explicit escape

### 5.1 Theorem Q: quasilocal covariant rules on events are condition-independent (proved)

**Statement.**
- Let Y be a compact metric space of single-event values. It may include "no record", and Γ may act on it through a compact group K.
- Let f(η) be any quasilocal, i.e. continuous, function of the conditions η ∈ Y^{L₇∖0} (or of the past cone only), valued in a metric space with an isometric K-action and Γ-equivariant: f(γη) = k(γ)f(η).
- Then f is constant (and K-invariant).
- So every quasilocal Γ ⋉ L₇-covariant specification or retarded formation kernel on events has single-site laws independent of the conditions. Its Gibbs measure is the i.i.d. product: no truncated correlation of any order, hence no composite with a dispersion. Its translation spectra are Haar-a.c., so by Theorem S there is no charge.

**Proof.**
- Let η, η′ differ on a finite set F′. By uniform continuity, choose a finite set F with |f(ξ) − f(ξ′)| < ε whenever ξ|_F = ξ′|_F.
- The set {γ : γF′ ∩ F ≠ ∅} is a finite union of cosets of the infinite-index subgroups Γ_x, x ∈ F′. By Neumann's lemma some γ avoids it.
- Then γη and γη′ agree on F, so |f(η) − f(η′)| = |f(γη) − f(γη′)| < ε. Hence f is constant on finite-modification classes, which are dense, so f is constant.
- The past cone of 0 is Γ-invariant with infinite orbits, so the retarded case is identical. ∎

**Quantum analogue (proved, sketch).**
- Under (SL), a Γ-invariant quasilocal operator in A_{L₇∖0} is a scalar: it is approximately in A_F and in A_{γF} with γF ∩ F = ∅.
- So every summable or quasilocal Γ ⋉ L₇-covariant interaction is on-site (R3-1 Lemma A, many-body form), and its β < ∞ KMS states are products.

**Price reading.**
- Admissibility on LRL cannot be both quasilocal and "vary with the conditions" (`MINIMAL_AXIOMS_2026-06-29.md:57-61`).
- R3-1's retarded orbit sums (`R3-1_report.md:117-134`) are non-quasilocal: changing far values changes the sum by a fixed amount. They are consistent with Q.

### 5.2 Proposition L: strict locality makes spectra time-symmetric (proved)

**Statement.**
- Assume (SL), translation invariance, and B ∈ A_F with F a finite set of cells. Then ν_B − R_*ν_{B*} (R: p ↦ −p) is Haar times a trigonometric polynomial with frequencies in F − F. So the singular parts satisfy ν_B^s = R_*ν_{B*}^s.
- Add **(SC_m)**: a charge with T(a) = e^{iP·a}, P ∈ V̄₊, and P² = −m² on the class [π_*Ω_m^±]. Then no bounded-support B creates mass-m content.

**Proof.**
- For a ∉ F − F, [B*, α_a(B)] = 0. So ∫e^{ip·a}dν_B = ω(B*α_a B) = ω(α_a(B)B*) = ∫e^{ip·a}d(R_*ν_{B*}).
- Mass-shell classes are Haar-null, and [π_*Ω_m^+] ⊥ [π_*Ω_m^−] (the overlaps are 2-surfaces).
- So B*Ω carries the reflected content on π(H_m^−). There P ∈ ι^−(p) + L₇* would need ι^−(p) ∈ H_m^+ − G: a null set. Contradiction. ∎

**Readings.**
- Commutative record algebras are in (SL). Their "particles" can only be classical both-frequency waves (as in D_cl below).
- A positive-energy particle needs non-commuting timelike structure: the unrecorded layer, consistent with O4's P4′ (`TESTS.md:2405-2412`).
- Prop. L uses only translations, so it also holds on Z⁴ spacetime-site models. (SC_m)'s "same mass on the reflected class" is a hypothesis: an equivariant Bragg shift with variable P² evades it.

### 5.3 Lemma H: frame-picking states cannot be restored in law (proved mod standard disintegration)

**Statement.**
- There is no Γ-invariant probability measure on the space of rest frames H³, nor on any Γ-space with a measurable equivariant map to H³.
- Hence a Γ-invariant state of one realization is never a mixture ∫ω_b dμ(b) over branches that measurably and equivariantly select a rest frame u_b.
- Likewise, no Lorentz-invariant-in-law LRL has per-realization states that select a frame. The conditional law given X must be Γ_X-invariant.
- Deterministic selection is impossible too: u(X) would be fixed by the infinite Γ_X, which contains loxodromics.

**Proof.** Γ acts properly on H³ with infinite orbits, so a finite invariant measure has every fundamental domain null. ∎

**Comparator.** Bombelli–Henson–Sorkin prove the Poisson case (`B_referee.md:52`); this is the LRL-with-states extension.

**Reading.**
- The "Γ-breaking state with restored-in-law symmetry" route is closed for every branch whose physics singles out a frame by a measurable covariant rule.
- Branches over a free probability-preserving Γ-space that define no frame are not excluded. But W-c then requires finite residual symmetry, and such branches' physics may not define a frame. That is the original problem without the symmetry.

### 5.4 Example D: the escape exists, with the continuum supplied (construction proved; checked)

**Cells.**
- Timelike links ℓ = (x, x+d), with x ∈ L₇ and d ∈ L₇ future-timelike.
- They form a Γ ⋉ L₇-set with finite stabilizers (Lemma K). Each event lies on infinitely many links.

**Profile.**
- Any Poincaré-covariant Schwartz profile f_ℓ(y) = f_d(y − x), with f_{Λd}(Λy) = f_d(y).
- Two choices:
  - the causal-diamond profile h(−(y−x)², −(x+d−y)²)·1_{D(x,x+d)}, smooth and compactly supported. Then links with spacelike-separated diamonds commute exactly (Pauli–Jordan support);
  - the rest-frame Gaussian exp(−E_u(y−x−d/2)/2σ²), with E_u(z) = 2(u·z)² + z². This one has a closed form and is used in the numerics.

**Theory.** The free field of mass m on Fock space over L²(H_m^+). U and T are second-quantized, and the vacuum is invariant.

**Observables.**
- Φ_ℓ = Φ(f_ℓ) has finite variance.
- **s_ℓ = sign(Φ_ℓ)** is a bounded ±1 link observable (a classical bit if the field is taken classical with Hadamard covariance; call that D_cl).

**Properties.**
- **Two-point function.** ⟨s_ℓ s_{ℓ+a}⟩ = Σ_{k odd} a_k² k! ρ_ℓ(a)^k, with ρ_ℓ(a) = W_d(a)/W_d(0) and W_d(a) = ∫dΩ_m |F_d|² e^{iq·a} (Wick/Hermite for a quasi-free state).
- **One-particle part.** The k = 1 term carries weight a₁² = 2/π of ‖s_ℓΩ‖² = 1. It is supported on π(H_m^+), and its charge is P = q:
  - multiplicity 1 a.e. (R4-2's lift, checked there to 60 digits);
  - exactly covariant;
  - unbounded;
  - positive-energy;
  - T(a) = e^{iP·a}.
- **Higher terms** sit on k-particle continua.
- **Consistency with Theorem S.** The one-particle class is boost-dissipative, so Theorem S does not apply.

**Checked** (`r51_diamond_link.out`; m = 0.5, σ = 1, lattice units).
- **(A)** F_{Λd}(Λq) = F_d(q), phase included, to a relative 9e-54 and 1.7e-53. The test used Λ ∈ {g₁, g₂, g₁R_zg₂⁻¹, g₂⁻¹g₁²}, d = e₀ and (1,1,1,0), and 6 random q each (`:1-3`).
- **(B) Decay with a dispersion.**
  - Timelike: |ρ|t^{3/2} → 5.01 at n₀ = 8 … 32 (massive dispersive decay; `:5-11`).
  - Spacelike: |ρ|e^{mr}r^{3/2} → 8.9 (`:12-18`).
  - The phase/(m t) column is a wrapped angle; ignore it.
- **Only finitely many Γ elements fix the link.** ρ_d(g₁a) ≠ ρ_d(a), e.g. 0.905 → −0.088 + 0.020i (`:19-22`).
- **(C) Independent check.** A 2D quadrature in the lab frame of W_{g₁d}(g₁a), at rapidity arccosh 8 = 2.77, equals the rest-frame W_d(a) to ≤ 1.5e-14 of W(0) at 5 separations (`:23-28`).
- **(D) Hermite weights.** a₁² = 2/π = 0.63662. The partial sums of Σa_k²k! reach 0.934 at k = 59, tending to 1 (`:29-37`).

**Reading.**
- D meets the wording of PASS for a bounded two-site observable.
- But the realization does no work: any Lorentz-covariant index set of timelike pairs would serve. The particle is the continuum's.
- This is set A in lattice coordinates, as R4-2 read E′ (`R4-2_report.md:219-222`) and R2-1 read its tower (`TESTS.md:2746-2748`).
- D sits outside every class in §6 at once:
  - finite stabilizer (W);
  - a non-quasilocal, continuum-defined law (Q);
  - not strictly local (L);
  - an invariant vacuum (H).

---

## 6. Against the FIXED readings (`TESTS.md:2870-2873`)

| Disjunct | Status |
|---|---|
| **PASS**: "an explicit composite (or symmetry-broken-state) excitation with a dispersion and a covariant charge, checked" | **Not claimed for LRL.** Its wording is met only by Example D (checked), whose substrate is the continuum free field supplied as data. No lattice law on L₇ is shown to produce it |
| **FAIL**: "a no-go for multi-site operators of bounded support, or for every Γ-breaking state, in a stated class (refereed)" | **Met by the worker in four stated classes, pending the referee:**<br>**𝔚** (Theorem W): every finite-dimensional family with infinite stabilizer. That is all bounded supports whose span is a point, a spacelike line or a spacelike plane, plus orbit-smeared site multiplets and states with infinite residual symmetry. No mass shell; positive-energy charge zero.<br>**𝔔** (Theorem Q): every bounded-support operator, of any shape, in states produced by a quasilocal Γ ⋉ L₇-covariant rule on events. Product measure.<br>**𝔏** (Prop. L + (SC_m)): every bounded-support operator in a strictly local net of cells.<br>**𝔋** (Lemma H): every Γ-breaking branch family that selects a rest frame, restored in law per realization or over the LRL ensemble |
| **INCONCLUSIVE** | This would be the reading if the referee judges 𝔚 ∪ 𝔔 ∪ 𝔏 ∪ 𝔋 too narrow, given that D escapes all four |

**Worker reading: FAIL (bounded to 𝔚 ∪ 𝔔 ∪ 𝔏 ∪ 𝔋)**, recordable only after the codex referee (`TESTS.md:2309`).

**Mandatory scope note.** The classes do not cover the following:
- finite-dimensional degrees of freedom on finite-stabilizer cells (timelike links, Lorentzian simplices, spacelike 3-simplices);
- with non-commuting timelike structure;
- under a Γ ⋉ L₇-covariant law, quasilocal on links or not, that generates a mass shell.

D shows this content is consistent at the state level once the continuum is supplied. Whether any LRL law generates it is **open**.

## 7. Strong-word check, and what needs the referee

- **Proved:** Lemma K; Theorem W (i)–(iii) and W-a/b/c; Theorem Q and its quantum sketch; Prop. L; Lemma H (mod disintegration); Example D's properties (standard free-field facts).
- **Proved mod RECALLED:** cocompactness and anisotropy (BHC), Borel density, Selberg, Neumann's lemma, Halmos recurrence.
- **Checked:**
  - the stabilizer counts and the explicit loxodromics (exact integers);
  - D's covariance (60 digits), decay, independent frame check, and Hermite weight.
- **Suggested:** that (SC_m)'s same-mass clause is natural; W-b's statement for general orbit smears (the norm argument is given only for one orbit family).
- **Reading:** "set A in lattice coordinates"; the price readings below.
- **"No-go"** is used only within 𝔚, 𝔔, 𝔏 and 𝔋. **"Exactly"** is used only for algebraic and representation identities.
- **Needs the codex referee:**
  - Theorem W(ii)–(iii), especially the use of a loxodromic element's axis in place of R4-2's three axis boosts;
  - Theorem Q, including its Neumann step and the claim that Admissibility's "varies with" fails for quasilocal rules on LRL;
  - Prop. L and the status of (SC_m);
  - Lemma H's disintegration step;
  - the class statement and the FAIL reading.

## 8. Price implications (named, none adopted)

For LRL as set B′/E′, beyond R3-1's unbounded-valency price (`R3-1_report.md:313-317`) and R4-2's §9:
- **(i) Cells (Qubit/Record/Lattice).** Particle-carrying degrees of freedom must live on finite-stabilizer cells, e.g. timelike pairs of events. Single events, and spacelike lines and planes, cannot carry them (W, Q).
  - This touches Qubit's "one-site possibility domain" (`MINIMAL_AXIOMS_2026-06-29.md:47`) and Record's one-record-per-site locking (`:77-82`).
  - Each event then belongs to infinitely many cells.
- **(ii) Admissibility.** On events, a covariant rule must be non-quasilocal: it depends only on tail data of infinite orbits (Q, `:57-61`). On link cells a quasilocal rule is not excluded.
- **(iii) Records versus particles.** If all cells commute (classical records), excitations are time-symmetric (L). The positive-energy particle must live in a non-commuting, unrecorded layer (reading, consistent with P4′).
- **(iv) No hidden frame.** A frame carried by the state cannot be averaged away on LRL (H). The X3 escape is a genuine preferred frame, i.e. a P11-type price (`PRICE_NOTE.md:365`).
- **(v) The only explicit realization** of (i)–(iii) is Example D: the continuum free field sampled on timelike links. So, as with R2-1 and R4-2, the escape collapses to set A unless an LRL law generating a mass shell on link cells is built.
