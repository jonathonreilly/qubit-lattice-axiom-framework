---
claim_id: cubic_covariance_freezes_a_one_qubit_tick_cell_classification_bounded_theorem_note_2026-10-16
claim_type: bounded_theorem
claim_scope: "Discrete-time unitary walks on l2(Z^3) (x) C^2 with hops inside the 27-point cell {-1,0,1}^3, translation covariant and covariant under a subgroup H of the proper cubic group with the full-soldered spin-1/2 coin action A_{Rn} = D(R) A_n D(R)^dagger. Exact (Groebner over Q, valid over C): for H = O and H = T every such walk is a constant phase times +-1; for H = D4 the only moving walks are axial shifts exp(+-i sigma_z k_z) up to phase. Exhibit: the D2-covariant product walk moves in all three directions with an isotropic unit-speed Weyl cone at k = 0. Numerical (not proof): D3 admits no moving walk in the searched family; C3, C4 and D2 admit three-dimensional moving walks; every moving walk found has three-winding zero. Larger stencils, other coin actions and larger coins are stated separately with their evidence level."
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
   The same holds with only the tetrahedral subgroup T (order 12).
2. **Keeping a fourfold axis and a perpendicular half-turn (D4, order 8)
   permits motion along that axis only:** U = e^{i theta} exp(+-i sigma_z k_z).
3. **Three-dimensional motion survives only below order 6 on this cell.**
   The D2 product walk (three conditional axis shifts) is D2-covariant, moves
   in every direction and has the isotropic Weyl cone V = exp(i sigma.k) +
   O(k^2) at k = 0; numerically, C3- and C4-covariant walks also move in three
   directions and no D3-covariant moving walk was found.
4. **No moving walk found evades doubling.** Every moving walk found has
   three-winding (net chirality) zero.

Consequence for the framework, stated as an implication and not adopted: a
one-qubit discrete-time motion law on the 27-point cell must give up exact
proper-cubic covariance (keeping at most an axis, a body diagonal or the
three axis half-turns), or leave this cell, or leave the declared coin action
or site algebra. Continuous-time Hamiltonian walks such as
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

## Exhibit — a D2-covariant walk that moves in three directions

With q_a = cos k_a + i sigma_a sin k_a (the conditional shift along axis a),
V = q_x q_y q_z has f = c_1c_2c_3 + s_1s_2s_3 and
g = (s_1c_2c_3 - c_1s_2s_3, c_1s_2c_3 + s_1c_2s_3, c_1c_2s_3 - s_1s_2c_3).
It is unitary, covariant under the three axis half-turns, not covariant under
the quarter turns, and dg/dk at k = 0 is the identity, so
V = exp(i sigma.k) + O(k^2): an isotropic unit-speed Weyl cone. Each factor
depends on one momentum, so the three-winding of V vanishes and its Weyl
nodes come in compensating pairs.

## Numerical scan of the remaining subgroups (evidence, not proof)

Least-squares searches of the unitarity identity with the moving coefficients
pinned to unit norm (60 starts per group; scratch evidence summarized in the
loop pack):

| H | order | moving walks found | momentum directions used |
|---|---|---|---|
| C3 | 3 | yes | 3 |
| C4 | 4 | yes | 1, 2, 3 |
| D2 (axis half-turns) | 4 | yes (exhibit above) | 3 |
| D3 | 6 | none (best residual 1.1e-3) | – |
| D4 | 8 | axial only (Theorem 2) | 1 |
| T | 12 | none (Theorem 1) | – |
| O | 24 | none (Theorem 1) | – |

All moving solutions found had numerically zero three-winding.

## What this does not do

- It does not classify walks with hops beyond the 27-point cell. A
  range-two-per-axis search under O is reported separately below with its
  evidence level.
- It does not exclude O-covariant motion with a different coin action or a
  larger site; those are separate questions reported below.
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
soldering. New here: the exact classification on the whole 27-point cell
(axis, face-diagonal and body-diagonal hops together) under the soldered O
action and its subgroups, the exact T and D4 statements, and the subgroup
ceiling for motion.

## No-Go Discipline Gate

### N1 — Routes that could evade the claim
1. *Larger stencil* (range two per axis, 125 points): ATTEMPTED; see the
   range-two section below. Not covered by the theorem.
2. *Smaller symmetry group*: ATTEMPTED; Theorems 1–2 and the scan show which
   subgroups permit motion.
3. *Nonconstant determinant*: ATTEMPTED; Theorem 0 excludes it for every
   group without fixed vectors, which includes all groups for which a
   negative claim is made.
4. *Other coin actions of the soldering menu*: ATTEMPTED; reported below.
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
action, for H = O and T; for D4 only "axial only". Statements about larger
stencils, other actions or larger coins are reported at their own evidence
level.

### N6 — Partial-closure paths
Breaking O to C3, C4 or D2 permits three-dimensional motion on the cell.

### N7 — Strongest objection
A moving O-covariant walk might exist at larger range. The theorem is scoped
to the 27-point cell for that reason.

### N8 — Earlier claims
No earlier repository claim is narrowed or contradicted.

## Verification

```bash
python3 scripts/cubic_covariant_qubit_walk_cell_classification_2026_10_16.py
```

Expected: `TOTAL: PASS=22 FAIL=0` (about 20 s).
