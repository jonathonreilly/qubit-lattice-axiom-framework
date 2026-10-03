"""Enumerate all mod-2 covariant Clifford QCA candidates on a box and check the QCA (symplectic) conditions:
   omega(f, T_v f) = 0  for all v,      omega(f, T_v h) = delta_{v,0},   h = alpha(Z_0) = C3^2 f.
Prints every surviving f (mod 2). Exact F2 arithmetic.
"""
import sys, itertools
import numpy as np
from scipy.signal import correlate
from cliff_lines import affine_solutions


def to_grid(vec, pts, r):
    n = 2 * r + 1
    gx = np.zeros((n, n, n), dtype=np.int64); gz = np.zeros_like(gx)
    for i, v in enumerate(pts):
        a, b, c = (v[0] + r, v[1] + r, v[2] + r)
        gx[a, b, c] = vec[2 * i]; gz[a, b, c] = vec[2 * i + 1]
    return gx, gz


def omega_corr(ax, az, bx, bz):
    """O[v] = sum_u a_x(u) b_z(u-v) + a_z(u) b_x(u-v)  (mod 2), all offsets ('full')."""
    return (correlate(ax, bz, mode="full", method="direct") + correlate(az, bx, mode="full", method="direct")) % 2


def check(fvec, hvec, pts, r):
    fx, fz = to_grid(fvec, pts, r); hx, hz = to_grid(hvec, pts, r)
    Off = omega_corr(fx, fz, fx, fz)
    Ofh = omega_corr(fx, fz, hx, hz)
    c = 2 * r  # zero-lag index
    ok1 = not Off.any()
    target = np.zeros_like(Ofh); target[c, c, c] = 1
    ok2 = np.array_equal(Ofh, target)
    return ok1, ok2


def show(vec, pts):
    lab = {(1, 0): "X", (0, 1): "Z", (1, 1): "Y"}
    return " ".join(f"{lab[(int(vec[2*i]), int(vec[2*i+1]))]}{v}" for i, v in enumerate(pts)
                    if (vec[2 * i], vec[2 * i + 1]) != (0, 0))


if __name__ == "__main__":
    cases = [("oct", 1), ("cube", 1), ("oct", 2), ("cube", 2), ("oct", 3)]
    if len(sys.argv) > 1:
        cases = [(sys.argv[1], int(sys.argv[2]))]
    for shape, r in cases:
        pts, idx, Bs, L3, part, hom = affine_solutions(shape, r)
        L33 = (L3.astype(int) @ L3) % 2
        d = len(hom)
        sols = []
        for s in itertools.product([0, 1], repeat=d):
            coeff = part.astype(int).copy()
            for si, hv in zip(s, hom):
                if si:
                    coeff = (coeff + hv) % 2
            f = (coeff @ Bs.astype(int)) % 2
            h = (L33 @ f) % 2
            ok1, ok2 = check(f, h, pts, r)
            if ok1 and ok2:
                sols.append(f)
        print(f"{shape} r={r}: {2**d} candidates, {len(sols)} pass the QCA conditions")
        for f in sols:
            print("    alpha(X_0) =", show(f, pts))
