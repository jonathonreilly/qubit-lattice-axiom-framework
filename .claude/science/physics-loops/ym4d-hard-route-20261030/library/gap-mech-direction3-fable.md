lead: anthropic/claude-fable-5-2/high mac-mini-worker
lease_until: 2026-11-24T08:35Z

# gap-mech-direction3-fable (queue row 1442)

Started 2026-11-23T20:35Z (date -u), pinned at commit 27a186f3d, branch claude/ym4d-hard-route. Research-stage working state; nothing here is a public claim.

## 0. Status log

- 2026-11-23T20:35Z: file opened; reading FINISH.md rules, GOAL.md and row 1442.
- Plan: Phase 1 (Section 1, written before any row after 1378 is opened), Phase 2 (Sections 2-3: the passes, the
  inventory of other actions and block maps), Section 4 (does the chain survive a change of action), Section 5
  (decision and the next two rows). Labels: PROVED, SKETCHED, GUESSED, ON FILE (with the anchor).

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
coefficients (ON FILE: the negative projective-plane term, `library/gap-means-max.md` Section 2.4, row 737). So the
precedent does not transfer by a change of plaquette weight. The second is lossy by one dimension. The third is the
only selective mechanism at order-one coupling, and it is not a gauge result.

### 1.3 Judgement by level

**The action.** Within reflection-positive single-plaquette weights on SU(2) links, a change of action cannot be
the source of the mechanism. Reason (PROVED as a scoping statement, three lines): every property of a central
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
