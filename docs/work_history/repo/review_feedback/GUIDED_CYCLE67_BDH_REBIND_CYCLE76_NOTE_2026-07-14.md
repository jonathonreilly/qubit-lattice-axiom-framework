# Guided Cycle-67 B/D/H Rebind — Cycle 76

**Date:** 2026-07-14  
**Authority:** none  
**Status:** candidate successor to Cycle 72; mixed audit pending

Companion runner:

```text
scripts/guided_cycle67_bdh_rebind_cycle76_2026_07_14.py
```

## Mechanism

Cycle 72 is exact after Cycle 67 completes, but the full mixed audit exposes a
single earlier race: `X_B` can form while `OPEN_C` is delayed, so `c` briefly
has the same bare-X signature as `D_y`. The D row can then permanently steal
`c` before `Z_C`.

This successor adds two four-record local guide layers:

```text
YS: E + L8 + L10
YG: OPEN_B + YS
D_y: X_B + YG
```

The intended D target is singleton; `c` is never adjacent to `YG`. `D_z`
retains its existing `X_B+L10` cage. The remainder of Cycle 72 is unchanged.

## Boundary

The companion runner first checks every schedule conditional on the Cycle-67
terminal. A separate mixed scan through all Cycle-60/Cycle-67 transients is
still required before this successor can replace Cycle 72. Renewal and
operational decoding remain open. No axiom conclusion follows.

