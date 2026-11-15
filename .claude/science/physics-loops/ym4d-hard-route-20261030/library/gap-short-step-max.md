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

## Status block (kept current; read Section 8 first)

- Step 1, inputs and duplicate check: done (Section 1).
- Step 2, the target: done (Section 2). Three forms; each lacks one clause. (T-per) is (CAS) of row 708 and is not attacked.
- Step 3, route (iii-b), barrier: done (Section 3). No counter-model in the target's own class. Lemma PAR PROVED.
- Step 4, route (ii), covariant moves: done (Section 4). FAILS at one bare coupling (ARGUED); Lemmas FLOW, PROJ, FR+, SPLIT PROVED.
- Step 5, route (iii-a), energy increment: done (Section 5). OPEN; no bounded monotone structure energy; Lemma NAB PROVED.
- Step 6, control run and tests: done (Section 6). Control of Lemma NAB PASS (a guide). Every proved piece is blind.
- Step 7, survivor and open statements: done (Section 7). Corollary MP PROVED. Open: O1, O2.
- Step 8, report and RESULT: Section 8.

**Nothing in this file is checked by another model.**

**What this run did not cover.** No literature search (the lane's records of rows 1007, 1009, 1010, 1012 and `library/prior/gap-lit-grok.md` are reused; one paper was fetched, see below). OpenAI's primary texts were not re-read; the 2D short step is used through rows 1009 and 1013. Mack and Petkova's paper (Ann. Phys. 125, pp. 117-134) was read in full by text extraction, after Lemmas PAR, SPLIT and Corollary MP were written; its figures were not seen. This one fetch is the only literature step of the run. Froehlich, Simon and Spencer's theorem is RECALLED. Proposition NP, Theorem D2 and Lemma SHEET were read at their statements only (`library/gap-crux-exercise4-max.md` L383-392, `library/gap-tiltproof-max.md` L240-246, `library/gap-sepinput-max.md` L358-364). Rows 1016 and 1017 were read at their first step only, as they stood at this pin. Other PR branches were not searched. One numeric run, a guide (6.1). The sizes marked ARGUED in 3.4, 4.5, 5.3 are not proved.

## Log

- 2026-11-15T20:03Z. File created. No earlier run of this item exists at the pinned commit.
- (between 20:03Z and 20:17Z; time not measured) Step 1, progress marker 1a. Read in full: `GOAL.md`; `FINISH.md` L1-90, L299-356 and rows 1009-1018; `parts/gap.md`; `library/gap-pinned-cell-gauge-max.md` (row 1011); `library/gap-invent-selective-max.md` (row 1013); the exercise skill at main 8b11ae2bb9 and its reference `proof-search-governance.md` (both fetched into `/tmp/gss-skill-w3/`). Still to read in this step: the two checks (rows 1014, 1015), rows 1009 and 1010 at the short step ([28] (3.52)), the statements of Lemma PT, Proposition NP, Theorem D2, Lemma SHEET, the five-dimensional test, and the files of rows 1016, 1017 if they exist at this pin (to avoid redoing them).
- 2026-11-15T20:17Z (`date -u`). Step 1 done. See Section 1. From here on every log time is read from `date -u` when the line is written.
- Later log lines stand at the end of each section. Step 8 (report and RESULT) was written at 2026-11-15T21:12Z (`date -u`).
- 2026-11-15T21:15Z (`date -u`). After Step 8: Mack and Petkova's paper fetched and read (text only); credits in 3.2, 4.4, 7.4 and the coverage list updated; wording softened where a mark was stronger than its proof; one table row repaired. Some log times in this file were first written by estimate and then replaced by the `date -u` value printed in the same step; the values that stand are the measured ones.

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

In OpenAI's 2D proof all four hold on one class: (L0) pinned squares with all pins and strengths; (L1) "the stiffness of the larger square is an average of cell stiffnesses minus a covariance"; (SS) is [28] (3.52); (L3) is [28] 3.9-3.12. In 4D no triple on record has all four. Two forms are written in this section and a third, (T-vor), in 3.2. Each lacks at least one clause.

### 2.2 Form (T-per): the periodic form. It is (CAS) of row 708 (named match; not attacked here)

Objects (DEF, `library/gap-crux-restate.md` L29-45): Wilson SU(2) at one beta on tori with sides at least 3, F = log Z, f = inf F(n)/|n|, Delta(n) = F(n) - f |n| >= 0, D(a) = Delta(a, a, a, a), Phi(a) = 16 F(a^4) - F((2a)^4) >= 0.

**Target (T-per).** There are delta > 0 and M with D(3) <= M such that, for every a >= 3 with 6.1 x 10^(-4) < D(a) <= M:

  D(2a) <= D(a) - delta.

- Cell Q: the torus of side a. R(Q) = D(a). Class: the engine's class (reflection-positive gauge models with (TM)). (L0): no conditioning is used. (L1): D(2a) <= 16 D(a) only (Lemma A), which is not a blind half in the sense above. (L3): Proposition Delta of row 708 (`library/gap-mid-max.md` L144): D(a) <= 6.1 x 10^(-4) at one a gives the seed.

**Lemma ADD (PROVED).** (T-per) holds for some delta > 0 if and only if (CAS) of `library/gap-mid-max.md` L64 holds for some theta < 1, with the same M. (T-per) with delta is the statement Phi(a) >= 15 D(a) + delta on the range; (CAS) with theta is Phi(a) >= (16 - theta) D(a) on the range.

Proof. D(2a) = F((2a)^4) - 16 f a^4 = 16 F(a^4) - Phi(a) - 16 f a^4 = 16 D(a) - Phi(a). So D(2a) <= D(a) - delta is Phi(a) >= 15 D(a) + delta. If (CAS) holds with theta, take delta = (1 - theta) 6.1 x 10^(-4). If (T-per) holds with delta, take theta = 1 - delta/M. In both directions D does not increase along the doublings, so the range condition D <= M is kept. QED

Also D(a) = sum over k >= 0 of Phi(2^k a)/16^(k+1) (PROVED: iterate D(a) = Phi(a)/16 + D(2a)/16; D(2^k a)/16^k = a^4 (F/|n| - f) at side 2^k a, which tends to 0). So (T-per) says: Phi at side a exceeds 15 times its own weighted average over the larger sides. In a scale-invariant theory Phi is constant and Phi = 15 D exactly.

**False for compact U(1) and for a product with a massless factor (PROVED, given the U(1) theorem I28 as the lane holds it, Villain at beta >= 2^14, and Proposition Delta, which row 708 proves given Theorem SH of row 705).** Such a model has no seed at any size (Corollary PT1, `library/gap-crux-exercise3-max.md` L715). By Proposition Delta, D(a) > 6.1 x 10^(-4) for every a >= 3. If (T-per) held, then after at most (M - 6.1 x 10^(-4))/delta doublings D would be at most 6.1 x 10^(-4). Contradiction. For the free photon D(a) tends to a positive constant (RECALLED in row 708). QED

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

**Target (T-pin) (candidate; its open clauses are named below).** There are r_0 < r_1, delta > 0, an integer L >= 2 with: r_0 <= Rbar(l) <= r_1 implies Rbar(L l) <= Rbar(l) - delta.

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

Credit. Mack and Petkova, Ann. Phys. 125 (1980) 117, prove a confinement criterion from vortex containers; the lane holds it as RECALLED (`library/prior/gap-lit-grok.md` Section 2, `library/gap-size-rec-astra.md` 4.1: "Its proof is not rebuilt here"). The lemma below was written before I read their paper. After Step 8 I read the paper (pp. 117-134, text only; the copy at www-library.desy.de/preparch/desy/postpr/1978/desy78-069.pdf, fetched into `/tmp/gss-lit-w3/`, not committed). Their method is the one used here: a change of variables by centre elements on links between the containers, then a Fourier transform over the centre; their exact formula (2.16) and bound (2.19) are for the Wilson loop (Corollary MP of 7.4 below). Lemma PAR applies the same substitution to the twisted partition function of a container itself; the statements (ii) and (iii) (vanishing of all proper sub-products, the cumulant form, the Hoelder form) are not in the pages I read. The one-plaquette case is on file as the centre-even form of row 859 (`library/gap-brainstorm2-max.md` L106, L187). No novelty is claimed beyond this lane.

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
- **A third form of the target, (T-vor).** R = xi (sup-pin), or the moment form (Etilde |a|^n)^(1/n) with the outer pin taken in supremum; (L0) holds (pinned sub-containers), (L1) is Lemma PAR, (L3) is Mack and Petkova's criterion for the centre-odd sector only (Corollary MP of 7.4; route RE of `parts/gap.md` L153, which still needs the even step). (SS) is OPEN, and its exact form is in 3.4 below.

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

The missing statement is a **series bound**: xi(Sigma_2l, D_l) <= kappa xi(Sigma_l, D_l). Arithmetic of the map r -> 2 artanh(tanh(kappa r/2)^4) (hand values: kappa = 4: 0.3 -> 0.167, 0.4 -> 0.394, 0.5 -> 0.70; kappa = 1: a contraction everywhere): with kappa = 4 it contracts below r = 0.40 and expands above, like R(2l) = 4 R(l) - log 4 for large R. Classical scaling of a thick vortex says kappa = 4 at fixed thickness and a factor 1/4 from doubling the thickness. The blind half recovers only the entropy term log 4 of that factor 1/4. So in this form the short step is exactly: **the gain of spreading a centre flux continuously over the doubled thickness**, at order-one cost. Frozen Z_2 has no such spreading; that it has R(2l) near 4 R(l) at large beta is ARGUED (the lane's THM is the degenerate flux sectors above beta = 2.191). Two cautions. The series bound is not proved at any kappa (a closed vortex cannot be cut into pinned patches without a thin crossing at each cut). And at weak coupling the sup-pin cost is not scale invariant: for a pin that forces a non-abelian interior curvature of order one per plaquette, a spread vortex pays the mass term of Lemma FR on its whole spread region, so the cheapest vortex is thin and costs of order beta |Sigma| (ARGUED). So the supremum must be taken over outer pins at distance at least l, or in moments (the Hoelder form of (iii)).

### 3.5 Verdict on route (iii-b)

- No model is built that keeps (T1)-(T5) on isotropic cubic cells in four dimensions, for a connected simple group without matter, and has no short step. None is believed to exist (test table point 5, `parts/gap.md` L222). Mark: OPEN, as before this row.
- What is established, PROVED: the bracket identity is kept verbatim by model (d), which is ordered at large beta given the RECALLED theorem; the central-twist identities, with their blind half (Lemma PAR), are kept verbatim by model (c). ARGUED: the readings of the last column.
- So a proof of the short step must use, beyond the bracket: (1) a perfect Lie algebra, in every direction of the response; (2) a continuous path to the centre (spreading); (3) isotropy of the cell in four dimensions, so that the classical cost is scale invariant; (4) the absence of a mass term in the contact term (no matter current); (5) for the consumer, a property of the Wilson weight. Items (1), (3), (5) are found again (rules R4, R6; tests K1, K7, Proposition V). Items (2) and (4) are stated here in exact form: (2) through Lemma PAR, (4) through Lemma GG.
- Off the path of (W) except as constraints. The one exact tool added to the lane in written form is the blind half of (T-vor), which is Mack and Petkova's algebra applied to the container itself.
- 2026-11-15T20:44Z (`date -u`). Step 3 done (Section 3). Step 4, route (ii), next.

## 4. Step 4 result: route (ii), field-dependent covariant moves

Overlap named (rule 0a): row 1016's plan step 7 takes reopen condition (ii) of row 1013 in general. This section keeps to the row's own question: what is the exact cost form of a field-dependent move, and can it stay a curl form at order-one response? Notation of row 1011 3.1-3.2: a link field b acts by U_l -> exp(eps b_l) U_l; X(b) = - sum_l b_l . N_l, with N_l the force on l in the frame of its tail (for a boundary link this is Proposition A (iii)).

### 4.1 Lemma FLOW: the response is a minimum over flows (PROVED; existence of the minimiser ARGUED)

**Setting.** A cell c with pin omega, interior configuration U, action A. A **flow field** V: on each boundary link the fixed rotation B_l (so omega_s = exp(s B) omega); on each interior link l a smooth su(2)-valued function b_l(U, omega). Put div V = sum over interior links l and a = 1, 2, 3 of the derivative of b_l^a in the direction a of link l, and

  Psi_V = V A + div V.

**Statement.** Let tau_s be the flow of V. Then F_c(omega_eps) - F_c(omega) = - log E_omega[exp( integral from 0 to eps of Psi_V(tau_s) ds )]. So F_c' = - E[Psi_V], and

  H_c(omega; B) = - E_omega[V Psi_V] - Var_omega(Psi_V) <= - E_omega[V Psi_V],     F_c(omega_eps) - F_c(omega) <= - E_omega[ integral from 0 to eps of Psi_V(tau_s) ds ].

Equality holds in the first bound if and only if Psi_V is constant almost surely.

**Proof.** For fixed omega the map U -> U_eps is a diffeomorphism of the interior configuration space. Left translations generate divergence-free fields for the Haar measure, so its Jacobian J_eps satisfies (d/ds) log J_s = (div V)(tau_s). Substituting U' = U_eps in Z_c(omega_eps) gives Z_c(omega_eps) = integral of exp(A(tau_eps)) J_eps dU. The exponent minus A is g_eps = integral from 0 to eps of Psi_V(tau_s) ds, with g' = Psi_V and g'' = V Psi_V at 0. Differentiate - log E[exp(g_eps)] twice; the last bound is Jensen. QED

With the extension by zero this is Proposition A (ii) of row 1011. A field with Psi_V constant exists (ARGUED: solve the Poisson equation of the Langevin generator on the compact interior space for the mean-zero function E[X(B)] - X(B); standard elliptic theory, not rebuilt, not used below). So **the response equals the least cost over all flows**, and every explicit flow is a blind bound. This is the exact form of "moves with a controlled Jacobian". For a flow that vanishes on the boundary, E[Psi_V] = 0 and E[Psi_V^2] = - E[V Psi_V]: its cost is a variance.

### 4.2 Lemma PROJ: a frame move sees the projected force; its gradient cost is the non-conservation of that current (PROVED)

A **frame** is a field of unit vectors n_x in su(2) at the sites; it may depend on U in any way. A frame move is b = theta n, b_l = theta_l n_tail(l), theta real. Put j_l = n_tail(l) . N_l (the projected force) and D_l n = n_tail - Ad(U_l) n_head.

**Statement.** For every configuration U:
(i) X(theta n) = - sum_l theta_l j_l.
(ii) (Gauss law.) For every site z with no pinned link: sum over l with tail z of N_l = sum over l with head z of Ad(U_l)^(-1) N_l.
(iii) For lambda a real function on the sites, zero at sites with a pinned link, and (d lambda)_l = lambda_tail - lambda_head: X((d lambda) n) = sum_l lambda_head(l) (D_l n) . N_l. Equivalently, the divergence of j at z is - sum over l with head z of (D_l n) . N_l.
(iv) If the frame move is divergence free (for instance tree-transported, C8 of row 1013), its cost form is Q(theta) = E[(sum_l theta_l j_l)^2], the covariance of the projected force. Q is a curl form (zero on every gradient) if and only if j is conserved almost surely.

**Proof.** (i) X is linear in the field at the configuration U. (ii), (iii) The field G_l = lambda_tail n_tail - lambda_head Ad(U_l) n_head is the first-order generator of the gauge map g_x = exp(eps lambda_x n_x), because g_x U_l g_y^(-1) = exp(eps lambda_x n_x) exp(- eps lambda_y Ad(U_l) n_y) U_l. The action is gauge invariant, so X(G) = 0 at every U, whatever the dependence of n on U. For (ii) take lambda the indicator of z and a fixed axis. For (iii) write G = (d lambda) n + lambda_head D n. (iv) For a divergence-free field Psi = V A = X(theta n). QED

Reading. In the lab frame (n constant) j_l = a . N_l and its covariance is diagonal by the gauge average: this is Lemma WN. For U(1), j = N is conserved identically. For SU(2), j is the abelian projection of a covariantly conserved force, and it is conserved exactly where D n is orthogonal to the forces.

### 4.3 Lemma FR+: the frame defect in spectral form (PROVED; a one-line extension of Lemma FR of row 1011)

For every field v of vectors in su(2) on the sites (not necessarily of unit length), with lambda_x(omega) = min over unit n of the sum over plaquettes p based at x of |s_p x n|^2 as in row 1011 7.3:

  sum over links of |D_l v|^2 >= (1/6) sum over sites x of lambda_x(omega) |v_x|^2.

Proof. The telescoping identity of Lemma FR, (1 - Ad(omega_p)) v_x = a sum of four rotated terms D_l v, is linear in v, and |(1 - Ad(omega_p)) v| = 2 |s_p x v|. So |s_p x v_x|^2 <= sum over the links of p of |D_l v|^2. Sum over the plaquettes based at x, use the definition of lambda_x for the direction of v_x, and sum over x; a link lies in at most 6 plaquettes. QED

So the adjoint covariant Laplacian of a configuration is bounded below by lambda_x/6 as a multiplication operator: every frame, and every su(2)-valued profile, pays the non-abelian part of the field site by site.

### 4.4 Lemma SPLIT: for U(1) a twist divides exactly; for SU(2) it divides only on a reducible cut (PROVED)

In the setting of Lemma PAR take G = U(1), phase fields in place of sign fields, and twist systems tau_i^(alpha) with tau_i^(alpha) = sigma^(alpha) on the pinned links and closed outside P_i, multiplicative in alpha. Then for all alpha_1, ..., alpha_n:

  E[prod_i r_i(alpha_i; om_i)] = rho(alpha_1 + ... + alpha_n),    so   V(alpha) <= sum_i E[v_i(alpha/n; om_i)]   (Jensen).

Proof: as Lemma PAR (i), with tau = prod_i tau_i^(alpha_i). QED

Credit: Mack and Petkova state the abelian fact in words (p. 123: for an abelian group "one may compose thick vortices with any gamma from thin vortices with gamma near 1"). Their Section 3 and Appendix A (read after this lemma was written) treat U(1) in three dimensions by another route: densely packed thin containers, an upper bound on the density of the vorticity distribution, and a bound on the Fourier coefficients of a bounded density on the circle (their (A.5)), which they call a substitute for the central limit theorem. Lemma SPLIT is the direct division identity with Jensen's inequality; it is not in their text.

Use. If each sub-container obeys a quadratic class bound v_i(alpha') <= (h/2) alpha'^2, the large container obeys it with h/n. With n = 4 parallel copies this is the factor 1/4 of doubling the thickness, exactly, for every pin. This is the container form of "the blind bound is scale invariant for compact U(1)" (row 1011 3.2).

For SU(2) the same substitution with a non-central g = exp(theta n) on the links that cross a cut changes the plaquettes that cross the cut twice: the two insertions of g conjugate the tangential link u between them, and the plaquette is unchanged if and only if g commutes with u. So the fractional identity holds exactly on configurations that are reducible along the cut, with axis n. That set has measure zero. Off it the defect per crossing plaquette is the second-order term beta theta^2 |u_perp|^2, where u_perp is the part of u outside the centraliser of n: the mass term of 4.2 (iii) again.

### 4.5 Sizes (ARGUED) and the verdict on route (ii)

- **Bare links, any frame.** By 4.2 the gradient cost of a divergence-free frame move is E[(sum_l lambda_head D_l n . N_l)^2]. With E|N_l|^2 = 18 beta xbar (Lemma WN) and a defect that is not aligned against the forces, this is of order beta E|D n|^2 per site. By 4.3 and typical plaquette axes (|s_p|^2 of order 1/beta, directions not parallel), E|D_l n|^2 is at least of order 1/beta. So the mass term is of order one per site, against a curl term of order beta/l^2 at wavelength l. The curl form survives up to l^2 of order beta. For tree-transported frames the defect on a non-tree link is 1 - Ad of the holonomy of its fundamental loop, and the same count gives l^3 of order beta. Both agree with rows 1011 7.3 and 1013 (C8, C9). Not proved: the lower bound E lambda_x >= c/beta, and the exclusion of a frame built to keep D n orthogonal to the forces (one scalar condition per site against two free angles; no such frame is constructed, none is excluded).
- **At order-one response.** The band is entered with beta_eff of order one at the cell scale. With bare links at beta of 2.3 to 2.6 the count above gives cells of side 1 to 2 only. With blocked variables a frame with defect of order one per block link exists by definition of "order one", and Lemma FLOW with such a frame can give a blind bound of order one. It cannot give the sign of the next step: the frame Ward identity (4.2 (iii)) has an error term of the same order as the bracket gain, with no small parameter. In 2D the gain c_sh min(v, 1) is positive because the identity is exact.
- **What an exact repair would be.** A covariant current with j conserved pathwise (4.2 (iv)), or a divisible twist (4.4). Each exists exactly on reducible configurations only. Lemma CEN said this for field-independent multipliers; 4.2 and 4.4 say it for field-dependent frames, in exact form.
- **Verdict.** Route (ii) FAILS as a mechanism for (SS) at one bare coupling (ARGUED, with the exact Lemmas FLOW, PROJ, FR+, SPLIT behind it). With blocked variables it is the open items (N1)-(N3) of row 1011 7.4, of the (K-flow) kind, and it stops at the upper edge of the band. Tests: compact U(1) passes with zero gain (4.4: exact division, scale-invariant bound, no drop); the five-dimensional test is not reached; Lemma PT is met through the product structure of N. On the path of (W) only as a constraint.
- 2026-11-15T20:49Z (`date -u`). Step 4 done (Section 4). Step 5, route (iii-a), next.

## 5. Step 5 result: route (iii-a), energy increment (structure against randomness)

### 5.1 The dichotomy as a lemma (PROVED; it is counting)

**Lemma DICH.** Let R_0, R_1, ... and E_0, E_1, ... be real sequences with 0 <= E_j <= E_max and E_(j+1) >= E_j. Let r_0 < r_1, delta > 0, eps > 0. Suppose R_(j+1) <= R_j for all j (blind half), and for every j with r_0 <= R_j <= r_1: R_(j+1) <= R_j - delta (random case) or E_(j+1) >= E_j + eps (structured case). If R_(j_0) <= r_1, then R_j < r_0 for some j <= j_0 + (r_1 - r_0)/delta + E_max/eps + 1.

Proof. While R_j >= r_0, each step is of one of the two kinds. The first kind occurs at most (r_1 - r_0)/delta times, the second at most E_max/eps times. QED

The lemma needs three things from a model: a blind half for R, a structure energy that is bounded **and monotone**, and the dichotomy itself. The tests below are on these three.

### 5.2 The three forms of the target against the three needs

| Form | Blind half for R | A bounded monotone structure energy | The dichotomy |
|---|---|---|---|
| (T-per), R = D | none of the needed kind (D(2a) <= 16 D(a) only) | every exact monotone on file is extensive (F(n) per site, the deficit kappa of Lemma K) or blind (row 1002); a scale-invariant theory keeps every normalised quantity constant | equals "no fixed point of the doubling map" (row 708's verdict on (CAS)) |
| (T-vor), R = vortex cost | yes, in the parallel direction (Lemma PAR) | not needed in the parallel direction: Lemma PAR (iii) is already the random case with no hypothesis | fails in the series direction, see 5.3 |
| (T-pin), R = Rbar | OPEN | candidate: the non-abelian content NA of Lemma FR; see 5.4-5.5 | OPEN; its exact shape is 5.5 |

### 5.3 (T-vor): randomness has two opposite effects, so the dichotomy has no soft sign (ARGUED; the Z_2 statement is THM, lane)

By Lemma PAR the cost of a vortex confined to one of n parallel sub-containers gains the entropy of its position, with no hypothesis. The other half of a cubic doubling is the series direction (the surface Sigma grows by 4). There the classical neutrality "4 times 1/4" needs the flux to spread over the doubled thickness, and by Lemma SPLIT spreading is exact only along a common colour axis.

- If the colour axis is coherent across the transverse size (structured), the spread vortex costs the classical amount: K(2l) = K(l), minus the quantum gain. Here K(l) is the cost per patch l^2 of Sigma at thickness l.
- If it is not coherent (random), fractional twists with independent axes compose like a random walk on the group: n twists of angle theta reach a total angle of order theta sqrt(n). The spreading gain is lost and K(2l) is near 4 K(l) - log 4 (3.4).
- So in the vortex form randomness raises the normalised cost (loss of spreading) and lowers it (entropy). Which wins is a number. Frozen Z_2 shows both outcomes with no spreading at all: at strong coupling the vortex cost tends to 0, and above beta = 2.191 the flux sectors stay degenerate (the lane's THM for T_per, by a Peierls bound), which is the vortex cost not tending to 0. That K flows up there like 4 K(l) - log 4 is ARGUED. The standard reading (Mack; 't Hooft; RECALLED, a belief): SU(2) at the scale l_d where colour frames decohere behaves like a Z_2 theory of thick vortices with coupling K(l_d), and confines if K(l_d) is below the critical value.
- Verdict for (T-vor), ARGUED: the dichotomy "the response drops, or a structure energy rises" FAILS as a soft statement. At order one it is an energy-entropy balance with a threshold. This agrees with the lane's rule that the order-one input is "a number, not a qualitative property" (`library/gap-crux-fp.md` L268).

### 5.4 Lemma NAB: a written lower bound on the bare non-abelian content (PROVED by hand, given xbar >= 3/4 for its numbers)

**Setting.** Wilson SU(2), constant beta > 0, a torus with all sides at least 3 (every site free), xbar = E x_p. For a plaquette p based at x write U_p = x_p + y_p, y_p the imaginary part (y_p = s_p of row 1011). lambda_x is as in Lemma FR: the minimum over unit n of the sum, over the six plaquettes (x; mu, nu), of |y_p x n|^2.

**Statement.** (i) E(1 - x_p^2) >= xbar/(2 beta) for every beta > 0.
(ii) For p = (x; 1, 2) and p' = (x; 3, 4): E|y_p x y_p'|^2 >= 3 (E[x_p x_p'] + (1/3) E[y_p . y_p'])^2 / (218 beta^2). If xbar >= 3/4, the right side is at least 1/(654 beta^2).
(iii) For every configuration, lambda_x >= (sum over pairs p < p' of |y_p x y_p'|^2) / (sum_p |y_p|^2) >= (1/6) |y_p x y_p'|^2 for each pair. So, if xbar >= 3/4: E lambda_x >= 1/(3924 beta^2), and by Lemma FR every frame, however it depends on the field, has E sum_l |D_l n|^2 >= (number of sites)/(23544 beta^2).

**Proof.** Notation: c, c', e are unit imaginary quaternions; D is the derivative of the left translation U_l -> exp(eps c) U_l of one link l with tail x. For a plaquette q that leaves x along l, D U_q = c U_q, so D x_q = - c . y_q and D y_q = x_q c + c x y_q. Haar invariance gives E[D G] + E[G X] = 0 for smooth G, with X = D A = - beta sum over the six q containing l of c . y_q.
(i) G = X gives E[X^2] = - E[D X] = beta sum_q E[x_q] = 6 beta xbar. G = c . y_q gives E[(c . y_q) X] = - E[x_q] = - xbar. By Cauchy-Schwarz xbar^2 <= E[(c . y_q)^2] 6 beta xbar. The gauge average at x gives E[(c . y_q)^2] = E|y_q|^2/3 = E(1 - x_q^2)/3. (xbar >= 0 because the derivative of log Z in beta is 0 at beta = 0 and non-decreasing.)
(ii) Let l = (x, 1) with D, c and l' = (x, 3) with D', c'. Then D moves y_p and not y_p', and D' moves y_p' and not y_p. Put f = (y_p x y_p') . e and S_2 = exp(-A) D D' exp(A) = X X' + D D' A. Two integrations by parts give E[f S_2] = E[D D' f], and E[S_2] = 0. Now D D' f = ((x_p c + c x y_p) x (x_p' c' + c' x y_p')) . e. Average over the gauge rotation at x, which rotates y_p and y_p' together and fixes x_p, x_p': the terms linear in y vanish, and the bilinear term gives (1/3) E[y_p . y_p'] sum_i ((c x e_i) x (c' x e_i)) . e = (1/3) E[y_p . y_p'] (c x c') . e. So with (c x c') . e = 1: E[D D' f] = E[x_p x_p'] + (1/3) E[y_p . y_p']. Cost: the only plaquette that contains l and l' is (x; 1, 3), and D D' of its trace is at most 1 in absolute value, so |D D' A| <= beta. E[X^4] = - 3 E[X^2 D X] <= 18 beta E[X^2] <= 108 beta^2, the same for X'. So E[S_2^2] <= 2 E[X^2 X'^2] + 2 beta^2 <= 218 beta^2. Cauchy-Schwarz: (E[D D' f])^2 <= E[f^2] 218 beta^2, and E[f^2] = E|y_p x y_p'|^2/3 by the gauge average. For the second claim: E[x_p x_p'] >= 1 - 2 E(1 - x_p) = 2 xbar - 1, and |E[y_p . y_p']| <= E(1 - x_p^2) <= 2 (1 - xbar). So the bracket is at least (8 xbar - 5)/3 >= 1/3.
(iii) Let M = sum_p y_p y_p^T with eigenvalues lambda_1 >= lambda_2 >= lambda_3 >= 0. Then lambda_x = tr M - lambda_1 = lambda_2 + lambda_3. The second symmetric function e_2 = lambda_1 lambda_2 + lambda_1 lambda_3 + lambda_2 lambda_3 is at most (lambda_1 + lambda_2)(lambda_2 + lambda_3) <= tr M (lambda_2 + lambda_3), and e_2 = (1/2)((tr M)^2 - tr M^2) = sum over p < p' of |y_p x y_p'|^2 (Lagrange's identity). tr M = sum_p |y_p|^2 <= 6. QED

Remarks. (a) The proof of (i) is sharp for one free plaquette: with one plaquette on the link, X is beta times - c . y, E[X^2] = beta E x, and the same steps give E(1 - x^2) = 3 E x / beta with equality (test (b) of row 1015). The factor 6 in (i) is the number of plaquettes on a link. (b) The expected size of E lambda_x is of order 1/beta (ARGUED in row 1011 7.3); the proof gives 1/beta^2 because it bounds tr M by 6 in (iii). (c) The lane's RECALLED bound E(1 - x_p) <= 2/beta gives xbar >= 3/4 for beta >= 8; the lemma itself assumes xbar >= 3/4. (d) The lemma is dimension free and holds for every lattice on which x is a free site with these plaquettes. So it does not tell four dimensions from five, or the Wilson model from the models of 3.3 with Haar links. It closes one "not proved" of 4.5 in a weaker form: the mean frame defect is positive, of order at least 1/beta^2.

### 5.5 (T-pin): the shape of an engine, and where each half stands

Write NA_l for a measure of the non-abelian content of the field at the cell scale l, between 0 and 1. For bare links it is the lambda_x of Lemma NAB. For blocked links no exact definition is fixed here; this is the open slot.

**Proposition ENG (arithmetic; PROVED as an implication).** Suppose that for all scales l of a ladder:
- (FL) NA_l >= c_1 min(1, 1/Rbar(l)) (a fluctuation lower bound: a response of size R allows fluctuations of size 1/R);
- (DEC) Rbar(2l) <= Rbar(l) (1 - c_2 NA_l) (decoherence: a non-abelian field reduces the colour correlation across the next scale).
Then Rbar(2l) <= Rbar(l) - c_1 c_2 min(Rbar(l), 1). So Rbar falls by the fixed amount c_1 c_2 per doubling while it is above 1, and by the fixed factor 1 - c_1 c_2 below 1.

Proof. Insert (FL) in (DEC). QED

This is the 2D statement "each step lowers h by c min(h, 1)" (row 1009 L148-150), with the long steps included. In the words of the row: (DEC) is the random half, (FL) is the structured half. With (FL) the structured case does not need to be counted; it is excluded.

**Tests of the two halves.**

| Test | (FL) | (DEC) |
|---|---|---|
| Compact U(1), free photon | false: NA = 0 | true and empty |
| Product with a massless factor | holds per factor | Rbar^2 adds over factors (2.3), so the massless factor keeps Rbar up: the pair gives no drop, as it must |
| Adjoint Higgs, Coulomb phase (BELIEF for kappa finite) | **false at the cell scale**: the photon has Rbar of order one, the blocked field is abelian up to exp(- m_W l). True at the bare scale (Lemma NAB holds there). So a proof of (FL) at the cell scale must use the absence of a mass term for the off-diagonal directions. | true and empty |
| Frozen slices, model (d) of 3.3 (THM given the RECALLED order) | holds: spin waves keep NA positive at every scale | **false as written**: the classical cost doubles per doubling, so the true statement there is Rbar(2l) <= 2 Rbar(l)(1 - c NA). A proof of (DEC) must use the isotropic cell in four dimensions. |
| Five dimensions (BELIEF) | holds at the bare scale (Lemma NAB) | false, as for (d) |
| Frozen Q_8, 2T | not defined (no Lie algebra; lambda_x exists but the group is discrete) | not defined: K_c is a second derivative |
| Lemma PT, Proposition NP | (FL) reads the SU(2) factor; the pair then gives a drop of that factor's response only. The consumer must read the whole state space. Proposition NP is not met: no value of D is read. | same |
| Theorem D2, Lemmas SHEET, SLAB | not bound: the form is in law, on cubes, at one homogeneous strength | SLAB binds through model (d) |
| Instanton cost (6.3 of row 1013) | not reached | not reached |

The entries of the table above for the adjoint Higgs model, the frozen-slice model and five dimensions are ARGUED from the standing given in 3.3; none is a proved refutation.

**Can either half be proved?**
- (FL): its bare-scale ingredient is PROVED (Lemma NAB: the bare non-abelian content is at least of order 1/beta^2), by a Cramer-Rao step with a second-order score. That ingredient is blind. The comparison with Rbar is not made, so (FL) itself is not proved at any scale. At the cell scale it is OPEN and false in a neighbouring model, so it is selective there.
- (DEC): OPEN. No exact identity is found that turns non-abelian content into a loss of cross-cell correlation. Lemma CHAIN is the place where it would act: K at scale 2l is a covariance of cell fluxes, and each cell flux depends on the pin through the tensors K_c. For a Gaussian abelian field the tensors compose exactly and Rbar is constant. The statement needed is a strict loss in that composition when the adjoint transport through the cells fluctuates. No proof, and no counterexample in four isotropic dimensions.
- "The structured half by the account": the account controls the regime g_k <= gamma, where the response falls by the one-loop amount per step. That is a (K-flow) input above the band. Inside the band the account gives nothing, and (FL), (DEC) there are statements at order one.
- "The random half by strong coupling or mixing": at small beta the vortex form is settled by Dobrushin-type uniqueness (the lane's seed for beta < 1/18), which gives decay uniformly in pins (ARGUED for containers). It does not reach order one.

### 5.6 Verdict on route (iii-a)

- The counting lemma is trivial (PROVED). The route lives or dies on a bounded monotone structure energy. None is known: NA is not monotone on the class (it falls to 0 in the adjoint Higgs model at large scales, BELIEF; it is constant in model (d)), and every exact monotone of the lane is extensive or blind. With an a-function as the energy (row 1002), the structured steps are bounded in number, and what is left is: no theory that is nearly scale invariant with a response of order one. That is the rigidity statement of row 1017 (named match; not attacked here).
- In the vortex form the dichotomy has no soft sign (5.3). In the pinned form it takes the shape (FL) and (DEC) (5.5); the bare-scale ingredient of (FL) is proved (Lemma NAB), and (DEC) is the open selective half.
- Mark: route (iii-a) OPEN. One ingredient of the structured half is proved at the bare scale; the random half is one named inequality with an open slot (the definition of NA at the cell scale). It does not move (W).
- 2026-11-15T20:59Z (`date -u`). Step 5 done (Section 5). Step 6 next: a GUIDE control of Lemma NAB, then the test table.

## 6. Step 6: GUIDE control of Lemma NAB, and the tests

### 6.1 Control run of Lemma NAB (a guide; it can show an algebra error, it proves nothing)

**Reading written before the run (2026-11-15T21:00Z).** Script `/tmp/gss-scripts-w3/nab_control.py`: plain numpy, quaternion links, checkerboard heat bath, torus 4^4, beta in {1.0, 2.3, 4.0}, the axes c = e_1 on the link (x, 1), c' = e_2 on the link (x, 3), e = e_3, all sites x. Memory free 68 percent before the run; numeric lock held as `row1018-fable-w3`.
- (C1) identity of the first-order step: mean of (c . y_p) X equals - xbar, and mean of X^2 equals 6 beta xbar, each within 3 standard errors. FAIL means a sign or count error in the proof of (i).
- (C2) identity of the second-order step: mean of f S_2 equals mean of x_p x_p' + (1/3) y_p . y_p' within 3 standard errors, with f = (y_p x y_p')_3, S_2 = X X' - beta (k-component of the plaquette (x; 1, 3)). FAIL means an algebra error in the proof of (ii).
- (C3) the inequalities: E(1 - x^2) >= xbar/(2 beta); E[S_2^2] <= 218 beta^2; E|y_p x y_p'|^2 >= 3 (bracket)^2/(218 beta^2); E lambda_x >= (1/6) E|y_p x y_p'|^2. A measured violation beyond 3 standard errors is a FAIL of the lemma.
- (G) guide only, no pass or fail: beta E lambda_x at the three couplings (the ARGUED size of order 1/beta).

**Follow-up reading, written at about 2026-11-15T21:02Z (between the two runs; the run ended at 21:03Z by `date -u`) before the follow-up run (the first run is kept as it is, see the table below).** In the first run (C2) passed at the three couplings, with the largest deviation 2.3 standard errors at beta = 2.3. Follow-up: the same script at beta = 2.3 only, seed 777, 6000 measurements. Reading: PASS if fS2 - bracket is within 3 standard errors of 0; a deviation above 3 standard errors would mean a small systematic term missing in the proof of (ii).

**Results (first run 34 s, follow-up 52 s; outputs in `/tmp/gss-out-w3/`; lock acquired 21:01Z and released 21:03Z).** Standard errors from 20 bins. "dev" is the deviation in standard errors.

| beta | xbar | (C1) cyX + xbar | (C1) X2 - 6 beta xbar | (C2) fS2 - bracket | E(1 - x^2) against xbar/(2 beta) | E[S_2^2] against 218 beta^2 | E abs(y_p x y_p')^2 against its bound | E lambda_x against (1/6) E abs(y_p x y_p')^2 |
|---|---|---|---|---|---|---|---|---|
| 1.0 | 0.2435(4) | -0.0002(9), dev 0.2 | -0.004(4), dev 1.1 | 0.0016(12), dev 1.4 | 0.719 against 0.122 | 2.36 against 218 | 0.345 against 0.00005 | 1.812 against 0.058 |
| 2.3 | 0.6091(8) | 0.0012(25), dev 0.5 | -0.032(26), dev 1.2 | 0.0111(48), dev 2.3 | 0.539 against 0.132 | 71.2 against 1153 | 0.195 against 0.00036 | 1.299 against 0.032 |
| 4.0 | 0.8001(1) | -0.0017(33), dev 0.5 | 0.018(57), dev 0.3 | -0.0018(69), dev 0.3 | 0.335 against 0.100 | 369 against 3488 | 0.0747 against 0.00035 | 0.754 against 0.012 |
| 2.3, follow-up | 0.6094(4) | 0.0019(8), dev 2.3 | -0.007(8), dev 0.9 | -0.0026(21), dev 1.3 | 0.539 against 0.132 | 70.8 against 1153 | 0.194 against 0.00036 | 1.298 against 0.032 |

- (C1) PASS, (C2) PASS, (C3) PASS at all points, by the readings written before each run. The follow-up reading named (C2) only; its (C1) value is reported, 2.3 standard errors, inside the first reading's limit. The error of a difference is taken as if the two means were independent, which they are not; no conclusion rests on it.
- The mean plaquettes 0.2435 and 0.609 agree with row 1011's control run (0.2436 and 0.6088, another script), so the sampler is sane.
- (G) Guide: beta E lambda_x = 1.81, 2.99, 3.02 at beta = 1.0, 2.3, 4.0, and beta^2 E|y_p x y_p'|^2 = 0.35, 1.03, 1.19. This is the ARGUED size (lambda_x of order 1/beta, the cross product of order 1/beta^2). The proved bounds are far from sharp: the Cauchy-Schwarz step uses 3 to 4.5 percent of its right side.
- What the run shows: no sign or count error in the two identities behind Lemma NAB at these points. It proves nothing. The proof is the text of 5.4.

### 6.2 The tests, piece by piece (valid form: a test refutes a tool only if the hypothesis holds and the conclusion fails in the test model)

Pieces. P1 = Lemma PAR and the blind half of (T-vor). P2 = Lemma CHAIN. P3 = Lemmas FLOW, PROJ, FR+, SPLIT. P4 = Lemma NAB, the bare form of (FL). O1 = (DEC), open. O2 = the series bound of 3.4 with spreading, open.

| Test | P1 | P2 | P3 | P4 | O1, O2 (what a proof must use) |
|---|---|---|---|---|---|
| Lemma PT (product with a massless factor) | holds per central involution; a twist of the SU(2) factor says nothing on the other factor | K is block diagonal; Rbar^2 adds | the force N splits; identities hold per factor | holds per factor | a response in every Lie algebra direction; the consumer must read the whole state space |
| Proposition NP (D contracts on J doublings with no seed) | not bound: no value of D is read | not bound | not bound | not bound | a consumer that reads more than finitely many values of D; (T-per) alone is bound |
| Theorem D2 (no supremum over tilts; pinned sheets) | an identity, so not refuted; the class of containers must fix the aspect ratio, or thin containers hold 2D and 3D spin systems | in law, on cubes: not bound | identities | torus, in law: not bound | no supremum over interior pins; cubes or containers of fixed shape |
| Lemma SHEET (no uniformity over coupling fields) | holds for every strength field, so it is blind to this | one homogeneous strength | identities | one homogeneous strength | homogeneous strengths |
| Lemma SLAB | as D2 | not bound | not bound | holds also in the slab model: it is blind | O1 is false in the frozen-slice model (5.5): isotropy of the cell |
| Compact U(1) | exact division (Lemma SPLIT): scale-invariant blind bound, zero gain | Gaussian composition: Rbar constant (ARGUED) | j is conserved; the cost is a curl form; zero gain | (ii) is empty (one axis) | the bracket; the non-abelian content NA |
| Frozen Q_8, 2T | **holds verbatim**; so P1 alone gives no short step | not defined (no derivative) | not defined | not defined | the Lie algebra: a continuous path from 1 to -1 |
| Five dimensions | holds verbatim | holds verbatim | holds verbatim | holds verbatim | **none of the proved pieces sees the dimension.** O1 and O2 must: in five dimensions the classical cost of a thick vortex and of a colour twist doubles per doubling |
| Instanton cost (row 1013 6.3) | not reached: P1 deforms no field | not reached | binds a repair of route (ii) by smooth frames: a frame adapted to a pin of non-zero degree has defects (Remark HOPF of row 1011), and at order-one coupling such cells are not rare | not reached | a frame may not be assumed smooth on every cell of the band |

Summary of the tests. Every piece proved in this row is blind: it holds in at least one model without a short step (P1 in Q_8, 2T and Z_2; P2, P3, P4 in five dimensions and in the frozen-slice model). So no piece proved here is a selective gain. The selective content is in O1 and O2, and both are open.
- 2026-11-15T21:05Z (`date -u`). Step 6 done (Section 6). Step 7 next.

## 7. Step 7 result: the first surviving piece, a second derivation of it, and the exact open statements

### 7.1 Which piece survives, and in what sense

The row asks: for the first piece that survives the tests, prove it or build the counterexample. By 6.2 no piece survives as a selective gain. Two pieces survive as exact tools that the lane did not hold in proved form, and both are proved here: Lemma PAR (3.2), which gives a central response a blind half; and Lemma NAB (5.4), a written lower bound on the bare non-abelian content, which is the bare-scale ingredient of the structured half. The counterexamples asked for are the models of 3.3: for a tool made of the central-twist identities alone, frozen Z_2 above its transition; for a tool made of the bracket identity and a symmetric twist, the frozen-slice model.

### 7.2 A second derivation of Lemma PAR in a solvable case (PROVED; same author, so it is a consistency test, not a check)

Take G = Z_2 in two dimensions. A disc of area A with boundary holonomy W = +1 or -1 has Z_A(W) = C_A (1 + W t^A), t = tanh beta (sum over plaquette signs with product W). The container is a disc of area A with pin holonomy W_Om = 1; the twist sigma flips an odd number of boundary links, so rho = (1 - t^A)/(1 + t^A) and tanh(V/2) = t^A. Take two disjoint sub-discs of areas A_1, A_2, with boundary holonomies W_1, W_2, and the rest region of area A_0 = A - A_1 - A_2, whose plaquette product is W_Om W_1 W_2. Then r_i = (1 - W_i t^(A_i))/(1 + W_i t^(A_i)) and a_i = W_i t^(A_i). The weight Z_i(W_i)(1 + r_i) = Z_i(W_i) + Z_i(-W_i) = 2 C_(A_i) does not depend on W_i. So under Etilde the pair (W_1, W_2) has weight proportional to 1 + W_1 W_2 t^(A_0). Hence Etilde[W_1] = 0, Etilde[W_1 W_2] = t^(A_0), and

  Etilde[a_1] = 0,   Etilde[a_1 a_2] = t^(A_1) t^(A_2) t^(A_0) = t^A = tanh(V/2).

This is Lemma PAR (ii) and (iii) in the exact solution, obtained without the substitution argument of 3.2. The sup bound reads t^A <= t^(A_1 + A_2).

### 7.3 The exact open statements this row ends at (quantifiers and constants written)

- **O1, pinned form.** (T-pin) of 2.3 as it stands: there are r_0 < r_1, delta > 0 and an integer L >= 2 such that r_0 <= Rbar(l) <= r_1 implies Rbar(L l) <= Rbar(l) - delta, for Wilson SU(2) at one beta and every l. By Proposition ENG it follows from (FL) and (DEC) for any numbers NA_l in [0, 1] with c_1 c_2 min(r_0, 1) >= delta. At the bare scale Lemma NAB gives the ingredient E lambda_x >= 1/(3924 beta^2) (for xbar >= 3/4); the comparison with Rbar at the smallest cells, which (FL) needs, is not made here (expected sizes: E lambda_x of order 1/beta, Rbar of order beta). Strength against (W): unknown, because (T-pin) has no consumer. Tests it must pass: false in five dimensions and in the frozen-slice model, so its proof must use the isotropic 4D cell.
- **O2, vortex form.** For cubic containers, with xi the sup over outer pins at distance at least l of the vortex cost: there are kappa, phi with kappa phi < 1 such that, in the band, (SER) xi(Sigma_2l, D) <= kappa xi(Sigma_l, D) and (SPR) xi(Sigma, D_2l) <= phi xi(Sigma, D_l). Classical scaling is kappa = 4, phi = 1/4. Lemma PAR gives, in place of (SPR), only tanh(xi(Sigma, D_2l)/2) <= tanh(xi(Sigma, D_l)/2)^4. Lemma SPLIT gives (SPR) with phi = 1/4 for compact U(1) under a quadratic class bound. For SU(2) neither (SER) nor (SPR) is proved at any constants. Strength against (W): weaker (it would feed the centre-odd sector only, route RE).
- **Not reduced further.** Neither O1 nor O2 is shown equivalent to (W) or to (CAS). Under the proof-search governance both families are blocked-local, with the reopen conditions of 8.8.
- 2026-11-15T21:07Z (`date -u`). Step 7 done (Section 7). Step 8, report and RESULT, next.

### 7.4 Corollary MP: the consumer of the central response, rebuilt (PROVED; the statement is Mack and Petkova's criterion as the lane records it)

The lane holds this as RECALLED (`library/prior/gap-lit-grok.md` Section 2: the confining potential is bounded below by a sum of - log tanh(xi_i/2)). The algebra of Lemma PAR gives it in a few lines. Read after it was written: this is Mack and Petkova's inequality (2.19) with (2.20)-(2.21) for SU(2) (their p. 129-130), and the exact form below is their (2.16); the statement and the method are theirs. What is added is only that the proof is now written in the lane, in the setting of Lemma PAR.

**Setting.** As in Lemma PAR, with no twist of the pin: sub-containers Lam_1, ..., Lam_n with disjoint plaquette sets P_i, and sign fields tau_i that are closed outside P_i and equal to +1 on the pinned links. Let O be a bounded function of the links outside the Lam_i that is **odd under each tau_i**: O(tau_i eta) = - O(eta). Example: O = (1/2) tr of the holonomy of a loop C that crosses each cut an odd number of times (each container links C).

**Statement.** E[O] = Etilde[O a_1 a_2 ... a_n], with Etilde the expectation with the extra weight 2^(-n) prod_i (1 + r_i), which is normalised. Hence

  |E[O]| <= sup|O| prod_i tanh(xi_i/2).

**Proof.** For a subset S substitute eta -> tau_S eta in E[O prod over S of r_i], as in Lemma PAR (i): the weight outside is unchanged, Z_i(tau_i tau_S eta) = Z_i(eta) for i in S, Z_j is unchanged for j not in S, and O picks up (-1)^|S|. So E[O prod_S r_i] = (-1)^|S| E[O]; with O = 1 and no oddness the same step gives E[prod_S r_i] = 1. Then E[O prod_i (1 - r_i)] = sum over S of (-1)^|S| (-1)^|S| E[O] = 2^n E[O], and E[prod_i (1 + r_i)] = 2^n. Write 1 - r_i = (1 + r_i) a_i. QED

So a Wilson loop linked by n disjoint parallel containers is at most the product of the tanh of their sup-pin vortex costs. This is clause (L3) of (T-vor) for centre-odd observables, now with a written proof. It gives no statement on centre-even observables, so no gap (route RE).
- 2026-11-15T21:09Z (`date -u`). 7.4 added (Corollary MP).

## 8. Step 8: report (exercise step 9) and RESULT

Every statement below carries the mark of the section it comes from. Nothing is checked by another model.

**8.1 The wall, in plain words.** We want to show that the four-dimensional gauge field forgets its surroundings. Take a block of the field and hold its surface fixed. Its response to a change of that surface should fall as the block grows. For small blocks the known theory gives a slow, steady fall. For large blocks, where the response is already tiny, a known engine finishes the proof. In between, where the response is neither large nor small, nothing is known. OpenAI's proof for two-dimensional magnets crosses that middle range with one exact step. This row asked for the same step in four dimensions. What keeps happening: every exact formula we can write also holds in some model that does not lose its response. The evidence covers three approaches: a counter-model, moves of the field along its own colour axes, and a count of structure against randomness. Getting past it needs one inequality that is false in those models.

**8.2 What the exercise found.**
1. The step is written as an exact target in three forms (Section 2, 3.2). Each has a missing clause. The periodic form is (CAS) of row 708 and has no mechanism (Lemma ADD, PROVED). The pinned form in law has a place for a mechanism (Lemma CHAIN, PROVED) and no consumer. The vortex-container form has closure, a blind half (Lemma PAR, PROVED) and a consumer for centre-odd observables (Corollary MP, PROVED; the statement and the method are Mack and Petkova's), and no selective half.
2. Barrier (Section 3). No counter-model is built in the target's own class (isotropic cubic cells, four dimensions, a connected simple group, no matter), and none is believed to exist. PROVED: the identities of central twists hold verbatim for frozen Z_2, and the bracket identity holds verbatim in the frozen-slice model; both lack the step (the first by the lane's Peierls theorem, the second given a RECALLED theorem). ARGUED: so a proof must use a continuous path to the centre, the isotropic four-dimensional cell, a perfect Lie algebra, the absence of a matter current, and, for the consumer, the Wilson weight.
3. Covariant moves (Section 4). PROVED: the response is the least cost over all flows (Lemma FLOW); a frame move sees the projected force, and its cost is a curl form exactly when that current is conserved (Lemma PROJ); a twist divides exactly for U(1) and, for SU(2), only on configurations reducible along the cut (Lemma SPLIT). ARGUED: at one bare coupling the curl form survives up to cells of side sqrt(beta), so the route fails there; with blocked variables it is row 1011's open items.
4. Energy increment (Section 5). The counting lemma is trivial (PROVED). No bounded monotone structure energy is known. In the vortex form randomness both raises and lowers the cost, so the step has no soft sign (ARGUED). In the pinned form the step would follow from two inequalities, (FL) and (DEC) (Proposition ENG, an implication). PROVED: a lower bound on the bare non-abelian content, E lambda_x >= 1/(3924 beta^2) when xbar >= 3/4 (Lemma NAB), with a passing numeric control of its two identities (a guide).
5. Every piece proved here is blind (6.2). The selective content sits in two open statements, O1 and O2 (7.3). The wall (W) is not moved. Much of the map was on file; the new exact items are Lemmas CHAIN, PAR (as a written proof), PROJ, SPLIT, NAB, FLOW and Corollary MP (as a written proof).

**8.3 Filters corrected (each ARGUED until checked).**
- Row 1011 4.3 says that a cube has no topological twist, so the bracket machinery has nothing to act on. In the valid form this holds for cubes. A container whose boundary is not simply connected has a central twist, with an exact parallel law and a blind half (Lemma PAR) and a consumer (Corollary MP), for every group with a central involution and every beta. What comes back: the vortex-container form as a carrier of clauses (L0), (L1), (L3). It is off the direct path of (W): it reaches centre-odd observables only.
- Row 1011 7.3 has the size of the non-abelian content as ARGUED. A lower bound of order 1/beta^2 is now PROVED (Lemma NAB); the order 1/beta stays ARGUED, with guide values beta E lambda_x = 3.0 at beta = 2.3 and 4.0.
- Check 1015 lists field-dependent moves as not covered by Lemma WN. They are covered in exact form by Lemmas FLOW, PROJ and SPLIT. The conclusion "a frame exists only above the band" stays ARGUED.
- The seed (iii-a) of this row, "a structure energy rises", has no valid form on the class: the non-abelian content is not monotone there (5.6).

**8.4 Routes worth doing.** One: the check W1 below. No attack route is proposed. O1 has no consumer and no mechanism; O2 feeds the centre-odd sector only and has no mechanism.

**8.5 What not to do next.**
- A further row on covariant or frame moves at one bare coupling: the cost form has a mass term of order one per site beyond cells of side sqrt(beta) (4.5).
- A soft energy-increment row without a bounded monotone structure energy: it reduces to the rigidity question of row 1017 (5.6).
- A search for a pure-gauge counter-model in the target's own class: none is believed to exist, and the neighbouring ones are listed (3.3).
- A class statement with a supremum over all pins of a vortex cost at weak coupling: it is not scale invariant (3.4, ARGUED). Use outer pins at a distance, or moments.

**8.6 The exact price.** Not changed: (W), or (CAS) with an extensive base (`parts/gap.md` L226-237). This row adds two exact shapes of the missing step and no equivalence: O1 (pinned form; it follows from (FL) and (DEC)) and O2 (vortex form; (SER) and (SPR) with kappa phi < 1).

**8.7 Work items.**

W1 (check; a model that did not write this file; high effort). Read `library/gap-short-step-max.md` at the commit that holds it. Redo by hand, in this order: (i) Lemma ADD (2.2) with the identity D(2a) = 16 D(a) - Phi(a); (ii) Lemma CHAIN (2.3); (iii) Lemma PAR (3.2), Fact 0, (i)-(iii), and the second derivation 7.2; (iv) Corollary MP (7.4); (v) Lemma FLOW (4.1); (vi) Lemma PROJ (4.2) and Lemma FR+ (4.3); (vii) Lemma SPLIT (4.4); (viii) Lemma NAB (5.4) (i)-(iii) with every constant; (ix) Lemma DICH and Proposition ENG (5.1, 5.5). Test first: (a) in Lemma PAR, that a twist system with (H1), (H2) exists for Sigma x D with paths that end at one common boundary point, and that boundary plaquettes are unchanged; (b) in PAR (i), the step Z_j(tau_S eta) = Z_j(tau_j eta) for j in S; (c) in NAB (ii), that (x; 1, 3) is the only plaquette containing the links (x, 1) and (x, 3) when all sides are at least 3, the gauge-average constant sum_i ((c x e_i) x (c' x e_i)) . e = (c x c') . e, and E[X^4] <= 108 beta^2; (d) in NAB (iii), lambda_x = lambda_2 + lambda_3 and e_2 <= tr M (lambda_2 + lambda_3); (e) in FLOW, the Jacobian formula; (f) the hand values of the map in 3.4. Then judge the ARGUED items: the two cautions of 3.4, the sizes of 4.5, the reading 5.3, the last column of 3.3. Verdict per statement: ADVANCE, CORRECT-NO-ADVANCE or WRONG with the failing line. Stop rule: stop at the first WRONG in Lemma PAR or Lemma NAB and report it; no new attack. Output `library/gap-short-step-check-<model>.md`.

Not proposed, with reasons:
- A proof row on (DEC), or on (SER) and (SPR): no mechanism is on record for either; a row would restate the crux.
- A sharper Lemma NAB (order 1/beta): it needs upper bounds on moments of 1 - x_p^2; off the path.
- A rebuild of the order of the 3D O(4) model from the lane's Gaussian domination, to make barrier (d) a theorem inside the lane: no route consumes it.
- A numeric measurement of Rbar(l) or of the moments of the vortex activity in the window 2.3 to 2.6: a guide only; no decision of the lane moves on it.
- A consumer for the pinned form by the Birkhoff-Hopf contraction of positive kernels (RECALLED): its projective diameter is a supremum over pins on a whole face and grows with the cross-section, so it is not uniform in the volume.

**8.8 Approach registry (proof-search governance).**

| Family | Object | Mechanism | Terminal obligation | Strength against (W) | Status | Evidence | Reopen condition |
|---|---|---|---|---|---|---|---|
| F1 periodic contraction, (T-per) | D(a) | none | (CAS) | target-equivalent or stronger (row 998) | blocked-equivalent | Lemma ADD | a mechanism that gives theta < 1 from the group (route RA) |
| F2 pinned response in law, (T-pin) | cross-cell covariance of the Neumann data | Lemma CHAIN; (FL) and (DEC) | (DEC), a definition of NA at the cell scale, and a consumer | unknown | blocked-local | Lemmas CHAIN, NAB; Proposition ENG | an exact identity that gives a strict loss in the composition of the cell tensors under adjoint decoherence, and uses the isotropic 4D cell |
| F3 vortex containers, (T-vor) | sup-pin or moment vortex cost | Lemma PAR; Corollary MP | (SER) and (SPR) with kappa phi < 1 | weaker (centre-odd sector) | blocked-local | Lemmas PAR, SPLIT; Corollary MP; 3.4 | a divisible twist for SU(2), or series sub-additivity from surface entropy; and the even step of route RE |
| F4 covariant frame moves, route (ii) | flows V = theta n | Lemma FLOW; the projected current | a conserved covariant current, or a divisible twist | unknown | retired at one bare coupling; with blocked variables it is G2 of row 1011 (blocked-local) | Lemmas FLOW, PROJ, FR+, SPLIT | a frame with D n orthogonal to the forces; or block variables with a controlled action inside the band |
| F5 energy increment, route (iii-a) | a pair (R, E) | Lemma DICH | a bounded monotone structure energy | unknown | blocked: reduces to rigidity (row 1017) | 5.3, 5.6 | a scale-invariant bounded monotone that is strict away from free theories |
| F6 barrier, route (iii-b) | counter-models | identities kept by the model | a counter-model in the target's class | not a route | no model found; a list of constraints | 3.3, 3.5 | none |

Assumptions most likely to be wrong in this row: the ARGUED sizes (the sup-pin cost under a non-abelian pin, 3.4; the alignment of the frame defect with the forces, 4.5); the reading that the vortex step has no soft sign (5.3). Most expensive if wrong: Lemma PAR and Lemma NAB (they carry the new exact content). Literature worth translating: none further. Mack and Petkova's paper was compared with Lemma PAR and Corollary MP (3.2, 7.4); their remark on p. 123, that the change of free energy may be proportional to the surface of the container at fixed diameter, agrees with the caution of 3.4.

RESULT: Row 1018 (Claude Fable 5.2 max, Mac mini worker 3; author, checked by no one; one numeric guide run; no literature search, one paper read for credit): the 4D short step is written as an exact target in three forms, and none is proved; the wall (W) and (CAS) are not moved. PROVED by hand, unchecked: Lemma ADD ((T-per) is (CAS) of row 708, and D(2a) = 16 D(a) - Phi(a)); Lemma CHAIN (the cross-cell covariance of the Neumann data at scale L l is the covariance over rings of the cells' mean fluxes); Lemma PAR (for parallel sub-containers, tanh(V/2) is exactly the n-th cumulant of the sub-container activities, so the vortex cost has a blind half) with Corollary MP (a loop linked by n containers is at most the product of tanh(xi_i/2); this is Mack and Petkova's inequality (2.19), by their method, now written in the lane) and a second derivation in 2D Z_2; Lemmas FLOW (response = least cost over flows), PROJ (a frame move sees the projected force; curl form if and only if that current is conserved), FR+ and SPLIT (a twist divides exactly for U(1), and for SU(2) only on reducible cuts); Lemma NAB (E(1 - x_p^2) >= xbar/(2 beta); E lambda_x >= 1/(3924 beta^2) when xbar >= 3/4), with a passing control of its identities at beta = 1.0, 2.3, 4.0 (guide only); Lemma DICH and Proposition ENG (implications). Verdicts: route (iii-b) builds no counter-model in the target's class and finds, PROVED, that central-twist identities hold verbatim in frozen Z_2 and the bracket identity in the frozen-slice model, so a proof must use more than the bracket (ARGUED list of five inputs); route (ii) FAILS at one bare coupling (ARGUED) and is row 1011's (N1)-(N3) otherwise; route (iii-a) is OPEN, with no bounded monotone structure energy, no soft sign in the vortex form (ARGUED), and the pinned form reduced to (FL) and (DEC). Every proved piece is blind (holds in a model without the step). Filters narrowed: "no topological twist" holds for cubes, not for containers; the size of the non-abelian content now has a proved lower bound. Open: O1 (the pinned step, or (DEC) with a definition of NA at the cell scale and a consumer), O2 ((SER) and (SPR) with kappa phi < 1), the ARGUED sizes of 3.4, 4.5, 5.3, the check W1; (W), (CAS) and the seed untouched.
