# Zero-Import Hydrogen: Lepton `1/256` Source-Probe Interface Compression Support

**Date:** 2026-07-04
**Type:** partial positive support note
**Claim type:** conditional source-interface compression support
**Status:** support-only. This note does not promote a retained mass claim,
does not derive `S_l = 1/256`, and does not derive hydrogen.
**Verifier:** `scripts/frontier_zero_import_hydrogen_lepton_256_source_probe_interface_compression_support.py`

## Scope

The current Lane 6 source-scale chain has narrowed exact `1/256` to three
source-side licenses:

```text
L1: the charged-lepton scalar source/action interface is supplied;
L2: that source interface is label-free under tensor-frame source relabelings;
L3: S_l reads the normalized singleton source-strength multiplier.
```

The prior notes support many pieces of this chain, but their live residues are
spread across several names. This note compresses those residues into one
auditable target:

```text
the normalized label-free charged-lepton full-cell source-probe interface.
```

That interface is a ratification or derivation target. It is not silently
available from the minimal axioms or approved primitives.

## Interface Compression Target

The compressed source-probe interface has four clauses.

1. **Full-cell source/action clause.** The charged-lepton scalar source is a
   lepton-specific full OS0-cell source coupled at the local action level:

```text
C = {0,1,2,3}^4,
|C| = 256,
S_lep[j] = h * B_lep * sum_{c in C} j_c O_c.
```

2. **Label-free source-coordinate clause.** The source controls carry no
   physical coordinate tag beyond the supplied tensor-frame source family
   `J(j) = sum_c j_c O_c`. Tensor-frame relabelings preserving this family are
   source-coordinate isomorphisms, not different physical source systems.

3. **Projective source-strength clause.** Source strength is the real
   monotone nonzero nonnegative projective ray `[j]`, with the L1 section

```text
sigma([j])_c = j_c / sum_d j_d.
```

The raw source-coupling/control pair is read through the quotient

```text
H = h * sum_c j_c,
h * J(j) = H * sum_c sigma([j])_c O_c,
```

so `H` carries the common source-coupling front and `sigma([j])_c` carries the
normalized source-shape coordinate.

4. **`S_l` source-readout clause.** In the charged-lepton scale factorization

```text
y_scale = g_2 * (1/sqrt(2)) * S_l,
```

`S_l` denotes the normalized singleton source-strength multiplier
`sigma([j])_c`.

## Conditional Compression Theorem

If the normalized label-free source-probe interface is supplied, then the
existing source chain composes as follows.

First, the source-coupled local action gives one scalar-multiplied source
insertion per full-cell coordinate:

```text
dS_lep/dj_c = h * B_lep * O_c.
```

Second, label-freeness makes tensor-frame source relabelings coordinate
isomorphisms of the same physical source interface. Therefore source-family
naturality supplies W5b:

```text
[j] = [rho_g j].
```

Third, the finite tensor-frame action is transitive on `C`. Since every
generator has finite order, positive projective scale characters are trivial.
The source ray is therefore uniform, and the projective L1 section gives

```text
sigma([j])_c = 1/256.
```

Fourth, the source-readout clause identifies

```text
S_l = sigma([j])_c.
```

Thus, under the compressed interface,

```text
S_l = 1/256.
```

This is a conditional composition theorem. It does not ratify the compressed
interface and does not account for the `256.082435...` precision residual.

## What This Moves

| before this note | after this note |
|---|---|
| source/action convention, label-free naturality, projective source strength, and `S_l` readout appeared as separate live licenses | one explicit normalized label-free source-probe interface can be derived, ratified, or rejected |
| exact `1/256` source-side closure required cross-reading multiple support notes | the dependency chain is a single interface implication with finite verifier checks |
| failure modes were named at different layers | each omitted interface clause has a concrete wrong-output counterexample |

The source-probe ratification target discriminator
`ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROBE_RATIFICATION_TARGET_DISCRIMINATOR_2026-07-04.md`
then tests this compressed target for minimality: the full F/L/P/R interface
closes the exact source-side scaffold conditionally, while every
one-clause-removed target fails with a concrete witness or an unbound `S_l`
symbol.

The live source-side target is now sharper:

```text
derive or ratify the normalized label-free charged-lepton full-cell
source-probe interface.
```

If that target is accepted through the normal review and audit path, the exact
source-side `S_l = 1/256` scaffold is conditionally closed. The hydrogen goal
would still need A3 precision, Koide/electron species readout, and `alpha(0)`.

## Clause Failure Boundaries

| omitted clause | what goes wrong |
|---|---|
| no full-cell source/action clause | there is no lepton-specific 256-coordinate action-source family attached to the D17 block |
| no label-free clause | a coordinate tag can select a nonuniform source ray |
| no monotone positive source-strength clause | signed or complex raw probes can produce negative, unordered, or undefined normalized weights |
| no projective source-strength clause | raw source controls rescale against `h`, so total strength and singleton weight are gauge-section choices |
| no source-coupling gauge quotient clause | the raw pair `(h,j)` has no assigned split into common front `H` and normalized source-shape coordinate `sigma([j])_c` |
| no source-shape readout selector clause | raw `h`, raw `j_c`, front-bearing `h*j_c`, or global `H` can be confused with the normalized source-shape singleton |
| RN/Fisher source-unit readout instead of L1 source-strength readout | a uniform 256-channel source unit gives `1/sqrt(256) = 1/16`, not `1/256` |
| no `S_l` source-readout clause | the chain derives `sigma([j])_c`, but not the lepton-scale symbol `S_l` |
| no A3 precision theorem | exact `256` is not the comparator divisor `256.082435...` |
| no Koide/electron readout | a charged-lepton scale handle is not yet the physical electron mass |

## Authority Boundary

| source | supplies | boundary here |
|---|---|---|
| `OBSERVABLE_PRINCIPLE_SOURCE_COUPLED_LOCAL_ACTION_ADMISSION_CANDIDATE_NOTE_2026-05-21.md` | open-gate source-coupled local-action convention shape | not retained authority for the lepton source-probe interface |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_COUPLED_ATTACHMENT_SUPPORT_2026-07-04.md` | conditional derivative attachment `dS_lep/dj_c = h * B_lep * O_c` | assumes source-coupled convention and lepton full-cell source |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_FULL_CELL_SOURCE_CARRIER_SUPPORT_2026-07-04.md` | `M_2(C)^tensor4` gives `256` coordinates after full-cell source locality is supplied | no derivation of physical lepton source locality |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_NATURALITY_LABEL_FREE_LICENSE_SUPPORT_2026-07-04.md` | label-free interface implies source-family naturality and W5b | assumes the label-free source-interface license |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_POSITIVE_CONE_DISCRIMINATOR_2026-07-04.md` | monotone finite-additive source-strength semantics forces singleton nonnegativity and separates source strengths from signed/complex probes | assumes source-strength semantics are physically supplied |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_COUPLING_GAUGE_QUOTIENT_PROJECTIVIZATION_SUPPORT_2026-07-04.md` | decomposes `(h,j)` modulo positive rescaling into invariant overall front `H` and normalized source-shape coordinate `sigma([j])_c` | assumes positive source-strength controls and does not ratify the `S_l` readout rule |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_SHAPE_READOUT_SELECTOR_DISCRIMINATOR_2026-07-04.md` | under source-shape criteria Q1-Q4, selects `sigma([j])_c = (h*j_c)/H` among current named candidates | does not physically bind `S_l` to that source-shape singleton |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROJECTIVE_SIMPLEX_SECTION_SUPPORT_2026-07-04.md` | projective L1 section `sigma([j])_c` | assumes projective source-strength semantics |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_SOURCE_PROJECTIVE_TENSOR_FRAME_UNIFORM_RAY_SUPPORT_2026-07-04.md` | W5b plus transitivity gives `sigma([j])_c = 1/256` | assumes W5b |
| `ZERO_IMPORT_HYDROGEN_LEPTON_256_S_L_READOUT_IDENTITY_BRIDGE_SUPPORT_2026-07-04.md` | `S_l = sigma([j])_c` after source-readout convention is supplied | assumes physical adoption of that convention |
| `MINIMAL_AXIOMS_2026-06-29.md` | lattice, one-site possibility algebra, admissibility, record formation and fixed record readout | no source/action bridge, weighting rule, normalization rule, probability rule, source-probe interface, or mass value |
| approved primitives | scale reference, OS0 kinetic-form isotropy, realized-state evaluation discipline | no source/action convention, source-coordinate selector, source-strength weighting, readout bridge, mass value, or empirical match |

The primitive registry was checked. Approved primitives are not walls, but they
also do not supply the source-probe interface.

## Open PR Alignment

Open PRs were checked on 2026-07-04 before writing this note and refreshed
after `#4956` appeared and `#4952` closed without merge, then again after
`#4957` appeared, then again after `#4958` appeared and `#4950` merged, then
again after `#4959` appeared, and again after `#4960` appeared. The current
moving review surface is:

| PR | current effect on this source-probe interface lane |
|---|---|
| `#4960` hypercharge downstream trace scope quarantine | `DIRTY`; hypercharge scope/audit requeue, no lepton source-probe interface |
| `#4959` dynamic helper dependency audit-packet repair | `DIRTY`; audit-control-plane helper dependency discovery, no lepton source-probe interface |
| `#4958` theta W2 physical registrability no-go | `CLEAN`; theta mass-side W2 registrability pruning, no lepton source-probe interface |
| `#4957` Gate B helper-runner artifact repair | `DIRTY`; helper-runner/cache metadata repair, no lepton source-probe interface |
| `#4956` AC first-order determinant retirement-readiness no-go | `CLEAN`; AC first-order determinant pruning, no lepton source-probe interface |
| `#4955` gravity eikonal small-k remainder repair | `DIRTY`; gravity runner/audit repair, no lepton source-probe interface |
| `#4954` stale sibling-interface runner repair | `CLEAN`; runner-interface hygiene and one escalated `g_bare` science regression, no lepton source-probe interface |
| `#4953` K-real physicalization current-surface no-go | `CLEAN`; AC/theta K-real physicalization pruning, no lepton source-probe interface |
| `#4952` Qualification unfixed-choice clarification | closed without merge; law-level anti-unfixed-choice support only if equivalent retained authority exists, and no lepton source/action bridge, source-probe normalization, or `S_l` theorem |
| `#4951` theta mass determinant-bridge retirement-readiness no-go | `CLEAN`; theta mass-side determinant-readout pruning, no lepton source-probe interface |
| `#4950` additive-even premise relocation onto K/CPT bridge | merged into `main` at 2026-07-04T16:10:45Z; theta-chain premise-edge repair, no lepton source-probe interface |
| `#4949` theta closed-nonexact sector-record no-go | `CLEAN`; theta-side sector-record pruning, no lepton source interface |
| `#4948` theta G1 exact-branch no-go | `CLEAN`; theta exact-branch pruning, no lepton source interface |
| `#4947` R-eta K-breaking transport no-go | `CLEAN`; AC(ii)/R-eta route pruning, no `S_l` source theorem |
| `#4943` stale-green runner-cache repair sweep | `DIRTY`; runner/cache hygiene, no source-probe theorem |
| `#4940` rule achirality from minimality | `CLEAN`; theta/admissibility achirality context, no charged-lepton source/action bridge |
| `#4902`, `#4905`, `#4906` Koide occupancy/slot/phase stack | Koide/electron readout context, no source-probe interface ratification |

Thus no open PR currently ratifies the compressed charged-lepton source-probe
interface.

## No-Go Discipline Gate

This section prevents overclaiming. The broad claim "`S_l = 1/256` is now
retained" is **not** shipped. The narrowed claim is:

```text
If the normalized label-free charged-lepton full-cell source-probe interface
is supplied, then the existing source-chain notes compose to exact
S_l = 1/256.
```

Verdict tag: broad `S_l` closure fails; narrowed interface-compression support
passes.

### N1 - Alternative Route Enumeration

| route | attempt | result |
|---|---|---|
| compressed source-probe interface | Adopt the four clauses as one normalized label-free charged-lepton source-probe interface. | SUPPORTED CONDITIONALLY here. It composes prior notes to exact `S_l = 1/256`. |
| source-coupled action only | Use only `S_lep[j] = h B_lep sum_c j_c O_c`. | ATTEMPTED BY PRIOR. It gives derivative attachment but not label-free naturality, projective normalization, or `S_l`. |
| label-free naturality only | Use source-coordinate isomorphism invariance. | ATTEMPTED BY PRIOR. It gives W5b after the interface is supplied, but not source/action, projective semantics, or `S_l`. |
| monotone positive source-strength only | Use the ordered source-strength domain to force nonnegative singleton strengths. | ATTEMPTED BY PRIOR. It separates strengths from signed probes but does not projectivize, force uniformity, or identify `S_l`. |
| projective L1 section only | Normalize a positive source ray by `sigma([j])`. | ATTEMPTED BY PRIOR. It fixes the gauge section but not the uniform ray or `S_l`. |
| RN/Fisher source-unit route | Transfer primitive source-unit normalization to 256 channels. | ATTEMPTED BY PRIOR. It gives `1/16`, not `1/256`. |
| projection/Born trace route | Read a rank-one event in `M_16(C)`. | ATTEMPTED BY PRIOR. It gives `1/16`, not matrix-unit source-strength density. |
| lattice `g_2^2/64` route | Identify `S_l` with the lattice `y_0` convention. | OPEN SEPARATE ROUTE. It needs a charged-lepton bridge `S_l = y_0_lattice` and does not ratify this interface. |
| empirical comparator route | Use observed `m_W/256` or the noninteger divisor directly. | RULED OUT AS ZERO-IMPORT ROUTE. Comparator data is not proof input. |

### N2 - Wall-Independence Audit

The collapsed wall set after this compression is:

| wall | content |
|---|---|
| C1 | normalized label-free charged-lepton full-cell source-probe interface is derived or ratified |
| C2 | A3 places or derives the `256.082435...` correction |
| C3 | Koide/electron readout supplies the physical electron branch |
| C4 | alpha-running gates supply `alpha(0)` without import |

| pair | closes automatically? | conclusion |
|---|---|
| C1 with C2 | no | exact `S_l = 1/256` does not place the precision correction |
| C1 with C3 | no | source-scale suppression does not choose the electron species/readout branch |
| C1 with C4 | no | lepton scale does not derive low-energy Coulomb coupling |
| C2 with C3 | no | precision placement does not derive Koide/electron readout |
| C2 with C4 | no | A3 precision does not derive QED/hadronic running |
| C3 with C4 | no | electron mass does not derive `alpha(0)` |

The previous source-side licenses are intentionally collapsed into C1 only if
they are adopted as one interface. Without that ratification, the older
sub-walls remain live.

### N3 - Hidden-Wall Scan

| phrase class | classification |
|---|---|
| `source-probe interface` | explicit C1 target, not background |
| `ratify` / `derive` | explicit governance or theorem path, not a silent premise |
| `label-free` | explicit C1 clause |
| `projective` | explicit C1 clause |
| `S_l denotes` | explicit C1 source-readout clause |
| `approved primitives` / `registry` | registry-limited content only |
| `physical` | marks the license target, not an assumed theorem |

No source/action convention, source-strength semantics, label-free condition,
`S_l` readout identity, A3 correction, electron readout, or alpha input is
hidden as background.

### N4 - Residual Matching

| cited surface | residual it attacks | residual here | match? |
|---|---|---|---|
| source-coupled attachment support | action-derivative attachment after source convention and source family are supplied | C1 clause 1 | yes |
| full-cell source-carrier support | 256-coordinate carrier after lepton full-cell source locality is supplied | C1 clause 1 | yes |
| source-naturality label-free license support | label-free interface gives source-family naturality | C1 clause 2 | yes |
| source positive-cone discriminator support | monotone source-strength semantics forces nonnegative singleton strengths | C1 clause 3 | yes |
| source-coupling gauge quotient projectivization support | decomposes raw `(h,j)` into invariant `H` and normalized source-shape coordinate | C1 clause 3 | yes |
| source-shape readout selector discriminator | selects `sigma([j])_c` among named source-shape candidates under Q1-Q4 | C1 clauses 3-4 | yes |
| projective-simplex section support | normalized projective L1 source-strength section | C1 clause 3 | yes |
| tensor-frame uniform-ray support | W5b plus transitivity gives `1/256` | downstream of C1 clauses 2-3 | yes |
| `S_l` readout identity bridge support | source singleton equals `S_l` after W6 convention | C1 clause 4 | yes |
| A3 placement discriminator | locates precision correction responsibilities | C2, not C1 | guard only |
| Koide electron-readout firewall | electron branch/readout residuals | C3, not C1 | guard only |
| open theta PRs | theta gauge/readout hygiene | lepton source-probe interface | no; review context only |

Only matching source-interface residuals are counted as support.

### N5 - Rhetoric Audit

The note avoids saying "the interface is retained" or "`S_l` is retained."
Tested resolutions are:

| resolution | tested? | outcome |
|---|---|---|
| finite source coordinate count | yes | `|C| = 256` |
| tensor-frame transitivity | yes | one orbit on all coordinates |
| uniform projective source section | yes | singleton weight `1/256` |
| source-readout cancellation | yes | common nonzero front gives `S_l = sigma([j])_c` |
| failure of coordinate-tagged ray | yes | nonuniform ray requires extra tag content |
| RN/Fisher/projection alternatives | yes by prior notes | return `1/16` class |
| physical ratification of C1 | no | explicitly left live |
| A3, electron branch, alpha running, hydrogen | no | explicitly outside this note |

### N6 - Partial-Closure Path Scan

The legitimate closure path for C1 is not "add a new axiom." It is either:

1. derive the normalized label-free source-probe interface from existing
   retained source/action structure; or
2. ratify it as an explicit source-probe convention, then pass it through the
   normal review and audit path as an import-retirement target.

The observable-principle source-coupled local-action candidate is a relevant
partial-closure path: it already frames local source derivatives of `S` as
operator insertions without changing the axiom count. It does not by itself
ratify the lepton-specific normalized label-free source-probe interface.

The primitive registry was checked. Minimal axioms and approved primitives
chain-satisfy their own roles, but they do not supply source/action,
source-strength weighting, normalization, source-coordinate selection, `S_l`,
A3, `m_e`, `alpha(0)`, or hydrogen.

### N7 - Steelman

A hostile reviewer can argue that this compression is strong enough to be a
near-retirement proposal: the repo already has a source-coupled local-action
candidate, the full-cell source-carrier theorem supplies the only natural
OS0-cell carrier, label-freeness mirrors the minimal axiom "no privileged
possibility" discipline, and the lepton-scale notation has exactly one
remaining scalar slot `S_l`. On that reading, C1 is a convention-ratification
cleanup rather than new physics. The narrow reply is that "natural" is still
not retained authority: source/action, lepton-specific full-cell source
locality, normalized projective source strength, and `S_l` symbol binding must
be explicitly derived or ratified before exact `S_l = 1/256` can be promoted.

### N8 - Cross-Cycle Echo

Similar walls have been retired in the repo by moving from a broad physical
principle to a narrower convention or interface and then auditing that
interface. The source-coupled local-action admission candidate is the closest
same-shape example: it tries to replace a scalar-generator selection premise
with a local-action source convention while keeping the formal axiom count
fixed. The same mechanism could apply here if the lepton source-probe
interface is accepted as the controlled source convention for charged-lepton
scalar probes. This is why the note ships as interface-compression support,
not as a no-go or a retained theorem.

**Gate result:** `PASS` for the narrowed source-probe interface compression
support. Broad retained `S_l` closure is not claimed.

## Non-Claims

- No derivation or ratification of the normalized label-free source-probe
  interface.
- No derivation that `S_l = 1/256` is retained.
- No derivation of the `256.082435...` precision correction.
- No derivation of the Koide/electron branch or physical `m_e`.
- No derivation of `alpha(0)` or hydrogen spectroscopy.
- No new axiom, primitive, or admitted import.
- No audit status change for any cited row.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_zero_import_hydrogen_lepton_256_source_probe_interface_compression_support.py
```

The verifier checks the finite 256-coordinate composition, the clause-failure
counterexamples, authority boundaries, PR alignment markers, no-go discipline
markers, and non-claim boundary.
