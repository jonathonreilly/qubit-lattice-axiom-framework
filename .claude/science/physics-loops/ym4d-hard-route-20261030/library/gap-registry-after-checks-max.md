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
  SEED-FP composition (L398); DEN as one E2 denominator substitution (L378).
- FAILS: G3, the exclusion of projected averaging (explicit normalized-Haar-average counterexample, L372);
  OVL for all trial times or all lenses (L389); the q = 1.6 ordering (L393: q = 8/5 is strictly better than
  q = 3/2 on the proved interval); "each valid in the whole class" (L404); **the global no-gain and
  stop-queuing recommendation (L409): "The support does not exclude the advertised route family. The narrower
  result is that this note supplies no improving variable-geometry bound."**
- Narrowed: DEN's "no room" use holds for one one-side, seed-time comparison only, at most g/23 (L379); the
  dominance table gives no new rectangular numerator bound and does not prove absence of other comparisons (L385).
- Open as before: the seed and (LSI-J-seed) (L410).

**2.2 Row 963 (`gap-rotgeom-opus.md`), check `gap-rotgeom-check-astra.md` (verdict map L314-360, RESULT L370).**

- HOLDS: R1-R4 (twists, mapping torus, characters), frozen trivial-sector counts, the local diagonal reflection
  positivity argument, straight-torus non-separation for N >= 3, Lemma M (no light-cone mirror among lattice
  hyperplane reflections), D2 on the displayed period lattice, same-state conditional D4.
- FAILS: "every sector form fails all rivals" (L335: nonzero-momentum frozen sectors are empty); "no coordinate
  mirrors or axis operators" (L339: an explicit invariant period lattice, and D2's twisted axis channel);
  "same finite thermal sum; only bulk-pressure bridge" (L345); "every seed form passes the fact-test filter"
  (L347); **the three-part "buys nothing" verdict (L350): replace by "no sufficient replacement is established
  here"**; the final result as a blanket obstruction (L357).
- Not supplied by the check (L359-362): (LSI-J-seed), (SEED-FP), a diagonal finite-torus transfer construction,
  an admissible diagonal recursion, shape independence, a projected seed consumer.

**2.3 Row 965 (`gap-squeeze-opus.md`), check `gap-squeeze-check-astra.md` (dispositions L322-354, defects L356-372, RESULT L394).**

- HOLDS (mostly after correction): COUNT on its schedule, BND, SHELL, FLUX, LEAK, PR/window, HALF, QF, the
  free-plaquette endpoint bounds (with 0.03019, 0.03694), the cube static formula, the one-link ceiling 3.
- FAILS: "doubled time for the full SU(2) seed" as an established consequence (overlap input missing, L339);
  top-level periodic r_1^w (L343); literature-to-J equivalence as a supplied implication (L344); the frozen
  centre-even-gap assertion (flat-state construction, L347 and defect 5); the quantitative full-window claim for
  the open endpoint (L348); **"every averaged squeeze is unchanged / every computable endpoint harder" (L354,
  defect 8): "a computable endpoint does not logically force a supremum over exterior data, and no such
  necessity theorem appears."**
- To retain (L374-378): "none of the displayed estimates supplies a new seed bound". Not to retain: the request
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
- Open as before: (LSI-traj-seed) (L205, L248). Raw lattice result files of the GUIDE runs are absent at the pin (L191).

**2.5 Row 968 (`gap-avgcurv-max.md`), check `gap-avgcurv-check-astra.md` (table L312-339, scope notes L341-387, RESULT L474).**

- HOLDS: Proposition FLOW, Lemma Z, Lemma NEC, the positive-radius ANG formula, AVG (b), (c), SCHR, the 6.3
  direction-resolved implication, the (ABS-flow) sufficient implication 7.1 (L335), the horizontal Fourier test
  7.2; POL-BR and AVG (a) after correction (explicit BBD extension, exact sine-cosine argument).
- FAILS: the inference that frozen-group failure must occur at nonzero tilt (L325, L364-372: the necessary
  growth k*/beta to infinity does not exceed the zero-field ceiling O(beta^2)); the broad conditional-CAP
  and (LOC-COV) obstruction claims (L334, L381-387): "LOC-COV plus CAP is one sufficient implementation of an
  averaged estimate. The text supplies no argument that every proof of ABS-flow must use LOC-COV, or that Ricci
  cannot help any collective horizontal direction... The negative conclusions in 5.5 and 8.2 must be
  statements about this attempt, not exclusions of other mechanisms."
- Narrowed: the strict hierarchy of 7.1 is a chain of sufficient implications; strictness and necessity of
  (LOC-COV) are not established (L336). The surviving claim on POL-BR (L352-357): "POL-BR itself has no
  fixed-beta smallness threshold, and the known zero-field obstruction does not kill its finite-interval
  integral. Its actual uniform hypothesis still requires proof."
- DENS (death by volume, L374-379) holds after adding the horizontal premise; it names no seed-box size.
- Open as before: (LSI-J-seed), (LSI-br-seed), (ABS-flow-seed), the seed.

**2.6 Row 977 (`gap-tiltproof-max.md`), check `gap-tiltproof-check-astra.md` (table L380-391, RESULT L404).**

- HOLDS: Theorem D1; D2 steps 5.1-5.4. HOLDS AFTER CORRECTION: Theorem D2 (normalize self-inverse modes, exact
  or downward-rounded constants; "the spectral theorem itself holds"), ZERO-CEIL (remove the unproved 0.234/117
  deduction), CAP (state beta lambda_* >= 3/2; side-4 and side-8 caps hold with exact bounds 589/69 and
  178859/8211), QUOT-CAP (uniform-in-b hypothesis; the side-16 number replaced).
- Scope sentences (L393-396): "No failing structural step was found in the pinned-sheet mechanism... The generic
  box-uniform bound remains open. The finite seed is excluded by ZERO-CEIL, conditional on the stated POL-BR
  output formula and the supplied seed target." Also (L377-378): "Finite-size growth also does not refute
  existence of some finite box-uniform bound without a proved continuation to arbitrarily large sides."
- Not proved: side-120 numerical claims; the uniform-in-b q_0 hypothesis of QUOT-CAP.

**2.7 Row 978 (`gap-ladder-max.md`), check `gap-ladder-check-astra.md` (table L375-388, RESULT L399).**

- HOLDS: Lemma IHC; 5.6 (a) trajectory restriction; the defective inequality with spectral tail (defect is an
  input). HOLDS AFTER CORRECTION: abstract Corollary CU; (TH) through 1.1.5 (iii) with the full vacuum
  normalization and an explicit determinant-comparison input; the (APR) form; R2.
- FAILS: (TH) assumption (a), the literal identification (L380: "The density lemma removes the Gaussian
  normalizers"); **the 5.7 universal method exclusion (L384: "The calculation does not cover methods retaining
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
  a gas model or with hypercontractivity (L105); on the U1 time grid the bound carries an extra 2 T E (L107-112).
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
  988's direction proposals (L457).

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
- FAILS: SHEET's extension to other groups from positive variance alone (cyclic-group example, L310).
- Survives (L316): "The source's SU(2) obstruction to a volume-uniform covariance supremum survives."

**2.13 Row 998 (`gap-crux-exercise3-max.md`), check `gap-crux-exercise3-check-astra.md` (table L133-159, L162-195, RESULT L249).**

- HOLDS: Lemma PT (a)-(d); KF (a), (b); 6d rows 30, 33, ex2 #18, ex2 6c point 1; the frozen Q_8/2T correction.
- HOLDS AFTER CORRECTION: Corollary PT1 (replace "U(1) in its massless phase" by an admitted factor with no
  periodic seed; "an always-false hypothesis is no counterexample to a valid implication", L140); KF (c)
  (require K_j to infinity at one fixed g); KF1 (delete the unconditional list of necessary U(1)/photon tests:
  "each comparison must meet the same H, including its ultraviolet clause", L146); 6d row 24 (the dependency
  is T2 and T3, L151); 6d row 28 (re-admit K-flow: "replace 'valid necessary conditions' by tests whose
  hypotheses must be verified", L152).
- FAILS: **I28, the published Wilson U(1) supplier of "no seed" (L141)**; **KF (d), "it must contain a
  separating number" (L145: "No such necessity follows from contraposition")**; 6d row 28 "(better: w_p)" for
  Route 3 (b) (L153: "V proves no seed, not branch G. Bounded D at its transition is missing"); the claimed
  non-converse of the printed (CONTR) (L162-190: the existential-base (CONTR) is equivalent to (PHYS-SEED) by Z3).
- Kept: the original (CAS) of row 708 (start at size 3, every integer size in its band) has no proved converse
  (L156). Logical limit (L213-219): a Wilson-only first-passage clause already excludes the standalone U(1)
  and free-photon comparisons; "no comparison model constrains an implication before this domain test."

**2.14 Row 1000 (`gap-d2-inputs.md`), check `gap-d2-inputs-check-astra.md` (Step 2 table L33-43, L45-91, disposition L247-267).**

- HOLDS: Lemma RP and Corollary PT (the reflection-positivity inputs). HOLDS AFTER CORRECTION: Lemma GD and
  Corollary IR and their consumption by Theorem D2.
- FAILS: **Step 2's confirmation of T3 and of rule N2**: L42 (e) "no law meeting the claimed common premises is
  constructed"; L44 (f) the claimed Gaussian energy identity is false (exact one-mode check: sigma^2 (1 - e^(-2E))
  = e^(-E)/beta_0, not 1/beta_0; choosing E = (beta_K/beta_0)|p| gives covariance of order 1/(2 beta_K |p|) with
  the bare kinetic coefficient unchanged, L60-83); L46 "The required transfer-structure conclusion does not
  follow... The text has not proved that every level-convexity route must fail or must use the named repair."
- Also a domain defect at L36 (L48-54): the linear colour test f(A) = sum <w_b, A_b> is not invariant under
  constant SU(2) rotations, and Theorem BR needs that invariance; "a suitable invariant nonlinear or quadratic
  test and its estimates are not supplied".
- What may be retained (L85-91): "a conditional benchmark warning, not a proved exclusion". TEL on independent
  levels gives a lower bound on an admissible LSI rate; an upper bound needs a matching sharpness example in
  the tested class, which is not supplied. T3's nonlinear conclusion remains open (L30-31).

**2.15 Summary of Step 2.** The fourteen checks leave the core lemmas standing (most after stated corrections)
and remove eleven broad negative claims as proofs. Those eleven are the input of Section 4:
(i) varying geometry buys nothing (960 L409); (ii) rotated or diagonal geometry buys nothing (963 L350);
(iii) every averaged squeeze is unchanged (965 L354); (iv) the (LOC-COV)/conditional-CAP obstruction and the
frozen-group nonzero-tilt inference (968 L325, L334); (v) the refutation of the integrated-flow, quotient and
ABS-flow forms, and CLASS's threefold failure (970 L226, L229); (vi) the universal method exclusion of 5.7
(978 L384); (vii) the hierarchy U1/U2/U3 and the blanket Poincare-absence claim (982 L93); (viii) the restricted
sector inference of FLOOR and ORD in real time (988); (ix) the full-E_0 identification (993 L196); (x) the
compulsory separating number KF (d), the Wilson U(1) supplier I28, and "(better: w_p)" (998 L141, L145, L153);
(xi) T3 and rule N2 (1000 L42-46). No check supplies a seed, a rate, or any order-one estimate.

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
