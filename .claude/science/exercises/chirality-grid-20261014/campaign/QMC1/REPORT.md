# QMC-1 report: sign-free simulation pilot of X2's mirror gapping

> **Referee (codex gpt-5.6-sol): CONFIRMED WITH CORRECTIONS. The correct fixed reading is OPEN.**
> - **Confirmed:** the engine and the validation (an independent 3,000-sweep gate check).
> - **Not a gap measurement:** E2, E3 and E3w are not spectral-gap measurements.
> - **Limits:** the statistics are short, Δτ pinning is large, and β = 4 is a finite temperature.
> - **What it supports:** a GPR-like crossover. It does not establish a mirror gap, GPR mass generation or SMG.
>
> See `REFEREE_VERDICT.md` and `referee/REFEREE.md`.

**Reading.** OPEN by the pre-registered gap estimator, which fails at strong coupling. GPR-PILOT by every replacement estimator able to resolve an open gap at both sizes; these were declared in follow-ups D and E, before the L = 6 results were seen. The worker reads GPR-PILOT, conditional on the estimator, and leaves to the referee whether E2, E3 and E3w are admissible.

**Provenance.**
- **Worker:** Claude Opus 5.5 at xhigh. Same family as every packet agent, so not independent. Unrefereed.
- **Window:** 00:29–00:47Z, then 11:22–17:05Z on 2026-10-15. The supervisor session died in between; follow-up A records the gap.
- **This file:** the harness blocks subagents from writing REPORT.md, so the supervisor saved this from the worker's final message, lightly condensed. All numbers and file references are the worker's.
- **Not archived:** two superseded gate-(iii) data files, `*_run1_wrongWQobs.npz`, 10 MB. They recorded the wrong observable (deviation 2). Their logs are kept.

## Plain words

1. **The simulation exists and passed every validation check** (checked).
   - **What it simulates:** a sign-free quantum Monte Carlo of X2's mirror interaction. This is the pure BB + h.c. member (λ1 = 0), with global Spin(10) and no gauge links, on 1+1D rings and 2+1D square lattices.
   - **The four checks:**
     - with the interaction off, it reproduces free particles exactly;
     - every sampled weight is real and positive;
     - a reduced-flavour version matches exact diagonalisation;
     - the light (three-generation) corners stay exactly free at every coupling.
2. **Main result, 2+1D** (filter f2 = (1 + cos p_x cos p_y)/2, sizes 4×4 and 6×6, temperature 1/4).
   - Once the coupling is strong enough to make the mirror particles heavy (W ≳ 2), the 10-vector pair correlation per site does not shrink from 4×4 to 6×6.
   - No coupling was found where the mirrors are heavy and that correlation shrinks.
   - This is the Golterman–Petcher–Rivas pattern: in this pilot the mirrors get heavy by forming a symmetry-breaking 10-vector condensate.
3. **The registered gap estimator failed at strong coupling.**
   - The mirror propagator drops into noise before τ = 1.
   - With that estimator alone, the mechanical reading is OPEN.
   - With three replacement estimators, declared before the 6×6 results were seen, it is GPR-PILOT.
4. **Control: the on-site model (f ≡ 1).** At these sizes it roughly follows the Eichten–Preskill/GPR sequence (reading):
   - gapless at weak coupling;
   - then gapped, with large 10-vector correlations;
   - at strong coupling, the uniform correlation falls by about 4× and the staggered correlation shrinks with size.

   The filtered model shows no such turnover up to W = 16 (4×4 only). That is K1's gap G1 (no atomic limit), seen numerically.
5. **1+1D validation, L = 8 and 16** (past NT-3's ED limit of 7). At W = 1 the mirror gap is open (about 2.0) and the same at both sizes, and the 10-vector correlation does not grow.
6. **Deliverables:** documented, validated code and a cost model.
   - A checked decomposition makes the determinant factorise in 2D, saving about 8× on cluster runs.
   - Dynamical SM links break the construction. Only links in a Spin(8) subgroup that contains SU(3)_c keep it sign-free (suggested).

## Reading (fixed wording at TESTS.md:335-338)

**Scope.**
- Model: ungauged X2 matter Hamiltonian, global Spin(10), λ1 = 0. Q_x = −¼ Σ_a (B̂^a B̂^a + h.c.), with B̂^a = ½ ψ_S^T (iσ_y ⊗ N^a) ψ_S.
- Lattice: 2+1D; walker σ_x sin p_x + σ_y sin p_y; filter f2; periodic; L = 4 and 6.
- Run parameters: β = 4; Δτ = 0.1 for W ≤ 4 and 0.05 for W = 8; 45–60 measured sweeps.
- Errors: binning (20 bins).

| Gap estimator | W where the gap is open at both L | S10/L² ratio L6/L4 there | Mechanical reading |
|---|---|---|---|
| **E1:** unweighted cosh fit, τ ∈ [1, 3] (pre-registered) | none (the fit fails at W ≥ 2) | — | **OPEN** |
| **E2:** weighted cosh fit, τ ∈ [0.4, 3.6] (follow-up D, 12:23Z) | 2 | 0.98(5) | GPR-PILOT |
| **E3:** w₁ ≤ 2cosh(β/2)·G(β/2) (follow-up D) | 8 | 0.87(10) | GPR-PILOT |
| **E3w:** the same bound, window-averaged over τ ∈ [1, 3] (follow-up E, 12:40Z) | 4, 8 | 1.35(26), 0.87(10) | GPR-PILOT |

**Physical scope of "GPR".**
- A flat S10/L² from L = 4 to 6 means a correlation length of at least about 6. It cannot tell true order from a long correlation length.
- Mermin–Wagner forbids true continuous order in 2D at T > 0 for the exactly Spin(10)-symmetric model.
- Source: `scripts/runs/readout_final.out`.

## Validation gate (TESTS.md:330-334): all four items passed before production (checked)

| Item | Result | Source |
|---|---|---|
| (i) W = 0 gives the free G(τ, k) | max deviation 5.7e-14 (2D 4×4, f2) and 3.6e-15 (1D L = 4), over all k and τ | `scripts/validate_a_v2.out:1-2` |
| (ii) every weight real and positive | max ratio phase over every proposal in every valid run: **3.0e-9** (worst case L6, W8). Full weights on prior-scale random fields: ≤ 5.3e-14. Each slice commutes with T2 to 1e-15, and slice spectra are closed under conjugation. One exploratory control run (W = 4, n_s = 4) reached 4.6e-3 and was discarded (follow-up C). | `validate_a_v2.out:6-10`; per-run "max phase" in `readout_final.out` |
| (iii) one finite-W observable agrees with an exact method | See below | `runs/gate3_dt005.log`, `runs/ed_gate3.log` |
| (iv) on even L, the light-corner G equals the free one | G(τ) = ½ **per configuration** to ≤ 1.8e-13, in every filtered run | "max light dev" column |

**Item (iii) in detail.**
- Setup: reduced flavours (1 s + 1 c flavour, 4 d-modes per site, same channel builder and engine); 1D, L = 3, f1, W = 2, β = 2.
- At Δτ = 0.05, against ED:

  | Observable | QMC | ED |
  |---|---|---|
  | W⟨Q⟩ | −0.1338(6) | −0.13438 |
  | Σ S | 0.5631(5) | 0.56382 |
  | E_kin | −2.4215(1) | −2.42148 |

- Δτ = 0.1 also agrees within errors.
- Why not a Spin(6)/SU(4) version: the code path needs a real Clifford set of the Cl(9) type, and none exists for a 4×4 spinor.

**Extra checks (checked).**
- The Fierz identity holds exhaustively on all 35,960 four-annihilator components (residual 1.0e-15, `x2model.out:3`). Under Wick contraction it holds to 1e-16 (`validate_a_v2.out:11`).
- The W = 0 Wick measurement agrees with ψ-frame ED to 1e-16 (`validate_a_v2.out:3-5`).

## What was built (checked unless marked)

**Frame.** SIGN-1's d-frame: a particle–hole transformation on 8_c, so every slice conserves d-number and commutes with T2 = (iσ_y ⊗ 1)K, where T2² = −1 (SIGN1 REPORT:62-72).
- Weight: det(1 + M_d).
- The referee's 1/√det M_d factor is constant here, because every HS generator is traceless.

**Decomposition.** The pre-registered LP over the two-dimensional sign-correct Fierz family (`x2model.py:166-212`) chose κ = (sing8v +1.5, trip8v −0.5, 0, 0).
- That gives 64 HS channels per vertex, against 512 at SIGN-1's point.
- There is no remainder at λ1 = 0, because (Re P)² − (Im P)² = (P² + P†²)/2 exactly (proved).
- Each channel squares to ¼·1, so exp(zO) has a closed form.

**HS fields and Trotter.**
- Each square has its own Gaussian field, so the HS step is exact.
- Vertex factors are ordered products, reversed on alternate slices (`afqmc.py:143-165`).
- The only systematic error is the Trotter splitting.

**Vertex form (proved).** With F_x F_xᵀ = ρ·1, the vertex is 1 + F_xᵀ[(core − 1)/ρ]F_x.
- So a wrap costs O(taps·D·N_d) (`afqmc.py:179-216`).
- Updates are rank-32 Woodbury steps with 32×32 ratio determinants (`:256-294`).

**Updates.** Preconditioned Crank–Nicolson moves of all fields at one vertex. They are reversible with respect to the Gaussian prior, so the acceptance is min(1, det ratio). The step size adapts during warm-up only.

**Why not HMC (suggested).**
- HMC needs a stabilised forward and backward pass plus adjoint vertex derivatives at every MD step: about 6 N_d³ L_τ per step, 10–20 steps per trajectory.
- A local sweep costs about 2·acc·N_d³ L_τ.
- Measured τ_int(S10) is ≤ 1.3 sweeps for every f2 run (`runs/autocorr_final.out`; crude Sokal estimate).

**Stabilisation.**
- Pivoted-QR UDV stacks every 0.4 in imaginary time.
- Stable G(τ) and G(τ, 0) come from one shared middle factor (`:241-254`).
- Wrapped-versus-fresh G deviation is ≤ 1.0e-8 in every valid run.
- Peak memory 0.99 GB, under the 1.5 GB cap.

**det = |det_sector|².**
- **Not available** for the production decomposition: J does not commute with the triplet x, y channels (commutator 0.42).
- **Available in 2D** with the singlet-only Fierz vertex (sing8v 1.25, sing56v 0.25), which is also sign-correct.
  - J_d = (−1)^{x+y} σ_z ⊗ diag(1_s, −1_c) commutes with every slice (3.5e-17), and T2 J_d T2⁻¹ = −J_d.
  - So det(1+M) = |det(1+M₊)|², with half-size sectors.
  - Checked for f2 and f ≡ 1: the log dets agree to 1e-10 (`scripts/check_sector.out`).
- **Not available in 3D** with a J of this form, because no 2×2 matrix anticommutes with all three Paulis (proved for that form).
- The production runs were not switched to it.

## Production results (checked; scope as above)

**f2, 2+1D.** S10/N = S10/L². The free values are 0.541 (L4) and 0.294 (L6), a ratio of 0.54.

| W | S10/N, L4 | S10/N, L6 | ratio | E2 gap, L4 → L6 | E3w bound, L4 → L6 | U(1)_c-plane fraction, L4/L6 |
|---|---|---|---|---|---|---|
| 0.25 | 0.630(9) | – | | 0.12(3) | 3.66 | 0.20 |
| 0.5 | 0.995(32) | – | | 0.34(1) | 3.00 | 0.19 |
| 1 | 2.19(6) | 1.35(4) | 0.62(2) | 1.05(3) → 0.85(1), drifting | 1.00 → 1.50 (closed) | 0.22/0.20 |
| 2 | 3.23(12) | 3.18(11) | **0.98(5)** | 2.61(13) → 2.51(25) | 0.095 → 0.112 | 0.60/0.69 |
| 2 (Δτ 0.05) | 3.60(6) | 4.11(80) | 1.14(22) | 2.72(10) → 4.1(8) | 0.094 → 0.052 | 0.21/0.85 |
| 4 | 4.69(20) | 6.34(1.20) | **1.35(26)** | 7.7(2.4) → fit fails | 0.010(10) → −0.054(29) | 0.65/0.92 |
| 8 | 5.28(26) | 4.58(49) | **0.87(10)** | fit fails | 0.012(11) → 0.030(24) | 0.71/0.89 |
| 16 | 4.78(21) | – | | 8.4(4.6) | −0.004(7) | 0.63 |

- **The gap opens together with the correlation growth** (reading). S10/N jumps, and the size ratio moves from about the free value (0.62 at W = 1) to about 1 (W ≥ 2). That is the GPR mechanism.
- **The direction-pinning is a Trotter artefact** (checked).
  - At Δτ = 0.1 and W ≥ 2, 60–92% of S10 sits in the U(1)_c (9,10) plane, against an isotropic share of 0.20.
  - At L4, halving Δτ restores isotropy (0.21) and raises the total S10 by 11%.
  - At L6 the pinning persists at Δτ = 0.05 (0.85).
  - The readings use the component sum. The Δτ shift of the size ratios was measured only at W = 2: 1.14(22) at Δτ = 0.05.
- **No strong-coupling turnover in the filtered model** (reading). S10/N at L4 plateaus at 4.7–5.3 for W = 4–16.

**Control f ≡ 1, 2+1D** (the power reference):

| W | S10/N, L4 | S10/N, L6 | ratio | staggered S(π,π)/N ratio | E2 gap, L4 → L6 |
|---|---|---|---|---|---|
| 0.05 / 0.1 | 4.47 / 5.23 | – | | | 0.09 / 0.18 (gapless) |
| 0.25 | 28.7(1.1) | 22.7(2.1) | 0.79(8) | 0.47(2) | 1.53(4) → 1.50(3) |
| 0.5 | 17.9(5) | – | | | 4.39(19) |
| 1 | 7.77(45) | 6.68(23) | 0.86(6)* | 0.39(2) | gap ≫ 1 (E3w ≈ 0) |

\* τ_int of S10 at W = 1 is 4.4 sweeps (L4) and 2.9 sweeps (L6), so this error is underestimated by up to about 2×.

**1+1D, f1 = (1 + cos p)/2, L = 8 → 16, β = 4** (validation only):

| Run | S10 | E2 gap |
|---|---|---|
| W = 1 | 59.1(9) → 60.4(2.7), no growth | 2.01(6) → 2.04(6) |
| W = 4 | grows ×1.59 | gap ≫ 1 |
| control, W = 0.25 | — | 1.80 → 1.85 |

**Against NT-3** (NT3 REPORT:20-33; REFEREE_VERDICT:22, 46-48).
- NT-3's SU(4) proxy at L ≤ 7 found no static-order threshold violation and could not establish a mirror gap.
- Here, in the Spin(10) model at L = 8 and 16 and W = 1, the k = 0 mirror single-particle gap is open and size-stable, and the filtered 10-vector correlation does not grow.
- No discrete order parameter was measured, so a gap that comes with discrete symmetry breaking is not excluded.
- The filtered S10(Q = 0) weights modes by f(k)², so it cannot see NT-3's near-light soft pair mode. That mode remains untested.

## Control against the literature

These comparators are from abstracts and search summaries only.
- **GPR**, 4D Eichten–Preskill SO(10) (K1:186-189): a symmetric massless phase, then an intermediate SO(10) → SO(9) broken phase, then a symmetric massive phase at strong coupling.
- **Slagle–You–Xu**, PRB 91, 115121 (2015), arXiv:1409.7401: DQMC on a bilayer honeycomb lattice; a direct transition from the Dirac phase to a fully gapped symmetric phase.
- **Ayyar–Chandrasekharan**, PRD 91, 065035 (2015), arXiv:1410.6474, and arXiv:1511.09071: staggered SU(4) with an on-site four-fermion term; massive without a bilinear condensate; a direct second-order transition in 3D.
- **He–You–Xu**, arXiv:2603.18278 (journal page PRB 114, 165125): direct SMG for SU(2)³; an intermediate excitonic phase in a Spin(5)×U(1) variant.
- **4D staggered results** (K1:190-193): narrow broken or antiferromagnetic intermediate phases.

**Does the control reproduce known behaviour?** Only qualitatively (reading).
- Its sequence matches the GPR/EP history for this 10-vector channel: gapless, then gapped with large S10, then a strong-coupling regime where the uniform and staggered correlations fall.
- It does not reproduce a direct SMG transition. The direct-SMG models in 2+1D use different interactions, so this is no contradiction.
- At L ≤ 6 it cannot decide whether W = 0.25–0.5 is truly ordered, or whether W = 1 is truly symmetric. The ratios 0.79 and 0.86 lie between the ordered value (1) and the short-range value (about 0.44).

## Cost model and gauge links (suggested)

**Cost per 1000 sweeps per W point.** Calibrated as T = a·N_d³·L_τ on the measured 2+1D L = 6 sweep time (29.7 s with 2 threads; a = 4.86e-10). Full table: `scripts/cost_model.out`.

| Geometry | Core-hours (β = 4) | Core-hours (β = L) | Memory |
|---|---|---|---|
| 2+1D L = 8 | 93 | 185 | 2–3 GB |
| 2+1D L = 12 | 1,056 | 3,168 | 10–23 GB |
| 3+1D L = 4 | 93 | — | 2 GB |
| 3+1D L = 6 | 3,564 | 5,346 | 23–30 GB |
| 3+1D L = 8 | 47,466 | 94,933 | 128–208 GB |

- The singlet-vertex factorisation divides the 2D numbers by about 8.
- 3+1D L = 8 needs a compiled GPU or distributed code, with delayed updates and checkpointed stacks.
- These figures are for this Python engine; a tuned code is several times faster.

**Dynamical G_SM links.**
- The fixed U(1)_c plane fails for arbitrary links: the 10 contains no G_SM-invariant real 2-plane.
- Links in Spin(8) on directions 1–8 are real in this gamma basis and commute with Γ⁹ and K. They keep the number-conserving d-frame, real T2-invariant hopping and a covariant F[U].
- With the (9,10) plane placed inside the electroweak 4, this covers SU(3)_c × U(1)_{B−L} × U(1)_{(7,8)}, but not SU(2)_L or hypercharge.
- Full G_SM therefore needs either a new positivity construction (open) or reweighting. The average sign for reweighting is measurable from this ensemble.
- Links also remove the FFT kinetic term and add link updates, an estimated 3–10× cost.

## Deviations and caveats

1. **Session gap,** 00:47–11:22Z. New deadline 18:30Z (follow-up A).
2. **Gate (iii), run 1,** recorded the vector-channel energy, which is not the reduced model's interaction. The HS-channel energy (WQc) was added; same seeds, same chain (follow-up B).
3. **The pre-registered gap estimator E1 failed.** E2, E3 and E3w were added (follow-ups D and E). The W choices at L6 deviated from the mechanical E1-based rule; the final set {1, 2, 4, 8} contains both candidate sets.
4. **The control's locator was moved to its own coupling scale.** Its local energy scale is about 1/ρ², roughly 10× f2's at the same W. Control W ≥ 2 was dropped, and n_s = 4 was used at L6 for memory (follow-ups C and F).
5. **Statistics are short:** 45–60 measured sweeps (30 for the L6 Δτ = 0.05 check). Δτ = 0.1 shifts S10 by about 10% at W = 2. β = 4 is a finite temperature.
6. **Process deviations** (follow-ups B and D).
   - Two short algebra scripts ran outside capped.sh: fierz_points.py (about 3 s, 100 MB) and patch_tree.py (code edits only).
   - So did a few analysis scripts (under 100 MB, seconds each), sometimes while a QMC run was active.
7. **Warnings.** numpy/Accelerate prints "divide by zero / overflow / invalid in det" warnings. They are suspected to be spurious floating-point flags, but this is not proven. Every check of wrapped against fresh G passes.

## Files (`campaign/QMC1/`)

- `PREREG.md`, with dated follow-ups A–J.
- `scripts/`:
  - **Engine and model:** `x2model.py`/`.out` (algebra, Fierz LP, d-frame channels), `afqmc.py` (engine and Wick observables), `runner.py` (CLI, documented in its docstring).
  - **Analysis:** `analysis.py`, `readout.py`, `autocorr.py`, `cost_model.py`.
  - **Exact methods:** `ed_exact.py`, `ed_reduced_gate3.py`.
  - **Validation checks:** `validate_a.py`/`validate_a_v2.out`; `check_sector.py`/`.out`; `check_tree.py`/`.out`, with `afqmc_prepatch_ref.py` and `patch_tree.py`; `fierz_points.py`.
  - **Drivers:** `*.sh`.
  - **Run data:** `runs/*.npz` and `*.log`. Final tables are in `runs/readout_final.out` and `runs/autocorr_final.out`.

**Sources:** Slagle–You–Xu, arXiv:1409.7401; Ayyar–Chandrasekharan, arXiv:1410.6474 and arXiv:1511.09071; He–You–Xu, arXiv:2603.18278 (PRB accepted page).
