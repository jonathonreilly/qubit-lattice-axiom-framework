# C5 R19-35 report: lambda_nn, the vacuum's degree-0 bulk graviton entry at the root

**Author/provenance.** Claude Opus 5.5 probe (same family as supervisor and all C5 workers). Unrefereed. Run 2026-10-13 07:44Z to ~09:45Z (LATE: past the 09:15Z hard return; a tool-hook stall cost ~1.5 h). No repository file edited; nothing downloaded.
**Paths.** `P/` = `.claude/science/exercises/gravity-current-state-20261009/`; `AX` = `docs/MINIMAL_AXIOMS_2026-06-29.md`; `S/` = `scratchpad/C5/R19-35/`. Scripts/outputs in `S/scripts/`; `arch18/`, `arch17_4/`, `r1929/` are unmodified copies of `P/scripts/C5/{R18-5, R17-4, R19-29}`; `root_refR18-9.npy` from `P/scripts/C5/R18-13/`. OMP_NUM_THREADS=2; every run < 2 min.
**Read.** AX in full; `P/TESTS.md:8795-8814` (item), `:8470-8600` (R19-24 Lemma E, referee records), `:8600-8794`; `P/agents/C5_R19-29_report.md` (all), `C5_R18-13_report.md` (all), `C5_R19-15_report.md` + verdict (all), `C5_R19-20_report.md:1-200`, `C5_R9-9_report.md` (all), `C5_R17-4_report.md:1-60,180-230` + verdict, `C5_R19-23` verdict + grep; archived runners `R18-5/{zz,dfam,content3,content4,smud_lib,photon}.py`, `R18-9/{lib9,solve4k}.py`, `R19-29/{a1lib,r1929_root}.py`. R19-24 report not read beyond TESTS (Lemma E as recorded at `TESTS:8485,8568`).
**Labels.** proved (complete argument, unrefereed) / checked (numerics here) / suggested / reading / comparator.

## 0. Plain words
1. **The bare-law value is small (checked).** Under the registered strain flow (SF; R19-15 Lemma H, R19-29 H4), the vacuum's total degree-0 nn entry at vR18-9's root is **lambda_nn = -0.1246** (R19-29 units, its G(0)/4). The bubble part is -6.4707 (x4 = -25.883, reproduces R19-29); the seagull part is **+6.3461**, so 98% of the bubble cancels. |lambda_nn|/|bubble| = **0.019**, below the 0.1 FIXED threshold.
2. **Why it is small (proved + checked).** For a rank-one strain h = nn, each band's SF Hessian is exactly one third of its band-level bubble: Hess(nn) = -(2w/24)<u^4/E^3>, u = n.p (Lemma R1). Its sign is fixed by statistics: negative for bosons, positive for the Dirac sea. At the root: scalars -0.0671, Dirac +0.4870, vectors -0.5445. lambda_nn is a boson-fermion-weighted fourth moment, like the CC; it is small here by a near-cancellation of Dirac and photon parts, not by any identity.
3. **At this point the entry is completion-dependent at O(7) (proved + checked).** The bare vacuum has a large one-point function (e0 = -29.998, SF tadpole tau = -0.611 per unit h_ii). With a nonzero one-point function the degree-0 kernel moves under field reparametrization by O(tadpole). So lambda_nn is fixed only once the one-point counterterms' O(h^2) parts are fixed, and the registered texts do not fix them (P-Tad: "c_h int h_ii", linear in which h is unstated; (S): "-e0 sqrt g", parametrization unstated). Four natural completions give -0.125, +7.375, -0.736, -8.236 (ratios 0.019, 1.14, 0.11, 1.27). Only the covariant-CC completions (B, D) give zero for a fluid vacuum (control).
4. **(S\*) and (Sigma) force lambda_nn = 0 (proved, definitional).** Both subtract the lowest state's whole uniform-static response, which is the degree-0 kernel (Lemma H/H4). No other registered piece (P-Tad, (S), (d-i), N_red, W1-weight) forces it to zero.
5. **face1.** In every completion with lambda_nn != 0 (A-D), R19-29's Theorem Q gives FACE1-HOLDS (Schur term O(s^4)); no crossing pole except B, at s*^2 = 19.4 (outside the zone). Under (S\*) alone: lambda_nn = 0, kappa unchanged, so R19-29's shifted branch applies (w_d = +0.753). Under (Sigma): kappa, c4, X and the raw face1 row are removed too, so there is no shift; face1 is zero by construction (suggested; Lemma R of R19-19).

**Reading (worker): LNN-ZERO-FORCED, naming (S\*) and (Sigma)** (literal first: LNN-NONZERO fails both its clauses). Under the bare SF law lambda_nn = -0.1246 != 0 but under the size threshold; its value is not completion-invariant (item 3). face1: HOLDS in the bare/route-A branch (lambda_nn != 0 at every completion tried), SHIFTS to w_d = +0.753 under (S\*), is paid by construction under (Sigma).

## 1. Class, hypotheses, exclusions (stated before titles)
- **Root:** vR18-9's retuned root (bs, bf, r, a, fr, bg, fw, m) = (2.5261037, 0.9091037, 0.5556042, -0.1760950, 1, 2.9435, 1, 0.01) (`S/scripts/root_refR18-9.npy`; `C5_R18-13_report.md:16`). Species weights 4 scalars (U) + 22.5 Dirac (UD, D1) + 12 vectors (VWa-geo), as R19-29 (`C5_R19-29_report.md:174`).
- **H4 (R19-29, `C5_R19-29_report.md:74-77`):** total degree-0 spatial block = SF uniform-strain Hessian of the lowest-state energy (Lemma H, `C5_R19-15_report.md:127-138`; refereed `C5_R19-15_referee_verdict.md:3`). Per band with zero-point weight w (w = 1/2 real scalar, 1 per vector, -Nc/2 = -2 per 4-component Dirac sea), e(h) = w<E o Phi_h>, v = (1/2)h.p, p = grad(E^2/2). Units are exactly the archived shear rows' (`P/scripts/C5/R18-5/zz.py:87-92`, `dfam.py:7,83-84`, `R18-9/lib9.py:25`), which I reproduce (section 3.1).
- **"Bare law"** = the vacuum's SF Hessian with no one-point counterterm O(h^2) parts (completion A). Completions B-D stated in section 3.3.
- **Dirac convention.** lambda_nn is vertex-free (H4), and at q = 0 R19-5's literal placement phase e^{+-iq.p} is 1, so the bubble split is the same in the rows' and the literal convention (proved by inspection).
- **Excluded:** two loops; finite T; degree-0 h_0nu terms (H4 "solid"); the photon's exact W1 completion; non-root laws; the m = 0.001 root.

## 2. Prior art (count once)
- R19-29 (worker; referee running): Theorem Q, the branch structure, bubble -25.9, "lambda_nn ... not computed" (`C5_R19-29_report.md:135-157,183-185,273`).
- R19-15 + verdict: Lemma H, seagull/bubble split, (S\*) (`C5_R19-15_report.md:127-138,213-222`; verdict items 1, 4).
- R19-20: (Sigma) and its implications; Ward-exact degree-0 kernels = 0 (`C5_R19-20_report.md:101-107,119,171`).
- R19-24 Lemma E: linear (Sigma) = kinetic counterterm incl. mass-like pieces (`TESTS:8485,8568`).
- R17-4: P-Tad = stipulated trace counterterm c_h int h_ii; Lemma Tad (`C5_R17-4_report.md:194-197`). R18-9 root and its per-species mu rows (`P/scripts/C5/R18-9/solve4k_N224.out`).
- Grep of `P/agents` and TESTS for "lambda_nn", "bulk", "lam_b": no prior value; R19-23's lambda_b is a free kernel parameter.

## 3. Results
### 3.1 Runner checks (checked; `lnn_laplace.out`, `lnn_dirac_GL410.out`, `lnn_N96.out`)
- Scalar mu_E (Laplace) +1.0627236e-2 = archived zz.mu_E +1.062724e-2. Photon 2 mu_E +2.8508917e-2 = R18-9's +2.850892e-2. Dirac mu_E -1.709412e-2, mu_T2 +4.4e-10 = dfam.evaluate to all digits.
- Root shear totals: 4(1.0627236e-2) + 22.5(-1.709412e-2) + 12(2.8508917e-2) = -1.8e-6 (paid, as registered).
- Bubble entries reproduce R19-29: scalar -5.03075e-2 (band-level SF bubble -5.030750e-2, identical: U vertex = SF), Dirac interband -7.36324e-2 per field (R19-29 -1.178118/16 = -7.36324e-2).
- The 3D midpoint grid is NOT converged for the photon edge (step width 0.198): N = 64/96 photon values are wrong and are not used. Separable bands use exact 1D-moment Laplace forms (2^14 vs 2^16 samples identical to 8 digits; regulator 1e-3 vs 1e-4 differ by 2e-7 relative).

### 3.2 (a) Seagull bulk entry per species; Lemma R1 (proved; checked)
**Lemma R1.** For h = nn (|n| = 1) on a periodic band, with u = n.p: A = u^2, B = (hp).H.(hp) = u^2 d_n u, and d_n E = u/E. Periodic IBP of d_n(u^3/E) gives 3<u^2 d_n u/E> = <u^4/E^3>. Hence seagull_SF = 2w<u^4/E^3>/12, bubble_SF = -2w<u^4/E^3>/8, Hess(nn) = -2w<u^4/E^3>/24 = bubble_SF/3. Sign = sign(-w). QED. Checked: Dirac IBP form vs rank-one form 2.164325e-2 vs 2.164335e-2; scalar grid 0.2% at N = 96.

| per field (R19-29 lam units) | Hess(nn) (SF) | vertex bubble (R19-29, N=128) | implied seagull |
|---|---|---|---|
| real scalar (U) | -1.676917e-2 | -5.03075e-2 | +3.35383e-2 |
| Dirac (UD; GL(4,10)) | +2.164325e-2 | -7.36324e-2 | +9.52756e-2 |
| vector (VWa) | -4.537562e-2 | -3.84392e-1 | +3.39017e-1 |
| **totals** | **-0.124611** | **-6.470665** | **+6.346054** |

- Totals by species (Hess): scalars -0.0671, Dirac +0.4870, vectors -0.5445.
- The photon's VW vertex bubble (-0.3844) is 2.8x its band-level SF bubble (-0.1361). So its H4 seagull is not the band-level flow seagull (+0.0908). That is a statement about H4, not a defect computed here (reading).
- Needed for lambda_nn = 0: seagull +6.4707. Actual: +6.3461.

### 3.3 (b) lambda_nn total, convergence, and completion dependence (checked; `lnn_totals.out`)
- **Bare SF: lambda_nn = -0.12461 +- 1e-5.** Dirac GL(3,8) vs (4,10) moves 4e-7 per field (x22.5 = 9e-6); separable parts converged to 1e-7. 4 lambda_nn = -0.498 vs bubble -25.883: **ratio 0.0193**.
- **One-point data:** e0 = -29.998, tau = -0.6113 (SF), W = e0 + 2 tau = -31.22. At a point with a nonzero one-point function a reparametrization h -> h + O(h^2) shifts the Hessian by tadpole x (second-order coefficient) (proved, one line). So the counterterm completion matters:

| completion of the one-point counterterms (O(h^2) part) | lambda_nn | ratio to bubble |
|---|---|---|
| A: all exactly linear in h_SF (bare SF value) | -0.125 | 0.019 |
| B: (S) = -e0 sqrt g with SF's exponential map (sqrt g = e^{-tr h/2}); P-Tad linear in h_SF | +7.375 | 1.14 |
| C: all linear in h_lin (g_ij = delta + h; h_SF = -h + h^2/2 + ...) | -0.736 | 0.114 |
| D: (S) = -e0 sqrt g in h_lin; P-Tad linear in h_lin | -8.236 | 1.27 |

- Fluid control (E = e0 sqrt g): B and D give 0, A gives e0/4, C gives -e0/4 (proved). So only B and D are covariant CC completions; their difference is W/2.
- No registered text fixes which (reading): P-Tad is "c_h int h_ii (stipulated)" (`C5_R17-4_report.md:194-197`), and (S) "enters as -e0 sqrt g" (`C5_R19-15_report.md:185-188`), neither with a stated map from R9-9's h to the metric at O(h^2).

### 3.4 (c) Which completions set it to zero
- **(S\*)** removes the whole lowest-state uniform-static potential at every order (`C5_R19-15_report.md:213-222`; verdict item 4). By H4 that is the full degree-0 kernel, so lambda_nn = 0 exactly in every parametrization (proved, definitional). It leaves kappa, c4, X (degree 2).
- **(Sigma)** implies (S\*) (`C5_R19-20_report.md:119`) and also removes T2[Pi_vac] (degree 0 and 2), replaced by Z E_EH (`:101-107`). Ward-exact degree-0 kernels number 0 (`:171`; Lemma E, `TESTS:8485,8568`). So lambda_nn = 0, and kappa = c4 = X = 0 (proved, definitional).
- **Not forcing:** P-Tad (linear: no O(h^2) part in A; its O(h^2) part is the unfixed datum above); (S) (shifts by -e0/4 in B, not to 0); (d-i), N_red, W1-weight (isotropic one-point clauses; they only shift the one-point data; no zero identity) (suggested, by R19-15's isotropy argument `C5_R19-15_report.md:183-209`).

### 3.5 (d) face1 under each reading
- **A-D (lambda_nn != 0):** Theorem Q (`C5_R19-29_report.md:144-157`) gives Schur/s^2 = kappa^2 s^2/(4 lambda_nn + (c4 + 8X)s^2). With c4 + 8X = -1.523 (R19-29 N = 128), there is no pole for A, C, D (same signs), and B's crossing is at s*^2 = 19.4, outside the zone. So **FACE1-HOLDS**: (w_d, w_o) = (-1.1716, -0.1954) unchanged (checked arithmetic; Theorem Q unrefereed).
- **(S\*) alone:** lambda_nn = 0 with kappa = -1.28: R19-29's shifted branch, w_d = +0.753, w_o unchanged, det -3.62 (R19-29 worker numbers, not recomputed).
- **(Sigma):** no shift. The raw face1 row and kappa are both removed, so the face1 coefficient is 0 by construction and the own-direction payment is unneeded. The Schur remainder is O(s^2) relative if the residual degree-4 gauge block is nondegenerate (suggested; not computed).

## 4. Against the FIXED readings (`TESTS:8808-8811`)
| reading | status |
|---|---|
| LNN-NONZERO | **not met.** lambda_nn = -0.1246 != 0 under the bare SF law (checked), but **0.019 x bubble < 0.1** (fails); and (S\*)/(Sigma) force it to zero (fails clause 2). In completions B-D the size clause would pass (0.11-1.27) |
| **LNN-ZERO-FORCED** | **met on the letter: (S\*) (P-R19-15a) and (Sigma) (R19-20)** force lambda_nn = 0 (proved, definitional). face1 shifts only under (S\*) alone (w_d = +0.753, R19-29). Under (Sigma) it does not shift; it is paid by construction |
| OPEN | not needed for the literal reading; the bare value's completion dependence is an OPEN registration gap |

**Worker reading: LNN-ZERO-FORCED** (naming (S\*) and (Sigma)), with the bare-law value lambda_nn = -0.1246 (SF, completion A) recorded as nonzero but sub-threshold and completion-dependent.

**Against the expectation (`TESTS:8812-8814`).**
- "LNN-NONZERO under the bare law": nonzero yes, size no (1.9%), from a Dirac-photon near-cancellation.
- "LNN-ZERO-FORCED under (Sigma)": yes.
- "face1 in R19-29's shifted branch whenever (Sigma) is adopted": **no.** (Sigma) also removes kappa; the shifted branch belongs to (S\*) alone. Count once with R19-29 section 3.6.

## 5. Prices (named, not adopted)
- **P-R19-35a (new, registration gap): the O(h^2) completion of the one-point counterterms** (P-Tad's map h -> metric; (S)'s sqrt g parametrization). It moves lambda_nn by O(e0/4) ~ 7.5. Gates `AX:85-90,114-130,187`.
- P-R19-29a (lambda_nn != 0) is met in every completion tried (A-D), but in A only at 1.9% of the bubble.
- No axiom text touched.

## 6. Strong-word check
- **"Proved"**: Lemma R1 (one IBP; needs periodic smooth p, met by all three root bands); the reparametrization shift; the fluid control; (S\*)/(Sigma) zeroing (definitional, given H4). All unrefereed.
- **"Checked"**: every number in the tables, at the stated quadratures. Archived mu rows reproduced to all printed digits.
- **"Exactly zero"** under (S\*)/(Sigma) holds by construction, for the lowest state only.
- **Not claimed:** H4 itself for the photon (its vertex bubble differs from the band-level one); any completion choice as the right one; R19-29's Theorem Q or its lambda_nn = 0 numbers (worker, unrefereed); two loops; the m = 0.001 root.

## 7. For the referee
1. Lemma R1 and its sign rule (bosons negative, Dirac sea positive).
2. Whether the FIXED size clause is meaningful at a point with e0 = -30: the A-D table shows lambda_nn is parametrization-dependent at O(e0).
3. Which O(h^2) completion route A registers (B is my best reading of "(S) enters as -e0 sqrt g" with SF's exponential map).
4. The photon H4 seagull (+0.339 per vector, vs band-level +0.091).

## 8. Files (`S/scripts/`)
- `lnn_fast.py` -> `lnn_N96.out` (3D grid: scalar/Dirac checks; photon grid NOT converged, superseded), `lnn_dirac_GL410.out` (Dirac GL(4,10)).
- `lnn_laplace.py` -> `lnn_laplace.out`, `sep_lap.npy` (separable bands, Laplace).
- `lnn_totals.py` -> `lnn_totals.out` (totals, split, completions A-D, crossover).
- Unmodified archives: `arch18/`, `arch17_4/`, `r1929/`; `root_refR18-9.npy`.
