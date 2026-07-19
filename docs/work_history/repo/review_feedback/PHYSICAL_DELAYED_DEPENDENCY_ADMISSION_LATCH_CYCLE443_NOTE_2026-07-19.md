# Physical delayed dependency-admission latch — Cycle 443

Date: 2026-07-19
Authority: none
Audit: unset

## Question and bounded result

Can one physically generated protected candidate packet supply the dependency
inputs of a later candidate, with reciprocal links and an admission certificate
then computed from the two retained packets rather than declared by the host?

Within the finite Cycle-433 code space, yes.  Cycle 443 joins two independent
actual Cycle-433 detector-to-complete-candidate writer copies.  The first actual
Cycle-430/Cycle-424 detector produces a parent candidate.  A reversible local
loader makes a provisional successor: its predecessor bank, predecessor
coordinate, predecessor-present, and readiness are derived from the retained
parent.  The complete bank and coordinate use paired local CNOTs.  A fixed
three-input reversible occupancy staircase computes the parent occupancy
conjunction, fans its physical output into predecessor-present and readiness,
and uncomputes all three prefix M2.  A second actual detector then controls the
successor writer.  No parent-present bit is computed by the host.

The reciprocal-link, certificate, and admit triples enter blank.  A fixed
reversible verifier compares the retained parent and
child packets, checks occupied parent and child, checks the complete child prior
bank against the parent word, checks the child predecessor coordinate against
the parent site, requires distinct parent/child target coordinates, and requires
a blank fork carrier.  It copies its conjunction into the four protected
triples and uncomputes every comparison and prefix work bit.  Admit=111 is
load-bearing: a fixed reversible twelve-input local staircase computes a
physical enable M2 from all twelve derived bits, controls the subsequent
writer/ingress/readability fixture, and clears its twelve prefix-work M2 and
enable M2.  There is no host-computed enable.  Removing one output lane from
any of the four triples, one prefix gate, or the enable-copy gate keeps the
downstream target blank.

The output is only a **branch-relative admitted Record candidate**.  It is not a
selected framework Record, occurrence, or history fact.

## Exact finite statement

For train L=3 and held L=6, and for arbitrary tested coherent two-detector
inputs, the declared branch-relative code-space encoding obeys

`E_443 G_coarse = G_physical,443 E_443`.

The tested residual is numerical roundoff only.  The exact inverse retains both
detectors, parent, child, verifier outputs, fork carrier, and downstream target.
No detector outcome is selected or erased.  The inverse restores the supplied
blank child-dependency inputs, verifier triples/work, and downstream interface.

The verifier is compiled into a fixed finite line/corridor schedule using only
X, CNOT, Toffoli, and adjacent SWAP decompositions.  Primitive support is at
most three M2.  The three Cycle-433 layouts, two detector patches, loader
corridors, verifier interface layout, and clean auxiliary locations are fixed
finite supplied geometry.  Under all 24 proper-cubic frames the detector
apparatus, packet/payload maps, writer patches, dependency relations, verifier
truth function, and schedule rotate as one family.  This is covariance of a
declared bounded compiler, not autonomous spatial genesis.

## Presentation and grade audits

Cycle 443 chooses the Cycle-436 presentation-faithful admission semantics for
this candidate experiment (Law B): operationally equal but presentation-distinct
packets remain distinct.  Coarse effect-functional Law A remains a live rival;
the framework law is not selected here.

Cycle-440 maximally-mixed trace metadata and its exact positive non-trace grade
metadata are separately reconstructed.  Trace and exact non-trace grade
metadata have byte-identical gate traces and physical outputs, not merely
matching counts.  Grade is therefore a
spectator and supplies no admission gate.

The actual Cycle-439 train/held three-label writer packets are also accepted as
parents by the same verifier path, with no host-side label oracle.

A static schedule-control audit classifies every remaining Python `int`,
equality, `all`, and branch.  State equality and conjunction appear only in the
independent coarse expected-output builder or diagnostics.  Frame `argmax`
chooses the externally supplied rotated apparatus family.  Sparse branch
iteration reads the retained physical detector basis M2, as in Cycle 433.  The
nominal `G_physical,443` schedule itself uses only those physical detector M2,
fixed paired loader CNOTs, the fixed loader occupancy staircase, the fixed
packet verifier, and the fixed downstream-enable staircase.  No state-derived
host Boolean controls a nominal physical gate.

## Exact results

| Check | Cold-run result |
|---|---:|
| Cycle-443 tally | 10 passed, 0 failed |
| `E_443 G_coarse - G_physical,443 E_443` | 0.0 |
| maximum inverse residual | 8.024928461843671e-16 |
| trace/non-trace physical-output residual | 0.0; byte-identical output and full trace |
| admission minus detector-sector-11 weight | 0.0 |
| downstream minus admission weight | 0.0 |
| writer/verifier/prefix work leakage | 0 |
| proper-cubic cases | 24 frames, 48 train/held cases, 0 failures |
| maximum apparatus/effect frame residual | 2.172217384091364e-16 / 7.850462293418876e-16 |
| main verifier resources | 505 interface/work M2; 1010 logical gates; 2,309,978 NN primitives; support <=3 |
| predecessor loader resources | 3 blank prefix M2; 100 paired field-copy CNOTs + 8 occupancy/fanout NN primitives; support <=3 |
| downstream physical enable resources | 13 blank M2; 25 NN primitives per compute or clear; 50 around writer; support <=3 |
| main verifier trace SHA-256 | `ed320cda203a4e987f2915d107f3e64e0b477376df0ea2b391bf09aa83e8a366` |
| predecessor-present trace SHA-256 | `6c9f2634e83e4e2ca14f2214f82da87ab8c50f389f2c702f5f874aac563c23b8` |
| downstream-enable trace SHA-256 | `cd3e6c57cf78d079f9ff78ed7d2fb378d4db0040cff9316fe681a38950536900` |
| Cycle-440 exact non-trace vector SHA-256 | `eec13b3c9099563414e2ceb7e8669d4abb350dcc072730ddb80185408a9d995f` |

## Controls

The runner checks:

- coherent four-sector branch retention, the exact intertwiner, and inverse;
- parent-to-successor loader inversion and full 79-lane prior equality;
- deletion of a loader occupancy-prefix gate and of each of its two fanouts;
- verifier work-zero forward and inverse;
- dirty-input refusal separately for each of the four protected triples;
- train L=3, held L=6, and all 24 proper-cubic frames;
- actual Cycle-439 three-label parent compatibility;
- missing child click, missing loader, prior splice, predecessor mismatch,
  target collision, occupied fork, downstream-control deletion, and payload
  write deletion;
- deletion of one fanout gate in each reciprocal-link/certificate/admit triple;
- deletion of a downstream conjunction-prefix gate and its output-copy gate;
- malformed widths, lanes, one-hot heads, and archive slots;
- finite capacity and exact reversible recurrence.

The finite archive is an XOR fixture with a supplied one-hot head.  After K
admitted copies its K slots are occupied, and after 2K identical steps it
recurs exactly.  Finite capacity recurrence is not renewal, and no erasure or
irreversibility is inferred.

## Supplied and derived structure

Derived here:

- parent and child candidates from two actual detector couplings;
- child predecessor bank, coordinate, predecessor-present, and readiness from
  the retained parent;
- reciprocal-link, certificate, and admit triples from retained packet fields;
- a downstream candidate conditional on all twelve derived output bits.

Still supplied:

- both normalized apparatus inputs and the finite detector/writer layouts;
- all parent, child, and downstream proposal fields;
- all remaining payload, faithful-close, provenance, freshness, lawfulness,
  and formation-law inputs remain supplied;
- blank packet, fork, verifier-output, verifier-work, and archive carriers;
- interface co-location/corridors, the finite all-frame family, archive
  capacity, and one-hot archive head;
- the presentation-faithful candidate semantics used by this experiment.

The result does not provide autonomous payload or proposal formation, select a
framework formation/admission law, or produce a selected global history.
There is no selected global history, occurrence, Born law, renewal,
irreversibility, no-go, minimum, or axiom pressure.  The result makes no
route-independent obstruction claim.

## Reproduction

```bash
python3 scripts/physical_delayed_dependency_admission_latch_cycle443_2026_07_19.py
```

The executable is the authority for exact residuals, hashes, resource counts,
deletion tables, and the final pass/fail total.
