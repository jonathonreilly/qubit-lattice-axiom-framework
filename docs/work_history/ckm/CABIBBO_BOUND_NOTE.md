# Historical Cabibbo Bound Note

**Date:** 2026-04-14  
**Status:** historical bounded CKM route note
**Script:** `scripts/frontier_ckm_mass_basis_nni.py`

## Source boundary (2026-06-12)

**Boundary:** numerical-match / bounded support only. Effective status is
audit-derived; this work-history note records only the source boundary.

The reported `|V_us| = 0.2251` is a Cabibbo-scale consistency result inside
the mass-basis NNI package. It load-bears PDG quark masses, PDG comparators,
and calibrated NNI/flavor coefficients from the bounded CKM route. This note
may not be cited as a first-principles derivation of quark masses, CKM
coefficients, the full CKM matrix, or the Cabibbo angle.

Promotion beyond numerical-match support requires deriving the mass inputs and
NNI coefficients from retained framework dynamics without fitting to CKM/PDG
targets.

## Source-edge repair (2026-06-17)

The live one-hop source for the algebraic NNI identities used by this note is
now:

- [CKM_MASS_BASIS_NNI_STRUCTURAL_IDENTITIES_NARROW_THEOREM_NOTE_2026-06-17.md](../../CKM_MASS_BASIS_NNI_STRUCTURAL_IDENTITIES_NARROW_THEOREM_NOTE_2026-06-17.md)
- [frontier_ckm_mass_basis_nni_structural_identities_2026_06_17.py](../../../scripts/frontier_ckm_mass_basis_nni_structural_identities_2026_06_17.py)

That source proves only the structural identities T1-T4 for arbitrary positive
masses and arbitrary positive NNI coefficients. It does not derive the
calibrated value `|V_us| = 0.2251`.

The calibrated Cabibbo number remains an imports-dependent output of
`scripts/frontier_ckm_mass_basis_nni.py`, because that runner still imports
quark masses, fitted NNI coefficients, and PDG comparators. The earlier
work-history mass-basis route remains route history and is not the live
one-hop source for the algebraic identities.

## Summary

The safe current Cabibbo statement on `main` is:

> within the mass-basis NNI flavor package, the framework gives
> `|V_us| = 0.2251`, compared with the PDG value `0.2243`.

That is a strong bounded flavor-companion result. It is **not** full CKM
closure, and it is **not** a retained flagship claim by itself.

## Safe Claim Boundary

### Safe to say

- the current main-branch flavor package contains a Cabibbo-scale result on the
  accepted authority surface
- the strongest current `main` value is `|V_us| = 0.2251`
- this sits inside the broader bounded CKM magnitude package

### Not safe to say

- that quantitative flavor is closed
- that the full CKM matrix is derived at retained-theorem grade
- that the older `epsilon = 1/3` fitted route is the current main authority

## Main Numerical Read

From the mass-basis NNI route:

- `|V_us| = 0.2251`
- PDG: `0.2243`
- ratio: `1.004`
- deviation: about `+0.4%`

This is the publication-facing Cabibbo number on `main`.

## Why This Is The Active Surface

The older combined Cabibbo/Jarlskog note is no longer the active authority
because it mixed:

- a fitted Cabibbo route
- a bounded Jarlskog phase check
- and a script path that is not part of the current main-branch authority chain

That combined route note is kept in work history only:

- [work_history/CABIBBO_JARLSKOG_ROUTE_NOTE_2026-04-12.md](work_history/CABIBBO_JARLSKOG_ROUTE_NOTE_2026-04-12.md)

The active source split for this work-history note is:

- structural identities:
  [CKM_MASS_BASIS_NNI_STRUCTURAL_IDENTITIES_NARROW_THEOREM_NOTE_2026-06-17.md](../../CKM_MASS_BASIS_NNI_STRUCTURAL_IDENTITIES_NARROW_THEOREM_NOTE_2026-06-17.md)
- calibrated bounded illustration:
  [frontier_ckm_mass_basis_nni.py](../../../scripts/frontier_ckm_mass_basis_nni.py)

## Relationship To Other Flavor Notes

- current CKM magnitude package:
  [CKM_MASS_BASIS_NNI_STRUCTURAL_IDENTITIES_NARROW_THEOREM_NOTE_2026-06-17.md](../../CKM_MASS_BASIS_NNI_STRUCTURAL_IDENTITIES_NARROW_THEOREM_NOTE_2026-06-17.md)
- current bounded Jarlskog companion:
  `JARLSKOG_PHASE_BOUND_NOTE.md` (sibling artifact; cross-reference only — not a one-hop dep of this note)
- historical combined route note:
  [work_history/CABIBBO_JARLSKOG_ROUTE_NOTE_2026-04-12.md](work_history/CABIBBO_JARLSKOG_ROUTE_NOTE_2026-04-12.md)

## Publication Disposition

- keep this as the current bounded Cabibbo authority on `main`
- keep Cabibbo on the bounded publication surface
- do not promote it beyond bounded flavor-companion status until the full CKM
  lane closes
