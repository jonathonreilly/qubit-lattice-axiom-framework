# C5 R15-3: graviton production, the auxiliary-irrep escape from X-G / G-mix

**Worker.** Claude Opus 5.5 (same family as the supervisor and every C5 worker). 2026-10-12, 21:40Z to about 22:10Z. **Unrefereed.** I edited no repository file. Scripts and outputs are in `S/scripts/` (s1–s4 and s2b). Every run took under 2 s on 2 threads.

**Paths.**
- `P/` = `.claude/science/exercises/gravity-current-state-20261009/`
- `TESTS` = `P/TESTS.md`. The R15-3 registration is at `TESTS:4954-4962`.
- `vR13-2` = `P/agents/C5_R13-2_referee_verdict.md`
- `R14-4` = `P/agents/C5_R14-4_report.md`
- `vR14-4` = `scratchpad/C5/ref_R14-4/REFEREE_VERDICT.md`. It reads CONFIRMED WITH CORRECTIONS, EXCLUDED in 𝒢_mix, and is not yet recorded in TESTS.
- `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`
- `S` = `scratchpad/C5/R15-3/`

**Labels.**
- proved = a derivation made here (unrefereed)
- checked = numerics run here
- suggested = an argument, not a proof
- reading = an interpretation
- comparator = literature. RECALLED means taken from memory and not verified.

---

## 0. Plain words

- **The question.** With only the six metric pairs, a stable local Gaussian can't give two light-like graviton polarizations without extra gapless modes ("partners"). X-G and G-mix showed this. Can extra fields (vectors, scalars, a second tensor, or any other cubic irrep) absorb the partners?
- **Answer: no.** The proof is short and uses almost nothing: no locality, no C², no mixing assumptions. Only symmetry and continuity at k = 0 enter.
- **Why.** The cubic lattice sees a mode's helicity only partially:
  - along an axis, modulo 4;
  - along a face diagonal, modulo 2;
  - along a body diagonal, modulo 3.
- **The k = 0 constraint.** Every gapless mode at small k must come from a field component that is gapless at k = 0, and those components carry a representation of the whole cubic group. No representation can look like "helicity ±2 only" from both an axis and a face diagonal.
- **The count.** Two light-like gravitons therefore force at least two more gapless branches, whatever auxiliary fields are added.
- **If the graviton must actually move the metric at long wavelength,** they force at least three more. That is exactly the six-pair count: two vector and one scalar partner, the same 2+2+1 content as the massless limit of Fierz–Pauli with Stückelberg fields (comparator).
- **The closest thing to a success.** Two pseudo-scalar (A2) auxiliary fields give exactly two light-like gapless modes that look like gravitons along every cubic axis.
  - Along body diagonals they are scalars.
  - Their coupling to the metric vanishes as k → 0.
  - So they are a lattice aliasing artefact, not a graviton.
- **The only way to get exactly two gapless TT branches** is a symbol that is discontinuous at k = 0: a direction-dependent mass, which is long-range non-local.

## 1. Class, target, excluded realizations

**Class 𝒜 (auxiliary Gaussians).**
- A translation-invariant, real, quadratic bosonic Hamiltonian H = ½ Σ_k z_k† 𝓗(k) z_k on Z³.
- **Finitely many canonical pairs per cell, in any real representation of the proper cubic group O** (`AX:37-41,57-58`), at any positions in the cell. This means the six h pairs plus any auxiliary content: vectors, scalars, pseudo-scalars, second tensors, T1/T2/A2, and so on.
- **Conditions on 𝓗:**
  - 𝓗(k) ⪰ 0 (PSD);
  - 𝓗(−k) = 𝓗(k)*;
  - O-covariant;
  - **continuous at k = 0** along the rays used. No locality, no C², and no analyticity is assumed for Theorem C.
- Arbitrary mixing is allowed: q–q, q–p, on-site, parity-odd, time-reversal-odd.

**Gapless branch (strict reading, N1).** A branch whose eigenvalue of iJ𝓗(k) tends to 0 as k → 0. This includes flat (ω ≡ 0) and o(k) branches. It is the campaign's usage of "partner": X-G's "scalar zero-frequency partner at k = 0" (`TESTS:4760-4762`), and the registered phrase "only the two TT branches gapless" (`TESTS:4960`).

**TT branch along a symmetric direction k̂.**
- Its frequency is positive for small |k| along k̂ and −k̂.
- Its positive-frequency eigenvector carries the stabilizer character of TT(k̂) ⊂ Sym². These characters are (s1, checked):
  - along a C4 axis: −1, −1;
  - along a C3 body diagonal: ω, ω̄;
  - along a C2′ face diagonal: +1, +1.
- This is implied whenever the branch's h-component is nonzero and TT.

**Excluded realizations.**
- Exact constraints, or indefinite IR theories (P-N3″, lane R's N-type, Gu–Wen).
- Non-Gaussian and strongly coupled phases.
- Infinitely many modes per cell (baths).
- Fermionic auxiliaries.
- A metric that is non-linear in the fields.
- Matter, nonlinear gravity, Λ.

## 2. Prior art (each counted once)

1. **R13-2 and its verdict.**
   - Lemma P holds for exactly six pairs.
   - The referee names this item's loophole exactly: "other cubic irreps can subduce into the axial TT sectors, and a gapless auxiliary branch can have vanishing TT residue as k→0" (`vR13-2:13`).
   - The open list includes auxiliary irreps (`vR13-2:25`, `TESTS:4764`).
2. **R14-4 and its verdict.**
   - G-mix is EXCLUDED in 𝒢_mix (`vR14-4:38-40`).
   - The weakened target is "two linear TT along one axis, ≤ 2 linear everywhere" (`R14-4:32`).
   - The price table lists auxiliary irreps as open (`R14-4:149`).
   - It names k²P_TT(k̂) as the non-local "symbol that works" (`R14-4:138`).
3. **Lane R / R2.**
   - Strong-class S, S-tl, V and V-tl have 5, 4, 3 and 2 modes (`TESTS:752`).
   - "Scalar charge gives linear TT modes only together with gapless partners" (`TESTS:753`).
   - PR #9363 probe 11: "a first-order (linear) spin-2 mode carries helicity-1 partners" (`P/agents/R2_report.md:23`).
   - The exact-constraint weak VS/N-type theory has two linear TT modes but lies outside PSD Gaussians (`TESTS:759`).
4. **The 09-14 note.** It warns that eliminating auxiliaries must preserve its hypotheses (`docs/LOCAL_FINITE_CLOCK_TENSOR_CONSTRAINTS_…_2026-09-14.md:255-259`).
5. **Comparators.**
   - **Gu–Wen, arXiv:0907.1203** (verified, abstract). L-type: helicity ±2 only, ε ∝ k³, semiclassical. N-type: ω ∝ k, uncontrolled. Both are constrained (gauge) models, outside 𝒜.
   - **Hinterbichler, arXiv:1105.3735.** §4.2 "Graviton Stückelberg and origin of the vDVZ discontinuity" was verified as a heading. The 2+2+1 helicity content of the m → 0 limit is RECALLED.
   - **Rasmussen–You–Xu, arXiv:1601.08235** (verified, abstract). Graviton-like algebraic Bose liquids are stable gauge phases. The abstract gives no dispersion or partner data.
   - **Xu 2006; Pretko 2017** (RECALLED; not load-bearing).

**Repo grep.** I grepped `TESTS.md`, `P/agents`, `docs/*.md` for "auxiliar", "Stückelberg", "A2u", "character" in the graviton context. Beyond items 1–4, the only hits concern matter or Ward-completion Stückelberg (lane RW/RFW, `TESTS:1615,2291`), which is a different question.

## 3. Theorem C (proved, unrefereed; checked s1)

**Setup.**
- Let G = the generalized kernel of J𝓗(0): the k = 0 soft space. It is an O-invariant symplectic subspace, and dim G = 2 × (number of gapless branches).
- Let k̂ be a symmetric direction with stabilizer S_k̂ ⊂ O.

**Step 1: characters at small k equal characters of G (Kato).**
- The eigenvalues of J𝓗(tk̂) near 0 form an isolated group for small t. Their Riesz projection P(t) is continuous, and P(0) projects onto G.
- S_k̂ commutes with J𝓗(tk̂).
- The character tr ρ(g)P(t) is continuous and takes finitely many values, so it is constant.
- Hence the S_k̂-character of the gapless space at small t equals that of G.
- For PSD 𝓗, the nonzero eigenvalues are real and semisimple. (Proof: iJ𝓗 is 𝓗-self-adjoint, and v†𝓗v > 0 on any eigenvector with λ ≠ 0, which excludes Jordan chains.)
- So for t > 0 the gapless space is spanned by:
  - the positive-frequency eigenvectors of the gapless branches at tk̂;
  - the conjugates of those at −tk̂.

  This uses the R14-4 referee's ±k pairing correction (`vR14-4:17-19`).

**Step 2: characters forced by TT.**
- Along ẑ, two TT branches put 4 vectors with C4-eigenvalue −1 in G.
- Along (110), they put 4 vectors with C2′-eigenvalue +1 in G.

**Step 3: per-irrep inequality.**
- In every irrep ρ of O: (multiplicity of −1 under C4) + (multiplicity of +1 under C2′) ≤ dim ρ.
- The values are A1 0+1, A2 1+0, E 1+1, T1 0+1 ≤ 3, T2 1+2 (s1, checked; explicit irreps verified as homomorphisms with ⟨χ,χ⟩ = 1).
- Summing over the irreps in G gives dim G ≥ 8.

**Theorem C.** In class 𝒜:

- **(i)** If two branches are TT along a C4 axis and along a C2′ face diagonal, there are **at least 4 gapless branches** (dim G ≥ 8). So at least 2 partners are present for every auxiliary content. "Exactly two gapless TT branches" is impossible.
  - Adding the C3 condition leaves the bound at 8.
  - The minimal soft contents are 4E, 2A2+2T2 and 2A1+2A2+2E (s1).
- **(ii)** Suppose, in addition, that the metric is any linear local Sym²-valued field (the h pairs, or any equivariant combination), and both axial TT polarizations keep a nonvanishing TT weight as k → 0. Then **at least 5 gapless branches** are present: G ⊇ 2E ⊕ 2T2, at least 3 partners. Auxiliaries cannot lower the six-pair partner count.
  - *Proof.* The limit eigenvectors lie in N = ker 𝓗(0) ⊂ G. The h-projection of N is an O-subrep of Sym² = A1 ⊕ E ⊕ T2 (multiplicity-free), and TT(ẑ) = span{E-component h_xx−h_yy, T2-component h_xy}, so N ⊇ E ⊕ T2.
  - G is symplectic, and O's irreps are all of real type, so every irrep in G appears with even multiplicity. (The invariant 2-forms on nρ are Λ²Rⁿ ⊗ (invariant inner product), which are nondegenerate only for n even.) ∎
  - The bound is attained by the refereed strong-class S model, which has 5 linear modes (`TESTS:752`).
- **(iii)** TT characters on C4 axes alone allow exactly two gapless branches, with G = 4A2. The bound is attained by model M1 (§4).
  - So R14-4's weakened target (`R14-4:32`) is **not** excluded once auxiliaries are allowed.
  - Any auxiliary no-go must use off-axis polarization.

**Bound summary (s1, checked).**

| TT characters required on | min dim G | gapless branches | partners |
|---|---|---|---|
| C4 axes only | 4 | 2 | 0 |
| C4 + C3 | 6 | 3 | 1 |
| C4 + C2′ (or all three) | 8 | 4 | 2 |
| all three + h-TT weight on z | 10 | 5 | 3 |

**What Theorem C does not use:**
- locality, C² or C⁴ (only continuity at k = 0 along the rays);
- inversion or time reversal;
- the form of the mixing;
- whether partners are linear, flat or o(k).

**What it needs:**
- PSD;
- finitely many pairs per cell;
- O-covariance;
- the strict N1 notion of "gapless".

## 4. The PRODUCED direction: what was built (checked, s2, s2b, s4)

**M1: the A2 near miss** (`s2_models.out`, block M1).
- *The model.* Six h pairs, gapped (½E:E + ½h:h). Two A2 pseudo-scalar pairs (a₁, a₂) with ½p² + ½c_α Σ_i(∇_i a_α)². They couple to h as follows:
  - a₁ through g₁ a₁ (D_x h_yz + D_y h_zx + D_z h_xy), at O(k) via T2;
  - a₂ through g₂ a₂ [e₁(Δ)ε₂(h) − e₂(Δ)ε₁(h)], at O(k²): the antisymmetric E⊗E → A2 pairing of the second-difference symbol with h's E part.
- *PSD check.* PSD holds on a 24³ zone grid (min eigenvalue 0.047) and in a small-k radial scan (min eig/|k|² = 0.67).
- **Exactly two gapless branches in every direction tested** (z, x, 111, 110, two generic). Both are linear: ω/|k| = 0.83666 and 0.97724, unchanged between |k| = 1e-3 and 2e-3.
- *Stabilizer characters:*
  - along axes, (−1, −1), which is TT;
  - along (111), (+1, +1), which is helicity 0;
  - along (110), (−1, −1), which is odd helicity.
- *h-TT weight along z.* It is 0.045 k² for a₁ and 0.06 k⁴ for a₂ (s2b, |k| = 1e-3 to 1e-1). Both vanish as k → 0.
- *TT fraction of the h-part:* 0 along (111) and (110).
- *Reading.* Two scalars that the cubic group mistakes for helicity 2 along axes. This is not a graviton: it fails off-axis polarization and the metric residue.

**M2: character-sharp 4-branch model** (s2, soft content 2A2 + 2T2).
- *The model.* A2 aux plus h's T2 part, with h's A1 and E parts gapped.
- *PSD check.* Grid min eigenvalue 0.041; small-k min eig/|k|² = 0.59.
- *Branches.* 4 linear gapless branches everywhere.
- *Characters.* TT characters are present on all three symmetric directions:
  - C4: {−1, −1, ±i};
  - C3: {ω, ω̄, +1, +1};
  - C2′: {+1, +1, −1, −1}.
- This shows the bound in (i) is attained. The TT characters are not exactly TT h-parts, though: along (110) one +1 branch has TT fraction 0.25.
- *A side check (M2-bad).* An O(k) coupling between two *soft* sectors breaks PSD (min eig/|k|² = −2.1e3). Soft–soft couplings must be O(k²), and A2 couples to T2 only at odd degree, first at O(k³).

**Vector or scalar compensators (Stückelberg type) and second tensors.**
- These are covered by (i) and (ii): their soft content adds irreps and can only raise dim G.
- *Comparator.* The m → 0 limit of Fierz–Pauli with Stückelberg fields keeps 2+2+1 helicities, i.e. 5 gapless modes, matching (ii) (RECALLED content).
- *Suggested, not proved.* A local Stückelberg Gaussian such as k²|h − sym(k⊗u) − δφ|² enters the soft theory only through its degree-2 part. The u-dependence first appears at O(k³)–O(k⁴) in the symbol. So at linear order u decouples, and the helicity-1 sector keeps a branch with ω ≈ |k|.

**Non-local symbols (s4).** These are the only exhibits with exactly two gapless TT branches.
- **X1 = R14-4's k²P_TT(k̂).** It has 2 linear plus **4 flat free-particle partners**: 6 gapless branches in all 6 directions. So under the registered strict reading it is *not* "the symbol that works" (correction to the scope of `R14-4:138,148`).
- **X2 = k² + m²(1 − P_TT(k̂)).** It has exactly 2 gapless linear TT branches, with the partners gapped at m, in all 6 directions. But ‖𝓗(10⁻⁸ẑ) − 𝓗(10⁻⁸x̂)‖ = 1.87: it is **discontinuous at k = 0**.
  - Its real-space kernel is homogeneous of degree 0 in k, so it decays as r⁻³ after subtracting the angular-average contact term (RECALLED).
  - This is the exact boundary of Theorem C's continuity hypothesis.

**Finite-slot realization.** Moot for PRODUCED.
- *Suggested:* spin-wave Gaussians of finite-slot models have finitely many pairs per cell and continuous symbols, so they lie in 𝒜 and Theorem C applies to them.

## 5. The flat-partner (gauge-tolerant, N2) question

This is not the registered reading. It is reported because it is where a graviton could still hide.

- **Lemma N (proved, unrefereed; s3 exact).** Take the soft class S0:
  - ker 𝓗(0) isotropic (every soft mode of free-particle type);
  - a C² symbol;
  - no O(k) q–p cross term in the soft sector. This holds, for example, for every time-reversal-invariant model with q even and p odd.

  In S0, let the metric be any linear local field, and let every Θ(k) branch have an exactly-TT leading h-part. Then every leading h-part vanishes. Other branches may be flat or o(k).
- *Proof.* The soft theory is ½eK₀e + ½qV(k)q with V a degree-2 polynomial; this is R14-4 Step 4 (`R14-4:64-76`), refereed with corrections (`vR14-4:9-15`), and extended here to auxiliary soft content by the same block reduction (suggested, not written out).
  - The linear modes' q-parts span K₀·range V(k̂).
  - So their leading h-parts span the image of Λ₀K₀V(k): a matrix whose columns are degree-2 polynomial Sym²-valued fields.
  - If every leading h-part is TT, each column is a polynomial TT field of degree 2.
  - s3 (exact sympy rank) shows the dimension of polynomial TT fields by degree d = 0, 1, 2, 3, 4 is **0, 0, 0, 5, 12**. Transverse-only fields exist from d = 2 (6 of them), so tracelessness is load-bearing.
  - Hence the columns vanish. ∎
- **Consequence.** In S0, accepting flat partners as gauge does not help, for any auxiliary content. This generalizes Lemma V/G-mix with polarization in place of rank.
- **Still open in N2.** The gyroscopic case (O(k) q–p terms, parity- and time-reversal-odd). The axioms allow it (`AX:37-38`).
  - *Proved:* the pure-cyclotron sub-case (V̂ = 0 on the relevant sector) is excluded by the degree-1 count, which is 0.
  - The mixed case P(λ) = −λ²M + λĜ + V̂ is not closed: the image argument fails, because each root fixes only one vector.

## 6. Prices (named, never adopted)

| Escape left | Axiom touched | Status |
|---|---|---|
| O(1) direction-dependent symbol (X2; discontinuous at k = 0; r⁻³ tail, RECALLED) | Admissibility nearest-neighbour locality `AX:57-58` | the only exhibited exact target; worse than R14-4's "fails C²" price |
| Flat partners accepted as gauge: needs exact constraints or an indefinite IR (lane R N-type, Gu–Wen, P-N3″) | a redundancy among records, not in the axioms (lane R price) | outside 𝒜; lane R open (`TESTS:759`) |
| Gyroscopic (time-reversal-odd) soft mixing with flat partners | none (proper-rotation-only already allows it) | open (N2 only) |
| Non-Gaussian / strong coupling | none | open (R13-2's window) |
| Decoupled ("dark") gapless partners tolerated physically | none; observational (extra radiation) | a reading, not tested |

## 7. Readings against the FIXED clauses (`TESTS:4958-4962`)

- **PRODUCED: no.**
  - Theorem C(i) rules it out for every finite auxiliary content, local or not, provided the symbol is continuous at k = 0.
  - The only exhibit meeting "only the two TT branches gapless and linear" is X2, which is non-local at O(1) and so not "local".
- **EXCLUDED: candidate, unrefereed.** Theorem C covers the stated class 𝒜:
  - any finite set of auxiliary pairs in any O-irreps;
  - any mixing;
  - PSD, with continuity at k = 0;
  - the strict gapless definition.

  Strongest form:
  - at least 4 gapless branches (characters alone);
  - at least 5 if the graviton moves the metric at long wavelength, which is the six-pair count.
- **Overall worker reading: OPEN by the fixed rule until refereed; EXCLUDED if confirmed.**
- **Perturbative order.** No PRODUCED is claimed. Theorem C is exact at Gaussian order and uses 𝓗 only through its k → 0 limit. Lemma N uses the symbol through O(k²).

## 8. Strong-word check and scope

- **"Proved" covers:**
  - Theorem C: Kato projection continuity, constant characters, PSD semisimplicity, the per-irrep inequality, and the even-multiplicity lemma;
  - (ii)'s projection argument;
  - Lemma N, given the soft reduction.
- **"Checked" covers:**
  - s1 character tables and the minimal-G enumeration;
  - s2/s2b spectra, PSD margins (sampled grids, not certified) and characters;
  - s3 exact ranks;
  - s4.
- **The weakest step.** Lemma N's extension of R14-4's soft reduction to auxiliary soft content: soft–soft couplings, hard auxiliaries and Schur terms. It is suggested by the same block argument but not written out. Theorem C does not depend on it.
- **"Any auxiliary" means:** finitely many bosonic pairs per cell, Gaussian, PSD, O-covariant, symbol continuous at k = 0.
- **Not covered:**
  - exact constraints or indefinite theories;
  - non-Gaussian phases;
  - baths (infinitely many modes);
  - fermions;
  - a non-linear metric;
  - discontinuous symbols (X2 shows that hypothesis is sharp).
- **The N1/N2 distinction is a reading choice made explicit here.** The registration's wording is N1. Under N2, only S0 is closed (Lemma N) and the gyroscopic corner is open.

## Files (`S/scripts/`)

- `common.py`: the group O, explicit irreps, the Sym² action, TT projectors.
- `s1_characters.py/.out`: irrep checks, stabilizer eigenvalues, TT/helicity characters, minimal-G enumeration (the table in §3).
- `s2_models.py/.out`: M1 (A2 near miss), M2-bad (non-PSD diagnostic), M2 (4-branch character-sharp model).
- `s2b_residue_scaling.py/.out`: M1 h-TT weights ∝ k² and k⁴.
- `s3_poly_tt.py/.out`: exact dimensions of polynomial transverse and TT fields by degree, for Lemma N.
- `s4_nonlocal_exhibits.py/.out`: X1 (k²P_TT: 2 linear + 4 flat) and X2 (discontinuous: exactly 2).
