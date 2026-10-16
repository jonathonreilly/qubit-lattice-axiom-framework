---
claim_id: cubic_covariance_freezes_a_one_qubit_tick_cell_classification_bounded_theorem_note_2026-10-16
claim_type: bounded_theorem
claim_scope: "Discrete-time unitary walks on l2(Z^3) (x) C^2 with hops inside the 27-point cell {-1,0,1}^3, translation covariant and covariant under a subgroup H of the proper cubic group with the full-soldered spin-1/2 coin action A_{Rn} = D(R) A_n D(R)^dagger. Exact (Groebner over Q, valid over C): for H = O and H = T every such walk is a constant phase times +-1; for H = D4 the only moving walks are axial shifts exp(+-i sigma_z k_z) up to phase; under the other three soldering-menu coin actions (trivial, sign twist, axis) an O-covariant cell walk is a constant on-site coin; on the 125-point stencil {-2,...,2}^3 and the 343-point stencil {-3,...,3}^3 (ranges two and three per axis) with the full-soldered action every O-covariant walk is a constant phase (range three computer-assisted with Singular); for H = D3 on the cell the only moving walks are the body-diagonal shifts exp(+-i (k1+k2+k3) sigma.(1,1,1)/sqrt 3) up to phase (both by line-branch certificates, second runner), so no subgroup of order 6 or more permits motion in more than one direction on the cell. Exhibit: the D2-covariant product walk moves in all three directions with an isotropic unit-speed Weyl cone at k = 0. Numerical (not proof): C3, C4 and D2 admit three-dimensional moving walks; every moving walk found has three-winding zero. Larger stencils, other coin actions and larger coins are stated separately with their evidence level."
upstream_dependencies:
  - minimal_axioms
runner: scripts/cubic_covariant_qubit_walk_cell_classification_2026_10_16.py
---

# Cubic covariance freezes a one-qubit tick on the 27-point cell

**Date:** 2026-10-16
**Type:** bounded_theorem
**Status:** bounded-support; exact finite classification on a declared stencil
and coin action; unaudited.
**Status authority:** independent audit only. This note adds no axiom,
primitive or dynamics clause.

## Result up front

1. **No covariant one-qubit tick moves on the 27-point cell.** A unitary walk
   on one qubit per site whose single time step hops at most one site along
   each axis (the 26 surrounding sites and the site itself), and which is
   covariant under lattice translations and the proper cubic rotations with
   the coin rotated by the spin-1/2 lift, is a constant: U = e^{i theta} (+-1).
   The same holds with only the tetrahedral subgroup T (order 12). Under the
   other three coin actions of the soldering menu (trivial, sign twist, axis)
   the walk is a constant on-site coin: nothing moves under any of the four
   actions. With the full-soldered action the freeze persists when the hop
   range is two or three sites along each axis (125- and 343-point stencils).
2. **Keeping a fourfold axis and a perpendicular half-turn (D4, order 8)
   permits motion along that axis only:** U = e^{i theta} exp(+-i sigma_z k_z).
   **Keeping a body diagonal and the three half-turns perpendicular to it
   (D3, order 6) permits motion along that diagonal only:**
   U = e^{i theta} exp(+-i (k_1 + k_2 + k_3) sigma.n), n = (1,1,1)/sqrt 3.
3. **Three-dimensional motion needs a symmetry group of order at most 4 on
   this cell.** Every subgroup of O of order 6 or more (O, T, D4, D3) is
   classified exactly above, and none of them allows motion in more than one
   direction.
   The D2 product walk (three conditional axis shifts) is D2-covariant, moves
   in every direction and has the isotropic Weyl cone V = exp(i sigma.k) +
   O(k^2) at k = 0; numerically, C3- and C4-covariant walks also move in three
   directions.
4. **No moving walk found evades doubling.** Every moving walk found has
   three-winding (net chirality) zero.

Consequence for the framework, stated as an implication and not adopted: a
one-qubit discrete-time motion law on the 27-point cell must give up exact
proper-cubic covariance (keeping at most an axis, a body diagonal or the
three axis half-turns), or use hops of range four or more, or leave the declared coin action
or site algebra. The companion note
`TWO_QUBIT_SITE_UNFREEZES_THE_CUBIC_TICK_DOUBLER_FREE_DIRAC_WALK_BOUNDED_THEOREM_NOTE_2026-10-16`
shows that a two-qubit site (the parked M_4(C) fork) does admit exactly
covariant moving cell walks, with a forced Dirac structure. Continuous-time
Hamiltonian walks such as
`H = sum_a sigma_a S_a` are O-covariant but their unit-time propagators have
unbounded range, so they are not in this class.

## Premises and declared objects

- **Axioms used:** the Lattice axiom supplies Z^3, translations and the
  proper cubic rotations O about each site; the Qubit axiom supplies the
  one-site algebra M_2(C). Neither supplies dynamics. The unitary walk, its
  stencil and the coin action are explicit mathematical hypotheses of this
  note, not framework content.
- **Walk.** U(k) = sum_{n in N} A_n e^{i k.n} with A_n in M_2(C) and N =
  {-1,0,1}^3 (Chebyshev range one). Unitarity is U(k) U(k)^dagger = 1 for
  every k.
- **Full-soldered covariance under H <= O.** A_{Rn} = D(R) A_n D(R)^dagger for
  R in H, D the spin-1/2 lift (sign ambiguity cancels in the conjugation).
  Equivalently U(Rk) = D(R) U(k) D(R)^dagger.
- **Other coin actions** of the soldering menu
  (`THE_SOLDERING_MENU_FOUR_ACTIONS_..._2026-09-22`) are treated separately
  below.

## Theorem 0 — reduction to an SU(2)-valued trigonometric identity

If H fixes no nonzero vector of R^3, every H-covariant unitary walk is
U = e^{i theta} V with V(k) = f(k) + i g(k).sigma, where f is a real
H-invariant trigonometric polynomial, g a real H-equivariant one
(g(Rk) = R g(k)), both supported on N, and f^2 + |g|^2 = 1 identically.

*Proof.* det U is a Laurent polynomial of modulus one on the torus, so
det U . conj(det U) = 1 in the Laurent ring and det U = c z^m is a unit
monomial. Covariance gives det U(Rk) = det U(k), so m is fixed by H and hence
m = 0. Then V = e^{-i theta} U has det V = 1 and V(k) is in SU(2) pointwise,
so V = f + i g.sigma with f = tr V / 2 and g real, with the same support.
D(R) (g.sigma) D(R)^dagger = (Rg).sigma gives the transformation rules.
The groups O, T, D4, D3 and the axis D2 fix no nonzero vector (runner check).

## Theorem 1 — O and T: only constant walks

For H = O the invariant scalars on N are spanned by 1, sum c_a, sum c_a c_b,
c_1 c_2 c_3 and the equivariant vectors by (s_a), (s_a (c_b + c_c)),
(s_a c_b c_c), with c_a = cos k_a and s_a = sin k_a. Reducing
f^2 + |g|^2 - 1 modulo s_a^2 = 1 - c_a^2 gives a system of coefficient
equations. Its Groebner basis over Q contains a_0^2 - 1 and a power of every
other coefficient. Hence on the complex variety every coefficient except a_0
vanishes and a_0 = +-1: V = +-1. For H = T the families have 5 + 6 members
(the extra invariant s_1 s_2 s_3 and the chiral vectors appear); the same
certificate holds.

The certificate is exact; it does not depend on numerical tolerance and
holds over C, so no complex or non-positive branch is hidden.

## Theorem 2 — D4: axial motion only

For H = D4 (the fourfold axis e_z with the half-turn about e_x) the Groebner
basis places every coefficient except a_0, a_1 (of c_3) and b_0 (of
(0, 0, s_3)) in the radical. The residual identity
(a_0 + a_1 c_3)^2 + b_0^2 s_3^2 = 1 forces a_0 a_1 = 0, a_1^2 = b_0^2 and
a_0^2 + b_0^2 = 1. Moving solutions are a_0 = 0, a_1 = +-1, b_0 = +-1, that
is V = +-exp(+-i sigma_z k_z): a conditional shift along the axis.

## Theorem 3 — the rest of the soldering menu

Let the coin transform by one of the other three homomorphisms O -> SO(3) of
the soldering menu, Q(R) = 1 (trivial), diag(1, s, s) (sign twist, s the sign
of the axis permutation of R) or s|R| (axis), so that f(Rk) = f(k) and
g(Rk) = Q(R) g(k). Momentum still rotates by R, so Theorem 0 applies.

- *Trivial.* f and each g_j are O-invariant; on the cell these are
  polynomials in c_1, c_2, c_3 of degree at most three. The identity
  f^2 + sum_j g_j^2 = 1 then holds on [-1, 1]^3 and so in R[c]; the top-degree
  homogeneous parts form a vanishing sum of real squares, so every function is
  constant.
- *Axis.* The Groebner basis places every k-dependent coefficient in the
  radical; U is a constant coin.
- *Sign twist.* Every k-dependent coefficient of f, and all but two of g,
  lie in the radical. The two survivors multiply (0, s_1 s_2 s_3, 0) and
  (0, 0, s_1 s_2 s_3); the residual identity contains b_4^2 + b_5^2 = 0, which
  for a real walk forces both to vanish (the complex branch b_4 = +-i b_5 is
  not a real walk). U is the constant coin cos theta + i sin theta sigma_x.

So under every coin action of the menu an O-covariant one-qubit walk on the
cell does not move.

## Exhibit — a D2-covariant walk that moves in three directions

With q_a = cos k_a + i sigma_a sin k_a (the conditional shift along axis a),
V = q_x q_y q_z has f = c_1c_2c_3 + s_1s_2s_3 and
g = (s_1c_2c_3 - c_1s_2s_3, c_1s_2c_3 + s_1c_2s_3, c_1c_2s_3 - s_1s_2c_3).
It is unitary, covariant under the three axis half-turns, not covariant under
the quarter turns, and dg/dk at k = 0 is the identity, so
V = exp(i sigma.k) + O(k^2): an isotropic unit-speed Weyl cone. Beyond the
cone, cos omega = f = 1 - |k|^2/2 + k_1 k_2 k_3 + O(k^4), so with n = k/|k|

    omega(k) = |k| - n_1 n_2 n_3 |k|^2 + O(|k|^3),
    group speed along n: 1 - 2 n_1 n_2 n_3 |k| + O(|k|^2).

The leading lattice correction is parity odd (omega(k) != omega(-k)), linear
in |k| a, and handed: it is the D2-invariant pseudoscalar k_1 k_2 k_3, at most
2/(3 sqrt 3) = 0.385 |k| a in relative size. Exact cubic covariance would
forbid this term; its presence is the price of motion on the cell. Each factor
depends on one momentum, so the three-winding of V vanishes and its Weyl
nodes come in compensating pairs.

## Numerical scan of the remaining subgroups (evidence, not proof)

Least-squares searches of the unitarity identity (60 starts per group with the
moving coefficients pinned to unit norm, plus a scale-free rerun with a lower
bound for D3; pinned searches can miss walks of other norm, so their positive
findings are reliable and their negative ones are not):

| H | order | moving walks found | momentum directions used |
|---|---|---|---|
| C3 | 3 | yes | 3 |
| C4 | 4 | yes | 1, 2, 3 |
| D2 (axis half-turns) | 4 | yes (exhibit above) | 3 |
| D3 | 6 | body-diagonal only (Theorem 5, exact); the 300-start search (sum b^2 >= delta) missed these isolated walks | 1 |
| D4 | 8 | axial only (Theorem 2) | 1 |
| T | 12 | none (Theorem 1) | – |
| O | 24 | none (Theorem 1) | – |

All moving solutions found had numerically zero three-winding.

The D3 row is a warning about the negative entries of such searches: 300
scale-free starts converged to the quartic valley of the constant walk and
never reached the two isolated body-diagonal shifts that Theorem 5 finds
exactly. Negative search results here and in the companion two-qubit note
are therefore weak evidence.

## Independent check of Theorems 1 and 2

A fresh agent context, given only the problem statement (not the expected
answer, nor this note or its runner), re-derived the O, T and D4 cases by a
different route: raw complex coefficients A_n = a_n0 I + a_n.sigma without
the SU(2) reduction, both U U^dagger = I and U^dagger U = I, the real/imaginary
split over Q, and Groebner bases in Singular 4.4 (slimgb), with a second
algorithm (modStd) for T, a sympy re-run over Q(i) for O, and a primary
decomposition (minAssGTZ) for D4. Results agree exactly: O and T give only
e^{i theta} I; D4 gives exactly three components, e^{i theta} I and
e^{i theta} exp(+-i k_z sigma_z). Scripts and outputs are kept in the loop
pack (`.claude/science/physics-loops/toe-campaign-20261015/independent_check_B1/`).
Limits of independence: the checker is the same model family in a new
context; the D4 result rests on one Groebner algorithm plus a hand argument
for the final one-dimensional step.

## Theorem 4 — range two per axis under O: still frozen (exact)

On the 125-point stencil {-2,...,2}^3 with the full-soldered action every
O-covariant one-qubit walk is a constant phase.

*Proof.* By Theorem 0, U = e^{i theta} V with V = f + i g.sigma; the
families have 10 invariant scalars and 15 equivariant vectors, and
f^2 + |g|^2 = 1 gives 149 coefficient equations. Restrict to the three
symmetry lines k = t e with e = (1,0,0), (1,1,0), (1,1,1). The stabiliser of
e in O (C4, C2, C3) fixes only the multiples of e, so along the line
g(t e) = gamma(t) e/|e| with gamma real. Then P = f + i gamma is a Laurent
polynomial in z = e^{it} with P(z) conj(P)(1/z) = f^2 + gamma^2 = 1, hence a
unit monomial lambda z^n. At t = 0 equivariance gives g(0) = 0 and
f(0) = +-1; absorbing the sign into the phase, lambda = 1, so
f = cos(n t) and gamma = sin(n t) on that line, with |n| bounded by the line
degree: 2, 4 and 6 on the axis, face diagonal and body diagonal. Each of the
5 x 9 x 13 = 585 choices (m, q, p) of the three exponents is a linear system
on the 25 coefficients. Exact linear algebra over Q(i, sqrt 2, sqrt 3) shows
all of them except (0, 0, 0) are inconsistent. On (0, 0, 0) the linear system
fixes f's coefficients (a_0 = 1, the rest 0) and leaves six g-coefficients
free; the Groebner basis over Q of the remaining unitarity equations places
a power (at most the third) of each of the six in the ideal. So the variety
is one point and V = 1.

The certificate is exact and holds over C. Two separate implementations
agree: the second runner (Laurent restriction and linsolve) and a scratch
version (trigonometric restriction and solve). A fresh agent context, given
only the problem, reached the same verdict by a different route. It classified
the D4-covariant slices k_3 = 0, pi exactly (100 line cases with Groebner
bases, cross-checked by Singular modStd and minAssGTZ) and then reduced the
3-D problem to a 4-variable Groebner basis. Its scripts are in
`.claude/science/physics-loops/toe-campaign-20261015/independent_check_R2/`.
The same limits of independence apply as for Theorems 1–2. The earlier numerical
searches are consistent with it. Their best residuals scale like delta^2
as the lower bound delta on the motion coefficients shrinks. For delta >= 0.5
they reach one isolated interior near-miss (residual 4.6e-4, nonsingular
Jacobian), which the theorem shows is not a walk.

*Split-step walks.* Composing steps does not escape Theorem 4.
Suppose a product U = U_2 U_1 of two one-qubit steps, each with hops in the
27-point cell, is O-covariant as a whole. Its hops lie in {-2,...,2}^3, so U
is a constant phase. The factors themselves need not be covariant. Two
conditional shifts along the same axis, or a D2 product walk followed by any
cell step, are examples. The same holds for any product whose total range
per axis is at most two.

## Theorem 4' — range three under O: still frozen (exact, computer-assisted)

On the 343-point stencil {-3,...,3}^3 with the full-soldered action every
O-covariant one-qubit walk is a constant phase.

*Proof.* The families have 21 invariant scalars and 42 equivariant vectors,
63 real unknowns in all. The line lemma is applied on six lines k = b + t e,
each with b a time-reversal-invariant momentum:

    Gamma + t(1,0,0),  Gamma + t(1,1,0),  Gamma + t(1,1,1),
    (0,0,pi) + t(1,0,0),  (0,0,pi) + t(1,1,0),  (0,pi,pi) + t(1,0,0).

On each line the stabiliser fixes only multiples of e. The stabiliser of b
fixes no nonzero multiple of e, so g(b) = 0 and f(b) = eps_b = +-1. The sign
depends only on the class of b (X or M), and is +1 at Gamma. Hence on each
line f = eps cos(n t) and gamma = eps sin(n t), with |n| <= 3 |e|_1. The
exponents on the three Gamma lines were checked exactly over all
7 x 13 x 19 choices: only n = 0 is consistent. With those fixed, all
7 x 13 x 7 x 4 = 2548 choices of exponents and signs on the other three
lines were checked exactly, and only the trivial one is consistent. That branch fixes f = 1 and leaves 21
real unknowns, constrained by 122 real linear and quadratic equations. Their
Groebner basis over Q (Singular modStd, verified mode; repeated mod 32003
with slimgb) is zero-dimensional and contains a power (at most the fifth) of
every unknown. So the variety is the single point V = 1.

This step relies on Singular, which the repository runners do not call. The
scripts, the Singular input and the logs are in
`.claude/science/physics-loops/toe-campaign-20261015/exact_extensions/`.

*Independent check.* A fresh agent context, given only the problem, proved
the same statement by a different and fully exact route. First it
classified the D4-covariant walks on the planes k_3 = 0, pi: 172 line cases,
171 of them linearly inconsistent, and the last closed by a Singular
radical. Hence V = 1 on all six planes k_j in {0, pi}. Then g vanishes there,
so g = s_1 s_2 s_3 h. Also 1 - f >= 0 vanishes there, so
1 - f = s_1^2 s_2^2 s_3^2 p, and unitarity becomes
p (2 - s_1^2 s_2^2 s_3^2 p) = |h|^2. At the eight points {0, pi}^3 the
stabilisers force h = 0, so p = 0 there. At range three p lies in the
4-dimensional span of {1, sum c, sum cc, c1c2c3}, and these point
conditions give p = 0. Its scripts are in
`.claude/science/physics-loops/toe-campaign-20261015/independent_check_B6/`.

Ranges one, two and three are therefore exact. In the line-branch method the
pattern is the same at each range: the lines force the trivial branch, and
the unitarity ideal then closes it. The checker's route reduces the 3-D
problem to a 2-D one plus a positivity identity. It is the more promising
path to every finite range, but it is not a proof of that: at higher ranges
p has more freedom than eight point values can fix. Every finite range
remains open.

## Theorem 5 — D3 on the cell: body-diagonal motion only (exact)

For H = D3 (the threefold rotations about n = (1,1,1)/sqrt 3 and the three
half-turns about (1,-1,0), (0,1,-1), (-1,0,1)), every covariant cell walk is,
up to a constant phase, V = 1 or V = exp(+-i (k_1 + k_2 + k_3) sigma.n):
a conditional shift by +-(1,1,1).

*Proof.* The families have 7 invariant scalars and 12 equivariant vectors
(99 coefficient equations). The stabilisers of the body axis (C3) and of the
half-turn axis (1,-1,0) (C2) fix only their lines, so the line lemma gives
exponents n_body in {-3..3} and n_face in {-2..2}. Unlike for O, all 35 linear
systems are consistent. On each branch the Groebner basis of the remaining
unitarity equations (5 free coefficients) is {1}, except on (0, 0) and
(+-3, 0); there it places v - v* in the radical for every free coefficient v,
so each is a single point: V = 1 and the two shifts above. Both shifts are
D3-covariant and not O-covariant (they single out one body diagonal).

D3 is the body-diagonal analogue of D4: a group that keeps one distinguished
axis permits a conditional shift along it and nothing else. This settles the
D3 entry, which the earlier numerical scan had wrong.

A second fresh agent context, given only the problem, found the same three
walks by its own route. It used a body-diagonal line lemma with the
symmetries U -> -U and U -> U^dagger, then Singular eliminants (`finduni`)
for each exponent case. Its scripts are in
`.claude/science/physics-loops/toe-campaign-20261015/independent_check_B5/`.

## What this does not do

- It does not classify walks with hops of range four or more, and at ranges
  two and three it covers only H = O with the full-soldered action. Subgroups of order
  at most 4 are treated numerically only.
- It does not exclude O-covariant motion with a larger site (two qubits or a
  spin-3/2 coin); that is outside the Qubit axiom's one-site algebra and is a
  separate question.
- It does not derive a dynamics clause, a tick, a clock or a light cone, and
  it does not select a subgroup, an axis or a handedness.
- It does not claim that continuous-time covariant dynamics is excluded.

## Relation to prior work

Bialynicki-Birula showed that the simple cubic lattice with nearest-neighbour
hops admits no homogeneous linear unitary automaton of the Weyl type;
D'Ariano and Perinotti (2014) and D'Ariano, Erba and Perinotti (2017) obtained
Weyl walks on the body-centred-cubic Cayley graph under their isotropy
definition (a group acting on the generator set with a unitary coin
representation). Those isotropy notions differ from the framework's full
soldering. The D2 exhibit above is not new. Expanding q_x q_y q_z leaves
only the eight body-diagonal hops (+-1,+-1,+-1), and its f = c1c2c3 + s1s2s3
and g agree with the known BCC Weyl automaton up to conventions. The point
added here is that this known walk is covariant under the axis half-turns
D2 with the soldered spin action and under no larger subgroup of O. The
groups containing D2 are D4, T and O, and Theorems 1 and 2 exclude them. It
also adds that its leading lattice correction is the handed term
-n1 n2 n3 |k|^2. New here: the exact classification on the whole 27-point cell
(axis, face-diagonal and body-diagonal hops together) under the soldered O
action and its subgroups, the exact T and D4 statements, and the subgroup
ceiling for motion.

## No-Go Discipline Gate

### N1 — Routes that could evade the claim
1. *Larger stencil*: ATTEMPTED; Theorems 4 and 4' close ranges two and three
   per axis under O with the full action. Range four and beyond are not
   covered.
2. *Smaller symmetry group*: ATTEMPTED; Theorems 1–2 and the scan show which
   subgroups permit motion.
3. *Nonconstant determinant*: ATTEMPTED; Theorem 0 excludes it for every
   group without fixed vectors, which includes all groups for which a
   negative claim is made.
4. *Other coin actions of the soldering menu*: ATTEMPTED; Theorem 3 closes
   all four actions on the cell.
5. *Larger coin (two qubits, spin 3/2)*: ATTEMPTED; reported below as a
   separate question outside the Qubit axiom's one-site algebra.
6. *Continuous time*: RULED OUT AS A COUNTERROUTE by scope: the
   O-covariant Hamiltonian walk exists but its unit-time propagator is not
   finite range.

### N2 — Wall independence
One structural statement per group; no wall count is asserted.

### N3 — Hidden-wall scan
The walk, its stencil, translation covariance on one-site cells and the
full-soldered coin action are stated hypotheses. The phrase "proper cubic
rotations" is the Lattice axiom's.

### N4 — Residual matching
The prior results cited are on different lattices or isotropy notions and
are not used as witnesses.

### N5 — Rhetoric audit
"Cannot move" is claimed only for the 27-point cell and the declared coin
actions, for H = O and T, and for the 125- and 343-point stencils with H = O and the
full action; for D4 and D3 only "one direction only". Statements about larger
stencils, other actions or larger coins are reported at their own evidence
level.

### N6 — Partial-closure paths
Breaking O to C3, C4 or D2 permits three-dimensional motion on the cell;
breaking it to D4 or D3 permits motion along one axis or one body diagonal.

### N7 — Strongest objection
A moving O-covariant walk might exist at range four or more. The theorems
are scoped to ranges one to three for that reason.

### N8 — Earlier claims
No earlier repository claim is narrowed or contradicted.

## Verification

```bash
python3 scripts/cubic_covariant_qubit_walk_cell_classification_2026_10_16.py
```

Expected: `TOTAL: PASS=31 FAIL=0` (under a minute).

```bash
python3 scripts/cubic_covariant_qubit_walk_line_branch_certificates_2026_10_16.py
```

Expected: `TOTAL: PASS=16 FAIL=0` (about ten minutes; Theorems 4 and 5).
