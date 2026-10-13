# C5 R18-10: does conserving the γ-dipole give the Z₂ ensemble a pinch point at finite fugacity?

**Worker.** Claude Opus 5.5, the same family as the supervisor and every C5 worker. Ran 2026-10-13, 03:00Z to about 03:40Z. Unrefereed.

**Reading against the FIXED clauses (`TESTS:6894-6896`): OPEN. No pinch point appears anywhere; SCREENED is checked at each βU tested up to 2.5 (0.5, 1, 1.5, 2, 2.5).**

Why OPEN and not SCREENED:
- βU = 3 and 3.5 were tested but are not seed-stable (§4.2). This mirrors the precedent of `vR18-1:3,9`.
- R18-1's patterns with the dipole filter alone are non-ergodic (proved, Lemma P), and the fixed text sends non-ergodic moves to OPEN.

What was found:
1. **The γ-dipole is the label count (proved; checked).** For N0914's stencil, Σ x γ(x) = −½ (N_ab), where N_ab is the total of 1-labels on slot type ab. The angular part vanishes identically. "Conserve the dipole" therefore means "conserve six global label numbers". It is not a constraint on local states.
2. **The equal-time (RK) readout sees a move restriction only through the class it picks (proved).** The stationary law of a symmetric, filtered Metropolis chain is the Boltzmann weight restricted to the chain's communicating class. A conservation law on the moves can change the static readout only by choosing a sector, or by fragmenting it.
3. **The fixed-dipole sector is screened with R18-1's ξ (checked).** I sampled the full N_ab = V/2 sector exactly, using the grand-canonical chain with an N-bias and conditioning on N. It reproduces R18-1's grand-canonical ξ² within errors:
   - βU = 0.5, 1, 1.5, 2, 2.5 at L = 6;
   - βU = 1 and 2 at L = 6, 8, 10, 12;
   - βU = 0.5–2.5 at L = 8.

   Further:
   - ξ² is L-independent and q-independent.
   - S_γ/q² is finite and rises toward a plateau (0.217, 0.238, 0.252, 0.259 for L = 6–12 at βU = 1). It is not o(k²).
   - The face and body channels agree with the grand-canonical ones (to the third digit at L = 6, βU = 2).
4. **R18-1's patterns plus the dipole filter fragment (proved; checked).**
   - Every accepted flip also conserves the diagonal-label count in every lattice plane (3L numbers), so each plane's net a-charge is frozen.
   - At L = 2, exact enumeration gives 511 classes for 1024 states, 504 of them frozen singletons.
   - Hot and cold starts disagree even at βU = 0.5.
5. **The declared second family fixes ergodicity at small L (checked).** It adds each pattern XOR its unit translate (pre-declared in METHOD for this case).
   - At L = 2 its filtered classes equal the N-sectors exactly: 53 = 53, none split.
   - At L = 6 it breaks the planar laws.
   - Hot and cold starts agree with each other and with the exact sector at βU ≤ 2 (L = 6 PT) and βU = 1 (L = 8).
   - At βU ≥ 2.5 the local chain is glassy. The dipole filter leaves about 6–9× fewer non-raising moves than the grand-canonical chain (§4.3).
6. **Even the most favourable fragment does not pinch (checked, βU = 1).** In the class of the registered chain with uniform diagonal plane profiles, only the scalar-longitudinal axis channel is frozen to zero. The vector channel that Identity V and Z₀ use is screened as in the grand-canonical ensemble.
7. **Correction to the diagnostic (checked).** A stronger move set that conserves every row slot's plane counts, started in a prepared uniform sector, gives on the axes ρ = 0 and S_γ(k ∥ axis) = 0 *exactly*, at finite charge density, at L = 6, 8, 10. R18-1's axis-only diagnostic would read that as ξ = ∞. Along the face and body directions the same runs are screened at the grand-canonical values. So axis zeros can come from planar (subsystem) conservation laws plus a chosen sector, not from a pinch point. Every pinch claim must report the off-axis channels.
8. **The expectation fails on its mechanism (`TESTS:6897`; proved).**
   - "S_γ ∝ k²" already holds in R18-1's screened ensemble. The pinch needs o(k²).
   - In fracton theories dipole conservation follows from a Gauss law imposed on the states (comparator). Imposed on the moves of an equilibrium ensemble, it fixes only six numbers.

**Paths.**
- `P/` = `.claude/science/exercises/gravity-current-state-20261009/`; `TESTS` = `P/TESTS.md`. R18-10 is registered at `TESTS:6871-6897`, with its readings at `:6894-6896`.
- `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`; `N0914` = `docs/LOCAL_FINITE_CLOCK_TENSOR_CONSTRAINTS_CUBIC_DISPERSION_AND_LINEAR_GRAVITY_BOUNDARIES_BOUNDED_THEOREM_NOTE_2026-09-14.md`.
- `rR18-1` = `P/agents/C5_R18-1_report.md`. `vR18-1` = `scratchpad/C5/ref_R18-1/REFEREE_VERDICT.md`; it is back: CONFIRMED WITH CORRECTIONS, with (a)–(c) demoted to OPEN at βU = 4 and Z₀ GAP-CLOSED in the LR class.
- `rR17-6`, `vR17-6`, `vR17-1` as in the packet.
- `S/` = `scratchpad/C5/R18-10/`. The method was fixed in `S/METHOD.md` before any run; scripts are in `S/scripts`, data in `S/data`.

**Labels.** proved (derived here, unrefereed); checked (numerics run here); suggested (argument, not proof); reading (interpretation); comparator (literature, RECALLED, not fetched).
- I edited no repository file and downloaded nothing.
- Every run used OMP_NUM_THREADS=2 and took under 10 minutes; the longest took 8.0 min.
- I checked the load throughout. I killed two L = 8 runs when the load reached 16 and kept at most 7 single-thread jobs afterwards.

---

## 1. Setting and what changed from R18-1

- **The R18-1 setting (`TESTS:6876-6883`; `rR18-1:46-62`).**
  - N0914's slots and stencil (`N0914:95-97`), with the mod-2 law. γ = Gn/2.
  - Weight exp(−βU Σγ²).
  - Shift action P112 (`rR18-1:53-56`; `vR18-1:5`).
  - Readout: X-basis labels (P113) through the RK equal-time bridge.
- **Added (`TESTS:6879`):** the move set conserves Σ x γ(x).
- **Removed hypothesis (`TESTS:6887`):** charge moves without dipole conservation.
- **Move sets** (fixed in METHOD; the second family is declared there for use if the first fragments):
  - **M1** (registered): R18-1's cube and μ8 (three orientations) XOR flips at every translate. A flip is accepted only if its signed per-type count change is zero (dN_ab = 0, which equals dD(γ) = 0 by Lemma D), then by Metropolis.
  - **M2** (declared): M1 plus each pattern XOR its unit translate along x, y and z. That gives 16 local patterns of 6–16 slots, all in the coset, with the same filter.
- **Sector: N_ab = V/2 for all six types.**
  - n = 0 is a frozen singleton (N = 0).
  - F_all maps Q = N − V/2 to −Q, so Q = 0 is the only F_all-invariant sector (proved, one line). F_all must be a symmetry for Proposition S's equivalence (`vR17-6:5`).

## 2. Prior art (each counted once)

1. **R18-1 / vR18-1.**
   - The grand-canonical (GC) ensemble, the ρ/ξ² diagnostic, and ξ(βU) (`rR18-1:127-137`).
   - The referee finds widths finite through βU ≤ 3.5, and βU = 4 not seed-stable, so (a)–(c) are OPEN (`vR18-1:3,9`).
   - S_γ/q² at βU = 2 rises from 0.165 to 0.311 over L = 6–16 (`vR18-1:9`).
   - ρ is a valid directional test (`vR18-1:7`). Z₀ is GAP-CLOSED for the uniformly LR-local class (`vR18-1:11`).
2. **R17-6 / vR17-6.**
   - Identity V (`rR17-6:209-214`), narrowed: along kẑ a vector gap forces only γ_x, γ_y to be o(k²) (`vR17-6:15`).
   - Lemma R, narrowed (`vR17-6:15`).
3. **R17-1 / vR17-1.** The patterns, and D(Gδ) = −M₀(δ) (`vR17-1:10`). Lemma D below makes it explicit per component.
4. **N0914.** Stencil (`:95-97`).
5. **Comparators (RECALLED):**
   - Pretko: rank-2 vector charge theory; dipole and angular-moment conservation follow from the Gauss law.
   - Prem–Vijay–Chamon: pinch points.
   - Lebowitz–Percus (1961): canonical and GC correlations differ by O(1/V) when ξ ≪ L.
   - Fragmentation under dipole conservation (Sala et al.; Khemani–Hermele–Nandkishore, 2020).
   - Fracton glassiness (Chamon 2005; Prem–Haah–Nandkishore 2017).
   - Subsystem (planar) symmetries.

## 3. Analytic results

**Lemma D (the dipole is the label count; proved; checked `s1_dipole_lemma.out`).**
- For finitely supported integer δ with N0914's stencil, Σ_x (Gδ)_j(x) = 0.
- D_ab(Gδ) := Σ_x x_a(Gδ)_b(x) equals −Σ_x δ_aa(x) for a = b. For a ≠ b, D_ab = D_ba = −Σ_x δ_ab(x) over face slots.
- *Proof.* A diagonal δ_jj at x gives +1 on edge (x − e_j, j) and −1 on (x, j). A face δ_ij gives ±1 on (x, j)/(x + e_i, j) and on (x, i)/(x + e_j, i). ∎
- So D(γ) = −M₀(n)/2 is symmetric, with identically zero angular part. For non-wrapping flips, dD = 0 ⟺ dN_ab = 0 for all six types. On the torus, N_ab is the well-defined form.
- *Checked.* 832 sign lifts of the 4 pattern copies and 2000 random integer δ: 0 failures.

**Lemma E (the static measure sees only the class; proved, standard).**
- The proposals are symmetric involutions, and the filter is symmetric (the reverse flip has −dN).
- So Metropolis gives detailed balance for π ∝ exp(−βUΣγ²)·1_C on each class C.
- The RK equal-time readout depends on π alone.

**Proposition M (mixture; proved, exact).**
- S_GC(k) = Σ_N P(N) S_N(k) for every k and every channel.
- With Lebowitz–Percus (comparator), S_N(k) = S_GC(k) + O(1/V) at fixed k ≠ 0 when ξ ≪ L (suggested).
- So a finite number of conserved totals cannot turn R18-1's finite S_γ/q² into o(k²) (suggested; checked in §4.2).

**Lemma P (planar laws of M1; proved by pattern inspection; checked `s4_planar.out`).**
- Cube flips touch no diagonal slot.
- Each μ8 orientation holds two diagonal pairs, and each pair lies in one plane perpendicular to its own index. For example, the xz-μ8 has its zz pair at equal z and its xx pair at equal x (`s4_planar.out:2-4`).
- A balanced flip is one-up-one-down on each pair. So M1 conserves N_aa(plane x_a = c) for all a and c: 3L numbers.
- Σ_{x,y}(Gn)_z(x,y,z) = N_zz(z+1) − N_zz(z) (checked). So these laws freeze the net a-charge of every a-plane.
- *Checked.* 9000 sweeps at L = 6 leave every N_aa profile unchanged, while N_xz(z) and N_xz(x) change.
- **M1 is not ergodic on the dipole sector.** Its classes are labelled at least by the three diagonal plane profiles. M2 breaks these laws (`s8_ext_checks.out:2`).

**Lemma F (what a planar law can freeze; proved).**
- Along k ∥ ẑ, Identity V decouples γ_x ↔ n_xz, γ_y ↔ n_yz, γ_z ↔ n_zz (`rR17-6:211-214`).
- n_s(kẑ) = Σ_z e^{−ikz}N_s(z) vanishes for every k ≠ 0 when N_s(z) is conserved and uniform.
- Under M1 only the zz laws hold. So in M1's uniform class γ_z(kẑ) ≡ 0 (scalar-longitudinal), but the vector part γ_x, γ_y, which Z₀ and Identity V need (`vR17-6:15`; `rR18-1:178-186`), is free.
- If every row slot's plane counts are conserved (§4.4), all three vanish on the axes. Off-axis momenta are constrained by no planar law.

**The expectation's mechanism fails (proved).**
- In R18-1's screened ensemble, S_γ ∝ k² already holds (S_γ/q² finite; `vR18-1:9`). Identity V needs o(k²).
- Lemmas D and E: dipole conservation on the moves fixes six numbers. It imposes no Gauss law on the static measure.

## 4. Numerics

### 4.1 (a) Detailed balance and small-L ergodicity (checked; `s2_exact_L2.out`, `s8_ext_checks.out`)
- **L = 2 coset (1024 states, as R18-1).**
  - **M1:** 53 N-sectors and 511 classes; 44 N-sectors are split. Class sizes: 504 singletons, six of 16, and one of 424.
  - **M2:** 53 classes, equal to the 53 N-sectors; none is split. M2 is ergodic on every N-sector at L = 2.
- **M1 MC against the exact restricted law on the 424-state class:**
  - ⟨Σγ²⟩ = 7.2567 ± 0.0215 vs 7.2453 (βU = 0);
  - 0.4082 ± 0.0070 vs 0.4216 (βU = 1);
  - 0.0085 ± 0.0012 vs 0.0080 (βU = 2).
  - The max state-probability difference is 0.0007, 0.0105 and 0.090. The last is a mixing limit between γ = 0 states (suggested).
- **Caveats.** μ8 wraps at L = 2, where dN = 0 is the torus-safe form of dD = 0. No half-filled state exists at L = 2. L ≥ 3 cannot be enumerated (coset dimension 78 at L = 3; `rR18-1` s1).

### 4.2 (b) The dipole sector itself: exact canonical sampling (checked; `run_bias.py`, `run_ptb.py`)
- **Method.** The GC chain with weight exp(−βUΣγ² − λΣ(N_ab − V/2)²), λ = 0.3, measured only when all N_ab = V/2. The bias depends only on N, so the measurements are exactly the canonical law on the full sector. The GC chain is irreducible on the coset (`vR18-1:5`).
- **PT** in βU (the bias is the same in every replica, so swap ratios are exact):
  - L = 6 full ladder: 108 round trips;
  - L = 6 focused ladder (βU from 2 to 3.5): 2 seeds, 99 trips each;
  - L = 8: 11 trips.
- **GC rerun** with the same code (rechecks R18-1): L = 6, βU = 2 gives E/edge 0.08407 ± 0.00021 and ξ² = 1.417/1.434; L = 8 gives 0.08447 and 1.388/1.446.

| βU | L | E/edge, sector | E/edge, GC (`rR18-1`) | ξ²(q₁)/ξ²(q₂), sector | ξ², GC | S_γ/q²(q₁), sector | GC |
|---|---|---|---|---|---|---|---|
| 0.5 | 6 / 8 (PT) | 0.27344 / 0.27311 | 0.27241 / 0.27223 | 0.109/0.083; 0.036/0.116 | 0.088/0.096; 0.113/0.098 | 0.211 / 0.221 | — |
| 1 | 6 | 0.19364 ± 0.00036 | 0.19225 | 0.326/0.302 (PT 0.279/0.306) | 0.305/0.296 | 0.217 | — |
| 1 | 8 | 0.19285 ± 0.00016 | 0.19205 | 0.288/0.299 (PT 0.262/0.331) | 0.317/0.290 | 0.238 | — |
| 1 | 10 | 0.19257 ± 0.00015 | 0.19202 | 0.315/0.305 | 0.248/0.298 | 0.252 | — |
| 1 | 12 | 0.19218 ± 0.00012 | 0.19216 | 0.267/0.281 | 0.330/0.295 | 0.259 | — |
| 1.5 | 6 / 8 (PT) | 0.13126 / 0.13056 | 0.12995 / 0.13004 | 0.700/0.697; 0.735/0.660 | 0.692/0.687; 0.698/0.671 | 0.203 / 0.238 | — |
| 2 | 6 | 0.08478 (3 more runs: 0.08465–0.08518) | 0.08407 | 1.423/1.412 (others 1.381–1.449 / 1.388–1.477) | 1.417/1.434 | 0.165 | 0.165 |
| 2 | 8 | 0.08492 ± 0.00016 (PT 0.08460) | 0.08447 | 1.386/1.381 (PT 1.628/1.545) | 1.388/1.446 | 0.214 | 0.213 |
| 2 | 10 | 0.08455 ± 0.00013 | 0.08461 | 1.367/1.444 | 1.378/1.431 | 0.251 | 0.247 |
| 2 | 12 | 0.08473 ± 0.00010 | 0.08437 | 1.460/1.404 | 1.412/1.358 | 0.273 | 0.278 |
| 2.5 | 6 (3 runs) | 0.05261–0.05338 | 0.0527 | 2.57–2.93 / 2.62–2.76 | 2.68–2.79 / 2.74 | 0.119–0.121 | — |
| 2.5 | 8 (PT) | 0.05393 ± 0.00034 | 0.0532 | 2.884/2.866 | 2.65–2.68 / 2.69–2.73 | 0.174 | — |
| 3 | 6 (3 runs) | 0.0240–0.0272 | 0.0315–0.0321 | 7.3–8.7 / **5.4–9.8 (seed-unstable)** | 4.9–5.1 / 5.1 | 0.063–0.068 | — |
| 3 | 8 (PT, 11 trips) | 0.03427 ± 0.00050 | 0.0324–0.0326 | 5.71/4.25 | 4.77–4.98 / 5.01–5.13 | 0.129 | — |
| 3.5 | 6 (2 seeds) | 0.0105 / 0.0166 | 0.0173 | 8.4/22.8 vs 17.1/5.8 (**unstable**) | 9.7/10.1 | — | — |

GC columns: `rR18-1:127-137`; `s5b_pinch_table.out` in R18-1's scratch folder.

**Checked.**
- For βU ≤ 2.5 the conserved-dipole sector matches the GC ensemble in ξ² at every L run, with ξ² independent of q and L.
- The energy differs by O(1) in the extensive total: 0.9, 1.2 and 1.6 at L = 6, 8, 10 for βU = 1.
- Face and body channels match GC (L = 6, βU = 2: S_V/S_TT 0.304/0.265 vs 0.304/0.264; `s7_offaxis.out`).
- S_γ/q² is finite. It rises with L toward a plateau and does not tend to 0.

**At βU ≥ 3 the sector is not certified.**
- At L = 6 the seeds disagree and sit below GC in energy, with ξ ≈ L/2.
- At L = 8, ξ² = 5.7/4.2 is close to GC and does not grow from L = 6 to L = 8.
- Every run gives a finite ξ (ξ/L ≤ 0.5 at L = 8). None shows ξ ∝ L. But the R18-1 referee's standard (seed-stable fits) is not met at βU = 3 and 3.5.

### 4.3 The local chains: fragmentation, ergodic repair, glass (checked)
- **M1 (registered).** Hot and cold starts disagree at every βU, including 0.5.
  - L = 6 PT, 1.2×10⁵ sweeps: E/edge 0.27550 vs 0.27082 (βU = 0.5) and 0.07293 vs 0.04555 (βU = 3); GC 0.2724 and 0.032.
  - By Lemma P these are different classes: the hot class keeps the random plane profile of a βU = 0 state, with frozen plane charges.
  - Even so, the vector-channel ξ² at βU ≤ 1.5 is GC-like in every class: hot 0.10/0.30/0.72, cold 0.08/0.27/0.78 at βU = 0.5/1/1.5; ρ(q₁) ≥ 0.59 at βU ≤ 1.5 in every M1 run.
- **M1, uniform-profile class** (prepared by `s6_prep_uniform.py`). At βU = 1:
  - ξ² = 0.39/0.30, 0.52/0.29 and 0.30/0.35 at L = 6, 8, 10 (GC 0.30);
  - axis S/TT = 0.17–0.19 against 0.48–0.53 in the sector: the frozen zz part (Lemma F);
  - V/TT on axis, face and body is GC-like: 1.08–1.33, 0.64–0.76, 0.52–0.63.
  - At βU = 2 this class did not equilibrate (ξ² = 0.7/2.4, 8.2/0.9, 1.5/2.8), so those numbers are not used.
- **M2 (declared second family).**
  - **L = 6 PT, hot vs cold:**
    - E/edge 0.27432/0.27348 (βU = 0.5), 0.19289/0.19313 (1) and 0.13104/0.12998 (1.5). The sector values are 0.27344, 0.19357 and 0.13126.
    - ξ² = 0.085/0.076, 0.298/0.294 and 0.699/0.692. The sector values are 0.083–0.109, 0.279–0.326 and 0.700.
  - **L = 8, βU = 1, single chains:**
    - E/edge 0.19243 ± 0.00026 vs 0.19261 ± 0.00035 (sector 0.19285 ± 0.00016).
    - Off-axis V/TT 0.722/0.711 (face) and 0.590/0.598 (body); sector 0.679–0.726 and 0.592–0.603.
  - **L = 6 PT, longer runs (3×; 19 and 12 round trips), hot vs cold:**
    - E/edge 0.27358/0.27374, 0.19369/0.19333, 0.13108/0.13035 and 0.08516/0.08542 at βU = 0.5, 1, 1.5, 2. The sector values are 0.2734, 0.1936, 0.1313 and 0.0847–0.0852.
    - ξ²(q₁)/ξ²(q₂) at βU = 2: 1.57/1.47 and 1.65/1.54 (± 0.1–0.25). The sector gives 1.38–1.45/1.39–1.48.
    - Face and body V/TT at βU = 2: 0.296/0.263 and 0.335/0.267. The sector gives 0.307/0.259.
  - **βU = 2.5:** hot and cold disagree (ξ²(q₁) 4.3 vs 2.3, and E/edge above the sector's), so the chain is not equilibrated. Those numbers are not used.
- **Why the local chains are slow at βU ≥ 2 (checked, `s3b_moves_compare.out`).** Non-raising moves available per canonical L = 6 state:

  | βU | GC chain | M1 balanced | M2 balanced |
  |---|---|---|---|
  | 1 | 209.5 | 23.3 | 45.1 |
  | 2 | 54.7 | 6.4 | 10.1 |
  | 3 | 8.5 | 1.1 | 1.4 |

  No canonical state sampled at L = 4 or 6 is frozen: every one had at least 14 (L = 4) or 70 (L = 6) balanced M1 flips available (`s3_frozen.out`). This is the fracton-glass pattern (comparator). Activated relaxation is suggested, not shown.

### 4.4 Stress test of the axis diagnostic: planar laws on every row slot (checked; `mcplanar.py`, `run_planar.py`)
- **Filter.** Each slot type's counts are conserved in every plane perpendicular to each of its indices. The start is a prepared state with all those counts at L²/2. The planar filter passes 5–6% of proposals.
- **Results, L = 6, 8, 10 at βU = 1 and 2.**
  - On the axes, ρ = 0 and S_γ(k ∥ axis) = 0 exactly (`s5_table_planar.out`), at 0.15–0.19 charged edges per edge.
  - Off-axis at βU = 1: S_V/S_TT = 0.58, 0.72, 0.78 (face) and 0.51, 0.62, 0.68 (body), against the sector's 0.63, 0.73, 0.76 and 0.52, 0.59, 0.64. Face and body S_γ/q² = 0.15–0.22, as in the sector.
  - The βU = 2 planar runs did not equilibrate (E/edge 0.15–0.18). Their exact axis zeros hold configuration by configuration.
- **Reading.** An axis-line zero is not a pinch point.
  - It fails "S_γ = o(k²)" off-axis.
  - It needs a prepared, measure-small sector, which is a state privilege (`AX:94-95`).
  - It is non-ergodic.
- **Correction to carry forward.** R18-1's ρ diagnostic (`rR18-1:113-116`; accepted for the screened setting at `vR18-1:7`) must be paired with face and body channels whenever a move set has subsystem conservation laws.

## 5. Readings against the FIXED clauses (`TESTS:6894-6896`)

- **PINCH-PRESENT: no (checked).**
  - No ensemble or class shows ξ growing as L together with S_γ = o(k²) in all directions.
  - The only exact zeros are axis-line zeros from planar laws (§4.4) and the frozen zz axis channel of M1's uniform class (§4.3). Both are screened off-axis.
  - Not reached: the T₂ clause.
- **SCREENED: checked at βU = 0.5, 1, 1.5, 2, 2.5,** for the fixed-dipole sector at L = 6–12, which is what an ergodic move set samples. M2 is ergodic at L = 2 exactly, and it is checked directly as a local dipole-conserving chain: hot and cold agree with the sector at L = 6 for βU ≤ 2, and at L = 8 for βU = 1. ξ is finite and L-independent.
  - **Not met:** "at every finite βU tested", because βU = 3 and 3.5 are not seed-stable. Their ξ is finite and does not grow from L = 6 to L = 8, but not certifiably.
- **OPEN: recorded.** Two reasons:
  1. βU ≥ 3 is not certified;
  2. "including non-ergodic moves": M1, the bare registered patterns with the dipole filter, is non-ergodic (Lemma P).

  If the referee scopes the tested set to βU ≤ 2.5 and the move set to M2, the reading is SCREENED.
- **Expectation check (`TESTS:6897`).**
  - "PINCH-PRESENT": not observed.
  - "Dipole conservation makes the charges hyperuniform (S_γ ∝ k²) at any fugacity": S_γ ∝ k² was already true without it, and it is not the pinch condition. Dipole conservation on the moves changes the static measure only by the sector (Lemmas D and E).
  - "It costs a new conservation law": yes. With R18-1's patterns it also brings 3L planar laws.
  - "Static window only": no window opened.

## 6. (c) Helicity check

Not triggered: no pinch appeared.
- In the stress test, the axis zeros sit in V and in the zz part of S along the axis, not in T₂.
- The T₂ component S_xz(k ∥ y) stays finite: S_T(q₁) = 0.82–1.17 at βU = 1 (0.42–0.53 at βU = 2, not equilibrated).

## 7. (d) Prices (named, never adopted)

| Price | Status | Axiom touched | Buys |
|---|---|---|---|
| **P-r18-10a** (new): the γ-dipole conserved by the moves ≡ six conserved label totals N_ab (Lemma D) | named | Admissibility is a static distribution rule and "not a dynamics axiom" (`AX:57-61`, `AX:116-123`). A conservation law on moves is new structure | **Nothing static.** The same ξ as R18-1 (Lemma E; §4.2). It costs glassy local dynamics (§4.3) |
| **P-r18-10b** (new; comes with R18-1's patterns plus the filter): 3L planar diagonal-label laws, i.e. a frozen net charge per plane | named | as above, plus subsystem structure on the Lattice (`AX:37-41`) | Fragmentation, and a frozen zz axis channel in a chosen class; no vector-channel effect |
| **P-r18-10c** (stress test only): planar laws for every row slot, plus a prepared uniform sector | named, not proposed | as above, plus a privileged state (`AX:94-95`) | Axis-line zeros, a false positive of the axis diagnostic. Screened off-axis |
| P112, P113, RK bridge | carried (`rR18-1:227-229`) | Lattice, Qubit, Record readout | the setting |
| **P96** | sharpened, no new number | Admissibility (dynamical) | A conservation law on the moves of an RK ensemble cannot replace exact charge suppression. The static route is still exact emergence, or a non-local or non-RK weight |

**Counting convention.** No tunings or counterterms arise.

## 8. Round-18 rule checklist (`TESTS:6395-6405`)

- **Vertices:** none used.
- **Λ:** not applicable.
- **Spectra:** none (excluded by the setting).
- **Certificates:** no CONFLICT is claimed.
- **v_max:** not applicable (static classical MC).
- **Controls.** All on the same observable and stencil:
  - the GC rerun reproduces R18-1;
  - the exact sector sampler is checked against GC;
  - the planar stress test is a constructed false-positive control for the diagnostic;
  - R18-1's corrected same-component Gaussian control passes (`vR18-1:7`).
- **Readout bridge:** RK equal-time S plus P113.
- **Forks and exclusions:**
  - other cosets, and N ≠ V/2;
  - dynamics beyond their classes;
  - βU ≥ 3 (not certified), and βU ≥ 2 for the M1 classes;
  - spectra;
  - integer lifts.
- **Removed hypothesis:** stated (§1).

## 9. Strong words and scope

- **Proved (unrefereed):**
  - Lemma D;
  - Lemma E;
  - Proposition M (the identity; ensemble equivalence itself is comparator);
  - Lemma P;
  - Lemma F;
  - F_all-uniqueness of Q = 0;
  - the failure of the expectation's mechanism.
- **Checked:**
  - s1, s2, s3, s3b, s4, s8;
  - the sector tables for βU ≤ 2.5 at L = 6–12;
  - the M1 classes at βU ≤ 1.5;
  - the M2 hot/cold agreement at βU ≤ 2 (L = 6) and βU = 1 (L = 8);
  - the stress test at L = 6–10.
- **Suggested:**
  - ensemble equivalence at βU ≥ 3;
  - M2's ergodicity at L ≥ 4, which is not provable by enumeration;
  - activated glassy relaxation.
- **"Exactly"** is used only for the lemmas, the L = 2 enumerations, and the planar zeros, which hold in every configuration of the sector.
- **Not covered:**
  - βU ≥ 3 certification;
  - local-chain equilibrium at βU ≥ 2.5 (M2), and at βU ≥ 2 in the M1 classes;
  - non-trivial cosets;
  - other dipole-conserving move sets;
  - the quantum RK ground space. Under M1's fragmentation it is degenerate, which Z₀'s (H2) excludes (`rR18-1:176`).

## Files (`S/`)

- `METHOD.md`.
- `scripts/` (each `s*.py` has its `.out`):
  - `common.py`, `mc.py`, `analyze.py`, `s5b_pinch_table.py`: R18-1's, copied unchanged and rechecked by the GC rerun;
  - `mc10.py` (M1 filtered chain), `ext.py` (M2), `mcpair.py` (exact sector sampler and planar drive), `mcplanar.py` (stress test);
  - `run_c.py`, `run_ptc.py`, `run_bias.py`, `run_ptb.py`, `run_planar.py`;
  - `s1_dipole_lemma`, `s2_exact_L2`, `s3_frozen`, `s3b_moves_compare`, `s4_planar`, `s6_prep_uniform`, `s8_ext_checks`;
  - the tables `s5_table.out`, `s5_table_planar.out` and `s7_offaxis.out`, plus `all_runs.log`;
  - the batch scripts and `finalize.sh`.
- `data/`: pickles and logs for every run cited.
