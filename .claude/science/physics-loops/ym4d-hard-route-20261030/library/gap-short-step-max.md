lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-16T08:03Z

# gap-short-step-max: the 4D short step, a selective gain at order-one response

Queue row 1018 of `FINISH.md`, pinned at commit df74a7421, branch `claude/ym4d-hard-route`.
Worker: Claude Fable 5.2, max effort, Mac mini worker 3. One session, no subagents.
This is research-stage working state. It grants no status.

Marks used below: PROVED (every step written here), ARGUED (argument written, a step not fully written), OPEN, FAILS (counterexample or failing step written).

## Plan (at most eight steps; one step per response; each result is appended before the next step)

1. **Read.** `parts/gap.md`; rows 1009, 1010 (2D short step, [28] (3.52)); `library/gap-pinned-cell-gauge-max.md` and its check; `library/gap-invent-selective-max.md` and its check; the exercise skill at main commit 8b11ae2bb9. Duplicate check against `library/open-core.md` and the FINISH rows (rows 1016, 1017 run in parallel and are not redone). Record what is read and what is established.
2. **Target.** Write the 4D short step as an exact inequality: the quantity R(Q), the class closed under the conditioning the proof uses, the statement R(lQ) <= R(Q) - delta at order-one R(Q). Show by hand that it is false for compact U(1) and for a product with a massless factor.
3. **Route (iii-b), barrier first.** Try to build an averaged or modified model that keeps every identity the tools use (bracket term of Proposition W, reflection positivity) and has no short step. If it exists, name what a proof must use beyond the bracket.
4. **Route (ii), field-dependent covariant moves.** Jacobian control and the curl form of the cost at order-one response; test against Lemma WN and row 1013 C8.
5. **Route (iii-a), energy increment.** Write the dichotomy lemma (response drops, or a structure energy bounded by the action rises); test both halves.
6. **Tests.** Each surviving piece against Lemma PT, Proposition NP, Theorem D2, Lemma SHEET, Lemma SLAB, compact U(1), frozen Q_8 and 2T, the five-dimensional test of `library/gap-crux-fp.md`, the instanton cost of 6.3 of row 1013.
7. **First survivor.** Prove it by hand, or build the counterexample.
8. **Result.** Marks per piece, what stays open, one RESULT line.

## Log

- 2026-11-15T20:03Z. File created. No earlier run of this item exists at the pinned commit.
- (between 20:03Z and 20:17Z; time not measured) Step 1, progress marker 1a. Read in full: `GOAL.md`; `FINISH.md` L1-90, L299-356 and rows 1009-1018; `parts/gap.md`; `library/gap-pinned-cell-gauge-max.md` (row 1011); `library/gap-invent-selective-max.md` (row 1013); the exercise skill at main 8b11ae2bb9 and its reference `proof-search-governance.md` (both fetched into `/tmp/gss-skill-w3/`). Still to read in this step: the two checks (rows 1014, 1015), rows 1009 and 1010 at the short step ([28] (3.52)), the statements of Lemma PT, Proposition NP, Theorem D2, Lemma SHEET, the five-dimensional test, and the files of rows 1016, 1017 if they exist at this pin (to avoid redoing them).
- 2026-11-15T20:17Z (`date -u`). Step 1 done. See Section 1. From here on every log time is read from `date -u` when the line is written.

## 1. Step 1 result: provenance, what was read, where the record sits, duplicate check (exercise step 0)

**Provenance.** Anthropic, Claude Fable 5.2, max effort, one session on Mac mini worker 3, no subagents. Nothing in this file is checked by another model. The target is a standalone proof target, so the contract of `GOAL.md` (no computer-assisted step; proofs that could be formalized in Lean) replaces the framework refresher read of the exercise skill. The skill was fetched at main 8b11ae2bb9 with its one reference file `proof-search-governance.md` into `/tmp/gss-skill-w3/`; both were read in full.

**Credit.** The 2D short step is OpenAI's (posted, unrefereed; github.com/openai/math commit 4eaee8754825; "Sharp mass bounds for the two-dimensional O(4) model", (3.52) and Section 3.8; "The canonical massive continuum limit of the two-dimensional O(3) model", (2.30)), as read by rows 1009 and 1010 (Claude Opus 5.5, unchecked). Rows 1011 and 1013 (Claude Fable 5.2) with their checks 1014 and 1015 (Claude Opus 5.5) supply Propositions A, W, B, B', SEAG, Lemmas CEN, EMB, FR, WN, TWIST, JEN, SLAB and the reopen conditions. Lemma GG is row 1004's. Balaban's background-field results and the Sussman-Alpoge account (with Claude and Codex as authors of their text) are credited where they are used.

**Read in full:** `GOAL.md`; `FINISH.md` L1-90, L299-356, rows 1009-1018; `parts/gap.md`; `library/gap-pinned-cell-gauge-max.md`; `library/gap-invent-selective-max.md`; the skill and its reference. **Read in part:** `library/gap-invent-selective-check.md` L262-473 (the two ARGUED remarks, W2, verdicts); `library/prior/gap-o4-pinned-cell-read-opus.md` L60-199 (the 2D class, Ward identity, variance gain, the short step (3.52), the iteration 3.8); `library/gap-crux-restate.md` L27-47, L176-222 (objects, Lemmas K, X, E, Theorem S); `library/gap-mid-max.md` L58-70 ((CAS)); `library/gap-crux-exercise3-max.md` L688-724 (Lemma PT); the first 60 lines of the in-progress files of rows 1016 and 1017. **Not read:** the rest of the lane (about 800 library files); the primary 2D texts (used through rows 1009, 1010, 1013).

**The 2D short step, as rows 1009 and 1013 restate it (OpenAI's mathematics; unchecked reading).** The class is all pinned squares, all pins, all signed strengths up to b, all fixed right twists. The monotone is the class bound h of the twist stiffness H. One step from side R to side L R uses the exact identity "H_Q(A, A) = v |A|^2 - Var J(A)" (Gaussian augmentation at level v > h) and a lower bound on Var J(A) from the bracket term of the rotation Ward identity. Long regime: Var J(A) >= (log L)/pi - C[log B + (log L)^2/v]. **Short regime ([28] (3.52)): with a bounded number of frequency octaves (K_1 = 8M, K_2 = 256M), Var J(A) >= c_sh min(v, 1), c_sh absolute.** So each short step lowers h by c min(h, 1), from h of order log B down to B^(-D) in O(log B) steps. The same exact Ward identity serves at every value of h, because the rotation is an exact symmetry on every configuration.

**Where the lane's record sits on the objects of this row (located before any attack; rule 0a).**

| Object | Where | Standing there | Consequence for this row |
|---|---|---|---|
| The short step in periodic form: (CAS), "Delta((2a)^4) <= theta Delta(a^4) while 6.1 x 10^(-4) < Delta(a^4) <= M" | row 708, `library/gap-mid-max.md` L64-67; `parts/gap.md` L106-108, route RA | open; "as a mechanism it is empty: it restates the seed in steps"; blocked-equivalent | I do not attack (CAS). Section 2 names it as the periodic form of the target and says what the target adds: a response with a mechanism slot. |
| Reopen condition (ii): covariant moves, controlled Jacobian, curl cost form at order-one response | row 1013 7.2; row 1016 plan step 7 (in work on worker 1; its file at this pin has step 1 only) | open; row 1016 takes it in general, with the homogeneous-strength case of B' | Overlap named. This row's route (ii) is kept to what the row asks: the exact cost form of field-dependent moves at order-one response. I do not attack the homogeneous-strength case of B'. |
| Compactness and rigidity (critical element, branch G) | row 1017 (in work on worker 2; step 1 at this pin) | open | Not redone. Where route (iii-a) reduces to "no scale-invariant end", I name row 1017 and stop. |
| Adjoint Higgs family ends at compact U(1) | row 1004, `library/gap-outside-box-max.md` 6.2, Lemma GG (PROVED there; check 1008 HOLDS, same provider) | a test, not a tool | Used in route (iii-b) as the end point of a family of models with a colour frame; credited. |
| Five-dimensional test | `library/gap-crux-fp.md` F15 (L50), L76, L88, L266 | GUIDE (numerics) | Used as a belief-grade test only. |
| Energy increment, structure against randomness, a barrier model | `library/open-core.md`: no hit (grep: short step, selective, energy increment, barrier, covariant move, tree-transport, frameable). Lane: no file states a dichotomy of this kind (grep: energy increment, structure against randomness, regularity lemma, density increment, barrier model). | not on file | Routes (iii-a) and (iii-b) are not covered by another row. |
| Nilpotent groups, the Killing form | lane grep: no file | not on file | used in Section 4. |

**What this run does not cover (kept current).** No literature search beyond the lane's records (rows 1007, 1009, 1010, 1012 are the literature lens of this object; the row asks for none). The primary OpenAI texts were not re-read. PR branches other than this one were not searched. Rows 1016 and 1017 were read only at their first step.

## 2. Step 2 result: the 4D short step as an exact target

Marks: DEF, PROVED (by hand here, checked by no one), ARGUED, OPEN.

### 2.1 The contract (DEF)

A **short step** is a triple (R, class, consumer) with four clauses.

- (L0) **Closure.** The class is kept by the conditioning the proof uses.
- (L1) **Blind half.** A bound that holds for every model of the class and never loses: R(lQ) <= R(Q) (or a stated blind map).
- (SS) **Selective half.** There are r_0 < r_1, delta > 0 and an integer l >= 2 with: r_0 <= R(Q) <= r_1 implies R(lQ) <= R(Q) - delta.
- (L3) **Consumer.** R(Q) <= r_0 for one Q gives the seed of Theorem S (`library/gap-crux-restate.md` L192), or (W).

In OpenAI's 2D proof all four hold on one class: (L0) pinned squares with all pins and strengths; (L1) "the stiffness of the larger square is an average of cell stiffnesses minus a covariance"; (SS) is [28] (3.52); (L3) is [28] 3.9-3.12. In 4D no triple on record has all four. Two forms exist. Each lacks one clause.

### 2.2 Form (T-per): the periodic form. It is (CAS) of row 708 (named match; not attacked here)

Objects (DEF, `library/gap-crux-restate.md` L29-45): Wilson SU(2) at one beta on tori with sides at least 3, F = log Z, f = inf F(n)/|n|, Delta(n) = F(n) - f |n| >= 0, D(a) = Delta(a, a, a, a), Phi(a) = 16 F(a^4) - F((2a)^4) >= 0.

**Target (T-per).** There are delta > 0 and M with D(3) <= M such that, for every a >= 3 with 6.1 x 10^(-4) < D(a) <= M:

  D(2a) <= D(a) - delta.

- Cell Q: the torus of side a. R(Q) = D(a). Class: the engine's class (reflection-positive gauge models with (TM)). (L0): no conditioning is used. (L1): D(2a) <= 16 D(a) only (Lemma A), which is not a blind half in the sense above. (L3): Proposition Delta of row 708 (`library/gap-mid-max.md` L144): D(a) <= 6.1 x 10^(-4) at one a gives the seed.

**Lemma ADD (PROVED).** (T-per) holds if and only if (CAS) of `library/gap-mid-max.md` L64 holds. Both are equivalent to: Phi(a) >= 15 D(a) + delta on the range.

Proof. D(2a) = F((2a)^4) - 16 f a^4 = 16 F(a^4) - Phi(a) - 16 f a^4 = 16 D(a) - Phi(a). So D(2a) <= D(a) - delta is Phi(a) >= 15 D(a) + delta. If (CAS) holds with theta, take delta = (1 - theta) 6.1 x 10^(-4). If (T-per) holds with delta, take theta = 1 - delta/M. In both directions D does not increase along the doublings, so the range condition D <= M is kept. QED

Also D(a) = sum over k >= 0 of Phi(2^k a)/16^(k+1) (PROVED: iterate D(a) = Phi(a)/16 + D(2a)/16; D(2^k a)/16^k = a^4 (F/|n| - f) at side 2^k a, which tends to 0). So (T-per) says: Phi at side a exceeds 15 times its own weighted average over the larger sides. In a scale-invariant theory Phi is constant and Phi = 15 D exactly.

**False for compact U(1) and for a product with a massless factor (PROVED, given the U(1) theorem I28 as the lane holds it, Villain at beta >= 2^14, and Proposition Delta).** Such a model has no seed at any size (Corollary PT1, `library/gap-crux-exercise3-max.md` L711). By Proposition Delta, D(a) > 6.1 x 10^(-4) for every a >= 3. If (T-per) held, then after at most (M - 6.1 x 10^(-4))/delta doublings D would be at most 6.1 x 10^(-4). Contradiction. For the free photon D(a) tends to a positive constant (RECALLED in row 708). QED

**What (T-per) lacks: a mechanism slot.** Row 708's verdict stands: "as a mechanism it is empty: it restates the seed in steps." Route RA is blocked-equivalent (`parts/gap.md` L152). The three routes of this row are tests of mechanisms. Each needs an identity in which a gain can appear. That is the second form.

### 2.3 Form (T-pin): pinned cubes, in the law of the model. It has a mechanism slot and no consumer

Rows 1011, 1013 and their checks leave these facts for any pinned form. A class supremum of a continuous response has no classical bound (Proposition B'). Cells must be cubes (Lemmas SLAB, EMB). The only symmetric link twists are central (Lemma CEN). So the class is taken **in law**, and the response is the one gauge-covariant object that needs no frame: the cross-cell covariance of the Neumann data (row 1011 7.5, registry line G5; credited).

**Objects (DEF).** Wilson SU(2) at coupling beta; mu is a translation-invariant Gibbs state on Z^4, or the law on a large torus. For l >= 2, T_l is the tiling of Z^4 by the cubes x + {0, ..., l}^4, x in l Z^4, with the weights w_p of row 1011 3.1. The **rings** are the boundary links of the cells. F_l is the sigma-algebra of the ring links. If l divides l', then F_l' is contained in F_l. Given F_l the cells are independent, each with the pinned law (c, omega_c, beta) of row 1011 3.1 (Markov). For a boundary link l of a cell c put N_l = sum over plaquettes p of c containing l of (+ or -) beta w_p (s_p transported to the tail of l), as in row 1011 Proposition A (iii), and Nbar_l(omega) = E_(c, omega)[N_l].

For two boundary links l, l' of c that share no plaquette put K_c(omega)(l, l') = Cov_(c, omega)(N_l, N_l'), a 3 x 3 matrix. By Proposition A, minus K_c(omega)(l, l') is the mixed second derivative of F_c in the rotations of l and l'. Under a gauge map g of the boundary sites it changes to Ad(g_tail(l)) K Ad(g_tail(l'))^T. So its Hilbert-Schmidt norm is gauge invariant. With F_- and F_+ the two faces x_1 = const of c, put

  R_c(omega)^2 = l^2 sum over l in F_-, l' in F_+ of |K_c(omega)(l, l')|_HS^2,    Rbar(l) = (E_mu[R_c(omega)^2])^(1/2).

**Lemma CHAIN (the mechanism slot; PROVED).** Let Q be a cube of side L l with pin Omega, tiled by L^4 cells of side l. Let l, l' be boundary links of Q such that no cell contains both. Then

  K_Q(Omega)(l, l') = Cov_(Q, Omega)( sum over cells c containing l of Nbar_l^c , sum over cells c' containing l' of Nbar_l'^c' ).

Proof. F_Q(Omega) = - log of the integral over the inner ring links of exp(- sum_c F_c(omega_c)), because cell actions add (the weights w_p) and the cell interiors are independent given the rings. Rotate l and l' with the extension by zero. The first derivative of sum_c F_c in l is sum over c containing l of Nbar_l^c. The mixed second derivative of sum_c F_c is zero, because no cell contains both links. So the mixed second derivative of F_Q is minus the covariance. QED

In words: the flux correlation across the large cube is the covariance, over ring configurations, of the mean fluxes of the cells at the two faces. The mean flux Nbar_l^c depends on the pin of c at its other faces through - K_c (the same Proposition A). So K at scale L l is built from the tensors K_c at scale l, composed through the ring fluctuations. This is the place where a gain or a loss of one step can be read.

**Target (T-pin) (candidate; its three open slots are named below).** There are r_0 < r_1, delta > 0, an integer L >= 2 with: r_0 <= Rbar(l) <= r_1 implies Rbar(L l) <= Rbar(l) - delta.

- (L0) holds by the tower property of conditional expectations. (L1): OPEN. No inequality Rbar(L l) <= C Rbar(l) is known. (L3): OPEN. No statement "Rbar small gives decay of all observables" is on record (the 4D analogue of rule R9 of row 1013).
- Size (ARGUED). For a Gaussian field with action (beta/2) sum_p w_p (d phi)_p^2, F_c is beta/2 times the Dirichlet-to-Neumann form of the cube, K_c = - beta times its off-diagonal block, and the kernel between opposite faces is of size l^(-4). Then R_c^2 is of order l^2 l^6 beta^2 l^(-8) = beta^2 at every scale. So Rbar is scale invariant for the free photon, and (T-pin) is false there. The normalisation l^2 is chosen for this. Not proved: the convergence of the lattice kernel.
- Products (PROVED). For a product model with product weight the Neumann data of the two factors are independent, so K is block diagonal and R_c^2 = R_(1,c)^2 + R_(2,c)^2. A massless factor keeps Rbar above its own value.
- Compact U(1): at theorem grade (T-pin) is tested only through a consumer, and it has none. At belief grade (Coulomb phase with renormalised stiffness of order one, beta from about 1.01 to a few) it is false.

**Why this form.** Lemma CHAIN is exact, needs no frame, no symmetric twist and no supremum over pins. Its right side is a covariance, so the routes below can be put as questions about one object: route (ii) asks for a flow that bounds it at order-one response; route (iii-a) asks whether the tensors K_c compose coherently (structure) or not (randomness); route (iii-b) asks for a model where they compose coherently for ever.

### 2.4 What "order one" means here

The band of `parts/gap.md` L41-47: the range of scales between first passage (the last scale where the account's coupling g_k is below its threshold gamma) and the seed size. In (T-per) it is 6.1 x 10^(-4) < D <= M. In (T-pin) it is r_0 <= Rbar <= r_1. For each form the long step (R large) is the account's asymptotic freedom and is a (K-flow) input; it is not part of this row.

- 2026-11-15T20:32Z (`date -u`). Step 2 done (Section 2). Step 3, route (iii-b), next.

## 3. Step 3 result: route (iii-b), barrier first

Question of the row: is there a model that keeps every identity the tools use, the bracket term of Proposition W and reflection positivity included, and has no short step? If so, what must a proof use beyond the bracket?

### 3.1 The identities the tools use (inventory; each with its source)

- (T1) Haar invariance on integrated links: Proposition A, Proposition W with its bracket term (row 1011 3.2, 3.3), Lemma WN, Lemma JEN, Lemma TWIST (row 1013 4.1, 4.2, 5.1). Valid for every compact Lie group, every cell complex, every dimension, every strength field.
- (T2) The cell structure: closure under conditioning on rings (row 1011 3.1), Lemma CHAIN (2.3 here).
- (T3) Central twists: Lemma CEN, Corollary CEN2 (row 1011 4.3), and Lemma PAR below.
- (T4) Reflection positivity and the transfer operator (TM), with the blind engine (Lemmas A, K, X, E, Theorem S).
- (T5) Compactness: |t_p| <= 1.

### 3.2 Lemma PAR: the exact parallel law of central twists (PROVED by hand; the algebra is Mack and Petkova's)

Credit. Mack and Petkova, Ann. Phys. 125 (1980) 117, prove a confinement criterion from vortex containers; the lane holds it as RECALLED (`library/prior/gap-lit-grok.md` Section 2, `library/gap-size-rec-astra.md` 4.1: "Its proof is not rebuilt here"). I did not read their paper. The algebra below is surely theirs in substance. It is written here for the partition function of the container itself, with its exact form. The one-plaquette case is on file as the centre-even form of row 859 (`library/gap-brainstorm2-max.md` L106, L187). No novelty is claimed.

**Setting.** A finite set of links, split into integrated links Lam and pinned links bd. A finite set of plaquettes, each with real strength beta_p (any sign; cell weights w_p absorbed). G is a compact group with a central element -1 of order 2 for which t_p changes sign when one link of p is multiplied by -1 (SU(2), Q_8, 2T, Z_2). Z(Om) is the integral over the integrated links of exp(sum_p beta_p t_p) with pin Om. A **sign field** tau assigns +1 or -1 to every link; (d tau)_p is the product of tau over the four links of p; t_p(tau U) = (d tau)_p t_p(U). tau is **closed** on a set of plaquettes if d tau = 1 there.

Fact 0. If tau is closed on all plaquettes, then Z(tau|_bd Om) = Z(Om). (Substitute U -> tau U on the integrated links.)

**Sub-containers.** Lam_1, ..., Lam_n are disjoint subsets of Lam such that no plaquette contains links of two of them. P_i is the set of plaquettes with at least one link in Lam_i; bd_i is the set of links outside Lam_i that lie in a plaquette of P_i; Z_i(om_i) is the integral over Lam_i of exp(sum over P_i) with pin om_i on bd_i. **Twist system.** Sign fields tau_1, ..., tau_n and sigma with: (H1) tau_i = sigma on bd, for every i; (H2) tau_i is closed on every plaquette outside P_i. Put

  rho = Z(sigma Om)/Z(Om),   r_i(om_i) = Z_i(tau_i om_i)/Z_i(om_i) > 0,   a_i = (1 - r_i)/(1 + r_i) in (-1, 1).

With V = - log rho and v_i = - log r_i (the signed vortex costs): a_i = tanh(v_i/2), and v_i(tau_i om_i) = - v_i(om_i). E is the expectation, in the pinned law with pin Om, of the links outside the Lam_i.

**Statement.** (i) For every subset S of {1, ..., n}: E[prod over i in S of r_i] = rho if |S| is odd, and 1 if |S| is even.
(ii) Let Etilde be E with the extra weight prod_i (1 + r_i), normalised. Then for every subset M with M not empty:

  Etilde[prod over i in M of a_i] = 0 if M is not all of {1, ..., n},     Etilde[a_1 a_2 ... a_n] = (1 - rho)/(1 + rho) = tanh(V/2).

(iii) So tanh(V/2) is the n-th joint cumulant of (a_1, ..., a_n) under Etilde, and

  |tanh(V/2)| <= prod_i sup |a_i| = prod_i tanh(xi_i/2), xi_i = sup over pins of v_i;     |tanh(V/2)| <= prod_i (Etilde |a_i|^n)^(1/n).

**Proof.** (i) Put tau_S = prod over i in S of tau_i. By (H1), tau_S = sigma^|S| on bd. By (H2) and the disjointness of the P_i, tau_S is closed on every plaquette outside the P_i with i in S, and on P_i (i in S) it equals tau_i times a field closed on P_i. Write Z(sigma^|S| Om) as the integral over the links eta outside the Lam_i of exp(A_rest(eta)) prod_j Z_j(eta|_bd_j), where A_rest is the sum over the plaquettes in no P_j. Substitute eta -> tau_S eta. A_rest is unchanged. For j not in S, Z_j(tau_S eta) = Z_j(eta) by Fact 0 in the sub-container j. For j in S, Z_j(tau_S eta) = Z_j(tau_j eta) by Fact 0 again, which is r_j Z_j(eta). So Z(sigma^|S| Om) = Z(Om) E[prod_S r_i], and sigma^2 = 1.
(ii) For signs eps_i: E[prod_i (1 + eps_i r_i)] = sum over S of (prod_S eps_i) E[prod_S r_i] = (1/2)[prod(1 + eps_i) + prod(1 - eps_i)] + (rho/2)[prod(1 + eps_i) - prod(1 - eps_i)]. For eps = +1 this is 2^(n-1)(1 + rho). For eps = -1 it is 2^(n-1)(1 - rho). For mixed signs it is 0. Divide the cases "eps_i = -1 on M, +1 off M" by the case eps = +1.
(iii) A joint cumulant is a sum over partitions of products of mixed moments of the blocks. Every partition other than the one block contains a proper block, whose moment is 0 by (ii). The two bounds are the sup bound and Hoelder's inequality. QED

**What it gives.** For containers Gamma = Sigma x D (Sigma a closed surface of plaquette-dual type, D a transverse disc) with n parallel sub-containers Sigma x D_i, a twist system exists: tau_i = -1 on the links that cross Sigma x (a path in D from inside D_i to a fixed point of the boundary of D, avoiding the other D_j). Then:

- **A blind half for a central response.** The vortex cost of a container is at most that of any parallel sub-container, and tanh(V/2) multiplies over parallel sub-containers. This is clause (L1) for the response xi = sup-pin vortex cost. It holds for every group with a central involution.
- **An exact statement of "structure against randomness" for this response.** The cost of the large container is exactly an n-point cumulant of the sub-container activities. If the activities were independent under Etilde, the cost would be 0. A positive cost is exactly a rigid parity correlation of the activities.
- **A third form of the target, (T-vor).** R = xi (sup-pin), or the moment form (Etilde |a|^n)^(1/n) with the outer pin taken in supremum; (L0) holds (pinned sub-containers), (L1) is Lemma PAR, (L3) is Mack and Petkova's criterion for the centre-odd sector only (RECALLED; route RE of `parts/gap.md` L153, which still needs the even step). (SS) is OPEN, and its exact form is in 3.4 below.

### 3.3 The barrier table (valid form of each test: a model with the identity and without the conclusion)

| Model | Identities it keeps | No short step: standing | What a proof must therefore use |
|---|---|---|---|
| (a) Compact U(1); free photon | all of (T1)-(T5); every bracket is 0 | THM for Villain at beta >= 2^14 (lane I28); free photon exact | a bracket (rule R4 of row 1013) |
| (b) Product with a massless factor | all; the bracket of the SU(2) factor is there | PROVED given (a) (Lemma PT) | the whole state space: a response in every Lie algebra direction, so a perfect Lie algebra, [g, g] = g |
| (c) Frozen Z_2 (and Q_8, 2T) | (T2)-(T5); Lemma PAR verbatim, with its blind half | Z_2: THM, lane (Peierls, beta > 2.191; T_per). Q_8, 2T: BELIEF at order one | a continuous path from 1 to -1: a vortex whose flux is spread over many sub-containers (fractional vorticity). Lemma PAR sees only vorticity 0 or 1 in each sub-container. |
| (d) Frozen slices: every spatial link pinned to 1 (Lemma SLAB of row 1013 on every slice) | (T1) for the time-like links with the full O(4) bracket and an exact symmetric twist with classical cost; (T4): it is a stack of independent 3D O(4) models, one per time layer; (T5) | long-range order at large beta: Froehlich, Simon and Spencer 1976, RECALLED (the lane's rebuilt Gaussian domination, row 1000, is its main input; the order itself is not rebuilt) | that all six plaquette orientations fluctuate at comparable strength: the classical cost of a twist is scale invariant only for the full 4D curl form. In (d) the cost of a twist at scale l is beta l. |
| (e) Adjoint Higgs field of unit length, hopping kappa | (T1) with a matter current added to X; brackets present for kappa finite | end point kappa = infinity is compact U(1) exactly (Lemma GG, row 1004; THM with (a)); kappa finite: BELIEF | the absence of a matter current: the contact term of Proposition W is a covariant curl form with no mass term |
| (f) SU(2) in five dimensions | all of (T1)-(T5), with the same formulas | BELIEF (numerics, F15 of `gap-crux-fp.md`) | dimension 4, through one mode sum (rule R6) |
| (g) Weights exp(beta ((1+x)/2)^p), p large; the K7 line | all, with the weight's derivatives in place of beta | first-order transition: THM (van Enter and Shlosman; Proposition V). A massless singlet at the K7 end point: BELIEF | not a barrier to a colour response dropping. It binds the consumer (L3): a small colour response does not give the gap of singlet observables without a property of the Wilson weight. |

Remarks. (d) is a translation-invariant form of Lemma SLAB and of Theorem D2's sheets (rows 977, 1013; credited). Proof of the identification: with all spatial links equal to 1, the plaquette (x, t; i, 4) is (1/2) tr(q(x+i, t) q(x, t)^(-1)), q = the time-like link; plaquettes of different layers share no integrated link. (c): every finite group with a central involution satisfies Lemma PAR; Q_8 is nilpotent, so its commutators are central.

### 3.4 What the barriers leave: the exact open half in the form (T-vor)

Take cubic containers: Sigma of linear size l, D of side l; doubling gives Sigma of size 2l and D of side 2l. The large container holds 4 parallel copies of (Sigma_2l, D_l). By Lemma PAR,

  tanh(xi(Sigma_2l, D_2l)/2) <= tanh(xi(Sigma_2l, D_l)/2)^4.

The missing statement is a **series bound**: xi(Sigma_2l, D_l) <= kappa xi(Sigma_l, D_l). Arithmetic of the map r -> 2 artanh(tanh(kappa r/2)^4) (hand values: kappa = 4: 0.3 -> 0.167, 0.4 -> 0.394, 0.5 -> 0.70; kappa = 1: a contraction everywhere): with kappa = 4 it contracts below r = 0.40 and expands above, like R(2l) = 4 R(l) - log 4 for large R. Classical scaling of a thick vortex says kappa = 4 at fixed thickness and a factor 1/4 from doubling the thickness. The blind half recovers only the entropy term log 4 of that factor 1/4. So in this form the short step is exactly: **the gain of spreading a centre flux continuously over the doubled thickness**, at order-one cost. Frozen Z_2 has no such spreading and has R(2l) near 4 R(l). Two cautions. The series bound is not proved at any kappa (a closed vortex cannot be cut into pinned patches without a thin crossing at each cut). And at weak coupling the sup-pin cost is not scale invariant: for a pin that forces a non-abelian interior curvature of order one per plaquette, a spread vortex pays the mass term of Lemma FR on its whole spread region, so the cheapest vortex is thin and costs of order beta |Sigma| (ARGUED). So the supremum must be taken over outer pins at distance at least l, or in moments (the Hoelder form of (iii)).

### 3.5 Verdict on route (iii-b)

- No model is built that keeps (T1)-(T5) on isotropic cubic cells in four dimensions, for a connected simple group without matter, and has no short step. None is believed to exist (test table point 5, `parts/gap.md` L222). Mark: OPEN, as before this row.
- What is established, PROVED: the bracket identity is kept verbatim by model (d), which is ordered at large beta given the RECALLED theorem; the central-twist identities, with their blind half (Lemma PAR), are kept verbatim by model (c). ARGUED: the readings of the last column.
- So a proof of the short step must use, beyond the bracket: (1) a perfect Lie algebra, in every direction of the response; (2) a continuous path to the centre (spreading); (3) isotropy of the cell in four dimensions, so that the classical cost is scale invariant; (4) the absence of a mass term in the contact term (no matter current); (5) for the consumer, a property of the Wilson weight. Items (1), (3), (5) are found again (rules R4, R6; tests K1, K7, Proposition V). Items (2) and (4) are stated here in exact form: (2) through Lemma PAR, (4) through Lemma GG.
- Off the path of (W) except as constraints. The one new exact tool is the blind half of (T-vor).
