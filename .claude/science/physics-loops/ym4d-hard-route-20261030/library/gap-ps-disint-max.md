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

- 2026-11-14T12:06Z: file created; steps 1-8 not started.
- 12:25Z: Sections 1 and 2 written (inputs read, duplicate check, Piazza-Shen skeleton). Next: Section 3 (STEP 1).
- 12:50Z: Section 3 written (STEP 1). Next: Section 4 (fact tests).
- 13:10Z: Section 4 written (STEP 2). Next: Section 5 (STEP 3 stage A) and the GUIDE criteria.

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
  (T1) by the factor (24/pi)(C_beta + 3 log a), above 59 for every a (row 947 4.3).

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
  the single-plaquette weight of Piazza-Shen. Without the last factor the q_l are independent and the inequality
  is immediate (one link, Holley-Stroock). In 1+1 dimensions V = 0 and Omega = 1, so the last factor is constant: there
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
small a (GUIDE): the local sector has R_J about 0.17 on boxes 8 to 12 (row 954 5c), so alpha_J <= 5.9, while
2 beta K_a > 5.9 for a <= 22.

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
is 3 x 2.3 x 0.60 = 4.2 (E_w t = I_2/I_1), twice the Ricci curvature. Piazza-Shen's macro Hessian is small only
through this cancellation, which needs the conditional law of each plaquette given the skeleton to be the free
law w up to r^(n-2). In 4D on a separating skeleton the k = 4 skeleton plaquettes at a link are not averaged: the
diagonal entry of the Hessian ranges over an interval of length 2 k beta = 18 to 21 in the window, against Ric = 2.
The pointwise criterion needs this ratio below 1. Whether the curvature bound holds at TYPICAL configurations is
a separate question, with no known answer in the lane; it is the GUIDE test of Section 7.
