---
claim_id: dynamics_clause_covariant_nearest_neighbour_two_qubit_generators_heisenberg_under_possibility_covariance_three_couplings_under_full_soldering_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "For a supplied dynamics clause that is recorded and not adopted - a time-independent Hermitian generator on the qubit lattice equal to a sum of two-site terms on nearest-neighbour bonds, covariant under lattice translations and under the proper cubic rotations acting on possibilities by one of the four actions of the landed soldering menu - the covariant bond data are classified exactly. The two-site couplings form spaces of dimension 6 (trivial action: symmetric M), 4 (sign twist), 4 (axis soldering) and 3 (full soldering: J s.s, K (e.s)(e.s) and the Moriya term D e.(s x s)). The net one-site field at a site vanishes for axis and full soldering and is a uniform field on the invariant internal axes for the trivial action and the sign twist. Adding possibility covariance (invariance under every internal rotation) leaves exactly the Heisenberg coupling J s.s = J(2 SWAP - 1) for every action. The Moriya term is odd under the improper inversion, which the axioms do not include. Checked by exact rational nullspaces, lattice-level covariance on the 3x3x3 torus and operator-level covariance on the seven-qubit star. Terms on three or more sites, time dependence and the dynamics clause itself are not derived."
upstream_dependencies:
  - minimal_axioms
  - the_soldering_menu_four_actions_of_the_proper_cubic_rotations_on_qubit_possibilities_and_what_each_lets_formation_build_bounded_theorem_note_2026-09-22
runner: scripts/dynamics_clause_covariant_nearest_neighbour_two_qubit_generators_2026_09_24.py
---

# The covariant nearest-neighbour two-qubit generator

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** exact finite classification under a supplied dynamics clause; unaudited.

## Result and scope

The axioms supply no dynamics. The memo says that Admissibility "is not a
dynamics axiom", and that it does not "choose a Hamiltonian or transfer
operator". Every landed result that moves content therefore supplies its
own generator. Examples are the supplied two-component walk of the
eight-species notes, the clocked walk of the rate-field notes, the finite
clock and Villain laws of the Maxwell-scaling notes, and the stochastic
generators of the mobile-record notes.

This note classifies the smallest candidate dynamics clause. The clause
is a decision point, recorded here and not adopted:

> **(D-dyn)** Between records, the site possibilities evolve under a
> time-independent Hermitian generator that is a sum of two-site terms on
> nearest-neighbour bonds. The generator is covariant under lattice
> translations and under the proper cubic rotations, which act on
> possibilities by one of the four actions of the landed soldering menu.

Within (D-dyn) the covariant generators are few:

- **Full soldering** (the rotations act on the Bloch vector as themselves)
  leaves exactly three couplings on a bond `(x, x+e)`:
  - the Heisenberg term `J s_x.s_{x+e}`;
  - the compass term `K (e.s_x)(e.s_{x+e})`;
  - the Moriya term `D e.(s_x x s_{x+e})`.
  No net one-site field survives.
- **Axis soldering** and the **sign twist** leave four couplings each, and
  the **trivial action** leaves six: any symmetric `M`.
- **Possibility covariance.** The Qubit axiom says "No possibility is
  privileged." Read as invariance under every internal rotation, it
  leaves exactly the Heisenberg coupling for every action, with no field.
  Since `s.s = 2 SWAP - 1`, the Heisenberg term exchanges neighbouring
  possibilities.
- **The Moriya term is handed.** It changes sign under the improper
  inversion. The axioms name proper rotations and no improper ones, so they
  permit it.

Nothing here derives a dynamics from the axioms. The note fixes how much
freedom the smallest local dynamics clause leaves: one coupling under
possibility covariance, three under full soldering.

## Premises and declared objects

- **Axioms** (`docs/MINIMAL_AXIOMS_2026-06-29.md`). Lattice: "Physical
  sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
  adjacency, standard translations, and proper cubic rotations about each
  site." Qubit: "The full one-site possibility domain has algebraic
  presentation `M_2(C)`"; "No possibility is privileged." Admissibility
  "does not choose a Hamiltonian or transfer operator".
- **Actions** (landed soldering-menu note). A homomorphism `rho` from the
  proper cubic group `O` into `SO(3)` acting on the Bloch vector. Up to
  conjugacy there are four: trivial; the sign twist `diag(1, s, s)`, where
  `s` is the sign of the axis permutation; axis soldering `s |g|`; and
  full soldering `g`.
- **Bond data.** A Hermitian two-site term on the bond `(x, y = x+e)` is
  `c + a.s_x + b.s_y + s_x^T M s_y`, where `s` is the Pauli vector.
  - A rotation `R` acts on the data by `(a, b, M) -> (rho(R)a, rho(R)b,
    rho(R) M rho(R)^T)`, and sends direction `e` to `Re`.
  - Reading the same bond from `y` swaps `a` and `b` and transposes `M`.
  - Covariance of the sum over bonds is equivalent to two conditions on
    the data at `+e_z`:
    - invariance under the stabiliser of `+e_z` (the four rotations
      about `z`);
    - the reversal rule under a rotation taking `+e_z` to `-e_z`.
- **Possibility covariance** (an option, not adopted). The generator is
  also invariant under every internal rotation, the same `SU(2)`
  conjugation on all sites together.

## Theorem 1 — covariant bond data

*Statement.*
- The one-site parts `(a, b)` of covariant bond data at `+e_z` form spaces
  of dimension 3, 1, 1, 1 for the trivial action, the sign twist, axis
  soldering and full soldering. In the four cases:
  - trivial: `b = a`, with `a` free;
  - sign twist: `b = a` along the invariant internal axis;
  - axis soldering: `b = a` along `(1, -1, 0)`;
  - full soldering: `b = -a` along `e_z`.
- The two-site couplings `M` form spaces of dimension 6, 4, 4, 3. For the
  trivial action they are exactly the symmetric matrices.
- The two sets of conditions do not couple `(a, b)` with `M`.

*Proof.* The conditions are linear in the 15 real entries of `(a, b, M)`.
The runner computes their nullspaces in exact rational arithmetic for each
action. Stabiliser invariance restricts `a`, `b` and `M` separately. The
reversal rule relates `a` to `b` and `M` to `M^T`. Hence the split. ∎

## Theorem 2 — the net one-site field

*Statement.* The field on a site is the sum of the one-site parts of its
six bonds.
- It is `sum_f rho(R_f) a`, where `R_f` takes `+e_z` to `f`.
- This equals `6 P a`, with `P` the projection onto the vectors fixed by
  every `rho(R)`.
- It vanishes identically for axis and full soldering. For the trivial
  action and the sign twist it is a uniform field on the invariant internal
  axes, of rank 3 and 1.

*Proof.* Averaging over cosets of the stabiliser gives the projection. The
fixed subspaces have dimensions 3, 1, 0, 0. Axis soldering is `A2 + E` and
full soldering is `T1`; neither contains the trivial representation. ∎

A uniform field singles out an internal direction. Possibility covariance
removes it (Theorem 3).

## Theorem 3 — possibility covariance leaves the Heisenberg coupling

*Statement.* With invariance under every internal rotation as well, every
one of the four actions leaves exactly `M = J I`, `a = b = 0`. On a bond,
`J s_x.s_y = J(2 SWAP - 1)`.

*Proof.*
- Invariance under all of `SO(3)` requires `M` to commute with the
  rotation generators. The Bloch representation is irreducible, so by
  Schur's lemma `M` is a multiple of the identity.
- A vector fixed by every rotation is zero, so `a = b = 0`.
- `J I` satisfies the stabiliser and reversal conditions of each action.
- The runner confirms a one-dimensional nullspace for each action, and
  checks the SWAP identity on `C^2 (x) C^2`. ∎

## Theorem 4 — full soldering: three couplings, one of them handed

*Statement.*
- Under full soldering the couplings are exactly
  `span{J I, K e e^T, D [e]}`, where `s_x^T [e] s_y = e.(s_x x s_y)` is the
  antisymmetric (Moriya) part.
- Under the improper inversion `x -> -x`, with spins axial, the Heisenberg
  and compass terms are fixed and the Moriya term changes sign.

*Proof.*
- The stabiliser of `+e_z` under full soldering is the four rotations about
  `e_z`. The matrices commuting with them are `p(I - e e^T) + r e e^T +
  q [e]`. The reversal rule `M_{-e} = M_e^T` holds for all three.
- Inversion maps the bond `(x, x+e)` to `(y+e, y)` with `y = -x-e`, and
  leaves axial spins alone. The symmetric parts are unchanged and the
  antisymmetric part changes sign. The runner checks this on the 3x3x3
  torus. ∎

## Checks

The runner prints fifteen checks in seven families. All pass in about five
seconds.

- **A.** The four actions are homomorphisms into `SO(3)`.
  - Kernel orders are 24, 12, 4, 1, and kernel orbits on the six directions
    are 1, 1, 3, 6. These are the landed soldering-menu values.
  - Fixed-subspace dimensions are 3, 1, 0, 0.
- **B.** Exact nullspaces give one-site dimensions 3, 1, 1, 1 and
  two-site dimensions 6, 4, 4, 3. No basis vector mixes the two parts.
- **C.** Net field ranks are 3, 1, 0, 0.
- **D.** Possibility covariance leaves a one-dimensional space, `M = J I`,
  for every action.
- **E.** Full soldering spans `{I, e e^T, Moriya}` exactly.
- **F.** Lattice-level covariance on the 3x3x3 torus, using coefficient
  tensors and all 24 rotations about a site:
  - every basis element of every family is invariant, with deviation zero;
  - a negative control, a stabiliser-invariant antisymmetric datum that
    breaks the reversal rule, is not;
  - inversion leaves `J` and `K` even and makes the Moriya term odd.
- **G.** Operator-level covariance on the seven-qubit star (a site and its
  six neighbours, `128 x 128`), with `SU(2)` lifts of each action:
  - a random covariant generator of each family commutes with all 24
    lifted rotations, with largest entry `1e-14` and lift error `3e-16`;
  - a random non-covariant bond datum does not;
  - `s.s = 2 SWAP - 1`.

The star check and the torus check use two different implementations: an
operator on the tensor product, and a coefficient tensor under site
permutation. Both use the classified basis from family B.

## What this does not do

- It does not derive a dynamics. (D-dyn) is a decision point. The axioms
  memo lists "record-production dynamics, physical persistence dynamics,
  time metric" among the open gates outside the axioms.
- Terms on three or more sites of a star, such as a scalar chirality
  `s_x.(s_y x s_z)`, are not classified. Neither are time-dependent,
  non-Hermitian or longer-range generators.
- No ground state, phase, excitation or physical identification of any
  coupling is claimed. The sign and size of `J`, `K`, `D` are free.
- Possibility covariance is used as a declared option. The Qubit sentence
  "No possibility is privileged" can also be read as allowing the soldered
  couplings `K` and `D`. The choice is recorded, not made.

## Decision points recorded

- **(D-dyn)** the dynamics clause itself.
- **(D-pc)** possibility covariance, which forces the Heisenberg coupling,
  versus a soldering that keeps the compass and Moriya couplings.

Neither is adopted. Later blocks of the same campaign use (D-dyn) as a
hypothesis and test what it generates: the record law's form, correlations,
clocks and handedness.
