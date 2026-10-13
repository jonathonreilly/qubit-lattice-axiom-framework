# C5 R19-32: a covariant 10-slot truncated Krein graviton with local dynamics

**Worker.** Claude Opus 5.5 (same family as the supervisor and every C5 worker), 2026-10-13, 07:11Z to 08:40Z. **Unrefereed.** No repository file edited; nothing downloaded. Scripts and outputs: `S/scripts/` (cov.py, mb.py, s1–s6), 2 threads.

**Paths.**
- `P/` = `.claude/science/exercises/gravity-current-state-20261009/`
- `TESTS` = `P/TESTS.md`. The registration is `TESTS:8656-8675`; the FIXED readings are `:8671-8674` and the expectation `:8675`.
- `R19-25` = `P/agents/C5_R19-25_report.md`. Its referee was still running; its log had no findings at 07:20Z.
- `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`
- `S` = `scratchpad/C5/R19-32/`

**Labels.** proved = derivation here (unrefereed); checked = numerics here; suggested = argument; reading = interpretation; comparator = RECALLED.

## 0. Plain words

- **Set-up.** The ten metric components (four with negative norm) are ten decoupled Feynman-gauge lattice fields, each truncated to d levels. Physical states are those killed by the lowering parts of the four de Donder constraints.

- **Correction to R19-25 s5 (proved and checked).**
  - With plain forward differences, the four lowering parts are not mutually null on the lattice: max |N|/ω² = 1.0.
  - With staggered placement, every difference has symbol 2i sin(k/2). Then N = 0 to ≤ 3.7e-16 at all 96 nonzero momenta of the 2³, 3³ and 4³ tori.
  - Also at all 96 momenta: dim V1 = 6, inertia (2, 0, 4), and the positive quotient is 2 TT tensors (s1).
  - Staggered placement is a lattice price (P-r19-32a).

- **(a) Lemma K, covariant (proved; checked to 1.6e-15 in s2).**
  - [D_n(k), D_m(k′)^K] = −(d/L)(u_k u_k′ − v_k v_k′) Σ_{x,A} ĉ_nA ĉ*_mA η_A e^{−i(k−k′)(x+o_A)} P^top_{A,x}
  - [D_n(k), D_m(k′)] = −(d/L)(u_k v_k′ − v_k u_k′) Σ_{x,A} ĉ_nA ĉ_mA η_A e^{−i(k+k′)(x+o_A)} P^top_{A,x}
  - The identity parts cancel by nullness, or because ω is even in k.
  - So the lowering parts commute iff all constrained modes share one frequency. With ≥ 2 frequencies, no slot frequency ν removes the Bogoliubov mixing, since v_k = 0 needs ω_k = ν.

- **Top-support lemma (proved; checked in s5).**
  - Hypotheses: mixing (some constrained v_k ≠ 0) and every ĉ_nA ≠ 0.
  - Conclusion: no nonzero physical state has all slots below the top level.
  - Proof: take the highest occupied level m ≤ d−2. The raising terms that land at level m+1 are injective, one slot each, so P^(m)_{A,x}ψ = 0 for every slot (A, x). That contradicts the choice of m. ∎
  - Checked: dim(V ∩ W_<top) = 0 in all 7 mixing cases with V ≠ 0. In the no-mixing controls it contains the vacuum.

- **(b) Formula reading, boxes with hopping (checked).**
  - The vector-x sector decides: on the slice, V = V_scal ⊗ V_vx ⊗ V_vy ⊗ TT.
  - **V = {0}:**
    - AP L = 3 at d = 2, 3, 4, 5, ν = 1 and 2, plus a 10-value ν scan at d = 2, 3;
    - AP L = 4 at d = 2, 3 for three ν;
    - scalar sector, AP L = 3, d = 2.
  - The best approximate residual falls geometrically: 6.5e-2, 1.2e-2, 2.3e-3, 4.1e-4 at ν = 1 (about ×0.18 per level).
  - The d = 6 (L = 3) and d = 4 (L = 4) runs did not complete and are not claimed.

- **Controls.**
  - **AP L ≤ 2.** These boxes have no hopping (proved: the bond terms cancel into on-site terms). With ν equal to the box frequency:
    - V ≠ 0 at every d tested (vector-x d = 2–12; scalar d = 2–6);
    - quotient = vacuum alone, positive;
    - TT untouched;
    - leak exactly zero below the top.
  - **Periodic rings.** The negative-norm k = 0 zero modes are unconstrained, at CCR too, so the quotient is indefinite: (16, 13) on periodic L = 3 at d = 4.

- **(c) Spectral reading** (energy-lowering parts with respect to the truncated H; proved H-invariant, always contains the ground state, never empty).
  - The one-particle states that should be null have Gram −0.040 (d = 4), +0.008/+0.018 (d = 5), +0.0008 (d = 6), +0.0004 (d = 7). This is on AP L = 3.
  - The quotient is therefore not positive at d = 2 and 4, and has extra non-TT branches at d = 5–7.

- **(d) Static pull (proved; checked in s6).**
  - Fields decouple, and W = diag(iⁿ) maps H_T to H_L and f_T to −i f_L.
  - So the second-order shift is −χ_d (t·G·t) J², with t·G·t = ½ and χ_d > 0. The pull is attractive at every d.
  - χ_d(η = −1) = −χ_d(η = +1) exactly.
  - χ_d → CCR: 0.50048, 0.50026, 0.500028, 0.500004 at d = 5–8 (L = 4).
  - The 3D 1/r shape at finite d is not run.

## 1. Readings against the FIXED clauses (`TESTS:8671-8674`)

- **KREIN-WORKS: not met.**
  - Formula reading on boxes with hopping: V = {0}.
  - Spectral reading: non-positive quotient or extra branches.
  - The only cases meeting every item are dispersionless (no-hopping) AP L ≤ 2 boxes. Reading: they are not local Bogoliubov-mixed dynamics (`TESTS:8675`).
- **KREIN-EMPTY: met only in a stated scope.**
  - Scope: formula lowering parts, AP rings with hopping.
  - Checked over 4 consecutive d (2–5) on L = 3.
  - Mechanism, proved: unavoidable mixing gives the non-commutation formula, and the top-support lemma forces any physical state onto the truncation edge.
  - Not proved for every d.
  - Not met for the registered setting as a whole: the 1–2-site AP rings and the periodic rings are single-frequency and nonempty, and the spectral reading is never empty.
- **OPEN: yes, overall.**
- **Expectation** (`:8675`).
  - Confirmed in the formula reading with mixing.
  - "Leak-controlled in the free-quotient limit" holds exactly only without mixing, which on a lattice needs a dispersionless box.
  - With mixing, only approximate states are controlled: residual ×0.18–0.3 per level, d ≤ 5.

## 2. Prices (named, never adopted)

- **P-r19-32a:** staggered (cell-complex) tensor placement for lattice nullness. Touches Lattice, `AX:37-41`.
- **P-r19-32b:** a spectral, dynamics-defined physical-state rule. Sharpens P-r19-25c (`AX:92-95`). It buys non-emptiness only.
- **P-r19-25a and P-r19-25b:** unchanged (`R19-25:268-274`).

## 3. Prior art (counted once)

- **R19-25:**
  - Lemma K, used in proved form and re-derived here (`:165-181`);
  - the decoupled truncated quartet (`:190-197`);
  - the non-covariant massive rings (`:199-222`), not reused as evidence;
  - covariant CCR (`:235-249`), reproduced and corrected above.
- **R19-22:** Lemma J, refereed (`vR19-22:7`).
- **R15-5:** Lemma E (`:122-145`) and the 1/r from the indefinite conformal mode (`:201-203`).
- **R15-3:** the PSD no-go (`vR15-3:15`).
- **Comparators (RECALLED):** Gupta 1952; Sylvester's theorem; perturbation theory.

## 4. Strong-word check and scope

- **"Proved"** is used for:
  - the §0 commutator formulas;
  - the top-support lemma;
  - the slice factorization;
  - no hopping on AP L ≤ 2;
  - the periodic zero modes;
  - the spectral space characterization;
  - the static sign.
  
  All are unrefereed.
- **"Empty"** means dim ∩ ker = 0 at the listed (L, d, ν), with kernel threshold singular value < 1e-6. Nonzero minima were ≥ 4e-4.
- **"Two TT branches"** is claimed only at CCR on whole tori, and on the slice for the no-mixing controls.
- **Not covered:**
  - 3D finite d;
  - HP slots;
  - BRST with auxiliary slots;
  - interacting phases;
  - matter, nonlinear gravity, Λ;
  - readout bridges.

## Files (`S/scripts/`)

- `cov.py`: the covariant fields and the staggered symbol.
- `mb.py`: the many-body builder.
- `s1_onepart_cell`: CCR one-particle on whole tori.
- `s2_check_ops`: the Lemma-K identities.
- `s3_formula_gb`, `s3s_sparse_kernel`: the formula-reading kernels. Outputs:
  - `s3a`, `s3b`, `s3s_L3AP`, `s3s_L3AP_nuscan`, `s3s_L4AP`, `s3c_L3P`, `s3d_scal`, `s3s_scal_v2`;
  - `s3s_scal` is superseded (its threshold was too strict);
  - `s3s_L3AP_d6` is empty (the run did not complete).
- `s4_spectral_gb`: the spectral reading, outputs `s4a` through `s4e`.
- `s5_top_support`: the top-support lemma check.
- `s6_static_pull`: the static pull.
