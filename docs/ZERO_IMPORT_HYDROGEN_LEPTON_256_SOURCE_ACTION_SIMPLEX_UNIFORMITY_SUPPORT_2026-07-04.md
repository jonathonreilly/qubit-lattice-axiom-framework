# Zero-Import Hydrogen: Lepton `1/256` Source-Action Simplex Uniformity Support

**Date:** 2026-07-04
**Type:** partial positive support note
**Claim type:** conditional source-action support
**Status:** support-only. This note does not promote a retained mass claim,
does not derive `S_l = 1/256`, and does not derive hydrogen.
**Verifier:** `scripts/frontier_zero_import_hydrogen_lepton_256_source_action_simplex_uniformity_support.py`

## Scope

This note follows the source-action simplex transfer discriminator:

- `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_ACTION_SIMPLEX_TRANSFER_DISCRIMINATOR_2026-07-04.md`
  shows that the top/RN/Fisher primitive source-unit precedent gives
  `1/sqrt(256)=1/16` on a 256-channel uniform source, not `1/256`.
- `ZERO_IMPORT_HYDROGEN_LEPTON_256_RESTRICTED_TENSOR_FRAME_INVARIANCE_SUPPORT_2026-07-04.md`
  shows that once uniform L1 density is supplied, it is stable under
  tensor-frame relabelings.

The remaining positive finite question is sharper:

```text
If the charged-lepton scalar source is a linear action coefficient over the
supplied M_2(C)^tensor4 matrix-unit source frame, and the source coefficients
are invariant under tensor-frame coordinate relabelings, is 1/256 forced?
```

The answer is yes. This note proves that conditional finite theorem. It does
not prove that the charged-lepton source has those source-action semantics, does
not prove that the tensor frame is physical, and does not identify the result
with `S_l`.

## Conditional Theorem

Let

```text
C = {0,1,2,3}^4,
|C| = 256.
```

Assume the charged-lepton scalar source contribution has the linear action
coefficient form

```text
S_src = h * sum_{c in C} w_c O_c
```

with simplex normalization

```text
w_c >= 0,
sum_{c in C} w_c = 1.
```

Assume also that the supplied tensor-frame coordinates are physically
unprivileged under independent local relabelings of each `M_2(C)` algebra slot:

```text
G = S_4^4
```

acts on `C` by

```text
(sigma_1, sigma_2, sigma_3, sigma_4) . (c_1,c_2,c_3,c_4)
  = (sigma_1(c_1), sigma_2(c_2), sigma_3(c_3), sigma_4(c_4)).
```

Then `G` acts transitively on `C`: for any two coordinates `c,d in C`, choose
each `sigma_i` so that `sigma_i(c_i)=d_i`. Therefore any `G`-invariant
coefficient vector has a single value:

```text
w_c = w_* for every c in C.
```

Simplex normalization gives

```text
1 = sum_c w_c = 256 w_*,
w_* = 1/256.
```

So the unique tensor-frame-relabeling-invariant linear action simplex density
over the supplied `M_2(C)^tensor4` coordinate frame is exactly `1/256`.
In short, transitivity forces one coefficient, and simplex normalization fixes
that coefficient to `1/256`.

## Why The Assumptions Are Load-Bearing

The theorem does not make the assumptions disappear.

| weakened premise | result |
|---|---|
| simplex normalization replaced by L2/RN/Fisher unit normalization | invariant coefficient is `1/sqrt(256)=1/16` |
| local coordinate relabeling removed, keeping only slot permutations | the action has 35 orbits, not one; uniformity is not forced |
| source-action coefficient form removed | no reason to treat weights as linear action coefficients |
| physical tensor-frame selector removed | the fixed coordinate vector is not full `U(16)` invariant |
| charged-lepton source bridge removed | no identification with `S_l` |

Thus the theorem proves the finite uniformity target after a precise source
semantics and symmetry package is supplied. It does not supply that package.

## Exact Orbit Contrast

The distinction between local coordinate relabeling and weaker symmetries is
important.

| symmetry | orbit count on `{0,1,2,3}^4` | consequence |
|---|---:|---|
| independent local relabelings `S_4^4` | `1` | all 256 coordinates have one shared coefficient |
| tensor-frame relabelings `S_4^4 semidirect S_4` | `1` | same uniform coefficient |
| all coordinate bijections `S_256` | `1` | same uniform coefficient |
| slot permutations only `S_4` | `35` | coefficients may depend on the multiset of local labels |
| no symmetry | `256` | every coordinate weight is free subject to normalization |

So the physically useful target is not "uniformity by notation." It is a
retained theorem that the charged-lepton source action is symmetric under the
local coordinate relabelings of the supplied tensor frame.

## What This Moves

This note narrows the A2 work:

| sub-gate | standing after this note |
|---|---|
| A2.1 measure-domain selector | still open: source must be a linear action coefficient density, not projection probability or RN amplitude |
| A2.2 norm-domain selector | still open but sharpened: if simplex normalization is supplied, tensor-frame symmetry forces `1/256` |
| A2.3 basis/source-frame selector | still open: the tensor-product matrix-unit source frame must be physically supplied |
| A2.4 coefficient uniformity | conditionally closed under supplied simplex normalization plus local coordinate relabeling symmetry |
| A2.5 charged-lepton source bridge | still open: the selected coefficient must be identified with `S_l` |
| A2.6 precision interface | still open: exact `256` must connect to `256.082435...` or be replaced by a direct noninteger divisor theorem |

The next theorem target is now:

```text
charged-lepton scalar source action is a simplex-normalized linear coefficient
over a physical M_2(C)^tensor4 source frame, invariant under local coordinate
relabelings of that frame.
```

If that lands, the finite coefficient is no longer an independent choice.

## Repo Authority Alignment

| source | relevant boundary |
|---|---|
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_ACTION_SIMPLEX_TRANSFER_DISCRIMINATOR_2026-07-04.md` | Establishes that `1/256` belongs to linear action simplex density, not primitive RN/Fisher source-unit amplitude. |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_RESTRICTED_TENSOR_FRAME_INVARIANCE_SUPPORT_2026-07-04.md` | Establishes tensor-frame relabeling invariance once uniform density is supplied; this note derives uniformity from transitivity plus simplex normalization. |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_MATRIX_UNIT_BASIS_SELECTOR_DISCRIMINATOR_2026-07-04.md` | Establishes that fixed matrix-unit coefficient density is not full `U(16)` invariant; the physical source frame remains explicit. |
| `OBSERVABLE_PRINCIPLE_SOURCE_COUPLED_LOCAL_ACTION_ADMISSION_CANDIDATE_NOTE_2026-05-21.md` | Provides an open-gate source-coupled local-action convention candidate, not retained closure of lepton source-action semantics. |
| `SOURCE_MEASURE_PCAL_RN_COCYCLE_THEOREM_NOTE_2026-05-30.md` | Provides the RN/Fisher source-unit contrast, where uniform 256-channel coefficient is `1/16`. |
| `MINIMAL_AXIOMS_2026-06-29.md` | Supplies one-site `M_2(C)` and records-form content, but no source/action bridge, weighting, normalization, probability, or physical observable identification. |

## Primitive Boundary

The primitive registry was checked. Approved primitives can be used only to
their declared content:

| node | declared help | boundary here |
|---|---|---|
| `minimal_axioms` | `Z^3`, one-site `M_2(C)`, admissibility, record additivity, generic record formation | no source/action bridge, weighting, normalization, source frame, probability rule, or physical observable identification |
| `kinetic_isotropy_primitive` | OS0 kinetic-form isotropy and fourth regulator slot | no source-density selector, local coordinate relabeling theorem, readout bridge, or value |
| `scale_reference_primitive` | one dimensionful ruler | no dimensionless simplex coefficient |
| `realized_state_primitive` | pointwise realized-state evaluation | no state-selection rule, measure, weighting, normalization, preferred state, or mass value |

## Open PR Alignment

Open PRs were checked on 2026-07-04 before writing this support note:

| PR | effect on this source-action simplex uniformity support |
|---|---|
| `#4922`, `#4924` Born/composite Gleason and graded-constraint interface | Projection/frame-function context; does not supply linear action simplex semantics. |
| `#4923` record scope semantics / arrow substrate | Record-scope context; no source/action measure, frame selector, or simplex normalization. |
| `#4928` Tier-A block03 AC value face | Koide bookkeeping; no lepton `1/256` source-action theorem. |
| `#4929` Tier-A block04 species-bridge partial-retirement | Species-bridge import-retirement context; no source-action theorem for `S_l`. |
| `#4930` Tier-A block05 R-eta route pruning | R-eta route pruning; no lepton source simplex theorem. |
| `#4931` Tier-A block06 R-eta occurrence axiom shortcut | Blocks an occurrence-axiom shortcut for K2; no lepton source simplex theorem. |
| `#4932` Tier-A block07 AC measure binary axiom shortcut | Blocks an axiom/primitives shortcut for K1; no lepton `1/256` source simplex theorem. |
| `#4903` D4 kinetic pattern dichotomy | Potential A1 tensor-lift context; no A2 source-action density selector. |

## No-Go Discipline Gate

This section prevents overclaiming. The broad claim "the simplex route closes
`S_l`" is **not** shipped. The narrowed claim is:

```text
Given a supplied physical M_2(C)^tensor4 source frame, linear action simplex
normalization, and local coordinate relabeling invariance, the coefficient is
uniquely 1/256. The theorem does not supply those physical selectors or
identify the coefficient with S_l.
```

Verdict tag: broad no-go fails; narrowed source-action simplex uniformity support passes.

### N1 - Alternative route enumeration

| route | attempt | result |
|---|---|---|
| local coordinate relabeling symmetry | Use `S_4^4` transitivity to force one coefficient. | SUPPORTED. Together with simplex normalization it gives `1/256`. |
| full tensor-frame relabeling symmetry | Add slot permutations to local relabelings. | SUPPORTED. The action is still transitive and gives `1/256`. |
| arbitrary coordinate-bijection symmetry | Use all bijections of the 256 labels. | SUPPORTED as finite-set arithmetic; stronger than needed. |
| slot permutations only | Use only the four-slot permutation group. | ATTEMPTED. It gives 35 orbits, so uniformity is not forced. |
| RN/Fisher primitive source unit | Replace simplex normalization by source-unit normalization. | ATTEMPTED. It gives `1/16`, not `1/256`. |
| full `U(16)` covariance | Treat fixed matrix-unit coordinates as full-algebra invariant. | RULED OUT AS CLOSURE by the basis-selector discriminator. |
| determinant/log-volume route | Bypass simplex coordinates with invariant volume density. | OPEN. Not supplied here. |
| charged-lepton source bridge | Identify the selected coefficient with `S_l`. | OPEN. Not supplied here. |

### N2 - Wall-independence audit

The collapsed wall set is:

| wall | content |
|---|---|
| W1 | A1 carrier: the charged-lepton scalar source carries the four OS0 algebra slots |
| W2 | A2.1 measure-domain selector: source is a linear action coefficient density |
| W3 | A2.2 norm-domain selector: simplex normalization rather than L2/RN/Fisher unit |
| W4 | A2.3 basis/source-frame selector: tensor-product matrix-unit source frame is physical |
| W5 | A2.4 local coordinate relabeling symmetry of the source coefficients |
| W6 | A2.5 charged-lepton sector/source identity for `S_l` |
| W7 | A2.6/A3 precision correction from exact `256` to the comparator divisor |

Pairwise audit:

| pair | closes automatically? | conclusion |
|---|---|---|
| W1 with W2-W7 | no | carrier does not choose measure, norm, frame, symmetry, sector identity, or precision |
| W2 with W3-W7 | no | linear action semantics does not by itself choose normalization, frame, symmetry, sector identity, or precision |
| W3 with W4-W7 | no | simplex normalization does not choose frame, symmetry, sector identity, or precision |
| W4 with W5-W7 | no | frame selection does not automatically prove coefficient symmetry, sector identity, or precision |
| W5 with W6-W7 | no | coefficient uniformity does not identify `S_l` or fix precision |
| W6 with W7 | no | sector identity does not derive the precision correction |

This note conditionally closes W5 only after W2-W4 are supplied. It leaves the
other walls live.

### N3 - Hidden-wall scan

| phrase class | classification |
|---|---|
| `assume` / `supplied` | explicit theorem hypotheses, not derived results. |
| `unprivileged` | encoded as local coordinate relabeling invariance, not rhetoric. |
| `simplex normalization` | explicit W3 hypothesis. |
| `physical source frame` | explicit W4 target. |
| `source action` | explicit W2 target. |
| `primitive` | registry-limited content only. |

No source-action, symmetry, or sector-identity assumption is left buried.

### N4 - Residual Matching

| cited surface | residual it attacks | match to this note |
|---|---|---|
| source-action simplex transfer discriminator | source-unit transfer versus simplex density | yes |
| restricted tensor-frame support | relabeling invariance after uniformity | yes, strengthened here by deriving uniformity from transitivity |
| matrix-unit basis-selector discriminator | full `U(16)` covariance firewall | yes as boundary |
| RN-cocycle source-measure theorem | L2/RN/Fisher source-unit contrast | yes |
| open PRs `#4930`-`#4932` | Koide K1/K2 hygiene | no direct `S_l` closure |

Only the finite simplex-uniformity residual is counted as supported here.

### N5 - Rhetoric Audit

The note avoids saying "`S_l` is derived" or claiming A2 closure. Tested
resolutions are:

| resolution | tested? | outcome |
|---|---|---|
| local relabeling group `S_4^4` | yes | transitive; coefficient `1/256`. |
| tensor-frame group `S_4^4 semidirect S_4` | yes | transitive; coefficient `1/256`. |
| full coordinate bijections `S_256` | yes | transitive; coefficient `1/256`. |
| slot permutations only | yes | 35 orbits; uniformity not forced. |
| no symmetry | yes | 256 free weights subject to normalization. |
| L2/RN source unit | yes | `1/16`. |
| physical charged-lepton source-action theorem | not closed | named W2-W6. |

### N6 - Partial-Closure Path Scan

Legitimate closure paths remain:

| path | what it could close |
|---|---|
| retained theorem that the lepton scalar source is a linear action simplex over the tensor-frame coordinates | W2-W3 |
| retained theorem that local coordinate relabeling symmetry is physical for that source | W5 |
| retained theorem deriving the four OS0 algebra slots on the scalar coefficient | W1 and part of W4 |
| determinant/log-volume theorem matching `1/256` invariantly | possible bypass of W4-W5 |
| charged-lepton source bridge identifying the selected coefficient with `S_l` | W6 |
| direct noninteger divisor theorem or controlled correction after exact `256` | W7 |

These are not called new axioms if derived or retired through audited
convention work.

### N7 - Steelman

A hostile reviewer can argue that once the framework supplies `M_2(C)^tensor4`
and no coordinate is privileged, local relabeling invariance should be
automatic. With simplex source-action semantics, this theorem then gives
`1/256` without any further numerical choice. This is a strong positive route.

The narrow rebuttal is that the current retained inventory has not yet shown
that the charged-lepton scalar source is a linear action simplex over that
tensor frame, nor that the physical source action is invariant under those
coordinate relabelings. Those are now the right theorem targets.

### N8 - Cross-Cycle Echo

This artifact avoids the recurring failure mode of treating a finite count as
the physical coefficient. It proves which added structure would force the
coefficient and keeps that structure explicit: simplex normalization,
physical tensor frame, and local coordinate relabeling symmetry.

## Non-Claims

- No derivation of `S_l = 1/256`.
- No derivation that the charged-lepton scalar source uses linear action
  simplex-density semantics.
- No derivation that the charged-lepton scalar source uses the tensor-product
  matrix-unit frame.
- No derivation that local coordinate relabeling symmetry is physically
  enforced for the charged-lepton source action.
- No derivation of the charged-lepton tensor lift.
- No derivation of the charged-lepton source bridge.
- No derivation of the `256.082435...` precision correction.
- No derivation of `m_e`, Koide readout, `alpha(0)`, or hydrogen spectroscopy.
- No audit status change for any cited row.
- No new axiom, primitive, or admitted import.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_zero_import_hydrogen_lepton_256_source_action_simplex_uniformity_support.py
```

The verifier checks transitivity, orbit counts, the unique simplex coefficient,
the L2/RN contrast, primitive boundaries, open PR context, no-go discipline
markers, and the non-claim boundary.
