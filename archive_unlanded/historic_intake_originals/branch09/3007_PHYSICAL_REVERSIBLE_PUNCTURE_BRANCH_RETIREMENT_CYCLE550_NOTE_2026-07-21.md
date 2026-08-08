# Physical reversible puncture/branch-retirement attempt — Cycle 550 (2026-07-21)

Authority: none.  Audit: unset.  Constitutional effect: none.

Runner:
`scripts/physical_reversible_puncture_branch_retirement_cycle550_2026_07_21.py`.

## Result

Cycle 550 constructs a literal physical **branch carrier**, then sharply
falsifies the requested exact-blank reversible puncture ansatz at its terminal
boundary.  The positive component is one fixed physical object: 24
proper-frame carrier loops are simultaneously installed in blank sites of the
Cycle-527 microgrid.  Their local branch-compute routes, loop SWAPs, and
reverse schedules are collision-free, use only nearest-neighbour one-/two-M2
primitives, have constant overhead, and rotate into themselves under all 24
proper-cubic frames and all 576 products.  This is not a list of 24
presentations and has no runtime path selector.

The sharp negative is narrower than a puncture no-go.  Suppose a reversible
create–transport–correct–close–uncompute circuit accepts all eight lawful
Cycle-532 Wilson sectors, preserves arbitrary target and gauge data, returns
to the same fixed plus-sector terminal code, and satisfies terminal auxiliary
blankness.  On any fixed target/gauge ray it must map eight orthogonal input
rays to the same output ray.  That map has rank one instead of eight and a
Gram residual of one, so it is not an isometry.  The circuit-level witness is
equally direct: after correction `W_final=+1`, reversing Wilson extraction
XORs zero into the syndrome token, leaving the old syndrome behind.

This statement survives arbitrary intermediate code deformation, including
a genuine reversible puncture, because it uses only the declared input and
terminal spaces.  It does **not** show that physical puncture surgery is
impossible.  Cycle 550 constructs the carrier loops but does not construct a
topology-changing stabilizer-check surgery.  A persistent puncture, enlarged
terminal gauge sink, reset bath, promised plus-sector input, or product
encoder changes the terminal/domain contract and remains live.

The non-CSS/subsystem probe is constructive: six branch bits transfer
reversibly into six sink M2 while the target is untouched.  The sink is
nonblank on 63 of 64 branches, exactly where the information went.  The
local-Clifford/reversible-block probe finds no blank-collapse permutation.

The rough-code input remains supplied.  Full Cycle-537 `Gamma(P)`, mass,
contact, seam, both matter parities, inverse, leakage, deletion, lawful-domain,
and held L6 checks replay.  The result is about reference retirement; it does
not construct rough-code product/reset preparation or a recurrent physical
update.

Broad negative gate: **FAIL / DO NOT SHIP**.  The narrow blank-terminal
isometry lemma is eligible after the N1–N8 audit below; it creates no shared
substrate obstruction and no axiom pressure.

## Exact terminal contract

The tested ansatz has five coherent stages:

```text
CREATE      compute a_d = s_axis AND frame_activation_d into blank carriers
TRANSPORT   move every carrier around its fixed noncontractible NN loop
CORRECT     apply the Cycle-547 local signed membrane correction
CLOSE       return carriers to their start sites and restore blank route work
UNCOMPUTE   reverse branch compute, Wilson extraction, and frame genesis
```

Success would require:

```text
|target,gauge,W=w>|all auxiliary blank>
    -> |same target,gauge,W=+>|all auxiliary blank>
```

for every `w in F2^3`, including arbitrary coherent superpositions, with an
exact inverse for the coherent schedule.  The terminal code, target algebra,
and gauge state are held fixed; putting `w` into a persistent sink is a
separate subsystem route rather than success under this contract.

The temporary 24 carriers do uncompute exactly while the Cycle-547 `s,b`
fields remain available.  The failure occurs when the six reference roots
themselves are retired.  Thus the physical routing positive and terminal
information negative are not conflated.

## One fixed all-24 physical carrier object

Let a proper cubic frame be `F=(d,e,f)` with ordered signed unit-vector
columns.  For every one of the 24 frames define

```text
x_F    = e + 2 f                         (mod L),
r_F(t) = 16 x_F + t d + 2 e + 3 f       (mod 16L),
t      = 0,...,16L.
```

All 24 loops exist simultaneously.  A rotation `R` sends the entire labelled
path `F` to `RF` at the same compiler tick.  The transverse `(2,3)` offset
keeps the same-tick loops and their SWAP edges disjoint.  It also avoids every
active Cycle-532 rough site and Cycle-547 frame, syndrome, and marker site.

For direction `d`, the relevant Cycle-547 frame and syndrome copies at cell
`x_F` sit at `16x_F+5d` and `16x_F+6d`.  An ordered, frame-covariant Manhattan
route moves transversely by `2e+3f` before removing its longitudinal offset.
Distances are therefore:

```text
frame -> syndrome: 1
frame -> carrier: 10
syndrome -> carrier: 11.
```

The ordinary H/T/CNOT Toffoli decomposition, with every remote CNOT compiled
by forward SWAPs, one nearest-neighbour CNOT, and reverse SWAPs, takes 91
one-/two-M2 primitive calls per carrier.  Compute plus inverse is 4,368 calls
across the 24 carriers.  All route work starts and ends blank on the declared
domain.  A deleted inverse Toffoli leaves a carrier nonblank in 16 of the 64
branch cases.

| physical control | L5 | held L6 |
|---|---:|---:|
| carrier loops / active carrier M2 | 24 / 24 | 24 / 24 |
| fine NN steps per loop | 80 | 96 |
| forward loop SWAPs, all carriers | 1,920 | 2,304 |
| forward-plus-inverse loop SWAPs | 3,840 | 4,608 |
| maximum simultaneous tokens in one coarse cell | 4 | 2 |
| carrier/source/active-role collisions | 0 / 0 / 0 | 0 / 0 / 0 |
| loop NN / layer-operand failures | 0 / 0 | 0 / 0 |
| control-path NN / layer-operand failures | 0 / 0 | 0 / 0 |
| all-24 loop/source/control covariance failures | 0 | 0 |
| all-576 frame-action failures | 0 | 0 |

The installed blank microgrid is the route work, so this adds 24 active tokens
globally and never more than four in one tested coarse cell.  The bound is
constant per cell.  The `16L` compiler ticks grow with system size and are not
called physical time or a rate.

The root origin, ordered frame-orbit labels, coefficients `(1,2)` in `x_F`,
transverse offsets `(2,3)`, tick origin, loop orientation, and closure schedule
are supplied design data.  They transform as one orbit; no host chooses one
frame or path at runtime.  A topology-changing puncture location/check-removal
law is not hidden here—it remains unconstructed.

## Branch truth table and exact failure

For a Wilson bit `w` and blank syndrome token `s`, coherent extraction and
correction have the binary action

```text
s <- s XOR w              so s=w,
w <- w XOR s              so w=0.
```

The carrier activation `a=s AND frame_activation` is copied into four
proper-frame lanes for its active signed direction.  Every carrier completes
its loop and the inverse Toffoli returns it to zero.  Reversing extraction
then gives

```text
s_terminal = s XOR w_final = w XOR 0 = w.
```

Across all 64 `(three Wilson bits, three frame bits)` cases, temporary carrier
uncompute failures are zero, but 56 cases retain a nonzero syndrome.  Only one
classical branch has all six reference roots zero.  This is not a numerical
tolerance: it is an exact F2 identity.

The frame bits expose a second, target-algebra version of the same boundary.
For one active axis, coherently preparing the side bit, applying the two
branch-dependent membranes, and attempting the inverse frame transform has
blank probability `1/2` on a target witness; with three active axes it is
`1/8`.  Applying the side-difference logical can decouple the frame bit, but
then both branches share one signed membrane.  That membrane still acts
nontrivially on the bare target algebra: the negative-side character counts
are 150 at L5 and 216 at L6.  The side-difference counts are 300 and 432.
Cycle 544's exact affine solves again return `(False,False,False)` for a Pauli
that flips one Wilson, preserves the local code, and commutes with the whole
matter/gauge target.

Cycle 547 avoided this loss by retaining `s,b` and representing observables as

```text
L(O)=O product_a Z(s_a)^eta_(a,0)(O) CZ(s_a,b_a)^chi_a(O).
```

Erasing those fields while demanding the bare target algebra removes the
very factors that made the correction target-transparent.

## Rank and Gram witness

The Cycle-532 bounded-local rough code and its fixed-Wilson subspace differ by
exactly three stabilizer ranks:

| dimension control | L5 | held L6 |
|---|---:|---:|
| physical rough M2 | 2,750 | 4,752 |
| bounded-local stabilizer rank | 1,873 | 3,238 |
| rough-local code exponent | 877 | 1,514 |
| fixed-Wilson rank | 1,876 | 3,241 |
| fixed-Wilson code exponent | 874 | 1,511 |
| independent Wilson labels | 3 | 3 |
| input/output dimension ratio | 8 | 8 |

Choose one normalized target/gauge vector in each orthogonal Wilson sector.
The desired target-preserving blank-terminal map sends all eight to the same
output ray (up to phase).  An off-diagonal input Gram entry is zero while the
corresponding output magnitude is one.  The exact residual is one, and the
requested branch map has rank one where an isometry needs rank eight.

Therefore at least three bits of distinguishing information must remain in a
sink, environment, persistent defect, enlarged gauge, or other terminal
degree of freedom if all eight inputs are admitted reversibly.  This is a
narrow minimum-content statement for this exact domain/terminal contract,
not a claim that the framework needs a new axiom.

## Alternative probes

### Non-CSS/subsystem gauge sink

For six live branch bits `q` and six blank sink bits `g`, two local-CNOT
layers implement

```text
(q,g=0) -> (q,g=q) -> (q=0,g=q).
```

All 64 branches pass, the target spectator is unchanged, and the reverse two
layers recover `(q,0)` exactly.  The sink is nonblank in 63 branches.  This is
a constructive reversible subsystem route if the terminal gauge is enlarged
by six M2; it is not reference retirement with every auxiliary blank.

No claim is made that this simple sink realizes a complete non-CSS stabilizer
code.  It is the normalized information-accounting core any such proposal
must satisfy.

### Local-Clifford/reversible block

The runner exhausts all 24 permutations of a two-bit block.  None sends both
`(w=0,a=0)` and `(w=1,a=0)` to the same `(0,0)` output.  This is stronger than
checking only the Clifford subset at that block size: reversible local gates
cannot collapse the two inputs unless another output stores their distinction.

A local-Clifford encoder from a **promised plus-sector** product input is not
covered.  It avoids rather than retires arbitrary Wilson branches and remains
live as part of the independent rough-code preparation campaign.

### Dissipative reset

Reset can erase the syndrome and has no exact inverse.  Cycle 544 constructs
sector convergence of that type; Cycle 547 shows how retaining the missing
relation restores target transparency.  A new dissipative law that both
retires the branch and preserves the target by exporting information to a
declared environment remains a distinct route.

## Inherited target replay

The cold certificate re-executes Cycle 537.  The fixed-Wilson local-fill code
has the exact full-Fock `Gamma(P)` target factor and the `(N-1)` gauge factor,
sectorwise across the shared parity.  Both matter parities are nonempty.
Mass, onsite mixing, contact, seam, and inverse checks pass.  Vacuum,
one-particle, complete two-particle, deterministic high-sector, two-cell
full-Fock, and three-cell censuses pass.  Terminal code leakage is zero.
Deleting one fill face changes rank by one; deleting one dressing factor
creates two face syndromes; the FSWAP fourth-term deletion residual remains
one.  These controls ensure the retirement failure is not purchased by
weakening the target physics.

## Supplied-structure inventory

Supplied here:

- the Cycle-527 scale-16 installed microgrid and its H/T/CNOT/SWAP law;
- the lawful Cycle-532 rough-code input, target/gauge interpretation, and
  three Wilson labels;
- the Cycle-547 frame/syndrome fields and local membrane correction;
- a macro origin, frame-orbit labels, lane offsets, tick origin, loop
  orientation, path rule, and closure schedule;
- reset genesis for the Cycle-547 fields and blank temporary carrier M2;
- finite periodic L5 and held-L6 geometries.

Constructed and tested:

- the simultaneous 24-loop physical branch-carrier object;
- literal NN paths for every Toffoli CNOT and every transport SWAP;
- exact reverse schedules and route-work/carrier blankness;
- all-branch create/correct/uncompute truth tables;
- the rank/Gram falsifier and reversible subsystem-sink comparator.

Not constructed:

- topology-changing stabilizer puncture creation and closure;
- exact blank retirement of the six Cycle-547 reference roots;
- rough-code preparation from product/reset matter/gauge M2;
- a non-CSS code, recurrent physical update, causal clock, gravity/source law,
  Born rule, or realized-history law.

## No-go discipline N1–N8

### N1 — Alternative-route enumeration

1. **Reversible puncture with identical terminal code and all branch
   auxiliaries blank:** attempted and sharply falsified by the exact rank/Gram
   and inverse-extraction witnesses, even granting arbitrary intermediate
   deformation.
2. **Persistent puncture or enlarged non-CSS/subsystem sink:** positive at the
   six-bit reversible information-transfer core; a full physical subsystem
   code is not built.
3. **Local-Clifford exact blank retirement on the arbitrary-sector domain:**
   the minimal reversible block is falsified and the rank lemma covers larger
   unitary blocks with identical terminals.
4. **Local-Clifford/product encoder on a promised plus sector:** open and not
   covered by the retirement lemma.
5. **Dissipative stabilizer pump/reset bath:** live; exact inverse is waived
   and exported information must be explicit.
6. **Retained relational frame:** constructive in Cycle 547; the target is
   transparent in the enlarged algebra rather than after field erasure.
7. **Different terminal topology or target/gauge factorization:** live; it
   changes the codomain dimension and must re-run `Gamma(P)` and commutants.

The first route fails.  The others are not silently folded into it.

### N2 — Wall-independence audit

Three residuals are independent:

- `W_info`: an isometry cannot erase eight arbitrary Wilson labels into the
  same terminal ray with every sink blank;
- `W_target`: the available Wilson-flipping membranes act nontrivially on the
  bare matter/gauge target unless the relational fields are retained;
- `W_prepare`: the rough local code itself still lacks a product/reset
  encoder.

The required pairwise audit is:

| pair | first closes second? | second closes first? | independent? |
|---|---:|---:|---:|
| `W_info`, `W_target` | no | no | yes |
| `W_info`, `W_prepare` | no | no | yes |
| `W_target`, `W_prepare` | no | no | yes |

A persistent gauge sink closes `W_info` without closing `W_target` or
`W_prepare`.  A promised-sector product encoder avoids `W_info` while still
having to close `W_prepare`.  A relational target closes `W_target` while
leaving the fields present.  The walls are therefore not one disguised claim.

### N3 — Hidden-wall scan

Puncture location, branch-carrier genesis, orientation, path choice, root,
closure schedule, and tick origin are audited explicitly.  The 24 paths are a
fixed orbit, not a host-selected frame.  The temporary carriers start blank;
the frame randomness, Wilson input sector, local reset bath, rough state, and
terminal-code equality are declared.  No global Jordan–Wigner order, parity
callback, postselection, or hidden entropy sink is used.  Actual check surgery
is named unconstructed rather than smuggled into “puncture.”

### N4 — Residual matching

Cycle 532 measures a Wilson rank increment of three.  Cycle 544's coherent
sector extraction followed by correction necessarily leaves information in a
token until reset, and its affine solve finds no transparent Pauli flipper.
Cycle 547 retains exactly three syndrome and three frame bits to repair target
dephasing.  Cycle 550 reproduces those residuals independently as `rank 1<8`,
`s_terminal=s_initial`, and nonzero side characters.  The positive subsystem
sink restores rank by retaining the labels, so the match is causal rather
than rhetorical.

### N5 — Rhetoric audit

- “Puncture ansatz” names the requested intermediate strategy; no physical
  stabilizer puncture surgery is claimed constructed.
- “Carrier blank” applies to the 24 temporary tokens and route work, not to
  the six Cycle-547 reference roots.
- “Exact inverse” applies to the coherent physical carrier schedule and the
  subsystem transfer, not to reset.
- “Constant overhead” describes installed M2 roles and primitive support, not
  constant total loop depth.
- “Minimum three bits” is conditional on arbitrary sectors, identical
  terminal target/gauge state, exact reversibility, and blank auxiliaries.
- Compiler ticks are not physical time; a phase is not energy; a sink is not
  a Record or realized history.

### N6 — Partial-closure path scan

Actionable next paths are:

1. promote the six-bit sink to a proper-cubic non-CSS/subsystem code and test
   whether its persistent gauge is compatible with the full target commutant;
2. build a local-Clifford or dissipative encoder directly into the promised
   fixed-Wilson sector, avoiding arbitrary-sector retirement;
3. keep Cycle 547's relational fields and construct the recurrent lifted
   update rather than erase them;
4. implement actual check-removal/check-restoration puncture surgery with a
   persistent terminal defect and quantify its added logical algebra;
5. specify an entropy-export environment and test whether the reduced target
   channel stays coherent after branch erasure.

### N7 — Steelman

The strongest rival is not a cleverer unitary that makes information vanish;
it changes the contract honestly.  A non-CSS subsystem code can make the
Wilson labels pure gauge and retain them in a local sink invisible to the
target.  Alternatively, a product encoder can start only in the desired
sector so no eight-to-one retirement is requested.  A dissipative encoder can
export the labels to a bath, provided that bath and the target-channel
coherence are audited.  None is excluded by the Cycle-550 lemma.

### N8 — Cross-cycle echo

The echo across Cycles 532, 544, 547, and 550 is consistent: three independent
Wilson characters must be fixed, reset exports their information, and a
retained relational field preserves the branch action.  This repetition
supports the narrow information ledger, not a general locality obstruction.
Static open-chain dressing growth, membrane-side target action, rough-code
preparation, and reversible blank retirement are distinct failures.  Because
persistent-gauge, promised-sector, relational, and dissipative routes remain
live, no broader impossibility or axiom-pressure statement survives N1–N8.

## Six-wall and TOE dependency update

| wall | Cycle-550 effect |
|---|---|
| `C_ref` | Sharpens the ledger: exact reversible arbitrary-sector closure needs at least three retained distinguishing bits; the six-bit subsystem sink is constructive.  Bare field retirement remains open only under a changed domain/terminal contract. |
| `C_num` | Not closed: a blank terminal loses a factor eight; a persistent sink restores it.  Cycle-547's full six-bit relational content remains explicit. |
| `C_wrap` | No new closure: inherited seam/wrapped-phase tests replay, and no phase is called energy. |
| `C_int` | No new recurrent update: target characters diagnose why bare correction is nontransparent; relational dynamics remains to be compiled. |
| `C_local` | Advances constructively: one fixed 24-loop NN carrier object, bounded support, collision-free all-24 controls, exact reverse, and held-size scaling are explicit.  Topology-changing check surgery and rough product preparation remain open. |
| `C_source` | Unchanged: no autonomous gravity/resource/source law is added. |

Maturity remains operational quantum/records `3/5`, time `1/5`,
inertia/matter `2/5`, gravity/source `1/5`, Born/probability `1/5`.  A branch
sink is not promoted to a Record, and a compiler schedule is not promoted to
causal time.

## Disposition and next campaign

The physical branch-carrier object is retained as constructive infrastructure.
The identical-terminal reversible puncture/blank-uncompute ansatz is closed
negatively and narrowly.  This is not a route-independent framework failure.

The optimal next campaign is the positive escape exposed by the falsifier:
compile the six-bit sink into a proper-cubic non-CSS/subsystem gauge sector and
recompute the exact target commutant, ranks, inverse, and local update.  In
parallel scientific order, attempt a promised-plus-sector product/reset rough
encoder.  Both change the information ledger explicitly and therefore test
real alternatives rather than repeating the impossible blank-terminal map.

## Cold certificate

The final cold command was:

```text
/usr/bin/time -lp python3 \
  scripts/physical_reversible_puncture_branch_retirement_cycle550_2026_07_21.py \
  --mode puncture-retirement-certificate
```

It passed `10/10` top-level tests.  Internal elapsed time was
`191.2115118750371 s`; external wall time was `192.71 s`.  Maximum RSS was
`124,715,008` bytes with zero process swaps.  The new physical carrier,
branch, dimension, and alternative-route controls completed at
`38.5532957080286 s`; the remainder was the pinned Cycle-537 replay.  The hard
wall was 1,200 seconds.

Zero cold residuals include carrier/source/active-role collisions, every NN
and layer-operand check, terminal carrier position, terminal route-work
blankness, all-24 loop/source/control covariance, all-576 group action,
temporary-carrier uncompute, subsystem transfer/inverse/target spectators,
and inherited target leakage/inverses.  The decisive nonzero controls are the
exact Gram residual `1.0`, 56/64 nonblank syndrome branches after inverse
extraction, 16/64 nonblank-carrier branches after deleting one inverse
Toffoli, frame inverse blank probabilities `1/2` and `1/8`, and 150/216
negative-side plus 300/432 side-difference target characters.
