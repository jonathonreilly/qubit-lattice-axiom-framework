#!/usr/bin/env python3
"""Second run. N3 with the measurement bug fixed and a positive control; N2 at L = 7, 9.
Criteria are in theorem-z-3b7fd4e57.md, written before this run."""
import sys
from collections import deque
import numpy as np
sys.path.insert(0, sys.argv[1])
from hm_checks import n2


def n3(L=5, W=40, rS=1, teeth=True):
    t = 2 * W // L + 2 * rS
    R = t
    M = 10 * t
    tip = W // 2
    rough = np.zeros((W, M), bool)
    if teeth:
        for th in range(0, M, t - 1):
            rough[:tip, th] = True
    seen = np.zeros_like(rough)
    q = deque((0, th) for th in range(M) if rough[0, th])
    for c in q:
        seen[c] = True
    while q:
        r, th = q.popleft()
        for dr in range(-R, R + 1):
            for dth in range(-R, R + 1):
                r2, th2 = r + dr, (th + dth) % M
                if 0 <= r2 < W and rough[r2, th2] and not seen[r2, th2]:
                    seen[r2, th2] = True
                    q.append((r2, th2))
    crossed = bool(seen[W - 1].any())
    G = W - t + 1
    ok = np.zeros((G, M + 1), bool)
    for g in range(G):
        for u in range(M + 1):
            cols = [(u + i) % M for i in range(t)]
            ok[g, u] = not rough[g:g + t][:, cols].any()
    fwd = np.zeros_like(ok)
    fwd[:, 0] = ok[:, 0]
    for u in range(M):
        for g in range(G):
            if fwd[g, u]:
                for g2 in (g - 1, g, g + 1):
                    if 0 <= g2 < G and ok[g2, u + 1]:
                        fwd[g2, u + 1] = True
    bwd = np.zeros_like(ok)
    bwd[:, M] = ok[:, M]
    for u in range(M, 0, -1):
        for g in range(G):
            if bwd[g, u]:
                for g2 in (g - 1, g, g + 1):
                    if 0 <= g2 < G and ok[g2, u - 1]:
                        bwd[g2, u - 1] = True
    on_path = fwd & bwd
    gs = np.where(on_path.any(axis=1))[0]
    gmin = int(gs.min()) if gs.size else None
    room = None if gmin is None else W - L * (gmin + rS)
    family = room is not None and room >= t
    print(f"N3 teeth={teeth} L={L} W={W} t={t} R={R} tip={tip}: crosses_annulus_1={crossed}; "
          f"min_inner_radius_on_any_winding_layer={gmin}; level0_room={room} (needs {t}); family={family}")
    return crossed, family


a = n3(teeth=True)
b = n3(teeth=False)
print("N3 counterexample", "PASS" if (not a[0] and not a[1]) else "FAIL",
      "; control", "PASS" if b[1] else "FAIL")
n2(7, 4)
n2(9, 4)
