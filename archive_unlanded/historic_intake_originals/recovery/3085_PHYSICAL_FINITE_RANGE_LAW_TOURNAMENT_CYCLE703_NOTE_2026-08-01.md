# The executed double-relational ratio suite finds no matching finite-range competitor: scale-blindness and isotropy lemmas, a nonsingular first-order response, a 63-law grid tournament, and an adversarial ghost search — Cycle 703

Date: 2026-08-01

Claim type: bounded_theorem

Authority: none. Audit: unset. Constitutional effect: none. This cycle edits no axiom, foundation, Qualification, primitive, registry, policy, queue, audit-status, or PR-control surface. No new axiom or primitive is proposed or adopted.

No coupling value, sign, or scale is selected or derived in this cycle; every such object is named as supplied.

Runner: `scripts/physical_finite_range_law_tournament_cycle703_2026_08_01.py`
(33 PASS / 0 FAIL, exit 0).

## What this cycle establishes

Hold the Cycle-700 readout chain fixed — its frozen source, its two detector
pairs, its double-relational ratio — and vary only the lattice law. The supplied
competitor family is

    A_L(w) = A_L + w_F S_F + w_B S_B + w_2 S_2,    w = (w_F, w_B, w_2) >= 0,

where `A_L` is the Cycle-700 nearest-neighbour operator on the odd box of side
`L` and the three shells are built on the twelve face offsets, the eight body
offsets, and the six doubled-axis offsets. Six things are established about this
family, each one under the executed protocol.

(i) **Lemma 1, exact projective scale-blindness.** For any `c > 0`, replacing a
law `A` by `cA` sends the response `phi` to `phi/c`, so both detector
differences scale by `1/c` and the double-relational ratio is exactly invariant.
Measured at `L = 13` against scale factors `2.0`, `0.5` and `17.0`, on the
nearest-neighbour law and on the mixed law `w = (1/2, 1/4, 1/4)`, the ratio moves
by at most `1e-12`. The consequence is structural, not incidental: this readout
suite can identify a law at best projectively, so the nearest-neighbour weight is
normalized to `1` without loss and the family's honest parameter space is exactly
`(w_F, w_B, w_2)`.

(ii) **Lemma 2, isotropic second moments.** Each shell's offset second-moment
tensor `sum_d d_i d_j` is `m` times the identity with `m = 2` for the
nearest-neighbour axis shell and `m = 8` for each of the three deformation
shells; every cross moment vanishes exactly. The small-`k` symbol
`lambda_w(k) = sum_s w_s sum_d (1 - cos(k . d))` therefore has the isotropic
quadratic limit `sigma_w |k|^2` with the single scale
`sigma_w = 1 + 4 (w_F + w_B + w_2)`, and by Lemma 1 the readout is blind to
`sigma_w`. The quadratic limit is confirmed numerically: at
`w = (1/2, 1/4, 1/4)`, where `sigma_w = 5.0`, the deviation of
`lambda_w(k)/|k|^2` from `sigma_w` falls by a factor of about `4` when `|k|` is halved.
The leading continuum order thus carries zero discriminating information about
`(w_F, w_B, w_2)`: everything this tournament measures is lattice-structure
content beyond the leading continuum symbol.

(iii) **First-order response.** At `w = 0`, with `phi0 = A_L^{-1} q_L` and `n`,
`d` the two detector differences of the ratio `n/d`,

    d ratio / d w_s = ( n(u_s) d(phi0) - n(phi0) d(u_s) ) / d(phi0)^2,
    u_s = -A_L^{-1} (S_s phi0),

so every Jacobian entry is an exact solve reusing the factorization of `A_L`. The
`3 x 3` matrix `J`, rows `L = 9, 13, 19` and columns face, body, doubled axis, is
(four significant figures; the runner prints full precision)

    -0.9311   -4.3125    7.4268
    -2.2975   -5.8541    4.9228
    -2.400    -5.9821    4.8279

and every entry is confirmed against a central finite difference at two step
sizes, whose error falls with the expected second-order convergence ratio.

The singular values of `J` are `1.400e+01`, `2.702e+00`, `6.662e-03`, so
`sigma_min = 0.00666167073733` is strictly positive: no deformation direction of
this family — not even with sign-unrestricted weights — is ratio-flat at first
order.

The smallness of `sigma_min` is structural rather than marginal. The `L = 13` and
`L = 19` rows are nearly collinear: their deviation from collinearity, one minus
the cosine of the angle between them, is `2.4370097294e-04`. Both boxes are
already close to the common infinite-volume response, so the two rows carry
nearly the same directional information, and what remains to discriminate them is
finite-size lattice structure rather than the continuum limit they share. The
right singular vector of the smallest singular value is
`(-0.8583, 0.4831, 0.1730)`, mixed in sign: neither it nor its negative has all
components non-negative, so the near-flat direction lies outside the supplied
conic family in both orientations and is not a supplied competitor at all.

The honest in-family first-order statement is therefore conic. On the weight
simplex `{u >= 0, sum u = 1}` the map `u -> max_L |(J u)_L|` is convex and
piecewise linear, and its minimum over the simplex is

    conic_min = 0.855038073072   at   u = (0.786289037867, 0, 0.213710962133),

which is `228.266836261` times the box-19 convergence residual
`0.003745783167973915`. Within the supplied family and under the executed
protocol, every infinitesimal competitor moves at least one of the three box
ratios at linear rate at least `conic_min` per unit total weight.

(iv) **The grid tournament.** The 63 supplied laws `w` in `{0, 1/4, 1/2, 1}^3`
minus the origin were each evaluated at `L = 9, 13, 19` — 189 ratios, every one
finite. With `sep(w) = max_L |ratio_w(L) - ratio_NN(L)|` and the comparison scale
`THR = 10 * staticerr19 = 0.0374578316797`, where
`staticerr19 = |ratio_NN(19) - R_pred_split| = 0.003745783167973915` and the
ten-fold form is the one Cycle 700 used for its own range discriminator, the
least separation anywhere on the grid is `0.1275845602`, attained at
`w = (1/4, 0, 0)`, a margin of `34.0608504224` over `THR`. The three pure
single-shell laws at weight `1/4` separate by `0.1275845602` (face),
`0.307962596333` (body) and `1.7394008584` (doubled axis). Within the supplied
family and under the executed protocol, all 63 competitors separate from the
nearest-neighbour law by more than `THR`.

(v) **The adversarial search and the held-out boxes.** A grid of four values per
axis is coarse, so the runner also searches the continuous domain `[0, 1]^3` for
a ghost law: a nonzero deformation whose separation per unit deformation is
small. The objective is `obj(w) = sep(w) / |w|_1`, with probes at `|w|_1 < 1e-3`
skipped; by (iii) its small-`w` limit along a simplex direction `u` is
`max_L |(J u)_L|`, bounded below by `conic_min`. The search is a fully
deterministic coordinate pattern search with no randomness anywhere: 12 fixed
starts, six axis probes per iterate, move to the best strictly improving probe
and otherwise halve the step, initial step `0.25`, stop at step below `1e-3`, a
per-start probe cap of 250, and a 700-second budget guard that prints how many
starts it skipped. All 12 starts completed, none hit the probe cap, none was
skipped, and 1106 probes were evaluated.

The best point found is `w* = (0.129140625, 0.26, 0)`, with
`obj_min = 0.344291566006` and `sep(w*) = 0.133977835178` — an order above `THR`.
Within the searched domain and under the executed protocol, no competing law
matched the ratio suite. On the four held-out boxes `L = 7, 11, 15, 17`, which
take no part in either the grid or the search, `w*` separates by `1.79210094375`
and the grid argmin by `1.45247757261`, both far above `THR`, so the separation
is not an artefact of the three ladder boxes used to find it.

(vi) **Saturation: the first-order slope overstates finite deformations.** Along
the pure face-shell ray `w = (eps, 0, 0)` the box-19 secant
`s(eps) = (ratio_w(19) - ratio_NN(19)) / eps` is

    eps  = 1e-3      1e-2      5e-2      0.1
    s    = -2.38393  -2.24735  -1.73125  -1.24214

strictly decreasing in magnitude. Its small-`eps` end recovers the analytic entry
`J[19, face] = -2.400` to `6.5e-03` relative, and its `eps = 0.1` end is, to
`1e-9`, exactly the Cycle-700 landed secant
`(-4.0411929130059585 - (-3.9169789686578382)) / 0.1 = -1.24213944348`; the same
code path produces the whole curve, which wires the landed Cycle-700 row into it.
The ratio of the two ends is `1.93187005476`: the landed competitor at weight
`0.1` responds at roughly half the first-order slope. First-order estimates
therefore overstate finite deformations here, and it is the tournament's direct
measurement, not the linearization, that carries the identification content
within the supplied family.

Taken together: within the supplied three-shell family and under the executed
protocol, no competing law matched the executed ratio suite — not one of the 63
grid laws, not the adversarial optimum over the continuous domain, and, at first
order, no infinitesimal deformation whatever. Cycle 700's own successor test says
that a competing law matching every ratio row at every box size would show that
this ratio suite does not identify the nearest-neighbour law; for this supplied
family and under this protocol, that conditional is answered in the negative,
because no such competitor was found.

## The wall this addresses

Cycle 700's landed note names the experiment this cycle executes, under its
header `## The single next discriminating experiment`:

Generalize the range-mutation row: replace the supplied nearest-neighbour law
with any competing finite-range law and compare the double-relational ratio
against the Bessel-Green prediction. The executed separation is
`0.12421394434812028`; a competing law that matched every ratio row at every
box size would show that this ratio suite does not identify the
nearest-neighbour law. Empirical law falsification would additionally require
an observed target and an uncertainty model, neither of which is supplied here.

The same note fixes the stance that this cycle keeps:

This is a comparison between two supplied
model laws, not an empirical falsification of the nearest-neighbour law.

Cycle 700 executed exactly one competitor, its face mutation at weight `0.1`.
That is a single point, and a single point cannot say whether the readout suite
discriminates laws or merely registered one unusually large deformation. This
cycle supplies the family the point sits inside, an exact first-order response
theorem on that family, a full grid tournament, and an adversarial search for a
ghost law. Everything remains a comparison among supplied model laws.

## Construction

The three deformation shells are the twelve offsets that are all permutations of
`(+-1, +-1, 0)`, the eight offsets `(+-1, +-1, +-1)`, and the six offsets
`(+-2, 0, 0)`, `(0, +-2, 0)`, `(0, 0, +-2)`. One generic builder takes an offset
list and produces the shell matrix in exactly the Cycle-700 face-matrix
convention: off-diagonal `-1` for each in-box shell neighbour, and a diagonal
equal to that site's in-box shell-neighbour count, which varies at the boundary.
The same code path builds all three shells, and the builder's face instance is
compared against Cycle 700's own face matrix for exact equality at `L = 19` and
at `L = 9`; the difference has zero stored entries in both cases, which certifies
the shared builder rather than assuming it.

Each shell matrix satisfies `x^T S x = sum over in-box shell bonds (x_i - x_j)^2`,
verified numerically to `1e-9` relative on a set of test fields, so each shell is
positive semidefinite and `A_L(w)` is positive definite for every `w >= 0`. The
smallest eigenvalue of the fully mixed law `A_13(1, 1, 1)` is computed directly
and is positive.

The readout is Cycle 700's, unchanged and named as supplied: the frozen source
`q_L` with its centre site and its six axial sites at distance `3`, the sparse
`LU` solve `phi = A_L(w)^{-1} q_L`, and the double-relational detector ratio
`(phi[c + (1,0,0)] - phi[c + (2,0,0)]) / (phi[c + (1,1,0)] - phi[c + (2,2,0)])`
about the box centre `c`. The base operator and the three shells are assembled
once per `L`; each law is then at most three sparse additions and one
factorization. Weights
that are exactly zero are skipped in the assembly rather than multiplied in, so
the sparsity pattern of the nearest-neighbour law is bit-identical to Cycle
700's and its landed values reproduce exactly.

The conic minimum in (iii) is computed exactly rather than by search. The
constraint set `{u >= 0, sum u = 1}` together with the nine half-planes
`+-(J u)_L <= t` defines a linear program whose optimum, since the objective is
convex and piecewise linear, is attained at a basic vertex; the runner enumerates
all 84 triples of those half-planes in plain dense arithmetic on the `3 x 3`
Jacobian, keeps the feasible ones, and reports the least objective value found.
A dense simplex grid at spacing `1/400` with a local pattern refinement is kept
as an independent upper-bound cross-check and is gated to lie above the
enumerated minimum and within one grid spacing of it; it returns
`0.855921612833` against the exact `0.855038073072`. No sparse solve enters this
step.

The adversarial search starts from the seven nonzero corners of `{0, 1}^3`, from
`(0.1, 0, 0)`, `(1/4, 1/4, 1/4)`, `(0.05, 0.05, 0.05)` and `(0.01, 0.01, 0.01)`,
and from the grid tournament's own argmin. Held-out evaluation uses
`L = 7, 11, 15, 17`, which appear nowhere in the grid, the search, or the
Jacobian.

## Measured results

| quantity | value |
|---|---|
| Cycle-700 nearest-neighbour ladder, `L = 9, 13, 19` | `-4.112204466641254`, `-3.938488211332885`, `-3.9169789686578382` |
| Bessel-Green prediction, split quadrature | `-3.913233185406517`, `-3.9132331854898643` |
| landed face-mutation readout, `L = 19`, weight `0.1` | `-4.0411929130059585` |
| landed separation, separation ratio | `0.12421394434812028`, `33.161007665936864` |
| box-19 convergence residual, comparison scale `THR` | `0.003745783167973915`, `0.0374578316797` |
| face-shell builder against the Cycle-700 face matrix | exact equality at `L = 19` and `L = 9` |
| scale-blindness deviation, both laws, three scale factors | at or below `1e-12` |
| continuum scale at `w = (1/2, 1/4, 1/4)` | `sigma_w = 5.0` |
| singular values of `J` | `1.400e+01`, `2.702e+00`, `6.662e-03` |
| `sigma_min(J)` | `0.00666167073733` |
| collinearity deviation, rows `L = 13` and `L = 19` | `2.4370097294e-04` |
| near-null right singular vector | `(-0.8583, 0.4831, 0.1730)` |
| conic linear-response minimum, argmin | `0.855038073072` at `u = (0.786289037867, 0, 0.213710962133)` |
| margin of the conic minimum over the box-19 residual | `228.266836261` |
| independent grid-and-refine upper bound on that minimum | `0.855921612833` |
| box-19 face secants at `eps = 1e-3, 1e-2, 5e-2, 0.1` | `-2.38393`, `-2.24735`, `-1.73125`, `-1.24214` |
| `J[19, face]`, landed secant at `eps = 0.1` | `-2.400`, `-1.24213944348` |
| saturation factor between the two ends | `1.93187005476` |
| grid ratios evaluated, all finite | `189` |
| least grid separation, argmin, margin over `THR` | `0.1275845602` at `(1/4, 0, 0)`, `34.0608504224` |
| pure single-shell laws at weight `1/4`: face, body, doubled | `0.1275845602`, `0.307962596333`, `1.7394008584` |
| search bookkeeping | 12 starts completed, 0 skipped, 0 capped, 1106 probes |
| adversarial optimum | `w* = (0.129140625, 0.26, 0)`, `obj_min = 0.344291566006`, `sep = 0.133977835178` |
| held-out separation at `w*`, at the grid argmin | `1.79210094375`, `1.45247757261` |
| nearest-neighbour residuals at `L = 7, 11, 15, 17` | `1.11509560345`, `0.0618059458985`, `0.0121393016167`, `0.00649097380679` |
| sparse solves executed | `1175` |

Three readings deserve naming. First, the doubled-axis shell is by far the
loudest competitor at equal weight — `1.7394008584` against `0.1275845602` for
the face shell — so the tournament's least-separating direction is the one Cycle
700 happened to test, and the executed separation was not a lucky choice of
deformation. Second, the adversarial optimum is not the first-order minimizer:
`w*` mixes face and body weight and switches the doubled-axis shell off, while
the conic minimizer splits between the face and doubled-axis shells and switches
the body shell off. The two need not agree — by (vi) the response saturates with
amplitude, so the finite-amplitude optimum is not determined by the
linearization. Third, the held-out separations exceed the ladder separations by
an order. The held-out set includes `L = 7`, whose own nearest-neighbour residual
against the infinite-lattice prediction is `1.11509560345`, so those boxes
corroborate law-versus-law separation and nothing else.

## What this does not establish

(a) This is not an empirical falsification of anything. No observed target and no
uncertainty model are supplied here, and every comparison in this cycle is
between supplied model laws.

(b) The family is supplied, not derived. It is three cubic-symmetric shells
within range `2` with conic weights. Longer-range shells, anisotropic or
sign-indefinite weights, and non-Laplacian competitors are outside the searched
family and outside every claim made here.

(c) The LATTICE axiom's nearest-neighbour adjacency is an axiom of the framework,
not the object under test. The competitors are supplied comparison objects used
to probe the discriminating power of the executed readout suite; no adjacency
change is proposed, licensed, or implied.

(d) The search certifies the searched domain under the stated deterministic
protocol; it is not a global nonexistence proof. The first-order theorem is exact
only in the small-deformation limit, and (vi) shows that limit understates how
fast the ratio saturates at finite weight.

(e) The geometry is pinned throughout: Cycle 700's source, its detector sites,
odd box sizes, and its box-boundary convention. Nothing here tests an alternative
source, detector placement, or boundary treatment.

(f) By Lemma 1 the suite cannot measure the overall coupling scale at all. That
scale remains named as supplied, exactly as in Cycle 700, and no value, sign, or
normalization for it is selected here.

(g) The held-out boxes are used only for same-box law-versus-law comparisons and
are never compared against the infinite-lattice prediction. At `L = 7` the
nearest-neighbour residual against that prediction is `1.11509560345`, which is
box-boundary geometry rather than a law difference; the held-out role is solely
to confirm that a separation measured on the ladder boxes persists on boxes that
took no part in selecting it.

## Reproduction

`python3 scripts/physical_finite_range_law_tournament_cycle703_2026_08_01.py`
— 33 PASS / 0 FAIL, exit 0, measured wall times between `107` and `154` seconds
across four runs on the executing machine, well inside the registered 900-second
budget. Output is deterministic: repeated runs printed byte-identical
transcripts apart from the recorded elapsed time. The `--no-receipt` flag suppresses the receipt write and leaves the
printed transcript unchanged; invoked without it, the runner additionally writes
`outputs/physical_finite_range_law_tournament_cycle703_receipt_2026_08_01.json`.

## Citations

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [Cycle 700 executed source-response-readout chain](PHYSICAL_OPERATIONAL_SOURCE_RESPONSE_READOUT_CHAIN_CYCLE700_NOTE_2026-07-25.md)

Backticked context only, with no links: `PR #5879`, `PR #5884`,
`PHYSICAL_ORBIT_AVERAGED_ALL24_CARRIER_CYCLE701_NOTE_2026-08-01`,
`PHYSICAL_MULTICOSET_STABILIZER_LATTICE_CYCLE702_NOTE_2026-08-01`,
`scripts/physical_operational_source_response_readout_chain_cycle700_2026_07_25.py`,
and `scripts/physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py`.
