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

**3.5 Outcome of Steps 2-3.** The cut half (E0)-(E5) and (CE) stay OPEN as readings; their status is now precise: they
are CMP 116 Section 2 content, not printed in CA-I (2.2-2.3), CMP 109 or CMP 119 (3.1), and filed in the T0 tree under
R1 (3.2). This corrects row 1294 Step 5's remark that the account's printed machine could supply them (2.4). What is
left for this row: the margin reading (M) of row 1294 Step 4, which needs only EM (Step 4 below).
