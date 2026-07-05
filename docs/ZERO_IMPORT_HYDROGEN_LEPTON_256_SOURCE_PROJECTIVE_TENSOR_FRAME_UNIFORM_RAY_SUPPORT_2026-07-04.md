# Zero-Import Hydrogen: Lepton `1/256` Source Projective Tensor-Frame Uniform-Ray Support

**Date:** 2026-07-04
**Type:** partial positive support note
**Claim type:** conditional source-uniformity support
**Status:** support-only. This note does not promote a retained mass claim,
does not derive `S_l = 1/256`, and does not derive hydrogen.
**Verifier:** `scripts/frontier_zero_import_hydrogen_lepton_256_source_projective_tensor_frame_uniform_ray_support.py`

## Scope

The projective-simplex section note showed that if charged-lepton source
strength is a nonzero nonnegative projective source ray `[j]`, then the L1
representative

```text
sigma([j])_c = j_c / sum_d j_d
```

has total strength `mu(C) = 1`. It did not derive that the ray is uniform.

This note attacks that next sub-wall. If the charged-lepton projective source
ray is invariant under the physical tensor-frame relabeling group acting
transitively on

```text
C = {0,1,2,3}^4,
|C| = 256,
```

then the ray is uniform, and the projective-simplex section gives

```text
sigma([j])_c = 1/256.
```

The result is conditional. It does not derive the source-coupled convention,
the full-cell source family, nonnegative projective source semantics, the
physical status of tensor-frame relabeling symmetry, the `S_l` identity, or the
precision correction.

## Conditional Theorem

Let `G` be a finite group of tensor-frame coordinate relabelings acting on
`C`. The relevant examples are:

```text
G_frame = S_4^4
G_frame_extended = S_4^4 semidirect S_4
```

where `S_4^4` relabels the four local matrix-unit coordinates independently
and the extra `S_4` permutes the four slots. The action of `S_4^4` on
`C = {0,1,2,3}^4` is transitive.

Assume a nonzero nonnegative source vector `j` and its positive projective ray
`[j]`. Projective invariance means:

```text
for every g in G, there exists lambda_g > 0 such that g.j = lambda_g j.
```

Because every `g` has finite order `m`,

```text
j = g^m.j = lambda_g^m j.
```

Since `j` is nonzero and `lambda_g > 0`, this implies

```text
lambda_g = 1.
```

Thus projective invariance under a finite tensor-frame relabeling group is
ordinary invariance:

```text
g.j = j  for every g in G.
```

If `G` acts transitively on `C`, ordinary invariance forces all coordinates to
be equal:

```text
j_c = j_*  for every c in C.
```

The nonzero condition gives `j_* > 0`. The projective-simplex section then
gives

```text
sigma([j])_c = j_* / (256 j_*) = 1/256.
```

Therefore:

```text
nonzero nonnegative projective source ray
  + finite transitive tensor-frame projective invariance
  -> uniform ray
  -> sigma([j])_c = 1/256.
```

## Why Projective Invariance Is Enough

The previous firewall showed that raw source controls can be rescaled against
the source-coupling amplitude:

```text
(h, j) -> (h/lambda, lambda j).
```

That is a real gauge freedom for raw controls. But tensor-frame relabeling is a
finite operation. A finite-order relabeling cannot carry a nontrivial positive
scale character on a nonzero ray, because `lambda_g^m = 1` and
`lambda_g > 0` force `lambda_g = 1`.

This is the extra step beyond ordinary simplex uniformity: the theorem does
not need normalized coordinates first. It says the projective ray itself is
uniform once the finite transitive tensor-frame relabeling symmetry is
physical for the charged-lepton source ray.

## What This Moves

| sub-wall | content | status after this note |
|---|---|---|
| W1 | source-coupled local-action convention | still supplied/conditional |
| W2 | charged-lepton full-cell source family `J(j)` | still supplied/conditional |
| W3 | source controls are nonzero nonnegative source strengths | still open |
| W4 | source strength is physically the projective ray `[j]` and may be read through the L1 section | conditionally supported by the projective-simplex section note |
| W5a | tensor-frame relabeling group acts transitively on the source coordinates | finite theorem/support from the tensor-frame source setup |
| W5b | the charged-lepton projective source ray is invariant under that physical relabeling group | still open as physical symmetry input |
| W5c | uniform ray follows from W5a and W5b | conditionally supported here |
| W6 | charged-lepton `S_l` reads `sigma([j])_c` | still open |
| W7 | exact `256` is corrected to, or replaced by, the physical comparator divisor | still open |

This note narrows the uniformity residual. Once the source ray and physical
tensor-frame invariance are supplied, the uniform `1/256` coordinate is no
longer an independent numerical choice.

## Authority Boundary

| source | supplies | boundary here |
|---|---|---|
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROJECTIVE_SIMPLEX_SECTION_SUPPORT_2026-07-04.md` | L1 section of a positive projective source ray and `1/256` for a uniform ray | no proof that the ray is uniform |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_ACTION_SIMPLEX_UNIFORMITY_SUPPORT_2026-07-04.md` | normalized simplex uniformity under transitive relabeling | assumes simplex semantics and physical relabeling |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_RESTRICTED_TENSOR_FRAME_INVARIANCE_SUPPORT_2026-07-04.md` | invariance of the uniform coordinate density under tensor-frame relabelings once the physical frame and L1 semantics are supplied | no derivation that the projective source ray is invariant |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_SLOT_FRAME_SELECTOR_SUPPORT_2026-07-04.md` | slot-resolved source family selects the tensor-product matrix-unit frame relative to `J(j)` | no source-ray semantics or physical invariance theorem |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_STRENGTH_ADDITIVITY_SELECTOR_SUPPORT_2026-07-04.md` | finite additivity plus `mu(C)=1` plus transitivity gives `mu({c})=1/256` | no projective source-ray theorem |
| approved primitives | minimal one-site algebra, OS0 kinetic-form isotropy, units/state discipline | no source/action bridge, weighting rule, normalization rule, projective source semantics, tensor-frame source symmetry theorem, readout bridge, mass value, or `S_l` |

The primitive registry was checked against the current methodology. Approved
primitives are not walls, but they also do not supply the charged-lepton
source-ray invariance or the `S_l` readout identity.

## Open PR Alignment

Open PRs were checked on 2026-07-04 before writing this note. The current
open-review surface does not close the projective tensor-frame uniform-ray
lane:

| PR | merge state at refresh | effect on this support note |
|---|---:|---|
| `#4938` K/CPT orbit-constancy supplied-context bridge | `UNSTABLE` | readout-context/theta-chain premise repair; no lepton projective source-ray invariance or `S_l` theorem |
| `#4939` AC(i) dynamical-index occupancy no-go | `CLEAN` | AC(i) occupancy shortcut pruning; no lepton source-strength projectivization or uniform-ray theorem |
| `#4940` rule achirality from minimality | `CLEAN` | theta gauge-side/admissibility achirality; no lepton source normalization or hydrogen input |
| `#4941` AC(i) determinant-order/chiral L-R no-go | `CLEAN` | AC(i) determinant/readout shortcut pruning; no lepton source-normalization theorem |
| `#4942` AC(i) mode-set / corner-transfer no-go | `CLEAN` | AC(i) mode-set/corner-transfer shortcut pruning; no lepton projective source-ray theorem |
| `#4943` stale-green runner-cache repair sweep | `DIRTY` | runner/cache hygiene and honest-red diagnostics; no charged-lepton source normalization, `m_e`, `alpha(0)`, or hydrogen theorem |
| `#4944` AC(i) matter-action/statistics no-go | `CLEAN` | AC(i) statistical-grain shortcut pruning; no lepton source-ray invariance, `S_l`, `m_e`, `alpha(0)`, or hydrogen theorem |
| `#4945` AC(ii) R-eta current-support-stack no-go | `UNSTABLE` | R-eta readout-license shortcut pruning for `Phi = S_sum = 2/3`; no lepton source-ray invariance, `S_l`, `m_e`, `alpha(0)`, or hydrogen theorem |

These PRs are review context, not proof inputs.

## No-Go Discipline Gate

This section prevents overclaiming. The broad claim "`S_l = 1/256` is now
derived" is **not** shipped. The narrowed claim is:

```text
If the charged-lepton source-strength object is a nonzero nonnegative
projective ray and that ray is invariant under a finite transitive
tensor-frame relabeling group, then the ray is uniform and its L1 simplex
representative has singleton coordinate 1/256.
```

Verdict tag: broad A2/S_l closure fails; narrowed projective tensor-frame uniform-ray support passes.

### N1 - Alternative route enumeration

| route | attempt | result |
|---|---|---|
| projective tensor-frame invariance | Use finite-order projective invariance plus transitivity to force a uniform ray. | SUPPORTED CONDITIONALLY. It gives the uniform ray after projective source semantics and physical tensor-frame invariance are supplied. |
| normalized simplex uniformity | Start after L1 normalization and use transitivity to force equal weights. | SUPPORTED BY PRIOR, but assumes the normalized simplex semantics first. |
| raw source-control linearity | Use `J(j_A+j_B)=J(j_A)+J(j_B)` to force equal source controls. | ATTEMPTED. Linearity gives additivity, not positivity, projective semantics, or symmetry invariance. |
| full `U(16)` covariance | Demand invariance under all inner automorphisms of `M_16(C)`. | ATTEMPTED BY PRIOR. It returns the tracial/projection `1/16` class unless a restricted tensor source frame is physically selected. |
| RN/Fisher source-unit route | Normalize 256 source amplitudes by Fisher norm. | ATTEMPTED. It gives `1/16`, not L1 singleton `1/256`. |
| Record additivity route | Transfer scalar record-readout additivity to source-ray uniformity. | RULED OUT BY PRIOR BOUNDARY. Record additivity does not supply source/action or source-ray symmetry. |
| determinant/log-volume route | Bypass source weights with an invariant scalar theorem. | OPEN. It could replace this route, but no charged-lepton theorem is supplied here. |
| empirical `m_W/256` route | Use the comparator relation directly. | RULED OUT AS ZERO-IMPORT ROUTE. It is the open comparison target, not proof input. |

### N2 - Wall-Independence Audit

The collapsed wall set is:

| wall | content |
|---|---|
| W1 | source-coupled local-action convention is adopted or derived |
| W2 | charged-lepton scalar source is a full-cell slot-resolved source family |
| W3 | source controls are nonzero nonnegative source strengths |
| W4 | source strength is physically the projective ray `[j]` and may be read through the L1 section |
| W5a | tensor-frame relabeling group acts transitively on source coordinates |
| W5b | charged-lepton projective source ray is invariant under that physical relabeling group |
| W5c | uniform source ray follows from W5a/W5b |
| W6 | charged-lepton `S_l` reads `sigma([j])_c` |
| W7 | exact `256` is corrected to, or replaced by, the physical comparator divisor |

| pair | closes automatically? | conclusion |
|---|---|---|
| W1 with W2-W7 | no | convention alone does not supply source family, positivity, projective semantics, symmetry, `S_l`, or precision |
| W2 with W3-W7 | no | source-family shape does not choose positive/projective semantics or physical invariance |
| W3 with W4-W7 | no | positivity does not by itself make the projective ray the physical object |
| W4 with W5a-W7 | no | projective section does not prove tensor-frame symmetry, `S_l`, or precision |
| W5a with W5b-W7 | no | transitive group action does not prove the physical source ray is invariant under it |
| W5b with W5c | yes with W5a | W5c is the finite theorem proved here from W5a and W5b |
| W5c with W6-W7 | no | uniform ray does not identify `S_l` or precision |
| W6 with W7 | no | `S_l` identity does not derive the precision correction |

This note conditionally supports W5c from W5a/W5b. It does not collapse W1-W5b
or W6-W7.

### N3 - Hidden-Wall Scan

| phrase class | classification |
|---|---|
| `projective source ray` | explicit W4 hypothesis, not hidden background |
| `finite transitive tensor-frame relabeling group` | explicit W5a hypothesis |
| `invariant under that group` | explicit W5b hypothesis |
| `uniform ray` | theorem output W5c after W5a/W5b |
| `physical` | marks the unproved status of W5b, not assumed |
| `S_l reads` | explicit W6 residual, not assumed |
| `primitive` / `approved` / `registry` | registry-limited content only |

No source/action convention, source family, positivity, projective semantics,
physical tensor-frame invariance, `S_l` identity, or mass value is hidden as
background.

### N4 - Residual Matching

| cited surface | residual it attacks | residual here | match? |
|---|---|---|---|
| projective-simplex section support | L1 section and `1/256` for uniform ray | W4 plus downstream section | yes |
| simplex uniformity support | normalized simplex uniformity under transitive relabeling | W5c analogue after normalization | yes as precursor |
| restricted tensor-frame invariance support | invariance of uniform density once frame and L1 semantics supplied | W5a/W5c context | yes, but not W5b |
| source-slot frame selector support | source family selects tensor matrix-unit frame | W2/frame setup | yes, but not source-ray invariance |
| matrix-unit basis selector discriminator | full `U(16)` covariance returns `1/16` class | contrast for restricted tensor frame | yes |
| `#4944` AC(i) matter-action/statistics no-go | AC(i) statistical-grain shortcut | lepton projective source-ray uniformity | no; cited only as open PR context |

Only matching residuals are used as support. Non-matching open PRs remain
review context.

### N5 - Rhetoric Audit

| phrase | tested resolution | result |
|---|---|---|
| "projective invariance forces ordinary invariance" | finite-order relabeling resolution | tested; positive scale character is trivial for finite-order relabelings |
| "transitivity forces uniform ray" | coordinate-set resolution on `C={0,1,2,3}^4` | tested; if the group is not transitive, only orbit-wise uniformity follows |
| "`1/256` follows" | uniform 256-coordinate L1 section resolution | tested; it does not follow for nonuniform rays or nontransitive groups |
| "full `U(16)` route does not close this target" | invariant matrix-algebra resolution | cited as contrast; restricted tensor-frame selection remains required |

No universal no-go is shipped. The result is a conditional support theorem for
one uniform-ray selector route.

### N6 - Partial-Closure Path Scan

Potential closure paths found:

| path | status | what it would close |
|---|---|---|
| Prove the charged-lepton source ray is invariant under the tensor-frame relabeling group | open physical-symmetry route | W5b |
| Ratify tensor-frame relabeling invariance as a source-strength convention for the charged-lepton scalar source | open convention/bridge route | W5b |
| Derive positivity/projectivization from source-response semantics | open theorem route | W3/W4 |
| Prove `S_l = sigma([j])_c` for the charged-lepton scalar source | open semantic bridge | W6 |
| Derive determinant/log-volume scalar directly | open bypass route | could bypass W3-W6 |

No new axiom is declared required. The legitimate import-retirement path is to
state the convention/bridge explicitly, prove conditional consequences, and
send the dependency through audit.

### N7 - Steelman

A skeptical reviewer could say the theorem proves only a group-theory
tautology: if the source ray is already invariant under a transitive frame
symmetry, then of course it is uniform. The real physics is exactly the
unproved premise that this tensor-frame relabeling group is a physical symmetry
of the charged-lepton projective source ray. That objection is correct. The
note therefore claims only W5c and leaves W5b as the next physical bridge or
convention target.

### N8 - Cross-Cycle Echo

Similar walls have closed only after the missing semantic or symmetry object
was named and policed:

| prior shape | mechanism | relevance |
|---|---|---|
| restricted tensor-frame invariance support | finite relabeling theorem after frame and semantics supplied | this note moves the same idea one level up to projective rays |
| matrix-unit basis selector discriminator | blocks full inner-automorphism transfer to `1/256` | confirms restricted tensor-frame selection is load-bearing |
| K/CPT supplied-context bridge in `#4938` | supplied-context bridge instead of axiom laundering | tensor-frame source symmetry could follow the same explicit bridge shape |
| kinetic-isotropy primitive | approved structural graining primitive | symmetry/normalization premises must be explicit and limited |
| RN/Fisher source-unit theorem | retained source-unit normalization | demonstrates that a different symmetry/norm object gives `1/16` |

Gate result: `PASS` for the narrowed projective tensor-frame uniform-ray
support and `FAIL` for the broad `S_l` closure claim.

## Non-Claims

- No derivation of `S_l = 1/256`.
- No derivation of the source-coupled local-action convention.
- No derivation that the charged-lepton scalar source is a full-cell
  slot-resolved source family.
- No derivation that source controls are nonnegative source strengths.
- No derivation that charged-lepton source strength is physically the
  projective ray `[j]`.
- No derivation that tensor-frame relabeling invariance is a physical source
  symmetry for the charged-lepton source ray.
- No derivation that `S_l` reads `sigma([j])_c`.
- No derivation of the `256.08` precision correction.
- No derivation of `m_e`, Koide readout, `alpha(0)`, or hydrogen spectroscopy.
- No audit status change for any cited row.
- No new axiom, primitive, or admitted import.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_zero_import_hydrogen_lepton_256_source_projective_tensor_frame_uniform_ray_support.py
```

The verifier checks finite-order projective character triviality, transitive
coordinate uniformity, the nontransitive contrast, L1 section arithmetic,
authority boundaries, open PR alignment, and the non-claim guard.
