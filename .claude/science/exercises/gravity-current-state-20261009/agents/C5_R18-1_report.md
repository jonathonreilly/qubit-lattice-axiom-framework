# C5 R18-1: the Z₂ window's signature. Pinch points at finite charge fugacity, and Theorem Z's k⁰ gap

**Worker.** Claude Opus 5.5, the same family as the supervisor and every C5 worker. Ran 2026-10-13, 01:53Z to about 02:50Z.
- **Unrefereed.** Worker readings:
  - **(a)–(c): SCREENED** (checked). At every registered finite βU (0, 0.5, 1, 2, 4), and at 1.5, 2.5, 3 and 3.5, ξ is finite, fitted and L-independent up to the largest L run. The weakest point is βU = 4, where ξ ≈ 4 against L ≤ 10 (§4–§5). βU = ∞ is sharp by Identity V, but frozen. I recommend a referee: SCREENED is evidence against the window.
  - **(d): Theorem Z₀ (proved here)** extends Theorem Z to every f-sum class, the k⁰ finite-response class included. It is offered to the referee as GAP-CLOSED; until refereed, (d) reads OPEN (§6).
- I edited no repository file and downloaded nothing.
- The method was fixed at about 02:00Z, before any run (`S/METHOD_preregistered.md`). One schedule fix (§3) and one estimator choice (§4, both pre-registered diagnostics reported) are noted where they occur.
- Scripts and `.out` files are in `S/scripts/`, data in `S/data/`. Every run used OMP_NUM_THREADS=2 and finished in under 10 minutes.

**Paths.**
- `P/` = `.claude/science/exercises/gravity-current-state-20261009/`; `TESTS` = `P/TESTS.md`. R18-1 is registered at `TESTS:6427-6471`, with its FIXED readings at `:6459-6466` and the expectation at `:6467-6471`.
- `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`. `N0914` = `docs/LOCAL_FINITE_CLOCK_TENSOR_CONSTRAINTS_CUBIC_DISPERSION_AND_LINEAR_GRAVITY_BOUNDARIES_BOUNDED_THEOREM_NOTE_2026-09-14.md`.
- `rR17-6` = `P/agents/C5_R17-6_report.md`, `vR17-6` = `P/agents/C5_R17-6_referee_verdict.md`; likewise `rR17-1`, `vR17-1`, `vR16-11`. `S23` = `P/agents/C5_S23_synthesis.md`.
- `S` = `scratchpad/C5/R18-1/`.

**Labels.** proved (derived here, unrefereed); checked (numerics run here); suggested (argument, not proof); reading (interpretation); comparator (literature, RECALLED, not fetched).

---

## 0. Plain words

- **The question.** R17-6 showed that a qubit (Z₂) graviton window with gapped vector and scalar channels needs a *pinch point*: a static response whose k → 0 limit depends on the direction of k. Identity V turns that into a condition on the mod-2 law's leftover even charges γ = Gn/2: they must be suppressed faster than k². Here I took the simplest local ensemble that penalizes those charges, with weight exp(−βU Σγ²), and measured whether a pinch point survives at any finite penalty.
- **The answer: no. The charges screen.** At every βU tested (0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4), the same readout component (xz) along the two directions where it is "vector" (k ∥ z) and "tensor" (k ∥ y) differs at short wavelength but becomes equal again at long wavelength.
  - The crossover length ξ is finite, the same at every L run (6 to 16 at small βU, 6 to 10 at βU = 4), and fits a single Lorentzian at every q (checked).
  - ξ grows smoothly with βU: about 0.3, 0.5, 0.8, 1.2, 1.6, 2.2, 3.0 and 4.0 lattice spacings for βU = 0.5 … 4. Its growth tracks the charge density, as Debye screening would (suggested).
- **βU = 4 is the hard point.**
  - A wide replica-exchange ladder (βU from 1 to 6) failed to equilibrate it. Its charge density was too high, by 27–59%.
  - A focused ladder (βU from 2 to 4; 212 round trips at L = 6, 39 at L = 8, 12 at L = 10) and long single-temperature runs agree at L = 8. They give ξ² ≈ 15–19 at L = 6, 8 and 10, with ξ/L = 0.64, 0.53 and 0.39.
  - If ξ were infinite, ξ² would have grown by 2.8× from L = 6 to L = 10. It did not.
  - The L = 10 point was still drifting slightly, and ξ is only about L/2.5 there. So this is the thinnest part of the evidence.
- **The exact-charge-free limit βU = ∞ is frozen under the registered moves (proved). I found no fluctuating phase there.**
  - No single cube or μ8 flip can keep γ = 0 (0 of 64 and 0 of 256 sign lifts are integer-invariant; checked). So the registered move set is frozen there. This was the expected failure.
  - The empty configuration has no charge-free local neighbour under *any* local move (a moment lemma; proved).
  - Even the minimal integer-invariant composite moves (weight 20) found no allowed move from a charge-free L = 4 configuration (0 of 768 000 proposals; checked).
  - By Identity V the vector channel vanishes exactly in every charge-free configuration. So βU = ∞ is "sharp" configuration by configuration, but it has no long-wavelength fluctuations under local dynamics to make a phase from.
- **(d) Theorem Z's gap closes (proved here, unrefereed).** Theorem Z₀: with a strict vector gap Δ, the jump of the static response χ between the two directions equals, as k → 0, the static weight the tensor (T₂) component carries below Δ. There is no condition on the f-sum (k⁰, k², k⁴ all covered) and none on χ_TT being finite.
  - The tool: the part of χ above the gap is the expectation of a commutator with a smooth odd function of ad_H. By Lieb–Robinson it is continuous in k, and by Schur it is equal in the vector and tensor channels. So high-energy weight can neither hide the jump nor fake it.
  - Consequence: two gapless helicity-2 branches that the readout can see statically (Z/ω bounded below), together with a strict vector gap, force a pinch point in every f-sum class. Branches the readout cannot see statically force nothing, but then the readout is blind to them at long wavelength.
- **What this means for the window (reading).** The static Z₂ window needs exact charge suppression. Finite fugacity screens it at every βU tested. Exact suppression freezes the local dynamics of this ensemble. What is left is P96 (an emergent constraint not dressing-connected to an integer law) at a critical point or phase boundary, or a different ensemble.

---

## 1. Setting, hypotheses, readout bridge

**Ensemble (`TESTS:6436-6442`).**
- Slots and stencil: N0914's slots (diagonal n_jj at sites, face n_ij at x + (e_i+e_j)/2) and its integer stencil (Gp)_j(x) = p_jj(x+e_j) − p_jj(x) + Σ_{i≠j}[p_ij(x) − p_ij(x−e_i)] (`N0914:96-97`). Labels n ∈ {0,1}.
- The mod-2 law: Gn is even on every edge. γ = Gn/2 ∈ {−1, 0, 1} (proved: each edge's Gn is a sum of three terms in {−1, 0, 1}).
- Classical weight exp(−βU Σ_edges γ²). By the RK identity, this is the equal-time law of the RK state with amplitude ∝ exp(−βU Σγ²/2). That is the registered readout bridge for "static response" (`TESTS:6438`). It is equal-time S, not the dynamical χ of Theorem Z.
- Moves: XOR of R17-1's minimal F₂-invariant patterns: the cube (the six faces of one lattice cube) and μ8 in its three orientations (`rR17-1` §4), at every translate, with Metropolis acceptance. Sector: the coset of the move span that contains n = 0.
- **Removed hypothesis** (`TESTS:6450`): Lemma R's uniform full-coset weight. Kept: locality, finite fugacity, the mod-2 law.

**Covariance (checked, `s1b`).**
- Σγ² is invariant under the **shift action** of all 24 site rotations (24/24), but not under the natural pure-permutation action (6/24).
- The trivial coset maps to itself under both actions, and F_all (flip every slot) lies in the move span and leaves the weight invariant. So the condition that `vR17-6:5` places on Proposition S's equivalence holds for this ensemble.
- So this ensemble is cubic-covariant only with the shift action, i.e. the R-point readout of Proposition S. That is P112 (`S23:431`), carried, not new. Under the shift action the centred labels n − ½ transform as tensor components. At k ≠ 0 their structure factor equals that of n.

**Readout and observables (fixed in advance).**
- O_ε(k) = Σ_s e^{−ik·pos_s} c_s n_s, with c = ε_jj on diagonal slots and 2ε_ij on face slots (R17-1's probe).
- The five traceless channels relative to k̂: TT (2), V (2), S (1); plus the trace. Also S_γ(k) = ⟨|γ(k)|²⟩/V.
- Directions: axis, face and body, every lattice k, all cubic copies.
- Readout bridge: X-basis labels, P113 (`S23:432`), carried.

---

## 2. Prior art (each counted once)

1. **R17-6 / vR17-6.** Theorems G, Z, Z′ (corrected), Identity V (narrowed) and Lemma R (narrowed to full-coset uniform states) (`rR17-6:153-229`; `vR17-6:11-19`). The open items this item takes up: pinch-point phases, and finite-response k⁰ f-sums (`vR17-6:19`).
2. **R17-1 / vR17-1.** The cube and μ8 patterns and their lift counts (0/64, 0/256 integer-invariant; `vR17-1:13`), Theorem M, and the TFIM duality (`vR17-1:19`).
3. **R16-11 / vR16-11.** The dressing cap, and the minimal integer-invariant {−1,0,1} hop of weight 20, confirmed in finite boxes only (`vR16-11:31` as cited in `rR17-1` §2).
4. **R16-7.** The integer-law k⁴ bound.
5. **N0914.** Stencil (`:96-97`); "not a no-go for qubits" (`:215`).
6. **S23** §1.2: the live window is "a pinch-point Z₂ phase" = P96 (`S23:168`).
7. **Comparators (RECALLED):**
   - Coulomb-phase pinch points in spin ice, broadened by monopoles at finite fugacity into Lorentzians of width ~ (charge density)^{1/2} (Henley; Castelnovo–Moessner–Sondhi);
   - rank-2 U(1) four-fold pinch points (Prem–Vijay–Chamon; Pretko);
   - Debye–Hückel screening and the Stillinger–Lovett condition;
   - vector-charge rank-2 theories conserve angular charge moment, so charges are mobile only along restricted directions, which gives slow relaxation (Pretko);
   - Lieb–Robinson bounds; Watanabe–Murayama (only as quoted in vR17-6).

---

## 3. (a) Move set, detailed balance, ergodicity

**Sectors (checked, `s1`).** Every pattern is F₂-invariant on the torus. The move span has codimension 6 in ker_F₂ G for odd L and 21 for even L ≥ 4 (for example L = 6: dim ker 655, span 634). These are non-local sectors that local moves cannot reach. The chain samples the trivial coset; I make no claim about the others.

**Ergodicity at finite βU (proved).** Every proposal is a symmetric involution (an XOR flip), and every state has positive weight. So the chain is irreducible on n₀ + span(moves), for every finite βU.

**Detailed balance (proved; checked, `s2`).**
- Symmetric involutive proposals with Metropolis acceptance satisfy detailed balance.
- At L = 2 the coset has dimension 10 (1024 states), which I enumerated exactly. MC against exact:
  - ⟨Σγ²⟩ = 5.9916 ± 0.0136 vs 6.0000 (βU = 0);
  - 0.2600 ± 0.0068 vs 0.2744 (βU = 1, 2.1σ with a blocking error);
  - 0.0040 ± 0.0009 vs 0.0045 (βU = 2).
  - Histogram differences are ≤ 0.005.
- **Schedule fix.** The first run showed a histogram error of 0.13 at βU = 0. The cause: with every move accepted, a fixed even number of flips between measurements samples only an index-2 sub-coset. Alternating the sweep length by one move fixed it. This affects the measurement schedule only; every production run alternates.

**βU = ∞ (the registered "likeliest failure").**
- **Single moves (checked, `s4` (i)).** 0 of 64 cube sign lifts and 0 of 256 μ8 sign lifts have Gδ = 0. So every single move from a γ = 0 state creates charge, and at βU = ∞ the registered chain is frozen on every charge-free state.
- **Moment lemma (proved).** For finitely supported integer δ on Z³, D(Gδ) = −M₀(δ) (`rR17-1` §3, confirmed `vR17-1:10`). If Gδ = 0 and δ ≥ 0, then every component sum Σδ_ab = 0, so δ = 0. So n = 0 (and, by F_all, n = 1) has no charge-free neighbour under *any* local move, composite moves included, whose support does not wrap the torus.
- **The charge-free set is not trivial (checked, `s4`).** MILPs with random objectives found 4 distinct non-winding charge-free configurations in the trivial coset at L = 3, and 3 at L = 4 (two of them are winding line configurations).
- **Composite moves (checked, `s6`; outside the registered move set).**
  - The minimal integer-invariant {−1,0,1} pattern has weight 20 (MILP, 4³ box). It has 6 signed rotation copies, each with Gδ = 0.
  - A uniform-measure chain from a MILP charge-free L = 4 configuration (Σn = 216) proposed 768 000 moves and accepted **0**. That configuration is isolated under weight-20 moves too.
  - L = 6: the start-configuration MILP hit its time limit, so this was not run (§9).
- **Identity V at βU = ∞ (proved, from `rR17-6:211-214`; checked to machine zero in every run).** Along k ∥ e_j, S_γ(k) = (q²/4)(S of the three slots in row j). So in any γ ≡ 0 configuration the vector channel along the axes vanishes identically at every k ≠ 0.
- **Reading.** βU = ∞ is sharp configuration by configuration, but it is not an ensemble with long-wavelength fluctuations under local dynamics. Post-selecting γ = 0 states from finite-βU tempering at L = 4 found only 2 distinct states (n = 0 and n = 1) in 4028 hits.

---

## 4. (b)–(c) Structure factors, pinch diagnostic, ξ(βU, L)

**Diagnostics (both pre-registered; METHOD (c)).**
- **Primary: the direct comparison** ρ(q) = S_xz,xz(k ∥ z)/S_xz,xz(k ∥ y). This is the same readout component in the direction where it is vector and the direction where it is tensor. It is averaged over the six cubic copies. White noise gives ρ = 1; a Coulomb pinch gives ρ → 0 as q → 0. Define ξ²(q) = (1/ρ − 1)/q², with q² = 4 sin²(k/2). A single Lorentzian has ξ² independent of q.
- **Secondary:** r = S_V/S_TT along the axis. It has white-noise baseline 4/3, not 1, because the TT pair mixes diagonal and face slots. With the baseline included it gives the same ξ. Raw values are in `s5_summary.out`.
- The free fit S_V = A/(1 + ξ²q²) was ill-conditioned at large βU, where two to four points carry the fit. I report the q-resolved ξ² instead, which shows the Lorentzian directly.

**Physical control (checked, `s7`; same observable, same stencil).** Gaussian labels with weight exp(−½Σn² − (λ/2)Σ(Gn)²).
- At λ = ∞ the law is the projector onto ker G(k), a Coulomb phase of the vector law with a known pinch point. The method reports ρ = 0 at every L (ξ = ∞): PASS, positive control.
- At finite λ the method returns ξ² = λ at every q and L (2.0 at λ = 3; 22.25 at λ = 30, L = 6), with ξ/L falling as L grows: PASS, screened control.
- These controls are Gaussian. No Z₂ model with a known pinch-point phase is available as a positive control.

**Results (checked; `s5b_pinch_table.out`; bin errors over 20 bins).**
- Equilibration evidence: E/edge agrees across L and samplers to ≤ 2% for βU ≤ 3.
- At βU = 3.5 and 4 only the focused ladder (`ptB_*`; round trips in `pt_roundtrips.out`) and long direct runs are used. The wide ladder (`pt_L*`) was not equilibrated there (§4(c)).

| βU | E/edge (γ-charged fraction) | ξ²(q₁), by L | ξ²(q₂), by L | ξ | ξ/L trend |
|---|---|---|---|---|---|
| 0 | 0.375 | 0.00 ± 0.01 (L = 6 to 16) | 0.00 | 0 | — (white noise, Lemma R) |
| 0.5 | 0.272 | 0.088, 0.113, 0.120, 0.094, 0.074 (L = 6, 8, 10, 12, 16; ± 0.004–0.033) | 0.096–0.106 | 0.31 | 0.050 → 0.017 |
| 1 | 0.192 | 0.305, 0.317, 0.248, 0.330, 0.273 (L = 6, 8, 10, 12, 16) | 0.290–0.298 | 0.54 | 0.092 → 0.033 |
| 1.5 | 0.130 | 0.692, 0.698, 0.678, 0.612 (L = 6, 8, 10, 12) | 0.646–0.687 | 0.83 | 0.139 → 0.065 |
| 2 | 0.0844 | 1.409, 1.440, 1.378, 1.412, 1.331 (L = 6, 8, 10, 12, 16; ± 0.01–0.11) | 1.36–1.43 | 1.19 | 0.198 → 0.072 |
| 2.5 | 0.053 | 2.79, 2.68, 2.65, 2.65 (L = 6, 8, 10, 12) | 2.64–2.76 | 1.65 | 0.278 → 0.136 |
| 3 | 0.0315–0.0327 | focused: 4.91, 4.77, 4.98, 5.04 (L = 6, 8, 10, 12; ± 0.10–0.38); wide: 5.08, 4.98, 5.25; L = 12 (wide, 0 trips): 6.4 ± 0.5 | 4.85–5.37 | 2.2 | 0.37 → 0.19 |
| 3.5 | 0.0173, 0.0197, 0.0201, 0.0205 (L = 6, 8, 10, 12) | focused: 9.67 ± 0.33, 9.03 ± 0.54, 9.66 ± 0.68, 10.0 ± 0.7 (L = 6, 8, 10, 12) | 10.1, 8.7, 7.9, 7.8 | 3.0 | 0.52 → 0.26 |
| 4 | 0.0097, 0.0122, 0.0142 (L = 6, 8, 10; focused); direct 0.0116 ± 0.0011, 0.0124 ± 0.0004 (L = 6, 8) | focused: 14.5 ± 0.6, 17.9 ± 1.0, 15.5 ± 1.0 (L = 6, 8, 10); direct: 21.6 ± 4.1, 19.3 ± 2.3 (L = 6, 8). L = 12 focused (5 trips): not equilibrated (E drifting 0.0169 → 0.0157; ξ² 11.7 vs 7.4 at q₂), not used | 17.5, 17.8, 16.2 (focused) | 3.8–4.2 | 0.64 → 0.53 → 0.39 |

- **What the table shows (checked).**
  - At every fixed βU, ξ² does not depend on q (a single Lorentzian) and does not depend on L over the range run (6–16 for βU ≤ 2; 6–10 for βU = 3–4). So ξ/L falls: the pinch point is broadened to finite width.
  - A pinch point would show up as ξ² growing with L (ρ(q_min) → 0, as in the λ = ∞ control). That never happens at finite βU.
- **Stillinger–Lovett form (checked).** S_γ/q² at q_min stays finite at every finite βU (for example 0.17–0.21 at βU = 2 for L = 6–16). It does not tend to 0. So the charges are not dipole-hyperuniform. This is exactly the condition Identity V says a pinch needs (`vR17-6:15`).
- **Debye form (suggested).** ξ²·ρ_γ/S_T approaches about 0.12–0.13 at large βU (0.10, 0.11, 0.12, 0.13, 0.13 at βU = 2, 2.5, 3, 3.5, 4, using L = 8 values). That is the Debye–Hückel scaling ξ² ∝ stiffness⁻¹/(charge density): a classical plasma of γ-charges screening an emergent tensor Coulomb field (comparator). The transverse response S_T grows from 0.50 (βU = 0) to about 1.4–1.5 (βU ≥ 3), as a Coulomb phase forms underneath.

**Probe (c): finite ξ, or a βU_c with ξ = ∞ at nonzero γ density?**
- **Checked for every βU tested, up to 4:** ξ is finite and fitted at every βU, and smooth in βU. There is no sign of a transition: E/edge and ξ² vary smoothly, ξ² rises by a roughly constant factor of 1.8–2.1 per 0.5 in βU from 2 to 4, and there is no peak in S_TT at any measured k.
- **Sampler caveat (checked).**
  - The wide ladder over βU ∈ [1, 5–6] made 28, 12, 0 and 0 round trips at L = 6, 8, 10 and 12. Its βU ≥ 3.5 replicas were *not* equilibrated: at βU = 4 its charge density was 0.0154, 0.0175 and 0.0180 at L = 6, 8 and 10, against 0.0097, 0.0122 and 0.0142 from the focused ladder. Its apparent plateau of E/edge ≈ 0.012–0.015 for βU = 4–6 is that failure, not physics.
  - At L = 8 the focused ladder and the long direct run agree: E/edge 0.0122 ± 0.0002 vs 0.0124 ± 0.0004, and ξ²(q₁) 17.9 ± 1.0 vs 19.3 ± 2.3.
  - At L = 10 the energy was still drifting down by about 10% during measurement, so that point is marginal.
  - Nothing beyond βU = 4 is equilibrated.
- **Slow dynamics (suggested).** Relaxation slows sharply above βU ≈ 3.5. This is consistent with the restricted mobility of vector charges (Pretko comparator) and with the frozen βU = ∞ set (§3).
- **Nonzero γ density** holds at every βU run (charged edges per edge ≥ 0.0097 at βU = 4; checked).

---

## 5. Readings for (a)–(c) against the FIXED clauses (`TESTS:6459-6463`)

- **PINCH-PRESENT: no.** No finite-βU ensemble showed ξ growing with L. At every βU, ξ/L falls from L = 6 to the largest L run (10 to 16).
- **SCREENED: yes (worker reading, checked).** At every registered finite βU (0, 0.5, 1, 2, 4), and at 1.5, 2.5, 3 and 3.5, ξ is finite, q-independent, L-independent within errors, and fitted. βU = ∞ is sharp: by Identity V the vector channel vanishes identically there. But βU = ∞ is frozen (§3).
  - **Scope.** The βU = 4 conclusion rests on L = 6, 8 and 10. There ξ ≈ 4 ≈ 0.4–0.6 L, and the L = 10 run was still slightly drifting. The ratio test (ξ² flat at 15–19 where ξ ∝ L would need 2.8× growth) is what carries it.
  - What would strengthen it: L = 12–16 at βU = 4 with a sampler that equilibrates there, for example a worm algorithm that moves charges along their allowed directions.
  - Nothing is claimed for βU > 4.
- **Expectation check (`TESTS:6467-6471`).**
  - "SCREENED": confirmed.
  - "Width ~ (γ-density)^{1/2}": confirmed in Debye form, κ² ∝ ρ_γ/S_T (suggested).
  - "The likeliest failure is MC ergodicity in the βU = ∞ sector": confirmed, and stronger than expected. The registered moves are frozen at βU = ∞ (proved). One charge-free L = 4 configuration is isolated under minimal composite moves (checked). In practice, sampling slows sharply from βU ≈ 3.5: a wide replica ladder failed there, and only a focused ladder equilibrated βU = 4.
- **Removed hypothesis (Lemma R's uniform weight).** Removing it does produce long-range tensor correlations: S_T grows and the V channel is suppressed at short wavelength. But at finite fugacity they are screened.

---

## 6. (d) Theorem Z₀: Theorem Z without any f-sum condition (proved; unrefereed)

**Hypotheses.**
- **(H1′)** H is finite-range (or exponentially decaying), translation- and O-covariant, on finite-dimensional sites. So Lieb–Robinson bounds hold, with velocity v. This is stronger than R17-6's summability (H1) (`rR17-6:173`).
- **(H2)** A unique translation- and O-invariant ground state on a family of tori (`rR17-6:174`).
- **(H3)** R17-6's readout: O_a(k) = V^{−1/2}Σ_x e^{−ik·x}τ_x(o_a), with o_a Hermitian, finitely supported, carrying E⊕T₂ once each (`rR17-6:175`).
- **(Gap_V)** There are Δ, k₀ > 0 such that for 0 < k < k₀ and every V, the spectral measure of the vector component xz along ẑ has no weight in (0, Δ). This is a strict gap, multiparticle weight included (`vR17-6:13`).

**Notation.**
- ρ_a,k = Σ_m(|⟨m|O_a(k)|0⟩|² + |⟨m|O_a(k)†|0⟩|²)δ(ω − ω_m).
- χ_a = 2∫dρ/ω, and χ_a^{<δ} = 2∫_{(0,δ)}dρ/ω.

**Statement.** For every 0 < δ < Δ there is a C, independent of V and k, such that
χ^{<δ/2}_{xy}(kẑ) − Ck ≤ χ_{xz}(kŷ) − χ_{xz}(kẑ) ≤ χ^{<δ}_{xy}(kẑ) + Ck.
In words: the jump of the static response between the two directions where xz is tensor and vector equals, as k → 0, the static weight that the T₂ tensor component carries below the vector gap.

**Proof.**
1. **Odd-function identity.** For real odd f with f̂ ∈ L¹, let f(ad_H)X = ∫dt f̂(t)e^{iHt}Xe^{−iHt}. Then ⟨m|f(ad_H)X|0⟩ = f(ω_m)X_{m0} and ⟨0|f(ad_H)X|m⟩ = −f(ω_m)X_{0m}. Hence ⟨[O†, f(ad_H)O]⟩ = ∫f dρ. R17-6's f-sum is the case f(ω) = ω (`rR17-6:176`).
2. **The cutoff function.**
   - Take φ ∈ C_c^∞, even, 0 ≤ φ ≤ 1, with φ = 1 on [−δ/2, δ/2] and support in [−δ, δ]. Let f = (1 − φ)/ω. It is smooth and odd, and f ~ 1/ω at infinity.
   - Its transform f̂ is bounded near t = 0. To see this, write f = ω/(1+ω²) + h, with h smooth, odd and O(ω⁻³). The first term has transform −(i/2)sign(t)e^{−|t|}, and h has a bounded transform.
   - f̂ decays faster than any power at large |t| (integrate by parts; f^{(n)} ∈ L¹ for n ≥ 1). So ∫|f̂(t)|(1+|t|)^{4}dt < ∞.
   - On ω > 0: 1_{ω≥δ}/ω ≤ f ≤ 1_{ω≥δ/2}/ω.
3. **Continuity.**
   - F_ab(k) := ⟨[O_a(k)†, f(ad_H)O_b(k)]⟩ = Σ_d e^{ik·d}C_ab(d), with C_ab(d) = ∫dt f̂(t)⟨[τ_0(o_a), τ_d(o_b)(t)]⟩, by translation invariance (H2).
   - Lieb–Robinson gives ‖[τ_0(o_a), τ_d(o_b)(t)]‖ ≤ c·min(1, e^{(v|t|−|d|)/ξ_LR}). So Σ_d|d||C(d)| ≤ c′∫|f̂|(1+v|t|)⁴dt < ∞, uniformly in V.
   - Hence |F(k) − F(0)| ≤ C|k|.
4. **Schur.** F(0) is O-invariant, and O's irreps are real, so F(0) = f_E1_E ⊕ f_T1_T (as in R17-6 (Z2), `rR17-6:185`). In particular F_xz,xz(0) = F_xy,xy(0).
5. **The two channels along ẑ.**
   - xz is a vector component. By (Gap_V) and supp φ ⊂ [−δ, δ] with δ < Δ, F_xz(kẑ) = χ_xz(kẑ)/2 exactly.
   - xy is the T₂ tensor component, so χ^{≥δ}_xy/2 ≤ F_xy(kẑ) ≤ χ^{≥δ/2}_xy/2.
   - By steps 3–4, |F_xy(kẑ) − F_xz(kẑ)| ≤ 2C|k|.
6. **Rotate.** The C₄ rotation about x̂ (ŷ → ẑ, ẑ → −ŷ) maps (xz, kŷ) to (−xy, kẑ). With χ_aa(−k) = χ_aa(k), this gives χ_xz(kŷ) = χ_xy(kẑ). So χ_xz(kŷ) − χ_xz(kẑ) = χ_xy(kẑ) − 2F_xy(kẑ) + O(k), and χ_xy − 2F_xy lies between χ^{<δ/2}_xy and χ^{<δ}_xy. ∎

**What it gives.**
- **Theorem Z is the special case m₁ → 0.** There the above-gap part of χ_TT vanishes by (Z4) (`rR17-6:187`), so χ^{<δ}_TT ≈ χ_TT ≥ c.
- **In the k⁰ class (μ_T > 0),** steps 3–4 match the high-energy weight between the vector and tensor channels: odd functions of ad_H are local in k. So a large high-energy f-sum can neither hide the jump nor create one. That closes the gap left at `rR17-6:198` and listed in `vR17-6:19`.
- **Corollary (proved).** Under (H1′)–(H3) and a strict vector gap, χ has a pinch point iff liminf_{k→0} χ^{<δ}_{xy}(kẑ) > 0 for small δ. In particular:
  - two gapless TT branches that are *statically visible* to the readout (residue with Z/ω ≥ c > 0, as an E-type readout of an ω ∝ k branch is: in H_N, |⟨1|E|0⟩|² = ω/(2J), so Z/ω ∝ 1/J and χ_E = 1/J; H_N is at `N0914:72-75`, and the values are a direct oscillator computation, as at `rR17-6:181`) force a pinch point in every f-sum class, with χ_TT finite or not;
  - statically invisible branches force nothing, but then the readout's static response does not see them at long wavelength. I read that as a readout-bridge failure (P113), not an escape.
- **Scalar analogue (proved by the same steps).** With a strict scalar gap, χ_{(xx−yy)}(kẑ) − χ_S(kẑ) → the TT(E) weight below the S gap. The pinch statement does not need it.
- **Scope; not covered:**
  - degenerate or symmetry-broken grounds, and gapless ground spaces (H2);
  - interactions without Lieb–Robinson bounds of the stated type;
  - readouts outside E⊕T₂;
  - non-strict vector gaps (continua reaching zero energy);
  - equal-time S instead of χ. Z₀ is about χ, while (a)–(c) measured S through the RK bridge.
- **Reading for (d):** GAP-CLOSED is offered to the referee. By the FIXED text (`TESTS:6465-6466`) it is **OPEN until refereed**.

---

## 7. (e) Prices (named, never adopted)

| Price | Status | Axiom touched | Buys |
|---|---|---|---|
| **P112** (shift action = R-point readout) | carried; *needed* here: the RK weight Σγ² is covariant only under it (`s1b`: 24/24 vs 6/24) | Lattice `AX:37-41` | a cubic-covariant charge penalty |
| **P110** (Z₂-clock slot), **P113** (N = 2 X-basis readout) | carried | `AX:47`; `AX:82-90` | the setting |
| **RK bridge** (equal-time S as "static response") | registered in the setting (`TESTS:6438`); not a general identity | Record readout `AX:82-83` | the classical MC |
| **P96** (emergent constraint, not dressing-connected) | sharpened, no new number. Finite fugacity screens (checked for βU ≤ 4, L ≤ 10–16); the exact limit is frozen under the registered moves (proved) and under minimal composite moves on one L = 4 configuration (checked). The window needs exact emergence at a critical point or phase boundary, or an ensemble outside this RK family | Admissibility `AX:57-61` (dynamical) | the only remaining static route |
| **P-r18-1a** (new, named): a non-local or composite move set that unfreezes the charge-free sector (minimal integer-invariant moves have weight ≥ 20 in tested boxes, and were stuck at L = 4) | named only | Admissibility (dynamics) | fluctuations at βU = ∞; it is the integer-law sector R16-7/R16-11 cap |

**Counting convention:** no tuning counts arise. Every number above is a measured ξ or a lift count, with no counterterms.

---

## 8. Round-17/18 rule checklist (`TESTS:6395-6405`)

- **Locality of vertices:** no TT or stress vertex is used. Z₀ concerns a finitely supported readout, which is local by (H3).
- **Number-free ≠ forced; Λ:** not applicable.
- **Bounded classes for spectra:** Z₀'s "gap" is the strict uniform spectral gap, continua included (Gap_V).
- **Certificates:** no CONFLICT is claimed. The numerics are checks, not enclosures.
- **v_max:** no dispersion or law is proposed. The classical MC has no light cone.
- **Controls:** the Gaussian λ-family uses the same observable and stencil, with a known pinch point at λ = ∞. There is no Z₂ positive control.
- **Readout bridge:** RK (§1).
- **Forks:** the PINCH/SCREENED/OPEN fork is the registered one. Excluded outside it: other coset sectors, non-RK ensembles, dynamics.
- **Generic GR:** not applicable.
- **Changed hypothesis:** Lemma R's uniform weight (§5).

---

## 9. Late results, strong words, scope

**Late results (all included above).**
- L = 16 at βU = 1 and 2 (direct): ξ² = 0.273 ± 0.025 and 1.331 ± 0.048, the same as at L = 6–12.
- Focused tempering at L = 6, 8, 10 and 12: §4 table. At L = 12 it made 5 round trips. That is enough at βU ≤ 3.5, where E/edge matches L = 8–10, but not at βU = 4.
- `s6` at L = 6: the MILP for a charge-free start configuration hit its 120 s limit, so there is no L = 6 composite-move check. The composite-move isolation is checked on one L = 4 configuration only. That the charge-free set is frozen *in general* under local moves is suggested, not checked.

**Proved (unrefereed):**
- weight covariance under the shift action (G(1 − n) = −Gn on flipped slots; also checked in s1b);
- irreducibility at finite βU and detailed balance;
- the frozen βU = ∞ chain for the registered moves;
- the Z³ moment lemma for n = 0;
- Identity V's exact vanishing of the vector channel at γ ≡ 0;
- Theorem Z₀ and its corollary.

**Checked:** s1, s1b, s2 (exact L = 2), s4, s5/s5b tables, s6 (L = 4), s7 controls.

**Suggested:**
- Debye scaling ξ² ≈ 0.12·S_T/ρ_γ;
- that the slow relaxation above βU ≈ 3.5 comes from restricted charge mobility;
- that ξ stays finite for every finite βU (Debye extrapolation beyond βU = 4).

**"Exactly" / "identically"** are used only for algebraic identities (Identity V, lift counts) and the exact L = 2 enumeration.

**Not covered:**
- equilibrium at βU > 4, and L > 10 at βU = 4;
- the non-trivial coset sectors;
- spectra and dynamics (excluded by the setting);
- any identification of the readout with geometry;
- N ≥ 3.

## Files (`S/`)

- `METHOD_preregistered.md`.
- `scripts/`:
  - `common.py`, `mc.py` (numba Metropolis), `run_mc.py`, `run_pt.py`, `run_pt_post.py`, `analyze.py`, `fitxi.py`;
  - `s1_ranks_sectors`, `s1b_symmetry_sectors`, `s2_exact_L2`, `s4_gamma0_manifold`, `s5_summary`, `s5b_pinch_table` (the primary table), `s6_binf` (`.out` for L = 4 and 6), `s7_gaussian_control`, each with its `.out`;
  - `pt_roundtrips.out` (tempering round trips), `direct.log`, `direct_b4.log`.
- `data/`: pickled structure factors per run, plus logs.
