# C5 R4-2: singular finite-fibre multipliers on a Lorentz-random-lattice (LRL) realization

**Worker.** Claude Opus 5.5 (probe R4-2). This is the same model family as the supervisor and every C5 worker. **Not refereed.** Run 2026-10-12, 13:08Z to about 13:32Z. No repository file was edited.

**Scratch.** `scratchpad/C5/R4-2/`: this report, plus `scripts/`:
- `r42_algebra.py/.out`: the exact group inputs of Theorem S, and Lemma G for the vector representation;
- `r42_sym2_gram.py/.out`: Lemma G for a site stress tensor (Sym² of the vector representation);
- `r42_shell_lift.py/.out`: Example E, the escape (60-digit checks);
- `r42_posdef.py/.out`: an illustration of Corollary N.

**Read in full.**
- `docs/MINIMAL_AXIOMS_2026-06-29.md`.
- `TESTS.md:2302-2851`: C5 method and readings, round 1 and its results, round 2 and its results plus the R2-1 addendum, round 3 and its results, and round 4. R4-2 is at `:2806-2813`.
- `agents/C5_O5_synthesis.md`: §0 and set B (§2.2).
- `SUMMARY.md` §§15–21.
- `PRICE_NOTE.md`: P10–P14 rows and the v6 delta.
- The cited inputs:
  - `agents/C5_R3-2_report.md` and `agents/C5_R3-2_referee.md` (with its verdict), plus the referee's `NO_GO_DISCIPLINE_CHECKLIST.md` in `scratchpad/C5/ref_R3-2/`;
  - `agents/C5_R2-1_report.md` and `agents/C5_R2-1_referee.md` (with its verdict);
  - `agents/C5_R3-1_report.md`, whose referee verdict (CWC) arrived during this run: `scratchpad/C5/ref_R3-1/REFEREE_VERDICT.md`;
  - `agents/C4_I1_referee.md`.

**Labels.**
- *proved*: a complete argument is written here (same family, unrefereed).
- *checked*: exact or numerical, in the scratch files.
- *suggested*: argued only.
- *reading*: an interpretation.
- *comparator* or *RECALLED*: an outside standard result.

---

## 0. In plain words

- **The question.** Gravity needs the matter's "momentum charge" to grow without limit under boosts. R3-2 proved that no *bounded* charge can do this on an LRL realization. Its referee left one door open: a charge that is unbounded but still finite at each quasi-momentum, i.e. a singular multiplier on a finite fibre (`C5_R3-2_referee.md:107-115`).
- **The door is shut wherever the momentum space recurs.** We prove this with no regularity assumption at all: any measurable multiplier, however singular. Suppose the boosts keep bringing quasi-momenta back near where they started, as they do for any one-particle space with a finite invariant measure (conservative dynamics). Then every boost-covariant four-vector charge with finite fibres is zero.
  - This covers every subspace of ℓ²(L₇) ⊗ C^N, which is T_Γ's own setting.
  - It also covers every one-particle state that finitely many on-site fields of finite variance can create from an invariant vacuum.
  - Under the Qubit axiom every on-site operator is a 2 × 2 matrix, so finite variance is automatic (Theorem S, Proposition I).
- **A second result, stronger than asked: on-site fields cannot carry a propagating particle at all.** On one LRL realization with an exactly invariant vacuum, the two-point function of any finite-variance on-site observable is a spike at zero separation plus, at most, a non-decaying almost-periodic part. That part is "conservative singular"; it is purely periodic given a recalled classification theorem. There is no dispersion relation (Corollary N).
  - A Lorentz-tensor site field, the stress tensor's spin-2 part included, cannot create anything from the vacuum (Lemma G).
- **Where the door is open.** It is open only on one-particle spaces where the boosts carry momenta off to infinity, as on the continuum mass hyperboloid. We build such a representation explicitly (Example E):
  - one state per quasi-momentum (finite fibre, multiplicity 1);
  - an exactly covariant, unbounded, nowhere-continuous momentum charge.

  But its particles are invisible to every finite-variance on-site field. The only way to make them is with infinite-variance point values or with multi-site (link) variables, and each site then has infinitely many links. Its content is the continuum hyperboloid embedded in the momentum torus. It is set A again, in lattice coordinates.
- **Nothing here builds a lattice *law* with an exact gauge identity.** So there is no PASS.
- **Reading: FAIL (bounded)**, with a sharp class, pending the codex referee. Scope warning: the class contains no propagating particle. For propagating matter the question moves to whether a lattice law can make particles that no on-site variable creates. That is open.

---

## 1. Hypotheses, stated before the titles, and the scope's exclusions

**Setting** (as refereed in R2-2 and R3-1).
- One realization is X = L₇ = diag(√7,1,1,1)ℤ⁴ (without loss of generality), with exact symmetry Γ ⋉ L₇, Γ = SO⁺(Q₇, ℤ).
- Every nonzero displacement has an infinite Γ-orbit, and Γ acts ergodically on the quasi-momentum torus T⁴. Both are confirmed by the R3-1 referee (`ref_R3-1/REFEREE_VERDICT.md`, items 1 and Strongest statement; `C5_R3-1_report.md:62-81`).
- Γ contains the pure boost g₁ = [[8,3],[21,8]] on (n₀, n₁), and its cubic-rotation conjugates g₂ and g₃ on (n₀, n₂) and (n₀, n₃). All are checked to be in Γ exactly, and R_z g₁ R_z⁻¹ = g₂ (`r42_algebra.out:1-3`).

**Hypotheses on a one-particle space H.**
- **(U)** Γ ⋉ L₇ acts on H by unitaries U(γ) and T(a), with U(γ)T(a)U(γ)⁻¹ = T(γa). This is R3-2's H5_Γ unitarity (`C5_R3-2_report.md:65`).
- **(Dec)** The constant-ξ generators P_μ commute with the translations. Each is decomposable over the translation spectral decomposition, H = ∫⊕ H_p dμ(p) on T⁴: P_μ = ∫⊕ τ_μ(p).
  - The multiplier τ_μ is **only measurable**. It may be unbounded, discontinuous, or nowhere locally bounded: a "singular multiplier".
  - We need τ_μ(p) to be a bounded operator on H_p for μ-almost every p. That is automatic when dim H_p < ∞ (finite fibre).
- **(C)** Covariance: U(γ)P_μU(γ)⁻¹ = Σ_ν L(γ)_μ^ν P_ν, with L any representation equivalent to the vector representation. The transpose convention does not matter here, which repairs the issue the referee noted at `C5_R3-2_referee.md:88-93`. Theorem S′ (§3) replaces (C) by any finite-dimensional multiplet.
- **(V)**, used only for Lemma G and Proposition I.
  - The vacuum Ω is Γ ⋉ L₇-invariant.
  - Site operators transform geometrically: U(γ)O(x)U(γ)⁻¹ is an operator at γx.
  - On-site operators have finite vacuum variance, ‖O(0)Ω‖ < ∞.

**Excluded (outside realizations; titles do not exceed proofs).**
- **(X1)** Infinite fibres with a pointwise-unbounded τ(p): the towers, P10 (`PRICE_NOTE.md:364`; `C4_I1_referee.md:15`).
- **(X2)** Non-unitary or indefinite-metric (Krein) implementations of Γ.
- **(X3)** A vacuum that is not Γ-invariant, i.e. a frame or arrow carried by the state.
- **(X4)** Infinite-dimensional identity multiplets, and finite multiplets whose representation is not rational (in Theorem S′ only).
- **(X5)** "Multipliers" that are distributions, not functions. These are non-ℓ² orbit-constant kernels, which define no decomposable operator on H (`ref_R3-1/REFEREE_VERDICT.md`, item 3).
- **(X6)** One-particle states not reachable by on-site operators (Proposition I's class boundary). Example E lives here.

## 2. Prior art (each counted once)

- **T_Γ** (`C5_R3-2_report.md:144-171`; referee `C5_R3-2_referee.md:77-86`). Bounded covariant charges vanish; this is CLOSED after the convention repair. The referee's open item is route 3 of the checklist: "an unbounded but finite-fibre/singular multiplier … is outside H5 and is a real escape" (`ref_R3-2/NO_GO_DISCIPLINE_CHECKLIST.md:22-25`).
- **R2-1 Theorem T** (CWC, bounded one-particle). Its determinant argument excludes a finite fibre on ℤ⁴ but does not classify infinite fibres (`C5_R2-1_referee.md:41-43`).
- **R3-1 Lemma A, Lemma M, and the note for R3-2** (`C5_R3-1_report.md:62-93,236-238`; referee item 1).
  - Every nonzero orbit is infinite.
  - Invariant L² symbols are constant.
  - "No regular equivariant translation charge exists" for L² vector-valued charges.
  - Theorem S below strengthens L² to every measurable multiplier, and the scalar case to operator fibres.
- **R2-2's N-Q′** (`TESTS.md:2711`), in the same spirit: covariant counts annihilate the vacuum. Lemma G is the site-operator analogue.
- **Repository grep** for Furstenberg, Benoist and Poincaré recurrence. The only hits are the Bougerol–Lacroix Lyapunov notes (`docs/BOUGEROL_LACROIX_STAGGERED_BLOCKING_LYAPUNOV_BRIDGE_NO_GO_NOTE_2026-05-10.md:64-68`), a different use (random matrix products). There are no hits for singular multipliers outside the R3-2 referee and TESTS.
- **Comparators (RECALLED):**
  - Poincaré and Halmos recurrence for conservative nonsingular maps, and the Hopf decomposition;
  - Bochner–Herglotz on ℤ⁴;
  - the Halmos ergodicity criterion for group actions on tori;
  - weights of rational representations of SO(1,3)°;
  - Benoist–Quint (Annals 2011) and Bourgain–Furman–Lindenstrauss–Mozes (JAMS 2011): Γ-invariant ergodic probability measures on T^d, for Zariski closures that are semisimple and strongly irreducible, are Haar or finitely supported on rational points. This is used only to *describe* Corollary N's singular part. No no-go depends on it.

---

## 3. Theorem S: singular multipliers vanish on the conservative part (proved; algebraic input checked)

**Statement.**
- Assume (U), (Dec) and (C).
- Let C ⊂ T⁴ be the set of quasi-momenta at which the torus actions β_g of the six pure boosts g₁^{±1}, g₂^{±1} and g₃^{±1} are all conservative (Hopf decomposition, with respect to the class of μ).
- Then τ_μ(p) = 0 for μ-almost every p ∈ C, for all μ. Equivalently, P_μ vanishes on the spectral subspace E(C)H, whatever the singularity of τ.
- **In particular, if the spectral class of H contains a finite Γ-invariant measure (M), then P ≡ 0.** By Poincaré recurrence, every invertible map preserving a finite measure is conservative.

**Proof.**
1. **(U) and (Dec) give the fibre structure.** U(γ) maps E(B) to E(β_γB), so it decomposes as a point map β_γ composed with fibre unitaries c(γ,p): H_p → H_{β_γp}. These carry a scalar Radon–Nikodym factor, which commutes with everything. By (C), c(γ,p)τ_μ(p)c(γ,p)⁻¹ = Σ_ν L(γ)_μ^ν τ_ν(β_γp).
2. **Define a seminorm.** For c ∈ ℝ⁴ set n_p(c) = ‖Σ_μ c^μ τ_μ(p)‖_op. This is finite for almost every p by (Dec), and it is a seminorm on ℝ⁴. Unitary conjugation gives n_{β_γp}(c) = n_p(L̃(γ)c), with L̃ the contragredient (or transpose) of L. That is again equivalent to the vector representation.
3. **Recurrence along a pure boost.** Take g = g₁, and let L̃(g) have the eigenvalue λ = 8 + 3√7 > 1 with real eigenvector e₊ (checked: `r42_algebra.out:3`).
   - Then n_{β_g^k p}(e₊) = λ^k n_p(e₊).
   - Let A_R = {p ∈ C : R⁻¹ ≤ n_p(e₊) ≤ R}. On C the map β_g is conservative, so almost every p ∈ A_R returns to A_R infinitely often (Halmos).
   - But λ^k n_p(e₊) > R for all large k, so μ(A_R) = 0.
   - The union over R is {p ∈ C : n_p(e₊) > 0}, which is therefore null.
   - g⁻¹ gives n_p(e₋) = 0 almost everywhere on C.
4. **Conjugates.** The same holds for g₂ and g₃. These are countably many null sets.
5. **Spanning.** The six vectors e_± of g₁, g₂ and g₃ span ℝ⁴. **Checked exactly: rank 4, in both the vector and the dual action** (`r42_algebra.out:5-7`; one boost alone gives rank 2).
6. **Conclusion.** A seminorm that vanishes on a spanning set is zero, so τ_μ(p) = 0 for all μ, for almost every p ∈ C. ∎

**What is *not* used:**
- continuity, boundedness, L^p membership, or analyticity of τ;
- commutativity [P_μ, P_ν] = 0;
- self-adjointness;
- interaction;
- H3's slope.

Only pointwise finiteness of the fibre operators and conservativity are used.

**Theorem S′: multiplets in place of (C)** (proved, with RECALLED weight theory).
- Suppose the identity's constant generators span a finite-dimensional Γ-stable space on which U(γ)·U(γ)⁻¹ acts by a representation ρ. Suppose ρ is the restriction of a rational representation of SO(1,3)° (or of Spin, given a specified lift; cf. `ref_R3-1/REFEREE_VERDICT.md`, item 1).
- Then on C every generator in a nontrivial Lorentz-isotypic component vanishes.
- **Proof.**
  - g₁ is a pure boost: it is identity on the (n₂, n₃) plane (`r42_algebra.out:14`). So in any rational representation it acts diagonalizably with positive real eigenvalues λ^w.
  - Step 3 kills the seminorm on every weight space with w ≠ 0, for g₁ and for each of its Γ-conjugates.
  - The span of these spaces is Γ-invariant, hence invariant under the Zariski closure, hence the sum of all nontrivial isotypic components. Every nontrivial irreducible representation of SO(1,3)° has a nonzero split weight. ∎
- So the referee's "larger or differently presented identity multiplet" (checklist route 5) does not escape when the multiplet is finite-dimensional and rational. Only Lorentz-scalar generators survive, and those are not energy-momentum.

**Scope.** Theorem S is not stronger than T_Γ; it is complementary.
- T_Γ: bounded charges vanish on *any* space.
- S: arbitrarily singular finite-fibre charges vanish on the *conservative* part.
- The remaining case is unbounded charges on a *dissipative* class. §5 shows it is genuinely open.

## 4. Lemma G, Proposition I and Corollary N: what on-site fields can create (proved; checked)

**Lemma G (proved; checked).**
- Assume (U) and (V). Let O^A(0), A = 1..r, be on-site operators with U(γ)O^A(0)U(γ)⁻¹ = Σ_B ρ(γ)_{BA}O^B(0) for γ ∈ Γ. Γ fixes site 0.
- Then the vacuum Gram matrix C_AB = ⟨O^A(0)Ω, O^B(0)Ω⟩ is a ρ(Γ)-invariant positive-semidefinite Hermitian form.
- If ρ is rational with no trivial summand, then C = 0, i.e. O^A(0)Ω = 0.
- **Proof.**
  - Invariance follows from unitarity and the invariance of Ω.
  - On the quotient by ker C, the image of Γ preserves a positive-definite form, so it is relatively compact.
  - Its Zariski closure, SO(1,3)°, would then act through a compact group. That forces the trivial action on the quotient, which is impossible without a trivial summand. ∎
- **Checked:**
  - Vector representation: the invariant Hermitian forms are c·G₇ (indefinite), so the only positive-semidefinite one is 0 (`r42_algebra.out:8-13`).
  - **Site stress tensor (Sym² of the vector representation):**
    - The invariant forms are 2-dimensional: (tr T)² and the contraction tr(G₇TG₇T).
    - The contraction is indefinite on the 9-dimensional traceless part, with inertia (6, 0, 3).
    - So every positive-semidefinite invariant Gram form vanishes on the traceless part (`r42_sym2_gram.out:1-17`).
- **Consequence (proved).** A finite-variance on-site stress tensor has **T^{μν}_traceless(0)Ω = 0**. Its spin-2 part creates nothing from the vacuum, and its vacuum Wightman function ⟨T_tl T_tl⟩ vanishes identically.

**Support lemma (proved).**
- Suppose a Γ-covariant tensor field T^{μν}(x) is attached to sites and has finite support S ∋ 0. Covariance maps the family's support S to γS, and the family spans the same space, so γS = S.
- Every nonzero orbit is infinite, so S = {0}.
- So the stress tensor that couples to h_μν must be on-site, and Lemma G applies to it, or else it has infinite support (unbounded valency, R3-1).

**Proposition I: invisibility (proved, no recalled classification needed).**
- Assume (U) and (V). Let V₀ = span{O^A(0)Ω}. This is finite-dimensional and Γ-invariant, and U(γ) acts on it unitarily.
- Then ν(B) = tr(P_{V₀}E(B)P_{V₀}) is a **finite Γ-invariant measure**, and the translates of V₀ generate a subspace H_ss whose spectral class is [ν]. A finite invariant measure is conservative for every element, so H_ss ⊂ E(C)H.
- Hence, by Theorem S:
  - **(a)** every (C)-covariant, translation-commuting, finite-fibre four-vector charge annihilates every one-particle state that finitely many finite-variance on-site operators create from Ω, however singular its multiplier;
  - **(b)** a one-particle sector whose spectral class is totally dissipative for some pure boost has zero overlap with every such on-site operator.
- Countably many on-site families (all on-site polynomials) give the same result with a weighted sum Σ2^{−k}ν_k.

**Under the Qubit axiom** (`MINIMAL_AXIOMS_2026-06-29.md:47`), on-site operators are 2 × 2 matrices, so they are bounded and (V)'s finite variance is automatic. **Reading:** on an LRL realization with qubit sites and an invariant vacuum, the gravitational four-vector charge is zero on everything on-site observables can create.

**Corollary N: no propagation for on-site observables** (a.c. part proved; singular part RECALLED).
- Under (U) and (V), the two-point function W_AB(a) = ⟨O^A(0)Ω, O^B(a)Ω⟩ has the form C₀δ_{a,0} plus the Fourier transform of a singular Γ-covariant finite measure.
- **Proof of the a.c. part.**
  - By Bochner–Herglotz, the spectral matrix measure is finite and Γ-covariant with unitary ρ on V₀.
  - Its Haar-a.c. density is an equivariant L¹ map into a unitary Γ-module.
  - Its bounded truncations span a finite-dimensional Γ-invariant subspace of L²(T⁴). That subspace must be the constants, because every nonzero character has an infinite orbit, so L²₀(T⁴) has no finite-dimensional subrepresentation.
  - So the density is constant, i.e. C₀δ in real space.
- **Singular part.** By Benoist–Quint and BFLM (comparator), it consists of atoms on finite orbits, i.e. an almost-periodic, sublattice-periodic W.
- The same holds for a classical Γ ⋉ L₇-invariant random field with finite on-site variance.
- **Checked as an illustration only** (`r42_posdef.out`).
  - Orbit-constant candidates W = δ + ε·w(Q₇(d)) were tested: the timelike shell indicator, the spacelike shell indicator, and a smooth e^{−|Q|/3}.
  - On boxes [−L, L]⁴ with L = 1…4 (up to 6561 sites), the positive-semidefinite window for ε shrinks: [−0.104, 0.104] → [−0.022, 0.022] for the timelike shell, and [−0.0125, 0.0261] → [−0.0035, 0.0104] for the smooth weight. Both extreme eigenvalues grow without visible bound.
- **Reading (for R4-1 and R4-3, not this item's verdict).** On an exactly Γ-invariant state, any per-realization long-wavelength law must be carried by multi-site (composite) observables or by a Γ-breaking state. Single-site correlations at nonzero separation have no decaying part: apart from the non-decaying singular (almost-periodic, given BQ) piece, they are zero.

## 5. Example E: the escape outside the class is real (proved; checked to 60 digits)

**Construction.**
- Let H_m = {q : q² = −m², q⁰ > 0} with its invariant measure dΩ, and let π: H_m → T⁴ be q ↦ Dq/2π mod ℤ⁴.
- **π is injective off an Ω-null set** (proved).
  - q and q + G both lie on H_m only on the 2-dimensional surfaces 2q·G + G² = 0. These are countably many, each Ω-null.
  - The exceptions include all rational points. Their Γ-orbits on T⁴ are finite, so infinitely many shell points sit over each one.
- Set Σ = π(H_m), μ = π_*Ω and H = L²(Σ, μ) ≅ L²(H_m, dΩ), with:
  - T(a) = multiplication by e^{iq·a};
  - U(γ) = the Lorentz action;
  - P_μ = multiplication by ι(p)_μ, where ι = π⁻¹ is the a.e.-defined lift.
- Then:
  - (U) holds exactly;
  - the multiplicity is **1** (finite fibre);
  - (C) holds exactly: ι(β_γp) = γ·ι(p);
  - P is nonzero and unbounded;
  - ι is nowhere locally bounded on T⁴, because Σ is dense. This is a genuine singular finite-fibre multiplier.
- **Why Theorem S does not bite.** Each pure boost acts on (H_m, Ω) properly, hence totally dissipatively: μ is σ-finite, Haar-null, and has no finite invariant member.

**Checked** (`r42_shell_lift.out`; m = 0.5 lattice units).
- **(A) Unique lift.** For 6 random irrational shell points, the lift of p = frac(k) in the box |n_i| ≤ 25 is unique and equals k to 1e-45.
- **(B) Equivariance.** ι(B p mod 1) = B ι(p) holds to ≤ 4e-62 for 15 cases: g₁^{±1}, g₂, g₃R_z, and R_z g₁ g₂⁻¹, with lifts up to |k|_E ≈ 12.9.
- **(C) Density.** For Haar-random p, the distance to shell lifts with |n| ≤ NB falls roughly as NB⁻³: 9.2e-5 → 1.9e-7 from NB = 4 to 32. A 1e-12 perturbation of a shell point has no exact lift in the box.
- **(D) Infinite multiplicity at rational points.** The rational point p = (½, ½, ½, ½) (M = 1) carries 232, 1006, 3280 and 13,744 lifts in boxes 5, 10, 20 and 40. The count grows like T², so the "tower" sits exactly on the finite-orbit atoms.

**Example E′: finite-variance link variables** (proved at the representation level; not run).
- Take a timelike d₀ with finite stabilizer Γ_{d₀}, and a Γ_{d₀}-invariant F ∈ L²(H_m) decaying in rapidity.
- Set v_{(x, γd₀)}(q) = e^{iq·x}F(γ⁻¹q).
- This is a covariant family of finite-norm "link" vectors that generates (a dense subspace of) L²(H_m). Each site carries the infinite orbit Γd₀ of such links.
- This is the multi-site interpolation that Proposition I leaves open, realized with the continuum supplied as data.

**Reading.** On LRL, R2-1's tower is replaced by an a.e.-injective embedding of the continuum hyperboloid into T⁴.
- Multiplicity 1, but an infinite and wandering invariant measure.
- The particles are created only by infinite-variance point values or by infinite-valency links.
- The content is the continuum one-particle space, i.e. set A in LRL coordinates, analogous to R2-1's COLLAPSES-TO-A (`C5_R2-1_referee.md:73`). This is a reading, not a theorem that every escape is the continuum.

## 6. The gauge identity itself

- **Not constructed.** Example E (or E′) supplies the representation-level content of the constant-ξ identity: a unitary, covariant, nonzero charge on a finite fibre.
- An exact *local* linearized-diffeomorphism identity needs more:
  - a lattice matter law;
  - a local stress tensor T^{μν}(x);
  - the Ward relation for x-dependent ξ.
- In E, these are the continuum's. The site "stress tensor" is a continuum point value with infinite variance.
- By the support lemma and Lemma G, a finite-variance site stress tensor would have T_tl(0)Ω = 0. Whether its one-particle matrix elements on a dissipative-class particle can still carry the spin-2 coupling is open.
  - *Suggested:* it can, as a bounded convolution operator on H³.
  - *Suggested, but would need crossing, which a lattice does not supply:* T_tl(0)Ω = 0 forbids it.
- No lattice law of this kind is known. R3-1 shows that invariant laws must be retarded and have tube-only symbols (`ref_R3-1/REFEREE_VERDICT.md`, item 3). Whether such a law produces particles that no on-site variable creates, carrying ι, is **open**.

## 7. Against the FIXED readings (`TESTS.md:2810-2813`)

| Disjunct | Status |
|---|---|
| **PASS**: an explicit finite-fibre example with an exact gauge identity | **Not met.** Example E is explicit and finite-fibre, with an exact covariant charge (checked), but there is no lattice law and no local identity. Its law is the continuum (§6) |
| **FAIL**: a no-go covering singular multipliers in a stated class (refereed) | **Met by the worker, pending the referee.** Theorem S, with S′ and Proposition I, covers **every measurable (singular, unbounded) finite-fibre multiplier**. The class is: unitary Γ ⋉ L₇; (C), or a finite rational multiplet; a translation-commuting charge; a conservative spectral class. The conservative class includes every subspace of ℓ²(L₇) ⊗ C^N, every state created by finite-variance on-site operators from an invariant vacuum, and every qubit-site theory |
| **INCONCLUSIVE** | This would be the reading if the referee judges class 𝔉 too narrow (scope below) |

**Worker reading: FAIL (bounded to class 𝔉)**, recordable only after the codex referee (C5 rules, `TESTS.md:2309`).

**Mandatory scope note.**
- Class 𝔉 contains **no propagating particle.** By Corollary N, on-site-created quanta have ultralocal plus non-decaying spectra.
- On dissipative (hyperboloid-like) one-particle sectors, the singular-multiplier escape **exists** at the representation level (Example E, checked).
- So the referee's open route 3 (`NO_GO_DISCIPLINE_CHECKLIST.md:22-25`) is:
  - closed on every conservative class;
  - open, and realized as a representation, on dissipative classes. There it requires matter whose quanta no finite-variance on-site variable creates.

## 8. Strong-word check, and what needs the referee

**Proved** (same family):
- Theorem S;
- Theorem S′ (with RECALLED weights);
- Lemma G;
- the support lemma;
- Proposition I;
- the a.c. part of Corollary N;
- Example E's properties: a.e. injectivity, unitarity, equivariance, dissipativity;
- Example E′ at the representation level.

**Checked:**
- the rank-4 spanning of the boost eigenvectors (exact);
- the invariant forms for the vector representation and Sym² with their inertia (exact);
- the lift uniqueness and equivariance (60 digits);
- the density;
- the rational-point towers;
- the positive-semidefinite windows (illustration only).

**RECALLED** (comparators):
- Halmos/Poincaré recurrence and the Hopf decomposition;
- Bochner–Herglotz;
- the Halmos ergodicity criterion;
- weight theory;
- Benoist–Quint and BFLM. These are used only in Corollary N's description of the singular part.

**Suggested:**
- μ = π_*Ω is infinite on every open set of T⁴ (from equidistribution);
- the §6 remarks on the stress-tensor matrix elements.

**"Exactly"** is used only for algebraic identities and the (C)/(U) properties of Example E.

**Needs the codex referee:**
- Theorem S and S′;
- Lemma G and the support lemma;
- Proposition I and Corollary N;
- the class statement and the FAIL reading;
- whether "conservative class" or "on-site-created" is the right stated class.

## 9. Price implications (named, none adopted)

- **No new price is needed to state the no-go.**
- **For LRL as a gravity substrate (set B′ / E′), an exact identity now requires all of the following** (reading):
  - (i) matter whose quanta lie in a boost-dissipative momentum class and are created by no finite-variance on-site variable (Proposition I). For qubit sites (`MINIMAL_AXIOMS_2026-06-29.md:47`) this means composite, multi-site, infinite-valency interpolation, on top of R3-1's unbounded-valency Admissibility price (`C5_R3-1_report.md:313-317`);
  - (ii) a local stress tensor whose spin-2 part annihilates the vacuum (Lemma G);
  - (iii) a lattice law that produces (i). None is known. Example E's content is the continuum hyperboloid, i.e. set A in lattice coordinates (reading).
- **Otherwise** the alternatives are those R3-2 named: tunings (codimension 5, conditional on (E2)), or P10 towers (X1).
- **Corollary N, for R4-1 and R4-3** (reading). An exactly Γ-invariant per-realization state has no decaying on-site correlations. Any per-realization long-wavelength law lives in composite observables or in a Γ-breaking state, i.e. a frame or arrow in the state (X3, cf. R2-5).
