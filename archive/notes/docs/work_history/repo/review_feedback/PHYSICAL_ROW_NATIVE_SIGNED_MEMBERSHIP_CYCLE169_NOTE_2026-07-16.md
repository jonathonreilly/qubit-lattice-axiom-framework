# Physical row-native signed membership — Cycle 169

Date: 2026-07-16

Status: constructive probe green; audit unset

Companion runner:

```text
scripts/physical_row_native_signed_membership_cycle169_2026_07_16.py
```

## Question

Can one physical nearest-neighbor apparatus decide whether a measured signed
two-qubit Pauli row is exactly one of `g1`, `g2`, or the physically derived
commuting product `g1*g2`, without a host supplying literal row bits, the
product row, equality records, or the final membership bit?

## Construction

The apparatus accepts exactly three variable input records: `g1`, `g2`, and
the measured row `P`.

- Cycle 165 exposes the four spatial bits and one whole-row tap of each
  original row.
- The generic Cycle 166 whole-row splitter fans ancestry before literal
  decoding. The measured-row tap needs eleven leaves: one sign for the first
  comparison and all five bits for each of the other two comparisons.
- Each generator tap has two leaves: its sign bit and its Cycle 164 multiplier
  feed.
- The Cycle 164 product has five decoder leaves.
- Existing ported bit readers decode indices zero through three. The Cycle 167
  `OY` reader decodes the sign bit.
- Three five-stage total-status comparators test exact signed equality.
- Two retained XOR rows combine the mutually exclusive equality records.

The binary ancestry lower bound is exact for this architecture:

```text
P tap: 11 leaves                         10 splitters
g1 tap: sign + multiplier                 1 splitter
g2 tap: sign + multiplier                 1 splitter
product: 5 leaves                         4 splitters
total                                    16 splitters
```

No onsite role is added. The product row, decoded row literals, running status
records, XOR records, and final membership record are all dynamically formed.

The comparator does not import a true seed or any H-typed operator rail. Its
first stage is a direct equality row: two derived literals, one existing GUIDE,
and two existing FRAME records produce H0 or H1. Each later stage is one
reusable fold row: the previous generated status and the next two derived
literals, guarded by GUIDE and FRAME, produce the new status. The comparator
geometry contains zero fixed H records.

## Why the comparator is spaced

The stock compact comparator assumes adjacent supplied bit records. Two
adjacent cable-derived bit endpoints cannot coexist: each endpoint needs the
other endpoint's face to carry cable FRAME or GUIDE furniture. The runner
keeps this as an explicit negative regression.

Cycle 169 spaces comparison targets ten cells apart. Each target uses the new
five-neighbor direct/fold local signature: two derived literals, GUIDE and
FRAME, plus either a FRAME backstop at the first stage or the previously
generated status at later stages. The retained H0/H1 cable transports only
that generated running status between spaced targets, leaving each candidate
and reference endpoint isolated.

Missing input ancestry stalls the corresponding status suffix. Absence is
never interpreted as H0.

## Law accounting

The membership apparatus alone uses:

```text
Cycle 165 base                         97,388
generic whole-row splitter               768
ported sign decoder                      768
direct/fold comparator                    288
membership law                        99,212
raw conflicts                              0
```

The union with the complete Cycle 166 update law is a separate number:

```text
Cycle 166 update law                  100,652
ported sign decoder                      768
direct/fold comparator                    288
unified law                           101,708
raw conflicts                              0
```

The note and runner do not exchange those two scopes.

## Current verification

The route-occupancy preflight closes all 38 route families with:

```text
dynamic path-target collisions             0
path targets on fixed furniture             0
path targets on original sources            0
```

One global cage then closes the full apparatus:

```text
fixed/cage records                  1,587,395
dynamic records                       132,541
generated terminal ports                   54
adjacent unordered dynamic seams             0
```

For the hard signed-product transcript
`g1=(0,1,0,0,0)`, `g2=(1,0,0,0,1)`,
`P=(1,1,0,0,1)`:

```text
initial enabled records                     15
initial scheduled records                   15
off-footprint enables                        0
missing scheduled enables                    0
local compiled-signature failures            0
minimum schedule                     PASS / terminal silent
maximum schedule                     PASS / terminal silent
```

The minimum replay formed all 132,541 dynamic records with maximum frontier
27. The maximum replay formed the same records with maximum frontier 23.

The strict initial-state firewall is green: only the three signed rows occupy
variable source sites; no dynamic product, decoded literal, status, XOR,
membership, or output-port site is initially occupied; and the complete fixed
geometry contains no H0 or H1 record.

The exhaustive local-semantics census factors the 132,541 dynamic sites into
523 symbolic local templates. Across all 360 ordered bases and six signed
transcripts per basis:

```text
transcripts                            2,160
supported                              1,080
opposite-sign rejected                 1,080
matches in g1/g2/product position  360/360/360
template failures                          0
```

This is exhaustive local-signature coverage, not 2,160 global million-record
replays.

Proper-cubic law and labeled-geometry checks cover all 24 rotations. The twelve
canonical direct/fold truth-table cases produce 288 rotated raw checks with
zero failures. Direction preservation and site injectivity hold for every
rotation. In addition to the unrotated minimum and maximum schedules, six full
rotated presentations, indices 0–5, were physically replayed through all
132,541 formations; all six ended with H1 and a silent terminal.

The hard global ancestry census removes every direct dynamic parent plus each
of the three original row sources:

```text
dynamic/source deletion controls     132,571
fixed structural-guard controls           35
total deletion controls              132,606
surviving intended formations              0
```

## Verification boundary

The runner requires:

- all 360 valid ordered independent stabilizer bases;
- six signed transcripts per basis, for 2,160 identity-geometry checks;
- 1,080 supported and 1,080 opposite-sign rejected transcripts;
- 360 matches in each of the three candidate positions;
- all 24 proper-cubic law/geometry images of a hard product/sign transcript;
- six full rotated presentations, indices 0–5;
- lexicographically minimal and maximal full frontier schedules;
- zero adjacent unordered dynamic seams;
- direct-parent deletion stalls across row ancestry, decoding, multiplication,
  comparison, and XOR;
- no initial literal input record and no initial product row.

The six rotated full replays are a stated physical sample, not a claim that all
24 million-record geometries were globally replayed. All 24 are covered at the
raw-law and labeled-geometry covariance level.

## Scope

This is a bounded compiler-law construction. It does not select the 99,212-row
law as fundamental, derive occurrence or probabilities, establish prepared
state identity, or add axiom content.

No axiom, primitive, registry, policy, or audit edit follows.
