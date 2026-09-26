# Independent paired-record process check

2026-09-21. The specified elementary event, conditional-law, Gauss/Fourier and
reflecting-cube claims are confirmed at the frozen sources below. No actionable
mathematical or implementation defect was found. The reflecting-cube unfilled
absorption probability is exactly **4/21**. An independent analytic reduction
establishes this without using the author's 91-state matrix inverse.
This is a bounded construction check, not an audit, phase theorem, microscopic
qubit realization or wave result.

## Independent reconstruction and absorption proof

The complete note was read first. An edge-mask implementation, distinct from
the author's recursive vertex enumeration, constructed all subsets of the
cube's twelve edges and retained the 108 matchings. Birth, translation and
cube channels were assembled separately. The exact census is (1,12,42,44,9)
for zero through four dimers. The complete graph is in `CUBE_GRAPH.json`.

There is a ten-class exact lumping by dimer number, axis counts and the
relative positions of parallel dimers. Its class sizes are

| Class | Size |
|---|---:|
| Empty | 1 |
| One dimer | 12 |
| Two parallel dimers on a face | 12 |
| Two diagonally separated parallel dimers | 6 |
| Two nonparallel dimers | 24 |
| Three parallel dimers | 12 |
| Three dimers with axis counts (2,1,0) | 24 |
| Three-dimer unfilled traps, counts (1,1,1) | 8 |
| Fully packed columnar | 3 |
| Fully packed mixed | 6 |

Every one-dimer configuration has seven birth channels. Three add a parallel
dimer; four add a dimer of another axis. Its two reflecting translations
preserve this classification. Every nonparallel two-dimer configuration has
three birth channels, one per axis. The unused axis leads to an unfilled
trap; either previously used axis leads to a fillable state. Translating a
dimer preserves its axis. A parallel pair can therefore never become a
three-axis trap. It follows that

    P_empty(unfilled closed class) = (4/7)(1/3) = 4/21.

This is also certified by a rational harmonic function on all 108 states:
4/21 on zero/one-dimer configurations, 1/3 on nonparallel two-dimer
configurations, one on the eight traps, and zero elsewhere. Its generator
vanishes separately under each channel family. Every other nonclosed state
has at least one birth channel. Positive beta and the bounded number of births
therefore give almost-sure entrance to a closed class. This supplies the
hitting-probability interpretation, not only an algebraic null vector.

At beta=kappa=nu=1 the independent seven-transient-class linear solve within
the ten-class lump gives aggregate probabilities

    unfilled 4/21; full columnar 13/49; full mixed 80/147.

Direct reachability on the complete graph gives 91 transient states and
14 closed components: eight unfilled singletons, three full columnar
singletons, and three full two-state cube-exchange components. The unfilled
singletons have opposite-corner vacancies and alternating dimers on the
remaining hexagon. Each is immobile under the reflecting event rules.
The mixed full classes continue to exchange; absorption here means entrance
to a closed component, not eventual fixation of every full configuration.

The supplied event graph is also invariant under the full cube graph symmetry.
Checking its action on the closed components divides the aggregate probabilities
into 1/42 for each unfilled singleton, 13/147 for each columnar singleton,
and 80/441 for each two-state component. These agree with every entry in the
author's absorption JSON, including its component representatives.

## Event, conditional-law and readout checks

A matching edge defines its two reciprocal contents without an extra orientation
choice. Birth has one beta channel per undirected empty-empty edge. Dimer
translation has six proposed displacements per occupied pair, not per record.
Parallel overlap requires deleting both old positions before placing both
translated records; only destinations outside the old pair need be vacant.
All six translations and their inverses preserve identities in the independent
implementation. The renewal history forms two new records after moving the
original pair away. It establishes two formations, not unlimited renewal.

Each qualifying cube has one channel for its chosen opposite-face axis, at
rate nu. The four facing swaps form a single atomic event. The independent
reflecting graph has six states with one cube channel each and 102 with none;
the author graph has exactly the same multiplicities. The dense witness moves
eight records one nearest-neighbor step each and returns under the inverse.
Birth/translation/cube covariance was checked on the complete finite graph
for all 24 proper cube transformations. Additional improper graph symmetries
were used only as exact symmetries of these supplied classical rules, not as
new physical assumptions.

All 64 nearest-neighbor vacancy patterns around a vacant site are realizable
by matching occupied neighbors outward. The conditional formation probability
is 1/r for each of the r vacant neighbors; at r=0 there is no conditional
event law. In contrast, a complete exterior matching forces the one-site
value: vacant if no neighbor points in, or the uniquely required partner if
one does. An all-vacant exterior thus permits only a vacant one-site DLR
completion while the future paired event has six possible directions.
The distinction in the note is correct and essential.

Counting each birth edge once gives L V_vac=-2 beta E_00. Empty-start density
has derivative 6 beta on a degree-six torus, and 3 beta on the reflecting
cube. There is no uniform positive hazard at every vacancy. The eight traps
are a direct counterexample to unconditional finite-cube full packing.

The Gauss identity follows from the six incident matching edges and
sigma_(x-e_i)=-sigma_x:

    div B(x)=sigma_x(o(x)-1)=-sigma_x v(x).

It holds for every matching. The independent integer check used 6B on an
even side-four torus, including wrapped dimers and all 108 embedded cube
matchings. The empty state has a staggered charge background, and a birth
removes an adjacent opposite-charge pair. The global parity convention
requires even periodic size; the reflecting unit cube is not a periodic
side-two torus.

For X=e^(-ik_x), Y=e^(-ik_y), Z=e^(-ik_z), direct edge changes give

    Delta Bhat=((Y-1)(1+Z),(1-X)(1+Z),0).

Its backward-divergence polynomial vanishes exactly; its linear term is
(-2i k_y,2i k_x,0). Its zero mode and every cut-flux increment vanish.
The independent readout covariance check handles negative-edge base-point
changes as well as the global parity sign under a unit translation. The
field's stated transformation qualification is therefore substantive, not
optional. A curl-shaped increment alone is not a dispersion relation.

Every conservative channel has an equal-rate inverse, so uniform measures
on finite connected components are reversible, and the specified mixtures
are invariant. Irreducibility is not implied. In addition, born partners retain
their partner identities under every supplied move: tagged classes can be
finer than content-matching classes. The 108-state count is correctly read
as the contents projection. No tagged-component census was asserted or proved.

## Source comparison, failure record and limits

`PRE_COMPARISON_DERIVATION.md`, the independent checker/graph and full logs
were sealed before opening the author runner or results. That seal SHA-256 is
`e346d7f19f42deceda307581d101d74b717efa0a2f677e584808c73a7232b616`.
Afterward, the complete author runner, result, run log and absorption JSON
were read. Calling its local helpers in memory reproduced precisely the
independent birth, translation and cube rates for every one of the 108 states.
All twelve logged rows and both source bindings match the result. The complete
author absorption inverse was not rerun; the independent lumped solve,
harmonic certificate and graph symmetry verify its stated probabilities.

Selective actual helper mutations were also tested. Identity translation is
rejected by the occupied-birth-endpoint guard in the renewal history; identity
cube exchange fails the dense-motion assertion; removal of staggering fails
the Gauss assertion. Their complete stdout/stderr and receipts are retained.
These rejection mechanisms are distinguished from the author's inline
constant anti-controls. No mutation was accepted.

The first independent Fourier check failed a structural symbolic equality:
-(X-1)(Z+1) and (1-X)(Z+1) had different expression trees. Its original source,
full outputs and diagnostic are preserved. Expanding the same polynomial
difference gives identically zero; only the comparison method was corrected.
The next complete run passed. A final pre-seal run added readout-transformation
and persistent-partner checks and passed; that preceding successful source
and log are also preserved. No coefficient or model premise changed.

Reproduce with `python3 independent_check.py`; post-seal comparison and targeted
mutations use `python3 compare_author.py`. Both write only here. The complete
uniform proofs of the elementary identities are in the pre-comparison
reconstruction; finite controls do not establish accessibility on a growing
periodic box. No new periodic search, production simulation, literature theorem,
source edit, Git action, formal audit or physical identification was performed.
The source's attribution/novelty history was not independently reviewed.

The frozen source identities are:

| Source | SHA-256 |
|---|---|
| PAIRED_RECORD_FORMATION_AND_DIMER_GAUSS.md | ed48192900501781ead6d60f17aedc1e9470746e65f449c5d75eccb6a66188ca |
| paired_record_dimer_check.py | 65ad8acc7384f25196132b23876f4510347832c4a7f4db548d9c9aead71d2288 |
| PAIRED_RECORD_DIMER_RESULTS.json | ecd779bbabaf253e0d307ab39ef4f944918bbe871179f792d0fb646889775f43 |
| PAIRED_RECORD_DIMER_RUN.log | 5cd40e89e1f6fbc88e06d258df28506cca0bcca8096b1210c90523c5bcc413ea |
| PAIRED_RECORD_CUBE_ABSORPTION.json | af49fce1761134e501ddbb6836cdfd61875713c7e66d804db4ac227ba8865f0e |

`FINAL_SEAL.json` binds these sources, unchanged procedural identities and all
review artifacts. There are no unresolved correction requests in this unit.
