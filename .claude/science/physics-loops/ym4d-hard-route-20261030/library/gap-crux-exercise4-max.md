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
- 2026-11-15 16:19Z: Step 3 done (Section 3: 20 inputs with source, lattice status and the two "lacks" columns). All 20 are on file in the lane; anchors given.
- 2026-11-15 16:23Z: Step 4 done (Section 4: the step each input would feed, and the tests). No input survives with a consumer. Two items go to Step 5: a counterexample to class-wide persistence, and the N = infinity test.
- 2026-11-15 16:25Z: Step 5, first part done (Section 5.1: Proposition NP, a no-seed model of the class whose D contracts on J consecutive doublings; PROVED by hand given named lane inputs and the Peierls bound). Next: 5.2, the N = infinity test.
- 2026-11-15 16:26Z: Step 5, second part: the hand computation of 5.2 and the pre-registered reading of its control run are written; the run has not started.
- 2026-11-15 16:29Z: Step 5, second part done: control run 16:27:02Z-16:27:06Z under the numeric lock (holder row1003-fable-ninf, acquired 16:26:58Z, released after the run; memory 69 percent free before). C0, R1, R2 PASS by the pre-registered reading. Results in 5.2.
- 2026-11-15 16:31Z: Step 6 done (Section 6: a second derivation of NP (a) that does not use Theorem SH; five further candidates, each found again in the lane and not attacked).

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

## 3. Task (2): the inputs that four-dimensional SU(2) has

Method. I wrote the list from the definitions and from the literature I know, then ran `grep` over `library/gap-*.md`
and `library/prior/gap-*.md` for each input before naming it (the lane rule). Every input below is already on file;
the lane anchor is in the table. The account's own statements were looked up in `library/sa-index/ca-full/index.tsv`
(titles only; the proofs were not read here). No input in this table is mine.

Columns. "Order one": is it a theorem on the lattice at a coupling of order one? "2D O(N)": L = the model lacks
it, A = it has an analogue (named). "Product": for M_1 x M_2 with M_1 = Wilson SU(2) and M_2 massless, K = the
product keeps the input, L = it lacks it. "Q_8, 2T": does the frozen finite group share it? This fourth column is
not asked by the row. It is added because it decides the result of this section.

| # | Input | Source: account first, then literature, then the lane anchor | Mark | Order one | 2D O(N) | Product | Q_8, 2T |
|---|---|---|---|---|---|---|---|
| 1 | Centre Z_2 one-form symmetry: flux sectors, (TM-c), twisted partition functions, Identity FL | account: flat fields with non-central holonomy, CA-I 4.24:prop-flat-holonomy L102460 (it does not use sectors); 't Hooft 1979; `gap-mid-max.md` L219-227 | THM, lane | yes | A: the central element -1 of O(N); charge parity and antiperiodic rings; 4 sectors, not 64 | K | yes |
| 2 | Fact T: the single-plane twist has classical cost zero (-1 is the commutator of i sigma_1 and i sigma_2) | `gap-crux-restate.md` L53; `gap-crux-exercise2-max.md` L192 (a) | DEF-level fact | yes | L for the central twist (cost beta pi^2 n_2 / (2 n_1), a gradient energy); for N = 3 a twist by a rotation costs zero on its axis | K | yes (i sigma_1, i sigma_2 lie in Q_8) |
| 3 | 't Hooft duality: electric and magnetic flux are both two-form fluxes in 4D; the axis exchange mixes the 64 twists | 't Hooft 1979; Theorem R, row 737, `gap-means-max.md` Section 4; check row 744 (`gap-brainstorm-max.md` L39) | THM, lane, cross-provider check | yes | A, poorer: the exchange of the two Z_2 twists; no crossed sectors | K | yes |
| 4 | Lattice Bianchi identity: the plaquette field is a product measure conditioned on every 3-cube | account: CA-II 8.10:lem-pure-gauge L114125; ours: `library/lattice-uhlenbeck.md` Lemma U; `gap-skeleton-max-b.md` L94-95, L215-216 | DEF-level fact | yes | A: the bond variables of a spin model are a flat connection | K | yes; U(1) too |
| 5 | Local gauge invariance: Elitzur; the Gibbs mean of the Hessian is diagonal; only closed flux | Elitzur 1975; `gap-brainstorm-max.md` L336 (idea 48) | THM | yes | L (global symmetry only) | K | yes; U(1) too |
| 6 | No continuous global symmetry of any degree: the centre is finite | `gap-crux-restate.md` L160; `gap-crux-fp.md` L88; `gap-brainstorm2-max.md` L179 (idea 29: the massless branch needs an emergent two-form current) | DEF-level fact | yes | L (it has the continuous O(N) symmetry) | L for a U(1) or free-scalar factor; K for a critical Ising factor | yes |
| 7 | Loop equations in Ward form; SU(2) Mandelstam constraints | Makeenko and Migdal 1979; rows 754, 756 (`gap-brainstorm-max.md` L41); `gap-form-exercise.md` L352 ("numerical, rule f") | THM, lane (Ward form) | yes | A (Schwinger-Dyson equations) | K | no (they need integration by parts on the group) |
| 8 | Comparison of gauge theory in d dimensions with the chiral model in d - 1 | Durhuus and Frohlich 1980; `gap-next3-max.md` L39; `gap-brainstorm2-max.md` L263 | THM, published; lane rows 825, 828 for the range beta_W < 2/3 | yes, as an inequality; its use stops at 2/3 | L (it is the comparison model: 3D gauge theory is bounded by a 2D O(4)-type model) | K | not checked here |
| 9 | Deconfinement at fixed time extent and large beta | Borgs and Seiler 1983; `gap-crux-exercise2-max.md` L155, L430 | THM, published, RECALLED (row 869 found a mismatch in one use) | yes; it is a negative input: thin boxes have no seed | L (no thermal transition in 1+1 dimensions) | K | yes (and at every time extent) |
| 10 | Positive Ricci curvature of SU(2); O'Neill's term on the orbit space | Singer; Feynman 1981; `gap-brainstorm-max.md` L309, L400, L486, L627 (ideas 27, G9); rows 812, 957, 968 | THM as geometry | the geometry yes; its consumer (Bakry-Emery) only below beta about 1/8 | A for the fibre (the sphere); L for the O'Neill term (no gauge quotient) | L as a lower bound on the whole space (a U(1) factor is flat) | no (discrete) |
| 11 | One-plaquette weight: SU(2) = S^3, log-linear weight, Turan log-concavity of c_j | rows 995, 996; `gap-mid-max.md` L48 | THM, published, cited | yes; kind (K-one) | A (exp(beta s . s') on the sphere) | K | no |
| 12 | Fact B: b_0 = 11/(24 pi^2) > 0. One doubling lowers 1/g^2 by 2 b_0 log 2 = 0.064 | account: CA-II 5.14:thm-one-loop-law L27042 (PROVED there), CA-I 4.2:lem-one-loop L3901 (CITED: Balaban CMP 109 (1.22) and Theorem 3, CMP 116 (2.41)); first-passage datum SA L6854-6861; `gap-crux-restate.md` L53 | THM, published, perturbative; account: conditional | no. "No exact inequality found here or in the sources uses Fact B at couplings of order one" (L53) | A: b_0 = (N - 2)/(2 pi) > 0 | L for the massless factor (a free photon does not run) | no |
| 13 | The account's effective actions on the trajectory: stability (ST5)-(ST6), the torus floor l_*(g), (TH), class S | SA L23767-23812, L21454-21534; CA-II 83837-83876, remark "no spectral gap" 84176-84185 (anchors of rows 970, 984); (TH): `gap-ladder-max.md` L141-150 | SUPPLIED (conditional on the account's packages) | no (g small) | L (no such account in print; RECALLED, not searched here) | L (it is a statement about Wilson SU(2); for a product it covers one factor) | no |
| 14 | Small-volume structure: toron valley, gap 4.1167 g^(2/3)/L, flux splitting exp(-12.4637/g); in a twisted box no zero modes and a gap of order 1/L | Luscher 1982; van Baal; `gap-phys-seed.md` L194; `gap-brainstorm2-max.md` L220 (idea 15); (AC'-lat) `gap-crux-restate.md` L76 | BELIEF (perturbative) | no | A (the rotor zero mode; the coupling of Luscher, Weisz and Wolff) | K | no |
| 15 | Instantons: action 8 pi^2/g^2; fractional charge in twisted boxes; centre-vortex semiclassics on R^2 x T^2 | Belavin et al. 1975; 't Hooft; Tanizaki and Unsal; `gap-brainstorm-max.md` L316, L404 (idea 31); `gap-brainstorm2-max.md` L175, L230 (idea 25) | BELIEF (semiclassical) | no (RECALLED: a topological charge on the lattice needs small plaquettes) | N = 3: A (action 4 pi/g^2); N >= 4: L | K | no |
| 16 | Trace anomaly and sum rules: the finite-size shift of the plaquette is a scale derivative | Michael; `gap-brainstorm-max.md` L311 (idea 29), L484 (G8); (VIR_K) `gap-mid-max.md` L52-58; Theorem D (f) | the beta-derivative identity is a THM, lane; the link to a scale derivative needs scaling | the identity yes | A | K | no |
| 17 | Freedom of the bare weight inside the universality class | (UNIV-FP) `gap-next3-max.md` L282; C4 there L318-319 | OPEN question | no | A | not applicable | no |
| 18 | In 4D a free photon is infrared stable; in 2D and 3D the massless candidate is unstable | Guth 1980; Frohlich and Spencer 1982; row 1002 item 5 (L336-339); row 786 for Villain at beta >= 2^14 | THM at very large beta | yes, against us | L, to its advantage | not applicable | not applicable |
| 19 | Self-duality of two-forms in 4D: Bogomolny bound; self-dual Z_2 gauge theory | `gap-crux-exercise-r858-max.md` L155 | THM for Z_2 only | for Z_2 only | L | K | Z_2 part only |
| 20 | Plaquettes are surfaces: area law as an order parameter; Seiler's and Simon-Yaffe's bounds; Tomboulis-Yaffe inequality | `gap-crux-restate.md` L65-70 (C2, Theorem F); Kanazawa (GUIDE there) | THM, published, cited | yes | L (random walks; no string tension) | K | yes |

### 3.1 What the table shows

**S1 (reading of the table; each cell has the mark of its row).** The row asks for inputs that both comparison
classes lack. In the strict sense there are two: input 13, the account's data, and input 6 against a factor with a
continuous symmetry. For all other inputs the product keeps what its SU(2) factor has. This is as it must be: the
product device (Lemma PT) binds steps that read one factor. It does not bind inputs.

**S2 (ARGUED from the table; this is the result of the section).** Sort the inputs that are theorems on the
lattice at order-one coupling by the last three columns.

- *Gauge kinematics* (1, 2, 3, 4, 5, 6, 9, 20, and 19 in its Z_2 part): the two-dimensional O(N) model lacks them
  or has a poorer analogue. The frozen groups Q_8 and 2T share every one of them. In particular Fact T holds for
  Q_8, because the twist eaters i sigma_1 and i sigma_2 are elements of Q_8.
- *Geometry of a continuous non-abelian fibre* (10 for the fibre, 11, 7, 16): Q_8, 2T and U(1) lack them. The
  two-dimensional O(N) model has an analogue of each.
- *Both at once:* one input only, the O'Neill term of input 10 (the curvature that the gauge quotient adds to a
  continuous non-abelian fibre). U(1) lacks it (the vertical commutator vanishes), Q_8 and 2T lack it, the
  two-dimensional model has no gauge quotient, and a product with a U(1) factor has flat directions.

So, at theorem grade and at order-one coupling, no input on this list separates Wilson SU(2) from the frozen
groups and from the two-dimensional O(N) model at once, except the O'Neill term. Its only known consumer is a
Bakry-Emery bound, which the Hessian of the action defeats above beta about 1/8 (rows 812, 957, 968; set-aside
method 31 of `parts/gap.md` L63). The other inputs that separate SU(2) from both classes are perturbative
(12, 13, 14, 15): they are statements at small g, and they are the first-passage data themselves.

**S3 (reading).** This is the sentence of row 998 6b (`parts/gap.md` L41-43) seen from the side of the inputs:
"the one selective fact that is provable today, asymptotic freedom at small coupling, has no engine that carries it
across the band". The list adds no input to it. What it adds is the sorting: the exact inputs fall in two classes,
and each class is shared with one comparison family in which the conclusion fails or is open.

**Marks of Section 3.** The table: each row has the mark shown; "A", "L", "K" cells are DEF-level readings of the
models, not proved lemmas, except where a lane row is cited. S2: ARGUED. The column "Q_8, 2T" for rows 8 and 19 was
not checked. The list is "every input I could name and find", not a proof that no other input exists.

## 4. Task (3): the step each input would feed, and the tests

The chain to (W), cut in steps (from Section 1 and `gap-mid-max.md` L219-227):

- (st-B) the base: a bound on D^+ at the size where the band starts ((TH), given (DET)).
- (st-P) the perturbative stretch: from the account's small g to a coupling of order one.
- (st-C) the contraction of D in the band: (CAS) with theta < 1.
- (st-F) the flux half: the weight U of the sectors of non-zero flux is small (L E_e(L) unbounded).
- (st-0) the zero-flux half: S_0 is small (L m_0(L) unbounded).
- (st-E) the engine from the seed on (Theorem S; done).

Tests, in the valid form of the skill: PT = product with a no-seed factor (Lemma PT); D2 = Theorem D2; SH = Lemma
SHEET; U(1) = compact U(1) at weak coupling; FG = frozen Q_8, 2T; 2D = the two-dimensional O(N) model, read as in
Section 2 (a price, never a refutation). "-" means the test does not apply to this kind of step. A "pass" entry
says only what a proof must use.

| # | Input | Step it would feed | PT | D2, SH | U(1) | FG | 2D (price) | Verdict; where the lane has it |
|---|---|---|---|---|---|---|---|---|
| 1 | centre flux sectors | (st-F), through Identity FL and Theorem F | binds: a product with a centre-neutral massless factor passes every flux-half statement and has no seed; so (st-F) never gives (W) alone (`gap-mid-max.md` L229-232) | - | the flux half is false there | the flux half is false there at large beta; so the input is not enough | the charged sector is the whole 2D problem | found again: row 731, registry RE (blocked-local at (EV-STEP)) |
| 2 | Fact T | (st-F) at small size: a twisted box with no classical cost and no zero modes; the chart (CH) of (AC'-lat) | as row 1 | - | lacks Fact T: pass | **refutes** "Fact T gives the flux half" in the frozen limit: Q_8 has the twist eaters and T_per fails (check 884 for the frozen limit; at order one a BELIEF) | lacks | dead as a single input; found again: row 697 C5, row 859 idea 31, row 876 ideas 10, 15 |
| 3 | 't Hooft duality | already consumed: Theorem R reduces the seeds to the even seed (ES) | (ES) reads the whole even sector: pass | - | different duality (continuous centre) | Theorem R holds for them; (ES) fails in the frozen limit (check 884) | poorer analogue | consumed; the open statement is (EV-STEP), registry RE |
| 4 | Bianchi identity | none. It is the constraint that makes the plaquettes dependent (`gap-skeleton-max-b.md` L94-95) | - | - | shares it (the photon is its consequence) | share it | analogue | not an input of a selective step; row 962 (no relaxation of the constraint system is a new input) |
| 5 | Elitzur; mean Hessian diagonal | (st-C), (st-0) through an averaged curvature criterion | - | D2 and SH bind the supremum and all-fields forms | shares it | share it | lacks | found again: row 863 ("exact but not a handle"), row 968 Proposition AVG |
| 6 | no continuous symmetry | (st-0): exclusion of the massless branch ("massless needs a symmetry") | binds: a critical Ising factor is massless at one coupling with no continuous symmetry (device of row 708); for a massless phase with no symmetry I know no theorem-grade model | - | has a continuous centre: pass | share it and have no seed (degenerate sectors, not massless) | lacks | no theorem: Goldstone's theorem has no converse. Found again: row 876 idea 29; row 988 Route 3 (set aside 28, re-judged "too strong" by row 998) |
| 7 | loop equations | none by hand (the bootstrap is numerical) | - | - | linear loop equations | lack | analogue | set aside under the no-computer rule: `gap-form-exercise.md` L352 |
| 8 | Durhuus-Frohlich comparison | (st-F): area law from decay in the 3D chiral model | - | - | - | - | it is the comparison model | range-limited: the 3D model orders at large beta (RECALLED), so the use stops at beta_W < 2/3. Found again: rows 825, 828, 831 |
| 9 | Borgs-Seiler deconfinement | none (a negative input) | - | - | - | - | lacks | exercise 2 I19, test K6 |
| 10 | Ricci curvature; O'Neill term | (st-C), (st-0) through a Bakry-Emery or Polchinski bound | pass (a U(1) factor is flat) | D2 and SH bind the supremum and all-fields forms | flat: pass | lack: pass | fibre part: the 2D price; O'Neill part: no analogue | no consumer above beta about 1/8: rows 812, 957, 968; set-aside method 31 |
| 11 | one-plaquette weight | kind (K-one), not (K-flow) | - | - | - | - | analogue | no consumer: row 996 |
| 12 | Fact B, b_0 > 0 | (st-P) at its lower end: D falls and z rises at a rate of order b_0 g^2 per doubling (GUIDE, `gap-mid-max.md` L212) | pass (D is additive, the photon part does not fall) | - | b_0 = 0: pass | lack | has it: the same statement holds there; the price is the 2D one | feeds the entry only; theta tends to 1 as g tends to 0. It needs D^+ to precision g^2, and the account gives an extensive bound. Found again: row 708 5.2 |
| 13 | the account's effective actions | (st-B) | - | - | - | - | lacks | the base only: rows 978-994. Row 982 N2 in the form of row 1000 forbids one use of it for the band |
| 14 | small-volume structure, twisted box | start values (z near 0, D large; twisted: z of order one); then a continuation in the size | as row 1 for the twisted half | - | no isolated twisted vacuum: pass | lack | analogue (twisted rings; the Luscher-Weisz-Wolff coupling) | the continuation is the band itself: "no monotonicity" (`gap-brainstorm-max.md` L404). Found again |
| 15 | instantons | none through order one | - | - | lacks | lack | N = 3 has them | first-passage statement in another geometry (idea 31). Found again |
| 16 | trace anomaly, sum rules | (st-C) in the coupling: (VIR_K), (NOCRIT-HF), the sign in beta (registry RB) | pass | - | the shift vanishes: pass | - | analogue | blocked-equivalent: registry RB; (MONO-Delta) is false for the ordered Ising model (`gap-phys-seed.md` L371-373) |
| 17 | freedom of the bare weight | (st-F) for a weight with a Griffiths structure of the centre (C4) | as row 1 | - | - | - | analogue | VARIANT, needs (UNIV-FP), open: `gap-next3-max.md` L282, L318 |
| 18 | photon stable in 4D | none (against us) | | | | | | row 1002 item 5 |
| 19 | self-duality of two-forms | none for SU(2) | | | | | | - |
| 20 | surfaces, area law | (st-F): Theorem F given (FLUX-4) | as row 1 | - | the inequality of Tomboulis and Yaffe holds for U(1) too (GUIDE, Kanazawa); (TUBE) fails there | (FLUX-4) fails there | lacks | found again: row 697 C2 |

### 4.1 What the table shows

**V1 (ARGUED; the rows cite the lane's verdicts, which I did not re-derive: "valid as reported").** No input of
Section 3 survives with a consumer. Each one falls in one of five cases.

- Its step is already consumed by a theorem of the lane: 3.
- It feeds the base or the entry of the band, and nothing in the band: 12, 13, 14, 15.
- Its step is blocked at a statement that the registry already holds: 1 and 20 at (EV-STEP) and (FLUX-4), 16 at RB.
- Its step fails in a model of the class: 2 (frozen Q_8; theorem in the frozen limit, belief at order one), 6 in
  its class-wide form (a critical Ising factor).
- It has no step, or its consumer stops below the band: 4, 5, 7, 8, 9, 10, 11, 17, 18, 19.

**V2 (reading).** The five tests split as follows. PT binds every step that feeds (st-F) alone: the flux half
never gives (W). D2 and SH bind only the curvature inputs 5 and 10. U(1) is passed by every input that uses the
commutator or the running. FG is the test that the gauge-kinematic inputs fail. The two-dimensional model prices
the inputs of the continuous fibre. So the two families of Section 3.1 meet two different tests, and no single
input passes both with a consumer.

**V3 (one place where a statement of the lane is ARGUED only and a counterexample can be built).** The test table
(`parts/gap.md` L193) carries "ARGUED only: it also refutes a class-wide step 'a decrease of D or S under doubling
persists'" (row 998 L5; check 999 L203: "correctly marked ARGUED (L5 says the two factors were not constructed)").
This is the class-wide form of the step (st-C). Section 5.1 builds the two factors.

**V4 (one test named and never run).** Row 998 3.3 names the O(N) model in two dimensions at N = infinity as the
toy for a claimed statement along scales and does not build it. Section 2.4 says what such a test can show.
Section 5.2 runs it by hand for (CAS).

## 5. Task (4): attempts

The row's first clause ("if one input survives with a consumer, write the exact lemma it needs") has no case: by
V1 no input survives. The second clause ("if a step fails in a model of the class, build the counterexample") has
one case that is not on record as a construction: V3. Section 5.1 builds it. Section 5.2 runs the test of V4.

Rule 0a before each attempt. `library/open-core.md` has no line of the gap lane (it lists hard-core items; `grep`
for gap, seed, (W), CAS returned only unrelated lines). `grep -l -i` for "persist" with "decrease" over
`library/gap-*.md` and `library/prior/`: three files, row 998, its check 999 and the draft of `parts/gap.md`; all
three carry the statement as ARGUED, with no construction. `grep -l -i "gap equation"`: row 998 (the toy named,
not built), row 1002 (literature), rows 934 and its check (another object). So neither attempt repeats a row.

### 5.1 Proposition NP: contraction of D on any number of doublings does not persist in the class

**Setting.** "The class" is the engine's class: models on the periodic lattice Z^4 tori with a partition function
that is invariant under permutations of the axes, with (TM) in each direction, and a simple top eigenvalue
(`gap-seed-shape.md` L207). D, Phi, S as in Section 1; for every model of the class, Phi(n) = 16 F(n^4) - F((2n)^4)
is non-negative (Theorem D (a), Lemma A).

**Inputs, each with its mark.**

- (i1) Lemma PT (a), (d) (row 998 L690-713; check 999: HOLDS). Its proof uses (TM), the symmetry of Z and the
  monotonicity I3 of each factor, and nothing about gauge fields. So it holds when a factor is a spin model of the
  class; this is the device of row 708 (`gap-mid-max.md` L230). By induction it holds for finitely many factors.
- (i2) D(2n) = 16 D(n) - Phi(n) <= 16 D(n), for every model of the class. Proof: D(2n) = F((2n)^4) - 16 f n^4 =
  16 F(n^4) - Phi(n) - 16 f n^4. PROVED (two lines, from the definitions and Phi >= 0).
- (i3) D(n) = sum over i >= 0 of 16^(-(i+1)) Phi(2^i n) (Proposition R of row 697, as used in `gap-phys-seed.md`
  L294). THM, lane, checked rows 698, 699.
- (i4) Wilson SU(2) at small coupling (`gap-seed-sc.md` L34-47, Theorems 1 and 2; lane mark: PROVED GIVEN Theorem
  SC's lemmas, checked in rows 694 and 704). For n >= 4 and 0 <= beta <= 1/12800:
  0 <= Phi(n; beta) <= 0.16 n^4 (12800 beta)^(4n). For each n >= 5: Phi(n; beta) = A_n beta^(4n) + O(beta^(4n+1))
  as beta tends to 0, with A_n = 192 n^3 4^(-4n) > 0.
- (i5) A model of the class with no seed: the Ising model on the sites of Z^4 at a coupling J >= J_P
  (`gap-seed-shape.md` L209-219: membership in the class PROVED there; no gap RECALLED there from the Peierls
  argument, not rebuilt). A seed gives a uniform gap (Theorem S), so this model has no seed.
- (i6) In a model of the class with no seed, D(a) > 6.1 x 10^(-4) for every a >= 3 (Proposition Delta with Theorem
  SH, `gap-mid-max.md` L63; checked row 709).

**Lemma NP0 (two-sided control at strong coupling; PROVED given (i3), (i4)).** Let u(n; beta) be the Casimir free
energy D of Wilson SU(2) at the coupling beta. For n >= 5 there is beta(n) > 0 such that for 0 < beta <=
min(beta(n), 1/25600):

 (A_n / 32) beta^(4n) <= u(n; beta), u(2n; beta) <= 0.176 n^4 (12800 beta)^(8n), and so
 u(2n; beta) / u(n; beta) <= 0.03 n (6.5536 x 10^8 beta)^(4n).

Proof. Put t = 12800 beta <= 1/2. By (i3) and Phi >= 0, u(n) >= Phi(n)/16. By the second line of (i4) there is
beta(n) > 0 with Phi(n; beta) >= (A_n/2) beta^(4n) for 0 < beta <= beta(n). This is the lower bound. For the upper
bound at any m >= 4, (i3) and the first line of (i4) give u(m) <= sum over i of 16^(-(i+1)) 0.16 (2^i m)^4
t^(4 m 2^i) = 0.01 m^4 sum over i of t^(4 m 2^i) <= 0.01 m^4 t^(4m) / (1 - t^(4m)) <= 0.011 m^4 t^(4m), because
t^(4m) <= 2^(-16). At m = 2n this is 0.011 x 16 n^4 t^(8n) = 0.176 n^4 t^(8n). The quotient is at most
0.176 n^4 t^(8n) x 32 x 4^(4n) / (192 n^3 beta^(4n)) = (0.176 x 32/192) n (12800^2 x 4 x beta)^(4n), and
0.176 x 32/192 < 0.03, 12800^2 x 4 = 655,360,000. QED

**Proposition NP (PROVED given (i1)-(i6); the only input that is not rebuilt in the lane is the Peierls bound
behind (i5)).** Let J >= 1 be an integer, 0 < theta < 1, and a_0 >= 5. Put n_j = 2^j a_0. There are a coupling
beta_s > 0, an integer K >= 1 and a model M of the class, the product of K copies of Wilson SU(2) at beta_s with
the Ising model of (i5), such that:

- (a) M has no seed, and D_M(a) > 6.1 x 10^(-4) for every a >= 3;
- (b) D_M(n_(j+1)) <= theta D_M(n_j) for j = 0, 1, ..., J - 1;
- (c) there is j >= J with D_M(n_(j+1)) > theta D_M(n_j).

So in M the contraction (CAS) holds, with the given theta, on J consecutive doublings on which D is above the
threshold, and M has no seed.

Proof. Choose beta_s with 0 < beta_s <= 1/25600, beta_s <= beta(n_j) and 0.03 n_j (6.5536 x 10^8 beta_s)^(4 n_j) <=
theta/2 for j = 0, ..., J - 1. This is a finite set of conditions, each true for all small beta_s. Write u(n) for
u(n; beta_s) and v(n) for D of the Ising factor. By Lemma NP0, u(n_j) > 0 and u(n_(j+1)) <= (theta/2) u(n_j) for
j < J. Choose an integer K >= (32/theta) v(n_j)/u(n_j) for every j < J. Let M be the product. By (i1),
D_M = K u + v, and a seed of M at a size N would be a seed of each factor at N. The Ising factor has none (i5).
So M has no seed, and (i6) gives (a). For j < J, by (i2) for the Ising factor and the choice of K:

 D_M(n_(j+1)) = K u(n_(j+1)) + v(n_(j+1)) <= (theta/2) K u(n_j) + 16 v(n_j) <= (theta/2) K u(n_j) + (theta/2) K u(n_j)
 <= theta D_M(n_j).

This is (b). If (b) held for every j >= 0, then D_M(n_j) <= theta^j D_M(n_0) would fall below 6.1 x 10^(-4),
against (a). So (c) holds. QED

**Corollary NP1 (what it refutes; PROVED as logic from Proposition NP).** Let J >= 1 and theta, theta' in (0, 1).
The following statement is false in the class: "if D(2^(j+1) a) <= theta D(2^j a) for j = 0, ..., J - 1 and
D(2^J a) > 6.1 x 10^(-4), then D(2^(j+1) a) <= theta' D(2^j a) for every j >= J with D(2^j a) > 6.1 x 10^(-4)".
(Take theta_0 = min(theta, theta') in Proposition NP: (b) gives the hypothesis, and (c) with (a) contradicts the
conclusion.) So no class-wide induction step for (CAS) reads only the history of D on finitely many scales.

**Remarks.**

1. *What is new against row 998.* L5 of row 998 argued the same conclusion from a massless factor "whose D
   converges" and a massive factor "with a long correlation length", and did not construct them. The construction
   above needs neither: the K copies make the falling part large, and (i2) controls the other factor at every
   size. It also needs no theorem about U(1): the no-seed factor is the ordered Ising model.
2. *The count in (CAS) is sharp in the class.* (CAS) with the pair (M, theta) gives the seed after
   k(M, theta) = log(M / 6.1 x 10^(-4)) / log(1/theta) doublings (`gap-mid-max.md` L65). Proposition NP shows that J
   contracting doublings with J < k prove nothing: in the model M the start value D_M(n_0) is so large that
   J < k(D_M(n_0), theta). A proof of (CAS) must cover the whole range down to the threshold.
3. *What it binds.* Class-wide persistence steps, and any step whose hypothesis is a finite history of the
   whole-space quantity D. Lead rule W2 already binds hypotheses that read one factor. This adds: reading the
   whole state space through D alone is not enough either; the step from L to 2L must use a property of the
   measure at the scale L that the product M does not have.
4. *What it does not bind.* A (K-flow) step whose hypothesis contains the first-passage data of Wilson SU(2). M
   is a model at one fixed coupling, with a product group. A concavity statement for log D along doublings is
   false in M (the fall stops), so such a statement is selective; Proposition NP does not say whether it is
   true for SU(2).
5. *The same for S.* By Lemma PT (c), 1 + S_M = (1 + S_g)^K (1 + S_Ising). I did not write the analogue of (b) for
   thermal sums.
6. *On or off the path.* Off the direct path: it is a statement about a filter. It turns one ARGUED cell of the
   test table (`parts/gap.md` L193) into a construction.

Mark: Proposition NP and Corollary NP1 are proved by Claude Fable 5.2 by hand, not yet checked by another model.
The arithmetic to re-check: 0.176 x 32/192 = 0.0293; 12800^2 = 163,840,000; the geometric sum with t^(4m) <= 2^(-16).

### 5.2 The N = infinity test of (CAS) in two dimensions (hand computation: ARGUED, formal at N = infinity; one control run: GUIDE)

**What is tested.** Section 2.3 asks that a (K-flow) candidate be tried first in a two-dimensional model where the
answer is known. The candidate here is the lane's own (st-C): strict fall of the Casimir free energy D under
doubling, with one theta < 1 from a size where the coupling is of order one ((CAS), `gap-mid-max.md` L64). The model
is the O(N) model on the square lattice at N = infinity. Reading fixed before the computation: if D rises
somewhere there, (CAS) is not a consequence of "gap and asymptotic freedom" and the form of the target is too
strong; if D falls, nothing is supported (a pass is no support), and the computation shows by which mechanism it
falls in the one case where the band is crossed by a proof.

**The model at N = infinity (formal; the exchange of the limit N to infinity with the integral is not proved
here; RECALLED as the standard saddle point).** Unit spins s_x in S^(N-1) on the periodic L x L lattice, weight
exp(N b sum over bonds of s_x . s_y). With a Lagrange multiplier for the constraint and the Gaussian integral over
the spins, log Z_N(L) = N [L^2 kappa(b) + min over mu > 0 of phi_L(mu)] + o(N), where kappa does not depend on L and

 phi_L(mu) = (b/2) L^2 mu - (1/2) sum over the L^2 momenta p of log(p^^2 + mu), p^^2 = 4 sin^2(p_1/2) + 4 sin^2(p_2/2).

phi_L is strictly convex in mu > 0, so the minimiser mu_L is unique; it solves the gap equation
(1/L^2) sum over p of 1/(p^^2 + mu) = b. In infinite volume the same holds with the integral over the Brillouin
zone, phi_inf and mu_inf. In two dimensions the integral of 1/(p^^2 + mu) diverges as mu tends to 0, so mu_inf > 0
at every b: this is the infrared divergence that row 1002 item 5 names. Put

 d(L) := limit of D_N(L)/N = min over mu of phi_L(mu) - L^2 phi_inf(mu_inf).

**Step 1 (the variational form; PROVED from the formulas above).** Write psi(mu) := phi_inf(mu) - phi_inf(mu_inf) and
delta_L(mu) := phi_L(mu) - L^2 phi_inf(mu). Then d(L) = min over mu of [L^2 psi(mu) + delta_L(mu)], where:

- psi >= 0, psi is strictly convex, psi(mu_inf) = 0 = psi'(mu_inf);
- delta_L(mu) = (L^2/2) sum over n in Z^2, n not 0, of the integral over t > 0 of (dt/t) exp(-t mu) K_t(nL), with K_t
  the heat kernel of the lattice Laplacian, which is positive. (Poisson summation of the momentum sum, and
  log A = - integral of (dt/t)(exp(-tA) - exp(-t)).) So delta_L > 0, and delta_L is strictly decreasing in mu.

delta_L(mu) is the Casimir free energy of a free field of mass sqrt(mu). The first term is the cost of moving the
mass away from its bulk value. Since delta_L decreases in mu, the minimiser has psi'(mu_L) > 0, so mu_L > mu_inf:
the mass on the torus is above the bulk mass.

**Step 2 (the scaling limit; ARGUED: the lattice corrections of relative order mu are dropped).** For mu small,
psi'(mu) = (1/8 pi) log(mu/mu_inf), so psi(mu) = (1/8 pi) [mu log(mu/mu_inf) - mu + mu_inf], and delta_L(mu) = c(x)
with x = sqrt(mu) L and c(x) = (1/2) sum over n not 0 of (x/(pi |n|)) K_1(x |n|) (K_0, K_1 the Macdonald
functions). With y = sqrt(mu_inf) L, the size in units of the correlation length:

 d(y) = min over x of [Psi(x, y) + c(x)], Psi(x, y) = (1/8 pi) [x^2 log(x^2/y^2) - x^2 + y^2].

The stationarity equation is the gap equation of the torus, log(x/y) = sum over n in Z^2, n not 0, of K_0(x |n|).

**Step 3 (the identity; PROVED from Step 2 by the envelope theorem).** d'(y) = (dPsi/dy)(x(y), y), so

 y d'(y) = - (x(y)^2 - y^2) / (4 pi) = - (L^2 / 4 pi) (mu_L - mu_inf) < 0. (ENV)

In words: the derivative of the Casimir free energy in the logarithm of the size is minus the shift of the mass
squared between the torus and the bulk, in units of the size. The sign is the sign of that shift.

**Step 4 (the two ends; ARGUED, leading orders only).** For y small: sum of K_0(x |n|) = 2 pi/x^2 + O(log), so
x^2 = 2 pi / log(1/y) to leading order, d = (1/2) log log(1/y) + O(1), and - y d'/d tends to 0: the ratio
d(2y)/d(y) tends to 1 at the ultraviolet end. For y large: x^2 - y^2 = 8 y^2 K_0(y) and d = (2y/pi) K_1(y) to
leading order, so - y d'/d = y (1 + o(1)): the ratio d(2y)/d(y) tends to 0 like exp(-y).

**Result (ARGUED given Steps 1 to 4).** At N = infinity, in the scaling limit, d is strictly decreasing at every
size, and for every y_0 > 0 the supremum over y >= y_0 of d(2y)/d(y) is below 1 (d is continuous and positive,
the ratio is below 1 at every y by (ENV), and it tends to 0). So (CAS) holds there from every size at which the
coupling is of order one, with theta tending to 1 only at the ultraviolet end. This is the shape that row 708
5.2 item 2 describes for SU(2) as a GUIDE (`gap-mid-max.md` L212). The test is passed. A pass is no support.

**Control run (GUIDE). Pre-registered reading, written before the run.** The run checks the algebra of Steps 1 to
3 on the lattice formulas. It can show a slip in the hand computation. It says nothing about SU(2).

- Script: `/tmp/row1003-num/ninf.py` (plain numpy; under the numeric lock; core lines copied below after the run).
- Couplings b = 0.6, 0.7, 0.8 (mu_inf = 32 exp(-4 pi b) to leading order: 0.017, 0.0048, 0.0014). Bulk values from
  a periodic 2048 x 2048 lattice (its own finite-size error is of order exp(-2048 sqrt(mu_inf)), below 10^(-30)).
- C0 (control of the bulk solver): mu_inf / (32 exp(-4 pi b)) within 10 percent of 1 at b = 0.8.
- R1: d(L) at every integer L from 4 to 256 (b = 0.8: to 320). PASS if d is strictly decreasing in L at each b.
  FAIL if d(L+1) > d(L) + 10^(-9) anywhere.
- R2: for the integers L from 16 to 256, compare d(16) - d(256) with the trapezoid sum of
  (L^2/4 pi)(mu_L - mu_inf) in log L. PASS if they agree within 5 percent at each b. FAIL above 20 percent. Between
  the two: report as "lattice corrections, not decided".
- R3 (no pass or fail): the table of d(2L)/d(L).

**Control run: result (GUIDE; run 2026-11-15 16:27:02Z to 16:27:06Z, numeric lock held, 0.1 GB, exit 0; output kept
at `/tmp/row1003-num/ninf.out` on the Mini, outside git).** The reading above was not changed.

| b | mu_inf | C0: mu_inf / (32 exp(-4 pi b)) | R1: largest d(L+1) - d(L) | R1 violations above 10^(-9) | R2: d(16) - d(256) | R2: trapezoid of (L^2/4 pi)(mu_L - mu_inf) | R2 ratio |
|---|---|---|---|---|---|---|---|
| 0.6 | 1.6776 x 10^(-2) | 0.9864 | + 7.3 x 10^(-12) | 0 | 0.158161 | 0.155450 | 1.0174 |
| 0.7 | 4.8179 x 10^(-3) | 0.9953 | - 4.6 x 10^(-9) | 0 | 0.317669 | 0.315009 | 1.0084 |
| 0.8 | 1.3755 x 10^(-3) | 0.9984 | - 7.3 x 10^(-7) | 0 | 0.466551 | 0.464390 | 1.0047 |

- C0: PASS (0.9984 at b = 0.8).
- R1: PASS at each b by the written criterion. Limit of the run: at b = 0.6 and L above about 150, d is below the
  floating accuracy of the difference of two numbers of size 10^5 (about 10^(-11)); the one positive step,
  7.3 x 10^(-12), and a value d(256) of order - 10^(-11) are rounding. There the run decides nothing; the hand
  result at large y covers that end.
- R2: PASS at each b (within 5 percent). The mismatch falls with mu (1.7, 0.8, 0.5 percent), as a lattice correction
  of relative order mu should.
- R3, the ratio under one doubling, with y = L sqrt(mu_inf) and x = L sqrt(mu_L):

| b | L | y | x | d(L) | d(2L)/d(L) | (x^2 - y^2)/(4 pi d) |
|---|---|---|---|---|---|---|
| 0.8 | 4 | 0.148 | 1.358 | 0.7379 | 0.824 | 0.197 |
| 0.8 | 8 | 0.297 | 1.523 | 0.6082 | 0.767 | 0.292 |
| 0.8 | 16 | 0.593 | 1.762 | 0.4667 | 0.642 | 0.469 |
| 0.8 | 32 | 1.187 | 2.150 | 0.2996 | 0.417 | 0.853 |
| 0.8 | 64 | 2.374 | 2.914 | 0.1248 | 0.135 | 1.821 |
| 0.8 | 128 | 4.747 | 4.842 | 0.01682 | 0.0116 | 4.284 |
| 0.7 | 16 | 1.111 | 2.100 | 0.3177 | 0.442 | 0.796 |
| 0.7 | 64 | 4.442 | 4.564 | 0.02215 | 0.0157 | 3.947 |
| 0.6 | 16 | 2.072 | 2.707 | 0.1582 | 0.183 | 1.526 |
| 0.6 | 64 | 8.289 | 8.293 | 6.17 x 10^(-4) | 3 x 10^(-4) | 7.771 |

Core lines of the script (plain numpy, `python3 -I`, `nice`; bisection in log mu, 90 steps; bulk on a 2048^2 lattice):
`A = s[:,None] + s[None,:] + mu` with `s = 4 sin^2(pi k/L)`; gap equation `sum(1/A)/L^2 = b`;
`phi = 0.5*b*L*L*mu - 0.5*sum(log A)`; `d[L] = phi(L, mu_L) - L*L*phi(2048, mu_inf)/2048^2`.

**What the test gives, and what it does not.**

1. (CAS) is not refuted as a form of the target by the one asymptotically free model with a proved crossing: at
   N = infinity D falls at every size, and the ratio under doubling is 0.82 at y = 0.15, 0.42 at y = 1.2, 0.012 at
   y = 4.7 (GUIDE values at b = 0.8). A pass is no support for SU(2).
2. The last column of the R3 table rises with the size at each coupling in the run. So in this model the
   logarithm of d is concave in the logarithm of the size at the sizes computed (GUIDE; by hand only at the two
   ends, Step 4). This is route CX of exercise 2 (`gap-crux-exercise2-max.md` L467, L517-523: "wounded: convexity
   is false in the class near an ordered critical point; no blind proof"). Nothing is added to its status for
   SU(2).
3. The mechanism at N = infinity is (ENV), and (ENV) has two halves. The first half is exact and class-wide: the
   derivative of D in the coupling is the number of bonds times the finite-size shift of the bond energy. For
   this model the bond energy is E_L = 1 - 1/(4b) + mu_L/4 (from the gap equation), so the shift is
   (mu_L - mu_inf)/4. For SU(2) the same half is Theorem D (f): dD/d beta = 6 n^4 (abar_inf - abar_n) (row 998
   L780). The second half is the sign and the size of the shift. At N = infinity it comes from Step 1: one
   collective variable, a convex bulk function, a finite-size term that decreases in the mass. For SU(2) the
   second half is the registry's route RB (the sign in beta) with a rate, and (VIR_K) of row 708: blocked, with
   (MONO-Delta) false for the ordered Ising model (`gap-phys-seed.md` L371-373). SU(2) at N = 2 has no collective
   variable of this kind on record.
4. So the test finds no new input. It confirms that in the solvable case the crossing rests on the large-N
   saddle, the "second small parameter" of row 998 3.4 (s1) and of row 1002 item 5.

Marks: (ENV) and Steps 1, 3: PROVED by hand from the N = infinity formulas, which are RECALLED and formal. Steps
2, 4: ARGUED. The run: GUIDE. Written by Claude Fable 5.2, checked by no one.

## 6. Second pass

### 6.1 Proposition NP (a) and (c) without Theorem SH (PROVED; a shorter chain of inputs)

Proposition NP (a) uses (i6), which rests on Proposition Delta and Theorem SH (same-provider check; the
cross-provider check of Theorem SH is row 959, queued, per row 998 I7). Part (c) needs less: only that D_M does not
tend to 0 along the sizes n_j. This follows from Theorem D alone (checked rows 698, 699):

- Theorem D gives 1 + S(n; (2n)^3) <= exp(Phi(n)) (row 998 I5), and (i3) with Phi >= 0 gives D(n) >= Phi(n)/16.
  So D(n) >= (1/16) log(1 + S(n; (2n)^3)) in every model of the class.
- "No seed" for M means S_M(n; (2n)^3) >= 1/5041 for every n >= 3. This holds: by Lemma PT (c), S_M >= S of the
  Ising factor at every box and time, and the Ising factor has S(n; (2n)^3) >= 1/5041 for every n >= 3, because one
  value below 1/5041 would give a uniform gap by Theorem S, against (i5).
- So D_M(n) >= (1/16) log(1 + 1/5041) > 1.2 x 10^(-5) for every n >= 3, and (c) follows as before.

With this, Proposition NP (b), (c) and Corollary NP1 (with the threshold 1.2 x 10^(-5) in place of 6.1 x 10^(-4))
rest on: Lemma PT; Theorem D and Theorem S; Proposition R; Theorems 1 and 2 of `gap-seed-sc.md`; (i2); and the
Peierls bound for the Ising model. Arithmetic: log(1 + 1/5041) = 1.98 x 10^(-4); divided by 16 it is 1.24 x 10^(-5).

### 6.2 Candidates looked at for a second attempt, each found again and not attacked

The skill's rule: search the registry before each attempt; if another row holds it, name the match and stop.

| Candidate (written before the grep) | Match in the lane | What the match says |
|---|---|---|
| A Jensen bound for the twist free energy: spread the vortex by a fixed multiplication of the links and average over the untwisted measure | row 876 idea 14, `gap-brainstorm2-max.md` L216 | "seam multiplication by a non-central constant conjugates the neighbouring links and costs order beta per plaquette for a rough field (ARGUED); the cheapest fixed insertion costs about beta L^2" |
| An exact one-variable form of D by convex duality in the energy density: D(n; beta) = sup over e of [Delta_n(e) - n^4 psi*(e; beta)] | no file has this form; it is Theorem D (f) again | a three-line computation by convex conjugates (F_n and f are convex in beta; D >= 0 gives Delta_n >= 0); not written out here, so its mark is reading. It is useless: its envelope derivative is the identity of Theorem D (f), and nothing is known about Delta_n in n |
| The two-layer SU(2) model with frozen layers is the principal chiral model, so the O(4) model sits in the closure of the gauge class with coupling fields | row 876 G8, `gap-brainstorm2-max.md` L263; Lemma SHEET's mechanism (`gap-sepinput-max.md` L379-381) | in three dimensions the slab is a two-dimensional O(4)-type model; in four dimensions the frozen slab is three-dimensional and orders (rows 950, 952) |
| SU(2) with an adjoint scalar as a test with a non-abelian group and a massless phase | `gap-crux-exercise-r858-max.md` L342 (E3) | "The centre and the twists survive. In four dimensions the Higgs phase has a massless photon. It moves toward the U(1) test" |
| "A massless branch needs a continuous symmetry": a dichotomy with an emergent two-form current | row 876 idea 29, `gap-brainstorm2-max.md` L179 | stated there as an idea; no theorem (Goldstone's theorem has no converse) |

Nothing else was attacked. I found no named sub-step under 5.1 or 5.2 that another proof attempt could take: 5.1
is complete, and 5.2 ends at route RB, which the registry holds as blocked-equivalent.
