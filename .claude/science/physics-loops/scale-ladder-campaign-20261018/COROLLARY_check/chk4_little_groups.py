#!/usr/bin/env python3
"""COROLLARY check, part 4 (independent model): little group of each cube point under the 24 dressed proper rotations,
and the C4 axis of the D4 little groups (is it e_i for the point k* + pi e_i?)."""
import itertools, sys
import numpy as np
sys.path.insert(0, '/home/user/qubit-lattice-axiom-framework/.claude/science/physics-loops/scale-ladder-campaign-20261018/B7_check')
from chk_core import OH, PROPER, fibre_image, same_k, wrap
kst = np.array([1, -1, 1]) * np.pi / 2
ok = True
for name, k in [("k*", kst), ("-k*", -kst)] + [(f"k*+pi e{i}", kst + np.pi * np.eye(3)[i]) for i in range(3)] + [(f"-k*+pi e{i}", -kst + np.pi * np.eye(3)[i]) for i in range(3)]:
    st = [g for g in PROPER if same_k(fibre_image(g, k), k)]
    c4 = [OH[g] for g in st if round(np.trace(OH[g])) == 1]
    axes = sorted({tuple(int(abs(x)) for x in np.round(np.real(np.linalg.eig(M.astype(float))[1][:, np.argmin(abs(np.linalg.eig(M.astype(float))[0] - 1))]))) for M in c4})
    c2axis = all(any((OH[g] == np.diag(d)).all() for g in st) for d in ([1, -1, -1], [-1, 1, -1], [-1, -1, 1]))
    print(f"{name:10s} = {np.round(wrap(k)/np.pi, 2).tolist()} pi: |little group| = {len(st)}, C4 axes {axes}, contains all axis C2: {c2axis}")
    if name.startswith("k*+") or name.startswith("-k*+"):
        i = int(name[-1]); ok &= len(st) == 8 and axes == [tuple(int(j == i) for j in range(3))] and c2axis
print("[PASS]" if ok else "[FAIL]", "each point k* + pi e_i and -k* + pi e_i has little group D4 with C4 axis e_i, containing the three axis C2s")
