# Complete corrected argument: Heat-kernel saddle and Wilson matching coefficients

This is inspectable mathematical source. The canonical claim is limited to: Result1–7, small-field derivation and coefficient comparison.

**Deferred continuation:** Physical scale identification or inference of a scheme-independent Lambda ratio from the top-eigenvalue floor. Complete arguments are retained below, but terminal negative conclusions are not promoted until the required residual-matched packet is supplied and reviewed. This does not make the exact identities uncertain. Historical verification statements below describe the original campaign, not a fresh capture or audit verdict.


# Heat-kernel saddle versus Wilson: the one-loop Λ ratio, and the two-dimensional 7/4

**Date:** 2026-10-18
**Type:** bounded_theorem
**Status:** bounded support, unaudited. Exact group-theory statements, a one-loop perturbative coupling map with numerical certificates, and an exact two-dimensional check. Nothing is adopted.

## Question

The scale-ladder probe of the native transfer lane (campaign `toe-campaign-20261017/scale_ladder_probes/gravity_gauge/REPORT.md`, item T3) found that matching the fundamental character of the Wilson single-plaquette weight to a heat kernel gives τ_eff = (3/β)(1 + 7/(4β) + O(β⁻²)) for SU(3). It called the 1/β coefficient "scheme", left its relation to the repo's ≥ 7/16 coefficient unchecked, and proposed P-T3: the one-loop Λ ratio between the native and Wilson actions.

Which comparison is nontrivial, what is that Λ ratio, and what is the 7/4?

## Result

1. **Native versus Wilson is trivial.**
   - The native packet operator's recurrence J = (χ_F + χ_F̄)/6 is the Pieri rule for SU(3) characters. Hence c_p(β) = ⟨p|exp(βJ)|0⟩ are exactly the character coefficients of exp[(β/3) Re tr U], the Wilson weight at β_W = β.
   - This is the existing β identification, rechecked. The Λ ratio of the native operator to Wilson is 1.
2. **The nontrivial comparison is the saddle.**
   - The large-β saddle multiplier d_λ exp(−3C₂(λ)/β) of the native lane is the heat-kernel (Menotti–Onofri) weight with τ = 3/β.
   - For SU(3), g² = 6/β, so τ = g²/2. This is the tree-level match: both weights give g⁻² trX².
3. **Heat-kernel small-field expansion.**
   - Up to exponentially small winding terms, −log w_HK = trX²/(2τ) − Σ_{i<j} log(θ_ij/sin θ_ij) + const. Here θ_ij = (x_i − x_j)/2, with x_i the eigenvalues of X.
   - Since Σ_{i<j} θ_ij²/6 = N trX²/24, the trX² coefficient is 1/(2τ) − N/24.
   - The quartic terms are τ-independent, O(g⁰). There is no O(1/g²) quartic term.
   - Wilson has −log w_W = const + g⁻²[trX² − trX⁴/12] + O(X⁶/g²).
4. **The one-loop shift.** Write g_HK⁻² = g_W⁻² + c(d) for the two couplings with the same long-distance physics. Then
   - c(d) = N/24 − (2/d)(2N² − 3)/(12N) = (dN² − 8N² + 12)/(24Nd).
   - In d = 4, c = (3 − N²)/(24N). For SU(3) that is c = −1/12, so β_HK = β_W − 1/2.
5. **The Λ ratio in four dimensions.** With b₀ = 11N/(48π²),
   - Λ_HK/Λ_W = exp(−c/(2b₀)) = exp[π²(N² − 3)/(11N²)].
   - That is 1.2515 for SU(2), 1.8188 for SU(3) and 2.0730 for SU(4).
6. **The probe's 7/4 is the d = 2 shift.**
   - In two dimensions single-plaquette weights factorise. So matching the fundamental coefficient a_F exactly gives the exact coupling map, and k = −2N c(2) = (N² − 2)/4.
   - That gives k = 1/2, 7/4 and 7/2 for N = 2, 3, 4. Exact character coefficients confirm all three, by Bessel determinants and separately by Weyl integration. These are numerical certificates (Richardson extrapolation over β = 100–1600), not proofs.
   - For SU(3) in d = 2, β_HK − β_W = 2N c(2) = −7/4. In four dimensions the tadpole halves (w = g²/2 instead of g²) and the shift becomes −1/2. So the probe's 7/4 is a d = 2 number, not the 4D shift.
7. **The repo multiplier contains the same 7/4.**
   - At fixed Q, β^{−3/2} d_λ exp[−τ_eff C₂ + (9/4)C₂²/β³] = W[1 + (3 − 7Q/4 + Q²/4)/β + O(β⁻²)], with τ_eff = (3/β)(1 + 7/(4β)). This is the proved multiplier W2 of the second-order multiplier note.
   - So W2 = saddle scalar 3 (from 3C₂/β = Q − 3/β) + the d = 2 shift −7Q/4 + a non-Casimir residue Q²/4.
   - The residue predicts β³[log a_λ − (C₂/C_F) log a_F] → (9/4)(C₂² − C₂C_F) = 11.25, 15, 63, 120 for the 8, 6, 10, 27. The probe's columns at finite β (11.5, 15.4, 64.5, 122.7) are these plus O(1/β); Richardson extrapolation of direct Weyl integration gives the limits. The prediction is read off W2, not fitted to the probe.
   - W2 is proved by Fourier-integral asymptotics of the native coefficients, a different route from the tadpole formula and from the numerical matching. Since it is a single-plaquette expansion, it independently confirms the single-plaquette 1/β coefficient 7/4, which by 2D factorisation is the d = 2 coupling shift.

The two dimensions compared:

| | d = 2 | d = 4 |
|---|---|---|
| tadpole w/g² | 1 | 1/2 |
| c(d), general N | −(N² − 2)/(8N) | (3 − N²)/(24N) |
| SU(3): c | −7/24 | −1/12 |
| SU(3): β_HK − β_W = 2N c | −7/4 | −1/2 |

## The ≥ 7/16 coefficient is a different quantity

The full-top note proves λ_top(A_β) = μ + c_full/β + o(β⁻¹) with c_full/μ ≥ 7/16 for the normalized native packet operator A_β = exp(−β) β^{−3/2} T_β.

- **What it is.** A first inverse-β correction to the top eigenvalue of one operator at one coupling, in a chosen normalization (exp(−β) β^{−3/2}, the shifted chamber and the h = β^{−1/2} scaling). Multiplying the normalization by (1 + a/β) shifts c_full by aμ. It is a spectral functional of the Perron vector, not a map between two couplings that give the same long-distance physics.
- **What it is not.** It is not a coefficient of trF² in an effective action, so it cannot be converted into a Λ ratio.
- **How the 7/4 enters it.** The −7Q/4 of W2 enters d₀, and hence c_full. If W2 − 3W had Q-coefficient −k_s, the same completing-the-square bound would give floor(k_s) = 105/32 − 3k_s/4 − k_s²/2, which is 7/16 at k_s = 7/4 (checked symbolically). So the d = 2 shift feeds the floor, mixed with the saddle scalar 3 and the heat correction ‖Lφ‖²/4. The floor is not a scheme-independent quantity.

## How this bears on the lane (interpretation, not a claim)

- The probe's P-T3 is answered at one loop: the native operator and Wilson are the same action, and the heat-kernel saddle is the action whose Λ differs, by a factor 1.82 for SU(3).
- A 1/β coefficient of a single-plaquette quantity is scheme in four dimensions. It becomes a coupling map only through the dimension-dependent tadpole. The exact 2D map is not the 4D one.
- If the recalled Hasenfratz–Hasenfratz form is right, the non-planar 1/(8N) term of Λ_MS/Λ_W cancels for the heat kernel, leaving Λ_MS/Λ_HK = 38.853·e^{−π²/11} ≈ 15.84 for every N. This is a structural observation with a recalled input, not a confirmation.
- The Hamiltonian (a_t → 0) variant, with Kogut–Susskind electric term and magnetic plaquette function only, gives c_H ≈ −0.1033 and a ratio ≈ 2.10 for SU(3), with a one-loop speed-of-light shift ≈ −0.207 g² that must be retuned. This is provisional and was not independently checked.

## Premises

- **Axioms used.** None beyond the definitions of the native packet operator in the cited notes.
- **Supplied.**
  - The Wilson action as comparator and the heat-kernel weight as the identified saddle multiplier.
  - Weak-coupling perturbation theory: two plaquette actions with the same tree-level term describe the same long-distance physics when their one-loop effective trF² coefficients agree; Λ is fixed by g⁻² through the universal b₀ (and b₁, which cancels in the ratio).
  - The matching uses the background-field tadpole of the plaquette-function difference. Both weights are invariant under U → U⁻¹, so there are no odd terms in X; the X⁶ terms contribute at two loops.
- **Standard facts used.**
  - The Pieri rule for SU(3) characters; Weyl dimension and Casimir formulas.
  - The closed form of the group heat kernel (Eskin).
  - b₀ = 11N/(48π²).

## Relation to prior work

- **Heat-kernel action.** Menotti and Onofri, NPB 190 (1981) 288. Their Λ ratio was not retrieved, so it is not compared here. The 4D closed form may already be there; novelty is not claimed for it.
- **Comparisons of lattice actions.** Lang, Rebbi, Salomonson and Skagerstam, PLB 101B (1981) 173. Not retrieved.
- **Wilson to MS-bar.** A. Hasenfratz and P. Hasenfratz (1980): Λ_MS/Λ_W = 38.853·exp(−3π²/(11N²)), giving 28.81 for SU(3) and 19.82 for SU(2). Recalled from memory, not retrieved. Used only for the structural observation above.
- **Repo.**
  - The β-identification note: the native β is the Wilson bare coupling.
  - Rung six and the A2 reflection theorem: the saddle multiplier d exp(−3C₂/β).
  - The second-order multiplier note: W2 = (3 − 7Q/4 + Q²/4)W, proved for β ≥ 2048.
  - The full-top note: c_full/μ ≥ 7/16.
  - The action-form no-go and the heat-kernel uniqueness notes: Wilson and heat kernel are distinct functionals; the heat kernel is the unique diffusion kernel among the candidates.
  - The scale-ladder cross-rung note (2026-10-18) records this result in its native-transfer row as unreviewed; this note supplies it.
- **New here.**
  - Recognising that the native-versus-Wilson comparison is trivial and the nontrivial one is the saddle.
  - The general-d shift c(d) and the identification of the probe's 7/4 as its d = 2 value.
  - The decomposition of the repo's W2 into saddle scalar, d = 2 shift and non-Casimir residue.
  - The explanation of the ≥ 7/16 coefficient as a spectral, normalization-dependent quantity.

## Historical packet proposal (promotion deferred)

- **N1 — routes.** Only the one-loop tadpole of the plaquette-function difference is used in 4D. A full background-field computation, a lattice Monte Carlo comparison of β_HK and β_W, and the literature value were not done.
- **N2/N3 — scope.** One loop; plaquette actions only; SU(N) with N = 2, 3, 4 evaluated. d = 2 is exact for single-plaquette weights.
- **N4 — inputs.** The 4D tadpole w = (2/d)g² is computed two ways: projector diagonal on tori and momentum sum. The heat-kernel expansion is checked against character sums. The d = 2 coefficients use Richardson extrapolation of exact coefficients; they are numerical certificates, not proofs.
- **N5 — wording.** "Λ ratio" means the one-loop ratio at equal long-distance physics. "Scheme" means removable by a coupling redefinition.
- **N6/N7 — strongest objections.**
  - The 4D result uses the same structural method in both the work and the check; no independent background-field calculation was done.
  - The literature values were not retrieved.
  - The negative statement about the ≥ 7/16 coefficient is a category statement (it is not an effective-action coefficient), not an impossibility theorem.
- **N8 — earlier claims.** The probe's "7/4 is scheme" is sharpened: it is the exact d = 2 coupling map. The full-top theorem is unchanged.

## Historical checking narrative (not fresh evidence)

Provenance: the check was run by a fresh-context agent of the same model family as the author. It is independent only in code path. It is not a different-model review.

- **B12_check** (campaign `scale-ladder-campaign-20261018/B12_check/REPORT.md`).
  - It confirmed w = (2/d)g² with a gauge-invariant plaquette projector on L^d tori, with no gauge fixing. It reproduced the textbook ⟨1 − P⟩ = (N² − 1)g²/(8N) in 4D.
  - It confirmed the heat-kernel trX² coefficient 1/(2τ) − N/24 to 1e−5 by direct fits to character sums, with a τ-independent (trX²)² coefficient.
  - It derived c(d) by an independent symbolic contraction (Σ_a T^a M T^a = (tr M − M/N)/2) and confirmed the Λ ratios 1.8188, 1.2515 and 2.0730.
  - It confirmed k = 0.5, 1.75 and 3.5 by direct Weyl integration rather than Bessel determinants, reproduced W2, and extrapolated the residues to 11.25, 15, 63 and 120.
  - Limits: the 4D one-loop result uses the same structural method; the Hamiltonian variant was not checked; the literature could not be retrieved.
- **This runner.** It is a consolidated adaptation of the author's and checker's code. It adds the Pieri-rule and native-recurrence checks (Part A) and the symbolic W2 and 7/16 algebra (Part E). It is not a further independent check.

## Historical execution record (not a fresh capture)

```bash
python3 scripts/heat_kernel_saddle_versus_wilson_one_loop_lambda_ratio_2026_10_18.py
```

Expected: `TOTAL: PASS=42 FAIL=0` (about 4 minutes).

## Load-bearing sources

- A2 reflection theorem (2026-09-02) (`docs/NATIVE_GAUGE_TRANSFER_A2_REFLECTION_UNIFORM_HALF_LINE_GAP_THEOREM_NOTE_2026-09-02.md`)
- Second-order multiplier W2 (2026-09-07) (`docs/NATIVE_GAUGE_TRANSFER_WILSON_SECOND_ORDER_MULTIPLIER_BOUNDED_THEOREM_NOTE_2026-09-07.md`)
- Full top second order, ≥ 7/16 (2026-09-07) (`docs/NATIVE_GAUGE_TRANSFER_FULL_TOP_SECOND_ORDER_BOUNDED_THEOREM_NOTE_2026-09-07.md`)
- Large-β gap rung six, saddle multiplier (2026-06-12) (`docs/NATIVE_GAUGE_TRANSFER_LARGE_BETA_GAP_RUNG_SIX_BOUNDED_NOTE_2026-06-12.md`)
- β identification (2026-06-12) (`docs/NATIVE_GAUGE_TRANSFER_BETA_IDENTIFICATION_PHYSICAL_PLAQUETTE_RELATIONSHIP_BOUNDED_NOTE_2026-06-12.md`)
- Character recurrence (`docs/GAUGE_VACUUM_PLAQUETTE_TRANSFER_OPERATOR_CHARACTER_RECURRENCE_NOTE.md`)
- Heat-kernel uniqueness among candidate actions (2026-06-08) (`docs/HEAT_KERNEL_UNIQUE_DIFFUSION_KERNEL_AMONG_CANDIDATE_GAUGE_ACTIONS_NARROW_THEOREM_NOTE_2026-06-08.md`)
- Action-form uniqueness no-go (2026-05-06) (`docs/BRIDGE_GAP_ACTION_FORM_UNIQUENESS_NO_GO_NOTE_2026-05-06.md`)
- Scale-ladder cross-rung invariants (2026-10-18) (`docs/SCALE_LADDER_CROSS_RUNG_INVARIANTS_CORNER_FERMION_BOUNDED_THEOREM_NOTE_2026-10-18.md`)
- Axioms (`docs/MINIMAL_AXIOMS_2026-06-29.md`)
