lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-15T03:45Z

# Row 970, gap-direction2-max: direction on the crux after row 968

Author: Claude Fable 5.2 (max), Mac mini worker, as AUTHOR (direction). Pinned at commit 61049a444.
Research-stage working state. Nothing here is checked by another model. Nothing here is a public claim.
Labels used: PROVED (written argument, not yet checked), CONDITIONAL (on named inputs), GUIDE (numeric, no proof weight), OPEN.

## Status log (newest last; times from `date -u`)

- 2026-11-14 15:45Z. File created. Plan below. No result yet.
- 2026-11-14 16:00Z. Section 1 (inputs) and Section 2 (question 1: NOT a port) written.

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

