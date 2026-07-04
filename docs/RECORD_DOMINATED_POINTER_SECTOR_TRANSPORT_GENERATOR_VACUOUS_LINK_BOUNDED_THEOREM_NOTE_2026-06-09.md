# The Record-Dominated Compression: an Exact Pointer-Sector Transport Generator and the Vacuous Link Generator

**Date:** 2026-06-09
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Scope:** at the record-dominated compression of the matter-induced composite
link, an exact autonomous CPTP transport generator on the local color densities
(pointer sector) — gauge-covariant, with a strict Lyapunov arrow and an admitted
rate — together with the exact statement that the induced **link** generator is
vacuous (frozen, or a `Z_2` flip), plus a non-autonomy-of-the-link exhibit at
this compression level and the instrument-inheritance of the covariance.
**Script:** `scripts/frontier_record_dominated_pointer_transport_generator_2026_06_09.py`
**Cache:** `logs/runner-cache/frontier_record_dominated_pointer_transport_generator_2026_06_09.txt`
**Status:** source proposal. All statements are finite-dimensional exact algebra
checked by the runner (`PASS=30 FAIL=0`). Authority role: source proposal; the
audit lane sets status.

## The named residual this addresses

The gauge-dynamics convergence note
(`ST1_ST2_SAME_WALL_GAUGE_DYNAMICS_RESIDUAL_CONVERGENCE_NARROW_THEOREM_NOTE_2026-06-08`;
`unaudited` on the live ledger at drafting time) reduces the interacting-gauge
foundation's undelivered input to a continuous-time gauge-link /
color-einselection dynamics, in particular a link generator with arrow and rate
(the link-generator residual). Two sibling results bound the matter-induced composite link
`U_eff = polar(M(x,y))` (the cross-site matter-bilinear unitarization,
`COLOR_LINK_INDEX_ROUTING_VIA_CROSS_SITE_MATTER_BILINEAR_UNITARIZATION_BOUNDED_THEOREM_NOTE_2026-06-08`,
`unaudited`):

- the induced-trajectory note
  ([`INDUCED_COMPOSITE_LINK_TRAJECTORY_COVARIANCE_INCREMENT_LAW_NON_AUTONOMY_BOUNDED_THEOREM_NOTE_2026-06-08`](INDUCED_COMPOSITE_LINK_TRAJECTORY_COVARIANCE_INCREMENT_LAW_NON_AUTONOMY_BOUNDED_THEOREM_NOTE_2026-06-08.md),
  on main, `unaudited`) showed the induced link trajectory exists and is locally
  covariant but is **not autonomous** in `U_eff`; its named not-foreclosed
  routes included **a coarse-grained / averaged compression where the hidden
  data could become slaved**;
- the record-instrument note
  ([`RECORD_INSTRUMENT_COMPOSITE_LINK_POINTER_ERASURE_EXACT_SLAVING_BOUNDED_THEOREM_NOTE_2026-06-09`](RECORD_INSTRUMENT_COMPOSITE_LINK_POINTER_ERASURE_EXACT_SLAVING_BOUNDED_THEOREM_NOTE_2026-06-09.md),
  PR #3425) showed that under named record instruments the link carrier `M(x,y)`
  is erased content, and in the record-dominated regime the link is slaved/frozen
  while the pointer-sector flow is the autonomous object at leading order.

This block works that named compression level **exactly**. The sharp question:
in the record-dominated regime, is there an autonomous generator, and on **what
carrier**? The answer is a clean split — there is a genuine autonomous generator,
but it lives on the **pointer sector (local color densities)**, not on the link;
the induced link generator is **vacuous**.

## The admission, named honestly (this is NOT a derivation)

The formation rule/process is not supplied by the axioms
(`record_formation_not_unconditionally_forced_by_minimal_axioms_narrow_no_go_note_2026-06-06`,
post-append narrowed scope). Any concrete record instrument is therefore a
**named admission**; this note reuses the two block-02 instruments at the
per-site occupancy level (Lueders instruments of this class have a framework-side
Stinespring construction,
`persistent_record_instrument_construction_narrow_theorem_note_2026-05-22`,
ledger `retained_bounded` at drafting time):

- **frame-naming occupation-basis instrument** — per-site occupation-basis dephasing (frame-naming, local color-frame redundancy-shaped);
- **color-blind total-occupation instrument** — per-site total-occupation Lueders (color-blind, names no frame).

Both act at strength `lam in [0,1]` interleaved with exact Hamiltonian steps
`e^{-iH tau}`. The strength `lam`, period `tau`, and which instrument acts are
the admitted content. Nothing here derives that records form or fixes a rate.

## Setting and conditionality (load-bearing, named)

Every statement is conditional on all of: (1) the **supplied `C^3` color
carrier** (`color_su3_matter_realization_residual_map_2026-06-05`, ledger
`meta`; nothing here derives color); (2) **the named model Hamiltonian** — a
single edge `H = kappa [[0,V],[V^dag,0]]` with `V` unitary (free `V = I`, or a
frozen generic `SU(3)` background; the covariant-hopping "connection" reading,
`matter_gauge_minimal_coupling_fiber_frame_forces_connection_narrow_theorem_note_2026-06-08`,
`unaudited`, is **not** consumed — `V` is a named model coefficient and its own
dynamics is not supplied); (3) **the named frame-naming occupation-basis and
color-blind total-occupation instruments with admitted
`(lam, tau)`**; (4) the **>= 3-occupied-mode / rank-3 precondition** of the
composite-link construction. States are one-body density blocks
`0 <= M(x,x) <= 1`; `M(x,y)` is the cross-site one-body block. Because
`H^2 = kappa^2`, the exponential `e^{-iH tau} = cos(kappa tau) - i sin(kappa
tau) H / kappa` is exact (checked against an independent eigendecomposition);
all identities below are exact at full record strength `lam = 1` on the single
edge, with measured `O((1-lam)^2)` windows away from it.

## Verdict (four exact findings)

### 1. An exact autonomous CPTP transport generator on the pointer sector

At full record strength `lam = 1`, the composite step's local blocks obey the
**closed, autonomous** map (exact, `< 3e-16`):

```
  M(x,x)' = cos^2(tau) M(x,x) + sin^2(tau)  V M(y,y) V^dag
  M(y,y)' = cos^2(tau) M(y,y) + sin^2(tau)  V^dag M(x,x) V
```

This map is:

- **CPTP** — it is the random-unitary channel
  `cos^2(tau) * Id + sin^2(tau) * (conjugation by W)`, with
  `W = [[0,V],[V^dag,0]]` the (unitary) edge swap; the swap component exactly
  reproduces `(M(x,x),M(y,y)) -> (V M(y,y) V^dag, V^dag M(x,x) V)`. A convex
  combination of unitary channels is unital CPTP; total occupation
  `tr M(x,x) + tr M(y,y)` is conserved and PSD is preserved (both checked on
  random inputs).
- **Gauge-covariant** — under a joint local rotation `(g_x, g_y)` with
  `V -> g_x V g_y^dag`, the map is exactly equivariant
  `M(x,x)' -> g_x M(x,x)' g_x^dag` (checked to `6e-16`).
- **A genuine generator with an arrow and a rate** (Finding 2).

This is the autonomous object the record-dominated compression delivers. It is
the leading-order behavior at `lam < 1`, with the cross-block (link-carrier)
contribution entering only at `O((1-lam)^2)` (Finding in §Boundaries).

### 2. The arrow and rate: a strict Lyapunov monotone toward link-transported balance

Define the **imbalance** `D = M(x,x) - V M(y,y) V^dag`. Under the pointer map
(exact, `< 8e-16`):

```
  D' = cos(2 tau) D.
```

So the Lyapunov functional `L = ||D||_F^2` obeys `L' = cos^2(2 tau) L`, **strictly
decreasing** for every `tau in (0, pi/2)` off the balance manifold (the
non-contracting cases are exactly `tau = 0`, no evolution, and `tau = pi/2`, a
full swap that preserves `||D||` — checked). The iterate relaxes monotonically
to the **fixed-point manifold** `M(x,x) = V M(y,y) V^dag` (a genuine fixed point,
checked to `2e-16`; `L_0 = 1.44 -> L_40 = 1.1e-16`). The arrow is the
record-accumulation direction; the rate is `sin^2(tau)` per step
(`|cos(2 tau)|` per step on `||D||`), set by the admitted schedule. The flow
equilibrates the two endpoints' local color densities **modulo the link
transport `V`** — color-density consensus along the edge.

### 3. The induced link generator is vacuous (frozen, or a `Z_2` flip)

The composite-link source `s = i(M(x,x) V - V M(y,y))` (so
`U_eff = polar(s)`) obeys, under the **same** pointer map (exact, `< 4e-16`):

```
  s' = cos(2 tau) s.
```

The source contracts **isotropically** — along its own direction — so the polar
factor is unchanged:

- for `cos(2 tau) > 0` (`tau in (0, pi/4)`): `polar(s') = polar(s)` — the link
  is **frozen** (checked);
- for `cos(2 tau) < 0` (`tau in (pi/4, pi/2)`): `polar(s') = -polar(s)` — a
  `Z_2` flip per step (checked).

The only link "flow" is the contraction of the **magnitude** `|s| -> 0`: the
source shrinks toward zero (the link `U_eff = polar(s)` degenerates exactly at
the balance fixed point, where `s = 0`), while its **direction stays frozen**
(direction deviation `< 6e-10` over 30 steps as `|s|` falls from `1.06` to
`1.1e-6`). The induced link generator therefore carries **no arrow and no rate**:
it is the vacuous (`F = 0`) generator. This is a cross-cycle echo of the ledger
entry "equivariance-of-force as dynamics delivery is vacuous (holds for `F = 0`)":
a frozen (or sign-oscillating) link is not the sought link-generator residual generator.

### 4. The link is a lossy coordinate; covariance is instrument-inherited

**Non-autonomy at the compression level (new exhibit).** Two slow-manifold
states with the **same** `U_eff = polar(s)` but **different** imbalance `D` have
**different** autonomous pointer flow. Concrete exact instance: a uniform
downscale `M -> kappa M` (`kappa = 0.5`) leaves `polar(s)` exactly fixed
(`U_eff` is scale-blind, `0.00`) but scales the pointer flow
`Delta M(x,x) = -sin^2(tau) D` by `kappa` (`||flow_1 - flow_2|| = 0.050` vs
`||flow_1|| = 0.099` — order 1). The autonomous generator **is** a closed law in
`(M(x,x), M(y,y))` (checked exact) but **cannot** be expressed as a closed law in
`U_eff`: the link coordinate discards the magnitude data the generator needs.
The genuine dynamics lives on the pointer densities; the link is a lossy
projection of them.

**Covariance is instrument-inherited (no discharge).** Under color-blind total-occupation instrument (color-blind)
the realized pointer step preserves the local-density spectrum (Ad-covariant
content) and is exactly joint-locally covariant (`1.3e-16`); under frame-naming occupation-basis instrument
(frame-naming) the spectrum is changed at order 1 (`0.26`) and covariance breaks
at order 1 (`0.43`). The covariance of the pointer transport generator is the
**color-blind instrument's footprint**, supplied by hand — not derived. No
einselection-selection is discharged.

## What the runner verifies (`PASS=30 FAIL=0`)

Part A (9): `H^2 = I` and exact polynomial exponential vs eigendecomposition;
the `lam = 1` closed pointer map for `M(x,x)'` and `M(y,y)'`; `W` unitary and
the conjugation decomposition; trace preservation; PSD preservation (CP); joint
local gauge covariance. Part B (5): `D' = cos(2 tau) D`; strict Lyapunov
decrease on a `tau` grid; the `tau = pi/2` non-contraction; the balance fixed
point; monotone relaxation of the iterate (`L_40 < 1e-3 L_0`). Part C (5):
`s' = cos(2 tau) s`; link frozen (`cos 2tau > 0`) and `Z_2` flip
(`cos 2tau < 0`); `|s| -> 0` with frozen direction. Part D (8): the same-`U_eff`
different-flow exhibit (lossy coordinate) plus pointer-density autonomy; the
`lam -> 0` weak-record boundary (slaving deviation `1.9e-16` at `lam = 1` rising
monotonically to `0.37` at `lam = 0`); the trace-blocking `2x2`
doubly-stochastic flow toward equal occupation (carries no link content).
Part E (4 + 1 INFO): color-blind total-occupation instrument preserves / frame-naming occupation-basis instrument changes the local-density spectrum;
color-blind total-occupation instrument covariant / frame-naming occupation-basis instrument order-1 broken realized step; the instrument-footprint INFO.

## Honest boundaries — what this does NOT establish

- **No discharge of any gate.** Local color-frame redundancy, the link-generator
  residual, the mixing-regime residual, and the blocking-isometry / einselection
  selection are all untouched. The pointer transport generator is **not** a link
  generator; it relocates the continuous-generator question to the
  pointer-sector carrier, with the link as a frozen dependent coefficient. The
  generator's covariance is put in by choosing the color-blind
  total-occupation instrument;
  frame-naming occupation-basis instrument gives a frame-dependent generator with equal admissibility.
- **Record formation, rate, and `V` are admitted/frozen.** The instruments,
  `(lam, tau)`, and the background `V` are named admissions consistent with the
  `retained_no_go` boundary; the rate is the admitted schedule `sin^2(tau)`, not
  derived. The link transport `V` does not evolve here; the link-generator
  residual remains undelivered.
- **The link generator is vacuous, not absent-by-no-go.** "Frozen / `Z_2` flip"
  is an exact statement about this compression at `lam = 1` on the single edge.
  It does not assert that no link generator can exist anywhere — only that the
  record-dominated matter compression on this carrier does not produce one with
  an arrow and a rate. Named not-foreclosed routes: weak-record averaging (where
  the sibling non-autonomy governs); carriers the matter compression does not
  reach; non-quadratic or multi-edge dynamics where `V` itself could acquire a
  generator.
- **Single edge, finite, leading order at `lam < 1`.** Exact at `lam = 1` on the
  2-site edge; the `lam < 1` statements carry measured `O((1-lam)^2)` windows.
  No continuum, thermodynamic, or mixing/CLT statement; the mixing-regime
  residual is shaped only in that the slaved regime names a compression level.
  The trace-blocking is the
  coarsest gauge-invariant compression; a multi-site Kadanoff cell aggregation
  is a named, not-attempted route.
- **Quantitative magnitudes** (`0.26`, `0.43`, `0.050`, ...) are seed-specific;
  the exact-identity and machine-precision statements are the load-bearing
  content.

## Relation to the wall

The same-wall convergence note left one undelivered input with four hats. This
block sharpens the link-generator residual from the compression side. The record-dominated matter
compression **does** contain an exact autonomous generator with an arrow
(strict Lyapunov monotone toward link-transported color-density balance), a rate
(`sin^2(tau)`, admitted), gauge covariance (instrument-inherited), and CPTP
structure — but it generates the **pointer sector (local color densities)**, not
the link. The induced **link** generator is exactly vacuous (frozen, or a `Z_2`
flip): the source contracts isotropically, freezing the polar factor while its
magnitude decays to the degeneracy at balance. Combined with the sibling
non-autonomy (weak records) and slaving (strong records) results, the picture at
this compression is: **the link is the frozen, covariantly-transported
coefficient of an autonomous color-density transport flow, not a dynamical
variable of its own.** Any genuine link generator on this route must therefore
live where records are weak (sibling non-autonomy regime) or on a carrier the
matter compression does not reach — and the autonomous generator that the
compression does deliver is a color-density consensus law whose covariance is
the admitted instrument's footprint.

## Negative-Boundary Discipline

The vacuous-link statement is a bounded compression-level constraint, not a no-go
against all gauge dynamics.

- Alternative routes left open: weak-record averaging (`lam -> 0`, the sibling
  non-autonomy regime); multi-edge / multi-site Kadanoff cell aggregation of the
  pointer data; non-quadratic or record-coupled matter dynamics; a carrier
  beyond the matter compression on which `V` itself evolves.
- Wall independence: the vacuous-link statement (Finding 3) and the
  lossy-coordinate non-autonomy (Finding 4) are distinct — one says the leading
  link motion is zero, the other says even the surviving pointer flow is not a
  function of the link. Neither follows from the other.
- Hidden-wall scan: the supplied `C^3` carrier, named instruments, named
  Hamiltonian, admitted `(lam, tau)`, and full-rank precondition are explicit
  assumptions, not derived inputs; the covariance is explicitly flagged as
  instrument-inherited.
- Residual matching: the result targets only the link-generator residual at
  the compression level named by the sibling notes; it does not target local color-frame redundancy,
  mixing-regime residual, the blocking-isometry selection, or the connection reading.
- Rhetoric resolution: the tested statements are finite-dimensional, single-edge,
  one-body, `lam = 1`-exact (with measured `O((1-lam)^2)` windows otherwise). No
  lattice-wide, long-time, or universal dynamics claim is made.
- Partial-closure scan: no new axiom or primitive is required; the live
  import-retirement path is to find a compression or carrier on which an
  autonomous **link** (or `V`) generator with an arrow and a rate appears, and
  then prove a retained generator theorem.
- Steelman: a hostile reviewer can argue that the pointer transport generator,
  being covariant and CPTP with a clean arrow, is "the dynamics" and the link's
  frozen-ness is just a coordinate artifact that a better link variable would
  cure. This note leaves that open: it does not claim the pointer generator is
  the framework's realized dynamics (covariance is instrument-inherited; the
  rate and `V` are admitted), and it names the better-coordinate route as
  not-foreclosed.
- Cross-cycle echo: the vacuous-link finding echoes the ledger's
  "equivariance-of-force as dynamics delivery is vacuous (`F = 0`)" entry; the
  instrument-inherited covariance echoes the block-02 einselection
  two-point-admission exhibit. Neither prior wall was retired by a mechanism
  this note overlooks.

## Cross-references

- Sibling induced-trajectory note (construction + non-autonomy reused):
  [`INDUCED_COMPOSITE_LINK_TRAJECTORY_COVARIANCE_INCREMENT_LAW_NON_AUTONOMY_BOUNDED_THEOREM_NOTE_2026-06-08`](INDUCED_COMPOSITE_LINK_TRAJECTORY_COVARIANCE_INCREMENT_LAW_NON_AUTONOMY_BOUNDED_THEOREM_NOTE_2026-06-08.md)
  (on main; `unaudited` at drafting time)
- Sibling record-instrument slaving note (the regime this block compresses):
  [`RECORD_INSTRUMENT_COMPOSITE_LINK_POINTER_ERASURE_EXACT_SLAVING_BOUNDED_THEOREM_NOTE_2026-06-09`](RECORD_INSTRUMENT_COMPOSITE_LINK_POINTER_ERASURE_EXACT_SLAVING_BOUNDED_THEOREM_NOTE_2026-06-09.md)
  (PR #3425; source proposal at drafting time)
- The composite-link construction (consumed as the definition under study):
  [`COLOR_LINK_INDEX_ROUTING_VIA_CROSS_SITE_MATTER_BILINEAR_UNITARIZATION_BOUNDED_THEOREM_NOTE_2026-06-08`](COLOR_LINK_INDEX_ROUTING_VIA_CROSS_SITE_MATTER_BILINEAR_UNITARIZATION_BOUNDED_THEOREM_NOTE_2026-06-08.md)
  (`unaudited` at drafting time)
- The admission's ground:
  [`RECORD_FORMATION_NOT_UNCONDITIONALLY_FORCED_BY_MINIMAL_AXIOMS_NARROW_NO_GO_NOTE_2026-06-06`](RECORD_FORMATION_NOT_UNCONDITIONALLY_FORCED_BY_MINIMAL_AXIOMS_NARROW_NO_GO_NOTE_2026-06-06.md)
  (`retained_no_go` at drafting time)
- Instrument-class constructibility:
  [`PERSISTENT_RECORD_INSTRUMENT_CONSTRUCTION_NARROW_THEOREM_NOTE_2026-05-22`](PERSISTENT_RECORD_INSTRUMENT_CONSTRUCTION_NARROW_THEOREM_NOTE_2026-05-22.md)
  (`retained_bounded` at drafting time)
- Record-side dynamics boundaries (respected): `record_classical_semigroup_boundary_2026-06-06`
  (`retained`), `record_markov_generator_embeddability_boundary_2026-06-06`
  (`retained_no_go`)
- The supplied color carrier (conditionality inherited):
  [`COLOR_SU3_MATTER_REALIZATION_RESIDUAL_MAP_2026-06-05`](COLOR_SU3_MATTER_REALIZATION_RESIDUAL_MAP_2026-06-05.md)
  (`meta`)
- The dynamics wall (the residual being shaped):
  `ST1_ST2_SAME_WALL_GAUGE_DYNAMICS_RESIDUAL_CONVERGENCE_NARROW_THEOREM_NOTE_2026-06-08`
  (`unaudited` at drafting time)
- The covariant-hopping connection reading (NOT consumed; named for scope):
  `matter_gauge_minimal_coupling_fiber_frame_forces_connection_narrow_theorem_note_2026-06-08`
  (`unaudited` at drafting time)
- Color algebra dependency: [`GRAPH_FIRST_SU3_INTEGRATION_NOTE`](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md)
  (`retained`)

Consult the audit ledger for current dependency status. This source note does
not set or update any dependency status. Standard math cited for method only:
polar decomposition, random-unitary (mixed-unitary) quantum channels, Lyapunov
contraction, doubly-stochastic relaxation.

Ledger statuses cited above were verified against the live audit ledger at
drafting time (2026-06-09); they are volatile and must be re-verified on use.
