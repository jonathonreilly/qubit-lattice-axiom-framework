# Physical row-reader payload tap — Cycle 165

Status: parked constructive result on the single bare-metal compiler PR.

## Question

Can each of the three original physical row records feed both the retained
commutator reader and the downstream row-payload network, without supplying a
duplicate row record or changing the reader's outputs?

## Result

Yes. The quiet axial face of the retained reader is surrounded by the same
four physical index markers already used to type its bit outputs. Opening that
face defines one covariant whole-row tap. The source row still enables the
ordinary four bit records, and independently enables one copy of its complete
32-valued row role.

The tap adds 32 canonical rows and 768 proper-cubic raw rows:

```text
Cycle-164 candidate law                  96,620
row-reader payload tap                      768
Cycle-165 candidate law                  97,388
raw overlap                                   0
raw conflicts                                  0
```

No new onsite role is introduced. The local context uses the retained row
role and the four retained reader-index roles.

## Exhaustive tests

Both retained reader interfaces were tested for all 32 signed Pauli rows at
identity and for a representative row in all 24 proper-cubic orientations.

The one-port generator reader plus payload tap has:

```text
reachable schedule states       112
canonical schedule edges        320
terminal history classes          1
maximum frontier                  5
wrong/dead/parasitic writes        0
```

The two-port measured-row reader plus payload tap has:

```text
reachable schedule states      4,375
canonical schedule edges      21,250
terminal history classes          1
maximum frontier                  9
wrong/dead/parasitic writes        0
```

Deleting the sole physical row source suppresses both the bit-reader work and
the whole-row payload branch. No bit, selector, product, or second row source
is supplied.

## Bare-metal and campaign meaning

One record can be a common causal parent of several later records. The
framework therefore does not need a cloning instruction, a second prepared
copy, or a host-side payload injection merely because the same row participates
in both commutation and state update.

This closes the last distinct interface mechanism identified in the
conditional stabilizer-update campaign:

- three physical row sources can feed both reader and payload work;
- two commutators derive the case bits;
- the controller derives the two selectors;
- row transport and forking reach all payload consumers;
- the multiplier derives `g2*g1`;
- two/three-way muxes select the updated rows;
- directional terminals converge them to two fixed outputs.

The remaining task is one joint geometric placement of those retained positive
atoms, followed by full covariance, schedule, deletion, and predecessor
regression. Cycle 165 does not claim that placement is already complete, and
it makes no impossibility or minimum-axiom claim.

## Framework relevance and failure conditions

The compiler is not the objective by itself, and the present axioms are not
being protected. This campaign tests whether one candidate local framework can
turn physical records into a nontrivial conditional quantum update without a
host calculation supplying intermediate bits, selectors, products, payloads,
or outputs.

That is a real contribution to the operational-quantum interface: the
conditional stabilizer-update map has now been decomposed into local,
covariant, deletion-sensitive mechanisms under one candidate law. The physical
row roles also test whether distinct algebraic carriers can be individuated
and reused by their record context, but they do not yet derive physical matter
or statistics.

The result does not connect the operational pipeline to a derived clock,
continuum dynamics, thermodynamic resource, gravity response, boundary
selection, occurrence rule, or probability law. Those cross-interface joins
remain the standard by which the framework—and therefore its axioms—must be
judged.

The candidate structure should be rejected or revised if joint placement
requires incompatible local laws, host-supplied intermediates, orientation-
specific exceptions, or unbounded new role types for each downstream
operation. Even a successful joint placement remains only a substrate theorem
until its records and transformations are identified with independently
derived physical lane quantities.

Nothing here addresses occurrence, outcome choice, weights, local time,
permanence, or fundamental-law selection. No axiom, primitive, registry,
policy, or audit edit follows.

## Verification

```text
PYTHONPATH=scripts python3 scripts/physical_row_reader_payload_tap_cycle165_2026_07_16.py
```
