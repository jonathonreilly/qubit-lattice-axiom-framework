# Independent review of dimer-routed stationary transport

2026-09-21. **The matching-uniform stationary finite-mode argument is sound
under its stated fixed-parameter assumptions. One narrow scope correction
remains: the four-propagating-mode count requires gamma!=0.** No other
mathematical or implementation finding was identified. This is a bounded
independent proof check, not an audit or retained-status decision.

## F1: zero coupling is included but does not propagate

The frozen note allows real gamma at line74 and states four propagating
transverse modes at line277. Setting gamma=0 makes S_delta, J_delta and
every A_i zero. Equation(9) then correctly has the identity propagator;
all thirteen probability-tangent modes are static. The exact narrow repair
is to qualify the four-propagating/nine-static count by gamma!=0 at the
already stipulated nonzero mode, and state the gamma=0 degeneration.
The positive orbit masses/full-support premise must remain. No change to
the stationary theorem or the author's gamma=1 controls is required.
Root acknowledged this finding and kept the source frozen during review.

## Read boundary and identities

The complete note was read before the author checker or outputs. Independent
reconstruction and controls were sealed in `PRE_COMPARISON_SEAL.json`, SHA
`9b9cb681178410d2053ba8af7c778c56cd105dddda2c161446c6214cc5a1da3b`.
The complete author runner and combined result were then read; every group
file and the complete log were authenticated. All precomparison artifacts
remain unchanged.

| Source/evidence | SHA-256 |
|---|---|
| `DIMER_ROUTED_RECORD_TRANSPORT.md` | `5fd0f707110dba04fbebb01a64d3fc1925fca6358c6245cc57f7dfe6e691f479` |
| `dimer_routed_transport_check.py` | `98aa5259d58a5355a2aa9283e19bad869160bd9432882d589db8bbb2e0f15921` |
| author `RESULTS.json` | `e61d7efc93e5898750b4b98074d2b834f70621e1f4967726f4039f8058667413` |
| author run log | `87d1bc3912f135eaa84aad6074ba5c0eaa4d0eedf65ca48166c1481a02f7cf2f` |
| independent proof assessment | `7c31bc6e3f13dccc7689e70fcbf8717d76918c576c45e59db03037ebef96afd7` |

The older primary fluctuation derivation was neither read nor imported in
this check. The finite-state replacement steps were reconstructed directly.
Only the unchanged, previously reviewed geometric filling/rare-formation
premises are reused for the ordered formation conclusion; their exact notes,
reports and seals are bound in the source manifests. No literature theorem
or production simulation was inspected.

## Why the geometry-uniform proof works

The routing maps are permutations with inverse q_delta^-1(v)=w_v-delta.
Every nonfixed step progresses1 or2 in its signed direction, so a nontrivial
cycle has at least N/2 vertices. Even N>=8 ensures four distinct context
pairs. Pair exchanges preserve every record and partnership but are explicitly
atomic range-two moves. Their union is the connected dimer-contracted lattice,
with channel multiplicities retained. Reversing the temporary parity choice
reverses the context and reverses delta; their signs cancel. The rate family
is parity independent and properly cubic covariant.

The cycle drive telescopes pointwise. Together with exchange-invariant
product weights this gives stationary product and canonical count laws.
The positive floor yields irreducibility in each color-count sector. The
symmetric generator has exactly k0/2 per routing transposition, irrespective
of the geometry or external colors. The product current and its factor1/2
normalization match Eqs.(5)-(7). Geometry itself never changes at full packing.

The new proof obligation is met by C_l, the pairs touching a connected
all-site cube. Its internal contraction graph is connected for every
matching, and its size is Theta(l^3). At each fixed l, finitely many local
matching patterns/count sectors give a common finite Poincare constant A_l.
No quantitative bound on A_l is needed in the successive limits. Conditional
centering kills the entire global-count kernel. Block Poincare and the
O(l^3) overlap count give Eq.(10).

The stationary forward/backward martingale identity applies to the actual
nonreversible chain: solving -S f=F makes their sum2 integral F and bounds
the second moment by2t||F||_-1^2. Acceleration by N supplies1/N. This does
not require a reversible generator or a sector estimate for its drift.

Canonical sampling of the distinct current footprint differs from product
sampling by O(l^-3). Taylor expansion and independent empirical moments give
a centered remainder with second moment O(l^-6). Its normalized spatial sum
costs O(l^-3) after block overlaps. Replacing C_l by the ordinary black cube
costs O(l^-4) per block: only O(l^2) labels and the normalization differ.
The overlap estimate consequently gives O(1/l) for the weighted spatial sum.
The same estimate holds after any allowed bounded displacement.

In Eqs.(13)-(16), the exact gradient coefficients are bounded and constant
currents cancel under each permutation. After Taylor expansion, the delta
term gives -i A(Q) times the black-cube averaged field. In the remaining
term, reindexing v=q_delta u puts d_v at a common site. Subtracting
phi(v)[q_l(v)-p] cancels by sum_delta A_delta=0. The residual separates into
an O(1/N) phase error and the controlled shifted-block difference. This
proves the claimed bound uniformly over arbitrary deterministic M_N.
Fixed routing points have zero spatial coefficient and are omitted from
the distinct-position canonical step; their formal linear terms cancel.

The jump bracket is O(T/N). Variation of constants and integration by parts
use a supremum of fixed-time second moments of the integrated error, not
an unproved expected time supremum. Taking N->infinity at fixed l and then
l->infinity proves Eq.(9). The finite-mode initial CLT has covariance C and
the usual opposite-mode conjugacy; the extra black-sublattice alias cannot
intersect a fixed finite mode list for sufficiently large N. Random geometry
independent of stationary colors can be averaged afterward.

## Decisive independent controls

The independent checks use winding and irregular matchings at N=8,12,16,
including complete radius-six current footprints. They verify routing,
cycle lengths, parity reversal, connected blocks, current displacement
normalization and exact block/shift coefficient variances. All14^4 local
contexts in each signed direction check the sharp drive/rate bounds.
Exact nonisotropic full-support currents, all24 cubic transformations of
the tensor and quartic color code, the full14 current symbol and all retained
modes are checked separately.

An irregular period-eight example has a mean-zero unsmoothed direction
coefficient whose normalized iid sum has variance65/128 at every repeated
volume. Averaging over black cubes gives variance1/52 at radius1 and
25951/1372554304 at radius10. Thus mean-current cancellation alone really
would be insufficient; the replacement proof supplies the missing control.

A complete256-state one-exceptional-color sector on an admissible irregular
matching checks exact uniform stationarity and the symmetric swap form of
a nonreversible generator. Numerical semigroup integration at times0.1
and0.7 gives integrated variances0.0998284345 and1.5961041483, below the
forward/backward bounds0.2730104689 and1.9110732826. These are finite controls
of the reconstructed identity, not numerical proof of the uniform limit.
Forty-five exact finite canonical count profiles separately check sampling
without replacement. Short-torus controls retain the N>=8 boundary.

After the pre-seal, selected complete event-rate catalogs on winding and
irregular N=8 matchings were independently rebuilt and compared under both
parity choices:1,280 and1,104 distinct physical actions agreed exactly.
The published equal-color tangent characteristic polynomial agrees, and
the generic full-support derivative satisfies A_i C=C A_i^T exactly.
Every author group/result/log binding authenticates. The complete author
suite, N=32 block fixture and FFT calculation were not replayed. Their stored
counts and numerical values are author evidence, not additional independent
computations.

## Formation and field scope

The even quartic code has positive-measure A and B regions, transitive cubic
color orbits and color-restricted first moment zero. Therefore the proposed
birth density has total edge rate beta and history-independent even-color
law p, while its one-record law depends on neighboring vacancies as stated.
This is a supplied exact-content classification, not a physical unknown-qubit
measurement procedure.

At partial density the fallback is local and parity independent; no partial
product stationarity is needed or claimed. Geometry and accumulated birth
colors project to the autonomous geometric process with iid color increments.
The final counts are multinomial and independent of the geometric history.
At fixed volume, the post-filling color chain mixes within each count sector;
mixing these counts gives pi_p independently of final geometry only in the
additional elapsed-time limit. This ordered argument does not prepare product
colors at first completion or give a simultaneous schedule.

The theorem requires fixed positive full-support p, fixed rates, fixed finite
times/modes and full frozen matching geometry during the propagation window.
It does not establish nonstationary hydrodynamics, a uniform result as p
approaches a boundary, microscopic preparation time, or high-mode/long-time
limits. The two-endpoint site color field has limiting covariance2C; its
normalization differs from independent site colors. The geometric Gauss field
remains static. It is not identified with the propagating color sector, whose
longitudinal and other conserved fluctuations remain present.

## Failures and reproduction

Two independent-check failures are preserved. The first attempted to obtain
an irregular fixture by plaquette flips from a maximal-winding matching,
which has no flippable squares. It correctly failed the nonzero direction-
variance assertion; irregular fixtures were then initialized from a separate
ordinary columnar matching. The winding fixture was retained. The second
was a comparison-helper parse failure because `lambda` is a Python keyword;
renaming the serialized variable for parsing fixed it. Neither changed a
primary source, mathematical target or stored author value.

Runnable sources are `independent_check.py`, `replacement_control.py` and
`compare_author.py`, with complete logs/receipts. Python, NumPy, SciPy and
SymPy are required. Reproduce in a fresh sibling directory to preserve sealed
outputs; the comparison also needs copies of the seventeen precomparison
artifacts and their seal, which authenticate the original absolute paths.
F1 is the only requested correction. No primary source or earlier evidence
was modified.
