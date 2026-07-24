# Finite Flat-Link Even-CAR Support Census Bounded Theorem

Date: 2026-07-23

Claim type: bounded_theorem

Authority: none

Audit: unset

Runner: [`scripts/frontier_finite_flat_link_even_car_support_census_2026_07_23.py`](../scripts/frontier_finite_flat_link_even_car_support_census_2026_07_23.py)

Runner cache: [`logs/runner-cache/frontier_finite_flat_link_even_car_support_census_2026_07_23.txt`](../logs/runner-cache/frontier_finite_flat_link_even_car_support_census_2026_07_23.txt)

## Exact claim

For the supplied finite graph/link Pauli data at periodic sizes `L=3,6,7`, the
runner proves the displayed stabilizer ranks, quotient invariants, complete
onsite `6 B / 15 H` incidence algebra, support census for the displayed `32N`
factor list, finite support coloring, canonical six-mode matrix fixtures, and
the stated covariance controls. Here `N=L^3`.

This is a support/census theorem. It does **not** construct an encoding
`E : M64 -> physical M2 code`, a physical update `G_physical`, or the required
intertwiner

```text
E G_coarse = G_physical E.
```

The canonical `64 x 64` word reconstruction and the graph/link Pauli census
are separately proved objects. The runner does not identify them by an
isometry or representation map. Consequently this note does not claim a
physical-site compiler, a finite local update generator, term completeness,
or an autonomous law.

## Repaired onsite algebra

The three reverse pairs `(0,1)`, `(2,3)`, `(4,5)` are absent as direct graph
edges and use a two-edge path through the first admissible third mode in
ascending local mode order. The correct Hermitian bilinear is

```text
H_lr = -HermitianNormalize(A_lh A_hr),   l < r,
H_rl = -H_lr.
```

The two-edge product already contains the helper-mode fermionic parity.
Multiplication by an additional `B_h` cancels that parity. The remaining minus
sign fixes the ordered-pair orientation against the twelve direct edges, as
checked by `H_ij H_jk H_ik = -i` on code for every `i<j<k`. The former formula
therefore failed the even-CAR endpoint-incidence algebra.

The repaired executable checks every cell at `L=3,6,7`:

| L | B rows | H rows | B² failures | B-B failures | H² failures | B-H incidence failures | H-H incidence failures | triangle-phase failures |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 3 | 162 | 405 | 0 | 0 | 0 | 0 | 0 | 0 |
| 6 | 1,296 | 3,240 | 0 | 0 | 0 | 0 | 0 | 0 |
| 7 held | 2,058 | 5,145 | 0 | 0 | 0 | 0 | 0 | 0 |

A separate three-mode operator test covers the five affected coin Givens and
all three reverse FSWAP factors. With the repaired two-edge bilinear, the
maximum Frobenius reconstruction residual is
`2.221417347195572e-16`. Reintroducing the extra helper `B_h` gives operator
residuals from `1.4142135623730947` to `2.0`; this is a genuine negative
control that would have rejected the old expression.

The all-24 derived-bilinear frame test uses one representative of the exact
translation orbit at each size. There are `54` raw Pauli representative
differences per size because the local graph gauge changes, but `0` failures
after phase-aware reduction by the declared local code constraints.

## Finite graph/link invariants

The supplied construction uses 22 graph algebra factors and three link
algebra factors per coarse cell. These are active algebra factors, not a
proved count of embedded physical sites or of the blank/controller/work
resources of a compiler.

| L | active algebra M2 | per cell | combined rank | code exponent | matter quotient dimension | symplectic rank | center |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 3 | 675 | 25 | 484 | 191 | 323 | 322 | 1 |
| 6 | 5,400 | 25 | 3,886 | 1,514 | 2,591 | 2,590 | 1 |
| 7 held | 8,575 | 25 | 6,172 | 2,403 | 4,115 | 4,114 | 1 |

The verified formulas are combined rank `18N-2`, code exponent `7N+2`,
matter quotient dimension `12N-1`, symplectic rank `12N-2`, and a
one-dimensional matter-parity center. At all three sizes:

- graph/link constraint phase inconsistencies: `0`;
- matter/constraint commutator failures: `0`;
- Gauss/matter and Gauss/plaquette commutator failures: `0`;
- plaquette-product equality and link-dressing-type failures: `0`;
- placement collisions: `0`;
- deleting one independent constraint lowers rank by exactly one;
- flipping one redundant correlation phase produces one inconsistency; and
- all eight supplied topological-bit sectors satisfy flatness and wrapping-loop
  character checks.

The eight sectors are lawful finite inputs. Their selection, preparation,
renewal, and coherent physical transport are not constructed.

## Displayed factor support census

The supplied ordered list contains `32N` factors: `10N` coin Givens, `N`
coin phases, `3N` onsite reverse FSWAPs, `3N` spatial link-dressed FSWAPs,
and `15N` contact phases.

| L | factors | colors | sequential layers | maximum Pauli weight | maximum fine-L1 diameter |
|---:|---:|---:|---:|---:|---:|
| 3 | 864 | 7 | 58 | 14 | 452 |
| 6 | 6,912 | 6 | 46 | 14 | 452 |
| 7 held | 10,976 | 7 | 58 | 14 | 452 |

Every reported color layer is support-disjoint. The held `L=7` calculation
uses the same seven-color ceiling without refitting. The 30 stage groups and
their order are supplied host-side data. A layer count is not physical time,
duration, or a transition rate, and no local clock or returned-work controller
is present.

## Canonical M64 word and shrinking-seam fixtures

In the canonical six-mode Fock space, independently of the graph/link code,
the runner reconstructs the ordered onsite word

```text
contact · reverse-FSWAP · coin.
```

The controls are:

- one-particle coin residual: `1.2678063666573761e-15`;
- exterior-coin residual: `5.853291543795948e-15`;
- three-FSWAP reverse-word residual: `0`;
- fifteen-contact residual: `2.2562397986482602e-15`;
- full ordered-word residual: `6.660841388536039e-15`;
- explicit inverse residual: `9.205213384579482e-15`;
- number-sector leakage: `0`;
- mass-fixture residual: `1.1102230246251565e-16`;
- deleted coin-factor operator residual: `0.006811295182974648`; and
- deleted contact-pair residual: `0.36789306705608277`, matching
  `|exp(i 0.37)-1|`.

These are matrix identities in `M64`; they are not an `E G` test.

The `L=3` modular resonance is retained under its correct name as a finite
fixture. Its singular values are
`(0.4957714067049812, 0.45566604871445027)`, its phase residual to `2 pi` is
`0`, its direct spatial reduction residual is `1.1864417069656778e-17`, and
an unbalanced channel has internal norm `0.8448087187256581` but spatial norm
`4.632480828019625e-18`.

The shrinking finite-volume seam sequence retained from historical Cycle 230
is also reexecuted, rather than being replaced by the `L=3` fixture:

| L | wrapped phase | minimum singular value | raw operator/g |
|---:|---:|---:|---:|
| 18 | 0.1038102904479215 | 0.970499830248236 | 1.6640943591362078e-4 |
| 34 | 0.05515539308573963 | 0.9916750873940344 | 2.523089475356286e-5 |
| 78 | 0.024069212818144826 | 0.9984148041719781 | 2.1039102230566485e-6 |
| 416 | 0.004514002770486904 | 0.9998884863600138 | 1.3890568104233032e-8 |

The supplied numerical root selectors are
`k_- = 1.5783929737448452` and `k_+ = 1.563199679844947`. The maximum
all-24 singular-value residual is `3.556181433338904e-15`; the ordinary
`U=+1` crossing comparison residual is `1.8343894894033213e-15`; and the
passive-spectator residual is `3.1031676915590914e-17`. These are conditional
wrapped-phase and contact-form fixtures, not physical energy or probability.

## Covariance boundary

All 24 proper-cubic frames and all 576 ordered products are enumerated. At
`L=3,6,7`, the primitive signed modes, graph `B/A` generators, link dressing,
stars, plaquettes, link homology, and frame-group composition have zero
failures. The derived onsite bilinears have zero on-code failures as stated
above.

The combined code-space question is stricter. A phase-aware `L=3` test finds:

- transported graph-local constraint span failures: `0`;
- fixed supplied Wilson-correlation-section span failures: `648`; and
- fixed combined code space invariant under all 24 frames: `false`.

Combined-code covariance was executed only at `L=3`; it was not extrapolated
to `L=6,7`. Covariance of a separately transported chart is true by the
supplied compile-time transport convention, but it does not make one fixed
code section covariant and is not a runtime physical mechanism. Therefore
proper-cubic covariance of a physical compiler is not established.

## Supplied-structure and execution-convention inventory

Every load-bearing discretionary input is exposed:

- Python standard-library facilities, NumPy, and `scipy.linalg.schur` are the
  complete runtime import surface; no mutable repository artifact is imported;
- the signed-mode order is
  `(+x,-x,+y,-y,+z,-z)`, with reverse map `(0 1)(2 3)(4 5)`;
- `beta=-0.3`, contact coupling `g=0.37`, inertial-mass fixture
  `m=3 tan(-beta/2)`, and the exact coin
  `C=exp(i m/3)(P_scalar-P_even+exp(i beta)P_vector)`, where
  `P_scalar=|s><s|`, `s=(1,1,1,1,1,1)/sqrt(6)`,
  `P_even=(I+R)/2-P_scalar`, and `P_vector=(I-R)/2`;
- the Pauli convention is `i^phase X^x Z^z`, with product phase increment
  `2 popcount(z_left & x_right)` modulo four;
- periodic domains `L=3,6,7` and the seam sizes `18,34,78,416`;
- square-pyramid, sink, spoke, rough-terminal, and flat-link incidence;
- ascending construction-index order for incident graph edges;
- the first-admissible-third-mode helper convention for missing reverse pairs;
- a compile-time graph/link correlation section containing nonlocal Wilson
  initializers and three supplied topological bits;
- the four `L=3` target momenta and target phases used to select the modular
  channel;
- the two numerical seam-root selectors;
- sparse placement scale `K=129`, periodic fine-coordinate modulus `2 K L`,
  cell centers `2 K x`, terminal offset `0`, spoke offsets `8 d_mode`, internal
  offsets `4(d_left+d_right)`, outer-edge offsets `32 d_source`, and link
  midpoints displaced by `K` along their axes;
- Wilson loops based at `(0,0,0)` with transverse mode axis
  `(axis+1) mod 3`; flat-link logical `Z` loops through the origin, logical `X`
  sheets on the coordinate-zero plane, sector-gradient root `(0,0,0)`, and
  topological-bit insertion on positive-axis wrap links;
- the supplied 30 stage groups and factor order, followed by deterministically
  computed greedy first-fit colors within lexicographically sorted stages and
  construction/lexicographic-cell factor order;
- compile-time frame/chart transport; and
- the choice of construction/train/held sizes.

The numerical and selection conventions are also explicit: global residual
tolerance `2e-11`; QR drop/phase cutoff `1e-13`; polynomial coefficient-sign
tolerance `1e-14`; `L=3` band-phase tolerance `1e-7`; unbalanced positive-phase
cutoff `1e-9`; the two eigenvalues nearest each supplied seam target; seam
subspace dimension `2`; seam-root comparison half-width `1e-3`; and RNG seeds
`2302` for degenerate-band rotations and `230` for the spectator control.

The load-bearing acceptance bounds are: `L=3` phase residual `<3e-14`, ordered
singular minima `>0.49,0.45`, form norm `>0.67`, spatial/momentum residuals
`<2e-15`, unbalanced internal norm `>0.1`, degenerate-basis residual `<3e-15`,
and frame residual `<2e-13`; seam terminal wrapped phase `<0.0046`, terminal
gap `<0.0077`, degenerate spread `<3e-14`, all-size singular minimum `>0.97`,
terminal singular minimum `>0.9998`, terminal singular-maximum residual
`<2e-4`, crossing/frame residuals `<3e-13`, plus-crossing phase cost `<7e-4`,
and spectator residual `<2e-15`; extra-helper-`B` residual `>1e-2`; deleted
coin-factor residual `>1e-3`; and support bounds of at most seven colors, 58
sequential layers, and Pauli weight 14. Diameter gates are stated in units of
the supplied embedding: factor and Gauss diameter at most `4K`, plaquette
diameter at most `2K`.

The nonlocal correlation section is not hidden behind the phrase “no runtime
Wilson table.” Its largest row has weight/diameter `34/903` at `L=3`,
`52/2314` at `L=6`, and `58/2451` at `L=7`. It is supplied at compile time.
No runtime global Jordan-Wigner ordering or parity service occurs in the
evaluated Pauli formulas, but a local incident-edge ordering is supplied.

Not supplied or constructed as executable resources are a physical `E`, a
blank physical M2 reference preparation, a local frame/chart register, an
autonomous controller, a clock, placement dynamics, a returned-work band, or
reference/topological-sector genesis.

## Route disposition and N1-N8 discipline

- Direct bounded-block route: partial positive algebra/support census; no `E`.
- Local gauge/auxiliary route: partial positive local constraints and dressing;
  the fixed Wilson section fails the tested combined covariance condition.
- Staggered/time-multiplexed route: partial positive finite coloring; schedule,
  chart transport, controller, blanks, and returned work remain supplied or
  absent.

N1 enumerates these routes plus transported-chart and local-genesis
constructive alternatives. N2 keeps the missing `E`, fixed-chart covariance,
controller, and genesis logically separate. N3 exposes the ordering, helper,
Wilson, chart, blank, and work imports. N4 reproduces the former helper-parity
failure and restores the shrinking-seam fixture with historical Cycle 230
provenance. N5 restricts every conclusion to the tested resolution. N6 lists
constructive partial-closure paths. N7
steelmans a coherent chart register with a reversible color clock. N8 prevents
the canonical M64 word from being promoted to a physical M2 intertwiner.

Broad negative gate: **FAIL / DO NOT SHIP**.

Minimum-content gate: **FAIL / DO NOT SHIP**.

Shared-obstruction gate: **FAIL / DO NOT SHIP**.

Axiom-pressure gate: **FAIL / DO NOT SHIP**.

No route-independent obstruction has survived the three constructive
attempts. No impossibility, minimum-content, shared-obstruction, or axiom
pressure claim is made.

## Prior-art and novelty boundary

Fermionic even-algebra encodings, auxiliary/gauge fields, Pauli stabilizer
rank calculations, exterior-algebra lifts, QR/Givens factorization, fermionic
swap identities, and greedy support-conflict coloring are established
techniques. Representative background includes Bravyi and Kitaev’s fermionic
quantum computation formalism ([Annals of Physics 298 (2002)](https://doi.org/10.1006/aphy.2002.6254))
and higher-dimensional auxiliary-field removal of nonlocal Jordan-Wigner
strings by Verstraete and Cirac ([J. Stat. Mech. P09012 (2005)](https://doi.org/10.1088/1742-5468/2005/09/P09012)).

The narrow result here is the corrected, self-contained coexecution of the
specific finite graph/link rank and support data, all-15 onsite incidence
tests, helper-parity negative control, canonical M64 word, held-size census,
fixed-chart covariance boundary, and restored shrinking-seam fixtures
(historical Cycle 230 provenance). No novel encoding principle, arbitrary-size
theorem, continuum limit, empirical prediction, or broader priority is
claimed.

## Scope

This note establishes only the bounded finite support/census result above. It
does not establish a physical-site compiler, autonomous law, state/reference
genesis, physical time, physical energy, source, stress, gravity, framework
Record, occurrence, probability, or Born weighting. The independent audit
lane alone may assign audit or effective status.
