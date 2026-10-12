# C5 R3-2: gravity on the Lorentz-random lattice (LRL)

**Worker.** Claude Opus 5.5 (probe R3-2). This is the same model family as the supervisor and as the R2-1 and R2-2 workers. **Not refereed.** Run 2026-10-12, 12:27Z to about 12:55Z. No repository file was edited.

**Scratch.** `scratchpad/C5/R3-2/`:
- `r32_forms.py` → `r32_forms.out`: invariant-form counts, the gauge-invariant subspace, TT ranks, and the E_g/T_2g split;
- `r32_orbit.py` → `r32_orbit.out`: the Γ_L7 orbit and torus checks, and the shell transform;
- `r32_scalar.py` → `r32_scalar.out`: what conserved sources see beyond TT;
- this report.

**Read in full.**
- `docs/MINIMAL_AXIOMS_2026-06-29.md`.
- `TESTS.md:2302-2704`: Campaign C5, the round-1 results, round 2, and round 3. R3-2 is at `:2672-2683`.
- `agents/C5_O5_synthesis.md`, at the sections used (F1, F2, set B).
- `SUMMARY.md` §§15–21.
- `PRICE_NOTE.md` §§1–2 and the v6 delta (P10–P14).
- Referee files: `C4_K1_referee.md`, `C4_V3_referee.md`, `RV4_S1_referee.md`, `RC_C3_referee.md`.
- `C5_O1_report.md` §3.3–3.6, for Lemmas C, C′ and D.
- The R2-1 worker report (Theorem T). Its codex referee run died on a stream error (`ref_R2-1/codex_run.log`, tail), so **Theorem T is unrefereed**.
- The R2-2 worker report and its **referee verdict, CONFIRMED WITH CORRECTIONS** (`ref_R2-2/REFEREE_VERDICT.md`). It confirms LRL's invariance in law, cocompactness and Bragg gap. It notes that reciprocal covectors transform as g^{−T}. It leaves "effective matter/gravity operators and analyticity" open (`:20`).

**Labels.**
- *proved*: a complete argument is written here (same family, unrefereed).
- *checked*: a numerical or exact-arithmetic check in the scratch files.
- *suggested*: argued only.
- *reading*: an interpretation.
- *comparator*: an outside result.
- *RECALLED*: a standard fact quoted from memory.

---

## 0. In plain words

- **The count of hand-set numbers drops from 11 to 5, and in the graviton's own wave sector from 5 to 1.**
  - On LRL every exact symmetry of a realization includes infinitely many genuine boosts.
  - Any fixed coefficient pattern those boosts leave unchanged is automatically Lorentz-invariant.
  - So the graviton's quadratic action can have only the Lorentz-invariant shapes: 2 mass shapes and 4 two-derivative shapes, against Z⁴'s 3 and 9.
  - Light-speed gravitational waves then need **no** tuning.
  - The wave sector needs one tuning, the graviton mass, plus the cosmological constant.
  - All of this holds only if each realization *has* a low-energy expansion. That is not shown, and §5 shows it is delicate.
- **The two shear numbers become one.** The vacuum can no longer tell the two cubic shear types apart (E_g vs T_2g), so V3's "E_g only" residue collapses into a single Lorentz-invariant shear coefficient. That coefficient is still not forced to zero: it is the graviton mass.
- **An exact gauge identity is even harder on LRL than on Z⁴.**
  - The identity needs a true 4-momentum: a charge that grows without limit as you boost.
  - A grid with finitely many states per site has a bounded charge.
  - On Z⁴ that clash needed interacting matter (R2-1).
  - On LRL the realization's own boosts force it **even for free matter**, provided the identity respects those boosts.
  - So the tower (a continuum folded into each cell) is forced again.
- **Not everything the wave sector misses is harmless.** Long-range forces between ordinary sources also see the non-gauge kinetic shapes, through the scalar part of the field (light bending, the Cassini γ). So the honest observational count is at least 3, not 2 (checked).

---

## 1. Hypotheses (stated before the titles) and the scope's exclusions

**Setting.**
- A single realization is X = g(L₇ + u), with L₇ = diag(√7,1,1,1)ℤ⁴ and Q₇ = −7n₀² + n₁² + n₂² + n₃².
- Its symmetry group is affine, with linear parts Γ_L^g = gΓ_{L₇}g⁻¹ ⊂ O(1,3).
- Momenta are covectors, transforming as Λ^{−T}. Quasi-momenta live in T⁴ = ℝ⁴/L^rec, with L^rec = 2π·diag(1/√7,1,1,1)ℤ⁴ in the realization frame. LRL facts are as refereed (`ref_R2-2/REFEREE_VERDICT.md:9-16`).

**Hypotheses.**
- **(Γ)** The matter + graviton law on a realization is covariant under its affine symmetry group, with finitely many fields per site and lattice-translation-covariant kernels.
- **(E2)** The per-realization effective quadratic action of h_μν has an asymptotic expansion at q → 0 to second order: K(q) = K₀ + K₂(q) + o(|q|²). Used only for the counts (§3, §4). It is **not** shown to hold (§5).
- **(H1)** As in R2-1 (`R2-1_report.md:36-38`): δh = D(∂)ξ + O(κ), with D translation-covariant and D(0) = 0, and δφ = κξ^μT_μ[φ,h] + O(κ²).
- **(H3_Γ)** The constant-ξ charge does not vanish on the one-particle sector. This is weaker than R2-1's slope H3, and implied by it.
- **(C)** Covariance of the identity: the constant-ξ generators P_μ satisfy U(Λ)P_μU(Λ)⁻¹ = (Λ⁻¹)^ν_μ P_ν for Λ ∈ Γ_L^g.
- **(H5_Γ)** Each P_μ is a bounded operator on the one-particle space, and Γ_L acts on that space by unitaries.
  - Bounded P_μ follows from finitely many fields per site plus a summable (ℓ¹) kernel for T_μ, since the symbol is then continuous on the compact T⁴.
  - SLAC-type bounded symbols are also covered.

**Excluded realizations.**
- (X1) Towers or infinite fibres, and unbounded or non-ℓ¹ generators T_μ (P10, P14).
- (X2) Identities that are not Γ_L-covariant, i.e. (C) fails.
- (X3) Laws without any per-realization q-expansion, i.e. (E2) fails.
- (X4) Curved backgrounds (R3-3).
- (X5) Non-unitary realizations of Γ_L, in the eigenvalue variant of §5.
- (X6) Nonlinear O(κ²) closure, which is not needed for the results here.

## 2. Prior art (each counted once)

- **Zariski density of the integral Lorentz group** and "invariant tensors Lorentz-invariant at every rank", with locality failing (`agents/C4_F2_report.md:98`). O(1,3;ℤ)'s only invariant symmetric tensor is η (`agents/C5_O1_report.md:138`).
- **Lemma C′** (refereed after correction): summable spanning couplings with norm-preserving covariance give a finite point group (`C5_O1_report.md:131-137`).
- **Lemma D** (refereed, abstract form): a connected group normalizing ℤ^d acts trivially on it (`C5_O1_report.md:155-165`).
- **K1** (`C4_K1_referee.md:3,15`): 3 + 9 W(B4) forms, a 4-dimensional O(4) subspace, one gauge-invariant combination, codimension 11, TT rank 5.
- **V3** (`C4_V3_referee.md:27,48`) and **RV4 S1** (`RV4_S1_referee.md:32`): the E_g-only Jacobian residue, which √g·Λ cannot cancel because it enters E_g and T_2g equally.
- **C3** (`RC_C3_referee.md:9,23`); R2-1's **Theorem T** (unrefereed); **I1**'s complete tower (`C4_I1_referee.md`).
- The **R2-2 referee**'s statement that effective operators and analyticity are open (`ref_R2-2/REFEREE_VERDICT.md:20`).
- **Comparators** (RECALLED):
  - Borel density: lattices in SO(1,3) are Zariski-dense;
  - the first fundamental theorem for O(1,3): invariant polynomials are polynomials in p²;
  - Barnes–Rivers spin projectors, and the vDVZ tensor structure −1/3 vs −1/2;
  - Sorkin/BDS causal-set d'Alembertians, as the model of non-analytic Lorentz-invariant kernels with layer sum rules.
- **What is new here:**
  - the exact counts on Γ_{L₇};
  - Theorem T_Γ (bounded covariant charge ⇒ zero; no interaction needed);
  - Lemma A (no analytic Γ_L-invariant periodic symbol);
  - the conserved-source check beyond TT.

---

## 3. Count of Γ_L-invariant quadratic forms (proved under (Γ)+(E2); checked)

**Theorem F (proved).** Under (Γ) and (E2), K₀ and K₂ are Γ_L-invariant tensors, hence O(1,3)-invariant (SO⁺(1,3) for the proper part).
- **Proof.** K(Λ^{−T}q) = Λ·K(q) for Λ ∈ Γ_L, with the appropriate action on the h-indices. The asymptotic coefficients are unique, so each one is Γ_L-invariant. The stabilizer of a tensor is Zariski-closed, so it contains the Zariski closure of Γ_L. Borel density makes that closure ⊇ SO(1,3)°. ∎
- **The resulting counts:**
  - 2 mass forms: h_μνh^μν and h²;
  - 0 one-derivative forms;
  - 4 two-derivative forms: q²h·h, (q·h)², (q·h·q)h and q²h²;
  - 0 parity-odd forms. With one symmetric h, ε must take ≤ 1 index from each h and ≤ 1 from the two q's, which is fewer than 4.
  - 1 gauge-invariant combination: the EH/K1 combination.

**Checked** (`r32_forms.out` §1–3). Exact ranks mod two primes on integer generators in lattice coordinates; float SVD cross-check with singular-value gaps ≥ 0.5 vs ≤ 2e-10.

| Group (generators) | mass | 1-deriv | 2-deriv | gauge-inv | gauge-restoration codimension | TT rank (mass, kinetic incl. EH) |
|---|---|---|---|---|---|---|
| W(B4) on ℤ⁴ (K1 control) | 3 | 0 | 9 | 1 | **11** | (2, 4) → K1's 2 + 3 = 5 ✓ |
| axioms' proper cubic O on ℤ³×ℝ | 6 | 8 | 30 | — | — | — |
| O_h × {1, T} on ℤ³×ℝ | 6 | 0 | 26 | — | — | — |
| **Γ_{L₇}**: O_h, T, γ = [[8,3],[21,8]] on (n₀,n₁) | **2** | **0** | **4** | **1** | **5** | **(1, 1)** |
| Γ_{L₇} proper orthochronous: O, γ | 2 | 0 | 4 | — | — | — |
| ⟨γ, R_z⟩ only (not Zariski-dense; control) | 5 | 6 | 18 | — | — | — |
| so(1,3) Lie algebra (target) | 2 | — | 4 | 1 | 5 | (1, 1) |

**What this means (proved and checked):**
- The registered K1 count (operator codimension of linearized gauge restoration, after the tadpole) falls from **11 to 5 = 2 + 3**.
- The TT-restricted tunings fall from K1's 5 to **1**: the TT mass, i.e. m_g. The TT kinetic rank 1 is the EH normalization itself, so **c_T = c needs no tuning**.
- The supervisor's thread item 1 (`TESTS.md:2654`) is confirmed at quadratic order for h, conditional on (E2).

---

## 4. The E_g / T_2g shear split collapses (proved under C² strain response; checked)

**Proof.** The per-realization vacuum energy E(h) under constant strain satisfies E(Λ^Th Λ) = E(h) for Λ ∈ Γ_L^g. The realization maps to itself up to a translation, and the energy density is translation-invariant. If E is C² at h = 0, its second-order form is Γ_L-invariant (Theorem F's argument), so it equals a·h_μνh^μν + b·h². Restricted to spatial traceless strains, in any frame, this gives **μ_E = μ_T2 = a**.

**Checked** (`r32_forms.out` §4). Every Γ_{L₇}-invariant mass form gives identical E and T2 values, with max |μ_E − μ_T2| = 1.1e-13. For W(B4) the difference is 0.90.

**What remains (proved, by counting).**
- (a, b) are two numbers, and the Λ-form √−g fixes their ratio to the tadpole: (E₁, a, b) ∝ (1/2, −1/4, 1/8)ρ.
- After the tadpole is tuned, **a** is the TT (graviton) mass and **b** is a trace mass.
- So P0's two shear tunings (`PRICE_NOTE.md` v6 §4, P0) become **one**. V3's specific "E_g only, so not Λ" argument (`C4_V3_referee.md:27`) no longer separates anything, but nothing forces a to its Λ value either.

**Escape at q = 0 only (suggested).** If the realization is drawn in the strained metric's own frames (it co-moves with a constant h), a constant h is a pure coordinate change and E(h) = ρ√−det(η+h) exactly. That is T0's "cutoff moves with the geometry". It needs a curved-space LRL for q ≠ 0, which is R3-3's open problem.

---

## 5. Exact gauge identity on LRL: Theorem T_Γ (proved under (Γ), H1, H3_Γ, (C), H5_Γ)

**Step 1 (as in R2-1 Step 1, `R2-1_report.md:91-97`; counted once).** For constant ξ, D(0) = 0 kills δh at O(κ⁰), so S_m is invariant under δφ = ξ^μT_μ[φ,0]. Nothing in this step uses ℤ⁴. **It also holds for free matter.**

**Step 2 (new; proved).** Let P_μ be the one-particle generators. By (C), for every Λ ∈ Γ_L^g and every coefficient vector c:

  ‖Σ_ν (Λ^{−T}c)^ν P_ν‖ = ‖U(Λ)(Σ_μ c^μ P_μ)U(Λ)⁻¹‖ = ‖Σ_μ c^μ P_μ‖ ≤ 2C|c|, with C = max_μ‖P_μ‖.

- The kernel {c : Σ c^μP_μ = 0} is a Γ_L-invariant subspace of ℝ⁴. The vector representation of a Zariski-dense subgroup is irreducible, so the kernel is 0 or ℝ⁴.
- If it is ℝ⁴, then P ≡ 0, contradicting H3_Γ.
- If it is 0, then c ↦ ‖Σc^μP_μ‖ is a norm on ℝ⁴, so it is ≥ k|c| for some k > 0. Then k|Λ^{−T}c| ≤ 2C|c| for all Λ ∈ Γ_L^g.
- But Γ_L·v (and Γ_L^{−T}·v) is unbounded for every v ≠ 0. A bounded orbit spanning ℝ⁴ would make the group preserve a positive form, i.e. make it relatively compact, which contradicts γ's eigenvalue 8 + 3√7 ≈ 15.9.
- Contradiction. ∎

**Eigenvalue variant (no unitarity needed; proved).** On a nondegenerate in-band shell point, the joint eigenvalue at U(Λ)ψ is Λτ(ψ). That is unbounded over Γ_L, while the eigenvalues of a continuous finite-dimensional symbol on the compact T⁴ are bounded.

**Checked** (`r32_orbit.out`).
- **The group ball.** 78,696 elements of the Γ_{L₇} ball, each checked to preserve Q₇ in exact arithmetic.
- **The in-band rest covector p₀ = (0.05, 0, 0, 0)** lies far below the Bragg gap |G²| ≥ (2π)²/7. Its orbit stays on the shell, to float precision.
- **Growth.** |τ| = |p|_E grows 0.05 → 9.0 → 2.3e3 → 3.6e4 → 1.6e5 at word lengths 0, 2, 4, 6 and 8 (the ball is capped at entries ≤ 1e7).
- **Spread over the torus.** Reduced mod L^rec, the orbit occupies all 256 cells of a 4⁴ grid and 1069 of 6⁴ = 1296. The median, over occupied cells, of the largest |τ| found is 1.5e5. So the required charge is unbounded in essentially every region of T⁴.
- **Other vectors.** Random, null and spacelike unit vectors all reach |Λv| of 3e6 to 5e6.

**Conclusion (proved under the stated hypotheses).**
- No Γ_L-covariant exact linearized-diffeomorphism identity exists with a bounded constant-ξ generator. That covers finitely many fields per site with an ℓ¹ T_μ and SLAC-type bounded symbols, **for free or interacting matter**.
- The only escapes are (X1), an unbounded one-particle charge spectrum (a tower: P10, i.e. the continuum folded into T⁴), and (X2), an identity that picks a frame.
- **The FAIL disjunct "the R2-1-type tower is forced" is met under (C) + H5_Γ.**
- Not shown: that the tower must be I1's *complete* reciprocal tower. Shown only: that it is unbounded over a set dense in T⁴ (checked occupancy).

**Comparison with ℤ⁴ (reading).**
- On ℤ⁴, W(B4) is finite, so bounded covariant charges exist, e.g. sin k_μ. That is why K2's free identity is exact through O(κ), and why R2-1 needed interactions (Steps 2–5, with analyticity and winding).
- On LRL the infinite boost group does the work that periodicity plus collisions did on ℤ⁴. So the free O(κ) identity of K2 type cannot exist on LRL under (C).

**Status of C3 (reading).** C3 and RB obstruct a *continuous* first-moment boost generator (`RC_C3_referee.md:9`). A realization has exact *discrete* boosts and needs no boost generator, so C3's hypotheses are not met. The C3 obstruction does not survive as such; its translation half reappears as Theorem T_Γ.

**Without (C) (open).** Theorem T's ℤ⁴ route would need H4's strip analyticity of the band along a winding path. Lemma A (§6) shows that no nontrivial Γ_L-invariant periodic symbol is analytic on a neighbourhood of the light cone. Whether a nontrivial Γ_L-covariant matter law has any analytic band is part of R3-1.

---

## 6. Lemma A: a Γ_L-invariant periodic symbol cannot be analytic near the light cone (proved)

**Statement.** Let F: ℝ⁴ → ℂ be L^rec-periodic and Γ_L-invariant. If F is real-analytic on U_r = {p : |p²| < r} for some r > 0, then F is constant there.

**Proof.**
1. The Taylor components at 0 are Γ_L-invariant, hence O(1,3)-invariant (Zariski density), hence polynomials in p² (first fundamental theorem). So F = f(p²) near 0, with f analytic of radius ≥ r′ > 0.
2. U_{r′} is star-shaped, hence connected. By the identity theorem F = f∘Q on U_{r′}.
3. Take G ∈ L^rec∖0 and a null n with n·G ≠ 0. For p = λn, Q(p) = 0 and Q(p + G) = 2λ n·G + G², which sweeps every c ∈ (−r′, r′) as λ varies.
4. Periodicity gives f(c) = f(0), so f is constant. ∎

The proof extends to matrix symbols with Lorentz-covariant internal structure, e.g. F = p̸f₁ + f₂ forces f₁ = 0 and f₂ constant. That extension is suggested, with a sketch only.

**Consequences.**
- **Proved.** Every nontrivial Γ_L-covariant kernel has a symbol that is non-analytic arbitrarily close to the light cone. This strengthens Lemma C′ (summable ⇒ trivial).
- **Proved, trivially.** A "Poincaré-series" kernel K = Σ_γ k(γx) is constant on the infinite Γ_L-orbits. Its couplings therefore do **not** decay along any orbit in any frame. So "quasi-locality with power-law tails" (`TESTS.md:2655`) is the wrong description: the orbit weights converge, but the law has causal-set-type unbounded valency.
- **Checked** (`r32_orbit.out` §3). A single timelike orbit shell's continuum transform is 4πK₁(κ)/κ, and κ²F/4π → 0.99909 at κ = 0.02. Each shell therefore contributes a **1/q² non-analyticity** at q → 0.
- **Suggested.** (E2) can hold only if the law's orbit weights satisfy exact moment sum rules (Σκ_Oc_O = 0, Σκ_Oc_Oτ_O² = 0, …), like BDS layer coefficients. Whether loops preserve those rules is **open**, and it is R3-1's question. If they do not, the generated graviton self-energy carries a 1/q²-type non-local term, and §3's count is moot.

---

## 7. Beyond TT: what conserved sources see (checked; Euclidean O(4) stand-in, same projector algebra)

`r32_scalar.out`, with the long-range amplitude q²·TK⁻¹T → c₁T·T + c₂(tr T)²:
- **EH plus any gauge fixing:** c₂/c₁ = −0.500000, the GR value. **EH plus a tiny Fierz–Pauli mass:** −0.333333 (vDVZ). Both reproduce the comparator.
- **Generic Lorentz-invariant non-gauge kinetic terms, TT mass tuned to 0:** c₂/c₁ = −0.28, −0.38, −0.18 and −0.27 with a natural trace mass, and −0.31, −0.09 and −0.31 with no trace mass. The sign and size of c₁ also vary.
- **With both masses zero,** one kinetic shift restores −1/2. Roots exist for shifts of F4, F3 or F2, so this observable has codimension 1.
- **With a natural trace mass,** the one-parameter scans were erratic (near-singular blocks). They are not interpreted.

**Reading.**
- Long-range gravity between ordinary bodies (light bending, PPN γ; Cassini) depends on the non-gauge kinetic directions.
- So the **observational linear count is ≥ 3**: m_g, the scalar ratio, and Λ. It is not "graviton mass + Λ only".
- Suggested: ghost and health conditions in the spin-1/spin-0w sectors add more.
- Without an identity (§5), nothing protects these directions. Their natural size, O(1) relative to EH from zone-scale loops, is suggested by analogy with K1's one-loop example (`C4_K1_referee.md:9`). It is not computed on LRL.

---

## 8. Against the FIXED readings (`TESTS.md:2679-2682`)

| Disjunct | Status |
|---|---|
| PASS (i): Γ_L-covariant law with an exact linearized identity | **Not met.** Excluded under (C) + H5_Γ (Theorem T_Γ, §5). Open only via (X1) towers or (X2) frame-choosing identities |
| PASS (ii): tuning count ≤ Lorentz count ("graviton mass + Λ only") | **Met only in the TT reading, and only conditional on (E2):** m_g + Λ, with c_T free (§3). By K1's registered definition the count is 5 (= the full Lorentz non-gauge codimension), not 2. For conserved-source observables it is ≥ 3 (§7, checked). (E2) itself is undecided: Lemma A, R3-1 |
| FAIL (i): the R2-1-type tower is forced | **Met under (C) + H5_Γ** (proved, same family; needs the codex referee). Interactions are not needed on LRL |
| FAIL (ii): the count does not improve | **Not met, conditional on (E2):** 11 → 5 (codimension), TT 5 → 1, E_g/T_2g 2 → 1 |

**Reading: INCONCLUSIVE.** The two halves split.
- **The identity half** meets FAIL (i), bounded to (C) + H5_Γ.
- **The counting half** is a real improvement. It meets PASS (ii) in the TT reading only, and only if a per-realization low-energy expansion exists. The fixed readings do not say which disjunct takes precedence.

**Against the expectation** (`TESTS.md:2683`: "INCONCLUSIVE, leaning a partial PASS"):
- The verdict matches.
- The counting collapse is as expected, with the precise numbers 11 → 5 and TT → 1.
- The identity result is **stronger than expected**. The Theorem-T analogue needs no interaction on LRL, and its cause is the infinite boost group, not "discrete translations" as such.
- Two caveats were not registered:
  - the Lorentz count for long-range observables is ≥ 3, not 2;
  - the whole count rests on (E2), which Lemma A shows cannot come from any analytic symbol.

---

## 9. Strong-word check, and what needs the referee

**What "proved" covers.**
- Theorem F, given (E2).
- §4's collapse, given C² strain response.
- Theorem T_Γ, both variants, under the listed hypotheses.
- Lemma A (scalar case).
- The parity-odd zero count.
- The "Poincaré series is constant on orbits" remark.

**External inputs, all RECALLED:** Borel density, the first fundamental theorem for O(1,3), Barnes–Rivers/vDVZ.

**Checked:** the counts (exact mod p, plus float), the E/T2 equality, the orbit growth and torus occupancy, the shell transform, and the conserved-source ratios.

**Not claimed:**
- that (E2) holds;
- that the generated coefficients are O(1) on LRL;
- that the tower must be complete;
- anything about curved backgrounds or O(κ²) closure.

**Needs the codex referee** (no-go type, per C5 rules, `TESTS.md:2308`): Theorem T_Γ and Lemma A. FAIL (i) is a bounded no-go.

## 10. Price implications (named, none adopted)

- **Set "E′/LRL" as a gravity substrate.** It pays everything R2-2 listed (the Lattice axiom with Γ_L in place of cubic rotations, unbounded valency, a flat affine background).
- **On top of that (suggested):** either
  - (i) **P10**: a tower per cell, needed for an exact identity even with free matter (§5); or
  - (ii) a **frame-choosing gauge structure**, which re-imports a preferred frame into the gravity sector (X2); or
  - (iii) **tunings**: m_g, Λ and at least one scalar-sector ratio, with 5 by codimension. That is fewer than ℤ⁴'s 11, with **no speed or anisotropy tunings**, but only if (E2) is supplied, i.e. orbit-weight sum rules that must be protected or tuned (R3-1).
