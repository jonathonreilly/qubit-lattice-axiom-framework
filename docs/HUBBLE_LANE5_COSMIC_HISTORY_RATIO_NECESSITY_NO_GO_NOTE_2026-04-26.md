# Lane 5 Cosmic-History-Ratio Necessity No-Go: `H_0` Needs Scale-Route And History-Ratio Content Beyond Baseline

**Date:** 2026-04-26
**Status:** support no-go / program-boundary note on `main`.
**Claim type:** no_go
**Status authority:** independent audit lane only; effective status is
pipeline-derived.
**Claim scope:** bounds the Lane 5 closure space after the registered
scale-reference primitive is recognized as units-only. The current framework
baseline plus that primitive does not supply the dimensionless scale-route or
cosmic-history content needed for a numerical `H_0` closure.
**Lane:** 5 — Hubble constant `H_0` derivation
**Workstream:** `hubble-h0-20260426`

**Primary runner:** [`scripts/frontier_hubble_lane5_cosmic_history_ratio_no_go_source_packet.py`](../scripts/frontier_hubble_lane5_cosmic_history_ratio_no_go_source_packet.py)
**Primary runner cache:** [`logs/runner-cache/frontier_hubble_lane5_cosmic_history_ratio_no_go_source_packet.txt`](../logs/runner-cache/frontier_hubble_lane5_cosmic_history_ratio_no_go_source_packet.txt)

---

## 0. Statement

Let the **current framework baseline** be the three named axioms in
[`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md):
Lattice, Quantum, and Record. Let the registered
[`scale_reference_primitive`](SCALE_REFERENCE_PRIMITIVE_NOTE.md) be available
only in its approved role: it converts lattice-natural units to physical
units via `a^{-1}=M_Pl`, and supplies no dimensionless content.

**No-Go Theorem (Lane 5 scale-route necessity).**
The current framework baseline plus the scale-reference primitive does not
derive the dimensionless scale-route content needed for a numerical Lane 5
closure, such as `R_Lambda/a`, `H_inf a`, or the `a/l_P = 1`
self-consistency bridge. The primitive is a ruler, not the C1 route.

**No-Go Theorem (Lane 5 cosmic-history-ratio necessity).**
The current framework baseline plus the scale-reference primitive does not
derive the dimensionless ratio `L = (H_inf / H_0)^2` without retaining at
least one additional dimensionless input from the cosmic-history layer —
concretely, at least one of

```text
{ Omega_m,0 / Omega_Lambda,0,
  Omega_r,0 / Omega_Lambda,0,
  Omega_m,0 / Omega_r,0,
  rho_m,0 / rho_Lambda,0   (after the scale route is fixed),
  any cosmic-history-fixing observation reducible to one of the above } .
```

**Lane 5 closure-pathway corollary.**
Any retained Lane 5 closure requires premises drawn from **two** classes:
the `(C1)` scale route, **and** exactly one dimensionless-`L` class,
`(C2)` or `(C3)`.

- **(C1) scale route** [REQUIRED]. A derivation of the dimensionless
  gravity/scale self-consistency content needed to anchor `R_Lambda/a` or
  `H_inf a` on the framework surface. The registered scale-reference
  primitive is not this route; it only converts units after the
  dimensionless route content is supplied.
- **(C2) cosmic-history-ratio retirement** [one of two `L`-pathways].
  A retained derivation of one of the listed dimensionless cosmic-history
  ratios on extended axioms, retiring `eta`, `alpha_GUT`, or
  `T_CMB`-equivalent observational pins from the bounded
  `Omega_b -> R -> Omega_DM -> Omega_m -> Omega_Lambda` cascade.
- **(C3) direct cosmic-`L` derivation** [one of two `L`-pathways]. A
  framework-internal structural derivation of `L` itself (independent of
  the cosmic-history cascade), e.g., from a separate vacuum/topology
  argument that gives `Omega_Lambda` without going through the matter
  cascade.

No fourth class exists in the current taxonomy, and no single class is
sufficient on its own.

## 1. Source Authorities

| Identity | Authority |
|---|---|
| current Lattice + Quantum + Record baseline | [`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) |
| scale-reference primitive is units-only and non-bounding | [`SCALE_REFERENCE_PRIMITIVE_NOTE.md`](SCALE_REFERENCE_PRIMITIVE_NOTE.md) |
| `Lambda = 3 / R_Lambda^2` retained spectral-gap identity | `COSMOLOGICAL_CONSTANT_SPECTRAL_GAP_IDENTITY_THEOREM_NOTE.md` |
| `H_inf = c / R_Lambda` scale identification | `COSMOLOGY_SCALE_IDENTIFICATION_AND_REDUCTION_NOTE.md` |
| `Omega_Lambda = (H_inf/H_0)^2` matter-bridge identity | `OMEGA_LAMBDA_MATTER_BRIDGE_THEOREM_NOTE_2026-04-22.md` |
| Open-number reduction: `S` is a function of `(H_0, L)` | `COSMOLOGY_OPEN_NUMBER_REDUCTION_THEOREM_NOTE_2026-04-26.md` (Cycle 2) |
| Bounded cosmology cascade `eta -> Omega_b -> R -> Omega_DM -> Omega_m -> Omega_Lambda` | `OMEGA_LAMBDA_DERIVATION_NOTE.md` |
| `(C1)` scale-route gate remains open after the units primitive | `HUBBLE_LANE5_PLANCK_C1_GATE_AUDIT_NOTE_2026-04-26.md` |
| `(C2)` eta-retirement gate remains open | `HUBBLE_LANE5_ETA_RETIREMENT_GATE_AUDIT_NOTE_2026-04-26.md` |

## 2. Proof of scale-route necessity

`H_0` has units of inverse time `[T^{-1}]`. The scale-reference primitive
converts lattice-natural units to physical units by setting `a^{-1}=M_Pl`,
but it carries zero dimensionless content. In particular, it does not
derive `R_Lambda/a`, `H_inf a`, `a/l_P = 1`, a source/action bridge, or a
gravity self-consistency theorem.

The current `(C1)` gate is therefore not the units conversion. It is the
dimensionless coframe/CAR response and action-unit self-consistency route
identified in
[`HUBBLE_LANE5_PLANCK_C1_GATE_AUDIT_NOTE_2026-04-26.md`](HUBBLE_LANE5_PLANCK_C1_GATE_AUDIT_NOTE_2026-04-26.md).
Without that route, the framework has a ruler but not the dimensionless
scale content needed for numerical `R_Lambda`, `H_inf`, or `H_0` closure.
`QED`

## 3. Proof of cosmic-history-ratio necessity

`L = (H_inf/H_0)^2` is dimensionless. By the open-number reduction
theorem (Cycle 2), every late-time bounded cosmology variable is an exact
function of `(H_0, L)` with `R = Omega_r,0` admitted. Inverting, given
`(R, q_0)` or `(R, z_mLambda)` or `(R, H(a))` for `a != 1`, the
single-ratio inverse reconstruction theorem (2026-04-25) recovers `L`.

So a retained `L` derivation must supply one of:

- (i) one of `(q_0, z_*, z_mLambda, H(a))` from framework structure, with
  `R` admitted;
- (ii) one of `(Omega_m,0, Omega_Lambda,0)` from framework structure, with
  `R` admitted;
- (iii) one of the bounded-cascade endpoints (`eta`, `alpha_GUT`-corrected
  `R = Omega_DM/Omega_b`, `Omega_b`) retained, propagating through the
  cascade.

Each `(i)` quantity is a late-time observable whose value depends on
matter/radiation/`Lambda` ratios — i.e., on cosmic-history content. Each
`(ii)` quantity is a cosmic-history-ratio in the listed set. Each `(iii)`
endpoint reduces under the bounded cascade to a cosmic-history ratio.

Hence retaining `L` requires retaining at least one cosmic-history ratio.
The current framework baseline and the scale-reference primitive carry no
matter/radiation/`Lambda` history ratios. Cosmic history is the time-evolved
ensemble of matter, radiation, and `Lambda` densities, which is separate
macroscopic content not supplied by Lattice, Quantum, Record, or a units
conversion.

Therefore the current baseline plus the scale-reference primitive does not
derive `L`. `QED`

## 4. Closure-pathway corollary

By §2, numerical `H_0`, `H_inf`, or `R_Lambda` closure requires the `(C1)`
scale route beyond the units primitive. By §3, retaining `L` requires a
`(C2)` or `(C3)` premise.

Lane 5 closure is the joint retention of `H_0` (numerical) and `L`
(equivalently `Omega_Lambda`). It therefore requires both:

- the `(C1)` scale route, AND
- a `(C2)` or `(C3)` premise (dimensionless `L`).

No single class is sufficient on its own:

- `(C1)` alone fixes the scale-route side but leaves `L` open, so
  `H_0 = H_inf / sqrt(L)` is not derivable.
- `(C2)` or `(C3)` alone fixes `L` but leaves the scale-route side open,
  so `H_0` and `R_Lambda` remain non-numerical.

Hence Lane 5 closure requires premises from at least two of the three
classes — specifically `(C1)` and one of `{(C2), (C3)}`. `QED`

The routes reviewed in the Hubble-H0 workstream all map into this taxonomy:

- **R6** (direct `R_Lambda`/scale-route derivation, blocked by the
  coframe/action-unit gate) ∈ `(C1)`.
- **R5** (eta retirement audit) ∈ `(C2)` (eta retirement is a cosmic-
  history-ratio retirement via the cascade).
- **R3** (open-number reduction theorem, completed Cycle 2) is structural
  framing; on its own it does not close Lane 5.
- **R4** (Hubble Tension Structural Lock theorem, completed Cycle 1) is
  not a closure route; it is a falsifier on the surface.
- A future direct `Omega_Lambda` derivation from a vacuum/topology argument
  ∈ `(C3)`.

The complete Lane 5 closure path requires one route from `(C1)`-class
landed AND one route from `(C2)`-or-`(C3)`-class landed.

## 5. What this no-go closes and does not close

**Closes.**

- The "no fourth class of derivation" program-bounding statement made
  informally in `COSMOLOGY_OPEN_NUMBER_REDUCTION_THEOREM_NOTE_2026-04-26.md`
  §3.2.
- A precise classification of Lane 5 closure routes into the three
  classes `(C1), (C2), (C3)`.
- A precise statement of why the current baseline plus the scale-reference
  primitive is insufficient.

**Does not close.**

- `(C1)`: the Planck/scale-route status. The coframe/action-unit gate
  remains live; this no-go does not predict that `(C1)` is impossible,
  only that the units primitive alone does not supply it.
- `(C2)`: the DM/leptogenesis lane status. Multiple no-gos have closed
  individual selector branches; the surviving live branches
  (`eta/eta_obs = 0.1888` exact one-flavor; `eta/eta_obs = 1.0`
  reduced-surface PMNS) remain open, and promotion lands `(C2)`.
- `(C3)`: this no-go does not rule out a direct framework-derivation of
  `Omega_Lambda` from a separate vacuum/topology argument. Such a route
  has not been opened in this workstream; it remains hypothetical.

## 6. Falsifier

The no-go is falsified if a candidate Lane 5 closure is exhibited that
derives numerical `H_0` from the current framework baseline plus the
scale-reference primitive, without any premise drawn from `{(C1), (C2),
(C3)}`. The proof's case structure (§2-§4) shows this is impossible, so
the falsifier is existential — exhibit a counterexample, and the no-go
falls.

## 7. How this advances Lane 5

Before this no-go, the program-bounding statement was informal in the
Cycle-2 open-number reduction theorem. After this no-go, Lane 5's
closure pathways are:

- formally limited to `{(C1), (C2), (C3)}`;
- each pathway has a sharp open-premise statement;
- the workstream's effort allocation is correctly directed at retiring
  one of those three premises.

The bounded cosmology cascade in `OMEGA_LAMBDA_DERIVATION_NOTE.md`
(`eta -> Omega_b -> R -> Omega_DM -> Omega_m -> Omega_Lambda`) is the
explicit `(C2)` pathway. The Planck-lane work is the explicit `(C1)`
pathway. There is currently no active `(C3)` pathway.

## 8. Cross-references

- `MINIMAL_AXIOMS_2026-06-05.md` — current Lattice + Quantum + Record
  baseline.
- `SCALE_REFERENCE_PRIMITIVE_NOTE.md` — units-only scale primitive.
- `PLANCK_SCALE_LANE_STATUS_NOTE_2026-04-23.md`,
  `PLANCK_SCALE_CONDITIONAL_COMPLETION_NOTE_2026-04-24.md`,
  `HUBBLE_LANE5_PLANCK_C1_GATE_AUDIT_NOTE_2026-04-26.md` — `(C1)` scale
  route status.
- `HUBBLE_LANE5_ETA_RETIREMENT_GATE_AUDIT_NOTE_2026-04-26.md` — `(C2)`
  eta-retirement gate status.
- `OMEGA_LAMBDA_DERIVATION_NOTE.md` — bounded cosmology cascade `(C2)`.
- `OMEGA_LAMBDA_MATTER_BRIDGE_THEOREM_NOTE_2026-04-22.md`,
  `COSMOLOGY_SINGLE_RATIO_INVERSE_RECONSTRUCTION_THEOREM_NOTE_2026-04-25.md`,
  `HUBBLE_TENSION_STRUCTURAL_LOCK_THEOREM_NOTE_2026-04-26.md` (Cycle 1),
  `COSMOLOGY_OPEN_NUMBER_REDUCTION_THEOREM_NOTE_2026-04-26.md` (Cycle 2)
  — retained cosmology theorem stack used in §3-§4.
- `docs/lanes/open_science/05_HUBBLE_CONSTANT_DERIVATION_OPEN_LANE_2026-04-26.md`
  — Lane 5; this no-go formalizes the closure-pathway classification.
- the Hubble-H0 workstream route portfolio — routes R1-R8.

## 9. Boundary

This is a structural no-go bounding the closure space for Lane 5. It does
not claim that any of `(C1), (C2), (C3)` is impossible. It does not retire
any input; it classifies what retirement requires. The scale-reference
primitive is recognized as an approved units conversion and is not treated
as a missing axiom, Tier-A admission, bounded-status source, or Planck import.

The primary source-packet runner records no audit verdict and makes no
status promotion. It verifies the dependency links requested for
re-audit and mechanizes the C1/C2/C3 closure taxonomy as a finite
case model: Lane 5 closure needs C1 plus one of C2 or C3. It does not
retire any of those premises.

## 10. No-Go Discipline Gate

**N1 - Alternative route enumeration.** PASS. Six distinct closure routes
were checked against the narrowed claim:

1. Units-only scale primitive route: fails because the primitive supplies no
   dimensionless `R_Lambda/a`, `H_inf a`, `a/l_P`, or history ratio.
2. `(C1)` scale route alone: fails because `L` remains open.
3. `(C2)` cosmic-history-ratio retirement alone: fails because the scale
   route remains open.
4. `(C3)` direct `L` derivation alone: fails because the scale route remains
   open.
5. Open-number/Hubble-lock route: reduces the live variables to `(H_0, L)`
   and gives falsifiers, but does not supply either missing class.
6. Bounded-cascade route without retiring `eta`, `alpha_GUT`, or equivalent
   history input: remains bounded support, not a retained `L` derivation.

**N2 - Wall-independence audit.** PASS. The collapsed wall set is exactly
two-class: `(C1)` scale route plus one `L` route, `(C2)` or `(C3)`. Closing
`(C1)` does not close `L`; closing `(C2)` or `(C3)` does not close `(C1)`.
`(C2)` and `(C3)` are alternatives, not cumulative independent walls.

**N3 - Hidden-wall scan.** PASS. The phrases "current framework baseline",
"scale-reference primitive", "retained authorities", and "standard
dimensional analysis" are explicit. The scale-reference primitive is named as
units-only; dimensional analysis is used only to separate dimensionful units
from dimensionless closure content; no hidden probability, dynamics, readout,
or Planck-import premise is introduced.

**N4 - Residual matching.** PASS. The cited residuals match the narrowed
claim: the open-number theorem reduces the surface to `(H_0, L)`; the matter
bridge identifies `Omega_Lambda` with the scale ratio; the bounded cascade is
the `(C2)` history-ratio path; the Planck/scale gate is the `(C1)` path; the
scale-reference primitive supplies only units and is not used as a no-go wall.

**N5 - Rhetoric audit.** PASS. "Cannot be derived" is scoped only to the
current framework baseline plus the units primitive and only to the numerical
Lane 5 closure content. The note does not say `(C1)`, `(C2)`, or `(C3)` is
impossible, and does not claim a per-site, per-mode, or lattice-wide
impossibility beyond that closure taxonomy.

**N6 - Partial-closure path scan.** PASS. Two partial-closure paths are
explicitly preserved: the `(C1)` coframe/action-unit gate and the `(C2)`
eta-retirement gate. The approved scale-reference primitive is recognized and
therefore is not counted as a missing axiom, Tier-A admission, bounded-status
source, or Planck import.

**N7 - Steelman.** PASS. A hostile reviewer could argue that a future
framework-internal vacuum/topology route derives `L` directly, or that the
coframe/action-unit route derives the full scale side. This note does not
foreclose either route; it classifies them as `(C3)` and `(C1)` respectively.
That steelman therefore does not falsify the narrowed no-go.

**N8 - Cross-cycle echo.** PASS. The prior "absolute scale" wall was partly
retired as a wording/registry issue by the scale-reference primitive; this
note incorporates that update and no longer treats the Planck scale reference
as a missing axiom. The remaining `(C1)` wall is the dimensionless
self-consistency gate identified by the current Planck C1 gate note.

**Gate result:** PASS for the narrowed no-go. The claim is a taxonomy no-go
for baseline-plus-units-primitive closure, not a no-go against the live
`(C1)`, `(C2)`, or `(C3)` research routes.

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency links named by a prior conditional audit so the audit citation graph can track them. It does not promote this note or change the audited claim scope.

- [minimal_axioms](MINIMAL_AXIOMS_2026-06-05.md)
- [scale_reference_primitive](SCALE_REFERENCE_PRIMITIVE_NOTE.md)
- [cosmology_open_number_reduction_theorem_note_2026-04-26](COSMOLOGY_OPEN_NUMBER_REDUCTION_THEOREM_NOTE_2026-04-26.md)
- [omega_lambda_derivation_note](OMEGA_LAMBDA_DERIVATION_NOTE.md)
- [cosmology_scale_identification_and_reduction_note](COSMOLOGY_SCALE_IDENTIFICATION_AND_REDUCTION_NOTE.md)
- [omega_lambda_matter_bridge_theorem_note_2026-04-22](OMEGA_LAMBDA_MATTER_BRIDGE_THEOREM_NOTE_2026-04-22.md)
- [planck_scale_lane_status_note_2026-04-23](PLANCK_SCALE_LANE_STATUS_NOTE_2026-04-23.md)
- [hubble_lane5_planck_c1_gate_audit_note_2026-04-26](HUBBLE_LANE5_PLANCK_C1_GATE_AUDIT_NOTE_2026-04-26.md)
- [hubble_lane5_eta_retirement_gate_audit_note_2026-04-26](HUBBLE_LANE5_ETA_RETIREMENT_GATE_AUDIT_NOTE_2026-04-26.md)
