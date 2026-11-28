lead: anthropic/claude-fable-5-2/high mac-mini-worker
lease_until: 2026-11-25T02:04Z

# Row 1468: design of the missing K-II tool

Provenance: Claude Fable 5.2, high effort, Mac mini worker 1, fresh session at commit b6b622f51. Research-stage
working state. Not an audit, no status. Every item below is marked proved, sketched or guessed.

Started 2026-11-24T14:04Z (date -u).

## 0. Plan (written first, before reading the inputs)

Task (FINISH row 1468): design the K-II tool, a renormalization step at order-one coupling that carries a sign.

1. Read the rule sections of FINISH.md and GOAL.md (done), then the RESULT parts of rows 1326, 1332, 1386, 1418-1437,
   1442, 1460-1467 and the statements they point to. Log one line per source in Section 1.
2. Repo search and registry grep (open-core.md, FINISH rows) for each candidate statement before calling it new.
3. Section 3: the block map and the exact one-step statement (what is carried, the sign, the iteration to (M-io-exists)).
4. Section 4: filter tests t1-t6 against U(1), Villain U(1), 5D.
5. Section 5: sizing of the finite computation and whether Lean `decide` / `norm_num` can check it.
6. Section 6: the first buildable component and its decisive outcome.
7. Section 7: an obstruction for a stated class, if the step cannot exist.
8. Section 8: the next two rows and their decisive outcomes. RESULT line.

Status log (one line per step, times from date -u):

- 2026-11-24T14:04Z file created, plan written.
- 14:04Z read FINISH rules, GOAL.md, rows 1326, 1332, 1386, 1442, 1460-1467 (RESULT text). Target = (M-io-exists); missing input = K-II (or K-I local); release floor above 2^2800 (row 1464, unchecked); LOSS for the plain kernel (row 1460, check 1463).
- 14:04Z read rows 1418-1437 (RESULT text): tensor-network step sized and rejected by cost and by filter (1418); one-link and two-cycle signed terms cancel or are tiny (1421-1431); Lean kernel replays exist (lean/glue, lean/ring, lean/haar); heat-factor class closed (1434).
- 14:05Z read row 1386 4.1-4.5 (STEP, Remark PAIR, requirements (a)-(i), K-I/K-II/K-III, t1-t5), row 1442 4.2 (t6), row 1332 Section 6 (Proposition CH, END, steps OPEN), row 1460 Sections 2-3 (LD-1, LD-2, LD-3, SE, LOSS, RANGE).
- 14:12Z read (M-io) in check 1465 Step 7 and the first lemma of row 1461 (seed = s_K(2w) <= 4/21 on n = l b^K, w = n/1024; implied by purity P >= 457/625). Next: rows 1449-1458 RESULT lines for (BASE).
- 14:19Z registry grep done (open-core.md has no line for K-II, block step, end class). On file and read (RESULT text): rows 1340-1354 (block steps for Proposition CH: Theorem TL/BS and (B-pin), the 2^4 cube map, the centre-sign map, strip elimination, end classes (11), (10), (10*), END-D), row 1128 1.2-1.4 (Haller-Kennedy, Bertini-Cirillo-Olivieri; stiffness upper bounds pass a block step for every group), rows 1449-1458 (release port), prior/sa-ym4-lean-flow-vs-ca-opus.md L36-66.
- 14:20Z (date -u) Sections 1 and 2 written. Next: Section 3, the consumer in exact form and the map.
- 14:26Z (date -u) Section 3 written (consumer, Q2, Lemma TW, Theorem K2). Next: Section 4, the carried class
  and the one-step statement.
- 14:27Z (date -u) Section 4 written (requirements (C1)-(C6), the tube template, (K2-STEP), (END-K2), Proposition GA, the filter). Next: Section 5, sizing.
- 14:29Z (date -u) Sections 5 and 6 written (sizing by part and by representation, kernel budget, verdict, obstructions for stated classes). Next: Section 7, the first buildable component; Section 8, next rows.
- 14:30Z (date -u) Sections 7, 8, 9 written. Next: re-read of the PROVED items, the label summary and the RESULT line.
- 14:31Z (date -u) re-read of the PROVED items: four repairs in place (Theorem K2 now says it rests on Remark (ii); the slab position for odd cells; the count of C1 item 2; the (C4) paragraph now names the global colour rotation, not a gauge orbit).
- 14:32Z (date -u) Sections 10 and 11 written; RESULT line in place.
- 14:32Z (date -u) finished. Final section order: 1 search and sources, 2 on file, 3 consumer and map, 4 class and step, 5 sizing, 6 obstructions, 7 first component, 8 next rows, 9 repo search result, 10 labels, 11 result.

## 1. Repo search and sources

Registry (rule 0a). `library/open-core.md` has no line for K-II, a block step at order-one coupling, or an end
class (grep counts 0 for "K-II", "end class", "END-D", "Haller", "constrained system"). FINISH rows with "K-II":
1386, 1418, 1442, 1460, 1464, 1468. A narrow search of main and PR #10114 runs in the background; its result
is in Section 9.

Sources read for this row (RESULT text of each row; the named sections of the files):

| Source | What this row takes from it |
|---|---|
| Rows 1461, 1462, 1465 (gpt-6.2-astra; checks Claude Opus) | the target (M-io-exists): one side l in 4N, one level g_0, the neutral seed s_K(2w) <= 4/21 on n = l b^K, w = n/1024, at infinitely many least roots; implied by the purity P >= 457/625; rate (2/l) log(2^18/5041) |
| Row 1332 Section 6 (Claude Fable; check 1335) | Proposition CH: mass-preserving maps between classes, (BASE), (END) |
| Row 1386 4.1-4.5, row 1442 4.2 (Claude Fable; checks 1387, 1443) | K-I, K-II, K-III; Remark PAIR; requirements (a)-(i); filter (t1)-(t6); Remark FI |
| Row 1460 Section 3, check 1463 (Claude Fable; gpt-6.2-astra) | Lemma LD-1, Corollary LD-2, Remark LD-3, Lemma SE, Theorem LOSS (plain kernel) |
| Row 1464 (Claude Opus; check 1467 queued, so unchecked) | the release's floor: g^(-2) above (2^51 L)^100 and above 2^2800 at any side |
| Rows 1449-1458 | the release's flow: exact soft block map `kernelImage` (side b odd, at least 2^40), readout, first passage; no rectangular or twisted tori in the release (row 1457) |
| Rows 1340-1354 and checks | the block-step work for Proposition CH: Theorem TL and BS with (B-pin) (1340), the exact 2^4 cube map and the eight-link enclosure, 6.5e14 gates (1341, 1344), the centre-sign map (1345), the finite-state cores (1348), the neutral end class (1351) and its dual (10*) (1354, Theorem E), Theorem END-D (1353) |
| Rows 1418-1437 | the tensor-network sizing (rank at least 67 at beta 2, 1e27 operations a fusion), the signed-term gates (all null), the Lean replays `lean/glue`, `lean/ring`, `lean/haar` with wall times |
| Row 1128 1.2-1.4 (Claude Fable) | Haller-Kennedy and Bertini-Cirillo-Olivieri as the only published scheme for one block step at order-one coupling; "an upper bound on stiffness passes a block step for every group" |
| Row 1326 (Claude Fable; check 1331) | Lemma DIM (cost of exact contraction), Theorem O with Remark OS (loop-equation certificates) |

Credit. Tadeusz Balaban: the block averaging renormalization method for lattice gauge fields, its small-field
and large-field split and the ultraviolet stability theorem. E. T. Tomboulis: the decimation scheme with
interpolating parameters and the vortex free energy as the carried quantity. Ethan Sussman and Levent Alpoge,
with Claude and Codex as authors of their text: the YM4 Lean release (3932084a9b82), its exact soft block map
(`kernelImage`, contour means, the von Mises-Fisher bond kernel), its readout and its first-passage calibration,
and the complete account. K. Haller and T. Kennedy; L. Bertini, E. Cirillo and E. Olivieri: the constrained-system
scheme (recalled from the lane's row 1128, not re-read here: a gap of this row).

## 2. What is on file, and what changed since

The lane has worked on a block step for Proposition CH before (rows 1340-1354, 2026-11-21). The state then:

- Exact maps on file: the 2^4 cube map (row 1341), the centre-sign map (row 1345), strip elimination (row
  1351), the soft pin step along the coupling ray (rows 861, 1340). Each is exact for every compact group
  (row 1353), so none is selective by itself.
- End classes on file: C_land of row 1340, class (11) of row 1345, class (10) of row 1351 (an alternative-II
  class: a twist-wise exact landing there would prove no confinement, row 1354), the dual class (10*) of row
  1354 (Theorem E), Theorem END-D of row 1353.
- First failing step, the same in all of them: one block step at a coupling above the hand range (2/9 to
  1.0109), into a class of the kind (10*), uniform in the cutoff; and (BASE), which was not a finite statement.

Four facts are new since then, and they fix the frame of this design:

1. (BASE) has an exact form. The release blocks the Wilson density exactly down to a top level whose
   unit-scale coupling lies in a bounded window [H, W_*] (rows 1451, 1453). So a chain can start from one
   class at a weak coupling. It need not enter from bare couplings that grow with the cutoff (the entry
   obstruction of rows 1341, 1346).
2. The consumer is weaker: (M-io-exists) (rows 1461, 1462, 1465).
3. The window is not near order one: H is above 2^2800 (row 1464, unchecked). So the band has a long weak part.
4. Theorem LOSS (row 1460, check 1463): thin transporters of length L lose the coarse field when L is large
   against the coupling. So a band step has block side at most of order the coupling.

## 3. The tool, part 1: the consumer in exact form and the block map

### 3.1 The consumer: sixteen masses

Fix the release witnesses (odd block factor b, calibration level g_0) as in check 1453. Fix a side l that is a
multiple of 1024. At cutoff K put n = l b^K and u = n/512 (this is 2w of row 1461). T is the Wilson transfer
operator at beta_K on the spatial torus of side n, P_0 the projector on the centre-neutral gauge-invariant
states, C_z (z in Z_2^3) the centre translations. Put

    Z^z(v) = Tr(C_z T^v),   Z_+(v) = (1/8) sum_z Z^z(v) = Tr(P_0 T^v),   P_K = Z_+(2u) / Z_+(u)^2.

Z^z(v) is the Wilson partition function on the torus n^3 x v with the temporal twist z (the lane's flux
formalism, `gap-flux-exercise.md` 3.0-3.1). So P_K is a function of sixteen masses: two tori, eight twists.

**Fact PUR (on file: rows 1373, 1461; check 1465; the proof is three lines, repeated here). PROVED.**
P_K >= 457/625 implies s_K(u) <= 4/21, the seed of (M-io-exists) at this K.

Proof. Let r_i in [0, 1] be the ratios of the neutral eigenvalues to the vacuum eigenvalue, s = sum of r_i^u
over i > 0. Then P_K = (1 + sum r_i^(2u)) / (1 + s)^2, and sum r_i^(2u) <= min(s, s^2). So P_K <= 1/(1 + s),
which gives s <= 168/457 < 1. Also P_K <= (1 + s^2)/(1 + s)^2. This function decreases on [0, 1] and equals
457/625 at s = 4/21. QED

So the consumer is: **(PUR-io) P_K >= 457/625 at infinitely many K, for one l and one g_0.** By rows 1461, 1462
and 1465 this gives a gapped calibrated limit with rate at least (2/l) log(2^18/5041).

Twisted fields. For the twist z and time side v, the field space F^z(n, v) is the set of link fields W on
(Z/n)^3 x Z with W(x + v e_0, mu) = (C_z W)(x, mu). Here C_z multiplies by -1 the links (x, i) with z_i = 1 and
x_i = 0. The measure is Haar on one period. A density on the twisted torus is a function on F^z(n, v).

### 3.2 The block map Q2

**Definition (the map; a small-side, plain form of the release's kernel; credit Sussman and Alpoge with Claude
and Codex for `kernelImage`, `contourMean` and the bond kernel).** Block side 2. The fine lattice has even
sides. The coarse site y is the fine site 2y (corner bases, one base choice). For a coarse bond c = (y, mu)
and a pair e = (xi, pi), xi in {0,1}^4, pi a permutation of the four axes, the contour of e is the lattice
path: the axis path from 2y to 2y + xi (axes in the order pi), then two steps in direction mu, then the
reverse axis path from 2y + 2 e_mu + xi to 2y + 2 e_mu. The contour mean is the quaternion

    M_c(W) = (1/384) sum over the 16 x 24 pairs e of hol_W(e),   norm(M_c) <= 1.

For a strength kappa > 0 the kernel and the image of a density D are

    K_kappa(W, V) = prod over coarse bonds c of exp(kappa Re(M_c(W) V(c)^(-1))) / Zc(kappa norm(M_c(W))),
    Zc(t) = integral over SU(2) of exp(t Re g) dg,
    (Q2_kappa D)(V) = integral of D(W) K_kappa(W, V) dW.

This is the plain kernel of row 1460 3.1 at L = 2 with corner bases in place of cell centres. The release's
own kernel has odd side, centred bases and field-dependent base choices; its hypotheses ask for side at least
2^40 (row 1464). Nothing below needs the release's theorems for Q2. Side 3 with centred bases is the same
design with 81 sites to a block; I choose side 2 because the cost of every finite part grows with the block.

Why this map (each line is a requirement, with its source):

- Exact and defined at every fine field: the kernel is a probability density in V for every W. A hard
  delta map on a normalized mean is not defined where the mean vanishes.
- Self-similar: hypercubic lattice to hypercubic lattice. The exact 2^4 cube map of row 1341 is not
  self-similar (check 1346: a retained link keeps all six plaquettes).
- Bounded transporter self-energy: Theorem LOSS of row 1460 needs L at most of order the coupling. A
  straight product of two links (decimation) is also short, but iterated decimation is a thin line of
  length 2^k after k steps, which is the LOSS case again. Iterated averaging makes tubes whose width grows
  with their length. SKETCHED (the Gaussian computation of Proposition GA below is the abelian form).
- Kernel strength: by Corollary LD-2 of row 1460, the image has Hessian at most kappa at every coarse field.
  So a step that returns a coupling x' needs kappa at least of order x'. I take kappa_k = a x_k with one
  constant a (the release takes a = 1 at unit mesh).

**Lemma TW (twist-wise exact carry). PROVED here by hand, unchecked.** Let n and v be even, at least 4. For W
in F^z(n, v) define C'_z on coarse fields as C_z on the lattice of side n/2. Then M_c(C_z W) = M_c(W) for every
coarse bond c, except M_c(C_z W) = - M_c(W) when c = (y, i) with z_i = 1 and y_i = 0. Hence
K_kappa(C_z W, C'_z V) = K_kappa(W, V), the map Q2_kappa sends densities on F^z(n, v) to densities on
F^z(n/2, v/2), and it keeps the mass: the integral of Q2_kappa D over one coarse period equals the integral of
D over one fine period. The same holds on the periodic tori.

Proof. Fix i with z_i = 1. C_z changes the sign of hol_W(e) by (-1)^N, N the number of traversals by e of
links (x, i) with x_i = 0. Case mu = i. The first leg uses the i-link at x_i = 2 y_i if and only if xi_i = 1.
The straight part uses the i-links at x_i = 2 y_i + xi_i and 2 y_i + xi_i + 1. The last leg uses the i-link at
x_i = 2 y_i + 2 if and only if xi_i = 1. If y_i = 0: for xi_i = 0 the straight part uses x_i = 0 once; for
xi_i = 1 the first leg uses it once and nothing else does. So N = 1 for all 384 contours. If 2 y_i = n - 2:
for xi_i = 1 the straight part uses the link at x_i = n = 0 and the last leg uses the link at x_i = 0 again, so
N = 2; for xi_i = 0, N = 0. For other y_i no link at x_i = 0 occurs. Case mu different from i. Only the legs
move in direction i. Both use the i-link at x_i = 2 y_i, if and only if xi_i = 1. So N is 0 or 2. This gives
the sign rule. The kernel depends on W and V through Re(M_c V(c)^(-1)) and norm(M_c), which the joint sign
change keeps. So the kernel is well defined on one period of the twisted torus, and it is a probability
density in V for each W. Fubini gives the masses. QED

Remarks. (i) The lemma uses that the slab of C_z lies on a block boundary. (ii) The release's `kernelImage`
on tori with sides divisible by b carries the sixteen masses in the same way if its contours stay in the two
cells of their bond, its hot lumps are functions of plaquettes, and the slab of C_z is put on a cell
boundary at each level (a translation of the torus; the centred cells of odd side have their boundaries off
the origin). SKETCHED: I did not read `usedContours` and `IsBaseChoice` line by line for this; row 1457 records that the release has no twisted or rectangular
tori. (iii) The image of a reflection-positive density under Q2 is not reflection positive in general (the
contours of a bond that crosses a mirror are not mirror images of themselves). The chain does not need it: it
reads the sixteen masses only.

### 3.3 Theorem K2 (soundness of a chain to (PUR-io)). PROVED here given Remark (ii) of 3.2 for the release's kernel (one line, the form of Proposition CH)

Let l = 512 * 2^N * v_E with integers N >= 0 and v_E >= 4. Level k, 0 <= k <= N, has the tori of spatial side
l_k = l / 2^k and time sides v_k = l_k/512 and 2 v_k, with the eight twists. A level-k family is a choice of a
positive integrable density on each of the sixteen twisted tori of level k. Let C_0, ..., C_N be sets of
families, C_k of level k, and kappa_0, ..., kappa_(N-1) positive numbers. Assume:

- (BASE-K2) for infinitely many K, the family obtained from the Wilson weights at beta_K on the sixteen tori
  of side n = l b^K by K steps of the release's `kernelImage` lies in C_0;
- (STEP_k) Q2 with strength kappa_k, applied to each of the sixteen densities, maps C_k into C_(k+1);
- (END) every family in C_N has purity at least 457/625.

Then (PUR-io) holds, hence (M-io-exists). If (BASE-K2) holds for every late K, then (M-neutral-all) holds.

Proof. Every map keeps each of the sixteen masses (the release's kernel is a probability kernel; Lemma TW and
Remark (ii) for the twists). The purity is a function of the masses. QED

What Theorem K2 does not give. As a bare existence statement it is equivalent to the target: take for C_k
the orbit of the Wilson data. So its content is in how the classes are defined. A class must be given by
bounds that do not name the orbit, and each inclusion must be provable at one scale. Section 4 states this.

## 4. The tool, part 2: what is carried, and the exact statement of one step

### 4.1 Requirements on a class (each with its source)

| # | Requirement | Source |
|---|---|---|
| (C1) | Torus-free. A member is a local rule that gives the density on all sixteen tori (and on larger ones), with one constant per site. Then the purity can be read at the end. | Theorem K2; Proposition CH |
| (C2) | Quasi-local: the rule has summable range. This excludes a global label. | Remark FI of row 1386; requirement (i) there |
| (C3) | Not an alternative-II class: at the end the eight twisted masses are equal up to small factors. The end class is of the kind (10*) or END-D, not (10) or (11). | row 1354, Corollary B1 and Theorem E; row 1353 |
| (C4) | Typical-field form above the hand range: no unweighted supremum over all coarse fields. | CA-FAIL (row 1072: uniform mixing over boundary values fails above beta = 1.0109); row 950 (GUIDE: at a pi-flux slice the colour direction orders from beta about 2.45 up); requirement (f) of row 1386 |
| (C5) | Narrow near the crossover: the class excludes every local SU(2) density with two vacua or no gap. By numerics (Bhanot and Creutz, GUIDE) the Wilson axis near beta 2.2 is at a distance of order one in the adjoint coupling from the end of a first-order line. | row 1128 1.4 item 4; `parts/gap.md` test table (K7); Proposition V of `gap-crux-fp.md` (van Enter and Shlosman) |
| (C6) | One scale: an inclusion names no cutoff and no torus side. | rule "Equivalent is not progress"; filter (t5) |

Why (C4) binds this map too (ARGUED). Take the coarse field with every plaquette equal to -1 (staggered
signs). The fine fields that Q2 maps near it carry flux pi through every 2 x 2 fine square. A uniform abelian
field with plaquette angle pi/4 in a colour direction n does this for every n in S^2, at the same Wilson
energy. These states are related by a constant colour rotation. It fixes a central coarse field, so it is a
global symmetry of the constrained system, and the coarse links tie the colour frames of the base points.
So the colour direction of the flux is a spin with a global SO(3) symmetry and a stiffness of order x. In
four dimensions such a spin orders at large stiffness, with slow modes. Then the value of -log(Q2 D) at this
field is set by a fine-lattice minimization, not by the readout x'; a centre of Wilson form with a bounded
radius in the supremum norm cannot hold as x grows; and decay of correlations of the fine system given such
a coarse field is not expected. This is the soft-tie form of the ordering that row 950 saw at a frozen
pi-flux slice. Balaban's large-field regions are the weak-coupling form of this
requirement.

### 4.2 Definitions (the template; the norm is a design choice, GUESSED adequate)

A **local rule** is a family Phi = (Phi_X), X the finite connected sets of bonds of Z^4, each Phi_X a
continuous gauge-invariant function of the SU(2) field on X, covariant under the hypercubic group with
translations. For x >= 1, r > 0 and a weight constant theta in (0, 1]:

    norm(Phi)_(x,r) = sup over bonds c of the sum over X containing c of
                      e^(r size(X)) sup over fields V of abs(Phi_X(V)) / (1 + theta x E_X(V)),
    E_X(V) = sum over the plaquettes p inside X of (1 - Re V_p).

A family (of level k) **realizes** Phi with site constant e and wrap error eta if on each of its sixteen tori,
of shortest side s, abs(log D(V) + e size(T) + sum over X of diameter below s/2 of Phi_X(V)) <= eta for every
V. The **tube** Tube(Phi*, rho; eta) is the set of families that realize some Phi with
norm(Phi - Phi*)_(x,r) <= rho, with wrap error at most eta. The **readout** x(Phi) is the coefficient of the
transverse k^2 term of the Hessian of Phi at the trivial field (the release's `nextCoupling`; Remark LD-3 of
row 1460).

The weight 1 + theta x E_X is the cheapest way I see to meet (C4): the bound is tight on regular fields and
loose in proportion to the local action on rough fields. It is not Balaban's class and not the release's. A
split into small-field and large-field regions with separate bounds is the alternative. I did not test
either against a step.

### 4.3 The one-step statement

**(K2-STEP) for the band.** There are a strength ratio a > 0, numbers delta_0 > 0 and r > 0, and for every
step k of the band a centre Phi*_k with readout x_k, a radius rho_k and a wrap error eta_k, such that Q2 with
strength a x_k maps Tube(Phi*_k, rho_k; eta_k) into Tube(Phi*_(k+1), rho_(k+1); eta_(k+1)), with

- (DR) the sign: x_(k+1) <= x_k - delta_0;
- (TR) the contraction: rho_(k+1) <= rho_bar(x_(k+1)), a fixed profile that stays inside the margin of (C5)
  and below the end threshold;
- (WR) eta_(k+1) <= eta_k + size(T) e^(-r s/8) on each torus T of shortest side s.

The chain starts at the release's window, x_0 in [H, W_*], and stops at the first N with
norm(Phi*_N) + rho_N <= eps_E.

**(END-K2).** There are eps_E > 0 and a function v_E(m) = O(log m) such that every family that realizes a rule
of norm at most eps_E on tori of spatial side m and time sides v, 2v with v >= v_E(m), with wrap error at most
1/100, has purity at least 457/625. SKETCHED: a polymer expansion of the sixteen masses; the site constant
cancels in the purity; the terms that wrap the time direction are at most m^3 e^(-c v). Relatives on file:
Theorem E of row 1354 for (10*), Theorem END-D of row 1353, Theorem BS of row 1340. No constants are computed
here. Not checked: that the weighted norm at x of order one gives the supremum bounds those theorems use.

With (BASE-K2) in the form "the release's level-K family lies in Tube(Phi*_0, rho_0; eta_0) for infinitely
many K", Theorem K2 gives (PUR-io).

**What a proof of one step consists of.** For a rule Phi and a coarse field V, the fine system with weight
exp(-Phi(W)) K(W, V) is the constrained system. log(Q2 D)(V) is its free energy. Lemma LD-1 of row 1460 gives
its second derivative in V as a posterior mean minus a posterior variance. Two obligations:

- (CM_k) mixing of the constrained system, with a rate and a constant, for every rule in the tube and every
  coarse field in a regular set, and a bound on the weight of the fields outside it. This gives the existence
  and the range of the image rule (the scheme of Haller and Kennedy and of Bertini, Cirillo and Olivieri; for
  weak coupling the scheme of Balaban). It is the contraction (TR).
- (EN_k) an enclosure of the new centre, with (DR). In the weak part this is the one-loop computation. In the
  order-one part it is a number.

### 4.4 The abelian control of the map

**Proposition GA (Gaussian model; PROVED here by an elementary Fourier computation, unchecked).** Let A be a
real field on the bonds of Z^d with the weight exp(-(x/2) sum over plaquettes of (dA)_p^2). Let Q be the
linear form of the contour mean of Q2 (the sum of A along each contour, averaged), and let the kernel be
exp(-(kappa/2) sum over coarse bonds of (A'(c) - (QA)(c))^2). Then the image is Gaussian and gauge invariant,
and the transverse part of its Hessian has the symbol 2^(d-4) x p^2 (1 + o(1)) as p tends to 0, for every
kappa > 0. So the readout is x' = 2^(d-4) x: x' = x in four dimensions, x' = 2x in five.

Proof. Q(d lambda) = d'(lambda at the base points), because every contour runs from 2y to 2y + 2 e_mu. So the
image is gauge invariant. On transverse fields the image has the Hessian (1/kappa + C_Q)^(-1), C_Q the
covariance of QA. For a fine plane wave a_nu e^(ik.x) the two legs of a contour cancel up to O(abs(k)) and the
straight part gives 2 a_mu e^(2ik.y)(1 + O(abs(k))). So the symbol of Q is 2 + O(abs(k)) at small k and is
bounded at the alias momenta p/2 + pi m, m not 0, where the fine transverse covariance 1/(x khat^2) is
bounded. The coarse lattice has 2^(-d) of the sites. So C_Q(p) = 2^(-d) 4 (x (p/2)^2)^(-1) + O(1)
= 2^(4-d)/(x p^2) + O(1) on transverse fields, and the Hessian is 2^(d-4) x p^2 (1 + O(p^2 (1 + x/kappa))).
QED

Reading. The classical factor of Remark PAIR (row 1386) is exact for this map, and the abelian readout does
not move in four dimensions. So for Q2 every drift is a non-Gaussian effect. For SU(2) at weak coupling the
drift is the one-loop term: x' = x - (11/(3 pi^2)) log 2 + O(1/x) = x - 0.2575 + O(1/x). SKETCHED for Q2: the
coefficient is the release's `oneLoopShift` at side 2, and I did not compute it for this map.

### 4.5 The filter (t1) to (t6), and one more

| Test | Result for (K2-STEP) | Line that decides |
|---|---|---|
| (t1) compact U(1), d = 4, weak coupling | (DR) fails | Proposition GA: the Gaussian part gives x' = x. The remainder is monopole loops with weight e^(-c x). By Guth and by Frohlich and Spencer (recalled, not re-read here) the model is massless at weak coupling, so the conclusion of the chain, a mass gap, is false there. In the weak-coupling proof of (DR) the gain is the term with two structure constants; it is zero for an abelian group. |
| (t6) Villain U(1) | (DR) fails, same line | The two exact identities of the step (the masses, Lemma TW; Lemma LD-1) hold for Villain U(1) and for every model. So neither is the mechanism. The mechanism is the inequality (DR). |
| (t2) SU(2), d = 5 | (DR) fails | Proposition GA: x' = 2x - c at weak coupling. The step is the pair of Remark PAIR: a carry with the exact factor 2^(d-4) and a gain per step. |
| (t3) SU(3) | same statement; one-loop gain (11 N^2/(12 pi^2)) log 2 = 0.579 at N = 3, in the account's normalization x = 2N/g^2 | nothing rests on dim G = 3 |
| (t4) beta grows at a fixed lattice | passes | a step is at one scale; a larger bare coupling means more steps |
| (t5) equivalence | not equivalent, and not proved | The conjunction over the band implies the seed. The seed does not give the locality of the intermediate images. But (t5) also asks for the method: Section 5 finds a method for the weak part only above the release's floor, and none for the order-one part. |
| K7 and Proposition V | binds the radius | (C5): the tube must exclude the mixed-action coexistence line and the deep-well weights of van Enter and Shlosman |

So the statement passes the selectivity tests, as any statement about the true flow does. It fails the last
clause of (t5) on the order-one part. That is the wall, restated at one scale.

## 5. Sizing

### 5.1 The three parts of the band, and the count of steps

x is the inverse coupling in the release's normalization (x = beta at the bare level). One Q2 step lowers x
by 0.2575 at one loop (SKETCHED for this map, 4.4).

| Part | Range of x | Steps of side 2 | What must prove (K2-STEP) there |
|---|---|---|---|
| Base | bare to the window [H, W_*] | K steps of the release, side b | the release (exists, Lean); (BASE-K2) on rectangular and twisted tori is a port item, OPEN |
| Weak part | from the window down to a floor x_pert | (x_0 - x_pert)/0.2575, at least 3.88 * 2^2800 if the window is as row 1464 reads it | ONE theorem, uniform in x. The steps cannot be listed. |
| Order-one part | from x_pert down to about 2.3 | about 3.88 (x_pert - 2.3): 30 at x_pert = 10, 110 at 30, 380 at 100, 3900 at 1000 | one certificate for each step, or a second uniform theorem |
| Entry to the end | from about 2.3 to norm at most eps_E | 2 to 3 (the fundamental coefficient goes about as c to c^4 a step: 0.51, 0.07, 2e-5; GUIDE) | one certificate each |
| End | below eps_E | none | (END-K2), by hand |

The counts are GUIDE: they use the one-loop drift, and no upper bound on the drift of a Q2 step is proved.

**The floor decides the count.** The only weak-coupling step theorem on file is the release's. Its floor is
above (2^51 L)^100 at side L, and its clause `floorMin` is at least 2^1600 at every side (row 1464, unchecked;
the growth comes from clusterRange x = ceiling of x^(1/100)). With that floor the order-one part has more
than 2^1600 steps. So a step-by-step certificate is excluded by count alone, whatever one step costs. A K-II
tool therefore needs, first, a weak-coupling step with a floor of human size. I call this component T1.

What floor could T1 reach (GUESSED)? A small-field expansion needs rough plaquettes to be rare in a block.
In the Wilson law the plaquette energy 1 - Re U_p has mean about 3/(4 beta), and the chance of a value above
1/2 is of order e^(-beta). A 2^4 block has 96 plaquettes. A polymer bound needs this chance to beat a
combinatorial constant of the order e^10 to e^50 in four dimensions. So x_pert of 30 to 100 is the best
case, with computed constants. A hand proof with Balaban's or the release's style of constants would give
much more. So the order-one part has 100 to 400 steps in the best case.

### 5.2 The finite part of one order-one step, by representation

| Representation | The finite part | Cost on file | Source |
|---|---|---|---|
| Site tensors (Oeckl-Pfeiffer; Ebel-Kennedy-Rychkov) | fusion of 16 sites | bond rank at least 67 at beta 2 for error 1/4; a dense site is 13 PB; one fusion above 1e27 operations; the rank-128 trial fails its own error test | row 1418, check 1420 |
| Enclosure of a block integral | the free energy of the constrained block, uniform in its surroundings | eight links of a 2^4 cube, error 2^(-24), beta up to 7/3: 6.5e14 rational gates. A Q2 block has 64 links, tied to 8 coarse bonds and to its neighbours. No method on file goes beyond eight links. | rows 1341, 1344 |
| Block Dobrushin criterion (B-pin) | a supremum of a block law over its surroundings | one link reaches 2/9; no rigorous method above 0.3609; the block needs side about 3 to 10 at the window (GUIDE) | row 1340, check 1346 |
| Loop-equation or positivity certificate | a patch of loops | the patch is as large as a seed box | row 1326, Theorem O with Remark OS |
| Character sums on one 2^4 block | one signed coefficient | spin order 42, eight producers, at most 149 s each; a coefficient, not a step | rows 1425, 1429 |

No row gives a closed class at order-one coupling. Each sizes one piece of one step.

### 5.3 What the Lean kernel can check

Measured on the Mac mini (lead's replays): `lean/glue` 3 s; `lean/ring` 1,289 s and 1.36 GB for 584 theorems
by `decide`, for arithmetic that the exact-rational producers of row 1425 ran in at most 149 s each;
`lean/haar` 6,822 s for 429 modules. So one Lean row holds about two hours of kernel time, and the kernel is
about ten times slower than exact-rational Python on this kind of table (one data point). At an assumed
1e6 rational gates a second in Python (GUESSED), a Lean row holds about 1e9 gates.

- The eight-link enclosure (6.5e14 gates) is about 1e5 to 1e6 Lean rows. It is the smallest piece of a
  step on file.
- So no finite part of an order-one step can be a `decide` or `norm_num` check. With `native_decide` (not
  allowed) the eight-link piece alone would be days.
- What does fit: the constants of hand theorems (the end thresholds, Bessel-ratio bounds), small
  combinatorial tables (the sign rule of Lemma TW), the algebra of Fact PUR.

### 5.4 Verdict of the sizing

| Component | Kind | State |
|---|---|---|
| T0, (BASE-K2) | port of the release's bounds to rectangular and twisted tori; its class inside a tube | OPEN; analysis and Lean engineering; size not estimated |
| T1, weak part with a floor of human size and side 2 or 3 | analysis (Balaban's method with explicit constants) | OPEN; nothing on file; the release's floor is above 2^1600 by its structure |
| T2, order-one part | 100 to 400 certified steps in the best case | NO METHOD: no closed class, and the smallest piece of one step is 1e5 Lean rows |
| T3, (END-K2) with numbers | hand proof, small Lean arithmetic | buildable; relatives on file |

The computation is not the bottleneck that a larger machine removes. T1 is not a computation. T2 has no
representation in which a step is a finite statement of a known cost.

## 6. Is there an obstruction? (task item 4)

No obstruction to the existence of a step is proved here, and none is on file. I believe (K2-STEP) in a
typical-field form is true for SU(2) (belief, not evidence). What can be said for stated classes:

- (O-a) Step-by-step certificates with the release as the weak part: excluded by count (5.1). GUIDE, because
  the count uses the one-loop drift.
- (O-b) Classes with an unweighted supremum over coarse fields, and steps proved by mixing that is uniform
  over all coarse fields: excluded above the hand range. The boundary-uniform form is CA-FAIL (row 1072, a
  theorem given Frohlich, Simon and Spencer, above beta 1.0109). For the soft ties of Q2 the same is ARGUED
  only (4.1) with GUIDE support (row 950). I did not prove it for Q2.
- (O-c) Certificates of the five kinds of 5.2: excluded by cost for the kernel, and for the first, second and
  fourth kind for any machine on file.
- (O-d) Exact identities of the step as mechanism: excluded by (t6). Lemma TW and Lemma LD-1 hold for every
  group and every dimension, and Proposition GA shows the abelian readout is exactly marginal.

What is left open by these: a typical-field class with a hand proof of (CM) and (DR) on the order-one part.
That is K-II in the sense of row 1386, "Balaban's method without a small coupling", and by Remark PAIR its
selective half is an inequality of kind K-I. This row does not supply it.

## 7. The first buildable component (task item 3)

No component of the order-one part fits a Lean row (5.3), and none has a method (5.4). So the first buildable
component cannot test the wall. I name what is buildable, in the order of what each decides.

**C1, one Lean row (small; a true part of the chain): `K2Chain`.** Contents:

1. Fact PUR as algebra over an ordered field: for s >= 0 and 0 <= c <= min(s, s^2), 625 (1 + c) >= 457 (1 + s)^2
   implies 21 s <= 4. The proof is two polynomial facts: 625 >= 457 (1 + s), and
   168 s^2 - 914 s + 168 = (21 s - 4)(8 s - 42) >= 0 with 8 s - 42 < 0.
2. The sign rule of Lemma TW by `decide`: on the fine torus of side 8, for the 4 bond directions mu, the 4
   slab directions i (the case i = mu included), the 4 values of y_i, the 16 offsets and the 24 axis orders
   (24,576 contours of at most 10 steps), the number of traversals of the slab x_i = 0 is odd exactly when
   mu = i and y_i = 0.
3. Theorem K2 as an abstract statement (masses kept by each map; purity a function of the masses).

Decisive outcome: all cases of item 2 pass, and then Q2 as defined carries the sixteen masses; or one contour
fails, and then the contour family changes before anything else is built on it. Cost: seconds of kernel time
for item 2; items 1 and 3 need an ordered field (Mathlib, as in the release's toolchain, or rationals in
core). Standing: it makes the consumer side of the tool formal. It does not move the wall.

**C2, one hand-proof row: (END-K2) with numbers.** eps_E and v_E(m) for the purity on the sixteen tori, for
rules in the norm of 4.2 at x of order one, from Theorem E of row 1354 or Theorem END-D of row 1353, plus the
entry of the Wilson weight at beta below a stated beta_E after one Q2 step with a stated strength. Decisive
outcome: an explicit end class that the Q2 chain can land in, with the largest beta_E that the hand methods
give (the hand range on file stops between 2/9 and 1.0109). It tells how many certified entry steps T2 needs.

**C3, one reading row: the floor of T1.** See Row 2 of Section 8. This is the component that decides whether
a K-II tool by step certificates stays on the list at all.

**C4, one GUIDE run (optional): (CM) at typical coarse fields.** Wilson SU(2) at beta 2.3 to 4 on a torus of
side 12 or 16, one Q2 draw of the coarse field with kappa = beta, two replicas of the fine field given that
coarse field, the decay length of a gauge-invariant overlap between the replicas. It can refute the
typical-field form of (CM) for this map and this strength (a decay length that grows with beta at fixed
kappa/beta). It cannot prove (CM). I expect it to pass, so I rank it last.

I did not build C1 in this row: the brief says to commit no code, and the row is the design.

Own check of Lemma TW by enumeration: NOT run. Free memory was 40 percent (`memory_pressure`, read in this
step), below the 50 percent rule for a numeric job, so the lemma stands on the hand proof of 3.2 until C1 or
a checker runs the count.

## 8. The next two rows, and their decisive outcomes

**Row 1, `gap-k2-tool-design-check-astra62` (cross-provider check of this file).** In order: Lemma TW, case
by case, and Remark (ii) against the release's `usedContours`, `IsBaseChoice` and `hotLumps` (do the contours
of a bond stay in its two cells, and is the set of base choices unchanged by C_z); Theorem K2 and Fact PUR;
Proposition GA (the symbol of Q, the alias sum, the gauge quotient); the counts of 5.1 and the claim of 5.2
that no row on file gives a closed class at order-one coupling; the (C4) argument of 4.1. Decisive outcome:
HOLDS, HOLDS AFTER CORRECTION with each repair, or FAILS at the first wrong line. If TW or GA fails, the map
changes. If the checker finds a closed class or a step method on file that 5.2 missed, that is the next
proof row.

**Row 2, `gap-k2-floor-sizing` (read only; decides whether K-II by step certificates stays on the list).**
Question: at what inverse coupling X does a weak-coupling block step with explicit constants close, when the
block side is small or is a power 2^m built by iterating Q2? Read the release's ledger of floor clauses (row
1464, Steps 3 to 6, with check 1467) and Balaban's large-field conditions (CMP 109, 116, 119, 122). For each
clause that binds the floor, give the smallest x at which it holds if the exponent 1/100 of `clusterRange`
and the constants are chosen again, and say whether the clause is structural. Decisive outcome, one of two:
(a) a number X at most 100 with the list of clauses: then the order-one part has at most 400 steps, and a
proof-design row for T1 is justified; (b) X at least 10^4, or a structural reason: then a K-II tool by step
certificates is closed on the record by count, and the band stays stopped under row 1442 with its triggers
(R1) to (R3).

Not proposed: a row on T2. There is no first lemma for it. Optional third row: the Lean row C1.

## 9. Repo search result (rule "Repo first")

Bare blob-less fetch of main and of PR #10114 into a scratch folder under /tmp, grep of the 67 ym4d text
files of main and of 28 files of PR #10114 chosen by name (mass gap, block, step, soft-hard, target), for:
order-one coupling, Haller, finite-size condition, constrained system, block side 2, Kadanoff, Tomboulis.
Main: no hit. PR #10114: three hits, all in `checks/review_massgap_block_literature.md` (lines 114, 120, 168);
line 168 records for "continuum, crossover, exact RG" that "No usable theorem was validated". So the other
target has no block step at order-one coupling either. PRs #10133, #10134, #10141, #10144 were not searched.

## 10. Summary of labels

| Item | Label |
|---|---|
| Fact PUR (purity gives the seed) | PROVED; on file (rows 1373, 1461, check 1465); repeated |
| Lemma TW (Q2 carries the sixteen masses, twist by twist) | PROVED here by hand, unchecked; own enumeration not run |
| Theorem K2 (soundness of the chain to (PUR-io)) | PROVED here given Remark (ii) of 3.2 |
| Remark (ii) (the release's kernel on rectangular and twisted tori) | SKETCHED |
| Proposition GA (the abelian readout of Q2 is x' = 2^(d-4) x) | PROVED here for the Gaussian model, unchecked |
| One-loop drift 0.2575 for Q2; bounded self-energy of iterated averaging | SKETCHED |
| (END-K2) | SKETCHED; relatives on file, no constants |
| The weighted norm of 4.2 as an adequate class | GUESSED |
| (C4) for the soft ties of Q2 | ARGUED, with GUIDE support from row 950 |
| Step counts of 5.1; the best-case floor 30 to 100; the kernel budget 1e9 gates a row | GUIDE and GUESSED, as marked there |
| Obstructions (O-a) to (O-d) | (O-a) GUIDE; (O-b) theorem for hard boundary values (CA-FAIL), ARGUED for Q2; (O-c) from on-file costs; (O-d) PROVED (TW, LD-1 and GA are group-blind) |
| (BASE-K2), T1, T2, (CM) and (DR) on the order-one part, the seed, the mass gap | OPEN |

What this row adds to the file: the consumer of a block chain in the form of sixteen masses with (PUR-io);
a named self-similar exact map with its twist-wise carry; the abelian control of that map; the one-step
statement with its three clauses; the split of the band into a weak part that needs one uniform theorem and
an order-one part that needs certificates; and the count that makes the floor of the weak part the first
thing to size. What it does not add: any step, any class shown closed, any method for the order-one part.

## 11. Result

RESULT: Row 1468 (Claude Fable 5.2 high, Mac mini worker 1; author only, checked by no one; hand arguments, no numeric run because free memory stayed at 38 to 47 percent, no Lean, no code committed). The K-II tool is designed as a specification and is NOT buildable today. (1) Design: the map Q2 (block side 2, corner bases, the Sussman-Alpoge contour mean over 384 contours a bond, von Mises-Fisher kernel of strength a x); PROVED by hand: Lemma TW (Q2 carries each of the sixteen twisted masses exactly), Theorem K2 (given the same for the release's kernel, SKETCHED: (BASE-K2) + (STEP_k) + (END) give purity at least 457/625 at infinitely many least roots, hence (M-io-exists)), Proposition GA (for the Gaussian abelian model the readout of Q2 is exactly x' = 2^(d-4) x at every strength, so in four dimensions every drift is non-Gaussian and the abelian step is marginal; five dimensions doubles). One step must satisfy (K2-STEP): a tube of local rules around a computed centre maps into the next tube with (DR) x' at most x - delta_0, (TR) a bounded radius inside the K7 margin, (WR) bounded wrap error; carried: a torus-free quasi-local rule in a field-weighted norm (GUESSED adequate), with requirements (C1) to (C6); U(1), Villain U(1) and 5D fail at (DR), and the exact identities of the step (TW, LD-1) are group-blind, so they pass (t6) as non-mechanisms. (2) Sizing: the band splits into a weak part that needs ONE uniform theorem (the release's floor is above 2^1600, so step certificates there are excluded by count, GUIDE), an order-one part of 100 to 400 steps in the best case (GUESSED floor 30 to 100), and an end; the smallest piece of one order-one step on file (the eight-link enclosure, 6.5e14 gates) is about 1e5 to 1e6 Lean rows, so no finite part of an order-one step is a `decide` or `norm_num` check, and no representation on file gives a closed class there. (3) First buildable component: the Lean row `K2Chain` (Fact PUR algebra, the 24,576-contour sign rule of Lemma TW by `decide`, Theorem K2 abstractly), decisive only for the map's exact carry; it does not test the wall. (4) No obstruction to the existence of a step is proved; excluded for stated classes: step certificates above the release's floor (count), unweighted suprema over coarse fields (CA-FAIL for hard boundary values; ARGUED for Q2's soft ties: a central pi-flux coarse field leaves a global colour rotation and an ordering spin), the five certificate kinds of 5.2 (cost), exact identities as mechanism. Open: (BASE-K2) on rectangular twisted tori, T1 (a weak-coupling step with a floor of human size), T2 (the order-one part: no method, no first lemma), (END-K2) with numbers, the seed, the mass gap. Next rows: a cross-provider check of this file (TW, K2 with Remark (ii), GA, the counts); `gap-k2-floor-sizing` (the smallest floor of a small-block weak-coupling step: at most 100 keeps K-II alive with at most 400 certified steps, at least 10^4 or structural closes K-II by step certificates on the record).
