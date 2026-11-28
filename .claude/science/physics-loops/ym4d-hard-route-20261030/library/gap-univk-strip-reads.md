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
- II 51981-52030, 57711-57745 (the two flat energy-difference bounds, declared proved as implications);
  III 37520-37600 ("the reading on exactly paired shells [...] is not proved"); Y 76060-76125 (chart densities of
  pre-main stops); O 6325-6358 (the exponent with the counter-insertions). Parts II and O were fetched by URL at
  31a47c543775 into /tmp/ym4d-strip-reads-w2/src. Part I was not fetched; nothing below reads it.

## 5. The comparison at the two real reads (step 4, written 2026-11-23T00:16Z by date -u)

Kind of result: proof of steps the account sketches or uses in another norm. Lemmas FIT, QF, DET, PIV are PROVED
here by hand from the named printed inputs; unchecked. Repo search for the names: `library/open-core.md` and the
FINISH rows have no hit for "Lemma FIT", "CL-OP", "CL-W", "Lemma QF" (one grep each).

**5.0 The pair and the reading fixed.** One good aligned label h, one live component (C, m) of it, a point of P_h,
the label's common inner space (III 11880-11884: "the space (Omega_h, mu_h) of the label's common inner variables.
This space is common to the two runs"). Reading of the owning action: the FIRST reading of check 1415 Section 1.
In O 6337-6349 the exponent is -A(x_k(.), U) - sum_(j<=k) b_j A(phi_j, U) + (E, R and boundary sums), and
"The pointwise identity x_k(p) + sum_(j<=k) b_j phi_j(p) = beta is exact. It does not authorize changing the index
maps". I keep each subtracted regular family with its own counter-insertion as one formed list entry, compared
once as a stored value (classes of III 11968-11972; owner ZONE-FORM). The physical channel -A(x_k(.), U_k(V)) is
compared directly: its coefficient part is Corollary WIL-z of row 1410 (check 1415 Section 4), its fixed-coefficient
part is U4 below. No b-entry is then used twice.
Every use below is split as the account splits it (Y 129407-129410; III 45708-45722): the family part is the
difference of the two runs' objects at ONE real datum; the reading part is the change of the datum in one run.

**5.1 Lemma FIT (the arithmetic of a classical charge).** Let n be a zone present in an aligned label. Then for
every real s with 0 <= s <= c_2 (1 + e_T),
  (log x_n)^s vartheta_w^n <= [[delta]]^c_n / (E_0 (C^nat_cl)^(1 + e_T)).
Proof. vartheta_w = vartheta_T = vartheta_x vartheta_2^(1/4) (III 12627, 12547). So
(log x_n)^s vartheta_w^n = (log x_n)^(s - c_2) vartheta_x^n times (log x_n)^(c_2) vartheta_2^(n/4). The last factor is
at most [[delta]]^c_n / (E_0 C^nat_cl) (III 43361, line (cl); it is (LB2) of 3.1). By (P5), vartheta_x^n <=
(C^nat_cl (log x_n)^(c_2))^(-e_T) (III 12458). So the first two factors are at most
(C^nat_cl)^(-e_T) (log x_n)^(s - c_2 - c_2 e_T) <= (C^nat_cl)^(-e_T), because log x_n >= 1 (III 12719, (h11)) and the
exponent is not positive. QED
Use: c_2 >= 2 p_0 (III 1919-1920), p_0 >= 5 r_pr (III 597) and e_T > 1 (III 12453) give c_2 (1 + e_T) >= 4 p_0 >=
2 p_0 + 10 r_pr. So s = 0 (scalars), s = 2 p_0 (a quadratic form at a field of size p_0(g)) and s = 2 p_0 + 4 r_pr
(a Wilson sum at a regular field, with the factor R^4) are all admitted. Caution: III 327-328 says the c_2 of the
operator size is "distinct from the constant c_2 of the glossary"; I use the c_2 of the alignment statement
(III 1919, 12369) throughout, as III 12458-12459 does.

**5.2 Input (CL-OP), in piece form.** For a real symmetric operator K of a use (the kept chain matrix K_j of a
stopped step with its parts K_A, K_G; the operator of the kept quadratic form), taken in the two runs at one real
common datum on the common real coordinate space: delta K = sum over pieces omega with connected supports, n(omega)
the lowest zone met by supp omega, and for every zone n and every cell c_0 of zone n
  sum over omega with n(omega) = n and c_0 in supp omega of sum_(b,b') abs(delta K_omega(b,b')) <= C_op vartheta_w^n.
Printed sources of this form: for the operators of a fluctuation step, Lemma zone-split (h1), (i), (iii) (III
12637-12643, 12719-12733; there with the size d^op_n, which includes the logarithm); for the kept form, "norm(delta
K)_delta <= C_cl vartheta_w^(h+1) at real common parameter points" (III 44105-44106, "the proposition on the
classical operator rows", an input (e) of the uniqueness theorem, III 41367-41369); for the Gaussian of one live
arrest, Corollary kept-gaussian (III 45663-45700). For Gaussians of interrupted steps "one nested in another" the
account lists the two-run difference as outstanding ((O2) of 4.3). So (CL-OP) is an input here, not a result.
It is a statement about Hessians and walk kernels of two lattices at one real background. It compares no masses,
so it is not equivalent to (LOG), to the seed or to the two-cutoff comparison of measures.

**5.3 Lemma QF (a quadratic use at two real reads, fixed coefficient).** Assume (CL-OP) for K. Let x be a real
vector on the coordinates with abs(x_b) <= r_n whenever b lies in the support of a piece of class n. Then
  abs( (1/2) <x, delta K x> ) <= (1/2) C_op sum_n r_n^2 vartheta_w^n N_n,   N_n := the number of zone-n cells met.
If r_n <= C_r (log x_n)^(p_0) then the right side is at most C' sum_n [[delta]]^c_n N_n, with
C' = C_op C_r^2 / (2 E_0 (C^nat_cl)^(1 + e_T)).
Proof. abs(<x, delta K_omega x>) <= r_n^2 sum_(b,b') abs(delta K_omega(b,b')) for a piece of class n. Assign each
piece of class n to one zone-n cell in its support and sum by cell with (CL-OP). Then Lemma FIT with s = 2 p_0. QED
Application to U1. The stored strip field of level j lives on Omega_(j+1) minus Lambda_(j+1) and satisfies
abs(A'(b)) <= C p_0(g_j) on the kept tests (O 17528, 17558; Y 63252; check 1415 "The ordinary stored strip
coefficient"). A piece of class n through such a coordinate has n <= j + 1, and then log x_j <= C log x_n by
x_i - x_j >= lambda (j - i) - c_5 for i <= j (Y 61911) and adjacent frame comparability. So r_n <= C_r (log x_n)^(p_0).
With Q_tau = tau K_A + K_G at one tau (the coefficient part was paid in check 1415), delta Q_tau = tau delta K_A +
delta K_G and tau <= 3/2 on the ratio disc (Y 77268-77270). So the fixed-coefficient change of the kept strip
quadratic is at most C' sum_n l^c_n N_n: a site charge at the classical load, filed at the cells of zone n met by
the pieces. PROVED GIVEN (CL-OP) for K_A and K_G.
Application to U2. For the kept quadratic form the field is B with abs(B) < r_t = A_1 p_1(g_t), p_1 < p_0 (Y
74994-74995; III 597). Same conclusion. This is the account's own line (l7) argument (III 44105-44118), read at a
real point and normalized per cell in place of the one-run size q_max(m). PROVED GIVEN (CL-OP).

**5.4 Lemma DET (the determinant and normalizer factors).** Let K^A, K^B be real symmetric, both >= gamma I with
gamma > 0, on one real space, and assume (CL-OP) for K. Then
  abs( log det K^B - log det K^A ) <= gamma^(-1) C_op sum_n vartheta_w^n N_n <= C'' sum_n l^c_n N_n.
Proof. K_s := K^A + s delta K >= gamma I for 0 <= s <= 1. d/ds log det K_s = tr(K_s^(-1) delta K), of modulus at
most norm(K_s^(-1)) times the trace norm of delta K, and the trace norm is at most sum_(b,b') abs(delta K(b,b')).
Sum the pieces by cell as in 5.3; Lemma FIT with s = 0. QED
Application. K >= gamma I is the printed real hypothesis (Y 77281-77283). For Q_tau at one real tau in the
half-disc, Q_tau >= K/2 >= (gamma/2) I (Y 77284-77288), so the same argument applies to Q_tau with (CL-OP) for K_A and K_G. Together with the
fixed-matrix bound 2 d abs(delta tau) of check 1415 (D11) this gives the whole change of the determinant factor:
abs(delta log det Q) <= 2 d_j abs(delta tau_j) + (5/gamma) C_op sum_n vartheta_w^n N_n (the factor 5 = 2 (tau + 1) with tau <= 3/2, from delta Q_tau = tau delta K_A + delta K_G). It answers defect 4 of
check 1415 for the determinants ("If K_A^run or K_G^run changes [...] take the additional determinant ratios
explicitly"). PROVED GIVEN (CL-OP). An incoming normalized precision D_0 is a stored output of an earlier step and
is compared as a value.

**5.5 Lemma PIV (pivot and chart densities, U3).**
 (a) An ordinary pivot factor J_c = abs(det m_c(V))^(-1) is a function of the chart row V alone (Y 75026-75041),
 and it is invariant under a common real frame change. In the presentation of Y the Haar chart density
 sigma(g_j B) uses the reference coupling g_j = theta_j^(-1/2) of the scaffold (Y 73074, 76548-76549: "Preparatory
 and main restoration Gaussians use theta_j"). So at one point of the common inner space these factors are EQUAL
 in the two runs, and their change is zero. In the presentation of III the factor sigma(g_i B) carries the run's
 coupling and is an object (z2) of Lemma zone-split, with class-n pieces of activity at most d^op_n eps-bar^pr
 (III 12612, 12727-12729); that is a classical site charge by 3.2. Either presentation fits; they must not be
 mixed in one ledger. This needs only that the inner variables and the
 averaging contours of the component are common (COMMON+ of check 1408, owner PD-REST); for an aligned label the
 private level of B is below every level of the component.
 (b) If a row is read through a run-dependent centre (the translated chart of a sharp pre-main stop, Y 76087-76101:
 "The density on this box keeps the Haar factors and the exact derivative of the linearizing correction [...] zero
 first derivative at the origin and uniformly bounded second derivative"), let mu be the norm of the difference of
 the two rows. With sigma_min(m_c) >= 2^(-1/3) L^(-4) (Y 75030-75034) and a Lipschitz constant C_m of V -> m_c(V):
   abs( log J_c^B - log J_c^A ) <= 3 x / (1 - x),   x := 2^(1/3) L^4 C_m mu,   for x < 1.
 Proof. det(m + e) = det m det(1 + m^(-1) e) on R^3 = su(2), and abs(log det(1 + T)) <= 3 norm(T) / (1 - norm(T)).
 QED. So one pivot costs at most 6 * 2^(1/3) L^4 C_m mu when x <= 1/2. With the net-mismatch bound of the two reads
 (III 6845-6850, 7228-7231: rate vartheta^((j ^ n_X)/2)) this is a classical charge of exponent s = 0. I did not
 verify that the rate vartheta^(n/2) of that bound is at most C vartheta_f^(n/4), which is what (LB1) needs
 (III 43360-43361). CONDITIONAL on that rate and on C_m; the count of pivots is at most C V° (Y 75041).
 (c) The coarea and cutoff-translation Jacobians of a stage or extendibility exit (Y 75106-75117, 76098-76100) are
 of kind (b). I did not find a printed two-run statement for them. They are the part of U3 that is NOT on file.

**5.6 The Wilson background at fixed coefficient (U4): not proved, and why.** The term is
  -[ A^B(c, .) - A^A(c, .) ] at one real datum, c a common real weight,
for the masked inner core of an island, the carrying action of a drop-out on its box, the w-weighted terms of the
restored identity, and the bulk carrying term. The two runs have different bare lattices (run B has the private
level j = -1, III 11821-11822). So there is no bare plaquette-by-plaquette matching, and the half-sum identity of
check 1415 (6.1(iv)) has nothing to act on at the bare scale. What is needed is a bound per unit cell of zone n on
the difference of the two cell actions of the two real backgrounds built from one datum:
  **(CL-W)** abs( S^B_cell(c) - S^A_cell(c) ) <= C_W sup abs(c) R_n^4 eps_n^2 vartheta_w^n   per unit cell of zone n.
GIVEN (CL-W): with abs(c) <= C x_n, x_n eps_n^2 <= C (log x_n)^(2 p_0) (Y 130613) and R_n <= L (log theta_n)^(r_pr)
(check 1415 Section 3), the cell cost is C (log x_n)^(2 p_0 + 4 r_pr) vartheta_w^n <= C l^c_n by Lemma FIT with
s = 2 p_0 + 4 r_pr. So U4 fits the site load GIVEN (CL-W), with the printed exponents and no new condition.
(CL-W) is not on file. In the account it is the second term of Proposition remainder-difference, "Proof
outstanding" (III 43753-43763: "the two-run difference of a weighted Wilson sum on slices with the common weights
c^B; it is the operator part and is classical"). Its natural source is the flat energy-difference bound, declared
proved as an implication in part II (II 51981-52010: abs(delta E^u(c)) <= varpi' 15 B_sharp^2 f^flat(c-bar) with
varpi' = C_E (varpi_H + varpi_W + L^(-l(c))), under the relative closeness (B1)-(B3) of the layers across the two
cutoffs; II 57711 on exactly paired sets). But the account says that reading this statement at the points where
its clause (v) compares the runs "is not proved" and "requires at least three things" (III 37545-37558: covariance
of the response functionals under the change of base, analyticity domains after one shrink, absorption of the
constant). I did not attempt it: it is a classical multiscale statement of the size of a chapter, and three
attempts by hand in one response would be notes, not a proof.
Three ways I looked at before stopping, each with the reason it fails as a short proof:
 1. Matched-plaquette half-sum (check 1415). Fails: the bare plaquette lists differ; a cell of B holds L^4 times
    as many bare plaquettes, each with curvature smaller by L^(-2). Only the cell sums are comparable.
 2. Minimality. Each background minimizes its own action under its own averaging constraints. Restricting the B
    minimizer to the A lattice (by block averaging the bottom level) gives a competitor for A, so S^A <= S^A(restr.
    of U^B); and S^A(restr. of U^B) <= S^B + (error of the one-step averaging identity at a regular field). The
    reverse direction needs an EXTENSION of the A minimizer to the B lattice with action S^A + small, that is, the
    one-step classical renormalization identity for the Wilson action at a regular field with its rate. That
    identity with the rate L^(-theta n) is the content of II chapter 5 (the response at zeroth order); it is not
    elementary. This route is the right one for a rebuild; it needs II 50158 and II 51981 ported, not re-derived.
 3. The account's own leaf route: treat the cell action as a stored leaf and use the classical load's last entry
    ("Its affine part in g^2 [...] is accounted for by the last entry of the classical load", III 13126-13128).
    This is the form the answer takes; it is the statement (CL-W) again, so it is not a proof.

## 6. Verdict (step 5, written 2026-11-23T00:18Z by date -u)

**6.1 Use by use.** "Fits" means: at most C l_n per cell of zone n met, each class once, with the read
multiplicity (k - n + 1) and the one-level shift of III 44760-44772; l_n = [[delta]]^(nat+)_n.

| Use | Coefficient part | Fixed-coefficient part (this row) | Standing |
|---|---|---|---|
| U1 kept strip matrix K_j of a stopped step | paid (check 1415): C' d_j gfrak_j z_j | Lemma QF: C' l^c_n per zone-n cell met | PROVED GIVEN (CL-OP) for K_A, K_G. (CL-OP) is printed for one live arrest (III 45663-45700, given the classical operator rows) and is the account's outstanding (O2) for nested interrupted steps |
| U1 determinant factors of K_j, Q_tau | paid at fixed matrix (check 1415, D11): 2 d_j abs(delta tau_j) | Lemma DET: (5/gamma) C_op vartheta_w^n per zone-n cell met | PROVED GIVEN (CL-OP) |
| U1 filed boundary factors (rejected chains; ratio correction filed in the boundary potential) | stored leaf: value difference | none: a stored output is compared as a value (III 13106-13133; per-cell domination III 13337-13393 with (INC-1)) | printed form; part of it is the account's outstanding (O3); owner ZONE-FORM |
| U2 glued restoring operator (kept quadratic form) | none: the coefficient is theta in both runs (row 1410 D8) | Lemma QF with abs(B) < A_1 p_1(g_t): C' l^c_n per zone-n cell met, n = h + 1 | PROVED GIVEN (CL-OP) = "the proposition on the classical operator rows" at real common points (III 44105) |
| U3 ordinary pivots; Haar chart density | none | zero at a common inner point (Lemma PIV (a)) | PROVED GIVEN the common inner space (COMMON+, PD-REST) |
| U3 translated charts of sharp pre-main stops | none | Lemma PIV (b): 6 * 2^(1/3) L^4 C_m mu per pivot | CONDITIONAL on the mismatch rate and on C_m |
| U3 coarea and cutoff-translation Jacobians of stage and extendibility exits | none | no printed two-run statement found | NOT ON FILE. Size if of kind PIV (b): a constant times the mismatch per coordinate. Not shown to be a live factor beyond the printed bounds; not shown to fit either |
| U4 Wilson background (masked core, carrying action on its box and on the remaining plaquettes, w-terms of the restored identity) | Corollary WIL-z (row 1410, check 1415): C' l_n per cell GIVEN (REG-P) | C (log x_n)^(2 p_0 + 4 r_pr) vartheta_w^n <= C l^c_n per cell GIVEN (CL-W) (5.6, Lemma FIT) | (CL-W) NOT PROVED. It is the operator part of the account's Proposition remainder-difference, "Proof outstanding" (III 43702) |
| kept potential V(Y~), family marks | - | K_val l_n per cell of Y^sharp met by class-n slots (III 42067-42077) | printed, declared proved under its hypotheses (a)-(j); not checked here |
| kept potential V(Y~), reading mark | - | abs(r_Y) <= 8 C*_TL vartheta^sharp_Y O^+(v) (III 44392), with O^+(v) up to C R_m^(p_Sigma) | per COMPONENT, not per cell: see 6.2 |

**6.2 The decision.** Does the total change of these uses cost the shifted site load C (k-b+1)(l_b + l_(b-1)) per
cell? Neither a clean yes nor a named misfit:
 (i) No use was found that fails to fit. Every use has a slot in the account's ledger (4.1), as a family mark or a
 change of read, each class once. No live factor beyond the printed bounds was found.
 (ii) The fixed-coefficient changes of the strip matrix, of its determinant factors and of the glued restoring
 operator ARE site charges at the classical load, by Lemmas FIT, QF, DET, GIVEN the one classical input (CL-OP).
 The printed exponent order (c_2 >= 2 p_0, p_0 >= 5 r_pr, e_T > 1) is exactly what the arithmetic needs; no new
 exponent condition enters for these uses.
 (iii) The Wilson background at fixed coefficient fits GIVEN (CL-W), and (CL-W) is open here and in the account.
 (iv) One use is per component and not per cell: the reading mark of the kept potential, of size
 C vartheta_f^m R_m^(p_Sigma) for a component created at step m. Against (LB1) it is a site charge on one cell of
 the component iff (log x_m)^(r_pr p_Sigma) vartheta_f^(3m/4) <= C on aligned zones, which holds if
   (EXP-R) c_2 >= (512/3) r_pr p_Sigma
 (from vartheta_f = vartheta_2^(1/512) and the alignment bound vartheta_2^(m/4) <= (C^nat_cl (log x_m)^(c_2))^(-1)).
 I did not find (EXP-R) printed. c_2 is subject only to a one-sided floor, so (EXP-R) can be added to the order of
 choice; it raises n_c. Without it the consumer's count moment (CAP-M0) needs the per-component form: one factor
 exp(C R_m^(p_Sigma) l^c_m) per live component of a good label, to be paid by the component's own activity
 e^(-c p_0(g_m) - kappa_1 abs(C)) (Y 61932). I did not prove that payment.
 (v) Incidence. Lemmas QF and DET charge the zone-n cells met by the pieces of ONE operator. A cell can be met by
 the operators of several steps and several components. The site form needs the per-level sum over all operators
 of one level in (CL-OP) (call it (INC-OP), the operator analogue of (INC-1)); "at any one place and level at most
 one drop-out mark is active" (Y 62128) gives the factor (k - n + 1) once (INC-OP) holds. Not proved here.

**6.3 What the row established about the lane.** The object of rows 1404 to 1415 on a live component, the two-run
change of the kept factors at a common real field, is the account's Proposition III 37667 ("The two-cutoff
smallness [...] of the two factors kept un-integrated inside a thrown-back region [...] Proof outstanding"),
with its four outstanding inputs (O1) to (O4) of 4.3. The weight leg of Theorem CAP on live components therefore
cannot be ported; it needs (O1) to (O4) or their pointwise forms (CL-OP), (CL-W), (INC-OP). Rows 1410 and 1415
proved the coefficient half of (O1) conditionally (4.2 (a)).

**6.4 Is the reduction equivalent to the open target?** No, for (CL-OP) and (CL-W). Both are zeroth-order
statements: two real backgrounds, their Hessians and their cell actions, built from one real datum on two
lattices. They contain no integral over fields and compare no masses; they hold or fail for each datum
separately. (LOG), (CAP-M0), (SHELL) and the seed are statements about measures. I cannot show that (INC-OP) and
the per-component payment of 6.2 (iv) are weaker than (CAP-M0); they are of the same kind as (INC-1) (owner
ZONE-FORM).

## 7. Next two rows and their decisive outcomes

**Row 1, `gap-univk-strip-reads-check` (cross-provider check of this row, gpt-6.2-astra).** In this order:
(1) Section 4: is the object of the queue row really the account's Proposition III 37667, and does the table of
4.1 match III 43791-43837 line by line (in particular: is the kept strip matrix of a stopped step the "Gaussians
Q(a)" of item (iv), and is (O2) about the same object in the nested case); (2) Lemma FIT: the exponent arithmetic,
and whether the c_2 of III 1919, 12369 and 12458 is one number; (3) Lemmas QF, DET, PIV, including the claim
n <= j + 1 for a strip coordinate and the trace-norm step; (4) whether (CL-OP) in piece form is what the classical
operator rows (alpha), (gamma) and Lemma zone-split (iii) give at a real common datum; (5) 6.2 (iv): the size of
the reading mark and (EXP-R).
 Decisive outcome: if (1) holds, the weight leg on live components is exactly (O1) to (O4) and no port closes it;
 if the table mismatches at a use, that use is the first candidate for a live factor beyond the printed bounds.

**Row 2, `gap-univk-clw` (proof row, classical, one unit cell; Claude Fable 5.2 medium after a prior-work digest
of II chapter 5).** Prove (CL-W) of 5.6 on one unit cell of zone n at one real regular datum, by the minimality
sandwich of 5.6 route 2: port II 50158 (the two-cutoff response at zeroth order) and II 51981, 57711 (the flat
energy-difference bounds) as cited inputs, write the restriction and extension maps between the two bare lattices,
and bound the two one-sided errors by C R_n^4 eps_n^2 L^(-theta n). Then obtain (CL-OP) for the Hessian of the same
cell action by the same sandwich at second order, or name why the second-order step needs more than II gives.
 Decisive outcomes: (1) (CL-W) holds with a rate L^(-theta n), theta >= theta_A / 8: then U4 fits by Lemma FIT with
 no new exponent condition, and the account's (O1) is closed on live components up to its incidence sum. (2) the
 extension step loses the rate at a regular datum (an explicit datum with cell-action difference bounded below by
 c R_n^4 eps_n^2): then the Wilson background at fixed coefficient is the named live factor, of size
 x_n R_n^4 eps_n^2 per cell, and the weight leg needs a moment of it.
Order: Row 1 first; it is short and it tests the identification on which Row 2 rests.

## 8. Status

| Statement | Mark |
|---|---|
| Sections 3, 4 (the account's frame and ledger; the identification with III 37667 and (O1)-(O4)) | READ, lines quoted; the match to the queue row's uses is mine; unchecked |
| (LB1), (LB2) | printed (III 43360-43362) |
| Lemma FIT | PROVED from III 12458, 12547, 12627, 12719, 43361; unchecked |
| Lemma QF, Lemma DET | PROVED GIVEN (CL-OP); unchecked |
| Lemma PIV (a) | PROVED GIVEN the common inner space; (b) CONDITIONAL; (c) NOT ON FILE |
| U4 fits GIVEN (CL-W) | PROVED GIVEN (CL-W), (REG-P) and three printed exponent bounds; unchecked |
| (CL-OP) for nested interrupted steps, (CL-W), (INC-OP), (EXP-R) or the per-component payment | OPEN |
| the hypotheses of III Lemma layer-store-bounds, Lemma kept-reading-mark, Theorem production-bound, Proposition constituent-bounds | cited, declared proved by the account, NOT checked here |
| (REG-P), (COMMON+), (INC-1), (PC-RD), (PC-LIST), (SC-CELL), formation test for V_X | OPEN, owners PD-REST and ZONE-FORM (not redone) |
| (CAP-M0), (SHELL), test leg, (RAR), term D, (GEO), (LOG), the seed | OPEN, untouched |

No numeric job was run; none was needed (memory was 68 percent free when checked). Files written in the
repository: this file only. Scratch: /tmp/ym4d-strip-reads-w2/src (part II and the short outline, fetched by URL
at 31a47c543775). Part I was not fetched. Rows 1404, 1406 and checks 1405, 1408 were read through row 1410's
digest, check 1415 and targeted greps, not line by line.

Finished 2026-11-23T00:18Z (date -u). All steps of the plan are done; Sections 1 to 8.

RESULT: Proof row done in part, author only, unchecked. Reading: the row's object (the two-run change of the factors kept by a live component at a common real field) is the account's own Proposition III 37667, "Proof outstanding", with four outstanding inputs (O1 remainder terms, O2 nested interrupted Gaussians, O3 one part of the R-step boundary terms, O4 a counting estimate whose statement is not written); the account's ledger (III 43791-43837) gives every use a slot, family or classical, each class once. PROVED here: Lemma FIT (any classical charge (log x_n)^s vartheta_w^n with s <= c_2(1+e_T) is at most the classical load of zone n; covers s = 0, 2p_0, 2p_0+4r_pr with the printed exponent order); Lemmas QF and DET (the fixed-coefficient change of the kept strip quadratic, of its determinant factors and of the glued restoring quadratic is a site charge at the classical load, GIVEN the classical operator input (CL-OP) in piece form); Lemma PIV (ordinary pivots and the Haar chart density do not change at a common inner point). No use was found that fails to fit and no live factor beyond the printed bounds was found. NOT decided: the Wilson background at fixed coefficient fits GIVEN (CL-W), a classical cell-action comparison of the two bare lattices that is open here and in the account (operator part of III 43702); the reading mark of the kept potential is per component with a factor R_m^(p_Sigma) and is a site charge only under a new exponent condition (EXP-R) or a per-component payment; the Jacobians of stage and extendibility exits have no printed two-run statement. OPEN: (CL-OP) for nested interrupted steps, (CL-W), (INC-OP), (EXP-R), plus the owners' inputs and (CAP-M0), (SHELL), the test leg. Next rows: a cross-provider check of this row, then gap-univk-clw.
