---
claim_id: dynamics_clause_moriya_handedness_is_a_twist_with_curvature_gauged_along_a_line_not_in_three_dimensions_and_seen_in_records_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "For the fully soldered dynamics clause of the supplied companion construction, supplied and not adopted, with bond term J s1.s2 + K (e.s1)(e.s2) + D e.(s1 x s2): (1) J s1.s2 + D e.(s1 x s2) = V [A (in-plane) + J (along e)] V^dag with A = sqrt(J^2 + D^2), V = exp(-i phi e.s2/2) and phi = atan2(D,J), with (J,D) != (0,0), exact for bonds along x, y and z. (2) A periodic J-D ring along e has exactly the spectrum of the XXZ ring whose closing bond carries the total turn N phi (N = 5, 6, 7). Twisted and untwisted bonds have equal spectra on a straight open chain. (3) Where bond directions meet they do not: the plaquette holonomy of turns about two axes is a nonzero rotation for 0 < phi < pi (20.74 degrees at D/J = 0.7), and twisted and untwisted spectra differ on a bent chain and on the open cube, so no unitary relates them there. (4) The two-site ground state (J > 0) gives record correlations on antipodal menus with E(a,b) - E(b,a) = -2 sin(phi) (a x b).e, odd in D; its CHSH maximum stays 2 sqrt 2. (5) On the open cube with J = 1, K = 0.3, D = 0.5 the ground state's mean bond vector chirality is -0.4585, odd in D, and the improper inversion maps H(D) to H(-D). No physical parity or weak-interaction reading is claimed."
upstream_dependencies:
  - minimal_axioms
runner: scripts/dynamics_clause_moriya_handedness_is_a_twist_with_curvature_2026_09_24.py
---

# The Moriya coupling's handedness is a twist with curvature

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** exact finite results for a supplied dynamics clause; unaudited.

## Result and scope

The Lattice axiom names "proper cubic rotations about each site" and no
improper ones. the supplied constructions found the consequence for a local dynamics
clause: full soldering admits the Moriya coupling `D e.(s_x x s_y)`, which
the improper inversion would forbid, since it changes the coupling's sign.
This note asks what that handedness is, and whether records can see it.

- **A Moriya bond is a turned XXZ bond.** `J s1.s2 + D e.(s1 x s2)` is an
  XXZ bond seen through a frame turned about the bond axis by `phi`, where
  `phi = atan2(D,J), with (J,D) != (0,0)`. The XXZ bond has in-plane strength `sqrt(J^2 + D^2)` and
  strength `J` along the axis.
- **Along a straight line the turn is a gauge.** Cumulative frame turns
  remove every twist of a straight chain. On a ring they leave one total
  turn `N phi` on the closing bond, as a twisted boundary.
- **Where directions meet it is not.** Turns about two different axes do
  not commute. The holonomy around a plaquette is a nonzero rotation, and
  each turn also moves the anisotropy axes of the other bond directions.
  On a bent chain and on the cube, the twisted and untwisted models have
  different spectra, so no unitary maps one to the other there. These finite supplied models are not related to the specified untwisted comparators by a unitary; no universal claim about all three-dimensional graphs follows.
- **Records see it.** For the twisted pair's ground state, correlations of
  records on antipodal menus have an antisymmetric part
  `E(a,b) - E(b,a) = -2 sin(phi) (a x b).e`. This is parity-odd and changes
  sign with `D`. The Bell value stays `2 sqrt 2`.
- **Handed ground states.** On the cube, the ground state's mean bond
  vector chirality is `-0.4585` at `D = 0.5` and `+0.4585` at `D = -0.5`.
  The improper inversion maps one Hamiltonian exactly onto the other.

So the axioms' symmetry content permits a handed local dynamics. The stated finite examples distinguish it from the specified untwisted comparator, and the supplied trace statistics detect its sign.

## Premises and declared objects

- **Axioms** (`docs/MINIMAL_AXIOMS_2026-06-29.md`). Lattice: "proper cubic
  rotations about each site".
- **Supplied, not adopted.** The fully soldered bond term of the supplied companion construction,
  `J s1.s2 + K (e.s1)(e.s2) + D e.(s1 x s2)` on the bond `(x, x+e)`. The
  improper inversion maps `D` to `-D` and fixes `J` and `K` (the supplied constructions).
- **Frame turns.** `R_e(phi)` is the rotation about `e` by `phi`. On a
  qubit it is implemented by `exp(-i phi e.s/2)`.
- **Records and menus.** Antipodal menus and the trace rule, as in the supplied constructions.
- **Vector chirality of a bond.** `f.(s_x x s_{x+f})`, a pseudoscalar under
  the inversion.

## Theorem 1 — a Moriya bond is a turned XXZ bond

*Statement.* For a bond along `e`, with `A = sqrt(J^2 + D^2)` and
`phi = atan2(D,J), with (J,D) != (0,0)`,

`J s1.s2 + D e.(s1 x s2) = V [A (s1.s2 - (e.s1)(e.s2)) + J (e.s1)(e.s2)] V^dag`,

where `V = exp(-i phi e.s2/2)`.

*Proof.* Exact symbolic identity for `e` = x, y, z, checked by the runner.
The in-plane part `A (cos phi (s1.s2)_perp + sin phi e.(s1 x s2))` is a
rotation of the in-plane Heisenberg form by `phi` about `e`. The
component along `e` is untouched. ∎

## Theorem 2 — along a straight line the twist is a gauge

*Statement.*
- A periodic ring of `N` sites along `e`, with bond term
  `J s.s + D e.(s x s)`, has exactly the spectrum of the XXZ ring whose
  closing bond is turned by `N phi` about `e`.
- On a straight open chain, the twisted and untwisted spectra are equal.

*Proof.* Theorem 1 with cumulative turns `exp(-i n phi e.s_n/2)`. These
commute with the anisotropy along `e`. The runner checks `N = 5, 6, 7`
(largest eigenvalue difference `3e-14`) and the straight 5-site open chain
(`6e-15`). ∎

## Theorem 3 — where directions meet, it is not a gauge

*Statement.*
- For `0 < phi < pi`, the plaquette holonomy
  `R_x(phi) R_y(phi) R_x(-phi) R_y(-phi)` is a nonzero rotation. It is
  `20.74` degrees at `D/J = 0.7`.
- At J=1, D=0.7, the twisted and specified untwisted models have different numerically computed spectra on a bent open
  chain with bonds along x, y, z, x (largest difference `0.085`), and on the
  open cube (`0.779`).

Thus at these tested parameters the spectra exclude unitary equivalence to the specified untwisted comparison; arbitrary untwisted targets are not classified.

*Proof.* In the SU(2) quaternion lift of the commutator the scalar part is `1-2 sin(phi/2)^4`. For `0<phi<pi` this lies strictly between -1 and 1, so the SO(3) rotation is not identity. The endpoints 0 and pi give identity. The grid of 60 values is a numerical check of this algebra, not its proof.
- A frame turn about `e` untwists the bonds along `e`. It also turns the
  anisotropy axes of the bonds along the other directions.
- Around a plaquette the turns fail to close.
- Equal spectra are necessary for unitary equivalence, and the runner shows
  they are not equal. ∎

## Theorem 4 — records see the handedness

*Statement.* For `J > 0`, the ground state of the pair
`J s1.s2 + D e.(s1 x s2)` gives, on antipodal menus `{+-a}` and `{+-b}`,

`E(a,b) - E(b,a) = -2 sin(phi) (a x b).e`,

which is `-1.1469` at `D/J = 0.7`, `+1.1469` at `-0.7`, and 0 at `D = 0`.
The CHSH maximum (Horodecki) is `2 sqrt 2` in all three cases.

*Proof.* For J>0 the untwisted XXZ bond has a unique singlet ground state: its energy is `-J-2A`, while the other energies are `-J+2A,J,J`, with `A=sqrt(J^2+D^2)>=J>0`. The twisted state is its local-unitary image. Its correlation matrix is the negative rotation matrix (with the convention of Theorem 1), giving the displayed signed antisymmetric term. Local unitaries preserve the singlet CHSH maximum. Diagonalisation and 100 random menu pairs check these identities. The
ratio of the antisymmetric part to `(a x b).e` is constant to `1e-10`. ∎

The quantity `E(a,b) - E(b,a)` is a statistic of records alone. It is odd
under the improper inversion. So a handed dynamics produces handed record
statistics.

## Theorem 5 — handed ground states on the cube

*Statement.* On the open 2x2x2 cube with `J = 1`, `K = 0.3`:
- the ground state's mean bond vector chirality is `-0.4585` at
  `D = 0.5`, `+0.4585` at `D = -0.5`, and 0 at `D = 0`;
- the ground state is non-degenerate, with gap `3.85`;
- the cube's inversion, a site permutation with axial spins, maps `H(D)`
  exactly onto `H(-D)`.

*Proof.* Exact diagonalisation on 256 states. The runner checks the
inversion map to `1e-12`. ∎

## Checks

The runner prints seven checks in five families. All pass in about two
seconds:
- **A.** The symbolic turned-bond identity.
- **B.** Ring spectra.
- **C.** Holonomy, and straight-versus-bent-versus-cube spectra.
- **D.** The handed record correlation, and the Bell value.
- **E.** The cube's chirality, and the inversion map.

## What this does not do

- It does not identify the Moriya handedness with any physical parity
  violation or weak interaction. It does not derive the sign or size of `D`.
- It computes ground states of small clusters. No infinite-volume phase
  (helical order or otherwise) is claimed.
- The handed record statistic is computed for the pair's ground state.
  Records formed in other states or orders are not treated.

## Decision points recorded

- The fully soldered clause and the sign of `D`. Choosing the sign is
  choosing a handedness. The axioms' proper-only rotation group permits
  either, and the improper inversion exchanges them.

Not adopted.

## Mathematical dependencies and reproduction

- [DYNAMICS_CLAUSE_COVARIANT_NEAREST_NEIGHBOUR_TWO_QUBIT_GENERATORS_HEISENBERG_UNDER_POSSIBILITY_COVARIANCE_THREE_COUPLINGS_UNDER_FULL_SOLDERING_BOUNDED_THEOREM_NOTE_2026-09-24](DYNAMICS_CLAUSE_COVARIANT_NEAREST_NEIGHBOUR_TWO_QUBIT_GENERATORS_HEISENBERG_UNDER_POSSIBILITY_COVARIANCE_THREE_COUPLINGS_UNDER_FULL_SOLDERING_BOUNDED_THEOREM_NOTE_2026-09-24.md)
- [DYNAMICS_CLAUSE_RECORDS_ACT_AS_FIELDS_A_SITE_WITH_SIX_RECORDED_NEIGHBOURS_IS_A_QUBIT_IN_THEIR_FIELD_AND_ITS_LAW_POINTS_ALONG_IT_BOUNDED_THEOREM_NOTE_2026-09-24](DYNAMICS_CLAUSE_RECORDS_ACT_AS_FIELDS_A_SITE_WITH_SIX_RECORDED_NEIGHBOURS_IS_A_QUBIT_IN_THEIR_FIELD_AND_ITS_LAW_POINTS_ALONG_IT_BOUNDED_THEOREM_NOTE_2026-09-24.md)
- [MINIMAL_AXIOMS_2026-06-29](MINIMAL_AXIOMS_2026-06-29.md)

Primary runner: [dynamics_clause_moriya_handedness_is_a_twist_with_curvature_2026_09_24.py](../scripts/dynamics_clause_moriya_handedness_is_a_twist_with_curvature_2026_09_24.py). Paired output: [current runner output](../logs/runner-cache/dynamics_clause_moriya_handedness_is_a_twist_with_curvature_2026_09_24.txt). All numerical historical figures above describe the declared finite setup; current tolerances and diagnostics are in this paired output.

## No-Go Discipline Gate

This section bounds the negative subclaims; it grants neither a retained grade nor an exhaustive search over physical alternatives.

### N1 — Alternative routes

- **ATTEMPTED — Single-bond gauge.** Remove the handed term by a local relative rotation. This succeeds on one bond, with the atan2 angle and altered transverse coupling.
- **ATTEMPTED — Open-line transport.** Propagate the local gauge along a line. This succeeds because no plaquette compatibility condition occurs.
- **ATTEMPTED — Plaquette holonomy.** Extend that same rotation assignment across orthogonal directions. The commutator quaternion has scalar 1-2 sin(phi/2)^4; interior angles give nonidentity holonomy.
- **ATTEMPTED — Pair record correlations.** Erase the signed handed observable by using only a scalar CHSH maximum. The maximum is unchanged under local rotations, while antisymmetric correlations retain the sign.
- **ATTEMPTED — Finite graph spectrum.** Identify the supplied bent or cube example with the specified untwisted comparison at the same couplings. Their numerical spectra differ at the tested parameters; no universal graph theorem is inferred.

These are the actual formulations tested in the argument and controls above. Successful escapes narrow the rejected broader claim; they are not counted as failed physical alternatives.

### N2 — Conditional structure

No count of independent physical walls is asserted. Dynamics, preparation and readout are supplied jointly; implication relations between possible derivations of them remain unresolved. The scoped results use their explicit hypotheses rather than an asserted wall-independence theorem.

### N3 — Hidden assumptions

The stated Hamiltonian, state preparation, record compression and readout are conditional mathematical inputs, not additions to the axioms. Numerical tolerances and finite graph sizes are diagnostics, not exact or thermodynamic proofs.

### N4 — Residual matching

No prior no-go is used to close an additional residual. Linked companion notes supply only their displayed covariance, projector or probability identities. The examples above do not certify other formation laws or physical models.

### N5 — Resolution

- `per_element:` Bond twist matrices and the signed pair correlator are tested.
- `per_site:` Local spin rotations and their finite compatibility constraints are tested.
- `per_mode:` checked and not executed — no dispersion or continuum parity theorem is claimed.
- `per_block:` Line, plaquette, pair and finite cube comparisons are tested.
- `lattice_wide:` checked and not executed — finite spectra do not certify all three-dimensional models.

### N6 — Partial closure

Choosing the stated supplied model yields the conditional theorem without adopting a new axiom. A convention cannot by itself select its state, dynamics or probability law. No claim that a new axiom is necessary is made.

### N7 — Strongest counter-route

A different transformation or different untwisted target might evade the particular bond-frame construction. Plaquette holonomy excludes that prescribed frame assignment, while the finite spectral comparison excludes only the specified target at the tested couplings. No proof here rules out every transformed Hamiltonian or physical realization; such a claim would require classifying allowed targets and maps.

### N8 — Related work

The linked companion sources are the relevant nearby arguments rechecked for this result. Their conditional boundaries are preserved here. Similar wording or a prior finite computation does not supply a universal obstruction.
