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
