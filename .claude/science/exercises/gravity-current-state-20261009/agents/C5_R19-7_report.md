# C5 R19-7: away from the RK point. Does a sign-free quantum Z₂ tensor model show a linear T₂ mode?

**Worker.** Claude Opus 5.5, the same model family as the supervisor and every C5 worker. Ran 2026-10-13 from 04:19Z to about 04:52Z.
- **Unrefereed. Worker reading: OPEN** (§8).
  - **LINEAR-T2-EVIDENCE is not met.** No tested T₂ pole disperses linearly. Also, no exact-diagonalization (ED) cluster that carries γ-charges has ≥ 3 nonzero k on a line, so this reading cannot be reached by ED (checked).
  - **NO-LINEAR is met only in part.** The T₂ channel is gapped, flat in k and size-consistent at βU ≤ 1 (every v tested) and at βU = 2 for v ≤ 0.5. It fails the pre-stated size rule at βU = 2 for 0.75 ≤ v ≤ 1.25, and it shows a finite-k soft T₂ mode at βU = 3. So it does not hold "in every v/t regime tested".
- I edited no repository file and downloaded nothing.
- Every run used OMP_NUM_THREADS=2 and stayed under 10 minutes. The tilt4 points at βU = 2 (v = 1.5, 2, 4) and βU = 3 (v ≥ 0.75) were not obtained: the eigensolvers did not converge (§3).
- The method was fixed before any spectral run (`S/METHOD_preregistered.md`, ~04:23Z), including the linearity and size rules.

**Paths.**
- `P/` = `.claude/science/exercises/gravity-current-state-20261009/`; `TESTS` = `P/TESTS.md`.
  - R19-7 is at `TESTS:7425-7448`: setting `:7430-7433`, prior art `:7434-7436`, removed hypothesis `:7437`, probes `:7438-7443`, FIXED readings `:7444-7447`, expectation `:7448`.
  - Round-19 rules: `TESTS:7117-7131`.
- `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`.
- `rR19-1` = `P/agents/C5_R19-1_report.md`. `vR19-1` = `scratchpad/C5/ref_R19-1/REFEREE_VERDICT.md`: the sol referee's verdict, CONFIRMED WITH CORRECTIONS, which arrived during this run.
- `vR18-1`, `vR18-10`, `vR16-7` = `P/agents/C5_*_referee_verdict.md`.
- `S` = `scratchpad/C5/R19-7/`. Scripts and `.out` files are in `S/scripts/`, pickles in `S/data/`.

**Labels.**
- **proved:** derived here, unrefereed.
- **checked:** numerics run here.
- **suggested:** argued, not proved.
- **reading:** an interpretation.
- **comparator:** literature, RECALLED, not fetched.

---

## 0. Plain words

- **The question.** At the RK point (v = t) the Z₂ tensor model relaxes; it does not propagate (R19-1, NEITHER, confirmed by `vR19-1`). In quantum spin ice the photon appears when you move off the RK point. Does a light-like T₂ mode appear here when v ≠ t, on either side?
- **What I could compute.** The family H(v, βU) is stoquastic for every real v, so exact diagonalization and QMC are both sign-free.
  - **ED is limited by size.** Only clusters with at most 8 sites and γ-charges fit (Hilbert dimension ≤ 2¹⁶). Every one of them is distorted by wrap-around, compared with the real (L ≥ 4) model (checked):
    - On the 2×2×2 cube, the diagonal labels never move.
    - On the tilted 2-site tori, zz never moves, and xy is touched by 2 moves instead of 6.
    - The 1×1×L chains, which are the only ED-feasible clusters with ≥ 3 nonzero momenta on a line, have no γ-charges at all, so they reduce to the trivial v = 0 model.
  - **QMC is not run.** I found that a correct world-line QMC needs a special update, because the moves obey a local 14-move relation (checked). Building and validating that did not fit in the slot.
- **What the clusters show (checked, 3 clusters, βU ∈ {0.5, 1, 2, 3}, v/t from −1 to 4).**
  - **No linear T₂ anywhere.** On every cluster and at every point, the T₂ pole does one of two things:
    - it is flat in k: max/min ≤ 1.30 over the available k, with ω(0) ≥ 0.77·ω(k_min);
    - or it has its minimum at a *finite* wavevector: the face corner (π, π, 0) on the cube, or k_z = π/2 on the 8-site tilted torus at βU = 3, v ≤ 0.5.

    It never approaches 0 at k = 0 while staying finite at k_min.
  - **The v < t side** moves continuously towards v = 0. There the model is exactly a trivial paramagnet with flat, gapped bands (proved).
  - **On the cube, at βU ≥ 2, the RK point is a sharp ground-state switch** (an avoided crossing at v = t) into the v > t state (checked). The long-wavelength T₂ stays at 8t through it.
  - **The v > t side** is where things go soft. For large v the ground state collapses onto the γ = 0 configurations:
    - the whole γ = 0 set on the tilted tori (152 and then 656 states);
    - 24 of the 88 on the cube.

    The T₂ energies there shrink as v grows (roughly like 1/v or faster) and with cluster size, but they stay flat in k. That is a degenerate manifold, not a propagating wave.
  - So the expectation's "soft T₂" is seen on the v > t side, not the v < t side, and it is flat rather than quadratic.
- **What a linear T₂ would need (proved, SMA level).**
  - Off the RK point the TT f-sum is still a finite, even trigonometric polynomial (Lemma B, checked to all printed digits).
  - In the k⁰ class, a linear branch that carries part of the f-sum forces S_TT ≳ 1/|k| and a static TT susceptibility χ_TT ≳ 1/k² (Proposition C).
  - On the v > t side the effective dynamics lives in the exact integer-law γ = 0 manifold. That is R16-7's k⁴ class, where a linear branch would need S_TT ∝ |k|³ (suggested).
- **Why OPEN and not NO-LINEAR.** At βU = 2 for 0.75 ≤ v ≤ 1.25 (up to and around the RK point), the flat T₂ energy shrinks by 31–49% from 6 to 8 sites. Larger v there did not converge on 8 sites. The pre-stated rule says that is OPEN. The finite-k soft mode at βU = 3 is neither "gapped" nor "quadratic". And all accessible sizes are wrap-degenerate. The registered question needs QMC at L ≥ 4 with the relation update (§6, Lemma G).

---

## 1. Setting, hypotheses, readout bridge (`TESTS:7430-7433`)

**Literal registration.**
- **Ensemble (as R18-1 and R19-1).** N0914's slots and integer stencil, labels n ∈ {0,1}, the mod-2 law, γ = Gn/2 and E = Σγ².
  - Moves: XOR of the cube and the three μ8 orientations, every pattern at every base site, with multiplicity.
  - The trivial coset is the move span.
- **Hamiltonian.** H(v, βU) = Σ_m [−t X^{p_m} + v·e^{−βUΔ_m(C)/2}], with Δ_m(C) = E(C ⊕ p_m) − E(C) and t = 1.
  - At v = t this is R19-1's RK Hamiltonian (`rR19-1:84-85`), reproduced exactly (§2).
  - Moves that wrap to the identity on small tori contribute only the constant (v − t). They are dropped, as R19-1 does at v = t.
- **Signs of law data (rule `TESTS:7125`).**
  - t > 0, so the off-diagonal elements are −t ≤ 0 for every real v. The family is stoquastic (proved: the off-diagonal part does not depend on v).
  - v < 0 is tested and labelled. No classical weights are signed.
- **Shift action (P112).** E is shift-action invariant (`vR18-1:5`), and the move set is rotation-closed, so H(v, βU) is shift-covariant. On the tilted tori the symmetry is reduced to the cluster group, which keeps C₄ about z, so TT1 ≠ TT2 stays meaningful along z.
- **Readout bridge.** X-basis labels (P113, carried). The T₂ channel is the R18-1/R19-1 polarization TT2 with cvec normalization (`mc.py` `channel_pols`, `cvec`). Off RK there is no classical-ensemble bridge: S and S(k, ω) are quantum ground-state quantities.
- **Excluded (as registered):** integer lifts; non-local moves.
- **Removed hypothesis (`TESTS:7437`):** v = t. Kept: stoquasticity, locality, the mod-2 law, the move set.

---

## 2. Prior art (each counted once) and rechecks

**Prior art.**
1. **R19-1 / vR19-1.**
   - Lemma 1 (RK ⇔ Markov) is confirmed.
   - Lemma 2 is confirmed for non-wrapping boxes only: "At L = 2, periodic XOR cancellation removes the diagonal-slot moves" (`vR19-1` item 2).
   - Proposition 4 is confirmed for the SMA quotient (item 4); Theorem 6 needs a boundedness hypothesis (item 7).
   - The reading NEITHER is confirmed (item 8).
2. **R18-1 / vR18-1.** The ensemble; screening through βU ≤ 3.5 (`vR18-1:9`); Z₀ in the LR-local class (`vR18-1:11`); the moment lemma and isolated MILP charge-free states (`rR18-1` §3).
3. **R18-10 / vR18-10.** The off-axis rule (`vR18-10:11`); planar laws fake axis zeros.
4. **R17-6 / vR17-6.** Theorems Z and Z₀; Theorem G (Goldstone means ≥ 4 branches).
5. **R16-7 / vR16-7.** Theorem B (integer vector law ⇒ TT-electric f-sum O(k⁴); `vR16-7:5`). Theorem D (stoquastic + conserved scalar charge ⇒ W(k) ≥ 0, no Newtonian attraction; `TESTS:5403`).
6. **Comparators (RECALLED).**
   - Hermele–Fisher–Balents quantum spin ice: the RK point bounds an unscreened classical Coulomb phase, and the photon lives at v < t.
   - Moessner–Sondhi QDM phase diagrams: v > t gives frozen or staggered states.
   - The Bogoliubov/Stringari moment inequality S² ≤ (χ/2)·f.
   - Banerjee–Isakov–Damle–Kim / Shannon et al. QMC of the stoquastic ring-exchange model: the photon is seen.
   - Xu's rank-2 vector-charge model: quadratic TT modes.

**Rechecks before reliance (checked).**
- `s0_dims.out` and `s0b_tilted_dims.out`: my general-torus G and pattern vectors (`gcommon.py`, `tcommon.py`) reproduce the archived `common.G_matrix`/`pattern_vectors` exactly at L = 2 and 3.
- **`s1_check.out` (the engine at v = t, L = 2) reproduces R19-1's `s1_ed_L2.out` exactly:**
  - gaps 0.840445 (βU = 1) and 0.087565 (βU = 2);
  - |Hψ_RK| = 4e-15; overlap with ψ_RK = 1 to 12 digits;
  - TT2 at k = (0,0,π), βU = 1: S = 1.57407, SMA = 8.2636, main pole 8.2159, all identical to `rR19-1` s1;
  - 80-step Lanczos equals dense ED;
  - βU = 0: spectrum independent of v (gap 8 at v = 0, 0.5, 2).
- **R18-1 / R18-10 / R17-1 runners.** Not rerun. Only their refereed statements are used. The archived `mc.py` and `common.py` are used for `channel_pols`, `cvec` and `PATTERNS`, and these are identical to R19-1's copies (`diff`: SAME).

---

## 3. Method and cluster feasibility (probe (a))

**The method** is `S/METHOD_preregistered.md`, written before any spectral run.
- Sign-free method: ED in F₂-coefficient coordinates. Every move is an XOR mask on the state index, so H acts matrix-free. The ground state is found by dense ED (N ≤ 4096) or Lanczos (eigsh).
- S_X(k, ω) for TT1, TT2, V1, V2 and S: exact poles (dense), or two real Lanczos runs (Re and Im of O_kψ₀, 80 steps; full reorthogonalization for N ≤ 2¹⁷).
- **Maximum-entropy-free diagnostics:**
  - (i) the first moment / SMA f/S;
  - (ii) the "main pole", the lowest pole carrying ≥ 10% of S;
  - (iii) the imaginary-time decay rate at τ = 20/ω_SMA, computed exactly from the poles.

  At every flat point these agree to a few percent with the main pole. Example: cube, βU = 2, v = 0.5, TT2 at k = 0 has SMA 8.011, main 8.000, decay rate 8.000 (`s2_scan_cube2.out`).

**Cluster dimensions (checked; `s0_dims.out`, `s0b_tilted_dims.out`).** d is the dimension of the move span (the trivial coset), so a cluster has 2^d states.

| torus (periods) | V | d | ED? |
|---|---|---|---|
| 2×2×2 cube | 8 | 10 | dense |
| (2,0,0), (1,1,0), (0,0,3) "tilt3" | 6 | 13 | Lanczos |
| (2,0,0), (1,1,0), (0,0,4) "tilt4" | 8 | 16 | Lanczos |
| 1×1×4, 1×1×6, 1×1×8 chains | 4, 6, 8 | 7, 13, 19 | yes, but no charges (below) |
| 2×2×3, 2×2×4, 2×2×6, 3×3×3 | 12–27 | 28, 34, 58, 78 | no (≥ 2.7e8 states) |
| tilted (2,0,0), (1,1,0), (0,0,5) or (0,0,6) | 10, 12 | 25, 28 | no |

**Wrap degeneracy of every ED cluster (checked; `s8_wrap_degeneracy.out`).** The table gives the number of nonzero moves that touch one slot of each type (xx, yy, zz, xy, yz, xz), against the bulk values at L = 4.

| cluster | moves per slot type | γ-charges |
|---|---|---|
| bulk, L = 4 | [4, 4, 4, 6, 6, 6] | — |
| cube | [0, 0, 0, 6, 6, 6]: diagonal labels frozen (as `vR19-1` item 2) | some moves create no charge |
| tilt3 / tilt4 | [2, 2, 0, 2, 6, 6] | max \|Δ\| = 4 (bulk 12) |
| chains | — | none at all: max \|Δ\| = 0 (`s2_scan_chain4.out` header), so H(v) = −tΣX + const at every βU |

- chain4 and chain6 are exactly flat at 4t for every v and βU (`s3_summary_chain4.out`, `s3_summary_chain6.out`). The chain6 run finished before my stop command; the note appended to its `.out` file is moot.
- **Consequence (checked).** The only ED clusters with ≥ 3 nonzero k on one line are charge-free chains. LINEAR-T2-EVIDENCE's "≥ 3 k-points" cannot be reached by ED in this model. The strongest available 3-point test is k_z = 0, π/2, π on tilt4.
- **Unconverged points (not used).** Near and above v = t at βU ≥ 2, the tilt4 ground state sits in a near-degenerate manifold of 656 γ = 0 states (§6, Lemma E).
  - eigsh at tolerance 1e-9 to 1e-11 took > 4 min per point without converging.
  - At βU = 3, v = 0.75, ARPACK stopped after 20001 iterations with 2 of 3 eigenvectors converged (`s2_scan_tilt4_b3a.out`).
  - LOBPCG with a Jacobi preconditioner printed nothing within the 2-minute limit. Its test script was deleted.
  - So tilt4 lacks βU = 2 at v ∈ {1.5, 2, 4} and βU = 3 at v ≥ 0.75. These are marked "(not run)" in `s6_compare.out`. The first run's partial output is `s2_scan_tilt4_partA.out`.

---

## 4. Probe (b): ω(k), SMA and channels along the axis (checked)

**Full tables:** `s2_scan_*.out` (every channel, S, SMA, main pole, lowest pole, decay rate) and `s3_summary_*.out`. The compact cross-cluster table is `s6_compare.out`. The cell entries below are main poles in units of t.

**Cube (2×2×2).** Along the axis only TT2 (xy) and V carry weight, because the diagonal labels are frozen.

| βU | v | T₂ at k = 0 / (0,0,π) | V at (0,0,π) | lowest excitation (where) |
|---|---|---|---|---|
| 1 | 0.5 | 8.17 / 8.14 | 13.1 | 3.51 (face TT2 at 6.49) |
| 1 | 1.0 (RK) | 8.12 / 8.22 | 16.1 | 0.840 (face TT2, 1.31) |
| 1 | 2.0 | 8.07 / 8.16 | 31.0 | 0.163 (face TT2) |
| 2 | 0.5 | 8.00 / 8.00 | 72.3 | 7.43 |
| 2 | 0.9 | 7.99 / 8.01 | 111 | 1.56 (face TT2, 1.61) |
| 2 | 1.0 | 8.00 / 8.03 | 16.8 | 0.0876 (face TT2, 0.101) |
| 2 | 1.1 / 2 / 4 | 8.01 / 8.04; 8.01 / 8.02; 8.00 / 8.01 | 18–460 | 0.0333 / 0.0141 / 0.00627 (face TT2) |
| 3 | 0.75 / 0.9 / 1 | 8 / 8 | 619 / 738 / 16.4 | 3.98 / 1.59 / 0.0114 |

- **The long-wavelength T₂ is flat and gapped at ≈ 8t** for every v ≥ 0.25 at βU ≥ 1. The spread over k ∈ {0, π} is ≤ 2%.
- **The only soft mode is the zone corner (π, π, 0)**, in the TT2 polarization there (xz − yz). Approaching RK from below at βU = 3, its energy is ≈ 16(t − v) (3.98 at v = 0.75, 1.59 at v = 0.9). For v > t at βU = 2 it falls like (0.025–0.037)/v.
- **Reading.** This is the finite-size splitting of 24 degenerate classical configurations (§6, Lemma E), which are related by translations. It is not a long-wavelength branch.
- **The RK point is where the ground state switches (checked; `s11_cube_fine_v.out`, v from 0.50 to 1.50 in steps of 0.02).**
  - At βU = 2, d²E₀/dv² is −0.26 at v = 0.90, −568 at v = 1.00, and −0.86 at v = 1.10.
  - Over the same range, the face-TT2 weight S jumps from 0.002 (v = 0.90) to 0.034 (0.98), 0.727 (1.00) and 2.61 (1.02).
  - At βU = 3 the peak is −767 at v = 1.00, with S rising from 0.001 to 0.727 to 2.67 at v = 0.98, 1.00, 1.02. At βU = 1 the peak is broad (−77 at v = 1.04).
  - The axis T₂ stays at ≈ 8.0–8.4 throughout.
  - **Reading.** On this cluster, the RK point is a sharp avoided crossing between the v < t paramagnet and the v > t degenerate γ = 0 state. It is the analogue of the QDM's RK point bounding the frozen phase (comparator). No long-wavelength T₂ softens at it.

**tilt3 (V = 6), k_z ∈ {0, 2π/3}.**
- At every one of the 48 points, the T₂ main pole and S_TT2 are *identical* at k = 0 and k = 2π/3, to all printed digits (48/48; checked by parsing). Examples:
  - βU = 1: 2.52 (v = 0.5), 1.13 (v = 1), 0.246 (v = 2);
  - βU = 2: 0.967, 0.146, 0.0369;
  - βU = 3: 0.219, 0.0172, 0.0052.
- V at k = 2π/3 is 9.97–177 at every v ≥ 0, apart from one artefact (below), and 0.15–7.0 at v = −1.

**tilt4 (V = 8), k_z ∈ {0, π/2, π}.** Entries are T₂ at k = 0, π/2, π.

| βU | v | T₂: k = 0, π/2, π | V at π/2 | 3-point linear test |
|---|---|---|---|---|
| 1 | 0.5 | 2.59, 2.76, 2.59 | 10.1 | fails (ω₀/ω(π/2) = 0.94) |
| 1 | 1.0 | 0.928, 1.02, 0.928 | 10.2 | fails (0.91) |
| 1 | 2.0 | 0.215, 0.220, 0.215 | 21.5 | fails (0.98) |
| 2 | 0.5 | 0.917, 0.960, 0.917 | 6.76 | fails (0.96) |
| 2 | 1.0 | 0.0825, 0.103, 0.0825 | 15.9 | fails (0.80) |
| 2 | 1.25 | 0.0565, 0.0668, 0.0565 | 36.4 | fails (0.85) |
| 3 | 0.25 | 3.03, **0.144**, 3.03 | 5.12 | fails (21.0): finite-k minimum |
| 3 | 0.5 | 1.11, **0.0258**, 1.11 | 5.12 | fails (42.9): finite-k minimum, with S_TT(π/2) = 0.995 against S_TT(0) = 0.007 |

- The pre-stated linear pattern (ω₀ < 0.5·ω(π/2) and ω(π/2)/ω(π) in [0.4, 0.85]) fails at **every** tilt4 point run (`s6_compare.out`). ω(0) is never below 0.77·ω(π/2).
- **S_TT does not grow toward k = 0 (checked; `s9_report_checks.out`).**
  - On the cube and tilt3, S_TT2(0)/S_TT2(k_min) lies between 0.93 and 1.02 at every point.
  - On tilt4 the k = 0 and k = π spectra coincide at every point: same S, same poles, in TT1, TT2 and S; this is observed, not explained. So the three tilt4 points cannot show a 1/|k| trend. There S_TT2(0)/S_TT2(π/2) ranges from 0.007 to 1.6 (for example 0.971, 0.772, 0.971 at βU = 2, v = 1).
- **V/S (checked; `s9_report_checks.out`).**
  - At the smallest nonzero axis k and every v ≥ 0, the V main pole is at or above the T₂ main pole.
    - It is equal at v = 0 on the cube, where both are in the 12t band.
    - The ratio is ≤ 1.3 only on the cube at βU ≤ 1 with v ≤ 0.5, and it reaches 7e4.
  - At v = −1 on tilt4, V lies *below* T₂ (ratio 0.10–0.78), but there T₂ is large (8.6–164 at k = π/2).
  - One V entry is a Lanczos artefact: tilt3 at βU = 1, v = 0.75, k = 2π/3. No pole carries 10% of the weight, and the diagnostic fell back to a ghost pole at 0 (`s10_main_pole_audit.out`). Its long-time decay rate is 2.99.
  - S has no weight along the axis on the cube, or at π/2 on tilt4 (symmetry). On tilt3 the S main pole is 1.0–19 times the T₂ pole.
- **The T₂ main poles are robust (checked; `s10_main_pole_audit.out`).** Every axis TT2 main pole (93 + 96 + 105 entries) agrees within 10% with the long-time imaginary-time decay rate r20, and no TT2 entry uses the fallback.
- **Exception: k = 0 V on the tilted tori.** These are the xz/yz label totals. For v > t this V channel becomes the softest excitation (it equals the global gap; tilt3 at βU = 1, v = 2 has V(k = 0) = 0.080). That is the k = 0 classical degeneracy, not a branch.

---

## 5. Probe (c): off-axis checks (R18-10 rule; checked)

- **Cube.** Face (π,π,0) and body (π,π,π) are reported in `s2_scan_cube2.out`.
  - The face TT2 is the soft zone-corner mode of §4.
  - The body channels are degenerate across TT/V (cubic star) and lie at 12–3300.
- **tilt3 / tilt4.**
  - Face (π,π,0): T₂-type weight is in TT1/S there; TT2 and V1 have zero weight by symmetry.
  - Body (π,π,π) on tilt4: every channel shares the lowest pole of that sector. For example, at βU = 2, v = 1 that pole is 0.0834 against 0.0825 for the axis T₂.
- No off-axis small-k points exist on any feasible cluster. So the R18-10 rule can be applied only at zone-boundary points, and there no channel shows a linear trend (there is no second k to compare).

---

## 6. Analytic results

**Lemma A (v = 0 and βU = 0 are exact; proved).**
- H(0, βU) = −tΣ_m X^{p_m}, and H(v, 0) = −tΣ_m X^{p_m} + vM. Both equal R19-1's βU = 0 RK Hamiltonian up to a constant.
- So the character solution of R19-1 Lemma 2 applies:
  - flat bands at 2t·N_type;
  - whole-generator gap ≥ 2t;
  - in the non-wrapping scope (L ≥ 3) per `vR19-1` item 2, the bands are at 8t (diagonal slots) and 12t (face slots).
- Checked: at v = 0, for every βU, the bands sit at 2t times the move counts of `s8`: 12t on the cube (face slots, 6 moves); 4t for xy and 12t for xz/yz on the tilted tori (2 and 6 moves) (`s6_compare.out`).
- **Reading.** The v < t side interpolates from the screened RK state (`vR18-1:9`) to this gapped paramagnet. The HFB mechanism (comparator) needs the RK point to bound an *unscreened* classical Coulomb phase. Here it bounds a screened one, so the comparator's "photon at v < t" has no parent to inherit from (suggested).

**Lemma B (the f-sum off the RK point; proved; checked).**
- For every real v and finite βU, with ψ the positive ground state:
  **f(k) = ½⟨[O†,[H,O]]⟩ = (t/2) Σ_m Σ_C ψ(C) ψ(C ⊕ p_m) |O(C ⊕ p_m) − O(C)|².**
- **Proof.** The diagonal part commutes with O. ⟨C ⊕ p|[O†,[X_m, O]]|C⟩ = −|ΔO|², so [O†,[H,O]] = tΣ_m X_m·diag(|ΔO_m|²). ∎
- **Consequences.**
  - As in R19-1 Lemma 3, f(k) is an even trigonometric polynomial with V-uniformly bounded coefficients. They are ground-state averages of local operators.
  - f₀ = (t/2V) Σ_m ⟨ψ| X^{p_m} |ε:ΔN_m|² |ψ⟩ is the ground-state-weighted squared change of the γ-dipole (label totals).
  - At v = t it reduces to `rR19-1:109`.
- **Checked (`s4_fsum_offRK.out`).** The formula equals Σ_n ω_n|⟨n|O|0⟩|² to all six printed decimals, at 18 (βU, v) points on the cube, for TT1 and TT2 at k = 0 and π.
  - f₀(TT2) is 5.33–16.0 at every v ≥ 0 tested. So the k⁰ class persists off RK.
  - At v = −1 it is about 0: there the ground state is classical.
  - Positivity uniform in V off RK is **not** proved (suggested). R19-1's bijection bound used π-weights.

**Proposition C (what a linear T₂ needs off the RK point; proved).**
- (i) *SMA level.* R19-1 Proposition 4 (confirmed for the SMA quotient, `vR19-1` item 4) holds verbatim for every v, by Lemma B: ω_SMA ∝ |k| iff S_TT ∝ |k|^{2a−1} when f ∝ k^{2a}.
- (ii) *Exact branch.* Suppose a T₂ branch ω(k) = c|k| carries a fraction α > 0 of f(k) → f₀ > 0. Its residue is then Z ≥ αf₀/(c|k|). So S_TT ≥ Z ≳ 1/|k|.
- By the moment inequality S² ≤ (χ/2)f (Cauchy–Schwarz on Σ|O_n|²), χ_TT ≥ 2S²/f ≳ 1/k².
- So in the k⁰ class, any linear T₂ that carries f-sum weight forces an Einstein–Hilbert-type static TT susceptibility. This is the χ_TT ∝ 1/k² half of R16-7's PRODUCED-EVIDENCE signature (`TESTS:5282`).
- Branches that carry a vanishing fraction of f are not constrained here.

**Lemma D (uniqueness; proved).** For every real v, finite βU and finite cluster, H is stoquastic, and its off-diagonal graph is connected on the coset (the coset is the move span). By Perron–Frobenius, the ground state is unique and strictly positive.
- Numerically, at v = −1 and βU ≥ 2, the splitting is near or below solver precision (cube gap 4.7e-10 at βU = 2 and 1.2e-6 at βU = 3; `s2_scan_cube2.out`). The classical maximizers of D are 2-fold (cube) and 16-fold (tilt4) degenerate (`s7`). So the PF state is not resolved there.

**Lemma E (the large-v limits; checked, `s7_classical_minima.out`).** As v → ±∞, H/v → D(C) = Σ_m e^{−βUΔ_m(C)/2}.
- **v → +∞.** The minimizers are γ = 0 configurations at βU = 1, 2 and 3:
  - tilt3 and tilt4: *all* of them (152 and 656 states). The degeneracy equals the size of the γ = 0 set, so D is constant on it, and every move from these states raises E (min Δ = 2);
  - cube: 24 of its 88.
- **v → −∞.** The maximizers are charged (E = 24, 8 and 16), with 2, 192 and 16 states.
- **Reading.** For v > t at large βU, the low-energy space is a degenerate, exact integer-law (Gn = 0) manifold. It is split only by virtual tunneling through charged states. The T₂ energies that shrink with v and are flat in k (§4) are read as those splittings.

**Proposition F (the v > t regime is in R16-7's integer class; suggested).**
- At leading orders in t/v, the effective Hamiltonian acts within Gn = 0 with 0/1 labels. It is quasi-local order by order.
- vR16-7's Theorem B (`vR16-7:5`: an exact integer vector Gauss law gives a TT-electric f-sum of O(k⁴)) then applies to it. By (i) above, a linear T₂ there would need S_TT ∝ |k|³.
- In the bulk, the γ = 0 manifold is sparse under local moves:
  - the moment lemma (`rR18-1` §3): n = 0 has no charge-free local neighbour;
  - the MILP charge-free states were isolated under weight-20 moves.

  So frozen or fragmented dynamics are the likelier outcome (suggested; the bulk manifold is not enumerated here).
- The tilted tori's 656-state manifold is a wrap artefact of size 8 (§3).

**Lemma G (QMC needs a relation update; checked; the consequence proved).**
- **Checked (`s5_local_dependencies.out`).** Inside an open 3³ block of base sites, the 108 registered moves have exactly one F₂ relation: 14 moves (8 cubes and 2 of each μ8 orientation) whose XOR is zero. A 4³ block has 8 such relations.
- **Proved.** A world-line or SSE QMC whose only off-diagonal updates insert or remove same-move pairs keeps every move count's parity fixed. So it cannot reach world lines that contain the relation an odd number of times, which have nonzero weight t¹⁴(…). Such a QMC is non-ergodic.
- **What a correct QMC needs:**
  - a relation-insertion update;
  - handling of the diagonal scale v·e^{6βU} (|Δ| ≤ 12), which makes local kink insertion stiff at βU ≥ 2.
- **Prerequisite for the round-20 QMC stub (`TESTS:7259`).**

---

## 7. Probe (d): is there a regime with ω ∝ |k| in T₂ and gapped V/S?

- **None at the sizes run (checked).** Every tested regime gives one of four things:
  - a T₂ pole that is flat in k and gapped (βU ≤ 1 at every v; βU = 2 at v ≤ 0.5);
  - flat in k and shrinking with size (βU = 2, 0.75 ≤ v ≤ 1.25);
  - a finite-k soft T₂ (cube corner near and above RK; tilt4 k_z = π/2 at βU = 3, v ≤ 0.5);
  - classical degeneracy (v < 0 at βU ≥ 2).
- None has ω → 0 at k → 0 while ω stays finite at k_min. At every point ω(0) ≥ 0.77·ω(k_min).
- For v ≥ 0, the V main pole is at or above the T₂ pole at the smallest nonzero axis k (§4). At v = −1 on tilt4 it lies below.
- **Scope.** All clusters have V ≤ 8, have at most 2 nonzero k on a charge-carrying line, and are wrap-degenerate (§3). This does not exclude a linear T₂ in the bulk model at any v.

---

## 8. Readings against the FIXED clauses (`TESTS:7444-7447`)

- **LINEAR-T2-EVIDENCE: not met.**
  - No T₂ channel with ω linear in k was seen. The 3-point test fails at every tilt4 point.
  - The "≥ 3 k-points" condition cannot be met by ED: the only such clusters are charge-free chains (checked).
- **NO-LINEAR: not met as a whole.**
  - *Met (checked)* at βU = 0.5 and 1 for all v ∈ [−1, 4], and at βU = 2 for v ∈ {−1, 0, 0.25, 0.5}. There:
    - the T₂ is flat in k, measured as max/min over the axis k: cube ≤ 1.17, tilt3 1.00, tilt4 ≤ 1.30;
    - it is gapped, with ω(0) ≥ 0.77·ω(k_min);
    - the tilt4/tilt3 ratio at k = 0 is ≥ 0.77, so no shrink beyond 30% (it grows at v = −1).
  - V/S is not part of NO-LINEAR's clause. For its status see §4.
  - *Not met:*
    - βU = 2, v ∈ {0.75, 0.9, 1, 1.1, 1.25}: the T₂ shrinks by 31–49% from V = 6 to V = 8 (ratios 0.51–0.69), so the pre-stated rule gives OPEN;
    - βU = 3, v ∈ {0.25, 0.5}: the T₂ minimum is at finite k on tilt4, which is neither gapped-flat nor quadratic;
    - tilt4 at βU = 2 (v = 1.5, 2, 4) and βU = 3 (v ≥ 0.75): not converged, so untested on the second size.
  - "Consistent across sizes" is also weakened by wrap degeneracy at every size.
- **OPEN: yes (worker reading).**
- **Expectation check (`TESTS:7448`).**
  - "NO-LINEAR at the accessible sizes": linear is not seen, but NO-LINEAR is not certified.
  - "v < t giving a soft but quadratic T₂": **not seen.** The v < t side is gapped and flat, connected to the v = 0 paramagnet (Lemma A). The soft T₂ is on the v > t side (Lemma E), and it is flat, not quadratic.
  - The removed hypothesis (RK fine-tuning) is named. Stoquasticity is kept, and holds for every real v (§1).
- **For the referee.** Nothing here is a FAIL or no-go. Lemmas B, D, E and G, and Proposition C, are positive or structural statements. Proposition F is suggested only.

---

## 9. Probe (e): prices (named, never adopted)

| Price | Status | Axiom touched | Buys |
|---|---|---|---|
| **P-r19-7a: off-RK ratio v/t** | new, named. One number for the whole Hamiltonian. It replaces P-r19-1a's v = t; Admissibility is not a dynamics axiom and supplies no Hamiltonian (`AX:116-123`) | Admissibility dynamics (`AX:57-61`) | at accessible sizes, nothing: no linear T₂ |
| **P96** (an emergent constraint / reactive tensor phase) | sharpened, no new number. Off RK in the k⁰ class it is "a phase with χ_TT ≳ 1/k² and S_TT ≳ 1/\|k\|" (Proposition C). On v > t it reduces to the integer class (Proposition F, suggested) | Admissibility dynamics | the only light-like route |
| **Theorem D (R16-7)** | carried. The whole H(v, βU) family is stoquastic for every real v (§1). So even a linear T₂ found here would not give Newtonian attraction, which needs an E-basis sign problem (P-r16-7b) | — | states what this family cannot supply |
| **QMC relation update** | a method requirement, not a price (Lemma G) | — | ergodicity of any sign-free QMC of this family |
| P112, P113 | carried | `AX:37-41`, `AX:82-83` | the setting |

**Counting.** One new ratio, v/t. Nothing else is tuned: every other number is a computed pole, f-sum or S.

---

## 10. Rules checklist and scope

- **v_max.** No dispersion law is proposed. The flat bands have group velocity ≈ 0 at the sizes run. No gauge-field symbol is used.
- **Exhaustive forks.** The fixed three-way reading is used. Proposition C's fork inherits R19-1's NEITHER branch (nodal or log-corrected S).
- **Literal first.** The registered H(v, βU) is used as written. The tilted and chain tori are reported as clusters of the same law, with their wrap degeneracies stated (`s8`).
- **Signs of law data.** Stated in §1.
- **Equilibration.** Not applicable (ED). Convergence: dense ED, or Lanczos with residual control. Unconverged points are listed and unused (§3).
- **Same-component control.** At v = t the identical estimator, component and normalization reproduce R19-1 (§2).
- **Off-axis.** Reported only where a cluster allows it (§5).
- **Thresholds.** The 10% main-pole rule, the 30% size rule and the 3-point linear test were fixed in advance (METHOD). Ratios are computed in `s6_compare.py` from printed values.
- **Invariance.** The ground state is the unique PF state (Lemma D), so it is invariant under the cluster symmetry group.
- **Strong words.**
  - "Exactly" is used for algebraic identities (Lemmas A, B) and for tilt3's k-independence, which agrees to all printed digits.
  - "Proved" means unrefereed.
- **Not covered.**
  - Any cluster with L ≥ 3 in all directions (d ≥ 28).
  - QMC.
  - The bulk γ = 0 manifold.
  - Tilt4 at v ≥ t for βU ≥ 2 (beyond v = 1.25 at βU = 2).
  - βU > 3.
  - Non-trivial cosets.
  - Any identification of the readout with geometry.

## Files (`S/`)

- `METHOD_preregistered.md`.
- `scripts/`:
  - `common.py` and `mc.py` (copied from R19-1);
  - `gcommon.py` and `tcommon.py` (general tori);
  - `ed.py` (the ED engine). The eigsh `k` and `tol` became environment-settable (R197_K, R197_TOL) for the later tilt4 runs; the cube, tilt3 and partA runs used k = 4 and tol = 1e-11;
  - `parse_out.py`;
  - `s0_dims.{py,out}`, `s0b_tilted_dims.{py,out}` (dimensions and cubic checks);
  - `s1_check.{py,out}` (reproduces R19-1);
  - `s2_scan.py` (per-point pickling was added for the later tilt4 runs) with `s2_scan_cube2.out`, `s2_scan_tilt3.out`, `s2_scan_tilt4_partA.out`, `s2_scan_tilt4_b3a.out`, `s2_scan_tilt4_b2rest.out`, `s2_scan_tilt4_b3b.out` (the last two stopped), `s2_scan_chain4.out`, `s2_scan_chain6.out`;
  - `s3_summary.py` with `s3_summary_{cube2,tilt3,chain4,chain6}.out` (tilt4 is tabulated in `s6_compare.out`);
  - `s4_fsum_offRK.{py,out}` (Lemma B);
  - `s5_local_dependencies.{py,out}` (Lemma G);
  - `s6_compare.{py,out}` (the readings table);
  - `s9_report_checks.{py,out}` and `s10_main_pole_audit.{py,out}` (recomputed ratios; main-pole audit);
  - `s11_cube_fine_v.{py,out}` (fine v scan through RK on the cube);
  - `s7_classical_minima.{py,out}` (Lemma E);
  - `s8_wrap_degeneracy.{py,out}`.
- `data/`: `s2_*.pkl`.
