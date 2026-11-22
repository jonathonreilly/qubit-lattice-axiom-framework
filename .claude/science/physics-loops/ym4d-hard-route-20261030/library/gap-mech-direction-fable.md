lead: anthropic/claude-fable-5-2/high mac-mini-worker
lease_until: 2026-11-22T17:05Z

# gap-mech-direction-fable (row 1380): direction for the mechanism programme

Status: IN PROGRESS. Worker pinned at commit 95f5d4e1a, branch claude/ym4d-hard-route. No commit, no push (relay copies).
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
| Thermal shift integrated along the coupling | row 1145 (24); (MONO-Delta) `gap-phys-seed.md` L355 | restates the seed at each coupling |
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
so the sum is at least sum_i |S_i|_2 >= |Q|_2. Last, |Q|_2 = lambda |h~|_2 >= lambda |[h]|_2. QED

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

