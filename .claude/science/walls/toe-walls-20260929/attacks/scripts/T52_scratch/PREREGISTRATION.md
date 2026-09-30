# T52 pre-registration (written BEFORE any script in this folder was run)

Author: Claude Sonnet 5.5 (same vendor family as the supervisor; same-family check).
Date: 2026-09-29.

## What is being tested
Wall T52 = L10-W5 (angles are data pins) + L10-W7 (chart, TM2, benchmark disagree).
Observation that motivated the test (from reading only, no run yet): the lane's
native Klein group V4 = <S, P23> has THREE non-trivial involutions, S (fixes W: TM2),
P23 (fixes eta: theta13 = 0), and S*P23 (fixes xi = (2,-1,-1)/sqrt6: TM1). The lane
tested only S. Algebra on paper (not yet run): TM2 gives s12^2 = 1/(3 c13^2) >= 1/3;
TM1 gives s12^2 = (1-3 s13^2)/(3 c13^2) ~ 0.318.

Data comparator (repo-quoted only, PMNS_DCP_FORECAST_..._NUFIT6 note, lines 22-46):
s12^2 in [0.2893, 0.3295]; s13^2 in [0.02070, 0.02420] (no-SK) / [0.02064, 0.02418]
(with-SK); s23^2 in [0.432, 0.587] / [0.435, 0.584]; delta 3sigma [114,405] / [125,365] deg;
NO best fit s23^2 = 0.470, delta = 207 / 212 deg. Box used = intersection of the two columns.
Older NuFIT-5.3 box (from the lane runner): s12^2 [0.275,0.345], s13^2 [0.02029,0.02391], s23^2 [0.430,0.596].

## Test A  (operator level; script A_v4_branches.py)
Build, in the corner basis with electron = corner 1, the general Hermitian operator M
commuting with each involution R in {S, S*P23, P23}; optionally also impose the mu-tau
reflection P23 M* P23 = M. Diagonalise with random parameters, assign columns by the
observational hierarchy |U_e1|^2 > |U_e2|^2 > |U_e3|^2 (the lane's sigma_hier premise, shared
by all routes), extract (s12^2, s13^2, s23^2, sin d, cos d) from the modulus/Jarlskog formulas.
PASS reading (TM1 branch viable): for R = S*P23 (+reflection) and every sample with s13^2 in the
data box: s12^2 in [0.3168,0.3192] (inside the box), s23^2 = 0.5 (1e-9), |sin d| = 1 (1e-9);
for R = S (+reflection): s12^2 >= 1/3 > 0.3295 for every sample (outside the box);
for R = P23 (unitary): no sample in the box.
FAIL reading: any of the three fails, or the operator-level numbers differ from the algebra.
Extra (no pre-registered value): TM1 without the reflection (free phase psi): the correlation
between s23^2 and delta, and whether the NuFIT-6.1 best fit (0.470, 207-212 deg) is reachable.

## Test B  (chart embedding; script B_chart_embedding.py)
Solve the chart H(m,delta,q_+) (chamber q_+ + delta >= sqrt(8/3), sigma_hier = (2,1,0)) for
(a) the TM1+reflection point at s13^2 = 0.0222: (0.3182, 0.0222, 0.5);
(b) the TM2+theta_e+phi point of L10 scratch: (0.307, 0.0222, 0.4887);
(c) the lane's own three-identity point (control).
Record the chart's predicted cos d, sin d and coordinates.
Readings: chart CONTAINS the TM1+reflection curve at the data if a chamber solution exists with
|cos d| < 0.01; chart is DISTINCT from it if the solution exists with |cos d| > 0.05 (a different
delta at the same three angles); NO SOLUTION means the chart cannot reach that triple.
Three-identity stability: the identities survive at a re-pinned target if all of
|m-2/3|/(2/3), |delta q_+ - 2/3|/(2/3), |det H - sqrt8/3|/(sqrt8/3) are < 3%; otherwise the
identities are tuned to one target, not structural.

## Test C  (how much does the data pin the chart; script C_preimage_width.py)
Linearise chart -> (s12^2, s13^2, s23^2) at the three-identity point, propagate the repo-quoted
3sigma half-widths to (m, delta, q_+). READING: if the 3sigma coordinate half-widths are >= 5% of
the coordinate, a match of a coordinate to a "named constant" at the 0.2-1.7% level cannot be
told from chance, and only the count of nearby simple constants matters (report it).

## Overall outcome mapping fixed in advance
- PASSED only if the operator-level route derives all three angles with no data input. (Not
  expected: theta13 is a free number in every branch.)
- PRICED if the reduced route (Test A PASS) shows the angles are equivalent to: one real
  number (theta13 / doublet breaking) + one discrete choice (which involution) + shared premises.
- STANDS if Test A FAILS.
- MISFRAMED if the operator-level check shows the wall's incompatibility is a label conflict
  rather than a physical one and the cheaper question is well-posed.

## Addendum: Test D (registered after tests A, A2, A3, B, B2, C had run; before D ran)
Test D: finite-group catalogue (script D_group_catalogue.py). The finite group acting on the hw=1 triplet
is (a) the lane's S3 = <C3, P23> (permutations of the 3 corners) and (b) if the lattice translations are
included (they act as diag(+-1) on the BZ-corner states) the octahedral group O_h = signed permutations (order 48).
Enumerate every abelian subgroup A whose joint eigenspaces on C^3 are all one-dimensional (so a residual
symmetry fixes a basis with no free angle); for every ordered pair (A_e, A_nu) form U = U_e^dagger U_nu, take
|U|^2 up to row and column permutations, and list every distinct pattern.
PASS reading (group theory alone cannot give the observed theta13): the smallest nonzero |U_e3|^2 over
all patterns (any row taken as electron, any column as nu3) is >= 1/6, so the observed 0.0222 is never a
finite-group number. FAIL reading (a finite-group pair lands within the repo-quoted 3sigma box): would
change the outcome to PASSED-at-a-discrete-price and must be reported first.
Also record the smallest |U_e3|^2 over patterns with s12^2 in the 3sigma box.
