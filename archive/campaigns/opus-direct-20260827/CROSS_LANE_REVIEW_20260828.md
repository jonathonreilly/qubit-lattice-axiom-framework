# Root cross-lane review of `POSITIVE_PATH.md`

Source reviewed:
`/Users/jonBridger/Projects/Physics-baremetal-probes/.claude/worktrees/gravity-toe-lane-work-427b0b/.claude/science/opus-direct-20260827/POSITIVE_PATH.md`

Disposition: **one useful next discriminator, no imported TOE closure**.

## What survives

1. The degree-uniform exterior-weight argument is mathematically promising in
   general dimension.  On the actual three-dimensional carrier, however, its
   principal conclusion `V^2=det(g)` is already Block214.  A general proof can
   be made analytic by restricting the Clifford anticommutator successively to
   exterior degrees; finite `d=2,3,4` enumeration should not carry the theorem.
2. The constant positive-metric dispersion
   `m^2+sin(k)^T g^-1 sin(k)` and the free transfer pole
   `asinh(sqrt(m^2+p^2))` reproduce exactly.  They are useful comparators, but
   are already represented in current-source and do not supply a physical time
   direction or repair Block226's connection-kernel common-clock obstruction.
3. Weighted skew-adjointness of the variable-cell hop reproduces.  Its useful
   content is already covered more generally by Blocks215--216: the full
   cross-form family exists, and the metric/Clifford-compatible section reduces
   the two endpoint contributions to one covariant half-hop.  The packet does
   not prove uniqueness of the endpoint-symmetric ansatz.

## What must not be imported

- The packet itself withdraws the `R/[8(d-1)]` curvature and induced-gravity
  reading after the anisotropic test.  A fresh execution of `opus_t12.py`,
  which includes the two-step hopping contribution through row sums of
  `-K_hat^2`, also fails its fitted local law (`holds everywhere: False`).
  There is no curvature or Einstein--Hilbert theorem here.
- The packet's variable-metric transport is the endpoint-only/pure-comparison
  section.  Block216 proves that this section has trivial closed-loop holonomy
  for arbitrary positive endpoint cells.  It therefore cannot by itself
  supply Levi-Civita curvature; a nontrivial selected orthogonal factor
  `R_sr` is still missing.
- Taking `V=sqrt(det g)` for indefinite `g` is an algebraic complexification,
  not a second admissible branch of the positive `D3` Hilbert carrier.  It
  abandons the positivity used by the current OS/transfer construction.
  `opus_t18.py` only finds selected finite-torus real-mass zeros (at
  `m=-1,0,+1` on its `L=4` witness); it does not derive a Lorentzian branch,
  a physical clock, or nonuniqueness for all masses.
- Record-weight positivity does not select the alleged branch: `opus_t17.py`
  returns positive flat `1/4` weights on both displayed branches.  The claim
  that a record requires a unique propagator remains an interpretive premise.
- The packet is not audit-ready as supplied.  For example, `opus_t2.py` prints
  `eps_a^dagger == iota` as `False` under its own unsimplified check even
  though entrywise rational-function cancellation gives zero; the runner needs
  a correct exact equality gate.  The inhomogeneous record probes did not
  complete in a bounded root replay and must not be treated as executed facts.

## High-value route unlocked

After Block226 delivery, attack Block216's exact residual rather than another
analytic-continuation packet:

1. Start from positive metric-volume cells and their coframes.
2. Construct a **candidate**, not a derived law, for a metric-determined
   orthogonal edge factor using the orthogonal polar part of a carefully
   oriented relative-coframe map.
3. Prove or falsify independent endpoint-frame covariance, reversal,
   `D3`/Clifford compatibility, and exact plaquette behavior.
4. State one explicit discrete Cartan torsion functional and test whether the
   polar candidate makes it vanish.  Do not rename closest-orthogonal transport
   as torsion-free.
5. Linearize the surviving candidate and compare with the continuum
   Levi-Civita spin connection on anisotropic, off-diagonal perturbations.  A
   conformal-only test is insufficient.
6. Only if those gates pass, insert the selected `R_sr` into the full
   two-step Dirac--Kahler operator and test the complete slowly-varying symbol
   for the Ricci/scalar-curvature combination.

This route can either retire the supplied-connection import or produce a sharp
no-go for the natural polar selector.  It changes no axiom or primitive and
does not claim physical gravity, Lorentzian time, or continuum closure in
advance.

## Secondary route

The free `asinh` transfer energy may be used as a comparator for a later
transfer-first Lorentz update.  It becomes relevant to the connection campaign
only after one common same-action generator/refinement construction couples
the Dirac--Kahler matter sector and the selected connection sector.  By itself
it is prior-art free propagation, not the missing TOE bridge.
