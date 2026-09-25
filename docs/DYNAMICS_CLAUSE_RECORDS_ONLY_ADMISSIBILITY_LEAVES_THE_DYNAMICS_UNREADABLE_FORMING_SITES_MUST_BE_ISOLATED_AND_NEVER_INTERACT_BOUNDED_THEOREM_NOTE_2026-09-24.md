---
claim_id: dynamics_clause_records_only_admissibility_leaves_the_dynamics_unreadable_forming_sites_must_be_isolated_and_never_interact_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "For supplied two-site Pauli dynamics and rank-one record compression: the product-state derivative exposes dependence on an unrecorded neighbour for suitable preparations; an isolated formation order exists exactly for an independent forming set whose neighbours are initially recorded; the compressed Hamiltonian separates into fields on forming sites and a never-recorded subsystem. Product record laws require an additional product stationary preparation. Entangled isolated sites are an explicit counterexample to inferring independence from decoupling. No universal dynamics dichotomy is asserted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/dynamics_clause_records_only_admissibility_leaves_the_dynamics_unreadable_2026_09_24.py
---

# Isolated formation: graph structure, local fields and preparation dependence

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** conditional finite identities and graph theorem; unaudited.

## Supplied model

Use a nearest-neighbour Hamiltonian with Pauli bond coefficient `M_f`, rank-one record compression `P_q=(1+q.s)/2`, tensor-product quantum kinematics, trace probabilities and selective projector updates. These are supplied mathematical conditions, not adopted framework axioms. Partition the finite graph into initial records `R0`, sites that later form `F`, and never-recorded sites `N`. Isolation means that every graph neighbour already carries a record. On the infinite cubic lattice each site has six neighbours; finite open windows use only their declared edges.

## Product-state derivative and its exact scope

For adjacent unrecorded `x,y` and initially factorized states with Bloch vectors `r_x,r_y`, partial tracing the commutator gives

`d r_x/dt = 2 (h_x + M_f r_y) x r_x`.

This is an instantaneous identity; interacting evolution need not remain product. For `M_f != 0`, choose `v` with `M_f v != 0`, take `r_y=+-v/|v|`, and choose a nonzero `r_x` perpendicular to `M_f v`. The derivatives differ. Therefore no universally state-insensitive closure covers all such preparations and all menus. This is not a statement that every state displays that dependence: maximally mixed states and selected stationary states are exceptions. Nor does isolation by itself make odds independent of the site's own preparation. Universal odds for every unrecorded state are impossible even at an isolated site under the trace rule.

The primary runner checks the commutator identity and finite-time separation in ten Heisenberg and ten general soldered cases. These checks complement the algebraic existence argument, not a universal numerical census.

## Graph theorem: when every site can form isolated

An isolated order exists if and only if `F` is independent and `N(F)` is contained in `R0`.

If two sites of `F` were adjacent, the first to form would have an unrecorded neighbour. A neighbour outside `R0` would then be in `F` or in `N`, both excluded. Conversely, if all neighbours are in `R0`, every order works. On an even periodic cubic box, an x-direction perfect matching bounds `|F|<=|V|/2`; the two sublattices attain equality. This does not assume the same equality for odd periodic boxes.

The runner exhausts all 6561 `R0/F/N` labellings of the cube, searches their formation orders, and checks the perfect matching and attaining sublattice on a 4x4x4 torus.

## Compression theorem

Under those graph conditions, every bond touching `F` terminates on a record. The rank-one identity `P_q s_a P_q=q_a P_q` gives

`P H P = sum_{x in F} h_x.s_x + H_N + const`,

on the record subspace, with `h_x=sum_f M_f q_{x+f}` and the transposed coefficient for a bond read backwards. Thus no Hamiltonian term couples `F` to another unrecorded site. The runner checks the full sparse operator on a 12-qubit 2x2x3 window, with two forming sites and an adjacent never-recorded pair.

## Conditional product law and counterexample

Add the preparation `rho=(tensor_{x in F} rho_x) tensor rho_N`, where each `rho_x` is stationary in its field. For nonzero `h_x`, write `rho_x=(1+lam_x hhat_x.s)/2`; if `h_x=0`, any fixed local state is stationary. Its trace odds multiply, are independent of formation times and orders, and do not depend on the supplied `rho_N`. The proof uses both factorized preparation and separated evolution. Commuting local projectors alone establish order independence at a fixed state, not factorization.

A counterexample to omitting preparation is the two-site Bell state `(00+11)/sqrt(2)` on separated isolated sites with Hamiltonian `Z_1+Z_2`. Both z-marginals are stationary and equal to 1/2, but `P(++ )=1/2`, whereas their product is 1/4. This correlation is readable despite no coupling between the sites. Prior entanglement can also make joint records sensitive to measurement times for noncommuting menus. No universal unreadability or isolation-versus-quantum dichotomy survives this example.

The runner's four arbitrary never-recorded states, three times, both orders and all outcomes test the explicitly factorized stationary preparation. An additional Bell-state control tests the missing-preparation counterexample. Its adjacent antiferromagnetic pair check independently retains the singlet correlation `E=-a.b` under the supplied trace rule.

## Boundary

No preparation, relaxation, formation mechanism, physical interpretation, or new axiom is derived. The graph theorem is conditional on imposed isolation; the derivative identity does not prove that physical formation must obey it. The stronger submitted unreadability claim is rejected. Useful local-field and graph arguments remain available with their exact hypotheses.

## Mathematical dependencies and reproduction

- [DYNAMICS_CLAUSE_COVARIANT_NEAREST_NEIGHBOUR_TWO_QUBIT_GENERATORS_HEISENBERG_UNDER_POSSIBILITY_COVARIANCE_THREE_COUPLINGS_UNDER_FULL_SOLDERING_BOUNDED_THEOREM_NOTE_2026-09-24](DYNAMICS_CLAUSE_COVARIANT_NEAREST_NEIGHBOUR_TWO_QUBIT_GENERATORS_HEISENBERG_UNDER_POSSIBILITY_COVARIANCE_THREE_COUPLINGS_UNDER_FULL_SOLDERING_BOUNDED_THEOREM_NOTE_2026-09-24.md)
- [DYNAMICS_CLAUSE_RECORDS_ACT_AS_FIELDS_A_SITE_WITH_SIX_RECORDED_NEIGHBOURS_IS_A_QUBIT_IN_THEIR_FIELD_AND_ITS_LAW_POINTS_ALONG_IT_BOUNDED_THEOREM_NOTE_2026-09-24](DYNAMICS_CLAUSE_RECORDS_ACT_AS_FIELDS_A_SITE_WITH_SIX_RECORDED_NEIGHBOURS_IS_A_QUBIT_IN_THEIR_FIELD_AND_ITS_LAW_POINTS_ALONG_IT_BOUNDED_THEOREM_NOTE_2026-09-24.md)
- [MINIMAL_AXIOMS_2026-06-29](MINIMAL_AXIOMS_2026-06-29.md)

Primary runner: [dynamics_clause_records_only_admissibility_leaves_the_dynamics_unreadable_2026_09_24.py](../scripts/dynamics_clause_records_only_admissibility_leaves_the_dynamics_unreadable_2026_09_24.py). Paired output: [current runner output](../logs/runner-cache/dynamics_clause_records_only_admissibility_leaves_the_dynamics_unreadable_2026_09_24.txt). All numerical historical figures above describe the declared finite setup; current tolerances and diagnostics are in this paired output.

## No-Go Discipline Gate

This section bounds the negative subclaims; it grants neither a retained grade nor an exhaustive search over physical alternatives.

### N1 — Alternative routes

- **ATTEMPTED — Universal state quantifier.** Require identical odds for every preparation, even at an isolated site. Opposite local polarizations refute that premise.
- **ATTEMPTED — Coupled marginal evolution.** Make every local marginal independent of its coupled neighbour. For nonzero M, opposite neighbour vectors and a transverse local vector give different derivatives; special states remain exceptions.
- **ATTEMPTED — Formation order.** Evade the independent-set restriction by choosing a different first site. The earlier endpoint of an edge between proposed forming sites is not isolated.
- **ATTEMPTED — Prior entanglement.** Deduce product probabilities from a decoupled Hamiltonian. An isolated Bell pair has joint ++ probability one half, not one quarter; the broad product claim is rejected.
- **ATTEMPTED — Factorized preparation.** Recover a product law with an explicit tensor-product stationary initial state. This succeeds as a conditional positive theorem; it does not derive that preparation.

These are the actual formulations tested in the argument and controls above. Successful escapes narrow the rejected broader claim; they are not counted as failed physical alternatives.

### N2 — Conditional structure

No count of independent physical walls is asserted. Dynamics, preparation and readout are supplied jointly; implication relations between possible derivations of them remain unresolved. The scoped results use their explicit hypotheses rather than an asserted wall-independence theorem.

### N3 — Hidden assumptions

The stated Hamiltonian, state preparation, record compression and readout are conditional mathematical inputs, not additions to the axioms. Numerical tolerances and finite graph sizes are diagnostics, not exact or thermodynamic proofs.

### N4 — Residual matching

No prior no-go is used to close an additional residual. Linked companion notes supply only their displayed covariance, projector or probability identities. The examples above do not certify other formation laws or physical models.

### N5 — Resolution

- `per_element:` Pauli interaction terms and dependence on a neighbour state are tested.
- `per_site:` Isolated local fields are tested without a universal preparation selector.
- `per_mode:` checked and not executed — no momentum-mode or continuum no-go is claimed.
- `per_block:` Finite formation graphs and an initially entangled isolated pair are tested.
- `lattice_wide:` checked and not executed — no universal unreadability or product law is established.

### N6 — Partial closure

Choosing the stated supplied model yields the conditional theorem without adopting a new axiom. A convention cannot by itself select its state, dynamics or probability law. No claim that a new axiom is necessary is made.

### N7 — Strongest counter-route

Prepare isolated sites in an entangled Bell state before decoupling. Their joint measurements remain correlated and can depend on noncommuting measurement times. This explicitly refutes universal unreadability, so the note retains only the graph theorem and a product-law theorem with an actual factorized stationary preparation.

### N8 — Related work

The linked companion sources are the relevant nearby arguments rechecked for this result. Their conditional boundaries are preserved here. Similar wording or a prior finite computation does not supply a universal obstruction.
