---
claim_id: dynamics_clause_records_only_admissibility_leaves_the_dynamics_unreadable_forming_sites_must_be_isolated_and_never_interact_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Under three supplied clauses, not adopted: the covariant nearest-neighbour two-qubit dynamics clause of open PR 9040, permanence as compression onto record projectors, and the trace rule (open PR 9041). Records-only admissibility means that the odds of every forming record are fixed by its six neighbour records whatever the state of the unrecorded sites. (1) With a nonzero bond coupling, a site that forms beside an unrecorded neighbour has odds that depend on that neighbour's state, exactly through d r_x/dt = 2 (h_x + M r_y) x r_x; so records-only admissibility requires every site to form isolated. (2) An order in which every forming site is isolated when it forms exists exactly when the forming set F is independent and every neighbour of F is initially recorded (all 6561 labellings of the cube graph and all orders). On a 4x4x4 torus, F has at most 32 of 64 sites, attained by a sublattice with the other initially recorded. (3) The record-projected generator is then a sum of fields on the forming sites plus terms on never-recorded sites, with nothing coupling a forming site to any other unrecorded site (12-qubit window). (4) The joint odds of the forming records are the product of their isolated-site laws, independent of formation order, time and the state and evolution of never-recorded sites. So records-only admissibility leaves no readable consequence of the dynamics beyond the fields of the initial records. Readable interaction requires a site to form beside an unrecorded neighbour, whose state then enters its odds."
upstream_dependencies:
  - minimal_axioms
runner: scripts/dynamics_clause_records_only_admissibility_leaves_the_dynamics_unreadable_2026_09_24.py
---

# Records-only admissibility leaves the dynamics unreadable

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** exact results under supplied clauses; unaudited.

## Result and scope

The Admissibility sentence says that a site's distribution "is determined
by, and varies with, the nearest-neighbor conditions". One reading takes
those conditions to be the neighbours' records alone. The campaign's earlier
blocks found two consequences of the local dynamics clause:
- A site with an unrecorded neighbour has odds that depend on that
  neighbour's state (open PR 9041).
- The quantum correlation value needs such states (open PR 9043).

This note asks what happens if records-only admissibility is imposed
anyway, together with the dynamics clause. The answer is a dichotomy.

- **Records-only admissibility forces isolation.** With any nonzero
  coupling, a site that forms beside an unrecorded neighbour has odds that
  depend on that neighbour's state. The dependence already appears in the
  first time derivative of the site's Bloch vector. So every record must
  form while all six of its neighbours already carry records.
- **Isolation forces a thin, one-layer history.**
  - Two adjacent sites cannot both form: whichever forms first has the
    other as an unrecorded neighbour.
  - So the sites that form are an independent set, and every neighbour of
    one of them was recorded from the start.
  - On a cubic torus at most half the sites can form. That is attained when
    one sublattice forms and the other is the initial record set.
- **The dynamics becomes unreadable.**
  - A forming site is a qubit in the field of its initial neighbours,
    coupled to no other unrecorded site.
  - Never-recorded sites may interact among themselves, but they touch no
    forming site.
  - The joint odds of every record that forms are a product of isolated-site
    laws. They are the same in every order, at every time, and for every
    state of the never-recorded sites.
  - Only records are readable, so nothing readable carries any trace of the
    dynamics beyond the fields of the initial records.

So under the local dynamics clause, readable interaction, propagation and
the quantum correlation value all need the other reading. Some sites must
form beside unrecorded neighbours, whose quantum states then enter the
"nearest-neighbor conditions".

## Premises and declared objects

- **Axioms** (`docs/MINIMAL_AXIOMS_2026-06-29.md`).
  - Admissibility, quoted above.
  - Record: "records are permanent. Only records are readable. A readout
    value is determined by record content alone."
- **Supplied clauses, not adopted.**
  - The covariant nearest-neighbour two-qubit generator of open PR 9040.
    On the bond from `x` in direction `f` it acts as `s_x^T M_f s_{x+f}`.
  - Permanence as compression onto record projectors.
  - The trace rule (open PR 9041).
- **Records-only admissibility.** The odds of each forming record are a
  function of the contents at its six neighbours. They are the same for
  every state of the unrecorded sites.
- **A formation process.** An initial record set `R0`, a set `F` of sites
  that form one at a time in some order, and never-recorded sites `N`.
  - A forming site is *isolated* if every neighbour carries a record when
    it forms.

## Theorem 1 — records-only admissibility forces isolation

*Statement.* Let site `x` have an unrecorded neighbour `y` in direction `f`,
with `M_f != 0`, and every other neighbour of `x` and `y` recorded. Then

`d r_x / dt = 2 (h_x + M_f r_y) x r_x`

at a product state with Bloch vectors `r_x`, `r_y`. Here `h_x` is the
field of `x`'s recorded neighbours. So two states of `y`, with every
record the same, give different evolutions of `x`, and in general
different odds.

*Proof.*
- The compressed generator of the pair is
  `s_x^T M_f s_y + h_x.s_x + h_y.s_y` (open PR 9041).
- Tracing out `y` from `[H, rho_x (x) rho_y]` gives the field
  `h_x + M_f r_y` on `x`.
- The runner checks the derivative formula exactly, for ten Heisenberg and
  ten random `(J, K, D)` cases. It also checks that two random states of
  `y` give Bloch vectors at `x` that differ by at least `0.215` after time
  `0.3`, in every case.

If the unrecorded site is instead held in a fixed relaxed state, open PR
9041 showed that its odds depend on records two steps away. Either way the
odds are not fixed by the six neighbour records. ∎

## Theorem 2 — isolated formation needs an independent forming set

*Statement.* An order in which every forming site is isolated exists
exactly when:
- `F` is independent, with no two forming sites adjacent;
- every neighbour of every forming site is in `R0`.

On a periodic cubic box of even side, `|F| <= |V|/2`. The bound is attained
by a sublattice, with the other sublattice in `R0`.

*Proof.*
- If `u, v` in `F` are adjacent, whichever forms first has the other
  unrecorded.
- If a neighbour of `u` in `F` is not in `R0`, it lies in `F` (excluded
  above) or in `N`, so it is never recorded.
- Conversely, under both conditions every order works.
- A perfect matching (the `x`-bonds from even `x`-coordinates) allows at
  most one site of `F` per matched bond.

The runner checks the equivalence on the cube graph over all `3^8 = 6561`
assignments of sites to `R0`, `F`, `N` and all orders of `F`. It also
checks the matching and the sublattice on the 4x4x4 torus. ∎

## Theorem 3 — isolated forming sites interact with nothing

*Statement.* Under the conditions of Theorem 2, the record-projected
generator is

`sum_{x in F} h_x.s_x + H_N + const`.

Here `h_x = sum_f M_f q_{x+f}` is the field of `x`'s initial neighbours,
and `H_N` acts on never-recorded sites alone. No term couples a forming
site to any other unrecorded site.

*Proof.* Every bond at a forming site ends on a record. By open PR 9041
each such bond compresses to a field. Bonds between records are constants,
and the remaining bonds join never-recorded sites. The runner checks this
on a 2x2x3 window: 12 qubits, sparse, random `(J, K, D)`, two forming
sites and an adjacent never-recorded pair. The largest deviation is
`8e-16`. ∎

## Theorem 4 — nothing readable depends on the dynamics

*Statement.* Under the conditions of Theorem 2, suppose each forming site's
odds satisfy records-only admissibility. Then they are its isolated-site law
`(1 + lam_x p.h^_x)/2` (open PR 9041). The joint odds of all forming records
are the product of these laws. They do not depend on:
- the formation order;
- the times of formation;
- the state or evolution of the never-recorded sites.

*Proof.*
- By Theorem 3 the forming sites evolve independently of each other and of
  `N`.
- By open PR 9041 their odds are read from states on their stationary
  lines.
- Single-site projectors on different sites commute, so sequential
  readout in either order gives the product.

The runner checks the product law against the full evolution of two
forming sites and an interacting never-recorded pair. It uses four random
pair states, three times and all outcomes, with largest deviation `8e-16`,
and both formation orders. ∎

## Consequence — a dichotomy

Under the local dynamics clause, one of two things holds:
1. **Records-only admissibility holds.** Then the history readable from
   records is the initial record set plus one layer of conditionally
   independent records on an independent set. No interaction between
   unrecorded sites leaves a readable trace. The formation order is
   invisible.
2. **Some site forms beside an unrecorded neighbour.** Its odds then depend
   on that neighbour's quantum state, which the dynamics has shaped. In this
   branch the records can show readable dynamics. For example, the
   correlated singlet odds `E = -a.b` of an adjacent pair, checked in
   family E, and the value `2 sqrt 2` of open PR 9043.

The landed formation notes reduce "how records form" to which neighbours
are already written when a site is written. Under records-only
admissibility and this dynamics clause, the answer is forced: all six.
That forces the one-layer history of branch 1.

## Checks

The runner prints eight checks in five families. All pass in about three
seconds.
- **A.** The derivative formula, and the state dependence.
- **B.** The cube-graph equivalence, and the torus bound.
- **C.** The 12-qubit decoupling.
- **D.** The product law, and order independence.
- **E.** The singlet and its correlated odds.

## What this does not do

- It does not choose between the two branches. The reading of
  "nearest-neighbor conditions" is recorded as a decision point.
- It covers the two-site dynamics clause of open PR 9040. Terms on three
  or more sites, and non-local or time-dependent generators, are not
  treated.
- The initial record set is supplied: a past hypothesis. Its size bound is
  exact on the stated tori.
- No physical reading is claimed for either branch.

## Decision points recorded

- **(D-nn)** Whether the Admissibility conditions are records alone
  (branch 1) or include the states of unrecorded neighbours (branch 2).
- (D-dyn), (D-perm) and (D-tr), as in open PRs 9040 and 9041.

None is adopted.
