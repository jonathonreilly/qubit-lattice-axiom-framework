# Zero-Import Hydrogen: Lepton `1/256` Source Projective-Simplex Section Support

**Date:** 2026-07-04
**Type:** partial positive support note
**Claim type:** conditional source-normalization support
**Status:** support-only. This note does not promote a retained mass claim,
does not derive `S_l = 1/256`, and does not derive hydrogen.
**Verifier:** `scripts/frontier_zero_import_hydrogen_lepton_256_source_projective_simplex_section_support.py`

## Scope

The source-strength normalization gauge firewall isolated the scale freedom:

```text
S_src[j] = h * B_lep * J(j),
J(j) = sum_{c in C} j_c O_c,
(h, j) -> (h/lambda, lambda j)
```

leaves `h * J(j)` invariant. Therefore source-control linearity does not by
itself fix the total-strength section `mu(C) = 1`.

This note records the corresponding positive support theorem. If charged-lepton
source strength is a positive projective source ray rather than a raw source
amplitude, then the L1 simplex section is canonical inside that projective
object:

```text
[j] in (R_{\ge 0}^C \ {0}) / R_{>0}
sigma([j])_c = j_c / sum_d j_d,
sum_c sigma([j])_c = 1.
```

For the uniform ray over

```text
C = {0,1,2,3}^4,
|C| = 256,
```

this gives the singleton weight

```text
sigma([1])_c = 1/256.
```

This is not yet a derivation of `S_l`. It is a convention/reframe path for the
normalization wall: if the framework ratifies that the physical lepton
source-strength object is the projective positive source ray and that `S_l`
reads the normalized singleton coordinate, then the total-strength section is
a gauge section, not a new dimensionless number.

## Conditional Theorem

Let `C` be finite with `|C| = 256`. Let

```text
P_+(C) = (R_{\ge 0}^C \ {0}) / R_{>0}
```

be the projective positive cone: two nonzero nonnegative source controls are
equivalent when

```text
j' = lambda j,  lambda > 0.
```

Define

```text
sigma([j])_c = j_c / sum_d j_d.
```

This is well-defined on projective rays because

```text
sigma([lambda j])_c
  = (lambda j_c) / sum_d (lambda j_d)
  = j_c / sum_d j_d
  = sigma([j])_c.
```

The normalized weights define a finite additive source-strength measure:

```text
mu_[j](A) = sum_{c in A} sigma([j])_c,
mu_[j](empty) = 0,
mu_[j](A union B) = mu_[j](A) + mu_[j](B)  for A cap B = empty,
mu_[j](C) = 1.
```

Therefore `mu(C) = 1` can be treated as the L1 gauge section of a positive
source ray, once the projective source-strength semantics are supplied.

For the uniform ray `u_c = 1`,

```text
sigma([u])_c = 1 / 256.
```

If tensor-frame physical relabeling symmetry forces the source ray to be
uniform, this section reproduces the required `1/256` normalized singleton
coefficient.

## Relation To The Previous Firewall

The firewall showed that raw source controls and source-coupling amplitude have
the gauge freedom

```text
(h, j) -> (h/lambda, lambda j).
```

The projective-simplex section uses that same freedom constructively:

```text
raw positive control vector j
  -> projective source ray [j]
  -> normalized simplex representative sigma([j]).
```

The total source amplitude remains outside the normalized weights and may be
kept in `h`. The normalized singleton coordinate is invariant under positive
source-control rescaling. This is the reason the `mu(C) = 1` section can be a
definition/convention target instead of a new physics number.

The support is only conditional because the current retained surface has not
yet supplied:

- that charged-lepton source controls are restricted to a nonnegative
  source-strength cone;
- that the physical source-strength object is the projective ray `[j]`;
- that tensor-frame symmetry forces the uniform source ray;
- that charged-lepton `S_l` reads `sigma([j])_c`;
- the precision correction from exact `256`.

## What This Moves

| sub-wall | content | status after this note |
|---|---|---|
| W1 | source-coupled local-action convention | still supplied/conditional |
| W2 | charged-lepton full-cell source family `J(j)` | still supplied/conditional |
| W3 | source-control linearity | conditionally supported by the source-control linearity note |
| W4a | nonnegative nonzero source-strength cone | still open |
| W4b | total-strength section `mu(C) = 1` | conditionally reframed as L1 section of a positive projective source ray |
| W4c | `S_l` reads normalized source weight | still open |
| W5 | tensor-frame relabeling symmetry forces the uniform ray | conditionally supported only after the physical source frame and symmetry are supplied |
| W6 | precision correction from exact `256` to the comparator divisor | still open |

The next useful attack is not "derive `mu(C)=1` from vector linearity." It is
one of:

```text
ratify source strength as the projective positive ray [j],
derive positivity/projectivization from source-response semantics,
or prove directly that S_l reads sigma([j])_c.
```

## Authority Boundary

| source | supplies | boundary here |
|---|---|---|
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_STRENGTH_NORMALIZATION_GAUGE_FIREWALL_2026-07-04.md` | positive-rescaling gauge obstruction for raw `h` and `j` | no source-ray semantics or `S_l` identity |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_CONTROL_LINEARITY_SUPPORT_2026-07-04.md` | algebraic additivity of source controls after the convention and source family are supplied | no positivity, projective quotient, or total-strength section |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_STRENGTH_ADDITIVITY_SELECTOR_SUPPORT_2026-07-04.md` | finite additivity plus `mu(C) = 1` plus transitivity gives `mu({c}) = 1/256` | no derivation of projective source-strength semantics |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_ACTION_SIMPLEX_UNIFORMITY_SUPPORT_2026-07-04.md` | transitivity forces uniform simplex coordinates after simplex semantics and physical frame are supplied | no source positivity or `S_l` identity |
| `SOURCE_MEASURE_PCAL_RN_COCYCLE_THEOREM_NOTE_2026-05-30.md` | RN/Fisher source-unit normalization; uniform 256-channel coefficient `1/16` | not the projective L1 source-strength section |
| approved primitives | minimal one-site algebra, OS0 kinetic-form isotropy, units/state discipline | no source/action bridge, weighting rule, normalization rule, projective source semantics, readout bridge, mass value, or `S_l` |

The primitive registry was checked against the current methodology. Approved
primitives are not walls, but they also do not supply the source-strength
projective semantics or the charged-lepton `S_l` identity.

## Open PR Alignment

Open PRs were checked on 2026-07-04 before writing this note. The current
open-review surface does not close the projective-simplex section lane:

| PR | merge state at refresh | effect on this support note |
|---|---:|---|
| `#4938` K/CPT orbit-constancy supplied-context bridge | `DIRTY` | readout-context/theta-chain premise repair; no lepton source-ray semantics or `S_l` theorem |
| `#4939` AC(i) dynamical-index occupancy no-go | `CLEAN` | AC(i) occupancy shortcut pruning; no lepton source-strength projectivization |
| `#4940` rule achirality from minimality | `CLEAN` | theta gauge-side/admissibility achirality; no lepton source normalization or hydrogen input |
| `#4941` AC(i) determinant-order/chiral L-R no-go | `CLEAN` | AC(i) determinant/readout shortcut pruning; no lepton source-normalization theorem |
| `#4942` AC(i) mode-set / corner-transfer no-go | `CLEAN` | AC(i) mode-set/corner-transfer shortcut pruning; no lepton source-strength projectivization |
| `#4943` stale-green runner-cache repair sweep | `DIRTY` | runner/cache hygiene and honest-red diagnostics; no charged-lepton source normalization, `m_e`, `alpha(0)`, or hydrogen theorem |
| `#4944` AC(i) matter-action/statistics no-go | `UNSTABLE` | AC(i) statistical-grain shortcut pruning; no lepton source-strength projectivization, `S_l`, `m_e`, `alpha(0)`, or hydrogen theorem |

These PRs are review context, not proof inputs.

## No-Go Discipline Gate

This section prevents overclaiming. The broad claim "`1/256` is now derived
for `S_l`" is **not** shipped. The narrowed claim is:

```text
If charged-lepton source strength is a nonzero nonnegative projective source
ray, then the L1 simplex representative sigma([j]) is a well-defined
rescaling-invariant section with total strength mu(C) = 1. For the uniform
256-coordinate ray, its singleton coordinate is 1/256.
```

Verdict tag: broad A2/S_l closure fails; narrowed projective-simplex section support passes.

### N1 - Alternative route enumeration

| route | attempt | result |
|---|---|---|
| projective positive source ray | Quotient positive source controls by positive rescaling and take the L1 section. | SUPPORTED CONDITIONALLY. It makes `mu(C) = 1` a gauge section after projective semantics are supplied. |
| raw source-control linearity | Use linearity of `J(j)` to fix the total source strength. | ATTEMPTED. The normalization gauge firewall shows raw controls remain rescalable against `h`. |
| finite additivity selector | Use additivity plus total strength one. | PARTIAL. It gives `1/256` after the section is supplied; this note supplies the mathematical section only under projective semantics. |
| tensor-frame transitivity | Force all normalized singleton weights equal. | PARTIAL. It gives uniformity after the physical frame and source semantics are supplied, but not the `S_l` identity. |
| RN/Fisher source-unit route | Normalize a 256-channel source unit by Fisher norm. | ATTEMPTED. It gives `1/16`, not the L1 projective simplex singleton `1/256`. |
| squared-amplitude route | Square RN/Fisher amplitudes to get `1/256`. | ATTEMPTED. It changes the object from a linear source coefficient to a squared-amplitude/probability weight. |
| Record additivity route | Transfer finite record-readout additivity to source-strength normalization. | RULED OUT BY PRIOR BOUNDARY. Record supplies scalar readout additivity over records, not source/action projectivization. |
| determinant/log-volume route | Bypass source weights with an invariant scalar theorem. | OPEN. It could replace this route, but no charged-lepton theorem is supplied here. |

### N2 - Wall-Independence Audit

The collapsed wall set is:

| wall | content |
|---|---|
| W1 | source-coupled local-action convention is adopted or derived |
| W2 | charged-lepton scalar source is a full-cell slot-resolved source family |
| W3 | source controls are nonzero nonnegative source strengths |
| W4 | source strength is physically the projective ray `[j]` and may be read through the L1 section |
| W5 | tensor-frame relabeling symmetry forces the uniform source ray |
| W6 | charged-lepton `S_l` reads `sigma([j])_c` |
| W7 | exact `256` is corrected to, or replaced by, the physical comparator divisor |

| pair | closes automatically? | conclusion |
|---|---|---|
| W1 with W2-W7 | no | convention alone does not supply source family, positivity, projective semantics, uniformity, `S_l`, or precision |
| W2 with W3-W7 | no | source-family shape does not choose positive/projective semantics or sector identity |
| W3 with W4-W7 | no | positivity does not by itself make the projective ray the physical object |
| W4 with W5-W7 | no | L1 section does not force uniformity, identify `S_l`, or fix precision |
| W5 with W6-W7 | no | uniform source ray does not identify the charged-lepton scalar or precision correction |
| W6 with W7 | no | `S_l` identity does not derive the precision correction |

This note conditionally supports W4's section math after W3/projective
semantics are supplied. It does not collapse W1-W3 or W5-W7.

### N3 - Hidden-Wall Scan

| phrase class | classification |
|---|---|
| `positive` / `nonnegative` | explicit W3 hypothesis, not derived |
| `projective source ray` | explicit W4 semantics, not hidden background |
| `canonical` / `section` | mathematical uniqueness inside the supplied projective object, not a physics claim |
| `uniform ray` | explicit W5 condition, not derived by this note |
| `S_l reads` | explicit W6 residual, not assumed |
| `primitive` / `approved` / `registry` | registry-limited content only |

No source/action convention, source family, positivity, projectivization,
uniformity, `S_l` identity, or mass value is hidden as background.

### N4 - Residual Matching

| cited surface | residual it attacks | residual here | match? |
|---|---|---|---|
| source-strength normalization gauge firewall | raw control/coupling scale gauge | motivation for projective quotient | yes |
| source-control linearity support | algebraic additivity of source controls | W1-W3 precursor only | yes, but not normalization |
| source-strength additivity selector support | `1/256` after `mu(C)=1` and transitivity | downstream of this section | yes |
| simplex uniformity support | uniformity after simplex semantics and relabeling symmetry | W5 | yes, but conditional |
| RN/Fisher theorem | source-unit norm gives `1/16` | norm-domain contrast | yes |
| `#4942` AC(i) mode-set no-go | AC(i) occupancy selector shortcut | source projective-simplex section | no; cited only as open PR context |

Only matching residuals are used as support. Non-matching open PRs remain
review context.

### N5 - Rhetoric Audit

| phrase | tested resolution | result |
|---|---|---|
| "`mu(C)=1` is a gauge section" | positive projective source-ray resolution | tested; it is not claimed for raw signed linear source controls |
| "uniform ray gives `1/256`" | 256-coordinate finite set resolution | tested; nonuniform rays give normalized weights summing to one but not `1/256` per coordinate |
| "RN/Fisher gives `1/16`" | uniform 256-channel source-unit resolution | tested as a norm-domain contrast |
| "primitives do not supply this semantics" | approved primitive-registry resolution | tested; no claim about future owner-approved updates |

No universal no-go is shipped. The result is a conditional support theorem for
one source-normalization convention route.

### N6 - Partial-Closure Path Scan

Potential closure paths found:

| path | status | what it would close |
|---|---|---|
| Ratify charged-lepton source strength as the positive projective ray `[j]` | open convention/bridge route | W4 source-normalization section |
| Prove positivity/projectivization from source-response semantics | open theorem route | W3/W4 |
| Prove `S_l = sigma([j])_c` for the charged-lepton scalar source | open semantic bridge | W6 |
| Use tensor-frame symmetry plus source family to force the uniform ray | partially supported by prior uniformity notes after selectors are supplied | W5 |
| Derive determinant/log-volume scalar directly | open bypass route | could bypass W3-W6 |

No new axiom is declared required. The legitimate import-retirement path is to
state the convention/bridge explicitly, prove any conditional theorem, and send
the dependency through audit.

### N7 - Steelman

A skeptical reviewer could say this note is merely a re-labeling trick: every
positive vector has an L1-normalized representative, so of course the uniform
ray gives `1/256`; the real physics is exactly the unproven claim that the
charged-lepton scalar source is a positive projective ray and that `S_l` reads
the normalized coordinate. That objection is correct as a warning against
overclaiming. The note therefore ships only the section theorem and identifies
the ratification target; it does not claim `S_l` closure.

### N8 - Cross-Cycle Echo

Similar repo walls have closed only after the missing semantic object was named
and policed:

| prior shape | mechanism | relevance |
|---|---|---|
| scale-reference primitive | approved units primitive | a section can be ratified, but it must be explicit and limited |
| kinetic-isotropy primitive | approved structural graining primitive | structural normalization is allowed only to declared content |
| K/CPT supplied-context bridge in `#4938` | context moved out of axiom content into named supplied bridge | source projectivization could follow the same bridge path |
| source-coupled local-action candidate | convention/admission candidate | source/action convention still does not supply projective weights |
| RN/Fisher source-unit theorem | retained source-unit normalization | demonstrates that a different normalization object gives `1/16` |

Gate result: `PASS` for the narrowed projective-simplex section support and
`FAIL` for the broad `S_l` closure claim.

## Non-Claims

- No derivation of `S_l = 1/256`.
- No derivation of the source-coupled local-action convention.
- No derivation that the charged-lepton scalar source is a full-cell
  slot-resolved source family.
- No derivation that source controls are nonnegative source strengths.
- No derivation that charged-lepton source strength is physically the
  projective ray `[j]`.
- No derivation that tensor-frame symmetry forces the uniform source ray.
- No derivation that `S_l` reads `sigma([j])_c`.
- No derivation of the `256.08` precision correction.
- No derivation of `m_e`, Koide readout, `alpha(0)`, or hydrogen spectroscopy.
- No audit status change for any cited row.
- No new axiom, primitive, or admitted import.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_zero_import_hydrogen_lepton_256_source_projective_simplex_section_support.py
```

The verifier checks projective-rescaling invariance, L1 simplex section
arithmetic, uniform and nonuniform rays, source-term scale separation, authority
boundaries, open PR alignment, and the non-claim guard.
