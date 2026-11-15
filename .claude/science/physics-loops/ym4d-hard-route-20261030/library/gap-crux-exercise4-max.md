lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-16T03:56Z

# Row 1003, gap-crux-exercise4-max: the wall exercise on the crux in its new shape

Worker file, pinned at commit 95fecd964 on `claude/ym4d-hard-route` (first run of this item: 9d96f0a06; it wrote
only the plan below). Research-stage working state. Nothing here is a
claim. Marks used: PROVED, ARGUED, OPEN, FAILS. Nothing in this file has been checked by anyone but its author
unless a line says who checked it.

## 0. Plan and status log

Plan (at most eight steps; one step per response; each step is appended here before the next starts):

1. Read the state: `parts/gap.md` (lead rules, obligations, registry, test table, price), the exercise skill at
   main 8b11ae2bb9, row 1002's filter, the statements of Lemma PT, Proposition KF, Theorem D2, Lemma SHEET, (CAS).
   Write Section 1: the crux in its new shape, in one paragraph, with anchors.
2. Task (1): audit the row 1002 filter (the 2D O(N) filter) as the skill audits a discard test. Section 2.
3. Task (2): the list of inputs that 4D SU(2) has and both 2D O(N) and a product with a massless factor lack,
   each with source and lattice status. Section 3.
4. Task (3): for each input, the step of the chain to (W) or (CAS) it would feed, tested against Lemma PT,
   Theorem D2, Lemma SHEET, compact U(1) and the 2D O(N) filter. Section 4.
5. Task (4): the surviving input (if any): exact lemma, registry grep, proof attempt or counterexample. Section 5.
6. Second pass of task (4) if the first attempt leaves a named sub-step. Section 6.
7. Self-audit against the skill's stop rules; table of marks; who checked what. Section 7.
8. RESULT line.

Status log (times from `date -u`):

- 2026-11-15 15:51Z: file created; plan written; nothing done yet.
- 2026-11-15 15:56Z: second run of this item starts from the plan above (the first run left no result). Step 1 begins.
- 2026-11-15 15:58Z: Step 1 done (Section 1 below). Read: `parts/gap.md` in full; the exercise skill and its
  proof-search governance reference at main 8b11ae2bb9 (fetched to `/tmp/row1003-skill-86957/`); row 1002's file in full;
  row 998 L105-358 and L686-818; `gap-mid-max.md` L40-71, L200-234; `gap-phys-seed.md` L52-66, L249-332;
  `gap-tiltproof-max.md` L236-255; `gap-sepinput-max.md` L356-402; `gap-crux-restate.md` L48-78; FINISH rows 999, 1000, 1003.
- 2026-11-15 16:01Z: Step 2 done (Section 2: the audit of the 2D O(N) filter). Verdict: a price and a routing rule, not a test.

**Skill header (exercise skill, Output rules).** Written by Anthropic Claude Fable 5.2, effort max, Mac mini worker
session, commit 95fecd964, 2026-11-15. Nothing in this file is checked by another model. The skill's framework
refresher is replaced by `GOAL.md` and the rules of `FINISH.md` (a standalone proof target; the skill allows this
replacement and asks that it be said). The row is a targeted run of the skill: task (1) is its step 6c on one filter,
task (2) its step 2 on one question, task (3) its step 7 with the kill pass, task (4) its step 8, and Section 7 its
step 9. Steps 1, 4, 5 and 6a of the skill are not rebuilt: the row forbids it ("do not rebuild them"), and
`parts/gap.md` carries them from row 998.

What this run did not cover (kept true as the run goes): see the list at the end of Section 7.

## 1. The crux in its new shape (state at this pin, with anchors; nothing here is mine)

Objects: Wilson SU(2) on periodic tori; D(a) = F(a^4) - f a^4 >= 0; m(B) the gap of the transfer operator of the
box B; S(k; B) the thermal sum; along a trajectory, D^+(L) and z^-(L) (row 998 1.2, `gap-crux-exercise3-max.md`
L111-127). The wall is (W): one physical size L with z^-(L) > 256 D_0 + 30 (L129-131). Its price: (W) iff
(BDD-Delta) and (Z-UNB) (Theorem ZD-c, `gap-phys-seed.md` L311-320, lane mark "PROVED GIVEN Theorem ZD"); and (W)
follows from (CAS) = (CONTR)_theta with one theta < 1 on a bounded range of sizes, with the extensive base (TH)
(`gap-mid-max.md` L64-67; row 998 8.3, L748-763; base conditional on the account and (DET)). The new shape: the
missing piece is one selective inequality at every scale between first passage and the seed size. Selective means
false for a product with a massless factor (Lemma PT (c), (d): 1 + S = (1 + S_1)(1 + S_2), D = D_1 + D_2; row 998
L690-718; check 999 HOLDS, Corollary PT1 after correction: theorem-grade for Villain U(1) at beta >= 2^14 only).
Lead rule W2 (`parts/gap.md` L90) splits inputs into (K-one), a number at one scale, and (K-flow), a statement that
reads the first-passage data (K_j to infinity at one fixed g) and is carried through the band. The filters on a
(K-flow) step at this pin: (f1) compact U(1) and the free photon bind no (K-flow) hypothesis as single models, but
T_W is false for them along every beta_j to infinity, so the carrying step cannot be class-wide (L1, L4 of row 998);
(f2) a hypothesis that reads one factor of the state space is bound by a product with any no-seed factor (Lemma PT);
(f3) a supremum over tilts is false (Theorem D2, `gap-tiltproof-max.md` L240-247, for SU(2), Q_8, 2T and U(1) alike;
its two inputs are rebuilt by hand in row 1000, unchecked); (f4) a form uniform over plaquette coupling fields is
false for every group (Lemma SHEET, `gap-sepinput-max.md` L360-377); (f5) K7 and w_p bind only hypotheses with no
ultraviolet clause (Proposition KF (c), (d), row 998 L724-738; check 999 HOLDS after correction); (f6), new and
unproved: the 2D O(N) filter of row 1002 (`prior/gap-kflow-read-opus.md` L340-348): "a (K-flow) tool whose transport
step uses no four-dimensional and no gauge-specific input would, read in 2D, prove the O(N >= 3) gap at fixed N".
Row 1002 itself marks (f6) "a test of plausibility, not a theorem-grade test (it binds nothing logically)" (L348).
The registry has no route near closure; RA = (CAS) reopens "on a mechanism that gives theta < 1 from the group"
(`parts/gap.md` L147). Task (1) audits (f6). Tasks (2)-(4) look for that mechanism among the inputs that 4D SU(2)
has and the two comparison classes of (f2) and (f6) lack.

## 2. Task (1): audit of the row 1002 filter (the 2D O(N) filter), as the skill audits a discard test

Source of the filter: `prior/gap-kflow-read-opus.md` L340-348 (row 1002, Claude Opus 5.5 high, checked by no one), and
the lead's wording in `parts/gap.md` L92. The skill's rule is step 6c: a test is a comparison model M'; it refutes a
tool (H, with a written proof of "H implies T" on a class K) only if M' is in K, H(M') is true and T(M') is false;
if T(M') is false it constrains the proof of H; and it does neither when "the proof also runs for M', and T(M') is
true there", or when "H(M') is not known".

### 2.1 The filter in its logical form

- M' = the nearest-neighbour O(N) model on the square lattice, N >= 3: spins in the sphere S^(N-1), weight
  exp(beta sum over bonds of s_x . s_y), periodic tori.
- K = the engine's class read in two dimensions: (TM), Lemma A and the exchange of the two axes (row 998 F1, L237-239;
  Corollary S2, `gap-crux-restate.md` L205, with the seed S(n; 2n) <= 1/20). The lane's own mark for M' in K is
  "plausible ... not proved here (scope corrected, row 698)" (same line). ARGUED here, three lines: the transfer
  operator of a ring is exp(-V/2) K exp(-V/2), K the product over sites of the kernel exp(beta s . s'); that kernel
  is of positive type on the sphere (its expansion in zonal harmonics has positive coefficients) and strictly
  positive, so the operator is positive, trace class, with a simple top eigenvalue and a positive eigenfunction
  (Perron-Frobenius-Jentzsch); the exchange of the axes is a lattice symmetry.
- T(M') = the two-dimensional seed at every beta (T_fix), or its trajectory form (T_W) as beta_j tends to infinity.
- How T(M') stands: it is OPEN, and believed TRUE. A gap at fixed N >= 3 and every beta is unproved (row 998 I37,
  BELIEF about the state of the literature; RECALLED here: theorems exist for small beta at every N, and for large N
  with beta of order N: Kupiainen 1980, Kopper 1999). The dissent of Patrascioiu and Seiler (on file:
  `gap-crux-lit-2.md`, `gap-crux-lit-cross.md`, per row 1002 L344) says T(M') is false at large beta.

So the row of the skill's table reads:

| Test (model M') | Class K | The exact T that fails in M' | How the failure is known | What a tool must use to pass | Binds from |
|---|---|---|---|---|---|
| 2D O(N), N >= 3, fixed N | engine's class in two dimensions (membership ARGUED above) | **none known.** T_fix and T_W are open and believed true | not a failure: BELIEF that T holds; OPEN as a theorem | nothing, as logic | no value of beta |

### 2.2 Verdict

**(a) It is not a test in the valid form. FAILS as a discard test; PROVED as logic (three lines).** A refutation
needs T(M') false. A constraint needs T(M') false. T(M') is not known to be false; the common belief is that it is
true. So a (K-flow) step whose proof also runs for M' is not refuted and is not constrained. It would be a proof of
an open problem. The skill's two exclusion clauses quoted above both apply.

**(b) What it is: a price. ARGUED.** Let a step be a statement H_step with a proof plan. Two cases.

- *Fixed-coupling form.* (CAS) of row 708 is a statement at one coupling: theta < 1 and M with D(3^d) <= M and a
  contraction at every a >= 3 where D(a) is above the threshold. In K it gives the seed at that coupling with no
  ultraviolet input (`gap-mid-max.md` L65). So a proof of (CAS) at every coupling that uses only properties that M'
  has would prove the gap of M' at every beta. That is the open problem as stated. The filter's sentence is exact
  for this form.
- *Trajectory form.* A step that reads first-passage data would, read in two dimensions, prove "first-passage data
  for M' imply the gap of M' for all large beta". Both the implication and its hypothesis are open: no account of
  the kind the lane ports exists for M' (RECALLED: Gawedzki and Kupiainen for the hierarchical model; Mitter and
  Ramadas 1989 for the effective actions of the lattice model; neither was read in this run, and row 1002 H15 says
  the same at digest level). So for this form the filter's sentence is too strong by one clause: the step would
  reduce the two-dimensional gap to its ultraviolet problem. It would not prove it.

In both cases the content is a statement of cost: the step is at least as hard as an open problem of the same
shape. It says nothing about whether the step is true.

**(c) What it binds. PROVED as logic.** Nothing about truth. It binds the estimate of cost and the order of work.
It would bind as a constraint (never as a refutation) only if T(M') were false, that is, only in the scenario of
Patrascioiu and Seiler. Under the common belief, a common mechanism for both models (non-abelian symmetry and
asymptotic freedom, with no property of four dimensions or of gauge fields) is not excluded by any theorem. So
the demand "name the four-dimensional or gauge-specific input" asks for a proof that is easier than the
two-dimensional problem. It is a choice of route, not a condition that a correct proof must meet.

**(d) Is "would also prove an open problem" a refutation or a price? A price.** In the skill's words it is a
discard reason of the kind "it also holds for model X" used with a model where T is not false. As a reason to set
a candidate aside it is invalid. As a reason to cost it, to order it after cheaper candidates, and to test it
first where the answer is known, it is sound.

**(e) The theorem-grade tests of the same kind (the skill asks for them when a test rests on a belief).**

| Test (model M') | Class K | The exact T that fails in M' | How the failure is known | What a tool must use to pass | Binds from |
|---|---|---|---|---|---|
| 2D O(2) (plane rotator) at large beta | as above | T_fix; and T_W along every beta_j to infinity | THM, published, RECALLED, not re-read (Frohlich and Spencer 1981: power-law decay at large beta; McBryan and Spencer 1977 for the upper bound). That "power-law decay gives no seed on periodic tori" needs the 2D form of Corollary S3' and a bridge from tori to the plane; not written in the lane | that the symmetry group is non-abelian (N >= 3) | large beta. It has no asymptotic freedom, so, like U(1) in (f1), it binds no hypothesis that contains first-passage data |
| 2D O(N) x 2D O(2) at large beta_2 (the product device, Lemma PT read in 2D) | as above | T_fix, T_W | as the row above, with Lemma PT (the proof of Lemma PT does not use the dimension) | the whole state space | as the row above |

These two are the two-dimensional copies of (f1) and (f2). They add no constraint that (f1), (f2) do not already
give in four dimensions. So the two-dimensional class contains no new theorem-grade test. Models with asymptotic
freedom and no gap that I can name in two dimensions have complex weights (the O(3) model at theta = pi; a
Wess-Zumino term) and lie outside K. That agrees with point 5 of the test table (`parts/gap.md` L217-219): no
refutation device for (K-flow) tools is on record. Mark of this paragraph: reading; the search behind "I can name"
is my memory, not a literature search.

**(f) Has anything been discarded on the filter? No.** The filter is of today (row 1002, 16:00Z by its own log; the
lead's note at FINISH L1087). No row was set aside by it. So nothing comes back. The correction is made before
the first use.

### 2.3 The filter in a valid form (proposed text; unproved; for the lead)

> For a (K-flow) step, say whether its proof plan would also run for the two-dimensional O(N) model at fixed
> N >= 3. If it would: the step costs at least the open two-dimensional gap (fixed-coupling form) or its reduction
> to an ultraviolet problem (trajectory form); the row says so, and its first test is the same statement in a
> two-dimensional model where the answer is known (N = infinity, or the Ising model for the engine). If it would
> not: the row names the input that the two-dimensional model lacks, with its source and its mark. Neither answer
> discards the step. The filter is a price and a routing rule. It becomes a constraint only if the
> two-dimensional gap is false.

### 2.4 One use of the two-dimensional model that is a real test (reading; not run here)

The O(N) model in two dimensions at N = infinity has a gap and asymptotic freedom, and its finite-size gap and
free energy are given by a gap equation on the torus (row 998 3.3, L299-302, names this toy and did not build it).
A candidate H_step that is claimed to hold "because of the gap and asymptotic freedom" must hold there. If it
fails there, the claim of mechanism is refuted (H_step may still hold for SU(2); then it holds for a reason that
the candidate did not name). This is a valid kill test of a mechanism claim. It is not a test of truth for SU(2),
and a pass is no support. It is used in Section 4 only if a candidate reaches that point.

**Marks of Section 2.** (a), (c), (d): PROVED as logic from the skill's definitions and the open status of T(M');
the open status itself is a BELIEF about the literature (RECALLED; row 998 I37 and row 1002 item 6 say the same).
(b): ARGUED. (e): the two rows rest on published theorems that I did not re-read and on a bridge that is not
written. Checked by no one.
