# C5 R19-26 report: the q = ±π cut is a placement mismatch in the VW pair block, not in R1; a local re-placement removes it with the rows unchanged

**Author and status.** Claude Opus 5.5 probe (same model family as the supervisor and every C5 worker). Unrefereed. Worked 2026-10-13 from 06:39Z to 07:06Z. No repository file was edited and nothing was downloaded. Every run used `OMP_NUM_THREADS=2` and took under 4 minutes; the longest were the N = 224 runs at 184 s and 217 s.

**Paths.**
- `P/` = `.claude/science/exercises/gravity-current-state-20261009/`
- `S/` = `scratchpad/C5/R19-26/`. My scripts and `.out` files are at the top level of `S/`.
- `S/orig/` is an unmodified copy of `scratchpad/C5/R19-16/orig/`, i.e. R19-9's code.
- `S/lib1916.py` is an unmodified copy of R19-16's library.
- `S/ref_cut_check.py` is an unmodified copy of the R19-16 referee's `independent_R19_16_check.py`.
- `vR19-16` = `P/agents/C5_R19-16_referee_verdict.md`.

**Read.**
- `docs/MINIMAL_AXIOMS_2026-06-29.md`, all of it.
- In `P/TESTS.md`:
  - the C5 method, `:2302-2319`;
  - R19-5 at `:7317-7349`, with its verdict at `:7747-7752`;
  - R19-9 at `:7546-7568`, with its worker reading at `:7761-7771` and its verdict at `:7862-7873`;
  - R19-16 at `:7906-7918`, with its worker reading at `:8206-8217` and its verdict at `:8362-8370`;
  - my item, `:8401-8418`.
- `vR19-16`, in full.
- The referee's script and its output.
- The R19-16 report.
- `lib199.py` and `lib1916.py`, in full.
- R18-13's `vwface.py` docstring and vertex.
- R9-9 report `:100` and R17-12 report `:14-62` and `:193`.
- `P/agents/C5_R19-16_referee.md` does not exist; only the verdict file does.

**Labels:** proved (a complete argument under the stated hypotheses; unrefereed) / checked (numerics here) / suggested / reading.

---

## 0. In plain words

1. **The cut reproduces exactly (checked).** The referee's unmodified script, run against R19-16's kernel, matches `vR19-16` item 3 to the last printed digit (`S/ref_cut_check_REPRO.out:5-8`):
   - Δ_x → ±3.678165139;
   - raw kernel jump 1.310001203;
   - projected M⁰² jump 0.2791999734.
2. **R1 is not the defect (proved; checked).**
   - R9-9's graviton puts T^{0x} on x-links and T^{xy} at the plaquette centre (e_x + e_y)/2 (`R9-9 report:100`; `lib199.py:7-10`). Any local stress component there has a lattice Fourier symbol that must change sign when the transfer q_x passes ±π. This is Lemma P in §2.
   - So the opposite limits of the divided difference Δ_x (which feeds M^{0x} and M^{xy}) are required, not a fault.
   - R19-9's dust scattering block, which contains R1, obeys this rule: its placement-corrected jump is 4.1e-9 at ε = 1e-8, proportional to ε (`S/r1926_diag.out:14`).
3. **The real defect is the VW pair block (checked).**
   - R18-13's VWa-geo puts every off-diagonal bilinear at the *site*. Its docstring says "both fields averaged along their own index -> site" (`orig/arch18_13/vwface.py:9`).
   - lib199 nevertheless uses VW^{ij} directly as the kernel of a stress placed at (e_i + e_j)/2 (`lib199.py:85-93`, `:144-148`). That is an exact half-lattice shift, e^{−i(q_i+q_j)/2}, which is non-local on the lattice.
   - Checked: VW's spatial kernel is continuous across the cut when read as a site operator (8.5e-9). Read as a plaquette operator it jumps by 1.39 (`r1926_diag.out:16`).
   - Through the pair-block time components (d_x·VW^{xy}/λ) this gives the referee's projected M⁰² jump of 0.279. The largest placement-corrected jump, 0.749, is in M^{xz} (`r1926_diag.out:9-12,15`).
4. **The repair is a local re-placement, not a twisted I (proved; checked).** The off-diagonal VW stress is multiplied by F(q_i)F(q_j), with F(q) = (9cos(q/2) − cos(3q/2))/8 (`S/lib1926.py:23-39`).
   - e^{−iq/2}F(q) is a 4-point average over offsets ±½ and ±3/2. It moves a site operator to the half-integer position, it is strictly local, and F = 1 − 3q⁴/128 + O(q⁶).
   - Every other part of the kernel is unchanged: R0/R1/R2, the pieces, the glue, the fibre identification I, dsym and SIGN.
   - A twisted fibre identification cannot do this job. I enters only the scattering block, which already passes.
5. **The repaired kernel is W1-exact, smooth and quasi-local torus-wide (checked).**
   - **W1:** ≤ 2.0e-15 everywhere tested. That covers the referee's seam, exact-zero legs, 3000 targeted random pairs, R19-9's 10 families and its 2×10⁴ dense pairs at r = 0.1 and 0.05, and every cut point.
   - **The cut:** across q_l = ±π on all three axes, including soft legs, the placement-corrected jump is ∝ ε (8e-7 at ε = 1e-9).
   - **The referee's own projected M⁰² jump** falls from 0.279 to 3.3e-11 at ε = 1e-10 (`r1926_refcheck_replaced.out:8`).
   - **A convention-free test.** The lattice Fourier symbol along full lines on the q-torus needs no sign rule (§4, C6). For R19-16's kernel its Fourier coefficients fall off like 1/n, which is the signature of a jump and of 1/r non-locality. For the re-placed kernel they fall off faster than any power, down to 1.7e-15 (`r1926_fourier_soft.out`, `r1926_fourier_fine.out`).
6. **The rows are unchanged and the root re-solves (proved; checked).**
   - **Exact rows (proved).** F_iF_j = 1 + O(q⁴), and the rows are q → 0 second derivatives, so every row is unchanged. The axial rows (T₂g, E_g; q ∥ z) and μ_E (law-only) are identical by inspection; μ_T₂ is Dirac-only.
   - **Face rows at N = 224 (checked).** The evaluator's finite-q values move by 2.1e-8 per vector, falling off like N⁻⁴ ln N.
   - **Re-solve (checked).** One direct Newton step in (w_d, w_o) of (−2.6e-8, −1.3e-8) returns the direct N = 224 face totals to (2.1e-12, −1.2e-12) at r = 0.1 and (2.3e-13, 3.2e-12) at r = 0.05 (`r1926_direct_r0.1.out:3`, `r1926_direct_r0.05.out:3`).
7. **Worker reading: PHOTON-EXACT** (unrefereed), within R19-16's inherited scope. One new piece of law data, F (P-R19-26a), enters no row.

---

## 1. Setting, removed hypothesis, prior art (each counted once)

- **Setting** (`TESTS:8411`): R19-9/R19-16's kernel at the root (U, UD, VW-exact; r = 0.05, 0.1), with R19-16's repairs R0/R1/R2 kept, and the referee's cut script.
- **Removed hypothesis** (`TESTS:8414`): "an untwisted, transfer-cut divided difference". Finding: the divided difference was never the problem (§2). The hypothesis that actually failed is that VW^{ij} may serve as the stress kernel at R9-9's placement.
- **Carried, not derived** (all from R19-9/R19-16):
  - one loop; the supplied vacuum; the ultralocal seagull; SF for the μ rows;
  - class 𝒢 (P-R19-5a);
  - linearized W1 only (W2/W15 not addressed);
  - m = 0.01;
  - the TT rows see only the spatial pair block at graviton momentum q (`R19-9 report:69`, vR19-5 item 3).
- **Prior art:**
  - **R19-9 and R19-16 with their verdicts:** the construction, R1, and the cut (`vR19-16` item 3).
  - **R8-2 Construction A:** the dust kernel, which here is the scattering block.
  - **R9-9's placement:** T^{jl} at (e_j + e_l)/2 (`C5_R9-9_report.md:100`).
  - **R17-12's VW:** its "co-location with R9-9's h" (`C5_R17-12_report.md:27,193`) was established at axial q, where only the z-placement enters (`:61`).
  - **R18-13's VWa-geo:** site placement of off-diagonal products (`vwface.py:4-10`).
  - **R16-5 and R18-12 (face and corner states):** not needed. No row or face state is changed (§5).
- **Comparator (recalled):** a lattice operator located at positions p + ℤ³ has a Fourier symbol, taken with true positions, that changes by e^{−2πi p_l} under q_l → q_l + 2π. A symbol with a jump on the torus has Fourier coefficients ~1/n, i.e. a kernel that decays like 1/r.

## 2. Diagnosis

**Lemma P (placement rule; proved).**
- lib199's kernels are tilde kernels: true-position Fourier transforms for both the fields (the rotated frame, `R19-9 report:57`) and each stress component at its own placement p_{μν} = (e_μ + e_ν)/2, with e₀ = 0 (`lib199.py:7-10`).
- lib199 evaluates them at the graviton representative q = wrap(k₁ − k₂), in the range (−π, π] (`lib199.py:134,174,199`).
- **Statement.** For any local stress component, with k₁ and k₂ fixed in the zone interior, the tilde kernel must change by (−1)^{2p_l} when q_l crosses ±π. At a BZ face of a leg, where q is continuous, it must pick up only the rotated-frame twist T_l.
- **Proof.** The periodic-gauge kernel G = e^{−iq·p}Φ(k₁)M̃Φ(k₂)⁻¹, with Φ = diag(e^{ik·r_a}) at the true field positions r_a, is the ordinary lattice symbol. It is representative-independent: T_l cancels against Φ. For a local operator it is continuous on the torus. At a q_l cut, wrap(q) jumps by 2π, and e^{−iq·p} jumps by e^{∓2πi p_l} = (−1)^{2p_l}. ∎
- **Consequences:**
  - M^{0x}, M^{xy} and M^{xz} must flip at a q_x cut;
  - M⁰⁰, M^{0y}, M^{0z}, M^{xx}, M^{yy}, M^{yz} and M^{zz} must be continuous there.

**Is the divided-difference cut intrinsic? Yes, and it is required (proved).**
- Δ_x = (σ_x(k₁)² − σ_x(k₂)²)/d(q_x). The numerator is continuous in the interior, and d = dsym(wrap q) runs from +2 to −2 across the cut.
- So Δ_x must change sign, as `vR19-16` item 3 measured.
- Δ_x enters only g_x, i.e. M^{0x}, M^{xy} and M^{xz} of the scattering block (`lib199.py:135-142`). Those are exactly the components Lemma P says must flip.
- **Checked.** The scattering block's placement-corrected jump at the referee's point is 4.1e-7 at ε = 1e-6 and 4.1e-9 at ε = 1e-8 (`r1926_diag.out:3,14`). M^{0x} is an exact sign flip: ⟨M_b, M_a⟩/⟨M_b, M_b⟩ = −0.9999999963 (`:13`).
- So R1 is correct, and so is the sign behaviour of a periodic σ² divided by an antiperiodic-tilde d.

**Where the O(1) jump comes from (checked).** Breaking the referee's point down by channel and (μ, ν) (`r1926_diag.out:7-16`):

| channel | raw jump (referee's metric) | placement-corrected jump, ε = 1e-8 |
|---|---|---|
| scattering (dust, R1, I) | 0.463 | 4.1e-9 (∝ ε) |
| pair (VW + P1 time components) | 1.015 | **0.749** (M^{xz}); M⁰ʸ 0.279, M⁰ᶻ 0.332, M^{xy} 0.595 |
| VW spatial kernel alone, read as a site operator (p = 0) | — | 8.5e-9 |
| VW spatial kernel alone, read as a plaquette operator (p = (e_i + e_j)/2) | — | **1.39** |

- So VW^{ij} with i ≠ j is a site operator (integer offsets along i and j). That is what VWa-geo states (`vwface.py:9`).
- lib199 inserts it where R9-9's graviton needs a plaquette-centred operator. Equivalently, it applies the exact half-shift e^{−i(q_i+q_j)/2}, whose symbol is discontinuous at q_i, q_j = ±π.
- This is a genuine non-locality of the R19-9/R19-16 object, not a bookkeeping artefact. The convention-free Fourier test gives R19-16's kernel a 1/n tail on every line tested (§4, C6).
- **Answers to the item's questions:**
  - **(i) Intrinsic?** The Δ sign change is intrinsic and harmless. The O(1) jump is not intrinsic to the photon.
  - **(ii) Removable?** Yes, by re-placing VW. A twisted I cannot remove it, since I touches only the scattering block, which already passes. R8-2's dust variant is irrelevant for the same reason.
  - **(iii) Physical defect or coordinate artefact?** Neither of the two named options:
    - it was a real 1/r non-locality of the delivered kernel;
    - it lives only at |q_i| ≈ π, so no row (q → 0) sees it;
    - it is removed at zero row cost.

**Correction to R17-12 (checked; reading).**
- R17-12 says VW is co-located with R9-9's h, with T^{jl} centred at (e_j + e_l)/2 (`C5_R17-12_report.md:27,193`).
- That is true only along z at axial q, the only placement R17-12 tested (`:61`).
- Off axis, VW's T_xy sits at integer x and y. No refereed row changes, because the mismatch is a phase at O(q) common to each component and then the O(q⁴) re-placement below. But the claim as worded is too broad.

## 3. The repair (`S/lib1926.py`; proved)

**Definition.**
- Re-placed spatial kernel: M̃^{ij} = F(q_i)F(q_j)·VW^{ij} for i ≠ j, and M̃^{ii} = VW^{ii}, with q = wrap(k₁ − k₂).
- F(q) = (9cos(q/2) − cos(3q/2))/8.
- It is used wherever lib199 uses VW:
  - the pair blocks of piece B and their P1 time components;
  - piece A's spatial kernel and its Neumann time components.
- Implemented by replacing `lib199.spatial_VW`. `glued` looks it up at call time.

**Properties (each proved).**
- **(a) Locality.**
  - F is antiperiodic, so e^{−iq/2}F(q) = (9/16)(1 + e^{−iq}) − (1/16)(e^{iq} + e^{−2iq}). That is a finite stencil, periodic and C^∞.
  - Hence F(q_i)F(q_j)·VW^{ij} is a local operator at (e_i + e_j)/2. The diagonal T^{ii} sits at e_i, an integer translate of the site operator, which is local as it stands.
  - Lemma P then holds for the pair block. d_x flips and M̃^{xj} flips, so d_x M̃^{xj}/λ is continuous where it should be.
- **(b) W1.**
  - The time components are still built from the spatial ones by the same exact formulas (P1 division, Neumann series, dust).
  - W1 is linear and pointwise, and each piece is exact on its support (R8-2 Lemma G). So W1 holds identically.
- **(c) Forward values and (H-E).** F(0) = 1, so Lemma F is unchanged.
- **(d) Cubic covariance.** F is even, and the factor is symmetric in (i, j). Under signed permutations F(q_i)F(q_j) maps to the factor of the image component.
- **(e) Rows.**
  - The TT rows are Ξ_e = ∂_{q²}Π_e(0, q) + ∂_{ω²}Π_e(ω, 0), built from the spatial pair block at graviton momentum q.
  - The re-placement multiplies each off-diagonal amplitude by F(q_i)F(q_j) = 1 − (3/128)(q_i⁴ + q_j⁴) + O(q⁶). So Π_e changes by O(q⁴)·(finite), and both derivatives at q = 0 are unchanged.
  - At axial q (T₂g, E_g, μ rows) and for the xz row on q ∥ y, F(0)² = 1 exactly, so these evaluator outputs are identical.
  - μ_E^γ = 2·mu_E(law samples) does not involve the vertex at all (`orig/arch18_9/lib9.py:24-25`). μ_T₂ is Dirac-only.
  - Only the evaluator's finite-q face values move (§5).
- **Not unique.** Any antiperiodic C^∞ F with F(0) = 1 and F″(0) = 0 works. The rows do not depend on the choice.

## 4. Checks (re-placed kernel unless marked; r = 0.1 and 0.05)

| # | check | result | file |
|---|---|---|---|
| C0 | referee's script, R19-16 kernel (reproduction) | Δ limits ±3.678165139; raw jump 1.310001203; projected M⁰² 0.2791999734 (identical to `vR19-16`) | `ref_cut_check_REPRO.out:5-8` |
| C0′ | referee's script, unmodified, re-placed kernel | projected M⁰² jump **3.27e-5 / 3.27e-7 / 3.27e-9 / 3.27e-11** at ε = 1e-4 … 1e-10 (∝ ε). The raw "kernel jump" stays 1.310: it is the required flip of M^{0x} (Lemma P), and the Δ limits are unchanged (R1 untouched). W1 sides ≤ 7.6e-16; R2 agreement 1.3e-15 | `r1926_refcheck_replaced.out:5-9` |
| C1 | W1, physical block: lib199 `w1_resid` plus an independent SVD transverse frame. Referee seam; exact-zero legs (left, right, both); 600 pairs each of hard×hard, soft×hard, hard×soft, annulus×annulus, annulus×hard | ≤ 1.95e-15 abs; all finite. `w1_resid` itself is NaN at an exact zero leg, because it calls `projs` on that leg, so the independent frame is used there: ≤ 1.9e-16 | `r1926_checks_r0.1.out:2-10`, `_r0.05.out` |
| C2 | cut crossings: 300 per axis l = x, y, z (1/3 hard, 1/3 soft k₁, 1/3 soft k₂), placement-corrected jump | r = 0.1: ≤ 9.5e-5 at ε = 1e-7 and ≤ 9.1e-7 at ε = 1e-9 (∝ ε; physical block ≤ 8.3e-7); W1 at the cut points ≤ 1.5e-15. **R19-16 control: 1.39–1.44 (physical block), independent of ε.** r = 0.05: ≤ 1.4e-6 at 1e-9 | `r1926_checks_r0.1.out:11-22`, `_r0.05.out` |
| C3 | BZ-face continuity (twist T_l, either leg, 1e-9 from the face, 240 crossings) | ≤ 2.8e-9 (∝ gap) | `:23` |
| C4 | line scans across q_l = −π, 801 points, step 1e-4, placement-corrected | max second difference 3.5e-9 to 7.9e-9 (\|M″\| ≈ 0.5); max first difference 5.5e-5 to 8.3e-5; no step | `:24-26` |
| C5 | cubic covariance C₄z, C₃(111), C₂(110), 300 pairs each (mine and R19-9's `r199_cov.py`) | ≤ 8.9e-16 | `:27-29`; `r1926_cov.out` |
| C6 | **convention-free locality:** Fourier coefficients of the periodic-gauge symbol G along full lines of the q-torus. 1024–8192 points; three hard lines along x, one along y, one along z, one line through k₁ = 0 (pieces C/A) | R19-16: max\|c_n\| = 2.0e-3 (n 64–128), 5.1e-4 (256–512), 2.6e-4 (512–1024), 1.4e-4 (1024–2048), i.e. **~1/n**. Re-placed, same line: 2.3e-5, 1.4e-7, 6.9e-10, **1.3e-12** (super-polynomial). y and z lines: **1.7e-15–2.2e-15** at n ≥ 2048. Through k = 0: 1.4e-9 at n ≥ 2048, still steepening (glue width r/16) | `r1926_fourier.out`, `r1926_fourier_fine.out`, `r1926_fourier_soft.out` |
| C7 | R19-9's `r199_exact.py` (10 families), unmodified, under the patch | ALL FAMILIES max abs 1.32e-15; symmetry 2.2e-16; Hermiticity 4.4e-16; (H-E) 3.9e-16; Lemma F 3.3e-16; face jump ∝ gap. Its item [3] "pair block = VW" now compares with the re-placed VW, by construction | `r1926_exact_r0.1.out:7-27`, `_r0.05.out` |
| C8 | R19-9's `r199_dense.py`, 2×10⁴ pairs | ≤ 1.69e-15 / 1.95e-15 abs (r = 0.1 / 0.05) | `r1926_dense_r0.1.out`, `_r0.05.out` |

## 5. Root re-solve (checked)

**What moves.**
- Only the off-axis photon face evaluator (`vwface.xi_geo`, q ∥ (1,1,0)) sees F at finite q. The F-wrapped vertex is checked against the original by setting F ≡ 1: the outputs are identical (`r1926_rows_lin_N64.out` against `r1926_rows_noF_N64.out`).
- Re-placed minus original, per vector:

| N | Δface1 | Δface2 | N⁴Δ/ln N |
|---|---|---|---|
| 64 | 2.05e-6 | 2.18e-6 | 8.3, 8.8 |
| 96 | 4.82e-7 | 4.99e-7 | 9.0, 9.3 |
| 128 | 1.68e-7 | 1.72e-7 | 9.3, 9.5 |
| 224 | 2.06e-8 | 2.09e-8 | 9.6, 9.7 |

  Source: `r1926_rows_N224_delta.out`.
- **Why it vanishes (proved).** Two-shift Richardson removes the q⁴ term exactly. What is left is the evaluator's q⁴ln q residual from the massless loop. It vanishes as N → ∞, as §3(e) requires.
- The w-derivatives change by ≤ 6.7e-8.

**Direct re-solve.** I used R19-9's `r199_direct_solve.py`, executed from its own source (`S/r1926_direct.py`). The only changes are:
- the analytic law (R0, as in R19-16);
- the re-placed off-diagonal vertex;
- the start point: R19-16's final (w_d, w_o).

The start totals are recomputed directly.

| r | direct face totals at start | step (Δw_d, Δw_o) | direct N = 224 face totals after one step |
|---|---|---|---|
| 0.1 | (9.04e-8, 9.32e-8) | (−2.61e-8, −1.34e-8) | **(2.09e-12, −1.21e-12)** |
| 0.05 | (9.04e-8, 9.32e-8) | (−2.61e-8, −1.34e-8) | **(2.35e-13, 3.16e-12)** |

Sources: `r1926_direct_r0.1.out:2-3`, `r1926_direct_r0.05.out:2-3`.

**The other rows.**
- The axial rows T₂g and E_g, and μ_E and μ_T₂, are unchanged exactly (§3(e)). R19-16's values stand: T₂g, E_g ≤ 1.4e-12; μ_T₂ ≤ 1.3e-16; μ_E ≤ 5.6e-11, which is the scalar/Dirac evaluator floor that `vR19-16` item 5 already accepted.
- b_s, b_f, r_D and a are unchanged. Lemma O(iii) says the axial rows do not depend on w, and the corner's w-dependence enters at about 1e-13.
- The knob shift against R19-16 is ≤ 2.6e-8. That is below R19-16's own shifts and about 2000 times below the root's quadrature ambiguity of 4.7e-5.

## 6. Reading against the FIXED readings (`TESTS:8415-8417`)

PHOTON-EXACT requires "a W1-exact (≤ 1e-12), smooth, quasi-local photon completion with no O(1) jump anywhere on the torus, including the q = ±π cut. The root is re-solved. Checked."

| clause | status |
|---|---|
| **W1-exact** | ≤ 2.0e-15 in every family (C1, C2, C7, C8). Met (checked). |
| **Smooth, quasi-local** | Strictly local re-placement (proved). Super-polynomial Fourier tails on the q-torus with no sign rule, against 1/n for R19-16 (C6). Line scans smooth (C4); faces continuous (C3). Met (checked; proved for the construction). |
| **No O(1) jump, including the cut** | Placement-corrected jumps ∝ ε on all three axes and on soft legs (C2). The referee's projected M⁰² jump is 3.3e-11 at ε = 1e-10 (C0′). Met (checked). |
| **Root re-solved** | Rows unchanged exactly (proved). Direct N = 224 face totals ≤ 3.2e-12 after a 2.6e-8 step; other rows as R19-16 (§5). Met (checked), at the evaluator floor `vR19-16` item 5 accepted. |

**Worker reading: PHOTON-EXACT** (unrefereed).

**What a referee should test first.**
- The sign rule of Lemma P. The referee's raw "kernel jump" metric still reads 1.310 on the repaired kernel, because M^{0x}, M^{xy} and M^{xz} must flip at a q_x cut.
- C6 is the test that needs no sign rule. I suggest the referee re-derive Lemma P independently, or rerun C6 with their own Φ and placement table.

**CUT-INTRINSIC is not supported.** The Δ sign change is intrinsic but is the link placement itself. The O(1) jump came from VW's placement and is removed.

**Scope (unchanged from R19-16):**
- one loop; the supplied vacuum; ultralocal seagull; SF;
- VWa-geo, plus the re-placement;
- class 𝒢;
- linearized W1 only (W2/W15 not addressed);
- m = 0.01;
- rows at the inherited finite resolution.

## 7. Prices

**P-R19-26a (law data, count once; zero numbers).**
- **What it is.** The off-diagonal photon stress is VW re-placed to R9-9's plaquette centre by a local average F with F(0) = 1 and F″(0) = 0.
- **What it costs.** A choice from a family. No row depends on which member is chosen.
- **Why it is needed.** Locality, together with R9-9's placement, forces some such re-placement. The bare VW kernel at that placement is a half-shift, which is non-local (§2).
- **Not an axiom change.** It joins R19-9's law data (r, the glue profile, the scattering kernel, I).

## 8. Flags (suggested; not done here)

1. **The same placement test for the scalar and Dirac completions.** R19-5's U and UD exact completions (`vR19-5` "strongest statement") should get the same placement test (Lemma P / C6), if their off-diagonal stresses are site-placed and used as R9-9 tilde kernels. Suggested only; I did not check them.
2. **R17-12's co-location wording** (`C5_R17-12_report.md:27,193`) should be limited to the z-placement at axial q (§2). No row is affected.

## 9. Files (all in `S/`)

- **Libraries:**
  - `lib1926.py`: the re-placement, the placement and twist tables, and the vertex wrapper for the pair-convention evaluator;
  - `lib1916.py` and `orig/`: unmodified copies.
- **Diagnosis:** `r1926_diag.py` → `r1926_diag.out`. Reproduction: `ref_cut_check.py` → `ref_cut_check_REPRO.out`; `r1926_refcheck_replaced.py` → `.out`.
- **Checks:**
  - `r1926_checks.py` → `r1926_checks_r0.1.out`, `_r0.05.out`;
  - `r1926_fourier.py`, `r1926_fourier_fine.py`, `r1926_fourier_soft.py` → `.out`;
  - `r1926_run.py` (runs R19-9's scripts under the patch) → `r1926_exact_r*.out`, `r1926_dense_r*.out`, `r1926_cov.out`.
- **Rows:**
  - `r1926_rows.py` → `r1926_rows_{noF,F,lin}_N*.out`, `rows_*.npy`, `r1926_rows_N224_delta.out`;
  - `r1926_direct.py` → `r1926_direct_r0.1.out`, `_r0.05.out`;
  - inputs copied from R19-16: `resolve_sols_analytic.npy`, `photface_analytic_N224.npy`.
