lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-02T03:16Z

# Gate: Codex repairs (repair-gate, item 8c), mapped side

Provenance: anthropic/claude-opus-5-5, effort high, commit 105283f2c, side mapped, Mac mini worker. All four notes were written by openai/gpt-6-astra, so this read is cross-provider, but it is one reader's check and not an audit. A same-model check would not be independent in model; no such check was run here. Verdicts steer research and grant no status. Nothing was committed or pushed.

**Short version.** All four notes stand at the level of their steps. The counterexample makes (CI-paid^𝔡) WRONG as printed at this commit, and (W2) loses its proof, though not its statement. A cheap trim that removes only frozen plaquettes is also false (D1). One sentence on weights in the finite-range note is false, with a local repair (D2). The half-unit shift works, but it now competes with a different rule already in `library/quiet-boundary-rarity.md` (D3).

## Verdicts

`Q` is `library/quiet-boundary-rarity.md`.

| Statement | Verdict | Note |
|---|---|---|
| **`excess-finite-range-repair.md`** | | |
| Scalar diagnostic, section 1 | ADVANCE | Exact. R3c now shows the same failure on the actual lift, within its limits, below. |
| (FR): range, D(MB) = I at flat fields, row sum, quadratic m | ADVANCE | First order re-derived by hand, including the anchor term T_0 lambda(y') against the contour difference. R2 agrees. |
| (INV), K_q, (MOM) | ADVANCE | The enlarged a does absorb the q^floor mismatch between neighbouring sites. The moments are uniform after q_* exp(nu_0 R) < 1. |
| (J), (T1-r), (T2-r), (T3-r) | ADVANCE | P_a inside W^+ is what lets (J) apply after local enlargement. The constants on leading terms are absolute. |
| Flux bootstrap, (TOP-tr) at W = 1 | ADVANCE | Recurrences re-derived; C_7 closes for f <= f_1(L). |
| Weighted trial estimate, line 101, and W^+ for down-averaged weights, line 56 | CORRECT-NO-ADVANCE | False as written, D2. The estimate survives by the local repair given there. |
| (CLASS) | ADVANCE | Stale constants, D5. |
| TOP-1 | Implication, unchanged | Reads item (o), not checked here. |
| Section 5, (H-W) as a gap | Agreed | A true gap, honestly stated. |
| **`excess-root-frame-repair.md`** | | |
| Diagnostic, (VP), (VP-W), fine endpoint | ADVANCE | |
| (ROOT), (FC), (ROOT-W) | ADVANCE | The three error terms and the weight exponents re-derived. This answers finding 1 of `gates/excess-codex-6c0d4e1c9.md`. |
| One-level contour gauge, section 4 | ADVANCE | Matches `block-poincare-energy-package.md`, Theorem 7 Step 1. C_j = 1 at t = 0. |
| (G), (D-r), the five groups of R-double-dot | ADVANCE | Identity re-derived with its signs; every Holder pairing dominates W. |
| Section 5, gradients from variances | ADVANCE | At the level the note writes it. The differentiated TL was read, not expanded term by term. |
| Lemma EX2-r | ADVANCE as an implication | A1-r to A4-r are open, and A4-r rests on the TOP-W gap. Nothing about the AN3 curve follows yet. |
| **`paid-inputs-frozen-energy.md`** | | |
| Necessary test, identity parent, quiet minimiser, nested packing | ADVANCE | Sections 1 to 4 checked against Q:19-23, 39-45, 243-247 and the relative-density definitions. R1 agrees on the parent. |
| (CI-paid^𝔡), Q:245, as printed at this commit | **WRONG** | D1. Not just a proposal now: Q has adopted it, and (W2) reads it at Q:235. |
| Section 5, gaps (QT^d), fixed-link RF | Agreed | True gaps. D1 narrows the repair. |
| **`paid-inputs-frozen-mesh.md`** | | |
| Literal (FG) fails | ADVANCE | Agrees with `gates/fill-cubical-a7ff7835d.md`, D1. |
| (G2), the vertex mesh, fill under (G3) and Theorem S | ADVANCE as an implication | Rectangular sides in [n, 2 n] are what Theorem S asks. D3 on which rule applies. |

## Defects, ranked by what each breaks

**D1. (CI-paid^𝔡) is false as printed, and the cheapest repair is false too.** This breaks the first inequality of (W2) at Q:235 and the frozen-data proof at Q:247. It does not break the conclusion of (W2): in the counterexample there are no rough cells, so Delta = 0 and (W2) reads 0 >= 0.

- *The failure is generic.* It is not a special field. Q:23 puts Dev_b at about t_0^4/x for typical data, so ordinary frozen data lock positive action in every fine brick. Take U a constrained minimiser. A level-(i - 1) cell holding enough fine bricks then has energy above kappa T^2, and the inequality fails with V_i class and N_ref empty.
- *Trimming frozen plaquettes alone fails.* Note line 34 leaves open "the action in the portion left free by the layers". Put the same copy one level up: at level 1, in Sigma_1, in the part of the row more than t_0/4 from the wall h_1, so clear of the parents of Sigma_0. Its abelian lift by T_1, with the block gauge, is exact, has range 4 L, and leaves Sigma_0 at identity, so a class chain exists. Parents are identity by section 2 of the note, and Dev = 12 a^2. For any fine field in that fibre, LE and Lemma K(b) give |theta'|^2 <= (1 + o(1)) times the fine energy on the support of chi_y, and those fine plaquettes are free at level 0, since the row lies below Sigma_0. So the minimiser has positive free action on these copies, and enough copies put a level-(i - 1) cell above kappa T^2. The action is still immovable, because it is forced by frozen level-1 bonds. Level of this bullet: a hand proof in this gate, unread by anyone else.
- *Repair, unproved.* Replace Z_{i-1}(U) by Z^max: over all j <= i - 1, the free level-j cells with energy above kappa T^2 whose parent is frozen, or with j = i - 1. These maximal free cells are disjoint. A rough cell is free at its own level, because quiet bricks have flux at most T/2, so it lies under exactly one of them. By clearance a free cell has no lower frozen layer under it. A maximal cell under a quiet frozen parent inherits energy of order eps_q^2 T^2/L^4, below kappa T^2, so both counterexamples give empty Z^max. Still to prove: Lemma TE cell by cell at mixed levels, and (QT^d) with the fixed-link RF.

**D2. Down-averaged orientation weights have no local rate.** This breaks line 56 ("with the local rate at that level"), line 101 ("exp(C sum_m nu L^-m)"), the matching sentence in Lemma LIFT in `parts/hard-core--excess.md`, and its "product of exp(C nu L^-m)" in Section 2.3. Concrete failure: a transverse direction is a box, so W_j^q there is piecewise constant, with a jump e^nu at each top-block face at every level. The tent orientation at the same site differs from it by up to nu. R4 gives rho(m) = 0.1000 = nu at every depth, for L = 3, 5, 7, with about 89 percent of sites above nu/10. So W^+/W is about e^{c nu} on most sites at each level, and the product over levels is not bounded.

*Repair, unproved but short.* Run T3-r with the scalar interpolated profile W-tilde_j, which has rate nu s_j per level-j cell, using W-tilde_j <= exp(C nu s_{j+1}) (W-tilde_{j+1})^down and W-tilde^+ <= exp(C nu s_j) W-tilde. The product is then bounded. Compare with the telescoped orientation weights W_j once, at a cost of one factor exp(C nu). COMP-g is unaffected: it reads a uniform W^+ <= C_w W, which is true.

**D3. Two frozen-brick rules at this commit, with different costs.** Q:53 has a copy rule (mesh below the dual wall). The note has a half-unit shift (mesh above it) plus (G3). They are mirror images: each leaves a strip inside a mesh cell on one side of the frozen plane. `parts/hard-core--paid-inputs.md` still says the reference is not adopted, which is stale here. The difference that matters: the copy rule reads the frozen mask, as Q:53 says, while `threshold-paid-reference.md:79-80` says P does not depend on a later stopping layer. The two statements cannot both stand. The half-unit mesh with (G3) keeps P a function of V alone.

*Recommendation, unproved.* Keep the half-unit mesh and add (G3) to the quiet test. A brick failing only (G3) has a plaquette above 2 T in its one-cell collar, so that plaquette is in Y and R, and the brick can be charged there with bounded multiplicity, as Q:235 charges marks whose patch meets a hull.

**D4. t_0 at Q:39 does not include 8 n.** The formula is max(8 L, 4 r_S, 3 R_loc, C L log(1/T)), while the mesh needs t_0 >= 8 n, with n about (8 pi/T)^(1/2). That is a power of 1/T against a log. Q:53 and Q:247 say so in passing, but the definition does not. Local: add the term. I saw no consumer that breaks, but I did not trace them all.

**D5. Stale constants in (CLASS).** It is written with C_p C_a, and Q drops C_p. At this commit T_2 = b_2 T with b_2 absolute, so (CLASS) reads C_7 b_2/L^2 <= 1. That helps: the ratio is absolute and fixed before L, which removes the note's "if they depend on L" caveat.

**Remark, not a defect.** The note's reflection argument for the identity parent is correct but more than is needed. Block weights are uniform in the transverse coordinate, so a pair of opposite links at any two transverse positions in a block cancels. R1's off-centre pair gives 1e-18.

## Numerics

`checks/gate_rg/`, criteria in `CRITERIA.md` written first, except the three entries marked as declared after the first runs. Memory was 68 percent free at the start and 66 percent at the end of the longest run. One job at a time under the numeric lock, since released. R3 used three amplitudes and R3c four.

| Check | Result |
|---|---|
| R1a, b, c: parent of the copy, L = 5, 7, four axis orders, 12 plaquettes, action | PASS. Parent at most 3e-19 |
| R1d: controls | **FAIL as registered**, on one clause. One link and equal signs behave as required (6e-3 to 2e-2). The off-centre pair gave 1e-18 where I registered above 1e-3. My expectation was wrong, see the Remark. Its log line and the script's summary line say FAIL, and I did not rerun it. |
| R2a, b: D(MB) = I at V = 1, at pure gauge, on gauge directions, d = 2, 3, 4 | PASS. Errors at most 2e-8. Control with no block gauge: 0.22 to 0.83 |
| R2c: row sum over f, d = 2, L = 3 | PASS. 0.059, 0.057, 0.056 at f = 0.083, 0.040, 0.020 |
| R2d: range, Np = 12 | Largest distance with block norm above 1e-8 is 3, far below 68. First run crashed on a script bug, rerun as `r2d_range.py`. It cannot test distances above 6 on this torus. |
| R3: exact right inverse, f = 0.106 to 0.028 | PASS. Picard 4 steps, residual below 1e-13, max\|Y\|/f^2 = 0.0076 to 0.0080 |
| R3c, declared after R3: tail powers | p = 2.1 up to the end of the support of m (shell 5), then **3.1 at shell 6 and 4.1 at shell 7**: p = 2 + s. The old tail asks 2 + 2 s, that is 4 and 6. |
| R4: weights | Claim refuted at every L, D2. Control PASS |

*What these do and do not establish.* R1 settles the parent for the comb map exactly as far as floating point goes, at four fixed axis orders. The mapped map averages over orders, and on this abelian field that average is linear, so it follows. R2 and R3 are d = 2 and 3 at L = 3 for the most part, on smooth fields, with kernels truncated by the code's window. They test (FR) and (INV); they prove nothing at large L, and no constant is evaluated. R3c is indicative only, on one field, but it goes further than finding 2 of `gates/excess-codex-6c0d4e1c9.md`, which offered a scalar diagnostic only: the old tail fails on this actual lift.

## Read and not read

Read whole: `FINISH.md`, `GOAL.md`, the four notes, `parts/hard-core--paid-inputs.md`, `library/threshold-paid-reference.md`, `gates/excess-codex-6c0d4e1c9.md`, `checks/excess/v10_lift_su2.py`.

Read in part: `parts/hard-core--excess.md` lines 1-60, 144-350, 363-482; `library/relative-density-bound.md` 215-304; Q at 15-60 (long lines cut, so the junction paragraph was only partly seen), 225, 235, 243-247; `library/fill-cubical-extension.md` 294-409; `library/fibre-propagator.md` 118, 132-140; `library/block-poincare-energy-package.md` 59-73; `parts/hard-core--mapped.md` Text 3.1 and 5.1-5.2; `checks/gate_ex/ex_core.py`; `gates/fill-cubical-a7ff7835d.md` opening; `gates/theorem-dm5-codex-3272ed4f2.md` lines 15, 23, 39.

Taken from earlier gates, not re-derived: (K), Lemma LE, Lemma TL, Theorem S. Not checked: item (o), Lemma TE, Lemma ST, Lemma RF, and whether A1-r to A4-r hold for any curve; A1-r and A2-r only had a scale count. `paid-inputs-junction-response.md` is outside this item and was not read.

Firewall: not opened `parts/hard-core--independent*.md`, any gate on that attempt, `gates/history-budget-*`, or the Sussman-Alpoge repository. The file listing of `gates/` showed their names only.
