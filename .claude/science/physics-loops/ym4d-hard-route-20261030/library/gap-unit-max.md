lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-15T12:45Z

# gap-unit-max (FINISH row 988): the unit-scale inequality (U1) or (U2), direction item, crux lemma

Worker: Claude Fable 5.2, max effort, Mac mini worker 1, one session, no subagents. Pinned commit 708bcda9e.
This is research-stage working state. Nothing here is a claim that the mass gap or any part of it is proved.
Marks used: PROVED (every step written here, by hand), ARGUED (argument written, a step is not complete),
OPEN, RECALLED (a literature statement quoted, not rebuilt here), GUIDE (numeric, can refute or guide, never prove).

## 0. Plan (at most eight steps; one step per response; each step appends its result here before the next)

1. Scope: the object and the goal as stated in row 982 Section 4.1-4.3 (statement only, no route text);
   duplicate check (rule 0a) against `library/open-core.md` and the FINISH rows.
2. At least three approaches of my own, written from the goal and the object before any route file or digest is read.
3. Fact tests on each approach, one verdict each: Lemma CAP, Lemma COUNT (row 982, checked in row 984);
   Theorem D2 (row 977, checked in row 979); Lemma META (row 975); the square-root test (row 978 5.7);
   free photon; compact U(1); frozen Q_8 and 2T; K7; FT-FK.
4. Attack on the crux lemma of the best approach, stage 1.
5. Attack, stage 2 (or the second route if stage 1 fails).
6. Attack, stage 3 (or the third route; a GUIDE run only with criteria written first and under the numeric lock).
7. Read rows 720, 970, 975-986; say per approach whether it is already there.
8. Verdicts, marks, what stays open, the next step, one RESULT line.

## Status log (UTC, read from `date -u`)

- 2026-11-15T00:45Z: session start; row 988 read (FINISH.md line 1065); output file created. No earlier run of this
  item exists at the pinned commit (`library/gap-unit-max.md` and `library/guide/lane988/` were absent).
- 2026-11-15T01:30Z: Steps 1 to 3 written (the first response was lost at the output limit; work redone in small steps).
- 2026-11-15T01:37Z: Steps 4 to 8 written; all eight steps of the plan are done. No script or data was produced, so
  `library/guide/lane988/` was not created. The lease above may be released.

## Step 1. Scope, object, goal, duplicate check

**Read so far (statement only):** GOAL.md; FINISH.md lines 1-84 and row 988 (line 1065); `library/gap-hcphys-max.md`
lines 1-22 and Section 4.1-4.3 (lines 117-163). No route text (its Steps 5-7) and no digest was read before Step 2.

**Object.** B is the cube of physical side 2 ell. The gauge-invariant transfer operator on B at the unit-scale
effective weight has energies E_0 = 0 < E_1 <= E_2 <= ... . For real t > 0 (lattice units of time):
S(t) = sum over i >= 1 of e^(-E_i t), X(t) = log(1 + S(t)) = log Z(B x t) - t * (vacuum rate), U(t) = -X'(t).
By (EX) of row 982 4.1, X is the same number for the fine weight and for the blocked weight.
The family: bare couplings g_0 with first-passage cutoff K, unit coupling in the window [g^(-2), g^(-2) + B_sharp]
(CA-I 631-683, Definition 1.2). The cube has e^(c/g^2) unit cells per side if masses scale by asymptotic freedom.

**Goal (row 988).** One of:
- (U1): ||P^(mT) g||_2 <= ||g||_(1 + e^(-2 alpha_* m)) for g = p_s(u, .), all integers m >= 0, alpha_* > 0 free of the cutoff;
- (U2): X(t + 2mT) <= (1 - tanh(alpha_* m)) X(t) at t = tau_0/a_iota, all m.
(U3) is not a goal form: row 984 corrected row 982, (U3) implies (U2) and not the converse.

**What (U2) says in plain terms (my reading, PROVED from the definitions).** 1 - tanh(alpha m) = 2/(e^(2 alpha m) + 1).
So (U2) is: the excess free energy X of the periodic box decays by a rate 2 alpha_* per unit of time, starting at the
time tau_0 where X is still of the order of the volume, Theta(ell). The gap alone gives decay only after the time t_c
where S(t_c) <= 1 (Lemma EE (d)). Between tau_0 and t_c the statement is about the number of states of the box
(Lemma COUNT). Row 988 says row 982 failed there three times: "the thermal sum of the cube between the hot end and
the cold range".

**Duplicate check (rule 0a).** `library/open-core.md` (564 lines): no line with (UNIT), (U1), (U2), unit scale,
HC-phys, LSI-traj-seed, Z-UNB or BDD-Delta. FINISH rows with (UNIT), (U1) or (U2): 982 (the source), 984 (its check),
988 (this row); row 635 matches only by a different (U1). Named matches stated by row 982 itself: (Z-UNB) and
(BDD-Delta) of row 720 Theorem ZD; (LSI-traj-seed) of row 970. Row 988 assigns this lemma to this lane, so the attack
is not a duplicate; rows 720, 970, 975-986 are compared in Step 7.

## Step 2. Approaches of my own, written before any route file or digest was read

Notation of my own. Phi(L_1, L_2, L_3, L_4) := log Z on the periodic torus with these sides (fine lattice units, Wilson
weight; by (EX) the unit weight gives the same number). f := - lim Phi/Vol_4, the free energy per site in infinite volume.

  Y(L_1, ..., L_4) := Phi(L_1, ..., L_4) + f L_1 L_2 L_3 L_4     (total finite-size excess; symmetric in the four sides)
  y(L) := Y(L, L, L, L)                                           (excess of the hypercubic torus)

What I use about the object: in each direction mu the torus sum is Tr T_mu^(L_mu) with T_mu >= 0 (Wilson transfer
operator on the gauge-invariant space of the cross-section; positivity is Osterwalder-Seiler / Luscher, RECALLED).

**Approach A (hypercube reduction).** For A >= 0 trace class, Tr A^k <= (Tr A)^k. So Phi(.., k L_mu, ..) <= k Phi(.., L_mu, ..)
in each direction. Consequences, each one line (written out and checked in Step 4):
 (A1) Y >= 0, and Y(.., k L_mu, ..) <= k Y(.., L_mu, ..).
 (A2) X(t; B) <= Y(B, t), because E_0(B) <= f |B|.
 (A3) X(t; B) <= (|B|/t^3) y(t) when the three sides of B are multiples of t.
 (A4) y(L) = sum over j >= 0 of 16^(-j) d(2^j L), d(L) := Phi(L^4) - Phi((2L)^4)/16 >= 0 (one-doubling defect).
So the seed X(ell; cube of side 2 ell) <= log(1 + s_*) follows from ONE number: y(ell) <= (1/8) log(1 + s_*).
Only hypercubic tori occur, which are the tori of the account (this would answer (PQ-EX) of row 982 4.1).
Extensivity of the state count, which the gap alone does not give (Lemma COUNT), is here a consequence of (A3).
Crux lemma: (Y-SEED) y(L_*) <= eps_* at one L_*, uniformly in the cutoff.
Expected behaviour (ARGUED, not proved): gapped phase with one vacuum y -> 0 exponentially; free photon y -> a positive
constant (Casimir energy of the 4-torus is scale free); deconfined finite group y -> log of the number of torus vacua.
So y is an order parameter for "massive with one vacuum", and the tests can act on its value.

**Approach B (twisted, flux-projected seed at weak coupling, then a marginal engine).** In a box with a 't Hooft twist
m != 0 there is no toron valley. Perturbation theory at small running coupling g(L) has a gap of order 1/L in the sector
e.m = 0. So a seed-like inequality X^(m, e.m = 0)(c L; L^3) <= small is within reach of the small-coupling RG at L << xi.
Crux lemma: an engine that carries a twisted seed across the scale xi. It must use Z_m/Z_0 -> 1 (vortex free energy),
or else it would prove (U2) for frozen Q_8, where the twisted sector is gapped at all scales and (U2) is false.
In step-scaling words the crux is a monotone law for r(L) = Z_m(L^4)/Z_0(L^4), a nonperturbative form of asymptotic freedom.

**Approach C (curvature of the orbit space).** In the ground-state representation H - E_0 is the Dirichlet operator of
nu = Omega^2 on G^E/G^V. O'Neill's formula adds (3/4)|[X, Y]^V|^2 to the sectional curvature of the quotient. The term
is zero for an abelian group and absent for a finite group, so it has the right sensitivity for the U(1), Q_8, 2T tests.
Crux lemma: Ric_quotient + Hess(-2 log Omega) >= rho > 0 in an averaged sense.
My own estimate before reading: the O'Neill term is bounded by the Hilbert-Schmidt norm of ad_X, of order |X|^2 in
lattice units, with no factor beta. The Hessian of the action has negative directions of order beta. So the pointwise
criterion fails for beta of order one or more, and an averaged form is what row 977 Theorem D2 speaks about (Step 3).

**Approach D (purity, two replicas).** Tr rho_t^2 = Z(2t)/Z(t)^2 for the thermal state rho_t. With D(t) := log Z(t) -
(1/2) log Z(2t): D <= X <= 2 D (since X(2t) <= X(t)). So (U2) is decay of the Renyi-2 entropy of the thermal state from an
extensive value. In four directions the same object is d(L) of (A4). Crux lemma: an upper bound on the "gluing cost"
Z(L^4)^16/Z((2L)^4). Chessboard estimates give only the lower bound 1. Jensen gives a bound of the order of the
boundary action, beta L^3. So D has no route to smallness of its own; it is a form of A.

**Approach E (operator comparison).** If H >= H' then Tr e^(-tH) <= Tr e^(-tH'). Golden-Thompson and a trial state give
X(t) <= log Tr(e^(-tK) e^(-tV)) + t <psi, H psi>. Both sides are extensive and X is their small difference, so any
comparison loses a constant per site. Fails at once: no crux lemma.

**Choice.** A is the best: it has a proved core, it removes the "between" range of row 982 from the problem, and its
crux is one number on the account's own tori. B is second: it names where a weak-coupling seed exists and what the
engine would have to be. C third. D and E are recorded as dead.

What I expect, said before the attack: (Y-SEED) at L_* near the correlation length is as hard as the gap itself.
No approach above supplies the order-one input from soft arguments. The attack in Steps 4-6 proves the core of A and
then tries three routes to (Y-SEED).

## Step 3. Fact tests, one verdict each; first comparison with the lane's core statements

Read for this step (statements only): `gap-crux-restate.md` 3.1 and 3.4 (Theorem D, Lemmas K, X, E, Theorem S,
Corollary S3'); `gap-phys-seed.md` L253-327 (Lemma Z, Theorem ZD, ZD-c, Corollary Z4); `gap-ladder-max.md` 5.7
(Proposition Delta, Corollary CU, square-root test); `gap-tiltproof-max.md` L240 (Theorem D2); `gap-ymcons-opus.md`
L134 (Lemma META); `gap-constraints-max.md` L73 (K7); `gap-pca-opus.md` L319 (FT-FK); `gap-hcphys-max.md` 3.0 (CAP).

### 3.1 What the core statements already hold (found right after Step 2 was written)

- Approach A is in the lane, in a stronger form. (A1) is Lemma K; my exchange identity is Lemma X; (A3) is
  Proposition Delta of row 708: g(a; b^3) <= (b/a)^3 Delta(a^4); my y(L) is the lane's Delta(L^4) = D(L); (A4) is the
  line "Delta(n^4) = sum over k of 16^(-(k+1)) Phi(2^k n)" (`gap-crux-restate.md` L123). Theorem D (b) needs ONE doubling
  defect, not the series: 1 + S(n; (2n)^3) <= exp(Phi(n)), Phi(n) = 16 F(n^4) - F((2n)^4). Theorem S turns s < 1/5041
  into a gap on all cubes. So (Y-SEED) is the lane's (SEED): Phi(n) <= 1.9 x 10^(-4) at one n. My claim that A
  "would answer (PQ-EX)" is void: Corollary CU (row 978 5.7) already uses hypercubic tori only, through (APR).
- Approach D is in the lane: row 982 Route 2 (d), (e) (Renyi-2 form), and `gap-compress-opus.md` L113.
- A sixth approach I wrote down while reading (Fisher zeros: a volume-uniform zero-free neighbourhood of [0, beta] in
  complex beta, the strong-coupling disc as anchor, the two-constants theorem for 16 F(n) - F(2n)) is the lane's
  Route Z (`gap-skeleton-final.md` 4.2; `gap-crux-fp.md` L232: "the zero-free radius shrinks like a power of the gap").
- My formula "seed = integral over the coupling of a finite-size plaquette shift" is Theorem D (f).

### 3.2 Test table (one verdict per approach and test)

Tests: CAP = Lemma CAP (b) of row 982 (an integrated bridge Poincare constant is at most (e^(2 E_1) - 1)/2);
COUNT = Lemma COUNT (b) (a decay claim caps log N(E)); D2 = Theorem D2 of row 977 (no criterion with a supremum over
tilts); META = Lemma META of row 975 (name the transience input); SQRT = the square-root test of row 978 5.7 (a
space-time constant restricted to a slice returns omega^2/2, not omega); PH = free photon; U1 = compact U(1), both must
fail through the rate; Q8 = frozen Q_8 and 2T; K7 = the mixed-action endpoint; FK = FT-FK.

| Approach | CAP, COUNT | D2 | META | SQRT | PH, U1 | Q8, 2T | K7 | FK | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| A hypercube / seed form | not engaged: exact, no rate | n/a | n/a | n/a | pass: Phi >= 0.41 for U(1) (row 697 fact (ii)) | pass: Phi -> log of the vacuum count | pass: no seed at the endpoint | n/a | sound, group-blind, already there; all content is in the seed |
| B twisted seed, marginal engine | COUNT engaged: a massless box has N(E) of a gas with M = 0 | n/a | fails to name it: the twisted sector of Q_8 is gapped, the full box is not | n/a | pass (no twist for U(1)) | FAILS unless the engine reads Z_m/Z_0 | must fail at the endpoint; no step named | n/a | no seed below the massless floor (Step 4) |
| C orbit-space curvature | CAP engaged: caps the constant by E_1 | pointwise form is a supremum over fields: hit by D2 | not named | FAILS on the 4D law; open on the slice law | pass (O'Neill term zero for U(1)) | pass (no manifold) | must fail; no step named | n/a | fails by size, Step 6 |
| D purity | as A | n/a | n/a | n/a | as A | as A | as A | n/a | a form of A |
| E operator comparison | fails COUNT at once: loses a constant per site | - | - | - | - | - | - | - | dead |
| Z zeros (Route Z) | not engaged | n/a | n/a | n/a | pass: zeros pinch the axis at the transition | pass | pass: zeros pinch at the endpoint | n/a | sound implication, already there; hypothesis is the open part |
| G anchor at beta_t = 0 (Step 5) | not engaged: an identity | n/a | not named | n/a | pass: the identity holds for U(1) and proves nothing | pass | pass: a level crossing on the path is not excluded | pass: the path acts on the kinetic part, and the identity keeps V | restates the seed along a new path |

Reading of the table. No approach of mine names a transience input (META) and none has a step that U(1) fails
through a rate while SU(2) passes. Each sound one (A, D, Z, G) is exact and group-blind, so it carries the seed and
cannot supply it. This is the lane's own finding (`gap-constraints-max.md` Section 2), reached again from the object.

## Steps 4 to 6. The attack on the crux lemma, three routes

**Crux lemma, in the lane's sharpest form (Theorem S, Theorem D (b), Corollary Z4; ported, not redone).**
(SEED): s = S(n; (2n)^3) < 1/5041 at one n, uniformly in the cutoff; it follows from Phi(n) <= 1.9 x 10^(-4).
(U1) and (U2) are suppliers of (SEED) through Corollary CU. With (BDD-Delta), D <= D_0, Corollary Z4 gives the
equivalent target: one cube with b m(b^3) >= 256 D_0 + 29.64. The routes below are mine and are not the three of
row 982 (fine metric, no metric, count of states).

### Route 1 (Step 4). A seed inside the window: twisted or flux-projected sectors (Approach B)

**Lemma FLOOR (PROVED; it is Theorem D (c) read backwards, stated for any sector).** Let T >= 0 be trace class with
simple top eigenvalue, and let the trace run over any T-invariant subspace that holds the top eigenvector. If the
subspace has a level E above the ground level, then S(a) >= e^(-a E). So s < 1/5041 on (n; (2n)^3) forces
n m((2n)^3) > log 5041 = 2 log 71 > 8.52, that is: side times gap above 17.04.
Proof. S(a) is a sum of positive terms, one of them e^(-a E). QED

Use. In the window (side far below the correlation length) the periodic cube has levels at (2 pi/side)(1 + o(1))
(RECALLED, the lane's K5; SU(2) torons lie lower). With side 2n: n E = pi, so s >= e^(-pi) > 0.04 per level.
In a 't Hooft-twisted cube the momenta are shifted by pi/side (RECALLED, twist-eaters; lane ideas 15 and 31 of
`gap-brainstorm2-max.md` L220 and `gap-brainstorm-max.md` L404): n E = pi/2, s >= e^(-pi/2) > 0.2. A twist removes
the toron valley, and the toron valley is not the obstruction: the obstruction is 17.04 against pi.
A long thin shape (time a = 6 x side) has a perturbative twisted seed, but Lemma X needs a < b: the Casimir deficit
of a box is bounded by its thermal sum only at a time shorter than the side. So that seed feeds no engine.

What is left of B is a marginal engine: a law that moves s (or the twist ratio r(L) = Z_m/Z_0, lane idea 8,
`gap-brainstorm-max.md` L284) monotonically across the order-one band. No engine that reads only positivity and the
exchange symmetry can do this (ARGUED): the Coulomb phase of U(1) has both, and its s is constant in n, at least
12 e^(-pi) (row 697, fact (ii)). So asymptotic freedom would have to enter as a new exact input valid beyond first
passage. The account supplies none: its flow constants are defined up to first passage only (CA-I 631-683).

Verdict: FAILS at the first step. Already there: SMALL-BOX and ideas 8, 15, 31. New here: nothing but the sector form
of the floor and the number 17.04.

### Route 2 (Step 5). A second anchor: zero temporal coupling at the full spatial coupling (Approach G, written here)

Take the anisotropic Wilson weight exp(-beta_s A_s - beta_t A_t), A_t = sum over the 3 |B| t temporal plaquettes of
(1 - (1/2) tr U_p). T(beta_t) = e^(-V/2) K_(beta_t) e^(-V/2), with V = beta_s (spatial action of one slice).

**Identity G (PROVED, by hand).** For every box B, every t and every beta_s:
 (a) at beta_t = 0 the slices are independent: Z(B x t) = Z_3(B)^t, T has rank one, and S(t; B) = 0 for all t;
 (b) X(t; B)(beta_s, beta_t) = 3 |B| t x integral over s in [0, beta_t] of (abar_inf(s) - abar_t(s)), where abar_t(s) is
     the mean temporal plaquette action on B x t at temporal coupling s and abar_inf its limit as t grows.
Proof. (a) With no temporal weight the temporal links integrate to 1 and the slices decouple; K_0 is the projection
on constants. (b) d log Z(B x t)/d beta_t = -3 |B| t abar_t. log lambda_0 is analytic in beta_t (simple isolated top
eigenvalue of an analytic family of compact operators with strictly positive kernels) and is the limit of the convex
functions (1/t) log Z(B x t), so its derivative is the limit of theirs, -3 |B| abar_inf. Integrate from 0, with (a). QED

So the seed at the isotropic point is an integral along a path on which the spatial coupling never leaves the unit
value. This differs from Theorem D (f), whose path runs through isotropic strong coupling, and from idea 32 of row 859
(the line beta_s = 0). The exchange symmetry is needed only at the end point, where it holds.

Attack on the path. Two inputs would be needed.
 (i) A seed in the time direction for small s, uniform in the box. One-link influence is small in total variation:
     changing one link of U changes the density of the next slice by a factor in [e^(-4 s), e^(4 s)] (PROVED: one
     factor e^(-s (1 - (1/2) tr)) in [e^(-2s), 1] changes inside the gauge average, so the kernel changes by a factor in
     [e^(-2s), e^(2s)], and so does the normalising constant). But the changed law can differ on
     all links, through the correlations of the slice law nu_0, the three-dimensional theory at the unit coupling. A
     volume-free rate needs s times a susceptibility of nu_0 below one. That is a mixing statement for three-dimensional
     SU(2) at weak coupling: OPEN, and not in the account.
 (ii) No level crossing along s in (0, beta]. The gap ratio lambda_1/lambda_0 of A e^(-tau C) A is not monotone in tau in
     general (ARGUED: a narrow deep well against a broad shallow well of V exchanges the ground state as tau grows; for two
     levels it is monotone, PROVED by det/tr^2 = [e^(-v)/(1 + e^(-v))^2] [4 e^(-tau)/(1 + e^(-tau))^2]). The coupling that
     runs is of order (beta_s s)^(-1/2), so the order-one band is crossed near s of order 1/beta_s (ARGUED).

Verdict: FAILS at (i) and again at (ii). It restates the seed along another path. What is left: Identity G as an exact
anchor that needs no strong spatial coupling. Marks: Identity G PROVED; (i), (ii) OPEN.

### Route 3 (Step 6). Exclude the gapless branch of Corollary Z4 by asymptotic freedom

Given (BDD-Delta), Corollary Z4 leaves two branches: (SEED), or every periodic cube of side b >= 4 a_0 has a level
within (256 D_0 + 29.64)/b of its ground level. Plan: show that the second branch contradicts the ultraviolet data.
 (a) The second branch is what a scale-invariant infrared limit looks like. The ultraviolet data of the account say
     that the coupling is small and grows up to first passage. A flow from a free ultraviolet end to an interacting
     scale-invariant infrared end is a consistent picture in general, so no contradiction follows from the two ends alone.
 (b) A contradiction needs a statement "light levels on all cubes force the unit action back into the window". K7
     refutes every soft form of it: at the mixed-action endpoint the cubes have light levels and the coupling is of
     order one (row 708, Proposition V, as quoted in `gap-constraints-max.md` L73).
 (c) So the branch can only be excluded by an input that tells the Wilson trajectory from the endpoint family beyond
     first passage. None is in the account or in the lane.

Verdict: FAILS at (b). Result of the route: the crux in one sentence. **The order-one input is the exclusion of a
gapless scale-invariant branch beyond first passage**; every exact tool in the lane (positivity, exchange, Theorems S,
D, ZD, Route Z, Identity G) is blind to the difference between the two branches.

### Correction to Step 2, Approach C

My Step 2 estimate bounded the O'Neill term by a Hilbert-Schmidt norm of ad_X. That is wrong as a bound: the vertical
part of a bracket of horizontal fields is D_U G_U b(X, Y) with G_U the Green function of the covariant site Laplacian,
so the term is (1/4) <b, G_U b>, which is unbounded near reducible configurations. The conclusion in kind stands (no
factor beta in the gain, a factor beta in the negative Hessian directions) and the lane has it with numbers: ideas 18
and G2 of `gap-brainstorm2-max.md` (L165, L257), rows 863, 957 (Lemma HESS, curvature test) and 968 (Proposition ANG,
Ricci 2/r^2 at one free link). C was not attacked again.

### Where the attack stands

The crux lemma failed by three routes of mine, each at the order-one band beyond first passage: no seed below the
massless floor (Route 1), a path that still crosses the band and needs a three-dimensional mixing input (Route 2), no
soft exclusion of the gapless branch (Route 3). No counterexample to (U1) or (U2) was found: both are consistent
with a glueball gas (X about |B| t^(-3) for t below the correlation length, exponential beyond it).

## Step 7. Rows 720, 970, 975-986 read; per approach, is it already there

Read in full: rows 720, 970, 975, 976, 977, 982. Read as head plus full RESULT text: rows 978, 979, 981, 983, 984,
985, 986. Row 980 has no result yet (brief only). Also read after the attack: `gap-skeleton-max-b.md` L304-330
(Corollary 4, Lemma HM, the crux (BD) of Route Z) and `gap-skeleton-final.md` L133.

| Approach or route of this file | Already there? | Where |
|---|---|---|
| A, hypercube reduction, (A1)-(A4), (Y-SEED) | YES, all of it, stronger | Lemmas K, X, E, Theorem S (rows 697-699); Theorem D (b), (f); Proposition Delta (row 708, checked 709); Lemma Z, Theorems ZD, ZD-c, Corollary Z4 (row 720); Corollary CU (row 978) |
| B and Route 1, twisted or flux-projected seed, marginal engine | YES | row 720 Part 2: "every step-scaling coupling ... and every twist ratio holds the flux half at most and fails at a point with two confining phases"; P1 of row 712 (14.8 correlation lengths at threshold 1/1650; my 17.04 is the same floor at 1/5041); SMALL-BOX; ideas 8, 15, 31 |
| C, orbit-space curvature | YES | ideas 18, G2 (row 876); rows 863, 957, 968; Theorem QUOT of row 970; the supremum forms are refuted by Theorem D2 (row 977, checked 979) |
| D, purity / Renyi-2 | YES | row 982 Route 2 (d), (e); Lemma RENYI of row 975 (S_2 below 0.439 gives S below 3/10; photon S_2 at least 5.06) |
| E, operator comparison | in kind | Lemmas SVD and VOL of row 975 (a gap alone misses the seed by a volume factor) |
| Z, zeros in complex beta with harmonic measure of a strip | YES, including the width | `gap-skeleton-max-b.md` Theorem LP, Lemma HM, Corollary 4; its line "w_inf = 11/(6 pi) = 0.584 for SU(2) ... |Im(1/g^2)| < pi b_0" is the number I derived again; the periodic torus fails it (zeros of the 4^4 lattice at Im beta 0.18 to 0.22, `gap-skeleton-final.md` L133), which is why Route Z moved to boxes with free walls ((ZF_B), rows 677, 681) |
| G and Route 2, anchor at beta_t = 0 | the anchor NO (greps: "beta_t = 0", "temporal coupling", "anisotrop" over `library/gap-*.md`); the failure YES | idea 32 of row 859 is the opposite line beta_s = 0; the failure (ii) is (NOCRIT) of row 709 on another path, as row 978 found for every carry in the coupling |
| Route 3, exclude the gapless branch | YES | row 720 Part 4: "Carrying the T0 chain past first passage to order-one coupling is the crux itself"; Corollary Z4; K7 = Proposition V of row 708 |

So seven approaches written blind from the object all landed on existing rows. The three routes of row 982 and the
three of this file fail at the same place seen from six sides.

### 7.1 Two small items that I did not find in the lane (each to be checked before any use)

**Lemma ORD (PROVED given two RECALLED classical facts: analytic perturbation of a simple isolated eigenvalue;
a kernel entire in beta with smooth values gives a trace-class-valued analytic family).** For SU(2) Wilson on a
periodic box B with all sides at least 4 and every t >= 1, S(t; B) is analytic in beta near 0 and has a zero of order
at least 4t there. The same
holds in beta_t at fixed real beta_s.
Proof. K_beta = sum over R of rho_R(beta) P_R on gauge-invariant functions, rho_R = product over links of rho_(j_l),
rho_j(beta) = I_(2j+1)(beta)/I_1(beta) with a zero of order 2j at 0. Gauss's law forces the support of a non-trivial R
to contain a closed loop (every site it touches has at least two of its links), of length at least 4 since the sides
are at least 4; so at least 4 links carry 2j >= 1, and K_beta - P_0 = beta^4 N(beta) with N analytic near 0.
T_0 := A P_0 A has rank one with eigenvalue integral e^(-beta V), not 0 near beta = 0, and T_0 (1 - Pi_0) = 0 for its
Riesz projection Pi_0. So T' := T (1 - Pi) = O(beta^4) in trace norm, and S(t) = Tr T'^t / lambda_0^t = O(beta^(4t)). QED

**Schwarz form of the transport (PROVED, classical one line).** Let D be simply connected with 0 in D, phi the
conformal map of D onto the unit disc with phi(0) = 0, and h analytic on D with |h| <= M and a zero of order N at 0.
Then |h| <= M |phi|^N on D. (Apply the maximum principle to h(phi^(-1)(w))/w^N.)

**Consequence (ARGUED; the Borel-Caratheodory step is not written out).** Put G_n := 2 log Z(n, 2n, 2n, 2n) -
log Z((2n)^4) = 2 X(n; (2n)^3) - X(2n; (2n)^3). For real beta, 1 + S(n; (2n)^3) <= exp(G_n) (first line of the proof of
Theorem D (b)). By Lemma ORD, G_n has a zero of order at least 4n at 0. If the two partition functions have no zero
in a simply connected D' that holds 0, then |G_n| <= C n^4 on a smaller D, and G_n(beta) <= C n^4 |phi_D(beta)|^(4n).
So zero-freeness of these two families on one fixed domain gives (SEED) at every real beta in D, with no
strong-coupling expansion (SC) and no bound (BD) as separate hypotheses, and with the Green function of D in place of
kappa_0 times the harmonic measure. This is Corollary 4 of `gap-skeleton-max-b.md` in the limit r_0 -> 0. It does not
revive Route Z on periodic tori: the lane found that the zero-free tube of periodic tori is too thin at weak coupling.
Whether Lemma ORD holds for boxes with free walls, where it could replace (SC_B), was not checked.

## Step 8. Verdicts, marks, what stays open, next step

### 8.1 Verdicts on the row

- Goal (U1) or (U2): NOT proved. No counterexample. Both stay OPEN.
- Approaches from the object: seven written (A, B, C, D, E in Step 2; Z and G during Step 3). Fact tests: Step 3.2.
- Crux attack: the crux lemma (SEED at the unit scale, the consumer of (U1)/(U2)) failed by three routes of mine,
  different from row 982's three: Route 1 at the massless floor, Route 2 at a three-dimensional mixing input and at
  (NOCRIT) on the beta_t path, Route 3 at K7. All three fail beyond first passage, at order-one coupling.
- Rows 720, 970, 975-986: every approach is already there except the anchor of G and the two items of 7.1.
- No numeric run was made. No GUIDE job was needed: no statement here had a cheap refutation test that the lane
  has not run.

### 8.2 Marks

| Statement | Mark |
|---|---|
| (A1)-(A4) of Step 2 | PROVED in the lane (Lemma K, Proposition Delta, Theorem D); ported, not redone |
| Lemma FLOOR (sector form; side times gap above 17.04 at threshold 1/5041) | PROVED (one line; Theorem D (c) read backwards) |
| Identity G (S = 0 at beta_t = 0 for every beta_s; X as an integral over beta_t) | PROVED by hand, not checked |
| One-link influence bound e^(+-4s) of Route 2 (i) | PROVED by hand, not checked |
| Two-level monotonicity of the gap ratio in tau | PROVED (the displayed formula) |
| No level crossing on the beta_t path; band crossed near s of order 1/beta_s | ARGUED / OPEN |
| A volume-free temporal seed at small beta_t for large beta_s | OPEN (needs 3D mixing at weak coupling) |
| Lemma ORD | PROVED given two RECALLED facts, not checked |
| Schwarz form | PROVED (classical) |
| Zero-freeness of two torus families gives (SEED) | ARGUED |
| Exclusion of the gapless branch of Corollary Z4 beyond first passage | OPEN; it is the crux |
| (UNIT), (U1), (U2), (HC-phys), (SEED-phys) | OPEN |

### 8.3 What this run did not cover

Rows 978-986 were read as results, not as files, except the sections of rows 978 and 982 quoted in Steps 1 and 3.
The account was not read here (the family and first passage are quoted from row 982 4.3). Lemma ORD and Identity G
have no check. The first response of the session was lost at the output limit; its work was redone in smaller steps.

### 8.4 Next step (each item is a complete brief)

**N1, check (small).** One line-by-line check, by another model, of Identity G, Lemma ORD and the consequence in 7.1
of `library/gap-unit-max.md`. Write out the Borel-Caratheodory step: with zeta_n := Z/Z(beta = 0), zeta_n(0) = 1 and
log|zeta_n| <= c |beta| Vol on D', show |log zeta_n| <= C Vol on D. Verdict per item: HOLDS, HOLDS AFTER CORRECTION, FAILS.

**N2, for the lead (I may not edit other files).** Do not queue another direction-author row that starts from the
object of (U1)/(U2). Evidence: seven blind approaches here and three routes each in rows 982 and 988 all return
to rows 697-720, 859, 876 and Route Z (row 670). The route "soft, group-blind supplier of the seed" is exhausted. A row on
(U1)/(U2) has value only if it brings an input that tells the Wilson trajectory from K7 beyond first passage.

**N3, port reading (only if Route Z on free-wall boxes is still live, rows 677 and 681).** Read `gap-sc-box.md` and
`gap-zf-box-x.md`. Decide whether Lemma ORD holds for boxes with free walls (is the thermal or winding sum of the box
identically 0 at beta = 0, with a zero of order proportional to the side?). If yes, state the Schwarz form of Theorem
ZB with (ZF_B) as the only hypothesis. If the lane's present (SC_B) already serves every consumer, say so and stop.

**N4, a reading, not a proof row.** For Route 2 (i): search the literature once for a volume-free mixing or
susceptibility bound for three-dimensional SU(2) lattice gauge theory at weak coupling (expected answer: none; it is
the three-dimensional gap problem at fixed lattice coupling). If none, record Identity G as an exact anchor with no
supplier and close the item.

RESULT: Row 988 (Claude Fable 5.2 max, Mac mini worker 1; author, checked by no one; no numeric run; ended 2026-11-15T01:37Z). (U1) and (U2) are NOT proved and no counterexample was found. Seven approaches written from the object before any route file (hypercube reduction, twisted seed with a marginal engine, orbit-space curvature, purity, operator comparison, zeros with a strip, anchor at zero temporal coupling) all land on existing lane material (Theorems S, D, ZD, Proposition Delta, row 720 Part 2 and Part 4, ideas 8, 15, 18, 31, 32, Route Z with its width 11/(6 pi)), except the anchor itself. The crux lemma failed by three new routes, each beyond first passage at order-one coupling: no seed below the massless floor (side times gap above 17.04), a beta_t path that needs three-dimensional mixing and (NOCRIT), no soft exclusion of the gapless branch of Corollary Z4 (K7). PROVED by hand, unchecked: Lemma FLOOR (sector form), Identity G (S = 0 at beta_t = 0 for every beta_s, X as a beta_t integral), Lemma ORD (S(t; B) has a zero of order 4t at beta = 0), the Schwarz form of the Route Z transport (zero-freeness of two torus families gives the seed without (SC); ARGUED in its last step). OPEN: (UNIT), (U1), (U2), (HC-phys), (SEED-phys), and the one input every route lacks, the exclusion of a gapless scale-invariant branch beyond first passage. Next: N1 check of the three small items; N2 the lead should not queue another direction row on (U1)/(U2) without an input that separates the Wilson trajectory from K7.
