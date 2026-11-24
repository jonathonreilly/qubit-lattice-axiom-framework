lead: anthropic/claude-fable-5-2/high mac-mini-worker
lease_until: 2026-11-25T02:57Z

# Row 1474: the missing tool T2, a representation for an order-one block step

Worker file of queue row 1474 (`gap-k2-t2-representation-fable`), pinned at commit a3c24b36f on
`claude/ym4d-hard-route`. Started 2026-11-24T14:57Z (date -u). Research-stage working state; nothing here is a
public claim. Every statement is marked proved, sketched or guessed. Nothing is committed or pushed from this
machine.

## 0. Plan (written first, per the save protocol)

1. Read the record the row names: rows 1460, 1461, 1466, 1468, 1470, 1471 and their checks;
   `library/gap-k2-tool-design-fable.md` sections 4-6, `library/gap-k2-floor-sizing-opus.md`,
   `library/gap-k2-end-class-fable.md`. Record which representations are already closed and why (cost or closure).
2. State T2 as a precise problem: a class C of local rules, a map S (the Q2 step or another exact self-similar
   map), with (a) S(C) inside C at order-one coupling, (b) the inclusion a finite check of bounded size,
   (c) selectivity under the filter t1-t6 (rows 1386, 1442).
3. Attack: candidate representations not on the closed list; for each, size of one step's check at beta about 2.3.
4. If no candidate survives for a stated class, prove the obstruction for that class.
5. End with the next two rows and their decisive outcomes, and one RESULT line.

Free memory at start: 37 percent (memory_pressure), below the 50 percent bar for a numeric job; no numeric job
is started unless that changes.


## 1. Step 1: the record, and T2 as an exact problem (written 2026-11-24T15:16Z, date -u)

### 1.1 What was read

Row 1474 in full. `gap-k2-tool-design-fable.md` (row 1468) Sections 2 to 11 in full. `gap-k2-floor-sizing-opus.md`
(row 1470) Steps 5 to 7. `gap-k2-end-class-fable.md` (row 1471): headings and the RESULT line. The filter (t1) to
(t5) in `gap-mech-direction2-fable.md` 4.2 to 4.5 (row 1386) and (t6) in the RESULT of row 1442. `gap-ds-gauge.md`
(row 691) Sections 0 to 3.3 in full (Theorem W and its proof). Proposition CA-FAIL with its precision
(`gap-bridge-exercise-opus.md` lines 337 and 368). The RESULT lines of rows 691, 735, 750, 770, 845, 1116, 1326. Rows 1460, 1461 and 1466 were read only through the uses that row 1468 makes of them (Theorem LOSS,
Lemma LD-1, Corollary LD-2); their files were not opened. That is a skipped step.

### 1.2 The closed list, by the means each one uses

Row 735 (`gap-form-exercise`, its findings F1 to F3) sorts every proved gap result by what makes its criterion checkable at one scale: (m1) a
small number at that scale; (m2) a second small number after an exact change of variables; (m3) exact closure;
(m4) a correlation inequality that gives a dichotomy. The representations closed for an order-one step:

| Representation | Means | Closed by | On file |
|---|---|---|---|
| Polymer expansion in plaquette activities | (m1) | closure: ceiling beta 0.0087 for the entry | row 1471 |
| One-link and block Dobrushin, complete analyticity | (m1) | closure: 2/9, 0.3609; false above 1.0109 in the uniform strong form | rows 1340, 1346, 1072 |
| Site tensors, exact contraction | none (in-law evaluation) | cost: rank 67, 13 PB a site; 2^(2 slice + 1) | rows 1418, 1326 (Lemma DIM) |
| Block enclosure, exact 2^4 cube map | (m3) for a map that is not self-similar | cost 6.5e14 gates for eight links; no closure | rows 1341, 1344, 1346 |
| Loop-equation or positivity certificate | none (linear in the density) | closure: patch as large as a seed box | row 1326 (Theorem O, Remark OS) |
| Character sums, heat factors on straight coarse links | (m3) attempted | closure: signed coefficients; no exact heat factor | rows 1425, 1434, 737 |
| Knabe or martingale criterion for the heat-bath generator | (m1) | closure in full L2 (gauge corner); every-boundary premise | row 750 (GC1 to GC4) |
| Cube criterion (W) of Dobrushin-Shlosman type | (m1) at the cube scale | not refuted; no method to verify it | rows 691, 1326 4.1 |
| Convexity (Bakry-Emery, Brascamp-Lieb) | (m1) | closure: hand range only | rows on Langevin gap (beta below 1/4), 34 files |
| Migdal-Kadanoff with interpolation (Tomboulis) | (m3) on a hierarchical lattice | not a proof on Z^4 (Ito and Seiler) | row 770 |

So the lane has no (m2), no (m3) on Z^4, and no (m4). Every (m1) entry is either below the hand range or is a
supremum over boundary values that nobody can evaluate.

### 1.3 T2 as an exact problem, and two remarks that fix what a solution can be

**Problem T2.** Find a set C of local rules (4.2 of row 1468) with readout near 2.3 and a statement S(Phi) such
that: (a) S(Phi) implies that the image of Phi under the next map is in the next class, or directly that every
family that realizes Phi has purity at least 457/625; (b) S(Phi*) for a computed centre Phi*, together with a
stability bound over a tube, is a finite computation of bounded size; (c) the filter (t1) to (t6).

**Remark SOUND (what (c) asks of a finite criterion). PROVED, one line.** If S implies the purity bound on
tori of all large sizes, then S is false for every model without a gap, so (t1), (t2), (t6) hold for S itself.
What the filter tests is the proof of (a): each of its lines must be valid for U(1), Villain U(1) and five
dimensions (then S fails there by a number), or must fail there at a named line. A criterion whose proof of
(a) is group-blind and dimension-blind, such as Theorem W of row 691, passes the filter as a criterion. It
then carries no mechanism: all the content is in the number that S asserts.

**Remark END (a step is not needed where an end criterion holds). ARGUED from rows 691 and 1471.** Row 1471
shows that a Q2 step of strength 0 maps into the end class exactly when the purity statement holds. So the
entry stretch moves no difficulty. A finite criterion of type (W) at readout 2.3 is an end class at order-one
coupling: Theorem W (C) gives a covariance bound on every torus with constants free of the torus, and (D')
gives the twisted actions. The step from that covariance bound to the purity of the sixteen masses is the
telescoping of one boundary link at a time; it is not written here and is OPEN as a written proof (see 4.3). So
T2 for the stretch from 2.3 to the end class is equivalent in strength to: a finite criterion for decay at
readout 2.3 that can be evaluated. This is the seed for a tube of rules. The row asks for a representation
that makes it finite at known cost; Sections 2 to 4 give one and size it.

### 1.4 What CA-FAIL does and does not exclude (re-read; this corrects a phrase of row 1468, not a theorem)

Row 1468 (C4) asks for "no unweighted supremum over all coarse fields" and cites CA-FAIL. CA-FAIL is proved
for volumes that are thin slabs with both faces pinned. It refutes complete analyticity and strong mixing over
all volumes. It does not refute (W) on cubes (row 1326 4.1 says the same: "the weak-mixing form (DS-W) of row
691 is not refuted"). What can make (W) false on cubes is surface order at a special boundary value: row 950
saw the colour direction order at a pinned pi-flux slice from beta about 2.45 up (GUIDE). With such a
boundary value the response to one changed boundary link has of order R^2 disagreeing links, and (W) allows
about R/8 per boundary link. So the state for cubes is: (W) may be true at 2.3 and is expected to fail a
little above; in both cases it is a supremum over a continuum of boundary values and no method evaluates it.
For a block step the coarse field is a field in the bulk, and there (C4) stands as argued in row 1468.

## 2. Step 2: six candidates tried in this row, each with the line where it stops (written 2026-11-24T15:25Z, date -u)

Each candidate is a representation with a possible check. For each: what holds, what is PROVED here, the
match on file, and the stop. None survives. Two small lemmas are proved on the way (FIB, NG).

### 2.1 Typical-field cube criterion (contraction only on good boundary values, bad ones paid by weights)

Idea. Keep Theorem W of row 691, ask the contraction only for good boundary values, and pay a bad boundary
link by a weight, as Dobrushin and Pechersky do for unbounded spins and Hairer and Mattingly do for Markov
chains (both recalled, not read here). The count that decides it: one bad boundary link may spoil all of the
cube, so the expected number of new bad links must be below one: (size of the cube) x (probability that a
resampled link is bad, uniformly in the boundary value) < 1.

Match on file: row 845, `gap-annealed-opus.md`. Theorem AG is the in-law (annealed) criterion along the
stationary block chain, Theorem LW (4.4 there) is the weighted form, and its stop is written there: bad
exteriors persist, a cycle of amplifying responses inside a bad region cannot be paid by any weight, and the
missing statement is the space-time bound (SP-ext). Row 1116 records that published rare-region criteria
(van den Berg; Gielis and Maes) are for quenched disorder, not for badness made by the field itself. So this
candidate is an attack equivalent to a closed one. I did not write a second form of it.

### 2.2 Local-gap (Knabe) form for the heat-bath generator

Idea. H = sum over links of (1 - E_l), E_l the conditional expectation given the other links, is a sum of
projections with the constants as its kernel. A local gap of the patch operators above a threshold that
tends to zero with the patch size gives a gap of H (Knabe; Gosset and Mozgunov; Lemm and Mozgunov; recalled).
A threshold that tends to zero would tolerate slow modes at a boundary. That is weaker than uniform mixing.

**Lemma FIB (the local gap is an infimum over exteriors). PROVED here, six lines.** Let mu have a continuous
positive density on G^L, Lambda a set of links, tau the configuration off Lambda, gamma_tau the conditional
law on Lambda, H_Lambda = sum over l in Lambda of (1 - E_l), and H^tau the same operator for gamma_tau. Let
g(tau) be the least value of <h, H^tau h> / Var_tau(h). Then the gap of H_Lambda above its kernel equals the
infimum of g(tau) over tau.

Proof. E_l acts fibre by fibre: (E_l f)(tau, .) = E_l^tau f(tau, .). A function with E_l f = f for every l in
Lambda does not depend on the links of Lambda. So the kernel is the set of functions of tau, and the distance
of f to it is the integral of Var_tau(f(tau, .)). For every f, <f, H_Lambda f> is the integral of
<f_tau, H^tau f_tau>, which is at least inf g times the integral of Var_tau(f_tau). For the other
direction take f = phi(tau) h with h continuous on G^Lambda. The quotient is the ratio of the integrals of
phi^2 <h, H^tau h> and phi^2 Var_tau(h). Both integrands are continuous in tau because the density is
continuous and positive. Let phi concentrate at tau_0. QED

The same holds, with the same proof, for every operator built from the E_S with S inside Lambda, for
example the pair norm of row 750. So the local-gap form is a worst-case criterion over exteriors. Its
advantage, the decaying threshold, is real: a boundary value with slow modes of gap c/n^2 need not break it.
It stops at (b): the quantity is the spectral gap of a Markov operator on SU(2)^n with n in the thousands,
uniformly in a continuum of exteriors, and no method evaluates it. Match on file: row 750 (GC1 to GC4; the
full-L2 form is refuted at weak coupling by the gauge corner, the gauge-invariant form PA_g is open with an
every-boundary premise). No new statement beyond Lemma FIB.

### 2.3 The noise map in field space (an exact map on the same lattice)

Definition. N_t D = e^(t Delta) D, Delta the sum of the Laplacians of the links (unit 3-sphere metric). It is a
Markov map. It commutes with the sign changes C_z. So it keeps each of the sixteen masses, and N_t D tends to
a constant as t grows. The rule Phi_t = - log N_t D solves d/dt Phi = Delta Phi - abs(grad Phi)^2.

**Lemma NG (gradient contraction with no small number). PROVED here.** On every finite torus and for every
link l: sup over fields of abs(grad_l Phi_t) <= e^(-2t) sup over fields of abs(grad_l Phi_0). For the Wilson
rule at coupling x the right side is at most 6 x e^(-2t). For U(1) the same proof gives the factor 1.

Proof. Put u = abs(grad_l Phi)^2. On a product manifold the Bochner formula for the factor l reads
(1/2) Delta u = abs(grad grad_l Phi)^2 + <grad_l Phi, grad_l Delta Phi> + Ric_l(grad_l Phi, grad_l Phi): for
the Laplacian of the factor l this is the usual formula with the other variables fixed, and for a factor
m other than l the derivatives commute with grad_l. Also <grad_l Phi, grad_l abs(grad Phi)^2> = <grad Phi,
grad u>, because grad_m u = 2 Hess Phi(grad_l Phi, .) in the factor m. So

    d/dt u = Delta u - 2 <grad Phi, grad u> - 2 abs(grad grad_l Phi)^2 - 2 Ric_l(grad_l Phi, grad_l Phi).

The unit 3-sphere has Ric = 2 g, so d/dt u <= Delta u - 2 <grad Phi, grad u> - 4 u. Phi_t is smooth for t > 0
and the manifold is compact. At a maximum point of u in the fields the first two terms are at most zero. So
the maximum of u decays at the rate 4. For the Wilson rule grad_l Phi_0 is x times the tangential part of
W_l S_l, S_l the sum of the six staples, of norm at most 6. On the circle Ric = 0. QED

Filter. The gain reads the group (Ricci curvature 2, zero for U(1) and for Villain U(1)) and not the
dimension. It is a local gain of the family of Proposition G1 of row 1128, in the language of Remark PAIR of
row 1386. It is not a mechanism: the lemma holds for SU(2) in five dimensions too.

Where it stops. (i) A small supremum of the one-link gradient is not an end class: Remark FI of row 1386 (a
mixture of two Wilson models with a global label has a small one-link score at every field and no seed).
(ii) What an end class needs is the mixed second derivatives. For a(t) = sup over fields of the row sum of
abs(grad_l grad_m Phi_t) the equation of the Hessian gives a Riccati inequality of the form a' <= 2 a^2 - 4 a
+ (terms in the one-link gradient). SKETCHED: I did not carry every curvature term. It closes only from
a(0) below about 2, and the Wilson rule has a(0) = 24 x at the worst field. So the bound holds for x below
about 1/12 and blows up at t about 1/(48 x) otherwise. This is the Bakry-Emery hand range. (iii) For large t
the constrained system of N_t is the measure itself, so the step moves no difficulty (Remark END). Relatives
on file: the soft pin step of rows 861 and 1340; Proposition VIL of row 1442 (heat noise is group-blind as a
factorization). Lemma NG itself was not found on file (grep for matrix Harnack, Li-Yau, Riccati, heat flow).

### 2.4 Convexity classes with exact closure (Brascamp-Lieb with curvature)

Idea. In flat space a log-concave joint weight has log-concave marginals, with the Schur complement as the
new lower bound. On a manifold the fibre block gets Ric added (the Bochner form of the Brascamp-Lieb
inequality; recalled). The class {Hess Phi + Ric >= Q} would then be closed under any marginal map, by a
finite computation in Fourier space, and it is empty for U(1), where Ric = 0.

Stop, PROVED in one line: for the Wilson rule the second derivative along one link is x Re(W_l S_l) times the
metric (the geodesic is W_l (cos t + X sin t), and the second derivative of Re(W_l e^(tX) S) at 0 is
- Re(W_l S)). At a field with the six plaquettes of l equal to -1 it is -6 x. So Hess Phi + Ric is positive
at every field only for x below 1/3, before any off-diagonal term. The class is the hand range again. On
file: the Langevin gap below 1/4 and 34 files that use Brascamp-Lieb.

### 2.5 Product defect of block tensors in L2 (no supremum, no boundary value)

Idea. Write the weight of a block, as a function of the links on its faces, as a product over the faces
times (1 + defect). Bound a contraction of block tensors by Hilbert-Schmidt or L^p norms (Cauchy-Schwarz on
a bipartite network; Finner's inequality when a variable is shared by more tensors; recalled). The check is
then a finite list of partition functions of closed doubled blocks. No supremum over fields occurs.

Stop. This is the rank-one test of rows 1353 to 1359 in the space directions. Its numbers are in-law
quantities of blocks of side several correlation lengths. The only exact evaluation on file costs at least
2^(2 slice + 1) (Lemma DIM of row 1326), and site tensors fail by rank (row 1418). A link on an edge or a
corner of a block is shared by more than two tensors, so the L^p norms needed are above 2 and grow with the
face. I did not prove a gluing theorem for it; it would be a new proof of a criterion that still cannot be
evaluated.

### 2.6 Migdal-Kadanoff as the exact map

It is exact and finite on a hierarchical lattice, and (a) and (b) hold there with a check of a few Bessel
ratios. It fails (t1): in four dimensions the recursion flows to strong coupling for U(1) at every coupling,
and compact U(1) is massless at weak coupling on Z^4. So every bridge from Z^4 to the hierarchical lattice
must fail for U(1) at a named line, and none on file does (row 770: Tomboulis's interpolation is not a proof).

