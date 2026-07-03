# Species Carrier Invariant Ring Has No Orbit-Separator at the Parent Readout Grade

**Date:** 2026-07-03
**Type:** bounded_theorem
**Claim type:** bounded_theorem (exact computation at the parent
corner-diagonal Hermitian linear-functional grade)
**Primary runner:**
[`scripts/frontier_species_carrier_invariant_ring_2026_07_03.py`](../scripts/frontier_species_carrier_invariant_ring_2026_07_03.py)

## Dependencies

- [`SPECIES_BRIDGE_MINIMUM_DECOMPOSITION_BOUNDED_THEOREM_NOTE_2026-06-13.md`](SPECIES_BRIDGE_MINIMUM_DECOMPOSITION_BOUNDED_THEOREM_NOTE_2026-06-13.md)
  supplies the parent carrier, readout-grade boundary, and proof-strength gap
  this note closes.

## Scope

This note closes only the parent note's invariant-ring proof-strength gap,
the ratification note's residue #9: the parent said the within-triplet
contentlessness conclusion was
"argued/strongly-supported, not exhaustively proven" because check 8 used
one representative diagonal corner-weight rather than the full invariant
functional ring.

The computation upgrades the within-triplet naming vacuity from that
representative argument to an exhaustive computation at the stated
functional grade. It retires the parent scorecard's invariant-ring gap.
It does not retire the bridge, does not change any count, and does not
touch the abstract-to-physical identification residue (#1) or the
CKM/PMNS alignment residue (#8). The audit lane owns statuses.

## Functional Space

The closed space is the real 9-dimensional space of Hermitian linear
functionals on the parent carrier `M3(C)`. A functional is represented by
a Hermitian test matrix `A`, acting on a carrier Hermitian `H` by
`f_A(H) = Tr(AH)`. The basis is

`D0,D1,D2,S01,S12,S20,A01,A12,A20`.

Here `Dk` are the three diagonal corner weights, `Sij` are real symmetric
off-diagonal reads, and `Aij` are imaginary antisymmetric Hermitian reads
on the cyclic oriented edges. The orbit-separation test is the parent
readout surface: restrict each averaged functional to the corner diagonal
and compute the spread of its three diagonal coefficients.

This is exactly the parent check-8 surface, but with the full Hermitian
linear-functional basis instead of one diagonal representative.

## Exact Computation

The runner reconstructs the parent carrier ordering:

- hw=1 carrier corners: `(1,0,0)`, `(0,1,0)`, `(0,0,1)`.
- hw=2 carrier corners: `(0,1,1)`, `(1,0,1)`, `(1,1,0)`.
- `C3` acts by the parent 3-cycle block `c3_1`.
- `eps` is the parent intertwiner `EH` from hw=1 to hw=2; pulled back to
  the hw=1 carrier, `EH* EH = I`.

The averaging group is the abstract order-6 `C3+eps` group. Its action on
this linear-functional space is nonfaithful because the pulled-back eps
acts trivially, but eps is still included in the six-element Reynolds and
Molien sums.

The degree-one Molien coefficient is

`(1/6) sum_g trace(rho(g)) = 3`.

The Reynolds average of the full 9-element Hermitian basis has exact rank
3, matching the Molien count. Thus the averaged generator set is complete
for this functional grade. A convenient spanning set is the diagonal trace
sum, the cyclic real off-diagonal sum, and the cyclic imaginary
off-diagonal sum.

Every averaged generator has zero corner-diagonal spread. The diagonal
trace sum has equal diagonal coefficients, and both off-diagonal invariant
generators restrict to zero on the corner diagonal. Therefore no invariant
generator in this complete functional-grade set separates the three
within-triplet corners.

The negative control drops the C3 generator and keeps only eps. The
Molien dimension rises to 9, and the diagonal corner weights survive as
separators. The test therefore has teeth: the no-separator result is
caused by the parent C3 orbit, not by a vacuous calculation.

## Boundary

This result closes the named invariant-ring residue at the parent
corner-diagonal Hermitian linear-functional grade. It does not identify
the abstract carrier with physical generations, does not address
across-fermion-type CKM/PMNS alignment, does not alter the bridge, and
does not alter any count.

## Reproduction

```bash
python3 scripts/frontier_species_carrier_invariant_ring_2026_07_03.py
```

Expected: eight `CHECK NN: PASS` lines, `TOTAL: PASS=8 FAIL=0`, and a
five-line summary naming the files, check count, invariant dimension,
separator verdict, and remaining scope limits.
