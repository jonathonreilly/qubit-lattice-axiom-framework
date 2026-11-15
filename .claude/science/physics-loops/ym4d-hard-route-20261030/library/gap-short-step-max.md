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
