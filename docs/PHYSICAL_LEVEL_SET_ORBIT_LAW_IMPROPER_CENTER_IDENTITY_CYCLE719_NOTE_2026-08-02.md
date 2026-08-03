# The level sets of the k-endpoint value functional are orbits of an order-12 assembly symmetry whose improper half carries no frame label — Cycle 719

Date: 2026-08-02

Claim type: bounded_theorem

Authority: none. Audit: unset. Constitutional effect: none. This cycle edits no
axiom, foundation, Qualification, primitive, registry, policy, queue,
audit-status, or PR-control surface. No new axiom or primitive is proposed or
adopted.

No coupling value, sign, or scale is selected or derived in this cycle; every
such object is named as supplied. The floating-point rows are conditional on the
fixed Cycle-696 compiler contract inventoried below; that compiler is a landed
but audit-excluded support surface, not an independent audit authority.

The frame dependence of the static endpoint value functional was previously
reduced to a four-valued body-diagonal label, with the sources whose four values
partially or fully merge left unexplained. This cycle explains all of them. The
exact stabilizer of the identity-frame static assembly inside the 24 proper
rotations is the six-element body-diagonal stabilizer and nothing more, with an
inside deviation of `1.243450e-10` against an outside deviation of
`4.000000e+00` at both box sizes; the value functional is therefore
body-diagonal-measurable for **every** source, not merely for the slot sources —
`98 of 98` and `279 of 279` slots, and drawn dense sources with within-label
spreads `7.581911e-12` and `2.214548e-10` against across-label gaps
`9.063688e-04` and `5.635424e-03`. The assembly additionally admits the
box-center point reflection, an involution that commutes with all 24 frames,
deviates from the assembly by `1.243450e-10`, and is equal to no frame; the
resulting symmetry has order `12 = 6 + 6`, and its improper half fixes each body
diagonal as an unsigned line and so carries no body-diagonal label at all. The
level sets of the diagonal value function are exactly the orbits of that
order-12 symmetry — `13` orbits at `L = 3` and `34` at `L = 4`, constant to
`2.391640e-11` and `7.638064e-10` and separated by `4.286579e-05` and
`1.264701e-04`. Full frame-blindness of a slot source is equivalent to its frame
stabilizer acting transitively on the four body diagonals (`6 = 6 = 6` and
`19 = 19 = 19`), and every one of the `180` and `450` merged value pairs is
carried by a symmetry: `24 / 50 / 106` and `70 / 110 / 270` split across
stabilizer, sextet, and center-reflection channels, with residue `0` in both
box sizes. The merges are not arithmetic accidents. They are symmetry, and the
majority channel is the one the frame label cannot name.

## Improper-relabelling framing

The box-center point reflection executed here has determinant `-1` on the
underlying spatial map. It is **not** an axiom symmetry — the Lattice axiom
names proper cubic rotations only, and nothing in this cycle enlarges the
framework's symmetry group or counts elements outside the 24. The reflection
enters this note ONLY as one of the computational identities of the compiled
chain: an exact relabeling of the static slot set that happens to preserve the
assembled operator, used here to classify the level structure of a quantity that
is itself defined over the 24 proper rotations. Every physical frame-scope
statement below — every use of the word label, every blindness count, every
coset — is over the 24 proper rotations alone. The reflection appears on the
classifying side of the equivalence, never on the claimed side.

## Setup

The compiled chain is the landed
[Cycle-696 open-coframe endpoint compiler](../scripts/physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py),
used verbatim and never re-implemented. The single object under study is the
static assembly

```
Q = c696.assemble_static_hessian(L, wrap=False)["Q"]
```

on the open spatial box at `L` in `(3, 4)`, with `n = 98` and `n = 279` static
slots respectively, together with `d = diag(Q^-1)`. Slots are indexed by
`c696.static_variable_index(L, wrap=False)`, whose keys are pairs `(c, x)` of a
spatial direction class in `c696.SPATIAL_CLASSES` and a low-corner site.

Frames are `c696.c576.FRAMES`, the 24 proper cubic rotations. The slot
relabeling induced by a frame `g` is built from `c696.frame_site_map(L, R)` and
the rotated direction word: the class is the rotated direction's class and the
site is the mapped site shifted by the negative part of the rotated direction.
This relabeling map is measured here to be a **homomorphism** of the 24 frames,
with mismatch `0`; the matrix convention of the corresponding permutation
matrices is the opposite composition, and the anti-homomorphism reading is
rejected at mismatch `64` and `177`. The relabeling is the object that acts;
that distinction is measured, not derived, and it is gated in the runner.

The body diagonals are the four unsigned lines `(1,1,1)`, `(1,1,-1)`,
`(1,-1,1)`, `(-1,1,1)`. The **sextet** is the stabilizer of `(1,1,1)` among the
24 frames, `[1, 4, 9, 15, 18, 23]`, of order `6`; the body-diagonal label of a
frame is `delta(g) = g^-1 . (1,1,1)`, and its four fibres are the four right
cosets of the sextet, each of size `6`. The value functional of a source `u` at
frame `g` is the Rayleigh quotient of the relabeled source against the single
identity-frame inverse assembly; for a single slot source this reduces to the
diagonal entry `d` at the relabeled slot.

The **box-center point reflection** is the slot relabeling
`(c, x) -> (c, (L-1) - x_a - |w_a|)`, where `w` is the direction word of class
`c`. It reflects the open box through its own center and carries each slot onto
the slot occupying the reflected region. That this map preserves the assembled
operator is measured, not derived: it is a property of this finite,
center-symmetric open box and its stencil at the sampled sizes, and it is
reported below with its measured deviation rather than asserted.

### Imported compiler contract

The following are supplied inputs, not outputs of this cycle:

- the open spatial box, the `L_T = 2` periodic tick fold, and the static-sector
  Regge Hessian assembly;
- the spatial direction-class inventory `c696.SPATIAL_CLASSES` and the direction
  words `c696.regge.DIRS15`;
- the 24-frame table `c696.c576.FRAMES` and the affine site action
  `c696.frame_site_map`;
- the selected samples `L = 3, 4`, the drawn-source count and the fixed seed
  offset, and every numerical gate tolerance in the runner.

There is no measured, fitted, or literature constant imported by this cycle. The
exact group-theoretic rows — the sextet, the four cosets, the homomorphism, the
transitivity classification, and the symmetry-linkage classification — are
integer statements independent of the floating-point assembly. The numerical
rows are claims about this fixed compiler only.

## Claims

### Theorem A — the exact frame stabilizer of the assembly is the body-diagonal sextet

Among the 24 proper rotations, the set of frames whose slot relabeling preserves
the assembly `Q` to `1e-9` is exactly the sextet `[1, 4, 9, 15, 18, 23]`. The
maximum deviation inside the sextet is `1.243450e-10`; the minimum deviation
outside it is `4.000000e+00`. The separation is nine orders of magnitude wide,
at both box sizes, so the identification is not a tolerance artifact.

### Theorem B — the value functional is body-diagonal-measurable for every source

Because the sextet stabilizes `Q` exactly, conjugating by a sextet element
before a frame leaves the frame-transported assembly unchanged, so the map
`g -> Q_g` factors through the four right cosets, and the value functional of
any source depends on the frame only through its body-diagonal label. Measured:
`98 of 98` and `279 of 279` slot sources are label-measurable, and eight drawn
dense sources per box size have within-label spread `7.581911e-12` and
`2.214548e-10` while the smallest gap between distinct labels is `9.063688e-04`
and `5.635424e-03` — seven to eight orders of magnitude of margin. Label
measurability is generic; blindness is not.

This is the structural reason the frame invariant of this observable is a body
diagonal: the assembly's own symmetry is a body-diagonal stabilizer.

### Theorem C — the box-center point reflection is an exact symmetry outside the 24

The center reflection is a permutation of the slot set, an involution, preserves
the assembly to `1.243450e-10` and the diagonal `d` to `2.391624e-11` and
`7.638423e-10`, commutes with all 24 frame relabelings at mismatch `0`, and is
equal to no frame. Consequently the symmetry of the assembly inside the 48
relabelings generated by the frames together with the reflection has order
`12 = 6 proper + 6 improper` at both box sizes. The count is the content: no
improper relabeling outside the reflected sextet is a symmetry either.

Because the reflection sends each body diagonal to itself as an unsigned line,
it carries no body-diagonal label. Half of the assembly's symmetry is therefore
structurally invisible to the frame label — present in the operator, absent from
the record's frame coordinate.

### Theorem D — the level sets of the diagonal value function are exactly the order-12 orbits

Under the group generated by the sextet relabelings and the center reflection,
the slot set falls into `13` orbits at `L = 3` and `34` at `L = 4`, with sizes
`{2: 1, 6: 8, 12: 4}` and `{1: 1, 2: 1, 6: 18, 12: 14}`. The diagonal value
function `d` is constant on those orbits to `2.391640e-11` and `7.638064e-10`,
and it **separates** them: the smallest gap between distinct orbit values is
`4.286579e-05` and `1.264701e-04`. Level set and orbit coincide exactly in both
directions. The orbit-size histograms reproduce the value-multiplicity structure
of `d` independently, which is a self-consistency check on the identification
rather than a second assumption.

### Theorem E — full blindness is transitivity of the frame stabilizer on the diagonals

A slot source is fully frame-blind — all four label values equal — if and only
if its frame stabilizer acts transitively on the four body diagonals. Measured:
`6` blind, `6` transitive, `6` agreeing at `L = 3`, and `19 / 19 / 19` at
`L = 4`. Both implications are measured, not one; the counts agree slot by slot,
not merely in total.

### Theorem F — every merged value pair is symmetry-linked, with no residue

Each slot source contributes six ordered label pairs; the merged ones are those
whose two values agree to `1e-8`. Every merged pair is classified by which
symmetry carries one label image onto the other: the source's own frame
stabilizer, the sextet, or the center reflection composed with a frame. The
tallies are `180 = 24 + 50 + 106` at `L = 3` and `450 = 70 + 110 + 270` at
`L = 4`, with residue `0` in both. Nothing is left over.

The dominant channel is the reflection: `106 of 180` and `270 of 450`. The
merges that looked like arithmetic accidents against the group alone are the
shadow of the improper half of the symmetry, the half the frame label cannot
name.

### Rejectors

Four wrong-value rejectors are gated so that a mis-implemented object would
fail rather than pass by construction.

- The anti-homomorphism reading of the relabeling composition is rejected at
  mismatch `64` and `177` against the homomorphism's `0`.
- Frames outside the sextet fail the stabilizer test at `4.000000e+00`, not
  marginally.
- Perturbing a single diagonal entry of the assembly breaks the sextet symmetry
  and destroys label measurability: the within-label spread of drawn sources
  rises to `4.482319e-04` and `1.636304e-03`, which is above the across-label
  gap scale, so Theorem B is not an identity that would hold for any operator.
- Replacing the single center reflection by the eight independent per-axis face
  swaps over-merges: the orbit count drops to `6` and `16`, and `d` is no longer
  constant on orbits, deviating by `2.356587e-01` and `1.858569e+00`. The
  improper half is the simultaneous flip, not the independent flips.

## Derivation sketch

Write `m_g` for the slot relabeling of frame `g` and `Q_g` for the assembly
transported by it. The relabeling is a homomorphism, so `m_{sg} = m_s . m_g`
and `Q_{sg}` is the `m_g`-transport of `Q_s`. If `s` stabilizes `Q` then
`Q_s = Q` and `Q_{sg} = Q_g`: the transported assembly, and hence the value
functional of every source, is constant on each right coset `S g`. Theorem A
identifies `S` as exactly the sextet, and the sextet's right cosets are exactly
the fibres of the body-diagonal label, which gives Theorem B without any
appeal to the particular source.

For a slot source `e_i` the value at label `j` is `d` evaluated at the relabeled
slot `m_{g_j}(i)` for any coset representative `g_j`. Two labels merge precisely
when `d` takes the same value at two of the four images. Since `d` is a class
function of the order-12 symmetry (Theorem D), that happens precisely when the
two images lie in a common orbit — which is Theorem F's classification, and its
transitive special case, all four images in one orbit reachable from the
stabilizer, is Theorem E.

The order-12 count in Theorem C is partly forced: since the reflection commutes
with every frame and preserves the assembly, the reflected sextet is
automatically a set of symmetries, so `improper >= 6` follows from Theorem A.
The measured content is the upper bound — that `improper` is `6` and not `24`,
so no additional improper relabeling sneaks in. The runner measures both halves
rather than inferring either.

## Honest boundary

The reflection symmetry is a measured property of this finite, center-symmetric
open box with this stencil at `L = 3, 4`. It is not derived from the axioms, it
is not claimed for other regions or other boundary conditions, and it is not
proposed as a framework symmetry; a region without a center-symmetric shape
would not be expected to carry it. The det = -1 map is used only as a
classifying computational identity, never counted among the frames.

The numbers are conditional on the fixed Cycle-696 compiler contract inventoried
above, including its boundary treatment and its Hessian assembly, and on the two
sampled box sizes. The static assembly is indefinite; nothing here uses or
assumes positivity, and all spectral language is avoided in favour of the exact
relabeling statements and the diagonal of the inverse.

The observable studied is the static value functional of a source, not a
dynamical quantity, and the blindness counted is blindness of that functional to
the frame label — not a statement about what any other observable can resolve.
Slot sources and drawn dense sources are the two sampled families; the dense
draws are a finite sample and are reported as such.

## What this cycle claims and does not claim

Claimed: the exact frame stabilizer of the static assembly; label measurability
of the value functional for every source; the existence, involutivity,
centrality, and exactness of the box-center point reflection as a symmetry of
this assembly outside the 24 frames; the order-12 count; the identification of
level sets with order-12 orbits in both directions; the equivalence of full
blindness with stabilizer transitivity; and the complete residue-free
classification of merged pairs.

Not claimed: any enlargement of the framework's symmetry group; any statement
about improper maps as physical frames; any extrapolation of the reflection
symmetry beyond this finite center-symmetric open box; any spectral claim about
the assembly; any dynamical statement; any coupling, scale, or sign selection.

## Physics reading

The frame coordinate a record can carry for this observable is exactly a
body-diagonal label with four values, and that is not a restriction imposed on
the source — it holds for every source, because the assembly's own symmetry is
precisely the stabilizer of a body diagonal. Within that four-valued coordinate,
a source fails to resolve two labels exactly when a symmetry of the assembly
carries one of its label images onto the other. All of the failure is symmetry;
none of it is coincidence.

What makes the accounting interesting is which symmetry does most of the work.
The proper half of the assembly's symmetry is the sextet, which is exactly what
the label already encodes. The improper half — the box-center point reflection
composed with the sextet — is equally exact, equally structural, and fixes every
body diagonal as an unsigned line, so it is entirely absent from the label. It
is the channel responsible for the majority of the merges at both box sizes. The
record's frame coordinate is thus not merely coarse; it is coarse in a way
governed by structure it cannot name, and the merges that a group-theoretic
census of the 24 frames alone would call residual are exactly the image of that
unnameable half.

## The next paths opened

- Test whether the center reflection remains an exact symmetry of the assembly
  under a boundary treatment that breaks center symmetry, which would separate
  the region-shape origin of the improper half from a stencil origin.
- Ask which observables built from the same assembly do carry a coordinate that
  distinguishes the improper half, since a quantity odd under the reflection
  would separate what the value functional merges.
- Extend the classification to composite sources beyond single slots, where the
  orbit decomposition of a source's support should predict its blindness pattern
  directly from Theorem D.

## Runner

The [Cycle719 runner](../scripts/physical_level_set_orbit_law_improper_center_identity_cycle719_2026_08_02.py)
executes every gated row above and reports

```
TOTAL: PASS=22 FAIL=0
```

with exit code `0`. Two consecutive runs produce byte-identical standard output
and a byte-identical receipt. The receipt is written to
`outputs/physical_level_set_orbit_law_improper_center_identity_cycle719_2026_08_02_receipt_2026-08-02.json`
and carries no timestamp, no wall clock, no host name, and no absolute path, so
it is comparable across machines. Cold standard output and the machine-readable
receipt are landed under `outputs/`.

Every floating-point number quoted in this note is the runner's own measurement
in the run that produced that `TOTAL` line; none is copied from an earlier probe.

## Citations

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [Cycle 700](PHYSICAL_OPERATIONAL_SOURCE_RESPONSE_READOUT_CHAIN_CYCLE700_NOTE_2026-07-25.md)
- [Cycle 707](PHYSICAL_SOURCE_STABILIZER_COSET_COLLAPSE_K_SIGN_LAW_CYCLE707_NOTE_2026-08-01.md)

Cycle 700 and Cycle 707 are landed. The linked Cycle696 compiler and Cycle719
runner are support/code dependencies. Context only, with no authority edge: the
in-flight Cycle-716 powerset blindness census, the Cycle-717 body-diagonal
invariant law, and the Cycle-718 frame-transport statement, none of which are
landed and none of which this cycle's gates depend on.
