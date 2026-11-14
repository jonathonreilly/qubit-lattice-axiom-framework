lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-15T03:45Z

# Row 970, gap-direction2-max: direction on the crux after row 968

Author: Claude Fable 5.2 (max), Mac mini worker, as AUTHOR (direction). Pinned at commit 61049a444.
Research-stage working state. Nothing here is checked by another model. Nothing here is a public claim.
Labels used: PROVED (written argument, not yet checked), CONDITIONAL (on named inputs), GUIDE (numeric, no proof weight), OPEN.

## Status log (newest last; times from `date -u`)

- 2026-11-14 15:45Z. File created. Plan below. No result yet.
- Between 15:45Z and 16:12Z (clock read at 16:12Z; earlier entries of this log carried estimated times that ran
  ahead of the clock by up to 50 minutes, and I replaced them): Sections 1 to 7 written, in this order. Section 2:
  question 1, NOT a port. Section 3: question 2, not circular; Lemma SUB links the supremum form to the frozen-slice
  runs of rows 950 and 952, so it is refuted at GUIDE level at beta 2.5 to 2.6. Section 4: three attacks ranked; top
  attack A1. Sections 5 to 7: the proof attempt on A1 in three stages (Theorem QUOT and Proposition ROTOR;
  Proposition TIE; Lemma TRAJ and Identity MM).
- 2026-11-14 16:13Z. Arithmetic guard of the three model formulas run (7b): all criteria pass.
- 2026-11-14 16:36Z. GUIDE batch 7a done (16:16Z to 16:35Z): the order at u_xy persists at t = c/2 and t = c at beta 2.6,
  volume law to L = 12. Section 8 written. Batch 7c (the discrete tie at t = c) started.

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

## 6. Question (4), stage 2 of A1: what a tie between two states costs each flow form (Proposition TIE)

**6.1 The two-phase model.** One coordinate phi in R; the component of q~ on it takes the values +a and -a with
probability 1/2 each. The flow of row 968, Section 3, with C_t = t on [0, c): Z(phi) = cosh(a phi) and V_0 = -log cosh(a phi).

**6.2 Proposition TIE (PROVED, hand).**
(a) V_t(phi) = -log cosh(a phi) - a^2 t/2 and Hess V_t(phi) = -a^2 sech^2(a phi) for every t in [0, c). nu_t has density
    proportional to cosh(a phi) e^(-phi^2/(2 (c - t))): the equal mixture of N(+a(c - t), c - t) and N(-a(c - t), c - t).
(b) The test function G(phi) = tanh(a phi) is invariant under the flow: P_(0,t) G = G for every t.
(c) Supremum form: kbar_t >= a^2 for every t. The criterion then returns 1/gamma = (e^(2 a^2 c) - 1)/(2 a^2).
(d) Averaged form: every kap_t admissible in (ABS-flow) of row 968, 7.1, obeys kap_t >= a^2/4 for every t in [0, c).
    So the averaged form gains a factor 4 in the exponent and no more.
Proof. (a) A centred Gaussian of variance t maps cosh(a .) to e^(a^2 t/2) cosh(a .). The variance of the two-point
law with weights e^(+-a phi) is a^2 sech^2(a phi). The density of nu_t is e^(-V_t) times the Gaussian of variance c - t.
(b) P_(0,t) G (phi) = e^(V_t(phi)) times the Gaussian average of e^(-V_0) G = cosh . tanh = sinh(a .), which is
e^(a^2 t/2) sinh(a phi). Divide by e^(a^2 t/2) cosh(a phi).
(c) phi = 0 in (a); then 1/gamma = integral over [0, c] of e^(2 a^2 t) dt (row 968, 2.1).
(d) Put F = 1 + eps G in (ABS-flow) and keep the order eps^2 (F_t = 1 + eps G by (b)): 2 E_(nu_t)[a^2 sech^2(a phi) G'^2]
<= 2 kap_t E_(nu_t) G'^2 + E_(nu_t) G''^2. Here G' = a sech^2, G'' = -2 a^2 sech^2 tanh. With u = a phi, A = a^2 (c - t) and
M_k := integral of sech^k(u) e^(-u^2/(2A)) du, the three terms are 2 a^3 M_5, 2 kap_t a M_3 and 4 a^3 (M_3 - M_5)
(use the weight cosh and tanh^2 = 1 - sech^2). So kap_t >= a^2 (3 M_5/M_3 - 2). Last, M_5 >= (3/4) M_3 for every A:
sech^2 and e^(-u^2/(2A)) are both decreasing in |u|, so they are positively correlated under the probability
density proportional to sech^3 (Chebyshev's sum inequality), and the mean of sech^2 under that density is
(integral of sech^5)/(integral of sech^3) = (3 pi/8)/(pi/2) = 3/4 (reduction I_n = ((n - 2)/(n - 1)) I_(n-2), I_1 = pi). QED

**6.3 What the model says about the lattice (ARGUED; the transfer is not proved).**
- A tie is a tilt phi_0 at which J_(b,phi_0) is an equal mixture of two states A and B, and a unit vector e,
  horizontal at phi_0 and fixed by its stabiliser, on which <e, q~> is near +a under A and near -a under B. If A
  and B are gauge inequivalent, a gauge-invariant function can tell them apart, and on the line phi_0 + rho e the
  partition function is Z(phi_0) cosh(a rho) times a smooth factor. Then (a)-(d) apply on that line.
- Size. a^2 is the variance of <e, q~> at the tie. For row 952's slice (u_xy with a flat colour holonomy, beta 2.6)
  the first-step variance per unit |z|^2 is 0.06 L^3 to 0.10 L^3, so at the mid-slice a^2 is at least
  4 beta^2 x 0.06 L^3 = 1.6 L^3 (GUIDE; Lemma SUB). By (d) the averaged form needs kap >= 0.4 L^3 wherever the tie
  persists in t, against a zero-field value of 2 beta^2 = 13.5.
- Truth against criterion. In the model the measure nu_0 is bimodal and its true constant is small too. On the
  lattice the tie sits in a region of tilts of nu_t-measure e^(-const L^3) (a slice near u_xy is a large deviation),
  and mass can pass around it. So the true constant of nu_s need not feel it. The flow forms do feel it:
  they ask for one rate for all test functions, and a test function may sit on the tie (take 1 + eps chi G with a
  cut-off chi around phi_0). This is the exact place where "uniform over test functions" costs more than the
  truth.
- Open in this transfer: the persistence of the tie along t (ARGUED in 3.5), the cut-off construction, and
  the product structure near phi_0.

**6.4 Verdict of stages 1 and 2 on the flow forms (GUIDE for SU(2); PROVED for the models).**

| Form | Plain u_xy (colour frame, row 950) | u_xy with flat holonomy (discrete tie, row 952) |
|---|---|---|
| (TILT-COV-sup), row 968 | refuted at beta 2.5, 2.6 (Lemma SUB; growth like L^3) | refuted at 2.6 |
| (TILT-COV-quot), Section 5 | zero mode removed (ROTOR); long waves remain (ARGUED, L^2) | refuted at 2.6 (no orbit gain) |
| (ABS-flow), row 968, 7.1 | not decided | needs kap >= a^2/4 of order L^3 at 2.6 (TIE (d), ARGUED transfer) |

At beta 2.3 none of the three is refuted by these slices (row 950: 2.5 saturated; row 952: "at 2.3 nothing
grows"; at 2.45 row 952 is inconclusive). A box-uniform bound there would still carry a constant of at least
53 at t = 0 (Section 3.5), about five times the zero-field value.
Direction. A proof of the seed in the whole window cannot pass through any flow criterion whose rate is
uniform over test functions. What stays is the inequality for the functions the seed actually reads
(Section 7).

## 7. Question (4), stage 3: what the seed actually reads (Lemma TRAJ, Identity MM), and the form that stays

**7.1 Lemma TRAJ (PROVED by inspection of two proofs; an implication).** For u in M and k >= 0 let f_(u,k) := P^k p_1(u, .)
be the density used in Proposition HC, and U_(u,k,s)(y) := E[f_(u,k)(w) | y_s = y] its bridge interpolation (the function
u_s of Theorem BR, step (i)). Put
  (LSI-traj)_s: Ent_(nu_s)(phi^2) <= (2/alpha_s) integral of |grad phi|^2 d nu_s  for phi = U_(u,k,s)^(q/2), u in M, k >= 0, 1 < q <= 2.
If (LSI-traj)_s holds with (1/2) integral over (0, 1/beta) of alpha_s ds >= alpha, then X(2m + 2; B) <= 72 beta |B| e^(-2 alpha m).
Proof. Proposition HC (`gap-direction-max.md` L305-312) applies (HC-vac) to h = p_1(u, .) only. Theorem BR
(`gap-fc-max.md` L144-177) gets ||P^m h||_2 <= ||h||_(q') from m one-step bounds, applied to f = P^k h with exponents
between p_k and p_(k+1), all in (1, 2] (its step (v)). Each one-step bound uses (LSI-br)_s once, in step (iii),
for phi = u_s^(q(s)/2) with u_s the interpolation of f. QED
Note for the checker of rows 931 and 947 (not my file). (HC-vac) is stated for gauge-invariant h, and
p_1(u, .) is invariant only under a joint transformation of u and the argument. I read p_1 as the kernel of
the chain on gauge-invariant functions (the average of the kernel over the gauge group in one argument). I did
not re-derive Lemma HOT for that kernel; its upper bound can only improve under averaging.

**7.2 Identity MM (PROVED given BBD (3.44) and Proposition FLOW, both as read in row 968; the gradient formula is
proved here).** Let J' be a probability law on M x M with bounded density with respect to J, mu_s the law of the
bridge point under J', and phi_t = (1 - t/c) q + (c - t)^(1/2) xi the tilt of row 968, 3.1 (d). Then
  D(mu_s | nu_s) = (1/2) integral over [0, c] of E_(J')| E_(J')[q~ | phi_t] - E_J[q~ | phi_t] |^2 dt.
Proof. Given (x, w), phi_t is Gaussian with mean (c - t) q~ and covariance (c - t) Id. So the density l'_t of phi_t under
J' has grad log l'_t(phi) = E_(J')[q~ | phi_t = phi] - phi/(c - t), and the same holds for J. F := d mu_s/d nu_s = l'_0/l_0. The chain
(x, w) -> phi_0 -> phi_t is Markov, so P_(0,t) F = E_J[F(phi_0) | phi_t] = l'_t/l_t =: F_t, and grad log F_t is the difference of
the two conditional means. BBD (3.44): Ent_(nu_0)(F) = 2 integral of E_(nu_t)|grad F_t^(1/2)|^2 dt = (1/2) integral of
E_(nu_t)[F_t |grad log F_t|^2] dt, and F_t nu_t = l'_t. QED
(This is the mismatched-estimation identity for a Gaussian channel; the name is RECALLED, the proof is above.)
Reading. For J' the two-slice law of the chain started at u, the entropy that the route must contract is an
integrated mean-square difference between two estimators of q~: the one that knows the start u and the
stationary one. The average is over the tilts that the started chain produces. No supremum over tilts and
no test function occurs. This is the exact sense in which the seed reads typical tilts only.

**7.3 The form that stays (OPEN).** (LSI-traj-seed)_a: (LSI-traj)_s on the box (a; (4a)^3) with
(1/2) integral of alpha_s ds >= K_a. Strength: (LSI-br-seed)_a implies it (restriction of the class); it implies the
seed (7.1). Its necessary consequence, by row 947 (BR-ent) restricted to the same functions:
  (EC-traj): D(mu^(u,k+1) | nu) <= e^(-A) D(mu^(u,k) | nu), with both sides given by Identity MM.
Why the ties of Section 6 do not refute it (ARGUED). The test function of Proposition TIE sits on the tie.
The functions U_(u,k,s) are fixed by the dynamics. For a typical start u a tie region has an exponentially small
share of both sides of (LSI-traj). I did not prove this: U can be as large as e^(36 beta |B|) on atypical sets, so
"small share" needs a large-deviation estimate that I do not have.
Why I cannot prove it. It is entropy production along one trajectory at order-one coupling. Identity MM turns
it into a comparison of two posterior means at typical tilts; the difference of the two is the memory of the
start, and its decay in k is the mass gap seen in an estimation problem. No estimate in the account, and no
tool of rows 941 to 968, bounds it.

**7.4 Where the proof attempt on A1 ends.** Stage 1 (PROVED): the gauge orbit gives a gain Q_phi; it removes the
rigid colour frame. Stage 2 (PROVED for the model): a discrete tie costs the supremum form a^2 and the averaged
form a^2/4. Stage 3 (PROVED implication): the seed reads the inequality on the trajectory functions only, and
there the entropy is an average over typical tilts (Identity MM). What failed: no stage gives a bound for
SU(2). What is left: (LSI-traj-seed)_a, or the route change of A3.

## 7a. GUIDE test of the one caveat of Section 3.5: does the tie persist for t > 0? (criteria written at 16:16Z, BEFORE the batch)

Why. Lemma SUB covers t = 0 only, and Theorem POL-BR reads the integral of kbar over t. Persistence was ARGUED.
Object. The two-slice law J_(b,phi) itself at the mid-slice (s = s' = 1/(2 beta)), with phi = (kap/(2 beta)) u_xy, so that both
slices carry the tilt kap u_xy, and with the middle time-like coupling b. b = 0 is t = 0; b = beta/2 is t = c/2; b = beta is
t = c. Script `guide/lane970/twoslice_tilt.py` (plain numpy, temporal gauge, open time, 5 free slices on each side,
half weight on the end slices, heat bath with the Creutz sampler, hot start). Observable: row 950's mode
(momentum (pi, pi, 0), polarisation (1, -1, 0), one colour) on x, on w and on x + w:
lam_w = E (O_w^a)^2/(2 L^3), lam_sum = E (O_x^a + O_w^a)^2/(2 L^3). Then Var(<z, q~>)/|z|^2 = 4 beta^2 lam_sum.
Runs. beta 2.6; (b, kap) in {(0, beta), (beta/2, beta), (beta, beta), (beta, 2 beta)}; L = 4 and 8 (2000 + 12000 and 2000 + 10000 sweeps);
L = 12 for the two points with b = beta (1500 + 6000 sweeps). Errors from 10 blocks.
Smoke test (about 16:15Z, lock holder gap-direction2-970, L = 4, zero tilt, b = beta, 300 + 1000 sweeps): lam_w = 0.234(22),
lam_x = 0.247(26) against the exact Elitzur value 1/4; lam_sum = 0.80(9) against (1 + tau)/2 = 0.84 with the measured
tau = 0.677; 2.2 ms per sweep.
Verdict rules.
- (V0) Validity. At (b, kap) = (0, beta) the factor w is the one-step law pi_(beta u) of row 950. lam_w must agree with row
  950's 4.19 (L = 4) and 22.62 (L = 8) within 20 percent (their slab has 6 free slices, mine 5). If not, the
  run decides nothing.
- (V1) Persistence at (b, kap): G := lam_sum(8)/lam_sum(4). G >= 4: the tie persists there (GUIDE). G <= 1.5: it does
  not. Otherwise inconclusive. Full order gives 8.
- (V2) At b = beta: lam_sum(12)/lam_sum(8) >= 2 confirms growth (full order 3.375); <= 1.3 means saturation.
What it cannot show: boxes above 12, slabs thicker than 5, other tilts, the quotient form (this mode is the
colour-frame zero mode that Proposition ROTOR removes; the discrete tie of row 952 is not run here).

**7a results (GUIDE; batch 16:16Z to 16:35Z under the numeric lock, 71 percent memory free; logs
`guide/lane970/results.jsonl`, `batch.log`; 2.3, 10.5, 32.4 ms per sweep at L = 4, 8, 12).** beta 2.6. Entries: lam_w and
lam_sum with block errors. Bulk plaquette 0.666 to 0.670 in all ten runs (recalled 0.670).

| (b, kap) | scale | lam_w, L = 4 | lam_w, L = 8 | lam_sum, L = 4 | lam_sum, L = 8 | lam_sum, L = 12 | lam_sum(8)/lam_sum(4) | (12)/(8) |
|---|---|---|---|---|---|---|---|---|
| (0, beta) | t = 0 | 4.14(7) | 22.98(41) | 8.3 (= lam_x + lam_w) | 45.8 (= lam_x + lam_w) | | 5.5 | |
| (beta/2, beta) | t = c/2 | 7.32(4) | 52.28(21) | 28.81(15) | 208.7(8) | | 7.2 | |
| (beta, beta) | t = c | 8.39(3) | 60.51(19) | 33.32(12) | 241.3(7) | 784.8(3.0) | 7.2 | 3.25 |
| (beta, 2 beta) | t = c | 8.73(1) | 65.52(13) | 34.65(4) | 262.0(5) | 865.3(2.7) | 7.6 | 3.30 |

At b = 0 the two factors are independent, so lam_sum = lam_x + lam_w exactly; the raw sample value at L = 8 was
36.3(3.2), low by a slow cross term between two frames that do not see each other, and I use the sum.
Verdicts by the rules written before the batch.
- (V0) PASS: lam_w = 4.14(7) and 22.98(41) at (0, beta) against row 950's 4.19 and 22.62 (1.3 and 1.6 percent), with an
  independent code and a slab of 5 free slices against 6.
- (V1) The order PERSISTS at every point: the ratio is 7.2 to 7.6 at b = beta/2 and b = beta, against 5.5 at b = 0 and 8 for
  full order. Coupling the two slices strengthens the order (lam_w per slice rises from 4.1 to 8.4 at L = 4), and
  the two frames lock: lam_sum is 4 lam_w within 1 percent.
- (V2) Growth confirmed at t = c: 3.25 and 3.30 from L = 8 to 12, against 3.375 for full order. lam_sum is about
  0.45 L^3, so Var(<z, q~>)/|z|^2 = 4 beta^2 lam_sum is about 12 L^3 at the mid-slice (21,000 at L = 12), against the
  zero-field value of at most 4 beta^2 = 27.
So at beta 2.6 the plain supremum form fails at t = 0, c/2 and c with a volume law (GUIDE, sides 4 to 12): the
integral of kbar over t grows like L^3, and the caveat of 3.5 is removed for this slice. As said in 5.3, this
mode is the colour-frame zero mode that Theorem QUOT removes. The discrete tie is tested next (7c).

**7c. The discrete tie at t = c (criteria written at 16:36Z, BEFORE the run).** Slice u_phi of row 952, 1.4: u_xy with
every z-link equal to exp((phi/L) k), phi = pi/2. The same script with a tenth argument phi; outputs per colour.
Runs: beta 2.6; control (b, kap) = (0, beta) at L = 4; then (beta, beta) at L = 4, 8, 12.
- (W0) Validity: at (0, beta), L = 4, the colour-3 moment of the w slice within 20 percent of row 952's raw
  temporal-gauge moment 11.4, and colours 1, 2 below 1.5 (row 952: 0.51, 0.87).
- (W1) Discrete tie at t = c: the colour-3 value of lam_sum grows by a factor at least 4 from L = 4 to 8 and at
  least 2 from 8 to 12, while colours 1, 2 do not grow (ratio at most 1.5). Then an Ising-type tie between the
  states n = +e_3 and n = -e_3, which Proposition TW of row 952 shows to be gauge inequivalent, exists in the
  two-slice law at t = c (GUIDE). If colours 1, 2 grow too, the order is still a frame: inconclusive.
What it cannot show: the transfer of Proposition TIE (6.3), which needs the cut-off construction.

## 8. Status, answers, and the result

**8.1 Status table.** "PROVED" means proved by hand here by Claude Fable 5.2, not yet checked by another model.

| Statement | Where | Status |
|---|---|---|
| The account proves a tilt-uniform local covariance bound for its class S of windowed Gibbs measures (CA-II 8.3, `lem-correlation-decay`, L83869; class data L83837-83866), used at levels K - s <= j <= K on clean branches | 2.1 | READ (their text; credited to Sussman and Alpoge) |
| Lemma CLASS: a member of S is uniformly log-concave on a convex window; the seed-scale laws J_(b,phi) fail the window (W), the box-uniform coercivity (Q) and the smallness (P) | 2.2 | PROVED given Brascamp-Lieb (RECALLED); (W), (P) rest on GUIDE numbers of rows 957, 968 and on row 968, 5.2 |
| Question (1): (TILT-COV-sup) or (LOC-COV) at the seed scale is NOT a port | 2.4 | READ; a bounded search, CA-III not read |
| Proposition OBJ, Lemma SLAB: all statements live on T_B; every time extent enters, with no rate | 3.1, 3.2 | PROVED (Jentzsch RECALLED) |
| Proposition DEP: FP has (TILT-COV-sup) on every box and no uniform gap on larger boxes | 3.3 | PROVED given row 968, 3.3 (i), 4.2 |
| Lemma SUB: kbar_(s,0) >= Var_(pi_(beta u))(<z, w>)/(s'^2 |z|^2) for every frozen slice u | 3.4 | PROVED |
| A box-uniform (TILT-COV-sup) fails at beta 2.5 and 2.6 at t = 0, and at beta 2.6 also at t = c/2 and t = c with a volume law | 3.5, 7a | GUIDE (t = 0: runs of rows 950, 952; t > 0: new run 7a, sides 4 to 12, control against row 950 within 2 percent) |
| Question (2): not circular; the supremum form is strictly stronger than the gap of the same box | 3.6 | PROVED parts 3.1-3.4; the "strictly stronger" half is GUIDE |
| Three attacks ranked: A1 tie test of the flow forms; A2 the trajectory form; A3 = the lane's open item EXIT (match, not attacked) | 4 | direction |
| Lemma FH (forced Hessian of an invariant function) | 5.1 | PROVED |
| Theorem QUOT: Theorem POL-BR with the gain Q_phi from the gauge orbit | 5.2 | CONDITIONAL on BBD Theorem 3.6 (as read in row 968) and Theorem BR |
| Proposition ROTOR: a rigid SO(3) frame never violates the quotient form; the plain supremum needs R^2/3 | 5.3 | PROVED (model); arithmetic guard passes (7b) |
| Proposition TIE: in the two-phase model the supremum form needs a^2 and (ABS-flow) needs a^2/4, at every t | 6.2 | PROVED (model); arithmetic guard passes (7b) |
| Transfer of TIE to the lattice: row 952's discrete tie refutes all three flow forms at beta 2.6 | 6.3, 6.4 | ARGUED from GUIDE |
| Lemma TRAJ: the seed reads the log-Sobolev inequality only on powers of the bridge interpolations of P^k p_1(u, .) | 7.1 | PROVED implication, by inspection of Proposition HC and Theorem BR |
| Identity MM: the entropy of a trajectory law is the integrated mean-square difference of two posterior means, over typical tilts | 7.2 | PROVED given BBD (3.44) as read in row 968; guard passes (7b) |
| (LSI-traj-seed)_a, (LSI-br-seed)_a, (LSI-J-seed)_a, the seed; (TILT-COV-sup) and (ABS-flow) at beta 2.3 to 2.4 | 7.3 | OPEN |

**7b. Arithmetic guard of the three model formulas (GUIDE; criteria in the script header, written before the run).**
`guide/lane970/check_models.py`, log `check_models.log`, run at 16:13Z under the numeric lock, 71 percent memory free,
peak 163 MB. C1 (ROTOR, h = 0.3, 1, 3, 10), C2 (TIE (b) at five points, (d) for a = 1, 3 and three scales:
kap_min/a^2 = 0.796, 0.879, 0.971 and 0.440, 0.546, 0.811, all above 1/4, direct expectation against the M_5/M_3
formula to 1e-15), C3 (Identity MM in the two-point model, four parameter sets, relative error below 3e-7): ALL
PASS. This guards the algebra only.

**8.2 Answers to the row.**
1. Port or new input: NEW input. The account has the statement for one block step at weak coupling (class S),
   and it asserts nothing on block laws or decay at first passage. Quoted and credited in Section 2.
2. Circular: NO. No larger box enters; all time extents enter without a rate. But the supremum form is not a
   gap statement: it asks that no boundary layer orders at any linear tilt. The frozen-slice runs of rows 950
   and 952 say that this is false at beta 2.5 to 2.6.
3. Ranking: A1 (tie test of the flow forms, no run needed), A2 (the trajectory form), A3 (EXIT, existing item).
4. Proof attempt on A1, three stages: the orbit gain (QUOT, ROTOR), the cost of a tie (TIE), what the seed
   reads (TRAJ, MM). Outcome: a negative result on the flow forms and one surviving inequality. No bound for
   SU(2) was proved.

**8.3 For the lead: what changes.**
- Do not queue proofs of a box-uniform (TILT-COV-sup), of its quotient form, or of (ABS-flow) for the whole
  window. At beta 2.5 to 2.6 they are refuted at GUIDE level (t = 0: Lemma SUB with rows 950, 952; t > 0: Section 7a).
- The open input of the Theorem BR route is now (LSI-traj-seed)_a: the same inequality, on the functions that
  Proposition HC and Theorem BR actually use. It is not smaller in any proved sense. Its entropy side has an
  exact form with typical tilts only (Identity MM).
- Row 969 (check of row 968) should also read Lemma SUB: row 968's GUIDE run used the uniform tilt and missed
  the frozen-slice family. Row 971 (literature) should search for bounds at typical tilts, not suprema.
- One point for the checker of rows 931 and 947: the gauge-averaged kernel in Proposition HC (7.1, note).

**8.4 For the checker of this file, in this order.** (1) Lemma SUB and the identification of row 950's observable
with a linear statistic of pi_(beta u). (2) Lemma FH (b), (d) and the use made of it in Theorem QUOT. (3) Proposition
TIE (b), (d), including the Chebyshev step. (4) Identity MM: the Markov step and the gradient formula.
(5) Lemma TRAJ against the two proofs it cites. (6) Lemma SLAB. The transfer 6.3 and the readings carry no
proof weight.

