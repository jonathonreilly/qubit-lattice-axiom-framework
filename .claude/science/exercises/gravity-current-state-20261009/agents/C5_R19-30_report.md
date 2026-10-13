# C5 R19-30 report: U and UD are not at R9-9's placement either; R19-26's F(q_i)F(q_j) fixes only the per-leg U; a parity-resolved re-placement fixes all of them with the rows unchanged and W1 exact

**Author and status.** Claude Opus 5.5 probe (same model family as the supervisor and every C5 worker). Unrefereed. Worked 2026-10-13, 07:09Z to 07:40Z. No repository file was edited and nothing was downloaded. Every run used `OMP_NUM_THREADS=2`; the longest took 282 s (machine load about 7).

**Paths.**
- `P/` = `.claude/science/exercises/gravity-current-state-20261009/`
- `S/` = `scratchpad/C5/R19-30/`. My scripts and `.out` files are at the top level of `S/`.
- Unmodified copies of earlier code: `S/r195copy/` (R19-5's `r195_dirac_exact.py`, plus the archived `dirac.py`, `sublum.py` and `r99_profiles.py`) and `S/r135copy/` (R13-5's `r135_w1_pair.py` and its profile module).
- `vR19-5` = `P/agents/C5_R19-5_referee_verdict.md`
- `vR19-26` = the R19-26 referee's verdict at `scratchpad/C5/ref_R19-26/REFEREE_VERDICT.md`. It appeared at 07:21Z, after the brief said "running". It reads CONFIRMED WITH CORRECTIONS and confirms Lemma P (item 1). I re-derived Lemma P myself before I saw it (§2).

**Read.**
- `docs/MINIMAL_AXIOMS_2026-06-29.md`, in full.
- In `P/TESTS.md`: my item, `:8595-8612`; R19-29 and R19-31 for context, `:8573-8632`.
- In `P/agents/`: `C5_R19-26_report.md` (all); `C5_R19-5_report.md` (all); `C5_R19-5_referee.md` and its verdict; `C5_R9-9_report.md:1-130`. For conventions: `C5_R18-5_report.md:80-140`, `C5_R18-13_report.md` (grep), and `C5_R17-4_report.md` (grep).
- Code:
  - R19-26's `lib1926.py`, `lib1916.py` and `orig/lib199.py`, in full;
  - R19-5's `r195_dirac_exact.py` and `r195_dirac_exact2.py`;
  - R13-5's `r135_w1_pair.py`;
  - R9-9's `r99_graviton.py`, Construction A part;
  - R17-4's `offaxis.py`;
  - R18-13's `dface.py`;
  - the D1 and G_w law code (`dirac.py`, `sublum.py`, `r161_laws.py`, `zz.py`).

**Labels.** proved (a complete argument under the stated hypotheses; unrefereed) / checked (numerics here) / suggested / reading / comparator.

---

## 0. In plain words

1. **Neither U nor UD sits where R9-9's graviton needs it (checked; proved).** The graviton reads T^{ii} at sites and T^{ij} (i ≠ j) at plaquette centres. Each delivered kernel misses that in a different way:
   - **R13-5's per-leg U** (the code R19-5 cites for the scalar completion) has exactly VW's defect. Its off-diagonal stress is a product of site-centred derivatives, but it is used as a plaquette-centred kernel. Across q_x = ±π, F^{xy} jumps by 2.3 and F^{00} by 1.1 (`r1930_origcode.out:2-3`). Its Fourier tail goes like 1/n.
   - **E1 midpoint U** (R17-4's off-axis extension, the vertex in the root's scalar face rows) and **UD** (R18-5's midpoint Dirac vertex) are bond-midpoint operators with **mixed offset parity**:
     - each bond sits at its own midpoint, so even bonds sit on sites and odd bonds on half-integers;
     - only one parity class per direction can be at R9-9's placement;
     - for UD the correctly placed class is a small minority: 17.5% of T^{xy} and 12.4% of T^{xx} by RMS (`r1930_parity.out:1-2`). The Dirac stress is first-order in derivatives, so it lives mainly on links.
2. **R19-5's Dirac code adds a separate placement error (checked).**
   - Its scattering block carries the placement phase e^{-iq·p} (`r195_dirac_exact.py:81,95-96`). Its pair block puts UD(k̄) in the same slot with no phase (`:105-108`; `r195_dirac_exact2.py:31-34`). So in each T^{ij} the pair part is displaced by p_ij from the scattering part.
   - Consequences:
     - it is not cubic covariant: the O_h relation fails by −9.9e-3;
     - its face1 row differs from the refereed UD face1 by **+1.11e-2 per field at m = 0.3**, against a row value of 6.2e-4. At m = 0.01 the difference is +1.30e-2 (`r1930_rows_m0.3_N48.out`, `r1930_rows_m0.01_N48.out`);
     - T₂g, E_g, face2, body and the μ rows are unaffected.
   - So R19-5's "Dirac rows identical (proved)" holds only after the phase is restored.
3. **R19-26's F(q_i)F(q_j) fixes the per-leg U, and only that kernel (checked).**
   - Per-leg U: the tails become super-polynomial (5.7e-17).
   - E1 U and UD: F vanishes at the cut, which removes the value jump but leaves a kink (1/n² tails). The diagonal components and UD's third-direction classes keep O(1) jumps (`r1930_cut_m0.01.out:13-15,25-27`).
4. **A parity-resolved re-placement does fix all of them (proved; checked).**
   - The re-placement: split the midpoint kernel into its offset-parity classes. Multiply each class by F(q_l) in every direction l where its parity does not match p_ij.
   - This is R19-26's F, applied class by class. In position space it is the same symmetric 4-point half-step average (`r1930_lemmaP.out`, line "fixed").
   - Every jump becomes ∝ ε. The Fourier tails fall to 1e-16 to 1e-17 on all six UD components and on both scalar components (`r1930_cut_m0.01.out:16-18,28-34`).
   - The change to the row kernel is O(q⁴), checked to be constant ×q⁴ (`r1930_rows_*.out` part 1). So every row is unchanged (proved). The direct Dirac rows move by at most 4.8e-9, which is Richardson residue.
   - W1 stays exact, at ≤ 2.7e-15 over the whole torus including the cut (`r1930_w1.out`).
5. **Worker reading: UD-LOCAL** (unrefereed). The expectation "UD-LOCAL after the same F re-placement" is right for the per-leg U only. For E1 U and UD it takes the class-resolved version of F, and R19-5's Dirac code first needs its placement phase restored.

---

## 1. Setting, conventions, prior art (each counted once)

- **Setting** (`TESTS:8600`).
  - R19-5's U and UD completions:
    - U = R8-2 Construction A plus R13-5's P1; the code is `r135_w1_pair.py`;
    - UD = Theorem E; the code is `r195_dirac_exact*.py`, `vR19-5` items 2 and 4.
  - R19-26's Lemma P and Fourier test, and R9-9's placement `C5_R9-9_report.md:100`: T^{0j} on j-links, T^{jl} at (e_j + e_l)/2.
- **Laws.**
  - The root edges: scalar G_w(2.5261508, π − b) (`C5_R18-13_report.md:85`) and Dirac D1(0.909103708, 0.555604226) (`vR18-9:11`), at m = 0.01; m = 0.3 is used for resolved row checks.
  - I evaluate both laws analytically (`lib1930.py`: Gauss–Legendre cumulative tables), so Fourier tails are not limited by tabulation.
  - Against the archived tables (`r1930_lawcheck.out`):
    - S agrees to 7e-15 and W to 2e-11;
    - the archived W′ carries 4.5e-9 rounding noise near the slab edges, from √(st(1 − st)) cancellation; I compute it as √(e₁e₂)/(e₁ + e₂) instead;
    - σ agrees to 1e-10.
- **Conventions (as in lib199, R13-5 and R19-5; rechecked in §2).**
  - The **site-label kernel** G obeys W1 with the periodic D_j = d(q_j)e^{iq_j/2}. A stress is local iff G is C^∞ on T³×T³.
  - The **tilde kernel** is M̃ = e^{iq·p}G, the true-position kernel. The TT rows use M̃ with the real tilde polarization: Σh*T = Σh̃*T̃ (`C5_R9-9_report.md:101`, `lib199.py:7-10`).
  - The rows actually used M̃ = (vertex) with no phase:
    - Dirac: `dface.py:51-57` and R18-5 `xiud`, with real e and UD at the midpoint (`C5_R18-5_report.md:111`);
    - scalar: `offaxis.py:2-3` (E1).
- **Carried, not derived:** one loop; the supplied vacuum; ultralocal seagull; SF; class 𝒢 (P-R19-5a); linearized W1 only.
- **Prior art:**
  - R19-16: the cut, counted once through R19-26;
  - R19-26 and its verdict: Lemma P, F, and the flag `C5_R19-26_report.md:243` that is this item;
  - R19-5 and its verdict: Theorem E, and "any smooth pair kernel";
  - R13-5's P1; R8-2 Construction A (in R9-9);
  - R18-5's midpoint prescription P-R18-5c (`C5_R18-5_report.md:109-112,309`);
  - R17-4's E1 versus E2 extensions. R17-4 itself says E1 and E2 differ off the axis (`C5_R17-4_report.md:27`).

## 2. (a) Placement audit

**Lemma P, rechecked (proved; checked).**
- An operator with pieces at true positions y has T_true(q) = Σ e^{-iq·y}O_y.
- If every y lies in p + ℤ³, then T_true(q + 2πe_l) = (−1)^{2p_l}T_true(q), and G = e^{-iq·p}T_true is periodic. It is smooth iff the operator is local.
- So M̃ = T_true must flip by (−1)^{2p_l} across q_l = ±π, and G must not jump.
- **Checked on explicit position-space operators** (`r1930_lemmaP.py` → `.out`):
  - a nearest bond declared at ½, and a next-nearest bond declared at 0: representative-independent to 2e-15, with Fourier tails at 1e-17;
  - a next-nearest bond declared at ½, or a mixed operator at either placement: jump 2.8 to 4.0, tails ~1/n;
  - the mixed operator after the 4-point move (offsets ±½, ±3/2; weights 9/16 and −1/16, whose symbol is exactly F): local to 2e-15.
- This agrees with `vR19-26` item 1.

**Lemma C (offset classes; proved).**
- A midpoint kernel f(k̄) = Σ_n f_n e^{-in·k̄} is the true-position kernel of bonds ψ†_{y+n}ψ_y, each at its own midpoint y + n/2.
- Write f = Σ_{σ∈{0,1}³} f_σ, with f_σ(k̄ + πe_l) = (−1)^{σ_l}f_σ(k̄). Class σ then sits at σ/2 + ℤ³.
- By Lemma P, class σ is local at p iff σ ≡ 2p (mod 2). Call that class τ_ij: τ_ii = 000, τ_xy = 110.
- A per-leg product g(k₁)h(k₂), with g and h periodic, is a site operator, i.e. class 000.

**The audit (checked: `r1930_parity.out`, `r1930_origcode.out`, `r1930_cut_m0.01.out`).**

| kernel (where it is used) | what it is | at R9-9's placement? |
|---|---|---|
| R13-5 per-leg U (`r135_w1_pair.py:12,51-57`), R19-5's cited scalar completion | site operator; e^{-iq·p} applied to a per-leg product | T^{ii}: yes. T^{ij}: **no** (VW's defect). Jumps of 2.3 in F^{xy} and F^{xz}; F^{00}, F^{0x} and F^{0y} inherit 0.9–1.3 |
| E1 midpoint U, f_i(K)f_j(K) (`offaxis.py:2-3`), the root's off-axis scalar vertex | mixed classes. f = σσ′ on G_w has odd-class part 1.57 and even-class part 1.05 (an NN sin k would be purely odd) | correct-class share 0.84 (xy) and 0.81 (xx). **No**: jumps of 1.6 (xy) and 3.0 (xx) |
| UD(k̄), rows convention (tilde = UD) | mixed classes. In D1, S, S′, W′ and W − W_π/2 are each pure odd class (to 1e-15), but p_j = S_jS′_j + MW′_j mixes classes | correct-class share **0.175 (xy), 0.124 (xx)**. The dominant classes are 010/100 for xy and 100 for xx: link-centred, as a first-derivative stress is. **No** on all six components: jumps of 1.0 (xy), 2.0 (xx), 0.08 in third directions |
| UD as coded in R19-5 (UD(k̄) as G, no phase) | the rows' operator displaced by p_ij, still mixed | **No**. Jumps of 1.1 (xy) and 1.8–1.9 (xx) in R19-5's own unmodified `far()` (`r1930_origcode.out:5-6`); its scattering-only kernel jumps ∝ ε (1.5e-8 at ε = 1e-8, `:7-8`), so the scattering blocks are local |

- **Why the earlier checks missed this.**
  - R13-5's locality test (6) runs in d = 1 (`r135_w1_pair.py:112-122`). There only F^{11}, at an integer placement, exists.
  - R19-5's whole-torus tests check W1 point by point. They never compare the two sides of a cut (`r195_dirac_exact2.py:79-93`).
  - W1 holds on each side, so it cannot see the jump.

## 3. (b) jumps and (c) Fourier decay, before and after (checked; `r1930_cut_m0.01.out`)

The jump is taken across q_l = ±π at the same torus point, at ε = 1e-6 / 1e-8. The Fourier coefficients are max|c_n| of G along a full k₁ line (N = 4096), in the band n ∈ [1024, 2048).

| kernel | jump before (x-cut) | tail before | after F(q_i)F(q_j) | after the parity-resolved re-placement (PR) |
|---|---|---|---|---|
| per-leg U, xy | 2.3 / 2.5 | 2.4e-4 (~1/n) | jump ∝ ε; tail **5.7e-17** | (equals FF for a class-000 kernel) |
| per-leg U, xx | ∝ ε | 8.6e-17 | unchanged | — |
| E1 U, xy | 1.6 / 1.5 | 2.1e-4 | jump ∝ ε, but tail 3.0e-4 → 2.5e-7 over n = 48 → 1500, **~1/n² (kink)** | jump ∝ ε; tail **1.1e-16** |
| E1 U, xx | 3.0 / 3.0 | 2.6e-4 | **3.3 / 2.9 (FF does not touch the diagonal)** | ∝ ε; tail 1.1e-16 |
| UD (rows conv.), xy | 1.0 / 1.0; z-cut 0.08 | 6.1e-5 | x, y ∝ ε (kink, tail ~1/n²: 6.8e-9); **z-cut 0.074 remains**, z-line tail 4.9e-7 | ∝ ε on all three axes; tails ≤ 2.1e-17 |
| UD (rows conv.), xx | 2.0 / 2.0 | 1.7e-4 | **2.1 / 2.1** | ∝ ε; tail 3.5e-17 |
| UD, xz, yz, yy, zz | (O(1), as above) | — | — | ∝ ε; tails ≤ 4.7e-17 |
| UD as coded in R19-5, xy / xx | 1.2 / 1.9 | 1.2e-5 / 1.7e-4 | — | (fix the phase first, then PR) |

- **Why FF leaves a kink (proved).** F(±π) = 0 with F′(π) = −3/4. A wrong-sign class times F is continuous at the cut but has a slope jump, giving c_n ~ 1/n². Classes whose parity already matches in direction l are made to flip wrongly by F(q_l).
- **No single multiplier of q that is nonzero at the cut works on a mixed kernel (proved).** Two classes in direction l would need A(q − 2πe_l) = +A(q) and −A(q) at once near the cut, so A would have to vanish identically there.

## 4. The repair: parity-resolved re-placement (`lib1930.tilde_component(..., 'PR')`; proved)

**Definition.** M̃′^{ij}(k₁, k₂) = Σ_σ A_σ^{ij}(q) f_σ^{ij}(k̄), with A_σ^{ij}(q) = Π_{l: σ_l ≠ τ_ij,l} F(q_l). Here F(q) = (9cos(q/2) − cos(3q/2))/8 is R19-26's F, and f^{ij} is the given midpoint kernel: UD^{ij}, or f_if_j for E1. The Dirac projectors and the scalar normalization 1/√(ε₁ε₂) are per-leg periodic and are not affected.

**Properties.**
- **(i) Local.**
  - Across a q_l cut, f_σ picks up (−1)^{σ_l} and A_σ picks up (−1)^{[σ_l ≠ τ_l]}. The product is (−1)^{τ_l} = (−1)^{2p_l}, so G′ = e^{-iq·p}M̃′ satisfies the identity of smooth functions that makes it C^∞ on the torus.
  - In position space each mismatched class is averaged with the symmetric 4-point half-step stencil, whose true symbol is F (`r1930_lemmaP.out`, "fixed").
  - Finite range per class: 4 points per affected direction.
- **(ii) Row-neutral.** Σ_σ f_σ = f exactly and A_σ − 1 = O(q⁴), with F = 1 − 3q⁴/128 + O(q⁶). So M̃′ − M̃ = O(q⁴), uniformly in k̄. The TT rows Ξ = ∂_{q²}Π(0, q) + ∂_{ω²}Π(ω, 0) at q → 0 and the μ rows at q = 0 are therefore unchanged.
- **(iii) W1.** The time components are rebuilt from the re-placed spatial kernel by the same exact formulas: R13-5's P1 for the scalar, and R19-5's P1 for the Dirac pair blocks. D, ω and E₁ + E₂ ≥ 2m are periodic and smooth, so the time components inherit locality.
- **(iv) Hermiticity.** F is real and even, and k̄ is exchange-symmetric.
- **(v) Cubic covariance.** F is even, and signed permutations permute the classes. Checked for scalar E1: ≤ 1.1e-14 for C₄z, a mirror, C₃(111) and C₂(110), including at the cut (`r1930_cov.out`).
- **(vi) Not unique.** Any antiperiodic C^∞ F with F(0) = 1 and F″(0) = 0 works. So does a plateau χ(q), equal to 1 near 0 and to 0 near the cut, applied to the whole component; but that switches off the coupling at large transfers. No row depends on the choice.

## 5. (d) W1 after the fix (checked; `r1930_w1.out`)

**Dirac.** R19-5's own construction was run on the analytic law: `near` unmodified, and `far`/`glued` copied verbatim. Its pair block was switched off and the re-placed pair block added, with R19-5's P1 time components.

| test set (150 points each) | W1, all ν, all four blocks | μν symmetry |
|---|---|---|
| generic | 2.4e-15 | 1.4e-16 |
| near region | 2.2e-15 | 0 |
| q_x = π − 1e-9 | 1.3e-15 | 6e-17 |
| q_x = −π + 1e-9 | 1.2e-15 | 4e-17 |

- The completed time components jump by 2.1e-8 at ε = 1e-8 across the cut, i.e. ∝ ε.
- Fourier tails of M^{0x} and M^{00} along a k₁ line: 1.4e-17 after the fix, against 2.2e-4 with UD unrepaired at R9-9's placement.

**Scalar.** R13-5's P1 on (a) per-leg U with FF and (b) E1 U with PR, over 4000 whole-torus pairs:
- creation-channel W1 ≤ 9.9e-16 and annihilation-channel W1 ≤ 2.7e-15;
- F^{0ν} tails 3.2e-17 and 2.9e-17.

All of these are below the 1e-12 required.

## 6. (e) Are the rows unchanged?

- **Re-placed kernels (proved; checked).**
  - |M̃_PR − M̃|/|q|⁴ is constant from s = 0.2 down to 0.025 along the axial, face and body directions: Dirac 2.5e-2 / 6.4e-3 / 2.9e-3; scalar E1 7.7e-2 / 3.1e-2 / 1.4e-2 (`r1930_rows_*.out`, part 1). The change is O(q⁴).
  - Direct Dirac rows, PR minus rows, on a k̄ grid with continuous q and Richardson extrapolation:

    | m | T₂g, E_g | face1, face2, body |
    |---|---|---|
    | 0.3 | ≤ 4.3e-11 | ≤ 4.0e-9 |
    | 0.01 | ≤ 7.6e-11 | ≤ 4.8e-9 |

    These are Richardson O(h⁴) residues, not row changes.
  - **Validation of the grid.** My row values at m = 0.3, N = 48 against `dface.py` run on the same law (`r1930_dface_ref_m0.3.out`) agree to 0.1–1%: T₂g 1.5358e-3 against 1.5343e-3; face1 6.220e-4 against 6.203e-4. They converge with N (N = 32 → 48).
  - The root is not moved: the scalar and Dirac rows are identical, so no re-solve is needed.
- **R19-5's code as written (checked).** Its tilde pair kernel is e^{iq·p_ij}UD(k̄). Within a face1 polarization that puts a relative phase e^{iq_x} on zz against xx/yy/xy.

  | | face1 change per field | O_h relation residual |
  |---|---|---|
  | m = 0.3 (N = 32 / 48) | +1.1102e-2 / +1.1108e-2 | −9.87e-3 |
  | m = 0.01 (N = 32 / 48; light region under-resolved, size only) | +1.295e-2 / +1.296e-2 | −1.15e-2 |

  - T₂g, E_g, face2 and body are identical (≤ 3e-14). In those, every component carries the same q·p.
  - **Robustness.** δΠ(s)/s² for face1 at m = 0.3 is 1.1051e-2, 1.1089e-2, 1.1099e-2 and 1.1101e-2 at s = 0.2, 0.1, 0.05 and 0.025, identical for either sign of the phase (`r1930_face1_lit.out`). So the shift is a genuine q² effect, not a Richardson artefact.
  - With 22.5 fields, the m = 0.01 shift would add about +0.29 to the face1 total.
  - **Correction (reading):** R19-5's "scalar and Dirac rows identical (proved)" (`C5_R19-5_report.md:249`) and `vR19-5` item 4 ("pair block = UD") are true for the phase-restored, re-placed construction. They are not true for `r195_dirac_exact*.py` as coded.

## 7. Reading against the FIXED readings (`TESTS:8608-8611`)

| reading | status |
|---|---|
| **UD-LOCAL** ("both already local at the cut … or made local by a row-neutral re-placement with W1 exact to ≤ 1e-12") | **Met (checked; proved for the construction).** Neither is already local (§2). Both are made local by a row-neutral local re-placement: FF for the per-leg U; the parity-resolved F for E1 U and UD, after restoring the placement phase in R19-5's Dirac code. The evidence: Fourier tails ≤ 1.1e-16; jumps ∝ ε; rows proved unchanged, with the O(q⁴) change and direct Dirac rows checked; W1 ≤ 2.7e-15 on the whole torus including the cut. |
| **UD-DEFECT** | **Not supported.** Every non-local piece is removed by a local, row-neutral re-placement. |
| **OPEN** | — |

**Worker reading: UD-LOCAL** (unrefereed). Against the expectation (`TESTS:8612`, "UD-LOCAL after the same F re-placement"):
- the reading matches;
- the mechanism matches only for R13-5's per-leg U;
- for E1 U and UD, the same F(q_i)F(q_j) leaves a kink and O(1) diagonal and third-direction jumps (§3). The class-resolved F is needed.

**What a referee should test first.**
1. Lemma C, and my claim that the rows use the tilde kernel. That claim decides which of the two Dirac conventions is "the rows'".
2. The R19-5 literal face1 shift, with an independent evaluator.
3. Rerun `r1930_cut.py` with your own class decomposition and placement table.

## 8. Prices and flags

- **P-R19-30a (law data, count once with P-R19-26a; zero numbers).**
  - What it is: the massive-species stresses are re-placed to R9-9's placement class by class in offset parity, using R19-26's F.
  - It extends P-R19-26a from site-placed kernels to mixed midpoint kernels. Row-invisible; a choice from a family (§4 vi).
  - For UD it moves most of the stress by half a step: the correctly placed class is 12–18% RMS. Reading: the natural home of a first-derivative Dirac stress is the links, and R9-9's graviton couples at sites and plaquettes.
  - Not an axiom change.
- **Corrections, with flags for the record.**
  1. **R19-5's Dirac construction** (`r195_dirac_exact.py:104-108`, `r195_dirac_exact2.py:31-34`). The pair block lacks the e^{-iq·p_ij} that its scattering block carries (`:81,95-96`). As coded it is non-local, non-covariant, and its face1 is not the refereed one (§6).
  2. **The premise of R19-5's Theorem E,** "any smooth pair kernel" (`C5_R19-5_report.md:187`, `:202` "including R17-4's E1 off-axis U"). The midpoint kernels E1 U and UD are not smooth on the torus at R9-9's placement. They become smooth after PR.
  3. **R19-5's scalar completion** is R13-5's per-leg kernel. That is R17-4's E2 type, not the root's E1 vertex, and their off-axis rows differ (`C5_R17-4_report.md:27`). The E1 completion needs PR.
  4. **R13-5's locality test (6)** is one-dimensional (`r135_w1_pair.py:112-122`). It cannot see the off-diagonal placement.
  5. **The archived `dirac.py` W′** has ~4.5e-9 rounding noise near the slab edges. That is row-irrelevant; it only sets a floor for Fourier tests.

## 9. Strong-word check

- **"Local"** means super-polynomial Fourier decay of the site-label kernel along full torus lines, together with jumps ∝ ε. It is checked on sampled lines and points, and proved for the construction (§4 i).
- **"Exact W1"** means ≤ 2.7e-15 at sampled points, and algebraic by construction.
- **"Unchanged rows"** is proved, via O(q⁴). The numerical checks cover the Dirac rows directly and the scalar E1 kernel only through the O(q⁴) test.
- **"Not at R9-9's placement"** is checked on the original code as well as on my re-implementation.
- **The R19-5 face1 shift** is checked at m = 0.3, with the grid validated against `dface.py`. At m = 0.01 it is a size estimate only.
- **Not claimed:**
  - anything about VW or the photon (that is R19-26);
  - W2;
  - two loops;
  - uniqueness of the re-placement;
  - that the rows convention is the only defensible placement. The rows *are* computed with it, and that is what makes it the row-neutral target.

## 10. Files (all in `S/`)

- `lib1930.py`: analytic laws, offset-parity classes, the FF and PR re-placements, placement phases.
- `r1930_lemmaP.py` → `.out`: the Lemma P recheck on explicit lattice operators.
- `r1930_lawcheck.py` → `.out`: the analytic laws against the archived ones.
- `r1930_parity.py` → `.out`: class content.
- `r1930_origcode.py` → `.out`: cut jumps in the unmodified R13-5 and R19-5 code.
- `r1930_cut.py` → `r1930_cut_m0.01.out`: probes (b) and (c), all kernels and modes.
- `r1930_w1.py` → `.out`: probe (d).
- `r1930_cov.py` → `.out`: covariance.
- `r1930_rows.py` → `r1930_rows_m0.3_N32.out`, `_m0.3_N48.out`, `_m0.01_N32.out`, `_m0.01_N48.out`: probe (e).
- `r1930_face1_lit.py` → `.out`: the s → 0 check of the literal face1 shift.
- `r1930_dface_ref_m0.3.out`: R18-13's `dface.py`, run unmodified on the root law at m = 0.3.
- `r195copy/` and `r135copy/`: unmodified copies of the code audited.
