---
claim_id: kcpt_chiral_parity_lagrangian_polarization_bounded_theorem_note_2026-07-19
claim_type: bounded_theorem
claim_scope: "Conditional finite-surface symplectic packaging on the fixed 4^3 staggered lattice. Given the linked chiral-parity sign-reversal theorem and Kähler-triple theorem, the even and odd staggered-parity planes are complementary Lagrangian subspaces for omega=-J_full; J_full exchanges them; S_eps is a real-linear antisymplectic involution that swaps the +/-i eigenspaces after complexification; the order-768 ambient group has a preserve/swap Z/2 grading with order-384 centralizer kernel; and J_alt exchanges the same parity planes. This is a mathematical finite representation statement, not a physical CP identification, orientation selection, dynamics, measure, continuum, or retained-grade claim."
upstream_dependencies:
  - kcpt_chiral_parity_common_sign_orbit_bounded_theorem_note_2026-07-19
  - kcpt_kahler_triple_ambient_invariant_metric_symplectic_bounded_theorem_note_2026-07-19
runner: scripts/kcpt_chiral_parity_lagrangian_polarization_2026_07_19.py
---

# KCPT chiral parity: Lagrangian polarization of the Kähler triple

**Date:** 2026-07-19
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Scope:** conditional on the two linked finite-surface theorems below. The
result is a symplectic-geometric reading of computed blocks, not a physical
identification.
**Audit-status authority:** independent audit lane only. This note sets no
audit verdict and predicts none.
**Primary runner:**
[`scripts/kcpt_chiral_parity_lagrangian_polarization_2026_07_19.py`](../scripts/kcpt_chiral_parity_lagrangian_polarization_2026_07_19.py)
**Runner cache:**
[`logs/runner-cache/kcpt_chiral_parity_lagrangian_polarization_2026_07_19.txt`](../logs/runner-cache/kcpt_chiral_parity_lagrangian_polarization_2026_07_19.txt)

## Supplied finite surface

Work on the real site representation `V_R ~= R^64` of the fixed `4^3`
staggered lattice and its complexification. The
[`chiral-parity common-sign-orbit theorem`](KCPT_CHIRAL_PARITY_COMMON_SIGN_ORBIT_BOUNDED_THEOREM_NOTE_2026-07-19.md)
supplies the real involution

> `S_eps = diag((-1)^(x_1+x_2+x_3))`

and the exact relation `S_eps J_full S_eps = -J_full`. That theorem explicitly
does not give this real-linear site-parity map a physical identification.

The
[`ambient-invariant Kähler-triple theorem`](KCPT_KAHLER_TRIPLE_AMBIENT_INVARIANT_METRIC_SYMPLECTIC_BOUNDED_THEOREM_NOTE_2026-07-19.md)
supplies the fixed counting metric and conventions

> `g = I_64`, `omega(x,y)=g(J_full x,y)`,
> `omega = J_full^T g = -J_full`, `h=g+i omega`.

It also supplies `J_full^2=-I_64`, compatibility with `g`, and the
order-`768` ambient signed-permutation group `G_amb`. The metric `g=I_64` is
one disclosed representative in the compatible positive cone, not a forced
metric. Consequently the Hermitian form inherits that choice.

Let `L_+` and `L_-` be the `+1` and `-1` eigenspaces of `S_eps`. They are the
real spans of the even and odd staggered-parity sites. Each has dimension
`32`, and `V_R=L_+ direct-sum L_-`.

## Real parity polarization

The involution is real, orthogonal, traceless, and diagonal with entries
`+1` and `-1`. Its two eigenspaces therefore partition the standard real site
basis into two `32`-planes.

The relation `S_eps J_full S_eps=-J_full` is equivalent to the vanishing of
the two diagonal parity blocks of `J_full`. Since `omega=-J_full`,

> `omega|_(L_+ x L_+) = 0`, and
> `omega|_(L_- x L_-) = 0`.

The form is nondegenerate structurally: `omega J_full=(-J_full)J_full=I_64`,
so `J_full` is its explicit inverse. Each isotropic plane has half the real
dimension of `V_R`; hence each is Lagrangian, and together they form a
complementary Lagrangian polarization.

## Plane-exchanging complex structure

Anticommutation, `S_eps J_full+J_full S_eps=0`, sends each parity eigenspace
to the other. Because `J_full^2=-I_64`, this restriction is injective and its
inverse is `-J_full`; therefore

> `J_full : L_+ -> L_-`

is a rank-`32` isomorphism, and likewise in the reverse direction. This is the
mathematical Kähler-polarization intertwiner on the supplied finite surface.

## Antisymplectic reality action

The same sign reversal gives

> `S_eps^T omega S_eps = -omega`.

Thus `S_eps` is a real-linear antisymplectic involution. On the supplied
Hermitian form it gives

> `S_eps^T h S_eps = g-i omega = conjugate(h)`.

After complexification, `S_eps` maps the `+i` eigenspace of `J_full` to the
`-i` eigenspace. This is an algebraic reality action on the complexified
finite representation. No charge-conjugation operator, physical CP map, or
observable readout is constructed or claimed.

## Ambient preserve/swap grading

Every element of `G_amb` is a signed permutation that changes total
staggered parity uniformly. It therefore either preserves both planes or
swaps them. The elements preserving each plane are exactly those commuting
with `S_eps`, namely `C_(G_amb)(S_eps)`. Exact enumeration of the integer
signed permutations gives

> `|G_amb|=768`, `|C_(G_amb)(S_eps)|=384`,

with `384` preserving elements, `384` swapping elements, and none outside
those classes. Composition adds the preserve/swap parity modulo two, so this
is a surjective homomorphism `G_amb -> Z/2` with the centralizer as kernel.

## Orientation-sibling boundary

The supplied sibling `J_alt=J_ker-J_bulk` also anticommutes with `S_eps` and
therefore exchanges the same two parity planes. It differs nontrivially from
`J_full`, since

> `J_full-J_alt=2J_bulk != 0`.

The real polarization is common to these two supplied complex structures;
the exchanging intertwiner differs. This statement does not select either
orientation or collapse the larger relative-sign family described by the
chiral-parity dependency.

## Claim boundaries

- The block-vanishing algebra is the linked chiral-parity theorem expressed
  in the parity basis; the new result is its bounded symplectic packaging and
  the explicit ambient preserve/swap grading.
- The result is conditional on two currently unaudited bounded dependencies
  and therefore makes no retained-grade or publication-usable claim.
- It is confined to the fixed `4^3` finite surface. It supplies no continuum,
  infinite-volume, Hamiltonian, admissibility-dynamics, measure, or
  probability statement.
- It is neutral in `r`, measure, metric selection, and orientation selection.
- Standard Lagrangian, Kähler, antisymplectic, and reality terminology
  describes the computed finite linear algebra; it is not imported as an
  additional axiom.

## Verification

The paired runner reconstructs the lattice matrices and all `768` ambient
signed permutations. Integer parity and group-classification assertions are
checked exactly. Matrices involving the shell coefficients in
`Q(sqrt(2),sqrt(3))` are evaluated numerically with declared tolerances, so
those gates are numerical certificates rather than exact-arithmetic ones. The
runner separately checks the definitions `g=I_64`,
`omega=J_full^T g=-J_full`, and `h=g+i omega`; checks the structural inverse
`omega J_full=I_64` instead of rounding a floating determinant; and carries
descriptive check names. It reads no mutable Markdown or environment-selected
fixture, so its cache is pinned only to its own source content.
