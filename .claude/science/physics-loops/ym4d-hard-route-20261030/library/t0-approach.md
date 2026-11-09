lead: anthropic/claude-fable-5-2/high mac-mini-worker
lease_until: 2026-11-10T08:30Z

# t0-approach: proof approach for T0 against the current YM4_1400 frontier

Queue row 608. Pinned at commit 03cf39bee. Approach and skeleton work; no status. In progress: sections are written as they are finished.

Provenance: one session of Claude Fable 5.2 (high), worker on the Mac mini. No other model checked this file. No numeric job was run; all work is by reading.

Credit: the text under study is Sussman and Alpoge's YM4_1400 and its overview (their texts name Claude and Codex as authors). The method they follow and extend is Balaban's (CMP 95-122). This file proves nothing new.

Sources, with how each was read:

- Y = `YM4_1400.tex`, 136,637 lines, fetched from the row's URL at their commit 2bc0658f into my scratch folder. "Y 4152" means line 4152. I read by `grep -n` and `sed -n` ranges only.
- OV = their overview `YM4/YM4_assembly_overview.pdf` at their commit 3ac0bf4f2973 (24 pages; the file at 2bc0658f is a one-page diagram). Read in full.
- Balaban: the PDFs and OCR text in `~/ym4d-papers`. Page numbers are journal pages.
- `library/prior/sa-boxes.md` does not exist at commit 03cf39bee. The line map below is mine.
- NOT READ: anything in Y outside the ranges cited below. The rule "printed page p is near line 98p" is rough; I located passages by label.

## Part 1. The frontier: what their text leaves open

### 1.0 The top-level reduction (new against CA-I)

Their Theorem 0 (Y 156-164) is conditional: "Assume the uniform renormalization and short-distance estimates stated below." It now asserts the OS axioms, a Wightman theory, positive energy and a unique vacuum in every canonical component. The precise statements are `thm:continuum-main` (Y 1748), `thm:phase-main` (Y 1884) and `thm:reconstruction-main` (Y 122703, statement NOT READ).

The catalogue says which inputs carry the scalar route:

- Y 1978-1986 of the catalogue head (Y 1962-1986 region): "the scalar route requires only its ordinary D1 and ultraviolet premises, together with the consequences derived from them." The joint induction A-C and the flow section must construct the data for D1.
- H3 (Y 3013-3016): "Actual D1, F2--F3 and the existence of the admissible data supplying these hypotheses remain the model requirements."
- H4 (Y 3044-3049): "Actual verification of D1 and of the interacting short-distance law is not supplied here."
- G1 (Y 2794-2804, finite-lattice symmetries and reflection positivity at all mirrors), G3 (Y 2861-2910, plateau law), G4 (Y 2912-2943, all-state moments from D1), H1 (Y 2949-2969, diagonal-flat extension from D2), H2 (Y 2976-2991) and H3 are stated as proved or derived there. I did not read their proofs (NOT READ: Y 96000-122700 except the ranges cited below).
- G2 (Y 2806-2859), full O(4): "This proves G2 conditionally for this state class, using either supplier of (TU18)." TU18 is `t^8 Gamma_phi(t) -> 0` (Y 112885). Supplier 1 is the upper bound TU10 (Y 112711-112716): `0 <= S_2(f,h) <= u(d) |f|_inf |h|_inf` with `u(d) -> 0`, on the shape class with `theta_* = 1/12000`. Supplier 2 is `sec:angular-mirror-budget` (Y 112897 ff.), which uses D1 at every first-passage stop with stability-plus-floor constants bounded by `C(1 + log x)` (Y 113012-113022).
- The far-shell flux (Ward) route for rotations is now separate and is not needed: "The angular proof does not establish those separate comparison estimates" (Y 2857-2859). So the CA-I wall "flux hypothesis derived nowhere" is replaced by TU18.
- Clustering and the unique vacuum per component are `thm:phase-main` (3)(iii)-(iv) (Y 1900-1912), from G3 and G4.
- F4 (Y 2758-2766): the result is a scalar `tr(F^2)` theory. "A nonzero scalar Wightman field alone does not provide this identification." T0 as GOAL.md states it is this scalar sector, so F4 is outside T0.

Consequence for T0. Three inputs remain, in their own words:

1. **D1** (Y 2358-2428), the ordinary localized source bound and stability, uniform in cutoff, torus and first-passage stop. It needs the joint induction (A1-A4, B1-B4, C1-C4, which is H_step) and the flow E1.
2. **TU10 or the mirror budget**, for O(4). The mirror budget is D1 again, at all stops. So O(4) costs no new analytic input beyond D1 with the logarithmic constant.
3. **F2-F3** (Y 2585-2640, 2685-2699), only for "non-trivial": F2 with `|r| <= 1/2` gives a nonzero two-point limit "by a closed lower bound" (Y 2698-2699).

E2, E3 and E4 (tuning, matched cutoffs, calibration; Y 2504-2543) are not on the scalar route (Y 1982-1986: "Weighted and matched-run comparisons and typed Ward estimates remain requirements for the stronger statements that invoke them").

### 1.1 The open inputs, one row each

Each row gives their line, their statement (short quote or exact paraphrase), and the root it belongs to (roots are in 1.2).

| # | Input | Line | Their statement of what is open | Root |
|---|---|---|---|---|
| 1 | H_step | Y 4152-4180 | "Retain the background and substitution admission in A1--A4 ... and the actual matrix/core, potential and window estimates"; retain `hi:pair-sup-envelope`, `hi:reference-gaussian-integral`, `hi:event-energy`; in the sourced case `hi:source-excess-budget`. "Any primitive estimate not yet verified for all actual histories remains a technical hypothesis." "A homogeneous regular-sector construction alone does not verify the all-history premises in H_step." | all of R1-R6 |
| 2 | A1, critical orbit | Y 1966-1989 | Existence and uniqueness of the regular critical orbit for every allowed nested family and every regular coarse datum. Proved: first step, homogeneous comb. Open: "the actual restrictions and substitutions must remain in their prescribed pair cores"; the pivot chart does "not imply existence, uniformity or all-substitution room for the many-level critical orbit." | R1, R2 |
| 3 | NB box | Y 44166-44174; Y 34889-34892; Y 3318-3321; OV p. 19 | The homogeneous curvature atlas (Y 44112-44145) "does not construct a mixed-scale proper trial, an independent-current history core, or a positive conditional measure." The nonstationary-trial theorem (Y 34919-34948) needs a real fine trial with small curvature, current and defect; "It does not supply a fine trial for every proposed curvature-only mixed datum." | R1 |
| 4 | A2, coercivity | Y 2059-2063, 2069-2070 | "Signed profiles, counterterm-modified precisions and interacting Hessians require their own comparisons on the joint history cores." "Verifying that every actual background and history substitution lies in this class remains necessary." | R2, R4 |
| 5 | A3, inverse and response | Y 2114-2116, 2138-2141 | "Each application must still verify that its actual history data, complete determining reads and substitution lie in the stated domains with the required radius margins." | R2 |
| 6 | A4, restriction | Y 2146-2172 | The restriction identity holds "under this admission and regular critical uniqueness"; other changes of averaging scheme "still need the stated physical and complex-domain intertwining estimates." | R1, R2 |
| 7 | B1, B4 tails | Y 2176-2200, 2264-2300 | "Their verification for the actual complex interacting matrices and all allowed cores remains necessary"; "Actual nonlinear background/core inclusions and history formation remain to be verified." | R2, R3 |
| 8 | `hi:read-coverage` | Y 77493-77524 | Every later read lies in `U_i(X~)` and in `K^#(omega_X, xi_X)`, "for every admissible later history and every configuration on its carried support. It is a pointwise statement." The geometric part is proved. "Admission of the resulting background to the analytic core, and the actual matrix bounds ... are the remaining analytic part of coverage." | R2 |
| 9 | `hi:pair-sup-envelope` | Y 73357-73371 | `sup_p |e^{Phi_omega(xi;p)}| <= e^{Phi°_omega(xi) + C_V N_0(omega)}` if `sup_z |V_X(xi;z)| <= C_V N_0(omega)`. "All representatives in the supremum must obey the same bound ... Proving the complete localized bound on V_X is an analytic formation task." | R3 |
| 10 | `hi:reference-gaussian-integral` | Y 74940-74966 | With a triangular chart `A_j = F_j(b_j; b_{j+1},...,U)`, inverse Jacobian `<= J_0^{d_j}`, and unspent forms `>= beta sum |A_j|^2`: the reference integral is `<= e^{C_5 V°}`. "The actual stored-coordinate identity or its explicitly bounded chart Jacobian is required; the mere use of the symbol A_j does not provide it." | R4 |
| 11 | `hi:event-energy` | Y 76720-76752 | Five conditions on every carried support and every argument of the supremum: exact exponent identity; `|V_X| <= C_V N_0`; real admissible reads; normalizer, kept-form coercivity and reference domination; disjoint ownership `A + sum theta_j G_j + beta_1 sum |A_j|^2 >= sum_e Gamma_e`. "For a drop-out the inequality must hold for every compatible real evaluation in its fibre." Y 76940-76960: the exponent arithmetic "does not establish the witness certificates or their ownership." | R3, R4, R5 |
| 12 | `hi:one-zone-test` | Y 77392-77404 | `|Psi_omega(z)| <= C |z| p_n n^#(omega)` for `|z| < r_n`, "and all its fields remain in the same admitted domains." "The coefficient C must be uniform in the histories, stored fields, levels, zones and allowed reads. A bound for one chosen background or a source function before it is formed is not (hi:one-zone-test)." | R6, R2 |
| 13 | B box | OV p. 19; Y 77493-77524 | "the actual retained-operation domains, common integrable majorants in stored coordinates, and history admission"; "A fixed-chart logarithm bound alone is insufficient." | R2, R3, R4 |
| 14 | LF box | OV p. 19 | "domains, stored-coordinate majorants and witness matching"; "The conditional component inequalities alone do not complete the stated R-operation theorem." | R2, R4, R5 |
| 15 | RS box | Y 83632, 83640-83655, 83670; Y 84048-84072; Y 84108-84115; Y 84202-84204; OV p. 19 | "Old-family amplitude estimates have to hold on this actual map and its declared joint complex domains." "Their general polynomial age factors do not automatically give the exact exponent 3/2 in (RF17). One must either verify that sharper estimate or allocate a smaller positive exponential rate." The rim count `sum_j #_j(Z_j^+) <= C sum_n #_n(Gamma_n)` "is an actual window/history count and is not proved by a local Cauchy estimate." The extraction order `E, b_j, x_j, R` "is an input to the full interacting construction." | R2, R7 |
| 16 | RC box, coefficient | Y 83250-83321; Y 83284-83292; OV p. 19 | B3: `|sum_{l<=k} b_l^0 - k c_0| <= c_2`, `c_0 = 11 N^2 log L/(12 pi^2)`. Proved on the homogeneous physical background (Y 83351-83500: coefficient preservation, `mlc:main`, `mrc`). Open: "The complex-current localization requirements in (RF9) remain separate"; the gap, continuation and walk expansion of `A_Y` "are part of this Gaussian-localization input." | R8 |
| 17 | RC box, vacuum | Y 86270-86313 | "The determinant estimates and first-step sign in (RF61) remain actual Gaussian targets." RF62: `|E + (3/2)(N^2-1)(L^4-1) sum_j (log x_j) N_{j+1}| <= C N_0`, "not proved merely by naming a field-independent constant." | R8 |
| 18 | E1, flow | Y 2492-2500; Y 2742-2755 | `b_i <= B_#` and `lambda(j-i) - C <= x_i - x_j <= B_#(j-i)`; "What remains for the interacting flow is to identify and estimate the literal formed coefficients and their admitted overlap domains." | R7, R8 |
| 19 | D1 | Y 2358-2428 | Holomorphic point counterterms, localized source energies with `e^{-kappa m(X)}`, upper stability and partition-function floor, uniform in cutoff and torus. Open: "identify the literal stored-coordinate operation and its fixed reference measure, admit every later read to the same core, prove the complete quadratic domination and localized energy envelope, and construct owned witnesses for the failed tests." | R2-R6 |
| 20 | CP box = F2, F3 | Y 2585-2640; Y 2685-2699; Y 100377-100385; Y 102732-102825; Y 105536-105549 | F2: `S^T_2 = C_G zeta^2 g^4 K(f,h)(1 + r)`, `|r| <= 1/2`, in every periodic Gibbs state. Open: "the literal identity in (CL2), with the actual exterior sigma-field, domain, numerator and normalizer"; the force bound CL5; the common-reference mean comparison CL19; marked bad moments. `prop:short-distance-7-1` is a "proof-outline conclusion conditional on that remaining package." | R9 |

RT box (the R-operation and T-operation theorem, OV "Complete, assuming inputs") is not a separate row: its inputs are rows 9-14.

### 1.2 Merged roots

Nine roots carry all twenty rows.

- **R1, TRIAL.** For every proper mixed-scale regular coarse datum there is a fine regular trial (small curvature, small current, small defect) to which the nonstationary-trial theorem applies. Rows 2, 3, 6.
- **R2, ADMISSION.** Every actual read, substitution and background that the history sum produces lies in the analytic cores (regular-pair domains) with the stated radius margins. Rows 1, 2, 4-8, 12-15, 19. This is the largest root. It is our I-ENTRY-MATCH item (FINISH rows 605-606).
- **R3, POTENTIAL.** The localized bound `|V_X| <= C_V N_0(omega)` for every representative in the supremum. Rows 7, 9, 11, 13.
- **R4, REFERENCE.** The stored-coordinate reference measure: the triangular chart with bounded Jacobian, and coercivity of the kept forms on the actual joint core. Rows 4, 10, 11, 13, 14.
- **R5, WITNESS.** Owned, disjoint witness energies for every failed test, valid on the whole fibre of a drop-out. Rows 11, 14.
- **R6, SOURCE.** The one-zone source bound, uniform in history, level, zone and read. Rows 12, 19.
- **R7, AGE.** The one-step comparison with the summable age factor of RF17, and the window count for the rims. Rows 15, 18.
- **R8, COEFFICIENT.** The Gaussian coefficient on actual constrained backgrounds with complex current (RF9, RF10), and the vacuum determinants (RF61, RF62). Rows 16-18.
- **R9, CONDITIONAL LAW.** F2-F3: the identity CL2 and its force, boundary, mean and bad-moment errors. Row 20.

Shared structure. R2 is a precondition of R3-R7: each of those estimates is stated "on the actual core". R3, R4 and R5 are the three conjuncts of `hi:event-energy`. R6 is R3 with a source. So the order inside H_step is R1 -> R2 -> {R3, R4, R5} -> R6, with R7 and R8 feeding the flow E1, and R9 standing apart.
