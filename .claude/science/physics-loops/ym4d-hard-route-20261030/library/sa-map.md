lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-02T23:20Z

# sa-map: the Sussman-Alpoge outline mapped onto this folder

Queue row 69. Author: Anthropic claude-opus-5-5, effort max, Mac mini worker,
started 2026-11-02T11:20Z. Folder pinned at branch commit `3267555c7`.
Same-model reading: not independent in model, not a gate, not an audit, no
status. Nothing here is load-bearing until checked by hand in this folder.

**Source and credit.** Ethan Sussman and Levent Alpoge (with Claude and Codex
as authors of their text), `YM4_sketch_500.tex` in
https://github.com/ethanwsussman/Yang--Mills-LLM-experiment at commit
`31a47c543775f3f74013d06dd5d85962358f3b9e` (the head of `main` when read),
32,992 lines, sha256 `d7f77d4d...4d6f`. Line numbers below are lines of that
file. The programme it adapts is Balaban's (CMP 95, 96, 98, 99, 102, 109, 116,
119, 122); it cites those papers by number ("95", "102", ...). Its own text
says it is unvetted ("Proof outline" banners, a "dependency catalogue" of
obligations). Scripts: `checks/samap/` (a read-only locator; no numerics).

Status: finished 2026-11-02. Map complete for all 18 coded obligations and for
the catalogue obligations of the main line; 14 open items ranked; four lanes
proposed (Section 5). The statement queue row 66 (`r3-global-c`) was told to
look for is in the outline as (1b) Theorems 3-4, outlined and unproved
(obligations A1, A3).

## 0. How the outline is organised (what "open" means there)

- Main theorems: Theorem 0 (clauses (a) existence, (b) inheritance, (c) bounds
  and non-triviality, (d) uniqueness on a torus, (e) rotations) and Theorem 0'
  (volume-first limit, O(4), canonical phase decomposition, reconstruction),
  lines 6829-7042. Observable: the smeared plaquette action density O(f), only
  separated tuples, n >= 2. The trajectory is "first passage": K(beta, g) is
  the first level at which the running inverse coupling x_k enters
  [g^-2, g^-2 + B_sharp]; g is fixed small. So the continuum limit is taken at
  a fixed renormalized coupling g at physical scale 1, as in our T1.
- Dependency catalogue, lines 3757-4649 (Section "Supporting analytic results
  and proof dependencies"): eight packages A-H, each with four numbered items
  (A1-A4, ..., H1-H4). Items called "Obligation" are unproved; items called
  "Requirement" are claimed proved or derived there, sometimes only
  conditionally. H4 (line 4629) states the route: "the actual D1 and F2-F3
  proof outlines must be completed and a sequence of admissible data
  constructed".
- Index, lines 32869-32923: "Statements still to be proved, by package" lists
  the coded tasks of this item. Tags in the body: "[to be proved; Package X]"
  (16 places), "[outlined below; Section ...]" (Props 2.10, 2.13) and
  "[outlined here; Section ...]" (Lemma 7.6), "[proved here; ...]" (4.10, 4.12),
  "[cited from Balaban; ...]" (Prop 1.2 of CMP 95, Prop 8 of CMP 102).
- The coded tasks and the catalogue obligations are two layers of the same
  debt: e.g. Package C's 2.8-2.13 sit inside catalogue C1-C4, 4.11 inside D1,
  7.5/7.6/7a.1.8 inside F2-F3, Package A inside A1-A4. Both layers are mapped
  below; the catalogue obligations are the "main-line steps outlined rather
  than proved" of the task (Section 3).

## 1. The coded obligations ("Statements still to be proved, by package")

Format per item: **where** (line of `YM4_sketch_500.tex`); **statement** (quoted or
closely paraphrased, with the symbols of the outline); **outline there**;
**here** (what in `library/`, `parts/`, `gates/` proves, refutes or bears on it).
"Duplicate" marks text of ours that restates theirs.

### Package A (background gauges)

**1a.3.2 (axial gauges across levels).** Where: statement in "Lemmas 1a.3.1,
1a.3.2 (axial gauges)", l. 7651; tagged "[to be proved; Package A]" at l. 7705.
Statement: "suppose that U_0, U in U_k(Omega_bullet, alpha_0), that U is tower
axial, and that the averages at the tops differ by an amount < alpha_1. Then
|M^j U (M^j U_0)^-1 - 1| < C alpha_0 + alpha_1 at every level, uniformly in k."
(1a.3.1 is the tree Stokes bound |V^ax(b) - 1| <= 4 D epsilon on a box of side
D.) Outline: one line, l. 7875: "a descent through the levels, with increments
C alpha_0 sum_i L^(-2i)". Consumer: Theorem 1a.3.6 (axial to Landau gauge).
Here: nothing proves it. Bears: `library/rel-phi-c.md` Lemma 1 (composite
contour average = sum over levels of one-step staircase averages) and Example E
(a pure gauge of small L^4 norm with contour averages growing like
(log B)^(3/4)) show that *gauge-dependent* level sums do not close by a
critical count; 1a.3.2 is gauge-invariant data (averages of U against U_0) in
the tower axial gauge, so Example E does not refute it, but any proof must use
the axial normalization, not an L^4 count. Low failure risk.

**1a.3.5 (Landau gauge: positivity and the Green bound).** Where: "Lemma 1a.3.4,
Proposition 1a.3.5 [to be proved; Package A] (the Landau gauge)", l. 7683.
Statement (the obligation proper): for U in U_k(Omega_bullet, alpha_0), M_1
large, M alpha_0 below a number depending on L, at least C M_1 sites per
direction, the form <A, Delta^W_U A> + ||R D*_U A||^2 + <Q# A, a Q# A> is
positive definite; its inverse G_k(U) maps |.|_(-3) into ||.||_1 with norm
depending only on L; H_k B = G Q#*(Q# G Q#*)^-1 xi^-1 B minimises the Hessian
under the constraint, exactly for the invariant extension Delta_pi, a
perturbation of size C M alpha_0. Outline: l. 7895, "consider U = 1 (the
remaining cases are perturbations of it). A gradient is detected by Q# if
d Q' lambda != 0, and by R d* otherwise". Here: the coercivity part is the
block-average analogue of our D-coer line: `library/fan-ext.md` (flat one-jump,
gate `gates/fan-ext-73b09692a.md`: no WRONG, C_0 free of L and depth),
`library/fd-local.md` (flat several-jump, gate 00f9df685), `library/lc-u.md`
(curved local lift, gate 0bfc3ff42), `library/c0-loc.md` (curved D-coer on an
admitted domain, gate 51679e441, threshold repair D1). Ours are for the class
map of the mapped attempt (composite gradient-removed rows, transported curl),
not for Balaban's block average with a Landau term, so they bear on 1a.3.5 by
method, and do not discharge it. The perturbation "U = 1 plus C M alpha_0" is
exactly where our gates found that curved backgrounds need their own supplier
(`gates/lc-u-0bfc3ff42.md` D1: C_0 has no supplier at a curved local
background, repair by frames). Moderate risk at the *uniform-in-depth* claim;
Balaban (CMP 99, 102) proved the single-scheme version.

### Package E (Balaban's Theorem 8)

**Balaban's Theorem 8.** Where: inside "Proposition 1a.3.12 (a generalisation
of Theorem 1a.3.6, in the scheme c)", l. 7763: "Balaban's Theorem 8 [to be
proved; Package E] also asserts, without proof, all the bounds of the theorem,
with the same B_1. The second-order and Hoelder bounds require, in addition, a
bound on Df in |.|_(-3)." Statement (as the outline reads it): for f in ran R
with |f|_(-2) < gamma'(alpha_0 + alpha_1), the unique u with trivial averages
and R D*_(U_0) A = f gives A with |A|_(-1), |grad_(U_0) A|_(-2),
|D*DA|_(-3), |Delta_(U_0) A|_(-3) <= B_1(alpha_0 + alpha_1) and Hoelder bounds,
i.e. the bounds of Theorem 1a.3.6 off the slice f = 0. The outline proves only
existence and uniqueness of u by the contraction in ||lambda||_0 (1a.3.12) and
notes Balaban uses the off-slice bounds "a single time, to obtain the
second-order bounds on the minimiser". Here: nothing. Bears:
`library/lattice-uhlenbeck.md` Lemma U (a global gauge delta a = 0 on a box at
small energy with ||grad a||^2 <= 4 ||theta||^2, uniform in the box size,
single scale, flat reference) is the closest thing we have to a uniform gauge
estimate; it is L^2-critical, not the weighted sup bounds of Theorem 8.
Low-moderate risk; it is a statement Balaban asserted without proof.

### Package C (large-field histories)

Context: Theorem 2.1 (l. 17259) is the inductive description with UV stability
(density = sum over labelled histories of T'_k(S)[chi exp A_{k,S}], E-, R-, B-
terms with norms E_0, g_j^kappa_0, B e^{-kappa d}, mass M(i, X) <= e^{-(2 - c')
p_0(g_i)}, a floor chi_k e^{-x_k A - E_- |T|} <= rho-bar_k and
int rho-bar_k <= e^{C(1 + log x_k)|T|}). It credits Balaban (CMP 119, Thm 1,
Cor 3; CMP 122) for the core and lists, l. 17290-17303, what it adds and "must
prove". Numbers 2.8, 2.10, 2.13 are *not displayed as statements* in this file;
their content is fixed by their uses, quoted below. Their outlines are in (2d),
l. 17841-19407. A detailed statement-by-statement comparison with our rarity
work is queue row 70 (`sa-histories`); here only the pointers.

**2.8 (the cancellation of the R operation).** Where: l. 17640, "This is what
makes the three Wilson terms of Proposition 2.8 [outlined below] cancel; two of
them carry the constant x_k"; the field B "that occurs in Proposition 2.8",
l. 17598 (multi-scale field on the shells, single scaling g_k, test
|B| < delta'_k/g_k, axial tree gauge T_0). Outline, l. 17842-17900: at a real
point of the tests,
-x_k A(phi_X, U_{k,X}(e^{i g_k B} V_Lambda)) - A(x''_k(.), U'') + x_k A(phi_X, U_0)
= -A(x_k(.), U-bar) - A(x''_k phi_c, U'') - (1/2)||phi^{1/2} D H B||^2 + R_X,
"the linear term in B vanishes because U_0 is critical on the fibre"; R_X is
"ten resulting terms", each bounded by exponential locality across a collar of
weighted width c M R-check_k: |R_X| <= C(1 + c-bar)(log theta_k)^{2q + Cr}
e^{-c delta_0 M (log theta_k)^r}; "the weight difference on a shell is O(k - j)
rather than O(x_k (k - j))". Here: this is our (GLUE-E)/(NL-pay)/(PATCH)
problem (FINISH, "(UP) at nonlinear level: open"): `library/seam-quadratic-c.md`
(quadratic (LC) at the flat background, by hand), `library/seam-nonlinear-c.md`
(Theorem GN: (GLUE-E) at the flat background as an implication from (REL),
(CMP); "(PATCH) not needed: one global relative field has no transition term"),
`library/rel-phi-c.md` (stop (REL-D)), `library/lift-nonlinear.md` (stops at
ES:88, a heavy frozen wall gives the stage no output). Their R_X bound consumes
A3 (response decay across seams) at every one of the ten terms; our seam work
says the hard part is the relative field in one global gauge (Section 2, A1).
Nothing of ours proves or refutes 2.8.

**2.10 (the sum over healed components is a polymer sum).** Where: l. 17451
("The part of R^(k) produced by R arises only through the sum over
(X-frak, varsigma), a sum which R itself performs (Proposition 2.10 [outlined
below])") and l. 17459. Outline, l. 17958-17990 and "Restriction and the healed
histories", l. 18877: complete the action at the output label by erasing the
treated cluster; factor out the empty family; Mayer expansion with a healed
component in every polymer, whose mass gives e^{-(2-c) p_0(g_k)}; result
log K = sum_Y (V_empty(Y) + R'_#(Y)), |R'_#(Y)| <= C e^{-(1+c) p_0(g_k)}
e^{-(1 + beta_s/2) kappa d(S'; Y)}, consistent on restricted domains. Here:
`library/gas2.md` (row 46: no uncancelled first-order term for the actual
kernel; stops at (S2), one marked birth cell), `library/explicit-region-two-step.md`
(row 32: integrating before testing removes (HW) and (PATCH) on two examples;
(GAS2) first), `library/polymer-covariance.md`. Bears by method; proves nothing
of 2.10.

**2.12 (aged load, age rate q_a).** Where: l. 23358, "Role (B), the age rate
q_a of the aged load of Proposition 2.12 [to be proved; Package C], concerns
the pairs of lists belonging to a class of the kind given there (2e), and it is
used in (8a)"; index l. 32898, "The stronger aged comparison 2.12 remains
separate." No outline in this file. Consumer: (8a), the matched-cutoff
comparison E3, hence Theorem 0(a)(i) (tuned limits) and 0(d) (uniqueness on a
torus). **Off our T1 path** (T1 needs a subsequential limit along a chosen
trajectory). Here: nothing.

**2.13 (the label sum with the logarithm).** Where: l. 17820 ("the form used in
Proposition 2.13 [outlined below], the statement that carries the logarithm"),
l. 17831, l. 22925: "CM^4 R-check_t^5 log x_t <= (1/2) c p_0(g_t) (Proposition
2.13): half of the exponent pays the cost and the other half is kept. Inside a
drop-out the mass has consumed the factors of the creations, and whatever the
label still shows there is paid for by the weight." Outline: (2d) paragraphs
"The scalar reserve" (l. 18605, c_t <= r_t = C_3 c_1 M^4 R_t^5), "The entropy of
the literal histories" (l. 18672), "The common envelope and the mass induction"
(l. 18719), "Action shares and the loaded label sum" (l. 18944). Here: the
same kind of gain-against-entropy arithmetic failed twice in our rarity line:
`gates/rarity-fresh-c-263afacbd.md` (unpaid n log n entropy of a one-ball EX on
a growing cluster; (1+p)^N <= 2 false for N > 1/p), repaired in
`library/rarity-repair.md` (fixed-box common denominator with explicit
entropy). `library/history-budget-sum.md` (Lemma HS) and
`library/generated-observable-history.md` (Theorem GH), gate
`gates/history-budget-769697e8d.md` (closes as a conditional implication, does
not close the induction), are budget sums of the same type for a different
quantity. Nothing proves 2.13.

### Package D

**4.11 (holomorphy suffices for the conjugated copies).** Where: l. 22609, end
of Proposition 4.5: "The conjugated copies of (4d) and (4e) make no use of these
facts; holomorphy is all they require (Lemma 4.11 [to be proved; Package D])."
Statement (by use): the sourced construction, mirror-conjugated in the
chessboard and all-state transfer steps (4d), (4e), is holomorphic on the
complex source polydisc; reality and positivity (Prop 4.5) are not needed
there. Outline: (4c) "Finite ordinary sources and the positive-label floor",
l. 22948 ff. (constant sources first, slopes summable, sum_j d_{2r}[b_j] <= 1/3;
general sources by interpolating step data). Here: the consumer side of the
same holomorphy is our UV-CT, CT1-CT3 (`parts/upper-chain.md` Text 7: an
analytic local counterterm E(w) at reflection-periodic complex plaquette
sources). **Duplicate, credited**: GOAL.md says the counterterm-with-sources
form "comes through `parts/hard-core--mapped.md` from the Sussman-Alpoge
account", and `parts/hard-core--mapped.md` l. 1033 proposes UV-EXT' "taken from
the account's (3.6)". `gates/uv-ct-upper-chain-41489e4876.md`: implications
hold, UV-CT open. No hard-core attempt of ours is holomorphic in sources (mapped
Text 5.8: "There is no analyticity and no complex source").

### Package F (short distance)

**7.5 (four-point positivity on the tori).** Where: l. 25990 (statement) and
l. 23356 (form of the thresholds). Statement: for theta <= theta_square,
g <= gamma_W(theta), there are n_4 >= n_0, d_4, l_4(g) and, for l > l_4(g),
d_4(l), such that for K - s(d) >= n_4, d below the threshold, and every nearly
collinear quadruple in T^(4)_{T_l}(d; theta) (supports in B(c_i, d/16), centres
on a line), c (N^2 - 1) g(d)^8 prod ||f_i||_inf <= S^T_4 <= C (N^2 - 1) g(d)^8
prod ||f_i||_inf, uniformly in (K, beta); "For four points, Theorem 0 asserts
nothing about the limits, and nothing about R^4." Outline: (7d), developed in
Sections `ym4:new-clean-box` to `ym4:new-gaussian-segment` (l. 26223-26700).
Here: **not an interaction witness in the sense of our NT2.** The connected
four-point function of a quadratic composite of a Gaussian field is already
non-zero (the ring of four propagators), so 7.5 holds for a free field with the
running normalization; GOAL.md's NT2 asks for the three-gluon-vertex part, and
`gates/witness-3b7fd4e57.md` (D1, D2) is the reason. `parts/witness.md` Text 8,
`library/nt2-free-value-by-hand.md`. Off our critical path; low relevance.

**7.6 (transfer of the two-point law to every torus and state).** Where:
l. 26062: "Lemma 7.6 [outlined here; Section finite-reference-normalizer] of
(7e) transfers the law to every T_l and every nu at a cost of
C_2 d^2 ||f||_inf ||h||_inf"; l. 26212 (it relies on Lemma 4.10, chessboard
domination of periodic Gibbs states, |nu(F)| <= liminf ||F||_ch,l, "proved
here"). Outline: l. 26935 ff.: the reference torus T_* carries upper
stability; larger tori contribute only their unsourced floors (ST5) and the
common vacuum-density bound. Here: our upper chain consumes the same pair of
facts in its interface: UV-CT CT4 (a volume floor, log Z_L >= (L/P)^4 log Z_Tor
- c_F (L/a_*)^4) and the chessboard per-ball bound (GOAL.md; mapped l. 1032
"the per-ball bound uses chessboard on periodised sources with a re-centred
counterterm (draft 3.4, 3.6)": **duplicate of the account's structure,
credited**). `gates/uv-ct-upper-chain-41489e4876.md`: "CT4 cannot be verified
at Gaussian order."

**7a.1.8 (the cumulant as a law on resummed histories).** Where: l. 26184:
"There the cumulant is written in terms of a law on resummed histories and
block fields (Lemmas 7a.1.8 [to be proved; Package F], 7a.1.9). Resummed
histories are classes of histories that become equal once their entries inside
healed components are deleted." Statement not displayed in this file. Outline:
`ym4:new-clean-box` (l. 26223: segment k_0 <= j <= k_1 = k_0 + n, n ~ log x;
read sets S_j, boxes I_j with N_j <= C(r + D)^4, supports r ~ (log x)^{2 p_0}
spacings apart) to `ym4:new-gaussian-segment`. Consumer: F2 (the two-point
extraction). Here: `library/explicit-region-two-step.md` and `library/gas2.md`
(resummation over healed components, by method). Nothing proves it.

### Package G (rotations by a Ward identity: optional in the outline)

**9.3, 9.1, 9.7, 9.10, 9.11.** Where: l. 6999 (9.3: the rotational Ward
identity sum_i <O(f_1); ...; O(grad^s_omega f_i); ...> = U_{omega,chi}(f) +
<B_{omega,chi}; O(f_1); ...>, with a bulk term of dimension-six artefacts and a
shell flux), l. 7008 (9.1: U_{omega,chi_R} -> 0 along every defining sequence;
9.7 with 9.8, 9.9: an insertion not of the form of the action followed to first
order through K steps; 9.11: a moment bound with several insertions; 9.10: the
transfer in the volume). Content: "The optional Ward target on arbitrary
defining sequences", l. 32326-32400, (CP10)-(CP12). The one number: the decay
exponent c_1 > 1/2 of the traceless diagonal anisotropy, claimed c_1 = 1 from the
one-loop law in that channel (l. 7010-7016). In the outline this route is
optional: Theorem 0' gets O(4) for volume-first limits by the angular route G2
"without any Ward identity (10b)". Here: **off our path** (GOAL.md: O(4) is a
later target; T1 asks for hypercubic invariance). Nothing of ours bears, except
that c_1 is a one-loop computation of the type of Theorem P1 (Section 2, B3).

### Package A-H

**1.2 (cited: Balaban, CMP 95 (1984) 17, Proposition 1.2).** Where: l. 26141:
"both G and grad G decay exponentially, at a rate that depends on the dimension
alone (95, Proposition 1.2 [cited from Balaban; Package A--H], (1.110))"; index
l. 32905. For centred blocks the outline adds three devices (a spectral gap
>= c(-Delta + 1) uniform in the fine spacing, Combes-Thomas, a Young bootstrap
L^2 -> L^8 -> L^inf). Here: cited lemmas are gaps under GOAL.md until rebuilt.
Bears: our flat kernel results (`library/fan-ext.md`, `library/fd-local.md`,
`library/ue-multilevel.md`: flat raw input bounded at fixed L but not uniformly
in L, ratio at least about L^2; `library/qr-decide.md` Green-function row
bounds; `library/convex-laplace-tree-decay.md`). The outline itself proves
flat exponential kernels (Section "Exponential kernels of the classical flat
precision", l. 9060). Low risk; a rebuild, not research.

**1.6 (the small-field step as a holomorphic map).** Where: l. 22879: "Its
small-field core is Proposition 1.6 [to be proved; Package A--H] of (1d), which
is the one-step theorem stated as a holomorphic map on a class of families of
activities"; l. 22942 (holomorphic in the shift difference on
D(0, sigma_* theta_j)). Outline: Proposition 1a.2.8 (l. 7569, the small-field
step as a map on actions), (1d), (1e); catalogue B1, B2, B4. Here: our one-step
theorems are real-coupling: mapped `library/one-step-closure.md` (gate
`gates/closure-bad958abb.md`), `library/sector-values.md`, `library/analytic-lift.md`;
independent `parts/hard-core--independent.md` Texts 4-5 (gates: (GOOD) WRONG as
displayed; (TAIL), (R1), (R2), the wall count do not close). They bear by
method and do not give the holomorphic version. Moderate risk.

## 2. Main-line steps the outline calls outlined, not proved

The outline's main route (H4, l. 4629): "the actual D1 and F2-F3 proof outlines
must be completed and a sequence of admissible data constructed"; D1 rests on
Packages A, B, C and E1. The catalogue items below are the steps of that line
that carry the word "Obligation", or a "Requirement" whose text says its
hypotheses "must still" be verified. Items the outline says are proved
(F1, G1, G3, the bootstrap of the energy of averages, the free and flat
computations) are listed at the end of this section as reusable.

**A1, the constrained critical orbit (l. 3811), with the background theorems
of (1b), l. 9583-9930.** Obligation: for every allowed nested family of
small-field regions and every regular coarse datum, a regular critical orbit
with the prescribed averages, unique among regular critical orbits in a larger
neighbourhood, with a gauge representative Borel in real data and holomorphic
near regular data, all radii and constants uniform in the number of scales,
compatible with restriction, seams and change of torus. Outline: (1b) Theorem 1
(one regular critical orbit; |dU - 1| < C eps_1 eta^2 L(p)^-2,
|J(U)| < C eps_1 L(b)^-3), Theorem 2 (local regularity, and a gauge on any cube
of side m xi_j with xi_j|A|, xi_j^2|grad A|, xi_j^3|d*dA| <= C m eps),
**Theorem 3 (the Landau pair: Phi(B) = (e^{i eta H(B)} U_0)^{u_B},
R D^T H(B) = 0, u_B v_j[H(B)] = 1 at the tops, ||H(B)||_X,
|D^T D H(B)|_(-3) <= C sup|B|, no dependence on depth, regions or volume)**,
Theorem 4 (exponential decay of the response,
xi_y|h|, xi_y^2|grad h|, xi_y^3|D^T D h| <= C e^{-c delta_0 d_B(y, y_c)}|e|),
Theorems 5, 6; plan in nine mechanisms, l. 9793-9930 (straightening and
geometric series in the level; one system with a multiplier; three resets; a
lower bound uniform in levels from scale-invariant bumps; regularity of the
datum; a cost rho per layer crossing; decay from the same contraction;
polydisc by Weierstrass; coarser constraints frozen by finer ones).
Here: **this is the statement that queue row 66 (`r3-global-c`) was told to
look for, and it is there, outlined and unproved.** Our stop is (REL-D) of
`library/rel-phi-c.md` (an l^1 sum over L-adic shells of L^4 norms of the
relative field at each top centre). rel-phi-c records that (REL-D) "holds for
bounded H"; Theorem 3 with Theorem 4 gives, in the outline's gauge, a pointwise
local-scale bound xi_y|H(y)| <= C sum_c e^{-c delta_0 d(y, y_c)}|B(c)|
(my inference, integrating the response along the segment sB, s in [0, 1]; unchecked), and a pointwise bound at the scale of one top cube
makes the shell sum geometric. So, for the relative field between **two
critical backgrounds**, SA Theorems 3-4 would supply (REL-D). Three differences
remain and are exactly what a lane must settle: (i) our (REL) compares the
class minimiser with the iterated **trial** T, which is not critical; (ii) our
bounds are by local energies (K_delta * E)(Q), theirs by sup|B| of the datum
(the conversion is the energy of the averages, below); (iii) our class map is
not Balaban's average (A4). Also bearing: mapped Text 5.3 (R1)-(R3) (fixed
point from the one-shot trial and Theorem F; (R3) H^2 in local Landau gauges,
numerics PASS, abelian, not reviewed), `library/relative-density-bound.md`
item (o) (identification with the class minimiser, a sketch),
`library/block-poincare-energy-package.md` Thms 5-7 (Thm 7 assumes the
minimiser exists), `library/lattice-uhlenbeck.md`. rel-phi-c's Example E
(pure gauge, contour averages ~ (log B)^(3/4)) is excluded in the Landau pair
gauge by uniqueness of the pair, so it does not refute Theorem 3.

**A2, coercivity on a fluctuation fibre (l. 3833).** The outline proves the
flat classical case: c(L) I <= A_k^flat <= C L^8 I uniformly in depth, and
||da||^2 <= E_k(a) <= 256 ||da||^2; it does not prove "the non-Abelian,
nonzero-current, signed-profile, layered or enlarged-complex-domain versions".
Here: our D-coer line goes further in curvature for a different fibre (the
mapped class map): `library/fan-ext.md` (flat, C_0 free of L and depth),
`library/fd-local.md` (flat several-jump), `library/lc-u.md` (curved local
lift), `library/c0-loc.md` (curved D-coer, TP-sharp, Ward, (NC) on the admitted
domain, gate 51679e441). **Possibly ours supplies part of A2**, after an
intertwining of the two averaging schemes (A4), which nobody has written.

**A3, local inverse and response bounds (l. 3866).** Exponential kernels, first
and Hoelder differences, on the full complex datum polydisc; (PW1)-(PW3);
"The corresponding non-Abelian background and multiscale response estimates
remain to be proved. This includes the decoupled response assertion numbered
1c.10". Proved there: flat exponential kernels uniformly in depth and volume
(l. 9060). Here: `library/qr-decide.md` (signed inverse estimate, two-step row
estimate, (RC) routing), `library/fd-jumps.md` (stops at (UE), a uniform
simultaneous block-average extension, open at flat nested walls),
`library/ue-multilevel.md` (stops at (WP); flat raw input not uniform in L),
`library/fibre-propagator.md`, `library/preconditioned-covariance.md`,
`library/curl-poincare-exterior.md`. Our (UE) and (WP) stops are inputs of the
same multiscale-response type that A3 names.

**A4, averaging schemes (l. 3895).** Transfer between schemes with a uniform
intertwining map. Here: nothing; needed if any of our class-map results is to
serve the outline.

**B1, B2, B4 (l. 3910, 3937, 4003).** Polymer majorant, pointed extraction,
ordinary step derivatives: each derived in the outline from "primitive
hypotheses" that "we must still verify ... for the actual complex interacting
matrices and all allowed cores". Here: `library/ultralocal_cluster_expansion.md`,
`library/polymer-covariance.md`, `library/cn-tree.md` (forest identity,
cut-safe tree bound, volume factor gone), `library/one-step-closure.md`,
`library/sector-values.md`. Ours are real-coupling.

**B3, the one-loop law (l. 3979).** |b_j^0 - c_0| <= C L^{-sigma j} or a summable
substitute, c_0 = 11 N^2 log L/(12 pi^2), from an actual lattice trace with the
stated zero-mode convention; (CP2) l. 31940: |sum_{i<=r}(b_i^0 - c_0)| <= C_0;
outline Section `ym4:new-one-loop-reduction` (l. 21065). Here: **mapped
Theorem P1** (`parts/hard-core--mapped.md` Text 3, l. 365 ff.:
beta^0_{l+1} = c_0 + c_l - c_{l+1}, sup|c_l| < infinity), an implication given
Leaf Scalar and (E), both "discharged" in `library/twisted-order-calculus.md`
(own proof, not reviewed), for the hard-constraint kernel. Same statement as
(CP2), different scheme; a gate of P1 against (CP2) could close B3 for the
mapped scheme. The outline's c_1 = 1 for the anisotropy (Package G) is a
one-loop number of the same kind.

**C1-C4 (l. 4041-4083), with Theorem 2.1 (l. 17259), Lemma 2.5 (l. 17676),
Props 2.6, 2.7 (l. 17719, 17794), Theorem 2.11 (l. 19435).** C1 exact
measurable operations; C2 geometric margins and an entropy bound with the same
size function as rarity; **C3 rarity with entropy and insertions paid for**
(mass <= exp[-c p_0(g_j) - kappa|X|_j], with the supremum over external complex
data inside the integral, including failure of existence of a background, and
drop-outs "need a separate bound after attachment to their carrying term");
**C4 invariance of the inductive class with "one simultaneous order of choice"**
(the order is displayed at l. 19465-19470). Outline: (2a)-(2e), l. 17315-19530;
the outline flags two hazards itself: Balaban's sentence on p. 387 of CMP 122
on joining regions (l. 17310, which its global count avoids), and the toy case
at l. 17836 (a supremum over a product set selects a flat U and loses the
factor, so each inequality of Lemma 2.5 must hold at every configuration of the
fibred set). Here: our whole rarity line, rows 56-65 and their gates
(`library/rarity-fresh-c.md`, `rarity-fresh-x.md`, `rarity-repair.md`,
`sp-decide.md`, `qr-decide.md`, `sp-nonlinear.md`), the stage examples
(`library/heavy-wall.md`, `hw-fine.md`, `hw-thick.md`, `lift-nonlinear.md`),
`library/explicit-region-two-step.md` (Lemma TYP, Prop HOLES; gate
`gates/explicit-region-codex-00f9df685.md`: Prop HOLES holds as a probability
bound for its mask, "Balaban's regions are not shown to be that mask"),
`library/quiet-boundary-rarity.md` (Theorem Z). The comparison statement by
statement is row 70; this map only ranks it (Section 4).

**D1, the ordinary localized source bound and stability (l. 4088).** (ST5)-(ST6)
with holomorphic point counterterms, a strict entropy gap, the rooted domain
geometry (GS1)-(GS3), and "the normalized upper stability bound and unsourced
partition-function floor ... uniform in cutoff and allowed torus"; Section
"Ordinary stability from a normalized history representation" (l. 23385) gives
sufficient criteria (OH1)-(OH6): a total-variation label sum, and the floor
from the all-small-field label, e^{-E} Z(0) >= exp[-(C + 6 log x)N], whose input
(OH5) "must be verified" for a non-Abelian minimizing background. Here: UV-CT
(duplicate interface, credited), `gates/uv-ct-upper-chain-41489e4876.md`,
`parts/hard-core--independent--ct.md`; our upper chain's Theorems 3, 4 and
Prop 5 (why UV-EXT without counterterm fails) agree with D1's cutoff-dependent
point counterterms.

**D3, age-resolved uniform rarity (l. 4161).** Persistence of live regions from
a level to a later level with a summable tail r(m), uniform in volume and test
location; used by the age series of (4d) in Theorem 7.1 (l. 26156, "(c1)",
"(d) Wild histories ... these one-cell bounds must hold uniformly in the
volume"). Here: `library/explicit-region-two-step.md` ("Persistent regions fail
at d = 4", for its own mask); **bears with a negative sign, not shown to apply
to the outline's regions.**

**E1, E2 (l. 4197, 4206).** Consistent flow up to first passage; holomorphic
frozen tuning map with 0 < c <= d x_K/d beta <= C. Here: mapped Lemma FLOW
(implication given P1 and H(k) item 4), `gates/history-budget-769697e8d.md`
(trajectory half deliverable, conditional). E2: nothing (no analyticity).
**E3, E4** (matched cutoffs, calibrations): off our path.

**F2, F3 (l. 4275, 4357), with Theorem 7.1 (l. 25966) and 7a.1.8.** The
interacting extraction S_2 = C_G zeta^2 g^4 K(f, h)(1 + r), |r| <= 1/2, for the
full class T(d; theta_*), theta_* = 1/12000, uniform in all periodic Gibbs states
and positions; and g_K(d)^-2 = c_* log(1/d)(1 + o(1)), zeta = 1 + o(1). "The
actual clean-history normal form must still control every old activity's
localized Hessian, the conditional exterior force and pointwise deletion".
Here: our NT2 witness line (`parts/witness.md`, parked) needs more than F2 (the
three-gluon part), and nothing of ours supplies F2. **F4** (identification of
the full gauge theory) is open for both: T1 asks for local gauge-invariant
observables, and our UV-CT, like the outline, uses plaquette sources.

**Proved in the outline and reusable here (not obligations; still to be
checked by hand before use).** F1, the free lattice-curvature comparison with
gamma = 1/2 (Section l. 1670); G1, link reflection and all-mirror reflection
positivity for every periodic SU(2) Wilson DLR state (Sections l. 2084, 2698;
our upper chain Lemma 1.1 rebuilds only the site-plane case after Osterwalder
and Seiler); G3, a lattice plateau law (l. 3195); the flat exponential kernels
(l. 9060); and the **energy of the averages** (l. 18206-18290): for every real U,
sum over N_0(S) of a_p(U) >= min{c sum_{p' in S} |dM^t U(p') - 1|^2, e_*}, c, e_*
depending on L only, by a Schur bootstrap. I read the bootstrap at the level of
its steps: P has row sums L^2 and column sums L^-2 (I recounted the column sum:
L^2 origins times weight L^-4), so ||P||_(2->2) <= 1 exactly in d = 4 and
||P^[j] h||_2 <= L^-2j ||h||_1; with E_l <= 4 E_0 the error sum is
<= 4 C E_0/(1 - L^-2), and the induction closes for E_0 below a threshold,
with E_t^{1/2} <= E_0^{1/2} + C' E_0. Its one unproved input is the one-step
inequality f_(MW) <= P f_W + r(W), ||r(W)||_1 <= C ||f_W||_2^2 ("a comb gauge
and the discrete Stokes formula give"). **This is the nonlinear conversion
that `library/seam-nonlinear-c.md` 4.1 lists as missing** ("a top plaquette of
angle theta' forces fine energy about theta'^2 in its shadow ... nonlinear case
needs (CMP)"), for Balaban's average; at small energy its constant tends to
the linear one.

## 3. Where our own folder duplicates their text (marked plainly)

Textual duplicates (their wording or structure restated here; all credited
where they occur):

1. **DUPLICATE: the UV-CT interface** (GOAL.md; `parts/upper-chain.md` Text 7,
   CT1-CT3): the localized-source form with an analytic local counterterm at
   complex plaquette sources is the account's (3.6) form (GOAL.md credits it;
   `parts/hard-core--mapped.md` l. 1033, "taken from the account's (3.6)").
   In the current outline it is D1, (ST5)-(ST6), l. 4088.
2. **DUPLICATE: the chessboard per-ball bound on periodised sources with a
   re-centred counterterm** (mapped l. 1032, "draft 3.4, 3.6"); in the current
   outline Lemma 4.10 (chessboard domination of periodic states, "proved
   here") and G1, G4.
3. **DUPLICATE: mapped Text 1, "The map, in my own words"**
   (`parts/hard-core--mapped.md` l. 263-335), a summary of the older account
   (`theorem_0_complete_account_raw_{I,II,III}.tex` at `c854ad8b3a42`): the
   thresholds eps_k = g_k p_0(g_k), cubes of side M R-check_k, the R operation
   with waiting, first passage K = min{k : x_k <= g^-2 + B}, the flow bounds
   (P1)-(P3), the vacuum-energy split. `gates/history-budget-769697e8d.md` D4
   already notes that this text "carries no weight here". The current outline
   restates the same objects in Theorem 0 (l. 6845-6870), Theorem 2.1 and E1.
4. **DUPLICATE (definitions): first passage and the window** used by mapped
   Lemma FLOW and by the upper chain's window are the outline's first-passage
   datum (l. 6853).

Same statement, separate derivations (not a copy of their text, but double
work):

5. Mapped **Theorem P1** (one-loop telescoping, |sum_{l<=k} beta^0_l - k c_0|
   <= c_2, hard-constraint kernel, own proof via `library/twisted-order-calculus.md`)
   = the outline's (CP2) and obligation B3 (its route: a telescoping heat-kernel
   trace, l. 7014, Section `ym4:new-one-loop-reduction`).
6. **The nonlinear "flux forces energy" conversion** that
   `library/seam-nonlinear-c.md` 4.1 lists as missing = the outline's energy of
   the averages (l. 18206-18290), proved there by a Schur bootstrap from one
   stated one-step inequality (Section 2, end). Theirs is further along.
7. Our per-creation pricing in `library/rarity-fresh-c.md` (read each rare
   event one level below its own, conditional on the exterior) parallels
   Lemma 2.5, Props 2.6, 2.7 of the outline; row 70 compares them.
8. Upper chain Lemma 1.1 (site-plane reflection positivity after Osterwalder
   and Seiler, proof written) is a smaller rebuild of the outline's G1 (all
   coordinate and diagonal mirrors, every periodic Wilson DLR state).

Not duplicates (checked): `library/lattice-uhlenbeck.md` and
`library/lattice_sobolev_box_gauge.md` (L^2-critical gauges uniform in box
size; the outline's gauges are pointwise and box-size dependent, Prop 1a.3.8,
Theorem 2); our D-coer line (A2 analogue for the class map, curved; the outline
proves only the flat block-average case); `library/nt2-free-value-by-hand.md`
(a different free computation than the outline's free curvature model,
l. 1379, 1670); the whole NT2 witness line (the outline has no interaction
witness; Section 1, 7.5).

## 4. Every open item ranked by how likely it is to fail, hardest first

Judgment of one same-model reader; it steers, it grants nothing. "Path" says
whether T1 of GOAL.md needs the item (existence of a non-trivial, RP,
hypercubic limit along a chosen trajectory).

| Rank | Item (outline codes) | Path | Why it ranks here |
|---|---|---|---|
| 1 | Renewed-test witness and floor screening of the R operation: Lemma 2.5 part (4) (l. 17712), "A new mark pays outside the old floor" (l. 18334-18415), drop-out mass with the fibred supremum (l. 18130-18205); inside C3 | yes | Only source of the factor that pays for a repeated drop-out; without it waiting need not end and C3 fails. New relative to Balaban (he removes failed components, CMP 122a pp. 181-183). Rests on a background-locality estimate through a collar "of fixed positive width" with the floor's field unknown; our heavy-wall/hw-fine examples are exactly fields beside an old large field. |
| 2 | Healing and resummation: Props 2.8 and 2.10 (l. 17640, 17842-17990), with A3 across seams | yes | The R_X bound sums "ten resulting terms" by exponential locality across a collar of width c M R-check_k at every depth; this is the nonlinear seam problem where our rows 61-65 all stopped ((GLUE-E), (REL-Phi)/(REL-D), (AR)). |
| 3 | One simultaneous order of constants: C4, Theorem 2.11 (l. 19435-19470) | yes | Catalogue's own words: "listing its clauses does not discharge it". Every one of our chains hit an order clash (`gates/rarity-fresh-x-0e8a5a4e7.md` D2, m_* >= C_D b_2^2; `library/excess-seam.md`, rate nu fixed before L; `library/fd-local.md`, t_0 >= 10^4 R L^2). Cheap to decide. |
| 4 | Global genealogy count and the label sum with the logarithm: Prop 2.6 (l. 17719), "Contraction and the count over generations" (l. 18475), Prop 2.13 (l. 22925) | yes | Replaces Balaban's double induction (CMP 122b pp. 384-387, whose p. 387 sentence the outline itself distrusts); the same gain-against-entropy arithmetic failed twice in our rarity line (`gates/rarity-fresh-c-263afacbd.md`). |
| 5 | Complex external data in the mass (C3: "supremum over external complex data inside its internal integral"), and the sourced construction: D1 with (OH1)-(OH6), 4.11 | yes (sources: through UV-CT) | Positivity is lost at complex w (Prop 4.5); the outline's toy case (l. 17836) shows a supremum over the wrong set loses the factor. Complex coupling shifts keep Re of the Wilson weight, which limits the risk. |
| 6 | Age-resolved rarity D3, uniform in volume (used in Theorem 7.1 (c1), (d)) | for F2 | Our Prop HOLES (persistent raw regions fail at d = 4) does not transfer: the outline tests averaged fields and heals after waiting, as `gates/explicit-region-codex-00f9df685.md` warns. Moderate. |
| 7 | Interacting extraction F2, F3, 7a.1.8 (uniform in periodic Gibbs states) | not for T1 as GOAL.md defines NT2; yes for the outline's non-triviality | Plausible given C and D1; the state-uniformity is handled by chessboard domination (4.10, proved there). |
| 8 | Backgrounds, gauges and responses: A1, A2 (non-flat), A3, A4; 1a.3.2, 1a.3.5, Balaban's Theorem 8, cited Prop 1.2 | yes | Balaban proved the single-scheme versions (CMP 95, 96, 99, 102); the outline adds seams, nodes, complex data and uniformity in the number of layers. Our D-coer line stands on its domains. Moderate-low. |
| 9 | Small-field step on the actual complex matrices: B1, B2, B4, Prop 1.6 | yes | "Verify the hypotheses" obligations of Balaban-type (CMP 109, 116, 119); our two attempts' versions are real-coupling and gated with defects. Moderate-low. |
| 10 | One-loop law and flow: B3, E1, E2, F3 | yes (B3, E1) | Physics-certain value; the risk is the lattice trace with its zero-mode convention. Our Theorem P1 is a candidate supplier. Low. |
| 11 | Matched cutoffs and uniqueness: E3, E4, Prop 2.12 | no | Needed only for tuned limits and Theorem 0(d). |
| 12 | Four-point positivity 7.5; transfer 7.6 | no (7.6 only for the outline's R^4 law) | 7.5 is not an interaction witness (Section 1). |
| 13 | Ward route, Package G (9.1, 9.3, 9.7, 9.10, 9.11; c_1 > 1/2) | no | Optional in the outline itself; O(4) is a later target here. |
| 14 | F4 identification; H3 external OS theorem | no for T1 | Scope statements; F4 is open for both projects. |

## 5. The next four lanes (one per item, ranks 1 to 4)

Each lane is one fresh session on one statement, written in the outline's
symbols, kill attempt first, ending PROVED, REFUTED or STOPPED with a strictly
smaller inequality. Each builds on the outline's text and credits Sussman and
Alpoge (and Balaban).

**Lane 1, `sa-floor` (rank 1; mapped and neutral; max).** Statement, from
l. 18334-18415 and Lemma 2.5 part (4), l. 17712: *Let X be treated by R at level
m with preparation bottom m_flat, old floor F (the level-m_flat cells of
Omega^c_{m_flat} cap X not touching Omega_{m_flat}) and waiting collar of one
local cell. Let U be any real field on X^+ compatible with the stored variables
(each recorded test at its recorded value; M^j U = V_j(xi) on the determining
bonds in X), arbitrary inside F. If the unspent Wilson, gauge and stored
Gaussian energies in X^+ minus F are below c l_m^{2 p_1 - 8r}, then every test
of the operation at level m passes, including the main-step bond test
|log V'(b)| < delta'_m on every bond of the prepared box Lambda^pr and the
existence and extension tests; in particular every stage background satisfies
|d U-hat(p) - 1| <= C(varsigma + R_m^2 eps_m e^{-delta_0 M R_m}) L^{-2 j(p)}
outside F.* Kill first, with written pass and fail criteria: (a) a bond of
Lambda^pr whose tested average reads cells of F (does "they agree on the gauge
tree and outside the central box" cover every tested bond?); (b) a field in F
with O(1) plaquettes and a non-trivial holonomy class seen from the window (a
Z_2 vortex sheet whose Dirac 3-chain cannot be chosen inside F, possible only
if F has non-trivial second homology); (c) the configurations of
`library/heavy-wall.md` and `library/hw-fine.md` placed in F. Consumers: C3
(Prop 2.7 for drop-outs), the renewed wait, Theorem 2.11; in our folder, the
same question as (HW) beside a frozen wall. Why first: if it fails, a drop-out
can recur with no factor and the large-field induction does not close.

**Lane 2, `sa-seam-response` (rank 2, its A3 input; mapped; max).** Statement,
from (1b) Theorems 3 and 4 (l. 9693-9745) at the flat background: *On a
separated sequence (Omega_j) of arbitrary depth k, cube size frak-M and gap
rho = R_1 frak-M, with several seams, at V_0 = 1, the Landau-pair response
h = d/ds H(s e_c) at s = 0 to a unit datum at a top bond c satisfies
xi_y|h(y)| + xi_y^2|grad h(y)| + xi_y^3|D^T D h(y)| <= C(L) e^{-c delta_0 d_B(y, y_c)}
with C, delta_0 independent of k, the regions and the volume.* Then derive
(REL-D) of `library/rel-phi-c.md` for the relative field between two critical
backgrounds, and state exactly what is left for the iterated trial T of
`library/seam-nonlinear-c.md` (REL) and for the class map (A4). Kill first: the
depth-growing field asked for in row 66, built in the Landau-pair gauge
(R D^T H = 0, u_B v_j[H] = 1 at the tops), at the linear level, where the
outline's model Prop 1a.2.10 (nested orthogonal projections) is exact. Why
here: the outline proves flat kernels only for a single region (l. 9060); the
layered, seam-crossing version is its open A3, it feeds every term of R_X in
Prop 2.8, and it is the stop of our rows 61-66.

**Lane 3, `sa-order` (rank 3; neutral; high).** Statement: *the conditions on
constants stated anywhere in the outline admit one simultaneous choice in the
order displayed at l. 19465-19470,* (r, p_0, p_1, q, kappa_0, beta_s, theta_s,
theta_c) < L < (M_1, R_1) < kappa < (kappa-bar, kappa_1) < M_1' < M_2 <
(Theta_1, varpi_T) < M < sigma_* < a_Lambda < (A_1, A_0, C_0, C_1, alpha_1,
alpha_0, E_0, M_0, alpha', B) < (lambda, c_5, B-bar) < gamma < (varrho, c_a) <
(g, l, beta, K). List each condition with its line (for example
2 p_1 - C r > p_0 near l. 17682, q > p_0 + 2r near l. 17831 and 18197,
2 p_1 - 8r > p_0 near l. 18403, q - p_0 > 2 near l. 26178, kappa_0 > 4 at
l. 3997, the slope-rate condition p_R >= 3/2 near l. 4381, the layer cost
a rho >= C log L of (1b) mechanism 6, eps-bar <= c(L)/frak-M of Theorems 3-4,
c_a >= C(b) log L at finitely many b), check that each C is free of later
constants, and decide ACYCLIC (with the choice) or name the first circle. Add
the outline's analogue of `gates/rarity-fresh-x-0e8a5a4e7.md` D2 (a dense-box
Haar branch needs m_* >= C_D b_2^2) if the outline has such a branch. Why: a
circle kills the route at no cost to find, and every one of our chains has hit
one.

**Lane 4, `sa-count` (rank 4; mapped and neutral; max).** Statement: *Prop 2.6
of the outline (l. 17719-17793), the count, the ledger and the credit, with the
contraction O(u) subset C(u) subset O(u)^[e] and the count over generations of
l. 18475-18604, holds with constants independent of the history and the number
of steps, and with it the label sum of Prop 2.13: C M^4 R-check_t^5 log x_t <=
(1/2) c p_0(g_t) pays every site cost.* Kill first: a genealogy in which two
old regions join repeatedly with no new creation (the case of Balaban's p. 387
sentence, which the outline says its count "never compares"), and a region that
grows by hull and boxing moves alone between creations; and recheck the entropy
of the literal histories (graph degree D = L^4 + 3^4 + 2, l. 18672) against the
gain per created cell, as `gates/rarity-fresh-c-263afacbd.md` did for ours.
Why: it replaces Balaban's double induction, and our own version of this
arithmetic failed twice.

**Cheap, not hardest (for the lead's queue, not one of the four).** Gate mapped
Theorem P1 and `library/twisted-order-calculus.md` against the outline's (CP2)
and Section `ym4:new-one-loop-reduction` (l. 21065): a finished P1 discharges
obligation B3 for the mapped kernel and is the one-loop input of E1 and F3.
Row 70 (`sa-histories`) continues the statement-by-statement rarity comparison
and should read Lanes 1 and 4 as questions.

## 6. What was read, what was not, and limits

Read in the outline (by line): the main theorem and plan (1-230, 6829-7042),
the dependency catalogue A1-H4 (3757-4649), Package A gauges (7640-7900), the
background theorems and plan of (1b) (9583-9760, headers to 9930), Theorem 2.1
and its credit list (17251-17330), the operation and B (17583-17612), Lemma 2.5
and Prop 2.6 head (17674-17720), the opening of (2d) (17841-18011), the
drop-out evaluations (18130-18205), the action seen by the tests (18206-18333),
the new mark and floor (18334-18415), headers of the other (2d) paragraphs,
(2e) the class, the order and Theorem 2.11 (19408-19470), Prop 4.5 and
Lemma 4.11 (22590-22612), the strategy and Prop 1.6 (22879-22942), (4c) opening
(22944-22990), ordinary stability (23385-23416, 23481-23541), Theorems 7.1, 7.5,
Lemma 7.6, 7a.1.8 context (25966-26240), the finite-reference opening
(26935-26950), the coupling capsule and Ward target (31889-31960,
32326-32400), the index (32869-32923). Located but not read: everything else,
in particular Props 2.7, 2.6 in full, the genealogy count (18416-18672), the
mass induction (18719-19189), the one-loop section (21065 ff.), the clean-box
and Gaussian-segment sections (26223-26700), the pointed Hessian and window
sections, the angular and phase sections.

Read here: FINISH.md, GOAL.md; heads or greps of `parts/hard-core--mapped.md`
(Text 1, the proof-status list, Text 3 head), `library/seam-nonlinear-c.md`
4.1, `library/rel-phi-c.md` head, `library/lattice-uhlenbeck.md` head,
`library/lattice_sobolev_box_gauge.md` head, `library/c0-loc.md` head,
`library/energy-by-stages.md` head, `library/explicit-region-two-step.md`
(TYP, HOLES), `library/nt2-free-value-by-hand.md` head,
`gates/history-budget-769697e8d.md` head, `gates/explicit-region-codex-00f9df685.md`
(HOLES), `parts/upper-chain.md` (Lemma 1.1 line). Everything else in this
folder is cited from the queue table of FINISH.md, not re-read.

Limits. A map, not a gate: no statement of the outline was checked except the
energy-of-averages bootstrap (Section 2, end) and the column count of P. The
claim that SA Theorems 3-4 would give (REL-D) is my inference. The ranking is
one same-model judgment. No numerics were run, so the memory gate was not
needed; `checks/samap/locate_codes.py` is a read-only line locator.
