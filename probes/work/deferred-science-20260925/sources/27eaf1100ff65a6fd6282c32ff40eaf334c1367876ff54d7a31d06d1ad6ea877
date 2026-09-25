---
claim_id: dynamics_clause_moriya_handedness_is_a_twist_with_curvature_gauged_along_a_line_not_in_three_dimensions_and_seen_in_records_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "For the fully soldered dynamics clause of open PR 9040, supplied and not adopted, with bond term J s1.s2 + K (e.s1)(e.s2) + D e.(s1 x s2): (1) J s1.s2 + D e.(s1 x s2) = V [A (in-plane) + J (along e)] V^dag with A = sqrt(J^2 + D^2), V = exp(-i phi e.s2/2) and tan phi = D/J, exact for bonds along x, y and z. (2) A periodic J-D ring along e has exactly the spectrum of the XXZ ring whose closing bond carries the total turn N phi (N = 5, 6, 7). Twisted and untwisted bonds have equal spectra on a straight open chain. (3) Where bond directions meet they do not: the plaquette holonomy of turns about two axes is a nonzero rotation for 0 < phi < pi (20.74 degrees at D/J = 0.7), and twisted and untwisted spectra differ on a bent chain and on the open cube, so no unitary relates them there. (4) The two-site ground state (J > 0) gives record correlations on antipodal menus with E(a,b) - E(b,a) = -2 sin(phi) (a x b).e, odd in D; its CHSH maximum stays 2 sqrt 2. (5) On the open cube with J = 1, K = 0.3, D = 0.5 the ground state's mean bond vector chirality is -0.4585, odd in D, and the improper inversion maps H(D) to H(-D). No physical parity or weak-interaction reading is claimed."
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
improper ones. Open PR 9040 found the consequence for a local dynamics
clause: full soldering admits the Moriya coupling `D e.(s_x x s_y)`, which
the improper inversion would forbid, since it changes the coupling's sign.
This note asks what that handedness is, and whether records can see it.

- **A Moriya bond is a turned XXZ bond.** `J s1.s2 + D e.(s1 x s2)` is an
  XXZ bond seen through a frame turned about the bond axis by `phi`, where
  `tan phi = D/J`. The XXZ bond has in-plane strength `sqrt(J^2 + D^2)` and
  strength `J` along the axis.
- **Along a straight line the turn is a gauge.** Cumulative frame turns
  remove every twist of a straight chain. On a ring they leave one total
  turn `N phi` on the closing bond, as a twisted boundary.
- **Where directions meet it is not.** Turns about two different axes do
  not commute. The holonomy around a plaquette is a nonzero rotation, and
  each turn also moves the anisotropy axes of the other bond directions.
  On a bent chain and on the cube, the twisted and untwisted models have
  different spectra, so no unitary maps one to the other there. In three
  dimensions the handedness is physical, not a choice of frames.
- **Records see it.** For the twisted pair's ground state, correlations of
  records on antipodal menus have an antisymmetric part
  `E(a,b) - E(b,a) = -2 sin(phi) (a x b).e`. This is parity-odd and changes
  sign with `D`. The Bell value stays `2 sqrt 2`.
- **Handed ground states.** On the cube, the ground state's mean bond
  vector chirality is `-0.4585` at `D = 0.5` and `+0.4585` at `D = -0.5`.
  The improper inversion maps one Hamiltonian exactly onto the other.

So the axioms' symmetry content permits a handed local dynamics. Its
handedness cannot be removed by frames in three dimensions, and it shows
directly in the statistics of records.

## Premises and declared objects

- **Axioms** (`docs/MINIMAL_AXIOMS_2026-06-29.md`). Lattice: "proper cubic
  rotations about each site".
- **Supplied, not adopted.** The fully soldered bond term of open PR 9040,
  `J s1.s2 + K (e.s1)(e.s2) + D e.(s1 x s2)` on the bond `(x, x+e)`. The
  improper inversion maps `D` to `-D` and fixes `J` and `K` (open PR
  9040).
- **Frame turns.** `R_e(phi)` is the rotation about `e` by `phi`. On a
  qubit it is implemented by `exp(-i phi e.s/2)`.
- **Records and menus.** Antipodal menus and the trace rule, as in open PR
  9041.
- **Vector chirality of a bond.** `f.(s_x x s_{x+f})`, a pseudoscalar under
  the inversion.

## Theorem 1 — a Moriya bond is a turned XXZ bond

*Statement.* For a bond along `e`, with `A = sqrt(J^2 + D^2)` and
`tan phi = D/J`,

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
- The twisted and untwisted models have different spectra on a bent open
  chain with bonds along x, y, z, x (largest difference `0.085`), and on the
  open cube (`0.779`).

So on these graphs no unitary relates the Moriya model to an untwisted one.

*Proof.* The holonomy is computed on a grid of 60 values of `phi`.
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

*Proof.* Diagonalise the pair and evaluate on 100 random menu pairs. The
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
