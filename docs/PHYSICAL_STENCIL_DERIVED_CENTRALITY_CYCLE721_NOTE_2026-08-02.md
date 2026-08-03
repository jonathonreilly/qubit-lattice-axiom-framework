# Centrality of the box-centre point reflection, derived from the assembly stencil — Cycle 721

Date: 2026-08-02

Claim type: bounded_theorem

Authority: none. Audit: unset. Constitutional effect: none. This cycle edits no
axiom, foundation, Qualification, primitive, registry, policy, queue,
audit-status, or PR-control surface. No new axiom or primitive is proposed or
adopted.

No coupling value, sign, or scale is selected or derived in this cycle; every
such object is named as supplied. The floating-point rows are conditional on the
fixed, joined Cycle-696 compiler contract inventoried below; that compiler is a
landed but audit-excluded support surface, not an independent audit authority.

Cycles 717 through 720 established, by direct evaluation of the assembled static
form, that a twelve-element set of signed axis permutations leaves that form
fixed, that the six proper members of the set are a sextet inside the
twenty-four proper rotations, and that the box-centre point reflection commutes
with all twenty-four. In those cycles the group was **measured, not derived**:
its members were found by relabelling the assembled form and reading off which
relabellings changed nothing. This cycle removes the evaluation. The same
twelve-element group, the same sextet, the same four-valued frame label, and the
centrality of the box-centre point reflection are obtained here from the
assembly stencil and the box geometry alone, and the assembled form is then used
only to confirm a prediction that was already fixed before it was consulted.

The derivation is a four-link chain. The site map carried by the landed compiler
is the centre conjugate `s -> R(s - c) + c`; its translation part is exactly
`(I - R)c`, an integer box-corner offset taking only the values `0` and `L - 1`
per axis, so the map is a signed axis permutation followed by a corner shift.
That structure makes the induced relabelling of edge slots a group homomorphism
on all forty-eight signed axis permutations. The box-centre point reflection is
the scalar `-I`, hence central in the matrix group; a homomorphism carries
centrality forward, so its slot relabelling commutes with every frame — with no
assembled form evaluated anywhere in the argument, and with the Cycle-719 closed
form for that relabelling recovered rather than remeasured. Finally the stencil
itself fixes the group: every one of the twenty-four path simplices of the base
cell carries the body diagonal of the four-cube, so a signed axis permutation
permutes the stencil exactly when it preserves the body-diagonal line, giving
order twelve, six proper and six improper, and `24 / 6 = 4` cosets — the
four-valued frame label as a theorem about the stencil rather than a count read
off a table of numbers.

## Improper-frame framing

Six of the twelve derived members have determinant `-1`. These are
**computational identities** of the assembled quadratic form, not lattice
symmetries: improper signed permutations are NOT axiom symmetries — the Lattice
axiom names proper cubic rotations only. They enter this note only as exact
relabellings under which the assembled form is unchanged, and every physical
statement below is carried by the proper sextet alone. The derivation makes
their origin explicit for the first time: without the periodic tick fold the
stencil stabilizer has order `6` and is entirely proper; the improper half
appears only once the tick of length `2` is identified periodically, on which
the tick complement acts as the identity, so the spatial point reflection is
realized as the full four-dimensional complement — the reversal of the path
simplices' chain order.

## Setup

The object is the static open-box assembly `Q` of the landed
[Cycle-696 open-coframe endpoint compiler](../scripts/physical_open_coframe_k_endpoint_compiler_cycle696_2026_07_25.py),
with wrap disabled, at box sizes `L = 3, 4, 5`, carrying `98`, `279` and `604`
edge-slot variables. A slot is a pair (spatial class, low corner). The forty-
eight signed axis permutations are enumerated as the three-by-three integer
matrices with one nonzero entry of modulus one per row and per column. The
twenty-four proper rotations of the landed frame table sit inside them; the
box-centre point reflection is the scalar `-I` and is not among them.

For a signed axis permutation `R` and box size `L`, the corner offset is defined
componentwise as `L - 1` on the axes where `R` carries a negative entry and `0`
elsewhere. The induced slot relabelling sends the slot with class direction `w`
and low corner `x` to the slot whose class direction is the non-negative
representative of `Rw` and whose low corner is `Rx + offset + min(Rw, 0)`
componentwise.

### Imported compiler contract

The following are supplied inputs, not outputs of this cycle:

- the open spatial box, `L_T = 2` periodic tick fold, the twenty-four path
  simplices of the base cell, and the static-sector Regge Hessian construction;
- the spatial class table, the class length assignment, the ten edge pairs of a
  five-vertex simplex, and the barycentric hinge-row convention;
- central finite-difference step `1.0e-4` and every numerical gate tolerance in
  the runner, including the relative comparison tolerance `1.0e-8`;
- the selected samples `L = 3, 4, 5` and the landed twenty-four-frame table.

There is no measured, fitted, or literature constant imported by this cycle. The
combinatorial statements — the offset identity, the homomorphism, the centrality
corollary, the stencil stabilizer and its determinant split, and the coset count
— are exact integer facts, independent of the floating-point construction. The
transport and invariance figures are machine-precision measurements of this
fixed compiler only.

## Claims

### The landed site map is a signed permutation plus a corner shift

Over all forty-eight signed axis permutations and all three box sizes, the
corner offset defined above agrees with `(I - R)c` at deviation `0.000000e+00`,
where `c` is the geometric box centre, and the resulting site map reproduces the
landed compiler's own frame site map with `0` mismatches. The integrality of
`(I - R)c` is not automatic for an integer linear map: four unimodular
non-permutation rejectors produce a non-integer corner offset at even box size,
so the offset identity is a property of the signed axis permutations and not of
integer maps in general. Dropping the offset is fatal — `7938` site images leave
the box across the sampled sizes.

### The slot relabelling is a homomorphism

At `L = 3` and `L = 5` all forty-eight slot relabellings are bijections of the
`98` and `604` slots, all forty-eight are distinct, and composition is exact:
the relabelling of a product frame equals the composite of the relabellings, at
`0` mismatches over all `2304` ordered pairs. The composition order is fixed and
discriminating, not conventional: the reversed order mismatches `175104` slot
entries at `L = 3` and `1094400` at `L = 5`.

### Centrality as a corollary, with no assembled form

The box-centre point reflection is the scalar `-I`, whose matrix commutator
against all forty-eight signed axis permutations is `0`. Since the slot
relabelling is a homomorphism, centrality transports: the worst slot commutator
of the box-centre point reflection against all forty-eight relabellings is `0`
at both sampled sizes. Nothing in this argument evaluates the assembled form.
The rejector is sharp — a single-axis sign flip, which is a signed axis
permutation but not a scalar, fails to commute with `32` of the forty-eight both
at matrix level and at slot level. The closed form recorded in Cycle 719 for the
box-centre relabelling, sending the slot with class direction `w` and low corner
`x` to the slot with the same class and low corner `(L - 1) - x - w`
componentwise, is recovered here at `0` mismatches, so it is a consequence of
the offset identity rather than an independent observation.

### The stencil fixes the group before any assembly

All `24` path simplices of the base cell carry the body diagonal of the
four-cube. On the folded lattice — free spatial translation together with the
free tick shift permitted by the periodic tick of length `2` — the set of signed
axis permutations that permutes the stencil has order `12`, and it coincides,
on all forty-eight, with the set that maps the body-diagonal direction to plus
or minus itself. Its determinant split is `6` proper and `6` improper; its
proper members are exactly the frames at indices `1, 4, 9, 15, 18, 23` of the
landed table, the sextet reported in Cycle 719. The stencil breaks into `2`
orbits of size `12` under it, and the twenty-four proper rotations fall into
`24 / 6 = 4` cosets.

Holding the tick fixed instead of folding it reduces the stabilizer to order
`6`, a proper subset of the order-`12` group, and that residual six is exactly
the proper half. The improper half is therefore supplied by the periodic tick
identification and by nothing else.

A structural fact of the stencil sits underneath: the twenty-four local pieces
of the assembly, one per path simplex, are pairwise identical at spread
`0.000000e+00`, although the twenty-four class tuples labelling them are all
distinct. An edge between the `i`-th and `j`-th vertex of a path simplex spans
`j - i` distinct unit axes whatever those axes are, so its length depends only
on the step count; the local piece cannot see which axes were used. All of the
stencil's dependence on direction therefore lives in the class and anchor data,
which is precisely the data the relabelling above transports.

### The prediction, and the discriminating counterfactual

The derived order-`12` group predicts which relabellings fix the assembled form.
At `L = 3, 4, 5` the prediction is correct on all forty-eight, with worst
deviation `1.243450e-10` inside the derived group against a floor of
`4.000000e+00` outside it and a largest entry of `2.945214e+01`. Grouping the
twenty-four proper frames by the assembled form they produce gives `4` classes
of `6`, and these coincide with the `4` derived cosets at every sampled size:
the four-valued frame label of Cycles 717 through 720 is the coset count.

Agreement with a prediction is not yet evidence that the derivation found the
source. The discriminating gate mutilates the stencil and asks whether the
derived group tracks it. Restricted to a single path simplex the derived group
drops to order `1` and the measured symmetry drops to `1` as well, at floors
`1.221442e+00` and `2.500719e+00` for the two sampled templates; restricted to
one full orbit of `12` templates both are `12` at floor `5.001437e+00`;
restricted to the first `12` templates, which is not an orbit, both are `2` at
floor `1.116895e+01`; restricted to a pair both are `1` at floor
`3.141593e+00`; on the full stencil both are `12` at floor `1.007048e+01`. In
all `6` cases the derived and measured groups are equal, not merely nested. The
derivation moves with the stencil.

## Derivation sketch

Write the compiler's site map as `f_R(s) = R(s - c) + c` with `c` the geometric
box centre. Expanding, `f_R(s) = Rs + (I - R)c`. Because every coordinate of `c`
equals `(L - 1) / 2` and every row of a signed axis permutation has exactly one
nonzero entry, of modulus one, the `a`-th coordinate of `(I - R)c` equals
`((L - 1) / 2)(1 - s_a)` with `s_a` the sign in row `a`. That is `0` when the
sign is positive and `L - 1` when it is negative — always an integer, and always
a box corner. Hence `f_R` is a permutation of the box sites, and `f_{RS} = f_R`
composed with `f_S`, since the centre conjugate is a group action by
construction. Passing to edge slots preserves this: an edge is determined by its
low corner and its class direction, the image direction is `Rw` up to the sign
convention that stores the non-negative representative, and the compensating
shift `min(Rw, 0)` is exactly the correction from "image of the low corner" to
"low corner of the image". So the slot relabelling is a group homomorphism.

The box-centre point reflection is `-I`, which commutes with every matrix. A
homomorphism sends a central element to an element commuting with the whole
image, so its slot relabelling commutes with every frame's relabelling. That is
the centrality of Cycles 719 and 720, reached without any reference to the
assembled form.

For the stencil: the assembly sums, over base cells and over the twenty-four
path simplices, a local piece contracted through the class-and-anchor data. Two
facts make this transport combinatorial. First, the local pieces are identical,
so relabelling cannot change them. Second, a path simplex of the four-cube is a
maximal chain in the cube's face lattice, so it contains both the all-zero and
the all-one vertex; the segment joining them is the body diagonal, shared by all
twenty-four. A signed axis permutation acting on the spatial part maps the
stencil into itself precisely when it maps that shared diagonal to itself as a
line, that is when `R` applied to the all-ones spatial vector has all three
components equal. Those `R` with the plus sign are the `6` rotations fixing the
diagonal pointwise; those with the minus sign reverse it, and reversal exchanges
the two ends of every chain — realizable only because the tick is folded, since
on a tick of length `2` the complement is the identity and the chain reversal
can be absorbed. The `12` derived elements are therefore the stabilizer of a
line, and the four cosets follow by index.

## Honest boundary

The chain establishes that the twelve-element group, the sextet, the four-valued
label, and centrality all follow from the stencil and the box geometry. It does
not establish that these are forced by the axioms: the stencil, the periodic
tick of length `2`, the barycentric hinge convention, and the slot storage
convention are all supplied by the landed compiler, and a different admissible
stencil would give a different group — which is exactly what the counterfactual
gate demonstrates. The derivation converts a measurement into a property of the
supplied stencil; it does not convert it into a property of the axioms.

The improper half remains registered as computational identities. Its derivation
here makes its status sharper, not stronger: it exists because a tick of length
`2` cannot distinguish a complement from the identity, which is a property of the
supplied tick fold and not a lattice symmetry.

The invariance and transport figures are floating-point measurements of one fixed
compiler at three box sizes. The floors are large — `4.000000e+00` against
`1.243450e-10` — but they are floors of this compiler, not of the framework. The
combinatorial rows carry no such caveat: the offset identity, the homomorphism,
the centrality corollary, the stabilizer order and split, and the coset count are
exact integer statements.

## The next paths opened

Two directions follow. First, the body-diagonal line is now the object that
carries the whole symmetry, and its stabilizer is what the frame label counts;
asking which admissible stencils share that line, and whether the framework's own
locality data selects such a stencil, moves the question from the compiler to the
axioms. Second, the tick fold is now identified as the sole source of the
improper half, so varying the tick length is a sharp probe: at tick length
greater than `2` the complement is no longer the identity and the derived group
should lose its improper half without touching the proper sextet. Both are
cheap to attempt on the landed compiler.

## Runner

The [Cycle721 runner](../scripts/physical_stencil_derived_centrality_cycle721_2026_08_02.py)
executes every gated row above and reports

```
TOTAL: PASS=46 FAIL=0
```

with exit code `0`. Two consecutive runs produce byte-identical standard output
and a byte-identical receipt. The receipt is written to
`outputs/physical_stencil_derived_centrality_cycle721_2026_08_02_receipt_2026-08-02.json`
and carries no timestamp, no wall clock, no host name, and no absolute path, so
it is comparable across machines.

Apart from the supplied finite-difference step and gate tolerances inventoried
under the imported compiler contract, every floating-point number quoted in this
note is the runner's own measurement in the run that produced that `TOTAL` line;
none is copied from an earlier probe.

## Citations

- [Minimal axioms](MINIMAL_AXIOMS_2026-06-29.md)
- [Cycle 700](PHYSICAL_OPERATIONAL_SOURCE_RESPONSE_READOUT_CHAIN_CYCLE700_NOTE_2026-07-25.md)
- [Cycle 707 coset collapse](PHYSICAL_SOURCE_STABILIZER_COSET_COLLAPSE_K_SIGN_LAW_CYCLE707_NOTE_2026-08-01.md)
- [joined-compiler tournament note](work_history/repo/review_feedback/PHYSICAL_OPEN_COFRAME_K_ENDPOINT_JOINED_COMPILER_TOURNAMENT_NOTE_2026-07-23.md)

Cycle 700, Cycle 707, and the joined-compiler tournament note are landed. The
linked Cycle696 compiler and Cycle721 runner are support/code dependencies.
Backticked context only, with no authority edge — these cycles are in flight and
carry no authority here:
`PHYSICAL_BODY_DIAGONAL_FRAME_FUNCTIONAL_TRANSVERSAL_LAW_CYCLE717_NOTE_2026-08-02.md`,
`PHYSICAL_LEVEL_SET_ORBIT_LAW_IMPROPER_CENTER_IDENTITY_CYCLE719_NOTE_2026-08-02.md`,
`PHYSICAL_AMBIENT_DOMAIN_SYMMETRY_SPLIT_CYCLE720_NOTE_2026-08-02.md`.
