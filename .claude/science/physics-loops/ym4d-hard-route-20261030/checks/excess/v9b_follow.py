#!/usr/bin/env python3
"""Follow-up to T8, T9, declared in CRITERIA.md after their FAIL: larger L only."""
import numpy as np
import v8_lift1d as v8
import v9_lift4d as v9

for L in (41, 101, 201):
    n, Nc, T0, R0 = v8.build(L, Nc=20)
    dz = np.roll(T0, -1, axis=0) - T0
    d2 = np.roll(dz, -1, axis=0) - dz
    print(f"T8 L {L}: L|grad zeta| {L*np.abs(dz).max():.3f} L^2|grad^2 zeta| {L*L*np.abs(d2).max():.3f}", flush=True)
v9.LS = (9, 13)
v9.TR = 4
v9.main()
