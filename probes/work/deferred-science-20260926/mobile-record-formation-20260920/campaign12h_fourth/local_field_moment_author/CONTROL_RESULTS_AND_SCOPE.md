# Completed local electric-moment controls

The first control run succeeded on September23 at22:06:07--22:06:08 UTC,
in0.922 seconds. It uses exact integer and Fraction algebra. Its source is
`electric_moment_identity_check.py`, SHA-256
`2ca2790d214993a51463b2a562cffc0a0e02990ba4baced3603602b14b096204`.
Full source, output, results and actual execution receipt are preserved.

This runner explicitly reuses root's elementary rotor-path helper,
`formation_capacity_author/capacity_and_dark_state_check.py`, hash
`3e9621b36280d19373909922b104c1ead0df9aa47c043d372abd9f9424393a4a`.
It is an author control, not an independent implementation or an independent
check of the capacity packet. The local-moment theorem relies on the already
checked target and volume premises, not on capacity or long-time conclusions.

The new control covers all65 Gauss-compatible matter words at the declared
total charge on each of path8,ring8,cubeQ3, using one exact spanning-tree field
per word. It checks every observed link under both instrument conventions:
910,1040,1560 field columns, respectively. Complete sparse output vectors
satisfy the dissipative quadratic identity, the Hamiltonian derivation identity
and Gauss. Coherent and resolved generators have the same E and E^2 images
in these controls; this does not identify their recycling states or arbitrary
evolved observables.

The largest squared column norms for twice the dissipative drift, quadratic
variation and Hamiltonian drift (divided by i) are respectively (16,16,8)
on the path and ring and (64,64,104) on the cube. These columns respect the
stated conservative norm bounds. They are not proofs of those infinite
operator norms; the explicit bounded-commutator argument supplies the proof.
Nor is the finite seed family an exhaustive electric-field scan.

Independent local star fixtures check every link orientation and both
instrument conventions at degrees4,6,8. Their A-to-B signed initial field
drifts divided by kappa are -6,-10,-14; their initial E^2 derivatives are
12,20,28. Reversing the stored orientation reverses the first value and
leaves the second unchanged. These exact local fixtures include all birth
channels affecting the chosen link. The initial Hamiltonian contribution
to a diagonal field expectation is zero by the initial field eigenstate
argument, not by replacing the full lattice Hamiltonian with a star.

No trajectory, numerical volume extrapolation, all-time energy bound,
independent reconstruction or error for separately cutoff dynamics was run.
The finite-time moment and tail conclusions are analytic. Their independent
reconstruction is still pending; original analytic draft and seal remain
unchanged.
