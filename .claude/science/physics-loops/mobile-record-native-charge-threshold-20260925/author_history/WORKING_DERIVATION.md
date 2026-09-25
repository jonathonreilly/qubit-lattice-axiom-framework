# Working candidate40: what the first formed pair does and does not identify

Personal unsealed scratch, 25 September 2026. No independent check, publication,
physical charge calibration or observed-particle identification. Original full
formation law and all color/field states stay in force. Do not infer a finite-g
bound-state statement from the flat magnetic reduction below.

The observation question is how to obtain charged excitations and their current
or force response in THIS supplied model, before using measured electric charge
to calibrate g. Three existing Coulomb notes were read fully at the identities
in OBSERVATION_CHARGE_SCALE_SOURCE_INVENTORY_0557.json. They use different supplied
Yee, finite-clock Villain, or ungated rotor/CAR laws and cannot provide that
identification. This is a three-source comparison, not an exhaustive no-go.

## Reused exact parent and new proposed threshold

PR9199, HEAD d3dfdff92b6eb9e422da3691d13af4c249b7c4e9, canonical native ground
note SHA d709a13f913f0f16cce7f4fe4ae47ebfc90dc8d90b1fcd0cf0c952337bedcf7b,
defines the flat magnetic two-occupied-B operator Q with coefficient TWO per
outward-outward-return-return path. Its vacuum value q0=321 L^3 and R=Q-q0 I.
The full one-minus color operator has the same largest eigenvalue through
the uniform-minus embedding; this is an edge statement, not deletion of colors.

For separated records (distance >4), every row of R has sum 12096=2*6048.
The six nearby displacement classes have corrections -196,-584,26,72,92,152
with multiplicities 6,12,6,24,12,24. Their total is -1548. The parent gives
the finite-L weak-g energy-edge relation Delta_L=-rho(R)/4 (rho here means
largest eigenvalue of the shifted operator, not its absolute spectral radius).

A newly found positive trial v(X)=1-x(type(b-c)) equals one outside distance6.
The13 cubic classes through distance6 have deficits with denominator10^9:

| Type | Deficit numerator |
|---|---:|
|002|30355481|
|004|0|
|006|82543|
|011|62454728|
|013|592565|
|015|257096|
|022|1564788|
|024|501938|
|033|0|
|112|2988879|
|114|733404|
|123|1227493|
|222|0|

Every listed exact residual Rv-12096v is negative. The37 stored rows cover all
cubic displacement classes through distance10. Only the13 through6 are needed
as nontrivial checks: outside6, the row sum is12096, v(X)=1, v(Y)<=1, and
off-diagonal entries are nonnegative. Thus the inequality there is automatic.
The original LP with support through2 and the support-through4 attempt were
infeasible under0<=x<1; those numerical failures are retained and prove no
general impossibility. Support-through6 gives an exact rational solution in
attempt03, then a shorter rational proposal with explicit strict margin in
attempt04. The floating LP only proposes numbers. Final verification must
reconstruct the primitive rows independently of that proposal and prove the
extension outside the checked region.

For a symmetric finite-range R and positive v, the ground-state transform is

  <psi,(lambda-R)psi>
  =1/2 sum_(X!=Y) R_XY v_X v_Y |psi_X/v_X-psi_Y/v_Y|^2
   +sum_X (lambda-(Rv)_X/v_X)|psi_X|^2.

It proves R<=12096 I on the unwrapped two-record configuration space if the
certificate and its tail argument hold. The operator is well defined there by
subtracting the vacuum scalar locally in each row, not subtracting two infinite
operators. Uniform row bounds and finite range give a bounded self-adjoint
operator on unordered-pair l2. Two large disjoint boxes whose separation exceeds
their sizes supply approximate constant two-record states: the interaction
defect is absent in the bulk, and finite-range boundary/volume terms vanish.
This should put12096 in the top spectral edge and identify it as the separated
threshold. It excludes a lower-energy pair below that threshold ONLY for this
flat magnetic occupancy operator, not the actual finite-g rotor model.

For conservative even L>=24, the required near-pair patches have no periodic
alias: initial distance<=6 and one-record displacement<=4 stay below distance10,
while local primitive star unions have diameter below24. Need check this detail
fully and run actual periodic primitive controls before a finite-torus claim.
Then the same v gives top(R_L)<=12096. The uniform-pair Rayleigh quotient is
12096-1548/(n-1), n=L^3/2, since each nonzero B displacement is equally represented
in the ordered-pair average. Proposed consequence:

  -3024 <= Delta_L <= -3024+387/(n-1), L>=24,
  lim_(L->infinity) lim_(g->0) g^2 tau(e_(n+2)-e_n)=-3024.

No uniform finite-g error or interchange of these limits is available. The
earlier finite-L cyclic edge result remains a support statement, not an atom,
mean, typical energy or physical particle mass.

## Charge interpretation, still to control

At fixed occupancy X the uniform-minus state has m=n+2 occupied sites. If U is
the uniform-minus embedding, then U* q_x U=(1-2/m)n_x on that occupancy fiber.
On A the excitation charge q_a-1 is -2/m; each occupied B has mean1-2/m.
Thus the leading symmetric color comparison cannot simply be called one plus
and one minus charge at the two B records. The negative color has probability
2/m to be on B and n/m to be on A. For vertex test f,

  rho(f)=f(b)+f(c)-2f(location_of_minus),
  Var_color rho(f)=4[(sum_occupied f^2)/m-(sum_occupied f)^2/m^2].

An actual resolved first birth from an all-A-plus input has a single minus
location for each resulting occupancy pair: on the selected B if sign plus,
or on its A if sign minus. Its squared projection onto the uniform-minus color
line is1/m for each pair. These need exact controls. A color comparison at
flat connection is not an invariant projector of h_g at general flux, nor a
claim that an energy-window probability equals1/m. Reference-flow choices
must be stated if a fiberwise extension is discussed.

Potential next useful calculation: derive the isolated-record hopping kernel
as an algebraic contribution and its small-momentum curvature. The odd-record
sector is not physically admissible here; an auxiliary one-body kernel is not
a new state sector. Any effective inertial mass or charge mapping must be
labelled conditional, and rest energy, Coulomb force and physical selection
remain separate obligations. Do not attach measured electron mass/alpha or
photon bounds to this auxiliary kernel without those identifications.

## Evidence and next decisions

explore_two_record_threshold.py reuses the exact personally authored root33
local_delta_row helper (SHA6d874248e3f7c3963f6fa3c6ec38c8bd9f465efc870fc29a740ec16bb290c9aa),
whose source was read fully. The extended program reuses that unwrapped row
builder. This is disclosed source reuse, not independent reconstruction.
attempt01:13 row groups, support2, LP infeasible. attempt02:23 groups, support4,
LP infeasible. attempt03:37 groups, support6, exact rational certificate.
attempt04:the same stored integer rows, strict-margin LP and rounded integer
numerators, all37 residuals then checked as exact Fractions. The first three
executions have complete source/stdout/stderr/receipts. attempt04's full shell
recorder was run from a here-document; retain that provenance and reconstruct
the final certificate in a saved standalone program before sealing.

Root has read all73 row coefficients across the first three result sets and
the complete37-row residual certificate. Larger full target dictionaries are
stored and mechanically parsed; do not claim a separate primitive replay yet.
Next: exact standalone primitive certificate, tail/periodic proof, charge
controls, then selective independent reconstruction at this consequential
milestone. Candidate40 is presently unsealed and should not be published or
described as independently checked.
