# Zero-Import Hydrogen: Lepton `1/256` Source Projective Tensor-Frame Invariance Bridge Support

**Date:** 2026-07-04
**Type:** partial positive support note
**Claim type:** conditional physical-invariance bridge support
**Status:** support-only. This note does not promote a retained mass claim,
does not derive `S_l = 1/256`, and does not derive hydrogen.
**Verifier:** `scripts/frontier_zero_import_hydrogen_lepton_256_source_projective_tensor_frame_invariance_bridge_support.py`

## Scope

The projective tensor-frame uniform-ray note proved the finite theorem:

```text
nonzero nonnegative projective source ray
  + finite transitive tensor-frame projective invariance
  -> uniform ray
  -> sigma([j])_c = 1/256.
```

Its live hypothesis was W5b: the charged-lepton projective source ray must be
invariant under the physical tensor-frame relabeling group. This note attacks
that bridge directly.

The result is conditional. It shows that W5b follows from a precise
source-family naturality rule: if the charged-lepton source family has no
physical labels beyond the tensor-frame coordinate and if the physical source
ray assignment is natural under source-family preserving relabelings, then the
projective source ray is tensor-frame invariant. The note does not derive that
naturality rule from the minimal axioms or approved primitives. This is the
physical invariance bridge isolated by the prior uniform-ray support note.

## Conditional Bridge Theorem

Let

```text
C = {0,1,2,3}^4,
|C| = 256,
J(j) = sum_{c in C} j_c O_c.
```

Here `O_c` denotes the tensor-product matrix-unit source basis from the
slot-resolved full-cell source family, and `[j]` is a nonzero nonnegative
projective source ray.

For a tensor-frame coordinate relabeling `g` of `C`, define the induced
source-family preserving relabeling `rho_g` by

```text
rho_g(O_c) = O_{g(c)}
(rho_g j)_c = j_{g^{-1}(c)}.
```

Then the source map is equivariant:

```text
rho_g J(j)
  = sum_{c in C} j_c O_{g(c)}
  = sum_{d in C} j_{g^{-1}(d)} O_d
  = J(rho_g j).
```

Therefore tensor-frame relabelings are automorphisms of the supplied source
family once that family is fixed as `J(j) = sum_{c in C} j_c O_c`.

Now add the physical bridge condition:

```text
The charged-lepton source-strength assignment is natural under every
source-family preserving relabeling rho_g.
```

Equivalently, the physical source ray is not allowed to depend on an arbitrary
name for a tensor-frame coordinate. Under that condition,

```text
[j] = [rho_g j]  for every tensor-frame relabeling g.
```

This is exactly W5b. Combining it with the previous finite theorem gives

```text
finite transitive tensor-frame projective invariance
  -> uniform ray
  -> sigma([j])_c = 1/256.
```

Thus the numerical uniformity step is no longer the live problem. The live
problem is the physical license for the source-family naturality rule.

## What This Moves

| sub-wall | content | status after this note |
|---|---|---|
| W1 | source-coupled local-action convention | still supplied/conditional |
| W2 | charged-lepton full-cell source family `J(j)` | still supplied/conditional |
| W3 | source controls are nonzero nonnegative source strengths | still open |
| W4 | source strength is physically the projective ray `[j]` and may be read through the L1 section | conditionally supported by the projective-simplex section note |
| W5a | tensor-frame relabeling group acts transitively on the source coordinates | finite theorem/support from the tensor-frame source setup |
| W5b | charged-lepton projective source ray is invariant under that physical relabeling group | conditionally reduced here to source-family naturality |
| W5c | uniform ray follows from W5a and W5b | conditionally supported by the projective tensor-frame uniform-ray note |
| W6 | charged-lepton `S_l` reads `sigma([j])_c` | still open |
| W7 | exact `256` is corrected to, or replaced by, the physical comparator divisor | still open |

This note is a bridge support result, not a closure. If source-family
naturality is ratified as the physical convention for the charged-lepton
projective source ray, then W5b closes without a new number. If the
charged-lepton source has a physical coordinate tag, preferred slot, or
realized-state dial that survives source-family relabeling, nonuniform rays
remain possible.

## Authority Boundary

| source | supplies | boundary here |
|---|---|---|
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_SLOT_FRAME_SELECTOR_SUPPORT_2026-07-04.md` | the source map `J(j) = sum_c j_c O_c` selects the tensor-product matrix-unit frame relative to the source controls | no physical source-ray naturality theorem |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROJECTIVE_SIMPLEX_SECTION_SUPPORT_2026-07-04.md` | L1 section of a positive projective source ray | no proof that the ray is uniform or physically invariant |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROJECTIVE_TENSOR_FRAME_UNIFORM_RAY_SUPPORT_2026-07-04.md` | finite transitive tensor-frame projective invariance forces a uniform ray and `sigma([j])_c = 1/256` | assumes W5b |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_RESTRICTED_TENSOR_FRAME_INVARIANCE_SUPPORT_2026-07-04.md` | invariance of the already-uniform density under tensor-frame relabelings | no derivation that the physical source ray is invariant |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_MATRIX_UNIT_BASIS_SELECTOR_DISCRIMINATOR_2026-07-04.md` | full `U(16)` covariance is too broad and returns the `1/16` projection/tracial class | supports using restricted source-family relabelings only |
| approved primitives | minimal one-site algebra, OS0 kinetic-form isotropy, units/state discipline | no source/action naturality rule, source-strength weighting rule, normalization rule, physical source-ray bridge, readout bridge, mass value, or `S_l` |

The primitive registry was checked against the fresh origin-main methodology.
Approved primitives are not walls, but they also do not supply source-family
naturality or the `S_l` readout identity.

## Open PR Alignment

Open PRs were checked on 2026-07-04 before writing this note. The current
open-review surface does not close the source-family naturality bridge:

| PR | merge state at refresh | effect on this support note |
|---|---:|---|
| `#4938` K/CPT orbit-constancy supplied-context bridge | `MERGED` | repairs theta-chain readout premises under supplied finite context; no lepton source-family naturality or `S_l` theorem |
| `#4939` AC(i) dynamical-index occupancy no-go | `CLEAN` | AC(i) occupancy shortcut pruning; no lepton projective source-ray bridge |
| `#4940` rule achirality from minimality | `CLEAN` | theta gauge-side/admissibility achirality; no source-strength naturality or hydrogen input |
| `#4941` AC(i) determinant-order/chiral L-R no-go | `CLEAN` | AC(i) determinant/readout shortcut pruning; no lepton source-ray invariance theorem |
| `#4942` AC(i) mode-set / corner-transfer no-go | `CLEAN` | AC(i) shortcut pruning; no charged-lepton source-family naturality |
| `#4943` stale-green runner-cache repair sweep | `DIRTY` | runner/cache hygiene and honest-red diagnostics; no charged-lepton source normalization theorem |
| `#4944` AC(i) matter-action/statistics no-go | `CLEAN` | AC(i) statistical-grain shortcut pruning; no lepton source-ray naturality, `S_l`, `m_e`, `alpha(0)`, or hydrogen theorem |
| `#4945` AC(ii) R-eta current-support-stack no-go | `CLEAN` | R-eta readout-license shortcut pruning for `Phi = S_sum = 2/3`; no lepton source-family naturality, `S_l`, `m_e`, `alpha(0)`, or hydrogen theorem |
| `#4946` AC(ii) R-eta transport-stretch no-go | `CLEAN` | same-surface transport equality pruning for `Phi = Tr L_3^+ = 2/3`; no lepton source-family naturality, `S_l`, `m_e`, `alpha(0)`, or hydrogen theorem |

These PRs are review context, not proof inputs.

## No-Go Discipline Gate

This section prevents overclaiming. The broad claim "W5b is now derived from
the framework axioms" is **not** shipped. The narrowed claim is:

```text
If the charged-lepton scalar source family is the slot-resolved family
J(j) = sum_{c in C} j_c O_c, if source strength is a projective source ray,
and if the physical source-ray assignment is natural under source-family
preserving tensor-frame relabelings rho_g, then W5b follows.
```

Verdict tag: broad W5b closure fails; narrowed source-family naturality bridge support passes.

### N1 - Alternative Route Enumeration

| route | attempt | result |
|---|---|---|
| source-family naturality | Treat tensor-frame relabelings as gauge/source-coordinate isomorphisms of `J(j) = sum_c j_c O_c`. | SUPPORTED CONDITIONALLY here. It closes W5b after the source family, projective semantics, and naturality rule are supplied. |
| finite projective uniformity | Use finite-order projective invariance plus transitivity to force a uniform ray. | SUPPORTED BY PRIOR, but it assumes W5b rather than deriving it. |
| normalized simplex uniformity | Start after L1 normalization and use transitivity to force equal weights. | SUPPORTED BY PRIOR, but assumes normalized simplex semantics and physical relabeling invariance. |
| source-control linearity/additivity | Use `J(j_A + j_B) = J(j_A) + J(j_B)` and finite additivity to force equal source strengths. | ATTEMPTED BY PRIOR. It supports algebraic additivity but does not force physical invariance of the ray. |
| full `U(16)` covariance | Demand invariance under all inner automorphisms of `M_16(C)`. | ATTEMPTED BY PRIOR. It is too broad and returns the projection/tracial `1/16` class unless the restricted source frame is selected. |
| Record or approved primitives | Use minimal axioms, OS0 kinetic isotropy, scale reference, or realized-state evaluation to supply source-ray naturality. | RULED OUT BY REGISTRY BOUNDARY for this specific content: they do not supply source/action, weighting, normalization, or source-ray bridge content. |
| realized-state selector | Let the realized state choose the source ray. | RULED OUT AS ZERO-IMPORT CLOSURE. It may register state-contingent data but does not derive a state-independent source-family naturality theorem. |
| empirical `m_W/256` route | Use the observed charged-lepton comparator relation as the selector. | RULED OUT AS ZERO-IMPORT ROUTE. It is the open comparison target, not proof input. |

### N2 - Wall-Independence Audit

The collapsed wall set is:

| wall | content |
|---|---|
| B1 | source-coupled local-action convention is adopted or derived |
| B2 | charged-lepton scalar source is a full-cell slot-resolved source family |
| B3 | source controls are nonnegative projective source strengths |
| B4 | source-family preserving relabelings are physically gauge/source-coordinate isomorphisms for that source family |
| B5 | physical source-ray assignment is natural under those relabelings |
| B6 | charged-lepton `S_l` reads `sigma([j])_c` |
| B7 | exact `256` is corrected to, or replaced by, the physical comparator divisor |

| pair | closes automatically? | conclusion |
|---|---|---|
| B1 with B2-B7 | no | source-coupled action alone does not supply family shape, projective semantics, naturality, readout identity, or precision |
| B2 with B3-B7 | no | the source family does not by itself choose projective source-strength semantics or physical naturality |
| B3 with B4-B7 | no | nonnegative projective semantics do not make tensor-frame relabelings physical gauge |
| B4 with B5 | no | treating relabelings as source-family isomorphisms still needs the source-ray assignment to respect them |
| B5 with W5a/W5c | yes after B2-B4 | naturality under transitive tensor-frame relabelings supplies W5b, then prior W5c gives uniformity |
| B5 with B6-B7 | no | source-ray invariance does not identify `S_l` or precision |
| B6 with B7 | no | `S_l` identity does not derive the precision correction |

This note narrows B4/B5 to an explicit bridge condition. It does not collapse
B1-B4 or B6-B7.

### N3 - Hidden-Wall Scan

| phrase class | classification |
|---|---|
| `source-family naturality` | explicit B5 hypothesis, not hidden background |
| `source-family preserving relabeling` | explicit B4/B5 bridge object |
| `no physical labels beyond the tensor-frame coordinate` | explicit B4 condition |
| `projective source ray` | explicit B3 hypothesis |
| `uniform ray` | downstream W5c theorem from the prior note |
| `physical` | marks the unproved bridge license, not an assumed theorem |
| `approved primitives` / `registry` | registry-limited content only |

No source/action convention, source family, positivity, projective semantics,
source-family naturality, `S_l` identity, mass value, or precision correction is
hidden as background.

### N4 - Residual Matching

| cited surface | residual it attacks | residual here | match? |
|---|---|---|---|
| source-slot frame selector support | source map selects tensor-product matrix-unit frame | B2 source-family setup | yes, but not B5 |
| projective-simplex section support | L1 section of a positive projective ray | B3 section semantics | yes, but not B5 |
| projective tensor-frame uniform-ray support | W5c from W5a/W5b | downstream use after this bridge | yes |
| restricted tensor-frame invariance support | invariance of an already-uniform density under relabelings | W5a/W5c context | yes, but not B5 |
| matrix-unit basis selector discriminator | full `U(16)` covariance returns `1/16` class | contrast for restricted source-family relabelings | yes |
| `#4945` AC(ii) R-eta current-support-stack no-go | `Phi = S_sum = 2/3` readout-license shortcut | lepton source-family naturality | no; cited only as open PR context |
| `#4946` AC(ii) R-eta transport-stretch no-go | `Phi = Tr L_3^+ = 2/3` same-surface transport equality | lepton source-family naturality | no; cited only as open PR context |

Only matching residuals are counted as support. Non-matching open PRs remain
review context.

### N5 - Rhetoric Audit

The note does not say "source-family naturality is not a framework fact" as a
universal no-go. It uses the narrower boundary "this note does not derive the
physical license for source-family naturality."

| resolution | tested? | outcome |
|---|---|---|
| formal source-family automorphism | yes | `rho_g J(j) = J(rho_g j)` holds for tensor-frame relabelings |
| projective-ray consequence | yes | naturality under all `rho_g` gives W5b |
| finite transitive uniformity consequence | yes by prior note | W5b plus W5a gives uniform ray and `sigma([j])_c = 1/256` |
| physical source/action license | no | left as the live bridge |
| `S_l` readout and precision | no | explicitly outside this note |

### N6 - Partial-Closure Path Scan

The legitimate import-retirement path is visible:

| candidate path | status | what it would close |
|---|---|---|
| source-slot frame selector support | already drafted support note | source controls select the tensor frame once the slot-resolved source family is supplied |
| projective-simplex section support | already drafted support note | total-strength normalization can be a projective L1 section rather than a new number |
| projective tensor-frame uniform-ray support | already drafted support note | W5c uniformity after W5b |
| this source-family naturality bridge | current conditional support | W5b if naturality is ratified as a source-coordinate convention |
| merged PR `#4938` supplied-context bridge pattern | merged and unrelated in content | shows a current repo pattern for supplied-context bridge repair, but does not close this lepton source bridge |

The bridge may be a convention/reframe or supplied-context theorem, not
necessarily a new axiom. Therefore this note does not classify the residual as
"new axiom required."

### N7 - Steelman

A hostile reviewer can object that the formal equivariance of
`J(j) = sum_c j_c O_c` does not make `rho_g` a physical gauge operation. Source
controls may be physical dial settings, realized-sector data, or couplings to a
specific charged-lepton block; a nonuniform ray could then be invariantly
meaningful even though the coordinate names can be relabeled. The minimal
axioms and approved primitives explicitly do not supply source/action,
weighting, normalization, or observable-identification bridges, so treating
naturality as automatic would launder a new source principle into W5b.

This steelman is accepted. The shipped result is therefore conditional bridge
support, not a retained W5b derivation.

### N8 - Cross-Cycle Echo

Similar bridge-shaped residuals appear in the live review surface:

| prior or parallel wall | status | lesson for this note |
|---|---|---|
| `AC_phi_lambda` species bridge | still live in open PR context | abstract-to-physical bridge content cannot be assumed from algebraic symmetry alone |
| R-eta `Phi = S_sum = 2/3` readout license in `#4945` | open no-go surface | readout-license shortcuts remain blocked unless the physical bridge is explicit |
| R-eta `Phi = Tr L_3^+ = 2/3` transport equality in `#4946` | open no-go surface | same-surface transport arithmetic still needs a physical readout bridge |
| K/CPT orbit-constancy bridge in `#4938` | merged supplied-context repair | supplied context can repair a bridge, but only when the supplied property is named and scoped |
| theta determinant-character/readout boundaries | live hygiene context | determinant/readout algebra does not automatically supply physical source selection |

The same mechanism could apply here: ratify source-family naturality as a
named supplied context or convention, then audit whether the import can be
retired. This note records that path instead of declaring closure.

Gate result: `PASS` for the narrowed source-family naturality bridge support.

## Non-Claims

- No derivation of `S_l = 1/256`.
- No derivation of the source-coupled local-action convention.
- No derivation that the charged-lepton scalar source is a full-cell
  slot-resolved source family.
- No derivation that source controls are nonnegative source strengths.
- No derivation that charged-lepton source strength is physically the
  projective ray `[j]`.
- No unconditional derivation that source-family naturality is physically
  licensed.
- No derivation that `S_l` reads `sigma([j])_c`.
- No derivation of the `256.08` precision correction.
- No derivation of `m_e`, Koide readout, `alpha(0)`, or hydrogen spectroscopy.
- No audit status change for any cited row.
- No new axiom, primitive, or admitted import.
