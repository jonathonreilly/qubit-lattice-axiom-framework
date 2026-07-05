# Zero-Import Hydrogen: Lepton `1/256` Source-Shape Readout Selector Discriminator

**Date:** 2026-07-04
**Type:** partial discriminator / positive support note
**Claim type:** conditional source-readout selector support
**Status:** support-only. This note does not promote a retained mass claim,
does not derive `S_l = 1/256`, and does not derive hydrogen.
**Verifier:** `scripts/frontier_zero_import_hydrogen_lepton_256_source_shape_readout_selector_discriminator.py`

## Scope

The source-coupling gauge quotient note decomposes a positive source-control
pair into an overall front and a normalized shape:

```text
S_src[j] = h * B_lep * J(j),
J(j) = sum_{c in C} j_c O_c,
H = h * sum_c j_c,
h * J(j) = H * sum_c sigma([j])_c O_c,
sigma([j])_c = j_c / sum_d j_d.
```

This note asks the next selector question:

```text
If the charged-lepton scale has one source-shape slot S_l after the common
front has been separated, which named scalar survives the source-shape
criteria?
```

The answer is conditional and narrow. Among the current named candidates in
the source chain, only `sigma([j])_c` is simultaneously:

1. invariant under `(h, j) -> (h/lambda, lambda j)`;
2. independent of the common source-coupling front;
3. a singleton coordinate of a normalized finite source-strength shape; and
4. equal to `1/256` on the uniform 256-coordinate ray.

Raw `h`, raw `j_c`, the product `h*j_c`, the total front `H`, projection/Born
trace `1/16`, and RN/Fisher source-unit amplitude `1/16` all fail at least one
of those source-shape criteria. This supports the selector step inside the
source-probe interface, but it still does not ratify that the physical
charged-lepton `S_l` symbol must read the source-shape coordinate.

## Selector Criteria

Let

```text
C = {0,1,2,3}^4,
|C| = 256,
j in R_{\ge 0}^C \ {0},
h > 0.
```

For a source-shape singleton readout, require:

| criterion | meaning |
|---|---|
| Q1 gauge invariance | the scalar is unchanged by `(h,j) -> (h/lambda, lambda j)` |
| Q2 front independence | the scalar does not carry the common source-coupling front |
| Q3 normalized shape | the singleton coordinates sum to one over `C` |
| Q4 uniform-ray value | the uniform ray gives singleton value `1/256` |

The current candidate table is:

| candidate | Q1 | Q2 | Q3 | Q4 | verdict |
|---|---:|---:|---:|---:|---|
| `h` | no | no | no | no | raw coupling/front, not a source-shape coordinate |
| `j_c` | no | yes | no | no | raw source-control amplitude, gauge dependent |
| `h*j_c` | yes | no | no | no | invariant coefficient, but still front-bearing |
| `H = h sum_c j_c` | yes | no | no | no | global front, not singleton shape |
| `(h*j_c)/H` | yes | yes | yes | yes | equals `sigma([j])_c` |
| `sigma([j])_c` | yes | yes | yes | yes | normalized projective source-shape coordinate |
| RN/Fisher amplitude `1/16` | yes | yes | no | no | L2/Fisher source-unit amplitude, not L1 singleton shape |
| projection/Born trace `1/16` | yes | yes | no | no | rank-one event trace in `M_16(C)`, not matrix-unit source-strength density |

Thus the quotient does not merely produce another way to write the same
ambiguity. It separates the common amplitude `H` from the normalized shape.
If the `S_l` slot is a source-shape singleton, the only current candidate that
matches the quotient criteria is:

```text
S_l candidate = sigma([j])_c = (h*j_c)/H.
```

The equality with `(h*j_c)/H` is not an independent new readout. It is the
same normalized projective shape expressed through the gauge-invariant source
coefficient and total front.

## What This Moves

Before this note, the quotient support showed that the raw pair `(h,j)` has a
clean decomposition, while the `S_l` readout bridge said that `S_l` equals
`sigma([j])_c` if the source-readout convention is supplied. This note narrows
the gap between those two statements:

```text
If S_l is the dimensionless normalized source-shape singleton after the common
front is separated, the current source chain selects sigma([j])_c and rejects
the other named candidates.
```

The remaining physical question is not arithmetic:

```text
Does the charged-lepton scale definition require S_l to be that normalized
source-shape singleton?
```

That remains a source-probe interface ratification or derivation target.

| sub-wall | status after this note |
|---|---|
| source-coupled local-action convention | still supplied/conditional |
| charged-lepton full-cell source family | still supplied/conditional |
| positive/projective source-strength semantics | still supplied/conditional |
| front/source-shape quotient | supported by the gauge quotient note |
| source-shape readout selector among named candidates | narrowed here to `sigma([j])_c` under Q1-Q4 |
| physical adoption of the `S_l` source-shape role | still open |
| uniform-ray/label-free interface | still conditional on the source-probe interface |
| A3 precision, Koide/electron readout, `alpha(0)`, hydrogen | still open |

## Authority Boundary

| source | supplies | boundary here |
|---|---|---|
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_COUPLING_GAUGE_QUOTIENT_PROJECTIVIZATION_SUPPORT_2026-07-04.md` | invariant decomposition into `H` and `sigma([j])_c` | no physical adoption of the `S_l` source-shape role |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_S_L_READOUT_IDENTITY_BRIDGE_SUPPORT_2026-07-04.md` | if `S_l` is the normalized singleton source-strength multiplier, then `S_l = sigma([j])_c` | assumes the readout convention |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROJECTIVE_SIMPLEX_SECTION_SUPPORT_2026-07-04.md` | projective L1 section of a nonzero nonnegative source ray | assumes projective source-strength semantics |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_POSITIVE_CONE_DISCRIMINATOR_2026-07-04.md` | source-strength positivity after monotone finite-additive semantics are supplied | no `S_l` readout convention |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_READOUT_MEASURE_DISCRIMINATOR_2026-07-04.md` | projection/Born trace on `M_16(C)` gives the `1/16` class | not the L1 matrix-unit source-shape singleton |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_L1_SOURCE_NORM_DISCRIMINATOR_2026-07-04.md` | L1 algebra-coordinate density is the `1/256` class once that source norm is selected | no physical adoption of `S_l` |
| `SOURCE_MEASURE_PCAL_RN_COCYCLE_THEOREM_NOTE_2026-05-30.md` | RN/Fisher source-unit normalization gives uniform 256-channel amplitude `1/16` | not the L1 singleton source-shape coordinate |
| approved primitives | scale reference, OS0 kinetic-form isotropy, realized-state discipline, and minimal axiom content | no source/action bridge, weighting rule, normalization rule, source-strength order, projective source semantics, source-probe interface, mass value, or `S_l` |

The primitive registry was checked against the fresh origin-main methodology.
Approved primitives chain-satisfy their own roles, but they do not supply the
source-shape readout selector as a physical charged-lepton `S_l` rule.

## Open PR Alignment

Open PRs were checked on 2026-07-04 after `origin/main` advanced and after
`#4959` appeared, then refreshed again after `#4960` appeared. The current
moving review surface is:

| PR | current effect on this source-shape selector lane |
|---|---|
| `#4960` hypercharge downstream trace scope quarantine | `DIRTY`; hypercharge scope/audit requeue, no lepton source-shape readout theorem |
| `#4959` dynamic helper dependency audit-packet repair | `DIRTY`; audit-control-plane helper dependency discovery, no lepton source-shape readout theorem |
| `#4958` theta W2 physical registrability no-go | `CLEAN`; theta mass-side W2 registrability pruning, no lepton source-shape readout theorem |
| `#4957` Gate B helper-runner artifact repair | `DIRTY`; helper-runner/cache metadata repair, no lepton source-shape readout theorem |
| `#4956` AC first-order determinant retirement-readiness no-go | `CLEAN`; AC first-order determinant pruning, no lepton source-shape readout theorem |
| `#4955` gravity eikonal small-k remainder repair | `DIRTY`; gravity runner/audit repair, no lepton source-shape readout theorem |
| `#4954` stale sibling-interface runner repair | `CLEAN`; runner-interface hygiene, no lepton source-shape readout theorem |
| `#4953` K-real physicalization current-surface no-go | `CLEAN`; AC/theta K-real physicalization pruning, no lepton source-shape readout theorem |
| `#4952` Qualification unfixed-choice clarification | closed without merge; adjacent law-level unfixed-choice route only if equivalent retained authority exists, no `S_l` readout theorem |
| `#4951` theta mass determinant-bridge retirement-readiness no-go | `CLEAN`; theta mass-side determinant-readout pruning, no lepton source-shape readout theorem |
| `#4950` additive-even premise relocation onto K/CPT bridge | merged into `main` at 2026-07-04T16:10:45Z; theta-chain premise-edge repair, no lepton source-shape readout theorem |
| `#4943` stale-green runner-cache repair sweep | `DIRTY`; runner/cache hygiene, no source-shape readout theorem |
| `#4940` rule achirality from minimality | `CLEAN`; theta/admissibility achirality context, no charged-lepton source/action bridge |
| `#4902`, `#4905`, `#4906` Koide occupancy/slot/phase stack | Koide/electron readout context, no source-shape readout ratification |

Thus no open PR currently ratifies the charged-lepton `S_l` slot as the
normalized source-shape singleton.

## No-Go Discipline Gate

This section prevents overclaiming. The broad claim "`S_l` is now retained as
`sigma([j])_c`" is **not** shipped. The narrowed claim is:

```text
Under the stated source-shape selector criteria Q1-Q4, the current source
chain selects sigma([j])_c and rejects the other named candidates. Physical
adoption of S_l as that source-shape singleton remains a separate interface
ratification or derivation target.
```

Verdict tag: broad `S_l` closure fails; narrowed source-shape readout selector
discriminator passes.

### N1 - Alternative Route Enumeration

| route | attempt | result |
|---|---|---|
| normalized projective shape | Use `sigma([j])_c` as the source-shape singleton. | SUPPORTED CONDITIONALLY. It satisfies Q1-Q4 under positive projective source semantics. |
| raw control `j_c` | Read the source amplitude directly. | ATTEMPTED. It fails Q1 and Q3 because it rescales and is not normalized. |
| raw coupling `h` | Read the coupling front as the scalar slot. | ATTEMPTED. It fails Q1-Q4 and is not coordinate shape. |
| source coefficient `h*j_c` | Read the invariant source coefficient. | ATTEMPTED. It passes Q1 but fails Q2-Q3 because it carries the common front. |
| total front `H` | Read the invariant total source front. | ATTEMPTED. It passes Q1 but fails singleton-shape criteria. |
| RN/Fisher source-unit amplitude | Transfer the retained source-unit amplitude class. | ATTEMPTED BY PRIOR. It gives `1/16` and fails the L1 singleton-shape criteria. |
| projection/Born trace | Read a rank-one event in `M_16(C)`. | ATTEMPTED BY PRIOR. It gives `1/16`, not the matrix-unit source-shape singleton. |
| lattice `y_0 = g_2^2/64` bridge | Identify `S_l` with the lattice weak convention. | OPEN SEPARATE ROUTE. It could bypass this selector, but it needs its own charged-lepton bridge. |

### N2 - Wall-Independence Audit

The relevant wall set is:

| wall | content |
|---|---|
| S1 | source/action convention and full-cell source family are supplied |
| S2 | source strength is a nonzero nonnegative projective shape |
| S3 | the common front is separated from source shape |
| S4 | `S_l` is physically the source-shape singleton slot |
| S5 | label-free/uniform-ray interface supplies the uniform ray |
| S6 | A3 precision, Koide/electron readout, and alpha running are supplied |

| pair | closes automatically? | conclusion |
|---|---|---|
| S1 with S2-S6 | no | action/source family does not supply projective strength, front separation, `S_l`, uniformity, or downstream hydrogen inputs |
| S2 with S3-S6 | no | projective shape semantics permit the selector but do not separate the front or name `S_l` |
| S3 with S4-S6 | no | quotient algebra selects a shape candidate but does not physically bind `S_l` |
| S4 with S5-S6 | no | `S_l` shape readout does not force the ray uniform or derive precision/electron/alpha |
| S5 with S6 | no | exact source-side `1/256` does not derive A3, electron mass, or `alpha(0)` |

This note conditionally supports the S3/S4 selector interface only after the
source-shape role is demanded. It does not collapse S1-S2 or S4-S6.

### N3 - Hidden-Wall Scan

| phrase class | classification |
|---|---|
| `source-shape slot` | explicit selector hypothesis, not a retained `S_l` fact |
| `criteria Q1-Q4` | declared discriminator criteria, not hidden physics |
| `among current named candidates` | bounded candidate set, not universal uniqueness over all possible functions |
| `sigma([j])_c` | normalized projective shape coordinate, not automatically physical `S_l` |
| `approved primitives` / `registry` | registry-limited content only |
| `ratify` / `derive` | explicit remaining interface target |

No source/action convention, source-strength semantics, quotient semantics,
physical `S_l` binding, uniformity, A3 correction, electron readout, or
hydrogen value is hidden as background.

### N4 - Residual Matching

| cited surface | residual it attacks | residual here | match? |
|---|---|---|---|
| source-coupling gauge quotient support | separates common front `H` from normalized source shape | selector setup | yes |
| `S_l` readout identity bridge support | binds `S_l` to `sigma([j])_c` after readout convention is supplied | downstream source-shape role | yes |
| projective-simplex section support | supplies L1 section `sigma([j])_c` | candidate shape | yes |
| positive-cone discriminator support | supplies nonnegative domain after monotone source-strength semantics | domain guard | yes |
| readout-measure discriminator | projection/Born trace gives the `1/16` class | rejected alternative | yes |
| L1 source-norm discriminator | L1 algebra-coordinate density gives the `1/256` class | selector support | yes |
| RN/Fisher source-unit theorem | retained source-unit amplitude gives `1/16` | rejected alternative | yes |
| open theta/AC/audit PRs | adjacent science or audit hygiene | lepton source-shape selector | no; review context only |

Only matching source-shape/readout-selector residuals are counted as support.

### N5 - Rhetoric Audit

The note avoids saying "`sigma([j])_c` is `S_l`" unconditionally. Tested
resolutions are:

| resolution | tested? | outcome |
|---|---|---|
| gauge-pair rescaling | yes | `sigma([j])_c` and `(h*j_c)/H` are invariant |
| raw control and raw coupling | yes | fail source-shape criteria |
| coefficient and total front | yes | invariant but front-bearing/global, not normalized singleton shape |
| uniform source ray | yes | `sigma([u])_c = 1/256` |
| nonuniform positive ray | yes | normalized but not `1/256`, so uniformity remains separate |
| physical adoption as `S_l` | no | explicitly left live |

### N6 - Partial-Closure Path Scan

Legitimate closure paths remain:

1. derive from retained source/action structure that the charged-lepton
   scale slot is the normalized projective source-shape singleton; or
2. ratify the normalized label-free source-probe interface explicitly and
   pass it through review/audit as an import-retirement target; or
3. bypass this source-shape route by proving a separate charged-lepton bridge
   such as `S_l = y_0_lattice`.

The source-probe interface compression note is the nearest convention/reframe
target. This discriminator supports that route by showing which named scalar
the source-shape clause selects; it does not call the remaining wall a new
axiom.

The primitive registry was checked. Minimal axioms and approved primitives
chain-satisfy their own roles, but they do not supply source/action,
source-strength weighting, normalization, source-coordinate selection,
projective source-probe readout, `S_l`, A3, `m_e`, `alpha(0)`, or hydrogen.

### N7 - Steelman

A hostile reviewer can argue that this selector nearly closes W6: after the
quotient, every sensible dimensionless singleton source-shape coordinate is
just `sigma([j])_c`, and the lepton-scale notation has no other remaining
source slot. The strongest counter is that "sensible" is not retained
authority. The framework could still define `S_l` through a separate lattice
weak bridge, RG boundary, or electron-readout convention. Therefore this note
ships only as selector support inside the source-probe interface route.

### N8 - Cross-Cycle Echo

Prior framework lanes often become cleaner after a broad physical wall is
turned into a convention/interface target. The same mechanism could close this
wall if the normalized label-free source-probe interface is ratified. This
note preserves that path and does not misclassify the remaining selector
license as an impossible no-go.

**Gate result:** `PASS` for the narrowed source-shape readout selector
discriminator. Broad retained `S_l` closure is not claimed.

## Non-Claims

- No derivation of the source-coupled local-action convention.
- No derivation that the charged-lepton scalar source is the full-cell source
  family.
- No derivation that charged-lepton source strength is physically a nonzero
  nonnegative projective source shape.
- No derivation that `S_l` is physically the normalized source-shape singleton.
- No derivation that `S_l = sigma([j])_c` is retained.
- No derivation that `S_l = 1/256` is retained.
- No derivation of the `256.082435...` precision correction.
- No derivation of the Koide/electron branch or physical `m_e`.
- No derivation of `alpha(0)` or hydrogen spectroscopy.
- No new axiom, primitive, or admitted import.
- No audit status change for any cited row.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_zero_import_hydrogen_lepton_256_source_shape_readout_selector_discriminator.py
```

The verifier checks finite candidate-selector arithmetic, quotient invariance,
uniform and nonuniform source-shape cases, rejected readout alternatives,
authority boundaries, live PR alignment markers, no-go discipline markers, and
non-claim boundaries.
