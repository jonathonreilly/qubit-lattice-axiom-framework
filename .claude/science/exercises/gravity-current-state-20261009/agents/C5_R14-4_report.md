# C5 R14-4: graviton production, the mixed h–E kernel escape from X-G

**Worker.** Claude Opus 5.5 (same family as the supervisor and every C5 worker). 2026-10-12, 21:14Z to about 21:45Z. **Unrefereed.** No repository file edited. Scripts and outputs: `S/scripts/` (s1–s8; every run under 1 min on 2 threads).

**Paths.** `P/` = `.claude/science/exercises/gravity-current-state-20261009/`. `TESTS` = `P/TESTS.md` (R14-4 registration `TESTS:4858-4870`). `R13-2` = `P/agents/C5_R13-2_report.md`; `vR13-2` = `P/agents/C5_R13-2_referee_verdict.md`. `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`. `S` = `scratchpad/C5/R14-4/`.

**Labels.** proved = derivation here (unrefereed); checked = numerics here; suggested = argument; reading = interpretation; comparator = literature (RECALLED).

---

## 0. Plain words

- **The question.** X-G (refereed) says a stable local Gaussian of the six tensor pairs can't give two light-like graviton polarizations without gapless partners, *if* the partners are made flat by a gauge-type kernel on one side (h only or E only). The open door was to let h and E mix, so the flat directions are mixtures of the two. Does that rescue the graviton?
- **Answer: no (proved, unrefereed), and the no-go is wider than X-G.** Any mixing works in two ways:
  - an on-site, k-independent mixing can be rotated away exactly;
  - an O(k) mixing (allowed because the axioms grant proper rotations only, so parity-odd terms are legal) acts like a magnetic, gyroscopic force. That can only add moving modes, never remove them.
- So everything comes down to one 5×5 "stiffness" matrix V(k) on the traceless tensors. It is quadratic in k and cubic-symmetric, and that family has exactly six parameters. Exact algebra shows that if V(k) has rank ≤ 2 in every direction, at most one of the two TT polarizations along an axis can have a linear dispersion.
- **Result.** Two linear TT polarizations along an axis force a third linearly dispersing branch in some direction, i.e. a gapless partner. No PSD local Gaussian with mixed kernels is the graviton. The obstruction is locality: the symbol that does the job, k²P_TT(k̂), is C¹ but not C² at k = 0.
- **By-products.**
  - An explicit nearest-neighbour model is perfect along the cubic axes: two light-like TT modes, with all partners exactly flat. Off-axis it has 4 to 5 linear branches. So the "axis-only flatness" escape is real but fails off-axis, and the theorem covers it.
  - Single-polarization local models do exist (three exact families).

## 1. Hypotheses, class, excluded realizations

- **Class 𝒢_mix.** A quadratic Hamiltonian H = ½ Σ_k z_k† 𝓗(k) z_k on exactly six canonical pairs per cell, z = (h, E), with h and E each transforming as Sym² = A1g ⊕ Eg ⊕ T2g. Conditions:
  - real (𝓗(−k) = 𝓗(k)*);
  - PSD (𝓗(k) ⪰ 0);
  - **C² at k = 0** (summable second moments; X-G used C⁴);
  - covariant under the **proper** cubic group O (24 elements, `AX:37-38,57-58`). Inversion is not assumed, so parity-odd terms are allowed.
  - **h–E mixing is unrestricted at every order** (on-site, O(k), O(k²), …).
- **Target (registered `TESTS:4863`).** Two linear (ω = Θ(|k|)) TT polarizations and no gapless partners.
  - I use the *weaker* requirement "two linear TT polarizations along one cubic axis, and at most two linear branches in every direction". A no-go under this requirement is stronger than one under the registered target.
- **Excluded, as in X-G** (`vR13-2:25`): auxiliary irreps beyond the six pairs, non-local symbols, indefinite or exactly constrained theories (P-N3″), non-Gaussian phases, matter, nonlinear gravity, Λ.

## 2. Prior art (each counted once)

1. **R13-2 + verdict.** Lemma P (confirmed for exactly six pairs, `vR13-2:11-13`); Theorem G cubic (exact, `vR13-2:15`); X-G open list, which includes "mixed h–E kernels" (`vR13-2:25`, `TESTS:4758-4772`). R13-2 suggested reducing mixed kernels by E → E + r(k)h "when r(k) is analytic; suggested, not shown" (`R13-2:106`). R13-2 also held that a semiclassical IR of a compact local model lands in 𝒢 (`R13-2:110`).
2. **Lane R / R2.** "Scalar charge gives linear TT modes only together with gapless partners" (`TESTS:753`). "Gaplessness of helicity 2 needs μ_E = μ_T2 = 0" (`P/agents/R2_report.md:114`): the same two k = 0 tunings as Lemma R below. Exact-constraint weak VS/N-type has two linear TT modes, but outside the Gaussian PSD class (`TESTS:759`).
3. **R11-2 X1** (`TESTS:4407-4409`): finite-slot exact constraints give O(k³).
4. **Comparator (RECALLED, not load-bearing).** Weinberg (1964–65) / Fierz–Pauli: a massless helicity-2 field needs gauge redundancy, and no local covariant symmetric tensor without it. The present result is a non-Lorentzian lattice Hamiltonian analogue for Gaussian theories.

No repo or packet hit for "gyroscopic", "symplectic mixing" or "Berry" in the graviton context (grep of `P/TESTS.md`, `P/agents/C5_R1[1-4]-*`, `P/agents/R2_*`, `docs/*.md`).

## 3. The reduction (proved; checked)

**Step 1 (Lemma P, refereed).**
- Two gapless axial TT branches give a zero symplectic eigenvalue in the k = 0 Eg block M_Eg and the T2g block M_T2.
- These are 2×2 real PSD forms on (h, E) per component, so each has rank ≤ 1.

**Step 2 (Lemma R; proved, checked s8).** Two *linear* TT branches along the axis need rank M_Eg = rank M_T2 = 1 exactly.
- *Proof.* Under C4 (proper only), B1 and B2 merge into one 2-pair sector B. 𝓗0 restricted to B has rank = rank M_Eg + rank M_T2. Suppose one of them is 0, so this rank is ≤ 1.
  - Factor 𝓗 = LL†, with L = L0 + O(k). This is possible because PSD forces the kernel block of 𝓗 to be O(k²).
  - The nonzero frequencies are the eigenvalues of L†iJL.
  - L0†iJL0 = 0, since L0 is rank 1 and real while J is antisymmetric.
  - The O(k) part has the form u w† + w u†. It has at most one positive eigenvalue.
  - So at most one branch has ω ≥ Ck². ∎
- *Check (s8).* With M_Eg = 0, the axial B sector has ω/|k| = 190.8 (one linear branch) and ω/|k|² = 117.09 (the other is quadratic), stable over |k| = 1e-2 to 1e-4.

**Step 3 (on-site mixing removed; proved).**
- Rotate the (h, E) plane in each irrep by its own angle. This map is on-site, O-covariant and canonical (SO(2) ⊂ Sp(2) per component).
- It sends M_Eg and M_T2 to diag(0, κ). So traceless h is soft and traceless E is hard, with K0 = κ_E P_Eg + κ_T P_T2 > 0.
- Frequencies are invariant under the map. **Every k-independent h–E mixing is disposed of here.**

**Step 4 (leading-order soft theory; proved, sketch: block reduction plus eigenvalue continuity; checked s3, s8).**
- Rescale E = k·e on the soft sector. To O(k²), the soft Hamiltonian is H̃ = ½ e K0 e + Re(e†A h) + ½ h V′ h, where:
  - A = 𝓗1_Eh is the O(k) h–E cross term. It is purely imaginary (𝓗1 = i·real antisymmetric) and parity-odd, so it is nonzero only because inversion is not assumed. It acts as a gyroscopic term.
  - V′ is the O(k²) h-block minus the O(k)-coupled hard-sector Schur term.
- **The O(k²) and higher h–E cross terms do not enter at this order.**
- Exact small-k frequencies equal k times the symplectic eigenvalues of H̃.
- The three A1g cases:
  - (i) trace pair gapped: Schur over it;
  - (ii) rank 1: rotate so h_tr is soft;
  - (iii) M_A1 = 0: the trace pair evolves at rate k² and is frozen on the Θ(k) scale, and the Θ(k) branches are those of the traceless system.
- *Checks.*
  - s3 (two seeds; mixing angles 0.89/1.19 and 0.29/0.46 rad; parity-odd content |𝓗(k) − 𝓗(−k)| ≈ 8–10 at |k| = 0.1): the exact ω/|k| at |k| = 1e-3 match the soft theory to 5.9e-5 and 1.4e-4 (relative), over 10 directions.
  - s8, case (iii): the 10 traceless branches match V2_0 theory; the trace pair has ω/|k| = 0.13 at |k| = 1e-3, so it is O(k²).

**Step 5 (counting; proved).**
- Let V2 = V′ − A†K0⁻¹A, the Schur complement. V2 is PSD, real symmetric and a degree-2 polynomial in k. It is O_h-covariant automatically, because a degree-2 form on rank-2 tensors is inversion-even.
- rank H̃ = n + rank V2. Williamson's form for PSD matrices gives rank H̃ = 2r + s with r + s ≤ n, where r is the number of positive frequencies and s the number of free-particle (Jordan) modes.
- Hence **(number of linear branches r) ≥ rank V2(k)** in every direction.
- **Gyroscopic (mixed O(k)) terms can create linear branches** (cyclotron-like, one per 2-dim sector) **but never remove them.**

**Step 6 (axis; proved).**
- In sector B at k ∥ ẑ, two linear branches means r = 2 = n_B. Then s = 0 and H̃_B is PD, so V2(ẑ)|_B is PD.
- V2(ẑ)|_B = diag(TT1, TT2) by the automatic C4v symmetry, so TT1 > 0 and TT2 > 0.
- Also, rank V2(ẑ) ≤ 2 (else the axis already has ≥ 3 linear branches). V2(ẑ) is diagonal in (T1, S, X, Y, Z), so this forces VEC = S = 0 on the axis.

## 4. Lemma V (proved, exact; s1, s2)

- **Invariant space (s1, sympy, Reynolds plus rref).** The O-covariant (equivalently O_h) degree-(2,2) forms h·V(k)·h on traceless h form a space of **dimension 6**, spanned by:
  - I1 = k²h:h;
  - I2 = |hk|²;
  - I3 = Σk_i²h_ii²;
  - I4 = Σk_i²(h²)_ii;
  - I5 = Σk_ik_j h_ij h_ii;
  - I6 = k²Σh_ii².
- On the axis, V = Σc_iI_i gives:
  - TT1 = c1 + c6;
  - TT2 = c1;
  - S = c1 + ⅔(c2+c3+c4+c5) + c6;
  - VEC = c1 + (c2+c4)/2.
- **Statement.** If VEC = S = 0 on the axis and rank V(k) ≤ 2 at the nine directions (1,1,0), (1,0,1), (0,1,1), (1,1,1), (1,2,0), (2,1,3), (1,−1,2), (3,1,2), (1,2,5), then **TT1·TT2 = 0**. PSD is not needed.
- **Proof (s2).** All 3×3 minors at the nine directions give 642 equations. Their Gröbner basis in (c2, c3, c4, c5), after the axis conditions, is printed in `s2_rank_lemma.out`. By hand:
  - (c4 − c5)²(2c4 + c5) = 0;
  - c5(2c2 + c5)² = 0;
  - c5²(2c3 − 2c4 + 5c5)(2c3 + 2c4 + c5) = 0;
  - (c4 − c5)(c3c4 + c3c5 + 2c4c5 + c5²) = 0.
- These give exactly three lines:
  - **A** = c3(0, 0, 1, 0, 0, −⅔), with TT1 = −⅔c3 and TT2 = 0;
  - **B** = c5(½, −½, 0, −½, 1, −½), with TT1 = 0 and TT2 = c5/2;
  - **C** = c5(−¼, −½, −3/2, 1, 1, ¼), with TT1 = 0 and TT2 = −c5/4.
- On every line TT1·TT2 = 0. ∎
- **The V2 used in the reduction lies in this span** (checked: fit residual 1.8e-8 and 1.1e-8 for the s3 models).

**Theorem G-mix (proved; unrefereed).** In 𝒢_mix, suppose both TT branches along a cubic axis are linear. Then in some direction (ẑ itself, or one of the nine above, and hence on an open set) there are at least three linear branches, i.e. a linearly dispersing gapless partner. Equivalently, no member has two linear TT polarizations and at most two linear branches in every direction.

**How it relates to X-G.**
- *Wider hypotheses.* Any h–E mixing; O instead of O_h; C² instead of C⁴; no gauge-kernel hypothesis F; flatness is not assumed anywhere.
- *Weaker conclusion when partners are suppressed.* At most one axial TT polarization is linear, versus X-G's ω_TT = O(k²) under F.
- *This is sharp (checked s4).* A, B and C are PSD over 3005 directions (min eigenvalue ≥ −1.2e-15). A and B have rank ≤ 2 everywhere and C has rank ≤ 1. Each has exactly one axial TT stiffness. A is proved PSD by hand: it equals (|c3|/3)Σ_i k_i²(h_jj − h_kk)², a single "+" polarization.

**Margin (checked; sampled, not certified).**
- Take TT1 = TT2 = 1 and VEC = S = 0. PSD near the axis forces the line c2 = c3/2 − ¼ (exact first-order condition, s5).
- Global PSD on that line holds for c3 ∈ [−1.5, 4.5] (s6, 3005 directions).
- Every PSD member has a direction whose third soft stiffness λ₃(V2) is ≥ 0.4375, minimized at c3 = 0 on a 0.25 grid.
- Only the equal-stiffness case was scanned.

## 5. The PRODUCED direction: what was tried

1. **Axis-perfect local model (s7; checked, exact along the axis).**
   - The model: H_F = ½Σ_x[E:E + m(tr h)²] + ½Σ_xΣ_i Φ_i(h(x+e_i) − h(x)), with Φ_z = ½(h_xx − h_yy)² + 2h_xy² (the TT part relative to axis i). It is nearest-neighbour, PSD and O_h-covariant.
   - **On axes:** two TT modes with ω = √(2(1−cos k)), exactly, at all k (checked at k = 1.3). The vector and scalar partners are exactly flat. The trace mode is gapped at √3.
   - **Off axes:** 4 linear branches on face diagonals (ω/|k| = 0.5, 0.707, 0.707, 0.866), 5 on body diagonals and generic directions.
   - This is the best a local Gaussian can do along axes. It fails the registered target off-axis.
2. **Single-polarization families A/B/C** (s4): local, PSD, and at most two (C: one) linear branches everywhere. But they have only one TT polarization per axis.
3. **Gyroscopic / parity-odd O(k) h–E terms** (the genuinely new content of the mixed class): Step 5 shows they act like a magnetic field. They give at most one cyclotron branch per 2-dim sector, and never reduce the linear count below rank V2. They cannot supply the second polarization.
4. **Mixed flat kernels with a non-analytic ratio r(k)** (R13-2's worry): not needed. Lemma V uses no kernel form at all. The symbol that works, k²P_TT(k̂), has rank 2 with the right kernel in every direction, but it is homogeneous of degree 2 and non-polynomial. It is C¹ but not C² at k = 0, which is exactly the hypothesis used.
   - Tail clause (subtraction named): after subtracting contact terms, its real-space kernel decays as r⁻⁵. This is a homogeneous-distribution fact, RECALLED.
5. **Finite-slot realization.** Not reached, since PRODUCED fails. *Suggested:*
   - spin-wave (semiclassical) Gaussian theories of finite-slot models are 𝒢_mix members whenever their 12 phase-space coordinates per cell form two Sym² copies. Berry-phase first-order terms are exactly the O(k) mixing covered by Step 4.
   - In that case X1's regime gains nothing from mixing.

## 6. Prices (named, never adopted)

| Escape left | Axiom touched | Status |
|---|---|---|
| Non-local symbol k²P_TT(k̂) (fails C²; r⁻⁵ tail after contact subtraction, RECALLED) | Admissibility nearest-neighbour locality `AX:57-58` | as R13-2's non-local price (`R13-2:175`) |
| Auxiliary irreps (more than six pairs) | none (a model-content choice) | open (`vR13-2:13`), not tested here |
| Indefinite IR with exact emergent constraints (P-N3″) | none named; a dynamical hypothesis | open; outside Gaussian PSD |
| Non-Gaussian strongly coupled phases | none | open |

Parity is **not** an escape. Proper-rotations-only (`AX:37-38`) admits parity-odd mixed terms, and they are covered.

## 7. Readings against the FIXED clauses (`TESTS:4867-4870`)

- **PRODUCED: no.** No PSD local Gaussian with h–E mixing gives two linear TT polarizations without a linear partner. The finite-slot step is moot.
- **EXCLUDED: candidate, not yet refereed.** Theorem G-mix extends X-G to mixed kernels and goes beyond it:
  - the proper group only;
  - C² regularity;
  - no gauge-kernel hypothesis;
  - axis-only flatness covered as a corollary (outside this item's scope; flagged for the supervisor).
- **Overall worker reading: OPEN by the fixed rule until refereed. EXCLUDED if confirmed.**
- **Perturbative order.** No PRODUCED is claimed. The theorem is exact at Gaussian order and needs the symbol only through O(k²) at k = 0. PSD, cubic covariance and C² are required at that order only.

## 8. Strong-word check and scope

- **"Proved"** covers:
  - Lemma R (rank-one factorization);
  - Step 3 (canonical on-site rotation);
  - Step 5 (Williamson count, standard);
  - Lemma V (exact Gröbner computation plus the hand case split above).
- Step 4's frequency convergence is a standard singular-perturbation / eigenvalue-continuity sketch, backed by checks to 1e-4. A referee may want it written out, especially case (iii).
- **"Checked"** covers all numerics. The margin of 0.4375 is a sampled number, not a certified bound.
- **"No gapless partner"** is weakened here to "at most two *linear* branches". Partners with ω = o(k) are not addressed and are not needed for the no-go.
- **Scope:**
  - exactly six Sym² canonical pairs;
  - Gaussian, PSD, C², O-covariant;
  - not auxiliaries, not non-local, not indefinite or constrained, not non-Gaussian.

## Files (`S/scripts/`)

- `s1_invariants.py/.out`: exact invariant basis (dimension 6 for O and O_h); axis sector values.
- `s2_rank_lemma.py/.out`: Lemma V (642 minors, Gröbner basis, the three lines); the axis-only form F.
- `s3_mixed_models.py`, `s3_mixed_models_seed{7,3}.out`: random mixed parity-odd local PSD models; reduction check; V2 in span.
- `s4_families_and_margin.py/.out`: families A/B/C (PSD, rank); plane scan.
- `s5_psd_plane.py/.out`: exact near-axis PSD conditions.
- `s6_psd_line.py/.out`: margin on the PSD line.
- `s7_axis_model.py/.out`: the nearest-neighbour axis-perfect model.
- `s8_edge_cases.py/.out`: A1g case (iii) and Lemma R.
