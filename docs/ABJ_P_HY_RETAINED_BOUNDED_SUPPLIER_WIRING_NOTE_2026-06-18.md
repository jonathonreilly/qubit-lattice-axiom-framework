# ABJ Left-Handed Formal Trace Arithmetic Boundary

**Date:** 2026-06-18
**Claim type:** bounded_theorem
**Status authority:** source-note proposal only; independent review and audit
own any effective-status movement.
**Stable row:** `abj_p_hy_retained_bounded_supplier_wiring_note_2026-06-18`
**Primary runner:**
`scripts/frontier_abj_phy_retained_bounded_supplier_wiring_2026_06_18.py`

## Target blocker

This row previously treated the physical `alpha=1/3` normalization as supplied
by the hypercharge normalization bridge. That use is not supported after the
bridge is narrowed to formal arithmetic. The strongest self-contained result
here is therefore the exact anomaly-trace calculation from an explicitly
supplied formal packet. This row does not supply P-HY and does not identify the
packet as physical hypercharge.

## Supplied formal packet

Take two formal entries with data

| entry | weak multiplicity | color multiplicity | `y` | color quadratic index | color cubic index |
|---|---:|---:|---:|---:|---:|
| `A` | 2 | 3 | `1/3` | `1/2` | `1` |
| `B` | 2 | 1 | `-1` | `0` | `0` |

Also supply the weak-doublet quadratic index `1/2`. Every multiplicity,
eigenvalue, representation index, sign, and normalization in this table is a
formal theorem hypothesis. The labels `Q_L`, `L_L`, and `U(1)_Y` are not
conclusions of this row.

## Theorem

For the supplied packet, exact rational arithmetic gives

```text
Tr[y]        = 2*3*(1/3) + 2*1*(-1)       = 0,
Tr[y^3]      = 2*3*(1/3)^3 + 2*1*(-1)^3   = -16/9,
Tr[C2*y]     = 2*(1/2)*(1/3)               = 1/3,
Tr[W2*y]     = 3*(1/2)*(1/3) + (1/2)*(-1) = 0,
Tr[C3]       = 2*1                          = 2.
```

The proof is direct substitution in `Q`. It does not derive why this packet
should occur in the framework or why its nonzero traces would be the anomaly
coefficients of a physical chiral gauge theory.

## Relationship to the normalization arithmetic row

`HYPERCHARGE_ALPHA_THIRD_NORMALIZATION_BRIDGE_BOUNDED_NOTE_2026-05-25.md`
independently proves the formal two-equation implication that its supplied
packet gives `(alpha,beta)=(1/3,-1)`. It does not supply the present packet's
physical meaning and is not a load-bearing dependency here. Reproducing the
numbers in two exact calculations cannot establish the missing physical
readout bridge.

Likewise, `HYPERCHARGE_IDENTIFICATION_NOTE.md` and
`LHCM_MATTER_ASSIGNMENT_FROM_SU3_REPRESENTATION_NOTE_2026-05-02.md` remain
context only for this narrowed result. Their names, source prose, and mutable
audit status are not used as mathematical evidence.

## Boundaries

This theorem does not close:

- P-HY or any physical identification of `y` with hypercharge;
- the Anti-squared-to-`L_L` readout;
- derivation of the `6+2` packet or either representation index;
- physical charge or weak-isospin assignments;
- the ABJ anomaly-to-inconsistency premise P-ABJ;
- P-COMP, P-REC, or B-AXIS;
- a right-handed completion or full Standard Model spectrum; or
- any parent theorem or audit-status promotion.

The parent ABJ row may consume this result only as conditional exact arithmetic
after separately naming all physical premises. It must not call this row a
retained physical P-HY supplier.

## Verification

The runner constructs the packet directly over `fractions.Fraction`,
recomputes all five traces, verifies a sign-reversal control for the cubic
index, and rejects both a changed `y` packet and a physical-readout inference.

Expected terminal line:

```text
TOTAL: PASS=8 FAIL=0
```

No new axiom, primitive, admission, physical readout, or audit verdict is
introduced by this narrowed row.
