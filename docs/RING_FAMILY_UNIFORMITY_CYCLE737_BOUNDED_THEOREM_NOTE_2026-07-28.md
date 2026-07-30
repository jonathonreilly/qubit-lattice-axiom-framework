# Selected constructor lengths, cycle-graph censuses, and literal diagnostics — Cycle 737

Date: 2026-07-28

Authority: none

Audit: unset

Status: bounded conditional construction

Claim type: bounded_theorem

Runners:

- [primary finite constructor/census runner](../scripts/frontier_cycle737_ring_family_uniformity_2026_07_28.py)
- [independent live-primary and gate-stream checker](../scripts/frontier_cycle737_ring_family_independent_check_2026_07_28.py)

Constitutional effect: none. This package changes no axiom, framework
Admissibility rule, primitive, registry, policy, audit result, or audit status.
The filename is retained for stacked-branch continuity; the submitted
ring-family uniformity claim is not retained below.

## Result

### One supplied constructor

For the current non-padded code constructor
`K.interleaved_program(b)`, with a supplied positive integer bank count `b`,
the station kinds occur with multiplicities

\[
  1,\quad b,\quad b-1,\quad 2(b-1),\quad 4(b-1),\quad 1
\]

for source, bank, cross, handoff, relay, and finalizer rows. Therefore

\[
  \operatorname{len}(K.\operatorname{interleaved\_program}(b))
  =1+b+(b-1)+2(b-1)+4(b-1)+1=8b-5.
\]

This is an exact property of that supplied program constructor. It is not a
uniqueness theorem, a restriction on other constructors or geometries, or an
identification with framework Admissibility. In particular the same
constructor continues with `b=5`, producing 35 stations.

### Four selected cycle-graph censuses

For the four explicitly selected pairs

\[
  (b,n)=(1,3),(2,11),(3,19),(4,27),
\]

the runners enumerate the independent sets of the cycle graph \(C_n\).
Their occupancy counts agree with

\[
 |\operatorname{Ind}_k(C_n)|
 =\frac{n}{n-k}\binom{n-k}{k}
\]

for \(k>0\), with the empty-set count equal to one.

| `n` | counts by occupancy `k` | total |
|---:|---|---:|
| 3 | `1, 3` | 4 |
| 11 | `1, 11, 44, 77, 55, 11` | 199 |
| 19 | `1, 19, 152, 665, 1729, 2717, 2508, 1254, 285, 19` | 9,349 |
| 27 | `1, 27, 324, 2277, 10395, 32319, 69768, 104652, 107406, 72930, 30888, 7371, 819, 27` | 439,204 |

The `n=3` fixture is degenerate for any multi-token reading: it contains only
the empty mask and three one-token masks, so its multi-token and pair-distance
censuses are both zero.

### Static marked-edge rows

For every selected independent mask \(A\), the runner reconstructs the
supplied canonical reference row with \(r_0=0\) and
\(h=|A|\bmod 2\), satisfying

\[
 A_s\oplus r_s\oplus r_{s+1}
 \oplus h\,\mathbf 1_{s=0}=0.
\]

The fixed cut and gauge are supplied. On the sample containing every mask
with occupancy at most two and one representative from each higher occupancy,
the explicit cut-compensated, gauge-normalized translation agrees with the
canonical target in `12`, `649`, `3,401`, and `9,801` identities for
`n=3,11,19,27`, respectively. This is static algebra, not passive covariance
of an unmarked ring and not autonomous preparation.

### Actual count/comparator prefix

For each selected ring, the actual current
[Cycle-731 count/comparator constructor](TOKEN_COUNT_CERTIFICATE_CYCLE731_BOUNDED_THEOREM_NOTE_2026-07-28.md)
is cut at `comparison_compute_stop`, before the guarded Q layer. With the
expected count supplied, a fresh bit-plane execution gives:

| `n` | matching-count accepts | off-diagonal refusals | exact prefix reversals |
|---:|---:|---:|---:|
| 3 | 4 | 4 | 8 |
| 11 | 199 | 995 | 1,194 |
| 19 | 9,349 | 84,141 | 93,490 |
| 27 | 439,204 | 5,709,652 | 6,148,856 |

These are literal prefix facts. The full guarded word is not executed or
claimed.

### Bare-word execution diagnostic

The current bare
[Cycle-719 recurrent-controller word](RECURRENT_MATTER_HISTORY_CONTROLLER_CYCLE719_BOUNDED_THEOREM_NOTE_2026-07-26.md)
is also applied to every selected independent mask under its supplied program,
genesis, orientation, endpoint direction, and clean B/work registers. The
literal word rotates the A rail, returns B/work clean after one circuit, and
is exactly reversed on all `12`, `2,189`, `177,631`, and `11,858,508`
configuration-steps.

This is only a reproducible reversible-circuit diagnostic. There is no
independent target for the changed data register, no multi-token
source/controller-domain theorem, no full guarded composition, and no
preparation or physical-law conclusion.

## Supplied and open boundary

Supplied inputs include the bank count, the current K program content and
order, each finite oriented ring, the marked cut and gauge, the K chain
genesis and endpoint direction, clean auxiliaries, the expected count, and
each external mask. These inputs vary with the selected fixture and are not
summarized by `frozen_n_dependence: null`.

The load-bearing or controlling proposal-only parents are:

- [Cycle 719 bare recurrent controller](RECURRENT_MATTER_HISTORY_CONTROLLER_CYCLE719_BOUNDED_THEOREM_NOTE_2026-07-26.md);
- [Cycle 728 marked-edge relation](BKSF_HOLONOMY_COMPRESSION_CYCLE728_BOUNDED_THEOREM_NOTE_2026-07-28.md);
- [Cycle 730 charge-row convention](CHARGE_ROW_ENFORCEMENT_CYCLE730_BOUNDED_THEOREM_NOTE_2026-07-28.md);
- [Cycle 731 count/comparator prefix](TOKEN_COUNT_CERTIFICATE_CYCLE731_BOUNDED_THEOREM_NOTE_2026-07-28.md);
- [Cycle 734 externally positioned template scope](PAIRED_EXCITATION_GENESIS_CYCLE734_BOUNDED_THEOREM_NOTE_2026-07-28.md);
- [Cycle 735 supplied separated-pair control](SEPARATED_PAIR_LAWFUL_CONTROL_CYCLE735_BOUNDED_THEOREM_NOTE_2026-07-28.md); and
- [the repaired Cycle 736 static boundary](PAIRWISE_SEPARATED_MULTISOURCE_CYCLE736_BOUNDED_THEOREM_NOTE_2026-07-28.md).

All remain proposal-only at their own scopes. Nothing here upgrades their
authority.

Open and explicitly not claimed:

- framework Admissibility, constructor completeness, or ring uniqueness;
- uniformity over all positive `b` for the finite diagnostics;
- controller lawfulness for simultaneous sources;
- the full Cycle-731 guarded word or W4 composition;
- source selection, genesis derivation, autonomous preparation, Record,
  time, Born, or physical realization;
- a maximal domain, adjacency wall, non-family failure, or no-go for other
  controllers, schedules, or geometries.

The observation that `n=5` is not in the image of this particular non-padded
constructor is only an algebraic membership observation. It is not a failed
ring or a foreclosure statement.
