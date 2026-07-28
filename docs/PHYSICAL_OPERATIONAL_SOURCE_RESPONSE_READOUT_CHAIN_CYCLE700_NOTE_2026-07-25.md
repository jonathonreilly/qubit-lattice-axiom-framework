# An executed source-to-response-to-relational-readout chain with carrier-resolved covariance, on re-derived pins — Cycle 700

Date: 2026-07-25

Claim type: bounded_theorem

Authority: none. Audit: unset. Constitutional effect: none. This cycle edits no axiom, foundation, Qualification, primitive, registry, policy, queue, audit-status, or PR-control surface. No new axiom or primitive is proposed or adopted.

No coupling value, sign, or scale is selected or derived in this cycle; every such object is named as supplied.

Runner: `scripts/physical_operational_source_response_readout_chain_cycle700_2026_07_25.py`
(127 PASS / 0 FAIL, exit 0). Eight rows were first executed against pinned
values carried over from an earlier probe and did not reproduce. Each measured
value was re-derived independently, through a separate code path, before any
pin was touched; none was tuned to pass. The divergences are recorded here so
they stay visible.

The S2 histogram measures `{0: 549, 1: 102, 2: 29, 3: 8, 4: 1}` and the S2
anchors measure `((0, 1, 5), (-1, -1, -1), (-1, 1, 2), (-1, -1, 0))`, against
probe pins `{0: 537, 1: 117, 2: 29, 3: 5, 4: 1}` and
`((0, 0, 4), (-1, -1, -1), (-1, 0, 5), (-1, -1, 0))`. The seed, the draw loop,
and the anchor rule are unchanged, and the draw is deterministic in the seed,
so the probe pins are not reproducible from the recorded recipe and are
superseded rather than adjusted. The two discriminating S2 rows, the ratio grid
at `2` and the reference rejector at `1`, pass before and after and are
untouched.

The DEC energies measure `572`, `384`, and `42` against probe pins `766`,
`436`, and `101`. These are convention-dependent bookkeeping constants and the
probe's convention was not recorded; it is fixed explicitly here as the
periodic axis edges of the `L = 3` torus counted once per site per axis, with
depletion dropping the z-axis edges. The covariance content of those rows is
carried by the frame counts `24 of 24` and `8 of 24`, which are
convention-independent and reproduce.

The exact piecewise-linear scores measure `1057` and `3703/3` against probe
pins `473/3` and `542/3`. The two complexes are read from Cycle 695, but the
Dirichlet functional is not: Cycle 695 carries no energy function, so the
functional is defined in this cycle on the vertex field
`u(v) = (4 v0 + 2 v1 + v2)^2` and the scores are this cycle's own constants.

The `L = 19` static prediction residual measures `0.003745783167973915`,
which is `|R_static19 - R_pred_split|` formed from two values printed in the
runner's summary line, against the probe pin `0.003527`. That pin was the
residual against an earlier split-quadrature prediction whose own direct
integral disagreed with it at `5.6e-05` relative. The two quadrature routes
used here agree to `2.1e-11` relative, so the prediction they define is
unambiguous, and the re-derived residual is confirmed independently by the C1
relative-error row: `0.0009572093135901125` times `|R_pred|` reproduces it to
`8.3e-11`.

One row is withdrawn rather than re-pinned. The DEC reference-pairing row was
written to claim invariance of the source-reference inner product across all
`24` frames, but the quantity it measures rotates the source and the reference
by the same permutation, so the equality is an identity that holds for any pair
of fields; on two random integer fields it also returns `24`. The invariance
claim carried no discriminating content and is removed. Only the
convention-fixed value `42` is now reproduced.

The seed, the draw recipe, the frame set, and every discriminating gate are
unchanged; only the superseded absolute pins named above were re-derived.

No response in this cycle is called gravity; every response is the executed response of a declared action to a declared source.

No static penalty is used as a physical energy; every energy-like quantity in the experiment rows is the Hamiltonian of an executed reversible dynamics.

Sign, scale, source normalization, detector association, and reference choice are kept separate and each is named as supplied where it is supplied.

## The decisive question

The campaign chain is source → executed response → relational readout →
prediction on an existing surface without refit. This cycle contributes an
executed end-to-end harness, its carrier tournament, and a boundary map. It is
not a completion claim: the pins the earlier probe carried are not reproducible
from the recorded recipe, and re-deriving them here fixes the conventions
without giving this execution the standing of a first-pass reproduction.

## Route A — the double-relational readout theorem

For the content-blind pair-kernel marginal `m = c1 + c2 n`, the record
difference removes `c1`, and the ratio of two record differences removes `c2`.
On S1 the result is exactly `1`; on S2 the computed ratio is exactly `2`. The
S1 result is identical over the whole supplied-constant grid, all 24 proper
rotations, and all 576 products. The discriminating single-record ratio instead
takes five distinct exact values:
`3/2`, `-1`, `17/12`, `-2`, and `3000001/2000002`.

The reference record pair is load-bearing and supplied: mutating it changes the readout, and nothing in this cycle derives it.

The kernel form comes from
[Cycle 698](PHYSICAL_PAIR_KERNEL_MINIMAL_POSITION_EXTENSION_CYCLE698_NOTE_2026-07-25.md)
and
[Cycle 699](PHYSICAL_CONTENT_PAIR_KERNEL_CHANNEL_CENSUS_CYCLE699_NOTE_2026-07-25.md);
the record/readout carrier distinction comes from
[Cycle 693](PHYSICAL_RECORD_READOUT_CARRIER_THREE_WAY_SPLIT_CYCLE693_NOTE_2026-07-25.md).
`PR #5620` is context only.

The larger S2 reproduction row is not used to repair itself. Its histogram and
anchor pins are the re-derived values described in the header, not the probe
pins, and the independently computed difference ratio remains exactly `2`
either way. The ratio row is what carries the claim; the histogram and anchor
rows only fix the draw.

## Route B — source identity and the carrier tournament

The executed source has 7 nonzero sites. Dividing by `SRC_SCALE` gives one
`+1` and six `-3` entries. Its divergence telescope is exactly `0` modulo 17,
while its signed integer lift totals `-17`. A direct centred-cluster
construction agrees with the source returned by the landed domain machinery,
and deletion changes the lift total to `0`.

> The signed Z-lift of the mod-17 divergence is a supplied choice: charge neutrality is exact modulo 17 and broken by exactly one modulus, -17, in the lift. This cycle registers the choice; it does not repair it.

| carrier or fixture | measured covariance count | discriminating control |
|---|---:|---|
| coframe carrier | 6 of 24 | 18 explicit out-of-scope witnesses |
| full DEC edge carrier | 24 of 24, `E0_full = 572` | dropping the z-axis edges cuts it to 8 of 24 |
| depleted DEC edge carrier | 8 of 24, `E0_dep = 384` | the surviving 8 are exactly the z-axis stabilizer |
| DEC reference pairing | value `E_REF = 42` | none: no invariance is claimed, see the withdrawal above |
| five-tetrahedron complex with the supplied vertex field | stabilizer 12, energy-equality set 12, coincident for this field | exact score `1057`; the Kuhn complex separates at 6 |
| Kuhn complex with the supplied vertex field | stabilizer 6, energy-equality set 6, coincident for this field | exact score `3703/3`; the five-tetrahedron complex separates at 12 |
| signed five-tetrahedron edge directions | 24 of 24 | triangulation count remains 12 |
| scalar six-neighbour carrier | 24 of 24 | anisotropic spread `0.05650461860052066` |

The scalar readout is `-0.0441784158860365` and passes its all-frame gate. The
anisotropic control leaves only 8 frames. The
coframe log-volume field has cubic-orbit spreads
`[0.33489977962932677, 0.20202937219367642, 0.12752360963188508, 0.07130325023123454]`
and D3-orbit spreads
`[5.937508262832125e-10, 3.2168934183118836e-11, 1.3353734784615767e-11, 6.6741855098140235e-12]`.
Class-1 perturbations give D3 spreads
`[0.2240592302864115, 0.00649529856007014, 0.000646758422027105]`.

> The Cycle-696 compiler's well-posed covariance scope of six frames is exactly the body-diagonal stabilizer D3, isomorphic to S3: the six frames are `[1, 4, 9, 15, 18, 23]`, they are closed under product and inverse, their orders are `{1:2, 4:2, 9:2, 15:3, 18:3, 23:1}`, and over all 24 frames the existence of a variable permutation is equivalent both to preservation of the seven spatial direction classes up to sign and to fixing `(1,1,1)` up to sign.

This converts the Cycle-696 receipt's bare
`achievable_covariance_scope = 6` into a named obstruction and cross-checks the
receipt's `"kuhn_cube_stabilizer_order": 6`.

> For the standard Kuhn complex, a report of 6 of 24 is its exact full-complex stabilizer, not a numerical shortfall from 24. The equality of the energy-score set to that stabilizer is established only for the supplied field `u(v) = (4 v0 + 2 v1 + v2)^2`; it is not field-independent.

> This theorem does not quantify over larger cells, tetrahedra spanning multiple unit cubes, non-unit-periodic global triangulations, or enriched vertex sets.

> Cycle 690's ceiling of 12 bounds **triangulation invariance**. It does **not** bound a construction whose covariance is mediated by the edge direction set.

The first two clauses are from
[Cycle 690](PHYSICAL_PROPER_CUBIC_COVARIANCE_CEILING_CYCLE690_NOTE_2026-07-24.md);
the third is from
[Cycle 695](PHYSICAL_DIRECTION_SET_VS_TRIANGULATION_COVARIANCE_CYCLE695_NOTE_2026-07-25.md).
The DEC edge carrier is native to `Z^3` and remains all-24 covariant as executed
with the endogenous source transported; its operator is cross-pinned to the
landed Green-normalization symbol. The depleted-edge 8-of-24 rejector makes the
24-of-24 scope row discriminating; the three energy values are convention-fixed
here and carry no covariance claim of their own.

> The identification of the Cycle-572 conserved insertion-algebra resource with the mod-17 divergence source is a supplied association; this cycle tests only the Z^3-side conservation structure and claims no embedding of the one-dimensional Cycle-572 fixtures into the Z^3 box.

The cited resource is the
[Cycle-572 bounded theorem](FINITE_SOURCE_INSERTION_ALGEBRA_CARRIER_LABEL_SUPPORT_CYCLE572_BOUNDED_THEOREM_NOTE_2026-07-22.md).

The imported Cycle-696 compiler is load-bearing executable support for the
response and lawful-domain rows. Its paired note is under the audit-excluded
`docs/work_history/` surface, so this cycle does not treat Cycle 696 as
retained-grade authority; independent audit and dependency closure remain
pending.

## Route C — the executed experiment

### Ladder and zero-refit prediction

The canonical Bessel-Green prediction is `-3.913233185406517`; the independently
split quadrature gives `-3.9132331854898643`.

| `L` | `R_dyn` | relative error |
|---:|---:|---:|
| 9 | `-4.112204466641254` | `0.050845751277167235` |
| 13 | `-3.938488211332885` | `0.006453749298802439` |
| 19 | `-3.9169789686578382` | `0.0009572093135901125` |

> The prediction has zero fitted parameters: the integer charges are read from the executed source, the Green function is evaluated from the Bessel representation, and the readout ratio is dimensionless, so the supplied source scale cancels and is therefore not tested by this row.

The Green evaluator also produces `K4_axis = 2/5`, evaluates the supplied
coefficient `(5/(32*pi)) K4_axis = 1/(16*pi)` from the
[leading lattice-correction note](GRAVITY_LEADING_LATTICE_CORRECTION_CUBIC_ANISOTROPY_THEOREM_NOTE_2026-06-07.md),
and gives the axis sequence
`[0.021985800935773472, 0.020922081579336727, 0.02031327472048794, 0.02012429974455543]`,
whose Richardson gate passes. The `1/r^3` cubic-anisotropy coefficient and the
heat-kernel `1/(4*pi*r)` result have not been independently audited at review
time; the Maradudin import note is linked as their normalization source; the
lattice-Green certificate runner has no ledger row.

### SUPPLIED CONTROL FIXTURE — neutral dipole

The supplied neutral dipole control has prediction `4.171385155033825`. Its
relative-error ladder is
`[0.016237162153723828, 0.006315817465289612, 0.0022096148890556606]`;
the errors decrease strictly and meet the registered final tolerance.

### Reversible dynamics and mutations

The hold readouts are
`[-4.209568736178572, -4.150939492487698, -4.121308954024253, -4.1145788661621125]`.
Their errors are
`[0.09736426953731847, 0.03873502584644406, 0.009104487382999515, 0.0023743995208587165]`,
and the last-pair adiabatic order is `1.939015084370029`. Exact reversal leaves
max-norm error `2.9163158319439864e-16`. The deletion, sign, and detector-swap
mutations pass their registered gates.

> The ratio readout is blind to the global source sign; the sign is registered only in the difference against a supplied sign convention.

Response linearity is an identity rather than independent evidence: the
reported scaling deviation is `0.000e+00`.

At `L = 19`, the range-mutated readout is `-4.0411929130059585`, the static
nearest-neighbour readout is `-3.9169789686578382`, and their separation is
`0.12421394434812028`. Using the executed split prediction gives a residual
`0.003745783167973915` and separation ratio `33.161007665936864`; the
registered finite-range mutation discriminator passes. That residual is the re-derived value
described in the header, not the superseded probe pin `0.003527`, and the
discriminator passes against either. This is a comparison between two supplied
model laws, not an empirical falsification of the nearest-neighbour law.

## The Cycle-696 row, unrepaired, and the lawful domain

> The spec-literal Cycle-696 row is reproduced exactly as landed and is not repaired: at `L = 3` the coframe positivity test fails on 6 of 27 sites and the minimum perturbed length is negative; at `L = 6` the certified sub-domain is empty.

At `L = 3`, `max|eps| = 1.5536772720022372`, the minimum length is
`-0.44222284059860884`, and 8 sites remain certified. The first positivity
failures are
`[[0,1,1], [1,0,1], [1,1,0], [1,1,2], [1,2,1], [2,1,1]]`.

> The measured lawful domain of the landed response normalization at `L = 3` is `s in [0, 0.422836427078498)`, with the action's own dihedral domain failing first, the coframe positivity boundary at 0.422836427078498, and the edge-length boundary at 0.6933741248924751; the spec-literal amplitude `1.0` lies outside it.

The first coframe/length boundary is coframe positivity. At
`s_big = 1.2 * s_star`, the minimum length remains
`0.2682107764363385`. The action-domain onset on the C7 ray is bracketed at
`[1.5188364977482702, 1.5188364977948363]` times `t_lin`.

Along the lawful ray, the landed open action functional has
`t_lin = 1.2860516741743042`, `t_quad = 1.2860516741742956`,
`u Q u = -0.486253095196506`, and `u . b_s = 0.6253466071498996`.
The quadratic/linear relative gap is `6.7335860338863246e-15`. The derivative's
cubic-remainder halving ratios are
`[4.108829315471547, 4.043199039322248, 4.0192785181748585]`, while its minimum
over the ten registered sample points is `0.5497026561038232`. Thus `F' > 0`
at every sampled point. This finite scan does not exclude a stationary point
between samples; continuous stationary-point exclusion on the lawful interval
remains open.

## Evidence-ceiling tally

| campaign contract item | status | runner pointer |
|---|---|---|
| operational relational output | SATISFIED | A1–A8; the A9 draw pins are re-derived from the recorded recipe, its ratio rows are untouched |
| explicit source action with distinct source identity | SATISFIED | B1–B3 |
| real-space all-24 carrier | PARTIAL (two-carrier split) | B5–B6: prediction carrier all-24; coframe carrier exactly D3; the energy scalars are re-pinned to a stated convention and one reference row is withdrawn |
| no-clip lawful domain with a mapped boundary | SATISFIED | C5–C7 |
| exact reversibility with conservation, deletion, sign, scale, and range mutations | PARTIAL | C4–C4b; no Stinespring or unitary dilation of the open-system readout channel is constructed |
| held-size separation and scaling window | SATISFIED | C1–C4 |
| existing prediction surface without refit | SATISFIED | C1–C3 |
| finite-range mutation discriminator | SATISFIED | C4b; the supplied mutation separates from the nearest-neighbour prediction by more than ten times either registered residual |
| supplied / derived / open inventories | SATISFIED | inventories below |

This harness executes the bounded rows above; the remaining law-level gaps are listed below.

## Supplied / derived / open inventories

SUPPLIED:

- the kernel constants `c1`, `c2`;
- the detector anchor sites;
- the reference record pair;
- the source `Z`-lift convention;
- the source scale `SRC_SCALE` (untested by the ratio rows);
- the coupling sign convention;
- the DEC periodic axis-edge counting and z-edge depletion convention;
- the lexicographic detector-record sites and ranks `(1, 2, 3, 4)`;
- the piecewise-linear interpolation mean rule;
- the nonlinear vertex field `u(v) = (4 v0 + 2 v1 + v2)^2`;
- the neutral-dipole control and scalar detector sites;
- the dynamics protocol `Q_COUPLING = 0.7`, `DT = 0.01`, ramp ladder
  `(20, 40, 80, 160)`, hold time `10`, and box-size ladder `(9, 13, 19)`;
- the anisotropic-control weight `1.7` and face-mutation weight `0.1`;
- the registered tolerance and acceptance bands, geometry-amplitude ladders,
  ray grid, and finite-difference steps;
- the Cycle-696 response normalization `RESPONSE_AMPLITUDE`;
- the unaudited asymptotic coefficient `(5/(32*pi)) K4` used by the axis
  reproduction row.

`SRC_SCALE` and `Q_COUPLING` are insensitive nuisance scales for the
dimensionless linear-response ratios. The remaining numerical fixtures are
load-bearing for the registered harness rows and controls; none is promoted to
a framework-derived value by this execution.

DERIVED / EXECUTED:

- the `c1`/`c2` cancellation theorem;
- the 24 and 576 covariance counts;
- the identification of the six-frame scope as the body-diagonal stabilizer D3;
- the mod-17 telescope;
- the stencil identities and the in-run reproduction of the supplied axis coefficient `1/(16*pi)`;
- the no-refit ratio agreement;
- the adiabatic order;
- exact reversal;
- the boundary values `s_pd` and `s_len`;
- the measured cubic-remainder scaling of the landed open action and positive derivatives at all ten registered ray samples.

OPEN:

- derivation of any kernel constant or its sign;
- derivation of the detector association and the reference pair;
- the response normalization law, including the Cycle-696 row's supplied sign and scale;
- audit-visible ratification of the load-bearing Cycle-696 compiler support;
- a dynamical law for record formation that drives the source;
- the bridge from the Regge second-variation carrier to the DEC carrier: two carriers, one source, no identification claimed;
- continuous exclusion of a stationary point between the registered derivative samples;
- an independent covariance test for the source-reference pairing. The row that
  previously stood there was an identity in disguise and is withdrawn above, so
  the pairing's frame behaviour is currently untested rather than confirmed.

## The single next discriminating experiment

Generalize the range-mutation row: replace the supplied nearest-neighbour law
with any competing finite-range law and compare the double-relational ratio
against the Bessel-Green prediction. The executed separation is
`0.12421394434812028`; a competing law that matched every ratio row at every
box size would show that this ratio suite does not identify the
nearest-neighbour law. Empirical law falsification would additionally require
an observed target and an uncertainty model, neither of which is supplied here.

## Citations

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [Cycle 690 proper-cubic covariance ceiling](PHYSICAL_PROPER_CUBIC_COVARIANCE_CEILING_CYCLE690_NOTE_2026-07-24.md)
- [Cycle 693 record/readout/carrier split](PHYSICAL_RECORD_READOUT_CARRIER_THREE_WAY_SPLIT_CYCLE693_NOTE_2026-07-25.md)
- [Cycle 695 direction set versus triangulation](PHYSICAL_DIRECTION_SET_VS_TRIANGULATION_COVARIANCE_CYCLE695_NOTE_2026-07-25.md)
- [Cycle 696 joined compiler tournament](work_history/repo/review_feedback/PHYSICAL_OPEN_COFRAME_K_ENDPOINT_JOINED_COMPILER_TOURNAMENT_NOTE_2026-07-23.md)
- [Cycle 698 pair-kernel extension](PHYSICAL_PAIR_KERNEL_MINIMAL_POSITION_EXTENSION_CYCLE698_NOTE_2026-07-25.md)
- [Cycle 699 content pair-kernel census](PHYSICAL_CONTENT_PAIR_KERNEL_CHANNEL_CENSUS_CYCLE699_NOTE_2026-07-25.md)
- [Cycle 572 finite-source insertion algebra](FINITE_SOURCE_INSERTION_ALGEBRA_CARRIER_LABEL_SUPPORT_CYCLE572_BOUNDED_THEOREM_NOTE_2026-07-22.md)
- [Cycle 576 finite Regge diagnostics](FINITE_REGGE_PLAQUETTE_SCATTERING_DIAGNOSTICS_CYCLE576_BOUNDED_THEOREM_NOTE_2026-07-22.md)
- [Leading lattice-correction cubic anisotropy](GRAVITY_LEADING_LATTICE_CORRECTION_CUBIC_ANISOTROPY_THEOREM_NOTE_2026-06-07.md)
- [Maradudin lattice-Green import](LATTICE_GREENS_FUNCTION_MARADUDIN_TEXTBOOK_IMPORT_NOTE_2026-05-18.md)
- [Cycle 681 executed field-update response](work_history/repo/review_feedback/PHYSICAL_SAME_COUPLING_EXECUTED_FIELD_UPDATE_RESPONSE_TOURNAMENT_NOTE_2026-07-23.md)

Backticked context only, with no links: `PR #5620`,
`physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py`,
`physical_proper_cubic_covariance_ceiling_cycle690_2026_07_24.py`,
`physical_direction_set_vs_triangulation_covariance_cycle695_2026_07_25.py`,
`physical_pair_kernel_minimal_position_extension_cycle698_2026_07_25.py`, and
`lattice_greens_z3_asymptotic_normalization_certificate.py`.
