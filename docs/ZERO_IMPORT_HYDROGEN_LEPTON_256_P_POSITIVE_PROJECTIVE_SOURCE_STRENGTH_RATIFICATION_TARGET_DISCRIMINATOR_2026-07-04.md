# Zero-Import Hydrogen: Lepton `1/256` P Positive Projective Source-Strength Ratification Target Discriminator

**Date:** 2026-07-04
**Type:** partial discriminator / positive projective source-strength target
**Claim type:** conditional source-strength convention support
**Status:** support-only. This note does not ratify P, does not ratify the
F/L/P/R interface, does not derive retained `S_l = 1/256`, and does not derive
hydrogen.
**Verifier:** `scripts/frontier_zero_import_hydrogen_lepton_256_p_positive_projective_source_strength_ratification_target_discriminator.py`

## Scope

The source-probe ratification target discriminator decomposed the source-side
interface into four clauses:

| clause | content |
|---|---|
| F | full-cell charged-lepton source/action family |
| L | label-free source-coordinate convention |
| P | positive projective source-strength and gauge quotient |
| R | `S_l` source-readout identity |

F and L now have explicit ratification targets. This note attacks only P. P is
the convention that the charged-lepton source controls, once separated from the
common source-coupling front, are read as a nonzero nonnegative projective
source-strength ray with L1 section

```text
sigma([j])_c = j_c / sum_d j_d.
```

## Conditional P Target

P is supplied if the framework derives or explicitly ratifies the following
positive projective source-strength target:

```text
j in R_{\ge 0}^C \ {0},
(h, j) ~ (h/lambda, lambda j) for lambda > 0,
H = h * sum_c j_c,
sigma([j])_c = j_c / sum_d j_d,
source-shape singleton = sigma([j])_c.
```

The target inputs are:

| input | content |
|---|---|
| SOURCE_STRENGTH_OBJECT | the source controls are source-strength data, not merely raw response probes |
| POSITIVE_NONZERO_DOMAIN | the source-strength ray lies in `R_{\ge 0}^C \ {0}` |
| SOURCE_SCALE_GAUGE | positive rescaling of `j` is quotient-equivalent to inverse rescaling of `h` |
| PROJECTIVE_L1_SECTION | the physical source shape is the L1 section `sigma([j])` |
| SHAPE_SELECTOR | the singleton source-shape candidate is `sigma([j])_c`, not raw `h`, raw `j_c`, `h*j_c`, `H`, or the `1/16` classes |
| RATIFICATION | the positive projective source-strength convention is derived or explicitly ratified for framework use |

All six inputs close the narrow P target conditionally:

```text
SOURCE_STRENGTH_OBJECT + POSITIVE_NONZERO_DOMAIN + SOURCE_SCALE_GAUGE
  + PROJECTIVE_L1_SECTION + SHAPE_SELECTOR + RATIFICATION
  -> P supplies the positive projective source-shape coordinate sigma([j])_c.
```

Every one-input-removed target fails:

| missing input | witness | result |
|---|---|---|
| no SOURCE_STRENGTH_OBJECT | signed or complex response probes remain available | no source-strength object to normalize |
| no POSITIVE_NONZERO_DOMAIN | a signed vector can give negative singleton weight, and a zero-total vector has undefined L1 section | no positive projective source ray |
| no SOURCE_SCALE_GAUGE | raw `h` or raw `j_c` can be treated as physical | no forced front/shape quotient |
| no PROJECTIVE_L1_SECTION | `(h,j) -> (h/lambda, lambda j)` leaves raw source scale ambiguous | no normalized singleton source shape |
| no SHAPE_SELECTOR | `h*j_c`, `H`, projection trace `1/16`, or RN/Fisher amplitude `1/16` remain live candidates | no selected P scalar |
| no RATIFICATION | the rule remains a candidate convention | no retained premise for P |

## Finite Checks

The source-coordinate set has `256` elements:

```text
C = {0,1,2,3}^4,
|C| = 4^4 = 256.
```

For a positive source-control vector and coupling front,

```text
T(j) = sum_c j_c,
H = h * T(j),
sigma([j])_c = j_c / T(j).
```

Under positive rescaling,

```text
h' = h / lambda,
j'_c = lambda j_c,
```

both `H` and `sigma([j])_c` are invariant. The raw pieces `h` and `j_c` change.
The product `h*j_c` is invariant but front-bearing and not normalized over
`C`; `H` is a global front, not a singleton shape.

For the uniform ray:

```text
sigma([1])_c = 1/256.
```

For a positive nonuniform ray,

```text
j_c = 4  if c_x = 0,
j_c = 1  otherwise,
```

the singleton value at `(0,0,0,0)` is

```text
sigma([j])_(0,0,0,0) = 1/112.
```

So P alone does not force uniformity; L/tensor-frame naturality is still needed
for the uniform ray. P also does not bind the symbol `S_l`; that is R.

## What This Moves

| before this note | after this note |
|---|---|
| P was named as "positive projective source-strength and gauge quotient." | P is narrowed to a ratifiable target with six explicit inputs. |
| Existing support notes could be mistaken for retained P. | Their exact roles are separated: positive cone, gauge quotient, L1 section, and shape selector remain support unless ratified as P. |
| Raw source variables could be confused with the source-shape scalar. | The one-input-removed witnesses isolate why raw `h`, raw `j_c`, `h*j_c`, `H`, and `1/16` alternatives do not close P. |

If P is ratified, the source-side chain still needs F, L, and R ratification
before exact `S_l = 1/256` can be retained.

The P-clause current-surface no-go
`ZERO_IMPORT_HYDROGEN_LEPTON_256_P_CLAUSE_CURRENT_SURFACE_NO_GO_2026-07-05.md`
records that current retained, primitive, and open-PR surfaces do not supply
`P_CLAUSE_RETAINED`. The positive route remains a retained derivation or
owner/audit acceptance of the positive projective source-strength decision
packet.

## Authority Boundary

| source | supplies | boundary here |
|---|---|---|
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_POSITIVE_CONE_DISCRIMINATOR_2026-07-04.md` | monotone finite-additive source-strength semantics force singleton nonnegativity | assumes the source-strength object is supplied |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_COUPLING_GAUGE_QUOTIENT_PROJECTIVIZATION_SUPPORT_2026-07-04.md` | `H = h * sum_c j_c` and `sigma([j])_c` are invariant under the positive source-scale gauge | does not ratify the physical source-probe readout rule |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROJECTIVE_SIMPLEX_SECTION_SUPPORT_2026-07-04.md` | L1 section for a nonzero nonnegative projective source ray | assumes projective source-strength semantics |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_SHAPE_READOUT_SELECTOR_DISCRIMINATOR_2026-07-04.md` | among current named candidates, `sigma([j])_c` satisfies the source-shape criteria Q1-Q4 | assumes the source-shape slot is the relevant physical slot |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_STRENGTH_ADDITIVITY_SELECTOR_SUPPORT_2026-07-04.md` | finite additive nonnegative source strength plus total strength and transitivity gives `mu({c}) = 1/256` | assumes physical source-strength semantics and total section |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_CONTROL_LINEARITY_SUPPORT_2026-07-04.md` | raw source controls add linearly after source convention and source family are supplied | no positivity, projective quotient, or shape readout |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_STRENGTH_NORMALIZATION_GAUGE_FIREWALL_2026-07-04.md` | raw source-control scale remains gauge unless a section/readout is supplied | does not close P |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md` | full F/L/P/R interface conditionally closes the source-side scaffold | does not ratify P |
| approved primitives | OS0 kinetic-form isotropy, scale reference, realized-state pointwise evaluation | no source/action naturality rule, source-strength weighting, normalization rule, projective quotient, readout bridge, mass value, or empirical match |

The primitive registry was checked with the current origin-main methodology.
Registered primitives chain-satisfy their declared dependencies, but they do
not supply P, F/L/P/R, A3, `m_e`, `alpha(0)`, or hydrogen.

## Current Open PR Alignment

Open PRs were checked on 2026-07-04 after `origin/main` was refreshed and
again after `#5006` appeared and again after `#5007` appeared. The moving
review surface does not close the P positive projective source-strength target:

| PR | state at refresh | effect on this P lane |
|---|---:|---|
| `#5007` Koide native zero-section route guard repair | `CLEAN` | Koide/electron route-guard context; no P closure |
| `#5006` static-source I1 hygiene companion refresh | `CLEAN` | static-source hygiene context; no P closure |
| `#5005` quark lane3 retention firewall companion refresh | `CLEAN` | quark lane3 retention-firewall context; no P closure |
| `#5004` quark C3 ward splitter hygiene companion refresh | `CLEAN` | quark C3 ward-splitter hygiene companion context; no P closure |
| `#5003` Hubble lane5 two-gate hygiene companion refresh | `CLEAN` | Hubble/lane5 two-gate hygiene companion context; no P closure |
| `#5002` Hubble lane5 A2 hygiene companion refresh | `CLEAN` | Hubble/lane5 A2 hygiene companion context; no P closure |
| `#5001` hadron lane1 record-invariance companion refresh | `CLEAN` | hadron lane1 confinement-to-mass firewall record-invariance hygiene; no P closure |
| `#5000` axiom-first record-invariance companion refresh | `CLEAN` | audit companion/record-invariance hygiene; no P closure |
| `#4999` Wilson descendant Schur entropy witness stabilization | `CLEAN` | Wilson/entropy numerical-interface repair; no P closure |
| `#4998` neutrino split2 edge transport witness refresh | `CLEAN` | neutrino numerical-drift repair; no charged-lepton projective source-strength theorem |
| `#4997` neutrino source-amplitude carrier premise bound | `CLEAN` | bounded neutrino source-amplitude carrier context; no P closure |
| `#4996` PMNS selector stationarity diagnostics repair | `CLEAN` | PMNS stationarity narrowing; no charged-lepton P theorem |
| `#4995` theta retirement-basis re-match | `CLEAN` | theta winding-account governance/rematch context; no charged-lepton source-strength ratification |
| `#4994` record-instrument polar contrast stabilization | `CLEAN` | record/instrument numerical repair; no P closure |
| `#4993` DELTA0 route inventory sibling-total refresh | `CLEAN` | stale route-inventory total repair; no source-strength convention |
| `#4992` g_bare two-Ward scope repair | `CLEAN` | keeps `g_bare = 1` conditional on residue normalization; no lepton P theorem |
| `#4991` owner-governed Tier-A retirement | `CLEAN` | governance retirement context; no source-side hydrogen theorem |
| `#4990` Tier-A residual owner decision packet | `CLEAN` | proposal-only governance packet; no P closure |
| `#4989` Tier-A residual governance readiness packet | `CLEAN` | governance readiness context; no P closure |
| `#4988` theta G2 registration stretch no-go | `CLEAN` | theta physical sector/readout registration remains open; no source-strength ratification |
| `#4987` theta G4 theta-bar assembly no-go | `CLEAN` | theta assembly hygiene; no charged-lepton source-strength convention |

Merge-state labels are moving review metadata, not proof inputs here.

## No-Go Discipline Gate

This section prevents overclaiming. The broad retained-P claim is **not**
shipped. The narrowed claim is:

```text
If SOURCE_STRENGTH_OBJECT, POSITIVE_NONZERO_DOMAIN, SOURCE_SCALE_GAUGE,
PROJECTIVE_L1_SECTION, SHAPE_SELECTOR, and RATIFICATION are supplied, P
conditionally supplies the positive projective source-strength target; every
one-input-removed P target fails.
```

Verdict tag: broad P retention not shipped; narrowed P positive projective
source-strength target supported conditionally.

### N1 - Alternative Route Enumeration

| route | attempt | result |
|---|---|---|
| full P target | Supply source-strength object, positivity/nonzero domain, scale gauge, L1 section, shape selector, and ratification. | SUPPORTED CONDITIONALLY. It supplies the P source-shape coordinate. |
| raw signed/complex probes | Use raw response probes as source strengths. | ATTEMPTED. Negative weights, undefined denominators, or no real order can occur. |
| raw `h` or raw `j_c` readout | Treat the split source-coupling variables as physical. | ATTEMPTED. They change under positive source-scale gauge. |
| invariant coefficient `h*j_c` | Read the gauge-invariant product. | ATTEMPTED. It is front-bearing and not normalized over `C`. |
| projection/RN/Fisher `1/16` route | Use projection trace or RN/Fisher source-unit amplitude. | ATTEMPTED BY PRIOR. These are `1/16` classes, not L1 singleton source-shape weights. |
| P-only source-shape route | Use P without F, L, or R. | ATTEMPTED. P can supply `sigma([j])`, but not the source family, uniform ray, or `S_l` identity. |
| latest open PR shortcut | Treat `#4987` through `#5007` as new P science. | ATTEMPTED. They are theta, record/instrument, DELTA0, `g_bare`, governance, PMNS, neutrino, Wilson/entropy, record-invariance, hadron lane1, Hubble lane5, static-source, quark, or Koide surfaces; none ratifies P. |
| primitive shortcut | Appeal to approved primitives or realized-state evaluation. | RULED OUT AS ZERO-IMPORT CLOSURE. The registry supplies no source/action, weighting, normalization, projective quotient, readout bridge, or value. |

### N2 - Wall-Independence Audit

The collapsed P wall set is:

```text
SOURCE_STRENGTH_OBJECT + POSITIVE_NONZERO_DOMAIN + SOURCE_SCALE_GAUGE
  + PROJECTIVE_L1_SECTION + SHAPE_SELECTOR + RATIFICATION.
```

Pairwise independence:

| pair | closes automatically? | conclusion |
|---|---|---|
| SOURCE_STRENGTH_OBJECT <-> POSITIVE_NONZERO_DOMAIN | no | a source-strength role does not by itself forbid signed or zero-total probes |
| SOURCE_STRENGTH_OBJECT <-> SOURCE_SCALE_GAUGE | no | a source-strength role does not alone declare the front/control split gauge |
| POSITIVE_NONZERO_DOMAIN <-> PROJECTIVE_L1_SECTION | no | positivity permits the section but does not ratify it as physical |
| SOURCE_SCALE_GAUGE <-> SHAPE_SELECTOR | no | quotient algebra does not choose the scalar slot among all candidates |
| PROJECTIVE_L1_SECTION <-> SHAPE_SELECTOR | no | the section exists before any physical slot is selected |
| SHAPE_SELECTOR <-> RATIFICATION | no | a selector can remain unratified |

### N3 - Hidden-Wall Scan

| term | status |
|---|---|
| `source-strength object` | explicit SOURCE_STRENGTH_OBJECT wall |
| `nonzero nonnegative` | explicit POSITIVE_NONZERO_DOMAIN wall |
| `gauge quotient` | explicit SOURCE_SCALE_GAUGE wall |
| `L1 section` | explicit PROJECTIVE_L1_SECTION wall |
| `source-shape singleton` | explicit SHAPE_SELECTOR wall |
| `ratification` | explicit RATIFICATION wall |
| `1/256` | value on the uniform ray only; P alone does not force uniformity or bind `S_l` |

No source/action, label-free uniformity, projective source-strength semantics,
normalization, or readout premise is left as background.

### N4 - Residual Matching

| source | claimed support | matched residual | counted? |
|---|---|---|---|
| source positive-cone discriminator | source-strength object plus monotonicity yields nonnegative singleton strengths | POSITIVE_NONZERO_DOMAIN support | yes, conditional |
| source-coupling gauge quotient projectivization | `H` and `sigma([j])` are invariant under positive source-scale gauge | SOURCE_SCALE_GAUGE / PROJECTIVE_L1_SECTION support | yes, conditional |
| projective-simplex section support | L1 section for a nonzero nonnegative projective source ray | PROJECTIVE_L1_SECTION support | yes, conditional |
| source-shape readout selector | `sigma([j])_c` wins Q1-Q4 among named candidates | SHAPE_SELECTOR support | yes, conditional |
| source-strength additivity selector | finite-additive source strength gives `1/256` after total section and transitivity | downstream after P plus uniformity | yes, not P ratification |
| source-control linearity support | raw source controls add linearly | setup context | yes, not P closure |
| F-clause and L target discriminators | source/action and label-free coordinate targets | sibling F/L clauses | no; sibling context only |
| `#4987` through `#5007` | theta, record/instrument, DELTA0, `g_bare`, governance, PMNS, neutrino, Wilson/entropy, record-invariance, hadron lane1, Hubble lane5, static-source, quark, and Koide residuals | P positive projective source-strength target | no; review context only |

Only matching P residuals are counted as support.

### N5 - Rhetoric Audit

The negative phrase used here is narrow: "one-input-removed P targets fail."
The note does not say P is impossible, does not say F/L/P/R is retained, and
does not say `S_l = 1/256` is retained. The positive phrase is conditional:
"supported conditionally."

### N6 - Partial-Closure Path Scan

| partial path | closes P? | remaining wall |
|---|---|---|
| source-strength convention ratification | yes if explicit ratification lands | needs retained/audit acceptance |
| projective-simplex section support | no | supplies math after P semantics are supplied |
| source-shape selector support | no | selects `sigma([j])_c` only under declared source-shape criteria |
| source-probe interface ratification | yes if accepted as full F/L/P/R | broader route, not current proof |
| primitive registry shortcut | no | approved primitives do not supply source-strength weighting or normalization |

### N7 - Steelman

A hostile reviewer can argue that P is nearly already retained: raw source-scale
gauge makes the front/control split unphysical, the L1 section is the unique
positive normalized projective section, and the source-shape selector eliminates
the named alternatives. This note accepts that as a strong convention-retirement
path but rejects closure. The existing notes supply conditional support pieces;
they do not themselves ratify the physical source-strength convention for the
charged-lepton source-probe interface. P therefore remains a ratification target,
not a retained theorem.

### N8 - Cross-Cycle Echo

Earlier source-side lanes were narrowed by turning vague convention language into
explicit ratification targets: F1 for source/action insertion, F3 for full-cell
source locality, F4 for scalar attachment, and L for label-free source
coordinates. The same mechanism could retire P if positive projective
source-strength convention is explicitly ratified. This note therefore ships as
P ratification-target support only.

## Acceptance Checklist

- P target isolated as source-strength object plus positive projective quotient.
- One-input-removed witnesses are explicit.
- Gauge-invariant `H` and `sigma([j])` arithmetic is finite and checked.
- Raw `h`, raw `j_c`, `h*j_c`, `H`, and `1/16` alternatives are not treated as P closure.
- P is not promoted to retained status.

## Non-Claims

- No derivation or ratification of P.
- No derivation or ratification of F/L/P/R.
- No derivation that `S_l = 1/256` is retained.
- No derivation of the `256.082435...` precision correction.
- No derivation of the Koide/electron branch or physical `m_e`.
- No derivation of `alpha(0)` or hydrogen spectroscopy.
- No use of latest open PRs as proof inputs.
- No new axiom, primitive, or admitted import.
- No audit status change for any cited row.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_zero_import_hydrogen_lepton_256_p_positive_projective_source_strength_ratification_target_discriminator.py
```
