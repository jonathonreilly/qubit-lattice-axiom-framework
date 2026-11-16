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
