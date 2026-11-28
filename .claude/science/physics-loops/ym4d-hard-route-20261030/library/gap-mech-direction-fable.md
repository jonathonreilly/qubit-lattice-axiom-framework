lead: anthropic/claude-fable-5-2/high mac-mini-worker
lease_until: 2026-11-22T17:05Z

# gap-mech-direction-fable (row 1380): direction for the mechanism programme

Status: DONE 2026-11-22T05:52Z (date -u). Worker pinned at commit 95f5d4e1a, branch claude/ym4d-hard-route. No commit, no push (relay
copies). Reading order: 3.1 (judgement), 4.4-4.5 (the proved result), 5 (next rows), 6 (report).
Started 2026-11-22T05:05Z (date -u).

## 0. Plan and status log

Plan (written before any derivation):

1. Read the rules (FINISH.md rule sections, GOAL.md), row 1378 (the switch), row 1379's output
   `library/prior/gap-mech-lit-luna.md`, the target statement (M-neutral) of row 1367 with the chain 1342, 1349,
   1356, 1359 and the lead notes after Theorem ZD-c in `library/gap-phys-seed.md`.
2. Read the prior work the row names: rows 1009-1018, 1021 (pinned-cell port, open items (N1)-(N3)), checks 1014,
   1015, rows 1139, 1140.
3. Section 2: the live mechanisms, each with first exact statement, non-equivalence to the seed, U(1) test.
4. Section 3: pick one; first lemma, what it reads, which chain statement consumes it.
5. Section 4: attack on that lemma.
6. Section 5: the next three rows with decisive outcomes.
7. RESULT line.

Status log (each line stamped by date -u in the command that wrote it):

- 2026-11-22T05:05Z file created; reading rules next.

- 05:05Z read: FINISH.md L1-84 and L299-351 (rules, incl. 'Equivalent is not progress'), GOAL.md, rows 1378-1380, `library/prior/gap-mech-lit-luna.md` in full, `library/gap-seed-astra62.md` L1-60 ((M-neutral)), `library/gap-phys-seed.md` L296-330 (ZD, ZD-c, lead notes). Next: rows 1009-1021, 1139, 1140.
- 05:14Z read: RESULT parts of rows 1009-1018, 1021, 1139, 1140; `library/gap-pinned-cell-gauge-max.md` Section 7 (L438-512, (N1)-(N3)); `parts/gap.md` L4-104 (state of attack, methods 19-36, lead rules CL and W2). Section 1 written next.
- 05:23Z grep of 46 mechanism terms over the gap files (all on file except 'charge-2'); read results of rows 1141, 1171, 1175, 1177, 1197, 1244; `prior/gap-2don-proofs-read-opus.md` L118-156 (OpenAI's one-annulus engine); `gap-invent-selective-max.md` L99-150 (C1-C8, Lemma WN). Next: kill verdict on C1 and the astra check items 12-17.
- 05:33Z read: C1's kill verdict (`gap-invent-selective-max.md` L152-232) and astra check items 11-18 (`gap-invent-selective-check-astra.md` L50-75): C1 and C2 are open again, the fourth-order family identity was never written. Checked 14 more terms (remnant symmetry, Coulomb confinement: rows 1041, 1045, 1141 and `gap-mini-solve-x-opus.md` L52 hold the frame readings). Next: where the seed chain stopped (rows 1375-1377).
- 05:36Z Sections 1.3 and 2 written (Lemma H). Next: Section 3, the mechanisms with first statements and tests.
- 05:41Z Section 3 written: mechanisms M-A to M-F with first statements, tests and verdicts; judgement 3.1. Next: Section 4, Theorem C1 with proofs.
- 05:42Z Section 4 written: the pick (class A1), Lemma SP, Lemma BR, Theorem C1, Lemma PIN. Next: a control run of the constants, then Section 5.
- 05:49Z Re-read of Section 3 found one overclaim (A2: 'kappa bounded by b alone' does not follow from Lemma H); corrected with Lemma H' (4.7) and rows 1026, 1034 (found by grep 'conserved current'). Control run 4.8 PASS. Next: Section 5 and the report.
- 05:52Z Sections 5 (three next rows) and 6 (report) written; two citations corrected (row 1145 (22)-(24); row 1058 removed). Next: re-read of every PROVED item and cited line, then the RESULT line.
- 05:52Z re-read of the PROVED items against the text: two wording repairs (Lemma H last line; the elementary bound cites Corollary WN2). RESULT written.

## 1. Inputs read, the target, and the constraints a mechanism must meet

Credits. The target form and its chain are the lane's: Theorem ZD-c (row 720, `gap-phys-seed.md` L311), (N-phys)
(rows 1161, 1342, 1349), (M-neutral) (Claude Fable row 1356, check 1359; stated in gpt-6.2-astra's row 1367,
`gap-seed-astra62.md` L9-L13). The 2D sources are OpenAI's O(4) and O(3) papers (github.com/openai/math, read in rows
1007, 1009, 1010, 1379) and Ding, Huang and Yang, arXiv:2611.04908 (rows 1006, 1379). The existence chain is Balaban's
and Sussman and Alpoge's (with Claude and Codex as authors of their text). Nothing below is checked by another model.

### 1.1 The target, as read

(M-neutral), `gap-seed-astra62.md` L11: on the prescribed trajectory fix one physical side L, n_j = L/a_j, 4 | n_j,
beta_0 <= beta_j <= B_0 log n_j. In the range of P_0 (zero spatial twist, average over the eight electric centre
translations), with transfer eigenvalues lambda_0 > lambda_1 >= ..., put s(t) = sum over a >= 1 of
(lambda_a/lambda_0)^t. Wanted: some L with s(2 w_j) <= 4/21 at every late cutoff, w_j = floor(n_j/1024).
In words: the neutral thermal trace of the cube of side L at the physical temperature 512/L is the vacuum term up to
4/21. Consumers: rows 1356/1359 (rank-one test), 1342/1349 ((N-phys), then (G_ev-phys), then the matched gap clause
given (P1)-(P4), (H2), (TOT)).

### 1.2 What the record says a mechanism must be (rows 1378, 998, 1011-1021, 1139-1140)

- (S) Selective: no gain for compact U(1) in four dimensions at weak coupling; a gain for SU(2).
- (T) Typical: it reads the Wilson law of the background, not a supremum over pins, tilts or coupling fields
  (Proposition B' and Theorem BH of rows 1011/1016; Theorem D2 row 977; Lemma SHEET row 996; row 1139 far above the
  window).
- (NE) Not equivalent to the seed or to (W) (rule of 2026-11-22).
- The direct port of the 2D engine fails at the twist: SU(2) has the bracket but no non-gauge symmetric continuous
  twist (Lemma CEN+ of row 1016, with the scope corrections of its astra check); compact U(1) has the twist and no
  bracket. The repair (N1)-(N3) needs a colour frame, which exists only above the band.
- The 2D proofs cross their band with an inequality valid at EVERY coupling (rows 1009, 1010). Neither 2D proof
  replaces the supremum by a typical field in the gain step itself (row 1379 (a)); Ding-Huang-Yang is typical in an
  auxiliary environment and selective through the extra intensity N - 2 (row 1379 (b)).


### 1.3 Repo search (rule "Repo first") and what a blind pass found already on file

Method: one loop of `/usr/bin/grep -l -i -F` over `library/gap-*.md` and `library/prior/gap-*.md` for 60 mechanism
terms, then the RESULT parts of the rows that matched. Row 1379's file holds the cross-branch search of this
programme (main, PR 10114, 10133, 10134, 10141: no mechanism). I did not repeat it.

Every mechanism I wrote down before reading was on file. Matches, so that the next row does not redo them:

| Blind candidate | On file at | Standing there |
|---|---|---|
| Typical-field Ward identity with a colour frame | (N1)-(N3), row 1011 7.4; row 1141 (2), (9)-(13) | frames fail on typical cells in the window (PROVED by gpt-6.2-astra, unchecked) |
| Jensen or relative-entropy bound of a spread twist | Lemma JEN row 1013; rows 1171, 1177 (33)-(35); row 1244 | the bound sees screening: the 4D running is a bubble, the 2D running a tadpole (row 1244, ARGUED) |
| Ding-Huang-Yang port: abelian part in a random environment | row 1197 (`gap-mini-solve-g-fable.md`), Lemma G1, G2, (GC) | fails at the free collective coordinate (ARGUED) |
| Centre signs given the SO(3) field | C6 row 1013; check 870 | no gain: the conditional Z_2 model is ordered for both groups at large beta |
| Layer of time-like links as a 3D O(4) model in an SO(4) background | C5 row 1013; rows 1139, 1140 | uniform form false far above the window; typical form OPEN |
| Remnant colour symmetry of a complete gauge as the rigid group | rows 1041, 1045, 1141; `gap-mini-solve-x-opus.md` L52 | frames; blocked |
| Adjoint-Higgs Coulomb phase and five dimensions as tests | A16 `gap-compact-rigidity-max.md` L94; row 1011 Section 6 | tests on file (belief grade for A16) |
| Thermal shift integrated along the coupling | row 1145 (22)-(24) and its Section 9; (MONO-Delta) `gap-phys-seed.md` L355 | restates the seed at each coupling |
| Exact stiffness as direct term minus the best Bogoliubov ratio | row 1244 Lemma 2.1 (F'' = D_K - V_K) | identity; no test flow with the logarithm |
| Soft Bianchi constraint, plaquette angles | Identity CUBE, Lemma SOFT row 1016 | no consumer |
| Lab-frame link-end moves, corner twists | C1, Lemma WN row 1013; astra check items 12-13 | **exclusion not established; the fourth-order family identity never written** |
| Non-central path to the centre twist | C2 row 1013; astra check item 14 | **exclusion not established** |

So two items of the 2D-engine port are open on the record: C1 and C2. Section 4 closes C1 with a proof.

## 2. What the 2D engine needs, in one inequality (Lemma H)

Source: OpenAI, exponential decay for O(n), n >= 3, as digested by Claude Opus in
`prior/gap-2don-proofs-read-opus.md` B(2) steps 2-5 (their Lemma 2.1, (2.10)-(2.12), Proposition 2.2,
Proposition 3.1, Lemma 3.2). I did not re-read the paper; the statement below uses only the displayed form of
their Proposition 2.2. Label: the engine inequality is theirs; Lemma H is a remark on it, PROVED here, unchecked.

**Setting (abstract).** A set C of cells (edges in 2D; corners in Section 4). Twist fields are real or complex
functions on C with the l^2 norm. Move fields f_i (i = 1..M) are complex functions on a set V (vertices; link-ends
in Section 4). Each move field has a trivial twist u_i = d f_i, a cost gamma_i = |u_i|_2^2, an amplitude
alpha_i = |f_i|_inf^2, and a bracket S_i = S(f_i, conj f_i), a twist field with the pointwise bound

  |S_i(c)| <= |f_i|_inf |u_i(c)|   for every cell c.                                   (2.1)

(In 2D: S(f, conj f)_e = i Im(f_x conj f_y) = i Im(f_x conj(f_y - f_x)).) The engine inequality has the form

  R(Q, conj Q) <= K |T|_HS^2 + B sum over i, j of min(alpha_i gamma_j, alpha_j gamma_i),          (2.2)

with Q = sum_i S_i, T = sum_i u_i (x) conj u_i, K >= 0 and B > 0 (OpenAI: K = 6 beta^2 + 4 beta^(3/2) + beta,
B = beta). R is the second-order response; R(h, conj h) <= B |h|_2^2 is the elementary bound, and R does not change
when a trivial twist is added. If Q = lambda h~ with h~ = h + (trivial), the engine yields

  R(h, conj h) <= Y := [right side of (2.2)] / lambda^2.

Write |[h]|_2 for the least l^2 norm in the class of h modulo trivial twists. The elementary bound gives
R(h, conj h) <= B |[h]|_2^2.

**Lemma H (the gain is at most the square root of the spread of softness).** Put rho_i = alpha_i/gamma_i (the
softness of move i) and kappa = max_i rho_i / min_i rho_i. Then

  sum over i, j of min(alpha_i gamma_j, alpha_j gamma_i) >= kappa^(-1/2) |Q|_2^2,   hence   Y >= B kappa^(-1/2) |[h]|_2^2.

Proof. alpha_i gamma_j = (alpha_i gamma_i)^(1/2) (alpha_j gamma_j)^(1/2) (rho_i/rho_j)^(1/2)
>= kappa^(-1/2) (alpha_i gamma_i)^(1/2) (alpha_j gamma_j)^(1/2), and the same for alpha_j gamma_i. Sum over i, j:
the left side is at least kappa^(-1/2) (sum_i (alpha_i gamma_i)^(1/2))^2. By (2.1), |S_i|_2 <= (alpha_i gamma_i)^(1/2),
so sum_i (alpha_i gamma_i)^(1/2) >= sum_i |S_i|_2 >= |Q|_2. Last, |Q|_2 = lambda |h~|_2 >= lambda |[h]|_2, and the
right side of (2.2) is at least B times the sum. QED

**Reading.** The engine beats the elementary bound only through a hierarchy of softness: moves whose amplitude
is large against their cost, with ratios spread over many scales. In 2D the moves are spin rotations by a
slowly varying angle. Their amplitude is free (the global symmetry), their cost is beta |df|^2, and plane waves
on a box of side N have softness between 1/N^2 and 1 in suitable units, so kappa^(1/2) = N and the proved gain
log N is allowed. The requirement, in words:

  (SOFT) a family of measure-preserving moves of the integration variables, defined on every configuration,
  whose softness spreads over a range that grows with the cell, and whose brackets generate the twist that the
  consumer reads, modulo trivial twists.

The four dead ends of the record are four ways to miss (SOFT): no rigid non-central group (Lemma CEN+, row 1016);
frames give soft covariant moves only where the frame defect is small (Lemma FR row 1011, row 1141 (2));
first-order bounds with bounded flows see screening (row 1244); a ball has no free collective coordinate
(row 1197 (GC)). Section 4 adds the exact form for lab-frame moves: there the softness has no spread at all.


## 3. Task (1): the mechanisms, each with its first exact statement, its tests and my verdict

Tests used in every row. (U1) compact U(1), d = 4, weak coupling: massless (the row's test). I add two tests that
are on file and that the U(1) test alone does not replace: (5D) SU(2) in five dimensions at weak coupling
(massless, belief grade; row 1011 Section 6); (AH) SU(2) with an adjoint Higgs field in its Coulomb phase
(massless, belief grade; item A16 of row 1017). Reason: a statement about the ultraviolet roughness of typical
SU(2) fields passes (U1) and still holds in (5D), so it cannot be a gap mechanism. "Reads" says typical (means
under the Wilson law) or supremum. (NE) is the rule of 2026-11-22.

### M-A. The 2D-type engine (trivial moves, brackets, fourth-order bound)

- First exact statement: (SOFT) of Section 2 for a named class of moves, with the pin twist of an annulus or a cell
  as target; then the port of OpenAI's Proposition 2.2 in the form (2.2).
- Three classes of moves.
  - A1, lab-frame link-end moves (C1 of row 1013). Reads: typical under Lemma WN, supremum under the elementary
    bound. **Closed in Section 4 (Theorem C1, Lemma PIN): the softness has no spread; no pin twist is reached.**
  - A2, covariant one-colour moves along a field-built axis (C7, C8 of row 1013; (N1)). Reads typical. On file:
    row 1141 (2), (9)-(13): on typical Wilson cells in the window every adjoint section has covariant energy at
    least c/(1 + b + (log R)^(1/2)) per unit norm, and every tree transport has a mass-like defect. Rows 1026 and
    1034 (Claude Fable, unchecked) hold the exact criterion: a curl bound needs a conserved current j - d of a
    local frame ((SYM)); link frames have it and change no bound (Proposition LF); for every pin-measurable
    site frame the cost of a boundary rotation is not a curl form off reducible pins (Theorem BD). In the
    language of Section 2 a mass m in the cost form caps the gain at a multiple of 1/m (Lemma H' in 4.7). With
    row 1141 (2) the cap is of order (1 + b + (log R)^(1/2))^(1/2): it does not depend on the family, but row
    1141's bound lets it grow like (log R)^(1/4), so this alone does not close A2 (GIVEN row 1141 (2), unchecked;
    that the engine's cost for a section is its covariant energy is ARGUED). Open on the record: "a general
    field-dependent frame whose Jacobian cancels the signed defect" (row 1141), and (SYM) for site frames.
  - A3, dressed moves: a translation of a block-scale mode together with the response of the finer modes. This
    is row 1244's conclusion ("a 4D step of the Jensen kind must carry the fluctuation response of an RG step").
    Remark TAD below says why. No exact statement exists outside the account's small-field region.
- (U1): one generator, all brackets vanish, no gain. Passes. (5D): the cost of a constant-field twist is not
  scale-free, no logarithm. Passes. (AH): not tested.
- (NE): the engine's output is a twist cost of a pinned cell. I cannot show that a pin-twist bound is not
  equivalent to the seed, because no consumer from a pin-twist bound to (M-neutral) is written (row 1141 names
  this gap as (L3)).
- Verdict: A1 dead (PROVED here). A2 blocked for pin twists by Theorem BD of row 1034 and in the window by row
  1141, not closed as a class. A3 is not a one-scale statement: it is M-D below.

**Remark TAD (why undressed moves are never soft on typical fields; ARGUED, the content is rows 1011 7.3, 1141 (2)
and 1244).** Let lambda be a Lie-algebra field of one colour in the smoothest available gauge of a typical
configuration U = e^a, wavelength r. Its second-order cost is the gradient term beta |d lambda|^2, of order
beta |lambda|^2 / r^2, plus beta |[a, lambda]|^2. The second term has mean of order beta <|a_l|^2> |lambda|^2 =
c |lambda|^2 with c of order one in lattice units at every beta (the fluctuation of one link is of order
beta^(-1/2)). This is the tadpole. Gauge invariance cancels it against a second-order term (the bubble), not at
first order. So for r above beta^(1/2) the first-order cost of every undressed one-colour move is mass-like, the
softness is bounded by a constant of order one, and (SOFT) fails. In the 2D model the move is a symmetry made
local, its cost is exactly the gradient term, and there is no tadpole. This is the same statement as "log S =
(1/2) log b" in row 1011 7.3. Lemma MC of row 1016 (exact rotations of a link about its staple, the generators of
overrelaxation) gives moves of zero cost that are not gauge; they keep the action pointwise and the measure of
every pinned cell, so their brackets are again exact symmetries and reach no twist.

### M-B. The non-central path to the centre twist (C2 of row 1013)

- First exact statement: on the periodic box of side n, Z(t) = the partition function with g_t = exp(t c) inserted
  at one corner of each plaquette of a co-closed sheet; wanted - Z''(t) <= delta_n Z(t) on [0, pi] with delta_n
  to 0. Then Z(pi)/Z(0) >= 1 - pi^2 delta_n / 2 (OpenAI's integration from the maximum).
- Reads: second derivatives of a free energy along a path of twisted laws; no supremum over pins.
- Consumer: the flux half only (rows 1175, 1177: given the neutral bound, (W) is equivalent to a small
  elementary twist cost). **It does not serve (M-neutral).**
- (U1): Z(t) is the partition function with flux t through one plane; - Z''(0)/Z(0) is of order beta. No gain.
  Passes.
- Standing: by Corollary WN2 of row 1013 (HOLDS in the astra check), - Z''(0)/Z(0) = beta rho n^2 for the sheet
  of n^2 plaquettes, rho = xbar - (beta/3) E(1 - x^2), and the lab-frame smearing is the same function of t. So
  the first statement is FALSE at t = 0 as soon as rho > 0. By the Schwinger-Dyson equation of one link, rho =
  (beta/3) times the sum over the five other plaquettes at a link of E[y_p . y_p'] (row 1013 writes this as a
  same-link field-strength correlation). rho > 0 is open on file (astra item 15); it holds if E(1 - x) <
  3/(3 + 2 beta).
- (NE): the conclusion at t = pi is the flux half, which with (N-phys) is equivalent to (W) (row 1175). I cannot
  show the hypothesis is not equivalent to it.
- Verdict: not live for the target. For the flux half it is false as posed given rho > 0.

### M-C. Locality of the one-step kernel on typical faces (the layer; C5 of row 1013, row 1139's open item)

- Object: K(A, A') = int prod_x dg_x exp(beta sum over space links l = (x, y) of (1/2) tr(g_x A'_l g_y^(-1)
  A_l^(-1))), the kernel of the kinetic part of the transfer operator between the slices A and A'. It is the
  partition function of a 3D O(4) model in the SO(4) background (A, A').
- Exact identity (elementary): the mixed second derivative of log K in two link directions of A' is the layer
  covariance of the two forces. So decay of layer covariances is quasi-locality of log K.
- First exact statement (LAY-cov): there are C and ell(b) with E | Cov_layer(f_x, h_y | A, A') | <= C exp(- |x - y|
  / ell(b)) for local functions of g near x and y, the mean taken over the Wilson law of two neighbouring slices.
- Reads: typical faces (the Wilson law of the pair of slices). Not a supremum.
- Why it could be selective: in U(1) the layer is a 3D XY model in the background A' - A. It keeps the exact global
  symmetry theta to theta + const in EVERY background, so at weak coupling it has a Goldstone mode and power-law
  covariances; then log K = - (beta/2) |(A' - A)^T|^2 up to corrections, with the dipole kernel of the transverse
  projection (ARGUED). For SU(2) the background (A, A') has trivial stabiliser on typical slices, the layer has no
  continuous symmetry, and by row 1141 (2) its fluctuation operator at a maximiser has a mass of order one.
- (U1): passes in this argued form. **(5D): fails as a gap mechanism: the mass comes from the roughness of thin
  links, which is the same in five dimensions at weak coupling.** So (LAY-cov) is true or false together in 4D
  and 5D and cannot separate a gapped theory from a massless one.
- (NE): not equivalent to the seed (it does not see the scale).
- Consumer: none. The Durhuus-Frohlich comparison needs the background-uniform form, which is false far above the
  window (rows 1139, 1140).
- Verdict: a true-looking selective fact about Gauss's law (colour-electric flux is not conserved on typical
  fields, so the instantaneous Coulomb kernel is short-ranged at the lattice scale), with no consumer and no
  information on the gap. Not picked.

### M-D. A flow statement through the band (K-flow) with dressed moves

- What it would say: for a class A(b) of laws on block fields, defined by typical-field properties and containing
  Wilson's first-passage data at b = 4/gamma^2, one block step maps A(b) into A(b - c) for every b >= b_0, and
  A(b_0) has a seed.
- (U1): the abelian class is mapped into itself with c = 0. (5D): b grows. (AH): a clause of A must exclude
  long-range order of an adjoint section.
- (NE): a class with a proved step is not the seed. But I cannot write a class. The account controls block
  actions only while g_k <= gamma (row 1012); Proposition NP and Lemma PT bind classes read through
  finitely many numbers (lead rule W2); Lemma AFF binds one-sample criteria (lead rule CL).
- Verdict: this is where the problem is. No first exact statement is available to me. Not picked.

### M-E. Statements that restate the seed (not mechanisms, by the rule)

- The thermal shift along the coupling: log(1 + s_(n, beta)(t)) = int_0^beta d beta' [E^(t) - E^(infinity)](sum_p
  x_p), since the transfer operator has rank one at beta = 0. On file: row 1145 (22)-(24) with the derivative
  identity of its Section 9; (MONO-Delta), `gap-phys-seed.md` L355. The path stays
  at lattice temperature 1/t; with t = 2 w_j this is below the deconfinement point at every beta' <= beta_j. A
  bound on the integrand at each beta' is the seed at each coupling. EQUIVALENT in kind; no progress.
- The whole-face conditional likelihood at physical time (rows 1367-1377): where the seed chain stopped.
- Typical-pin mixing of a cell at one scale: by lead rule CL a two-sample mean with a small constant is one-scale
  mixing of the class.

### M-F. The Ding-Huang-Yang port

- Standing: row 1197 (GC): a ball of gauge field has no collective coordinate with a scale-free law. I add one
  remark (ARGUED): the collective coordinates of a gauge field with an exactly known law are the gauge frame
  (Haar, but invisible to invariant functions) and the centre flux sectors of a torus (discrete). Neither gives
  a good-box event of probability bounded below at every scale.
- Verdict: dead for the target as far as the record goes.

### 3.1 Judgement

1. **No mechanism with an exact first lemma is live for the neutral target (M-neutral).** The two items that the
   record left open in the 2D port are C1 and C2. C1 is closed in Section 4. C2 serves the flux half only and is
   false as posed when rho > 0.
2. The 2D proofs use symmetric soft moves. In 4D SU(2) every undressed move has a mass-like first-order cost on
   typical fields (Remark TAD, Theorem C1, row 1141). The gain can only come from dressed moves, which is a
   renormalization step in the band (M-D). The two 2D papers do not have this problem and give no tool for it.
3. The (U1) test alone lets ultraviolet facts through (M-C). The (5D) test should be part of the selectivity test.

## 4. Tasks (2) and (3): the pick, its first lemma, and the attack. Result: C1 is closed (Theorem C1, Lemma PIN)

**The pick.** M-A, class A1: the corner-twist engine with lab-frame link-end moves. It is the one item of the 2D
port that the record left open with an unwritten first lemma ("the fourth-order family identity was never
written", astra check of row 1013, item 13). Its first lemma is (SOFT) for this class: a family of link-end
fields whose brackets give lambda times a twist class with lambda growing against the cost.
- What it reads: with free sites, means under the Wilson law (Lemma WN (iii) of row 1013); without them, the
  elementary bound, which is uniform over pins. So the class has both readings.
- Which statement would consume it: the analogue of OpenAI's Proposition 3.1 (a vanishing twist cost of a pinned
  annulus), then a mixing bound for pinned cells. No statement of the chain 1342-1359 consumes a pin-twist bound
  today (row 1141's open step (L3)). So even a success would have needed a second lemma.
- Outcome: the first lemma is FALSE in the strongest sense. The proof needs no fourth-order identity.

Everything in this section is PROVED by hand by Claude Fable 5.2 in this session and checked by no one. Lemma WN
(i)-(ii), which I use only for the definitions, is row 1013's and holds in its astra check.

### 4.1 Setting

A periodic lattice Z^4/(n Z)^4, n >= 3. A set of pinned links; the other links are integrated with Haar
measure. (A pinned cell is the case where all links outside a box are pinned.) A link-end is a pair e = (l, x)
with x an end of l. V_x is the set of the 8 link-ends at x. Two link-ends at x are opposite if their links have
the same direction. A corner at x is an ordered pair c = (e -> e') of non-opposite link-ends at x, one for each
plaquette through x, oriented as the plaquette: there are 24 corners at x, one for each unordered non-opposite
pair. The corner graph Gamma_x has vertex set V_x and one edge for each corner. It is K_(2,2,2,2) (row 1013 4.1).

For a complex function f on link-ends put (delta f)_c = f_e' - f_e, gamma(f) = |delta f|_2^2 = the sum over corners
of |f_e' - f_e|^2, alpha(f) = the largest |f_e|^2, kappa_x(f) = the mean of f over V_x, r = f - kappa (the
reduced field), |r|_x^2 = the sum over V_x of |r_e|^2. The bracket of f is the real corner field

  S(f)_c = Im(conj(f_e) f_e').

(With F_e = f^1_e a + f^2_e b, f = f^1 + i f^2 and [a, b] = c: [F_e, F_e'] = S(f)_c c. So row 1013's corner
bracket B = (1/2)[F_e, F_e'] is (1/2) S(f)_c c.) A real corner field is removable if it is delta G with G a real
function on link-ends that vanishes on the ends of pinned links: by Lemma WN (i)-(ii) the translation by G is a
change of Haar variables and the twisted partition function does not change. For a real corner field h,
|[h]|_2 is the least value of |h + delta G|_2 over such G. Since delta and the pinning condition act inside each
V_x, |[h]|_2^2 is a sum over sites of a function of the restriction of h to the corners at that site.

### 4.2 Lemma SP (spectrum of the corner graph)

The Laplacian of Gamma_x has eigenvalues 0 (once), 6 (four times), 8 (three times). Hence for every complex f

  6 |r|_x^2 <= the sum over corners at x of |f_e' - f_e|^2 <= 8 |r|_x^2.

Proof. The adjacency matrix is A = J - 1 - M, with J the all-ones matrix and M the matching of opposite
link-ends. On constants A = 8 - 1 - 1 = 6. On the functions with sum 0 that are even under M (dimension 3),
J = 0 and M = 1, so A = -2. On the functions that are odd under M (dimension 4), J = 0 and M = -1, so A = 0.
The Laplacian is 6 - A. Apply it to the real and imaginary parts of f; r is the part orthogonal to constants. QED

### 4.3 Lemma BR (the bracket modulo removable fields)

For every complex f that vanishes on pinned link-ends, S(f) = S(r) + delta g with g_e = Im(conj(kappa_x) r_e) for
e in V_x. The field g is real and vanishes on pinned link-ends. Further

  the sum over corners at x of |S(r)_c|^2 <= (1/2) |r|_x^4.

Proof. conj(f_e) f_e' = |kappa|^2 + conj(kappa) r_e' + conj(r_e) kappa + conj(r_e) r_e'. The imaginary part of the
third term is - Im(conj(kappa) r_e). So S(f)_c = g_e' - g_e + S(r)_c. At a pinned link-end f_e = 0, so r_e =
- kappa_x and g_e = Im(- |kappa_x|^2) = 0. For the bound, |S(r)_c| <= |r_e| |r_e'|, and the sum over unordered
pairs of |r_e|^2 |r_e'|^2 is at most (1/2) (sum over V_x of |r_e|^2)^2. QED

In words: the free part of a link-end field at a site, its mean kappa_x, is a gauge rotation. It can be as
large as one likes at no cost, and its bracket with anything is removable. Only the reduced field r makes a
bracket, and r is controlled by the cost (Lemma SP). Amplitude and cost are the same thing on the corner graph.

### 4.4 Theorem C1 (the corner engine has no gain)

Let f_1, ..., f_M be complex functions on link-ends that vanish on pinned link-ends. Put alpha_i = alpha(f_i),
gamma_i = gamma(f_i), Q = sum_i S(f_i), Q~ = sum_i S(r_i), T = sum_i (delta f_i) (x) conj(delta f_i). Then

  (I)  |Q~|_2^2 <= (2/3) sum over i, j of min(alpha_i gamma_j, alpha_j gamma_i),
  (II) |Q~|_2^2 <= (7/72) |T|_HS^2,

and Q - Q~ is removable. Consequently, let any inequality of the form (2.2),

  R(Q, conj Q) <= K |T|_HS^2 + B sum over i, j of min(alpha_i gamma_j, alpha_j gamma_i),   K >= 0, B >= 0,

be used with a family for which Q = lambda h + (removable), lambda > 0, h a real corner field. The bound that it
gives for the response of h, Y = (right side)/lambda^2, satisfies

  Y >= ((72/7) K + (3/2) B) |[h]|_2^2.

Proof. By Lemma BR, Q - Q~ = delta(sum_i g_i) is removable. At a site x, by the triangle inequality and Lemma BR,
the l^2 norm of Q~ over the corners at x is at most 2^(-1/2) sum_i |r_i|_x^2. So

  |Q~|_2^2 <= (1/2) sum_x (sum_i |r_i|_x^2)^2 = (1/2) sum over i, j of sum_x |r_i|_x^2 |r_j|_x^2.            (4.1)

(I): |r_i|_x^2 <= the sum over V_x of |f_(i,e)|^2 <= 8 alpha_i, because subtracting the mean lowers the l^2 norm.
By Lemma SP, sum_x |r_j|_x^2 <= gamma_j / 6. So sum_x |r_i|_x^2 |r_j|_x^2 <= (4/3) alpha_i gamma_j, and the same
with i and j exchanged; insert the smaller one in (4.1).
(II): T is positive semi-definite. Dropping the blocks between different sites lowers the Hilbert-Schmidt norm:
|T|_HS^2 >= sum_x |T_x|_HS^2. T_x has rank at most 7, the rank of delta on V_x, so |T_x|_HS^2 >= (tr T_x)^2/7, and
tr T_x = the sum over i of the cost of f_i at x >= 6 sum_i |r_i|_x^2 by Lemma SP. So |T|_HS^2 >= (36/7) sum_x
(sum_i |r_i|_x^2)^2 >= (72/7) |Q~|_2^2 by (4.1).
Last, Q~ = lambda h + (removable), so |Q~|_2 >= lambda |[h]|_2. Insert (I) and (II) in the right side. QED

**What it says.** Whatever the constants K and B of a port of OpenAI's Proposition 2.2 to corners are, and
whatever family is used (any number of modes, any supports, any scales), the bound for a twist class [h] is at
least a fixed multiple of |[h]|_2^2. The elementary bound is also a multiple of |[h]|_2^2 (at most 4 beta
|[h]|_2^2 by the direct term of Lemma WN's proof; at most beta xbar |h|_2^2 under the hypotheses of Corollary WN2).
|[h]|_2^2 is a sum of site-local terms. So the route can change the constant and nothing else: no logarithm, no
dependence on the size of the cell, in any dimension. In the language of Lemma H the softness of every reduced
move lies between fixed numbers. This is the exact form of row 1013's sentence "the family inequality is a
one-site statement", which its check could not accept as a deduction. The fourth-order identity need not be
written.

**What it does not say.** It is a statement about the bounds this route can produce. It does not bound the
true response from below. (At t = 0 and for corners at distinct free sites the true response is beta rho |theta|_2^2
by Corollary WN2 of row 1013, also site-local.)

### 4.5 Lemma PIN (no pin twist is a bracket class)

Let G be a real function on the ends of pinned links, extended by 0 to the other link-ends, and h = delta G: the
corner field of the pin twist u_l -> exp(G_(l,x) c) u_l exp(- G_(l,y) c). Suppose lambda h = sum_i S(f_i) + delta G'
with lambda not 0, and f_i, G' vanishing on pinned link-ends. Then G is constant on the pinned link-ends at each
site. So the twist is a gauge transformation of the pinned links by exp(phi_x c), and Z(twisted pin) = Z(pin).

Proof. Let c = (e -> e') be a corner at x with e or e' pinned. Then S(f_i)_c = Im(conj(f_(i,e)) f_(i,e')) = 0.
So lambda (G_e' - G_e) + G'_e' - G'_e = 0. If both are pinned, G_e = G_e'. If e is pinned and e' is not, G'_e' =
lambda G_e. Take two pinned link-ends e_1, e_2 at x. If they are not opposite, G is equal on them. If they are
opposite, any third link-end e_3 at x is opposite to neither; if e_3 is pinned, G_(e_1) = G_(e_3) = G_(e_2); if
not, lambda G_(e_1) = G'_(e_3) = lambda G_(e_2). So G = phi_x on the pinned link-ends at x. Put phi = 0 at the
sites without pinned link-ends. The gauge transformation by exp(phi_x c) maps the pinned links to the twisted
pinned links, keeps every plaquette trace, and is a change of Haar variables on the integrated links. QED

**What it says.** The consumer of the 2D engine reads the twist of the pinned boundary of an annulus. In the
corner class the brackets of bulk moves reach only those pin twists that are gauge transformations, whose cost is
zero already (Lemma TWIST of row 1013). The abelian boundary field of the Schrodinger functional, with a
transverse part, is never reached. This is the gauge form of "a gauge cell that is a ball has no free collective
coordinate" (row 1197): in the spin model the relative rotation of the inner and outer pins is not removable,
here it is.

### 4.6 Standing of M-A after this section

| Class of moves | Standing | By |
|---|---|---|
| A1 lab-frame link-end moves, any family, any port of the form (2.2) | CLOSED: no gain in scale; no pin twist reached | Theorem C1, Lemma PIN (PROVED here, unchecked) |
| A2 one-colour covariant moves along site frames, sections or tree transports | blocked: no curl form for a pin-measurable site frame at a pinned face; mass-like defects in the window; gain capped by Lemma H' | row 1034 Theorem BD, Corollary P (Claude Fable, unchecked); row 1141 (2), (9)-(13) (gpt-6.2-astra, unchecked) |
| A2 general field-dependent moves with Jacobian one | open as a class; (SYM) for site frames NOT DECIDED (row 1034); Remark TAD argues the first-order cost is mass-like | rows 1034, 1141 |
| A3 dressed moves | not a one-scale statement; needs block actions in the band | row 1244; M-D |

### 4.7 Lemma H' (a mass in the cost form caps the gain; PROVED, unchecked)

Setting of Section 2. Assume in addition: (a) each cell c has a vertex v(c) with |S_i(c)| <= |f_i(v(c))| |u_i(c)|,
and each vertex is v(c) for at most D cells; (b) |u_i(c)| <= 2 |f_i|_inf for every cell; (c) (MASS) the move fields
satisfy |f_i|_2^2 <= gamma_i / m^2 for one m > 0. Then

  sum over i, j of min(alpha_i gamma_j, alpha_j gamma_i) >= (m / (2 D^(1/2))) |Q|_2^2,   so   Y >= (m B / (2 D^(1/2))) |[h]|_2^2.

Proof. |Q|_2^2 <= sum over i, j of sum_c |S_i(c)| |S_j(c)|. By (a) and (b) the inner sum is at most
alpha_i^(1/2) (2 alpha_i^(1/2)) sum_c |f_j(v(c))| |u_j(c)| <= 2 alpha_i D^(1/2) |f_j|_2 gamma_j^(1/2) <= (2 D^(1/2)/m)
alpha_i gamma_j, by the Cauchy-Schwarz inequality and (c). The inner sum is symmetric in i and j, so it is at most
(2 D^(1/2)/m) min(alpha_i gamma_j, alpha_j gamma_i). QED

Reading. (a) and (b) hold in 2D with D at most 4. (MASS) fails there, because constants are free: that is the global
symmetry. A local symmetry removes the free part site by site (Lemma BR) and leaves a field with (MASS) (Lemma SP,
m^2 = 6). Theorem C1 is this lemma for corners, with better constants. For a covariant frame the mass is the
least covariant energy of an adjoint section per unit norm (row 1141 (2), in units of the stiffness).
Lemma H (Section 2) is the weaker statement that needs no mass.

### 4.8 Control run (GUIDE only; it decides nothing)

Run 2026-11-22 under the numeric lock (holder row1380-fable, acquired and released; 62 percent memory free
before the run; 1 second; 34 MB). Script and output are in the scratch folder of this session, not in git.
Pass criteria written in the script before the run: (a) the eigenvalues of the Laplacian of K_(2,2,2,2) are
0, 6 (x4), 8 (x3); (b) the identity of Lemma BR to 1e-10 relative, and g = 0 on pinned link-ends; (c) (I) and
(II) of Theorem C1 on random families (1 to 6 sites, 1 to 5 modes, amplitudes spread over four decades, large
gauge parts, sparse supports, pinned link-ends with probability 0, 0.2 or 0.5).
Result: PASS. (a) 0, 6, 6, 6, 6, 8, 8, 8. (b) largest relative defect 2.7e-16; g on pinned ends 3.5e-17.
(c) 3,956 families; the largest ratio of the two sides was 0.209 for (I) and 0.062 for (II) (both must be at
most 1). So the constants 2/3 and 7/72 are not sharp. The run cannot prove the inequalities; the proofs are 4.2
to 4.4.

### 4.9 Where Section 4 sits against rows 1026 and 1034

Rows 1026 and 1034 treat covariant frames: the cost of a frame move is a curl form if and only if a current
j - d is conserved with a local potential ((SYM), Proposition CURL). Section 4 treats the remaining case that
their check left open, the lab-frame class of row 1013, where the moving group is the gauge group itself with
link-end parameters. The common reading (ARGUED; the proved parts are Theorem C1, Lemma PIN, and Proposition LF,
Theorem BD of row 1034):

  a soft family of undressed moves is the local form of a continuous symmetry that is global and not local.
  The Wilson measure has local continuous symmetries (the gauge group; the staple rotations of Lemma MC), and
  for them every parameter is exactly free and the rest is uniformly stiff. A local symmetry has no soft modes.

The step from "no soft family in the classes tried" to "no global continuous symmetry with local field-dependent
generators exists" is not proved (astra check of row 1016, L207). It is the open classification behind M-A.

## 5. Task (4): the next three rows, each with its decisive outcome

Each row opens with "Moves:" as the rules ask. Models follow the owner's split; the lead decides.

**Row 1. `gap-mech-direction-check-astra62` (cross-provider check; gpt-6.2-astra max).**
Moves: the standing of C1, the last unwritten item of the 2D port, and the judgement 3.1 that no mechanism with
an exact first lemma is live for (M-neutral).
Task: check line by line Section 2 (Lemma H), Section 4 (Lemmas SP, BR, PIN, H'; Theorem C1) and the verdict
lines of Section 3. Test first: (a) that (2.2) is the form of OpenAI's Proposition 2.2 in the primary text
(pp. 5-8; I used the lane's digest only); (b) the (5D) verdict on M-C; (c) "false as posed given rho > 0" in M-B;
(d) each (NE) line.
Decisive outcome: C1 is closed, and `parts/gap.md` records the 2D port with no open first lemma for the neutral
target; or the first failing line reopens it.

**Row 2. `gap-selective-5d-sweep-opus` (reading and short proofs; Claude Opus 5.5 high).**
Moves: the selectivity test of row 1378. The (U1) test lets ultraviolet facts through (M-C; row 1141 (2)).
Task: for every positive selective statement on the record (row 1141 (2) and (8); Lemma NAB of row 1018; Lemma FR
of row 1011; Identity CUBE and Lemma SOFT of row 1016; Corollary WN2's rho; Proposition LF and Theorem BD of row
1034; M-C here; any other in the registry of `parts/gap.md`), say in one line whether its proof uses d = 4
through a scale-free sum, and whether the statement holds verbatim for SU(2) in five dimensions at weak coupling
and with an adjoint Higgs factor. No new attack.
Decisive outcome: the list of selective facts that survive (5D). If the list is empty, the lane holds no
selective fact that sees the scale, the programme has only M-D, and the lead adds (5D) to the selectivity test.
If one survives, it is the seed of a mechanism and gets the next proof row.

**Row 3. `gap-short-step-variance-fable` (direction and first statement of M-D; Claude Fable 5.2 high, then a
cross-check).**
Moves: M-D, the only form of the engine left (dressed moves), which has no exact first statement.
Start from: row 1018 (the short step in three forms, O1 and (DEC)), row 1244 (Lemma 2.1, the split F'' = D_K - V_K
and Proposition 2.3), rows 1026 and 1034 ((SYM), Theorem BD), and Section 4 here.
Task: for one explicit gauge-covariant block map of ratio 2 and one explicit lift of a block move, write the exact
identity "cost of the block move under the blocked law = cost of the lift under the Wilson law minus the mean
conditional variance, given the block field, of the lift's divergence term" (the variance decomposition; the
second term is the bubble, the excess of the first over the classical curl form is the tadpole of Remark TAD).
State the one-step inequality (BUB): bubble minus tadpole >= c > 0. Run (U1) (both terms vanish for the harmonic
lift), (5D) and (AH). Compare at weak coupling with the Ward-Takahashi identification of the marginal term
that row 1012 quotes from Balaban CMP 109. Then a GUIDE run in the window (beta = 2.3 to 2.6, ratio 2), with the
pass and fail criteria written first.
Decisive outcome: (i) the sign of (BUB) in the window. If the measured gain is not positive with margin at some
coupling, this form of the short step is dead and M-D has no engine form. (ii) If it is positive, (BUB) is one
inequality between two means of the Wilson law at each coupling: a (K-one) number at every b, read on typical
fields, selective by construction. Then the lead knows the exact statement the mass gap needs from the band, and
the owner can decide whether a hand proof or a formal computation is the route. I expect (ii), and I do not see
a hand proof.

**Lead-level items (no row).** (1) After Row 1, mark C1 closed in `parts/gap.md` and note that C2 serves the flux
half only. (2) Add (5D) to the selectivity test. (3) The small lemma rho > 0 (astra item 15 of row 1013's check)
would make C2 false as posed; it is a number in the band at intermediate coupling and I would not queue it.

## 6. Report

**Kind of result.** A direction row. One proved negative result on a quantified class (the row's "equally good
result"), a judgement, and three rows. No step of the gap chain is proved. Nothing here is checked by another
model. The control run is GUIDE only.

**PROVED by hand in this session (unchecked).**
- Lemma H (Section 2): in any engine inequality of the form (2.2) the gain over the elementary bound is at most
  the square root of the spread of the softness alpha_i/gamma_i of the moves.
- Lemma H' (4.7): if the move fields obey |f|_2^2 <= gamma/m^2, the gain is at most 2 D^(1/2)/m, for every family.
- Lemma SP (4.2): the corner graph K_(2,2,2,2) has Laplacian eigenvalues 0, 6, 8.
- Lemma BR (4.3): the bracket of a link-end field is the bracket of its reduced field plus a removable field.
- Theorem C1 (4.4): for lab-frame link-end moves, every bound of the form (2.2), with any constants K, B and any
  family, is at least ((72/7) K + (3/2) B) |[h]|_2^2, and |[h]|_2^2 is a sum of site-local terms. No gain in scale.
- Lemma PIN (4.5): the bracket classes of bulk lab-frame moves contain no pin twist except gauge changes of the
  pin, whose cost is zero.
So candidate C1 of row 1013 is closed without writing its fourth-order identity. It was the item its astra check
reopened.

**ARGUED (not proved).** Remark TAD; the (U1) and (5D) verdicts on M-C; the cap for class A2 from row 1141 (2);
the reading in 4.9 (a local symmetry has no soft modes); the remark on collective coordinates in M-F.

**Judgement (Section 3.1).** No mechanism with an exact first lemma is live for (M-neutral). The 2D engines need
soft symmetric moves. A gauge theory has only local continuous symmetries, for which every parameter is free and
the rest is stiff. What is left is a renormalization step in the band with dressed moves (M-D), which the two 2D
papers do not need and do not supply.

**Equivalence rule.** No statement proposed here is claimed to be a sufficient condition for the seed. The (NE)
lines say where I could not show non-equivalence (M-A's consumer is unwritten; M-B's conclusion is the flux half).
M-E lists the statements that restate the seed.

**Not done.** I did not re-read OpenAI's Proposition 2.2 in the primary text (digest only). I did not read rows
1026, 1027, 1034 in full (their RESULT lines and the first lines of `gap-sym-reg.md`). I did not repeat the
cross-branch search (row 1379 ran it for this programme). No literature search beyond row 1379. M-D has no
statement. The lemma rho > 0 is open.

**Credits.** OpenAI (the O(n), O(3), O(4) papers: the engine, Proposition 2.2, the form (2.2)); Ding, Huang and
Yang (arXiv:2611.04908); Balaban; Sussman and Alpoge with Claude and Codex (the account); Durhuus and Frohlich
(the layer picture, as on file); the lane's rows by Claude Fable, Claude Opus, gpt-6.2-astra and gpt-6-luna named
at each use: 1011, 1013 (corner formalism, Lemma WN, C1, C2), 1016 (CEN+, MC), 1018, 1026, 1034 ((SYM), BD), 1139,
1141 ((2), (9)-(13)), 1197 ((GC)), 1244 (tadpole against bubble), 1379 (literature).

RESULT: Row 1380 (Claude Fable 5.2 high, Mac mini worker 1; author, checked by no one; one 1-second control run, GUIDE only; no subagents). Direction for the mechanism programme. (1) Mechanisms: six families listed with first exact statement, tests and verdict (Section 3); judgement: no mechanism with an exact first lemma is live for (M-neutral). The 2D engines need soft symmetric moves; a gauge theory has only local continuous symmetries, whose parameters are all free and whose remainder is stiff. (2)-(3) Picked the one unwritten item of the 2D port, candidate C1 of row 1013 (lab-frame corner twists), and closed it: PROVED by hand, unchecked: Lemma H (the gain of any engine inequality of OpenAI's form is at most the square root of the spread of softness), Lemma H' (a mass m in the cost form caps the gain at 2 D^(1/2)/m), Lemma SP (corner graph K_(2,2,2,2): eigenvalues 0, 6, 8), Lemma BR, Theorem C1 (every bound of that form is at least ((72/7) K + (3/2) B) times a site-local class norm: no gain in scale, for any family and any constants), Lemma PIN (bulk brackets reach no pin twist except gauge changes of the pin). The fourth-order corner identity need not be written. C2 serves the flux half only and is false as posed if rho > 0 (open). The typical-face layer statement passes the U(1) test and fails the five-dimensional test (ARGUED), so the selectivity test should include five dimensions. (4) Next rows: the cross-provider check of this file; a sweep of the record's selective facts against the five-dimensional and adjoint-Higgs tests; the short step as one conditional-variance inequality (BUB) with its sign test in the window. OPEN: every form of the seed, (M-neutral), (W); a first exact statement for the band step with dressed moves (M-D); class A2 for general field-dependent moves and (SYM) for site frames (rows 1034, 1141); rho > 0; the primary text of OpenAI's Proposition 2.2 was not re-read (digest only).
