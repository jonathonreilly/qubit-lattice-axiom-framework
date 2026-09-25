---
claim_id: dynamics_clause_records_act_as_fields_a_site_with_six_recorded_neighbours_is_a_qubit_in_their_field_and_its_law_points_along_it_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Conditional on three supplied clauses that are recorded and not adopted - a covariant nearest-neighbour two-qubit generator (D-dyn, classified in the supplied companion construction), record permanence modelled as compression onto record projectors P_q = (1 + q.s)/2 (D-perm), and odds read from the site's state by the trace rule (D-tr) - the following are exact. (i) P_q s P_q = q P_q, so each bond to a recorded neighbour acts on an unrecorded site as the field M_f q. (ii) A site whose six neighbours carry records evolves as one qubit in h(N) = sum_f M_f q_f, decoupled from every other unrecorded site. (iii) If its odds are a function of the neighbour records alone, not of elapsed time or of its own earlier state, for nonzero h, the state they are read from lies on the stationary line rho = (1 + lam h^.s)/2, and the odds on every antipodal menu are (1 + lam p.h^)/2. (iv) Under the Heisenberg coupling h^ is along the resultant of the six records. With one effective neighbour the odds are the landed affine class f(t) = (1 + c t)/2 with c = lam sgn J; ground-state relaxation gives c = 1 for J < 0 (repeat certainty) and c = -1 for J > 0; thermal relaxation gives |c| = tanh(beta|J|). The landed non-affine witnesses are not trace readings of any state. (v) Full soldering gives h = J sum q_f + K sum f(f.q_f) + D sum q_f x f. (vi) With one unrecorded neighbour, stationary states with the same records give different odds, and ground-state odds change with records two steps away. The clauses, the relaxation profile lam and the formation site, time and rate are not derived."
upstream_dependencies:
  - minimal_axioms
  - menus_and_born_stabilizer_degenerate_supports_antipodal_weight_class_and_non_affine_witness_bounded_theorem_note_2026-09-22
runner: scripts/dynamics_clause_records_act_as_fields_isolated_site_law_2026_09_24.py
---

# Records act as fields: a site with six recorded neighbours is a qubit in their field, and its law points along it

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** exact finite results under three supplied clauses; unaudited.

## Result and scope

the supplied constructions classified the smallest local dynamics clause. On a
nearest-neighbour bond it allows the Heisenberg coupling alone under
possibility covariance, and three couplings under full soldering. This
note asks what such a dynamics does to the law of a forming record, once
records are permanent.

The answer is simple:
- **Records act as fields.** A recorded neighbour enters the dynamics through
  its content alone. Each bond to a record becomes a fixed field on the
  unrecorded site.
- **An isolated site is a qubit in a field.** When all six neighbours carry
  records, the site is exactly one qubit in the field `h(N)` of their
  contents. It is decoupled from every other unrecorded site.
- **The law points along the field.** Suppose the odds are to depend on the
  neighbour records alone, as the Admissibility sentence says. Then they
  cannot depend on how long ago those records formed, so they are read from
  a stationary state. For nonzero `h(N)`, every stationary state lies on the line along that field.
  The odds on a menu `{p, -p}` are therefore `(1 + lam p.h^)/2`. The
  length `lam` is what remains open.
- **The landed Born decision points relocate.** The landed menus-and-Born
  note recorded two decision points: affinity in the neighbour state, and
  same-label repeat certainty. Here, with one effective neighbour, the odds
  are its affine class `(1 + c t)/2` with `c = lam sgn J`.
  - Repeat certainty `c = 1` is obtained by ground-state relaxation with a
    ferromagnetic coupling `J < 0`.
  - An antiferromagnetic coupling gives the anti-Born flip `c = -1`.
  - Thermal relaxation gives `|c| = tanh(beta|J|)`.
  - The two landed non-affine witnesses are exactly laws that no state gives
    by the trace rule.
- **Limit of scope.** A site with an unrecorded neighbour is not a qubit in
  a field. Its odds then depend on the unrecorded neighbour's state, and
  through it on records two steps away. With a separately selected stationary preparation profile this gives a records-only law at isolated sites. The non-isolated examples demonstrate failure of universal closure, not failure for every state or coupling.

## Premises and declared objects

- **Axioms** (`docs/MINIMAL_AXIOMS_2026-06-29.md`).
  - Record: "When present, a record locks exactly one admissible local
    possibility. A site never carries more than one record; records are
    permanent."
  - Admissibility: "For each site, the probability distribution over the
    possibilities is determined by, and varies with, the nearest-neighbor
    conditions."
  - The memo's reading note: "the law supplies the odds; the realized state
    supplies the pick."
- **(D-dyn), supplied, not adopted.** The covariant nearest-neighbour
  two-qubit generator of the supplied companion construction, `H = sum_bonds s_x^T M_f s_{x+f}`.
  - Heisenberg: `M_f = J I`.
  - Full soldering: `M_f = J I + K f f^T + D [f]`, where
    `s^T [f] t = f.(s x t)`.
- **(D-perm), supplied, not adopted.** A record locking the pure possibility
  with Bloch vector `q` is the projector `P_q = (1 + q.s)/2`. Permanence is
  modelled by compressing the generator onto the record subspace, `P H P`.
  This is the generator seen by a record that is never disturbed, for
  example in the limit of repeated confirmation.
- **(D-tr), supplied, not adopted.** Odds are read from the site's state
  `rho` by the trace rule, `w(p) = Tr(P_p rho)`.
- **Menus.** Antipodal menus `{p, -p}`, as in the landed menus-and-Born
  note. On the full sphere, the trace rule gives the Husimi density
  `1 + lam a.h^` with respect to the uniform measure.

## Theorem 1 — records act as fields

*Statement.* `P_q s_a P_q = q_a P_q` for every unit `q`. Hence for a bond
between an unrecorded site `x` and a recorded site `y`,

`(1 (x) P_q) s_x^T M s_y (1 (x) P_q) = (M q).s_x (x) P_q`.

A bond between two recorded sites compresses to a constant. A bond
between two unrecorded sites is unchanged.

*Proof.* Pauli algebra. The runner checks it symbolically on the unit
sphere, and numerically for 50 random `q`. ∎

## Theorem 2 — an isolated site is a qubit in the field of its neighbours

*Statement.* Let every neighbour of `x` carry a record, with contents
`q_f`. The compressed generator acting on `x` is `h(N).s_x`, where
`h(N) = sum_f M_f q_f`. No term couples `x` to any other unrecorded
site.

*Proof.* In `Z^3` the bonds at `x` are the six bonds to its neighbours.
Theorem 1 turns each into the field `M_f q_f`. Every other bond avoids `x`.

The runner checks both steps:
- on the seven-qubit star, `P H P = (h(N).s_0) (x) P_N` for 12 random
  Heisenberg and `(J, K, D)` cases;
- on an eight-qubit cross (`x`, its six neighbours, and a site `y` beyond
  one of them), with deviation `4.7e-16`, the compressed generator is
  `h_x.s_x + h_y.s_y`, with no coupling between `x` and `y`. ∎

## Theorem 3 — odds that depend on the records alone point along the field

*Statement.* Let the site be isolated from time 0, with some state `rho_0`.
Suppose the odds on every antipodal menu, read by (D-tr), are the same whatever the
elapsed time before formation. Then `rho_0` commutes with `h(N).s`. So
when `h(N) != 0`, `rho_0 = (1 + lam h^.s)/2` for some `lam` in `[-1, 1]`.
The odds on every antipodal menu are

`w(p | N) = (1 + lam p.h^)/2`.

Selecting `lam` as a function of `N` is an additional preparation rule. It is not supplied by stationarity: different stationary states with the same field have different odds.

For uniform averaging over whole precession periods (or the Cesaro long-time average), the effective state is the time average instead. An arbitrary phase-independent waiting-time distribution need not remove transverse components. This also lies
on the line, with `lam = r_0.h^`.

*Proof.*
- The trace against every projector determines a qubit state, so
  time-independent odds force a time-independent state.
- The commutant of `h.s` in the Hermitian `2 x 2` matrices is spanned by
  `1` and `h^.s`.
- The time average of the precession about `h^` keeps the component of
  the Bloch vector along `h^` and removes the transverse part.

The runner checks the commutant for 20 random fields, and the time average
of random states over one period to `2e-15`. ∎

This is where the dynamics does its work. Covariance alone lets the site's
state be any covariant function of the six records. Stationarity under the
record-projected dynamics puts it on one line, the line of the field.

## Theorem 4 — the Heisenberg law and the landed affine class

*Statement.* Under the Heisenberg coupling, `h(N) = J S` with
`S = sum_f q_f` the resultant of the six records. So the odds are
`(1 + lam sgn(J) p.S^)/2`.

Suppose the resultant reduces to one effective neighbour, as when the
other five records sum to zero (a planar regular pentagon is an example).
Then with `t = p.q_1` the odds are the landed affine class
`f(t) = (1 + c t)/2` with `c = lam sgn J`. In particular:
- **Ground-state relaxation.** `f(t) = (1 + t)/2` for `J < 0`, which is
  repeat certainty `f(1) = 1`. For `J > 0` it is `f(t) = (1 - t)/2`.
- **Thermal relaxation** at inverse temperature `beta`, `J < 0`:
  `f(t) = (1 + tanh(beta|J|) t)/2`, affine at every `beta`.
- **The landed non-affine witnesses** `(1 + t^3)/2` and
  `(1 + t)/2 + t(1 - t^2)/8` have degree 3 in `t`. Every state gives degree
  at most 1 by the trace rule. So neither can be read from any state.

*Proof.*
- For a Hamiltonian `h.s`, the ground state has Bloch vector `-h^`, and
  the thermal state has `-tanh(beta|h|) h^`.
- The runner builds the pentagon configuration, and checks the ground
  states for `J = -1.3` and `0.8` and the thermal states at three values
  of `beta`. The largest deviation is `2e-16`.
- The degrees and the midpoint values `9/16`, `51/64` (against the affine
  `3/4`) are exact. ∎

**What this does to the landed decision points.** The landed note recorded
affinity and repeat certainty as separating decision points. Under the
three clauses here:
- **Affinity** is the trace rule, (D-tr). A state gives the odds, and a
  state's odds are affine.
- **Repeat certainty** is ferromagnetic ground-state relaxation.

The decisions are relocated rather than removed. They are now statements
about the dynamics and the site's state, not about the weights directly.

## Theorem 5 — the field of six records under full soldering

*Statement.* Under full soldering,

`h(N) = J sum_f q_f + K sum_f f (f.q_f) + D sum_f q_f x f`.

The Moriya part turns the field away from the resultant. At `D/J = 0.8`,
for one random configuration, the turn is `21.7` degrees.

*Proof.* `[f] q = q x f` for the matrix with `s^T [f] t = f.(s x t)`. The
runner checks the formula against the compressed generator in 20 random
cases, to `9e-16`. ∎

The handed coupling of the supplied companion construction therefore enters the law directly. The
odds at a site point along a direction twisted, in a definite sense, away
from the resultant of its neighbours' records.

## Theorem 6 — the limit: a site with an unrecorded neighbour

*Statement.* Let `x` and `y` be adjacent, both unrecorded, with every
other neighbour of each carrying a record. Under the Heisenberg coupling
(`J = -1`):
- the four stationary states of the pair, with the same records, give odds
  `0.013, 0.709, 0.332, 0.946` at `x` on one menu;
- if `x`'s other five records cancel, the ground-state odds at `x` range
  from `0.105` to `0.896` over six draws of `y`'s other records. Those
  records are two steps from `x`.

So under these clauses, the odds at a site with an unrecorded neighbour are
not a function of its neighbour records. These examples require extra state information if one keeps their supplied quantum model; they do not choose a framework interpretation.

*Proof.* Exact diagonalisation of the two-qubit Hamiltonian
`J s_x.s_y + h_x.s_x + h_y.s_y`. The runner prints the values. ∎

## Checks

The runner prints twelve checks in eight families, and all pass in under a
second:
- **A.** Projection lemma, symbolic and numeric.
- **B.** Compression on the seven-qubit star.
- **C.** Isolation on the eight-qubit cross.
- **D.** The stationary line, and time averages.
- **E.** Odds on 200 random menus, and the normalisation of the Husimi
  density.
- **F.** Ground and thermal laws with one effective neighbour, and the
  exclusion of the non-affine witnesses.
- **G.** The full-soldering field formula, and the Moriya turn.
- **H.** The two scope counterexamples.

## What this does not do

- **No clause is derived.** (D-dyn), (D-perm) and (D-tr) are supplied.
  Record permanence is modelled by compression, and other models of a
  permanent record are not treated.
- **The relaxation profile `lam` is not derived.** Ground-state and thermal
  values are shown as cases. The formation site, time and rate are not
  treated.
- **Non-isolated sites** are covered by the counterexamples of Theorem 6
  and nothing more. No law for them is proposed.
- **No physical reading.** Nothing is claimed about the physical sign of
  `J`, or about ferromagnetism, magnetism or temperature. Those words name
  the mathematical cases.

## Decision points recorded

- **(D-dyn)** the dynamics clause (the supplied companion construction).
- **(D-perm)** permanence as compression onto record projectors.
- **(D-tr)** odds read from the site's state by the trace rule. Under the
  other clauses it replaces the landed affinity clause.
- **(D-relax)** the relaxation profile `lam`. With `J < 0`, ground-state
  relaxation replaces the landed repeat-certainty clause.

None is adopted.

## Degenerate and preparation boundaries

For `h=0`, every qubit state is stationary and no field direction is defined. For `h!=0`, the parameter in this note is the signed component `lam=r.h^`; ground-state preparation has `lam=-1` and thermal preparation has `lam=-tanh(beta|h|)`. Thus `c=lam sgn(J)`. Saturation `c=1` by itself does not determine a physical relaxation mechanism; it also admits an excited aligned preparation for the opposite sign. A single field-aligned menu has time-independent odds even for a precessing nonstationary state, so the stationarity implication requires all menus. The sphere density is an additional continuous measurement convention, with normalization following from the zero uniform spherical mean of the vector, not a new framework probability postulate.

## Mathematical dependencies and reproduction

- [DYNAMICS_CLAUSE_COVARIANT_NEAREST_NEIGHBOUR_TWO_QUBIT_GENERATORS_HEISENBERG_UNDER_POSSIBILITY_COVARIANCE_THREE_COUPLINGS_UNDER_FULL_SOLDERING_BOUNDED_THEOREM_NOTE_2026-09-24](DYNAMICS_CLAUSE_COVARIANT_NEAREST_NEIGHBOUR_TWO_QUBIT_GENERATORS_HEISENBERG_UNDER_POSSIBILITY_COVARIANCE_THREE_COUPLINGS_UNDER_FULL_SOLDERING_BOUNDED_THEOREM_NOTE_2026-09-24.md)
- [MINIMAL_AXIOMS_2026-06-29](MINIMAL_AXIOMS_2026-06-29.md)
- [MENUS_AND_BORN_STABILIZER_DEGENERATE_SUPPORTS_ANTIPODAL_WEIGHT_CLASS_AND_NON_AFFINE_WITNESS_BOUNDED_THEOREM_NOTE_2026-09-22](MENUS_AND_BORN_STABILIZER_DEGENERATE_SUPPORTS_ANTIPODAL_WEIGHT_CLASS_AND_NON_AFFINE_WITNESS_BOUNDED_THEOREM_NOTE_2026-09-22.md)

Primary runner: [dynamics_clause_records_act_as_fields_isolated_site_law_2026_09_24.py](../scripts/dynamics_clause_records_act_as_fields_isolated_site_law_2026_09_24.py). Paired output: [current runner output](../logs/runner-cache/dynamics_clause_records_act_as_fields_isolated_site_law_2026_09_24.txt). All numerical historical figures above describe the declared finite setup; current tolerances and diagnostics are in this paired output.

## No-Go Discipline Gate

This section bounds the negative subclaims; it grants neither a retained grade nor an exhaustive search over physical alternatives.

### N1 — Alternative routes

- **ATTEMPTED — Rank-one compression.** Keep a quantum neighbour operator after a record. The projector identity reduces it to its supplied content.
- **ATTEMPTED — State stationarity.** Infer stationarity from just one menu. A transverse precessing state keeps field-menu odds fixed; only all-menu stationarity has the stated implication.
- **ATTEMPTED — Signed polarization.** Replace the signed coupling by its magnitude. Direct traces give c=lam*sgn(J), including positive lam; the opposite sign is rejected.
- **ATTEMPTED — Menu functional form.** Obtain the displayed non-affine menu witnesses from one fixed qubit density matrix. A trace against an antipodal projector is affine, so this route fails within that specified representation.
- **ATTEMPTED — Nonisolated preparation.** Treat neighbouring records as a universal selector of a pair state. Distinct pair preparations give distinct local odds; no universal selection claim survives.

These are the actual formulations tested in the argument and controls above. Successful escapes narrow the rejected broader claim; they are not counted as failed physical alternatives.

### N2 — Conditional structure

No count of independent physical walls is asserted. Dynamics, preparation and readout are supplied jointly; implication relations between possible derivations of them remain unresolved. The scoped results use their explicit hypotheses rather than an asserted wall-independence theorem.

### N3 — Hidden assumptions

The stated Hamiltonian, state preparation, record compression and readout are conditional mathematical inputs, not additions to the axioms. Numerical tolerances and finite graph sizes are diagnostics, not exact or thermodynamic proofs.

### N4 — Residual matching

No prior no-go is used to close an additional residual. Linked companion notes supply only their displayed covariance, projector or probability identities. The examples above do not certify other formation laws or physical models.

### N5 — Resolution

- `per_element:` Rank-one Pauli compression and signed trace odds are tested.
- `per_site:` Isolated-site stationary states and finite menu probabilities are tested.
- `per_mode:` checked and not executed — no momentum-mode or continuum statement is claimed.
- `per_block:` Recorded-star compression and supplied coupled-pair examples are tested.
- `lattice_wide:` checked and not executed — no lattice-wide preparation or relaxation law is derived.

### N6 — Partial closure

Choosing the stated supplied model yields the conditional theorem without adopting a new axiom. A convention cannot by itself select its state, dynamics or probability law. No claim that a new axiom is necessary is made.

### N7 — Strongest counter-route

A precessing transverse state has constant odds on the field menu, and an excited preparation can realize same-label certainty for the other coupling sign. These concrete routes defeat inference of stationarity from one menu and inference of a unique relaxation mechanism. The theorem uses every menu and labels preparation separately; a records-only law still requires an explicit selector for lam.

### N8 — Related work

The linked companion sources are the relevant nearby arguments rechecked for this result. Their conditional boundaries are preserved here. Similar wording or a prior finite computation does not supply a universal obstruction.
