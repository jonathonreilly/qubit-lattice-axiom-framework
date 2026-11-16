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
- 2026-11-16 13:58Z: step 1 read done: `parts/gap.md` (257 lines, in full) and `library/gap-dichotomy.md` (473 lines, in
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
- 2026-11-16 14:06Z: step 2 in progress: read row 1046 (`library/gap-o2-extension.md`, in full) and the verdict parts of
  its two checks (`gap-o2-extension-check-opus.md` L130-220, `gap-o2-extension-check-astra.md` L124-191).
- 2026-11-16 14:12Z: read row 1011 Section 2 and 7.1-7.5 ((M1)-(M8), Lemma FR, (N1)-(N3)); row 1032 L205-386 (B14, B15,
  kill table, ranking, Lemma BAR, CHAIN-4, NUC, CAS-0, GS, RISE, AMP, GS-dir, GS-eq) and the meaning + verdict parts of
  checks 1049 (`gap-afield-b-check-opus.md` L336-428) and 1050 (`gap-afield-b-check-astra.md` L442-514).
