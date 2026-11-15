lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-16T09:19Z

# Queue row 1021, `gap-registry-after-checks-max`: the route registry after the fourteen cross-provider checks, then an attack on the top route

Worker: Claude Fable 5.2 (max), Mac mini worker 1, pinned at commit ae561a40d of `claude/ym4d-hard-route`.
Started 2026-11-15T21:19Z (`date -u`). Research-stage working state. Nothing here is a public claim, and
nothing here is checked by another model.

Marks used: PROVED (every step written here, by hand), ARGUED (argument written, a step is not complete),
OPEN, FAILS (a counterexample or a failed step is written). GUIDE marks a numeric run; a run can refute
or guide, and no status rests on one.

## 0. Plan (save protocol; at most eight steps, one step per response, result appended after each)

1. Read `parts/gap.md` in full. Fetch the exercise skill at main commit 8b11ae2bb9 and the reference
   file it names into a new folder under /tmp. Write down its registry and ranking steps and its tests.
2. Read the RESULT lines and verdict tables of the fourteen gpt-6-astra checks (rows 960, 963, 965,
   968, 970, 977, 978, 982, 987, 988, 993, 996, 998, 1000). Record each verdict with its line anchor.
3. Read today's rows 1011, 1013, 1016, 1017 and their checks 1014, 1015, 1019, 1020 (RESULT lines and
   verdict tables). Record (W), Theorem CR and (LIOU) with anchors. Row 1018 (short-step hunt) is not redone.
4. Task (1): the table of every discard verdict, filter and lead rule the lane relies on, with its
   status after the checks: stands, narrowed (to what), or no longer supported (by which check line).
5. Task (2): the route registry rebuilt from that table: terminal obligation, strength against (W) or
   Theorem CR, status, cheapest decisive next step, rank, and which routes were blocked only by a
   verdict that no longer stands.
6. Task (3a): the top route. Registry grep first (`library/open-core.md`, FINISH rows). Then the first
   lemma, stated in full, and the first attack by hand.
7. Task (3b): continue the attack, or build the counterexample; a numeric run only to refute or guide,
   under the numeric lock.
8. Re-read every item marked PROVED here, print each cited line anchor, write the work-item briefs and
   the RESULT line.

## Status log

- 2026-11-15T21:19Z: file created with the plan. Nothing else done yet.

## 1. Step 1: the skill's procedure, and the state file

Read in full: `parts/gap.md` (242 lines, 29.7 KB, at the pin); the exercise skill `SKILL.md` at main commit
8b11ae2bb9 (704 lines) and its one reference `proof-search-governance.md` (127 lines), both fetched by raw
URL into `/tmp/row1021-skill/`. The target is a standalone proof target, so `GOAL.md` and the FINISH rules
replace the skill's framework refresher list (skill L130-132). No subagents, so there is no blind check
and no independent pass; every statement of this file is `argued` at most in the skill's words.

**1.1 What the skill asks of a registry (used in Sections 4 and 5).**

- A family is the triple (object or formulation, load-bearing mechanism, terminal proof obligation), never
  an agent, a wording or an artifact type (governance L34-44).
- Registry columns: family, object, mechanism, terminal obligation, strength against the target (weaker,
  unknown/comparable, target-equivalent, stronger), status (unexplored, active, provisional, blocked-local,
  blocked-equivalent, retired, candidate-complete), concrete evidence, reopen condition (governance L46-56).
- Theorem-strength gap test for each terminal lemma L and target T: state L, test L => T, test T => L,
  classify. A target-equivalent or stronger L is `blocked-equivalent` unless the route brings a new
  mechanism for L (governance L85-100).
- Rank by what the route would change if it worked, divided by the cost to find out; a cheap test that
  moves an owner decision outranks an elegant reduction that ends at a target-equivalent lemma (skill L590-592).
- Before an attempt, search the open registry and the queue; if another row holds the statement, stop and
  name the match (skill L600-602).

**1.2 The valid form of a discard test (skill 6c, L437-490; used in Section 4).**

- A tool is a hypothesis H with a written proof of "H(M) implies T(M)" on a class K containing our model.
- Refutation: a model M' in K with H(M') true and T(M') false, for the same T.
- Constraint: for a tool with a written proof, T(M') false gives H(M') false; the test then says what a
  proof of H must use. It does not refute the tool.
- No refutation when: the proof also runs for M' and T(M') is true; M' is outside K; T(M') fails for another
  constant, quantifier or range; H(M') is not known.
- Range form: if H is blind to the difference of M and M' at a parameter value, a sound tool proves nothing
  for M wherever T(M') fails. So each test has a range.
- Other reasons: "circular" is not circular for an induction on a smaller case; "needs a small number" is
  valid as a range only; "was tried" rules out nothing.
- A verdict not re-derived is "valid as reported; not re-derived" (skill L502-503). A pass is no support.

**1.3 The state file `parts/gap.md`, the points this row reads.**

- The wall (W), verbatim at L18-20: "There is a physical size L in P with z^-(L) > 256 D_0 + 30, where D_0
  bounds D^+ on the sizes from L/4 on." Price at L231-242: (W) iff (BDD-Delta) and (Z-UNB) (Theorem ZD-c,
  row 720); (W) follows from (CAS) with theta < 1 and an extensive base (rows 708, 978).
- Route registry of row 998 (seven families RA-RG) at L148-177. Test table at L188-229.
- Lead rules in force at L88-96. Rule W2 (kinds (K-one), (K-flow)) L90. Row 982 N2: UNSUPPORTED since
  2026-11-15 (L91). Row 1002 filter WITHDRAWN (L92). The 2D mechanism and rows 1011, 1013 (L93). "Not refuted"
  notes: the integrated-flow, quotient and ABS-flow forms of row 970 (L94); the geometry routes of rows 960,
  963, 965 and the conditional ratio-4 HC/BR-J route (L95). RA's reopen candidate (L96).
- Obligations L98-136, among them: Theorem CR and (LIOU) (L135, row 1017, same-provider check 1019); (E0-tor)
  open (L134); T3 argued only (L124 with L91); Theorem D2 HOLDS AFTER CORRECTION cross-provider (L126).

## 2. Step 2: the fourteen gpt-6-astra checks, verdict by verdict

Read for each check: its verdict table (or final-verdict section) and its RESULT line, not the full file.
Line numbers are those of the check file at the pin. "Row n" is the checked row. Each check is one reading
by one other model; it grants no status.

**2.1 Row 960 (`gap-vargeom-opus.md`), check `gap-vargeom-check-astra.md` (verdict register L355-418, RESULT L452).**

- HOLDS: Lemma Q, SH' with threshold 1/550 at ratio 2 and even a (L392); the HC table and the BR-J consequence
  after correction (L396); the conditional ratio-4 HC/BR-J seed route, K_30 about 0.811 at beta 2.3 (L452);
  SEED-FP composition (L398); DEN as one E2 denominator substitution (L377).
- FAILS: G3, the exclusion of projected averaging (explicit normalized-Haar-average counterexample, L373);
  OVL for all trial times or all lenses (L390); the q = 1.6 ordering (L393: q = 8/5 is strictly better than
  q = 3/2 on the proved interval); "each valid in the whole class" (L404); **the global no-gain and
  stop-queuing recommendation (L408): "The support does not exclude the advertised route family. The narrower
  result is that this note supplies no improving variable-geometry bound."**
- Narrowed: DEN's "no room" use holds for one one-side, seed-time comparison only, at most g/23 (L378); the
  dominance table gives no new rectangular numerator bound and does not prove absence of other comparisons (L385).
- Open as before: the seed and (LSI-J-seed) (L409).

**2.2 Row 963 (`gap-rotgeom-opus.md`), check `gap-rotgeom-check-astra.md` (verdict map L314-362, RESULT L370).**

- HOLDS: R1-R4 (twists, mapping torus, characters), frozen trivial-sector counts, the local diagonal reflection
  positivity argument, straight-torus non-separation for N >= 3, Lemma M (no light-cone mirror among lattice
  hyperplane reflections), D2 on the displayed period lattice, same-state conditional D4.
- FAILS: "every sector form fails all rivals" (L338: nonzero-momentum frozen sectors are empty); "no coordinate
  mirrors or axis operators" (L343: an explicit invariant period lattice, and D2's twisted axis channel);
  "same finite thermal sum; only bulk-pressure bridge" (L350); "every seed form passes the fact-test filter"
  (L352); **the three-part "buys nothing" verdict (L355): replace by "no sufficient replacement is established
  here"**; the final result as a blanket obstruction (L362).
- Not supplied by the check (L364-367): (LSI-J-seed), (SEED-FP), a diagonal finite-torus transfer construction,
  an admissible diagonal recursion, shape independence, a projected seed consumer.

**2.3 Row 965 (`gap-squeeze-opus.md`), check `gap-squeeze-check-astra.md` (dispositions L322-357, defects L359-378, RESULT L394).**

- HOLDS (mostly after correction): COUNT on its schedule, BND, SHELL, FLUX, LEAK, PR/window, HALF, QF, the
  free-plaquette endpoint bounds (with 0.03019, 0.03694), the cube static formula, the one-link ceiling 3.
- FAILS: "doubled time for the full SU(2) seed" as an established consequence (overlap input missing, L340);
  top-level periodic r_1^w (L344); literature-to-J equivalence as a supplied implication (L345); the frozen
  centre-even-gap assertion (flat-state construction, L348 and defect 5); the quantitative full-window claim for
  the open endpoint (L349); **"every averaged squeeze is unchanged / every computable endpoint harder" (L356,
  defect 8): "a computable endpoint does not logically force a supremum over exterior data, and no such
  necessity theorem appears."**
- To retain (L379-383): "none of the displayed estimates supplies a new seed bound". Not to retain: the request
  to stop all squeeze lanes; the claimed equivalence of the pointwise-in-beta target to the seed; that EP1
  settles every open-box obstruction.

**2.4 Row 970 (`gap-direction2-max.md`), check `gap-direction2-check-astra.md` (final verdicts L209-231, RESULT L248).**

- HOLDS: SUB (exact temporal-gauge law); FH (a)-(d); QUOT, conditional on the flow identity and BR, with no
  supplied seed rate; ROTOR and TIE (a)-(c) as model statements; the SLAB implication; CLASS (a)-(c) given
  convex-domain Brascamp-Lieb; TRAJ and the MM/Markov step after correction (L221-222).
- FAILS: "CLASS: all three seed hypotheses fail" for the interacting law (L226: "Q and P are not established for
  the interacting law"); **the integrated-flow / quotient / ABS-flow refutation (L229: "Missing uniform time
  width and lattice transfer")**. Detail at L197-205: three sampled times give no lower bound on a time integral
  (explicit spike functions k_L with integral at most c + 3/L); gauge-inequivalent states do not give
  Q_phi(z) = 0 (the SO(2) radial example); the claim "strictly stronger than the gap" is not established.
- Also (L207): SUB does not refute (LOC-COV)'s typical-tilt formulation, which allows a bad set and a
  negative-curvature budget.
- Open as before: (LSI-traj-seed) (L205, L248). Raw lattice result files of the GUIDE runs are absent at the pin (L190).

**2.5 Row 968 (`gap-avgcurv-max.md`), check `gap-avgcurv-check-astra.md` (table L312-337, scope notes L339-388, RESULT L474).**

- HOLDS: Proposition FLOW, Lemma Z, Lemma NEC, the positive-radius ANG formula, AVG (b), (c), SCHR, the 6.3
  direction-resolved implication, the (ABS-flow) sufficient implication 7.1 (L335), the horizontal Fourier test
  7.2; POL-BR and AVG (a) after correction (explicit BBD extension, exact sine-cosine argument).
- FAILS: the inference that frozen-group failure must occur at nonzero tilt (L324, L363-371: the necessary
  growth k*/beta to infinity does not exceed the zero-field ceiling O(beta^2)); the broad conditional-CAP
  and (LOC-COV) obstruction claims (L334, L382-388): "LOC-COV plus CAP is one sufficient implementation of an
  averaged estimate. The text supplies no argument that every proof of ABS-flow must use LOC-COV, or that Ricci
  cannot help any collective horizontal direction... The negative conclusions in 5.5 and 8.2 must be
  statements about this attempt, not exclusions of other mechanisms."
- Narrowed: the strict hierarchy of 7.1 is a chain of sufficient implications; strictness and necessity of
  (LOC-COV) are not established (L336). The surviving claim on POL-BR (L351-358): "POL-BR itself has no
  fixed-beta smallness threshold, and the known zero-field obstruction does not kill its finite-interval
  integral. Its actual uniform hypothesis still requires proof."
- DENS (death by volume, L373-379) holds after adding the horizontal premise; it names no seed-box size.
- Open as before: (LSI-J-seed), (LSI-br-seed), (ABS-flow-seed), the seed.

**2.6 Row 977 (`gap-tiltproof-max.md`), check `gap-tiltproof-check-astra.md` (table L381-392, RESULT L404).**

- HOLDS: Theorem D1; D2 steps 5.1-5.4. HOLDS AFTER CORRECTION: Theorem D2 (normalize self-inverse modes, exact
  or downward-rounded constants; "the spectral theorem itself holds"), ZERO-CEIL (remove the unproved 0.234/117
  deduction), CAP (state beta lambda_* >= 3/2; side-4 and side-8 caps hold with exact bounds 589/69 and
  178859/8211), QUOT-CAP (uniform-in-b hypothesis; the side-16 number replaced).
- Scope sentences (L394-397): "No failing structural step was found in the pinned-sheet mechanism... The generic
  box-uniform bound remains open. The finite seed is excluded by ZERO-CEIL, conditional on the stated POL-BR
  output formula and the supplied seed target." Also (L377-378): "Finite-size growth also does not refute
  existence of some finite box-uniform bound without a proved continuation to arbitrarily large sides."
- Not proved: side-120 numerical claims; the uniform-in-b q_0 hypothesis of QUOT-CAP.

**2.7 Row 978 (`gap-ladder-max.md`), check `gap-ladder-check-astra.md` (table L377-388, RESULT L399).**

- HOLDS: Lemma IHC; 5.6 (a) trajectory restriction; the defective inequality with spectral tail (defect is an
  input). HOLDS AFTER CORRECTION: abstract Corollary CU; (TH) through 1.1.5 (iii) with the full vacuum
  normalization and an explicit determinant-comparison input; the (APR) form; R2.
- FAILS: (TH) assumption (a), the literal identification (L381: "The density lemma removes the Gaussian
  normalizers"); **the 5.7 universal method exclusion (L386: "The calculation does not cover methods retaining
  further information")**. The Gaussian scalar square-root loss holds for the tested scalar restriction only.
- Delivered consumer statement (L390-392): a correctly normalized uniform start bound plus (HC-phys) at a box
  satisfying (SIZE-phys) gives (SEED-phys). Neither hypothesis is proved for SU(2).

**2.8 Row 982 (`gap-hcphys-max.md`), check `gap-hcphys-check-astra.md` (Sections 3-5 L82-141, RESULT L195).**

- HOLDS: CAP (a), (b), (c); TEL on independent levels; EE (a)-(d) (so U1 implies U2; U3 implies the seed under
  EE (b)'s size condition); COUNT (a)-(c) under its all-real-time hypothesis; Route 2 (a) (no (HC) on all of
  L^2 for a non-atomic law); the crossed-channel identity on integer lattice tori.
- FAILS: L70's two-sided comparison; **the hierarchy at L131/L274, the deduction of pointwise U3 from the
  integrated decay (L93)**; L225's blanket Poincare-absence claim.
- Narrowed: COUNT's reading is an upper bound on state counts from a thermal envelope, not an equivalence with
  a gas model or with hypercontractivity (L110); on the U1 time grid the bound carries an extra 2 T E (L112-117).
- Correct replacement (L95-100): "U1 implies U2; U3 separately implies the seed under EE(b)'s size condition...
  Neither this proof nor the original EE identifies U1, U2 and UNIT as equivalent."

**2.9 Row 987 (`gap-det-fable.md`), check `gap-det-check-astra.md` (verdict record L380-398, RESULT L406).**

- HOLDS: Lemmas A, P, A'; (S1)-(S3); HOLDS AFTER CORRECTION: Corollary B and the repository-form (DET) with
  row 989's m-independent constant.
- FAILS: Step 6, "no elimination factor at identity" (L349-359: SA QC16/QC25 leave a non-unit pivot factor
  L^9 per coarse bond; harmless for the two-torus density only with the identical per-cell rule retained).
- Scope: a conditional matrix comparison, not an unconditional (DET) for the account's physical normalizer;
  inputs R and W are not discharged.

**2.10 Row 988 (`gap-unit-max.md`), check `gap-unit-check-astra.md` (table L448-455, RESULT L466).**

- HOLDS: Schwarz transport; the Borel-Caratheodory step. HOLDS AFTER CORRECTION: Identity G (integer temporal
  extent), Lemma ORD (integer time), Lemma FLOOR (its gap is the gap of the traced sector; for the full trace
  the displayed numerical threshold holds), consequence 7.1 (n >= 2, n_0(beta) at fixed coupling).
- FAILS: the real-time analytic extension of ORD; an inference from a restricted sector to an excluded
  excitation of the full trace.
- The corrected implication: a seed at each fixed nonnegative coupling from a common zero-free domain. That
  domain, the cutoff-uniform physical seed, (U1) and (U2) stay open. The check did not check the rest of row
  988's direction proposals (L458).

**2.11 Row 993 (`gap-idab-opus.md`), check `gap-idab-check-astra.md` (E_0 readings L185-216, table L384-400, RESULT L419).**

- HOLDS AFTER CORRECTION: the explicit scalar input (ID-a) and the classical form identification (ID-b);
  the physical pivot factor is L^9 (the per-length delta gives L^12).
- FAILS: "the account's E_0 is reading (i)" (L196-206). CA-I identifies const_s, not all of E_0^(j); CMP 119
  p. 279 adds the vacuum values of E^(k+1) and R^(k+1). So Lemma C does not give torus independence of the
  whole E_0. "This is a failure of the given justification, not a counterexample to torus independence."
- Open: (E0-tor), needed wherever (DET) or the (HC-phys) reduction compares two tori: matching non-wrapping
  coefficients and a summable wrapping tail (L212-216).

**2.12 Row 996 (`gap-sepinput-max.md`), check `gap-sepinput-check-astra.md` (table L302-314, RESULT L326).**

- HOLDS: Identity MIX, Proposition TILT, LIP, K7-A, K7-B, ELL. HOLDS AFTER CORRECTION: POL, SU(2) SHEET
  (embedded non-degenerate tube made explicit), MF, 4F.
- FAILS: SHEET's extension to other groups from positive variance alone (cyclic-group example, L311).
- Survives (L316): "The source's SU(2) obstruction to a volume-uniform covariance supremum survives."

**2.13 Row 998 (`gap-crux-exercise3-max.md`), check `gap-crux-exercise3-check-astra.md` (table L133-159, L162-195, RESULT L249).**

- HOLDS: Lemma PT (a)-(d); KF (a), (b); 6d rows 30, 33, ex2 #18, ex2 6c point 1; the frozen Q_8/2T correction.
- HOLDS AFTER CORRECTION: Corollary PT1 (replace "U(1) in its massless phase" by an admitted factor with no
  periodic seed; "an always-false hypothesis is no counterexample to a valid implication", L139); KF (c)
  (require K_j to infinity at one fixed g); KF1 (delete the unconditional list of necessary U(1)/photon tests:
  "each comparison must meet the same H, including its ultraviolet clause", L146); 6d row 24 (the dependency
  is T2 and T3, L151); 6d row 28 (re-admit K-flow: "replace 'valid necessary conditions' by tests whose
  hypotheses must be verified", L152).
- FAILS: **I28, the published Wilson U(1) supplier of "no seed" (L140)**; **KF (d), "it must contain a
  separating number" (L145: "No such necessity follows from contraposition")**; 6d row 28 "(better: w_p)" for
  Route 3 (b) (L153: "V proves no seed, not branch G. Bounded D at its transition is missing"); the claimed
  non-converse of the printed (CONTR) (L162-190: the existential-base (CONTR) is equivalent to (PHYS-SEED) by Z3).
- Kept: the original (CAS) of row 708 (start at size 3, every integer size in its band) has no proved converse
  (L159). Logical limit (L213-219): a Wilson-only first-passage clause already excludes the standalone U(1)
  and free-photon comparisons; "no comparison model constrains an implication before this domain test."

**2.14 Row 1000 (`gap-d2-inputs.md`), check `gap-d2-inputs-check-astra.md` (Step 2 table L33-43, L45-91, disposition L247-267).**

- HOLDS: Lemma RP and Corollary PT (the reflection-positivity inputs). HOLDS AFTER CORRECTION: Lemma GD and
  Corollary IR and their consumption by Theorem D2.
- FAILS: **Step 2's confirmation of T3 and of rule N2**: source line 42 (e), check L41, "no law meeting the claimed common premises is
  constructed"; source line 44 (f), check L42, the claimed Gaussian energy identity is false (exact one-mode check: sigma^2 (1 - e^(-2E))
  = e^(-E)/beta_0, not 1/beta_0; choosing E = (beta_K/beta_0)|p| gives covariance of order 1/(2 beta_K |p|) with
  the bare kinetic coefficient unchanged, L56-83); source line 46, check L43, "The required transfer-structure conclusion does not
  follow... The text has not proved that every level-convexity route must fail or must use the named repair."
- Also a domain defect at source line 36 (check L45-52): the linear colour test f(A) = sum <w_b, A_b> is not invariant under
  constant SU(2) rotations, and Theorem BR needs that invariance; "a suitable invariant nonlinear or quadratic
  test and its estimates are not supplied".
- What may be retained (L85-91): "a conditional benchmark warning, not a proved exclusion". TEL on independent
  levels gives a lower bound on an admissible LSI rate; an upper bound needs a matching sharpness example in
  the tested class, which is not supplied. T3's nonlinear conclusion remains open (L30-31).

**2.15 Summary of Step 2.** The fourteen checks leave the core lemmas standing (most after stated corrections)
and remove eleven broad negative claims as proofs. Those eleven are the input of Section 4:
(i) varying geometry buys nothing (960 L408); (ii) rotated or diagonal geometry buys nothing (963 L355);
(iii) every averaged squeeze is unchanged (965 L356); (iv) the (LOC-COV)/conditional-CAP obstruction and the
frozen-group nonzero-tilt inference (968 L324, L334); (v) the refutation of the integrated-flow, quotient and
ABS-flow forms, and CLASS's threefold failure (970 L226, L229); (vi) the universal method exclusion of 5.7
(978 L386); (vii) the hierarchy U1/U2/U3 and the blanket Poincare-absence claim (982 L93); (viii) the restricted
sector inference of FLOOR and ORD in real time (988); (ix) the full-E_0 identification (993 L196); (x) the
compulsory separating number KF (d), the Wilson U(1) supplier I28, and "(better: w_p)" (998 L140, L145, L153);
(xi) T3 and rule N2 (1000 L41-43). No check supplies a seed, a rate, or any order-one estimate.

## 3. Step 3: today's rows 1011, 1013, 1016, 1017 and their same-provider checks 1014, 1015, 1019, 1020

Read: the FINISH rows 1011, 1013-1020 in full (tasks and RESULT text, FINISH L1092-1101), and in
`gap-compact-rigidity-max.md` the definitions 3.1 (L131-158), Proposition OM (L223-232), Theorem CR (L239-249),
(LIOU) with its test table (L288-304) and the four failed ways (L363-384). The other three files were not
opened in this step; their content is taken from the RESULT text. All four checks are by Claude Opus 5.5,
the same provider as the author, so none is independent.

- **Row 1011** (direct port of the 2D pinned-cell iteration; check 1014: no WRONG). The port FAILS in the class
  of all pins and strengths: only central link symmetries exist (Lemma CEN, Corollary CEN2), the pin supremum
  is blind to colour coherence (Propositions B, B'). Open there: a typical-field form with a colour frame
  ((N1)-(N3) of its 7.4), which reads first-passage data; the Schrodinger-functional bound at the trivial pin.
- **Row 1013** (nine invented mechanisms; check 1015: all confirmed). None survives. Lemma WN (lab-frame link
  translations have a corner-diagonal cost), Lemma TWIST (every gauge twist of pinned data is removable), Lemma
  SLAB. The missing object: a 4D analogue of the 2D short step, a selective gain at order-one response.
- **Row 1016** (ten exact reformulations with a global non-abelian group; check 1020: no WRONG). All FAIL. Lemma
  CEN+, Lemma AUX, Lemma MC, Theorem BH (the homogeneous-strength case of B'). Corrected reopen condition: rigid
  group + charged pins + a response on the gauge-invariant algebra; no candidate meets the three.
- **Row 1017** (compactness and rigidity; check 1019: first failing step none). PROVED there: Theorem CE
  (blow-down limits of the torus data exist if (PHYS-SEED) fails and (BDD-Delta) holds), Proposition OM, and
  **Theorem CR** (`gap-compact-rigidity-max.md` L241): for a trajectory with (BDD-Delta) these are equivalent:
  (1) (W); (2) (PHYS-SEED); (3) Omega is empty; (4) Omega has no uniformly recurrent element; (5) for one
  continuous Lambda, no element of Omega has Lambda(sigma E) >= Lambda(E). Scope repair of check 1019: Omega is
  built from the trajectory with D_0 a (BDD-Delta) bound. **(LIOU)** (L288): the limit set Omega of Wilson SU(2)
  on the account's trajectory has no uniformly recurrent element. It is target-equivalent given (BDD-Delta).
  The rigidity half failed four ways (L363-384): the kept properties are those of the engine, and the constants
  log m (models with m vacua) have all of them; products are absorbed (Lemma PT-inf); Proposition SI: a kept
  property is invariant under the doubling, so the limit keeps no condition at one end of the scale axis.
  The object is a function of four sizes; the group, the action and the Markov property are lost (L215).
- **Row 1018** (the 4D short step: field-dependent covariant moves, energy increment, barrier model) runs at
  the same time on worker 3 and writes `library/gap-short-step-max.md`. This row does not redo it. Its
  status block was read once (Section 5 says where) so that the registry does not duplicate its three routes.

Reading for the registry: the four rows are a negative result about one-scale mechanisms that are uniform
over a class of boundary data or that pass through a scale limit. They leave (K-flow) statements, which
read the trajectory, as the only family with no refutation device against it (`parts/gap.md` L227-229).

## 4. Task (1): every discard verdict, filter and lead rule, with its status after the checks

Status words. **stands**: the check holds it (with the stated correction, if any). **narrowed**: it holds in a
smaller form, which is written. **no longer supported**: the check marks its support FAILS; the line is given.
**not covered**: none of the fourteen checks read it; it is "valid as reported; not re-derived" (skill L502).
"Check n" means the gpt-6-astra check of row n (file and line as in Section 2). A status is the reading of a
check file; it grants nothing. Sources of the lists: `parts/gap.md` L49-72, L88-96, L188-229; row 998 6a/6d
(`gap-crux-exercise3-max.md` L498-513, L568-590); exercise 2 6a/6d (`gap-crux-exercise2-max.md` L394-413,
L441-450); the RESULT text of rows 1011-1018; additional reads named in the rows (rows 970, 968, 977, 982, 960).

### 4.1 Lead rules in force

| # | Rule (where) | Status after the checks | What it now says |
|---|---|---|---|
| A1 | Rule W2: a direction row states its kind, (K-one) or (K-flow); tests per kind (`parts/gap.md` L90) | **narrowed** by check 998 (L139, L140, L145, L146, L153) | (i) A (K-one) hypothesis need not name a number: KF (d) FAILS. (ii) A comparison model binds a tool only after the tool's own hypothesis H, with its ultraviolet clause, is verified on that model; a Wilson-only first-passage clause excludes the standalone U(1) and photon comparisons. (iii) The product clause needs an admitted no-seed factor (in the lane: Villain U(1) at beta >= 2^14); the published Wilson U(1) supplier I28 FAILS as cited. (iv) w_p (Proposition V) proves no seed at one coupling, not branch G. The clauses on Theorem D2 and Lemma SHEET stand (A6, C8, C9). |
| A2 | Row 982 N2: no row on (LSI-br) from the account's level convexity (`parts/gap.md` L91; FINISH L1081) | **no longer supported**: check 1000 L41-43 (source lines 42, 44, 46); check 998 L151 (the rule also leans on T2) | T3 (the port is short by beta_K/beta_0) is ARGUED only. What may be kept is "a conditional benchmark warning, not a proved exclusion" (check 1000 L85). T2 stays as a constraint in the valid form: a proof must use more than (P1)-(P3) and "order-one coupling at the unit", or read first-passage data. Section 6 decides what the route is worth. |
| A3 | Row 1002 filter for (K-flow) rows (the 2D O(N) plausibility test) (`parts/gap.md` L92) | withdrawn by rows 1003, 1006 before the checks; **not covered** | Not a test. The 2D model is a source of mechanisms. |
| A4 | The reading of the 2D pinned-cell mechanism; "the direct port FAILS in the class of all pins and strengths" (`parts/gap.md` L93; rows 1011, 1013, 1016) | **not covered** by a cross-provider check; same-provider checks 1014, 1015, 1020: no WRONG | Stands as same-provider-checked. Theorem BH covers homogeneous strengths. The corrected reopen condition (rigid group, charged pins, response on the gauge-invariant algebra) is ARGUED. |
| A5 | "Not refuted" notes on rows 970 and 960-965 (`parts/gap.md` L94-95) | **stands** (they record checks 970, 960, 963, 965) | See B1-B3, B6. |
| A6 | Lead note under row 996: a hypothesis uniform over plaquette coupling fields gets no row (FINISH L1105) | **stands for SU(2)**, after correction (check 996 L310: embedded non-degenerate tube); **narrowed** for other groups (L311: needs the identity-maximizer hypothesis) | Lemma SHEET binds all-fields forms for SU(2). |
| A7 | Last sentence of row 988 N2: no row "without an input that separates the Wilson trajectory from K7" | replaced by W2; the replacement **stands after correction** (check 998 L152) | (K-flow) rows are admissible. "Valid necessary conditions" is replaced by "tests whose hypotheses must be verified". |
| A8 | Lead note under row 998: the conditional dichotomy (W4, route RD) is not queued; "proofs or counterexamples, not a catalogue of open conditions" (FINISH L1104) | **not covered** (an owner-level rule, not a mathematical verdict) | Unchanged. Corollary TRI of row 1017 is a hypothesis-free form of the same statement. |
| A9 | Row 998 9.5, "what not to do next" (`parts/gap.md` L70-72): no further fresh-framing exercise by this model family; no further one-scale search against K7; no monotone or convex statement along scales by class-wide tools; no urgent theta(L) run; no Migdal-Kadanoff comparison | **stands** as advice; one clause **narrowed** | "Class-wide tools": the product test holds (PT (a)-(d), check 998 L135-138), but the objection "a decrease persists" is ARGUED only (L147). This row is itself a registry row, not a fresh-framing exercise. |
| A10 | Lead note under row 1000: "a route must use the transfer structure at each level" (FINISH L1081) | **no longer supported** as a rule (check 1000 L43) | "The text has not proved that every level-convexity route must fail or must use the named repair." |

### 4.2 Discard verdicts of the fourteen checked rows

| # | Verdict (row; where) | Status | Narrowed form, or what comes back |
|---|---|---|---|
| B1 | Row 960: varying the geometry buys nothing; stop queuing such rows (`gap-vargeom-opus.md` 4.4, L152, L208-218) | **no longer supported**: check 960 L408; also G3 FAILS (L373), OVL for all trial times FAILS (L390), the q = 1.6 ordering FAILS (L393) | "This note supplies no improving variable-geometry bound." Back: projected averaging; lens states at long trial times; other comparisons than the displayed ones; real second times q = 8/5. |
| B2 | Row 963: rotated or diagonal geometry buys nothing (three parts) | **no longer supported**: check 963 L355, L362; parts at L338, L343, L350, L352 | "No sufficient replacement is established here." Back: diagonal tori with coordinate mirrors on an invariant period lattice and D2's twisted axis channel; sector forms with empty nonzero-momentum frozen sectors. Missing objects named at L364-367. |
| B3 | Row 965: every averaged squeeze leaves the crux unchanged; every computable endpoint is harder; stop all squeeze rows | **no longer supported**: check 965 L356, defect 8 (L375-378) | "None of the displayed estimates supplies a new seed bound." Back: time-dependent squeezes; averaged block estimates. Struck: the equivalence of the pointwise-in-beta target to the seed; "EP1 settles every open-box obstruction". |
| B4 | Row 962: no relaxation of the constraint system is a new input (row 998 6a row 22) | **not covered**; weakened in part, since three members of the family lost their proofs (B1-B3) | Valid as reported; not re-derived. |
| B5 | Row 968: (a) averaged forms reduce to the pointwise criterion or to the Poincare inequality (Proposition AVG); (b) the obstruction through (LOC-COV) and conditional CAP (5.5, 8.2); (c) frozen groups must fail at non-zero tilt | (a) **stands** (check 968 L329-330); (b) **no longer supported** (L334, L382-388); (c) **no longer supported** (L324, L363-371) | (b): "statements about this attempt, not exclusions of other mechanisms". Back: collective Ricci terms; other proofs of entropic stability; conditional CAP. |
| B6 | Row 970: (a) a box-uniform (TILT-COV-sup) is refuted in the upper window; (b) the quotient form and (ABS-flow) are refuted with it; (c) all three seed hypotheses of class S fail for the interacting law; (d) "do not queue proofs of (TILT-COV-sup), its quotient form, or (ABS-flow)" | (a) **narrowed**: Lemma SUB stands (L213), but the run "supports growth at the sampled parameters, not a mathematical refutation" (L201); (b) **no longer supported** (L229, L203); (c) **no longer supported** (L226); (d) **narrowed** to the supremum form | The supremum form stays dead for the use at the seed box through B7. The quotient form, the averaged form (ABS-flow), the integrated form, (LOC-COV) with a bad set (L207), and (LSI-traj-seed) are open. |
| B7 | Row 977: Theorem D2 (every kbar of the supremum form is at least lam_* k00, from hard-pinned sheets), Corollary CAP, ZERO-CEIL, QUOT-CAP | D1 **stands**; D2, CAP, ZERO-CEIL **stand after correction** (check 977 L381-392); QUOT-CAP **stands only as a conditional statement** (uniform-in-b q_0 hypothesis, unproved) | Theorem-grade by hand at sides 4 and 8 (589/69, 178859/8211). Side-120 numbers are ARGUED. "The generic box-uniform bound remains open": D2 caps the use, not the existence, of a box-uniform kbar. |
| B8 | Row 978: (a) 5.7, every one-shot method loses a square root; (b) a carrier of a seed from one coupling to finer cutoffs is (NOCRIT) plus a climb (R2); (c) (TH) by literal identification | (a) **no longer supported** as universal (check 978 L386); (b) **stands after correction** (L388); (c) **no longer supported** (L381) | (a) holds for the tested scalar restriction. (c): (TH) needs the full vacuum normalization and a determinant comparison, so it now rests on (DET) and on (E0-tor) (B11). |
| B9 | Row 982: (a) N2 and T3; (b) the hierarchy U1/U2/U3 and the reading "the seed is exactly (UNIT-EE)"; (c) no Poincare inequality (L225); (d) Route 2 (a), no (HC) on all of L^2; (e) Lemmas CAP, COUNT as necessary conditions | (a) **no longer supported** (A2); (b) **no longer supported** (check 982 L93); (c) **no longer supported** (RESULT L195); (d) **stands**; (e) **stand**, COUNT **narrowed** (L110-117) | (b): "U1 implies U2; U3 separately implies the seed." No equivalence of U1, U2, (UNIT). |
| B10 | Row 988: (a) Lemma FLOOR, no seed below the massless floor 17.04; (b) the beta_t path needs 3D mixing and (NOCRIT); (c) Route 3 (c), soft exclusion of branch G is impossible without a separator from K7; (d) Route Z needs a common zero-free domain | (a) **narrowed** (check 988 L452: the gap is that of the traced sector; the inference from a restricted sector to the full trace FAILS; the full-trace threshold holds); (b) **stands** as an open premise (Identity G after correction); (c) "too strong" (row 998), **confirmed after correction** (check 998 L152); (d) **stands** (7.1 after correction), ORD in real time FAILS | Back from (a): seeds in restricted or twisted sectors are not excluded by FLOOR. This meets route RE (sector engines). |
| B11 | Rows 987, 993: (DET) and the identification inputs of (TH) | Lemmas **stand**; "no elimination factor at identity" **no longer supported** (check 987 L349); the full-E_0 identification **no longer supported** (check 993 L196) | The extensive base (TH) is conditional on the account, (DET) and the open (E0-tor). |
| B12 | Row 996: (a) hypotheses uniform over coupling fields are empty on large tori (SHEET); (b) one-plaquette separating properties have no consumer | (a) **stands for SU(2)** after correction (A6); (b) **stands in range**, (K-one) only (check 998 L154) | - |
| B13 | Row 998: (a) KF (d), a (K-one) input must contain a separating number; (b) I28; (c) "(better: w_p)" refutes soft statements about branch G; (d) (CONTR) has no converse; (e) "RA is stronger than the target" | (a), (b), (c) **no longer supported** (check 998 L145, L140, L153); (d) **no longer supported** for the printed existential-base (CONTR), which is equivalent to (PHYS-SEED) (L162-190); **stands** for the original (CAS) of row 708 (L159) | (e): the strength of RA is "unknown/comparable or stronger" for (CAS) with a prescribed start; "target-equivalent" for (CONTR). |
| B14 | Row 1000: reflection positivity and Gaussian domination as inputs of D2 | **stand** (RP, PT), **stand after correction** (GD, IR) | Theorem D2 now has cross-provider support for its two ported lemmas. |

### 4.3 Older discard verdicts (exercise 2 rows 1-18; row 998 rows 19-33 not listed above)

None of these was read by the fourteen checks unless a line says so. All are "valid as reported; not re-derived".

| # | Verdict | Status |
|---|---|---|
| 1-3 | worst-case Dobrushin (ceilings 2/3, 0.775); background-uniform twist bounds (1.0109); annealed block condition | **not covered**; valid as ranges only (C11). Check 968 L351-358 corrects one reading: ceiling (i) of row 941 is a flipped spatial link at non-zero endpoint tilt, not a zero-field statement. |
| 4, 5 | one-way step for a torus quantity; (MONO-Delta) false for the ordered Ising model | **not covered** |
| 6-9 | linear (ES-1); Wilson-loop association (EP-NO); fixed-radius loop equations; full-L^2 block certificate | **not covered** |
| 10 | soft block step then a high-temperature theorem: circular | **not covered** |
| 12, 14, 16 | strand counting (0.2135 against a guide value 0.267); thin Z_2 lift; localization along plaquette tilts | **not covered**; each "needs a small number" and is a range |
| 13 | flux half from glue half by clustering | **not covered** |
| 15 | vacuum Bakry-Emery (G2) is the Langevin gap | **not covered**. Section 6 uses its exact form (the ground-state Dirichlet form). |
| 17 | thick vortex by field-independent spreading | **not covered** by the fourteen; row 1018 (Lemma PAR, Corollary MP) narrowed "no topological twist" to cubes |
| 18 | hierarchical and Migdal-Kadanoff lattices are group-blind | **stands** (check 998 L156, scope only) |
| 19 | (TILT-COV-sup) and (ABS-flow) "refuted, theorem-grade" | **narrowed**: theorem-grade for the supremum form only (B7). For (ABS-flow) **no longer supported** (B6 (b)). |
| 20 | box-uniform quotient form fails (q_0 about 0.24 with QUOT-CAP) | **narrowed**: a GUIDE number in a conditional proposition (B7); check 970 L203 |
| 21 | forms uniform over coupling fields | **stands** for SU(2) (A6) |
| 22 | relaxations of the constraint system | B4 |
| 23 | a carrier of a seed to finer cutoffs | **stands after correction** (B8 (b)) |
| 24 | (LSI-br) from small-field convexity | **no longer supported** (A2) |
| 25 | (UNIT) by three routes | "was tried": rules out nothing (row 998 6d) |
| 26 | a seed below the massless floor | **narrowed** to the full trace (B10 (a)) |
| 27, 29 | the beta_t path; Route Z in Schwarz form | **stand** as open premises (B10 (b), (d)) |
| 28 | soft exclusion of branch G | "too strong"; (K-flow) admissible (A7) |
| 30 | one-plaquette separating properties | **stands in range** (B12 (b)) |
| 31 | averaged curvature, Polchinski flow, Piazza-Shen: "did not close; circular" | **narrowed**: Proposition AVG stands; the obstruction claims do not (B5) |
| 32 | plaquette automata; squeeze, rotate, vary the box: "no input" | **narrowed** to "no bound found in these notes" (B1-B3) |
| 33 | (DRIFT)_c and (ESC) | (ESC): "not tested", not "fails" (**stands**, check 998 L155); (DRIFT) open |

### 4.4 Filters: the test table, row by row

| # | Test (source: `parts/gap.md` L199-213 unless named) | Status | Valid form now |
|---|---|---|---|
| C1 | Compact U(1), Coulomb phase | **narrowed** (check 998 L140, L146, L213-219) | Theorem-grade in the lane for Villain at beta >= 2^14. The cited published Wilson supplier of "no seed" FAILS. It binds a tool only if the tool's hypothesis holds for U(1); a hypothesis with a Wilson SU(2) first-passage clause is not bound. |
| C2 | Free photon "through the rate"; the floor 17.04 | **stands** for the full trace (check 988 L452) | Not for a restricted sector. |
| C3 | Product with a massless factor (Lemma PT, Corollary PT1) | PT **stands**; PT1 **stands after correction** (check 998 L139, L147) | Binds a hypothesis that holds on a second factor and survives the product with an admitted no-seed factor. |
| C4 | Frozen Z_2 | **not covered** | T_per only, beta above 2.191. |
| C5 | Frozen Q_8, 2T | **stands** in the frozen limit (check 998 L150; check 965 defect 5) | At least two centre-even flat states in the frozen limit. No fixed finite coupling is inferred. |
| C6 | w_p at its transition coupling (Proposition V) | **stands after correction** (check 998 L148) | Failure of T_fix at one coupling, given van Enter and Shlosman and (TM-gen). "A number" is not forced. No statement on branch G. |
| C7 | K7 line and end point | **stands** as BELIEF (check 998 L149) | A belief-grade analogue of C6 for a seed conclusion only. |
| C8 | Theorem D2; Lemma SUB | D2 **stands after correction** (check 977); SUB **stands** (check 970 L213) | D2 binds the supremum-over-tilts form at every flow time. Neither binds a typical-tilt form with a bad set (check 970 L207) nor, by any written argument, the averaged form (ABS-flow). |
| C9 | Lemma SHEET | **stands for SU(2)** after correction; **narrowed** for other groups (check 996 L310-311) | Forms uniform over coupling fields. |
| C10 | Lemmas CAP, COUNT | **stand** (check 982); COUNT's reading **narrowed** | CAP: (1/2) integral of gam_s ds <= (e^(2 E_1) - 1)/2 for a rate obtained through Theorem BR. |
| C11 | Ceilings 1/3, 2/3, 0.775, 1.0109 | **not covered** | Ranges of single families. |
| C12 | ZERO-CEIL (row 977 2.0) | **stands after correction** (check 977 L383) | Caps the output of Theorem POL-BR for the supremum form at 2 beta/(e^beta - 1), so it excludes the a = 30 seed through that formula. It is a statement on one formula. |
| C13 | Lemma NEC (row 968 4.1): k* >= 2 beta log(1/E_1) | **stands** (check 968, Section 4 heading) | Given the repaired POL-BR and Proposition HC. |
| C14 | DEN, "no room" (row 960) | **narrowed** (check 960 L378) | One one-side, seed-time comparison; at most g/23. |
| C15 | Proposition NP (row 1003) | **not covered** (same-provider check 1006) | No proof of (CAS) by induction on finitely many values of D. |
| C16 | The five-dimensional test; instanton and refilling tests | **not covered** | As reported. |
| C17 | Proposition SI, Lemma PT-inf, the constants log m (row 1017) | **not covered** (same-provider check 1019) | Soft rigidity statements on blow-down limits fail. |
| C18 | Gauge theories with matter in the conformal window | **not covered** | Outside K. BELIEF. |

### 4.5 What the table shows

1. Eleven broad negative claims lost their proofs (Section 2.15). In each case the lemmas under the claim
   stand. So the lane's map of what is proved is intact; its map of what is excluded was too large.
2. Three theorem-grade filters survive in full for SU(2): Theorem D2 (supremum over tilts), Lemma SHEET
   (uniformity over coupling fields), Lemma PT with an admitted no-seed factor (class-wide soft statements).
   Each binds a quantifier (a supremum, a uniformity, a class), not a route.
3. No check moved the wall. No check supplied a seed, a rate, or a mechanism. Every route that comes back comes
   back as "not excluded", with its terminal obligation unchanged.

## 5. Task (2): the route registry, rebuilt from Section 4

Target of every row: (W) (`parts/gap.md` L18-20), or its checked equivalent form of Theorem CR (same-provider
check 1019). Columns follow the governance file (Section 1.1). "Strength" uses its four words. A family is the
triple (object, mechanism, terminal obligation). Statuses are the reading of this row; nothing is checked.

Additional reads for this section: row 970 Sections 1, 4, 7 (`gap-direction2-max.md` L39-80, L229-292,
L402-450); row 968 Section 3, 4.1, 7.1 (`gap-avgcurv-max.md` L124-199, L370-390); row 977 2.0, Step 4, 5.5-6.1,
9.1 (`gap-tiltproof-max.md` L54-72, L170-200, L235-266, L388-412); row 960 4.3-4.5 (`gap-vargeom-opus.md`
L142-170); row 982 Steps 2-4 and 8.4 (`gap-hcphys-max.md` L40-163, L258-275); row 947 Step 5
(`gap-fc-max.md` L121-191); rows 973-975 and 1018 at their RESULT text.

### 5.1 The registry

| Rank | Route | Object and mechanism | Terminal obligation | Strength against (W) | Status | Blocked only by a verdict that no longer stands? | Cheapest decisive next step, and its cost | What the step would change |
|---|---|---|---|---|---|---|---|---|
| 1 | **LC**, level convexity as a carrier to (LSI-br) | fine slice law and bridge marginals nu_s in the fine link metric; entropy over the account's levels below the unit ((P1)-(P3)), plus one inequality at the unit | the unit inequality ((U1) or an LSI of the unit block law), the exact size of the loss between unit metric and fine metric (T3, "roughness"), and (TR-LF) | stronger ((U1) with (TH) gives the seed; no converse) | set aside by rule N2 until 2026-11-15; now provisional | **yes**: N2 / T3 (A2, A10) | decide T3 by hand: is the factor beta_K/beta_0 a property of the model or of the linear count? One session, no run | the lead rule A2/A10; whether the Theorem BR family can be used at all in the continuum form (HC-phys) |
| 2 | **RF-avg**, averaged and trajectory flow forms at one coupling, with consumer **K4** (the ratio-4 HC/BR-J route) | bridge marginals; Polchinski flow of the middle layer; (ABS-flow), (LOC-COV) with a bad set, (LSI-traj-seed)_a; consumer: Proposition HC on (a; (4a)^3), K_30 = 0.811 at beta 2.3 | (ABS-flow-seed)_a or (LSI-traj-seed)_a or (LSI-J-seed)_a at one beta of the window, then the carry of row 978 R2 ((NOCRIT) and a climb) | unknown/comparable (a fixed-coupling statement of kind (K-one); with the carry it gives (W)) | active, no mechanism; K4 is candidate-complete as an implication (check 960) | **yes** for (ABS-flow) and the integrated form (B6 (b), row 998 6a row 19); (LSI-traj-seed) was never refuted | GUIDE: the entropy form (EC-traj) at intermediate k, beta 2.3, sides 12 to 24 (row 974 left it untested); hours under the lock. By hand: none known | keeps or retires the whole bridge family at fixed coupling |
| 3 | **GEO**, other geometries for the engine | Theorem S / SH' on other complexes: real second times (Lemma Q), diagonal tori with twisted axis channel, time-dependent squeezes, projected averaging | the same seed with another threshold or box | unknown/comparable (an engine change; it supplies no input) | provisional | **yes** (B1, B2, B3) | by hand: the q = 8/5 line of Theorem SH' (check 960 L393); a diagonal finite-torus transfer construction (check 963 L365). Hours each | thresholds and box sizes only (K_a of route 2 falls); not the wall |
| 4 | **RD / TRI**, the dichotomy or trichotomy as a theorem | Theorem ZD-c, Corollary Z4 (row 720); Corollary TRI (row 1017) | none (given its inputs) | weaker | candidate-complete as a weaker statement | no (A8 is an owner-level rule) | an owner decision; no cost | whether a conditional theorem is a milestone |
| 5 | **RF-quot**, quotient form | (TILT-COV-quot) box-uniform; gain Q_phi from the gauge orbit | a box-uniform bound; QUOT-CAP caps it if q_0 >= 0.24 uniformly in b | stronger | blocked-local on one number | partly (row 998 6a row 20 rests on a GUIDE; B7) | by hand: q_0 > G_S/beta on side 4 (threshold 0.117; proved 0.064, row 977 9.1). Needs the vacuum on a pinned slice; not cheap | retires the form at theorem grade on small boxes only |
| 6 | **RE + F3**, sector engines and vortex containers | flux sectors, centre twists; Lemma PAR, Corollary MP (row 1018) | (EV-STEP); (SER) and (SPR) with kappa phi < 1 | weaker (one sector) | blocked-local | partly: FLOOR no longer excludes a seed in a restricted sector (B10 (a)) | none cheap; no mechanism for (SER) or (SPR) | - |
| 7 | **LIOU**, compactness and rigidity | blow-down limits of torus data; Theorem CE, Theorem CR | (LIOU), with (BDD-Delta) | target-equivalent given (BDD-Delta) | blocked-equivalent | no | none: four soft ways failed (row 1017 5.3); the limit loses the group | - |
| 8 | **RA / RB**, contraction of D, sign in beta | (CAS) of row 708; printed (CONTR) | theta < 1 on the band | (CAS) with prescribed start: unknown/comparable or stronger; printed (CONTR): target-equivalent (check 998 L162-190) | blocked-equivalent | no | none | - |
| 9 | **RF-sup**, supremum over tilts | (TILT-COV-sup) | a box-uniform kbar | stronger; by Theorem D2 its constant is at least that of a pinned 2D sheet | retired for the use at the seed box (theorem-grade at sides 4, 8); existence open | no | none; do not attack | - |
| 10 | **RC**, a one-scale property | a property of the measure at one scale | none with a consumer | target-equivalent | blocked-equivalent | no (KF (d) failing widens the search; it supplies no candidate) | none | - |
| 11 | **KF-frame / F2**, typical-field colour frame; pinned short step O1 | (N1)-(N3) of row 1011; (FL), (DEC) of row 1018 | (DEC) and a consumer | unknown | blocked-local | no | none | - |
| 12 | **Route Z; beta_t path** | zero-free torus families; Identity G | a common zero-free domain; 3D mixing and (NOCRIT) | unknown | blocked on open premises (B10 (b), (d) stand) | no | none | - |
| 13 | **RG**, hierarchical comparison | Migdal-Kadanoff flows | - | unknown | retired (group-blind; check 998 L156) | no | none | - |

### 5.2 Kill pass (skill step 7), one line per route

- LC: does not assume the target below the unit. Its unit inequality is the wall. Kill verdict: wounded;
  decided in Section 6.
- RF-avg: no test in the valid form binds it. Theorem D2 binds a supremum; (ABS-flow) at t = 0 reads
  E_(mu')[v^T (C_phi - kap) v] <= (1/2) E_(mu')|grad v|^2 with v = grad log(d mu'/d nu_s) and C_phi the tilted
  covariance (multiply (ABS-flow) by F and use grad F^(1/2) = F^(1/2) v/2). A weight F that moves mass to
  pinned tilts has a large v in the pinned directions, and that part is charged with the same kap on the
  right. So the supremum argument of D2 does not transfer. Reading, ARGUED; it is not a bound on kap. Lemma
  META and Lemma DEF of row 975 (each metastable set adds about 1 to S; bad links must be rarer than about
  7.5 x 10^(-10)) are the standing constraints. Verdict: survives, with no mechanism.
- K4: an implication that holds. Its hypothesis (LSI-J-seed) is a fixed-coupling statement: w_p and the K7
  belief test it (rule W2). Verdict: survives as an implication.
- GEO: an engine change keeps the class (F1), so every blind test passes it and it stays blind. It can lower
  a threshold. It cannot supply the order-one input. Verdict: survives as an engine item, off the wall.
- RF-quot: wounded by QUOT-CAP if q_0 >= 0.24; that number is a GUIDE value.
- RE + F3, LIOU, RA/RB, RC, KF-frame, Route Z, RG: verdicts of rows 998, 1017, 1018 unchanged by the checks.

### 5.3 Ranking rule and the top route

Rank is "what the cheapest decisive step would change, divided by its cost" (skill L590-592). No route has
a known step that moves the wall. So the rank follows the decisions that a step can move.

- **Top: LC.** It is the only route (a) that was blocked only by a verdict the checks removed, (b) that reads
  the account's data below the unit, so that no comparison model binds it (rule W2, kind (K-flow)), and (c)
  whose decisive step is a hand argument of one session. The step decides a lead rule. Section 6 takes it.
- Second: RF-avg with K4. Its decisive step is a GUIDE run of hours, and its outcome moves the whole bridge
  family at fixed coupling. It is the larger change at the larger cost.
- Third: GEO. Cheap steps, small change.

Routes that were blocked only by a verdict that no longer stands: **LC** (N2/T3); in **RF-avg** the forms
(ABS-flow) and the integrated form, and **RF-quot** in part; **GEO** (three notes); a seed in a restricted
sector under **RE** (the FLOOR inference). The family of (K-flow) rows as a whole was freed earlier by rule W2.
None of them gained a mechanism from the checks.

## 6. Task (3): the top route LC. Its first lemma, the attack by hand, and the verdict

Kind of result: a check of the lane's own argued verdict T3 (row 982), with four small lemmas proved by hand,
and one corrected filter. It is a result about a carrier. It does not move the wall (W).

### 6.0 Duplicate check (rule 0a), run before the attack

- `library/open-core.md`: no entry of the gap lane (grep for roughness, LSI-br, level convexity, HC-phys,
  UNIT, LSI-traj, ABS-flow, LIOU: no hit). `library/open-registry.md`: no hit.
- `FINISH.md`: "T3 and the roughness exponent" are listed OPEN in the RESULT text of rows 982 and 984. Row 1000
  Step 2 tried to confirm T3; that confirmation FAILS in the cross-provider check (Section 2.14). N4 of row
  982 (a one-loop test of the exponent) was never queued. No live row attacks T3. Row 1018 does not touch it.
- Prior statements used below, with credit: Theorem BR, the Gaussian mode and the linear ceiling (row 947,
  `gap-fc-max.md` 5.2, 5.4, 5.5); Elitzur's argument for the pair (row 941 (A5); Lemma Z, row 968 3.2); Lemma
  CAP, Lemma TEL and T3 (row 982); the endpoint proof of the energy identity and the one-mode check (the
  gpt-6-astra checks of rows 982 and 1000); the port answer on equal-time statements (row 985). Time
  decimation is a known family (row 962 B7, rows 846-877) and is not proposed again.

### 6.1 The route, and the statement that blocked it

**Route LC.** Prove (LSI-br)_s on the fine lattice with (1/2) integral of alpha_s ds >= M_H a_iota, M_H free of the
cutoff, from the account's level convexity (P1)-(P3) below the unit and one inequality at the unit. Theorem BR
then gives (HC-vac), and Proposition HC gives the decay of the thermal sum.

**T3 (row 982, `gap-hcphys-max.md` L88; its reading at L99).** "Needed (Lemma CAP): sup_s alpha_s >= 2 beta_0 M_H a_iota, bare
beta_0. Given by the port: stiffness a_- beta_k at level k ... one level-k bond moves L^(3k) fine slice links
by L^(-k) each, so ||R_0 D_k||^2 is of order L^k. A level-by-level bound (Lemma TEL) then gives 1/alpha of
order the sum over k of L^k/(a_- beta_k) ... alpha of order a_- beta_K a/l_unit ... Benchmark: a Gaussian field
with independent levels of stiffness beta_k satisfies (P1)-(P3) and has exactly this slice precision. So no
argument from (P1)-(P3) alone gives more."

**The first lemma of the route** is therefore the decision of T3: is the factor beta_K/beta_0 forced on
every proof that goes through the levels, or is it a property of one estimate?

### 6.2 Setting, and the one identity taken from the lane

As in Theorem BR (`gap-fc-max.md` L128-142). beta is the bare coupling, b = 1/beta. (X_t), t in Z, is the
stationary vacuum chain on M in R^N, with one-step law J and transition operator P, self-adjoint on L^2(nu).
For continuous f on M, u_s^f(y) = E[f(X_1) | Y_s = y] is its bridge interpolant, 0 < s < b, and

  EE(f) := integral over (0, 1/beta) of E_(nu_s) |grad u_s^f|^2 ds   (the bridge energy of f).

**(E1) Energy identity.** EE(f) = ||f||^2 - ||P f||^2 = <f, (1 - P^2) f>_nu for every continuous f.
Source: row 982 Lemma CAP (a), (a') (`gap-hcphys-max.md` L66-68); the two end limits are written in the
gpt-6-astra check (`gap-hcphys-check-astra.md` L42-55, "HOLDS AFTER CORRECTION"). I use it as given and
did not re-derive it. Every statement below that names (E1) is "PROVED given (E1)".

### 6.3 Four lemmas (PROVED by hand; elementary; not checked)

**Lemma S1.** Let P be a self-adjoint contraction on a Hilbert space and T >= 1 an integer. Then, as
quadratic forms, 1 - P^2 <= 1 - P^(2T) <= T (1 - P^2).
Proof. By the spectral theorem it is enough to take a number mu = lambda^2 in [0, 1]. Then
1 - mu^T = (1 - mu)(1 + mu + ... + mu^(T-1)), and the second factor lies in [1, T]. QED

**Proposition FR (the bare diffusion bound; PROVED given (E1)).** For continuous f on M and every T >= 1:

  EE(f) <= ||f||^2 - ||P^T f||^2 <= T EE(f),   that is   (1/2) E |f(X_(2T)) - f(X_0)|^2 <= T integral over (0, 1/beta) of E_(nu_s) |grad u_s^f|^2 ds.

Proof. ||f||^2 - ||P^T f||^2 = <f, (1 - P^(2T)) f>. Apply Lemma S1 and (E1). For the second form,
E |f(X_(2T)) - f(X_0)|^2 = 2 ||f||^2 - 2 <f, P^(2T) f>. QED
Reading. The bridge has length 1/beta. So the mean-square displacement of any slice function in one step
is at most 2/beta times the mean over s of its Dirichlet energy. The coupling is the bare one, at every
lag T. No gap is assumed. The statement holds for every model with this kernel: it is blind.

**Lemma EL (Elitzur at every time lag; lags 0 and 1 are row 941 (A5), row 947 5.5 and row 968 Lemma Z).**
On a cubic periodic box of side at least 3, for all integers k >= 0 and all links l, l':

  E[X_(0,l) (x) X_(k,l')] = delta_(l l') (tau_k/4) Id_4,   tau_k := E <X_(0,l), X_(k,l)>,  tau_0 = 1,  tau_(2j) >= 0.

So for every z in R^N and f_z := <z, .>:  <f_z, P^k f_z> = tau_k |z|^2/4,  Var_nu(f_z) = |z|^2/4,  and
||f_z||^2 - ||P^T f_z||^2 = (1 - tau_(2T)) |z|^2/4.
Proof. T_0(x, w) = e^(-V(x)/2) e^(beta <x, w>) e^(-V(w)/2) is invariant when one gauge transformation acts on x
and on w, and its top eigenfunction is unique, so it is gauge invariant. Hence the law of the whole path is
invariant under gauge transformations that do not depend on the time. Two distinct links do not have the
same pair of end sites. For l != l' take the central element -1 at an end site of l that is not an end
site of l': it changes the sign of X_(0,l) and not of X_(k,l'), so the expectation vanishes. For l = l'
the matrix commutes with q -> g q h^(-1) for independent g, h at the two ends, that is with SO(4), so it is a
multiple of Id_4; take the trace. The same flip gives E X_(0,l) = 0. tau_(2j) = 4 <f_z, P^(2j) f_z>/|z|^2 >= 0. QED

**Corollary NS (no soft linear statistic; PROVED).** In the ambient coordinates in which Theorem BR is
posed, the slice covariance is exactly (1/4) Id_N, and every linear statistic <z, x>, smooth at the unit scale
or rough, has the autocorrelation tau_k of one link. A covariance of the form sum over k of
R_0 D_k C_k D_k^T R_0^T with norm of order L^K/beta_K is not the covariance of the slice law in these
coordinates. (For nu_s the same holds with v_s of row 947 5.5 in place of 1/4.)

**Lemma KL (a Gaussian chain carries the bare stiffness at every frequency; PROVED).** One real mode, as
in row 947 5.4: the kernel is the heat kernel of time 1/beta, m(dw) = e^(-c w^2/2) dw, c > 0, and
omega := log(1 + c/beta). Then the vacuum chain is the stationary Gaussian process with
E[X_0 X_k] = sigma^2 e^(-omega |k|), sigma^2 = 1/(2 beta sinh omega), and:

- (i) its spectral density is S(p) = 1/(beta (2 - 2 cos p) + 2 beta (cosh omega - 1)), p in [-pi, pi];
- (ii) E |X_T - X_0|^2 = (1 - e^(-omega T))/(beta sinh omega) <= T/beta for every T >= 1;
- (iii) for every finitely supported real sequence (c_t) with sum zero, Var(sum of c_t X_t) is at most its
  value for the free walk with step variance 1/beta, namely (1/beta) times the integral over [-pi, pi] of
  |c-hat(p)|^2/(2 - 2 cos p) dp/(2 pi).

Proof. The two-slice law J has precision matrix [[beta + c, -beta], [-beta, beta + c]] (`gap-fc-max.md` L510),
and beta + c = beta e^omega. So E[X_1 | X_0] = e^(-omega) X_0, and the precision of nu is
(beta + c) - beta^2/(beta + c) = beta (e^omega - e^(-omega)) = 2 beta sinh omega. A stationary Gaussian Markov chain with
these two numbers has the stated covariance. (i) The sum over k of e^(-omega |k|) e^(i k p) is
sinh omega/(cosh omega - cos p); multiply by sigma^2. (ii) E |X_T - X_0|^2 = 2 sigma^2 (1 - e^(-omega T)), and
1 - e^(-omega T) <= T (1 - e^(-omega)), and (1 - e^(-omega))/sinh omega = 2/(e^omega + 1) <= 1. (iii) The variance is the integral
of |c-hat|^2 S dp/(2 pi), S(p) <= 1/(beta (2 - 2 cos p)), and c-hat(0) = 0 makes the integral finite. QED

Consequences, each one line from (i)-(iii), for any Gaussian chain with this kernel (a product of such
modes):

- (K1) The precision of the path measure in a mode is beta (2 - 2 cos p) + mu^2, mu^2 = 2 beta (cosh omega - 1). The
  coefficient of the time-like difference term is the bare beta at every frequency. It does not run.
- (K2) Slice variance and rate are tied: 2 beta sigma^2 sinh omega = 1. A mode with sigma^2 >= S has omega <= 1/(2 beta S).
- (K3) If a two-sided, isotropic form bound a_- beta_K (2 - 2 cos p + q^2) <= beta (2 - 2 cos p) + mu^2 <=
  a_+ beta_K (2 - 2 cos p + q^2) holds for one frequency with 2 - 2 cos p >= q^2, then beta <= 2 a_+ beta_K.

### 6.4 T3 in the valid form of a discard test (skill 6c)

The tool: H = "(P1)-(P3) at the levels below the unit, and one inequality at the unit"; T = "(LSI-br)
with a rate free of the cutoff"; the class K = reversible chains with the kernel e^(beta_0 <x, w>), on which
Theorem BR is posed. T3 says "H does not give T", by a benchmark M'.

1. **The benchmark is outside K (PROVED for Gaussian chains, given the reading of (P1) in (K3)).** A
   Gaussian chain with the slice variance of the count, sigma^2 of order L^K/(a_+ beta_K) in a unit mode, exists.
   By (K2) its rate is at most a_+ beta_K/(2 beta_0 L^K): this is exactly the loss that T3 names. But by (K1) and
   (K3) that chain does not satisfy (P1): its time-like stiffness is beta_0 and its space-like stiffness is
   of order beta_K^2/beta_0, not beta_K in both. A Gaussian chain with (P1) has beta_0 <= 2 a_+ beta_K. So for
   beta_0 > 2 a_+ beta_K no Gaussian chain satisfies the premises of T3. The independent-level Gaussian field
   of T3 satisfies (P1) but is not a chain with the bare kernel (its time-like increments break (ii)).
   In the words of the skill: M' is outside K, or H(M') is false. This agrees with the cross-provider
   finding "no law meeting the claimed common premises is constructed" (`gap-d2-inputs-check-astra.md` L41)
   and makes it exact in the Gaussian class.
2. **The count is not a statement about the functions that (LSI-br) reads (PROVED).** The count is made
   in a gauge-fixed chart, for linear statistics. In ambient coordinates no linear statistic is soft
   (Corollary NS). (LSI-br) is posed for gauge-invariant functions. The check of row 1000 found the same
   defect at one line (`gap-d2-inputs-check-astra.md` L45-52).
3. **On gauge-invariant functions the chain gives the bare coupling by an identity (PROVED given (E1)).**
   For continuous gauge-invariant f of mean zero, Proposition FR with T = 1 and the definition of the
   gap give Var_nu(f) (1 - e^(-2 E_1)) <= EE(f). (This is the paragraph after Lemma TEL in row 982, there
   ARGUED because (a') was; with (E1) it is exact.) So no upper bound on gam_s or alpha_s below the bare
   order follows from the structure of the chain.
4. **What stays true (PROVED in row 982, Lemma TEL; check 982 HOLDS).** Lemma TEL, used with the operator
   norm of sum over k of D_k D_k^T/rho_k, cannot return more than a_- beta_K a/l_unit. This is a statement on
   one estimate.

**Verdict on T3: FAILS as a discard test; it stands as a warning on one estimate.** No model with H true
and T false is on record, and none exists in the Gaussian class.

### 6.5 The first lemma in a form the chain allows; the attack; where it stops

(LSI-br) reads functions of one slice (or of the bridge point). So a unit-level input has to be a
statement on a gauge-invariant variable V of one slice.

**Lemma LIFT (PROVED, two lines).** Let mu be a probability measure on R^N, V: R^N -> R^d a C^1 map with
law rho. Assume (i) Ent_rho(phi^2) <= (2/varrho) integral of |grad phi|^2 d rho for C^1 functions phi on R^d, and
(ii) G(y) := DV(y) DV(y)^T >= r Id_d for mu-almost every y, r > 0. Then for f = phi(V):
Ent_mu(f^2) <= (2/(varrho r)) integral of |grad f|^2 d mu.
Proof. Ent_mu(f^2) = Ent_rho(phi^2), and |grad f|^2 = <grad phi, G grad phi> >= r |grad phi(V)|^2. QED

So on functions of V the fine constant is varrho r. If the unit-level constant is varrho = varrho_0 beta_K (the
normalisation of (P2)), the bare constant varrho_0 r_0 beta_0 a/l_unit follows from

  (R-pt)   G >= r_0 (beta_0/beta_K) L^(-K) Id_d almost everywhere.

**What is proved towards (R-pt).** Its average along the bridge, for each unit vector e (Proposition FR
with T = L^K): the bridge energy of <e, V> is at least L^(-K) (||<e, V>||^2 - ||P^T <e, V>||^2). If the
increment of <e, V> over two units of time has mean square at least c/beta_K, the mean over s of the
energy is at least c (beta_0/beta_K) L^(-K). Mark: PROVED given (E1) and given that hypothesis on the
increment, which is not derived from the account here.

**Lemma NB (why (R-pt) has the right size; PROVED, calculus).** Let S_1, ..., S_n be unit vectors of R^d
with mean Phi != 0, and n-hat := Phi/|Phi|. For a unit vector e orthogonal to n-hat:
the gradient of <e, n-hat> with respect to S_i is e/(n |Phi|), so the sum over i of its squared norms is
1/(n |Phi|^2); for the mean itself the sum is 1/n; and <e, n-hat> = <e, Phi>/|Phi|.
Proof. d n-hat = (Id - n-hat n-hat^T) d Phi/|Phi| and d Phi = (1/n) sum of d S_i. QED
Reading. Normalising a block average multiplies its fluctuation and its fine gradient by the same factor
1/|Phi|. So the quotient of variance by squared gradient, which is what a Poincare or log-Sobolev constant
reads, does not see the normalisation. "Running" (the normalised block variable fluctuates more) and
"roughness" (its fine gradient is larger) are one factor. The count of T3 pairs the stiffness of the
normalised variable with the gradient of the linear average. (That the account's block average is of this
kind is a reading of its definition, CA-I Def 1.5; not re-read in this row.)

**Where the attack stops (four points, each exact).**

- (S-a) (R-pt) is pointwise; Proposition FR gives an average. An average does not give a pointwise bound
  (for V(y) = y^3 on the line, G = 9 y^4 vanishes at 0 and has a positive mean under any law not carried
  by 0). No counterexample for the model is claimed. OPEN.
- (S-b) Hypothesis (i) is not a port. (P1)-(P3) are statements on four-dimensional fluctuation fields in a
  block gauge (CA-II 80039-80041, 80156-80172, as quoted in row 982 Step 2). A function of one fine slice
  is not a function of one level's fluctuation field. The account has no equal-time statement: row 985
  found no slab tori and no decay in Euclidean time ((PQ-EX): NO; (TR-LF): not found). OPEN, and new.
- (S-c) Proposition FR bounds an energy by an increment. An entropy cannot be bounded by increments of
  the chain (row 982 Route 2 (a), HOLDS in its check). So FR alone does not give a log-Sobolev inequality.
- (S-d) Hypothesis (i) at the unit is the order-one input. In log-Sobolev form it is stronger than the
  seed. It is the wall.

### 6.6 Result of the attack

| Statement | Mark | Where |
|---|---|---|
| Lemma S1; Proposition FR (bare diffusion bound at every lag) | PROVED; FR given (E1) | 6.3 |
| Lemma EL, Corollary NS (slice covariance is Id/4 at lag 0, tau_k Id/4 at lag k; no soft linear statistic) | PROVED | 6.3 |
| Lemma KL with (K1)-(K3) (Gaussian chains: bare time-like stiffness at every frequency; variance and rate tied) | PROVED | 6.3 |
| T3 as a discard test | FAILS: its benchmark is outside the class of Theorem BR, for every Gaussian chain | 6.4 |
| T3 as a warning on Lemma TEL with operator norms | stands (row 982; check 982) | 6.4 |
| Lemma LIFT; Lemma NB | PROVED | 6.5 |
| (R-pt), the pointwise roughness of a unit variable | OPEN; its bridge average is PROVED given a hypothesis on increments | 6.5 |
| A unit-level log-Sobolev inequality for a gauge-invariant variable of one slice | OPEN; not a port; it is the wall in log-Sobolev form | 6.5 |
| (W), (CAS), the seed | not moved | - |

**Corrected filter (skill: "a corrected filter").** Rule N2 of row 982 and the lead note "a route must use
the transfer structure at each level" are not discard tests. In the valid form: the factor beta_K/beta_0 is a
property of Lemma TEL with operator norms, not of the model; the exact relations of the chain (FR, the
Rayleigh form) carry beta_0; the linear count has no counterpart in ambient coordinates. What comes back:
route LC as a carrier. Where it matters: off the wall. The route still needs the unit inequality.

**For the lead.** Do not queue a proof row on route LC now. Reason: not T3, but (S-b) and (S-d): its first
lemma is not a port and its unit input is the wall. Keep the route as the carrier for the day a unit-level
inequality exists; then (R-pt) is its first open step, and Lemma NB says which size to expect.

No numeric run was made in this row. The lemmas of 6.3 and 6.5 are algebra and one spectral inequality.
