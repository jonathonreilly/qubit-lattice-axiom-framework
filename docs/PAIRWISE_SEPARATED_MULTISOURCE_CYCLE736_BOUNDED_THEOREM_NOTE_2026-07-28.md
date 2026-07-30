# Static independent-mask templates and count-prefix census — Cycle 736

Date: 2026-07-28

Authority: none

Audit: unset

Status: bounded conditional theorem

Claim type: bounded_theorem

Runners:

- [`frontier_cycle736_pairwise_separated_multisource_2026_07_28.py`](../scripts/frontier_cycle736_pairwise_separated_multisource_2026_07_28.py)
- [`frontier_cycle736_multisource_independent_check_2026_07_28.py`](../scripts/frontier_cycle736_multisource_independent_check_2026_07_28.py)

Constitutional effect: none. This package changes no axiom, primitive,
registry, policy, queue, audit result, or audit status.

## Result

On the supplied oriented ring with 11 stations, the primary enumerates the
199 masks with no adjacent occupied sites. Their count by occupancy is

\[
  (1,11,44,77,55,11),\qquad k=0,\ldots,5,
\]

in agreement with
\[
  |\operatorname{Ind}_k(C_{11})|
    = \frac{11}{11-k}\binom{11-k}{k}.
\]

For each externally supplied mask \(A\), the pure-X word writes:

- that mask on the logical A rail;
- \(h=|A|\bmod 2\); and
- the canonical reference row with the supplied gauge \(r_0=0\) satisfying
  the single-marked-edge relation
  \[
    A_s\oplus r_s\oplus r_{s+1}
      \oplus h\,\mathbf 1_{s=0}=0.
  \]

All 199 words are bit exact and all 199 reference rows satisfy that static
relation. This is a static register theorem. It is not a controller-orbit or
source-preparation theorem.

The unchanged Cycle-731 constructor is then cut at
`comparison_compute_stop`, after the count and equality comparison but before
the guarded Q layer. Over expected counts \(0,\ldots,5\), that actual prefix
has:

- 199 matching-count accepts;
- 995 off-diagonal refusals; and
- 1,194 exact literal reversals.

No part of the Cycle-731 full guarded word is executed by this result.

## Supplied cut and covariance

The reference gauge has a distinguished supplied cut: \(r_0=0\). Therefore
ordinary passive wire translation is not an exact symmetry of the canonical
representatives. It succeeds in 707 of 2,189 mask/shift cases and fails in
1,482.

The exact result is covariance modulo the stated canonical-gauge
normalization. For a shift by \(d\):

1. passively translate the A and reference wires;
2. when \(h=1\), toggle reference sites \(1,\ldots,d\), the marked-cut
   compensation; and
3. if the translated \(r_0\) is one, complement the complete reference row
   to restore \(r_0=0\).

That explicitly defined action matches the canonical target word in all
2,189 cases: 1,100 in the \(h=0\) sector and 1,089 in the \(h=1\) sector.
This is not described as passive covariance or as absence of a distinguished
gauge site.

## Independent check

The independent runner imports no frontier module. It:

1. executes the live primary in a subprocess and requires a successful report;
2. obtains the primary's actual template and count-prefix gates through a
   hash-checked subprocess export;
3. reconstructs the \(C_{11}\) census and the marked-edge reference recurrence
   independently;
4. evaluates every exported X/CNOT/Toffoli word with a fresh integer
   interpreter; and
5. reruns the repaired Cycle-735 adjacent positive control.

As a convention falsifier, it also inserts \(h\) at every recurrence edge.
That rejected rule disagrees with the actual canonical row on all 99 odd
configurations, and all 99 substituted rows fail the governing marked-edge
relation.

## Adjacent positive regression

The parent Cycle-735 runner still succeeds for all 11 adjacent inputs under
the **bare Cycle-719** transport. Separately, the inherited radius-one guard
predicate reports 22 step-zero rows and is explicitly not used as a maximal
controller domain.

Cycle 736 retains this positive bypass as a required regression. The 199-mask
enumeration is the selected positive test family, not an assertion that other
masks are dynamically invalid, unpreparable, or excluded.

## Dependency boundary

The load-bearing and controlling proposal-only parents are linked directly:

- [Cycle 719 bare recurrent controller](RECURRENT_MATTER_HISTORY_CONTROLLER_CYCLE719_BOUNDED_THEOREM_NOTE_2026-07-26.md), used only through the inherited finite fixture and the adjacent positive regression;
- [Cycle 724 radius-one guard](LOCAL_TOKEN_ROW_ENFORCEMENT_CYCLE724_BOUNDED_THEOREM_NOTE_2026-07-28.md), whose predicate-specific scope is preserved;
- [Cycle 728 marked-edge reference relation](BKSF_HOLONOMY_COMPRESSION_CYCLE728_BOUNDED_THEOREM_NOTE_2026-07-28.md);
- [Cycle 730 charge-row enforcement](CHARGE_ROW_ENFORCEMENT_CYCLE730_BOUNDED_THEOREM_NOTE_2026-07-28.md), which fixes the marked-edge convention consumed here;
- [Cycle 731 count/comparator constructor](TOKEN_COUNT_CERTIFICATE_CYCLE731_BOUNDED_THEOREM_NOTE_2026-07-28.md), consumed only through its count/comparison prefix;
- [Cycle 734 external adjacent template and guard witness](PAIRED_EXCITATION_GENESIS_CYCLE734_BOUNDED_THEOREM_NOTE_2026-07-28.md), whose no-controller-no-go boundary is preserved; and
- [Cycle 735 joint templates and bare transport](SEPARATED_PAIR_LAWFUL_CONTROL_CYCLE735_BOUNDED_THEOREM_NOTE_2026-07-28.md), including its distinction between static rows, bare transport, and the full guarded word.

No parent supplies retained authority or audit promotion. The runners bind
their caches to the complete mutable source/input closure used through these
constructors.

## Supplied inputs

- ring size 11, orientation, and marked gauge cut;
- the mask as an external parameter;
- a blank logical register;
- the inherited two-bank program used to construct the Cycle-731 prefix; and
- the expected count \(0,\ldots,5\).

No mask selection, application position, genesis, physical source, or
autonomous preparation mechanism is derived.

## Outside the claim

- bare Cycle-719 motion of the 199 static rows;
- transport or preservation of their reference rows during motion;
- the Cycle-731 full guarded-controller orbit;
- controller lawfulness, source arbitration, or source-factor semantics;
- W4 composition or renewal;
- autonomous, factorized, or physical preparation;
- any maximal domain, adjacency wall, complement theorem, or no-go;
- other ring sizes, dirty-register domains, or a uniform family.

These are open or separate construction obligations, not conclusions of this
note.

## Negative-claim discipline

This note makes finite positive statements about one explicitly selected
family and one constructor prefix. Non-independent masks are neither tested
nor excluded. The successful adjacent bare-transport regression supplies a
known alternate route. Therefore no derived no-go, wall, or exact-domain
conclusion is shipped.

## Verdict

Cycle 736 supplies a bounded static-template census, an explicit
fixed-cut-gauge covariance statement, and a complete finite check of the
Cycle-731 count/comparator prefix on those 199 supplied masks. It does not
supply guarded multi-source control, W4 composition, autonomous preparation,
or an adjacency/domain theorem. Independent audit remains required.
