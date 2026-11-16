lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-17T01:51Z

# gap-direction3-max: direction after rows 1032-1050 (queue row 1051)

Worker: Claude Fable 5.2 (model id claude-fable-5-2), effort max, Mac mini worker 1, pinned at commit 14a12e900 on
branch `claude/ym4d-hard-route`. One session, no subagents. Research-stage working state: nothing here is a public
claim, and no item below is checked by a second party. Marks used: PROVED (written argument in this file, unchecked),
ARGUED (argument with a named gap), OPEN, FAILS (with the counterexample or the failing step).

## 0. Plan and status log

Plan (at most eight steps; each response does one step and appends its result before the next):

1. Read `parts/gap.md` in full and `library/gap-dichotomy.md`; write Section 1 (the wall (W), the repaired (W), the
   dichotomy, the test table, as I read them, with line anchors).
2. Read rows 1036, 1038, 1042, 1046 with both checks of each; write Section 2 (what route (ii) at the pinned boundary
   now is: EXT, MEAN, AVG, H_c, (N1)).
3. Read rows 1031, 1032 with both checks (1049, 1050); write Section 3 (B15 with (INV) and (UV-Cas); GS-eq; (GS-CAS)
   with (NO-CONST); (TB)_n of row 1017; (BDD-Delta) and (LIOU); any line a check names as open).
4. Task (1) + (2): one paragraph per live line with the worth-doing test and hardest-first ranking; Section 4.
5. Task (3): for the top one or two lines, a mechanism with the first lemma written out, tried by hand (or the
   counterexample built); Section 5. Registry grep of `library/open-core.md` and FINISH rows BEFORE each attempt.
6. Task (4): literature lens on any new path chosen in step 5; Section 6.
7. Task (5): the next one to three proof rows as complete briefs; Section 7.
8. Re-read every PROVED item, print every cited line anchor, final RESULT line; Section 8.

Status log (times from `date -u` in the same call that writes them):

- 2026-11-16 13:51Z: started. Memory 72 percent free. Output file did not exist at the pinned commit; created with
  this plan. Queue row 1051 = FINISH.md line 1132 (row n at line n + 81).
- (between 13:51Z and 14:05Z; the time first typed here was a guess and is removed) step 1 read done: `parts/gap.md` (257 lines, in full) and `library/gap-dichotomy.md` (473 lines, in
  full). Section 1 written.

## 1. The wall as read at the pin (step 1; no new mathematics)

All line anchors in this section are of `parts/gap.md` at 14a12e900 unless another file is named.

- **(W), verbatim** (L18-20): "For Wilson SU(2) along the account's trajectory (first-passage data, dilated), prove:
  (W) There is a physical size L in P with z^-(L) > 256 D_0 + 30, where D_0 bounds D^+ on the sizes from L/4 on."
- **(W), repaired** (L21-23; gpt-6-astra check of row 720): there are a bound (L_0, D_0) of (BDD-Delta) and L in P with
  L at least 4 L_0 and z^-(L) > 256 D_0 + 30. Equivalent to (PHYS-SEED).
- **The dichotomy** (`library/gap-dichotomy.md` 2.1-2.2). Form 1: exactly one of (I) (PHYS-SEED), (II) not (BDD-Delta),
  (III) (BDD-Delta) with z^-(L) at most 256 D_0 + 30 at every size L at least 4 L_0 of P. Form 2: at least one of (I),
  (II), (III') a uniformly recurrent critical element in Omega(D_0). (I) iff (W). Objects: D(a) = F(a^4) - f a^4, the
  Casimir free energy of the symmetric torus; m(B) the transfer gap of the box B; S(k; B) the thermal sum; z = side
  times gap; Theorem ZD-c: (W) iff (BDD-Delta) and (Z-UNB).
- **The price** (L246-257): (W) iff (BDD-Delta) and (Z-UNB); (W) follows from (CAS) with theta < 1 and an extensive
  base; in words, "the wall is the absence of one selective inequality at every scale between first passage and the
  seed size. Selective means: false for a massless factor."
- **The two kinds of input** (L47-50): (K-one), a property of the measure at one scale in the band; (K-flow), a
  statement that starts from first-passage data and is carried through the band by a step that fails for U(1), for
  frozen groups and for products with a massless factor.
- **The theorem-grade tests for T_W** (test table L214-228, point 2 L235-237): compact U(1), the free photon, the
  product with a massless factor (Lemma PT; Proposition NP for tools that read finitely many values of D), Theorem D2
  (no supremum over tilts), Lemma SHEET (nothing uniform over coupling fields). "None of them asks for a number at one
  scale. They ask for: non-abelian structure, a rate, the whole state space, typical fields." Point 5 (L242-244): for
  (K-flow) tools the lane has constraints and no refutation device.
- **Lead rules in force** (L91-99) that bind this row: rule W2 (a direction row states its kind, (K-one) or (K-flow));
  the 2D O(N) model is a source of mechanisms, not a price (two posted unrefereed proofs: Ding, Huang and Yang,
  arXiv:2611.04908; OpenAI 2026-10-06); the 2D band is crossed by ONE step, a mixing bound at one fixed bare coupling
  from a pinned-cell stiffness iteration whose gain is the bracket term, zero for the abelian model; the direct port
  FAILS in the class of all pins and strengths (row 1011, Theorem BH of row 1016); "the missing object is a 4D
  analogue of the 2D short step, a selective gain at order-one response".
- **Obligation entries from row 1003 on** (L135-150) that this row must build on: Proposition NP (1003); Lemmas LYP,
  LYP2, Theorem TW-T (1004); (E0-tor) open (993 check); Theorem CR and (LIOU) (1017); Theorem BH, Lemma CEN+, Lemma MC
  (1016); the short step in three forms (T-per), (T-pin), (T-vor), Lemma NAB (1018); aligned frames, (SYM) with (REG)
  (1026, 1034); the decimation line, (TB)_n (1025); kept ultraviolet data is the wall, Lemma FV, Lemma REC, Proposition
  CONST (1028); afield set A, Theorem CR^c, Proposition VIR, (ENT+) (1031); route (ii) at the pinned boundary: Theorems
  GR, TP, H4 (1036), LIP-TREE, NOLIP, WEAK, TUNE (1038), EXIST, CUBE-COUL, CURL-P (1042), EXT, MEAN, AVG, O2-GR, O2-GR+,
  CURL-Q (1046); afield set B, Lemma BAR, CHAIN-4, NUC, CAS-0, GS, RISE, AMP, GS-dir, GS-eq, NOCS, FP-U1, TRI, SPH with
  the named open (INV), (GS-CAS), (NO-CONST) (1032).
- (between 13:51Z and 14:05Z; guessed time removed) step 2 in progress: read row 1046 (`library/gap-o2-extension.md`, in full) and the verdict parts of
  its two checks (`gap-o2-extension-check-opus.md` L130-220, `gap-o2-extension-check-astra.md` L124-191).
- (between 13:51Z and 14:05Z; guessed time removed) read row 1011 Section 2 and 7.1-7.5 ((M1)-(M8), Lemma FR, (N1)-(N3)); row 1032 L205-386 (B14, B15,
  kill table, ranking, Lemma BAR, CHAIN-4, NUC, CAS-0, GS, RISE, AMP, GS-dir, GS-eq) and the meaning + verdict parts of
  checks 1049 (`gap-afield-b-check-opus.md` L336-428) and 1050 (`gap-afield-b-check-astra.md` L442-514).
- (between 13:51Z and 14:05Z; guessed time removed) read (TB)_n in context (`gap-cr-tomboulis-max.md` L196-295, L370-409), the contract and (T-pin) of row
  1018 (`gap-short-step-max.md` L74-136), and the RESULT lines of checks 1033, 1037 and the astra checks of rows 1031, 1036.
- 2026-11-16 14:05Z (`date -u`): Sections 2 and 3 written (digests). Process slip: four log lines above carried times
  typed by hand; they were wrong and are replaced. From here every time is read from `date -u` in the same call.

## 2. Route (ii) at the pinned boundary after rows 1036-1048 (step 2; digest, no new mathematics)

Sources read: row 1046 `gap-o2-extension.md` in full; checks 1047 (`gap-o2-extension-check-opus.md` L130-220) and 1048
(`gap-o2-extension-check-astra.md` L124-191); row 1011 `gap-pinned-cell-gauge-max.md` Section 2, 3.1-3.5, 7.1-7.5; row 1018
`gap-short-step-max.md` 2.1, 2.3; the entries of rows 1034-1046 in `parts/gap.md` L145-149; RESULT lines of checks 1037 and
of the gpt-6-astra check of row 1036. Rows 1036, 1038, 1042 themselves were read through those entries and through row
1046's Step 1 (statements K1-K9), not line by line.

**What route (ii) is.** The gauge form of OpenAI's 2D pinned-cell chain (M1)-(M8) (row 1011 Section 2; all of the 2D
mathematics is OpenAI's). Objects (row 1011 3.1-3.2): a cell c (a box of Z^4), a pin omega on its boundary links,
F_c(omega) = - log Z_c(omega); a boundary link field B acts by left rotation; the response is the Hessian
H_c(omega; B) = E sum_p beta_p w_p (t_p abs(delta_p)^2 + kappa_p . s_p) - Var(X_c(B)) (Proposition A). For compact U(1) the
direct term is the classical curl energy at every pin. For SU(2) it is not (Propositions B, B', SEAG; Theorem BH of
row 1016): the supremum over pins is mass-like. Route (ii) tries to restore a classical direct cost by twisting along
a colour frame n(omega) (unit vectors on the sites, gauge covariant), theta -> theta n.

**The consumer** (row 1046 5.1, HOLDS as a reading in check 1047 L132): the start bound

  (S)  H_c(omega; theta_bd n(omega)) <= Q_V(theta) <= C sum_p w_p (d theta)_p^2 for every link field theta of the cell,

for the cells of a tiling and the pins the ring law produces, with one frame rule, one linear extension rule and C the
classical constant times a blind factor. After (S) the route needs (row 1011 7.4, L488-501):

- **(N1)** "A frame on typical ring configurations. A gauge-covariant, ring-measurable frame whose defect is small on
  the cells of the tiling, with the rare cells where it is not small controlled". In the wording of row 1046: (S) at
  the pins that carry the measure.
- **(N2)** "The cancellation of the mass-like term. An exact or controlled Ward identity for the U(1) about the frame".
- **(N3)** "The gain": a variance lower bound through the bracket of Proposition W and the shell sum (1/(8 pi^2)) log.
  Only (N3) is selective.

**What rows 1036-1046 established** (each as it stands after its two checks):

- A boundary gradient of a frame is a gauge move plus a pin move (Theorem GR, row 1036; Lemma GR+ on the whole boundary,
  row 1046 6.1): H_c(omega; (d lambda) n) = (d/d eps)^2 F_c(omega_eps), omega_eps,l = exp(- eps lambda_y n_x) omega_l exp(eps lambda_y n_y).
- In the class of smooth flows the least cost over extensions equals the response at every pin and for every
  boundary field (Theorem EXT, Lemma POLY; group-blind). So the boundary half of (S) is one statement about H_c
  alone, (S') (Proposition EQ).
- On gradients the sign H_c <= 0 holds, with a strict margin, for one frame on small open pin sets P', P_2, P_3 near
  the pure-gauge orbit of one fixed cell, for beta below 3/2 or outside a discrete set (Theorems EXIST, O2-GR, O2-GR+),
  with a curl bound whose constant is not classical (CURL-P, CURL-Q). No measure estimate, no number.
- Lemma MEAN: for a frozen colour the response Hess f_H(theta)[lambda, lambda] has mean zero on every torus orbit, so the
  negative sign at one pin is paid for elsewhere on the orbit. Lemma AVG: a pin set of probability p gives
  p C sum (d theta)^2 + (1 - p) A_0 abs(theta)^2, a mass term unless p is near 1.
- Both checks: (W) does not move; the first missing consumer step is (N1); (O1) (the interior potential) is an
  independent open input; check 1047 precision 2: EXT does not help (N3), because a gain step has to fix its
  extension before it bounds a variance from below.

**Reading for this row.** The positive results are descents of F_c at special pins. None is a statement in the law of
the model. Lemma FR (row 1011 7.3, PROVED) says every frame has sum abs(D_l n)^2 >= NA(omega)/6, and at bare ring links
of coupling 2.3 to 2.6 the non-abelian content NA is of order one per site (ARGUED there). So at order-one coupling
"a frame with small defect on typical ring pins" does not exist at the lattice scale: (N1) can hold there only in a
form where the mass-like term is cancelled, not small, and that is (N2). Section 4 states this as the status of line A.

## 3. The far-afield rows 1031, 1032 and the other named lines (step 3; digest, no new mathematics)

Sources read: row 1032 `gap-afield-b-max.md` L205-386; checks 1049 (`gap-afield-b-check-opus.md` L336-428) and 1050
(`gap-afield-b-check-astra.md` L442-514); row 1025 `gap-cr-tomboulis-max.md` L196-295, L370-409; the entries of rows 1017,
1025, 1028, 1031 in `parts/gap.md` L138-144; RESULT lines of checks 1033 and of the gpt-6-astra check of row 1031; row 1007
`prior/gap-2don-proofs-read-opus.md` L44-176 (both posted 2D proofs).

Exact statements (quoted from the rows; anchors by `grep -n` at the time of writing):

- **B15, (INV), (UV-Cas)** (row 1032 L212-217, Lemma BAR L280-290). Lemma BAR: given D^+ finite at one size,
  (BDD-Delta) holds iff there are D_* and L_2 with: D^+(L) >= D_* implies D^+(2L) <= D^+(L) for all L >= L_2 in P.
  "(INV): for each g_* > 0 there is D_* such that D_j(n) >= D_* forces the torus of side n at beta_j to be in the
  weak-coupling domain of the account at the scale n, with running coupling at most g_*. (UV-Cas): in that domain
  D_j(2n) <= D_j(n)." Consumer: (BDD-Delta) only. Row 1032 L300: "B15 stops at (INV): one precise lemma, with no route."
- **(GS-CAS), (NO-CONST)** (row 1032 L340-341; Corollary GS). "(GS-CAS): for every eps > 0 there are L_eps in P and j_eps
  such that (L/a_j) c_j((L/a_j)^3) <= eps for all L >= L_eps in P and all j >= j_eps", c(B) = log lambda_0(B) - f abs(B) the
  deficit of the box; "(NO-CONST): Omega(D_0) contains no constant." Given (BDD-Delta), the two give (W), and (W) gives both.
- **GS-eq** (row 1032 L373-375): (W) iff there is L in P with D^+(L) < log 2 and Gamma_1^+(L) < eps_*(D^+(L)). Both
  checks: a restatement of (W) as a one-size certificate; "neither side is closer to a proof than (W)" (check 1049 L358).
- **Lemma CHAIN-4** (row 1032 L311-316): D = G_0 + G_1 + G_2 + G_3, all terms non-negative, G_0 = log(1 + S(a; a^3)),
  Gamma_1 = a c(a^3). **Lemma RISE** (L353): D(2a) <= D(a) + 15 Gamma_1(a).
- **(TB)_n** (row 1025 L241; the queue row says "row 1017", the statement is row 1025's Proposition BR):
  rho(Lambda; c(beta)) >= rho(Lambda(n); c^U(n)), the odd-flux weight of the Wilson model is at most that of the
  Migdal-Kadanoff model after n decimations. Row 1025 L385-394: the line reads one factor (Lemma FAC), so its
  conclusion is the flux half at one coupling; "(TB)_n is not blind"; "(TB)_n in the range where DEC needs it is the
  flux half itself".
- **(BDD-Delta), (LIOU)** (`gap-dichotomy.md` 1.3, 2.2; row 1017 L288): (LIOU) = no uniformly recurrent critical element
  in Omega(D_0); equivalent to (W) given (BDD-Delta). (BDD-Delta): no row has it as its target (`gap-dichotomy.md` L362).
- **Lines that a check names as open and the queue row's list does not name** (from `parts/gap.md` L93-99, L137-150):
  1. a soft proof of (BDD-Delta) on torus data is NOT excluded (gpt-6-astra check of row 1031: NR-II's broad no-go
     FAILS at its line 892; check 1033: FAILS as a PROVED claim);
  2. C1 (corner twist) and C2 (non-central path to the centre twist) of row 1013: their exclusions are "not
     established" (gpt-6-astra check of row 1013, items 12-17), open with no mechanism;
  3. the integrated-flow, quotient and ABS-flow forms of row 970 (not refuted; gpt-6-astra check of row 970);
  4. geometry-varying routes (rows 960, 963, 965; the conditional ratio-4 HC/BR-J seed route HOLDS as conditional);
  5. the reformulation route of row 1016: "the claim that no other rigid group exists and the broad reformulation
     no-go are NOT proved" (gpt-6-astra check of row 1016);
  6. (O1), a finite-range site frame with j - d conserved and square integrable (row 1034);
  7. (E0-tor) (gpt-6-astra check of row 993); (R-pt) of row 1021; (EV-STEP) of row 731; (PLATEAU) of row 1028;
  8. (T-pin) with (FL), (DEC), and (T-vor) with (SER), (SPR) (row 1018 7.3).

**One fact from row 1007 that the rows after it did not use** (found while reading; it shapes Section 5). The lane's
transfer rows (1009-1011, 1016, 1018, 1026-1046) port OpenAI's O(4) pinned-cell stiffness ITERATION. Row 1007 B(2) reads
a second OpenAI text, "Exponential decay in two-dimensional classical O(n) models" (2026-09-23), whose engine is not an
iteration: Proposition 3.1 there bounds the twist cost of ONE annulus, min_t Z(t)/max_t Z(t) >= 1 - C_beta/log N, by
(a) an exact identity W(dF) = W(B), B_e = (1/2)[F_x, F_y] + O(F^3) (an additive gradient of non-commuting rotations is
gauge equivalent to a commutator field), (b) a fourth-order inequality that bounds the response to a commutator field
by the square of the Dirichlet energies of its constituents, and (c) a family of plane waves on frequency shells
whose commutators add coherently to the twist while their costs add incoherently (row 1007 L129-133). Row 1007 B(4)
(L148): the seed is proved "for every N at once by a direct estimate in one annulus", no induction in scale, no
first-passage data. Row 1007 B(5) judged the 4D analogue "NONE directly". Section 5 re-opens that judgement at one
point: on the PIN SPACE of a gauge cell the boundary gauge group acts field-independently, and identity (a) holds
there verbatim (it is Lemma TAN of row 1046 at second order).

## 4. Tasks (1) and (2): the live lines, one paragraph each, with the worth-doing test and the ranking (step 4)

Marks in this section: READ = taken from the row and its checks; ARGUED = my judgement with its reason. No statement
here is a theorem of this row. "Renamed" means: the line restates (W), or one half of it, with no new input.

### 4.1 The lines

**Line A. (N1) at order-one coupling.** *Statement* (row 1011 7.4; row 1046 5.1): for the cells of a tiling and the
pins that the ring law produces, with one gauge-covariant frame rule n and one linear extension rule,
H_c(omega; theta n(omega)) <= C sum_p w_p (d theta)_p^2 with C the classical constant times a blind factor, the cells where it
fails being controlled. On gradients this is the sign H_c(omega; (d lambda) n) <= 0. *Consumer:* the start bound (S) of
the gauge form of OpenAI's pinned-cell iteration; then (N2), (N3), then a short step ((T-pin) of row 1018), then (CAS),
then (W). *What a proof would change in (W):* nothing by itself. (N1) is a blind statement (true for U(1) with the
constant frame); the selective step is (N3), and the last link, "small response gives decay of all observables"
((L3) of row 1018 2.3), has no statement on record. *On file:* existential (O2) with a strict sign on small open pin
sets near pure gauge (rows 1042, 1046; both checks HOLD); universal (Q-INV) and pin-uniform (O2) refuted (row 1036,
both checks); Lemma MEAN and Lemma AVG (row 1046); Lemma FR (row 1011): every frame has defect at least NA(omega)/6;
Corollary WN1 (row 1013; HOLDS after correction in the gpt-6-astra check): for the lab frame the score variance of
every link translation is at least 3 beta xbar abs(f)^2. *Renamed?* No. It is not the crux. It is a prerequisite that
sits before the crux, and at bare ring links of coupling 2.3 to 2.6 its sign form is false in the mean for every
frame whose move keeps the Haar measure (Section 5.1 below proves this; it is two lines beyond Corollary WN1).
*Kind:* with bare links, (K-one) and false in the sign form; with blocked frames it is the background field of
Balaban's account, a (K-flow) statement that holds only above the band (row 1013 6.2, ARGUED there).

**Line B. The barrier B15 with (INV) and (UV-Cas).** *Statement:* Section 3. *Consumer:* (BDD-Delta), the exclusion of
branch (II). *What a proof would change in (W):* (W) iff (LIOU) would hold without a hypothesis; the wall would be
the rigidity half alone. *On file:* Lemma BAR HOLDS (both checks): the barrier alone is (BDD-Delta) in other words.
(INV) "one precise lemma, with no route" (row 1032 L300); in the abstract class it is false (ARGUED there). (UV-Cas)
needs D to an error of order one on two tori at weak coupling, the grade of the open (E0-tor). *Renamed?* (BAR) alone:
yes, it renames (BDD-Delta). (INV) with (UV-Cas): no, it is a mechanism with two open inputs, and it does not touch
the selective half. *Kind:* (K-flow).

**Line C. (GS-CAS) with (NO-CONST).** *Statement:* Section 3. *Consumer:* (W), given (BDD-Delta) (Corollary GS).
*On file:* both checks: "a restatement of the rigidity requirement, not its solution" (check 1050 L483-484);
"(GS-CAS) is not easier than (Z-UNB): an upper bound on lambda_0 of a periodic box against the bulk is not variational"
(row 1032 L347). (GS-CAS) says that the Casimir energy of the periodic cube times its side tends to zero; for a
massless model it is a positive constant. *Renamed?* Yes: it is (LIOU) in ground-state form. GS-eq likewise.

**Line D. (TB)_n** (row 1025, Proposition BR; after Tomboulis, Kanazawa, Ito and Seiler). *Statement:* Section 3.
*Consumer:* the flux half at one coupling (T_flux), through the decimation line; then route RE, which still needs
the even step (EV-STEP). *What a proof would change in (W):* nothing directly (Lemma FAC with Lemma PT: the line reads
one factor). It would prove the area law for the centre-odd sector of Wilson SU(2) at every coupling, which is a
classical open problem in its own right. *On file:* (TB)_n is selective (fails for Z_2 at large beta, PROVED; for
U(1) at large beta, GIVEN Ito and Seiler); it sees the dimension through the flow; Proposition SIGN, Lemma PAR-T,
Identity MOV (row 1025; check 1029 no FAILS); three ways to prove it stop. Row 1025 4.4 point 3: "(TB)_n in the range
where DEC needs it is the flux half itself", so the step from the flux half to (TB)_n renames. By Estimate RATE
(row 1025 4.2, ARGUED) the decimation scale is not a fixed physical scale along the trajectory (the Migdal-Kadanoff
drop per doubling is 1/4 against the true 0.2575), so even a proof would be a statement at one coupling.
*Renamed?* Yes for the flux half at one coupling; it is not (W).

**Line E. (BDD-Delta) and (LIOU).** *Statement:* `gap-dichotomy.md` 1.3, 2.2. (W) iff both. *On file:* (LIOU) is
target-equivalent given (BDD-Delta) (Theorem CR; cross-provider HOLDS AFTER CORRECTION); every soft form of rigidity
fails (constants log m, products, Proposition SI); kept ultraviolet data is the wall (row 1028). (BDD-Delta): no row has
it as target; Lemma CHAIN-4 and Corollary NUC give its exact content (bounded counts of states of the periodic boxes
below the inverse side); Theorem CE-II; and the gpt-6-astra check of row 1031: the claim "no soft proof of (BDD-Delta)
on torus data" is NOT established. *Renamed?* (LIOU): it is the crux. (BDD-Delta): a genuine half, not renamed, open.

**Lines that the checks leave open and the queue row does not list** (Section 3, items 1-8), in one line each:

- **F. A soft proof of (BDD-Delta) on torus data.** Not excluded. No mechanism on file. Section 5.3 writes its exact
  content in one more form and says why the positivity tools point the wrong way.
- **G. C1 and C2 of row 1013.** The exclusions are not theorems (gpt-6-astra check, items 12-14). No mechanism for
  either. For C1 the family inequality "was never written" (item 13). Section 5.2 writes the reason the port of
  OpenAI's one-annulus engine fails in both of its exact gauge forms, and scopes it.
- **H. Flow forms of row 970; geometry-varying routes (rows 960-965); the reformulation route (row 1016).** Each
  "not refuted"; none has a supplier or a mechanism on record (`parts/gap.md` L97-98, L139).
- **I. (T-pin) with (FL), (DEC); (T-vor) with (SER), (SPR).** The exact shapes of the missing step (row 1018 7.3).
  (DEC) and the pair (SER), (SPR) are selective and have no mechanism; (L1) and (L3) of (T-pin) are open too.
- **J. (O1), (E0-tor), (R-pt), (EV-STEP), (PLATEAU).** Named open inputs of other lines. (E0-tor) is the one that
  two lines share (B through (UV-Cas); the (DET) and (HC-phys) reductions). It is a statement about the account.

### 4.2 The worth-doing test and the hardest-first rule

For each line: the critical-path item it moves, what changes if it succeeds, and where its proof could die.

| Line | Critical-path item moved | If it succeeds | Where it could die; cost to find out | Verdict (ARGUED) |
|---|---|---|---|---|
| A (N1) | none; it feeds (S) of route (ii) | route (ii) has its start bound on typical pins; (N2), (N3), (L3), (O1), tilings remain | it dies before the crux: sign form false in the mean for Haar-preserving frames (5.1); with blocked frames it is the account's object above the band | **stop** as a proof target at bare coupling; keep 5.1 as the scope of the stop |
| B (INV), (UV-Cas) | (BDD-Delta) | branch (II) excluded; wall = (LIOU) alone | (INV): no route; (UV-Cas) at the grade of (E0-tor) | not first; (E0-tor) is the cheap shared piece |
| C (GS-CAS), (NO-CONST) | (W) given (BDD-Delta) | the gap | it is (LIOU) | **renamed**; no row |
| D (TB)_n | flux half at one coupling | a classical theorem (area law of the odd sector at every coupling); not (W) | at the non-abelian sign of bond moving; no mechanism | off the path of (W); no row now |
| E (LIOU) | (W) | the gap | it is the crux; no mechanism | no direct row |
| F soft (BDD-Delta) | (BDD-Delta) | as B | 5.3: needs a lower bound on a glued partition function; reflection positivity gives only the upper bound | one short row could decide whether a soft form exists; see 7.2 |
| G C1, C2 | none without a consumer | - | 5.2 | **stop**; one check row for 5.2 |
| I (DEC); (SER), (SPR) | (CAS) through a short step | the gap, if (L1), (L3) also hold | at the blind half first (5.2, Lemma BL-need) | the blind half is the cheap decisive test: 7.1 |

**Hardest-first.** The place where every stiffness-type line (A, G, I, and the 2D ports of rows 1009-1048) can die
cheaply is not its selective half. It is its blind half: in 2D the bound "response at most the coupling times the
classical cost, at every pin and every scale" is one line (drop the variance); in 4D it is not on record at any
scale inside the band, for any pin class, and every positivity tool the lane has bounds the response from below,
not from above (5.2). If the blind half has no proof, no selective gain can be iterated, and those lines stop
together. So the first row should attack the blind half in its smallest exact form (7.1). The selective half and
(LIOU) are harder, but no mechanism is on record for them, so a row there would restate the crux (the lead's own
rule in `parts/gap.md` L87-89).

## 5. Task (3): the top lines, tried by hand (step 5)

Everything marked PROVED in this section is written by hand by Claude Fable 5.2 in this row and is checked by nobody.

### 5.0 Registry grep before the attempts (rule 0a; done 2026-11-16 14:20Z to 14:30Z by `date -u`)

- `library/open-core.md` (the T0 registry, last changed 2026-11-06): no entry for (N1), (N2), (N3), (O2), (BDD-Delta), a
  blind bound, a Schrodinger-functional response, a score variance or a ring law (`grep -n -i` on those terms: two
  unrelated hits, L227 and L526).
- FINISH rows and `library/`: the mean identity of 5.1 is on file for a FIXED lab-frame boundary field as Identity AV
  (row 1016, `gap-global-reform-max.md` L693-707; no WRONG in check 1020; Theorem BH HOLDS AFTER CORRECTION in the
  gpt-6-astra check). Corollary AV2 and Theorem BH there give the lab-frame value. I do not attack those. What 5.1
  adds is the form for frame moves (a field that depends on the pin) with the Jacobian term.
- The corner form of the port of OpenAI's one-annulus engine is C1 of row 1013 (Lemma WN, Corollaries WN1-WN3). The
  finite identity of 5.2 is Lemma TAN of row 1046 (stated there to second order). I do not attack C1. What 5.2 adds
  is the pin-space form at all orders, the exact cost form on a slab, and the count.
- (BDD-Delta): named open by rows 720, 982, 1017, 1024, 1031, 1032; no row has it as target. Lemma CHAIN-4, Corollary NUC,
  Lemma RISE (row 1032) and Theorem CE-II (row 1031) are its exact forms on file. 5.3 states no new lemma on it.

### 5.1 Line A: the mean of the response to a frame gradient (Lemma RM; PROVED)

**Setting.** X = G^E for a finite set E of links, G = SU(2) (any compact Lie group serves), mu the Haar probability
on X. Phi is a smooth real function on X, Z = int e^(-Phi) d mu, and rho = e^(-Phi) mu/Z. Let S_eps, abs(eps) < eps_0, be
diffeomorphisms of X, smooth in (eps, omega), with S_0 the identity. J_eps > 0 is the Jacobian of S_eps for mu:
int g d mu = int (g o S_eps) J_eps d mu for continuous g. Write Phi' and Phi'' for the first and second eps-derivative
of Phi(S_eps omega) at 0, and l', l'' for those of log J_eps(omega).

**Lemma RM.** (i) E_rho[Phi'] = E_rho[l']. (ii) E_rho[Phi''] = E_rho[(Phi' - l')^2] + E_rho[l''].
(iii) If every S_eps keeps mu (J = 1), then E_rho[Phi''] = E_rho[(Phi')^2] >= 0, with equality only if Phi' = 0 at
every point of X.

Proof. Z = int exp(-Phi(S_eps omega) + log J_eps(omega)) d mu(omega) for every eps (change of variables). X is compact
and the integrand is smooth, so the eps-derivatives pass under the integral. The first derivative at 0 is
int (-Phi' + l') e^(-Phi) d mu = 0: (i). The second is int [(-Phi' + l')^2 - Phi'' + l''] e^(-Phi) d mu = 0: (ii). (iii) is
(ii) with l = 0; Phi' is continuous and rho has full support. QED

Not new in kind: for S_eps = left translation of the boundary links of one cell by a fixed field it is Identity AV
of row 1016 (credited). In the words of Lemma FLOW (row 1018 4.1), Phi' - l' is minus the score Psi_V of the flow.

**Use for route (ii).** A cell Q with pin Omega, tiled by cells c with the weights of row 1011 3.1. E = the ring links
of the tiling that are not in the boundary of Q. Phi(omega) = sum over c of F_c(omega_c). By the Markov property (row
1011 3.1) rho is the law of the inner ring links in the pinned law of Q. Let n_x(omega) be unit vectors on the ring
sites, smooth in omega, and lambda a real function on the ring sites that vanishes on the boundary of Q. Put

  S_eps(omega)_l = exp(- eps lambda_y n_x(omega)) omega_l exp(eps lambda_y n_y(omega))   for a ring link l = (x -> y)

(the frame is frozen at omega along the curve; the links in the boundary of Q do not move). For small eps these
are diffeomorphisms (a smooth family through the identity on a compact manifold). By Lemma GR+ (row 1046 6.1 (c),
HOLDS in both checks), cell by cell, Phi''(omega) = sum over c of H_c(omega_c; (d lambda) n(omega)). So

  (RM-fr)   E[ sum_c H_c(omega_c; (d lambda) n) ] = E[(Phi' - l')^2] + E[l''].

**Corollary RM-TREE (PROVED).** Let n be a frame transported from one base point: fix a spanning tree of the ring
graph and a root x_0, and let n_x = Ad(W_x) a, W_x the product of the link variables along the tree path from x to
x_0 (so D_l n = 0 on tree links). Then every S_eps keeps mu, and for every lambda as above

  E[ sum_c H_c(omega_c; (d lambda) n) ] = E[(Phi')^2] >= 0,

with equality only if the ring action Phi is stationary along the frame move at every ring configuration.
Proof. On a tree link l = (x -> y), n_x = Ad(omega_l) n_y gives exp(- eps lambda_y n_x) omega_l = omega_l exp(- eps lambda_y n_y),
so S_eps fixes the tree links. Hence W_x and the frame do not change along the move. Given the tree links, S_eps acts
on each other link by one left and one right translation with fixed elements. These keep Haar measure, and Fubini
gives J = 1. Then RM (iii). QED
The same proof gives the one-cell form: in the free ensemble of row 1016 7.1 (boundary links of c with density
Z_c/Z_free), for a tree in the boundary and every lambda on the boundary sites,
E_free[H_c(.; (d lambda) n)] = E_free[(F_c')^2] >= 0. This extends Identity AV from fixed lab fields to this frame.

**What it says about (N1).**
1. For the frame of row 1038 (transported from one base point; "the fixed colour in axial gauge") the response of
   the cells to an interior gradient has non-negative mean in the law of the model. The consumer needs that mean
   to be at most 0 (the right side of (S) vanishes on gradients). So for this frame (S) holds in the mean on a
   gradient only if the ring action is exactly invariant under the move. For cells of side 1 the ring action is
   minus the Wilson action (no interior links; the weights w_p of the cells that contain a plaquette add to 1 inside
   Q). It is not invariant as soon as one plaquette has two non-tree links l_1, l_2 whose heads carry different values
   of lambda (PROVED for the pin Omega = 1: take the configuration with all tree links and all other non-tree links
   equal to 1; the move conjugates l_i by exp(eps lambda_i a) and fixes the links equal to 1; every plaquette but
   the one through l_1 and l_2 is then a constant or a class function of one link, and that one has derivative
   (lambda_1 - lambda_2) Re(U_1 [a, U_2]) up to orientation, which is not 0 for generic U_1, U_2). For
   larger cells invariance fails for all beta outside a discrete set (ARGUED: Phi is analytic in beta and equals
   minus the Wilson action of the ring plaquettes at first order in beta; the step is not written out).
2. So "the sign at the pins that carry the measure" is not available for a frame whose move keeps Haar measure. The
   negative signs of rows 1042 and 1046 at special pins are paid for elsewhere, now in the law of the model and not
   only on a torus orbit (Lemma MEAN is the Haar form of this).
3. For a general covariant frame the exact condition is (RM-fr): the mean is at most 0 only if E[l''] <= - E[(Phi' - l')^2].
   The frame move must contract Haar volume at second order by at least the variance of its weighted score. No frame
   on file has a computed l''. A row on (N1) would have to supply this inequality; nothing suggests it holds.
4. Scope. RM is an identity. It refutes no frame other than those with J = 1, and for those only the mean-sign
   form on gradients. It does not bound E[(Phi')^2] below by a number (for the lab frame Theorem BH of row 1016
   does). It says nothing about co-closed fields.

Mark: Lemma RM, (RM-fr), Corollary RM-TREE: PROVED (given Lemma GR+ for the identification of Phi''). Item 1's
"outside a discrete set": ARGUED. Verdict for line A: (N1) in its sign form FAILS in the mean for frame TREE (and
for the lab frame by rows 1013 and 1016); for other frames it is OPEN and equivalent to a Jacobian inequality.

### 5.2 Line G: the port of OpenAI's one-annulus engine, in its pin-space form (identity PROVED; verdict ARGUED)

Row 1013 ported the engine of OpenAI's "Exponential decay" text to link-end translations (C1) and found a
site-local cost (Lemma WN). There is a second exact form, on the space of pins of one cell, where the group that
acts without reference to the field is the gauge group of the boundary sites.

**Proposition PIN (PROVED; the finite form of Lemma TAN of row 1046; the idea is OpenAI's (2.10)-(2.12)).** Any cell
c, any pin omega, any function F from the boundary sites to su(2). For a boundary link l = (x -> y) put
Y_l = Ad(omega_l) F_y, (d_omega F)_l = F_x - Y_l, and E_(F,l) = exp(- F_x) exp(F_x - Y_l) exp(Y_l) in SU(2). Then

  Z_c( exp(d_omega F) omega ) = Z_c( E_F omega ),

where exp(d_omega F) omega and E_F omega are the pins with links exp((d_omega F)_l) omega_l and E_(F,l) omega_l.
Proof. Gauge covariance Z_c(omega^g) = Z_c(omega) (row 1011 3.1) with g = exp(F), applied to the pin E_F omega:
g_x E_(F,l) omega_l g_y^(-1) = exp(F_x) E_(F,l) exp(- Y_l) omega_l = exp(F_x - Y_l) omega_l. QED

Consequences. For small F write E_(F,l) = exp(B_(F,l)); by the Baker-Campbell-Hausdorff series B_(eps F) = eps^2 B_2 + eps^3 B_3
+ eps^4 B_4 + ..., with B_(2,l) = (1/2)[F_x, Y_l] = F_x x Ad(omega_l) F_y. With f(B) = Z_c(exp(B) omega), comparing Taylor
coefficients of f(eps d_omega F) = f(B_(eps F)):

  (P2)  (1/2) D^2 f(0)[d_omega F, d_omega F] = D f(0)[B_2],
  (P4)  (1/24) D^4 f(0)[d_omega F, d_omega F, d_omega F, d_omega F] = D f(0)[B_4] + (1/2) D^2 f(0)[B_2, B_2].

(P2) is Lemma TAN. (P4) is the gauge form of OpenAI's fourth-order identity: the second-order response to a
commutator field is a fourth-order response to additive covariant gradients, plus a force term. At an abelian pin
(all omega_l = exp(alpha_l sigma_3)) with F in the plane of sigma_1, sigma_2, written as a complex function phi, B_2 is the
field along sigma_3 with coefficient Im(conj(phi_x) e^(2 i alpha_l) phi_y) up to the sign convention. So commutators of
transverse gauge parameters generate abelian boundary fields, as in the spin model.

**Lemma SF-D (the cost form is the Dirichlet form of the boundary; PROVED).** Slab (Z/L)^3 x {0, ..., T}, homogeneous
beta, the spatial links of the slices 0 and T pinned to 1, everything else integrated; E the pinned expectation.
For a top link l let p(l) be the one interior plaquette that contains l, and xbar_1 = E[t_(p(l))] (the same for all
top links, by the symmetries of the slab). For a field B on the top links let X(B) = - sum_l B_l . N_l (row 1011,
Proposition A (iii)). Then:
 (a) E[N_l] = 0 for every top link;
 (b) for every F on the top sites: E[X(dF)^2] = beta xbar_1 sum over top links of abs(F_x - F_y)^2;
 (c) for a real field h on the top links with zero curl on the top plaquettes (for example the constant field on
     the links of one direction): - D^2 f(0)[h sigma_3, h sigma_3]/f(0) = beta xbar_1 sum_l h_l^2 - E[X(h sigma_3)^2] <= beta xbar_1 abs(h)_2^2.
Proof. (a) The pinned law is invariant under U -> k U k^(-1) for constant k (the pins are 1), and N_l -> Ad(k) N_l, so
E[N_l] is fixed by every rotation. (b) D^2 f/f = E[X^2] + E[D^2 A]. By Proposition A (i) of row 1011 a top plaquette
contributes - beta w abs(delta_p)^2, which is 0 for B = dF at the pin 1 (the four differences cancel), and the plaquette
p(l) contributes - beta abs(B_l)^2 t_(p(l)); no other plaquette contains a top link. By (P2) and (a),
D^2 f[dF, dF] = 2 D f[B_2] = 0. (c) The same count for B = h sigma_3: the top plaquettes contribute
- beta w (dh)_p^2 = 0. QED

So at the trivial pins the blind bound of the abelian boundary twist is exactly beta xbar_1 abs(h)_2^2. For the
twist of unit holonomy (h = 1/L on the L^3 links of one direction) it is beta xbar_1 L. The classical action of the
same twist in the slab with T = L is of order beta, with no factor L. This is Lemma JEN of row 1013 with its
constant, for this pin (the gpt-6-astra check of row 1013, item 17, asked for a normalised profile; this is one).

**The count (ARGUED).** Suppose a fourth-order inequality of OpenAI's type holds on pin space: the response to
Q = sum_i S(phi_i, conj(phi_i)) is at most K times the sum of the squares of the pair energies
E_i = beta xbar_1 abs(d phi_i)_2^2 (their Proposition 2.2 after Fourier orthogonality; I do not prove the gauge form).
Boundary waves phi_i = eps exp(i k x) have S = eps^2 sin(k . e_l) on the links of direction e_l. A shell of M modes with
abs(k) of order r/L on a boundary of dimension b has M of order r^b. To reach h = 1/L one needs M eps^2 r of order 1.
The bound for the response to h is then of order

  K M (beta eps^2 (r/L)^2 L^b)^2 / (M eps^2 r)^2 = K beta^2 r^(2-b) L^(2b-4).

For b = 2 (the 2D spin model, where the "boundary" is the lattice itself) this is K beta^2 for every shell, and the
log N independent shells give OpenAI's 1/log N. For b = 3 (a 4D gauge cell) it is K beta^2 L^2/r, at least K beta^2 L,
which is above the blind bound beta xbar_1 L of Lemma SF-D. Combining shells does not help: the harmonic combination
of the shell bounds is again of order K beta^2 L. So on pin space the family inequality gives nothing.

**Why both exact forms fail, in one sentence (ARGUED).** In the corner form and in the pin-space form the moves whose
action does not depend on the field are gauge parameters, that is functions on sites; their commutators make
link fields at the cost of a Dirichlet form on the set where they live (one site for corners, the 3-dimensional
boundary for pins). The 4D count that is scale invariant (row 1011 3.4: a harmonic sum of abs(k)^(-4)) needs moves
that are link fields with a cost that is a curl form, and for those no family with a field-independent action is
on record (Lemma WN; Lemma CEN+ of row 1016).

Mark: Proposition PIN, (P2), (P4), Lemma SF-D: PROVED. The count and the sentence: ARGUED. Scope: the count
assumes the form of the fourth-order inequality; it does not exclude an inequality of another form; it concerns
the trivial pins of a slab. Verdict for line G: the pin-space form of C1 FAILS as a route to an L-uniform bound
(ARGUED); C1 in corner form and C2 stay as the gpt-6-astra check of row 1013 left them.

### 5.3 The blind half (the line this row ranks first): statement, what the attempts give, what is left

**Four statements of one kind (not claimed to be equivalent).** Each says that the theory at scale L is not more
ordered than a free massless theory with a coupling bounded below. Each holds for compact U(1). They differ in
what they exclude (ARGUED): (BDD-Delta) excludes infrared freedom only (it holds for frozen Z_2, where D tends to a
constant); (BL-c) also excludes the branch with degenerate flux sectors, the constants log m of rows 1017 and 1028;
(BL) and (L1) need a continuous twist and have no form for a finite group.

- (BDD-Delta), periodic: D^+ is bounded on the large sizes of P. Exact content: bounded counts (Corollary NUC).
- (BL), slab: for the slab of Lemma SF-D with T = L, top pin exp(i t sigma_3/L) on the links of one direction and
  Z(t) its partition function: sup over t of - Z''(t)/Z(t) <= C(beta) for every L.
- (BL-c), periodic and frame-free: the 't Hooft twisted partition function of the symmetric torus has
  Z_tw(L^4)/Z(L^4) >= c(beta) > 0 for every L (a bounded vortex free energy).
- (L1) of (T-pin): Rbar(L l) <= C Rbar(l) (row 1018 2.3, "OPEN").

**What is proved, by model.** Compact U(1): (BL) with C of order beta, and the analogue of (BL-c) for the twist of a
co-closed sheet by any angle alpha, hold by one line: shift the links so that the twist is spread evenly over the
L^2 plaquettes of each plane, an exact change of variables, and use Jensen; the cost is at most beta alpha^2/2 (the
abelian form of row 1011 3.2). Frozen Z_2 at large beta: (BL-c) is false; the twisted ratio tends to 0 (the lane's
Peierls bound, `parts/gap.md` L219; the rate exp(- c beta L^2) is RECALLED). SU(2): Lemma SF-D gives beta xbar_1 L for
(BL) at t = 0; Jensen on a thin sheet gives the lower bound exp(- 2 beta xbar L^2) for the ratio of (BL-c). In the files
read for this row nothing L-uniform is on record for SU(2) outside the couplings where the lane has a seed (the
ceilings of `parts/gap.md` L227).

**The attempts of this row, and of the lane, at an L-uniform bound.**
1. Lab frame, extension by zero: exactly beta xbar_1 L (Lemma SF-D (c)). FAILS (PROVED value).
2. Temporal-gauge frames (the colour carried down the time links; a Haar-preserving flow by the argument of
   RM-TREE). The time-like plaquettes then cost beta (theta_j - theta_(j+1))^2 per link, the classical form, and the
   space-like plaquettes of the slice at depth j cost of order theta_j^2 min(j, beta) per plaquette, because the
   links of that slice have drifted from the frame by j/beta. The twist then enters to a depth of order beta^(1/3) and
   the bound is of order beta^(2/3) L. FAILS (ARGUED; the depth beta^(1/3) is row 1013's kill of C8).
3. Commutator families on pin space: no gain (5.2). FAILS (ARGUED).
4. Positivity. Reflection positivity bounds a twisted or glued partition function from above (chessboard,
   Z((2a)^4) <= Z(a^4)^16; Gaussian domination, Theorem D2). All four forms need a bound from below. The only
   exact tool for that on file is a flow: H_c = inf over flows of Q_V (Lemma FLOW; Theorem EXT of row 1046), and
   Jensen. So the blind half asks for one flow whose cost is classical, at every scale of the band.
5. Such a flow needs a colour direction that is parallel, to accuracy 1/L, for the fluctuating links of the cell
   (the count in attempt 2). Bare links are not that smooth at any coupling of the trajectory (Lemma FR). Blocked
   links are, where the account controls them. So the blind half is on record above the band only (ARGUED; it is
   Balaban's extraction of (1/g_k^2) A(U_k(V)), CMP 109, as row 1013 5.1 says).

**Reading (ARGUED).** (i) The lane has looked for the selective half since row 988. The blind half is as open as
the selective half inside the band, and the 2D proofs get it for free. A 4D engine of the 2D kind therefore lacks
both halves, not one. (ii) The blind half is where the SIGN of the response to gauge fluctuations sits (they do not
screen), and (LIOU) is where its strictness sits. Scalar matter screens (the diamagnetic inequality of Brydges,
Frohlich and Seiler gives the opposite sign for a charged scalar; RECALLED), so the blind half is not a soft
property of gauge models with matter; inside the pure-gauge class no model on record violates it in four
dimensions. (iii) By (i) a proof of (BDD-Delta) or of (BL) inside the band would be the first statement of any kind
that enters the band from the weak side. That is the reason to rank it first: it is strictly easier than the wall,
it is a genuine half of the trichotomy, and the 2D analogy says it should be the easy part.

No mechanism for the selective half was invented in this row. No mechanism for the blind half was found either;
attempts 1 to 3 are the counterexamples to the three obvious ones.
