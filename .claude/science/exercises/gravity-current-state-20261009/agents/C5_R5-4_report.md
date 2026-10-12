# C5 R5-4: a law on timelike-link cells that generates a mass shell

**Worker.** Claude Opus 5.5 (probe R5-4). Same model family as the supervisor and every C5 worker. **Not refereed.** Run 2026-10-12, 14:04Z to about 14:33Z. No repository file was edited.

**Scratch.** `scratchpad/C5/R5-4/`: this report, plus `scripts/`:
- `r54_link_nbhd.py/.out`: Lemma N on L₇. Finite covariant link neighbourhoods; exact integer set equality under five elements of Γ.
- `r54_ergodic.py/.out`: an element of Γ whose toral action is ergodic (used in Theorem Δ).
- `r54_1p1_walk.py/.out`: the 1+1 analogue. (a) the phase identity; (b) two-term laws (Theorem T2); (c) a coined unitary link walk, with mismatch statistics at fixed mass.
- `r54_1p1_branches.py/.out`: the same walk. Masses at which ℓ² solutions exist, as a function of rapidity.
- `r54_1p1_lowmass.py/.out`: the same walk in the low-mass regime.

**Read in full.**
- `docs/MINIMAL_AXIOMS_2026-06-29.md`.
- `TESTS.md:2302-2981`: the C5 method, rounds 1–4 with results, R5-1 to R5-4, and the R5-1 refereed result at `:2968-2981`.
- The R5-1 worker report (`scratchpad/C5/R5-1/R5-1_report.md`), all of it.
- The verdicts `C5_R3-1_referee_verdict.md`, `C5_R4-1_referee_verdict.md`, `C5_R4-2_referee_verdict.md` and `C5_R4-3_referee_verdict.md`.
- `SUMMARY.md` §§21–22 (`:534-567`).

**Read in part.** `TESTS.md:300-335` (E1′) and `:569` (the C3 M-B referee); R5-1's `scripts/r51_stabilizers.py` (for the generators).

**Labels.**
- *proved*: a complete argument written here (same family, unrefereed).
- *proved mod RECALLED*: complete except for a named standard theorem.
- *checked*: computed in the scratch files.
- *suggested*: argued only.
- *reading*: an interpretation.
- *comparator*: an outside result.

**R5-1 items relied on, rechecked here.**
- Lemma K, timelike case: W ∋ timelike ⇒ W^⊥ is definite ⇒ Γ_S is finite. Re-derived in one line. `r51_stabilizers.out` shows the e₀ count saturating at 24.
- Example D's form. Re-derived as the necessary form in Lemma F below.
- R5-1 was refereed CONFIRMED WITH CORRECTIONS, FAIL bounded (`TESTS.md:2970-2981`). Its open class is this item's target (`:2981`).

---

## 0. In plain words

**The question.** On one crystal of the Lorentz-random lattice, put a few quantum degrees of freedom on each timelike link (a pair of events, one in the other's future). Can any rule that respects the crystal's symmetries make these links carry a particle of one fixed mass, without the continuum field being put in by hand?

**What was found.**
1. **Links, unlike events, can have local rules.** A timelike link fixes its own rest frame. So "the links within distance R in this link's own frame" is a finite neighbourhood, and it moves correctly under every symmetry. R5-1's Theorem Q made rules on events independent of their neighbours; on links that conclusion fails (proved; checked).
2. **Any particle the links carry must look like R5-1's Example D.** For a free (Gaussian) link field, a fixed-mass two-point function always has Example D's form. The only question is whether a local rule forces the form factor or it is put in by hand. Forcing it means the rule has a nonzero solution at every momentum on the mass shell (proved).
3. **A dichotomy (proved).** For any linear, local, symmetric link rule, the set S of crystal momenta with a normalizable solution has one of two forms:
   - **almost everything.** Then every mass works, and the rule picks no mass.
   - **almost nothing.** Then for almost every mass there is no particle. A mass shell can exist only at exceptional masses, and only if the whole 3-dimensional shell sits inside the null set S.
4. **Why that is hard: the crystal's symmetry ties almost nothing together.** In the continuum, Lorentz boosts carry any point of the shell to any other, so one condition covers the whole shell. On the crystal, the boosts relate only a discrete set of points. The shell splits into a 3-parameter continuum of unrelated pieces: the points of the compact space Γ∖H³. A rule with finitely many numbers must meet a condition at each of them (proved). Whether some rule manages this is open.
5. **In a 1+1-dimensional toy crystal it does not happen** for the two natural classes:
   - First-order rules: their solutions always grow at one end in rapidity (proved, modulo standard ergodic theorems; checked).
   - A coined quantum walk on links: normalizable solutions exist only along a tangle of mass branches that change with rapidity (period one crystal boost). That is a rapidity-dependent mass, not a shell. At masses below 5% of the inverse link length, one tested coin has none at all, and the other only a few, at rapidity-dependent masses (checked).
6. **No law with a mass shell was found, and no general no-go was proved.**

**Reading: INCONCLUSIVE** (§9). PASS is not met: no explicit link law with a mass shell. FAIL is not met: Theorem Δ is a dichotomy, not a no-go, and Theorem T2 is a no-go only in the 1+1 analogue, not on L₇.

---

## 1. Setting, hypotheses (stated before the titles), and exclusions

**Setting** (`TESTS.md:2949-2960`; R5-1 §1).
- One realization L₇ = diag(√7,1,1,1)ℤ⁴. In lattice coordinates Q₇(n) = −7n₀² + n₁² + n₂² + n₃², with bilinear form B = diag(−7,1,1,1).
- Γ = SO⁺(Q₇,ℤ) is cocompact; Q₇ is anisotropic.
- Quasi-momenta p ∈ T⁴ = ℝ⁴/Λ*, with Λ* = 2πℤ⁴ in these coordinates. β_γ = γ^{−T} acts on T⁴, and π: ℝ⁴ → T⁴ is the reduction.
- H_m^+ is the future mass shell (dual form), Ω_m its invariant measure, and Γ∖H_m^+ ≅ Γ∖H³ a compact hyperbolic 3-orbifold.

**Hypotheses.** Each result names which it uses.
- **(C) Cells.** C = L₇ × 𝒟, where 𝒟 is a finite union of Γ-orbits of cell shapes based at 0 with finite stabilizers Γ_δ. Examples: future-timelike link vectors, or Lorentzian simplices (Lemma K). Each cell carries ℂᵏ, with k finite.
- **(L) Linear covariant law.** (Kφ)(c) = Σ_{c′} K(c,c′)φ(c′) = 0, with K(gc, gc′) = ρ(g)K(c,c′)ρ(g)⁻¹ for g ∈ Γ⋉L₇ and ρ unitary. The law is banded: each cell couples to finitely many cells, and is coupled from finitely many. The band is uniform on orbits, which holds automatically for finite-range covariant laws over finitely many orbits.
- **(H3) Mass-shell family at mass m.** A measurable F: H_m^+ → (ℂᵏ)^𝒟 with these properties:
  - covariant up to a measurable phase cocycle: F_{γδ}(γq) = e^{iα(γ,q)}ρ(γ)F_δ(q);
  - finite variance per cell: ∫‖F_δ‖²dΩ_m < ∞;
  - nonzero;
  - the plane waves e^{iq·x}F_δ(q) solve the law for Ω_m-a.e. q.
- **(QF)** A Γ⋉L₇-invariant quasi-free state of the link field whose two-point function solves (L) in its second argument. Its one-particle translation spectrum is a.c. with respect to π_*Ω_m^+, with multiplicity one, or with finite multiplicity r.

**Excluded (outside realizations).**
- interacting (non-linear) link laws and spin-foam amplitudes (§8);
- laws with unbounded per-row coupling;
- massless shells (§6, remark);
- other L₇-type forms;
- curved realizations;
- ensemble-only laws (R5-5's subject);
- the gravity coupling.

## 2. Prior art (each counted once)

- **R5-1** (refereed CWC, `TESTS.md:2970-2981`): Lemma K, Theorem W, Theorem Q, Prop. L, Lemma H, Example D. Its open class is the target here. Theorem Q's referee note says Q bears on L₇, not on Admissibility as written (`:2977-2978`).
- **R4-2** (refereed, `C5_R4-2_referee_verdict.md`): Theorem S (conservative ⇒ no charge) and Example E. "Dissipative finite-fibre sectors are not excluded" (`:15`). The present fibres are dissipative (Lemma F(ii)).
- **R4-3 Lemma Z** (refereed, `C5_R4-3_referee_verdict.md:7,23`): null and spacelike orbits are dense. "Timelike automorphic branches remain unconstrained". Lemma O below is the timelike counterpart.
- **R3-1 Lemma M / R4-1** (refereed): event kernels are constant on infinite orbits, and finite-orbit retarded kernels have no per-realization □.
- **E1/E1′** (`TESTS.md:300-335`): influence along links on a Poisson sprinkling, with Johnston's path-sum propagator G_m = aL(I − abL)⁻¹. That is a chain sum over event links. On LRL the event version is R4-1/R5-2's object. The link-cell version here is the "transfer on links" candidate.
- **C3 M-B** (refereed, `TESTS.md:569`): finite event fibres cannot move amplitude. "Link (arc) states", "an arc unitary" and "a massive mean" are left open there. This report addresses the LRL arc/link unitary in a stated linear class.
- **Repository quantum walks** (`docs/CHIRAL_WALK_SYNTHESIS_2026-04-09.md` and others found by grep): all on Z^d, none on Γ-covariant cells. Counted, not used.
- **Comparators (RECALLED).**
  - Halmos's ergodicity criterion for toral automorphisms; Birkhoff; Livšic; the CLT/LIL for Hölder observables of hyperbolic toral automorphisms; Fubini in a linear flow box.
  - Bourgain–Schlag (2000), Anderson localization for potentials driven by hyperbolic toral automorphisms: background for the coined walk only.
  - Jensen's formula and the Mahler measure.
  - Mackey duality for conservativity; Halmos recurrence.

---

## 3. Lemma N: timelike links admit finite covariant neighbourhoods (proved; checked)

**Statement.**
- For a future-timelike d ∈ L₇, define E_d(z) = 2B(d,z)²/(−Q₇(d)) + Q₇(z). This is the rest-frame Euclidean norm in the frame u = d/√(−Q₇(d)). It is positive definite, and E_{gd}(gz) = E_d(z) for every g ∈ SO(Q₇).
- Then N_R(x,d) = {(x+a, d′) : E_d(a) ≤ R², E_d(d′−d) ≤ R², d′ in a fixed set of shells, d′₀ > 0} is finite.
- It is covariant: gN_R(ℓ) = N_R(gℓ) for g ∈ Γ⋉L₇.
- Hence finite-range, Γ⋉L₇-covariant specifications on link cells whose single-link law depends on the neighbours exist. One example is any Ising-type rule on N_R.
- R5-1's Theorem Q (`R5-1_report.md:146-166`) does not extend to links. Its Neumann step needs the base cell to have an infinite stabilizer. A link's stabilizer is finite (Lemma K), so covariance constrains the single-link law only by a finite group.

**Proof.** E_d is the Minkowski form plus twice the squared u-component, which is positive definite. Covariance follows from B(gd,gz) = B(d,z). Finiteness holds because a positive-definite quadratic form has finitely many lattice points below R². ∎

**Checked** (`r54_link_nbhd.out:1-7`).
- With R² = 6, |N_R| = 81 for e₀.
- For g ∈ {B₁, B₂⁻¹, B₁RB₂⁻¹, B₃B₁, RB₂R}, the neighbourhood of g·e₀ was enumerated independently. Examples: g·e₀ = (8,21,0,0) and (64,21,0,168), with bounding boxes up to [83,27,2,219].
- In every case the set is exactly g·N_R(e₀).
- The link (2,4,2,1), on the same shell, has 4 distinct d′.

**Reading.** On links, the "quasilocal where possible" clause of R5-4 can be met exactly. Locality is not the obstruction.

## 4. Lemma F: what a link law must force (proved)

**Statement.** Assume (C), (L).

**(i) Example D's form is necessary.** Under (QF) with multiplicity r:
- W((x,δ),(x′,δ′)) = ∫_{H_m^+} dΩ_m(q) Σ_{α≤r} F^α_δ(q)^* F^α_{δ′}(q) e^{iq·(x′−x)}.
- Each F^α satisfies (H3).
- So R5-1's Example D (`R5-1_report.md:200-245`) is the general form. The only freedom is the form factor F_{δ₀} on H_m^+, up to the finite stabilizer.

**(ii) ℓ² fibres.** Let F satisfy (H3) with m > 0. Then for Ω_m-a.e. q:
- F(q) := (F_δ(q))_{δ∈𝒟} ∈ ℓ²(𝒟, ℂᵏ);
- K(πq)F(q) = 0, where (K(p)v)_δ = Σ_{(a,δ′)} K((0,δ),(a,δ′)) e^{ip·a} v_{δ′} is the fibre operator. It is bounded on ℓ²(𝒟,ℂᵏ) uniformly in p (Schur), and strongly continuous in p.

**(iii) Conversely,** any (H3) family yields a quasi-free covariant state with a multiplicity-one mass-shell spectrum. This is Fock space over L²(H_m^+), with the covariant, positive-energy, unbounded charge P = q, exactly as in Example D and R4-2's Example E. Positivity is automatic, and the law is solved by construction.

**Proof.**
- **(i)** W is a positive-definite, L₇-translation-invariant matrix kernel on 𝒟. Bochner/SNAG on T⁴ gives a positive matrix measure M_{δδ′}. By hypothesis M ≪ π_*Ω_m^+.
  - π restricted to H_m^+ is injective off the Ω-null set ∪_{G≠0}{q : q+G ∈ H_m^+}. For fixed G each piece is a hyperplane section of H, so it has dimension 2.
  - Lift M to H_m^+ and take the rank-r factorization of its density. That gives the F^α.
  - "W solves (L) in its second argument" becomes K(πq)F^α(q) = 0, Ω-a.e.
  - Covariance of the state makes the factorization covariant up to a unitary cocycle, which is a phase for r = 1.
- **(ii)** Let 𝔉 be a fundamental domain of the proper Γ-action on H_m^+. Then
  ∫_𝔉 Σ_δ‖F_δ‖² dΩ = Σ_i |Γ_{δᵢ}|⁻¹ ∫_{H_m^+}‖F_{δᵢ}‖² dΩ < ∞.
  So the sum is finite a.e. on 𝔉, and by invariance a.e. on H_m^+. This uses dissipativity: Γ acts properly on H³.
  - The plane-wave condition at the cell (0,δ) is exactly (K(πq)F(q))_δ = 0.
  - Boundedness: the row and column counts are constant on orbits.
- **(iii)** This is standard second quantization, as in R5-1 §5.4. ∎

**Reading.** "Without supplying a continuum field as data" can therefore only mean one thing. The shell and the form factor must be forced by K: S ⊇ π(H_m^+) a.e., with F a selection from the kernel. Here S = {p : ker_{ℓ²}K(p) ≠ 0}. Example D fails this: its form factor (a diamond or Gaussian profile) solves no banded equation. That is suggested, not proved: finite exponential sums restricted to H_m^+ are linearly independent.

## 5. Theorem Δ: the dichotomy (proved)

**Statement.** Assume (C), (L). Then S = {p ∈ T⁴ : ker_{ℓ²(𝒟,ℂᵏ)} K(p) ≠ 0} is a Borel, Γ-invariant set, and exactly one of the following holds.
- **(Δ1) S is Haar-conull.** Then for Lebesgue-a.e. m > 0 an (H3) family exists. The law admits almost every mass and selects none.
- **(Δ2) S is Haar-null.** Then the set M_K = {m > 0 : (H3) holds at m} is Lebesgue-null. At each m ∈ M_K, a positive-Ω_m-measure Γ-invariant part of H_m^+ maps into the null set S, and for a full shell, Ω_m-almost all of it.

**Proof.**
- **Borel.** p ↦ K(p) is a uniformly bounded, strongly continuous family, and so is K(p)*. Let E₀(p) be the spectral projection of K(p)*K(p) at 0: the strong limit of f_n(K*K) for continuous f_n ↓ 1_{0}.
  - Each p ↦ ⟨e_j, E₀(p)e_j⟩ is Borel, and S = ∪_j{⟨e_j,E₀(p)e_j⟩ > 0}.
- **Invariance.** U_γK(p)U_γ⁻¹ = K(β_γp), where U_γ permutes 𝒟 and applies ρ.
- **Ergodicity.** γ = B₁B₂B₃ ∈ Γ has characteristic polynomial x⁴ − 536x³ + 384x² − 536x + 1. This is irreducible and not cyclotomic, so no eigenvalue of γ or γ^{−T} is a root of unity, and the toral automorphism is Haar-ergodic (Halmos; `r54_ergodic.out:7-9`).
  - So a Γ-invariant Borel set is null or conull.
- **(Δ2).** Ψ(m,u) = π(mu) is a local diffeomorphism from (0,∞)×H³ onto its image in T⁴, and d⁴q = m³dm dΩ₁. So Ψ⁻¹(S) is null.
  - By Fubini, for a.e. m, {u : π(mu) ∈ S} is Ω-null.
  - (H3) at m needs π(q) ∈ S on the support of F (Lemma F(ii)), which has positive measure. Hence M_K is null.
- **(Δ1).** The same Fubini step gives Ω-a.e. shell points in S for a.e. m.
  - Choose kernel vectors Borel-measurably on a fundamental domain 𝔉: v(q) = E₀(πq)e_{j(q)}/‖·‖, with j(q) the first index with nonzero image.
  - Weight them by w ∈ L²(𝔉), w > 0, and extend by F(γq) = U_γF(q). This is consistent off the null set of points with nontrivial stabilizer.
  - Kernel membership is preserved by the intertwining. Finite variance holds per cell: for each orbit representative δᵢ, ∫_{H_m^+}‖F_{δᵢ}‖²dΩ = |Γ_{δᵢ}| ∫_𝔉 Σ_{δ∈Γδᵢ}‖F_δ‖² dΩ ≤ |Γ_{δᵢ}| ∫_𝔉 w² < ∞. ∎

**Readings.**
- (Δ1) is not a mass shell generated by the law: the law is satisfied on every shell, and the mass must be supplied.
- In (Δ2), mass selection is possible only at exceptional masses whose entire shell lies in a Γ-invariant Haar-null set.
- In the continuum the same structure is automatic: the Klein–Gordon S is a union of shells because SO⁺(1,3) acts transitively on each shell. Section 6 shows what LRL lacks.

## 6. Lemma O: on LRL a mass shell is a 3-parameter family of unrelated conditions (proved)

**Statement.**
- For Ω_m-a.e. q ∈ H_m^+, the shell points equivalent to q under the problem's symmetries, {q′ ∈ H_m^+ : π(q′) ∈ Γ·π(q)}, are exactly the orbit Γq. This orbit is discrete in H_m^+.
- So the conditions "π(q) ∈ S" for q in a fundamental domain 𝔉 are indexed by the compact 3-orbifold Γ∖H³, which has positive volume, and no element of Γ⋉L₇ identifies any two of them.
- In particular, Γ-covariance of K gives no relation between the shell conditions at two points of 𝔉.

**Proof.**
- π(q′) = β_γπ(q) iff q′ − γq ∈ Λ*.
- For fixed (γ, G ≠ 0), the set of q with γq + G ∈ H_m^+ is γ⁻¹ of a hyperplane section {q″ ∈ H : 2q″·G + G² = 0} (Minkowski product), so it is 2-dimensional and Ω-null.
- The union over countably many (γ,G) is null.
- Translations act trivially on momenta. ∎

**Reading / suggested.**
- A banded covariant law has finitely many coupling constants. An exact shell needs the kernel condition to hold on a 3-parameter family that the symmetry leaves unrelated.
- A generic covariant link law should instead produce a mass that depends on the rapidity relative to the crystal, m_*(u) with u ∈ Γ∖H³. That is the "timelike automorphic branch" R4-3's referee left unconstrained (`C5_R4-3_referee_verdict.md:7`).
- That generic laws do this is **suggested** for L₇ and **checked** only in the 1+1 analogue (§7).

**Remark (massless shells, outside Δ).**
- On C^+ the Γ action is conservative and ergodic: Mackey duality with the null-vector stabilizer acting on finite-volume Γ∖G, plus Moore (RECALLED).
- So for any covariant finite-variance family, Halmos recurrence gives Σ_δ‖F_δ(q)‖² = ∞ a.e. on its support. Massless solutions are never ℓ² in the fibre, and Theorem Δ does not apply. *proved mod RECALLED*.
- Lemma Z's density of null orbits (refereed) suggests that continuity could collapse the conditions there. Not pursued.

## 7. The 1+1 analogue (an analogue only; it differs from L₇ in Γ ≅ ℤ abelian and in trivial stabilizers of every nonzero vector)

**Setting.**
- L^{(k)} = diag(√k,1)ℤ², with Q = −kn₀² + n₁².
- k = 3, g = [[2,1],[3,2]], η₀ = arccosh 2.
- k = 7, g = [[8,3],[21,8]], η₀ = arccosh 8: the L₇ boost of R5-1.
- Links (x, d_n) with d_n = gⁿe₀.
- On H_m^+: q·d_n = −√k m cosh(θ − nη₀). Checked to 1e-79 (`r54_1p1_walk.out:1-2`).
- A banded covariant law reduces to a recurrence in n with coefficients A_j(βⁿp). Here A_j are trigonometric polynomials on T², and β is the dual action of g on T², a hyperbolic toral automorphism (a cat map), since q·(gⁿa) = ((gⁿ)ᵀq)·a. *proved*: the same covariance reduction as Lemma F.

### 7.1 Theorem T2: first-order (two-term) scalar laws give no shell at any mass (proved mod RECALLED)

**Statement.**
- Take a law A₀(βⁿp)f_n + A₁(βⁿp)f_{n+1} = 0 with A₀, A₁ trigonometric polynomials that vanish nowhere on T².
- Then for every m > 0, for a.e. θ, the solution through any f₀ ≠ 0 is not in ℓ²(ℤ).
- Hence (H3) fails at every mass.

**Proof.**
- h = log|A₁/A₀| is real-analytic.
- The forward Birkhoff averages of h converge to ∫h on a full-measure set. That set is saturated by stable leaves, since differences along stable leaves are summable.
- The backward averages converge on a full-measure set saturated by unstable leaves.
- The shell curve θ ↦ π(q_m(θ)) is transverse to both linear foliations: its tangent is non-null, and the eigenlines of β are null. By Fubini in a linear flow box, a.e. θ lies in both sets.
- Then log|f_n/f₀| = −S_n(h) and log|f_{−n}/f₀| = +S_{−n}(h), and ∫h = m(A₁) − m(A₀) (Mahler measures).
  - If ∫h ≠ 0, one tail grows exponentially.
  - If ∫h = 0 and h is a coboundary (Livšic: h = u − u∘β with u continuous), S_n is bounded and |f_n| stays bounded below.
  - Otherwise σ² > 0, and the LIL gives liminf S_n = −∞ a.e. So |f_n| = |f₀|e^{−S_n} is unbounded. The LIL set is leaf-saturated, because S_n changes by a bounded amount along stable leaves.
- In no case is f in ℓ². ∎

**Checked** (`r54_1p1_walk.out:3-12`, N = 60, 80-digit phases). For c = (1, 0.9, 0.5) and the vectors a = (0,1), b = (1,1):
- the forward exponents are 0.06–0.20, against Jensen's χ = 0.105;
- χ₊ + χ₋ is in [−0.04, 0.13], consistent with 0 within sampling noise of about 0.07;
- the backward exponents are negative, so |f_{−N}| decays and |f_N| grows.

**Reading.** In 1+1 the "time-symmetric growth" is forced by the Galois symmetry of the phases. Mahler measure is invariant under z₁ → z₁⁻¹, which exchanges the two null ends.

### 7.2 Coined unitary link walk (checked)

**The model.**
- (Wψ)_n = e^{−iφ_n}[P₊Cψ_{n−1} + P₋Cψ_{n+1}], with φ_n = q·d_n and C a rotation by ζ.
- The law φ = Wφ has an SU(1,1) transfer matrix T_n = c⁻¹[[e^{−iφ_n}, −s],[−s, e^{iφ_n}]] (derived in the script docstring).
- Both decaying directions lie on the invariant circle |z| = 1 (checked: ||z|−1| = 0 to print precision, `r54_1p1_walk.out:14-26`).
- So "an ℓ² solution exists" is the vanishing of one real mismatch angle. This is the codimension-1 condition a shell needs.

**Results.**
- **Covariance is exact.** The mismatch at θ+η₀, evaluated at the shifted site, equals the value at θ to 1e-55 to 1e-81 (`:17,20,24,27`).
- **At fixed m, the zeros in θ are isolated.**
  - The fraction with |mismatch| < ε falls roughly linearly in ε. Example: at m = 0.5, N = 34 with 600 rapidities, the fractions are 0.070, 0.022, 0.010, 0.002 for ε = 0.3, 0.1, 0.03, 0.01 (`:26`).
  - The crossing count grows from 30 to 70 when the grid is refined from 240 to 600 points (`:15` vs `:26`). The mismatch is rough in θ.
  - No tested mass has an exact shell: m = 0.2, 0.5, 1.0 at k = 3, and m = 0.2, 0.5 at k = 7.
- **Where the ℓ² solutions are** (`r54_1p1_branches.out`, ζ = 1.2, m ∈ (0.02, 1.0), 1200-point grid, 30-step bisection):
  - At each rapidity there are 16–31 ℓ² masses.
  - The lowest one varies from 0.082 to 0.290 across θ ∈ [0, η₀) (`:29`).
  - The lists at θ and θ+η₀ are identical (`:2` vs `:26`, and `:27` vs `:28`), as Γ requires.
  - The ℓ² set is a tangle of Γ-periodic branches m_j(θ), none of them constant. This is a rapidity-dependent mass.
- **Low-mass regime** (`r54_1p1_lowmass.out`, m ∈ [1e-4, 5e-2]):
  - For ζ = 1.2 there are no ℓ² solutions at any of 12 rapidities. The mismatch stays near π (median 3.13), because eigenvalue 1 lies in the spectral gap of the bare walk (cos ω = c cos k).
  - For ζ = 0.6 there are 2–14 sparse crossings per rapidity, at θ-dependent masses: the lowest is 3.5e-3 to 3.0e-2.

**Reading.**
- In the analogue, the natural walk produces only Planck-scale, rapidity-dependent "gap states". It produces no low-mass shell.
- That a walk whose bare band contains eigenvalue 1 would do better is **suggested against**, not tested. Anderson localization from the far, wildly varying phases would again give codimension-1 tangles.

## 8. The three named candidates

| Candidate (`TESTS.md:2952-2955`) | Status |
|---|---|
| Quantum walk / transfer matrix on links | Linear: Theorem Δ applies to K = 1 − W. 1+1 analogue: first-order walks never give a shell (T2, proved); a coined unitary walk gives rapidity-dependent masses, not a shell (checked). No L₇ walk was computed: the fibre is the non-amenable Γ/Γ_d, and ball truncations are dominated by boundary |
| Gaussian link field with covariant couplings | Lemma F(i) makes (H3) necessary; Theorem Δ and Lemma O then apply. Not found |
| Link "spin foam" amplitude | Outside the proved classes (non-linear). With finite-dimensional link spaces, covariance acts only through the finite stabilizers. EPRL-type models carry infinite-dimensional unitary SL(2,ℂ) representations, i.e. continuum group data (comparator / reading) |

Classical (commuting) link Gibbs measures exist by Lemma N, and are correlated in the Dobrushin regime (suggested). Prop. L (refereed with the (SC_m) caveat, `TESTS.md:2979`) then excludes fixed-mass positive-energy content only under (SC_m).

## 9. Against the FIXED readings (`TESTS.md:2958-2960`)

| Disjunct | Status |
|---|---|
| **PASS**: "an explicit link law, not continuum-supplied, with a mass shell and a covariant charge, checked" | **Not met.** No banded covariant link law with S ⊇ π(H_m^+) was found. Lemma F(iii) shows that such a law would automatically give the charge (P = q, covariant, positive-energy) via Example D's construction |
| **FAIL**: "a no-go covering quasilocal covariant link laws in a stated class (refereed)" | **Not met on L₇.** Theorem Δ is a dichotomy, not a no-go: (Δ2) leaves a null set of exceptional masses open. Theorem T2 is a no-go in the 1+1 analogue only (first-order scalar laws, nowhere-vanishing coefficients). If the referee wants a recordable bounded FAIL, the honest scope is "1+1 analogue, two-term scalar laws", which is not R5-4's class |
| **INCONCLUSIVE** | **Worker reading.** Proved on L₇: Lemmas N, F, O and Theorem Δ. Exact shells need exceptional masses whose 3-parameter family of Γ-unrelated points all lie in a Γ-invariant Haar-null set. In the 1+1 analogue the natural laws do not achieve this |

**What would settle it.**
- **(i) For FAIL.** Prove that for every banded covariant K on L₇ link cells, S ∩ π(H_m^+) is Ω-null for every m, not just a.e. m. This is the L₇ form of T2. It needs Oseledets-type control for Γ-cocycles over the non-amenable fibre, plus transversality of the shell to the stable structure.
- **(ii) For PASS.** Construct an exactly solvable K: a banded covariant intertwiner from link fields onto L²(H_m^+).

## 10. Strong-word check, and what needs the referee

- **Proved:** Lemma N; Lemma F (i)–(iii); Theorem Δ (Borel, invariance, (Δ1), (Δ2)); Lemma O; the 1+1 covariance reduction.
- **Proved mod RECALLED:**
  - Theorem T2 (Birkhoff, Livšic, LIL, linear flow-box Fubini);
  - the ergodicity step (Halmos's criterion);
  - the massless remark (Mackey duality, Moore, Halmos recurrence).
- **Checked:**
  - Lemma N's set equalities (exact integers);
  - the irreducible non-cyclotomic polynomial;
  - the phase identity;
  - the T2 exponents;
  - the walk's invariant circle and exact Γ-covariance;
  - the fixed-mass ε-scaling and the rapidity dependence of the ℓ² masses;
  - the low-mass absence.
- **Suggested:**
  - that generic L₇ laws give rapidity-dependent masses m_*(u);
  - that Example D's profiles solve no banded equation;
  - that in-band walks would also give tangles;
  - Dobrushin correlations for link Gibbs measures.
- **Reading:** "not continuum-supplied" read as "S ⊇ π(H_m^+) forced by K"; the price readings in §11.
- **Strong words.**
  - "No-go" is used only for T2, in the 1+1 analogue.
  - "Exactly" is used for algebraic identities and for the covariance checks.
  - "Never" (massless ℓ²) is used within its stated hypotheses only.
- **Needs the codex referee:**
  - Theorem Δ: the Borel step, the ergodicity element, and the measurable covariant selection in (Δ1);
  - Lemma F(i)'s factorization and cocycle;
  - Lemma O's null-set argument;
  - T2's leaf-saturation and transversality steps;
  - whether INCONCLUSIVE, rather than a bounded FAIL, is the right reading.

## 11. Price implications (named, none adopted)

- **(i)** Lemma N removes R5-1's locality price for link cells. On links, a quasilocal covariant rule whose odds vary with the neighbours exists. The Admissibility-form clause "varies with the nearest-neighbor conditions" (`MINIMAL_AXIOMS_2026-06-29.md:61`) is satisfiable on L₇ link cells, though not on L₇ events (R5-1 Q).
  - Using link cells still re-prices Qubit (`:47`, one domain per site) and Record (`:77-82`, one record per site): each event lies in infinitely many cells (R5-1 §8(i)).
- **(ii)** If no banded link law has exact shells, LRL matter faces three options:
  - (a) continuum-supplied form factors: set A in lattice coordinates, as in R2-1, R4-2 and R5-1;
  - (b) accept a rapidity-dependent per-realization mass m_*(u) on Γ∖H³. That is a timelike Lorentz violation whose size at physical masses is not computed here; in the analogue it is O(1) and rough at Planck masses, and at low mass either absent or sparse and rapidity-dependent;
  - (c) an interacting or non-linear mechanism outside Δ.
- **(iii)** Lemma O is the precise sense in which a lattice subgroup Γ cannot protect a mass shell the way SO⁺(1,3) does. The shell's points mod Γ form a compact 3-manifold of unrelated conditions. This is the timelike counterpart of R4-3's Lemma Z, where null orbits are dense and continuity does the work.
