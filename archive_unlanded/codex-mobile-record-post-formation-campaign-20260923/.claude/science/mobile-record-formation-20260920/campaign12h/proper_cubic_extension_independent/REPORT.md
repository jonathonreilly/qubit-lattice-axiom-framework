# Independent proper-cubic eleven-coupling extension check

2026-09-21. The six added maps and stated conditional selection results are
confirmed at the sources sealed here. No actionable mathematical or
implementation defect was found. This is a finite classification and local
realization check; it supplies no new hydrodynamic theorem or physical-field
identification and assigns no audit status.

## Boundary and method

The complete new note was read first. The independent reconstruction, exact
checker, outputs and failed first attempt were sealed before opening its
checker/results under `PRE_COMPARISON_SEAL.json`, SHA-256
`52fa9ab1a4fd3f55db57fb61fb9ececffd9b38fd951ca0dd24052698a0261563`.
The old full48/proper24 character counts and five-map construction are reused
from the unchanged `cubic_symbol_independent/FINAL_SEAL.json`, SHA-256
`485b0abf604335fd7cf93c18c933952a25877d9db39f42493a8e467d682a9fb1`.
The old dimension-eleven result by itself did not establish the new maps.

The new independent checker reconstructs the orthonormal tangent basis and all
24 actual permutations of the fifteen labels. It tests exact covariance of
each added species tensor for each coordinate direction, independence of all
eleven maps, polynomial closure constraints for arbitrary q, reversal parity,
the determinant, a generic rank, and the 15/2 species-current normalization.
No floating tolerance is used in these mathematical assertions.

The first execution reached the longitudinal-readout assertion and failed an
unexpanded symbolic structural-equality test. Its source and full stderr/stdout
are preserved as `independent_check_attempt1.py` and `ATTEMPT1.*`. Expanding
the same polynomial matrix yields exactly zero; the only code correction was
adding that expansion. The second complete run passed. Nothing was removed
from the mathematical condition. This was a checker simplification issue,
not a counterexample. All raw outputs and source identities remain available.

## Reconstruction

For proper rotations, E and B both transform by the same vector action.
Consequently B has the two scalar-gradient and two tensor-gradient couplings
already available to E. For C=[q]_cross and a diagonal traceless D,
CD-DC is symmetric off-diagonal and conjugates covariantly. Trace pairing with
Q_ij yields the fifth added map. The actual triple moment w transforms by the
permutation sign; with the off-diagonal tensor signs this gives the sixth
map, (q3,q2,q1). Exact actual-label checks confirm these sign assignments.
The six additions occupy blocks independent of the old five. Their eleven
independent directions saturate the previously proved proper-group dimension.

The generic symmetric pair tensor is S_i=(15/2)U A_i U^T. Product balance uses
the previously reconstructed periodic four-site coboundary and symmetry of S;
reflection symmetry is unnecessary. The exact species current is

    J_a = 2 p_a [(S_i p)_a - p^T S_i p].

At uniform p=1/15 and S_i 1=0 its tangent derivative is (2/15)S_i, confirming
the normalization for every new map. Finite tensors admit a sufficiently
large linear-rate constant or the positive-floor/positive-part construction.
Proper rotations taking an oriented bond to a negative coordinate direction
also reverse the four-site context; symmetric S supplies the required sign.
The distinct-four-site premise is retained (periodic sides at least four).

Full closure of all six raw-vector fields for arbitrary other moments requires

    a1=a2=u=v=b1=b2=b_u=b_v=0.

Multiplication of the two vector rows by q^T gives the same necessary and
sufficient conditions for preserving both raw Gauss constraints for arbitrary
remaining moments. This is not inferred merely by testing each coefficient
alone: the independent polynomial linear systems include all coefficients
simultaneously, excluding cancellation loopholes. The m curl survives;
d and g can remain entirely within the nonvector subsystem.

The derivative readout pair (i[q]_cross B,-i[q]_cross E) instead requires only

    u=v=b_u=b_v=0.

All four scalar columns are killed by [q]_cross q=0. Besides deleting external
forcing, closure requires that longitudinal E/B inputs in the readout kernel
remain invisible. The independent check includes that condition explicitly.
The d,g maps also remain allowed. All these statements concern every q and
arbitrary excluded moments; none follows from one prepared transverse state.

The t-versus-(d1,d2,w) block is exactly

    [ 2d q3             0       g q3 ]
    [ -d q2    -sqrt(3)d q2     g q2 ]
    [ -d q1    +sqrt(3)d q1     g q1 ].

Its determinant is -6sqrt(3)d^2 g q1 q2 q3. When it is nonzero it contributes
six nonzero signed eigenvalues. With m nonzero the closed vector block adds
four, leaving four zeros in fourteen fields: two longitudinal vector modes
and two scalars. Exact rank ten is independently checked at q=(1,2,3),
m=d=g=1. Special directions, vanishing coefficients and coincident speeds
require the stated degeneracy qualifications. These extra propagating moments
have no supplied matter, gravity or spin interpretation.

Under T=diag(-I3,I11), the old five maps are odd and all six extras are even.
Their independence proves that T A(q) T=-A(q) removes exactly the six extras.
Thus this additional internal reversal assumption recovers the five-dimensional
family without imposing spatial reflections. Its microscopic stationary
adjoint is the previously checked construction for that selected family;
this does not establish the adjoint property for generic eleven-coupling rates.

## Author comparison and limits

After the independent seal, the complete author note, checker, result and run
log were compared. The author checker imports the exact previously frozen
base checker before its result-write boundary. That dependency hash matches.
The recorded run log parses to precisely the recorded JSON. Its covariance
and closure controls are numerical, while its determinant and inherited
character calculation are exact; its scope describes this distinction.
The author output was authenticated, not rerun or counted as independent
mathematical evidence. Our exact checks additionally cover simultaneous
coefficient cancellations, the raw-Gauss row identity, and the longitudinal
kernel relevant to derivative closure.

`COMPARISON_RESULTS.json` binds the complete author identities. `FINAL_SEAL.json`
binds those sources, the prior independent dependency, unchanged procedural
sources, and every artifact in this review. The author note/results still
say independent review was initially pending; they are preserved as the
historical sources evaluated here. The present report supplies the separate
completed check rather than editing those sources or inheriting a broader
publication status. No external literature, new simulation, continuum proof,
or additional scientific premise was needed for this bounded extension.
