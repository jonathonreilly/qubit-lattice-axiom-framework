# SU(2) mass-gap lane: proof tree and open dependencies

Working map for [PR #10149](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/10149),
2026-11-09. Continue on this PR and branch; no dependency stack is required.
The map covers the present research route. It does not claim that the listed
open nodes form a proved reduction of the mass-gap problem or an exhaustive
list of every lemma a continuum construction will need.

The present results are finite two-step posterior decay with terminal field
fixed to identity, and compact connected response for the actual seven-edge
two-plaquette marginal, including its conditional-normalizer subtraction.
Their exact checking records are linked below; they do not constitute formal audit or retained status. There is no proved physical
mass gap and no evidence-based completion percentage or delivery date.

## Target and decision order

For the SU(2) starting case, the eventual target is a nontrivial continuum
Yang-Mills theory on R^4 satisfying the required QFT axioms, with a positive
finite mass and a gap above the vacuum in the physical energy spectrum. The official problem
asks for every compact simple gauge group; this lane currently treats SU(2).
See [Jaffe and Witten's problem statement](https://www.claymath.org/wp-content/uploads/2022/06/yangmills.pdf).
An auxiliary conditioned Hessian or decay rate in block units is not that
spectral statement. No TOE identification follows from the present work.

```mermaid
flowchart TD
  E[Exact normalized two-step chain and forest quotient]
  H[Actual flat precision and local nonlinear chart]
  C[Chart connected fourth response]
  R[Compact coercivity and regional comparisons]
  P[Exact source-marked compact decomposition]
  G[Frozen Gaussian suppliers and density forest]
  B[Full compact identity-terminal response]
  Q[Exact partial-terminal law and full cumulance identity]
  K[Seven-edge compact coercivity and actual flat precision]
  U[Marginal nonlinear chart, regional energy, moments and ratio jets]
  Pj[Marginal exact compact gas and actual Gaussian producers]
  Dj[Marginal connected-density expansion and fourth response]
  D[Identity two-plaquette conditional with Q subtraction]
  V[OPEN: required nonidentity terminal control]
  T[OPEN: third transition and inherited-action closure]
  S[OPEN: depth and cutoff control at physical scales]
  X[OPEN: nontrivial continuum QFT reconstruction]
  M[OPEN: positive physical spectral gap]
  E --> H
  H --> C
  E --> R
  R --> P
  H --> G
  P --> G
  C --> B
  G --> B
  E --> Q
  R --> K
  Q --> K
  K --> U
  Q --> U
  U --> Pj
  Pj --> Dj
  G --> Dj
  B --> D
  Q --> D
  Dj --> D
  D -. research route .-> T
  V -. research route .-> T
  T -. unproved iteration .-> S
  S -. unproved limits .-> X
  X -. unproved spectral step .-> M
  S -. unproved physical decay .-> M
```

Solid arrows summarize the current finite-model argument. Dotted arrows
are proposed research dependencies with open hypotheses, not established
implications. The exact-Q and marginal nodes have separate source/check records below.
The direct marginal estimate bounds the complete conditional cumulant,
without discarding any of the 15 total-cumulance terms.

## Complete current finite-model packet

All twenty earlier proof parts are listed here. Their exact SHA-256 identities
and the primary note are bound by the manifest and the frozen reports linked
from [HANDOFF](HANDOFF.md). Historical author headers describe their original
draft state; subsequent gate reports carry the actual checking record.

| Part | What it supplies and where it is used |
|---|---|
| [Compact forest exchange](parts/compact-forest-exchange.md) | Exact Haar quotient, source-dependent orbit law, aligned exchange and true reader sets. Starting law for all branches. |
| [Flat two-step bound](parts/flat-two-step-bound.md) | Actual two-layer precision with both normalized kernels, at fully fixed terminal I. Input to chart and Gaussian estimates. |
| [Nonlinear chart response](parts/nonlinear-chart-response.md) | Local derivatives, chart coercivity and covariance machinery. Input to connected chart and Gaussian producers. |
| [Compact energy coercivity](parts/compact-energy-coercivity.md) | Compact energy control for the pinned two-step model. Input to compact/regional estimates. |
| [Rough density bound](parts/rough-density-bound.md) | Absolute compact-versus-chart density accounting; includes normalization powers. |
| [Local conditional tail](parts/local-conditional-tail.md) | Local conditional tail bounds under its stated exterior hypothesis; not general influence contraction. |
| [Local relative coercivity](parts/local-relative-coercivity.md) | Relative-energy supplier for conditional component estimates. |
| [Rough component bound](parts/rough-component-bound.md) | Component geometry and tails using that relative supplier; not itself a connected logarithm. |
| [Full compact fourth scaling](parts/full-compact-fourth-scaling.md) | Compact local moment and fourth-response scaling; separate from spatial connected decay. |
| [Chart fourth connected bound](parts/chart-fourth-connected-bound.md) | Complete connected cut cancellations and the chart C/u tree bound. |
| [Original-source response](parts/original-source-four-response.md) | Exact orbit covariance correction and its source-class distinctions. |
| [Arbitrary-boundary interior moments](parts/arbitrary-boundary-interior-moments.md) | Interior moment/radial estimates with the specified buffered boundary setup. This does not mean arbitrary terminal backgrounds are solved. |
| [Buffered conditional ratio](parts/buffered-core-conditional-ratio.md) | Regional log ratios with complete source jets and buffers. |
| [Global chart-sector ratio](parts/global-chart-sector-ratio.md) | Exact sector comparisons; an input, not a replacement for a connected expansion. |
| [Two-step compact decomposition](parts/two-step-compact-polymer-decomposition.md) | Exact compact insertion gas for the actual two-step density. |
| [Source-marked decomposition](parts/source-marked-compact-decomposition.md) | Complete source factors, regional denominators and source readers. |
| [Frozen Gaussian producers](parts/frozen-gaussian-producers.md) | Actual fixed-reference covariance, path norms and local Taylor remainders. |
| [Scalar-leg forest count](parts/scalar-leg-forest-count.md) | Combinatorial bound consumed by the density forest. |
| [Zero-shift density forest](parts/zero-shift-marked-density-forest.md) | Connected correction with normalized Gaussian density jets, full-cell activation and all reader costs. |
| [Full connected response](parts/full-connected-four-response.md) | Exact supplier match, compact/chart composition, original-source correction and weighted boundary-pair sum. |

The last composition is checked in the
[composition gate](gates/full-connected-four-response-check.md); the
[primary note](../../../../docs/SU2_CONNECTED_FOUR_RESPONSE_BOUNDED_THEOREM_NOTE_2026-11-09.md)
has its own [text/source gate](gates/primary-note-check.md).
These are same-provider fresh-context research checks. Formal independent
audit remains separate, and all frozen proof bytes remain unchanged here.

The composed claim is for fixed L and kappa, sufficiently large u, finite
volume uniformly, exactly two hidden layers, V=I and distinct terminal links.
Fixed local C^2 quotient singlets have a C/u four-region tree bound.
Original sources retain their conditional orbit covariance, with the stated
O(1) allowance when orbit readers overlap. This is not arbitrary-boundary,
all-depth, continuum, or physical spectral control.

## Work in this PR after the first publication

| Node | Exact deliverable | Current scope |
|---|---|---|
| Q-exact | [Partial-terminal normalization](parts/partial-terminal-normalization.md) | Exact deletion of integrated last-layer kernels, the two distinct-link derivative cases, and all 15 total-cumulance partitions. Fresh-context proof check completed; see the separate report below. |
| Q-geometry | [Released terminal gauge directions](parts/released-terminal-gauge-directions.md) | Explicit residual component-gauge symmetry and precision eigenvectors on the unchanged forest slice. Fresh-context proof check completed; see the separate report below. |
| Q-coercivity | [Seven-edge compact estimate](parts/two-plaquette-compact-coercivity.md) | Recovers all seven missing constraints through an unused coordinate direction, with positive local discrepancy forms and volume-uniform coefficient bounds. Identity exterior, zero sources, all compact configurations. |
| Q-precision | [Actual normalized marginal Hessian](parts/partial-terminal-normalizer-hessian.md) | Exact finite-u Hessian for arbitrary deletion, conditional coercivity transfer, and its application to this seven-edge set. Every surviving radial normalizer and coordinate-Haar term is retained. |
| Q-chart | [Marginal nonlinear chart](parts/marginal-nonlinear-chart-estimates.md) | Actual finite-u convexity, finite-order derivatives and weighted covariance on fixed Cartesian cubes and principal restrictions, with all readers small. Includes a direct cube-corner/mixed-domain argument. |
| Q-relative | [Marginal regional relative energy](parts/marginal-regional-relative-coercivity.md) | Small hidden-reader collar, measurable stationary leading field, exponential penetration, all-compact relative coercivity and cap upper bound. This leading-energy statement does not assert a finite-u normalized-action minimum. |
| Q-normalized | [Complete normalized regional energy](parts/marginal-normalized-regional-coercivity.md) | Uniform in all u>=1: the actual Haar-density mode, exponential penetration, global compact relative coercivity and cap upper bound under a small hidden collar. Also strengthens the chart Hessian bound to u c_J/2+1/2 for all u>=1 on a smaller cube. |
| Q-regional | [Marginal moments and buffered ratios](parts/marginal-regional-moments-and-ratios.md) | Arbitrary quotient exterior, complete surviving factors, radial-profile interior moments and full two-source/two-distinct-boundary jets of the buffered whole-core-rough correction. It is not an all-good-chart or spatial connected estimate. |
| Q-compact | [Marginal source-marked compact gas](parts/marginal-source-marked-compact-decomposition.md) | Exact complex-source insertion identity with actual surviving counts, source-dependent regional denominators and complete readers. |
| Q-Gaussian | [Actual marginal Gaussian producers](parts/marginal-frozen-gaussian-producers.md) | Exact normalized nontranslation-invariant Hessian; positive covariance core, symmetric paths, whole-cell vertices and all physical prefactors. |
| Q-bound | [Marginal connected expansion and response](parts/marginal-connected-density-expansion.md) | Actual compact activity count, F1–F7 match, connected compact/chart correction, C/u singlet tree response, original orbit covariance and exact seven-edge conditional subtraction at identity. |

[The separate continuation check](gates/partial-terminal-check.md) reconstructs
both new arguments. It does not promote them to formal retained status.

The compact and precision continuation has its own
[complete check](gates/two-plaquette-coercivity-check.md) and
[primary theorem note](../../../../docs/SU2_TWO_PLAQUETTE_MARGINAL_COERCIVITY_BOUNDED_THEOREM_NOTE_2026-11-09.md).
Historical author headers remain frozen; the gate records subsequent checks.
The new bound is uniform in volume, pair placement/orientation and arbitrary
internal trees, including zero means and m=3 seams. It closes the named
compact supplier for this geometry; it is not a connected-cumulant estimate.

The subsequent [regional/chart primary note](../../../../docs/SU2_MARGINAL_REGIONAL_AND_CHART_ESTIMATES_BOUNDED_THEOREM_NOTE_2026-11-09.md)
composes the four new suppliers above. Their exact mathematical and claim-
surface checks are indexed in REVIEW_HISTORY. Compact regional estimates
fix terminal exterior I; only the chart theorem allows a small nonidentity
terminal neighborhood. General original sources keep their joint orbit
integral and conditional covariance in the regional ratio derivatives.

If both varied links lie in the exterior, the log-conditional response
subtracts a fourth cumulant under a different hidden marginal. The exact
conditioning formula contains the expected conditional fourth cumulant,
four third-cumulant/mean covariances, three covariance/covariance terms,
six third cumulants of one conditional covariance and two means, and the
fourth cumulant of the means. The new direct marginal proof bounds their combined value on the full
compact released-terminal integration domain through the exact rho_J law;
it does not assert that the individual terms vanish. The first pi_I theorem
alone did not supply that bound.

The geometry diagnostic also prevents indiscriminate reuse of the fully
pinned precision bound: at zero sources and V_O=I, when the retained terminal
graph has r components, the current slice has 3(r-1) explicit gauge directions
of precision 2/(3u).
The eight-edge isolated-vertex example is NOT the seven-edge two-plaquette
problem. It directs attention to the correct quotient and geometry, without
claiming physical masslessness or ruling out this route.

## Marginal compact/connected milestone

The [new primary note](../../../../docs/SU2_MARGINAL_CONNECTED_RESPONSE_BOUNDED_THEOREM_NOTE_2026-11-09.md)
composes the actual compact gas and Gaussian producers with the existing
abstract density-forest theorem. The core union determines its unique
components; an explicit animal count pays all shell, reader and Gaussian
costs. Its connected compact/chart correction is O(exp(-c log(u)^(2A))).
The actual marginal chart covariance then gives the C/u connected fourth
response for fixed C2 quotient singlets, with boundary-pair summability.
Original source reconstruction retains the O(1) conditional-orbit allowance.
The complete p_J=N/Q_J coefficient is controlled by the two actual laws.

The [independent mathematical check](gates/marginal-connected-expansion-check.md)
records its own derivations before new author proofs, exact normalization
and reader discriminators, and final-file scope. Its result and the separate
Fable approach record are indexed in REVIEW_HISTORY. This is bounded-support
research evidence, not formal audit or a recertification of every ancestor.
The three earlier primary notes remain frozen historical milestones; this
map and the new primary give the current result.

## Next theorem to attack and its acceptance test

The identity-exterior seven-edge normalization task is now the stated local
milestone. The next supplier is compact connected control on an explicitly
specified nonidentity terminal-background class, preserving actual kernel
normalizers and source readers. A first bounded target is a fixed small
terminal neighborhood: construct the actual centered field, prove full
compact relative coercivity around it, and transport the source-marked
connected estimate with constants uniform in volume and background.
The existing small-chart theorem is useful, but it does not control that
background's compact complement. An extensive action comparison is not a
uniform local bound.

Before using this as an iteration theorem, specify which larger conditional
geometries and rough terminal components an exact third transition needs.
It is not established that an everywhere-small background class suffices.
The third-transition test must use the actual inherited law, not a new
Wilson density, and must pay every new reader and normalization cost.
These tasks remain open rather than being assumed in an arrow of the map.

Reachability is reassessed on those estimates: do their constants survive
the iteration and physical-scale limit required by the target? Until that
question and continuum reconstruction are answered, the repo supplies a
concrete research attack rather than evidence that the mass gap is near.
