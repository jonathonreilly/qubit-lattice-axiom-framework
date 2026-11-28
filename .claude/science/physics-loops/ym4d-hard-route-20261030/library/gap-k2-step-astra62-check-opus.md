# Check of row 1650 (library/gap-k2-step-astra62.md), FINISH.md row 1651

Checker: Opus 5.5 (Claude Code subagent). Started 2026-11-27.

## Log

Sources read in full: `library/gap-k2-step-astra62.md` (row 1650, 246 lines); FINISH.md rows 1648-1651.
Read in part: row 1386 file section 4.4-4.5 (K-I, K-II, filter); row 1553 file sections 1.3-1.5 (P-law, Lemma ALG,
(g1)-(g6)); check 1648 RESULT; row 1468 file section 3.1 (consumer, Fact PUR); check 1527 part (ii) (thresholds above 1/2).
Not read: `library/gap-direction8-fable.md`.

Method. By hand, line by line. Arithmetic re-done a second way: an exact rational script (Python `fractions`, one
process, a few MB) at `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-peaceful-heisenberg-e2d2a0/b3f5c21a-8638-4944-b69d-c639619895d6/scratchpad/chk1651/cum2.py`.
It uses the moment-cumulant recursion and power-series division, not the set-partition sums of the file. It is exact but
it is not Lean-checked, so it is a guide here, not a proof step. Its output agreed with every number below.

## 1. The PROVED items, line by line

### 1.1 Block map (2), grouping rule, and consumer (4): HOLDS

- (1)-(2). f'(D') = f(q^{-1}D'). A subset A is in q^{-1}D' iff qA is in D'. So f'(D') = sum over H in D' of
  (sum over qA = H of a(A)). Moebius inversion is unique, so (2) follows. It is correct, and it is an identity of
  bookkeeping. The pushforward to coarse gauge fields (line 32) is not used by (2) or by (4).
- Normalization by the one-plaquette integral cancels in P_K: Z(2u) has twice the plaquettes of Z(u). Twisted
  plaquettes have the same one-plaquette integral (Haar is invariant under U -> -U). HOLDS.
- Contraction line 53: V_{j+1} = sum_H |sum_g sum_{A in g} a_j(A)| <= sum_g |P_g - N_g| = V_j - 2 sum_g min(P_g, N_g).
  Long is defined on the final clock, so the fibre of a long H holds only long A. HOLDS.
- Short supports. A fine support with short image lies in a non-wrapping time slab (arc < m/4 + one fine slice < m/2).
  The twist seam moves out of the slab by a centre change on spatial links between two time cuts (temporal plaquettes
  at the two cuts change sign; spatial plaquettes keep both flips). So every Z(D), D in A, is the slab integral. It is
  twist-free and the same on both periods. Each short support at m has exactly two short lifts at 2m. HOLDS.
- (4): log Z^z(u) in [s - eps, s + eps], log Z^z(2u) in [2s - eps, 2s + eps], so P_K >= e^{-3 eps} = e^{-1/4} > 3/4 >
  457/625. HOLDS. Early exit when V_j <= 1/12: HOLDS (triangle inequality).

### 1.2 Ribbon coefficient (5)-(6): HOLDS

- Peeling. A partial sheet loses every face: from a hole, each face across a non-boundary edge has a link in one active
  face only, and integrating it gives 1. The dual graph is connected. For each i not in J the sum over proper subsets of
  S_i of (-1)^{|S_i| - |D_i|} is -1. This gives (5). HOLDS.
- Kernel (6). Area-only annulus kernel sum_l r_l^a chi_l(g) chi_l(h)-bar, by the standard Haar sewing. The kernel is a
  class function of the two Polyakov loops, so Haar on the temporal links gives Haar on g, h. HOLDS.
- Twist. The three twist planes x_i = 0 can be moved by temporal-link centre changes at the seam time. A plane that misses
  the spatial ball touches no sheet plaquette. HOLDS.
- Bulge geometry, checked by coordinates: the cube faces at y = 1, z = 0, x in [2, 3] miss all rails, the sixth path
  (at (y, z) = (1, 1)) and each other (slots t and t + 2 use times t, t + 1 and t + 2, t + 3). Each edge is in exactly two
  faces of its sheet. HOLDS. Note: a(A) depends only on Z(D) for D in A. So every coefficient in (5)-(13) is a quantity
  of one support with every other plaquette off.

### 1.3 Asymptotic (7): HOLDS

- Ratio facts: I_{j+1}/I_j = E[t] under density e^{beta t}(1 - t^2)^{j - 1/2}. The tilt by (1 - s^2) and the increasing
  s tanh(beta s) give decreasing adjacent quotients. So r_1 <= Q and r_j / r_1 <= Q^{j-1}. The bound
  1 - Q >= c (1 + beta)^{-3/2} is valid (weaker than the true 1/(2 beta), which is fine). HOLDS.
- Leading term: the squarefree coefficient of log E prod(1 + x_i Y_i) is the joint cumulant. All Y_i equal Y to
  O(Q^{a_*}), so it is the k-th cumulant of Y. Relative error O(max x_i) <= O(Q^{a_*}). HOLDS.
- Numbers. SU(2): m_2, m_4, m_6 = 1, 4, 25 (Catalan squared); kappa_4 = 1, kappa_6 = -5. U(1): Y = 2 cos(phi), phi
  uniform; m = 2, 6, 20; kappa_4 = -6, kappa_6 = 80. Script: same. HOLDS.

### 1.4 Five-plus-one cancellation (8): HOLDS

- Lengths 4, 8, 8, 8, 8, 12 and 4, 8, 8, 28; totals 48; internal disjointness; one spatial B-cell; same orientations
  tx, ty, tz at all fine times; xy labels fixed by E. So qA is the same for all six. HOLDS.
- SU(2): 5(1) + (-5) = 0, absolute 10. U(1): 5(-6) + 80 = 50, absolute 110, ratio 5/11. Error O(Q^{4v}) since
  a_* >= 4v. HOLDS as a computation on this group of six.

### 1.5 (9) and (11): HOLDS

- (9): sum over E of r_1^{48v + 4|E|} = r_1^{48v}(1 + r_1^4)^{floor(v/2)}. On beta_K ~ log n, 48 log r_1 -> 0 and the
  growth rate per slice tends to (log 2)/2. (7) applies since v / beta_K^{3/2} -> infinity. HOLDS.
- (11): groups G(E) are disjoint and lie in one fibre; all other supports stay singletons; the triangle inequality gives
  the gain. HOLDS. It is a lower bound on the numerator of (3) only, as the file says.

### 1.6 Residual (10): HOLDS

- Parity: g -> -g flips every t_i, so only even total degree survives. Relative degree 2 needs t_0^3 (or t_0^2 t_i^2,
  which is o(1) since x_i / x_0 <= r_1^{2v}). Harmonics j = 2, 3 on the direct path carry b_{0j} <= (q_2/q_1)^{a_0} -> 0
  (on beta_K ~ log n because v / beta_K -> infinity; on [2, 3] by compactness). HOLDS.
- Tilted cumulants (m'_j = m_j + t_0 m_{j+1}): kappa_3' = t_0 + 2 t_0^3; kappa_5' = -5 t_0 + 20 t_0^3 + 24 t_0^5.
  So 5(2) + 20 = 30. Script: same. Sum of w r_1^{2 a_0} = r_1^{56v}(1 + r_1^{12})^{floor(v/2)}. HOLDS.

### 1.7 Same-group change of sign (weight 1 + chi_1/36 + chi_2/12): HOLDS

- Positive: 1 - 2/36 - 3/12 > 0. r_1 = 1/72, r_2 = 1/36, r_j = 0 for j >= 3. Adjoint single-end moments of orders
  2..6: 1, 1, 3, 6, 15 (trivial multiplicities of spin-1 tensor powers). Two-end: 1, 1, 9, 36, 225. kappa_4 = 6,
  kappa_6 = 110, 5 kappa_4 + kappa_6 = 140. Script: same. HOLDS. It changes the law away from Wilson; it says nothing
  inside the Wilson family.

### 1.8 Exterior through the two end holonomies (12): HOLDS (conditional identity)

- The background log mass drops out of the alternating sum. With nu fixed, the squarefree coefficient is the joint
  cumulant under nu. Example g = 1, Y = +-1: kappa_4 = -2, kappa_6 = 16, (12) = 6. HOLDS. The hypothesis "the exterior
  sees only g and h" is assumed, not shown for any Wilson exterior. The file says so.

### 1.9 Tube separation (seed does not need (3)): HOLDS

- A square tube times the time circle is a closed torus surface: Z = 1 + sum_{j>=1} r_j^{4v}. Proper subsets peel. One
  coefficient, positive, long. (3) fails for every delta > 0. P_K -> 1 at fixed beta and on beta_K ~ log n. Tuned
  coupling with Z(u) = 9/8: V = log(9/8) > 1/9 > 1/12 and P >= 64/81 > 457/625. HOLDS. Scope: a positive gauge-action
  family on a tube, not reflection positive and not in the consumer class (F1). The file states this scope.

### 1.10 Interior magnetic cap (13): HOLDS

- Geometry: the 4 by 2 disk at time 2 has boundary = direct path + rail 1 at time 2. Slot 2 is not in E, so no bulge
  link at times 2 or 3. Its xy label shares a coarse time cell with the bulge at time 4. So q(A u D) = qA. HOLDS.
- a(A u D) = c^D - c: an incomplete cap peels across its interior; an incomplete sheet peels in its cut disk, then the
  cap peels. HOLDS.
- Quaternions: W_i = 4(g_0 h_0 + g . Ad(V_i) h). Under the cap E[Ad V_1 | V_0] = eta Ad V_0 with eta = r_2^8.
  The change of E[W_0 W_1 | g, h] is eta (16/3)|g|^2|h|^2 = eta D_0. HOLDS.
- Only the first power of eta enters a squarefree coefficient. The correction is eta times kappa(D_0, Y^{k-2}).
  E D_0 = 3, E D_0 Y^2 = 4/3, E D_0 Y^4 = 3; kappa(D_0, Y, Y) = -5/3; kappa(D_0, Y^4) = 1. Script: same. (13) HOLDS.
- Bound at beta <= 3: the GL4 citation (r_2 <= 3/8) is not needed. The file's own recurrence later gives
  r_2(t) <= t/(4 + t) <= 3/7, so eta <= (3/7)^8 < 1/16. Fractions: 22 eta/(30 - 28 eta) at eta = 1/16 is 11/226;
  at eta -> 1 the six cap-enabled weights are -2/3 (x5) and -4 (fraction 1), and the twelve raw supports give 11/29.
  Script: same. HOLDS.
- Coupling dependence: sign change of c_4^D at eta = 3/5. HOLDS.

### 1.11 One-cycle attachment theorem: HOLDS, with its scope stated in section 3

- Lengths 16, 20 x 4, 24 and 16, 20, 20, 64; totals 120; fits in a 32-cell. HOLDS.
- Gauge-fixing a spanning path of C makes the exterior density on C central. Only its adjoint coefficient eta enters at
  leading order (Schur). Higher strip harmonics: relative O(q_2^a), uniform under a positive tilt. HOLDS.
- |eta| bound. No plaquette holds two collinear links, so the 16 direct links are conditionally independent given all
  other links. (An exterior xy plaquette can hold a direct link and a rail link at the ends; this is harmless, since the
  rail links are conditioned on.) Each conditional law is a Wilson tilt with t <= 6 x 3 = 18 (in fact at most 4 exterior
  plaquettes, since two of the six slots are sheet plaquettes). E[Ad L | rest] = r_2(t) x rotation. So
  |eta| <= (9/11)^16 < 1/16. 5D: (6/7)^16 < 1/8. Both checked exactly. Negative eta only lowers the fraction. HOLDS.

### 1.12 Small items

- Source measurements Z(D)/Z(P) = E^full prod_{p not in D} w_p^{-1}: HOLDS (trivial).
- Weight required by the consumer, delta = 3 gamma / 4: a group with remainder at most 1/4 has 2 min(P, N) >=
  (3/4)(P + N). HOLDS.

No PROVED item FAILS. One citation is replaceable (GL4 in 1.10). The selectivity reading of 1.4 is corrected in section 4.

## 2. Is map (2) with (3) equivalent to the seed?

- (2) is not a change of theory. At the full mask f'(P') = f(P): the coarse partition function is the fine one, on
  every twist and period. The a(A) are the connected activities of the plaquette on/off expansion of log Z relative to
  Haar, that is the strong-coupling (high-temperature) cluster expansion taken exactly. (2) regroups these activities by
  coarse label. Nothing is carried from scale to scale: V_M is a functional of the bare law and the final grouping.
- With one group per fibre (the file's strongest choice), 2 sum_g min(P_g, N_g) = V_j - V_{j+1}. So (3) at step j is
  exactly V_{j+1} <= (1 - delta) V_j. The chain (entry + (3)) is "V_0 <= C and geometric contraction to V_M <= 1/12".
  Only V_M <= 1/12 is used by (4).
- Direction. (entry + (3)) => V_M <= 1/12 => (PUR-io): PROVED (1.1). The converse fails in a positive gauge-action
  class: the tuned tube has the seed and V = log(9/8) > 1/12 at every level (1.9). So the input is strictly STRONGER
  than the seed in that class, not equivalent and not weaker. For the calibrated isotropic Wilson trajectory the
  comparison is unknown (the file says so). Not equivalent, so the rule is met; but a strictly stronger sufficient
  condition is progress only if it is easier to prove, and section 5 finds no reason to think so.
- The entry bound alone is already seed-type. V_0 >= |L^z|, so V_0 <= C gives P_K >= e^{-3C}. For C < (log 2)/3
  this is a purity above 1/2, which by check 1527 (ii) gives the gap at a changed aspect with no B step. So the B steps
  only lower a large C; the main load sits in the entry bound, an absolute-value bound on the whole box.

## 3. Is it a genuine order-one step?

No. Three reasons.
- No class is carried. A K-II step (row 1386, 4.4) maps a theory in a class at order-one coupling to one in the same
  class, with an estimate that the next step can use. Here there is no effective action or coupling at level j. The
  hypothesis at level j does not imply (3) at level j + 1. Each level needs its own proof about fixed sums of bare
  activities.
- Every proved computation is local. Each a(A) in (5)-(13) is a single-support quantity with all other plaquettes off,
  in one spatial cell. The small parameter is the sheet weight x = r_1^{area} (leading order in the character weights,
  that is the strong-coupling surface expansion). It is valid at large beta only because the areas are at least 4v with
  v >> beta^{3/2}. This is the strong-coupling expansion to leading order on six special ribbon graphs.
- The "order-one" bound is a bare-coupling bound. The one-cycle theorem holds because every exterior link has a
  conditional Wilson tilt t <= 18, so |eta| <= (9/11)^16. This is a one-link a priori estimate (row 1460, Lemma SE kind).
  It holds in any dimension and fails as beta grows: on the calibrated bare sequence eta -> 1 and the cap-enabled
  fraction tends to 1 (1.10). Blocked images are not Wilson lattices, and the hypotheses (Wilson plaquettes with
  coupling at most 3, conditional independence of collinear links) have no stated analogue on an image.

What "uniform for every exterior attached through one spatial cycle" covers:
- The six specific long-ribbon supports A_i (direct length 16), with bulges E, at bare sheet coupling in [2, 3] and
  large v. One fixed exterior X of Wilson plaquettes with couplings at most 3, of any finite size, that meets the
  ribbon links only on the one cycle C at time 2, enabled as a background in all sheet deletions.
- The bounded object is the background-enabled sum sum_{X' in X} sum_i a(A_i u X') (identity: this equals the
  Moebius coefficient of A_i relative to the background X). Its remainder fraction is at most 1/4.

What it leaves out:
- Admissibility in (3). The supports A_i u X' lie in the fibre of qA u qX'. If qX is not inside qA, the bounded sum
  runs over 2^{|X|} different fibres and is not a group in (3). It is a group only when qX is inside qA: X inside the
  same coarse cell column and labels (tx, ty, tz, xy). So the "arbitrary volume" clause gives no admissible group
  outside one cell column.
- Exteriors that touch the ribbon links anywhere else: on two cycles (the file names this as the next test), on
  temporal links, or on sheet faces.
- Every support that is not one of these ribbon graphs. In particular the dense supports, which dominate V_j by count.
- Every level j >= 1. At j >= 1 the coefficients are fibre sums, and nothing is computed for them.
- The calibrated couplings. The bound is for bare couplings at most 3; on beta_K ~ log n it fails (1.10).

## 4. Selectivity (Lemma ALG, (g1)-(g4))

- Nothing proved separates 4D SU(2) from 5D SU(2). The ribbons are embedded three-spatial-direction graphs, so (5)-(10)
  are the same in every dimension at least 4. The one-cycle bound passes in 5D ((6/7)^16 < 1/8). RECALLED, not
  load-bearing: 5D SU(2) Wilson has a bulk transition near beta = 1.64 (Creutz 1979). So [2, 3] in 5D is on the side
  believed gapless, and the local test passes there. Test (g2) fails.
- The SU(2) cancellation reads the algebra. 5 kappa_4 + kappa_6 = 0 uses only Haar moments of the fundamental
  character (Catalan numbers). It holds at every Wilson beta, gapped or not, and in the product with a massless factor.
  By Lemma ALG it cannot be an input. The law enters only through eta (an adjoint loop at fixed size). eta -> 1 as beta
  grows in every dimension and every phase, so it reads the scale, not the phase (fails (P-law)).
- The U(1) "failure" at 5/11 reads the group size, not U(1). (3) allows any disjoint grouping inside a fibre, and the
  fibre holds many more supports than the file's six. Counterexample to the reading:
  - Four-path supports with a staircase fourth rail: from p take one +z step, then any order of 11 further steps in
    +y and +z (i of them +y, 0 <= i <= 11), then 4 steps in +x at (y, z) = (i, 12 - i), then the mirror walk at x = 4.
    After the first step z >= 1, so the rail misses the direct path, the +-2e_y rails and the bulges (all at z = 0).
    Length 28, total 48, orientations tx, ty, tz, inside one cell. There are 2^11 such rails, so at least 2048
    four-path supports in the same fibre as the file's group (same E).
  - Six-path supports: the sixth path at transverse offset (+-1, +-1) instead of (1, 1) gives 4 variants; each misses
    the rails (whose transverse points are (0, +-1), (0, +-2), (+-1, 0), (+-2, 0)).
  - U(1), 13 four-path + 1 six-path: signed 13(-6) + 80 = 2, absolute 158, remainder 1/79 < 1/4.
    U(1), 40 four-path + 3 six-path: signed 40(-6) + 3(80) = 0, an exact leading cancellation. (Checked exactly.)
  So weak 4D U(1) passes the same quarter test with its own groups. The 5/11 is a property of the 5 : 1 ratio chosen
  to match SU(2)'s kappa_6 / kappa_4 = -5. Both groups have kappa_4 and kappa_6 of opposite sign, so both admit
  leading cancellation. Test (g1) fails as a selectivity test. The file already concedes (g3) (the ratio is the same
  at strong U(1)).
- Net: the proved items read the algebra (Haar moments) and the bare coupling (eta). None reads a property of the 4D
  SU(2) law that weak 4D U(1) or 5D SU(2) lacks.

## 5. The exact open estimate

Two inputs, both open (the file labels them GUESSED):
- (ENTRY) At an entry level where the Creutz readout lies in [1/4, 4], V_0(T, z) = sum over long entry supports of
  |a_0(H)| <= C, with C independent of M and K, on both periods and all eight twists, on an infinite set of K. Here
  a_0(H) is the Moebius coefficient of log Z over the block on/off variables (all fine plaquettes of one entry cell and
  orientation switched together), on the whole torus of side l_0 B^M entry spacings.
- (SHARE) At every B step j <= M, disjoint within-fibre groups with remainder fraction at most 1/4 carry a share
  gamma >= gamma_0 > 0 of V_j(T, z), with gamma_0 independent of M and K. Then delta = 3 gamma_0 / 4.

Is it within reach? No. Reasons.
- (ENTRY) is an absolute-value cluster-expansion bound at order-one coupling on a box of B^M correlation lengths. With
  C independent of M it forces the long activities to decay in their time extent faster than the B^{4M} growth of their
  positions: a convergent, decaying polymer expansion at order-one coupling. No method gives this; it is the band. For
  C < (log 2)/3 it is already a seed form (section 2). Reaching the entry level from the bare lattice also crosses the
  weak-coupling running (the file's own (9): the bare absolute sum grows like 2^{v/2} per cell).
- (SHARE) needs a lower bound on the cancelling share of the weight of all long supports, at the blocked coefficients.
  The weight is dominated by dense supports, whose activities are alternating sums over 2^{|A|} subsets. The six ribbon
  groups have weight r_1^{48v} per cell, a vanishing share. polymer-covariance.md item 4 already records that Moebius
  sums of this kind give only 2^{|S|}-sized bounds that do not sum over large sets.
- Selectivity: (SHARE) has no proposed failure line for 5D SU(2) or 4D U(1), and the local test in hand fails (g1)
  and (g2) (section 4).
So the open estimate is the band again, in a strictly stronger absolute-value form.

## 6. New and on file

New in row 1650 (no earlier lane statement found by grep for the four- and six-ribbon cumulants or the mask grouping):
- the mask Moebius regrouping (2) with the long/short two-period consumer (4) and the early exit;
- the ribbon cumulants (7) for k = 4, 6; the 5 + 1 cancellation (8); (9)-(11); the residual 30;
- the changed-law sign example; (12); the tube separation of (3) from the seed;
- the cap formula (13) and the one-cycle theorem.
On file and used:
- annulus and cylinder sewing: rows 701 and 1105 (check 1105), row 1341, row 1418;
- the two-period consumer and Fact PUR: row 1468, section 3.1 (rows 1373, 1461, check 1465);
- threshold above 1/2 at a changed aspect: check 1527 (ii);
- the conditional one-link bound: row 1460, Lemma SE (check 1463);
- the Bessel ratio facts: SA outline GL3-GL4 (credit Sussman and Alpoge, with Claude and Codex);
- "absolute values first" entropy losses: rows 811/816, 838, 1418; Moebius-sum growth: polymer-covariance.md item 4;
- Proposition NEG and Lemma ALG: rows 1386, 1553. Row 1650's local test is one more instance of Proposition NEG
  (lattice-local, holds in five dimensions).

What moved on the critical path: nothing. (ENTRY), (SHARE), (PUR-io) and the gap stay open.

## RESULT

Row 1650: every PROVED item HOLDS ((2), (4), (5)-(13), the tube separation, the one-cycle theorem); no line fails;
arithmetic re-derived by an exact rational script (a guide, not Lean). One citation is replaceable: GL4 in the cap bound,
by the file's own r_2(t) <= t/(4 + t). Map (2) is an identity: the coarse partition function equals the fine one, and (2)
regroups the exact strong-coupling cluster activities by coarse label. (entry + (3)) => seed is proved; the converse fails
in a positive gauge-action class (tube), so the input is strictly stronger than the seed, not equivalent; the entry bound
alone with C < (log 2)/3 is already a seed form. Not an order-one step: no class is carried, every computation is one
support in one cell at leading order in r_1^{area}, and the one-cycle bound is a bare one-link estimate (|eta| <= (9/11)^16)
that fails on the calibrated sequence. It covers only background-enabled sums for six ribbon graphs, which are groups in (3)
only when the exterior stays in the same coarse labels. Selectivity: none. The SU(2) cancellation is Haar algebra; 5D passes;
the U(1) 5/11 reads the 5 : 1 group size: 13 + 1 staircase groups leave 1/79 and 40 + 3 cancel exactly. Open: (ENTRY) and
(SHARE), the band again in absolute form. Recommendation: do not continue this step (no two-cycle row); record the facts.
