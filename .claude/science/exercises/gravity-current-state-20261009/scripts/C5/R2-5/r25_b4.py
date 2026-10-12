"""R2-5 check 0: B4+ (proper signed 4x4 permutations) contains proper elements reversing the time
axis, so whole-law B4+ covariance already maps a vertical formation pair at (x1, t) to an
un-formation pair at (-x1, -t) for orientation-free (scalar) record predicates."""
import numpy as np, itertools
tot = cnt = 0
for p in itertools.permutations(range(4)):
    for s in itertools.product((1, -1), repeat=4):
        M = np.zeros((4, 4), int)
        for i, (j, sg) in enumerate(zip(p, s)): M[j, i] = sg
        if round(np.linalg.det(M)) != 1: continue
        tot += 1
        if (M @ np.array([1, 0, 0, 0]))[0] == -1: cnt += 1
print(f"B4+ order {tot}; proper elements with g e0 = -e0: {cnt}; examples diag(-1,-1,1,1) and -1 (det +1)")
