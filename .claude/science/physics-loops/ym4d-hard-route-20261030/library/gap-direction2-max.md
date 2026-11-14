lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-15T03:45Z

# Row 970, gap-direction2-max: direction on the crux after row 968

Author: Claude Fable 5.2 (max), Mac mini worker, as AUTHOR (direction). Pinned at commit 61049a444.
Research-stage working state. Nothing here is checked by another model. Nothing here is a public claim.
Labels used: PROVED (written argument, not yet checked), CONDITIONAL (on named inputs), GUIDE (numeric, no proof weight), OPEN.

## Status log (newest last; times from `date -u`)

- 2026-11-14 15:45Z. File created. Plan below. No result yet.
- 2026-11-14 16:00Z. Section 1 (inputs) and Section 2 (question 1: NOT a port) written.
- 2026-11-14 16:25Z. Section 3 (question 2) written, with Lemma SUB: the supremum form contains the frozen-slice
  statement of rows 950 and 952, so it is already refuted at GUIDE level at beta 2.5 to 2.6. Working notes for the
  next sections are at the end of Section 3 (3.6).
- 2026-11-14 16:35Z. Section 4 (ranking of three attacks) written. Top attack: A1, the tie test of the flow forms.
- 2026-11-14 16:45Z. Section 5 (stage 1 of A1: Theorem QUOT, Proposition ROTOR) written.

## Plan (eight steps, one per response)

1. Inputs. Read rows 947, 954, 960, 965, 968 and `library/gap-status-1113.md`. Write the exact statements of
   (LSI-J-seed), (TILT-COV-sup), (LOC-COV) and what consumes them. Section 1.
2. Question (1), port or new input. Search the Sussman-Alpoge text (sa-index, outline copy) for small-field cluster
   bounds and one-block decay that would give (TILT-COV-sup) or (LOC-COV) at the seed scale. Quote lines. Section 2.
3. Question (2), circularity. Does (LOC-COV) on the seed box need the gap of a larger box? Proof or counterexample
   of the dependence. Section 3.
4. Question (3), ranking. At most three attacks, each with fact test and refutation test, cheapest first. Section 4.
5. Question (4), stage 1 of the top attack. Section 5.
6. Question (4), stage 2. Section 6.
7. Question (4), stage 3, or the refutation test if a stage fails. Section 7.
8. Summary table of verdicts, what stays open, RESULT line. Section 8.

## 1. Inputs, exact statements, duplicate check (READ; no new claim)

**1.1 Read.** FINISH rows 947, 954, 960, 965, 968 in full. `gap-avgcurv-max.md` (row 968) Sections 1-8 in full.
`gap-status-1113.md` Sections 1 and 6. Rows 969 (check of 968, HELD) and 971 (literature on the tilted covariance,
queued, no output at this commit).

**1.2 Objects (row 968, 1.1 and 3.1; quoted in short).** B is a periodic spatial box with L links. M = (S^3)^L in R^N,
N = 4L. V(x) = -beta sum_p (1/2) tr x_p. T_0(x, w) = e^(-V(x)/2) e^(beta <x, w>) e^(-V(w)/2) in temporal gauge. Omega is its top
eigenfunction. m(dw) = e^(-V(w)/2) Omega(w) dw. pi_theta(dw) = e^(<theta, w> - Lambda(theta)) m(dw) for theta in R^N; the one-step law
of the vacuum chain is pi_(beta x). J(dx, dw) = m(dx) e^(beta <x, w>) m(dw)/Z is the two-slice vacuum law. For s in (0, 1/beta):
s' = 1/beta - s, c = s s'/(s + s'), q~ = x/s + w/s', and for 0 <= b <= beta, phi in R^N:
  J_(b,phi)(dx, dw) = e^(b <x, w> + <phi, q~>) m(dx) m(dw)/Z_b(phi).
At b = 0 this is the product pi_(phi/s) x pi_(phi/s').

**1.3 The three statements of the row.**
- (LSI-J-seed)_a (row 947): the log-Sobolev constant of J on gauge-invariant functions obeys alpha_J >= 2 beta K_a on
  one box, K_a = (C_beta + 3 log a)/(a - 2). On the box (a; (4a)^3) of row 960: K_30 = 0.811.
- (TILT-COV-sup) (row 968, 3.3): Var_(J_(b_t,phi))(<z, q~>) <= kbar_(s,t) |z|^2 for every phi in R^N and every z orthogonal to
  the gauge orbit of phi, with b_t = t/(s s'), 0 <= t <= c. A bound kbar that is uniform in the box gives the seed for
  some a (Theorem POL-BR, CONDITIONAL on BBD Theorem 3.6 and Theorem BR).
- (LOC-COV) (row 968, 6.3): K_s(y) >= diag_l(k_l(y)) on horizontal vectors, with k_l >= rho off a set Bad_l and
  k_l >= -D on it. Here K_s(y)(z, z) = |z|^2/c - Var_(pi_(y/s))(<z, x>)/s^2 - Var_(pi_(y/s'))(<z, w>)/s'^2. So (LOC-COV) is a bound
  of the covariance of the tilted law pi_theta by a diagonal form, at typical tilts with rare exceptions. With the
  capacity bound (CAP)_l it gives a gauge-invariant Poincare constant of nu_s.
Reading used below. m is the law of the boundary slice of the half-infinite cylinder B x {0, 1, 2, ...} (half
weight on the boundary plaquettes). pi_theta is that law with a linear field theta on the boundary links.

**1.4 Chain to the consumer (rows 931, 947, 960, 968).** (TILT-COV-sup) box-uniform -> (LSI-br)_s -> (HC-vac)_alpha ->
X(2m + 2; B) <= 72 beta |B| e^(-2 alpha m) -> the seed on (a; (4a)^3) when alpha >= K_a -> Theorem S. Necessary sizes: m_G >= K_a (row
954), and kbar >= 2 beta log(1/E_1(B)) (Lemma NEC, row 968).

**1.5 Duplicate check (rule 0a).** `grep -n -i -E "TILT-COV|LOC-COV|ABS-flow"` on `open-core.md`, `l17c.md`,
`open-registry.md`: no hit. FINISH rows with a hit: 968 (source), 969 (its check, HELD), 970 (this row), 971
(literature, reading only). Library files with a hit: `gap-avgcurv-max.md` only. So no other row attacks
(TILT-COV-sup) or (LOC-COV). Row 971 reads the literature on them; this row does not repeat its search.
Prior GUIDE evidence that bears on the supremum form, found in the lane notes: rows 950 and 952 report that the
one-step law at a frozen pi-flux slice orders its colour direction near beta 2.4 to 2.5. Section 4 reads them.

**Credit.** Ethan Sussman and Levent Alpoge (with Claude and Codex as authors of their text): the account, its
transfer frame and its renormalisation-group bounds, read in Section 2. Rows 931, 941, 947, 950, 952, 954, 960, 965,
968 (Claude Fable 5.2 and Claude Opus 5.5): the statements above. Bauerschmidt, Bodineau, Dagallier; Chen, Eldan:
the criteria behind Theorem POL-BR.

## 2. Question (1): is (TILT-COV-sup) or (LOC-COV) at the seed scale a port? Answer: NO (READ, with one PROVED lemma)

Kind of result: reading of their text, plus a comparison. Source: Ethan Sussman and Levent Alpoge, complete account
CA-II (`theorem_0_complete_account_raw_II.tex`, commit 31a47c543775, fetched to `/tmp/gap-direction2-970/sa/`, not
committed), found through `sa-index/ca-full/index.tsv`; CA-I and outline lines as read by row 837
(`gap-finishline-opus.md` L44-87), re-used here and not re-read.

**2.1 What they prove that has the shape of (TILT-COV-sup) and (LOC-COV).** CA-II Section 8.3, in the chapter
"A two-point witness of non-triviality: clause (iv)" (heading at CA-II L68374).
- The class (CA-II L83837-83866, items (i)-(vi)). "S denotes the class of windowed Gibbs measures": sites X with a
  metric; a window, "K_x in R^n is an open bounded convex set"; the density is 1_K e^(-Phi) with
  "Phi(y) = (1/2)<y, Q y> + <h, y> - P(y)", "Q is real symmetric with q_- 1 <= Q <= q_+ 1 and q_- > 0", "the vector h lies
  in R^(n|X|)" with no bound on it; "P'' has operator norm at most varpi ... The smallness condition of the class gives
  varpi <= q_-/4, and we put m := q_-/2"; and (vi): the conditional law given y_S "is again a member of S, with the
  same constants".
- Lemma 8.3 `lem-correlation-decay` (CA-II L83869-83900; the index marks it PROVED; it assumes the Helffer-Sjostrand
  representation, stated inside the lemma). For mu in S:
  |Cov_mu(F, G)| <= (2/m) sum over x, x' of e^(-nu dist(x, x')) ||d_x F|| ||d_x' G||.
- Proposition 8.3 `prop-lipschitz-stability` (CA-II L81162-81200): for a Hamiltonian that is "coercive for phi" with
  lambda = lambda_A - eps_0 > 0, the mean of a Lipschitz function moves by at most (l_G/lambda) x (weighted size of the change of
  the linear term and of grad P). `cor-subgaussian-tails` (CA-II L81804-81850, read by the row 944 lane) tilts the
  linear term.
- Where they use it: `cor-extracted-covariance` (CA-II L83289): "Fix a level j with K - s <= j <= K and a clean branch
  of the Gaussian extraction". So the class is met by the fluctuation variables of one of the last s steps before
  first passage, in a small-field ("clean") branch. The decay of the propagators themselves is CITED from Balaban
  (`5.8:prop-local-decay`, CA-II L54464: CMP 99b (3.42)-(3.45), Theorems 3.1, 3.3; CMP 102b (71), (73)); the kernel decay
  of the fluctuation form is `5.2:cor-kernel-decay` (CA-II L10009, PROVED in their index).
Reading. For a member of S the bound holds for every linear term h and every conditioning. Taking F = G linear,
it gives Cov_mu <= (2/m) x (a kernel with exponential decay), uniformly in h. That is exactly a (TILT-COV-sup) with a
(LOC-COV)-type local kernel, for that class. So the account does contain the statement, at weak coupling, for
one block step. I credit it as the model of what (LOC-COV) asks.

**2.2 Lemma CLASS (PROVED, hand): the three places where the seed-scale law leaves their class.** Let mu be a
member of S. Then (a) mu is carried by a product of convex sets and Hess Phi >= q_- - varpi >= (3/4) q_- there; (b) the
bound of 2.1 is a consequence of (a) alone in its covariance form: Cov_mu <= (4/(3 q_-)) Id for every h (Brascamp-Lieb,
RECALLED); (c) so a law to which 2.1 applies with box-independent constants has a covariance that is bounded
uniformly in the box and in all linear tilts, in the coordinates y.
For the laws J_(b,phi) of the seed scale each of the three inputs fails:
- (W) Window. The link variable ranges over all of S^3. The lane's GUIDE value of the plaquette at beta 2.3 is 0.60
  (row 968, 7.5), so 1 - (1/2) tr U_p is of order 0.4: there is no small-field window that carries the mass. In the
  account the complement of the window is paid by e^(-c p_0(g_k)^2) with p_0(g) = A_0 (log g^(-2))^(p_0) (SA L17257, L32642-32646, read by
  row 837): a small number only when g is small.
- (Q) Coercivity q_- > 0. In the account q_- comes from the block-average constraint of one step: the fluctuation
  form is the Hessian of the action plus a times Q^* Q (CA-II 5.2, `def-rim-datum` L8421-8480 and L9030-9104, read by the
  b99-w lane). The law m has no constraint: it is the full boundary law, all scales integrated. Its quadratic part
  on horizontal vectors has modes down to the box momentum. PROVED consequence: in the Gaussian model FP of row 929
  the sharp q_- on the box (a; (4a)^3) is the lowest mode, omega_min < 1.58/a (row 968, 4.2), against the needed K_a > 12.5/a.
  So a coercivity that is uniform in the box cannot come from the quadratic form. It would be the mass.
- (P) Smallness varpi <= q_-/4. At beta 2.3 the largest horizontal eigenvalue of the Wilson Hessian is 9 to 11 against
  Ric = 2 (GUIDE, row 957), and the one-link tangential curvature is negative near the origin for beta > 2 (PROVED, row
  968, 5.2). The non-quadratic part is not a perturbation.
Proof of (a)-(c). (a) is items (ii)-(iv) of the class. (b) is the Brascamp-Lieb inequality for a density e^(-Phi) with
Hess Phi >= lambda on a convex set: Var(<z, y>) <= |z|^2/lambda. (c) follows. QED

**2.3 What the account says at and after first passage (READ by row 837; lines re-used, not re-read here).**
- CA-I L2556-2560: "No statement about the laws of the block variables is a clause of the present theorem".
- SA L31871-31882: "Nor does polynomial clustering establish a mass gap ... A positive spectral gap requires an
  estimate that excludes spectral support in an entire interval above the vacuum. That question remains separate".
- CA-I L2610-2620, (iii-b): for the per-ball bound, "no decay in d is asserted".
- The running coupling stays in (0, gamma_H] down to first passage (CA-I L2533-2545), and gamma_H is small and not
  explicit. The seed box is at order-one coupling, many steps past first passage (row 837; `gap-status-1113.md` 1.1).

**2.4 Verdict on question (1).** NOT a port. The account proves the tilt-uniform local covariance bound for
its class S: one block step, a convex small-field window, coercivity from the block-average constraint, and a
perturbation below q_-/4. Its estimates stop at first passage with g <= gamma_H, and it asserts no block law and no
decay there. At the seed scale all three hypotheses (W), (Q), (P) fail, and (Q) uniform in the box is the gap
itself. So (TILT-COV-sup) or (LOC-COV) at the seed scale is a new input. What the account does give is the
template: where a constraint supplies coercivity, tilt-uniform locality follows from convexity (their Lemma 8.3).
Section 4 asks whether any constraint of that kind can be put into the two-slice flow.
What this reading does not show. I read Section 8.3 and the index titles. I did not read CA-III. A bounded
search is not a proof of absence; the index (1,647 statements, 43 with "decay" in the title) has no statement at
order-one coupling.

## 3. Question (2): is the reduction circular? Answer: NO larger box is needed; the supremum form is strictly stronger than the gap, and it fails where a frozen slice orders

**3.1 Proposition OBJ (PROVED, one line).** (TILT-COV-sup), (LOC-COV), (LSI-J-seed) and the seed on (a; B) are
statements about the one operator T_B: they read B only through m = e^(-V/2) Omega and the kernel e^(beta <x, w>). No
larger spatial box occurs in any of them. The time direction occurs in full: m is the boundary law of the
half-infinite cylinder over B.

**3.2 Lemma SLAB (PROVED): the infinite time extent needs no gap.** Let Omega_n := T^n 1/||T^n 1||_2 and
m_n := e^(-V/2) Omega_n, the boundary law of the slab of n slices with a free far end. If (TILT-COV-sup) holds for
every m_n, n >= n_0, with one bound kbar, then it holds for m with the same kbar.
Proof. T has a continuous strictly positive kernel on the compact space M, so T^n 1/lambda_0^n converges uniformly to
<Omega, 1> Omega (Jentzsch's theorem, RECALLED; no rate is used), and <Omega, 1> > 0. So Omega_n -> Omega uniformly, and for each fixed
(b, phi, z) the variance under J^(n)_(b,phi) converges to the variance under J_(b,phi) (bounded integrands on a compact
space). A supremum of limits is at most the lower limit of the suprema. QED
Reading. A proof may work on slabs of every length, with a free end, and never use the rate of convergence
in n. The rate is E_1(B), the conclusion. So the dependence on the time extent is real (all n are needed), and
it is not circular.

**3.3 Proposition DEP (counterexample of the dependence; PROVED for FP given row 968, 3.3 (i) and 4.2).** In the
Gaussian mode model FP the laws J_(b,phi) are Gaussian with a covariance that does not depend on phi. So
(TILT-COV-sup) holds on every box B with its exact constant kbar(B), finite, and kbar(B) grows with the box, because
the lowest mode omega_min(B) tends to 0. On no larger box does FP have a gap bounded below. So the truth of
(TILT-COV-sup) on B, for one B, neither needs nor gives a gap on a larger box. What carries the content is
the size of the constant: by Lemma NEC, kbar >= 2 beta log(1/E_1(B)) on the same box, and through the seed and
Theorem S a constant of seed size gives the gap on all larger cubes. That is the forward chain, not a circle.

**3.4 Lemma SUB (PROVED): the supremum form contains the frozen-slice statement.** For every s in (0, 1/beta), every
u in M and every z orthogonal to the gauge orbit of u:
  kbar_(s,0) >= Var_(pi_(beta u))(<z, w>) / (s'^2 |z|^2).
Proof. At t = 0, b_0 = 0 and J_(0,phi) = pi_(phi/s) x pi_(phi/s'). Take phi = s' beta u. The gauge group acts linearly, so the
orbit of phi is s' beta times the orbit of u, and z is orthogonal to it. The two factors are independent, so
Var(<z, q~>) = Var_(pi_(phi/s))(<z, x>)/s^2 + Var_(pi_(beta u))(<z, w>)/s'^2. Drop the first term. QED
pi_(beta u) is the one-step law of the vacuum chain at the frozen slice u. Its covariance on horizontal vectors
is the first-step electric susceptibility of rows 944, 950, 952 (their E_l is the imaginary part of w_l u_l^(-1),
linear in w). So (TILT-COV-sup) at t = 0 implies (SC-hor) of row 950 with C = s'^2 kbar_(s,0).

**3.5 Consequence (GUIDE, from the runs of rows 950 and 952; no new run).** Row 950, layered pi-flux slice u_xy,
top eigenvalue lambda of the one-colour first-step covariance at its predicted horizontal mode: beta 2.3: 2.03,
2.55, 2.51, 2.46 at L = 4, 6, 8, 10 (saturates); beta 2.4: about 8 (saturates); beta 2.5: grows like the volume for
L = 4 to 20; beta 2.6: 4.19 at L = 4, 22.62 at L = 8, growth to L = 12. Row 952: at u_xy with a flat colour holonomy
the tie is between gauge-inequivalent states and the variance grows like 0.06 L^3 to 0.10 L^3 at beta 2.6. By Lemma
SUB, at the mid-slice (s' = 1/(2 beta)): kbar_(s,0) >= 4 beta^2 lambda, that is 53 at beta 2.3, about 184 at beta 2.4, and no
box-uniform value at beta 2.5 and 2.6 on the boxes run. The zero-field value is 2 beta^2 = 10.6 at beta 2.3.
**So a box-uniform (TILT-COV-sup) is REFUTED at GUIDE level at beta 2.5 and 2.6 at the scale t = 0, for every s.**
At 2.3 and 2.4 it is not refuted by this slice, with a constant at least 5 to 17 times the zero-field value.
Limits. The runs used slabs of 6 slices and one family of slices. Only t = 0 is covered: Theorem POL-BR reads
the integral of kbar over t, and a spike at one t costs nothing. Persistence for t > 0 is ARGUED only: the
coupling b <x, w> is invariant under the symmetry that makes the tie, so an ordered phase at b = 0 should persist
for small b. Row 968 tested the uniform tilt only (its 7.2-7.5) and did not see this family.

**3.6 Verdict on question (2).** Not circular. (i) No larger spatial box enters (3.1). (ii) All time extents
enter, with no rate (3.2). (iii) The supremum form is not equivalent to a gap. It implies the gap of the same
box (Lemma NEC). It does not follow from a gap: FP has it without a uniform gap (3.3), and at beta 2.5 to 2.6 the
GUIDE says SU(2) lacks it although nothing suggests that the gap closes there (3.5). (iv) What (LOC-COV) "needs"
is not a gap of a larger box. It needs the absence of long-range order of the boundary layer of the half-space
lattice at every linear tilt. That is a statement about a different system (a gauge theory with a frozen
link field), and the frozen-slice runs say it is false in the upper part of the window.
Working notes for Sections 4 to 7 (not yet written out; kept here so that an error does not lose them).
(N1) For gauge-invariant F the Hessian in orbit directions is forced: Hess log F(X phi, h) = <X grad log F, h>. This
gives a quotient form of Theorem POL-BR with the gain Q_phi(z) = sum_alpha |X_alpha z|^2. For a rigid SO(3) frame mode
(the zero mode at u_xy) the gain cancels the divergence exactly: 2 Var - Q = -(2/rho^2) h^2/sinh^2 h <= 0. Goldstone
waves of the frame are not cancelled. (N2) Two-phase model: J = (delta_a + delta_(-a))/2 along one direction. Then
V_t = -log cosh(a phi) - a^2 t/2 for all t, the test function tanh(a phi) is invariant under the flow, the supremum
form needs kbar >= a^2 and the averaged form (ABS-flow) needs kap >= a^2/4. So a discrete tie between
gauge-inequivalent states (row 952) kills every flow criterion that is uniform over test functions, although
the true constant is not affected (mass flows around the tie). (N3) The seed reads the inequality only along
the functions of Theorem BR's proof started from one-step kernels; their Fisher information sits at typical
tilts. (N4) A tilt that freezes the x- and y-links leaves a layered O(4) model of z-links at coupling at
least beta: its susceptibility bounds kbar from below at every beta, box-uniformly but hugely.

## 4. Question (3): three attacks, cheapest first, each with its fact tests and its refutation test

Idea inventories checked before ranking (rule 0a): `gap-next3-max.md`, `gap-brainstorm-max.md`,
`gap-brainstorm2-max.md`, `gap-constraints-max.md` were not re-read in full; I grepped the lane for "TILT-COV",
"LOC-COV", "ABS-flow" (Section 1.5) and for the frozen-slice results (rows 944, 950, 952). A1 uses those results; it
is not a new run. A3 is an existing open item and is named as a match, not attacked.

**A1 (cheapest). Decide the flow forms at their weakest point: a tie at one tilt.**
- Statement attacked: a box-uniform (TILT-COV-sup), its quotient form (Section 5), and the averaged form
  (ABS-flow) of row 968, 7.1. All three ask for one rate that serves every test function.
- Method: (i) Lemma SUB (Section 3.4) links the supremum form to the frozen-slice runs. (ii) For gauge-invariant
  test functions, find the exact gain from the gauge orbit and see which ties it removes (Section 5). (iii) Solve
  the two-phase model exactly and read off what a tie between gauge-inequivalent states costs each form
  (Section 6). No run is needed for the upper part of the window.
- Fact tests. FP: Gaussian, the covariance does not depend on the tilt, no tie; the forms hold with the exact
  constant and fail only the rate (row 968, 4.2): pass. Compact U(1): row 950's control has a tie at u_xy
  (charge conjugation; 41, 140, 332 at L = 4, 6, 8, the volume ratio), so the forms fail for U(1), as Lemma NEC
  demands: pass. Frozen Q_8, 2T: ties are generic for a finite group at large beta; nothing is claimed: pass.
  SMALL-BOX: a tie costs a^2 of the order of the volume, bounded on a fixed box, and it grows with beta on that box
  (row 950 at beta 6.0: 11.9, 38.7 at L = 4, 6): consistent with Lemma NEC: pass. K7: a bulk coexistence is a tie of
  m itself; the forms must fail there and do: pass. FT-FK: the kinetic-only model is a product, has no tie, and
  the forms hold: pass.
- Refutation test of the forms: the frozen-slice runs. Done at beta 2.5 and 2.6 (rows 950, 952). Open at 2.3 and 2.4:
  a tie search over slices of reduced symmetry on sides 8 to 16 (GUIDE, about one to two hours with the slab
  code of `guide/lane952`). Criterion: growth of the tie-mode variance by more than 1.25 per step of the side.
- What success means: the flow forms are dead in the upper window, and the lane stops spending on them.

**A2. The inequality along the trajectories of one-step kernels (typical tilts only).**
- Statement: (LSI-traj), stated in Section 7. Proposition HC applies (HC-vac) only to the functions p_1(u, .)
  (`gap-direction-max.md` L309-311), and Theorem BR applies the log-Sobolev inequality of nu_s only to powers of
  their bridge interpolations. A tie at an atypical tilt carries an exponentially small share of the Fisher
  information of these functions, so the two-phase obstruction of A1 does not apply (ARGUED).
- Fact tests. FP: the trajectory functions are Gaussian densities and the rate is the exact photon rate: FP
  fails the seed rate only: pass. Compact U(1) in the Coulomb phase: must fail; p_1(u, .) has a component on the
  lowest photon mode, so the trajectory rate is at most the photon rate: pass. Q_8, 2T: no gradient, the
  bridge form still makes sense (row 968, 4.3); nothing claimed. SMALL-BOX: the trajectory rate is at most E_1,
  because the average over u of p_1(u, .) components on the first excited state does not vanish (the trace);
  so the box size must enter: pass. K7: at a bulk coexistence a typical start u lies in one phase and the
  trajectory must cross to the other: the rate dies, as it must: pass. FT-FK: an argument on the kinetic
  part alone cannot give it; the model enters through m at typical tilts: pass.
- Refutation test: GUIDE, nested sampling. Sample a vacuum slice u, the chain from u, and the bridge points;
  estimate the entropy of the law of the bridge point at step k against nu_s, or directly X(2m + 2; B) of
  Proposition HC, on sides 8 to 16; compare its decay rate in m with K_a. Decay slower than the seed rate
  refutes the route at that beta. Cost: several hours; the estimator of a relative entropy in high dimension is
  the difficulty, so use the chi^2 form X on small boxes first.
- No proof method is known for it at order-one coupling. It is not smaller than (LSI-br-seed) in any proved sense.

**A3. (LOC-COV) at typical tilts with a local recovery of bad regions.**
- This is the large-field problem of the renormalisation group at order-one coupling. The account's class S
  (Section 2.1) is the template: locality follows from convexity where a block constraint gives coercivity.
- Match (rule 0a): the lane's open item EXIT and the hand-off Theorem HO (rows 846, 850, 861; `gap-status-1113.md`
  1.2, "The hand-off") ask for exact block steps past first passage that land in an explicit zone. A3 is that
  item in the language of covariances. I do not attack it.
- Fact tests. FP: the conditional covariance at typical tilts is the same Gaussian, with the soft photon modes:
  (LOC-COV) fails with rho of order 1/b: pass. Compact U(1): the same through the photon: pass. SMALL-BOX: a
  local diagonal bound with rho uniform in beta on a fixed box would give a gap uniform in beta: so rho must
  carry the box size: pass only if the statement is made on boxes above the confinement length.
- Refutation test (GUIDE, row 968, 7.3, second test, not run): the top horizontal eigenvalue of
  Cov(x | y)/s^2 + Cov(w | y)/s'^2 at typical bridge points y against 1/c. At the mid-slice the threshold per
  slice is 1/(2 beta) = 0.217 at beta 2.3; row 968's uniform-tilt values at kap = 4.0 are 0.18 to 0.20 (its table 7.5),
  so the outcome is not predictable by hand.

**Ranking.** A1 first: it costs no run and it decides whether the flow forms are worth any further work. A2
second: it is the form that A1 leaves standing. A3 third: it is the known hard problem.

## 5. Question (4), stage 1 of A1: the gain from the gauge orbit (Theorem QUOT) and the rigid frame (Proposition ROTOR)

Kind of result: proof of a step that row 968 left unused (the dropped Hessian term), for gauge-invariant test
functions. It generalises row 968's Proposition ANG from one link to the whole gauge orbit of the tilt.

**5.1 Lemma FH (forced Hessian; PROVED, hand).** Let a compact Lie group G act on R^N by orthogonal maps, with Lie
algebra g acting by skew-symmetric matrices X. Let F > 0 be smooth and G-invariant. Then at every phi:
(a) <grad log F(phi), X phi> = 0 for X in g.
(b) Hess log F(phi)(X phi, h) = <X grad log F(phi), h> for every h in R^N. In words: the Hessian applied to the orbit
    vector X phi is the vector X grad log F(phi).
(c) If X phi = 0 then X grad F(phi) = 0.
(d) Let e_alpha = X_alpha phi, alpha = 1..d, be an orthonormal basis of the tangent space of the orbit at phi, and psi := F^(1/2).
    Then (1/4) F |Hess log F|^2 >= Q_phi(grad psi), where Q_phi(z) := sum over alpha of |X_alpha z|^2.
Proof. (a) Differentiate F(e^(tau X) phi) = F(phi) at tau = 0. (b) (a) holds at every point; differentiate it in the
direction h: Hess log F(h, X phi) + <grad log F, X h> = 0, and X is skew. (c) If X phi = 0, then e^(tau X) fixes phi and
F o e^(tau X) = F gives e^(-tau X) grad F(phi) = grad F(phi) for all tau. (d) The squared Hilbert-Schmidt norm of a symmetric
matrix H is at least sum_alpha |H e_alpha|^2 for an orthonormal family. By (b), H e_alpha = X_alpha grad log F = 2 X_alpha grad psi/psi, and
F = psi^2. Q_phi does not depend on the choices: by (c) the form (X phi, Y phi) -> <X z, Y z> is well defined on the
tangent space for z = grad psi(phi), and Q_phi(z) is its trace. QED

**5.2 Theorem QUOT (CONDITIONAL on BBD Theorem 3.6 as read in row 968, 2.1, and on Theorem BR).** Theorem POL-BR
of row 968 holds with (TILT-COV-sup) replaced by the weaker hypothesis
  (TILT-COV-quot): 2 Var_(J_(b_t,phi))(<z, q~>) - Q_phi(z) <= 2 kbar_(s,t) |z|^2
  for every phi and every z that is orthogonal to the gauge orbit of phi and obeys X z = 0 whenever X phi = 0.
Proof. In BBD's proof the hypothesis is used once, on the identity (their Lemma 3.10, C-dot = Id, psi = F_t^(1/2))
(L_t - d/dt)|grad psi|^2 = 2 Hess V_t(grad psi, grad psi) + (1/4) F_t |Hess log F_t|^2, where the last term is dropped. F_t is
gauge invariant (row 968, 2.1 (a)). Keep the part Q_phi(grad psi) of the last term (Lemma FH (d)); by FH (a), (c) the
vector z = grad psi(phi) is of the stated kind. With Hess V_t = -Cov (row 968, 3.1 (c)) the right side is at least
-2 Var(<z, q~>) + Q_phi(z) >= -2 kbar |z|^2. The rest of the proof is unchanged. QED
Check (one free link; G = SO(4) on R^4, r = |phi|). The orbit is the sphere of radius r, z is radial, X_alpha z = e_alpha/r,
so Q = 3/r^2. This is the forced part (n - 1)(F'/r)^2 of the Hessian of a radial function, n = 4.

**5.3 Proposition ROTOR (PROVED, hand; a model).** Rigid frame: the moment of q~ on a three-dimensional space is
R n with n uniform on S^2, and the tilt enters as e^(<D, R n>), D in R^3, with G_0 = SO(3) rotating D and n. For D != 0
put rho = |D|, z = D/rho, h = R rho. Then
  Var(<z, R n>) = R^2 (1/h^2 - 1/sinh^2 h),   Q_D(z) = 2/rho^2,   2 Var - Q_D(z) = -(2/rho^2) h^2/sinh^2 h < 0.
The supremum of Var over D is R^2/3. So the plain supremum form needs kbar >= R^2/3, and the quotient form
needs nothing, for every R.
Proof. E cos(theta) = coth h - 1/h and Var(cos theta) is its derivative, 1/h^2 - 1/sinh^2 h, with limit 1/3 at h = 0. The
orbit of D is the sphere of radius rho; the two unit tangent vectors are X_alpha D with X_alpha z = e_alpha/rho. QED
Reading. At the plain pi-flux slice u_xy the tie of row 950 is a colour frame: the stabiliser SO(3) of the
tilt rotates the pattern, R^2 is m_st^2 times the number of links, and the growth "like the volume" of row 950
is the zero mode R^2/3. Theorem QUOT removes exactly this mode. So the plain u_xy runs of row 950 refute
(TILT-COV-sup) and do NOT by themselves refute (TILT-COV-quot).
What stage 1 does not remove (ARGUED, not proved). (i) Long waves of the frame. A slow rotation of the pattern
is a gauge transformation of the slice w, not of the tilt, and the tilt gives it a stiffness of the order of
its strength. In an ordered phase its variance at the lowest momentum grows like L^2. Q_phi sums over orbit
directions of the tilt and gives a bounded gain for such a wave. (ii) A tie between gauge-inequivalent states
(row 952) is discrete: no orbit direction joins the two states, and Q gives nothing. Section 6 treats it.

