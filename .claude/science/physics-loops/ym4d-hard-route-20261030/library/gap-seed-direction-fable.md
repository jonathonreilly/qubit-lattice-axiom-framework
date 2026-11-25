lead: anthropic/claude-fable-5-2/high mac-mini-worker
lease_until: 2026-11-25T16:32Z

# gap-seed-direction-fable (queue row 1515): direction for the physical seed after rows 1510 and 1511

Status: IN PROGRESS. Research-stage working state; nothing here is a public claim. Unchecked.
Pinned at commit c4db00930 on branch claude/ym4d-hard-route. Started 2026-11-25T04:32Z (date -u).

## 0. Plan (written first, per the save protocol of the row)

Task of the row: from the target (PUR-io) and the results of rows 1510 (`library/gap-seed-solve-fable.md`)
and 1511 (`library/gap-seed-solve-astra62.md`), find the attack that could still succeed, or prove that every
attack of an explicitly stated family fails. Decide what kind of input the calibrated obstruction of row 1511
still allows:

- (a) scaling of the action insertion,
- (b) cancellation between signed seam responses,
- (c) rates integrated over shrinking coupling intervals,
- (d) an in-law carry as in row 1510 (PC, REV),

and whether any of these has a first lemma that is not equivalent to a closed line.

Steps, each appended as its own section when done:

1. Read rows 1510 and 1511 in full; restate (PUR-io), the refutation of (W), criterion (3) and the calibrated
   obstruction in the exact form used below, with line anchors.
2. Formalize the family of attacks the obstruction covers, and state precisely what it leaves outside.
3. Test each of (a)-(d) against the obstruction and against the closed lines (grep `library/open-core.md` and
   the FINISH rows before calling anything new).
4. Decisive outcome: one named attack row with its first lemma, or an obstruction theorem over a stated family,
   or the statement that no such row exists on present knowledge, with triggers.
5. Next two rows with their decisive outcomes.

## Status log

- 2026-11-25T04:32Z file created with plan; no reading done beyond the queue row and GOAL.md.
- 2026-11-25T04:39Z read rows 1510 and 1511 in full, FINISH rules, row 1496 Sections 2-4, row 708 Section 4 (L112-200), row 1461 first lemma and (1)-(2). Section 1 written.
- 2026-11-25T04:49Z Section 2 written (Lemma B, Proposition WIN, integrated form of input (a)). memory_pressure read 36 percent free: no numeric job in this row.
- 2026-11-25T04:51Z Section 3 written (inputs (a), (c) = row 708 transport; (VIR-top) named, no row).
- 2026-11-25T04:51Z Section 4 written (input (d): obstruction does not reach it; source missing).
- 2026-11-25T04:52Z Section 5 written (criterion (3): no consumer, no method; two hand probes).
- 2026-11-25T04:52Z Section 6 written (verdict of the third kind, triggers (R11), (R12), next two rows).
<!-- LOG-MARKER -->

## 1. The target and the two results, in the form used below (read; nothing new here)

Written 2026-11-25T04:39Z (date -u). Labels: **proved** (a written proof is in this file), **read** (read in a row, not
re-derived), **sketched**, **guessed**, **guide** (heuristic size, never a proof step).

### 1.1 Target (read: row 1468 3.1, checks 1462, 1465; row 1511 "Physical target")

n = l b^K, u = n/512, T the Wilson transfer operator on the spatial torus n^3 at the least-root coupling
beta_K(g_0), Z_+(v) = Tr(P_0 T^v), P_K = Z_+(2u)/Z_+(u)^2. **(PUR-io):** P_K >= 457/625 at infinitely many K
for one l and one g_0.

### 1.2 Three exact forms of the same number (read; elementary)

With r_i the neutral eigenvalue ratios and s(v) = sum of r_i^v:

- (E1) -log P_K = 2 log(1 + s(u)) - log(1 + s(2u)).
- (E2) -log P_K = 12 u n^3 * integral over t in [0, beta_K] of (x_u(t) - x_2u(t)) dt, where x_v(t) is the
  mass-weighted mean plaquette of the n^3 x v tori at coupling t (the proof of (4) in row 1511; rows 1461
  and 1465, Step 6; P(0) = 1).
- (E3) the same with the infinite-time torus as reference: d/dt log(1 + s(v)) = 6 v n^3 (x_v - x_inf)
  (row 708, `gap-mid-max.md` Lemma 4.1, L112-116, in that row's sign convention).

### 1.3 Row 1511 (gpt-6.2-astra; unchecked, check 1514 running)

- **(W) refuted.** Bound (1): delta >= 3 [1 - ((R-1)/(R+1))^3] m_beta. At beta = 23/10 and side four it
  forces delta > 392/225. Every cube with R <= 10 fails at every beta >= 23/10.
- **Criterion (3).** With the cost counted modulo vertex gauges on the cube, C_i < N_R + b_i gives decay of
  gauge-invariant correlations with rate lambda and prefactor 2 N_R |Y| |V| e^(lambda (R+2)) / L. At R = 4
  the test is C_i < 1350: the sum of 796 excess costs below 554. Open.
- **Bound (4).** Under a common margin on [0, beta_K]:
  -log P_K <= 768 beta_K u n^3 N_R |V| e^(-lambda D) / L, D = (u/2 - R - 4)_+.
- **Calibrated obstruction.** (i) Rate bound: an actual uniform periodic covariance rate lambda_K at the
  least roots has lambda_K b^K bounded (reflection positivity removes the prefactor; the positive separated
  two-point witness of row 1461 forbids an unbounded physical rate). (ii) Hence the right side of (4), and
  every majorant bounded below by a_K e^(-c lambda_K n) with a_K -> infinity, diverges at the calibrated
  roots. Its last paragraph names three features a physical comparison could use: the scaling of the action
  insertion, cancellation between the signed seam responses, rates integrated separately over shrinking
  coupling intervals.

### 1.4 Row 1510 (mine; unchecked, check 1513 queued)

Proposition PC (a weighted Poincare inequality passes fine to coarse through one Q2 step, in law), Lemma REV
(coarse to fine, given (H1), (H2) for the posterior), Corollary NF and Theorem NB (weak steps give every
family a Poincare constant above 3/2 and keep the sixteen masses), and the unproved (FL). Its own verdict:
PC and REV both transport a gap; neither makes one.

### 1.5 First reading (the dictionary that the rest of this file uses)

(E2) is the transport of the thermal sum along the coupling on a fixed lattice. This is on file: row 708
(`gap-mid-max.md` Section 4: Lemma 4.1, Theorem TR, (VIR_K), Remark LEV, (DEF_K), (VIR-log)), with the
verdicts "three ways failed" (its 4.4) and "the trace anomaly has no lattice form" (its 4.5); the table of
row 1380 (`gap-mech-direction2-fable.md` L258) lists it as blocked-equivalent; row 1496 4.1 lists "integration
along beta at a fixed lattice" as equivalent to a closed line. So row 1511's (4) is one bound for the
integrand of row 708's transport, and the three features named in 1.3 are three ways to bound that
integrand. Sections 2-4 test them one by one against row 708, and Section 5 tests the in-law carry.

## 2. The seam family, and what the calibrated obstruction forces

Written 2026-11-25T04:49Z (date -u).

### 2.1 Definitions

- **Single response.** For the lattice n^3 x v at coupling t put R_v(t) = d/dt log(1 + s(v; t)). By (E3),
  R_v = 6 v n^3 (x_v - x_inf). With E_i = -log r_i and V_i = -dE_i/dt (the velocity of the level i), where the
  levels are differentiable: R_v = v * sum_i V_i r_i^v / (1 + s(v)), the thermal mean of the velocities
  (Hellmann-Feynman; row 708 Remark LEV). The integrand of (E2) is D = 2 R_u - R_2u.
- **Seam majorant.** For K in an infinite set, a measurable M_K >= 0 on [0, beta_K] with D_K <= M_K. Then
  -log P_K <= integral of M_K.
- **Product form.** M_K(t) = 12 u n^3 A_K(t) e^(-c lambda_K(t) u), with a fixed c in (0, 1], a per-plaquette
  prefactor A_K(t) >= 0, and lambda_K(t) <= lambda*(t). Here lambda*(t) is the supremum of the rates for
  which the Wilson laws at coupling t on all large periodic cubes obey a bound of the kind (3), with any
  prefactor that does not depend on the separation or on the cube (the hypothesis of row 1511's rate bound).
- Row 1511's (4) is the product form with c = 1/2, a constant rate and the constant prefactor
  A = 64 N_R |V| e^(lambda (R+4)) / L.

### 2.2 Lemma B (the long seam is at most a factor 2). Proved; elementary.

For every lattice with u even and every coupling: log(1 + s(u)) <= -log P <= 2 log(1 + s(u)).

Proof. By (E1), -log P = 2 log(1 + s(u)) - log(1 + s(2u)). The ratios r_i are real with |r_i| <= 1 and u is
even, so 0 <= r_i^(2u) <= r_i^u and 0 <= s(2u) <= s(u). QED (u = n/512 is even because l is a multiple of
1024.)

Consequences. (i) (PUR-io) follows from log(1 + s_K(u)) <= (1/2) log(625/457) at infinitely many K, and it
implies log(1 + s_K(u)) <= log(625/457) there. So the target is the one-torus thermal sum, as rows 1367,
1386 and 1496 say. (ii) log(1 + s(u; t)) = integral of R_u over [0, t] is non-negative for every t. So the
number to bound is one positive integral of one response. (iii) The eight twists enter Z_+ with positive
weights (row 1511, proof of (4)). So **input (b), cancellation between the signed seam responses, can
change a bound by at most a factor 2 at the integrated level.** It is not an independent input. A sign
change of R_u along t would be a different effect. In the scaling picture R_u is positive (guide: every
level falls as the spacing falls), and I know no statement that uses a negative part.

### 2.3 Proposition WIN (the forced scaling on the top window). Proved in case (i); conditional in case (ii).

Let W_K = [beta_K - w_K, beta_K] with w_K > 0, and let a seam majorant have the product form on W_K. Assume

    (RB-win)   lambda*(t) u <= H for every t in W_K and every K of the set, with one finite H.

If the integral of M_K is at most log(625/457), then

    integral of A_K over W_K  <=  log(625/457) e^(cH) / (12 u n^3)  =  C(l, H) b^(-4K).

Proof. M_K >= 12 u n^3 A_K e^(-cH) on W_K, and M_K >= 0 elsewhere. QED

(i) **Unconditional case: a common rate on a terminal interval.** If lambda_K is constant on W_K (a common
margin on an interval that ends at beta_K, as in (4)), then lambda_K <= lambda*(beta_K). Row 1511's rate bound
gives sup over K of lambda*(beta_K) b^K < infinity (if it were unbounded, a subsequence would contradict that
bound). So (RB-win) holds with H = (l/512) times this supremum. Hence: **a majorant with an absolute
prefactor A_K >= A_0 > 0 needs w_K <= C b^(-4K)/A_0.** A terminal interval with its own rate must shrink
like the fourth power of the spacing. The next interval then ends at a coupling that is not a root, which
is case (ii).

(ii) **General case.** (RB-win) on a window of fixed width is not proved here. It asks for the rate bound
of row 1511 at every coupling of the window, not only at the least root of one level. Row 1461's (2) puts
the largest roots of all levels r in a closed interval I inside |beta - B_K| <= C_I. A rate bound that is
uniform in r in I would need the positive separated witness uniformly in r, that is, the release's bounds
on a compact set of levels. I did not read that. Guide: the rate at coupling t is m a(t) with the same
physical mass, so lambda*(t) u is of order (m l / 512) e^(kappa (beta_K - t)), bounded on every window of
fixed width.

**Reading.** Under (RB-win) on a window of fixed width, the mean of the per-plaquette prefactor over the
window is O(b^(-4K)). The rate cannot supply this factor (it is bounded by lambda*), and by Lemma B the
second seam cannot. So of the three features that row 1511 names, **(a) is forced, and (b) and (c) cannot
replace it.** Input (c) alone, a separate rate on each coupling interval with absolute prefactors, fails:
the couplings with lambda*(t) u <= H' fill the top levels (guide: about log_b of H' levels), and there the
prefactor u n^3 has nothing against it.

### 2.4 What input (a) is, in integrated form (proved from Lemma B; the reading is argued)

By Lemma B, sup over K of -log P_K is finite if and only if

    (UV-TS)   sup over K of s_K(u) < infinity   (the neutral thermal sum of the physical box of side l at
              the physical temperature 512/l is bounded in the cutoff).

So a per-plaquette prefactor of order b^(-4K) with no further small factor gives exactly (UV-TS). That is an
ultraviolet statement, of the kind of CT4 in `GOAL.md` (free energies of tori compared up to a constant per
unit of physical volume). (PUR-io) implies it along its sequence. It does not imply (PUR-io): it bounds
P_K below by a positive constant e^(-C(l)), and Fact PUR needs 457/625. I did not find (UV-TS) under the
greps "thermal sum is bounded", "bounded in K", "trace class uniformly" in four lane files; I do not call it
new, I do not prove it, and nothing below needs it.

The number that (PUR-io) needs beyond (UV-TS) is the infrared factor. Guide: with a(t) the spacing at
coupling t and T(t) = 1/(u a(t)), R_u(t) dt is 512^3 Theta(T) d log T with Theta the thermal mean of
energy over temperature per unit of T^3 volume, and log(1 + s_K(u)) is 512^3 times the integral of Theta
over the temperatures below 512/l. This is the integral method of lattice thermodynamics (Engels, Fingberg,
Karsch, Miller and Weber; Boyd and others; recalled, not read). The target asks for a value of order 1e-10
of this integral, which is m l of order 1e4 (row 1510, guide).

## 3. Inputs (a) and (c) together are the transport of row 708

Written 2026-11-25T04:51Z (date -u).

### 3.1 The coupling integral, root by root (proved; a relabelling)

Write Lam_d(l') for log(1 + s) of the seed lattice of side l' at depth d: the lattice of side l' b^d and time
l' b^d / 512 at the coupling beta_d(g_0). Put Lam_(-1) = 0 (coupling 0). The lattice of (E2), n = l b^K, at
the coupling beta_(K-j) is the seed lattice of side l b^j at depth K - j. So

    log(1 + s_K(u)) = Lam_K(l) = sum over j = 0..K of [ Lam_(K-j)(l b^j) - Lam_(K-j-1)(l b^(j+1)) ],

and the bracket j is the integral of R_u over the root interval from beta_(K-j-1) to beta_(K-j). (The sum
telescopes whatever the order of the roots.) So a bound for the integrand on the root interval j is a bound
for the difference between two seeds with the same number of sites: side l b^j at depth K - j, and side
l b^(j+1) at depth K - j - 1.

### 3.2 Where the weight sits: one root interval (the identity is proved; the bound on its first term is read)

Cut the sum of 3.1 after j = 0:

    Lam_K(l) = Lam_(K-1)(l b) + integral of R_u over the last root interval, from beta_(K-1) to beta_K.

- The first term is a seed-type quantity at one fixed coupling, beta_(K-1), on a box that is b times larger
  and b times colder than the seed box of side l at depth K - 1. The lane's fixed-coupling volume theorems
  are the tools that bound it by that seed (Theorem SH of row 705 and Proposition Delta of row 708, as
  quoted in `gap-mid-max.md` 4.3; read there, not re-derived, and I did not check their constants at the
  aspect 512; guide for the size: of order b^3 times the b-th power of the seed value). No integral over couplings is needed
  for it. So **input (c) is not needed below the last root interval**: where a seed is known one depth
  earlier, the rates on all lower coupling intervals are already used, at fixed coupling.
- All the weight is in the second term: the transport over one root interval on a fixed lattice, from the
  cold box (side l b at depth K - 1) to the seed box (side l at depth K). The thermal sum must rise there,
  from about the b-th power of the seed value to the seed value. The lemma has to bound that rise. This is
  one "step" of row 708 4.5.
- Without a seed one depth earlier the same cut can be made at any earlier root, and the first term is then
  a seed-type quantity at an order-one or strong coupling. At strong coupling it is proved (row 708,
  Corollary TR1; the end class of rows 1471, 1473). In the band it is the gap of the bare lattice model,
  which is open (Section 5).

### 3.3 The forced form of the first lemma is relative, and it is (VIR_K) (read: row 708 4.2-4.5; the step from Section 2 is argued)

By 3.2 a lemma for the last root interval must bound R_u(t) by a number of the size of the thermal sum at
the same coupling. An absolute bound (a prefactor times a rate factor, as (4)) can do that only if its rate is
the physical rate at that coupling and its prefactor has the scaling of 2.3. A physical rate at the
coupling t on this lattice is the gap of the box of side l a(t)/a(beta_K) >= l. That is the seed at a
larger side, the target again (the seed may choose its side). So an absolute bound is circular on the last
root interval, with or without scaling.

The only form that is not circular is a relative one: a bound for the response by the thermal sum at the
same coupling, which a continuity argument along t can close. That is exactly hypothesis (VIR_K) of row
708, in this file's notation

    R_v(t) <= - K(t) v (d/dv) log(1 + s(v; t)),

"the thermal mean of the level velocities is at most K times the thermal mean of the energies". Theorem TR
of row 708 turns it into: the thermal sum does not grow along the curve v(t) = v_0 exp(integral of K). With
K equal to the scaling rate this compares one physical temperature on boxes of growing physical side, so
no infrared factor is lost; this is what "scaling of the action insertion" must mean to be usable.

State of (VIR_K) on file: three ways failed (row 708 4.4: the pointwise operator inequality is false by the
published scaling values, locality gives a volume factor, convexity is refuted by the Ising member of the
class); the exact open statement is (VIR-log); row 708 4.5: a hand proof of one coupling step "needs an
identity that produces the ratio", the trace anomaly, and "the lattice has no dilation"; the table of row
1380 marks the line blocked-equivalent (registry RB); row 1496 4.1 repeats the verdict. Row 1511's objects
do not change this: (3) and (4) are absolute bounds at lattice resolution, and by 2.3 an absolute bound
needs the forced scaling before it can even be finite.

**The continuity argument with an absolute bound, done once (argued; elementary calculus).** Take the rate
from the seed at the same coupling, which is not circular: while y(t) = log(1 + s(u; t)) stays below eps on
the last root interval, the box has the lattice gap E_1 >= (1/u) log(1/y), and I grant the same number as
the covariance rate on all large cubes (the best case). A scaled absolute bound then reads
y' <= Q (y)^c with Q = 12 u n^3 A = (12 l^4 / 512) C_A, where C_A = A b^(4K) is its scaled constant in
reference units, and c <= 1 is its exponent factor (1/2 in (4)). Start: y is about eps^b at beta_(K-1).

- c < 1: the inequality allows y to reach eps after a coupling length eps^(1-c) / ((1-c) Q). The root
  interval has length of order one. So nothing is proved.
- c = 1: y <= y_0 e^(Q s) over an interval of length s. This stays below eps only if
  (b - 1) log(1/eps) >= Q s, that is C_A <= (512 (b - 1) / (12 s)) log(1/eps) / l^4. With log(1/eps) of
  order m l / 512 (guide) this is C_A of order m / l^3 at most: the per-plaquette prefactor must be as small
  as one mass spread over the box. A constant from ultraviolet stability is of order one per unit of
  reference volume. So the bound that closes is again a relative one.

### 3.4 The two places where a first lemma could sit, and why neither is a row

1. **(VIR_K) on a window of order-one couplings.** This is the closed line of row 708. Nothing in rows 1510
   or 1511 supplies a relative bound.
2. **(VIR-top): (VIR_K) on the last root interval at weak coupling**, with the integral of K at most log b.
   It says: the thermal sum of the physical box of side L at temperature T at depth K is at most that of
   the box of side b L at the same T at depth K - 1. The room is a factor of about b^3 in the thermal sum
   (guide). So it asks that the low masses converge in the continuum limit with a relative error of order
   T/m per step, which is an ultraviolet statement about an infrared quantity. It is not on file under
   this name. It is a carry at weak coupling: it gives the seed at depth K from a seed-type statement at
   depth K - 1 with aspect 512 b. Iterated, it stops at the release floor, above the band. So it has the
   standing of T1 in row 1496 Section 3: no consumer until the band is crossed, not selective, not in
   doubt in kind. I do not propose it as a row.

So inputs (a) and (c), alone or together, have no first lemma that is new against row 708 and that has a
consumer.

## 4. Input (d): the in-law carry of row 1510

Written 2026-11-25T04:51Z (date -u).

### 4.1 The calibrated obstruction does not reach it (read and argued)

The obstruction of row 1511 is about majorants of -log P. A route that ends in a rate does not need the
purity. Two facts on file give this:

- the diagonal reflection-positive argument inside row 1511's rate bound removes any prefactor that does
  not depend on the separation; and
- `gap-os-equiv.md` statement (5): one common rate passes to the limit, and "no bound on the constants is
  used".

So the gap in the calibrated limit follows from

    (RATE-io)  at infinitely many K, a uniform periodic bound of the kind (3) for the Wilson law at beta_K
               with rate lambda_K >= m_0 b^(-K), m_0 > 0, and any prefactors,

without (PUR-io) (read; I did not re-derive (5)). This is (A1) in rate form, trigger (R3); it is not new.
The in-law route FI of row 1510 aims at a statement of this kind: a weighted Poincare inequality with
physical constant, then decay (its 4.2 (iii), open). So the absolute prefactor that kills (4) is harmless
for input (d). The obstruction leaves one more fact for any route to (RATE-io): by its last display,
(B_R - C_*)_+ = O(b^(-K)), a criterion on a block of fixed lattice size has no margin at the roots. The
margin of a block of physical size is the gap itself.

### 4.2 What stops it is the source (read: row 1510 3.5, 4.2; nothing new)

PC carries a weighted inequality from fine to coarse, REV from coarse to fine given (H1), (H2). Both
transport a gap. The source at the coarse end is the blocked action at small readout, T2 of row 1474, a
closed line. The first unproved lemma (FL) is a carry at order one, formally weaker than (TILT-COV-sup),
not shown easier, and after it three parts stay open (source, joint moments, decay from a weighted
inequality). Rows 1512 (literature) and 1513 (check) are queued on it. This row adds nothing to (FL) and
proposes no build row for it.

### 4.3 One structure for all four inputs (argued)

Each of (a), (b), (c), (d) is a carry: it relates the seed, or a rate, at one pair (depth, side) to the
same kind of statement at another pair, or to a blocked family. None is a source of infrared smallness.
The only proved source in the lane is the strong-coupling end (the end class at beta <= 0.00872, rows 1471
and 1473; the strong-coupling seed of row 708). The open part is the same in every representation: the
carry across the band of order-one couplings, as the Q2 chain (rows 1468, 1496 2.4), as (VIR_K) (row 708),
as (FL) with T2 (rows 1510, 1474), or as a finite-block criterion ((W), refuted for R <= 10 by row 1511;
(3), Section 5).

## 5. The one new finite object: criterion (3) at side four

Written 2026-11-25T04:52Z (date -u). Row 1511 proposes as its second row to decide whether the sum of the 796 excess
costs stays below 554 on [0, 23/10]. I tested what either outcome would move.

### 5.1 A pass has no consumer (read and argued)

A pass gives decay for bare Wilson at every coupling up to 23/10 and, by (4), purity on large boxes at a
fixed bare coupling. It would be a strong theorem about the bare lattice model. For the target:

- In the transport of row 708 it moves the source from beta_0 <= 1/25600 to 23/10. The carry from 23/10 to
  the roots is (VIR_K) on [23/10, beta_K], with no small parameter up to the release floor (rows 1464, 1470;
  row 1496 2.2 item 2). That carry is the closed line of Section 3.
- In the Q2 chain a gap of bare Wilson at 23/10 is not on the trajectory: the chain needs the blocked
  family at readout 2.3 (row 1496 4.2, last bullets).
- At the roots the criterion has no margin: (B_R - C_*)_+ = O(b^(-K)) (row 1511).

### 5.2 A fail changes nothing

(3) at R = 4 with unit costs is one member of a family (sides, costs). A fail closes that member, as (1)
closed (W) for R <= 10.

### 5.3 Neither direction has a method (sketched; not decided)

- Pass. C_i is a supremum over all boundary values of an optimal transport cost on 2000 links. This is
  kind B of row 1496 4.1: no certificate of feasible size (guessed). By hand it needs couplings for
  worst-case boundaries at a coupling where the one-link sums are above 1 (the hand range of row 691).
- Kill, two probes tried by hand. (i) The centre probe of (1) gives nothing here. Flipping all normals at a
  vertex is a gauge move on S, so its aligned cost is zero and the triangle inequality bounds nothing from
  below. For the layer set L_x, the completed arrays before and after differ by centre gauges at x and at
  its outward neighbours; the mixed plaquettes are invariant, so every function of them has the same mean.
  (ii) Row 1511's anchored path gives c_z - 1 >= the total variation distance of two tilts of one path
  law pi. For the pair z = g, -g and pi = Haar this distance is m_beta, which is about 0.755 at 23/10 (guide: the
  ratio of the two hand series of row 1511, 1.5836/2.0978; row 1511 proves m > 20/27). On all 600 layer
  links of one direction that gives about 453, below 554.
  The distance can be larger for a path law with two modes, and smaller for a concentrated one; I have no
  proved lower bound for the supremum over the boundary. A kill would need the second shell (neighbouring
  anchored paths) and the 196 normals at vertices on several faces, each with a proved lower bound for a
  conditional law at order-one coupling.

So I do not recommend row 1511's second row: no method in either direction, and no outcome that changes a
decision. It returns to the path if trigger (R12) below fires.

## 6. Verdict, triggers, next two rows

Written 2026-11-25T04:52Z (date -u).

### 6.1 Decisive outcome: of the third kind

**No attack row exists on present knowledge.** For each input that the calibrated obstruction of row 1511
leaves open, the first lemma is a closed line or a carry without a source:

| Input | What it is, exactly | First lemma | Standing |
|---|---|---|---|
| (b) cancellation between the signed seam responses | At most a factor 2 in -log P (Lemma B, proved); twists have positive weights | none | Not an input. |
| (c) rates integrated over coupling intervals, absolute prefactors | Not needed below the last root interval: given a seed one depth earlier, the fixed-coupling volume theorems give that part (3.2). On the last interval it fails: a terminal interval with its own rate must shrink like b^(-4K) (Proposition WIN (i), proved from row 1511's rate bound); on a window of fixed width it fails given (RB-win) (not proved) | none | Closed by row 1511 with WIN, up to (RB-win). |
| (a) scaling of the action insertion | Forced (WIN). Integrated with no decay factor it is (UV-TS): ultraviolet, bounded and not small (2.4). With the decay factor it must be relative | (VIR_K) on an order-one window, or (VIR-top) at weak coupling | (VIR_K): closed line, row 708, registry RB. (VIR-top): a weak-coupling carry with no consumer, standing of T1. |
| (d) in-law carry (PC, REV) | Not reached by the obstruction: its consumer is a rate, (RATE-io), with any prefactor (4.1) | (FL) | A carry at order one with no source; the source is T2 of row 1474, closed. Rows 1512, 1513 are on it. |
| Criterion (3) at side four | A finite test with a supremum over boundary values | the excess sum below 554 | No method either way, no consumer (Section 5). |

This is a judgment over the four inputs that the row names and the lines on file. Lemma B and Proposition
WIN (i) are proved here; the rest is read or argued. It is not a theorem over all attacks.

What rows 1510 and 1511 changed, in one line each: row 1511 removes the Hamming block criterion for
R <= 10 and every absolute seam bound at the roots; row 1510 removes classes of normalized measures and
gives the carry calculus without a supremum. Neither supplies a source or a relative bound.

### 6.2 Triggers added (the list (R1)-(R9) of row 1496 4.4 and (R10) of row 1510 stand)

- **(R11) A relative transport bound at one coupling of order one.** For Wilson SU(2) in four dimensions
  and one coupling t in the band: R_v(t) <= -K v (d/dv) log(1 + s(v; t)) on a sequence of boxes of side n
  with K growing more slowly than log n ((VIR-log) of row 708 at one coupling), by a method that fails for
  the Ising member of row 708 4.4 across its transition and for compact U(1). Or a published identity that
  plays the part of the trace anomaly at finite spacing with a relative error of order one.
- **(R12) A consumer for a gap of bare Wilson at a coupling of order one.** A proved carry from a coupling
  t_1 >= 2 to the release floor, on the bare trajectory. Then criterion (3), or any finite test at
  t <= t_1, gets a row.

Registry lines proposed for the lead (not written by me): "seam majorants with an absolute prefactor:
closed at the roots (row 1511; this row 2.3)"; "seam bounds with the forced scaling: equal to registry RB
(row 708)"; "cancellation between seam responses: not an input (Lemma B)".

### 6.3 The next two rows and their decisive outcomes

I propose no attack row and no build row.

**Row 1, `gap-seed-direction-fable-check-astra62` (cross-provider check of this file; gpt-6.2-astra).**
Order: (i) Lemma B; (ii) Proposition WIN (i): that a common rate on an interval ending at beta_K is a rate
at beta_K, and the use of row 1511's rate bound, read together with the verdict of check 1514 on that
bound; (iii) the relabelling 3.1 and the claim of 3.3 that the forced form is (VIR_K), against row 708
Lemma 4.1 and Theorem TR; (iv) 4.1: the exact hypotheses under which `gap-os-equiv.md` (5) and the
prefactor removal give the gap from (RATE-io); (v) try to name a seam input outside (a)-(d), or a relative
bound that is not on file. Decisive outcome: if it holds, the three registry lines and triggers (R11),
(R12) are entered and row 1511's second row is not queued. If (v) finds an input, that input is the next
direction row. If check 1514 rejects row 1511's rate bound, WIN (i) falls with it and Section 2.3 is
re-read; Lemma B and Sections 3-5 do not depend on it.

**Row 2, `gap-seam-window-rate-astra62` (a short proof row; held until Row 1 and check 1514 report; low
priority).** Prove or refute (RB-win) from the release: for a closed interval I of levels and late K, the
rate bound of row 1511 holds uniformly at the largest roots beta_K(r), r in I; state which couplings of
the window |beta - B_K| <= C_I this covers and their measure (row 1461's last-crossing integral).
Decisive outcome: proved, and Proposition WIN (ii) is a theorem on the covered set, so input (c) is
closed as a theorem; refuted or stuck, and it names the first bound of the release that is not uniform
in the level. The direction verdict of 6.1 does not depend on this row, so the lead may skip it.

<!-- APPEND-MARKER -->
