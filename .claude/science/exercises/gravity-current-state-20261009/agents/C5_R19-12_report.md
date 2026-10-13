# C5 R19-12 report: the charge block on the gravity root's edges (one law, the whole SM cone bill)

**Author.** Claude Opus 5.5 probe (same model family as the supervisor and every C5 worker). Unrefereed. 2026-10-13, 04:52Z to about 05:45Z. No repository file was edited. No downloads, no web lookups.

**Paths.**
- `P/` = `.claude/science/exercises/gravity-current-state-20261009/`.
- `S/` = `.../scratchpad/C5/R19-12/`. My scripts and `.out` files are in `S/scripts/`. `S/arch/` holds unmodified copies of `P/scripts/C5/{R16-10, R16-2, R18-5, R18-9, R18-13}` (R16-2's files under `S/arch/R16-10/arch/R16-2/`, as R16-10's imports expect; `S/arch/arch18/` is a second copy of R18-5 so that R18-9's `lib9.py` imports resolve).
- Every run used `OMP_NUM_THREADS=2` and finished in under 8 minutes (longest: the direct N = 160 gravity-root solves, 458 s). Load was 6–10 on 10 cores from other jobs. At most two of my runs were active at once (4 threads), during two windows of about 6 minutes each.

**Read.**
- `docs/MINIMAL_AXIOMS_2026-06-29.md`, in full (`AX`).
- `P/TESTS.md`: the C5 method and readings (`:2302-2319`); R16-1, R16-2 (`:5041-5083`), their worker lines (`:5210-5220`, `:5246-5256`) and verdicts (`:5414-5426`); R16-10 (`:5451-5476`), worker line (`:5563-5572`) and verdict (`:5890-5893`); R17-4 (`:5816-5845`, `:5940-5946`, `:6171-6178`); R18-9 (`:6847-6869`, `:7044-7059`, verdict `:7284-7297`); R18-13 (`:7063-7091`, `:7305-7315`, verdict `:7505-7516`); the head rules of rounds 17–19 (`:5688-5706`, `:6395-6406`, `:7117-7130`); R19-11 (`:7628-7653`); my item (`:7673-7703`).
- `P/agents/`: `C5_R16-2_report.md` (all) and `vR16-2`; `C5_R16-10_report.md` (all) and `vR16-10`; `vR16-1`; `C5_R18-9_report.md` (all) and `vR18-9`; `C5_R18-13_report.md` (§§0, 3.7–4) and `vR18-13`; `C5_R16-9_report.md` (§0) and `vR16-9`; `C5_R17-4_report.md` (§3.9 bill table); `C5_S26_synthesis.md` §1.6 and Q5; `vR11-1` item 4.
- R19-11 (running, unrefereed): only its worker file `scratchpad/C5/R19-11/run/root0_m0.out`, used once as an unrefereed claim (§3.6).

**Runners rechecked before use (checked; `scripts/r1912_recheck.out`, `scripts/r1912_recheck_photon.out`).**
- R16-10's point functions reproduce the archived R16-2 scalar runner and R13-7 Dirac runner to all 10 printed digits (−2.4249903748; −9.8481846559), as in `P/scripts/C5/R16-10/r1610_validate_exact.out:1-2`.
- R16-10's Theorem-L split reproduces its archived scan rows: D1(1.0, 1/√3) with Gph(3.0) gives −5.1692, and G(2.6) with Gph(3.0) gives −1.1126 (`r1610_scan_N48.out:17,47`).
- R16-2's photon moments reproduce: G_½ = +0.0993 on D1(1.0, 0.2) and G_0 = −0.0988 on G(1.0), both at m = 0.05, N = 128 (`r162_dirac_family_N128.out`, `r162_scalar_family_N128.out`).
- **The root photon is R16-10's Gph.** R18-5's γG_w(2.9435, π − 2.9435) and R16-10's Gph(2.9435) agree to 6e-11 on |q| < π. At q = ±π the two codes pick opposite signs of the same odd-symbol value |d(π)| = (π + c)/2; neither grid samples that point.
- **Root files.** `root4k_N224.npy` and R18-13's `root_refR18-9.npy` hold (b_s, b_f, r, a, fr, b_γ, fw, m). The refined root (`vR18-9:11`) is (2.526103698, 0.909103708, 0.555604226, −0.176095005) with fr = 1, b_γ = 2.9435, fw = 1, m = 0.01. At it, the archived R18-5 runners give per-species gravity rows equal to R18-9's table (`C5_R18-9_report.md:225-227`) to the printed digits: scalar (−6.2775e-4, −3.6216e-4, +1.06272e-2); Dirac (+1.98457e-3, +1.3215e-4, −1.70941e-2, μ_T2 4e-10).

**Labels.** proved (complete argument under stated hypotheses; unrefereed) / checked (numerics here) / suggested / reading / comparator (literature, RECALLED).

---

## 0. In plain words

1. **On the root's own edges the charge rows are all nonzero and one-signed (checked).** I computed them on both root edge sets:
   - the refereed m = 0.01 root: D1(0.9091, 0.5556), G(2.5261);
   - R19-11's m → 0⁺ root (worker, unrefereed): D1(0.915439, 0.568281), G(2.590035).

   The photon γG_w(2.9435) is the same in both. In units of e²/16π², m = 0.01 root first, then the 0⁺ root:
   - electron-type speed shift per unit charge²: **F_½(0⁺) = −5.2444 / −5.2448**;
   - charged-scalar shift: **F_0(0⁺) = −1.1674 / −1.1488**;
   - photon shift from one unit-charge Dirac loop: **G_½(0⁺) = +0.1148 / +0.1304**, so the SM photon shift is **Σ = 8G_½ = +0.919 / +1.043**.

   In physical units (× α/4π = 5.807e-4), the electron, up and down classes sit at −3.05e-3, −1.35e-3 and −3.4e-4 from the tree cone on both edge sets, and the photon at +5.3e-4 / +6.1e-4. The class splits Δ_c(0⁺) = u(q_c²F − Σ) are **−3.58e-3, −1.89e-3, −8.7e-4** (m = 0.01 root) and **−3.65e-3, −1.96e-3, −9.4e-4** (0⁺ root). The count below is the same on both.
2. **One law costs one more charge row than separate edges did (proved, given the checked numbers).** R16-2's "3 per class" aligns charged matter with the photon only. On one law the graviton and every neutral species (neutrinos, neutral scalars, gluons, Z) are on the same lattice. At this order the neutral species are exactly on the tree cone (no photon vertex), and GW170817 and SN1987A (comparators, RECALLED) tie the photon to them. So five natural cone values must be equalized, and in the per-class basis that takes **4** counterterms: κ_e, κ_u, κ_d and the photon's κ_γ. On separate edges this row was hidden, because the photon could sit at its own shifted cone.
3. **One gravity freedom can pay that fourth row (checked bracket; existence by continuity, suggested).** The gravity root is not isolated: R18-9's photon window is a one-parameter family of roots. Along it the Dirac edge (b_f, r) moves, and the photon shift Σ, which depends only on the Dirac edge (Lemma Q), **changes sign**.
   - At m = 0.01 (R18-9's convention), three new direct N = 160 gravity roots (four axial rows ≤ 6e-11, all subluminal) give Σ = +0.0245 at b_γ = 2.93717, **Σ = −0.00044 at b_γ = 2.936996** (uΣ = −2.6e-7), and Σ = −0.128 at b_γ = 2.93613.
   - At the Σ = 0 point, b_γ ≈ 2.936999 and b_f ≈ 0.83795, the photon is on the neutral/graviton cone with no counterterm. At S1 all six gravity rows close, including the off-axis pair, by R18-13's route.
   - At m → 0⁺ (R19-11's convention), μ_T2 = 0 and Σ = 0 are both Dirac-only rows, so together they pin the Dirac edge at D1(0.834591, 0.527606).
   - The 0⁺ gravity family reaches that edge near b_γ ≈ 2.93605, by direct roots at b_γ = 2.9368, 2.9361 and 2.9360. Σ = +0.0072 at 2.9361 and −0.0073 at 2.9360 (§3.4).
   - Then the charge block costs **3 class counterterms plus one equality on the gravity family**, which spends the window.

   This is the only gravity knob that doubles as a charge knob:
   - the stencil and placement data (a, w_d, w_o) never enter one-loop QED;
   - b_s enters only charged-scalar rows, which the SM setting excludes;
   - the photon edge moves F_½ by only 1.6e-3 across the window and cannot make it vanish.
4. **The photon window helps the size and the photon row, not the count of matter rows (checked).** With the near-linear subluminal photon, |F_½| is 5.24, against 9.88 for R16-2's box photon and 18.6 for R18-5's earlier gravity photon, so every class counterterm is about half as large. But no subluminal photon in the family nulls F_½: as the photon box grows toward π, F_½ levels off at −5.23. R16-10's two-tuning route needs a stiffened photon; on the root's Dirac edge its zero is at G\* = 3.341 with whole-zone **v_max = 8.05**, which the gravity root's all-subluminal setting excludes.
5. **The bill (reading, per (spin, |q|) class basis, on one law):**
   - on the root's own edges: 6 gravity equalities + 1 window selection + 4 charge counterterms + tadpole + CC, i.e. **11 equality tunings + 1 window + CC** (10 + window + CC if the tadpole is paid by (d-i));
   - at the family's Σ = 0 root: 6 + 1 (Σ = 0, replacing the window) + 3 + tadpole + CC = **11 + CC with no open selection left** (10 + CC under (d-i)).
   - Per species: 17 + CC (Σ = 0 root) or 17 + window + CC (root's edges). q²-correlated: 9 + CC or 9 + window + CC.
6. **Against the FIXED readings: ONE-LAW-BILL (worker reading, checked).** Every row's payment is named, and no charge payment breaks a gravity row at the computed orders. CONFLICT is not met. The expectation's "3 charge counterterms per class" holds only at the Σ = 0 root of the same family, where the fourth row is paid by the window's freedom; on the root's own edges it is 4. The expectation's total "≈ 11 + CC" holds in both routes, if the window is not counted as a tuning.

---

## 1. Hypotheses, classes and basis (stated before any title)

- **Setting (registered, `TESTS:7688-7691`).**
  - R16-2's one-loop runner and R16-10's split evaluator (Theorem L), at the R18-9/13 root edges.
  - SM charges counted per class and per species; m → 0⁺.
  - The charge block is **R16-2's setting** (`TESTS:5067-5070`; `C5_R16-2_report.md:45-49`): one-loop QED on Z³ × ℝ, Peierls coupling, Feynman gauge, λ → 0 by Theorem L. The charged species are the nine SM Dirac flavours, all on the root's one Dirac edge. Colour is a multiplicity in the photon loop, so Σ_j n_j q_j² = 3 + 4 + 1 = 8 (`C5_R16-2_report.md:85-87`).
  - Excluded, as in R16-2: W± and every non-abelian sector, two loops, non-Peierls vertices, and physical charged scalars. A **charged-Higgs variant** (one complex q = 1 scalar on the root's scalar edge) is carried separately, because probe (a) asks for F_0.
- **Edges.** Two sets:
  - the refined R18-9 root at m = 0.01 (`vR18-9:11`; checked above), detailed below;
  - R19-11's m → 0⁺ root (`agents/C5_R19-11_report.md`, §0 item 2; worker, unrefereed): (b_s, b_f, r, a) = (2.590035, 0.915439, 0.568281, −0.176177), same photon. The coordinator asked that the charge block, which runs at m → 0⁺, use these edges or report both. I report both.

  The m = 0.01 root:
  - Dirac: D1(b_f = 0.909103708, r = 0.555604226), R14-1's family. r < 1/√3, so v_max ≤ 1 (`vR18-9:15`).
  - Scalar: G_w(2.526103698, w = π − b_s) = R14-1's G(b_s) (ZLaw([1, 0], [b + w/2], w) has h′ = 1 − sstep((k − b)/w); with fr = 1 this is SymG(b_s)).
  - Photon: γG_w(2.9435, 0.198093) = Gph(2.9435). It has d = q on |q| ≤ 2.9435 and d′ ∈ [0, 1], so whole-zone v_max = 1. Box-exact, so Theorem L applies with r₁ < min(b_f, 2.9435).
  - Gravity-side data, not used by the charge block: stencil a = −0.176095, own-direction weights (w_d, w_o) ≈ (−1.172, −0.195) (`vR18-13:13`).
- **Observables.**
  - Matter: δc_i = q_i²·u·F_s(m_i), with u = α/4π = 5.807e-4 (α RECALLED), and F_s(0⁺) = K_s + Λ_s (Theorem L, `vR16-10:3`).
  - Photon: δc_γ = u·Σ, Σ = Σ_j n_j q_j² G_s(m_j). G_½ is R10-1's Theorem D moment; G_0 is Theorem T′ (`C5_R16-2_report.md:73`). By Lemma Q, Σ does not depend on the photon symbol or on λ (`vR16-2:5`).
  - The split is Δ_c(0⁺) = u(q_c²F_½(0⁺) − Σ), the electron–photon split for SM content. The single-species split F − G (R16-1's convention) is also printed.
- **Counterterm bases (the counting rule, `TESTS:5700`).**
  - **(C) per (spin, |q|) class:** κ_c for each class, including the neutral classes (½, 0), (0, 0) and (1, 0), plus κ_γ.
  - **(S) per species:** κ_i for each of the nine charged flavours, plus κ_γ.
  - **(Q) q²-correlated:** κ_i = q_i²κ for the Dirac spin class, plus κ_γ.

  Each counterterm adds to one party's (or, for Q, a q²-weighted set of parties') O(e²) cone and to nothing else at this order. A tuning is a nonzero counterterm, or one equality imposed on law parameters (R16-2's convention, `C5_R16-2_report.md:231`).
- **Orders.** Gravity rows are one loop in G with tree matter. Charge rows are one loop in e with tree gravity. Mixed O(G e²) terms are two-loop and are **not computed** (§3.6).
- **Comparators (RECALLED).**
  - ε\* = 2.66e-19 (charged matter against the photon; `C5_R8-5_report.md:261`, via R16-2).
  - GW170817: |c_g − c_γ| ≲ 1e-15.
  - SN1987A: |c_ν − c_γ| ≲ 2e-9.
- **Subtractions named before any run:** none. Counterterms are tunings, not subtractions. Theorem L's split is an exact identity.
- **Removed hypothesis (`TESTS:7693`):** the charge and gravity blocks on separate edges.

## 2. Prior art (each counted once)

- **R16-2 + vR16-2.** Lemma Q (q²F factorization; Σ independent of the photon symbol and λ), the scalar runner, Lemma T′, and the conditional 3-per-class / 7-per-species count. That count is **relative**: charged matter against the photon (`C5_R16-2_report.md:232-240`; `vR16-2:13,17`). "κ_γ is replaceable" (`vR16-2:13`), including by a matter edge with Σ = 0 (the referee's literal-family point near b₂ = 2.31).
- **R16-10 + vR16-10.** Theorem L, with K_½ = +2/3 and K_0 = −1/3 (`vR16-10:3-5`). The stiffened-photon Dirac zero at v_max 7.35 (`vR16-10:7,16`). The subluminal-photon tadpole bound ≤ −2.02 (`vR16-10:21-25`). "One photon-side condition (κ_γ, or a matter shape with Σ = 0)" (`C5_R16-10_report.md:43`).
- **R16-1 + vR16-1.** The Wilson-edge interval no-go (`vR16-1:19`). Not re-used here. Its hypothesis (H2′) requires d ∈ {2 sin(q/2), q} wherever W > 0 (`C5_R16-1_report.md:56`). The root photon's turn (2.9435, π] lies where W > 0, so the root law is outside R16-1's class as stated (reading). The interval no-go is not needed for the bill, because masses are not knobs.
- **R16-9 + vR16-9.** The first one-law bill. It splits the conditions into a charge block and a gravity block that "share no knob", and adds the counts (`C5_R16-9_report.md:19,27`). It counts the charge block as R16-2's relative 3/7 and does not treat the photon against the graviton or neutral species. vR16-9 calls the split valid only in the scalar-only truncation (`vR16-9:13`).
- **R18-9, R18-13 + verdicts.** The root, its five, then seven, continuous knobs (`vR18-9:17`; `vR18-13:13`), and R18-9's model-interpolated window b_γ ≈ 2.936–2.947 with its family of roots (`C5_R18-9_report.md:265-277`; `window_model.out`; not enclosed, `vR18-9:3`). That family is the free direction used in §3.4.
- **R17-4 / S26 bill tables** (`C5_R17-4_report.md:225-234`; `C5_S26_synthesis.md:233-244`). These are the row lists, and their "charged-matter cones 3 / 7" line.
- **R11-1(b) + vR11-1.** Matter's own graviton-loop speed is split from the graviton, but only in one prescription (`vR11-1` item 4). It is listed here as a row outside the bill.
- **R19-11 (running, unrefereed).** Its worker file gives a massless-limit gravity root (§3.6).
- **Grep.** I searched `P/agents/*.md`, `TESTS.md` and `SUMMARY.md` for "neutral" with cone or speed, "photon" with "graviton cone", "absolute", "Σ = 0", and "SN1987A". The hits are R16-9's block split, R16-10's Σ = 0 remark, and an unrelated C3 table. No prior item states that one law adds the photon-to-neutral row, and none computes Σ along the gravity root family.

## 3. Results

### 3.1 (a) F_s(0⁺) and G_s(0⁺) on the root's edges (checked)

`scripts/r1912_a.out`. The photon is the root's γG_w(2.9435, fw = 1). λ = 0; m = 1e-6 (Dirac) and 0 (scalar).

| N | F_½(0⁺) | Dirac tadpole | F_0(0⁺) | scalar seagull |
|---|---|---|---|---|
| 48 | −5.24456 | −5.35002 | −1.17826 | −1.33496 |
| 64 | −5.24436 | −5.35010 | −1.16666 | −1.31803 |
| 96 | −5.24447 | −5.35013 | −1.16765 | −1.31949 |
| 128 | −5.24444 | −5.35011 | −1.16743 | −1.31918 |
| 160 | −5.24444 | −5.35011 | −1.16743 | −1.31917 |

- **Convergence.** N = 128 and N = 160 agree to 1e-5 (`r1912_a.out:8,10`).
- **Split radii.** Two radius pairs give identical digits (`:2-9`). This is expected: in the excised shell the box-exact integrand at m = λ = 0 has a P₂(n_x) angular profile (`C5_R16-10_report.md:134`), and that sums to zero over a cubic-symmetric grid shell.
- **Lemma T′ check.** The tadpole −5.35 lies below the Lemma T′ bound for a subluminal photon, −2.02 (`vR16-10:25`), as it must.
- **Mass dependence** (N = 128, `:12-19`).
  - Dirac: F(m) − F(0⁺) = +1.008m, +1.031m, +1.075m at m = 0.0025, 0.005, 0.01. This is linear (the Wilson term, as in R16-10).
  - Scalar: +0.517m², even in m.
- **Photon moments** (N = 128/192/256 agree to 3e-6, `:21-23`).
  - G_½(m) = 0.11429 at m = 0.0025 and 0.11374 at 0.005, so **G_½(0⁺) = +0.11484** (linear extrapolation, slope −0.220).
  - G_0(0⁺) = −0.05917, flat in m.

### 3.2 The splits and Σ on the root's edges (checked)

`scripts/r1912_bill_routeA.out`. Physical values are × u = 5.807e-4.

| party | natural O(e²) cone shift | counterterm to reach the neutral cone |
|---|---|---|
| neutral species (ν; neutral scalars; gluons, Z) | **0 exactly** (no QED vertex; proved) | — |
| photon: Σ = 8G_½ = +0.91872 | +5.335e-4 | κ_γ = −5.335e-4 |
| e class (q² = 1): F = −5.24444 | −3.0455e-3 | κ_e = +3.0455e-3 |
| u class (q² = 4/9) | −1.3535e-3 | κ_u = +1.3535e-3 |
| d class (q² = 1/9) | −3.384e-4 | κ_d = +3.384e-4 |
| [variant] φ⁺ (spin 0, q = 1): F_0 = −1.16743 | −6.779e-4 | κ_φ = +6.779e-4 |

- **Splits Δ_c(0⁺) = u(q_c²F − Σ):** e −3.579e-3; u −1.887e-3; d −8.72e-4.
- **Single-species split:** F − G = −5.359, i.e. −3.11e-3. R16-1's −10.88 was on D1(1.4, 1/√3) with a different photon (`vR16-1:11`).
- **With the charged-Higgs variant:** Σ′ = 8G_½ + G_0 = +0.8596.
- **Residuals after tuning** (class counterterms set at m → 0⁺; F′ = +1.03):
  - top (4/9)·F′·m_t a·u = 3.75e-21;
  - τ 8.7e-23;
  - b 2.3e-23.

  The photon's own mass slope, from the top-quark loop, contributes 2.4e-21. All are below ε\* = 2.66e-19 by at least 70×.
- **Required precision.** κ_c to about ε\* ≈ 3e-19 absolute, i.e. about 1e-16 of its size, matching R16-2/F2. κ_γ to about 1e-15 (GW170817).

### 3.3 Lemma A: one law adds the photon-to-neutral row (proved, given the checked inputs of §3.2)

- **Hypotheses.**
  - (i) The orders of §1.
  - (ii) Tree cones all equal 1: the edges are box-exact (Lemma Q step 5, `C5_R16-2_report.md:125`), and the graviton's tree cone is 1.
  - (iii) Basis (C).
  - (iv) The comparators force all parties onto one cone. Every pairwise gap of natural values in §3.2 is ≥ 1.9e-4, far above 2e-9.
  - (v) The gravity rows' count does not depend on their target. The graviton cone rows are equalities Ξ = target, so retargeting the graviton is free.
- **Claim.** If F_½(0⁺) ≠ 0 and Σ ≠ 0, the charge block on one law needs **exactly 4** basis-(C) counterterms (κ_e, κ_u, κ_d, κ_γ). On separate edges, R16-2 needed 3.
- **Proof.**
  1. The parties' natural shifts are:
     - 0 for every neutral class. There are three of them in the setting: (½, 0) ν, (0, 0) the four real scalars, and (1, 0) gluons and Z.
     - uΣ for the photon.
     - u q_c²F for c = e, u, d.
  2. With F ≠ 0 and the q_c² distinct, the class values are distinct and nonzero. With Σ > 0 > q_c²F, all five values {0, uΣ, uF, (4/9)uF, (1/9)uF} are distinct.
  3. Each basis-(C) counterterm moves exactly one class value.
  4. If the common cone is the neutral value 0, the four non-neutral parties each need one counterterm: 4. Sufficiency is the table in §3.2.
  5. If the common cone is any other party's value, the three neutral classes and the other non-neutral parties must all move: at least 3 + 3 = 6.
  6. The graviton's target is free by (v), so it changes neither count. Hence the minimum is 4. ∎
- **Why R16-2 found 3.** Without neutral parties and a graviton on the same law, the photon can sit at its own shifted cone. The untuned class aligns to it (`C5_R16-2_report.md:236`). On one law that leaves the photon 5.3e-4 off the neutrino cone. That is excluded by SN1987A (RECALLED), and by GW170817 unless the graviton is retargeted.
- **Other bases (same argument).**
  - **(S):** 9 + 1 = **10**, against R16-2's 7. No charged species can be left untuned, because F ≠ 0 and the target is the neutral cone.
  - **(Q):** κ = −uF aligns all nine charged flavours at once, and κ_γ aligns the photon: **2**, unchanged. q_i²κ leaves the neutral classes alone.
  - **Charged-Higgs variant:** +1 in every basis (κ_φ; F_0 ≠ F_½, so Q's Dirac κ cannot cover it).
- **Scope.** The lemma is a count in a stated additive basis. It is not R16-10's convention-independent codimension count (`vR16-10:19`). In a basis where all parties may be correlated, the count changes, as (Q) shows.

### 3.4 (b) Which gravity knobs can double as charge knobs

**Never, by inspection of the one-loop QED Feynman rules (proved).** F_s and G_s involve only the matter symbols, the photon symbol and the Peierls vertex (Lemma Q; the runners' inputs, `r1610_core.py:16-63`, `r101_dirac_moment_copy.py:17-52`). So:
- **a, w_d, w_o** (graviton–vector vertex stencils) do not enter.
- **b_s** enters only the charged-scalar variant.

**The photon edge b_γ: negligible lever (checked, `r1912_photon.out:6-8`).** At the root's matter edges, F_½(0⁺) = −5.24557, −5.24447 and −5.24398 at b_γ = 2.9361, 2.9435 and 2.9469 (R18-9's quoted window ends; not recomputed by me). That is a change of 1.6e-3 out of 5.24. Σ does not depend on b_γ at all (Lemma Q).

**The gravity family's free direction pays the photon row (checked bracket).**
- **Structure (proved).**
  - μ_T2 is a Dirac-only row (`C5_R18-9_report.md:140-145`), and Σ is a Dirac-only row (Lemma Q).
  - So on one law the pair {μ_T2 = 0, Σ = 0} fixes the Dirac edge (b_f, r) by itself.
  - The window's photon edge then solves the a-blind row X, b_s solves μ_E, a solves T₂g, and (w_d, w_o) solve the face rows (Lemma O, `vR18-13:7`).
  - The joint root is then isolated: the window's one free parameter becomes an equality.
- **Σ along R18-9's model family (`scripts/r1912_Gfamily.out`; family rows from `P/scripts/C5/R18-9/window_model.out`):**

  | b_s (fr = 1) | b_γ\* | b_f | r | G_½(0⁺) | Σ = 8G_½ |
  |---|---|---|---|---|---|
  | 2.90 | 2.94688 | 0.94281 | 0.57390 | +0.16837 | +1.347 |
  | 2.526 (refined root) | 2.9435 | 0.90910 | 0.55560 | +0.11484 | +0.919 |
  | 2.20 | 2.94148 | 0.88492 | 0.54323 | +0.07610 | +0.609 |
  | 2.00 | 2.94026 | 0.87191 | 0.53681 | +0.05513 | +0.441 |
  | 1.534 (W2, direct) | 2.9378 | 0.84663 | 0.52480 | +0.01416 | +0.113 |
  | 1.50 | 2.93781 | 0.84532 | 0.52418 | +0.01201 | +0.096 |
  | 1.00 | 2.93613 | 0.82590 | 0.51534 | −0.01972 | −0.158 |
  | 1.00 (fr = 0.02) | 2.94159 | 0.79041 | 0.49995 | −0.07826 | −0.626 |

- **Direct N = 160 gravity roots** (R18-9's `solve4k.py`, unmodified; four axial rows at m = 0.01; photon at N = 160):
  - **S0, b_γ = 2.93717** (`scripts/solve4k_S0_N160.out`): (b_s, b_f, r, a) = (1.38003, 0.839823, 0.521651, −0.175517). Totals ≤ 5.4e-11; det J = −1.59e-4; r < 1/√3. There **G_½(0⁺) = +0.003057, Σ = +0.0245** (`scripts/r1912_bill_S0.out`).
  - **S1, b_γ = 2.936996** (secant prediction from W2 and S0; `scripts/solve4k_S1_N160.out`): (1.33422, 0.837916, 0.520778, −0.175502). Totals ≤ 6.4e-11; det J = −1.53e-4; r < 1/√3. There **G_½(0⁺) = −0.000055, Σ = −0.00044, uΣ = −2.6e-7** (`scripts/r1912_bill_S1.out`). F_½(0⁺) = −5.2935.
  - **E1, b_γ = 2.93613** (R18-9's quoted window end; `scripts/solve4k_E1_N160.out`): (1.07547, 0.828169, 0.516362, −0.175429). Totals ≤ 1e-11; det J = −1.22e-4; r < 1/√3. There **G_½(0⁺) = −0.01600, Σ = −0.128** (`scripts/r1912_bill_E1.out`).
  - **Root files:** `scripts/root4k_{S0,S1,E1}.npy` (same format as R18-9's).
- **Reading.**
  - Σ changes sign between two directly computed, transversal (det J ≠ 0), all-subluminal gravity roots: S0 (+0.0245) and S1 (−0.00044), which are 1.7e-4 apart in b_γ.
  - Linear interpolation puts Σ = 0 at b_γ ≈ 2.936999, b_f ≈ 0.83795, r ≈ 0.52086, b_s ≈ 1.336.
  - By continuity of the root branch between S0 and S1, there is a gravity root with Σ = 0 exactly. That continuity is **suggested**, not proved. It is supported by four direct roots (W2, S0, S1, E1) that are monotone in every knob, and by R18-9's smooth model.
- **All six gravity rows at S1 (checked; `scripts/r1912_offaxisS1_N160.out`).** This uses R18-13's route with its unmodified evaluators: scalar E1/U, Dirac UD `dface` at GL(4,10), and photon VWa-geo at N = 160.
  - The own-direction weights solve to (w_d, w_o) = (−1.1168, −0.1839), against R18-13's (−1.140, −0.191) at N = 160 at the main root. Jacobian det = +11.6.
  - Direct re-evaluation leaves face totals of −5.6e-6 and −1.3e-6, and axial totals of −1.3e-7 and −2.1e-7. These are the same N = 160 grid artefacts R18-13 had at the main root (−5.9e-6, −1.4e-6, `P/scripts/C5/R18-13/photface_N160.out`).
  - So S1 is a six-row gravity root, in R18-13's sense, with uΣ = −2.6e-7.
- **The Dirac-only pin (checked; `scripts/r1912_pin0.out`).** Solving {μ_T2 = 0, Σ = 0} for (b_f, r) alone:
  - at m_f = 0.01: (0.83795, 0.52079). This matches the S0–S1 interpolation (0.83795, 0.52086).
  - at m_f → 0⁺: **(0.834591, 0.527606)**, with G_½ = 3e-11 and μ_T2 = 8e-19 there.

  Any Σ = 0 one-law root at m → 0⁺ must have this Dirac edge (proved: both rows are Dirac-only). Whether the 0⁺ gravity family reaches it is tested next.
- **The m → 0⁺ family (R19-11's mass convention; `scripts/r1912_root0B_{A,B,C}.out`).** Direct four-row axial roots: Dirac m = 0, scalar m = 1e-5, vector μ_E regulator 1e-3 as in R19-11's `root0.py`, photon coefficients at N = 160. All are transversal and subluminal.

  | b_γ | (b_s, b_f, r, a) | max |rows| | det J | G_½(0⁺) | Σ = 8G_½ |
  |---|---|---|---|---|---|
  | 2.9368 | (1.42430, 0.842805, 0.531457, −0.175563) | 9e-13 | −1.76e-4 | +0.013395 | +0.1072 |
  | 2.9361 | (1.23694, 0.835146, 0.527865, −0.175504) | 2e-10 | −1.51e-4 | +0.000906 | +0.00725 |
  | 2.9360 | (1.20762, 0.834031, 0.527346, −0.175495) | 3e-11 | −1.47e-4 | −0.000915 | −0.00732 |

  The pin's b_f = 0.834591 lies just beyond the 2.9361 root's 0.835146. Linear extrapolation in b_γ, from both the pin and the two G values, puts the 0⁺ Σ = 0 root at b_γ ≈ 2.93605, b_s ≈ 1.22, r = 0.5276. That is inside the subluminal domain (r < 1/√3 by 0.050). The 2.9360 root then gives **Σ = −0.00732 against +0.00725 at 2.9361**: a direct sign change between two transversal 0⁺ roots 1e-4 apart in b_γ. So the 0⁺ Σ = 0 root lies at b_γ ≈ 2.93605, b_f ≈ 0.83459, as the pin requires (checked bracket; continuity between the two roots suggested). Its off-axis pair was not recomputed. At m = 0.01, S1 shows R18-13's route closes it nearby.
  - At that point the photon's one-loop shift from SM charged loops vanishes. The photon then sits on the neutral cone with κ_γ = 0, and the GW170817/SN1987A row is paid by the window's freedom.
  - Precision: dΣ/db_f ≈ 13 (from W2 → S0), so |uΣ| ≤ 1e-15 needs b_f fixed to about 1.3e-13, the same order as the gravity rows' own precision (`C5_R17-4_report.md:238`).
- **What cannot be paid by gravity data (checked on the sampled family).** F_½(0⁺) lies in [−5.30, −5.23] at every sampled family point (`scripts/r1912_family.out`, `r1912_bill_{S0,S1,E1}.out`), so no class row is ever paid for free.
- **Mass convention.** Σ is always evaluated at m → 0⁺; only the gravity rows' mass changes.
  - With gravity rows at m = 0.01 (R18-9's convention), the pin is b_f = 0.83795.
  - With gravity rows at m → 0⁺ (R19-11's), it is b_f = 0.83459, a shift of −0.0034 that comes through the μ_T2 curve r*(b_f; m).
  - The Σ = 0 root exists, by direct bracket or near-bracket, in both conventions.
  - One law at the actual SM masses is R19-11's question. Suggested, not checked: its IFT argument (R19-11 §0 item 4) carries over with Σ added as a seventh equality, because Σ's mass dependence is linear and small (dG_½/dm ≈ −0.17). One law at all masses is R19-11's question.

### 3.5 Does the photon window help or hurt? (checked, `scripts/r1912_photon.out`)

F_½(0⁺) on the root's D1 and F_0(0⁺) on the root's G(b_s), as the photon changes (N = 96):

| photon | whole-zone v_max | F_½(0⁺) | F_0(0⁺) |
|---|---|---|---|
| γG_w(1.0, fw 1) | 1 | −8.145 | −2.069 |
| γG_w(2.0, fw 1) | 1 | −5.829 | −1.374 |
| γG_w(2.6, fw 1) | 1 | −5.346 | −1.192 |
| **γG_w(2.9435, fw 1) (root)** | 1 | **−5.244** | **−1.168** |
| γG_w(3.13, fw 1) | 1 | −5.231 | −1.167 |
| R18-5's γG_w(1.271, 0.260) | 1 | −18.634 | −5.275 |
| R16-2's R85(1, 2, G = 1) box photon | 1 | −9.885 | −2.386 |
| R16-10's stiffened R85(1, 2, G\* = 3.3413) | **8.05** | 0.0000 | — |

- **It helps the size (checked).** The near-linear photon roughly halves |F_½| against R16-2's photon, and divides it by 3.6 against R18-5's. So the class counterterms are 2–4× smaller.
- **It does not help the count of matter rows (checked, sampled).** Within subluminal γG_w photons, F_½ rises monotonically with the box and levels off at −5.23 as the box approaches π. Every subluminal photon sampled here, and R16-10's 92 sampled 𝒞_sub laws (`vR16-10:21-25`; `C5_R16-10_report.md:172`), leave F_½ ≤ −3.8. No subluminal zero is known, and none is excluded by proof (Lemma F is OPEN on 𝒞_sub, `vR16-10:17`).
- **It forecloses R16-10's two-tuning route (checked).** On the root's own D1 the stiffened-photon zero sits at G\* = 3.3413 with whole-zone **v_max = 8.05** (`r1912_photon.out:14-16`). That is outside the gravity root's setting (all edges subluminal, `TESTS:6854`) and the v_max rule for gauge fields (`TESTS:5699`). The stiffened photon would also change every photon gravity row; its rows were not computed.
- **Its family freedom pays the photon row** (§3.4). This is a benefit of the window that R18-9 did not need.

### 3.6 (c) The total bill on one law, every row listed (reading; per (spin, |q|) class basis unless stated)

| row | count | payer | status |
|---|---|---|---|
| graviton axis cone Ξ_T2g, Ξ_Eg | 2 | jointly with the next two rows: b_s, b_f, r, a | [ref] O(q) convention (`vR18-9:23`) |
| E_g shear μ_E | 1 | (joint) | [ref] |
| T₂g shear μ_T2 | 1 | Dirac r on R17-13's curve (joint) | [ref] |
| off-axis face1, face2 | 2 | own-direction weights w_d, w_o (signed) | [ref] O(q) convention (`vR18-13:13`) |
| body | 0 | follows (rank 4) | [ref] |
| photon window | 1 open selection (A), or consumed (B) | b_γ | [ref] window sampled, not enclosed |
| charged-matter cones e, u, d | 3 | κ_e, κ_u, κ_d | checked here (§3.2) |
| photon on the neutral/graviton cone | 1 | (A) κ_γ; or (B) the Σ = 0 equality on the gravity family | checked (A); bracket checked, existence by continuity suggested (B) |
| neutral-matter cones at O(e²) | 0 | exact | proved (no QED vertex) |
| LV tadpole | 1, or 0 numbers under (d-i) | trace counterterm, or P-vac′ | [ref] `vR17-4:11`; (d-i) conditional bookkeeping |
| CC | 1, or 0 numbers under (S) | — | [ref] |

**Totals.**
- **(A) On the root's own edges:** 6 + 4 + 1 = **11 equalities + 1 window + CC**; under (d-i), 10 equalities + 1 window + CC.
- **(B) At the family's Σ = 0 root:** 6 + 1 + 3 + 1 = **11 equalities + CC, with no open selection**; under (d-i), 10 + CC.
- **Per species:** 6 + 10 + 1 = 17 equalities + window + CC (A), or 6 + 1 + 9 + 1 = 17 + CC (B).
- **q²-correlated:** 6 + 2 + 1 = 9 + window + CC (A), or 6 + 1 + 1 + 1 = 9 + CC (B).
- **Charged-Higgs variant:** +1 in each.

**Mass convention (checked).** The gravity rows in (A) are R18-9's, at m = 0.01. At R19-11's m → 0⁺ root (2.590035, 0.915439, 0.568281, −0.176177; `agents/C5_R19-11_report.md` §0 item 2, unrefereed), the charge inputs are (`scripts/r1912_bill_R19-11report_root.out`):
- F_½(0⁺) = −5.24475, F_0(0⁺) = −1.14876;
- G_½(0⁺) = +0.13038, so Σ = +1.04305;
- Δ_c = −3.651e-3 (e), −1.959e-3 (u), −9.44e-4 (d);
- κ_γ = −6.057e-4; the κ_c are unchanged to 4 digits.

All are one-signed as before, so the (A) count is the same at the 0⁺ root. (An earlier run at R19-11's pre-refinement file values, `r1912_bill_R19-11root.out`, agrees to 1e-5.)

R19-11 also finds the Wilson-Dirac gravity rows linear in m. The charge rows are linear in m in the same way (F′ ≈ +1.04, from the Wilson mass). Their residuals at SM masses (≤ 3.8e-21) stay below ε\*, so the charge block adds no mass-relation condition beyond R19-11's.

**Rows outside this bill (listed, not counted).**
- **Mixed O(G e²) corrections to every cone row (two-loop; not computed).** They change the same rows, not their number. Whether the same knobs re-zero them depends on transversality. The weak direction of the gravity Jacobian (σ_min ≈ 6.3e-4, `vR18-9:13`) is sensitive: a 1e-5 shift in X moves b_s by about 0.01 (`C5_R18-9_report.md:247`). An O(u)-relative change of the Dirac row contributions (about 0.04 each) could move b_s by O(0.1) (suggested).
- **Matter's own graviton-loop speeds** (R11-1(b), SPLIT-PRESENT in one prescription; `vR11-1` item 4). If they are edge-dependent, there is one row per (spin, edge) relative to the graviton. Not in R13-8's rows, and not computed here.
- **W± and the non-abelian sectors.** Suggested: quarks sit on the same D1 edge and gluons on the same photon edge, so the quarks' QCD shift is C_F g_s² times the same F_½. That would add a colour-class row and a gluon-side row with the same Lemma-Q structure. Not computed.
- **The rest:** exact W1 (R19-5); the E2 extension (+1); radiative stability; two loops; the vector-like D1 edge (the SM's chiral content is not represented; P132-type).

### 3.7 (d) Prices (named, not adopted)

- **No axiom text is touched.**
  - Edges, photon shape and counterterms are downstream dynamics (`AX:114-130`).
  - The source/action gate is `AX:187`.
  - Physical sizes use a = ℓ_P, the scale-reference primitive (`AX:189-190`).
- **P-R19-12a (new): the photon-to-neutral row.** On one law the photon's O(e²) shift must be removed absolutely, not relatively. The payer is either:
  - κ_γ ≈ −5.3e-4, fixed to about 1e-15; or
  - the Σ = 0 root of the gravity family, which spends R18-9's window as an equality and fixes b_f to about 1e-13.
- **P73 refined again (one law).**

  | basis | root's edges | Σ = 0 root |
  |---|---|---|
  | per class | 4 | 3 + the family equality |
  | per species | 10 | 9 + the family equality |
  | q²-correlated | 2 | 1 + the family equality |

  This replaces R16-2's relative 3 / 7 for any law that also carries the graviton and neutral species.
- **P-R19-12b (variant):** a charged Higgs component on the root's scalar edge adds κ_φ, and moves the Σ′ = 0 point (Σ′ already changes sign between W2 and S0: +0.032 → −0.061).
- **Not a new price.** R16-10's P-r16-10a, the superluminal photon, is incompatible with the gravity root: v_max = 8.05 on the root's Dirac edge.

## 4. Against the FIXED readings (`TESTS:7699-7702`)

**ONE-LAW-BILL: worker reading MET (checked).**

| clause | status |
|---|---|
| explicit total count on the root's edges | (A): 11 equalities + 1 window + CC (per class); 17 / 9 in the S / Q bases; §3.6. The same count holds on both the m = 0.01 root and R19-11's m → 0⁺ root |
| every row's payment named | yes, table §3.6. The gravity rows are paid as refereed (O(q) convention). The charge rows are paid by κ_e, κ_u, κ_d, κ_γ, with numerical values (§3.2) |
| checked | F, G, Σ, Δ_c on the root's edges at N ≤ 160/256 (§3.1–3.2); residuals ≤ 3.8e-21 |
| charge payments do not break gravity rows | at the computed orders, κ's enter gravity rows only at O(G e²) (two-loop, not computed; §3.6) |

**CONFLICT: not met.** The charge rows are paid on the root's edges by counterterms that do not touch any gravity row at the stated orders. Nothing here is a no-go, so no referee is required by the rule. A referee is still advisable for Lemma A's count and for the §3.4 bracket.

**OPEN:** not needed.

**Expectation (`TESTS:7703`).**
- "3 charge counterterms per class": **not on the root's own edges, where it is 4** (Lemma A). It holds at the family's Σ = 0 root, where the fourth row is paid by the window's freedom (§3.4).
- "≈ 6 + 1 + 3 + tadpole + CC ≈ 11 + CC": met in count in both routes. In (A) the window is the "+1" and the charge block is 4, so 6 + 4 + tadpole = 11 equalities, plus the window. In (B) the "+1" is the Σ = 0 equality. "Fewer if the tadpole is paid by (d-i)": 10 + CC (B).

**Removed hypothesis** (separate edges). Removing it changes the charge count, through Lemma A. It also creates a coupling: a gravity-family freedom pays a charge row.

## 5. Strong-word check

- **"Proved":**
  - the neutral parties' zero O(e²) shift (no QED vertex);
  - Lemma A's count, given the checked distinct values and the stated additive basis;
  - "a, w_d, w_o and b_s (SM setting) never enter one-loop QED" (Feynman-rule inspection);
  - the Dirac-only structure {μ_T2, Σ}.

  All are unrefereed.
- **"Checked":** every F, G, Σ value, the convergence in N and the mass slopes, the direct gravity roots, and the photon scan. Resolutions are in the `.out` files.
- **"Σ = 0 root exists":** a sign change between direct roots is checked at m = 0.01. Continuity of the branch between them is suggested; it is not proved. The S1 root (uΣ = −2.6e-7) is checked on all six gravity rows to N = 160 grid accuracy.
- **"Window":** R18-9's interpolated numbers are quoted as theirs (not recomputed or enclosed). My claims use only directly computed roots.
- **"Levels off at −5.23":** sampled to box 3.13; not a bound.
- **"No subluminal zero":** not claimed. It is sampled only, and Lemma F remains OPEN on 𝒞_sub.
- **Not claimed:**
  - minimality in a convention-independent sense;
  - the mixed O(G e²) rows;
  - W±, QCD and electroweak-unbroken classes;
  - the matter graviton-loop rows;
  - exact W1;
  - one law at both masses (R19-11);
  - radiative stability.

## 6. For the referee

1. **Lemma A.** Is the absolute target (neutral parties exactly on the tree cone at O(e²)) right, and is the basis-(C) count of 4 (vs R16-2's relative 3) correct? Does the SN1987A comparator (RECALLED) or the gluon/Z cones carry the argument when the graviton is retargeted?
2. **Reproduce F_½(0⁺) = −5.2444 and G_½(0⁺) = +0.1148** on the refined root's edges with an independent evaluator.
3. **The Σ = 0 roots.** Check the Σ sign change between the direct roots S0 and S1 (m = 0.01), and whether the root branch between them is continuous. Check the six-row closure at S1. At m → 0⁺, check the Dirac-only pin D1(0.834591, 0.527606) and the direct roots near b_γ ≈ 2.9360–2.9361.
4. **Whether the Σ = 0 root counts as "on the root's edges".** It is a different member of the same refereed family, with the same knobs and vertices. Under "literal first" (`TESTS:7124`), the reading above uses the root's own edges (A) and reports (B) as a new root.

## 7. Files (`S/scripts/`)

- **Rechecks:** `r1912_recheck.{py,out}`, `r1912_recheck_photon.{py,out}`.
- **Library:** `r1912_lib.py` (imports `S/arch/` unmodified).
- **(a):** `r1912_a.{py,out}`.
- **Photon dependence:** `r1912_photon.{py,out}`.
- **Family:**
  - `r1912_family.{py,out}` (F, G at the directly solved and model roots);
  - `r1912_Gfamily.{py,out}` (Σ along R18-9's model family).
- **Bills:**
  - `r1912_bill.py` → `r1912_bill_routeA.out` (refined root), `r1912_bill_S0.out`, `r1912_bill_E1.out`, `r1912_bill_S1.out`;
  - `r1912_bill_R19-11root.out` (R19-11's unrefereed massless root).
- **Direct gravity roots** (R18-9's `solve4k.py`, unmodified, run from `S/arch/R18-9/`):
  - `solve4k_S0_N160.out`, `solve4k_E1_N160.out`, `solve4k_S1_N160.out`;
  - root files moved to `S/scripts/root4k_{S0,E1,S1}.npy`.
- **Six rows at S1:** `r1912_offaxisS1.py` → `r1912_offaxisS1_N160.out` (R18-13's `photface_hi.py` logic with S1's edges; R17-4's archive copied to `S/arch/arch17_4/`).
- **The m → 0⁺ track:**
  - `r1912_bill_R19-11report_root.out` (R19-11's reported 0⁺ edges);
  - `r1912_pin0.{py,out}` (the Dirac-only pin);
  - `r1912_root0B.py` → `r1912_root0B_{A,B}.out`, `root0B_{A,B}.npy`.
