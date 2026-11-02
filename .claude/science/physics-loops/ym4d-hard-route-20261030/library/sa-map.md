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

Status: in progress, written section by section.

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
