# Strict Unitary Chiral Band Velocity Quantization

**Date:** 2026-06-09
**Claim type:** bounded_theorem (conditional 1D/per-axis theorem for the
free single-particle band velocity; not a primitive retirement)
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not
set, predict, promote, or demote any audit outcome.
**Primary runner:**
[`scripts/kinetic_isotropy_from_strict_license_chiral_quantization_2026_06_09.py`](../scripts/kinetic_isotropy_from_strict_license_chiral_quantization_2026_06_09.py)
(SCORECARD: PASS=36, FAIL=0; cached:
[`logs/runner-cache/kinetic_isotropy_from_strict_license_chiral_quantization_2026_06_09.txt`](../logs/runner-cache/kinetic_isotropy_from_strict_license_chiral_quantization_2026_06_09.txt))

---

## What this proves and why it matters

This note proves a narrow band theorem: under a strict radius-1,
translation-covariant, unitary, K/CPT-paired 2-band tick, a nonzero-winding
band has exactly linear quasi-energy `omega(k) = +-(k + phi)` and unit
real-time cone slope. That theorem is conditional on the listed tick readings
and carrier-realization premise below.

The approved
[`kinetic_isotropy_primitive`](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md)
supplies the OS0 kinetic-form isotropy `c_t = c_s` ("one tick is one edge in
FORM"). Its support note
([`KINETIC_ISOTROPY_PRIMITIVE_IRREDUCIBILITY_SUPPORT_2026-06-09.md`](KINETIC_ISOTROPY_PRIMITIVE_IRREDUCIBILITY_SUPPORT_2026-06-09.md))
shows the LISTED structures (positive transfer, reflection positivity, the
single-clock product, 6-NN reachability, Record/readout, cubic spatial
symmetry, scale) do not fix `xi := c_t/c_s` — on a bosonic positive-transfer
witness family — and its own N7 steelman names the door this note walks
through: *"a future retained dynamics could derive the same kinetic isotropy
and retire the primitive."*

This note walks through that door only conditionally. It consumes structures
not on the support note's list: the license's strict R-local update form,
unitarity of the tick, K/CPT pairing of the tick spectrum, and the chiral
(band-winding) structure of the realized carrier. Translating the real-time
cone slope into OS0 `c_t/c_s` remains the separately named bridge B-W.

## 2026-06-15 premise-discharge bridge candidates

The 2026-06-15 source repair narrows the old P1/P2/P3/P4 conditional blob
without claiming retained status:

- `SITE_LICENSE_TICK_DICHOTOMY_ALL_PERIODS_BOUNDED_THEOREM_NOTE_2026-06-11.md`
  supplies a candidate exact all-finite-period site-license theorem. If
  independently audited clean, it discharges the larger-periodicity part of
  P1/P4 for one-component site-licensed ticks: every dispersive licensed
  unitary tick is flat-or-saturating, with no tunable third cell and no
  finite-period mass-hosting cell.
- [`TICK_UNITARITY_FROM_SPECTRUM_REFLECTION_CONJUGACY_BOUNDED_THEOREM_NOTE_2026-06-10.md`](TICK_UNITARITY_FROM_SPECTRUM_REFLECTION_CONJUGACY_BOUNDED_THEOREM_NOTE_2026-06-10.md)
  supplies a candidate exact theorem reducing the bare unitary-tick reading
  P2, and the tick-level P3 pairing, to two narrower named readings:
  spectrum-reflection transport of the retained CPT identities plus the
  channel-envelope contraction.

These packets are source-side audit candidates, not status authorities. If
they pass independent audit, this row's remaining live physics residual is
not the internal band theorem: it is the B-W Wick/readout bridge plus the
named realization readings that connect the strict tick packet to the
framework's realized matter carrier. This note still does not retire the
kinetic-isotropy primitive, does not add a new axiom, and does not set any
audit verdict.
They are also not load-bearing authorities for this kinetic note. In the
source graph, the all-period site-license note is the downstream consumer of
this note's monomial/winding-budget lemma, so this note records that candidate
by plain filename rather than by a dependency edge.

## 2026-06-16 B-W bridge-chain source graph

The current source graph now contains explicit bridge-chain packets for the
old naked B-W residual. This note records them so re-audit has concrete named
rows to inspect rather than a prose-only bridge name:

- `docs/BW_BRIDGE_REDUCTION_OS0_IDENTIFICATION_CONSUMES_ONLY_IR_SLOPE_BOUNDED_THEOREM_NOTE_2026-06-10.md`
  computes the exact OS0 inverse map and reduces B-W to the named Wick-IR
  cone-agreement premise; it also refutes the stronger full Wick-pairing
  reading for strict ticks.
- `docs/WIR_CONE_AGREEMENT_FROM_SECTOR_ALIAS_UNIQUENESS_BOUNDED_THEOREM_NOTE_2026-06-11.md`
  discharges Wick-IR in the bounded setting into sector alias uniqueness plus
  the record-stack spectral reading.
- `docs/REALIZATION_ROW_SIGMA_RECONCILIATION_BOUNDED_THEOREM_NOTE_2026-06-11.md`
  reconciles the exhibited realization-row candidates at the slope consumed by
  W-IR and exposes the remaining unit/normalization premise.

These are source-side audit candidates and downstream bridge-chain inspection
rows, not proof inputs for this kinetic band theorem and not status
authorities. They do not by themselves retire the
`kinetic_isotropy_primitive`; they move the residual from an unnamed B-W bridge
to named rows: spectrum-reflection transport, channel envelope, site-license
carrier, record-stack spectral reading, the dichotomy's periodicity scope, and
the remaining realization/unit readings.

## 2026-06-16 B-W interface no-go

`docs/KINETIC_BW_OS0_IDENTIFICATION_BRIDGE_INTERFACE_NO_GO_NOTE_2026-06-16.md`
sharpens the remaining B-W residual. It proves that the unit real-time band
slope checked here does not, by itself, determine the OS0 Euclidean
kinetic-form coefficient: positive Euclidean transfer envelopes
`E_E(k)=r |omega(k)|` with different `r > 0` preserve the same saturated
unitary band theorem but infer different OS0 slopes. Therefore B-W cannot be
treated as an automatic conventionless consequence of `|v|=1`; a retained
closure must derive the specific readout/normalization rule `E_E(k)=|omega(k)|`
in the same tick/edge units, or keep the primitive-retirement consequence
conditional on that bridge.

This is a downstream negative route-pruning artifact, not a primitive
retirement, not a proof input for this band theorem, and not an audit verdict.

## Premises, with provenance (each graded honestly)

- **(P1) Strictness of the realized tick** — a retained source note plus a
  realized-tick reading, now with an exact finite-period discharge candidate.
  The retained reachability note
  ([`LATTICE_NN_LIGHT_CONE_NOTE.md`](LATTICE_NN_LIGHT_CONE_NOTE.md)) defines
  R-locality with *"no arguments outside the listed dependency set"* (its
  hypothesis-side locality definition); asserting the framework's realized
  one-tick map IS radius-1 strict is a reading of that definition applied to
  the realized tick — the same strict reading the landed per-plaquette
  enumeration
  ([`PER_PLAQUETTE_FROM_ADJACENCY_LICENSE_BOUNDED_THEOREM_NOTE_2026-06-09.md`](PER_PLAQUETTE_FROM_ADJACENCY_LICENSE_BOUNDED_THEOREM_NOTE_2026-06-09.md))
  uses at the gauge level. The all-period site-license theorem cited above
  removes the larger-periodicity escape for one-component licensed ticks, if
  the audit lane accepts it.
- **(P2) The unitary-tick reading** — named conditional. The retained Stone
  theorem
  ([`SINGLE_CLOCK_STONE_FINITE_DIM_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md`](SINGLE_CLOCK_STONE_FINITE_DIM_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md))
  is transfer-relative and does NOT supply a strict-local unitary tick (the
  scope boundary
  [`SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md`](SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md)
  records exactly that). Runner Part C shows a Hamiltonian-generated tick
  `e^{-i a_tau H}` violates P1 for every nonzero hopping (distance-2 amplitude
  `-(a kappa)^2/8 + O(kappa^4)`, exact, plus numeric ring check), so under P1
  the unitary reading forces a strict quantum-cellular-automaton tick, not a
  Stone exponential. The spectrum-reflection conjugacy theorem cited above
  reduces the bare unitarity reading to tick-level CPT transport plus the
  channel-envelope contraction, if independently audited clean.
- **(P3) K/CPT pairing of the TICK spectrum** — named conditional reading.
  The retained [`CPT_EXACT_NOTE.md`](CPT_EXACT_NOTE.md) constrains the
  continuous-time staggered Hamiltonian; the `omega <-> -omega` quasi-energy
  pairing of the STRICT TICK is the same symmetry read on an object the CPT
  note does not construct — a transfer of spectral pairing, declared as a
  reading. P3 is provably load-bearing: runner Part E2 exhibits
  `U(k) = S_+ C(theta)` — radius-1, unitary, COMPLEX trace, det-winding 1 —
  whose winding branch has continuously tunable velocity (range
  `[0.087, 0.913]` at `theta = 0.6`). The spectrum-reflection conjugacy
  theorem supplies the paired quasi-energy corollary once its two named
  readings are granted.
- **(P4) Nonzero band winding (genuine chirality)** — named realization
  premise. The realized carrier's band wraps the quasi-energy circle once per
  Brillouin zone — the discrete-time form of the framework's chirality
  surface (the `gamma_5`/epsilon selector machinery; the staggered carrier).
  Runner Part D5 shows winding is IMPOSSIBLE in continuous time (for any real
  periodic band, `(1/2pi) Int E'(k) dk = 0`): chirality in this sense is a
  tick-native structure. The all-period site-license theorem removes the
  finite-period tunable/mass-hosting licensed-tick alternative, but the
  realized-carrier identification remains a named reading until audited.
- **(B-W) The OS0 identification bridge** — named, not computed by this note.
  The theorem below quantizes the real-time cone slope. Identifying that slope
  with the OS0 Euclidean kinetic-form ratio `c_t/c_s` is an additional bridge
  chain, now represented by the B-W/Wick-IR/realization rows named above. The
  runner's own G2 keeps the two one-tick objects (positive transfer vs unitary)
  distinct, so the bridge chain is not bundled into the band theorem. The
  2026-06-16 B-W interface no-go proves this distinction is load-bearing:
  unit real-time slope permits `E_E(k)=r |omega(k)|` transfer envelopes with
  arbitrary positive `r` unless the B-W readout rule fixes `r=1`.

## The theorem (1D / per-axis, exact, runner Parts B-D)

**Monomial lemma (B1-B4):** a finite Laurent polynomial of degree `<= r` that
is unimodular on the circle is a monomial `c z^n`, `|n| <= r` — proved by a
complete top-coefficient case analysis (`conj(a)c = 0`; in each case the
middle coefficient kills the second survivor). A 1-component strict unitary
Bloch amplitude therefore has `omega(k) = n k + const` exactly: velocity
quantized to an integer number of edges per tick.

**Band-winding saturation (D1-D4):** for a 2-band strict radius-1 unitary
tick with P3, the trace is real on the circle, and the FORWARD direction is
derived by Fourier matching (D1): `tr = beta + 2|gamma| cos(k + phi)`.
Unitarity bounds `|tr| = 2|cos omega| <= 2` (computed, D2); a winding band is
a nonzero-degree circle map, hence surjective, so it attains both `omega = 0`
(`tr = +2`) and `omega = pi` (`tr = -2`), forcing `beta = 0`, `|gamma| = 1` —
the unique solution (D2). The spectrum is then DERIVED (D3): the bands solve
`lambda^2 - 2cos(k + phi) lambda + 1 = 0`, giving `e^{+-i(k + phi)}` exactly:

```text
omega(k) = +-(k + phi)   EXACTLY.
```

`|v| = 1` at every momentum and every curvature order of the free
single-particle dispersion of the winding band vanishes identically (D3, D4).
Radiative/interacting orders are the velocity-RG row, not claimed here. The
cone-slope ratio is quantized:

```text
xi = 1/|v| = 1   (quantized, not tuned),
```

as a real-time band statement. Only after the additional B-W bridge would this
support the OS0 wording `c_t = c_s`. `phi` is a uniform quasi-energy offset —
clock-normalization class, the retained clock-rate boundary
([`RECORD_CLOCK_RATE_NORMALIZATION_GATE_2026-06-06.md`](RECORD_CLOCK_RATE_NORMALIZATION_GATE_2026-06-06.md)).

**The cell structure, from explicit constructions (D6a-D6d):** one-particle
Bloch matrices of 2-layer brickwork circuits are constructed explicitly and
their traces COMPUTED (not assumed):

- the **symmetric partial-swap family** has `tr = 2cos^2(t) - 2sin^2(t)cos k`:
  it touches `omega = 0` at `k = pi` for EVERY `t` — permanently gapless,
  non-winding, with tunable touching velocity. A second hostile witness for
  P4 (sibling of the split-step), NOT a mass family.
- the **asymmetric family** (full swap x partial swap `t`) has
  `tr = -2 sin(t) cos k` — the `beta = 0, g = sin(t)` family: GAPPED with
  gap `pi/2 - t` (the mass), closing INTO the winding cell as `t -> pi/2`
  with `v -> 1` (D6b, D6c).
- the **dichotomy sweep** (D6d): every `(beta, g) != (0, 1)` sample is
  non-winding with `max |v| < 1` strictly.

The marginal anisotropy dial `xi != 1` does not exist in the winding cell:
the dichotomy is {winding: exactly saturating} vs {non-winding: gapped, or
non-chiral gapless}. This mirrors the per-plaquette lift dichotomy (empty
theory vs `B_1`): the structure is quantized away, not tuned away.

## Every premise is load-bearing (runner Parts A, C, D6, E)

| dropped premise | what survives | witness |
|---|---|---|
| P2 unitarity | `xi` sweeps continuously | the bosonic positive-transfer family — re-derives the #3360 support's stated dispersion formula (A1-A3) |
| P1 strictness | tunable velocity `v = kappa` | the Hamiltonian tick (C1-C3) — the continuous-time horn the Collins-route no-go already names |
| P3 CPT pairing | tunable winding-branch velocity | `S_+ C(theta)`: complex trace, det-winding 1, branch velocity sweeping `[0.087, 0.913]` (E2) |
| P4 winding | tunable cone velocity | the split-step walk, `v = |cos(theta)|` (E1a-E1c), and the symmetric partial-swap brickwork (D6a) — both radius-1, unitary, gapless, non-winding |

So the #3360 independence conclusion is simultaneously SHARPENED and bounded:
the primitive boundary is real for every structure on its list, and the
quantization mechanism lives exactly in the structures the list omits.

## The first-order carrier (runner Part F)

The joint-rescale normalization quotient is GENERIC — the bosonic family has
it too (F1 verifies both): the anisotropy gate's two coefficients
([`SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md`](SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md))
are {one ratio, one removable normalization} for every carrier. What is
carrier-specific is only the FORM: for the first-order carrier the surviving
ratio IS the cone velocity `v = kappa_s/kappa_t` (bosonic: `v^2`), consistent
with the velocity-RG note's canonical-time observation. The theorem above
then quantizes that real-time ratio for the winding carrier; the OS0
`c_t/c_s` statement still requires B-W.

## Consequence map (no status claim)

The `audited_renaming` verdict on
[`MIN_TIME_STEP_TIED_TO_THE_LATTICE_EDGE_BY_CAUSAL_LOCALITY_RATIO_DERIVED_SCALE_IS_THE_CLOCK_RATE_NO_GO_NARROW_THEOREM_NOTE_2026-06-08.md`](MIN_TIME_STEP_TIED_TO_THE_LATTICE_EDGE_BY_CAUSAL_LOCALITY_RATIO_DERIVED_SCALE_IS_THE_CLOCK_RATE_NO_GO_NARROW_THEOREM_NOTE_2026-06-08.md)
states: *"Re-audit if a retained bridge theorem derives the record/update tick
as the time coordinate rather than defining it."* Under P1-P4 the winding
carrier transports exactly one edge per tick IN AMPLITUDE (not merely in
reachability support): the tick-to-edge tie becomes the carrier's own
transport fact rather than a definition. Consequence recorded only; re-audit
decisions belong to the audit lane.

## What this note does NOT claim

- **No primitive retirement or registry action.** The theorem does not prove
  the OS0 `c_t = c_s` primitive by itself. Even after the two premise-discharge
  candidates above and the B-W bridge-chain packets are independently audited,
  that consequence remains conditional on the candidate packets' own named
  readings, the P4 realized carrier identification, the record-stack spectral
  reading, and the realization/unit readings named in the bridge chain. The
  primitive registry is owner/audit territory.
- **1D / per-axis scope.** In 3D a chiral (Weyl) component is 2-component per
  cell; 2x2 blocks can mix (the split-step witness exists, G1) and the
  enumeration of strict 3D Weyl automata is a separate cycle. Quantization is
  expected to remove the dial there too, but the quantized 3D cone slope must
  be computed, not assumed.
- **Matter sector only; free single-particle dispersion only.** The
  gauge-sector plaquette-coefficient anisotropy and radiative/interacting
  artifact orders are separate rows.
- **No empirical input.** No Lorentz-violation bound, PDG value, or
  astrophysical limit enters anywhere; comparators are not cited.

## Falsifiers

- A framework derivation that the fundamental inter-record tick map is
  non-unitary, non-strict, or non-CPT-paired (kills P2/P1/P3; the dial
  returns — each failure mode is exhibited as a witness in the runner).
- A realized carrier identified with a non-winding cell (split-step or
  symmetric-brickwork class) — then the velocity is tunable and the
  candidate OS0 consequence is genuinely free.
- The 3D strict Weyl enumeration producing a quantized cone slope different
  from 1 — the dial would still be removed, but the realized kinetic-form
  normalization would need its own reconciliation row.

## No-Go Discipline Gate (for the negative legs)

The negative claims here are: "the anisotropy dial does not exist in the
winding cell" and "winding is impossible in continuous time."

- **N1 alternative routes:** (1) tune `beta != 0` — RULED OUT: winding forces
  `beta = 0` (D2, unique solution; D6d sweep). (2) tune `|gamma| < 1` —
  RULED OUT: gapped, no winding (D6b). (3) higher radius `r > 1` —
  ATTEMPTED: the monomial cascade gives `v in Z`, `|v| <= r`; radius 2
  violates P1. (4) non-unitary tick — RULED OUT BY PREMISE, witnessed
  (Part A). (5) k-dependent band basis evading the trace argument — RULED
  OUT: trace and determinant are basis-independent.
- **N2 wall independence:** the pre-repair conditional set was P1/P2/P3/P4
  plus B-W for the OS0 consequence. The 2026-06-15 source repair routes
  P1/P4 and P2/P3 through explicit candidate packets, but no one of the four
  structural premises closes another: each has an explicit witness satisfying
  the other three and breaking the conclusion (A: drop P2; C: drop P1; E2:
  drop P3; E1/D6a: drop P4). B-W is not a band-theorem premise; it is only the
  named bridge for any OS0 `c_t/c_s` consequence.
- **N3 hidden-wall scan:** "translation-covariant" is consumed (Bloch
  decomposition) — provenance: the Lattice axiom's standard translation
  action. "2-band cell" — provenance: the qubit/one-Grassmann-per-site
  scheme surface. The OS0 identification is separated as the explicit named
  bridge B-W, not treated as a hidden standard-QFT step. All stated.
- **N4 residual matching:** the Collins-route no-go (loop-measure asymmetry
  in continuous time) matches D5 exactly: continuous time cannot wind;
  discrete UV time is where the protection lives.
- **N5 rhetoric audit:** "the dial does not exist" is scoped to the WINDING
  cell of strict radius-1 unitary 2-band CPT-paired updates in 1D/per-axis;
  not bosonic carriers, not gauge anisotropy, not 3D Weyl blocks, not
  non-unitary dynamics, not interacting orders.
- **N6 partial-closure scan:** the registered kinetic-isotropy primitive
  chain-satisfies dependencies without making this row bounded; it is not a
  wall, no-go premise, or missing source. The existing partial closures (B4
  relabel theorem; velocity-RG attractor) both presuppose `c_t = c_s` or flow
  toward it slowly; neither quantizes. No convention-route closure exists for
  the band theorem's conditional tick/carrier surface (the #3360 clock-rate
  distinction stands — reproduced in A1).
- **N7 steelman:** "the unitary strict tick is itself the smuggled isotropy:
  choosing the QCA reading over the Stone reading is choosing the answer."
  Response: the strict reading is the license note's own locality definition,
  already load-bearing in the landed per-plaquette enumeration — the same
  reading cannot be a derivation at the gauge level and a smuggle at the
  matter level; and the reading does NOT by itself fix `xi` (the split-step,
  symmetric-brickwork, and `S_+ C` witnesses all share it) — P4 with P3 does
  the selecting. The residual honest content of the steelman is exactly the
  conditionality of P2/P3/B-W, which is declared, not hidden.
- **N8 cross-cycle echo:** the per-plaquette lift dichotomy (empty vs `B_1`)
  was retired by reading the license strictly at the generator level; this
  note is the same mechanism one level down (the matter kinetic form), which
  is why the dichotomy shape recurs.

## Dependencies

- [LATTICE_NN_LIGHT_CONE_NOTE.md](LATTICE_NN_LIGHT_CONE_NOTE.md) — P1 (retained theorem; its locality definition, read on the realized tick).
- [CPT_EXACT_NOTE.md](CPT_EXACT_NOTE.md) — the retained CPT surface P3's reading transfers from.
- [SINGLE_CLOCK_STONE_FINITE_DIM_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md](SINGLE_CLOCK_STONE_FINITE_DIM_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md) — what P2 is NOT supplied by.
- [SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md](SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md) — the transfer-relative boundary.
- [KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md](KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md) — the target.
- [KINETIC_ISOTROPY_PRIMITIVE_IRREDUCIBILITY_SUPPORT_2026-06-09.md](KINETIC_ISOTROPY_PRIMITIVE_IRREDUCIBILITY_SUPPORT_2026-06-09.md) — the independence surface this sharpens.
- [SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md](SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md) — the two-coefficient counting (Part F).
- [PER_PLAQUETTE_FROM_ADJACENCY_LICENSE_BOUNDED_THEOREM_NOTE_2026-06-09.md](PER_PLAQUETTE_FROM_ADJACENCY_LICENSE_BOUNDED_THEOREM_NOTE_2026-06-09.md) — the strict-reading precedent (NOT a premise; cited for the reading only, since its D2 consumes the target primitive).
- `SITE_LICENSE_TICK_DICHOTOMY_ALL_PERIODS_BOUNDED_THEOREM_NOTE_2026-06-11.md` — non-dependency source-side candidate discharge for the finite-period P1/P4 licensed-tick dichotomy residual. It consumes this note's monomial/winding-budget lemma when read as an all-period bridge, so it must not be represented as an upstream authority of this note.
- [TICK_UNITARITY_FROM_SPECTRUM_REFLECTION_CONJUGACY_BOUNDED_THEOREM_NOTE_2026-06-10.md](TICK_UNITARITY_FROM_SPECTRUM_REFLECTION_CONJUGACY_BOUNDED_THEOREM_NOTE_2026-06-10.md) — source-side candidate discharge reducing the bare P2/P3 tick readings to spectrum-reflection transport plus the channel envelope.
- `docs/KINETIC_BW_OS0_IDENTIFICATION_BRIDGE_INTERFACE_NO_GO_NOTE_2026-06-16.md` — downstream negative route-pruning packet: B-W is not automatic from unit real-time slope; a retained closure must derive the `r=1` OS0 readout/normalization rule.
- [RECORD_CLOCK_RATE_NORMALIZATION_GATE_2026-06-06.md](RECORD_CLOCK_RATE_NORMALIZATION_GATE_2026-06-06.md) — the `phi` offset class (retained).
- [MIN_TIME_STEP_TIED_TO_THE_LATTICE_EDGE_BY_CAUSAL_LOCALITY_RATIO_DERIVED_SCALE_IS_THE_CLOCK_RATE_NO_GO_NARROW_THEOREM_NOTE_2026-06-08.md](MIN_TIME_STEP_TIED_TO_THE_LATTICE_EDGE_BY_CAUSAL_LOCALITY_RATIO_DERIVED_SCALE_IS_THE_CLOCK_RATE_NO_GO_NARROW_THEOREM_NOTE_2026-06-08.md) — the consequence-map row (`audited_renaming`).

**No-promotion statement:** this note does not promote, demote, or set the
audit status of any dependency or of the kinetic-isotropy primitive. The
independent audit lane is the only status authority.

## 2026-06-15 audit-unlock residual certificate

This source update asks for re-audit of the theorem at its narrowest honest
surface: a strict radius-1, unitary, K/CPT-paired, nonzero-winding
single-particle tick has exactly unit real-time band velocity. The runner
checks that algebra and the premise-drop witnesses.

The row does not retire the kinetic-isotropy primitive by itself. The open
inputs remain P1-P4 as realized-tick/carrier readings plus the B-W bridge
that identifies the real-time cone slope with the OS0 Euclidean kinetic-form
ratio. Re-audit should keep the band theorem and the OS0 bridge separate.
This repair adds no new primitive, axiom, or audit status claim.
