# Physical joint stabilizer update — Cycle 166

Status: parked constructive result on the single bare-metal compiler PR.

## Question

Can the retained Cycle 160–165 mechanisms coexist in one finite
nearest-neighbor geometry and physically execute one valid representative of
each of the four conditional two-generator update branches, without a host
supplying commutation bits, case selectors, row products, copied payloads, or
final output rows?

## Result

Yes, for the four tested valid representatives, as a constructive closure
witness for the present candidate law.

One joint apparatus now:

1. reads the three original signed Pauli-row records;
2. derives both symplectic commutation bits;
3. forms the four-way case record and carries it to both update lanes;
4. exposes and transports the original rows without duplicate supplied rows;
5. derives the commuting product `g2*g1`;
6. selects the correct two recurrent rows; and
7. writes them at two fixed common-output sites.

For every append in those executions, the enabled singleton map equals the
declared causal frontier. Each run terminates with the two independently
expected tableau rows and no parasitic enabled write.

## What had to change

The stock Cycle 160–165 devices did not compose unchanged. Two interface seams
were real:

- a Cycle-165 whole-row tap has one transport face and cannot directly feed
  two downstream consumers;
- the stock isolated three-way mux context does not coexist with the derived
  case-selector cable at the same socket.

The joint witness adds three covariant local families and no new onsite role:

```text
Cycle-165 candidate law                         97,388
generic whole-row splitter                         768
integrated case-to-selector family                 192
new transport-ready gate rows                    2,304
Cycle-166 candidate law                         100,652
raw conflicts                                         0
```

The gate family has 3,840 raw images, of which 1,536 are identical retained
rows. The net law delta is therefore 3,264 raw neighborhoods.

These are compiler-law rows, not axiom content. The integrated selector is a
finite closure construction with explicit lane semantics; it is not yet the
preferred candidate for fundamental-law compression.

## Interface lessons

Three details were load-bearing.

First, each tap is carried along a short ordinary cable before it reaches the
splitter. This moves the split away from the reader's physical index furniture.
The trunk and both branches are solved as one interface bundle so the trunk's
guide marker cannot occupy a cell required by a branch.

Second, the case record is physically forked into two long, disjoint cables.
The multiplier and all six row-payload branches occupy explicitly separated
corridors. The construction uses finite measured separations, not an appeal to
unbounded empty space.

Third, empty interface faces must remain genuinely empty. Caging begins outside
the complete one-neighbor shell of every dynamic site. Otherwise a late frame
record silently changes the local premise of a selector or common-output join.
Absence is not promoted to an onsite object; it remains non-occupation required
by the exact nearest-neighbor signature.

## Case, schedule, and deletion tests

One valid independent commuting stabilizer basis, paired with four legitimate
measured Pauli rows, covers all commutation cases:

```text
g1 = +ZI, g2 = +IZ

(c1,c2) = (0,0)  -> (g1, g2)
(c1,c2) = (0,1)  -> (g1, P)
(c1,c2) = (1,0)  -> (P,  g2)
(c1,c2) = (1,1)  -> (P,  g2*g1)

P00 = +ZZ, P01 = +IX, P10 = +XI, P11 = +XX
```

All four close under the same geometry and 100,652-row law.

The largest representative contains:

```text
initial fixed records             379,288
required dynamic records           30,831
maximum enabled frontier                16
final parasitic writes                   0
```

For each of the four valid cases, both lexicographically minimal and maximal
schedulers close with the same two outputs. More strongly, each dynamic
dependency graph has zero adjacent unordered pairs: whenever two dynamic sites
are nearest neighbors, one is a declared parent of the other. Since the law is
nearest-neighbor and append-only, independent enabled writes cannot alter one
another's premise. This is the finite confluence certificate used here; it is
causal order, not metric time.

The same twenty direct-parent deletion controls pass in each case, for eighty
checks total. They cover:

- each original row source and its tap;
- each tap trunk and splitter;
- both commutation parents of the case record;
- both multiplier operands;
- each lane's case input, selector, selected bus, path endpoint, terminal, and
  common-output join.

In every control, removing the named parent suppresses the claimed child write
rather than producing the same or an alternate output.

Every case is replayed in every proper-cubic orientation, for ninety-six
case-orientation executions. Cycles 160–165 are rerun as predecessor
regressions.

## Bare-metal meaning

This establishes a nontrivial substrate theorem: for the four tested valid
representatives, one candidate local, covariant, append-only record law can
physically compose the complete four-branch conditional update structure from
original input records to recurrent output records. Intermediate algebra is
not performed by the host.

The result is relevant to the TOE lanes in bounded ways:

- **O:** the tested four-branch stabilizer/Lüders update fragment is now one
  physical causal apparatus rather than a collection of separately tested
  gadgets;
- **T:** independent writes are order-confluent, but no duration, rate, or
  metric time is derived;
- **I:** signed Pauli rows act as transportable, forkable, multiplicable
  physical record carriers, but this does not derive matter, particles, or
  statistics;
- **B:** one supplied measurement row determines one complete conditional
  record history, but outcome occurrence and outcome choice remain open;
- **G:** no gravity claim follows. Harness size and record count are compiler
  costs until a physical resource map is independently derived.

## Architecture status

The integrated route proves existence, not uniqueness or fundamentality.

A generic binary mux controlled directly by retained `H0/H1` records has
separately passed both controls, all 32 row roles, all 24 rotations, exact
frontier replay, and deletion controls. With the shared splitter it would give
a 99,740-row candidate law and factor the update as:

```text
lane1  = c1 ? P       : g1
stageA = c1 ? g2*g1   : P
lane2  = c2 ? stageA  : g2
```

That architecture is more reusable but permanently writes an intermediate
`stageA` row even when `c2=0`. Under append-only record ontology this is a real
physical difference, not free scratch space. A direct-predicate/pivot route
without selector roles also remains open. The correct next architecture test
is an out-of-sample four-input selector or three-generator update, not a choice
by aesthetic preference.

## Next cross-lane target

The strongest immediate science bridge is a record-native Peres–Mermin
context-wise parity-support certificate.

The joint apparatus can supply transported signed observables, commutation,
conditional update, multiplication, and fixed terminal records. An independent
checker must keep three types distinct:

1. the three unsigned observables multiply to `+I` for five contexts and `-I`
   for the sixth;
2. the three scalar outcome signs have the same five-plus/one-minus parity;
3. the three full signed outcome rows multiply to `+I` in every lawful
   completed context.

The third statement follows because the observable-product sign and
outcome-parity sign cancel. Expecting the signed rows themselves to produce
`-I` in the sixth context would accept an impossible history or silently strip
part of the record. The three checks must be physically separate and the parity
checker must not read the update controller's internal case or selector roles.

This target is pointwise and weight-free: it does not require Born weights or a
prepared-state identity.

One compact atom remains before that probe is honest: signed membership in the
commuting case, so the physically impossible opposite outcome is rejected by
the law rather than by a host table.

Until the same observable in its row and column contexts has one physical
ancestry or a record-faithful instrument-equivalence theorem, the licensed
claim is context-wise parity support rather than a contextuality certificate.

## Scope and axiom consequence

This result does not select the 100,652-row law as fundamental, prove the
current axioms correct, or show that the compiler vocabulary is minimal. The
axioms remain falsifiable by failure to reach independently measured
cross-lane physics.

Nothing here derives occurrence, probability, prepared-state identity, local
time rate, permanence beyond local non-revocation, mass, chirality, continuum
dynamics, gravity, or law selection.

No axiom, primitive, registry, policy, or audit edit follows.

## Verification

```text
PYTHONPATH=scripts python3 scripts/physical_joint_stabilizer_update_cycle166_2026_07_16.py
```
