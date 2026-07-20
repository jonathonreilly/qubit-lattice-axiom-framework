# Physical static-quadrupole Stinespring/NN compiler — Cycle 460

Date: 2026-07-19

Authority: none

Audit: unset

## Frozen question and result boundary

Cycle 460 asks whether Cycle 458's diagnosed separation-kernel mismatch can
be removed constructively by compiling the exact finite Cycle-420 static
quadrupole receiver map, while leaving the source normalization and receiver
coordinate scale unchanged.  The target is a **finite positive
receiver-weight/Stinespring channel**, not a claim that the imported legacy
`|amplitude|^2` interpretation is physical probability.

The compiled object must use the exact single-source state

```text
s(p)=(sqrt(1-p),sqrt(p)),
p_route = route_strength / 5e-5,
```

for the free, unit, and coefficient-two source coordinates.  There is no
route label, state query, per-row factor, or held refit in the update.  One
fixed `V_a` handles `p=0`, unit, and coefficient-two without lookup.  The two
supplied geometries, train a=1 and held a=2, occupy two invariant blocks of
one shared block schedule on a 4356-M2 nearest-neighbor line.

Success certifies only a bounded compiler of a supplied kernel.  The legacy
Green profile, finite lattice, source geometry, normalized receiver weights,
and both separation blocks remain imports.  The construction is neither a
derived law nor gravity, and it is not a held prediction of the imported
kernel itself.

## Exact supplied operator inventory

The Cycle-420 comparator supplies:

- a `25 x 33 x 33` ordered lattice with 27,225 host nodes;
- 169 weighted offsets between each pair of adjacent x-layers;
- the edge factor `exp(i K L (1+p f_edge)) w h_m/L^2`;
- the signed source profile `(+1,-2,+1)` at separation `a=1` or `a=2`;
- source normalization `5e-5` and the two exact route strengths;
- an input point packet, 1,089 final-layer detector labels, transverse
  coordinates, host normalization, and the width functional;
- all three compile anchors `p=0`, `0.015003358529489008`, and
  `0.07565725585107586` at both separations.

The runner calls that host operator six times during compilation.  It then
freezes the physical gate schedule.  There is no host array solve during
update, but the compiled coefficients continue to contain the supplied host
kernel and geometry.  Complex legacy packet phases are inventoried but not
promoted: this cycle compiles the positive receiver-weight channel only, not
the full amplitude phase channel.

## Positive effect reconstruction

For each detector label `j`, write the three supplied normalized receiver
weights as `w_j(0),w_j(p_1),w_j(p_2)`.  The unchanged two-amplitude source
state induces the most general real two-dimensional effect response

```text
w_j(p) = (1-p) A_j + p D_j + 2 sqrt(p(1-p)) B_j,
R_j    = [[A_j,B_j],[B_j,D_j]].
```

`A_j=w_j(0)`, while the two remaining rows solve one declared 2x2 linear
system for `D_j,B_j`.  The construction proceeds only if every `R_j` is
positive semidefinite and `sum_j R_j=I_2` within frozen tolerance.  Each
effect is factored as `R_j=L_j^dagger L_j`; stacking its two rows defines

```text
V_a = stack_j L_j,
V_a^dagger V_a = I_2.
```

The two factor rows are explicit Stinespring tags carrying the same receiver
coordinate.  They are not outcomes, occurrences, or Records.  This
factorization converts the supplied finite positive channel into a linear
isometry without postselection or normalization feedback.

## Physical nearest-neighbor compiler

Each `V_a` has shape `2178 x 2`.  Adjacent-row rectangular QR eliminates its
tail.  The resulting 2x2 seed and the reversed eliminations are adjacent,
number-preserving Givens rotations.  Every Givens is lifted to two physical
M2 as identity on `|00>` and `|11>` and its declared two-mode unitary on the
one-excitation sector.  The a1 and a2 schedules act on disjoint consecutive
2,178-site blocks of one connected 4,356-site line.

The runner checks input/output Gram matrices, the source-to-receiver E/G
intertwiner, the exact adjoint inverse, target-code leakage, primitive
unitarity, and every nearest-neighbor support.  It applies the same `V_a` to
all three source states; it never selects an output column by route.

This is one fixed finite schedule, not a homogeneous scalable cubic law.  Its
block placement, Givens angles, source preparation, and initial geometry
sector are supplied structure.

## Receiver calibration and named rows

The receiver position and second-moment effects repeat the exact Cycle-420
transverse coordinate over both Stinespring tags.  One receiver calibration
is derived from the a1 free operator representation, frozen, and transported
unchanged to held a2.  There are no per-row factors.  The named tolerance
remains `5e-10`.

The first immutable cold run returned `11 PASS / 0 FAIL`, exit status 0, and

```text
RESULT PHYSICAL_STATIC_QUADRUPOLE_STINESPRING_NN_COMPILER_CERTIFIED
```

The positive-channel and fixed-isometry controls are:

| separation block | minimum `R_j` eigenvalue | `||sum_j R_j-I||` | `||V_a^dagger V_a-I||` | maximum anchor-weight residual |
|---:|---:|---:|---:|---:|
| a=1 | `6.447010259437623e-08` | `1.2978275924574884e-14` | `1.3754728104038923e-14` | `1.5565801613083906e-17` |
| a=2 | `6.450331407614947e-08` | `2.445294179443596e-14` | `2.3794846201601644e-14` | `1.6710377250678836e-17` |

No positivity clipping was needed.  Each fixed `V_a` closes the free, unit,
and coefficient-two weights.  Rectangular QR produced 4,354 adjacent Givens
per block, 8,708 total.  The combined 4,356-M2 schedule has

```text
E/G residual       = 1.830907053716079e-14
inverse residual   = 3.9613835036012496e-14
target leakage     = 2.7943878049084003e-14
non-NN gates       = 0.
```

The sole operator-coordinate calibration is
`0.9999999999999999`.  With it frozen, the named rows are:

| row | compiled shift | Cycle420 target | exact residual |
|---|---:|---:|---:|
| a1/unit | `6.692829903620633e-07` | `6.692829912502418e-07` | `-8.881785255792436e-16` |
| a1/coefficient-two | `3.3757457469363312e-06` | `3.3757457469363317e-06` | `-4.235164736271502e-22` |
| a2/unit | `1.319789611819999e-06` | `1.3197896109318208e-06` | `8.881782079418884e-16` |
| a2/coefficient-two | `6.65600115112852e-06` | `6.656001151128521e-06` | `-8.470329472543003e-22` |

There are zero per-row factors and zero held receiver refits.  This closes the
bounded finite compiler target.  Because all a2 anchor weights were supplied
to compile `V_2`, it does not turn the a2 rows into independent predictions
of a selected framework law.

## Controls, covariance, and resource cap

The frozen deletions remove, separately, the source coordinate, receiver
scale, entire propagation schedule, one Givens, one Stinespring tag, and the
held geometry block.  The runner also retains the inherited Cycle-219 mass
fixture and Cycle-230 contact.

Every Givens support is mapped through all 24 proper-cubic frames.  The line
axis rotates as a body-frame axis and every edge remains nearest-neighbor;
the width effect is even under body-frame reversal.  This is covariance of a
supplied finite apparatus, not autonomous placement or a homogeneous law.

The entire executable has a 600-second wall cap enforced by a process timer
and a 4 GiB RSS cap.  Compile-time and update-time host-solve counts are
reported separately.  Phase is not physical energy, a generator element is
not a rate, Givens depth is not time, receiver weights are not Born
frequencies, pointer/tag labels are not Records, and the source is not gravity
or calibrated stress-energy.

## Dependency ledger

| factor | supplied | derived here | open |
|---|---|---|---|
| source | Cycle420 strengths and `5e-5`; exact two-amplitude preparation | no change to `p_route` | autonomous preparation, recurrence, energy/stress calibration |
| propagation | complete Cycle420 finite host kernel and both geometries | positive effects, Stinespring isometries, adjacent Givens schedules | derive a homogeneous local interaction rather than compile supplied coefficients |
| receiver | host detector coordinates, normalized legacy weights, width functional | two explicit tags/label and one a1 coordinate calibration | physical detector coupling and operational units |
| local compiler | M2 sites and NN supports | one 4,356-M2 finite one-excitation schedule, E/G/inverse/leakage | constant cell compiler, autonomous placement, scalable cubic law |
| named surface | all six operator anchors including held geometry | exact schedule replay and residuals | prediction beyond compiled anchors and independent observables |
| TOE semantics | none | none | time, energy/stress source, metric, Records, Born/occurrence, realized history |

`C_num` advances if the compiled schedule closes the four imported named
rows; the immutable run closes those finite imported rows to a maximum
residual `8.881785255792436e-16`.  `C_local` gains one bounded one-excitation realization but remains
open at homogeneous scalable law selection and the L13 M64 shell.  `C_ref`
remains open because the kernel, geometry, coordinate spectrum, anchors, and
preparation are supplied.  `C_wrap`, `C_int`, and `C_source` remain open.

## No-Go Discipline Gate

Gate status: **FAIL for any broad static-kernel, propagation, gravity,
source, receiver, or framework no-go**.  Even a failed PSD or Givens check
would address only this two-dimensional source-code Stinespring route.  The
licensed negative classification is
`partial-attempt-with-named-untested-routes`.  There is no gravity, no-go,
minimum-content, shared-obstruction, or axiom-pressure claim.

### N1 — alternative route enumeration

| route | honesty marker | disposition |
|---|---|---|
| two-dimensional positive receiver-effect/Stinespring compiler | `ATTEMPTED` | Cycle460 |
| amplitude-and-phase preserving contraction/block encoding | `UNTESTED` | retains the full complex legacy packet rather than only receiver weights |
| symmetric-copy or larger source-code Stinespring lift | `UNTESTED` | remains available if any `R_j` loses positivity |
| analytic local matched propagation kernel | `UNTESTED` | derives link behavior instead of compiling the finite coefficient set |
| Cycle-213 retarded carrier join | `UNTESTED` | targets a causal dynamic carrier |
| Cycle-216 reversible static approximation | `UNTESTED` | targets a local static solver/dilation |
| homogeneous scalable one-excitation QCA | `UNTESTED` | removes finite block placement and dense compiled angles |
| alternative packet/receiver functional | `UNTESTED` | may match separation dependence with a smaller apparatus |
| independent impact-parameter surface | `UNTESTED` | tests a distinct positive-source prediction lane |

At least eight constructive resolutions remain untested after the present
route.  They are not treated as failed or absorbed into this compiler.

### N2 — wall-independence audit

The live conditions are `K`, derivation of the kernel; `H`, a homogeneous
scalable NN law; `A`, preservation of the full amplitude/phase channel; `S`,
autonomous source preparation; and `R`, physical receiver coupling/units.

| pair | closing first closes second? | reverse? | independent? |
|---|---:|---:|---:|
| K,H | no | no | yes |
| K,A | no | no | yes |
| K,S | no | no | yes |
| K,R | no | no | yes |
| H,A | no | no | yes |
| H,S | no | no | yes |
| H,R | no | no | yes |
| A,S | no | no | yes |
| A,R | no | no | yes |
| S,R | no | no | yes |

The four named rows are targets, not four additional walls.  Passing a finite
schedule does not close any of the five independent conditions above.

### N3 — hidden-condition scan

The load-bearing imports are explicit: lattice dimensions, offsets, K,
signed source profile, both separations, all three source anchors, detector
coordinates, legacy normalization, and width effect.  Further supplied
structure is the direct-sum geometry block, two tags per detector label, line
placement, every Givens coefficient, and geometry-sector preparation.  There
is no “by construction,” “standard QFT,” “natural,” “background,” or
“framework provides” premise hiding those imports.  The host solve occurs at
compile time and its zero update-time count is tested rather than implied.

### N4 — residual matching

| witness | predecessor residual | Cycle460 target | exact match? |
|---|---|---|---:|
| Cycle453 | direct local finite kernel ratios `0.724` at a1 and `0.331` at a2 | maximum compiled named residual `8.881785255792436e-16` | yes |
| Cycle458 | physical `a2/a1=0.9027544307825409` versus legacy `1.9720031257423813` | both supplied separation blocks now occur in one schedule | yes |
| Cycle420 | four exact width rows from signed host profile | identical lattice/operator/anchors/tolerance; all four pass | yes |
| Cycle435 | local quadrupole packet and M64 receiver | not the Cycle460 one-excitation apparatus | no; retained control only |
| impact-parameter lane | positive source and log-fit holdout | not executed | no; live independent route |

Only the first three exact matches license statements about the bounded
finite receiver-weight compiler.

### N5 — rhetoric audit

“Compiled” means the six supplied operator anchor packets are encoded into a
fixed 4,356-M2 schedule.  “Shared” means one fixed direct-sum schedule and one
source-state rule, not a repeated homogeneous microscopic law.  “Held a2 no
refit” means no receiver/source refit after the a1 calibration; the a2 kernel
and both a2 anchor packets are still compilation inputs.  Therefore any
numeric pass is compiler validation, not an independent held prediction, a
gravity calculation, or evidence that the kernel is derived.

### N6 — partial-closure path scan

No axiom edit is needed.  A positive result can be reduced constructively by
seeking a low-rank/shared-angle factorization of the two `V_a`, compiling the
full amplitude channel by unitary dilation, or replacing dense finite angles
with a repeated local Cycle-213/216 carrier.  A PSD failure would motivate a
larger or symmetric-copy source code before any negative conclusion.

### N7 — hostile steelman

A hostile reviewer can correctly say that any finite table of positive
receiver weights may admit a large Stinespring apparatus and that embedding
both held anchors removes independent predictive force.  They can also note
that discarding output phases and choosing 4,356 tailored M2 does not explain
why the Cycle420 Green kernel or detector coordinates occur.  Cycle460 can
answer only the narrower compiler question: whether the already supplied
finite map is compatible with bounded unitary NN execution and the unchanged
source coordinate.

### N8 — cross-cycle echo

Cycle435 supplied a local packet mechanism, Cycle453 carried exact source
strengths, and Cycle458 separated correct strength scaling from incorrect
separation scaling.  Cycle460 deliberately moves the legacy separation
dependence into a compiled finite channel.  This can close a representation
wall while reopening reference selection and law derivation, just as earlier
finite-menu compilers separated executability from selection.  It creates no
shared obstruction or axiom pressure.

## Reproduction

```bash
python3 -m py_compile \
  scripts/physical_static_quadrupole_stinespring_nn_compiler_cycle460_2026_07_19.py
python3 \
  scripts/physical_static_quadrupole_stinespring_nn_compiler_cycle460_2026_07_19.py
```

The expected result token is
`PHYSICAL_STATIC_QUADRUPOLE_STINESPRING_NN_COMPILER_CERTIFIED` with exit status
0.  The run completed in `83.32 s` external wall time (`2.5277674170210958 s`
inside the Cycle460 body after inherited imports); the 600-second timer did
not fire.  Maximum resident set size was `727711744` bytes, peak memory
footprint was `769131552` bytes, and compiled array payload was `278784`
bytes, all below the 4 GiB cap.  Compile-time host solves numbered six and
update-time host solves numbered zero.

Deletion witnesses were: source shift `0`, receiver shift `0`, propagation
shift `-2.737300166619376`, one-Givens E/G residual
`0.015176332595449234`, retained weight with one Stinespring tag deleted
`0.5457363876315204`, and the a2-target residual when its geometry is replaced
by a1 `-6.505066205697575e-07`.

No axiom, foundation, Qualification, primitive, registry, policy, queue, or
audit surface is edited.
