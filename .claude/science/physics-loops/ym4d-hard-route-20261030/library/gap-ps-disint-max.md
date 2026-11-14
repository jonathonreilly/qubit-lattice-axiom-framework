lead: anthropic/claude-fable-5-2/max mac-mini-worker
lease_until: 2026-11-15T00:06Z

# gap-ps-disint-max (queue row 957): Piazza-Shen disintegration against (LSI-J-seed)

Worker file, written section by section. Pinned at commit 5da1cade7 of `claude/ym4d-hard-route`.
Author: Claude Fable 5.2 (max), Mac mini worker 1, as AUTHOR. Not checked by another model.
Labels used: PROVED, CONDITIONAL (on named inputs), GUIDE (numeric, proves nothing), OPEN.

Credit. The new input is Piazza and Shen, arXiv:2610.35286 (Theorem 1.1). The lattice two-slice setting and
the vacuum factors follow the gap lane of this repository, which builds on the account of Ethan Sussman and
Levent Alpoge (with Claude and Codex as authors of their text). Each section names what it takes from whom.

## 0. Plan (at most eight steps; one step per response)

1. Read the target: (LSI-J-seed), Theorem BR, Corollary BR-J and Section 7.3 of `library/gap-fc-max.md` (row 947),
   and the two prior digests (`library/prior/gap-fullread-2.md` Section 1, `library/prior/gap-lit-bridge-lsi.md`).
   Duplicate check against `library/open-core.md` and the FINISH rows. Write the exact statements.
2. Read Piazza-Shen itself (`~/ym4d-papers/dl-2026-11-11/`): the two-scale criterion, the block law, the coarse
   law, and where dimension 2 is used. Write the proof skeleton with line anchors.
3. STEP 1 of the row: which step fails in 3D/4D and why; is the two-slice law J closer to their 2D setting
   (disintegration over temporal links, or over one slice given the other).
4. STEP 2 of the row: fact tests (compact U(1) Coulomb phase, frozen Q_8 and 2T, SMALL-BOX use of the box size,
   the worst-case ceilings 2/3, 0.775, 4 G_3 = 1.0109, the Bakry-Emery ceiling at beta 1 of row 941).
5. STEP 3, stage A: the two-scale disintegration of J written as a real proof attempt; the block conditional
   laws and their LSI constants.
6. STEP 3, stage B: the coarse law at the box size; close it or state the exact obstruction.
7. If it does not close: the smallest unproved inequality, and one GUIDE test (run only under the numeric lock
   and with 50 percent memory free).
8. Verdict table and the RESULT line.

Status log (updated in place):

- Clock correction (12:36Z). Earlier entries of this log and three section headers carried clock times that I
  had estimated, not read; they were wrong by more than an hour. Measured times: file created 12:06Z; first launch
  of the GUIDE batch 12:32:07Z (sanity only, stopped); relaunch (batch 1b) 12:34:19Z. Everything in Sections 1-6 and
  7a was written between 12:06Z and 12:36Z, in the order of the file. The order "criteria, then run" is as stated.
- 12:06Z file created. Then, in order: Sections 1-2; Section 3 (STEP 1); Section 4 (STEP 2); Section 7a (criteria);
  first launch 12:32Z; amendment (A1); relaunch 12:34Z; Sections 5-6; Section 7 (7.1, 7.2).
- 12:36Z: batch 1b running; batch 1c (dense counts, addition (A2)) queued behind it.
- 12:41Z: batch 1b done (12:34:19Z-12:39:51Z); Section 7b written with its results; batch 1c running.
- 12:45Z: batch 1c done (12:39:51Z-12:41:13Z); dense counts added to 7b; self-check corrections (four numbers or
  wordings in Sections 1, 3, 4); Section 8 (verdicts) and the RESULT line written. Item finished.

## 1. Target, objects, duplicate check (READ; no new claim)

**Read at 5da1cade7.** FINISH.md (lines 1-84, 299-349, rows 954 and 957), GOAL.md, `library/gap-fc-max.md`
(row 947) lines 39-282 and 487-590, `library/prior/gap-fullread-2.md` Section 1, `library/prior/gap-lit-bridge-lsi.md`
in full, `library/gap-lsij-scale-opus.md` (row 954, in progress) Sections 3, 4, 5b-5e, 6, and the four ceiling lines
of `library/gap-status-1113.md` (68, 110, 112, 341).

**Objects (row 941 and row 947, quoted in short).** B a periodic spatial box, L = 3|B| links, M = (S^3)^L in R^(4L)
with the unit-sphere metric. V(x) = -beta sum_p (1/2) tr x_p. T_0(x, w) = e^(-V(x)/2) e^(beta <x, w>) e^(-V(w)/2),
<x, w> = sum_l <x_l, w_l> (temporal gauge). Omega its top eigenfunction, nu = Omega^2 dx, m(dw) = e^(-V(w)/2) Omega(w) dw.
The two-slice law is J(dx, dw) = m(dx) e^(beta <x, w>) m(dw)/Z on M x M.

**Reading of J used below (one line; PROVED by unrolling Omega = lim lambda_0^(-n) T_0^n 1).** m(dx) = e^(-V(x)) H(x) dx,
where H(x) is the integral over a half-infinite time of the Wilson weights of all plaquettes that do not lie in the
slice of x (limit of normalised finite times). So
  J(dx, dw) = H(x) e^(-V(x)) e^(beta <x, w>) e^(-V(w)) H(w) dx dw/Z.
J is the law of two consecutive time slices of the 4D Wilson measure on B x Z in temporal gauge. H is the "vacuum
factor". It is gauge invariant and not local.

**Target (row 947, 7.1-7.3).**
  (LSI-J)_(alpha_J): Ent_J(Phi^2) <= (2/alpha_J) E_J[ |grad_x Phi|^2 + |grad_w Phi|^2 ] for smooth Phi on M x M, bounded
  above and below, invariant under the gauge group acting on both slices at once (tangential gradients).
  (LSI-J-seed)_a: on B = (24a)^3, one even a >= 30: (LSI-J) with alpha_J >= 2 beta K_a, K_a = (C_beta(x_*) + 3 log a)/(a - 2),
  C_beta(x_*) = log(72 beta 24^3/x_*) (16 at beta 2.3).
Corollary BR-J (row 947; HOLDS in check 949 per the queue row): (LSI-J-seed)_a gives (HC-vac)_(K_a), and Proposition HC
(row 931, check 938) then gives the seed.

**Two remarks on the size of the target (PROVED, arithmetic).**
- (T1) With box side b = 24a: 2 beta K_a = 48 beta (C_beta + 3 log(b/24))/(b - 48). So (LSI-J-seed) asks for alpha_J above
  about (144 beta log(b/24) + 48 beta C_beta)/b on ONE box of side b. Any lower bound alpha_J(b) with
  b alpha_J(b)/log b -> infinity gives (LSI-J-seed)_a for some a. In particular a box-uniform (LSI-J), with any
  positive constant, gives it. This is why a volume-uniform theorem of Piazza-Shen type is the right kind of input.
- (T2) The free photon has alpha_J = c_min = beta (e^(omega_min) - 1), about 2 pi beta/b (row 954 Section 3). It fails
  (T1) by the factor (24/pi)(C_beta + 3 log a) b/(b - 48), above 200 for a >= 30 (row 947 4.3 has 59 for the rate form).

**Duplicate check (rule 0a).** `grep -n -i -E "LSI-J|Piazza|disintegrat|two-scale|Otto|Reznikoff|log-sobolev|LSI"`:
no hit in `library/open-core.md` and `library/l17c.md`; one unrelated hit in `library/open-registry.md` (line 276,
H-STAGE). FINISH rows that name Piazza-Shen or a two-scale method: 689, 690, 697, 713, 719, 735, 939, 955 (reading
rows or one-line leads), 936 (two-scale wording for the cut rotation; another object), 941 (names "a block or
two-scale decomposition" as a possible input; its result has no such attempt), 947 (states (LSI-J-seed)), 954 (GUIDE
measurement of R_J; in progress; no proof attempt), 957 (this row), 958 (its check). No row attacks (LSI-J) by a
disintegration. Disintegration of J over one slice given the other IS the older route: (LSI-vac) + (SG-step)/(SC),
rows 931, 941, 944, 950, 952. I do not attack (SG-step) or (SC); Section 3 only places them. I proceed.

**Sussman-Alpoge account.** Rows 938-941, 946, 947 and 955 record that `library/sa-index/` has no log-Sobolev,
hypercontractive or two-scale statement (955: only block Poincare estimates of the deterministic RG, and SA 3717-3720
"No gap above the invariant subspace has been proved"). I did not repeat those greps. Their account enters through
the transfer frame and the slice/axial-gauge setting. Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex
as authors of their text.

## 2. Piazza-Shen, read in full (arXiv:2610.35286v1, 26 Oct 2026, pp. 1-11; fetched to a scratch folder, not committed)

`~/ym4d-papers` does not exist on this machine. I fetched the PDF from arxiv.org and read the extracted text
(pp. 1-11 in full; pp. 12-13 are Remark 7.2 and references). Page and equation numbers below are theirs.

**Theorem 1.1 (p. 1).** G = SU(N), periodic square lattice (Z/LZ)^2, density exp(N beta sum_p Re Tr U_p) against product
Haar. Then Ent(F^2) <= 2 C_(N,beta) sum_e integral of |grad_e F|^2, for all smooth F of ALL edge variables, with C_(N,beta)
independent of L. Metric: Hilbert-Schmidt, <X, Y> = Tr(X^dagger Y), for which Ric = (N/2) g.

**Proof skeleton, with the place where each input is used.**
- (PS-a) Section 2, group only. Single-plaquette density w, e^(-2t) <= w <= e^(2t), t = N^2 |beta|. Doeblin split
  w = (1 - r) + r v, r = 1 - e^(-2t)/2. Lemma 2.1: w^(*k) = 1 + r^(k-1) (w - 1) * v^(*(k-1)). Lemma 2.2: w^(*k) - 1 and its
  first two derivatives are at most M r^(k-1) in sup norm. (2.5): the same for log w^(*k) once M r^(n-1) <= 1/3.
- (PS-b) Section 3, the 2D step. Block B of m x m plaquettes, n = m^2. Integrate the n - 1 edges I_B that cross an
  axial spanning tree of plaquette centres. (3.1): the integral of prod_(p in B) w(U_p) over I_B equals
  w^(*n)(W_(dB)(s)), a function of the boundary holonomy only. Used: each integrated edge lies in exactly two
  plaquettes, and the identity integral of w(A u B) w(C u^(-1) D) du = w^(*2)(B A D C).
- (PS-c) (3.2)-(3.3): the marginal of the kept edges S is prod_B w^(*n)(W_(dB)(s)) ds; the conditional law of the
  integrated edges is a product over blocks. Used: the kept edges carry no plaquette weight of their own (a
  one-dimensional skeleton), and the blocks are separated by kept edges.
- (PS-d) Lemma 4.1 and (4.3), the macro law. |Hess log w^(*n)(W_(dB))| <= 4 n^(1/2) (|grad psi| + |Hess psi|), psi = log w^(*n):
  perimeter 4 n^(1/2) against the decay r^(n-1) in the AREA n. For n large the Hessian of the macro log-density is at
  most 1/2, and Ric - Hess >= 1/2 gives the macro LSI with constant 4 by Bakry-Emery. Used: positive Ricci
  curvature. This is the only place; it is why U(1) is excluded (Remark 1.2).
- (PS-e) Section 5, the micro laws. Haar product LSI (Bakry-Emery) plus Holley-Stroock on one block: K = e^(4tn).
  Group-blind apart from the Haar LSI; blocks of bounded size only.
- (PS-f) Section 6, gluing. Entropy chain rule (6.1); Lemma 6.1 bounds the gradient of s -> nu_s(F^2)^(1/2) by the
  block Poincare inequality and |grad_e H_R| <= 2t. Group-blind. This is the two-scale criterion of Otto-Reznikoff
  and Grunewald-Otto-Villani-Westdickenberg in the simple form of Bauerschmidt-Bodineau (their references
  [OR07, GOVW09, BB19]).
- (PS-g) Section 7: C_(N,beta) must grow with beta (at least beta^(1/3) for SU(4), from a degenerate non-minimal critical
  point; Remark 7.1: the test function can be gauge invariant). So no beta-uniform LSI is to be expected.

**Their own words on dimension (p. 2, short quote).** "In higher dimensions, conditional integrations would naturally
produce nonlocal, larger Wilson loops, which would be much more difficult to analyze."

**What the theorem is, in the lane's language.** The mechanism is (PS-a)+(PS-b): one block of area n is disordered
as soon as ONE of its n plaquettes takes the flat part (1 - r) of the Doeblin split, because in two dimensions a
loop bounds one surface. The rate r^(n-1) is an area law at every beta. (PS-d) then needs only that the area decay
beats the perimeter. (PS-e) and (PS-f) are soft.

## 3. STEP 1: which step of Piazza-Shen fails in 3D/4D, and whether J is closer to 2D

Setting for 3.1-3.5: Wilson SU(2) on a finite periodic lattice of dimension d, density proportional to
exp(beta sum_p t_p), t_p = (1/2) tr U_p, against product Haar. Unit-sphere metric on each link (the metric of
(LSI-J)): Ric = 2 g, and Haar on S^3 has a log-Sobolev inequality with constant at least 2 (Bakry-Emery, RECALLED).
"Macro" = kept links S, "micro" = integrated links I, as in Piazza-Shen.

**3.1 First failing step: (PS-b), identity (3.1) (PROVED, hand).** The convolution identity integrates a link that
lies in exactly two plaquettes. In Z^d a link lies in k = 2(d - 1) plaquettes. With a_1, ..., a_k the staples at the link,
  integral of prod_(i <= k) e^(beta t(a_i u)) du = 1 + (beta^2/8) [ k + 2 sum_(i < j) t(a_i a_j^(-1)) ] + O(beta^3).
(First-order terms vanish; integral of t(a u) t(b u) du = t(a b^(-1))/4 by character orthogonality.) The integral is
invariant under a_i -> a_i g, so it is a function of the k - 1 relative variables a_i a_1^(-1), and already at order
beta^2 it contains every one of the k(k - 1)/2 six-link loops a_i a_j^(-1). For d = 2 this is one loop, the 2 x 1
rectangle, and the function is w^(*2). For d = 4 it is 15 loops (3 planar, 12 bent) after ONE integration. So (3.1)
fails at the first integrated link, whatever the order. After a whole block is integrated, the weight is the
block partition function Z_B(s) as a function of the boundary field: all loops of the boundary. This is the
"larger Wilson loops" sentence of Piazza-Shen, made exact at the first step.

**3.2 What is lost with (3.1) (identity RECALLED; the reading is mine).** For SU(2), w^(*n) = sum_j (2j + 1) c_j^n chi_j
with c_j = I_(2j+1)(beta)/I_1(beta) < 1. So the block weight of Piazza-Shen is the two-dimensional area law, true at
every beta, and their Lemma 2.1 is a group-blind proof of a cruder rate. Their proof is exact Migdal decimation in
two dimensions followed by Bakry-Emery at the trivial fixed point. In d >= 3 no exact decimation exists (3.1), and
the corresponding flatness statement cannot be group-blind: (PS-a) and (PS-b) hold word for word for U(1), and 4D
compact U(1) at large beta has no area law (Guth; Frohlich-Spencer; RECALLED). So in 4D the block step itself needs
an SU(2)-specific input. In Piazza-Shen the group enters only later, in (PS-d), as an absorber.

**3.3 Second failing step: (PS-c) and (PS-d). Lemma SEP (PROVED, hand).** Let mu-bar = e^(H-bar) ds be the marginal on
a set S of links. Let e in S lie in k plaquettes all of whose links are in S, and in k' = 2(d - 1) - k others. Then
there are s and a unit tangent vector v at s_e with
  (Ric - Hess H-bar)(v, v) <= 2 - beta (k - k').
So the Bakry-Emery step (PS-d) fails for mu-bar as soon as beta (k - k') >= 2.
Proof. H-bar(s) = log integral of e^(H(s, x)) dx. Along a geodesic s(tau) that moves s_e only,
(d/d tau)^2 H-bar = E_s[(d/d tau)^2 H] + Var_s((d/d tau) H) >= E_s[(d/d tau)^2 H]. Each t_p with p containing e is <s_e, a_p> with
a unit staple a_p, and (d/d tau)^2 <s_e(tau), a_p> = -t_p on the unit sphere. So (d/d tau)^2 H = -beta sum_(p at e) t_p. Take
s = 1 on S except s_e = -1. The k plaquettes inside S equal -1, the others are at most 1. QED
Consequences. In PS (d = 2) the kept edges are lines and k = 0. For d >= 3, conditional independence of bounded
blocks needs kept links that separate; for cubic blocks S contains the (d - 1)-dimensional faces, which carry
their own plaquettes at full weight beta:
- d = 4, e inside a 3D face: k = 4, k' = 2. (PS-d) fails for beta >= 1. This is the configuration and the number of
  row 941's ceiling (i).
- d = 4, e in the intersection of two faces: k = 6. Fails for beta >= 1/3. d = 3, e on a block edge: k = 4, k' = 0,
  fails for beta >= 1/2.
I proved this for cubic blocks only, not for every separating S.

**3.4 Lemma FOREST (PROVED; Elitzur's argument).** If S contains no closed loop, the marginal of S is exactly
product Haar, at every beta, in every dimension, on every box. (Proof. Gauge maps act transitively on G^S when S is
a forest, the Wilson measure is gauge invariant, and the image of Haar on the gauge group is product Haar.) So
for a forest the macro step holds exactly, with the curvature constant of SU(2), and with no Hessian to absorb.
Then the micro law is the law of all other links given S. By gauge covariance all these conditional laws are
isometric images of the one at S = 1. For a spanning tree this is the completely gauge-fixed measure, whose
log-Sobolev inequality is the original problem. So a forest makes the scheme circular.

**Dichotomy (reading of 3.3 and 3.4).** A separating skeleton makes the micro step soft and the macro law the whole
problem. A forest skeleton makes the macro law exact and the micro law the whole problem. The skeleton of
Piazza-Shen is both at once: it separates, and its gauge-invariant content is one holonomy per block with no
plaquette of its own. No skeleton in d >= 3 is both.

**3.5 Proposition EQ (PROVED given Holley-Stroock and the Haar inequality, both RECALLED; the proof is PS Sections 5-6,
which do not use d = 2).** Cubic blocks of side m in dimension d, S = all links in the faces. Write the inequality as
Ent(F^2) <= 2 C E|grad F|^2, with best constants C(mu) for the full law and C-bar for the marginal mu-bar of S. Then
  C-bar <= C(mu) <= max( 2 C-bar, K + 8 C-bar K kappa^2 n' ),
with K = (1/2) e^(2 beta N_B) (N_B = number of plaquettes that meet one block), kappa = 2 (d - 1) beta (a bound for
|grad_e H|), n' = the largest number of kept links e whose adjacent blocks contain a given micro link.
Proof. Left: a function of s alone. Right: chain rule (6.1); micro term by Holley-Stroock and tensorisation over
blocks (the blocks are conditionally independent because every plaquette that contains a micro link lies in the
closure of one cube); gradient of s -> nu_s(F^2)^(1/2) by Lemma 6.1 of PS with R(e) = the union of the blocks whose
closure contains e (their covariance step uses only the block Poincare inequality and sup |grad_e H_R|). QED
Reading. With bounded blocks the full inequality and the skeleton inequality are EQUIVALENT up to a factor that
depends on (m, beta, d) only. Nothing is gained and nothing is lost: the decomposition moves the problem to the
skeleton law. In 2D the skeleton law is explicit and nearly flat. In 4D it is the 3D skeleton field with the
bare weight on its own plaquettes and the factors Z_B, and by Lemma SEP no pointwise curvature bound holds for
it above beta = 1.

**3.6 Is the two-slice law J closer to the 2D setting? No, in three exact senses; yes in one soft sense.**
- (a) J has no local specification (H is not local), so no block of J is conditionally independent of another.
  A block argument has to be run on the 4D slab measure, of which J is a marginal. Lemma MARG (PROVED, hand, given
  the transfer-matrix limit, RECALLED): if the Wilson measure on B x (Z/TZ) satisfies
  Ent(F^2) <= (2/alpha_4) E|grad F|^2 for all smooth F and all large T, then (LSI-J) holds with alpha_J >= alpha_4/7.
  Proof. For gauge-invariant Phi put F(x, u, w) = Phi(x, u.w), (u.w)_l = u_s w_l u_(s')^(-1), with u the temporal links
  between the two slices. |grad_x F| and |grad_w F| equal those of Phi at (x, u.w). A rotation of u_s moves u.w along the
  gauge direction at s, whose three generators are orthogonal with squared norm 6. So
  |grad_(u_s) F|^2 <= 6 sum_(l at s) |grad_(w_l) Phi|^2, and the sum over s is at most 12 |grad_w Phi|^2. By invariance the same
  holds with x. So |grad F|^2 <= 7 (|grad_x Phi|^2 + |grad_w Phi|^2). The law of (x, u.w) tends to J on invariant functions as
  T grows. QED
  So (LSI-J) is weaker than a 4D theorem of Piazza-Shen type, by a factor 7. It is not nearer to their proof.
- (b) Disintegration over one slice given the other is the older route of this lane: macro law nu, micro law
  pi_x. (PS-d) for nu is dead above beta = 1 (row 941 ceiling (i)). (PS-e) for pi_x uniformly in x is (SG-step) in sup
  form (rows 944, 950; GUIDE-refuted at beta 2.6 at flat twisted slices, row 952).
- (c) Disintegration over the temporal links (Proposition SIGMA, PROVED identity; the order statement is RECALLED).
  Before gauge fixing the layer law is m(dx) m(dw) prod_s du_s exp(beta sum_(l = (s, s')) <x_l, u_s w_l u_(s')^(-1)>). Given
  (x, w), the temporal links are an S^3-valued nearest-neighbour spin model on the (d - 1)-dimensional box, with
  the O(4) couplings q -> x_l q w_l^(-1). For d - 1 = 1 it is a chain, its integral is a convolution along the chain,
  and this is exactly (PS-b). For d - 1 = 3 and x = w flat it is the 3D O(4) model at inverse temperature beta,
  which has long-range order for beta > 4 G_3 = 1.0109 (Frohlich-Simon-Spencer; this lane's Proposition TB2, row 839,
  check 849). So the ceiling 4 G_3 is the failure of (PS-b) and (PS-e) for this disintegration. The time direction
  supplies one layer; the three space directions remain. J is not closer to 2D.
- (d) The soft sense. In the variables (x, q), q_l = x_l^(-1) w_l, J is m(dx) prod_l w(q_l) dq_l times (dm/dw)(x q), with w
  the single-plaquette weight of Piazza-Shen. Without the last factor the q_l are independent of each other and of x, and their part of
  the inequality is immediate (one link, Holley-Stroock). In 1+1 dimensions V = 0 and Omega = 1, so the last factor is constant: there
  J is a product law. In 3+1 dimensions the factor e^(-V(xq)) H(xq) couples all q_l, and it is the vacuum factor.

**Answer to STEP 1.** The first step that fails is (3.1) of Piazza-Shen (3.1 above), at the first integrated
link, because a link lies in 2(d - 1) > 2 plaquettes. Independently, (PS-c)/(PS-d) fail because a separating
skeleton carries plaquettes (Lemma SEP: beta >= 1 in 4D). What survives in every dimension is the soft part,
(PS-e) and (PS-f) (Proposition EQ), and it only moves the problem. J is not closer to the 2D setting than the 4D
measure: it is a marginal of it (Lemma MARG), and each of its natural disintegrations is either the older route
(b) or a 3D spin system where Piazza-Shen have a chain (c).

## 4. STEP 2: fact tests, before any proof

A 4D adaptation has three slots. (BLOCK): after the links inside blocks of side m are integrated, the skeleton
law is "flat enough" (replaces (PS-a), (PS-b)). (MACRO): an inequality for the skeleton law (replaces (PS-d)).
(GLUE): (PS-e), (PS-f), which hold in every dimension (Proposition EQ). Each test is a statement with its computation.

**FT-U1.**
- (i) In 2D, (PS-a), (PS-b), (PS-c), (PS-e), (PS-f) hold word for word for U(1): the Doeblin bound, the convolution on
  the circle, the product structure, Holley-Stroock (Haar on the circle has a log-Sobolev inequality). Only (PS-d)
  fails: Ric = 0, and -Hess H-bar >= 1/2 is impossible on a compact manifold (H-bar has a minimum). So Piazza-Shen
  exclude U(1) at the absorber, not at the block step.
- (ii) In 4D the target must fail for the photon. FP: alpha_J = c_min, about 2 pi beta/b, fails (T1) by the factor above
  59 (T2). Compact U(1) at beta 1.5: R_J grows with the box, exponent 0.71 +- 0.04 (GUIDE, row 954 Section 5d).
- (iii) Consequence (PROVED given the Coulomb phase of 4D U(1), RECALLED; exact for FP). (GLUE) is group-blind and
  box-uniform. So for U(1) at large beta, (BLOCK) or (MACRO) is false for every block side m. An adaptation that
  keeps (MACRO) = "curvature absorbs a small Hessian" passes this test formally, as in 2D. But flatness of the
  skeleton law is false for the photon (its skeleton loops have power-law correlations). So a correct proof of
  (BLOCK) in 4D cannot be group-blind: it must use the non-abelian group in the block step, where Piazza-Shen use
  nothing but a Doeblin bound.

**FT-FROZEN (Q_8, 2T).** These groups have no tangent space: (PS-d), the gradient form and (LSI-J) are undefined
(row 947 4.4). The mechanism test is on (BLOCK): the Doeblin bound w >= e^(-2 beta)/z and the convolution identity
hold for every compact group, finite ones included. In 2D this is right (no freezing in two dimensions). In 4D
the frozen phases have E_1 -> 0 on a fixed box (row 931, Proposition HC (b); check 896 D6, ARGUED rate), and the
window 2.3-2.6 lies in the frozen phase of Q_8 and at or above the freezing point of 2T (RECALLED lattice values,
GUIDE). So a 4D (BLOCK) step must use connectedness, not only the Doeblin bound.

**FT-SMALLBOX (conditional on the premise of row 941: E_1 -> 0 as beta grows on a fixed lattice box).** Then
alpha_J -> 0 on a fixed box (row 954 Lemma GAP-R: R_J >= 1/(2 beta E_1) once E_1 <= 1). So every constant of an
adaptation must degrade with beta. Piazza-Shen do: r -> 1, the block area grows like e^(2t), and C_(N,beta) >= c beta^(1/3)
for SU(4) (their Section 7). Proposition EQ does: K = (1/2) e^(2 beta N_B). The box size enters through (T1): a
box-uniform constant c(beta) gives (LSI-J-seed)_a only for a >= a_0(c). At beta 2.3 the seed inequality is false for
small a (GUIDE): the local sector has R_J about 0.17 on boxes 8 to 12 (row 954 5c), so alpha_J <= 5.9 there, while
  2 beta K_a > 5.9 for a <= 20 (K_20 = 1.39, K_22 = 1.26). This reads the cap of boxes 8 to 12 on to larger boxes.

**FT-CEIL (which slots are sup forms, and their caps).**
- (MACRO) by pointwise curvature on a separating skeleton: capped at beta < 1 in 4D (Lemma SEP; the same number as
  row 941 ceiling (i)).
- A micro inequality uniform in the conditioning, for an UNBOUNDED micro set (the temporal links of a layer, or a
  slice given a slice): capped by 4 G_3 = 1.0109 (Proposition SIGMA with row 839's TB2); GUIDE-refuted at 2.6 (row 952).
- Single-link or vertex-block worst-case response criteria on the skeleton (Otto-Reznikoff, Dobrushin type): the
  families capped at 1/3, 2/3 and 0.775 (rows 834-836, checks 840, 841, 857; not re-derived here).
- Not capped: Holley-Stroock on bounded blocks (true at every beta, constant e^(-2 beta N_B)); Lemma FOREST (exact).
So the open slot (MACRO) has to be a statement about ONE law (the skeleton law or J), not a supremum over
conditionings. Every tool Piazza-Shen use for it is a supremum.

**FT-CURV (what the curvature input of Piazza-Shen becomes; PROVED identity).** For one free plaquette,
Laplacian of e^(beta t) on S^3 is e^(beta t) (beta^2 (1 - t^2) - 3 beta t), and its Haar integral is 0. So
3 beta E_w[t] = beta^2 E_w[1 - t^2]: the mean-curvature term and the force variance cancel exactly. At beta 2.3 each
is 3 x 2.3 x 0.48 = 3.3 (E_w t = I_2/I_1 = 0.48 for one free plaquette), 1.7 times the Ricci curvature. Piazza-Shen's macro Hessian is small only
through this cancellation, which needs the conditional law of each plaquette given the skeleton to be the free
law w up to r^(n-2). In 4D on a separating skeleton the k = 4 skeleton plaquettes at a link are not averaged: the
diagonal entry of the Hessian ranges over an interval of length 2 k beta = 18 to 21 in the window, against Ric = 2.
The pointwise criterion needs this ratio below 1. Whether the curvature bound holds at TYPICAL configurations is
a separate question, with no known answer in the lane; it is the GUIDE test of Section 7.

## 7a. The GUIDE test: design and criteria (written about 12:30Z, BEFORE any run; first launch 12:32:07Z)

(Placed here in work order. Sections 5 and 6 follow below; Section 7b holds the results.)

**Question.** FT-CURV left one thing open: Piazza-Shen's absorber (Ric against the Hessian of the log-density) fails
pointwise above beta = 1 (Lemma SEP). Does it hold at TYPICAL configurations of 4D SU(2) Wilson in the window? If
it fails there too, no averaged form of the curvature step exists at the lattice scale (block side 1), and any
curvature step needs a renormalised block action. If it holds, the exact shape of the defect set is the next object.

**Quantity.** Periodic L^4, density e^H, H = beta sum_p t_p, unit-sphere metric, tangent frame u xi (xi imaginary
quaternion). For a configuration U let Hs(U) be the matrix of Hess H (second derivative along product geodesics
U_l exp(tau xi_l); for one plaquette: diagonal blocks -t_p Id_3, off-diagonal blocks from two insertions of xi).
- lam_full(U) := largest eigenvalue of Hs on the whole tangent space. Margin 2 - lam_full.
- lam_hor(U) := largest eigenvalue of Hs on the horizontal space (orthogonal complement of the gauge directions
  xi_l = U_l^(-1) eta_s U_l - eta_(s')). Margin 2 - lam_hor. Only this one matters for gauge-invariant functions: the
  Bakry-Emery argument run on invariant functions needs the tensor on horizontal vectors only (Section 5,
  Proposition HBE).
- n_hor(U) := number of horizontal eigenvalues above 2 (counted among the top 24); the participation ratio (in
  links) of the top horizontal eigenvector; the largest diagonal entry -beta min_l sum_(p at l) t_p.

**Runs.** Heat bath (Creutz sampler, checkerboard by direction and parity), hot start, 300 sweeps, then
configurations 10 sweeps apart. L = 4: beta = 0.5, 1.0, 1.5, 2.0, 2.3, 2.6, 40 configurations each. L = 6: beta = 2.3
and 2.6, 16 configurations each. One thread, nice, under the numeric lock, memory cap 2 GB.

**Sanity checks, run first (a failure stops the batch).** S1: the matrix Hs against second differences of H along
random tangent directions (relative error below 1e-4). S2: at the flat configuration the largest eigenvalue of Hs
is 0 within 1e-8 beta (H is at its maximum). S3: the first derivative of H along random gauge directions is 0
within 1e-7. S4 (not a stop rule): mean plaquette near 0.60 at beta 2.3 and 0.67 at 2.6 (row 947 Run 3: 0.603-0.606, 0.671).

**Verdict rules (per L and beta).**
- TYP-CURV HOLDS (GUIDE): 2 - lam_hor > 0 in at least 95 percent of the configurations.
- TYP-CURV FAILS (GUIDE): 2 - lam_hor < 0 in at least 50 percent of the configurations.
- Otherwise MIXED. In every case report the mean number of horizontal eigenvalues above 2 per site.
- Volume rule: if n_hor per configuration grows from L = 4 to L = 6 by about the volume ratio 5.06, the violating
  modes are local defects with a density; then HOLDS on a small lattice means only that the density is below
  1/(number of sites), and the typical configuration of the seed box violates the bound somewhere.

**What each outcome can and cannot show.** A run proves nothing. FAILS at 2.3 and 2.6 would say: curvature is not
an absorber at the lattice scale even on average; the Piazza-Shen macro step has no averaged form without block
renormalisation. HOLDS would say: the Wilson law in the window is curvature-convex on gauge-invariant directions
except on a sparse defect set, and the smallest unproved inequality in this direction is an absorption of sparse
curvature defects (stated in Section 7b if this happens). My expectation before the run: the diagonal entries are
strongly negative (about -beta x 3.6), the positive part comes from the commutator terms and from negative
plaquettes; I expect HOLDS at L = 4 for beta = 2.3 with a few violating local modes at L = 6. I do not know.

## 5. STEP 3, stage A: the adaptation written as a proof, as far as it is true

**5.1 Lemma BLK (block laws; PROVED given Holley-Stroock and the Haar inequality, both RECALLED).** Write
Ent(F^2) <= 2 C E|grad F|^2. Haar on a product of copies of S^3 has C = 1/2 (Bakry-Emery, Ric = 2).
- (a) Slab law on B x (Z/TZ). For a finite set D of links and any values outside D, the conditional law of the links
  in D has C_D <= (1/2) exp(2 beta N_D), N_D = the number of plaquettes with a link in D.
- (b) The same for J: for D a set of links of the two slices, the conditional law under J of the links in D given
  all other links of the two slices has C_D <= (1/2) exp(2 beta N_D), with N_D counted in four dimensions.
  Proof of (b). The density of J is H(x) e^(-V(x)) e^(beta <x, w>) e^(-V(w)) H(w). A change of the links in D changes the
  explicit factors by at most 2 beta per two-slice plaquette that meets D. H(x) is an integral of
  exp(beta sum_l <x_l, y_l>) against a positive measure in the earlier slice y (temporal gauge), so
  H(x)/H(x') <= exp(2 beta |D|) when x and x' differ on D only: one earlier temporal plaquette per link. QED
This is the sentence of the queue row, "block conditional laws have an LSI from positive curvature at the block
scale". It is true at every beta, uniformly in the box and in the conditioning. It is also true for U(1) (Haar on
the circle), so it carries no SU(2) content: it is the soft part.

**5.2 Proposition HBE (horizontal curvature criterion; PROVED given the Bakry-Emery argument, RECALLED).** Let H be
gauge invariant on M = (S^3)^n. If (Ric - Hess H)(v, v) >= rho |v|^2 at every point, for every v orthogonal to the gauge
orbit, then Ent(F^2) <= (2/rho) E|grad F|^2 for every gauge-invariant F, under the law e^H.
Proof. The gauge group acts by isometries that preserve H, so the diffusion semigroup P_t of e^H commutes with it.
For invariant f > 0, g_t = log P_t f is invariant and its gradient is horizontal. The Fisher information
I(t) = E[P_t f |grad g_t|^2] has I'(t) = -2 E[P_t f Gamma_2(g_t)], and
Gamma_2(g) = |Hess g|^2 + (Ric - Hess H)(grad g, grad g) >= rho |grad g|^2. So I(t) <= e^(-2 rho t) I(0). The entropy of f is the
integral of I(t) over t >= 0, so Ent(f) <= I(0)/(2 rho), which is the stated inequality for F = f^(1/2). QED
It does not rescue the pointwise criterion (PROVED). At U = 1 except one link e with U_e = -1: grad H = 0, so
Hess H(g, .) = 0 for every gauge direction g (differentiate <grad H, X_xi> = 0). For v on e, Hess H(v, v) = 6 beta |v|^2 in
4D, and the horizontal part v_h of v has |v_h|^2 = (1 - (V - 1)/(4V)) |v|^2 (the gauge directions there are lattice
gradients, -1 being central). So Hess H(v_h, v_h) = 6 beta |v|^2, about 8 beta |v_h|^2: the horizontal criterion fails for
beta >= 1/4.

**5.3 Theorem TS-J (two-scale reduction for J; PROVED implication from Proposition EQ and Lemma MARG).** Let B be a
box whose sides are multiples of m, and mu-bar_T the law of the links in the faces of the cubic blocks of side m in
B x (Z/TZ). Assume for all large T: Ent(g^2) <= 2 C-bar E|grad g|^2 under mu-bar_T, for smooth g of the skeleton links. Then
(LSI-J) holds on B with
  2/alpha_J <= 14 max( 2 C-bar, K + 8 C-bar K kappa^2 n' ),   K = (1/2) e^(2 beta N_B), kappa = 6 beta, N_B <= 6 (m + 1)^4, n' <= 4 (m + 1)^4.
The constants do not depend on B. With (T1): (LSI-J-seed)_a follows from
  (MAC)_(m,a): on B = (24a)^3, 14 max( 2 C-bar, K + 8 C-bar K kappa^2 n' ) <= 1/(beta K_a).
Since 1/(beta K_a) grows like a/log a, (MAC)_(m,a) allows C-bar to grow with the box almost linearly in its side.
The hypothesis is one inequality for one law per slab; it is not a supremum over conditionings. But by
Proposition EQ it is equivalent, up to the same constants, to the inequality for the full slab law. So Theorem
TS-J is a true two-scale statement with curvature used at the block scale (Lemma BLK), and it reduces nothing.

**5.4 Lemma HESS (the Hessian that the curvature step would have to absorb; PROVED identity).** For the skeleton
law and a tangent vector v at s,
  Hess H-bar(v, v) = beta sum_(p inside S) Hess t_p(v, v) + beta E_s[ sum_(p not inside S) Hess_s t_p(v, v) ] + Var_s(<grad_s H, v>).
For one plaquette with holonomy W and v = (U_i xi_i), with Z_i the xi_i moved to the end of the word (PS (4.1)-(4.2),
psi = t, Hess t = -t g on S^3, inverse links with a minus sign):
  Hess t_p(v, v) = -t_p |Z_1 + Z_2 + Z_3 + Z_4|^2 + <grad t(W), W sum_(i < j) [Z_i, Z_j]>,
and the second term is at most 2 (1 - t_p^2)^(1/2) sum_(i < j) |Z_i| |Z_j| in size. Three parts:
- the curl part -t_p |sum Z_i|^2: non-positive where t_p >= 0, zero on gauge-like directions. Near smooth fields it
  makes -H convex, in favour of the criterion;
- the commutator part, of either sign and of size beta (1 - t_p^2)^(1/2) per plaquette. It is the lattice form of the
  spin term 2 tr(F [a, a]) of the continuum fluctuation operator. It vanishes for U(1);
- for the macro law, the variance term, which is non-negative and so against the criterion.
In 2D after block integration the mean-curvature and variance terms cancel in the mean (FT-CURV), and nothing is
left to absorb. In 4D the skeleton plaquettes are not averaged, and at a rough configuration the commutator
part has no sign. The GUIDE test of Section 7a measures the largest eigenvalue of the first line of this
identity for block side 1 (no integration), at typical configurations.

## 6. STEP 3, stage B: the coarse law at the box size. Attempts on (MACRO) and where each stops

- **B1, pointwise curvature (the step of Piazza-Shen).** Dead for beta >= 1 on the skeleton (Lemma SEP), and for
  beta >= 1/4 in the horizontal form at one flipped link (5.2). Nothing at the box size can change a pointwise
  statement.
- **B2, curvature at typical configurations.** This is the only averaged form of (PS-d) that I can state. Two
  stops. (i) Whether it is true at block side 1 in the window is the GUIDE test (7a, results in 7b). (ii) Even
  if true on small lattices, on the seed box a typical configuration violates the bound somewhere (local
  defects have a density; Lemma SEP's flipped link is one). No theorem turns "curvature bound outside a sparse
  defect set" into a log-Sobolev inequality: in the proof of 5.2 the density P_t f is arbitrary and can sit on
  the defects, where Gamma_2 >= rho Gamma fails. The statement needed is (DEF-ABS) of Section 7b. OPEN.
- **B3, criteria with mixed derivatives (Zegarlinski, Otto-Reznikoff, Dobrushin-Shlosman) for the skeleton law.**
  They need sup bounds, over the skeleton field, of covariances of forces inside a block: sup forms, of the
  families capped at 0.775 and at 4 G_3 (FT-CEIL). Not attempted further.
- **B4, the split of one inequality on one box (Rothaus' lemma, RECALLED; not a sup form).** If J has a Poincare
  inequality with constant 1/gam_J and a defective inequality Ent(Phi^2) <= A E|grad Phi|^2 + B E Phi^2, then
  2/alpha_J <= A + (B + 2)/gam_J. At the seed the defect may be as large as B + 2 = gam_J (1/(beta K_a) - A), of order
  a/log a. The block-scale curvature (Lemma BLK) is an input of the defective kind only. The Poincare part is the
  gap of J on the seed box. No block-scale input gives it: Lemma BLK holds for the photon too (FT-U1). And I
  found no way to a defective inequality with defect below the volume: telescoping the entropy over blocks
  needs gradients of conditional expectations given ever larger sets, which is the cross term of (PS-f) with
  micro sets that are no longer bounded. Stop: circular.
- **B5, where the box size enters.** Only through (T1). A 4D box-uniform theorem with a constant of order one is
  false on small boxes: R_J = 0.57 on 4^3 at beta 2.3 and 1.54 on 4^3 at beta 2.6 (GUIDE, row 954), from light flux
  states. So a block scheme needs blocks above the confinement length (side about 6 at beta 2.3 and above 12 at
  beta 2.6, read from the flux energies of row 954). Lemma BLK then gives constants like exp(-2 beta x 6 x 13^4).
  They are box-uniform, and (T1) accepts them with an astronomically large a. This costs nothing in logic and
  shows that the scheme has no use for the box size beyond (T1).

**The exact obstruction (answer to STEP 3).**
- (O1) No exact decimation: one integrated link gives all 15 six-link loops (3.1). The block weight is the block
  partition function as a function of the whole boundary field.
- (O2) A separating skeleton carries its own plaquettes at weight beta. The curvature of SU(2), Ric = 2, is the
  only absorber in the method, and it is used pointwise. It dies at beta = 1 (Lemma SEP), at 1/4 horizontally.
- (O3) What Piazza-Shen get from the two-dimensional area law, flatness of the macro law, must in 4D fail for
  U(1) and for the frozen groups. So it is an SU(2)-specific statement at least as strong as disorder at the
  block scale in the window. No hand method gives it; the 2D proof gives it from a Doeblin bound alone.
- (O4) The open slot (MACRO) must be one inequality for one law. With bounded blocks it is equivalent to the
  target (Proposition EQ). Every known way to prove it is a supremum over conditionings (capped) or needs the
  gap first (B4).
So the Wilson-loop growth (O1) is the first obstruction, and it is not the deepest one. Even with an explicit
block weight, the absorber (O2) would fail in the window, and what has to be absorbed is not small (O3).

**7a, amendment (A1), written about 12:33Z after the first launch and before any production number.** The first launch
(12:32:07Z) ran the sanity checks only and stopped at its own rule: S1 passed (worst relative error 2.8e-6), S2 passed
(top eigenvalue 2.0e-14 at the flat configuration), S3 gave 1.66e-7 against the stated 1e-7. No production run was
made. Cause: S3 used a central difference along the product geodesic U_l exp(tau xi_l), which leaves the gauge orbit
at second order, so the difference has a truncation error of order tau^2 that I had not allowed for. Amended S3:
the central difference along gauge directions at tau = 2e-3, 1e-3, 5e-4 must fall by a factor 4 at each halving
(between 3.6 and 4.4), which shows that the derivative at tau = 0 vanishes and the residue is truncation. All other
rules are unchanged. Relaunched as batch 1b at 12:34:19Z.

## 7. The smallest unproved inequality (written about 12:35Z, while batch 1b runs; 7b holds the test results)

**7.1 What the Piazza-Shen input gives for the crux.** It gives no inequality smaller than (LSI-J-seed)_a. The
reason is Proposition EQ: in every dimension the two-scale decomposition with bounded blocks is an equivalence
between the inequality for the law and the inequality for its skeleton marginal. In 2D the skeleton marginal is
explicit. In 4D it is not, and its inequality is the target again. In decreasing strength (each implies the next;
the implications are PROVED here or in row 947):
  (4D-LSI): a log-Sobolev inequality for the Wilson law on (24a)^3 x (Z/TZ), all large T, with alpha_4 >= 14 beta K_a
     (a theorem of Piazza-Shen type in 4D; box-uniform alpha_4 is more than enough, by (T1));
  equivalently up to constants in (m, beta): (MAC)_(m,a) of Theorem TS-J, for one block side m;
  (LSI-J-seed)_a (Lemma MARG);  then (HC-vac)_(K_a) and the seed (row 947, Corollary BR-J; row 931, Proposition HC).
First instance, at the Poincare level: the same chain with variances gives gam_J >= gam_4/7, and gam_4 is the
spectral gap of the 4D Langevin dynamics on the slab. So the smallest unproved inequality stays
  (LSI-J-seed)_a, or its Poincare instance gam_J >= 2 beta K_a on B = (24a)^3 (row 947's (PI-br-seed) chain).
No smaller statement came out of this row.

**7.2 The one new candidate that is not a supremum (OPEN; stated for the record, with its own fact tests).**
  (DEF-ABS): for the Wilson law e^H on the slab over the seed box there is rho > 0 and a non-negative field D(U)
  of symmetric forms with (Ric - Hess H)(v, v) >= rho |v|^2 - D(U)(v, v) on horizontal v, such that for every positive
  gauge-invariant density f with g = log f:
     E[ f D(grad g, grad g) ] <= (rho/2) E[ f |grad g|^2 ] + E[ f |Hess g|^2 ].
Then the proof of Proposition HBE gives the inequality for invariant functions with constant rho/2 (PROVED
implication: insert the two displays in Gamma_2). (DEF-ABS) is an averaged statement in the sense that D may be
large on a sparse set; it is still a statement for every density f. Fact tests. U(1): Ric = 0 and the horizontal
Hessian of H has the photon's soft directions, so rho > 0 fails at once (as it must). Frozen groups: undefined.
SMALL-BOX: rho and D depend on beta through H. Ceilings: at Lemma SEP's flipped link D must be at least 8 beta - 2 + rho
there, so D is not small in sup norm; the inequality can only hold through the Hessian term, that is through
a Poincare-type bound for the one-form grad g near a defect. I did not prove it and I have no route to it. The
GUIDE test says whether its first premise (a positive rho off a sparse set) is even plausible at block side 1.

## 7b. The GUIDE test: results (batch 1b, 12:34:19Z-12:39:51Z; lock holder gap-ps-957; 73 percent memory free; one thread, nice)

Script `/tmp/gap-ps-957/scripts/curv_guide.py` (full text at the end of this file), logs
`/tmp/gap-ps-957/logs/curv_L{4,6}_b*.log`, not committed. Sanity (amended S3): S1 worst relative error 2.8e-6; S2 top
eigenvalue 2.0e-14 at the flat configuration; S3 step-halving ratios 4.000 to 4.000: PASS. S4: mean plaquette on 6^4
is 0.6023 at beta 2.3 and 0.6706 at 2.6 (expected 0.603, 0.671); on 4^4 it is 0.6107 and 0.6713 (a small-torus effect
at 2.3). Peak memory 476 MB.

lam_full, lam_hor = largest eigenvalue of Hess H on the whole tangent space and on the horizontal space. The
curvature criterion needs lam_hor < Ric = 2.

| L | beta | plaquette | lam_full mean (min, max) | lam_hor mean +- sd (min, max) | share of configurations with lam_hor > 2 | 24th horizontal eigenvalue (mean) | links in the top horizontal mode (participation) |
|---|---|---|---|---|---|---|---|
| 4 | 0.5 | 0.1239 | 3.86 (3.70, 4.14) | 3.79 +- 0.10 (3.60, 4.08) | 40 of 40 | 3.41 | 24 |
| 4 | 1.0 | 0.2475 | 6.96 (6.61, 7.31) | 6.79 +- 0.16 (6.46, 7.17) | 40 of 40 | 5.99 | 24 |
| 4 | 1.5 | 0.3666 | 9.43 (8.92, 10.64) | 9.16 +- 0.42 (8.58, 10.49) | 40 of 40 | 7.71 | 20 |
| 4 | 2.0 | 0.5061 | 10.89 (10.00, 12.39) | 10.26 +- 0.58 (9.32, 12.07) | 40 of 40 | 7.87 | 23 |
| 4 | 2.3 | 0.6107 | 10.79 (9.63, 12.06) | 8.98 +- 0.80 (7.29, 10.68) | 40 of 40 | 5.83 | 22 |
| 4 | 2.6 | 0.6713 | 10.87 (9.46, 13.28) | 7.94 +- 1.08 (6.31, 10.54) | 40 of 40 | 4.51 | 39 |
| 6 | 2.3 | 0.6023 | 11.94 (11.10, 13.37) | 10.79 +- 0.89 (9.86, 12.74) | 16 of 16 | 8.30 | 10 |
| 6 | 2.6 | 0.6706 | 11.79 (10.40, 13.47) | 8.96 +- 0.84 (7.31, 10.38) | 16 of 16 | 6.35 | 17 |

The count n_hor (eigenvalues above 2 among the top 24) saturated at 24 in every configuration, so it measures
nothing. Addition (A2), made after seeing this and before its own numbers: batch 1c diagonalises the full
matrices on 4^4 and counts all eigenvalues above 2. The verdict rules are unchanged and do not depend on it.

**Verdict by the rules written before the run. TYP-CURV FAILS (GUIDE) at every coupling tested, 0.5 to 2.6, on both
lattice sizes, in every configuration.** The smallest margin seen is 2 - 3.60 = -1.6 (beta 0.5). In the window the
largest horizontal eigenvalue of Hess H is 9 to 11 at beta 2.3 and 8 to 9 at 2.6, against Ric = 2: the criterion
fails by a factor 4 to 5 at typical configurations, not only at Lemma SEP's rare ones.
Readings (GUIDE).
- (a) My expectation was wrong. I expected the negative diagonal (the pinning of each link by its staples) to
  dominate. It does not: the off-diagonal part of the Hessian at a rough field is of size about 4 beta.
- (b) lam_hor/beta falls with beta (7.6, 6.8, 6.1, 5.1, 3.9, 3.1 on 4^4). At small beta the configuration is nearly
  Haar-random and lam_hor is about 7.6 beta, so the typical criterion can hold only below beta about 2/7.6 = 0.26.
  This is the pointwise horizontal threshold 1/4 of Proposition HBE's counterexample again: for this action
  "typical" and "worst case" give the same range. The run at beta 0.25 in batch 1c tests this.
- (c) The top modes sit on 10 to 40 links and the 24th eigenvalue is still far above 2, also on 6^4, where
  lam_hor is larger than on 4^4 (10.8 against 9.0 at beta 2.3). So the violating modes are local and many.
- (d) Consequence for the method. The Hessian that Piazza-Shen's absorber meets is small only AFTER block
  integration (FT-CURV). At block side 1 nothing is integrated, and the curvature of SU(2) is too small by a
  factor 4 to 5 on average. So no averaged form of the curvature step exists without a block integration that
  makes the macro action nearly flat, which is (O3). And (DEF-ABS) of 7.2 has no support at block side 1: its
  defect field D would have to be at least lam_hor - 2, about 7 to 9, on a positive share of the modes, not on a
  sparse set.
Limits. Block side 1 only: the macro Hessian of a block-integrated law was not measured (it needs conditional
expectations inside blocks, a Monte Carlo inside a Monte Carlo). Lattices 4^4 and 6^4 only. A largest eigenvalue
above 2 refutes a sufficient criterion, never the inequality: (LSI-J-seed) is untouched by this run.

**7b, addition (A2): dense counts on 4^4 (batch 1c, 12:39:51Z-12:41:13Z; lock holder gap-ps-957c; 73 percent memory
free; peak memory 547 MB; 3 configurations per coupling, 20 sweeps apart; script `curv_dense.py` below; logs
`/tmp/gap-ps-957/logs/dense_L4_b*.log`).** All eigenvalues of Hess H on the horizontal space (dimension 2304 = 9 per
site; the 768 gauge directions are projected out and appear as exact zeros, counted 768 in every case).

| beta | largest horizontal eigenvalue (3 configurations, mean) | horizontal eigenvalues above 2 (mean) | share of the 2304 | per site | horizontal eigenvalues above 0 (mean) |
|---|---|---|---|---|---|
| 0.25 | 1.955 (1.946, 1.956, 1.963) | 0 | 0 | 0 | 1058 |
| 0.5 | 3.77 | 333 | 14.4 percent | 1.30 | 966 |
| 1.0 | 6.68 | 468 | 20.3 percent | 1.83 | 779 |
| 1.5 | 9.18 | 409 | 17.8 percent | 1.60 | 607 |
| 2.0 | 9.80 | 255 | 11.1 percent | 0.99 | 387 |
| 2.3 | 8.47 | 120 | 5.2 percent | 0.47 | 210 |
| 2.6 | 8.47 | 83 | 3.6 percent | 0.33 | 154 |

Readings (GUIDE). (e) At beta 0.25 the criterion holds in the three configurations, with margin 0.04 to 0.05:
the typical threshold on 4^4 is beta about 0.25, as reading (b) predicted from lam_hor about 7.8 beta, and it is the
pointwise horizontal threshold 1/4 of 5.2. (f) In the window the violating modes are not sparse: one mode above
Ric = 2 for every two sites at beta 2.3 and for every three sites at 2.6. (g) Most directions are on the good
side: at beta 2.3 about 91 percent of the horizontal modes have a negative eigenvalue (H concave along them), and
this share grows with beta. So the picture at block side 1 is: a field that is curvature-convex in nine
directions out of ten, with a dense set of local unstable directions of strength 2 to 10. I did not identify
these modes with a field-theory object; by Lemma HESS they come from the commutator part and from negative
plaquettes.

## 8. Verdicts (written 12:45Z)

Reading order: Sections 1 to 4, then 5, 6, 7 (7.1, 7.2), then 7a, 7b. Sections 7a and 7b sit where they were
written.

| Statement | Label |
|---|---|
| 3.1: one integrated link gives 1 + (beta^2/8)[k + 2 sum t(a_i a_j^(-1))] + O(beta^3); identity (3.1) of Piazza-Shen fails at the first integrated link for d >= 3 (15 six-link loops in 4D) | PROVED (hand) |
| Lemma SEP: the curvature step for a skeleton marginal fails when beta (k - k') >= 2; cubic skeleton in 4D: beta >= 1 inside a face, beta >= 1/3 where two faces meet | PROVED (hand); cubic blocks only |
| Lemma FOREST: the marginal of a loop-free set of links is product Haar; the scheme is then circular | PROVED (Elitzur's argument); circularity is a reading |
| Proposition EQ: with bounded blocks, C-bar <= C(mu) <= max(2 C-bar, K + 8 C-bar K kappa^2 n') in every dimension | PROVED given Holley-Stroock and the Haar inequality (RECALLED) and the proof of PS Sections 5-6 (ported; read in full, not rebuilt line by line) |
| Lemma MARG: a slab inequality with alpha_4 gives (LSI-J) with alpha_J >= alpha_4/7 | PROVED (hand) given the transfer-matrix limit (RECALLED) |
| Proposition SIGMA: the temporal links given the two slices are an S^3 spin model on the 3D box; at flat slices the 3D O(4) model at beta; this is the ceiling 4 G_3; in 1+1 dimensions it is the chain of Piazza-Shen | identity PROVED; the order above 4 G_3 RECALLED (Frohlich-Simon-Spencer; row 839) |
| Lemma BLK: block conditional laws of the slab law and of J have C_D <= (1/2) e^(2 beta N_D), uniformly | PROVED given Holley-Stroock and the Haar inequality (RECALLED) |
| Proposition HBE: a horizontal curvature bound gives the inequality for invariant functions; the bound fails pointwise for beta >= 1/4 | PROVED given the Bakry-Emery argument (RECALLED); the counterexample PROVED (hand) |
| Theorem TS-J: (MAC)_(m,a) gives (LSI-J-seed)_a | PROVED implication; by Proposition EQ it is equivalent to the target up to constants and reduces nothing |
| Lemma HESS: curl part, commutator part, variance part of the macro Hessian | PROVED identity (PS (4.1)-(4.2) with psi = t) |
| FT-CURV: 3 beta E_w t = beta^2 E_w(1 - t^2) for a free plaquette | PROVED (hand) |
| FT-U1 (iii), FT-FROZEN, FT-SMALLBOX, FT-CEIL | CONDITIONAL on the recalled facts named in Section 4 |
| (DEF-ABS) gives the inequality for invariant functions with constant rho/2 | PROVED implication; (DEF-ABS) OPEN, and without support at block side 1 (7b) |
| Curvature at typical configurations: lam_hor(Hess H) is 9 to 11 at beta 2.3 and 8 to 9 at beta 2.6 (4^4, 6^4), above Ric = 2 in every configuration for beta >= 0.5; below 2 only near beta 0.25; one violating mode per 2 to 3 sites in the window | GUIDE |
| A theorem of Piazza-Shen type in 4D ((4D-LSI), or (MAC)); (LSI-J-seed); (HC-vac); the seed | OPEN. Not proved. No smaller inequality was found |

**Answers to the three steps of the row.**
- STEP 1. The first failing step is identity (3.1) of Piazza-Shen, at the first integrated link (a link lies in
  2(d - 1) plaquettes). The second, independent failure is that a separating skeleton carries plaquettes (Lemma
  SEP). J is not closer to the 2D setting: it is a marginal of the 4D law (Lemma MARG); over one slice it is the
  older route; over the temporal links it is a 3D spin system where Piazza-Shen have a chain (Proposition SIGMA).
- STEP 2. The soft parts ((PS-e), (PS-f), Lemma BLK) pass no test: they hold for U(1) too. The block step must fail
  for U(1) and for the frozen groups, so it must use the non-abelian connected group, where Piazza-Shen use a
  Doeblin bound. The curvature absorber is capped at beta = 1 (1/4 horizontally) pointwise, and it fails at
  typical configurations by a factor 4 to 5 in the window (GUIDE). The open slot must be one inequality for one
  law; every tool of the method is a supremum.
- STEP 3. The adaptation is written as far as it is true: Theorem TS-J, with curvature at the block scale in
  Lemma BLK. It does not close. Exact obstruction: (O1)-(O4) of Section 6. Smallest unproved inequality:
  (LSI-J-seed)_a itself, equivalently (MAC)_(m,a); first instance gam_J >= 2 beta K_a (Section 7.1). One GUIDE test:
  Sections 7a, 7b.

**What this row did not do.** It did not prove or refute (LSI-J-seed). It did not measure the Hessian of a
block-integrated law. It did not rebuild Holley-Stroock, the Bakry-Emery criterion, Rothaus' lemma, the
transfer-matrix limit or the Frohlich-Simon-Spencer bound; each is marked RECALLED where used. Nothing here was
checked by another model.

**Credit.** Piazza and Shen (arXiv:2610.35286) for the theorem and every step labelled (PS-a) to (PS-g), and for
Lemmas 4.1 and 6.1, which Lemma HESS and Proposition EQ port. Otto-Reznikoff, Grunewald-Otto-Villani-Westdickenberg
and Bauerschmidt-Bodineau for the two-scale criterion, as cited by them. Ethan Sussman and Levent Alpoge (with
Claude and Codex as authors of their text) for the transfer and slice setting on which the two-slice law rests.
Rows 931, 941, 947 (the target and its chain), 839 (TB2), 954 (R_J values, Lemma GAP-R) of this lane.

**Files.** This note. Scratch, not committed: `/tmp/gap-ps-957/` (the PDF and its text, scripts, logs).

### Scripts (GUIDE only)

`curv_guide.py` (run as `python3 -I curv_guide.py --sanity`, then `--L 4 --beta 2.3 --ncfg 40 --seed 11`, or
`--L 6 --beta 2.3 --ncfg 16 --seed 12`; about 0.25 s per configuration on 4^4 and 6 to 8 s on 6^4):

```python
#!/usr/bin/env python3
# GUIDE test for library/gap-ps-disint-max.md Section 7a (row 957): largest eigenvalues of Hess H, H = beta sum_p t_p,
# on the full and on the horizontal tangent space, at heat-bath configurations of periodic 4D SU(2) Wilson.
# Refutes or guides only. Criteria are in the note (written before the run).
import sys, time, argparse, resource
import numpy as np
import scipy.sparse as sp
import scipy.sparse.linalg as spl
import scipy.linalg as sl

E = np.eye(4)

def qmul(a, b):
    a0, a1, a2, a3 = a[..., 0], a[..., 1], a[..., 2], a[..., 3]
    b0, b1, b2, b3 = b[..., 0], b[..., 1], b[..., 2], b[..., 3]
    return np.stack([a0*b0 - a1*b1 - a2*b2 - a3*b3,
                     a0*b1 + a1*b0 + a2*b3 - a3*b2,
                     a0*b2 - a1*b3 + a2*b0 + a3*b1,
                     a0*b3 + a1*b2 - a2*b1 + a3*b0], axis=-1)

CJ = np.array([1.0, -1.0, -1.0, -1.0])
def qconj(a):
    return a * CJ

def staples(U, mu):
    S = np.zeros_like(U[mu])
    for nu in range(4):
        if nu == mu:
            continue
        Unu_xpmu = np.roll(U[nu], -1, axis=mu)
        Umu_xpnu = np.roll(U[mu], -1, axis=nu)
        S += qmul(qmul(Unu_xpmu, qconj(Umu_xpnu)), qconj(U[nu]))
        Unu_xm = np.roll(U[nu], 1, axis=nu)
        Umu_xm = np.roll(U[mu], 1, axis=nu)
        Unu_xpmu_m = np.roll(Unu_xm, -1, axis=mu)
        S += qmul(qmul(qconj(Unu_xpmu_m), qconj(Umu_xm)), Unu_xm)
    return S

def sweep(U, beta, rng, pmask):
    for mu in range(4):
        for par in (0, 1):
            S = staples(U, mu)
            m = pmask[par]
            Sm = S[m]
            k = np.sqrt((Sm**2).sum(-1))
            a = beta * k
            n = a.shape[0]
            x0 = np.empty(n)
            todo = np.ones(n, dtype=bool)
            for it in range(2000):
                idx = np.nonzero(todo)[0]
                if idx.size == 0:
                    break
                ai = np.maximum(a[idx], 1e-9)
                r = rng.random(idx.size)
                xi = 1.0 + np.log(r + (1.0 - r) * np.exp(-2.0 * ai)) / ai
                xi = np.where(a[idx] < 1e-6, 2.0 * r - 1.0, xi)
                xi = np.clip(xi, -1.0, 1.0)
                acc = rng.random(idx.size) < np.sqrt(1.0 - xi * xi)
                x0[idx[acc]] = xi[acc]
                todo[idx[acc]] = False
            if todo.any():
                raise RuntimeError("sampler did not finish")
            v = rng.normal(size=(n, 3))
            v /= np.linalg.norm(v, axis=1)[:, None]
            s = np.sqrt(1.0 - x0 * x0)
            X = np.concatenate([x0[:, None], s[:, None] * v], axis=1)
            Vq = np.where(k[:, None] > 1e-12, Sm / np.maximum(k, 1e-300)[:, None], E[0])
            U[mu][m] = qmul(X, qconj(Vq))

def plaq_fields(U):
    out = []
    for mu in range(4):
        for nu in range(mu + 1, 4):
            U2 = np.roll(U[nu], -1, axis=mu)
            U3 = np.roll(U[mu], -1, axis=nu)
            W = qmul(qmul(qmul(U[mu], U2), qconj(U3)), qconj(U[nu]))
            out.append(W[..., 0])
    return out

def action(U, beta):
    return beta * sum(t.sum() for t in plaq_fields(U))

def hessian(U, beta):
    L = U.shape[1]
    V = L**4
    site = np.arange(V).reshape(L, L, L, L)
    rows, cols, vals = [], [], []
    diag = np.zeros(12 * V)
    one = np.zeros((V, 4)); one[:, 0] = 1.0
    sg = [1.0, 1.0, -1.0, -1.0]
    for mu in range(4):
        for nu in range(mu + 1, 4):
            U1 = U[mu].reshape(V, 4)
            U2 = np.roll(U[nu], -1, axis=mu).reshape(V, 4)
            U3 = np.roll(U[mu], -1, axis=nu).reshape(V, 4)
            U4 = U[nu].reshape(V, 4)
            links = [mu * V + site.reshape(V),
                     nu * V + np.roll(site, -1, axis=mu).reshape(V),
                     mu * V + np.roll(site, -1, axis=nu).reshape(V),
                     nu * V + site.reshape(V)]
            U3c = qconj(U3); U4c = qconj(U4)
            P2 = qmul(U1, U2)
            Ps = [U1, P2, P2, qmul(P2, U3c)]
            S3 = qmul(U3c, U4c)
            Ss = [qmul(U2, S3), S3, S3, U4c]
            t = qmul(Ps[3], U4c)[:, 0]
            Mid = {(0, 1): U2, (0, 2): U2, (0, 3): qmul(U2, U3c), (1, 2): one, (1, 3): U3c, (2, 3): U3c}
            for i in range(4):
                for a in range(3):
                    np.add.at(diag, 3 * links[i] + a, -beta * t)
            for (i, j), M in Mid.items():
                for a in range(3):
                    A = qmul(qmul(Ps[i], E[a + 1]), M)
                    for b in range(3):
                        val = beta * sg[i] * sg[j] * qmul(A, qmul(E[b + 1], Ss[j]))[:, 0]
                        rows.append(3 * links[i] + a); cols.append(3 * links[j] + b); vals.append(val)
                        rows.append(3 * links[j] + b); cols.append(3 * links[i] + a); vals.append(val)
    n = 12 * V
    H = sp.coo_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(n, n)).tocsr()
    return H + sp.diags(diag), diag

def gauge_matrix(U):
    L = U.shape[1]
    V = L**4
    site = np.arange(V).reshape(L, L, L, L)
    rows, cols, vals = [], [], []
    for mu in range(4):
        Ul = U[mu].reshape(V, 4)
        Ulc = qconj(Ul)
        l = mu * V + site.reshape(V)
        s0 = site.reshape(V)
        s1 = np.roll(site, -1, axis=mu).reshape(V)
        for a in range(3):
            R = qmul(qmul(Ulc, E[a + 1]), Ul)
            for b in range(3):
                rows.append(3 * l + b); cols.append(3 * s0 + a); vals.append(R[:, b + 1])
            rows.append(3 * l + a); cols.append(3 * s1 + a); vals.append(-np.ones(V))
    return sp.coo_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(12 * V, 3 * V)).tocsr()

def move(U, xi, tau):
    # U_l exp(tau xi_l); xi shape (4, L,L,L,L, 3)
    nrm = np.sqrt((xi**2).sum(-1))
    ang = tau * nrm
    unit = xi / np.maximum(nrm, 1e-300)[..., None]
    ex = np.concatenate([np.cos(ang)[..., None], np.sin(ang)[..., None] * unit], axis=-1)
    return qmul(U, ex)

def xi_from_vec(v, L):
    return v.reshape(4, L, L, L, L, 3)

def hot(L, rng):
    U = rng.normal(size=(4, L, L, L, L, 4))
    U /= np.sqrt((U**2).sum(-1))[..., None]
    return U

def sanity(rng):
    L = 2; beta = 2.3
    ok = True
    U = hot(L, rng)
    pm = parity(L)
    for _ in range(20):
        sweep(U, beta, rng, pm)
    Hs, _ = hessian(U, beta)
    n = Hs.shape[0]
    worst = 0.0
    for _ in range(6):
        v = rng.normal(size=n)
        xi = xi_from_vec(v, L)
        tau = 1e-3
        fd = (action(move(U, xi, tau), beta) - 2 * action(U, beta) + action(move(U, xi, -tau), beta)) / tau**2
        ex = v @ (Hs @ v)
        worst = max(worst, abs(fd - ex) / max(1.0, abs(ex)))
    print("S1 hessian vs second difference, worst relative error: %.2e" % worst)
    ok &= worst < 1e-4
    Uf = np.zeros((4, L, L, L, L, 4)); Uf[..., 0] = 1.0
    Hf, _ = hessian(Uf, beta)
    top = np.linalg.eigvalsh(Hf.toarray())[-1]
    print("S2 flat configuration, top eigenvalue of Hess H: %.2e" % top)
    ok &= abs(top) < 1e-8 * beta
    G = gauge_matrix(U)
    worst = 0.0; ratios = []
    for _ in range(6):
        c = rng.normal(size=G.shape[1])
        xi = xi_from_vec(G @ c, L)
        d = []
        for tau in (2e-3, 1e-3, 5e-4):
            d.append((action(move(U, xi, tau), beta) - action(move(U, xi, -tau), beta)) / (2 * tau) / np.linalg.norm(c))
        worst = max(worst, abs(d[2]))
        ratios.append((d[0] / d[1], d[1] / d[2]))
    rr = np.array(ratios)
    print("S3 (amended A1) first derivative of H along gauge directions at tau=5e-4, worst: %.2e; step-halving ratios min %.3f max %.3f (4 = pure truncation)" % (worst, rr.min(), rr.max()))
    ok &= (worst < 1e-4) and (rr.min() > 3.6) and (rr.max() < 4.4)
    # horizontal check: Hess restricted to gauge directions at the hot configuration equals -<grad H, accel>; not tested
    return ok

def parity(L):
    g = np.indices((L, L, L, L)).sum(0) % 2
    return [g == 0, g == 1]

def analyse(U, beta, K):
    L = U.shape[1]
    Hs, diag = hessian(U, beta)
    n = Hs.shape[0]
    wf = spl.eigsh(Hs, k=K, which='LA', return_eigenvectors=False, tol=1e-7, maxiter=20000)
    wf = np.sort(wf)[::-1]
    G = gauge_matrix(U)
    GtG = (G.T @ G).toarray()
    GtG[np.diag_indices_from(GtG)] += 1e-10
    cho = sl.cho_factor(GtG)
    def Ph(v):
        return v - G @ sl.cho_solve(cho, G.T @ v)
    c = 12.0 * beta
    def mv(v):
        v = np.asarray(v).ravel()
        w = Ph(v)
        return Ph(Hs @ w) + c * w
    op = spl.LinearOperator((n, n), matvec=mv, dtype=float)
    wh, vh = spl.eigsh(op, k=K, which='LA', tol=1e-7, maxiter=20000)
    order = np.argsort(wh)[::-1]
    wh = wh[order] - c
    v0 = Ph(vh[:, order[0]])
    wl = (v0.reshape(-1, 3)**2).sum(1)
    wl /= wl.sum()
    pr = 1.0 / (wl**2).sum()
    return wf, wh, pr, diag.max()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--L', type=int, default=4)
    ap.add_argument('--beta', type=float, default=2.3)
    ap.add_argument('--ncfg', type=int, default=40)
    ap.add_argument('--therm', type=int, default=300)
    ap.add_argument('--sep', type=int, default=10)
    ap.add_argument('--K', type=int, default=24)
    ap.add_argument('--seed', type=int, default=1)
    ap.add_argument('--sanity', action='store_true')
    a = ap.parse_args()
    rng = np.random.default_rng(a.seed)
    if a.sanity:
        ok = sanity(rng)
        print("SANITY", "PASS" if ok else "FAIL")
        sys.exit(0 if ok else 3)
    L, beta = a.L, a.beta
    V = L**4
    U = hot(L, rng)
    pm = parity(L)
    t0 = time.time()
    for _ in range(a.therm):
        sweep(U, beta, rng, pm)
    print("# L=%d beta=%.2f therm=%d (%.1f s) ncfg=%d sep=%d K=%d seed=%d" % (L, beta, a.therm, time.time() - t0, a.ncfg, a.sep, a.K, a.seed), flush=True)
    print("# cfg plaq lam_full[0..2] n_full(>2) lam_hor[0..2] n_hor(>2) n_hor(>1) n_hor(>0) PR_links maxdiag secs")
    rec = []
    for cfg in range(a.ncfg):
        for _ in range(a.sep):
            sweep(U, beta, rng, pm)
        t1 = time.time()
        pl = np.mean([t.mean() for t in plaq_fields(U)])
        wf, wh, pr, md = analyse(U, beta, a.K)
        rec.append((pl, wf[0], (wf > 2).sum(), wh[0], (wh > 2).sum(), (wh > 1).sum(), (wh > 0).sum(), pr, md, wh[-1]))
        print("%3d %.4f  %.3f %.3f %.3f  %2d   %.3f %.3f %.3f  %2d %2d %2d  %7.1f  %.3f  %.1f" % (
            cfg, pl, wf[0], wf[1], wf[2], (wf > 2).sum(), wh[0], wh[1], wh[2], (wh > 2).sum(), (wh > 1).sum(), (wh > 0).sum(), pr, md, time.time() - t1), flush=True)
        if resource.getrusage(resource.RUSAGE_SELF).ru_maxrss > 2 * 1024**3:
            print("RSS above 2 GB, stop"); sys.exit(4)
    r = np.array(rec, dtype=float)
    nc = r.shape[0]
    print("SUMMARY L=%d beta=%.2f ncfg=%d plaq=%.4f" % (L, beta, nc, r[:, 0].mean()))
    print("  lam_full: mean %.3f sd %.3f min %.3f max %.3f; mean n_full(>2) %.2f" % (r[:, 1].mean(), r[:, 1].std(), r[:, 1].min(), r[:, 1].max(), r[:, 2].mean()))
    print("  lam_hor : mean %.3f sd %.3f min %.3f max %.3f; frac(lam_hor>2) %.3f; mean n_hor(>2) %.2f (per site %.5f); mean n_hor(>1) %.2f; mean n_hor(>0) %.2f; K-th hor eig mean %.3f" % (
        r[:, 3].mean(), r[:, 3].std(), r[:, 3].min(), r[:, 3].max(), (r[:, 3] > 2).mean(), r[:, 4].mean(), r[:, 4].mean() / V, r[:, 5].mean(), r[:, 6].mean(), r[:, 9].mean()))
    print("  PR(top hor vector, links): mean %.1f of %d links; max diagonal entry mean %.3f max %.3f" % (r[:, 7].mean(), 4 * V, r[:, 8].mean(), r[:, 8].max()))
    print("  peak RSS MB %.0f" % (resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024**2))
    print("DONE")

if __name__ == '__main__':
    main()
```

`curv_dense.py` (run as `python3 -I curv_dense.py <path to curv_guide.py> <beta> 3 21`; about 3.5 s per configuration):

```python
#!/usr/bin/env python3
# GUIDE, row 957, addition (A2): full count of eigenvalues of Hess H above thresholds, by dense diagonalisation, L = 4.
# Loads the functions of curv_guide.py by exec (python3 -I has no script folder on sys.path).
import sys, time, resource
import numpy as np
import scipy.linalg as sl
path, beta, ncfg, seed = sys.argv[1], float(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
ns = {'__name__': 'curv_guide_lib'}
exec(compile(open(path).read(), path, 'exec'), ns)
L = 4; V = L**4
rng = np.random.default_rng(seed)
U = ns['hot'](L, rng); pm = ns['parity'](L)
for _ in range(300):
    ns['sweep'](U, beta, rng, pm)
print("# dense count L=4 beta=%.2f; horizontal dimension %d, full dimension %d" % (beta, 9 * V, 12 * V))
print("# cfg plaq | full: top, n(>2), n(>1), n(>0) | horizontal: top, n(>2), n(>1), n(>0), n(<0), zeros | secs")
acc = []
for cfg in range(ncfg):
    for _ in range(20):
        ns['sweep'](U, beta, rng, pm)
    t1 = time.time()
    pl = np.mean([t.mean() for t in ns['plaq_fields'](U)])
    Hs, _ = ns['hessian'](U, beta)
    A = Hs.toarray()
    wf = np.linalg.eigvalsh(A)
    G = ns['gauge_matrix'](U).toarray()
    GtG = G.T @ G
    P = np.eye(12 * V) - G @ sl.solve(GtG, G.T, assume_a='pos')
    Ah = P @ A @ P
    Ah = 0.5 * (Ah + Ah.T)
    wh = np.linalg.eigvalsh(Ah)
    z = int((np.abs(wh) <= 1e-6).sum())
    row = (pl, wf[-1], int((wf > 2).sum()), int((wf > 1).sum()), int((wf > 0).sum()),
           wh[-1], int((wh > 2).sum()), int((wh > 1).sum()), int((wh > 1e-6).sum()), int((wh < -1e-6).sum()), z)
    acc.append(row)
    print("%2d %.4f | %.3f %4d %4d %4d | %.3f %4d %4d %4d %4d %4d | %.1f" % ((cfg,) + row + (time.time() - t1,)), flush=True)
a = np.array(acc, dtype=float)
print("SUMMARY-DENSE L=4 beta=%.2f ncfg=%d: horizontal top %.3f; n_hor(>2) mean %.1f = %.4f of %d horizontal modes = %.4f per site; n_hor(>0) mean %.1f; full n(>2) mean %.1f; min horizontal eigenvalue not recorded; peak RSS MB %.0f" % (
    beta, ncfg, a[:, 5].mean(), a[:, 6].mean(), a[:, 6].mean() / (9 * V), 9 * V, a[:, 6].mean() / V, a[:, 8].mean(), a[:, 2].mean(),
    resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024**2))
print("DONE")
```

RESULT: Row 957 (Claude Fable 5.2 max, author, checked by no one): the Piazza-Shen adaptation does NOT close; (LSI-J-seed) stays OPEN and no smaller inequality was found. PROVED (hand, unchecked): identity (3.1) of Piazza-Shen fails at the first integrated link for d >= 3 (15 six-link loops in 4D); Lemma SEP (a separating skeleton carries plaquettes, so their curvature step is dead for beta >= 1 in 4D, and for beta >= 1/4 in the horizontal form); Lemma FOREST; Proposition EQ (with bounded blocks the two-scale step is an equivalence in every dimension, so it only moves the problem to the skeleton law); Lemma MARG ((LSI-J) follows from a 4D slab inequality with factor 7; J is a marginal, not closer to 2D); Proposition SIGMA (the temporal-link disintegration of J is a 3D O(4)-type spin model, which is the 4 G_3 ceiling, where Piazza-Shen have a chain); Lemma BLK and Theorem TS-J (the adaptation as far as it is true; it reduces nothing). GUIDE: the curvature absorber fails at typical configurations too (largest horizontal eigenvalue of Hess H 9 to 11 at beta 2.3 and 8 to 9 at 2.6 against Ric = 2, on 4^4 and 6^4; it holds only near beta 0.25). OPEN: a 4D theorem of Piazza-Shen type, i.e. the macro inequality as one statement for one law ((MAC), equivalent to the target); (DEF-ABS); (LSI-J-seed); the seed.
