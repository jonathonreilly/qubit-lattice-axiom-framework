lead: anthropic/claude-fable-5-2/high mac-mini-worker
lease_until: 2026-11-24T08:35Z

# gap-mech-direction3-fable (queue row 1442)

Started 2026-11-23T20:35Z (date -u), pinned at commit 27a186f3d, branch claude/ym4d-hard-route. Research-stage working state; nothing here is a public claim.

## 0. Status log

- 2026-11-23T20:35Z: file opened; reading FINISH.md rules, GOAL.md and row 1442.
- 2026-11-23T20:46Z: Section 1 (Phase 1) written before any row after 1378 was opened.
- 2026-11-23T20:51Z: Sections 2.1-2.3 written (the passes; Proposition VIL).
- 2026-11-23T20:53Z: Sections 2.4 and 3 written (inventory; survival of the chain).
- 2026-11-23T20:54Z: Sections 4 and 5 written (decision; next two rows).
- 2026-11-23T20:55Z: anchors verified by grep, PROVED items re-read, RESULT written. No numeric run, no subagent, no
  network fetch. Files written: this one only.
- Plan as carried out: Phase 1 (Section 1, written before any row after 1378 was opened), Phase 2 (Section 2: the
  passes, Proposition VIL, the inventory of other actions and block maps), Section 3 (does the chain survive a
  change of action), Section 4 (decision), Section 5 (the next two rows), Section 6 (labels and RESULT).
  Labels: PROVED, SKETCHED, ARGUED, GUESSED, ON FILE (with the anchor).

Moves: the open item is the mass-gap clause (a later target of `GOAL.md`), through the seed (M-neutral) of row 1367.
If the review finds a level that a change would unblock, the next row attacks there. If not, the band stops and the
capacity returns to the T0 chain.

Credit. The existence chain is Balaban's and Dimock's work and the complete account of Ethan Sussman and Levent
Alpoge (with Claude and Codex as authors of their text). Named literature results below are credited where used.
All literature statements in Section 1 are recalled, not re-read in this row: label `unchecked`.

## 1. Phase 1: which level to choose afresh (blind to rows after 1378)

Blindness, stated honestly. Read before this section: `GOAL.md`, the FINISH rule sections, rows 1332, 1335, 1342,
1349, 1356, 1359, 1367, 1378, 1442, `library/gap-seed-limit.md` L130-210, and my two memory notes on the lane.
Those notes name rows 1386, 1390 and 1402 (earlier Fable passes) in a few lines each. No row after 1378 was opened.
Row 1442's own text states three findings of rows 1434, 1438, 1439 in one sentence each; I use them only in 1.4.

### 1.1 What the target fixes and what it frees

The Jaffe-Witten statement fixes the output: a Euclidean theory on R^4 with reflection positivity, O(4) invariance,
non-triviality and a gap. It frees the regularisation. So the action, the block map and the reduction are all free
in principle. Three facts limit that freedom (SKETCHED, standard):

- (F-a) O(4) invariance and non-triviality force a scaling limit: the correlation length in lattice units must
  diverge. For SU(2) the only known place is zero bare coupling. Every action with that limit has the same
  two regimes: a cutoff scale where the coupling is small, and a physical scale where it is of order one.
- (F-b) The gap is of the form exp(-c/g^2) in the bare coupling. No argument at small effective coupling can see
  it. So every route holds one statement at an effective coupling of order one. This is the band. It is a property of
  the target, not of the Wilson action.
- (F-c) The comparison case, compact U(1) in four dimensions, has no gap at weak coupling (Guth; Froehlich and
  Spencer). So the statement of (F-b) must use the group, not only the general shape of the model.

### 1.2 The published record, by what each result can supply

| Result (credit) | Regime | Selective? | Uses the action how |
|---|---|---|---|
| Strong-coupling gap and area law (Osterwalder, Seiler) | small beta | no (any group) | any bounded plaquette weight |
| Coulomb phase of 4D U(1) (Guth; Froehlich, Spencer) | weak | the comparison case | Villain or Wilson |
| 3D U(1) gap at every coupling (Goepfert, Mack) | all | abelian only | **Villain weight is essential** (exact duality) |
| d-dimensional gauge loop below (d-1)-dimensional chiral model (Durhuus, Froehlich) | all | yes in 3D with a 2D O(4) gap | Wilson form; in 4D it lands on the ordered 3D O(4) model |
| Vortex conditions (Mack, Petkova; Tomboulis, Yaffe) | all | reductions, not suppliers | positive type |
| Decimation bounds (Tomboulis; critique by Ito, Seiler) | all | no: group-blind | positive type; gap at one step |
| Bakry-Emery for the Langevin dynamics (Shen, Zhu, Zhu) | small beta | no | convexity range |
| Gap and centre symmetry give the area law (Chatterjee) | any | wrong direction | none |
| Ultraviolet stability (Balaban; Dimock; Sussman, Alpoge) | weak | yes, by one loop | **Wilson, as written** |
| Small-volume spectrum (Luescher; van Baal) | size much below 1/Lambda | yes | continuum |
| 2D O(N), N >= 3, decay at every beta (OpenAI release; Ding, Huang, Yang) | all | **yes** | spin model, not gauge |

Reading of the table (SKETCHED). Only three results reach every coupling with a continuous group: Goepfert-Mack,
Durhuus-Froehlich and the 2D O(N) proofs. The first needs the Villain weight, and it is abelian. This is the one
published precedent where the choice of action decided a proof. Its mechanism is an exact positive dual
representation. For SU(2) the dual weights carry signs that come from the group integrals, not from the plaquette
coefficients (ON FILE: the negative projective-plane term, `library/gap-means-max.md` L78, row 737). So the
precedent does not transfer by a change of plaquette weight. The second is lossy by one dimension. The third is the
only selective mechanism at order-one coupling, and it is not a gauge result.

### 1.3 Judgement by level

**The action.** Within reflection-positive single-plaquette weights on SU(2) links, a change of action cannot be
the source of the mechanism. Reason (PROVED as logic; the list of shared properties is by inspection): every property of a central
positive-type weight that the heat-kernel weight on SU(2) shares with the Villain weight on U(1) (positivity of all
character coefficients, the convolution semigroup, coefficients exp(-t C_j) quadratic in the dual variable, a
transfer operator exp(-V/2) exp(t Delta) exp(-V/2) with continuous time, analyticity) holds in a massless model. A
proof that reads the weight only through such properties, and the group only through group-blind steps, proves
nothing. So the selective input must be a statement about products and integrals in the group. That input is the
same for every weight.

The one property of the SU(2) heat kernel that U(1) lacks is the positive Ricci curvature of the group. It gives a
gain of order g^2 per step in lattice units. A mass of order g^2 over the spacing is excluded by perturbation theory
(no mass at any order, by gauge invariance), so other terms of the same order cancel it (GUESSED from that argument;
ON FILE as a measured fact: the horizontal Hessian exceeds the Ricci bound above beta about 0.25, rows 957, 968).

What a change of action can do is remove technical obstructions for a mechanism that exists already. The honest
list (SKETCHED):

1. Heat-kernel time-like plaquettes give an exact continuous-time transfer operator. This removes Lemma JF of row
   1356 (discrete Wilson time) and makes Proposition TR of that row apply as stated. The supplier (REG-vac) stays.
2. A heat-kernel weight has exact heat factors by definition. The Wilson weight has none: its coefficients
   I_{2j+1}(beta)/I_1(beta) fall only factorially, and exp(-t j(j+1)) falls faster, so Wilson = heat * measure
   would need unbounded Fourier coefficients of the measure (PROVED, two lines; row 1442 says row 1434 has this).
3. In two dimensions the heat-kernel weight is an exact fixed point of decimation (Migdal). In four dimensions a
   link lies in six plaquettes and no single-plaquette family is closed under any block map (SKETCHED).

The cost is on the other side. The existence chain is written for Wilson: the account's 1,647 statements, and
Balaban's papers. A change of the ultraviolet action reopens the port. A change only at the physical scale is not a
change of action at all: there the theory is the block-effective action, whatever the bare weight was.

**The blocking map.** The block-effective theory at the physical scale is fixed by the bare theory and the map.
A map that commutes with the reflections keeps reflection positivity for the marginal law. No published map is
controlled at order-one coupling for a non-abelian group, and none is exact in four dimensions. The map decides
what can be computed. It does not decide whether a gap exists. So the map is a tool level, not a wall level
(SKETCHED).

**The reduction (M-neutral).** It is a correct consumer and, by the lane's own rule, equivalent to the problem at
one scale (gap and count on a box of more than 17 correlation lengths, uniformly in the cutoff). A seed can never
sit in a calculable regime: asymptotic freedom makes every calculable box small against the correlation length
(ON FILE: the rate filter, `library/gap-seed-limit.md` Section 5). So the reduction puts the whole problem in one
statement at strong effective coupling. That is acceptable for a consumer. It gives no hold for an attack. A
weaker first milestone exists and is not equivalent to the seed: (G-latt) a gap of Wilson SU(2) at each fixed
beta, with no rate. It is the exact analogue of the 2D O(N) theorems, it needs no ultraviolet carry, and it is a
classical open problem. It needs the same mechanism.

**The overall route.** By (F-a) and (F-b) the outline is forced: ultraviolet control by a weak-coupling
renormalisation group, and one selective statement at order-one coupling. What is free is the type of supplier of
that statement. I see three types (SKETCHED):

- (S-mech) an inductive, selective inequality across scales (the type of the 2D O(N) proofs);
- (S-comp) a verified finite computation with two carries (Theorem T of row 1332). Its infrared carry is of type
  (S-mech) again (a monotonicity in the coupling with a rate), so it does not escape;
- (S-exact) an exact positive representation in which disorder is visible (the type of Goepfert-Mack). For SU(2)
  none is known, for any weight.

### 1.4 What I would choose, before reading the passes

1. Keep Wilson as the ultraviolet action. The wall is not there, and the existence chain is.
2. Keep the checked chain from (M-neutral) as the consumer. Do not re-choose the reduction.
3. Treat the heat-kernel weight as a licensed auxiliary, not a new start: use it where a step needs continuous
   time or an exact heat factor, and pay for it by a comparison at one scale. Check in Phase 2 whether the lane
   already did this.
4. The level to choose afresh is the supplier type. On the record of 1.2 the only live type is (S-mech), and its
   only published instance is the 2D O(N) pair. If Phase 2 shows that the band passes after row 1380 ran the
   (S-mech) search to exhaustion against the selectivity filter, the correct decision is a stop on the band, not a
   new action.
5. One item to test in Phase 2, because it is cheap and uses only published inputs: Durhuus-Froehlich with the new
   2D O(4) decay gives the area law for three-dimensional SU(2) lattice Yang-Mills at every coupling, if the
   hypotheses match. This is selective (it fails for U(1), where the 2D XY model has a massless phase). It is not the
   target. It would be the first all-coupling selective gauge statement, and the question is whether the lane has it.

Questions that Phase 2 must answer: (Q-a) which obstruction of rows 1434, 1438, 1439 falls with the heat-kernel
weight; (Q-b) what the lane did with heat-kernel, Villain, mixed and constrained actions and with other block maps;
(Q-c) whether item 5 is on file.

## 2. Phase 2: the passes, read against the action and the block map

Read for this section: the RESULT lines of rows 1379-1381, 1386, 1387, 1390, 1393, 1396, 1401, 1402, 1407, 1409,
1411, 1434, 1436, 1438-1441 in full; the heads of rows 1330, 1340, 1383, 1418, 1431; parts of the files of rows
1434, 1436, 1438, 1439. I did not re-derive their proofs. Each "depends on" entry below is my reading of the stated
proof, labelled.

### 2.1 Phase 1 against the file

| Phase 1 item | Where it already sits | Verdict there |
|---|---|---|
| Supplier types (S-mech), (S-comp) | K-I, K-II, K-III of `library/gap-mech-direction2-fable.md` 4.4 (row 1386) | none found |
| Heat-kernel weight as an auxiliary | idea 17 of `library/gap-brainstorm2-max.md` L164, L222, L306; b1 of `library/gap-crux-exercise2-max.md` L260; A1 of `library/gap-crux-exercise-r858-max.md` L243; 1g of `library/gap-wall-assume-max.md` L55 | "nothing at order one"; "adds exact structure, not known to remove (S-ir)"; "COSMETIC" |
| The engine does not need Wilson | A1 of `library/gap-crux-exercise-r858-max.md` L243 (I6: any reflection-positive, axis-symmetric weight) | on file |
| Wilson has no exact heat factor | row 1434 (3), check 1436 | PROVED there, checked |
| Durhuus-Froehlich with the 2D O(4) theorems (item 5) | method 36 of `parts/gap.md` L70; rows 1139, 1140; `library/gap-mini-solve-h-fable.md` L54 | **dead in the uniform form**: the comparison needs decay uniform over backgrounds, and a period-four background orders the layer at large b |
| Positive dual for a heat-kernel weight | `library/gap-mini-solve-x-opus.md` L56; rows 737, 744, 878 | signs from crosscaps and 6j symbols |

So Phase 1 produced nothing that is new to the file. Its item 5 is withdrawn. Its item 3 is on file as cosmetic.

### 2.2 The obstructions of the nine passes, by what they depend on

W = depends on the Wilson weight. S = depends on straight-product (or slice) blocking. A = holds for every
reflection-positive single-plaquette weight with the same proof idea. The last column is my reading (SKETCHED unless
marked).

| Row (check) | Obstruction | Depends on |
|---|---|---|
| 1380 (1381) | Theorem C1: lab-frame link-end moves have a site-local cost in every bound of OpenAI's form (2.2); corner graph K_(2,2,2,2) | A: the cost form is a quadratic form of any smooth weight; the constants (72/7) K + (3/2) B change |
| 1386 (1387) | Proposition NEG: every proved band statement on file is lattice-local, an identity or a negative, and holds in five dimensions. Lemma GRP: the borderline logarithm sits at D = 2N/(N-1) | A: NEG is logic over the file; GRP is a continuum toron integral, no lattice weight in it |
| 1390 (1393) | Lemma CW (degree d - 4 of the classical weight); REF and MKO (bond moving, log-majorization); NOSIGN | A: REF needs only positive type. CW is classical. Check 1393 found the closure of the grid class FAILS |
| 1396 (1401) | Inequality (1) undecided; USE (no transport, no rate, no entry); Lemma KER (the Wilson kernel difference changes sign near beta 4) | **W for Lemma KER** (a Bessel fact). USE is A. With a heat-kernel time weight, time coarsening is exact (semigroup), and the trace comparison is Araki-Lieb-Thirring; NOSIGN still applies to the quotient |
| 1402 (1407) | COVER is a rewriting of the seed; TORNEG | A |
| 1409 (1411) | Lott's weighted-fibre transport fails on a regular fibre by (4 beta/N) sin(t/2); second obstruction beta above N^2/(4(d-1)) | **W in the number, S in the map** (two-link product). For Villain U(1) the hypothesis holds class by class (Gaussian fibres are translates) and gives nothing, as the O'Neill term is zero. Other maps "need a separate test" (row 1409's own words) |
| 1434 (1436) | No exact independent heat factor on a straight-product coarse link: factorial lower bound on all-spin loops | **W, by check 1436's own argument**; S only in the statement. See Proposition VIL below: with the Villain weight the factor exists and gives nothing |
| 1438 (1440) | (11)-(12): any invertible slice channel leaves the neutral spectrum unchanged. (5)-(6): the residual is not site reflection positive through a kept slice | A (row 1438 L176: "works for any time-ho[mogeneous]" law); S in the sense of slice-wise observation |
| 1439 (1441) | Independent thinned commutator factors exist only for p up to about e^(-12 beta); they fix no coupling sign (9) | A in kind: Lemma 2 holds for "any central probability N" and reads the weight through its log oscillation on one link (12 beta for Wilson; six times log(K(1)/K(-1)) for a heat kernel). The number is W |
| 1418-1437 | signed finite facts on bare Wilson blocks; check 1431: the sign depends on the reference | W in the numbers (Bessel coefficients); A in the conclusion of check 1431 |

Count. Of the nine passes, three have an obstruction that a heat-kernel weight removes or changes in kind (1396
Lemma KER, 1409's number, 1434). None of the three removals gives a gain: 1396's USE holds for every weight; 1409's
hypothesis is then met by U(1) with zero curvature term; 1434 is Proposition VIL. The other six do not see the weight.
Straight-product blocking enters 1409, 1434 and 1439 as the chosen map. No pass tested Balaban's averaging map at a
coupling of order one, and no pass could: no one has an estimate for it there (K-II of row 1386).

### 2.3 Proposition VIL: the heat-factor class is realised exactly by a massless model

This answers question (Q-a) for row 1434, and it is the one statement of this row that I did not find on file
(grep of `library/open-core.md`, of the four candidate files, and of the FINISH rows for "Villain" with "heat factor"
or "heat kernel": no match but this row).

**Setting.** A finite periodic lattice (Z/N)^d with link set E and plaquette set P. Cochains over R, d from 1-forms to
2-forms, K = ker d. The Villain law at coupling beta > 0 has the density, with respect to Haar measure on the
torus T^E = (R/2 pi Z)^E,

  f(theta) = sum over n in Z^P of exp( -(beta/2) || d theta - 2 pi n ||^2 ),

computed on any lift of theta (a change of lift by 2 pi m shifts n by dm). Let k_s be the wrapped Gaussian of
variance s on the circle. It is the heat kernel of U(1) at time s.

**Proposition VIL (PROVED by hand here, unchecked).** Let 0 < tau <= 1/(4 d beta). Then

(a) f/Z = (product over links of k_tau) * nu, with nu a probability measure on T^E. In words: a Villain field is
    theta' + xi, with theta' of law nu and xi independent of theta', independent over links, each of law k_tau.
(b) For every block size b >= 1 that divides N, the straight sums Theta_e = sum of theta over the b fine links of the coarse edge e
    have the law (product over coarse edges of k_(b tau)) * nu_b, with nu_b the law of the straight sums of theta'.
    So the pushed-forward law has an exact independent heat factor of time b tau on every coarse link, with a
    positive residual, at every coupling, every block size and every dimension.
(c) If a law on G^E, G a compact group, has independent central heat factors of time tau on all links with a
    positive residual, then its straight products of b links have independent central heat factors of time b tau.
(d) In d = 4 at large beta the Villain model is in a massless phase (Froehlich and Spencer, CMP 83, 1982; Guth
    for the perimeter law; both `unchecked`, recalled; lane anchor `library/prior/gap-lit-vmf-tor.md` L52). So the first lemma of row 1434's candidate, in the strongest
    form (every link, every scale, a time that does not shrink), does not imply a gap, and implies nothing that
    separates a massive from a massless model.

Proof. (a) Fix n. Write 2 pi n = d y_n + r_n with r_n orthogonal to the image of d and y_n in the orthogonal
complement of K. Then ||dx - 2 pi n||^2 = ||d(x - y_n)||^2 + ||r_n||^2 for x in R^E. So
g_n(x) := exp(-(beta/2)||dx - 2 pi n||^2) is constant along K and, on the complement, is a constant times the
density of the Gaussian N(y_n, (beta A)^(-1)), A the restriction of d*d to the complement. A is positive definite,
and A <= 4d: d*d and dd* commute, their product is zero, and their sum is the lattice Laplacian on 1-forms, whose
symbol sum_mu (2 - 2 cos k_mu) is at most 4d. So (beta A)^(-1) - tau is non-negative, and
N(y_n, (beta A)^(-1)) = N(0, tau) * N(y_n, (beta A)^(-1) - tau) on the complement (the second factor may be
degenerate; it is a positive measure). Along K a constant is the convolution of a Gaussian with a constant. So
g_n = G_tau * h_n, with G_tau the density of N(0, tau Id) on R^E and h_n a positive measure. The sum F = sum_n g_n
converges and is 2 pi Z^E-periodic, so H = sum_n h_n is a positive, locally finite, periodic measure with
F = G_tau * H. For a periodic measure H, (G * H)(x) is the torus convolution of the wrapped G with H on one period.
The wrapped G_tau is the product of the k_tau. Divide by Z. (b) The coarse edges use disjoint fine links, so the
sums of xi over them are independent, each of law k_(b tau), and independent of theta'. (c) Write the links of one
coarse edge as U'_1 xi_1, ..., U'_b xi_b. Then the product is U'_1 ... U'_b times the product of the conjugates of
the xi_i by later U'. A central law is invariant under conjugation, so given U' the conjugates are independent
with the same laws, and their product has the heat law of time b tau, independent of U'. Distinct coarse edges use
disjoint links. (d) is the citation. QED

Remarks. (i) The bound 1/(4 d beta) is 1/(16 beta) in four dimensions. It is the inverse of the largest precision
of the Gaussian, so it is sharp for this proof. (ii) Whether the SU(2) heat-kernel plaquette law has such a factor
on its fine links is OPEN, and by (d) it does not matter for the band. (iii) What the consumer of a heat factor
needs, and U(1) lacks, is a statement on the residual: that it is again a law of the same kind at a weaker coupling.
For Villain U(1) the residual is a mixture of Gaussians with covariance (beta A)^(-1) - tau, long-ranged. So the open
content of row 1434's candidate was never the factor. It was the carry, K-I of row 1386. (iv) The same reading
applies to row 1439: Lemma 2 there gives thinned factors for any central noise at every coupling, and (9) shows
that they fix no sign.

**Answer to (Q-a).** The heat-kernel weight removes the obstruction of row 1434 (ARGUED by check 1436; for U(1)
PROVED by VIL (a), (b)) and removes nothing else that matters. The class it reopens is realised by a massless
model. The obstructions of rows 1438 and 1439 do not depend on the weight.

### 2.4 Inventory: what the lane already did with other actions and other block maps

Other actions (file counts by `grep -l -i -F` over `library/gap-*.md` and `library/prior/gap-*.md`: Villain 183,
Kogut 41, adjoint action 37, positive plaquette 32, Bhanot 29, Manton 11, heat-kernel action 9):

| Action or weight | Where | What was done | Verdict on file |
|---|---|---|---|
| Heat kernel on SU(2) | `library/gap-brainstorm2-max.md` L164, L222, L306 (row 876, idea 17) | semigroup fusion needs a link in two active plaquettes; in 4D it lies in six | "nothing at order one" |
| Heat kernel, Manton, mixed | `library/gap-crux-exercise-r858-max.md` L243 (A1) | the engine keeps any reflection-positive axis-symmetric weight; the account must be re-run | free for the engine, not for the account |
| Heat kernel; weight with no Z_2 monopoles; mixed | `library/gap-crux-exercise2-max.md` L260 (b1), L334 (R4) | exact structure listed; conditional Griffiths inequalities for the centre part | "neither is known to remove (S-ir)" |
| Villain, heat kernel, Manton | `library/gap-wall-assume-max.md` L55 (1g) | the flat layer stays an O(4) ferromagnet of positive type | COSMETIC |
| Heat kernel as plaquette Brownian motions under Bianchi | `library/gap-mini-solve-c-fable.md` L133 (15) | Identity MIX, Remark POL of row 996 | no consumer |
| Positive dual for a heat-kernel weight | `library/gap-mini-solve-x-opus.md` L56 | crosscap and Frobenius-Schur signs | signs |
| Heat kernel against row 1434 | `library/gap-mech-candidate-check-opus.md` L147-151 (check 1436) | the factorial tail is a property of the bare Wilson weight | ARGUED; no proof row |
| Mixed fundamental-adjoint (K7) | rows 708, 995, 996; `library/gap-mid-max.md` L48; Identity MIX | Wilson with annealed Gaussian plaquette couplings; the end point as a kill test | a test, not a route |
| May the lane choose its weight? (UNIV-FP) | row 904, `library/gap-univfp-opus.md` L207 | read the account's universality proposition (YM4_1400 L94368-94386) | **does not follow**: fixed ball of small-field profiles, one frozen endpoint, normalized laws on one volume, no large-field histories, no vacuum factors |
| Villain U(1), Gaussian Model G | rows 930, 1388 Proposition B, `library/prior/gap-lit-vmf-tor.md` L52 | the comparison case of the filter | used as a test |
| Continuous time (Kogut-Susskind) | row 1356 Proposition TR, Lemma JF; I14 of `library/gap-outside-box-max.md` L153; Identity HAM1 of row 1016 | the transport comparison holds with continuous time; the Wilson operator gives the gap only | supplier (REG-vac) missing in both |
| Fundamental or adjoint Higgs | I10, I11 of `library/gap-outside-box-max.md` L146-147 | seed in the Higgs regime; Lemma GG | no carry to kappa = 0 |
| Refined family above a strong-coupling base | V4 of `library/gap-wall-vectors-max.md` L146; Proposition PF of row 1332 | exactly consistent fine measures | only the base lattice's translations |
| A warning | `library/gap-means-astra.md` L780 | "Do not replace fixed SU(2) by ... a heat-kernel action ... without an exact comparison" | rule |

Other block maps (file counts: decimation 76, Migdal-Kadanoff 43, majority 22, bond moving 19, gradient flow 16,
smearing 16, Balaban averaging 2):

| Block map | Where | Verdict on file |
|---|---|---|
| Migdal-Kadanoff decimation with interpolation (Tomboulis) | rows 1025, 1029; `library/gap-cr-tomboulis-max.md` | group-blind; (TB)_n has no sign |
| Hierarchical flow | `parts/gap.md` L237, L257 (rows 859, 876, 878) | group-blind; retired |
| One-direction bond moving, grid changes | row 1390 REF, MKO, NOSIGN; check 1393 | no sign on the top quotient |
| Geometric time coarsening | rows 1396, 1401 | no transport, no rate, no entry |
| Straight-path decimation, two-link product | rows 1383 (LIFT, THIN, U1), 1409 (Lott), 1434, 1439 | rough in U(1) and 5D too; transport fails; no heat factor; no sign |
| Slice channels (kept even slices) | row 1438 | spectrum unchanged; residual not reflection positive |
| Soft pinned block step, Dobrushin block kernels | rows 861, 1340 (Theorem TL, DC-B, BL, BS), 1341-1352 | reduces to a one-block statement of seed strength |
| Site-tensor fusion, computer-assisted | rows 1418-1437 | rank and error rule out the carry; signs depend on the reference |
| Gradient flow, smearing | rows 720, 1002, 1005 ((K-flow)) | a renamed coupling |
| Balaban's averaging map | the existence chain only | no estimate at order-one coupling (K-II) |

**Answer to (Q-b).** Every other action that I named in Phase 1 was considered on file, each time at the level of a
table entry, and each time with the same verdict: exact structure, no gain at order-one coupling. One row tested
the freedom itself (row 904) and found that the account does not give it. No other action was ever carried into a
proof row, and I find no reason on file or in Phase 1 to do so now. The block maps on file cover every map with an
exact formula. The one map with estimates, Balaban's, has them only at small coupling.

## 3. Does the chain from (M-neutral) to the gap, and the seed, survive a change of action?

Take a new single-plaquette weight w on SU(2): a continuous, strictly positive class function with w(U) = w(U^-1)
and non-negative character coefficients, the same on all plaquettes. Example: the heat kernel.

| Link of the chain | Reads the weight through | Survives? | To re-prove |
|---|---|---|---|
| Transfer operator (TM), (TM-c): `library/gap-crux-restate.md` Section 1; `library/gap-transfer.md` (rows 667, 671) | positivity of the kernel (non-negative coefficients), strict positivity (simple top eigenvalue), centre symmetry of a class function | yes (ARGUED on file: A1/I6 of row 858, b1 of row 878; not written out) | `gap-transfer.md` for w: N.1-N.7, (8b), trace class. Routine |
| Lemma A, Theorem S, Corollaries (the engine), row 697 | (TM), (TM-c), the symmetry of Z under axis exchange | yes, word for word | nothing but the inputs |
| Theorem L3, Propositions P, P' (`library/gap-seed-limit.md`) | Lemma FE (a bound exp(12 beta Gamma) on density ratios), (TR), hypercubic symmetry | yes with the constant exp(6 Gamma osc(log w)); fails for a weight with hard constraints | Lemma FE's constant |
| Neutral sector: rows 1161, 1179, 1342, 1349 (Pfaffian seed, branch, Theorem O, Proposition C) | centre flips, twisted tori, and in places Wilson numbers (row 1161 (19): a count of low neutral levels) | the structure yes; each numeric statement no | every display with a number in beta: SKETCHED, I did not audit them line by line |
| Rank-one test: rows 1353, 1356 (M1, M2), checks 1355, 1359 | nothing (operator facts) | yes | nothing |
| Continuum datum: (P1)-(P4), (H2), (TOT) | the existence chain for the same family of lattice laws | **no** | the whole account for w, or a theorem that the continuum state is the same. Row 904: the account's universality does not give it |
| The seed (M-neutral) itself | everything | it becomes the same statement for w's trajectory | all of it. By 2.2 and VIL no step gets easier in kind |

So (PROVED as bookkeeping from the cited rows; the numeric audit of the neutral rows is SKETCHED): the engine and
the rank-one test survive any such weight unchanged. The limit-state theorems survive with new constants. The
continuum inputs do not survive: they cost the existence chain again, or a bridge theorem that nobody has (a
full-measure comparison of two bare weights that differ on large fields, on several tori, uniform in the cutoff;
row 904's "missing"). The seed survives as an open statement of the same strength.

One more point decides the question. At the physical scale the law is the block-effective law of the bare family.
The bare weight enters it only through irrelevant terms, which the ultraviolet carry (A1) = (UNIV-K) must bound in
any case. So if (A1) held in rate form, two bare weights would give the same window problem. If (A1) does not
hold, the lane cannot use any bare weight. In both cases the choice of bare weight does not change the band.
(ARGUED; this is the physical content of universality, and rows 1391-1422 show that (A1) is open in the account's
own terms: check 1422 FAILS for the complete native pair.)

## 4. Decision

### 4.1 The owner's two questions, answered

**"Maybe NOT use Wilson?" No.** Four reasons, each with its evidence.

1. The band is a property of the target ((F-a), (F-b) of 1.1). Every reflection-positive action with the
   Yang-Mills scaling limit has it. SKETCHED, standard.
2. The mechanism must separate SU(2) from U(1). A single-plaquette weight cannot do that: each exact property of
   the SU(2) heat kernel that could serve is shared by the Villain weight, and the Villain model is massless at weak
   coupling in four dimensions. Proposition VIL makes this exact for the one class where a pass was stopped by the
   Wilson weight (row 1434): there the Villain model has the wanted factor on every link, at every scale. PROVED
   here, unchecked.
3. Six of the nine passes do not read the weight. The three that do (1396, 1409, 1434) lose an obstruction under a
   heat-kernel weight and gain nothing (2.2). SKETCHED from the rows' stated proofs.
4. The cost is the existence chain. The account is written for Wilson, and its own universality proposition does
   not let the lane change the weight (row 904). The engine would survive; the continuum inputs (P1)-(P4), (H2),
   (TOT) would not (Section 3). On file.

The lane had this option on file five times since row 876 and marked it cosmetic each time (2.4). That verdict
stands, now with a proof for the heat-factor class.

**"Do we need to go further back up the attack?" The levels above the seed are sound, and none of them is the
wall.** The chain from (M-neutral) to the gap is a correct consumer and survives. The block map is a tool. The
action is cosmetic. What is missing is one kind of input, the same in every pass since row 1380: an exact carry with
a sign for a typical-field quantity (K-I), or a renormalization step at an effective coupling of order one (K-II).
That input is not a level of this lane's design. It is the open problem. No published work supplies it for a gauge
model, and the two published instances in spin models (OpenAI; Ding, Huang and Yang) were ported and stop at a
named step (rows 1009-1018, 1197, 1380).

### 4.2 Stop on the band

**Decision: stop attack and direction rows on the band.** Reason: the search has converged. Four blind first
phases (rows 1402, 1434, 1438, 1439) and this one produced only items that were on file or that closed a class
with no selectivity. Three direction rows before this one (1386, 1390, 1402) reached the same recommendation.
The two estimates that check 1407 kept open do not change it: the relative winding comparison of row 1131 is
algebraically the defect bound (it fails (t5), `library/gap-band-fresh-check-astra62.md` L107), and (GC) of row 1197 is an argument with no
neutral consumer. The typical-field shell estimate of row 1388 has no consumer (check 1389).

This row adds the one direction that the earlier stops had not closed: the level of the action.

What a stop does not say. It does not say that (M-neutral) is false or that the route is wrong. Nothing in the
chain was disproved by any pass. It says that the lane has no first lemma to attack.

**Reopen on any one of these (triggers).**

- (R1) A published proof, for a non-abelian gauge model in three or four dimensions, of any inequality at
  order-one coupling that fails for compact U(1). The OpenAI Yang-Mills write-up is the first place to look when it
  appears.
- (R2) A candidate that passes (t1) to (t5) of `library/gap-mech-direction2-fable.md` 4.5 and states its carry, not
  only its gain (Remark PAIR). After VIL, add one test: **(t6) the Villain test.** If the first lemma is an exact
  identity of the law (a factor, a mixture, a dual form), check it in Villain U(1) in four dimensions before any
  proof row. If it holds there, the lemma is not the mechanism, whatever the Wilson weight does to it.
- (R3) (A1) proved in rate form. Then a verified computation at the window (K-III) has a statement to prove. It
  still needs (A2).

### 4.3 Bookkeeping that the stop exposes (for the lead; I edit no other file)

`library/open-registry.md`, `library/t0-tree.md` and `library/open-core.md` have no line for (M-neutral) or
(N-phys) (grep at this pin: no match). Rule 0f asks for one. One registry row would hold the gap clause's state:
"(M-neutral), row 1367; consumer chain rows 1342, 1349, 1356, 1359; extra inputs (P1)-(P4), (H2), (TOT); band
stopped at row 1442 with triggers (R1)-(R3)". Then a later lane starts from that row and not from a new blind pass.

## 5. The next two rows

**Row 1, `gap-mech-direction3-check-astra62` (cross-provider check of this file).** Order: Proposition VIL (a)
to (d) line by line, with the bound A <= 4d, the periodic convolution step and the conjugation step of (c); then
the table of 2.2, entry by entry against the rows' proofs, first the three W entries and the two SKETCHED claims
(Villain fibres under Lott's hypothesis; Araki-Lieb-Thirring for a heat-kernel time weight); then the table of
Section 3, with the numeric displays of rows 1161 and 1179 that I did not audit. Decisive outcome: if VIL holds and
no W entry hides a gain that passes (t1), the question of the action is closed on the record and the band stop
stands with test (t6). If an entry FAILS in the direction of a gain, that entry is the next proof row.

**Row 2, off the band: the two-cutoff comparison (A1), at the proof row that check 1422 named** ("the one-family
change of read for the ordinary stored strip at a common datum"). It is the account's own outstanding statement
(`library/open-registry.md` L60, CA-III 37667, "Proof outstanding"), so it is proof work of the kind `GOAL.md`
allows. It is also what decides, in the other direction, whether any bare weight can be used at all (Section 3,
last paragraph), and it is trigger (R3). Decisive outcome: the per-cell bound of check 1422 proved, or a native
violation found. I have not read that part of the account in this row; the lead should confirm with
`library/port-map.md` that the statement sits on the T0 chain before queuing it. If it does not, the capacity goes
to the first open hard-core obligation of the T0 chain instead, and that is the lead's choice, not mine.

A standing item, not a row: a weekly literature scan for (R1) by the bulk reader, as row 1379 did.

## 6. Summary of labels

- PROVED here by hand, unchecked: Proposition VIL (a), (b), (c); (d) given the cited massless phase. The two-line
  remark that the Wilson weight has no heat factor is row 1434 (3), checked by row 1436, not mine.
- SKETCHED: (F-a) to (F-c); the dependence table 2.2; the numeric audit column of Section 3; the two claims on
  Villain fibres and on Araki-Lieb-Thirring.
- ARGUED: that the ultraviolet carry (A1) makes the bare weight irrelevant to the window problem.
- GUESSED: that the Ricci gain of the SU(2) heat kernel is cancelled at one loop (the measured fact is on file).
- ON FILE, not new: every Phase 1 item (table 2.1), the inventory 2.4, the stop recommendation (rows 1386, 1390,
  1402).
- Not done: no proof of the rows read was re-derived; the neutral rows 1161 and 1179 were not audited for Wilson
  numbers; the account was not opened; no literature was fetched (all literature statements are recalled).

RESULT: Row 1442 (Claude Fable 5.2 high, Mac mini worker 1; author only, checked by no one; no numeric run). Direction review with a negative verdict and a stop. (1) Level: neither the lattice action, nor the blocking map, nor the reduction (M-neutral), nor the outline of the route is the wall; the band is a property of the target, and the missing piece is one input kind, K-I or K-II of row 1386. Keep Wilson. (2) Of the nine passes, six obstructions do not read the weight; three (1396 Lemma KER, 1409's number, 1434) are Wilson-specific and their removal gives no gain. PROVED here, unchecked: Proposition VIL (for Villain U(1), every coupling, dimension and block size, the law is independent heat noise of time up to 1/(4 d beta) on every link convolved with a positive residual, the same holds for straight-product coarse links with time b tau, and the model is massless at weak coupling in d = 4; so the heat-factor class of row 1434 is realised exactly by a massless model and is not a mechanism under any weight). Inventory: other weights were tabled five times as cosmetic and never reached a proof row; row 904 shows the account does not let the lane change its weight. (3) Under a change of weight the engine and the rank-one test survive unchanged, the limit-state theorems survive with new constants, the continuum inputs (P1)-(P4), (H2), (TOT) do not (the existence chain or a missing bridge theorem), and the seed stays an open statement of the same strength. (4) Decision: stop attack and direction rows on the band, with reopen triggers (R1)-(R3) and a new filter test (t6), the Villain test. Next rows: a cross-provider check of this file (VIL first), and off the band the two-cutoff comparison (A1) at the proof row named by check 1422, if the lead confirms it is on the T0 chain. OPEN: (M-neutral), (A1), (A2), a carry with a sign at order-one coupling, the mass gap.
