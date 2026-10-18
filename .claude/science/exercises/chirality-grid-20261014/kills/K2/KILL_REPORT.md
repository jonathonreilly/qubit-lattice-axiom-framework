# K2 kill round: the Euclidean set-B package (X3) and its parent F2-H

**Agent and provenance.** Claude Opus 5.5, kill-round agent, run 2026-10-14 from 14:58Z to 16:15Z. This is the same model family as the X3 author, the route agents and the supervisor. Nothing here is independent or refereed. No repository was edited. Every script is my own code; X3's scripts were read but never imported. All runs used OMP_NUM_THREADS=2, one at a time (brief exceptions: two 3-second unit tests of about 50 MB). Four runs exceeded 0.3 GB peak RSS; see the memory note in §5.

**Refresher read.**
- `docs/MINIMAL_AXIOMS_2026-06-29.md`, in full (233 lines). Cited as AX.
- Skill steps 6 and 8 (origin/main).
- In full: `WALL.md`, `ASSUMPTIONS.md`, `ROUTES.md`, `APPROACH_REGISTRY.md`, `routes/F2/ROUTE_REPORT.md`, `combos/X3/COMBO_REPORT.md` and `combos/X3/PREREG.md`.
- X3's script `tx3fp_admissible_gi_rp_2d.py`; F3 route report lines 60-110.
- Gravity-packet lines were located by a read-only search agent. I re-read the load-bearing ones myself (cited below).

**Paths.**
- `CH/` = `.claude/science/exercises/chirality-grid-20261014/` in the chirality-grid worktree.
- `GR/` = `.claude/science/exercises/gravity-current-state-20261009/` in the toe-leverage worktree.
- `K2/` = my folder `scratchpad/chirality_ex/kills/K2/`.

**Labels.** proved (my argument, unrefereed) / checked (a script run here) / suggested / reading / comparator.

---

## 0. Plain-words summary

**The free (no gauge field) part of X3 holds up.** I rebuilt the real-time spectrum of the free overlap fermion from scratch, in 4D, with my own code. Exactly as X3 said:
- there is one light handed particle per projection;
- every would-be doubler sits in a heavy continuum starting at energy ln 2 (Planck scale) with positive norm;
- for M ≤ 1 the transfer matrix is positive; for 1 < M < 2 a gapped, non-inverted negative sector appears;
- the number of hidden real-time states per momentum grows without bound.

**The gauge-field part breaks.** I ran X3's own "single cheapest decisive next test" cleanly. That means:
- every plaquette is admissible, and the H_W gap is ≥ 0.70 everywhere;
- the gauge averaging over the links crossing the mirror plane is done exactly (smooth rules on the exact domain, error 1e-14).

On a 2 × 12 lattice (open time ends), the gauge-invariant reflection-positivity matrix of the gauged overlap has a **negative eigenvalue**:
- −7.4 × 10⁻⁶ of the largest eigenvalue, about 9 orders above the numerical error;
- a second set gives −5.1 × 10⁻⁷;
- a separate, independently written code reproduces it to 0.07%;
- it stays negative for gauge couplings β = 0, 1, 4 and 10, and for M = 0.6 and 1.0;
- the Wilson-fermion control is positive on the same configurations.

That meets the pre-registered FAIL line. So **L3g, the gauged reflection-positivity lemma, fails as a general property of the gauged overlap measure**: one clean finite counterexample is enough.

Where I did *not* find a violation:
- the smaller open lattice (2 × 8);
- the torus with antiperiodic time (2 × 8 and 2 × 12);
- clustered configuration sets on the torus (V5).

The torus matrices are far from degenerate (margins 1e-5 to 1e-2), so they have less power to show a 1e-5-size effect. On the torus, the setting closest to an infinite time direction, L3g is therefore **open, not refuted**.

On open lattices the violation does not fade as the ends move away from the mirror plane. Clean failing sets (6 per length):
- Lt = 12: 3 of 6;
- Lt = 16: 0 of 6;
- Lt = 20: 2 of 6, the largest −3.3e-5.

**X3's earlier "no violation" evidence was never able to see it.**
- Its gauge-invariant runs used open time ends with periodic space. There the Wilson kernel H_W has *exact* zero modes at the time edges: the Chern edge states of the 2D Wilson operator, present even with no gauge field.
- Its overlap was therefore not the local one. X3's "bulk plaquettes up to 0.74" diagnosis is wrong.
- Its quadrature error (≈ 5e-3) was about 1000× larger than the violation.

**Consequence for the set-B package.** The package needs reflection positivity of exactly this measure. Its standard proof route (gauge-fixed positivity) was already closed by X3 (reproduced here). Now its general form has a counterexample. What remains is a torus- or infinite-time-specific positivity with no known mechanism.

X3's own price table says what happens if L3g fails: the package falls under "Euclidean-only without reflection positivity", which the wall forbids (`CH/WALL.md:44`), unless matter pays Π-W (a non-positive weight). The other exits are:
- domain-wall fermions at finite L_s (F2-R's ~60-auxiliaries-per-site price);
- a positivity proof specific to periodic or infinite time.

**X3-C ("F2-R's prices (a) and (b) are one price") is overstated.** It is shown only for the overlap, in one direction. And it means the route touches *both* axiom texts (AX:57 and AX:47), not one.

**Caveats.** Tiny 2D U(1) lattices; the vector-like Dirac overlap, not the chiral measure; gauge-only observables. Step 8 requires another-vendor referee before this is read as a scientific no-go.

---

## 1. Verdicts

| Item | Verdict | Reason (label) |
|---|---|---|
| **X3-A** (free OS spectrum: one light Weyl per projection; doublers a positive continuum at E ≥ ln 2; T ≥ 0 for M ≤ 1; π sector for 1 < M < 2) | **survives** | Independent 4D rebuild (K2-T1 + V4, checked). Honesty note: the as-registered K2-T1 formally hit a DEAD line (H0 −2.8e-4). The cause was FFT aliasing at my own p = 10⁻³ point, named before checking in V4 and removed there; every other momentum was PSD. All numbers reproduced: thresholds ln 2 (M = 1, 0.5), 0.881 (M = 2−√2), 0.405 / 0.693 (M = 1.5), 0.095 / 0.105 (M = 1.9); poles iff β < √(1+S²) at 58/58 momenta per M; no corner poles. One wording nit: at M = 2−√2 the minimum is a flat valley along the whole p₁ axis (cosh E₁ = √2 exactly, proved by one line of algebra), not a set of S = 0 points. |
| **X3-B** (F3-A's π-copy kill does not reach the Euclidean route) | **survives (free fields only)** | No isolated negative-λ pole for any M; negative λ only in the gapped continuum where β < 0, with H0 PSD (checked). Scope: X3-B presupposes that an OS transfer matrix exists. For gauged overlap matter on open-time lattices, K2-T3 says it does not; on the torus this is open. Where no T exists, F3-A is moot, but only because something worse has happened. |
| **X3-C** (price relocation; (a) ≡ (b) as one price) | **wounded** | (i) An infinite real-time fibre: checked (Hankel rank 8, 12, 16, 20, 20, 20, 22 for n = 2..8; Wilson 2 throughout). (ii) The "threshold = 5D bulk band at p₅ = 0" identity is the same algebraic expression written twice (the Wilson transfer formula with one extra momentum set to zero); it carries no equivalence. X3 concedes full equivalence is not shown (`X3/COMBO_REPORT.md:139`). (iii) "(a) ≡ (b)" is shown only for the overlap, and one way. In general the step from a non-rational kernel to an infinite fibre goes through Lemma H (bounded, continuous H) and leaves an "infinitely heavy band" exit unexamined. (iv) Reading: paying (a) entails (b)'s consequence, so the overlap route touches both AX:57 and AX:47. "One price" (`CH/ROUTES.md:55`, listed as a genuine gain) should read "the two prices come together for the overlap; both axiom texts are touched". (v) Reading: set B's reconstructed gauge links already have infinite-dimensional Hilbert spaces, so an infinite real-time site is not new to the fermion fibre. |
| **L3g** (RP of the gauged overlap measure on gauge-invariant observables) | **dead as a general property; open on the torus** (checked, same family; other-vendor referee owed) | K2-T3 FAIL line met on the open-time-end lattice: G1p δ = 0.6, set 1, min/max −7.4e-6, q 4.8e-15, min\|H_W\| 0.861, Wilson +1.1e-5. Reproduced by independent code (V1b, −7.40e-6). β-robust: −7.4e-6 to −8.5e-6 for β ∈ {0, 1, 4, 10} (V2a). The Θ control discriminates (V2c). Clustered open sets also give negatives (−1.1e-7, −1.7e-7; V5). It persists as the open ends recede: Lt = 20 gives FAIL-line sets 2/6, down to −3.3e-5 (V6). Torus (antiperiodic t, Lt = 8 and 12; random and clustered sets): all PSD, but with margins 1e-5 to 1e-2, i.e. low power (V3, V5). So L3g cannot be proved as a property of the overlap measure alone. A torus- or infinite-time-specific positivity is not refuted and has no known mechanism. Scope: §3.3. |
| **X3-E method claims** | split | "Gauge-fixed (Osterwalder–Seiler) positivity fails for the overlap": **survives**, reproduced independently in clean geometries (−2.7e-3 to −2.5e-2, K2-T2; −1e-4 to −6.6e-3 on admissible sets, D-GF). "No violation on gauge-invariant observables" (T-X3f′, D1): **dead**. The open geometry has exact H_W edge zero modes (K2-T2) and the error bar is 1000× the effect. |
| **Set-B package (X3 as a whole)** | **wounded (named gap: L3g)** | Its only RP route for gauged overlap matter is now: no gauge-fixed positivity (X3, reproduced); general positivity false (K2-T3, open-end lattice); torus positivity unrefuted but with no mechanism. The X3 contingency row (`X3/COMBO_REPORT.md:252`) becomes the likely branch: Π-W for matter, DWF at finite L_s (the F2-R finite-n price), or an infinite-time positivity proof. This affects vector-like (QCD-type) overlap matter too, not only the chiral measure. It is not "dead": the decisive torus or infinite-time test has not been run with enough power. |
| **F2-H (parent)** | **wounded** | Its leaf L3 (`CH/routes/F2/ROUTE_REPORT.md:111`) now has a negative finite certificate in the vector-like 2D proxy. F2-H's "Euclidean-with-RP" form (`:116-119`) now hinges on a torus- or infinite-time-specific positivity for which no mechanism is known. L2 (non-abelian measure locality) is untouched. F2-H's correction of R2-4 :204 is right for free fields only. |

**Does X3 assume the target?** No.

**Already tried (step 0)?** Free overlap RP is in Kikukawa–Usui, conceded by X3 (K1). Gauged RP was not in the repo before X3.

**Terminal target-equivalent?** No. X3's terminal L_pkg is stronger than T (`X3/COMBO_REPORT.md:272-284`). Its L3g leaf has now failed a finite test.

---

## 2. (d) Consistency with landed results (reading, with lines)

**R10-2, "box symbols lose RP".** It does **not** cover the overlap.
- R10-2's "box symbol" is a momentum-space box: the continuum symbol on |k_μ| < b < π, glued to a periodic band, non-analytic at the box edge (`GR/agents/C5_R10-2_report.md:29, :63`). The mechanism is non-analyticity of a time-local two-point function at some θ₀ ∉ πZ (Corollary A1, `:112`).
- The free overlap symbol is real-analytic on the real torus for 0 < M < 2. Proved: ω² = 1 + S² + β² − 2β cos p₄ ≥ S² + (|β| − 1)², which vanishes only at a corner with |β| = 1, i.e. M ∈ {0, 2, 4, 6}.
- So Lemma A's necessary condition is met, and K2-T1 confirms free link RP.
- R10-2's referee restricts it to bosonic transfer-representable laws and excludes "unrestricted Grassmann laws" (`GR/agents/C5_R10-2_referee_verdict.md:21`). It says nothing about the gauged overlap.
- K2-T3's failure has a different mechanism: a non-factorizable coupling of U₊ and U₋ through a time-nonlocal fermion kernel, after gauge averaging. It contradicts nothing in R10-2; it is in R10-2's spirit (non-local kernels endanger RP).

**R19-28 (set B).**
- B3 requires "the conditional of a reflection-positive (RP) Euclidean Gibbs weight" (`GR/agents/C5_R19-28_report.md:205`).
- It names overlap couplings as the chiral-matter option, "suggested", "No class-wide no-go [ref]" (`:207`).
- K2-T3 is a finite counterexample to B3 for gauged overlap matter in the 2D proxy. That is not a contradiction, since R19-28 never claimed it, but it removes the suggested chiral-matter option unless Π-W is paid.

**R19-33.**
- Refereed B-RP-FAILS: the conserved bridge has a strict negative site-RP witness (`GR/TESTS.md:8909-8913`).
- "Site RP alone — insufficient" (`GR/agents/C5_R19-33_referee_verdict.md:7`).
- X3 uses link RP and checks T ≥ 0 directly (H1), which is what the referee asks for. No contradiction.
- X3's L3grav leaf is correctly open: R19-33's positivity rests on a slice-local stress (`C5_R19-33_report.md:22, :93`), and the overlap stress is not slice-local.
- Suggested, untested: K2-T3 makes L3grav look worse, not better. The graviton would couple through the same time-nonlocal kernel that breaks gauge-link RP.

**R2-4 :204** ("RP of overlap … in physical time: not established").
- Out of date for free fields (Kikukawa–Usui; X3; K2-T1).
- For gauged fields it is now sharpened to "fails in the 2D U(1) vector-like proxy" (K2-T3).
- Π-W (`C5_R2-4_report.md:293`) is the existing named price that would absorb this, if the owner extends it from gravity to matter.

---

## 3. Tests (all pre-registered in `K2/PREREG.md` before running; follow-ups dated, readings never edited)

### 3.1 K2-T1 + V4: free 4D OS transfer content (X3-A, X3-B)

**Method.** Own gammas. D built numerically. C(t; p) by FFT over N₄ = 8192. Block-Hankel H0/H1 with a GEVP. Branch points from the numerically continued X̃X (its linearity in cos p₄ checked, not assumed). Poles located directly as zeros of σ_min(D(p₄ = iE)). E₁ minimized globally: 12³ grid plus Nelder–Mead from 201 starts.

**Calibration.** Γ = +γ4 (Wilson r = 1 H0 min/max −7e-17; −γ4 gives −1.0).

**Controls.**
- Naive fermion: H1 = −1.00, with the time-doubler λ = −0.489 detected.
- Wilson: rank 2.

**As registered (`k2t1_free_transfer_4d.out`).** Worst H0 min/max is −1.5e-4 / −2.8e-4 at M = 0.5 / 1.0. That formally hits a DEAD line.
- The cause, stated before checking (V4): my own choice of the momentum p = (10⁻³, 0, 0), where FFT aliasing ~ e^{−E·N₄} ≈ 3e-4.
- Every other momentum was PSD (corners +6e-15 to +3e-9).
- The GEVP top-eigenvalue mismatches come from an n = 6 Hankel failing to resolve a pole just above a continuum.

**V4 (`k2t1b_free_transfer_4d_V4.out`; near-zero point moved to p = 0.02).**
- M = 0.5 and 1.0: H0 and H1 PSD (+6e-15 and −5e-17). Direct poles iff β < √(1+S²) at 58/58 momenta, with |E_pole − arcsinh S| ≤ 3.6e-9. No pole at any of the 7 nonzero corners. No GEVP eigenvalue above the ceiling.
- M = 1.5 and 1.9: negative λ only at β < 0 (11 and 12 momenta); H0 PSD (−1e-17); H1 indefinite (−3.5e-3, −2.9e-2).
- Thresholds as in §1.
- Hankel rank as in §1.
- **Reading: X3-A SURVIVES; X3-B survives for free fields.**

### 3.2 K2-T2: X3's gauge-invariant test geometry (`k2t2_geometry_and_sanity.out`)

**Free min|eig H_W|, M = 1.**

| Geometry | min\|eig H_W\| |
|---|---|
| X3's (Lx = 4 periodic, open t ∈ −3..4) | **2.4e-16** |
| Lx = 2 periodic, open t | 1.3e-21 |
| Lx = 8 periodic, open t | 2.9e-17 |
| Lx = 4 antiperiodic, open t | 0.707 |
| Lx = 2 antiperiodic, open t | 1.02 |
| Every torus | 1.000 |

- The zero modes sit 100% on the boundary slices t = −3 and t = 4.
- Proved (one line): H_W = γ5(D_W − M) is the Qi–Wu–Zhang Chern insulator for 0 < M < 2. With open time ends its edge band crosses zero at k_x = 0, which periodic x contains.
- A boundary Wilson line W shifts the edge energy to ~sin(W/Lx). That fits X3's reported min|H_W| = 0.002–0.021 for its random configurations (`X3/PREREG.md:248`).
- **Pre-registered reading triggered.** X3's diagnosis ("bulk plaquettes up to 0.74") is wrong. T-X3d/e/f/f′ and D1 tested an overlap whose kernel range was about 1/0.002 lattice spacings, so they are not L3g evidence.

**Sanity.**
- Gauge invariance of log det to 7e-15.
- The Wilson gauge-fixed kernel is PSD in every clean geometry (−3e-15 to +1.5e-4), which calibrates Θ.
- The overlap gauge-fixed kernel is negative (−2.7e-3, −1.0e-2, −2.5e-2, −1.8e-2). This independently reproduces X3's T-X3c.

### 3.3 K2-T3: the decisive L3g test (`k2t3_*.out`)

**Kernel.**
- Zt_ab = ∫ dU_c w(U_c) det D_m[u_a, U_c, θ⁻¹u_b], with M = 1, m = 0.05, k = 8 configurations per set.
- The crossing integral is reduced exactly to the gauge-invariant variables: crossing-plaquette angles, plus the Polyakov phase on the torus.

**Admissibility.**
- Bulk plaquettes |arg| < δ by rejection sampling.
- Crossing plaquettes carry the Fejér weight (1 − |θ|/δ)₊.
- Amendment A1, made before any K2-T3 code existed: the hard indicator has sign-changing Fourier coefficients, so Wilson + indicator is not guaranteed RP once fermions carry charge across the plane. The Fejér weight has the same support and coefficients ≥ 0.

**Quadrature.** Gauss–Legendre on kink-split intervals, Duffy rules on triangulated polytope cells, trapezoid on the Polyakov circle.

| Geometry | δ | Overlap min/max (3 sets) | Wilson min/max | q (quadrature change) | min\|H_W\| | Reading |
|---|---|---|---|---|---|---|
| G1: Lx = 2, Lt = 8, open t, antiperiodic x | 0.3 | +1.5e-6, +6.9e-5, +8.8e-7 | +2.2e-6, +7.0e-5, +2.3e-6 | ≤ 5e-15 | 0.958 | clean, PSD |
| G1 | 0.6 | +2.3e-6, +1.3e-4, +3.0e-6 | +8.6e-6, +1.4e-4, +1.6e-5 | ≤ 5e-15 | 0.857 | clean, PSD |
| G1p: Lx = 2, Lt = 12, open t | 0.3 | +2.1e-5, +2.3e-5, +7.5e-5 | +2.2e-5, +2.7e-5, +7.6e-5 | ≤ 1e-14 | 0.953 | clean, PSD |
| **G1p** | **0.6** | +1.4e-5, **−7.4e-6**, **−5.1e-7** | +4.1e-5, **+1.1e-5**, **+1.4e-6** | ≤ 8e-15 | 0.861 | **set 1 meets FAIL** (−7.4e-6 < −1e-6 and > 10q; Wilson PSD). Set 2 is negative but above the −1e-6 line |
| G3: torus, Lx = 2, Lt = 8 | 0.6 | +6.5e-3, +2.5e-2, +1.3e-3 | +5.4e-3, +2.3e-2, +1.0e-3 | ≤ 2e-15 | 0.707 | clean, PSD |
| G3p: torus, Lx = 2, Lt = 12 (V3) | 0.6 | +2.3e-2, +5.8e-3, +1.1e-2 | +2.1e-2, +2.7e-3, +1.0e-2 | ≤ 3e-15 | 0.716 | clean, PSD with LARGE margin (see V5) |
| V5 G1p clustered (open, Lt = 12) | 0.6 | −1.1e-7, +2.1e-8, −1.7e-7 | +2.7e-7, +2.6e-7, +2.0e-7 | ≤ 1e-14 | 0.893 | negatives recur, below the −1e-6 line |
| V5 G3p clustered (torus, Lt = 12) | 0.6 | +3.5e-5, +2.1e-5, +4.8e-5 | +2.2e-5, +1.9e-5, +3.2e-5 | ≤ 7e-15 | 0.776 | PSD (torus open) |
| V6 open, Lx = 2, Lt = 12 / 16 / 20 (6 sets each) | 0.6 | most negative −2.8e-6 / +3.0e-6 / **−3.3e-5** | min +1.7e-6 / +9.8e-6 / +5.2e-6 | ≤ 2e-14 | ≥ 0.83 | FAIL-line sets 3/6, 0/6, **2/6**: persists as the ends recede |
| G2: Lx = 4, Lt = 8, open t (1 set, time-cut) | 0.6 | +1.3e-4 | +1.2e-4 | 7.6e-10 (Duffy n = 5 vs 7) | 0.507 | clean, PSD (like G1 at Lt = 8). G2 and G3 at δ = 0.3 not run (time) |

**Pre-registered K2-T3 reading: FAIL.** A clean set has a negative eigenvalue beyond error with the Wilson control PSD. PASS is excluded.

**Bug hunt and robustness (V1, V2; registered after seeing the negative value, before running).**
- **V1a.** The full 64-entry kernel, with no symmetry filling, has symmetry defect 4e-15 and min/max −7.4055e-6.
- **V1b, independent code.** Different site indexing, links assembled explicitly, every plaquette computed from links, D_ov = 1 + X(X†X)^{−1/2} (no sgn(H_W)), trapezoid over the full circle of the crossing phase. Result −7.3872e-6 at N = 20000 and −7.4005e-6 at N = 40000, converging O(h²). Wilson +1.08e-5.
- **V2a.** Set 1 stays at −7.4e-6, −7.8e-6, −8.4e-6, −8.5e-6 for β_g = 0, 1, 4, 10 (weight tri·e^{β cos}, positive-type). Wilson stays +1.1e-5 to +1.2e-5. The "weight-robust" reading holds.
- **V2b.** (M, m) = (1, 0.3): −4.7e-6; (0.6, 0.05): −2.0e-5; (1.4, 0.05): +6.2e-6.
- **V2c.** Under a deliberately wrong Θ (unconjugated mirrored temporal links), the Wilson gauge-fixed kernel goes non-Hermitian (1.2e-1) and negative (−3.4e-4). So the control has discriminating power.

**Scope of the FAIL (reading).**
- Vector-like Dirac overlap, link reflection, gauge-only observables, 2D U(1), Lx = 2 (degenerate x extent), open time ends, Lt = 12 and 20.
- Is it an open-end effect? Reading: an end effect should shrink like e^{−ν·Lt/2}, with ν the overlap's decay rate (order 1 at this gap). The observed size does not shrink: −7.4e-6 at Lt = 12, −3.3e-5 at Lt = 20. That fits a bulk effect better, though the number of sets is small (V6: Lt = 16 had none).
- Torus with antiperiodic time: no violation found. The margins (1e-5 to 1e-2) exceed the open-lattice effect size, so the torus is open, not cleared.
- Not tested: the chiral (Weyl) measure, fermionic observables, Lx ≥ 4 at Lt ≥ 12, 4D, non-abelian groups.
- The violation is small: ~1e-5 of the largest eigenvalue, at lattice-scale configuration differences. In a framework whose lattice is fundamental, there is no continuum limit to absorb it.
- Interpretation as a scientific no-go needs an other-vendor referee (skill step 8).

---

## 4. What this changes, and the next cheapest decisive tests

1. **Registry, ROUTES.md X3 row (`CH/ROUTES.md:44`).**
   - Replace "Gauged RP: … gauge-averaged tests are inconclusive" with "gauge-invariant RP FAILS on clean open-time 2D U(1) lattices (K2-T3, V6). On the torus, no violation was found at limited power. Same family; referee owed".
   - Round-2 synthesis item 3 ("set B … the only chirality route whose free real-time spectrum is clean") stays true for free fields. Its shared obligation L3g is now failing, not open.
2. **"F2-R's two prices are one price" (`CH/ROUTES.md:55`)** → "come together for the overlap; both AX:57 and AX:47 are touched".
3. **Referee owed.** Codex sol on `lat2d.py`, `k2t3_gi_rp.py`, `k2t3_verify.py` and the Amendment A1 argument.
4. **Next tests** (cheap, each under 1 h, pre-registrable):
   - (i) a torus test with power: many clustered configurations (k ≥ 16), or a direct search for the most negative f, at Lt = 12–20, and Lx = 4;
   - (ii) the same kernel for a 2D anomaly-free *chiral* U(1) measure (Lüscher), Θ = θ∘conj;
   - (iii) a domain-wall control at finite L_s, which must be RP;
   - (iv) site reflection instead of link reflection.

   If (ii) also fails, the set-B chirality route needs Π-W for matter or the DWF finite-n price; that is an owner decision.

---

## 5. Files (all in `K2/`)

- `PREREG.md`: K2-T1, K2-T2 and K2-T3 (with Amendment A1), written before any run. Follow-ups V1–V6 are dated, and each was registered before its run.
- `scripts/lat2d.py`: own 2D U(1) Wilson/overlap code (geometries, exact gauge-invariant reduction, quadrature).
- `scripts/k2t2_geometry_and_sanity.py` → `.out`: K2-T2 and sanity checks.
- `scripts/k2t3_gi_rp.py`, `run.sh` → `k2t3_<geom>_d<δ>_tri.out` / `.err`: K2-T3 and V3.
- `scripts/k2t3_verify.py` → `.out`: V1 (independent code path).
- `scripts/k2v2_robustness.py` → `.out`: V2.
- `scripts/k2t1_free_transfer_4d.py` → `.out`: K2-T1 as registered.
- `scripts/k2t1b_free_transfer_4d_V4.py` → `.out`: V4.
- `scripts/k2v5_clustered.py` → `k2v5_G1p.out`, `k2v5_G3p.out`: V5.
- `scripts/k2v6_open_Lt.py` → `.out`: V6.
- **Memory note (rule breach, reported).** Peak RSS stayed under 0.3 GB for most runs, but four runs went over: G3p 329 MB, V5-G3p 323 MB, V6 313 MB (299 MiB), and V1 (independent check) 410 MB, the worst. The first breach was a 3-operand einsum with a p·N³ intermediate, fixed at 15:50Z; the remainder is baseline (numpy/scipy) plus batch arrays. All runs were sequential, and nothing is left running.
- **Numerical note.** numpy 2.4's slogdet raises spurious divide/overflow RuntimeWarnings on these matrices. I checked it against the sum of log eigenvalues: agreement to 1e-14, min\|eig D_m\| = 1.39.
- `chain*.sh`: run queues. Note: chain2–chain4 were stopped by hand; chain4 stalled about 10 minutes because its `pgrep -f` matched my own monitor command lines.
