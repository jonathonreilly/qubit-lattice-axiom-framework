# Physical five-lane formation and membership — Cycle 179

**Status:** constructive probe; cold standalone runner PASS 17/17; audit
unset.

**Companion runner:**
[`scripts/physical_five_lane_formation_membership_cycle179_2026_07_16.py`](../../../../scripts/physical_five_lane_formation_membership_cycle179_2026_07_16.py)

## Question

Can Cycle 176's formation-then-readout result be orthogonalized into a genuine
**five-lane formation** apparatus?

The target has:

- ten matching physical witnesses;
- five separated H0/H1 formation sites;
- five physical bit-cable trees;
- fifteen physical candidate leaves, one for each of five literals in three
  membership comparisons; and
- no reconstructed 32-valued measured-row site.

The existing generator and product reference readers remain in scope. The
measured candidate enters the comparator only through five physical H0/H1
records.

## Minimal law price

The first census asks only whether matching opposite H0/H1 records can form
the same H0/H1 record at an open site.

```text
canonical schemas                            2
proper-cubic raw rows                        6
overlap with Cycle-169 unified law           0
merged rows                            101,714
deterministic conflicts                      0
new onsite roles                             0
```

This is smaller than Cycle 176's 96-row signed-row ingress because the output
alphabet is only H0/H1.

The two canonical schemas are simply:

```text
H0 at +z and H0 at -z  ->  H0 at the open center
H1 at +z and H1 at -z  ->  H1 at the open center
```

Their six proper-cubic rows cover the three unoriented opposite-axis pairs.
No coordinate, direction, measured-row role, or new onsite role is encoded in
the output.

## Constructed apparatus

The apparatus has one fixed geometry for every five-bit word:

```text
ten matching witnesses
          |
          v
five separated H0/H1 formation sites
          |
          v
five three-branch physical cable trees
          |
          v
fifteen candidate-literal leaves
          |
          v
three existing signed-membership comparators
          |
          v
existing Boolean reduction and terminal identity sink
```

The five source neighborhoods are pairwise disjoint and noncontacting. Each
source has exactly its two matching witnesses at opposite z-neighbors; its
other four faces are open. The measured word is therefore never reconstructed
at a single site. Each literal consumer receives the corresponding H0/H1
record through its own physical cable branch.

The terminal identity sink is an existing AND-role use with a fixed H1 input.
It consumes either H0 or H1 so the reject branch can also terminate with no
enabled residue. It adds no row and no onsite role.

## Finite composition boundary

Five disjoint local M2 copies generate the ordinary 32-codeword joint algebra
only on the generated finite-composition domain tested here. The runner must
show that the five source neighborhoods are disjoint, that the same geometry
accepts all 32 H0/H1 assignments, and that no cross-lane local contact changes
their independent ingress signatures.

That is an operational finite-composition result. It is **not a tensor-product
theorem** and does not silently assume that disjoint lattice sites already
carry an approved qubit tensor product.

The five H0/H1 records are extensional record-law labels. A later
CP/instrument bridge is still required before calling them a nondisturbing
physical qubit code.

## Required controls

The probe distinguishes:

- deletion of either witness for any lane, which must suppress that bit source
  and its downstream membership use; and
- payload-only deletion after formation, which must leave all five bit
  sources present while suppressing the selected comparator branch and final
  readout.

It must also include complete local-law checks, at least two discriminating
physical replays, causal depth, terminal cleanliness, and all 24 proper-cubic
images.

The runner records the following exact hard-instance certificate:

```text
fixed initial records                         3,971,023
dynamic records                                341,029
load-bearing dynamic edges                     341,044
causal roots                                        15
maximum causal depth                            22,905
five source depths                       (1, 1, 1, 1, 1)
first candidate payload depth                   10,777
final output depth                              22,905
```

The accept replay uses `00100` and yields H1. The sign-flipped reject replay
uses `00101` and yields H0. Both terminate with an empty enabled set.

All ten single-witness local deletions suppress the affected source
signature. The stronger physical deletions cut that source and its descendants
while preserving the other four formed source records. The independent
payload-only deletion is downstream of formation: it preserves all five
formed sources while suppressing the selected comparator branch and final
output. This is the control that distinguishes local formation from later
transport and readout.

The all-codeword and all-rotation totals are runner gates rather than
hand-selected examples:

```text
five-bit codewords                                  32
expected H1 membership accepts                       3
expected H0 membership rejects                      29
proper-cubic images                                 24
exact rotated local checks                   8,184,696
```

The cold standalone result is:

```text
PASS 17
FAIL 0
RESULT FIVE_LANE_FORMATION_MEMBERSHIP
```

## What the probe says about “formation by reading”

Within this exact finite construction, downstream readout is not required for
the five source records to form. The sources are causal roots, while every
candidate leaf, membership payload, and final output is later in the
dependency graph. Deleting a downstream payload leaves all five source
records present.

That is evidence for a clean bare-metal decomposition:

1. matching local witnesses enable a bit record;
2. the formed record is transported;
3. a later apparatus consumes it in a membership/readout operation.

It does not prove that Nature must use this decomposition. In particular, the
runner does not identify one witness with an observer, a clock, or a readout
event. It instead shows that those identifications are not required to make
the local five-lane science close. A claim that reading or a clock is the
second witness would need a separate physical interface identifying that
event with one of the two local witness records.

## Scope

This runner concerns exact local enablement and causal closure. It does not
select the next enabled event, derive fairness, supply an occurrence rate,
assign probability weights, or explain the first/cosmological seed.

It does not choose axiom language. Failure of a particular cable or comparator
interface is to be localized as compiler geometry unless a genuinely
underivable physical condition survives the alternative-route checks.

No axiom, primitive, registry, policy, or audit edit follows.
