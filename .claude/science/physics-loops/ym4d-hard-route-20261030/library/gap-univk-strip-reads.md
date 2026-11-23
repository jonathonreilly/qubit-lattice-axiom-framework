lead: anthropic/claude-fable-5-2/medium mac-mini-worker
lease_until: 2026-11-23T12:06Z

# Row 1417, gap-univk-strip-reads: the moving-read comparison of one complete native pair

Written by Claude Fable 5.2 (medium), Mac mini worker 2, at commit 5ae9c78c6. Started 2026-11-23T00:06Z (date -u).
Not checked by another model. Research-stage working state; no status.

Credit. The objects compared here (the kept strip matrix, its boundary and determinant factors, the glued restoring
operator, the pivots, the chart densities, the counting by uses) are constructions of Ethan Sussman and Levent Alpoge
(with Claude and Codex as authors of their text): YM4_1400.tex (cited "Y line"), the complete account part III (cited
"III line"), and the short outline (cited "O line"), all at revision 31a47c543775 (Y at 2bc0658f91d2). The background
structure is Balaban's. Rows 1404, 1406, 1410 and checks 1405, 1408, 1415 of this folder are the consumer and the
prior readings.

## 0. Plan (written before any reading; revised below as steps finish)

Problem (queue row 1417). One complete native pair of reads of a good aligned live label: its owning action and
counterterm, its original strip mask, tree and chart, its normalization. Compare, at the two real reads:

- U1. the kept strip matrix and its filed boundary and determinant factors (Y 76507-76554, 77278-77296);
- U2. the glued restoring operator;
- U3. the pivots and chart densities (Y 75023-75117, 76086-76105);
- U4. the Wilson background at fixed coefficient.

Decide: does the total change of these uses cost the shifted site load C (k-b+1)(l_b + l_(b-1)) per cell, in the
counting by uses of III 11963-11993 and Y 129399-129629 (each use once; a stored output is compared as a value or
expanded, never both)? If a use does not fit: name it, give its actual size, say whether it is a live factor beyond
the printed bounds. Not to redo: the ordinary stored strip coefficient (check 1415); CV, PD-REST, ZONE-FORM,
ZONE-RESERVE, ZONE-CAPACITY.

Steps, one per response, each appended here before the next:

1. Repo search and prior rows: row 1410, check 1415 in full; rows 1404, 1406, checks 1405, 1408 for the consumer.
2. Source read A: the owning action and counterterm (Y 61913-61932; O 6331-6356); fix the reading.
3. Source read B: the strip matrix and its factors (Y 76507-76554, 77278-77296).
4. Source read C: pivots, chart densities, restoring operator (Y 75023-75117, 76086-76105).
5. Source read D: the counting by uses (III 11963-11993; Y 129399-129629) and the per-cell domination (III 13337-13393).
6. The comparison: a list of uses, each with its change between the two reads and its charge.
7. Verdict per use; the first use that does not fit, with its size; next two rows.

## 1. Repo search and prior rows (written 2026-11-23, step 1)

Read in full: row 1410 (`library/gap-univk-native-ends.md`) and check 1415
(`library/gap-univk-native-ends-check-astra62.md`). Rows 1404, 1406 and checks 1405, 1408 were read through the
digest in row 1410 Section 1 and the citations of check 1415; I did not re-read them line by line.

What binds this row (from check 1415):
- (W3) of row 1410 fails. The counting rule is by uses: III 11963-11993 gives each slot one class (anchor zone j,
  read level k'); Y 129399-129424 recurses only on a child's empty-switch value; Y 129603-129629 replaces the raw
  brackets by the localized remainder. A stored output is compared as a value, or expanded into inputs and reads.
- The ordinary strip coefficient is paid: abs(A'(b)) <= C p_0(g_j) on the kept tests (O 17558, Y 63252) and
  norm(K_j^keep) <= C_w (Y 76514-76521) give (1/2) abs(delta tau_j) abs(<A', K A'>) <= C' d_j gfrak_j z_j.
- Open after check 1415: the fixed-coefficient change of each operator, chart factor and scalar between the two
  real reads (its D10, the field part of D8, D11 beyond the fixed matrix, D13 beyond the matched pivot, D5, D7), and
  the outer carrying action on its remaining plaquettes with its counter-insertions.

Repo search. `library/open-core.md` (one grep): no hit for "strip matrix", "restoring operator", "kept chain",
"operator entr", "moving read", RD-BG, strip-reads. FINISH rows that name this comparison: 1404 to 1410, 1415 and this
row. Owners used and not redone: CV, PD-REST (`library/open-registry.md` L19, L418), ZONE-FORM, ZONE-RESERVE,
ZONE-CAPACITY (L543-545, owner `b4-typed`, all open).

## 2. Sources read (appended as read)

- Y 61895-61940 (terminal exponent -A(x_k(.),U) + E_k + R_k + B_k - E_(k,S); the two sequences of a label).
- III 11805-11830, 11955-12060 (the pair of runs; "one assembly formula P_h, carrying no run index, applied to the
  array x^c of the run's stored numbers"; uses, classes, marks; the loads [[delta]]^u_j and [[delta]]^c_j).
- Y 129395-129760 (exponent of a nested history; arguments of the production formula; bounds on the class discs).
- Y 76495-76560, 77240-77300 (the complete kept quadratic; the parameter tube; the half-disc determinant).
- III 385-410, 13100-13135, 13330-13395, 17280-17300 (classical index rates; the read split G^(n) + G^rd + G^own;
  per-cell domination; the c-load envelope).
- Y 74885-74912, 75020-75125 (the compensated form Q_tau; pivot factors J_c; late and early drop-out reference).
- III 318-332, 1912-1924, 12355-12380, 12436-12462, 12530-12560, 12602-12760 (operator size d^op_n; alignment
  index n_c; (P4), (P5); Lemma "Zone split of the two-run differences at the fluctuation step").
- III 6820-6870, 7205-7265 (net mismatch of the two runs' block data; the two-run read bound with rate
  vartheta^((j ^ n_X)/2)).
- III 13036-13062 (class (b3): classes inside a live component).
- III 40960-41010 (Definition of the kept factors K(Y) = {V(Y~), Q_Y}), 42025-42080 (Lemma layer-store-bounds),
  44362-44420 (Lemma kept-reading-mark), 44509-44612 (Proposition kept-later-sites), 44760-44772, 45455-45510,
  42998-43026 (purely classical constituents), 43310-43311 (the classical index rate).
- `library/sa-index/ca-full/index.tsv`: declared status of these statements (all PROVED by their own declaration).

## 3. The account already prints the moving-read frame (step 2; reading of their text, unchecked)

Kind of result: check of their text. Every statement in 3.1 to 3.4 is theirs. Rows 1410 and 1415 did not cite
part III chapter 9.5 (the 44xxx lines); a grep of this folder's `library/gap-univk-*.md` for "44509" or
"kept-later-sites" gives no hit. So this section is the prior work the row should have started from.

**3.1 Two kinds of two-run change, two loads.** For a member read at a parent, the account writes "the two-run
difference as the family difference evaluated at a common datum plus the change of read in one family"
(Y 129407-129410), and charges "each own unit [...] once, with the original class for each family mark, reading
mark, form and Gaussian" (Y 129421-129424). The family part is measured by the unknown load [[delta]]^u_j. The
reading part is classical and is measured by [[delta]]^c_j (III 12044-12053, 13120-13128):
  [[delta]]^c_j = sum_(i<=j) (varsigma_(1+j-i) E_0 + w_(j,i) g_i^(kappa_0) + w^B_(j,i) B_0) hat-vartheta^nat_i
                  + E_0 min{1, C^nat_cl (log x_j)^(c_2) vartheta_2^(j/4)}.
Here hat-vartheta_n = min{2, 2 (16 C_W C_* c_3 vartheta_f^n)^(1/2)} and hat-vartheta^nat_n = hat-vartheta_n^(1/2)
(III 43310-43311), with vartheta_f = vartheta_2^(1/512) (III 388). These are explicit numbers, so the classical
load has explicit LOWER bounds, which is what a charge needs:
  (LB1) [[delta]]^c_j >= varsigma_1 E_0 hat-vartheta^nat_j = c_1' E_0 min{2^(1/2), C vartheta_f^(j/4)}   (the i = j term);
  (LB2) [[delta]]^c_j >= E_0 C^nat_cl (log x_j)^(c_2) vartheta_2^(j/4) on an aligned label (III 12369-12373, 13746).
(LB2) is printed and used by the account (III 13746-13758). (LB1) is my reading of the definition; varsigma_1 =
(2 + rho) rho^2 > 0 (III 11996-11999).

**3.2 The operators of a fluctuation step (printed, declared proved).** Lemma zone-split (III 12602-12760):
the covariance D, the walk operator Gamma, the first form F = Gamma^T D^(-1) Gamma, the potentials, "the Jacobians
and the factor sigma(g_i B)" and the normaliser split by lowest zone met, and the class-n pieces are at most the
operator size
  d^op_n := C^T_cl (log x_n)^(c_2) vartheta_T^n,   c_2 >= 2 p_0 (III 1919-1920),
in the weighted kernel norm (clause (iii)); and d^op_n <= (C^T_cl / C^nat_cl) vartheta_x^n on a zone present in an
aligned label (clause (iv)). With (LB2): d^op_n <= (C^T_cl / (E_0 C^nat_cl)) vartheta_x^n [[delta]]^c_n. So at a
fluctuation step every fixed-coefficient operator change is a site charge at the classical load, with a spare factor
vartheta_x^n. This is for the small-field step. It does not cover the operators inside a live large-field component.

**3.3 The kept factors of a live island (printed, declared proved).** III 40974-40996: by Balaban CMP 122b (1.71)
and the sentence after it, T'_m(Y) is a sum of integrals "over the fluctuation field B and the older integration
variables, of an exponential whose exponent contains a quadratic form in B and the term V(X~, U_m) [...] these two
are the only ingredients of that definition that depend on the background configuration (U, J)". The kept factors are
  K(Y) := { V(Y~), Q_Y },   Q_Y := -(1/2) <D H''_(1,m,Y) B, zeta D H''_(1,m,Y) B>.
Q_Y is the glued restoring quadratic of the queue row (U2), in Balaban's letters. Proposition kept-later-sites
(III 44509-44612) gives, "identically at the site's paired points P^A, P^B",
  v~^B(P^B) - v~^A(P^A) = sum_(n <= m) delta v^(n)(rd^A P^A (+) c^B_col, c^A; Phi_Y) + r_Y,
with the family marks in the classes (n, k') and the reading mark r_Y in the class (m, k'). The sizes:
 - family marks of the kept potential: sup abs(delta V^(n)) <= K_val [[delta]]^(nat+)_n times the number of cells of
   Y^sharp met by class-n slots (III 42067-42077). "The right-hand side of the last line is a volume; it is read at
   the top storeys only, under un-normalised weights."
 - reading mark: abs(r_Y) <= 8 C*_TL vartheta^sharp_Y O^+(v^(B sharp)), and in the natural norm the two members
   together are at most k^rd_m R_m^(p_Sigma), k^rd_m := (32 C*_TL)^(1/2) C_Sigma vartheta_f^(m/2) (III 44390-44400).
 - "Purely classical constituents" (III 43009-43026): for "the units v_e among the Gaussians Q(a) of an interrupted
   run, the kept quadratic form q_C at the core C, and the classical part of the localised members v^C of the
   remainder terms [...] the whole difference between its values in the two runs takes the place of the reading
   mark". So the strip Gaussians of an arrested component and the kept quadratic are classical: they have no family
   mark at all, only a change of read.
 - support: a kept mark of class (n, k') is nonzero only if the history of (Y, m) has zone n or n = m, and then
   j(C) <= n + 1 (III 44760-44772). This is the origin of the one-level shift.

**3.4 What 3.1 to 3.3 do not print.** (a) Each bound above is a bound on a mark in a norm (natural norm, dial
supremum, activity norm), stated for use under the dial. The first line of the reading-mark bound is pointwise at
the paired points; the family bound is a supremum over common data. The consumer of this row needs the pointwise
value on P_h, which these give. (b) They concern the two background-dependent factors. The other factors of
T'_m(Y) (measures, tests, pivots, chart densities, determinants, the inner Wilson term at the prepared inner field)
do not depend on the later background by CMP 122b (1.71). They can still depend on the run: "some of these factors
still depend on the cutoff through the coupling, density or chart. In particular the old inner quadratics have
their own cutoff differences even when independent of the later background" (Y 129579-129584). Section 4 takes
these one by one.
- III 41949-42024 (Definition layer-store: the layer-n difference of a kept factor), 43026-43106 (the seven lines
  (l1) to (l7) that define the layer size d^(n)_m; kept quotients), 43107-43215 (Theorem production-bound),
  43703-43766 (Proposition remainder-difference, "Proof outstanding", and its route), 43766-43840 (Proposition
  constituent-bounds), 11845-11906 (the terminal term and the label's chart; the common inner space).

## 4. The account's ledger for the uses of this row (step 3; reading of their text, unchecked)

Kind of result: check of their text. The table is theirs (III 43766-43837); the match to the queue row's four
uses is mine.

**4.1 The statement.** For a component C of Z at R_m on an aligned label and a layer n <= m, the two kept
factors obey (Theorem production-bound, III 43131-43140)
  O^+(delta V^(n)(C^sharp)) + O^+(delta q^(n)_C) <= [C^nat_Sigma d^(n)_m + (1/2) k^(<m)_n
                                                     + (1/2) c'_rd C_Sigma vartheta_f^(n/2)] R_m^(p_Sigma),
and "No constant in the right members depends on [...] the count sum_j abs(Gamma^0_j cap C) [...] or the volume
of the core [...] an age [...] the number, the sizes or the pasts of thrown-back regions and of arrests". The
layer size d^(n)_m is the least constant in seven inequalities (III 43047-43069). Proposition constituent-bounds
(III 43791-43837) bounds it:
  d^(n)_m <= K_D [[delta]]^(nat+,(m))_n + Theta-bar k^(+,(<m))_n,
with the contributions listed by constituent. Matched to the queue row:

| Use of row 1417 | Constituent in III | Printed contribution to d^(n)_m | Kind |
|---|---|---|---|
| U1 kept strip matrix of a stopped run (the Gaussians of an interrupted run) | (iv), line (l2), "the Gaussians Q(a)" | c_G vartheta_w^(n/4) <= 2 c_G C_(hat-vartheta) [[delta]]^c_n / E_0 | classical; whole difference is a change of read (III 43011-43016) |
| U1' filed boundary factors of the strip (rejected chains, ratio correction filed in the boundary potential, Y 76536-76549) | (i), (ii): family marks of B^(j), B'^(j) and of the chain terms; (iii) their reading marks | (1/(2 B_0)) (y_n + y'_n); K^fr_C [[delta]]_n (...) + (4 theta_P / (3 N C^sharp_0)) k^(+,(<m))_n; c_rd vartheta_f^(n/2) <= 2 c_rd C_(hat-vartheta) [[delta]]^c_n / E_0 | family (unknown load) and classical |
| U2 glued restoring operator (the kept quadratic form q_C = Q_Y) | (ix), line (l7) | K^q_D [[delta]]^c_n, "present only for n = h + 1, where h is the index in the bound norm(delta K)_delta <= C_cl vartheta_w^(h+1) for the operator difference delta K supplied by the proposition on the classical operator rows" | classical operator difference |
| U4 Wilson background at fixed coefficient, and the coefficient itself (weight-linear Wilson members of Balaban's C_m) | (viii), line (l6) | K^C_D [[delta]]_n, GIVEN Proposition remainder-difference | **"Proof outstanding"** (III 43702) |
| copies, rim totals, pointed units | (v), (vi), (vii) | K^pt_D [[delta]]_n; K^cp_D [[delta]]_n (n = m only); (1/3) K_rim [[delta]]_n + (1/3) sup theta^dagger_L k^(+,(<m))_n | family |

So the account's answer to the row's question is YES for U1, U1', U2 in the layer sizes, as declared proved
statements with hypotheses, and OPEN for U4. The exact outstanding statement (III 43703-43718):
  sum_(Y_4 in C^sharp) sup abs(delta v^(C,(n))(Y_4)) <= C^x_C [ gfrak_n z^sharp_n + E_0 (log x_n)^(c_2) vartheta_w^n ].
Its route (III 43721-43763) splits A^B(c^B, .) - A^A(c^A, .) = A^A(delta c, .) + [A^B(c^B, .) - A^A(c^B, .)]. The
first term is the coefficient part ("A proof must show that this part is controlled by the entry gfrak_n z^sharp_n
[...] linearly and under no root"). The second "is the two-run difference of a weighted Wilson sum on slices with
the common weights c^B; it is the operator part and is classical", to be bounded by "the classical operator bound
on the two-run difference of a weighted Wilson sum on slices". "What a proof must show is that the sum is bounded
by C^x_C E_0 (log x_n)^(c_2) vartheta_w^n".

**4.2 Consequences for this lane.**
 (a) The coefficient part A^A(delta c, .) is what row 1410 Lemma WIL and Corollary WIL-z prove (check 1415 Sections
 3, 4: HOLDS at a matched fixed read, GIVEN (REG-P)). So rows 1410 and 1415 supply the first term of the outstanding
 proposition on a live component, conditionally. That is a contribution to their open statement; it was not
 recognised as such in those rows.
 (b) The second term is exactly "the Wilson background at fixed coefficient" of this queue row. It is open in the
 account. Section 5 attacks it.
 (c) The charge is per component with the factor R_m^(p_Sigma), not per cell. The one-run size of the kept factors
 is A^nat(m) <= (1/2) C^nat_Sigma R_m^(p_Sigma) (III 43084), uniformly in the cell count of C. So the total change
 of the uses of one live component (C, m) in layer n is at most
   [C^nat_Sigma (K_D l_n + Theta-bar k^+_n) + (1/2) k_n + (1/2) c'_rd C_Sigma vartheta_f^(n/2)] R_m^(p_Sigma),   l_n := [[delta]]^(nat+)_n.
 This is a site charge in the sense of row 1404 only after one more step: either the component holds at least
 c R_m^(p_Sigma) cells of zones n and n+1 (not printed; false for p_Sigma > d if the component is one box), or
 the factor R_m^(p_Sigma) <= C (log theta_m)^(r p_Sigma) is paid once per live component. Section 6 states this as
 the per-component form of the consumer's moment.
 (d) The quotients k_n are themselves bounded by a recursion in m (the term Theta-bar k^(+,(<m))_n). I did not
 read its closure; hypothesis (2) of the proposition is an induction over sites.
- III 44060-44142 (proofs of lines (l6), (l7)), 45663-45730 (Corollary kept-gaussian: the Gaussian factor kept by a
  live arrested region), 41358-41372 (inputs of the uniqueness theorem), 37640-37760 (Proposition "two-cutoff
  smallness [...] of the two factors kept un-integrated inside a thrown-back region [...] Proof outstanding"; the
  account's list of four outstanding statements of its clause (v)).

**4.3 The account declares this row's statement outstanding (III 37667-37745).** Proposition
9.5:prop-the-two-cutoff-smallness-of-the-kept-fac, "Proof outstanding": for a thrown-back region that still carries
its large-field factor at a later step, "Two factors are kept un-integrated over the region. The first is the
quadratic form kept by the large-field operation, built on the region's own background and localized to the region.
The second is the sum of the effective-action terms of the earlier steps together with the current step's localized
remainders of the action expansion". The assertion is that the two-run difference of each, measured by its
oscillation "with the real field on the region itself held fixed at one value common to both runs", divided by the
normalizing power of the radius, is below the threshold of the uniqueness theorem. Its route is the layered
machinery of 4.1, and "The current step's remainder terms of the action expansion enter through one further input,
not proved". The account then lists (III 37725-37741) the outstanding statements "of clause (v)'s own making":
 (O1) "the two-run difference [...] of the field-free remainder terms of the basic step of R for which [CMP 122a]
      writes 'we omit details' [...] taken near a large-field region that the step leaves un-integrated, and [...]
      split by the lowest level that they meet". This is Proposition remainder-difference (III 43702): U4.
 (O2) "the two-run difference of the Gaussian factors, quadratic in the real variables common to the two runs, that
      are kept inside such a region by large-field steps interrupted there, one nested in another". This is U1, the
      kept strip matrix of stopped steps, in the nested case.
 (O3) "the two-run difference of one part of each boundary term produced at a step of R. This part is carried by
      the small-field region of that step, or by large-field regions whose large-field factor is absorbed back into
      the small-field format at that step". This is part of U1' (the filed boundary factors).
 (O4) the mixed-size counting estimate, whose statement "is not written out here" (III 37716-37718).
The index `library/sa-index/ca-full/index.tsv` marks III 37667, 37716 and 43702 OUTSTANDING.

**4.4 Verdict of the reading (before any attack).** The queue row asks whether the total change of U1 to U4 costs
the shifted site load. The account's answer:
 - It has a complete FORM for the answer: every constituent is a family mark (unknown load) or a change of read
   (classical load), each class once, with the one-level shift j(C) <= n + 1 (4.1, 3.3). That form answers "yes,
   per component, with the factor R_m^(p_Sigma)".
 - It does NOT have the proof. The statement is its Proposition III 37667 with (O1) to (O4) open. So this row
   cannot be closed by a port. Row 1410's dichotomy and check 1415's "next row" both asked for a decision that the
   account itself lists as outstanding.
 - Nothing in the passages read shows a live factor BEYOND the printed form. The pivots and chart densities of the
   queue row are treated in 5.4 below.
