# GMN Vev-Annihilator L4 Support Lemma

**Date:** 2026-07-02
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Status:** bounded support theorem. This note records only the finite
two-dimensional algebra that turns a supplied Higgs hypercharge `Y_H = +1` and
a supplied neutral lower-component vev record into the unbroken generator
`Q = T_3 + Y/2`. It does not derive the Higgs sector, the vev direction,
`Y_H = +1`, the hypercharge table, or any audit outcome.
**Status authority:** independent audit lane only.
**Primary runner:** `scripts/frontier_hypercharge_identification.py` (PART 9)
**Runner cache:** `logs/runner-cache/frontier_hypercharge_identification.txt`

## Statement

Let

```text
T_3 = diag(+1/2, -1/2)
```

act on an `SU(2)` doublet, let a supplied `U(1)_Y` generator act on the Higgs
doublet by the scalar `Y_H = +1`, and take the supplied neutral vev record to
be the lower component

```text
v_0 = (0, 1)^T.
```

Inside `span{T_3, Y}`, the annihilator condition

```text
(a T_3 + b Y) v_0 = 0
```

has a one-dimensional solution space and fixes `b/a = +1/2`. Up to overall
normalization, the unbroken generator is therefore

```text
Q = T_3 + Y/2.
```

This is the bounded L4 readout used by
`HYPERCHARGE_IDENTIFICATION_NOTE.md`.
The historical EWSB/Higgs-Y notes
`EWSB_PATTERN_FROM_HIGGS_Y_NOTE_2026-05-02.md` and
`HIGGS_Y_FROM_LHCM_AND_YUKAWA_STRUCTURE_NOTE_2026-05-02.md` remain useful
context, but they are not graph authorities for this L4 carrier because those
surfaces participate in the older LHCM/hypercharge citation cycle.

## Verification

PART 9 of `scripts/frontier_hypercharge_identification.py` checks:

- the stabilizer of the supplied neutral vev record in `span{T_3, Y}` is
  exactly one-dimensional;
- the coefficient ratio is computed from the nullspace as `b/a = +1/2`;
- applying the derived `Q` to the parent note's already-supplied LH-doublet
  hypercharge table gives the expected charge multiset;
- setting `Y_H = 0` removes the `T_3` component and degenerates the
  `u_L/d_L` charges, so the supplied `Y_H = +1` input is load-bearing;
- choosing the opposite vev component gives the component-swapped conjugate
  table, so the `T_3(e_L)` component assignment is a vev-direction convention.

The cache reports `PART 9 CHECKS: PASS=5 FAIL=0`, and the runner exits
nonzero if that count changes.

## Boundary

This support lemma does not close the hypercharge note by itself. It only
removes the need to treat `Q = T_3 + Y/2` as an unstructured admitted formula.
The parent remains bounded/conditional on its separate matter-assignment,
normalization, and supplied-Higgs-sector boundaries until the independent
audit lane grades those rows.
