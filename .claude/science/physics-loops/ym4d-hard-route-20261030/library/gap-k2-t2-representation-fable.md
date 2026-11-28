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
match on file, and the stop. None survives. One small lemma is new as far as my grep shows (NG); Lemma FIB is repeated from the file.

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
A threshold that tends to zero would tolerate slow modes at a boundary (ARGUED). That is weaker than uniform
mixing.

**Lemma FIB (the local gap is an infimum over exteriors). ON FILE: `gap-glue-max.md` lines 241-242 (operators
that commute with the exterior functions are decomposable; norms and spectra are fibre suprema) and
`gap-gc-check-opus.md` line 90. Repeated here in the form used, with an elementary proof.** Let mu have a continuous
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
every-boundary premise). No new statement: Lemma FIB is on file too.

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

The unit 3-sphere has Ric = 2 g, so d/dt u <= Delta u - 2 <grad Phi, grad u> - 4 u. Phi_t is smooth for t >= 0
(the Wilson density is smooth and positive) and the manifold is compact. At a maximum point of u in the fields the first two terms are at most zero. So
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
a(0) below about 2. For the Wilson rule a(0) is at least 6 x (the diagonal term at a field with six
plaquettes at -1, see 2.4) and at most 24 x (six plaquettes, eighteen neighbours). So the bound closes for x
below 1/12, cannot close for x above 1/3, and at larger x it blows up at a time of order 1/x. This is the
Bakry-Emery hand range. (iii) For large t the constrained system of N_t is the measure itself, so the step
moves no difficulty (Remark END). Relatives
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
ratios. It fails (t1): in four dimensions the recursion flows to strong coupling for U(1) at every coupling
(recalled),
and compact U(1) is massless at weak coupling on Z^4. So every bridge from Z^4 to the hierarchical lattice
must fail for U(1) at a named line, and none on file does (row 770: Tomboulis's interpolation is not a proof).

## 3. Step 3: the scoped negative, with sizes (written 2026-11-24T15:27Z, date -u)

### 3.1 Every sufficient finite statement on file is of one of three kinds

- (K-small) a small number at the scale of the statement: the expansions of rows 1471 and 1353, one-link and
  block Dobrushin, convexity. Ceilings: 0.0087, 2/9, 0.3609, 1/3 (2.4), 1/4.
- (K-sup) a supremum over boundary values of a finite region: (W) of row 691, PA_g of row 750, every local-gap
  form (Lemma FIB). Truth at 2.3 unknown.
- (K-law) an in-law number of a finite region: (AN) of row 845, the rank-one test and the purity on a finite
  torus (rows 1353 to 1359), the product defect of 2.5.

I found no fourth kind in this row, and rows 735, 770 and 1116 found none in the literature. This is an
inventory, not a theorem.

### 3.2 The size of one check at readout 2.3 (all lattice numbers GUIDE)

Correlation length: about one lattice unit at beta 2.3 (`gap-verified-compute-sizing-fable.md` line 290: the
published values put m a = 4.1 at four lattice units, and its smallest test torus at about 4 x 8^3).

| Kind | Region the statement needs | What must be evaluated | Best exact method on file | Cost |
|---|---|---|---|---|
| (K-sup), (W) | a cube of side R with 8 R^3 k <= delta R^4 roughly, k the mean response to one changed boundary link; k of order 1 gives R at least 8 (GUESSED) | a transport cost between two laws on about 23,000 links, uniformly over boundary values in a space of dimension about 3 x 10^4 | none above eight links (rows 1341, 1344) | not bounded by any method on file |
| (K-law), purity or rank-one test | a torus of about 4 x 8^3 (row 1326 5.1) | two or more partition functions with a small absolute error in the logarithm (row 1326: 3.6e-4 at its window instance) | exact contraction | at least 2^(2 x 256 + 1), about 10^154 (Lemma DIM, row 1326) |
| (K-law), (AN) | blocks larger than the correlation length (row 845 Section 5 (4)) | mixed moments of block responses along the stationary chain | none | not sized on file; not smaller than the line above |
| (K-small) | one plaquette to one 2^4 block | Bessel ratios, small tables | hand, or seconds of exact arithmetic | fits a Lean row; false at 2.3 |

What exact evaluation reaches today: one 2^4 block (rows 1425 and 1429: character sums to spin order 42 in at
most 149 s for one coefficient; row 1341: an eight-link enclosure in 6.5e14 gates).

**The mismatch.** A statement of kind (K-sup) or (K-law) needs a region of side about 4 to 8 at readout 2.3.
Exact evaluation reaches side 2. The cost of exact contraction grows like 2^(2 L^3). A Q2 step does not
close the mismatch (ARGUED): one step halves the correlation length, but the image rule is known only through
the constrained system on fine regions of the same physical size, and computing it to the accuracy of the
class is again a number of kind (K-sup) or (K-law) at the fine scale.

**Answer to the sizing question of the row.** For every representation I can name, one step's check at beta
about 2.3 does not fit exact Lean kernel checking (`decide`, `norm_num`), and it does not fit exact rational
computation on a 16 GB machine: the smallest in-law instance is about 10^154 operations, and the worst-case
instance has no method. The only checks that fit a Lean row are of kind (K-small), and they are false at 2.3.

### 3.3 T2 against (a), (b), (c), candidate by candidate

| Candidate | (a) closure or end | (b) finite check of known cost | (c) filter | State |
|---|---|---|---|---|
| (W) on cubes as an end class at readout 2.3 (Remark END) | yes, given (W): Theorem W of row 691; the step to the sixteen masses is OPEN as a written proof (3.5) | finite in principle (a strict inequality of continuous functions on a compact set); no bound on the cost | passes as a criterion (Remark SOUND); carries no mechanism | fails (b) |
| Local gap (2.2), pair norm (row 750) | yes in the gauge-invariant form, conditionally (GC4) | same as above (Lemma FIB) | same | fails (b) |
| (AN) and weights (2.1, row 845) | yes, given (AN): Theorem AG | in-law; (SP-ext) open; no evaluation | fails for Villain U(1) at a named step (Theorem UA there) | fails (b) |
| Purity or product defect on finite regions (2.5) | not proved in the space directions | 10^154 at least | passes as a criterion | fails (a) and (b) |
| Noise map with the gradient class (2.3) | closed with no small number (Lemma NG), but the class is not an end class (Remark FI) | trivial | gain zero for U(1), blind to the dimension | fails (a) |
| Convexity with curvature (2.4) | closed by Schur complements | Fourier arithmetic | empty for U(1) | empty above x = 1/3 |
| Migdal-Kadanoff (2.6) | exact on the hierarchical lattice only | Bessel ratios | fails (t1) | fails (c) |
| Tubes of local rules with a typical-field norm (row 1468 4.2) | not proved; no method | not defined | passes | as in row 1468: no first lemma |

**Verdict. T2 is NOT solved.** No representation named here or on file meets (a), (b) and (c) with a check
that can be run. Each candidate fails at a different clause, and the three that are sound criteria fail at
the same one: the evaluation of a number of a region several correlation lengths wide, with no small
parameter.

### 3.4 Is there an obstruction? What is proved and what is not

No obstruction to the existence of a T2 representation is proved here. I do not believe one exists as a
theorem: (W) at readout 2.3 may be a true statement, and a true strict inequality on a compact set has a
finite proof in principle. What holds for stated classes:

- Classes whose check is of kind (K-small) in a variable on file (plaquette activities, one-link or block
  influence, Hessian plus curvature): empty at 2.3. PROVED for convexity (2.4: x below 1/3); on file for the
  others. For the expansion in the plaquette activity the published strong-coupling series puts the
  crossover near its radius (GUIDE, recalled), so no better counting of polymers will reach u = 0.51.
- Classes whose check is exact contraction: excluded by Lemma DIM of row 1326 (10^154), on file.
- Classes whose check is a supremum over boundary values: no method, and expected false a little above 2.3
  (row 950, GUIDE). Not refuted by CA-FAIL (1.4).
- Linear classes (convex in the density): excluded by Remark FI of row 1386, on file.

So the negative is by cost for the sound criteria and by closure for the cheap ones, as row 1468 5.2 to 5.4
said for its five representations. This row extends that verdict to six more candidates and adds no new
kind. It does not show that the list of kinds is complete.

**What would reopen T2 (proposed triggers, to add to (R1) to (R3) of row 1442).**
- (R4) A rigorous method, not sampling, that bounds an in-law number of a block of side 4 or more at cost
  polynomial in the block volume. Bootstrap bounds on one-point functions are of this type (Kazakov and
  Zheng, recalled from row 770), but Theorem O with Remark OS of row 1326 says that a certificate of decay
  needs a patch as large as a seed box.
- (R5) An exact self-similar map whose constrained system is a product over blocks. The exact 2^4 cube map
  of row 1341 has a product constrained system and is not self-similar (check 1346). A map with both
  properties would make every step a one-block computation.
- (R6) A second small number at readout 2.3 after an exact change of variables (means (m2) of row 735).
  The numbers at hand there: u = 0.51, the higher character ratios 0.19, 0.056, 0.014 (recalled Bessel
  values, not recomputed), and e^(-m) of about 0.25 to 0.37 for the decay over one lattice unit, which is
  known only from numerics.

### 3.5 An open written step, named so that nobody assumes it

If (W) or (AN) were ever evaluated at readout 2.3, the chain still needs: covariance decay with constants free
of the torus, on the sixteen twisted tori, gives purity at least 457/625. Sketch: change one link of a time
slice at a time; each change of the log of a mass ratio is the log of a ratio of expectations of a bounded
local positive function under two boundary values at distance of order the time side; sum over the m^3 links
of the slice. SKETCHED, not written. Relatives on file: Theorem END-K2 of row 1471 (for the expansion class),
Lemma BT and Corollaries BT1, BT2 of row 1353. This is not a row to queue now: it has no supplier.

## 4. The next two rows, and their decisive outcomes

**Row 1, cross-provider check of this file.** In order: Lemma NG (the Bochner identity on a product of
spheres, the term <grad Phi, grad u>, the maximum principle, the factor 1 for U(1)); the one-line Hessian of
2.4 and the bound x below 1/3; Lemma FIB as repeated; the reading of CA-FAIL in 1.4 against row 1468 (C4);
the claims that 2.1, 2.2 and 2.5 are covered by rows 845, 750 and 1353 to 1359; the table of 3.2 against rows
1326 and 1418. Decisive outcome: HOLDS, HOLDS AFTER CORRECTION, or FAILS at the first wrong line. If the
checker names a representation of means (m2) or (m4) that is not on file, that is the next proof row. If it
finds that one of the six candidates is not covered by the row I cite, that candidate reopens.

**Row 2, `gap-k2-cube-response-guide` (GUIDE run; decides whether the worst-case kind is false at 2.3).**
Wilson SU(2) at beta 2.2, 2.3, 2.5 in cubes of side R = 4, 6, 8 with fixed boundary values: (i) typical
boundary values drawn from a larger torus, (ii) the pinned pi-flux face of row 950, (iii) all boundary links
equal to 1. Measure the response to one changed boundary link by two coupled heat-bath copies with common
random numbers: the mean number of plaquettes of the cube whose traces differ by more than a tolerance,
against R. Decisive outcome, one of two: (a) at some boundary value the response per boundary link grows
like R^2 or exceeds R/8 at R = 8 for beta 2.3: then (W), PA_g and every local-gap form are false at the
readout where the chain needs them (GUIDE grade), the worst-case kind is closed on the record, and only
in-law criteria remain; (b) the response stays below R/8 at all three boundary values: then (W) at 2.3 stays
a possible true statement with no method, and nothing is closed. The run cannot prove (W). Cost: minutes
(row 936 measured about 13 ms per sweep at 3,500 sites; recalled from the worker's notes). It needs 50 percent free memory; this session had 37 to 40.

Not proposed: a proof row on T2. There is no first lemma for it. The row that can still lower the count of
certified steps is `gap-k2-entry-hand-radius`, already named by row 1471.

## 5. Summary of labels, repo search, credits

| Item | Label |
|---|---|
| Remark SOUND (a sound finite criterion passes the filter as a criterion; the filter tests the proof of (a)) | PROVED, one line |
| Remark END (a criterion of type (W) at readout 2.3 is an end class; a step is not needed there) | ARGUED from rows 691 and 1471 |
| 1.4: CA-FAIL does not refute (W) on cubes | READ; agrees with row 1326 4.1 |
| Lemma FIB | ON FILE (`gap-glue-max.md` 241-242), repeated with proof |
| Lemma NG (one-link gradient of the noise-map rule decays like e^(-2t); factor 1 for U(1)) | PROVED here by hand, unchecked; not found on file |
| Riccati bound for the Hessian row sum under the noise map | SKETCHED |
| 2.4: Hess Phi + Ric positive at every field only for x below 1/3 | PROVED, one line |
| 2.1, 2.2, 2.5, 2.6 | covered by rows 845, 750, 1353 to 1359, 770; no new statement |
| Sizes of 3.2 | GUIDE and GUESSED as marked; costs from rows 1326, 1341, 1418, 1425 |
| Verdict of 3.3; triggers (R4) to (R6) | the verdict is an inventory of failures, not a theorem; the triggers are proposals |
| A T2 representation; an obstruction to one; (W) or (AN) at readout 2.3; the step of 3.5; T1; (BASE-K2); the seed; the mass gap | OPEN |

Repo search (rule 0a, and "before you call a statement new"). `library/open-core.md`: no hit for chessboard,
Knabe, frustration-free, weak mixing, Brascamp, Pechersky, Lyapunov, direct integral, Riccati (grep counts
all zero). FINISH rows and `library/`: the hits are the rows cited in Sections 1 and 2. Not searched: main,
PR #10114 and the other PR branches (row 1468 Section 9 searched them for the block step two hours before
this row and found no step at order-one coupling). The Sussman-Alpoge repository was not opened in this row:
the question is at order-one coupling, where the release has no statement (rows 1464, 1470); I relied on
those reads.

Credits. T. Balaban: the small-field and large-field scheme that the weak part needs. E. T. Tomboulis: the
Migdal-Kadanoff interpolation (with the objection of Ito and Seiler). R. Kotecky and D. Preiss: the expansion
criterion of the end class. E. Sussman and L. Alpoge, with Claude and Codex as authors of their text: the
contour mean and the kernel that Q2 copies, and the release whose floor rows 1464 and 1470 read. R. Dobrushin
and S. Shlosman: the cube criterion; Dobrushin and Pechersky; Hairer and Mattingly: weights for bad states.
Knabe; Gosset and Mozgunov; Lemm and Mozgunov: local-gap thresholds. Bakry and Emery; Brascamp and Lieb;
Bochner; Li and Yau; Hamilton: the curvature calculus of 2.3 and 2.4. Finner: the inequality named in 2.5.
Frohlich, Simon and Spencer: the order used by CA-FAIL. In the lane: Claude Opus 5.5 (rows 845, 1072, 1470),
Codex gpt-6-astra (row 750), Claude Fable 5.2 (rows 691, 1326, 1386, 1442, 1468, 1471), Codex gpt-6-luna (row
1116). Everything recalled from the literature in this row is marked recalled and was not re-read.

Not done in this row: no numeric job (free memory 37 to 40 percent, below the 50 percent rule); no Lean; no
code; no commit or push; the files of rows 1460, 1461 and 1466 were not opened; the Riccati inequality of 2.3
was not derived in full.

Status: done 2026-11-24T15:28Z (date -u), author only (Claude Fable 5.2 high, Mac mini worker 1), unchecked.

## 6. Result

RESULT: Row 1474 (Claude Fable 5.2 high, Mac mini worker 1; author only, checked by no one; hand arguments, no numeric run because free memory stayed at 37 to 40 percent, no Lean, no code, nothing committed). T2 is NOT solved, and no obstruction to its existence is proved. (1) Exact form: for the stretch from readout 2.3 to the end class a block step is not needed where an end criterion holds (Remark END), so T2 there is a finite criterion for decay at readout 2.3 that can be evaluated; a sound criterion passes the filter (t1) to (t6) by itself, and the filter tests the proof of its sufficiency (Remark SOUND). (2) Six candidates tried, none survives: the typical-field cube criterion with weights (covered by row 845, Theorems AG and LW, open (SP-ext)); the local-gap form of Knabe for the heat-bath generator (a worst-case criterion over exteriors by Lemma FIB, which is on file in `gap-glue-max.md`; covered by row 750); the noise map e^(t Delta) in field space (exact, same lattice, keeps the sixteen masses; Lemma NG, PROVED here and not found on file: the supremum of the one-link gradient of the rule decays like e^(-2t) with no small number, by the Ricci curvature 2 of SU(2), factor 1 for U(1); but a small one-link gradient is not an end class by Remark FI of row 1386, and the Hessian obeys a Riccati bound that closes only in the hand range, SKETCHED); convexity with curvature (closed by Schur complements, empty for x above 1/3, PROVED in one line); the L2 product defect of block tensors (the rank-one test of rows 1353 to 1359 in space; in-law cost); Migdal-Kadanoff (fails (t1)). (3) Sizes at beta about 2.3 (GUIDE): every sound criterion is a supremum over boundary values or an in-law number of a region of side about 4 to 8, exact evaluation reaches side 2, the smallest in-law instance costs at least 10^154 operations (Lemma DIM of row 1326) and the worst-case instance (a cube of side about 8, 23,000 links) has no method; so one step's check fits neither Lean kernel checking by `decide` or `norm_num` nor exact rational computation on 16 GB; only checks with a small number fit, and they are false at 2.3. (4) Correction to the record: CA-FAIL refutes strong mixing over all volumes, not the cube criterion (W) of row 691; (W) at 2.3 may be true and has no method (agrees with row 1326 4.1; row 1468 (C4) stands for block steps as argued). OPEN: a T2 representation, (W) or (AN) at readout 2.3, the written step from covariance decay on the sixteen tori to purity, T1, (BASE-K2), the seed, the mass gap. Proposed triggers: (R4) a rigorous in-law method of polynomial cost that is not sampling, (R5) an exact self-similar map with a product constrained system, (R6) a second small number at readout 2.3. Next rows: a cross-provider check of this file (Lemma NG first); `gap-k2-cube-response-guide`, a GUIDE run of the boundary response in cubes of side 4 to 8 at beta 2.2 to 2.5 (growth like R^2 at the pi-flux face closes the worst-case kind at 2.3 on the record; a bounded response closes nothing); no proof row on T2 is proposed.
