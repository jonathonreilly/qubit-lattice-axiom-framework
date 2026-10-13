# C5 R19-16 report: R19-9's photon kernel repaired (no seam, no NaN); W1 exact torus-wide; root re-solved

**Author and status.** Claude Opus 5.5 probe (same family as the supervisor and every C5 worker). Unrefereed. 2026-10-13, 05:43Z to 06:12Z. No repository file was edited. Nothing was downloaded. Every run used `OMP_NUM_THREADS=2` and took under 4 min (the N = 224 row runs took 223–235 s).

**Paths.**
- `P/` = `.claude/science/exercises/gravity-current-state-20261009/`.
- `S/` = `.../scratchpad/C5/R19-16/`. My scripts and `.out` files are at the top level of `S/`. `S/orig/` holds an unmodified copy of `scratchpad/C5/R19-9/` (lib199.py, the arch* folders, the scripts) plus the referee's `referee_R19_9_check.py`.
- `vR19-9` = `P/agents/C5_R19-9_referee_verdict.md`.

**Read.**
- `docs/MINIMAL_AXIOMS_2026-06-29.md`, all of it.
- `P/TESTS.md`: the C5 method (`:2302-2319`); R19-5 (`:7317-7349`, worker reading `:7470-7490`, verdict `:7747-7752`); R19-9 (`:7544-7568`, worker reading `:7761-7771`, verdict `:7862-7873`); my item (`:7904-7918`).
- `vR19-9` in full; `scratchpad/C5/ref_R19-9/referee_R19_9_check.{py,out}`; R19-9's report §§0–3.1; `lib199.py` in full.

**Labels:** proved (a complete argument under stated hypotheses; unrefereed) / checked (numerics here) / suggested / reading / comparator.

---

## 0. In plain words

1. **The two defects were reproduced exactly (checked).** I ran the referee's own script against R19-9's unmodified `lib199`. It gives:
   - seam residual 1.603e-12 at q_x = 9.99e-8 (and 8.02e-13 at 5e-8);
   - a kernel jump of 1.489e-5 across |q_j| = 1e-7;
   - an exact zero soft leg that is not finite (12 warnings).

   Each value matches `vR19-9` to the last digit (`r1916_referee_check_ORIG.out:11-15`).
2. **Three repairs. Each is a pure implementation change; the law data are unchanged** (`S/lib1916.py`, which patches the `lib199` module object; the file itself is not modified).
   - **R1. One divided-difference formula for the whole torus, with no switch.**
     - The formula is Δ_j = [q/dsym(q)]·∫₀¹ g′(k₂ + tq) dt, with g = σ² and g′ = 2σc (Hadamard's lemma). It is the same function as the quotient (σ₁² − σ₂²)/dsym(q) wherever that quotient is defined, and at q_j = 0 it gives the analytic limit g′(k₂).
     - The integral is done by composite Gauss–Legendre, split at the non-analytic points ±b and ±π.
     - The factor q/dsym(q) is exactly 1 for |q| ≤ 1.
   - **R2. The soft-leg time components come from the analytic Neumann series in h(k_soft), on both sides and on the whole support.**
     - R19-9 used the series only as a check. The eigen-sum it used divides by ω_soft².
     - At k_soft = 0 the series gives −R h₂⁺ (left soft) or h₁⁺R (right soft). Both are finite.
   - **R0. The photon law γG_w(2.9435, 0.198093) is evaluated from its definition,** not from the archived 400001-point table.
     - R1 needs this: with the table, σ is piecewise linear, so the q → 0 limit of the exact quotient jumps by 5.0e-4 at every table node (`r1916_tabkink.out`). No uniform analytic Δ exists for the table.
     - The table differs from the definition by at most 1.4e-10 in σ and 1.9e-9 in c at the evaluators' sample points.
3. **W1 is exact torus-wide (checked).** Every family below has a physical-block residual ≤ 2.3e-15 absolute. That is about 400 times below the 1e-12 bar. The families cover:
   - the referee's seam point;
   - 171 targeted q values from 0 to 1;
   - 4374 kernels at exact special points (0, ±1e-300, ±b, ±π, the |q| = π tie);
   - exact zero legs on either side and on both;
   - R19-9's ten targeted families and its 40,000 dense pairs at r = 0.1 and 0.05;
   - 40,000 new dense pairs aimed at small q, the q_j = 0 planes, the k_j = 0 planes and soft legs.

   The kernel is continuous wherever it was not before. Line scans across the old switch have second differences of 7e-16 to 1.2e-15, against 1.49e-5 for the original. At an exact zero leg the kernel equals the limit from every direction, with the difference ∝ ε.
4. **The root re-solve is unchanged by the repairs (checked).**
   - The repairs touch only scattering blocks and soft-leg time components, and the TT rows see neither. R19-9's re-solve, rerun under the patch, reproduces `r199_resolve.out` exactly (difference 0.0).
   - With the law evaluated analytically (R0), the N = 224 photon rows move by ≤ 8e-10 per vector, so the root was re-solved. All six rows are again zero to the model's floor:
     - photon-bearing rows ≤ 1.4e-12;
     - direct N = 224 face rows ≤ 3.6e-12;
     - μ_E ≤ 5.6e-11, the scalar/Dirac evaluator floor already present in R19-9's own run.
   - Knob shifts against R19-9 are ≤ 3.9e-8 in b_s. That is about 1000 times below the root's quadrature ambiguity (4.7e-5).
5. **Worker reading: PHOTON-EXACT** (unrefereed), within R19-9's inherited scope: one loop, the supplied vacuum, ultralocal seagull, SF, VWa-geo, class 𝒢 (P-R19-5a), linearized W1 only (not W2), m = 0.01. No new price.

---

## 1. Setting, hypotheses, prior art (counted once)

- **Setting** (`TESTS:7912`). R19-9's construction (pieces C, A, B, the glue, the fibre identification I, VW at the root a, w_d, w_o; R9-9's graviton dsym) and its root (U, UD, VW-exact; r = 0.05 and 0.1).
- **Removed hypothesis** (`TESTS:7914`): the finite-width numerical fallback.
- **Carried (not derived):** everything R19-9 carried (R19-9 report §1; `vR19-9:21`). That includes the TT rows seeing only the spatial pair block (R19-5 §1, vR19-5 item 3).
- **Prior art:**
  - **R19-9 and vR19-9.** The seam is at `lib199.py:113-123` (fallback |q_j| ≤ 1e-7 with a separately interpolated `cfun`). The NaN comes from `lib199.py:55-58,151-160,173-180`: `glued` calls the eigen-sum `sylv`, whose projectors divide by ω² = 0 (`vR19-9:5,9`).
  - **R19-5 and vR19-5:** the outline, P-R19-5a/b, and the removable limits on coordinate planes that must be implemented (vR19-5 item 4).
- **Comparator:** Hadamard's lemma, i.e. the divided difference of a C^∞ function is C^∞ in both arguments (RECALLED).

## 2. The repairs (proved; `S/lib1916.py`)

**R0. Analytic law** (`lib1916.py:33-79`).
- c(k) = 1 − sstep((|k| − b)/w), in closed form.
- σ(k) = sgn(k)d(|k|), with d(x) = x for x ≤ b and d(x) = x − wS((x − b)/w) beyond, where S(u) = ∫₀ᵘ sstep.
- S is evaluated from a 4096-panel cumulative table built with 16-point Gauss–Legendre, plus one GL panel to the target. S(1) = ½ exactly, by sstep(t) + sstep(1 − t) = 1, so d(π) = (π + b)/2.
- Checked against 40-digit mpmath at 106 points (60 in the transition): σ to 2.8e-16 and c to 8.3e-16 (`r1916_law.out:2`).
- **Why R0 is needed (checked).** With the archived table, σ is piecewise linear. The exact quotient at q = 1e-10, centred 1e-9 either side of a table node, then jumps by 5.0e-4; with the analytic law the change is 1.2e-7, which is just the smooth g″·2e-9 (`r1916_tabkink.out`). So no fallback, however narrow, can make the table kernel continuous on the q_j = 0 planes. The referee's 1.49e-5 jump is this table kink seen through a 1e-7-wide window.

**R1. Uniform divided difference** (`lib1916.py:81-121`).
- **Formula.** Δ_j = [q_w/dsym(q_w)]·(1/(k₁ᵘ − k₂))∫_{k₂}^{k₁ᵘ} g′.
  - q_w = wrap(k₁ − k₂) is the graviton's own convention.
  - k₁ᵘ is the image of k₁ with k₁ᵘ − k₂ = q_w. This includes the tie q_w = +π.
  - g′ = 2σc is periodic and C^∞, since c is flat zero at |k| = π.
- **Proof.** g is C^∞ and periodic, so (g(k₂ + q) − g(k₂))/q = ∫₀¹g′(k₂ + tq)dt is C^∞ in (k₂, q) (Hadamard). q/dsym(q) is C^∞ and nonzero on (−π, π], and equals 1 exactly for |q| ≤ 1, where `plateau` = 1. So Δ_j is C^∞ on the torus², it equals the quotient wherever that is defined, and R19-9's dust-block identity Σ_j d_jΔ_j = ω₁² − ω₂² (vR19-9 item 2) holds pointwise. ∎
- **Implementation.**
  - Composite 16-point GL with panels ≤ 0.02, split at ±b and ±π.
  - No branch: the direct quotient survives only as an optional cross-check (`QS = inf`).
  - The segment uses the actual endpoints, so no `wrap()` rounding enters it.
- **Checked** (`r1916_law.out:4-5`):
  - **Against the 40-digit reference,** on 165 segments (q from 1e-12 to π; the transition, the box edge b, the BZ face, the |q| = 1 plateau edge, the |q| = π tie, the referee's seam): max error 1.7e-14 absolute (6e-15 relative). That is the conditioning floor |∂Δ/∂k|·ulp(k) ≈ 30 × 4.4e-16, i.e. the quadrature nodes are themselves rounded.
  - **Against the direct quotient at the same point,** 400 pairs with |q| from 0.1 to π: ≤ 4.0e-15.
  - **Across the old 1e-7 switch:** 8.9e-16. **At q = 2e-12 against q = 0:** 1.1e-15.

**R2. Soft legs** (`lib1916.py:122-155`).
- **Left soft** (full × T₂): X = −Σ_n h₁ⁿR(h₂⁺)ⁿ⁺¹ solves h₁X − Xh₂ = RP_{T2}.
- **Right soft** (T₁ × full): X = Σ_n(h₁⁺)ⁿ⁺¹Rh₂ⁿ solves h₁X − Xh₂ = P_{T1}R.
- Here h⁺ = (Π₊ − Π₋)/ω is the pseudo-inverse on the hard side.
- **Proof.**
  - Telescoping gives h₁X − Xh₂ = P_{T1}R in two lines, and the left identity the same way.
  - On the support of φ_A·(1 − χ_C), the soft leg is < r/8 and the hard leg > r/2. Then ω_hard ≥ min(|k|, b) gives ratio < ¼, so the series converges geometrically.
  - The solution with the stated support is unique, because the spectra {0, ±ω_soft} and {±ω_hard} are disjoint. So the series equals R19-9's eigen-sum as a matrix, not only on the physical block.
  - At k_soft = 0 the series gives −Rh₂⁺ or h₁⁺R. ∎
- **Checked:** Neumann series against eigen-sum ≤ 7.2e-16 relative on the full 4×4×6×6 kernel, both sides, |k_soft| from 1e-6 to 1 × r/8 (`r1916_neumann_full.out`); ≤ 6.4e-16 on the physical block (`r1916_seam_zero_r0.1.out:17`).
- **No `projs` on soft legs.** After R2 the kernel never calls `projs` on a leg below r/16: piece B needs both legs ≥ r/16, and R2 calls `projs` only on the hard leg.

**Unchanged:**
- pieces C and B (apart from Δ), the glue, the fibre identification I, the VW vertex, dsym, SIGN;
- the law data (r, the glue profile, the scattering kernel);
- the bill (6 equalities + 1 window).

## 3. Checks (all with the repaired kernel unless marked)

| check | result | file |
|---|---|---|
| referee's script, ORIGINAL lib199 (reproduction) | seam 8.02e-13 / **1.603e-12** / 1.97e-16 at q = 5e-8 / 9.99e-8 / 1.001e-7; jump **1.489e-5**; zero leg **not finite** (12 warnings); Prop K and face values as `vR19-9` | `r1916_referee_check_ORIG.out:11-20` |
| referee's script, unmodified, REPAIRED kernel | seam 2.64e-16 / 2.07e-16 / 1.65e-16; jump 1.43e-10 (= the smooth change over Δq = 2e-10; S3 below); zero leg **finite, 0 warnings**; face continuity 2.69e-7 / 2.10e-9 (∝ gap, unchanged); Prop K identical (6.670789573264e-5, …, 1.609194844576e-4) | `r1916_referee_check_REPAIRED.out:2-21` |
| S1 seam point (3.05, 1.0, 0.7), q along x, y, z, 57 values in {0} ∪ [1e-16, 1] | max abs 5.9e-16 (`w1_resid`), 6.3e-16 (independent SVD transverse frame) | `r1916_seam_zero_r0.1.out:1-6` |
| S2 300 hard midpoints (transition / within 1e-6 of a face / uniform), small q in 1–3 components, exact planes | ≤ 9.9e-16 | `:7` |
| S3 continuity: \|M(0.999e-7) − M(1.001e-7)\| and at \|q\| = 1 ± 1e-9 | 1.43e-10 and 9.55e-10, equal to \|dM/dq\|·Δq from a wide central difference (old: 1.49e-5) | `:8-9` |
| Z1 exact zero leg: referee's k₂; 100 hard k₂; 100 k₂ in the corner annulus (C + A both active); both sides; k₁ = k₂ = 0 | all finite; W1 on (full soft side) × P_T(hard) ≤ 1.4e-15 abs; \|M(εn̂, k) − M(0, k)\| ∝ ε down to ε = 1e-12 (e.g. 1.4e-12); k₁ = k₂ = 0 gives residual 0 | `:10-16` (r = 0.05: `r1916_seam_zero_r0.05.out`) |
| E 4374 kernels at exact special points (components in {0, ±1e-300, ±b, ±π, mid-transition, random}), r = 0.1 and 0.05 | all finite, warnings as errors; max W1 1.8e-15 | `r1916_edges.out` |
| D1 10⁴ pairs, q = 10^U(−16, 0.5) × direction, components zeroed w.p. 0.2 (forward region, planes, wrapped faces) | ≤ 1.3e-15 abs (both frames), r = 0.1 and 0.05 | `r1916_dense_q_r0.1.out:1`, `_r0.05.out:1` |
| D2 10⁴ pairs, legs log-uniform 1e-12..π with exact k_j = 0 components | ≤ 2.0e-15 abs | `:2` |
| L1 line scans, 801 points: max second difference | REPAIRED 7.2e-16 / 1.2e-15 / 2.8e-15 (\|M\| ≤ 0.7); ORIGINAL 1.49e-5 / 8.63e-6 / 2.9e-15 (old switch at two midpoints; \|q\| = 1 edge) | `r1916_dense_q_r0.1.out:3-8` |
| R19-9 `r199_exact.py` (10 families), unmodified, r = 0.1 / 0.05 | ALL FAMILIES max abs 1.74e-15 / 1.74e-15 (R19-9: 6.5e-14, from the old fallback in "forward, q_l = 0 planes", now 6.2e-16); symmetry 0; Hermiticity 4.4e-16; (H-E) 3.9e-16; Lemma F 3.3e-16; pair block = VW outside U_r 8.0e-16; = continuum inside U_{r/2} 0; face jump ∝ gap | `r1916_exact_r0.1.out`, `r1916_exact_r0.05.out` |
| R19-9 `r199_dense.py`, 2 × 10⁴ pairs, r = 0.1 / 0.05 | ≤ 2.3e-15 / 1.9e-15 abs | `r1916_dense_r0.1.out`, `_r0.05.out` |
| R19-9 `r199_cov.py` (C₄z, C₃(111), C₂(110)) | ≤ 8.9e-16 | `r1916_cov.out` |
| R19-9 `r199_exact_extra.py` | Gauss-law scope unchanged (full-space residual 1.00); reflected-transposed kernel 6.7e-15 rel | `r1916_exact_extra.out` |

**Note on R19-9's item [4].** Under the patch, `r199_exact.py` item [4] compares the series with itself (0.0), because `piece_A` now defaults to the series. The real comparison is Z2 and `r1916_neumann_full.out`.

**Worst W1 residual anywhere: 2.3e-15 absolute (checked).** The relative maxima of 2e-14 to 3.4e-14 come from the "corner, on shell" family, where the cancelling terms are themselves ~1e-2 (absolute 1.3e-16).

## 4. Root re-solve (checked)

1. **The repairs do not enter the rows (proved; checked).**
   - R1 changes only scattering blocks (Π±·Π± with equal sign).
   - R2 changes only soft-leg time components, on a set of measure ~ (r/8)³.
   - The TT rows see only the spatial pair block (carried hypothesis, §1). The pair block equals VW outside U_r to 8.0e-16 (table above).
   - R19-9's `r199_resolve.py`, rerun under the patch, reproduces `r199_resolve.out` exactly: max |difference| over all knobs and rows = 0.0 (`r1916_resolve_repro.out:23-26`).
2. **R0 moves the photon rows slightly (checked).** I ran the archived evaluators (R18-9 `lib9.phot_quad`, R18-13 `vwface.xi_geo`), unmodified, with the analytic law at N = 224:
   - axial coefficients change by ≤ 5.8e-11, and μ_E^γ by −2.4e-12 (`r1916_photrows_axial_N224.out:1-3`);
   - face rows per vector change by +7.97e-10 (face1) and +5.03e-10 (face2) against the full-precision table (`r1916_photrows_face_N224.out:1`, `r1916_photrows_facetab_N224.out:1`);
   - the exact w-derivatives agree to 1e-10.
   - Control: R19-9's printed 7-digit w-derivatives were themselves off by 9e-9 to 2e-8. That alone moves (w_d, w_o) by (7.3e-8, 7.0e-9) (`r1916_resolve_tabfull.out`).
3. **The re-solve with the analytic law** (`r1916_resolve.py analytic`) uses R19-9's model executed from its own source, with only the photon inputs replaced (`r1916_resolve_analytic.out`):

| r | rows (T₂g, E_g, μ_E, μ_T₂, face1, face2) | knobs − R19-9's (b_s, b_f, r_D, a, w_d, w_o) |
|---|---|---|
| 0.05 | −7.5e-13, −6.1e-13, 1.75e-11, −3e-17, 5.3e-13, −5.9e-14 | +1.04e-8, +1.2e-9, +6.2e-10, −1.2e-11, +6.9e-8, +6.1e-9 |
| 0.1 | −1.37e-12, −1.07e-12, 5.58e-11, −1.3e-16, 1.10e-12, 1.4e-13 | +3.89e-8, +1.4e-9, +7.2e-10, −1.3e-11, +6.9e-8, +6.1e-9 |

   - Of the w_d shift, +7.3e-8 is R19-9's rounding (control above). Analytic against full-precision table: (+3.9e-8, +1.4e-9, +7e-10, −1.3e-11, −3.9e-9, −8.7e-10) at r = 0.1.
   - The corner-term shifts relative to r = 0 are unchanged: b_s +2.913e-6 against R19-9's +2.885e-6 at r = 0.1.
4. **The μ_E row's 2–6e-11 is the model's floor, not a photon effect (checked).**
   - The photon's μ_E is a constant, Vmu.
   - In R19-9's own run (tabulated law) the same row ends at 9.3e-11 (r = 0) and 3.3e-11 (r = 0.05) (`orig/r199_resolve.out`).
   - With a 1e-12 stopping rule, the iteration oscillates at ±4–7e-11 in μ_E (`r1916_resolve_analytic_tight.out`). The cause is the ill-conditioned b_s direction (σ_min 6.3e-4): ~1e-12 residuals in T₂g/E_g move b_s by ~2e-9, which moves μ_E by ~6e-11.
5. **Direct N = 224 face rows with the analytic law (checked).** This uses R19-9's `r199_direct_solve.py` from its own source, with the start totals recomputed rather than hard-coded, as the referee did. One Newton step in (w_d, w_o) (Δw ≈ 9.0e-7, 5.7e-8) gives direct face totals:
   - r = 0.1: (−6.0e-13, −1.9e-12);
   - r = 0.05: (3.6e-12, 3.4e-12).

   For comparison: R19-9 got −2.7e-11 / −2.2e-11, and the referee got 2.35e-12 / 3.67e-12 (`r1916_direct_r0.1.out:3`, `r1916_direct_r0.05.out:3`). Axial and μ rows do not depend on w (Lemma O(iii)); the corner term changes by ~1e-13.

## 5. Reading against the FIXED readings (`TESTS:7916-7917`)

**PHOTON-EXACT** requires "W1 ≤ 1e-12 torus-wide, including the referee's seam and zero-leg cases, and the SM root re-solved with all rows zero. Checked."
- **W1:** ≤ 2.3e-15 absolute in every family, including the referee's seam (2.6e-16) and the exact zero legs (≤ 1.4e-15, finite, equal to the limit). **Met (checked).**
- **Root:** re-solved with all six rows at the inherited model's floor, in the same sense `vR19-9` item 5 accepted for R19-9:
  - photon-bearing rows ≤ 1.4e-12;
  - direct N = 224 face rows ≤ 3.6e-12;
  - μ_T₂ ≤ 1.3e-16;
  - μ_E ≤ 5.6e-11 (the scalar/Dirac evaluator floor present in R19-9's run).

  Knob shifts are ≤ 3.9e-8 against R19-9. **Met (checked), with the floor stated.**

**Worker reading: PHOTON-EXACT** (unrefereed).

**Scope (not extended here):**
- one loop, the supplied vacuum, ultralocal seagull, SF for the μ rows;
- R18-13's VWa-geo off-axis extension;
- class 𝒢 (P-R19-5a);
- linearized W1 only (W2/W15 not addressed);
- m = 0.01;
- the rows at the inherited finite resolution (N = 224; b_s quadrature ambiguity 4.7e-5, `vR18-9`).

## 6. Prices

**None new.**
- The repairs are implementation: an exact representation of the same law functions and the same kernel.
- The law data listed by R19-9 (r, the glue profile, the scattering kernel) and P-R19-5a/b are unchanged and counted once.
- **One evaluator fact recorded (checked):** the archived tabulated photon law used by R18-9/R18-13/R19-9 differs from the stated law by ≤ 1.9e-9 in c and ≤ 1.4e-10 in σ at the sample points. Its effect on the root is ≤ 4e-8 in the knobs.

## 7. Files (all in `S/`)

- **Repaired library:** `lib1916.py`.
- **Runners for the unmodified originals:** `r1916_run.py` (runs `orig/` scripts against the patch), `r1916_resolve.py`, `r1916_direct.py`.
- **Checks:** `r1916_law.py`, `r1916_seam_zero.py`, `r1916_dense_q.py`, `r1916_edges.py`, `r1916_neumann_full.py`, `r1916_tabkink.py`, `r1916_photrows.py`.
- **Outputs:** `r1916_*.out`, `photquad_analytic_N224.npy`, `photface_{analytic,tab}_N224.npy`, `resolve_sols{,_analytic,_tabfull,_analytic_tight}.npy`.
- **Unmodified copies:** `orig/` (R19-9's code and the referee's script).
