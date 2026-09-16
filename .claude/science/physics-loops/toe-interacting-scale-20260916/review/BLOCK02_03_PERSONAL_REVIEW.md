# Personal review: uniform energy and equal-time gauge limit

2026-09-16 UTC. Same-author review, not an independent review receipt.
The user requires personal execution without subagents. No audit status is
set and no main-branch science is changed.

## Consequential questions checked

- **Matter premise mismatch found and corrected.** Block01 permits an extra
  nonnegative onsite charge penalty. A fixed penalty would survive g->0 and
  add a nonvanishing Slater trial cost. Block02 explicitly excludes it and
  uses the stated quadratic paired Wilson Hamiltonian. No free-matter claim
  is made for Block01's larger model class.
- **Integer topology.** The electric boundary lattice is primitive because
  torus first homology is free. The dual is the projected integer link
  lattice, bijective under C with integer curls. The 3^3 Smith-invariant
  calculation challenges the proposed finite complex, while the argument
  in the note supplies the general-L justification. The trial carries zero
  harmonic electric flux; its fermion dressing need not preserve that
  subspace, and the proof does not require that it do so.
- **Weights and noncommuting inverses.** K is inverted on range C^*, not
  obtained by moving W_E through a square root. Both Riccati and plaquette
  identities were compared with a direct spectral inverse in the fixture.
- **Positive-square sign and cutoff boundary.** The cosine divergence has
  the positive sign in the gauge-energy decomposition. The finite Fourier
  fixture preserves an order-one hard-boundary discrepancy and identifies
  its exact shift-nonunitarity source. It vanishes on the padded core.
  Reversing the divergence sign fails on that core. The theorem has no
  artificial Fourier cutoff.
- **Dressed energy.** The flow sign is fixed by Dp_x=delta_root-delta_x.
  Literal Fock matrix energies agree after dressing; the reversed sign
  differs by an order-one amount. Electric cost uses charge variance,
  with zero mean cross term, rather than a worst-configuration norm.
  Slater variance was challenged through determinant fidelity curvature.
- **Fixed filling and actual-state block charges.** Open-block Wilson
  particle-hole symmetry ensures an unrestricted minimum at half filling,
  including an even zero eigenspace. The trial has neutral blocks. The
  actual state need not: the matter lower bound is a pointwise full-Fock
  matrix inequality, valid before Gauss restriction. The tiling includes
  periodic seams and arbitrary L, with O(V/R) removed links.
- **Uniformity mechanism.** The dual partition function need not approach
  one as V grows; only its logarithm per volume is bounded. The choice
  R=floor(min(g^-1/2,L)) gives the claimed joint rate without restricting
  g against L. The nonlocal polar multiplier is controlled by Fourier
  covariance positivity, not an unjustified absolute-summability bound.
- **Characteristic ODE.** The complex smear is u+iMv. The perpendicular
  imaginary term in the commutator was checked through directional
  differentiation; changing its sign gives a finite discrepancy. The
  argument uses the annihilator norm on ground vectors, not the creator
  norm. It explicitly controls cosine defects after angle translations,
  rather than assuming a ground-state estimate is unchanged by unitaries.
  A separate single-rotor diagonalization compares the exact characteristic
  derivative with the Duhamel decomposition. This is a selective finite
  check of the algebra, not a simulation of the charged thermodynamic model.

## Scope and disposition

The energy theorem and single-exponential gauge characteristic theorem have
complete author arguments and selective tests. Their claimed status remains
provisional, pending independent mathematical review. The working-route note
is historical/provisional scaffolding, with later completed steps identified.
Joint products of field exponentials, matter correlations and factorization,
and dynamics require separate arguments. No fixed-positive-g massless phase,
TOE derivation or forced axiom update follows from these two notes.

The two Block02 runners were run once, then rerun after changing only their
stdout to concise summaries and adding actual check counters for local
instruction conformance. No tolerance, sampled input or mathematical check
was weakened. The Block03 helper provenance is recorded in its JSON.
The final frozen source/output hashes are in BLOCK02_03_SOURCE_HASHES.json.
