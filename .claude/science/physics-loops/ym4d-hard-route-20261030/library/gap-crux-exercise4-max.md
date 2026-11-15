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
