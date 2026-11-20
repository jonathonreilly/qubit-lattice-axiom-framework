lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-21T04:33Z

# gap-mini-solve-aw-opus: mass gap for 4D SU(2) Yang-Mills (row 1299)

Started 2026-11-20T16:33Z (date -u). Worker: Mac mini Claude worker 2, Claude Opus 5.5 max. Pinned at commit 30dae6625 on branch claude/ym4d-hard-route.

Status labels: PROVED, ARGUED, GUIDE, OPEN.

## Step 0. Record read (statements about the record, not evidence; written 2026-11-20T16:40Z by date -u)

Read at pin 30dae6625: `GOAL.md` in full; `FINISH.md` L1-90, L299-357 and this row (L1380); the RESULT segments of rows
1250-1304; `parts/gap.md` L1-104; `library/prior/gap-onebound-read-sol.md` (row 1218) in full; Steps 0-1 and 4-5 of
`library/gap-mini-solve-at-opus.md` (row 1294); Step 1 of `library/gap-mini-solve-av-opus.md` (row 1296, running);
row 1259's Lemma CD and Corollaries CD1-CD2 (`library/gap-mini-solve-ah-opus.md` L95-170); row 1268's statement of
(E0)-(E6) (`library/gap-mini-solve-al-opus.md`, located by grep).

What the record fixes (pointers only):
1. Modulo the ultraviolet carry, the gap clause reads one lattice input at one physical size, (N-phys) (row 1161), or a
   seed at one coupling in the window: a uniform cube gap plus the count (TR) (rows 720, 1259). Every engine on file is
   blind; the one selective proved fact, asymptotic freedom at small coupling, has no carrier through the band
   (`parts/gap.md`, "Hardest open obligation"). Rows 1277-1294 all leave the seed OPEN; rows 1301-1304 (running) work
   the owner's tiling and positivity directions on it.
2. The one-cutoff carry on the pin route (rows 1256-1294, mostly Mac mini worker 2) is reduced to named inputs. Open at
   this pin (row 1294 Step 5, check 1288): (CE) and the margin reading (M); the cut half (E0)-(E6) of (FC-1);
   `9.1:prop-blind-site-expansions` (Proof outstanding in the account, CA-III L16558-16560); (V9) and (DET)'s
   normalisation (row 1296 holds (V9), running); the account's premises; the seed.
3. Balaban's CMP 116 is not in the owner's paper folder and Project Euclid gives a bot check (rows 1264, 1294). Row
   1294 Step 5 notes that the account prints its own expansion machine with one-term bounds and holomorphy for the
   large-field stages (CA-I 4.22, L80618-80700; 4.24, L108354-108610) and cites CMP 116 only for the regular step
   (CA-I L58700-58760), and that applying the printed machine to the regular step "is possible in principle ... but was
   not checked here".
4. Published work (row 1218): Bhattacharjee et al.'s thermal ascent is conditional on its own one-scale seed; their
   Corollary 166 is a blind weak-coupling statement on coarse straight-path variables; Zeng's routes are conditional.
   None supplies the seed.

## Step 1. How best to attack it (judgement, ARGUED; written 2026-11-20T16:41Z by date -u)

**The seed.** Modulo the carry, the problem is a lattice statement at order-one coupling (SU(2) Wilson near
beta = 2.4, correlation length a few lattice spacings) on a box of many correlation lengths: a uniform cube gap plus
the count (TR). Any proof needs a selective step at order-one coupling that fails for compact U(1), the free photon,
products with a massless factor and frozen finite groups (`parts/gap.md`, test table). The candidates I could name
before reading the tables (sharpness via OSSS, Ginibre/character positivity, centre-vortex comparison with Z_2,
analyticity in beta, Lee-Yang, chessboard Peierls for disorder, uniform gap implies (TR) via additivity of excitation
energies, Langevin/Bakry-Emery on the orbit space, valley tilings) are on file with a first failing step (rows 998,
1084, 1229, 1237, 1259, 1273-1292, and the screen of row 1296 Step 1). Rows 1301-1304 work the owner's tiling and
positivity directions now. Row 998 9.5 rules another screen by this model family a waste. Verdict: no route to the
seed off the record; I do not attack it, and nothing below counts as progress on it.

**What I do instead.** Only closures count. The unowned carry input that sources on hand can decide is the regular
(all-small-field) step's expansion: (CE) of row 1294 (the input of Proposition HAN, hence of Theorem PE and Corollary
FC-s, the smooth half) and (E0)-(E5) of row 1268 (the input of Theorem FCT', the cut half). Both are read today
against Balaban's CMP 116, which this machine cannot read. Row 1294 Step 5 notes that the account prints its own
expansion machine, with one-term bounds and parameter holomorphy, for the large-field stages, and that applying it to
the regular step "was not checked". Rule 0a: `(CE)` occurs in FINISH.md only in row 1294; no row holds this item;
row 1296 holds (V9) and (DET), which I do not touch.

Moves: the one-cutoff carry on the pin route (rows 1256-1294). Success: (CE) and (E1)-(E3) become readings of the
account's printed and proved statements (no CMP 116), and the carry's list loses its CMP 116 dependence in the smooth
half and, if (E0), (E4), (E5) also close, in the cut half. Failure: the exact clause of the printed machine that does
not cover the regular step. Neither changes the seed.

**Plan, one step per response, each appended before the next.**
- Step 2: read the printed machine (CA-I 4.22 L80178-80239 and L80618-80700; 4.24 L108354-108610) and the regular step
  (4.3, L4073-4210; L58700-58760; L8778-8781). Record what each statement assumes and proves, with its index status.
- Step 3: decide whether the regular step is a case of the printed machine (large-field set empty, no arrested
  components). Prove the reduction or name the clause that fails.
- Step 4: (E0), (E4), (E5) of row 1268 against the same text; then (CE) as row 1294 6.5 states it, including the
  threshold eps_0 and its dependence on the floor (row 1294 6.5 "Robustness").
- Step 5: labels, state of the carry, what a checker should redo, RESULT.

## Step 2. What the account prints for the regular step's expansion (READ; written 2026-11-20T16:43Z by date -u)

Sources: Sussman and Alpoge, CA-I at 31a47c543775 (`theorem_0_complete_account_raw_I.tex`, 166711 lines), and the
component manuscripts YM4_EM, YM4_FP, YM4_LP, YM4_MB at c7fef8b21b58, fetched by URL into a scratch folder outside the
repository; Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, after Balaban. Statuses are
those of `library/sa-index/ca-full/index.tsv`.

**2.1 The regular step is cited, not printed.** 4.3:thm-small-field-step (CA-I L4136, status CITED) is "Balaban's
one-step small-field renormalization theorem, cited by statement": its first part is CMP 109 Theorem 3; "Its second
part is the argument of [CMP 116], including its bound [CMP 116 (2.41)], read with the fluctuation domain of [CMP 119
(3.43)] ... For the proofs we refer to [CMP 109 2-5] and [CMP 116]" (L4196-4201). The lemma before it,
4.2:lem-unmarked (L4031, INCOMPLETE), quotes "the argument ... Balaban's for [CMP 116 Lemma 3], carried out with the
small-field cutoff of [CMP 119]" at its marked step (L4078-4081).

**2.2 The printed large-field machine is stated only for a non-empty arrested set and rests on the full-stage
expansion.** 4.24:thm-survivor-block-expansion (L104684, PROVED) works "at a fixed term of the expansion [CMP 122a
(1.55)] whose set W of arrested components is non-empty" (L104687-104688). Its hypotheses include (h3) "The
normalisation lemma at the full stage and the fluctuation cluster expansion at the full stage, together with the three
statements of the full stage on which these two rest" (L104740-104743), (h4) "the analysis of the Gaussian integrals in
[CMP 119 (3.33)-(3.37)] ... used as stated there", and (h6) "The abstract cluster-expansion proposition". Its lemmas
4.24:prf-counted-once (L108354) and 4.24:prf-single-term (L108507), which row 1268 read as the written-out form of the
cut expansion, apply "the first step of the cluster expansion for the survivors ... with no change" (L108484) and "the
general one-term bound ... used here as stated in this chapter" (L108536-108538).

**2.3 The cited-by-description statements have no defining text in CA-I.** Grep of CA-I for "fluctuation cluster
expansion at the full stage", "normalisation lemma at the full stage", "abstract cluster-expansion proposition",
"general one-term bound", "the one-term lemma", "cluster expansion with parameters" and "parameter-free majorants" finds
only the citing sentences (L80181-80210, L80619-80638, L104730-104852, L108536-108599); no statement carries those
names, and the index has no label with "one-term" other than 4.22:lem-one-term-bound (whose own hypothesis is "the
hypotheses of the one-term lemma, including its floors (F1)-(F3)", L80619). Row 1294 6.1 found the same for the two
statements assumed by 4.22:lem-cluster-manifold. The component manuscripts do not supply them: FP (action-density
asymptotics), LP (periodic Wilson states and reflection positivity), MB (linear lattice PDE with block constraints) and
EM (the one-step comparison, which takes the step's expansion as supplier inputs 1-4) prove no fluctuation cluster
expansion.

**2.4 Consequence (PROVED as a reading, from 2.1-2.3).** The regular step is not a case of the printed machine: the
machine takes the full-stage expansion as an input (h3) and states itself only for W non-empty. So the route of row
1294 Step 5 ("applying the printed machine to the regular step") cannot supply (CE) or (E1)-(E3) from the account's
proved statements. Within the account, (CE) and (E0)-(E5) rest on Balaban's text: CMP 116 for the cut and (2.41), CMP
109 for the inductive bounds, CMP 119 (3.33)-(3.37) and (3.43) for the Gaussian analysis and the fluctuation domain.
What fails: Step 3 of the plan as written. What is left: whether CMP 119, which is on hand, already carries the cut
expansion (Mayer expansion, the decomposition chi = chi_(Y_0) sum_P (-1)^|P| chi^c_P, conditioning, whitening,
decoupling, and a one-term bound with the factor exp(-(1/2) gamma_2 T^2 |P|)) for a term whose large-field set is
empty. If it does, (E1)-(E3) become readings of an available Balaban paper; if not, they need a rebuild. Step 3 decides
this from the owner's copy of CMP 119.

## Step 3. Where the cut expansion of the regular step actually lives, and two routes that fail (written 2026-11-20T16:49Z by date -u)

**3.1 CMP 119 defers to CMP 116 (READ, owner's copy of Balaban CMP 119, OCR text, pages 33-37 and the references).**
CMP 119 is Balaban, "Convergent renormalization expansions for lattice gauge theories", Commun. Math. Phys. 119, 243-285
(1988). Its references are [I] = CMP 109 (RG approach I, small-field effective actions) and [II] = CMP 116 (RG approach
II, "Cluster expansions", 1-22). For the expectation values of the step it says: "To construct their cluster
expansions we repeat all the considerations of Sect. 3.7 [I], with minor changes ... We describe here briefly these
changes and additions only" (p. 275), and "The final step ... is the exponentiated cluster expansion of Sect. 7 [I], or
rather its appropriate generalization ... In each integral we apply the Mayer expansion (1.7.1)" (p. 277). So CMP 119
prints the changes for its boundary layers and new terms, and cites the cluster expansion itself. CMP 109's contents end
at Section 5 (its p. 249 table of contents), so the cited cluster-expansion sections and formulas are those of the
sequel CMP 116 (the OCR prints the citation keys as "[I]" and "(1.7.1)"; I did not resolve the key on a page image).
Either way, the Mayer expansion, the decomposition of the cut and the one-term bound are not printed in CMP 119 or CMP
109. Consequence: (E1)-(E3) for the regular step cannot be read from Balaban's papers on hand.

**3.2 The cut expansion is part of an open node of the T0 tree with an owner (READ; rule 0a).** `library/t0-tree.md`
L205 lists "R1 small-field family step (owner `b109`) | CMP 109 Theorem 3 plus CMP 116 refinement: S1-S12 ... activity
budgets and final family closure ... P1-P21 are pieces, not the full theorem", OPEN. `library/b109.md` L138-139 records
that "Local Gaussian integration and cutoff estimates | 116 (2.14)-(2.17), (2.31), Lemma 3" and "Mayer expansion,
connected logarithm, union filing | 116 Section 2" are taken as the account reads them, with only the finite
combinatorics ported (P8). `library/lrb.md` (frozen) proves CA-I 4.4 "under ... the CMP 116 (2.14) setting", whose
bounds "are taken as the account reads them" (lrb change log, item 8). So the carry's (CE) and (E0)-(E5) are not a
gap-specific blocker: they are the same CMP 116 Section 2 content that the whole hard-core chain reads through R1.
By rule 0a I do not rebuild CMP 116 Section 2 here; it belongs to R1's owner. The gap carry should cite R1 for these
inputs, so that one rebuild serves both.

**3.3 Route that fails: the cut difference through threshold-free totals (ARGUED, elementary).** Idea: the full step
integral over all fluctuation fields does not depend on the threshold, so the two unmarked totals differ by the
difference of the two large-field parts, each of which Balaban's large-field analysis makes small. It fails at the
one-step level that (FC-1) uses: at a common unmarked input list f the integrand is defined only on the small-field
domain of the previous step (the list's members are analytic there and nowhere else), so "the full integral with input
f" does not exist; the threshold-free object is the whole density with its large-field structure, and comparing frames
there is (FI) itself, which row 1260 2.4 already found out of reach by calibration.

**3.4 Route that fails: an ultralocal two-cut bound (ARGUED, proof sketched only; fails at the presentation).** If the
step were an integral against a product measure over cubes, with the cut a product of indicators of each cube's own
variables, then the cut only replaces each cube measure mu_c by its normalized restriction mu_c^T, and the ultralocal
expansion of `library/ultralocal_cluster_expansion.md` (after Dimock's Appendix B, Theorem 27, crediting Balaban) gives
a localized logarithm whose activities are multilinear in the cube measures. Two cuts change each cube measure by
total variation at most 2 P(N_c >= T_lo), so the two logarithms differ by that amount per cube with the same decay
(telescoping cube by cube, then row 1268's Lemma TL). Written out, this would prove the two-cut comparison in the
ultralocal case; I did not write it out, because it has no consumer: it fails for the actual step: the reference Gaussian of the step (precision tau_0 H_A + H_G) is not a product over cubes,
and a cut on the white-noise array xi (B = C^(1/2) xi) is a different cut from Balaban's cut on B, so its output would
again have to be compared with the account's. Making the actual cut ultralocal is exactly the decoupling of CMP 116
Section 2 ((2.5)-(2.8): conditioning, whitening, decoupling in s), which is R1's content.

**3.5 Outcome of Steps 2-3 (superseded by Step 4: the outline, not the account, prints the expansion).** The cut half (E0)-(E5) and (CE) stay OPEN as readings; their status is now precise: they
are CMP 116 Section 2 content, not printed in CA-I (2.2-2.3), CMP 109 or CMP 119 (3.1), and filed in the T0 tree under
R1 (3.2). This corrects row 1294 Step 5's remark that the account's printed machine could supply them (2.4). What is
left for this row: the margin reading (M) of row 1294 Step 4, which needs only EM (Step 4 below).

## Step 4. The outline prints the regular step's cut expansion: (E0)-(E6) and (CE) without CMP 116 (written 2026-11-20T16:59Z by date -u)

Source: Sussman and Alpoge's outline `YM4_sketch_500.tex` ("SA") at 31a47c543775 (32992 lines), fetched by URL into a
scratch folder outside the repository; Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text,
after Balaban. SA L-numbers are TeX lines.

**4.1 What SA prints (READ).** Two consecutive chapters treat the finite regular fluctuation integral.
- "Comparison of the actual localized complex Gaussian functional" (SA L13893-14272). Theorem
  thm:localized-complex-Gaussian (L13954-13972), with its proof printed (L13974-14089): for symmetric complex C and Gamma
  within eps of real references with constant K (FG1), the auxiliary functional J (FG4) equals integration against the
  normalized D = C + C Gamma Gamma^T C, J[1] = 1, and |J[F]| <= F_0 exp(A_K (eps + rho) m) for every Borel F with
  |F| <= F_0 e^(rho |b|^2) (FG5)-(FG6), constants independent of the local dimension m and the auxiliary dimension n.
  The failed-test form (FG12) (L14225-14234): integrands carrying 1{|b_beta| >= b} on distinct bonds of P_0 pay
  exp(-gamma b^2 |P_0|/2); "Multiplication by additional indicators only improves the bound." Parameter holomorphy
  (L14236-14242): "If the matrices and the potential part of an integrand depend holomorphically on external
  parameters, and the sharp cutoff sets remain fixed, the same estimates give a parameter-independent Gaussian majorant
  ... Fubini and Morera then prove holomorphy of the integrals." The weight tau (L14244-14249): "The rescaled structure
  (tau^(-1) C, tau^(1/2) Gamma) has effective covariance tau^(-1) D ... A small complex displacement of tau is included
  in the matrix perturbation." Stated obligations (L14258-14260): "The matrix gap and kernel closeness are the actual
  A2-A3 obligations, which we must prove."
- "The unmarked majorant for the actual regular polymer gas" (SA L14276-14810). (UM1) (L14306-14312): local
  potentials of a fixed number of types (free, intrinsic, already formed older, optional inserted) with
  |V(Y;P,B)| <= a_Y e^(-lambda_V d_f(Y)) (1 + M^(-4) sum_(b in Y) |B(b)|^2), holomorphic on declared complex boxes.
  (UM2) (L14325-14331): the exact integrand F_(D,P_0) = (-1)^|P_0| chi_(Y_0) prod_(b in P_0) (1 - chi_b)
  prod_(Y in D) (e^(V(Y)) - 1), chi_b = 1{|B(b)| < b}, with Y_0 the bonds requiring a field box and P_0 failed bonds
  outside Y_0. (UM3) (L14354-14361): T(Z, iota) = prod_(Delta in Z \ Z_0^#) int_0^1 ds_Delta d/ds_Delta J(Z_0; s_Z)[F],
  H(Z) = sum_iota T(Z, iota). (UM4)-(UM6) (L14378-14396): the matrix package on the coarse discs |s_Delta| < R_s and
  the failed-test bound. Structural hypotheses (L14406-14412): "the actual heredity, normalized-functional and
  wall-factorization identities". Counting (UM7)-(UM11). Term bound by "repeated Schwarz" in selection couplings and
  "Mixed coarse Cauchy on circles centered at s_Delta in [0,1]" (UM12)-(UM16), (L14484-14556). Activity bound
  (UM17)-(UM24): |H(Z)| <= tau e^(-(K_*-2)N) <= C_tau (a + p_star) e^(-Lambda l(Z)), p_star = n_b e^(-gamma b^2/2),
  tau = e^Theta [A_a a + p_star] (L14560-14656). Union filing and local logarithm (UM25)-(UM30):
  e^(mu l(X)) |E(X)| <= tau B_* <= C (a + p_star) (L14658-14757). Holomorphy and uniform convergence on smaller
  domains (L14762-14766). Insertion budget (L14793-14808): with a_* = min{W_0/2, 1/(4 e^Theta A_a)} and
  p_star <= 1/(4 e^Theta), every total norm a <= a_* has tau <= 1/2; "reserve one additional potential slot of norm
  w_star <= a_*/2. The entire slot stays within (UM23) and hence within (UM24)-(UM30) ... The constants may depend on
  the fixed localization parameters and rate choices, but not on cutoff, torus size, old-level count or the auxiliary
  Gaussian dimension."
- For comparison, the complete account's activity bound is a placeholder: CA-I L22393-22395, "Remark
  4.6:prop-activity-bound. The statement of this proposition is not written out here; parts of its proof are printed
  below." (`library/t0-tree.md` R3 lists it as unwritten.) So the outline, not the account, carries the printed
  regular-gas expansion; Step 2's grep of CA-I was right about CA-I and wrong to stop there.

**4.2 How SA's premises stand in this repository (READ, with pointers).** Frozen `library/hma.md` Theorem 4 supplies
UM4-UM6 and UM14 for the adopted Y family D4 on R4, conditional on its named premises (SA FG1-FG12, frozen hm and
descent, PIV); its referee verdict (hma L598) records that this is "proved only for the adopted Y family D4, on R4
within descent (7)-(8)'s ceilings, without Rep; not for SA's absolute gauge factor", and the FINISH row 284 summary
records "UM1 for non-gauge potentials not supplied". `library/ci-form.md` (distilled, not refereed) is the lane's own
conditional version of the regular gas (Lemma 4, Theorem 5) with the cut b = C_win A_1 l^(p_0) < R = l^q. So the
remaining premises of the route below are: (UM1) for every potential type of the step on the boxes; (UM4)-(UM6),
(UM14) for the step's actual matrices in the presentation the carry uses; SA's structural identities; SA's constant
conditions (UM19), (UM23), and (UM26) strengthened by a factor e (4.4).

**4.3 Correspondence (READ unless marked).**

| Row 1268/1294 input | What SA supplies | Label |
|---|---|---|
| (E1) term structure, threshold-free functionals | (UM2)-(UM3): the index set iota = (D, P_0), Z_0(iota), its collar, the functional prod int ds d/ds J(Z_0; s_Z) and the Mayer factor do not depend on the threshold; the cut enters only through chi_(Y_0) prod_(P_0) (1 - chi_b) | READ |
| (E2), (E2') Mayer bound | replaced by SA's Schwarz bound in the selection couplings (UM12)-(UM16), which needs only (UM1) on the support of the cut | READ, used in 4.4 |
| (E3), (E3') one-term bound with tail set | (FG12); for an admissible product cut (4.4 (C1)) the same with the low threshold | READ; PROVED for admissible cuts in 4.4 |
| (E4) convergence with margin | (UM24)-(UM30), with (UM26) strengthened by the factor e | READ; margin in 4.4 |
| (E5) common post-processing | EM L563-581, L665-700 (as row 1268 read them); SA's union filing (UM29) is threshold-free | READ |
| (E6) vertex as one more element type | SA's insertion slot (L14793-14808) | READ; used in 4.5 |
| (E0) both thresholds admissible | (UM23) at the low threshold and the box condition (L14333-14336) at the high one | ARGUED in 4.7 |
| (CE) Lemma PH form, fixed eps_0 | fixed J and cut sets, fixed Cauchy circles (L14552-14556), holomorphy principle (L14236-14242, L14762-14766), threshold a_* fixed (L14793-14808) | READ; 4.6 |

Next: Lemma TL-SA (two cuts), Lemma V-SA (vertex), then (CE) and the consequences (4.4-4.8).

**4.4 Lemma A and Lemma TL-SA (two product cuts in SA's regular gas; PROVED).**

*Admissible cuts.* Fix the step's data as in SA's chapter. A family f = (f_b) indexed by the free bonds, each f_b a
Borel {0,1}-valued function of the real free variables, is an *admissible cut with thresholds b_lo <= b_hi* if
  (C1) {f_b = 0} is contained in {|B(b)| >= b_lo} for every b, and
  (C2) {f_b = 1} is contained in {|B(b)| < b_hi} for every b, and every potential of the step that reads b obeys (UM1)
       and is holomorphic on a declared complex box containing the real box |B(b)| < b_hi;
  (C3) f_b reads only the free variables of a fixed neighbourhood of b (a fixed number of fine-cube layers around its
       incident cubes), and that width is included in the collar of every structural identity, as SA permits:
       "A fixed number of additional neighboring cube layers is permitted only if it is part of the assigned collar
       in every structural identity; its fixed width is then included in the constants" (L14346-14349).
SA's own cut chi_b = 1{|B(b)| < b} is admissible with b_lo = b_hi = b. In the frame comparison of row 1268 7.5 the two
cuts are f^psi_b = 1{N_b < T^psi} and f^phi_b = 1{N_b o Psi_c < T^phi} with |N_b o Psi_c - N_b| <= Lip |c - 1| and
N_b = |B(b)| in the common chart (row 1268 7.3 (iii)); both are admissible with
b_lo = min(T^psi, T^phi - Lip |c - 1|) and b_hi = max(T^psi, T^phi + Lip |c - 1|).

*Lemma A (SA's chapter holds for every admissible cut; PROVED by reading SA's derivation).* For an admissible cut f,
define F_(D,P_0) by (UM2) with chi_b replaced by f_b, and T(Z, iota), H(Z), E(X) by (UM3), (UM29). Then (UM15)-(UM30)
hold with p := exp(-gamma b_lo^2/2), p_star := n_b p and tau := e^Theta [A_a a + p_star], under the same constant
conditions. *Proof.* The decomposition prod_b f_b = f_(Y_0) sum_(P_0) (-1)^|P_0| prod_(P_0) (1 - f_b) is algebra and
holds for any product of {0,1}-valued functions. SA's derivation uses the cut at two places only: well-definedness of
the selected factors on the support of f_(Y_0) (L14333-14336), which (C2) gives, and the failed-test bound (FG12) inside
(UM6) and (UM15), which uses only the pointwise inequality 1{f_b = 0} <= 1{|B(b)| >= b_lo} <= exp(gamma (|B(b)|^2 -
b_lo^2)/2) given by (C1), on distinct bonds. The fine support Z_0(iota) and its collar read the cut only through the
supports of the cut functions of Y_0 u P_0, which (C3) keeps within the fixed collar width; the structural identities
(heredity, normalization J[1] = 1, wall factorization) are then the same identities for a product of local bond
functions as for SA's chi. Every other step ((UM7)-(UM14), (UM16)-(UM30)) does not read the cut. QED (The structural
identities themselves remain SA's hypotheses, L14406-14412, for f as for chi.)

*Lemma TL-SA.* Let f^1, f^2 be admissible cuts with common thresholds b_lo <= b_hi, let H^i, E^i be built with f^i,
put eta := exp(-gamma b_lo^2/2), p_star := n_b eta, tau := e^Theta [A_a a + p_star], and assume SA's hypotheses, the
constant conditions (UM14), (UM19), (UM23), and
  (UM26')   g_* > kappa_D + C_v  and  e c_adj B_* <= 1   (SA's (UM26) with one more factor e; "the explicit factor
            e^(-5 g_*) allows the last inequality by increasing the rate gap", L14699-14701).
Then, uniformly on the declared cores:
  (a) |H^i(Z)| <= tau e^(-(K_*-2) N(Z)) for i = 1, 2;
  (b) |H^1(Z) - H^2(Z)| <= 2 n_b (1 + e^Theta) eta e^(-(K_*-2) N(Z));
  (c) e^(mu l(X)) |E^1(X) - E^2(X)| <= 2 e n_b (1 + e^Theta) B_* eta for every X.
*Proof.* (a) is Lemma A with (UM24). (b) Fix Z and iota = (D, P_0) with Z containing Z_0^#(iota), iota not (empty,
empty). By (UM3) and Lemma A, iota, Z_0(iota), Z_0^#(iota), the functional
Lambda_(Z,iota)[F] := prod_(Delta in Z \ Z_0^#) int_0^1 ds_Delta d/ds_Delta J(Z_0; s_Z)[F] and the Mayer factor
M_D := prod_(Y in D) (e^(zeta_Y V(Y)) - 1) do not depend on the cut, and J is linear in F. Put g^i_b := f^i_b for b in
Y_0 and g^i_b := 1 - f^i_b for b in P_0, v := |P_0|, and list Y_0 u P_0 as b_1, ..., b_n. Then
    F^1 - F^2 = (-1)^v M_D sum_(l=1..n) G_l,   G_l := prod_(j<l) g^2_(b_j) (g^1_(b_l) - g^2_(b_l)) prod_(j>l) g^1_(b_j).
Since |f^1_b - f^2_b| <= (1 - f^1_b) + (1 - f^2_b) <= 2 1{|B(b)| >= b_lo} by (C1), and |g^i_b| <= 1{|B(b)| >= b_lo}
for b in P_0, we get |G_l| <= 2 prod_(b in Q_l) 1{|B(b)| >= b_lo} with Q_l := P_0 u {b_l}. On the support of G_l each
b in Y_0 has f^1_b = 1 or f^2_b = 1 (for b = b_l because f^1_(b_l) differs from f^2_(b_l); for the others because their
factor is 1), so |B(b)| < b_hi by (C2) and (UM1) holds there. Therefore SA's estimate (UM13)-(UM16) applies to
(-1)^v M_D G_l verbatim, with the failed-test factor p^v replaced by 2 eta^|Q_l|: on the coupling polydisc (UM12) the
integrand is at most 2^(r+1) e^(C_p W_0 L^4 N) eta^|Q_l| e^((C_p W_0 M^(-4) + gamma/2) |B|^2), (FG6) with (UM4)-(UM5)
and (UM14) bounds its J-integral by 2^(r+1) e^(C_0 N) eta^|Q_l| on both polydiscs, the integrand vanishes when any
zeta_Y = 0, and repeated Schwarz and the coarse Cauchy estimate give (UM16) with 2 eta^|Q_l| for p^v. The pass from
(UM16) to (UM20) uses (UM8), whose count reads v = |P_0| (not |Q_l|), so
    |Lambda_(Z,iota)[(-1)^v M_D G_l]| <= 2 e^(-K_* N) prod_(Y in D) u_Y e^(Theta v) eta^|Q_l|.
If b_l is in Y_0, |Q_l| = v + 1 and e^(Theta v) eta^(v+1) = eta q^v with q := eta e^Theta. If b_l is in P_0, then
v >= 1, |Q_l| = v and e^(Theta v) eta^v = eta e^Theta q^(v-1). Summing over l,
    |T^1(Z, iota) - T^2(Z, iota)| <= 2 eta e^(-K_* N) prod_(Y in D) u_Y [ |Y_0| q^v + v e^Theta q^(v-1) ].
Every bond of Y_0 u P_0 has its collar in Z (Y_0 lies in the fine support Z_0 and Z contains Z_0^#), so |Y_0| <= n_b N
by (UM11). Drop the restriction that P_0 and Y_0 are disjoint, as SA does (nonnegative terms), and use (UM10)-(UM11):
    sum_iota prod u_Y |Y_0| q^v <= n_b N prod_(Y in Y(Z)) (1 + u_Y) prod_(b: b^# in Z) (1 + q) <= n_b N e^(tau N),
    sum_iota prod u_Y v e^Theta q^(v-1) <= e^Theta prod (1 + u_Y) (d/dq) prod_b (1 + q) <= e^Theta n_b N e^(tau N),
since sum_(Y in Y(Z)) u_Y <= e^Theta A_a a N and the number of bonds with collar in Z is at most n_b N. Hence
|H^1(Z) - H^2(Z)| <= 2 eta n_b (1 + e^Theta) N e^((tau - K_*) N) <= 2 eta n_b (1 + e^Theta) e^(-(K_*-2) N), using
N e^(tau N) <= e^(2N) for tau <= 1. (c) Put h_Z := tau e^(-(K_*-2) N(Z)) and lambda := 2 n_b (1 + e^Theta) eta / tau,
so that by (a)-(b) |H^i(Z)| <= h_Z and |H^1(Z) - H^2(Z)| <= lambda h_Z. For a list (Z_1, ..., Z_n), telescoping gives
|prod_j H^1(Z_j) - prod_j H^2(Z_j)| <= n lambda prod_j h_(Z_j) <= lambda prod_j (e h_(Z_j)) (n <= e^n). The polymer
set, the incompatibility relation, the coefficients phi and the union filing (UM29) do not depend on the cut. So, with
(UM28), e^(mu l(X)) |E^1(X) - E^2(X)| is at most lambda times SA's majorant series for (UM30) with the weights
e w_hat_Z, w_hat_Z := h_Z e^(mu l(Z)), in place of w_hat_Z. With these weights (UM25) reads
sup_q sum_(Z contains q) e w_hat_Z e^(#Z) <= e tau B_*, and (UM27) holds by (UM26'):
sum_(Z' incompatible with Z) e w_hat_(Z') e^(#Z') <= c_adj N e tau B_* <= N. SA's rooted argument (L14738-14757) then
gives e^(mu l(X)) |E^1(X) - E^2(X)| <= lambda e tau B_* = 2 e n_b (1 + e^Theta) B_* eta. QED

*Remark (size).* The bound (c) is of the size of the cut's own contribution p_star to (UM30), as it must be: two cuts
differ exactly on failed-test events. The ratio lambda is small when the potential amplitude a dominates p_star
(lambda <= 2 (1 + e^(-Theta)) p_star/(A_a a + p_star)); (c) needs no relation between a and eta.

**4.5 Lemma V-SA (the vertex part (E6) from SA's insertion slot; PROVED given SA's chapter).** Let the two expansions
E^0, E^1 of the same admissible cut differ by a local vertex prod_x (1 + q_x), each q_x a function of the fluctuation
near the site x, holomorphic on the declared complex boxes, with |q_x| <= rho on them and rho <= 1/2 (row 1268 7.3 (ii),
7.5 "vertex part", with rho = rho_k). Assume the base potentials have total norm a <= a_*/2, p_star <= 1/(4 e^Theta),
and let a_w be the (UM1) norm of the inserted type w := sum_x log(1 + q_x), so a_w <= c_1 rho with c_1 depending only on
the fixed geometry (|log(1 + q)| <= 2 |q| for |q| <= 1/2, and each w_x has a domain of bounded size). Then for every X,
    e^(mu l(X)) |E^1(X) - E^0(X)| <= (4 c_1 B_*/a_*) rho,   once R := a_*/(2 a_w) >= 2.
*Proof.* Put the coupling zeta on the inserted type: the integrand carries e^(zeta w) = prod_x (1 + q_x)^zeta. For
|zeta| < R the total norm is at most a + |zeta| a_w <= a_*, so SA's insertion budget (L14793-14808) gives tau <= 1/2
and (UM24)-(UM30); the local logarithm E(zeta; X) exists, is holomorphic in zeta (SA L14236-14242, L14762-14766), and
e^(mu l(X)) |E(zeta; X)| <= B_*/2. E(0; X) = E^0(X) and E(1; X) = E^1(X). Cauchy's estimate on circles inside |zeta| < R
gives |dE/dzeta (t)| <= sup|E|/(R - t) for 0 <= t <= 1, so |E(1; X) - E(0; X)| <= sup|E| log(R/(R - 1)) <= 2 sup|E|/R
for R >= 2. Hence e^(mu l(X)) |E^1(X) - E^0(X)| <= B_*/R = 2 a_w B_*/a_* <= (4 c_1 B_*/a_*) rho, using a_w <= c_1 rho and
absorbing a factor 2. QED
This is row 1268's (E6) in the form Theorem FCT' uses: the vertex part is O(rho_k) = O(theta_k^(-3/2) polylog).

**4.6 (CE) of row 1294 (READ in SA; with the answer to row 1294 6.5 "Robustness").** Row 1294's Proposition HAN asks
that the regular-step expansion have the form of its Lemma PH (fixed reference Gaussian, decoupling, cut, partitions
and contours; holomorphic elements), and converge with majorant bounds when every element obeys
|v_e| <= eps_0 e^(-kappa d(e)) with a FIXED eps_0. SA's chapter has this form: the terms (UM3) are finite sums of
products of J-integrals against one normalized Gaussian with fixed cut sets, with the s-derivatives taken by Cauchy
integrals on fixed circles (L14552-14556); holomorphy in parameters with fixed cut sets is SA L14236-14242; the series
is dominated by majorants built from the norms only (L14762-14766); the weight tau sits in the matrix perturbation
(L14244-14249). The convergence threshold is the (UM1) total norm a_* = min{W_0/2, 1/(4 e^Theta A_a)}, whose constants
"may depend on the fixed localization parameters and rate choices, but not on cutoff, torus size, old-level count or
the auxiliary Gaussian dimension" (L14806-14808). Row 1294's elements (i)-(v) obey the uniform bound of its Lemma EB
on the collar polydisc, which is stronger than (UM1) (UM1 allows growth (1 + M^(-4) sum |B|^2)); the quadratic weight
shift (ii) fits (UM1) as written, or can be moved into the matrices by L14244-14249. So (CE) holds with
eps_0 := a_*/2 (keeping the insertion slot free), and the threshold does not shrink with the floor: row 1294 6.5's
"if the threshold had to shrink like a power of theta" case does not occur on SA's chapter. Premises: those of 4.2.

**4.7 (E0) (ARGUED from readings).** Both frames' cuts must be admissible with one pair b_lo <= b_hi satisfying
(UM23) at b_lo and the box condition (C2) at b_hi. In chart units the account's cut radius is a fixed multiple of
p_0(g) = (log g^(-2))^(p_0) (CA-I 4.3, L4172-4174: "the cutoff radius (A_1/A_0) p_0(g)"), and the fluctuation domain
on which the step's potentials live has radius C_1 p_1(g) (L4167-4169, L4176-4178, the domain of CMP 119 (3.43)); the lane's
distilled ci-form uses b = C_win A_1 l^(p_0) < R = l^q with l = log theta. The two frames' thresholds differ by the
relative amount |c - 1| = O(theta^(-1/2) polylog) (row 1268 7.3). So b_lo -> infinity like (log theta)^(p_0), giving
(UM23) above a floor, and b_hi <= (1 + o(1)) b stays inside the box once (log theta)^(q - p_0) exceeds a fixed
constant, provided q > p_0 (equivalently p_1 > p_0; not checked against the account's choice of p_1 here).

**4.8 Consequences for the one-cutoff carry (PROVED GIVEN the premises listed in 4.2 and below).**
- *Cut half.* Row 1268's Theorem FCT' needs (E0), (E1), (E2'), (E3'), (E4)-(E6) "at every step with uniform
  constants". Lemma TL-SA (4.4) gives the cut part directly, in place of row 1268's Lemma TL with (E1)-(E4):
  e^(mu l(X)) |E^phi(X) - E^psi(X)| <= 2 e n_b (1 + e^Theta) B_* exp(-gamma b_lo^2/2), with b_lo of 4.4 for the
  non-nested pair of row 1268 7.5 (so (E2'), (E3') are covered). Lemma V-SA (4.5) gives the vertex part, O(rho_k), in
  place of (E6). (E5) is EM's linear post-processing (row 1268's reading), and (E0) is 4.7. Since row 1267's |||.||| is
  an infimum over localisations of a total (row 1267 3.1), the difference of the two SA localisations bounds the
  difference of the two totals, with EM's post-processing constant C_post. So Theorem FCT' holds with
      nu_k <= K_1' exp(-(1/2) gamma b_lo(k)^2) + K_2' rho_k,
      K_1' := 2 e n_b (1 + e^Theta) B_* C_post,   K_2' := (4 c_1 B_*/a_*) C_post,
  the form row 1268 summed (its Lemma S and S''), with SA's constants (gamma, Theta, n_b, B_*, a_*) in place of the
  unread CMP 116 ones. The constants are uniform in the step, because SA's are independent of cutoff, torus size and
  old-level count (L14806-14808), given that the premises hold uniformly along the run.
- *Smooth half.* Row 1294's Proposition HAN is PROVED GIVEN (CE), (S) and Lemma SC; (CE) is now READ in SA (4.6). So
  Proposition HAN, row 1293's Theorem PE and Corollary FC-s, and row 1294's Corollary U' rest on SA's chapter and its
  premises, not on CMP 116.
- *What the carry no longer reads.* No input of the one-cutoff carry on the pin route reads Balaban's CMP 116 after this
  step, except through SA's own citations inside its premises (SA's structural identities are stated by SA as
  hypotheses of its chapter). This removes the access block recorded in rows 1264, 1268, 1294 for the carry.
- *Premises that stay open (OPEN, not attacked here).* (P1) (UM1) for every potential type of the step on the boxes of
  (C2), uniformly along the run (the account's inductive bounds; FINISH row 284 records "UM1 for non-gauge potentials
  not supplied"). (P2) (UM4)-(UM6), (UM14) for the step's actual matrices in the presentation the carry uses; frozen
  hma Theorem 4 supplies them for the adopted Y family D4 on R4, not for SA's absolute gauge factor (hma L598), so the
  carry's presentation must be matched to D4 or supplied separately. (P3) SA's structural identities (heredity,
  normalized functional, wall factorization), SA L14406-14412, and the completeness identity at complete physical
  pairs, SA L14262-14271. (P4) The constant conditions (UM14), (UM19), (UM23), (UM26') in one order of choice, and
  q > p_0 in 4.7. (P5) Row 1268's other hypotheses: (TH), (H1)-(H3), (H5), with rows 1278, 1280, 1284, 1293, 1294
  on (H2), (H3), (U).
- *Relation to the T0 tree.* R1's "CMP 116 refinement" (t0-tree L205) reads the same CMP 116 Section 2 content. Step 3.2
  filed the carry's need under R1; with 4.1-4.6 the carry's need is met by SA's chapter instead, and R1's owner may want
  the same substitution (b109 L139 already lists "SA 1150-1377 and 14276-14816" as the source of the Mayer expansion,
  connected logarithm and union filing, and "assumes the actual activity bound", which is SA's (UM24) given (P1)-(P4)).
  Evidence for R1's owner only; I do not edit R1.

**4.9 What a checker should redo first.** (1) Lemma A: that SA's derivation (L14276-14810) reads the cut only at
L14333-14336 and in (FG12)/(UM6), and that (C3) keeps the collars and structural identities intact. (2) Lemma TL-SA (b):
the telescoping bound |G_l| <= 2 prod_(Q_l) 1{|B(b)| >= b_lo}, the support claim on Y_0, and that the pass (UM16) ->
(UM20) charges e^Theta only for the v bonds of P_0 (so the extra failed bond b_l is free). (3) Lemma TL-SA (c): the
factor n <= e^n absorbed into the weights e w_hat, and (UM26'). (4) Lemma V-SA: the inserted type's (UM1) norm
a_w <= c_1 rho and the Cauchy step. (5) 4.6: that row 1294's elements fit (UM1) with the needed decay rate
(kappa >= lambda_V) and that SA's tau-handling L14244-14249 covers the weight shift. (6) 4.7: the account's p_1
versus p_0.
